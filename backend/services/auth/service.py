"""
Authentication Service

认证服务核心实现 - PostgreSQL版本。

对照契约: backend/core/contracts/auth_models.py
"""

import calendar
import hashlib
import logging
import os
import secrets
from datetime import datetime, date, timedelta
from typing import Optional, Tuple

import bcrypt
from jose import JWTError, jwt
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.contracts.auth_models import (
    AuthProvider,
    JWTPayload,
    TokenPair,
    UserInfo,
)
from backend.models.auth import (
    AuthCredential,
    RefreshToken,
    EmailVerification,
    User,
    IPRateLimit,
    SexAtBirth,
)
from backend.db import async_session_maker

logger = logging.getLogger(__name__)


# =============================================================================
# 配置
# =============================================================================

# JWT 配置
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"  # 开发用 HS256，生产可改 RS256

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

# 安全检查：生产环境必须设置JWT_SECRET_KEY
if not os.getenv("JWT_SECRET_KEY") and os.getenv("ENV", "dev") == "production":
    logger.critical("SECURITY WARNING: JWT_SECRET_KEY not set in production!")
    raise RuntimeError("JWT_SECRET_KEY must be set in production environment")

# 验证码配置
VERIFICATION_CODE_LENGTH = 6
VERIFICATION_CODE_EXPIRE_MINUTES = 10
MAX_VERIFICATION_ATTEMPTS = 5  # 最大验证尝试次数

# 开发模式（跳过邮件发送，控制台打印验证码）
DEV_MODE = os.getenv("AUTH_DEV_MODE", "true").lower() == "true"

# 管理员白名单（不受限流限制）
ADMIN_WHITELIST = {
    "3118895255@qq.com",  # 1号用户 - 李晴吾
}

def is_admin_email(email: str) -> bool:
    """检查是否为管理员邮箱"""
    return email.lower().strip() in ADMIN_WHITELIST


# =============================================================================
# ID 生成
# =============================================================================

def generate_auth_id() -> str:
    """生成认证ID: auth_xxxxxxxxxxxx"""
    return f"auth_{secrets.token_hex(6)}"


def generate_token_id() -> str:
    """生成 Token ID: tok_xxxxxxxxxxxx"""
    return f"tok_{secrets.token_hex(6)}"


def generate_user_id() -> str:
    """生成用户ID: user_xxxxxxxxxxxx"""
    return f"user_{secrets.token_hex(6)}"


def derive_org_id_from_user_id(user_id: str) -> str:
    """
    派生 org_id（最小可行：默认一用户一租户）

    规则：
    - 若 user_id 符合 user_<12hex>，则 org_id = org_<同后缀>
    - 否则生成随机 org_id
    """
    if user_id and user_id.startswith("user_"):
        suffix = user_id.removeprefix("user_")
        if len(suffix) == 12 and all(c in "0123456789abcdef" for c in suffix):
            return f"org_{suffix}"
    if user_id:
        return f"org_{hashlib.sha256(user_id.encode()).hexdigest()[:12]}"
    return f"org_{secrets.token_hex(6)}"


def generate_verification_code() -> str:
    """生成6位数字验证码"""
    return "".join(str(secrets.randbelow(10)) for _ in range(VERIFICATION_CODE_LENGTH))


# =============================================================================
# 密码处理
# =============================================================================

def hash_password(password: str) -> str:
    """哈希密码（bcrypt）"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()


def verify_password(password: str, password_hash: str) -> bool:
    """验证密码"""
    try:
        return bcrypt.checkpw(password.encode(), password_hash.encode())
    except Exception:
        return False


def hash_token(token: str) -> str:
    """哈希 Token（用于存储 Refresh Token）"""
    return hashlib.sha256(token.encode()).hexdigest()


# =============================================================================
# JWT 处理
# =============================================================================

def create_access_token(
    user_id: str,
    provider: AuthProvider,
    tier: str = "free",
    expires_delta: Optional[timedelta] = None,
) -> str:
    """创建 Access Token"""
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    now = datetime.utcnow()
    expire = now + expires_delta
    
    payload = {
        "sub": user_id,
        # 使用 calendar.timegm 正确转换 UTC datetime 为 Unix 时间戳
        "exp": calendar.timegm(expire.timetuple()),
        "iat": calendar.timegm(now.timetuple()),
        "provider": provider.value,
        "tier": tier,
    }
    
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def create_refresh_token() -> Tuple[str, datetime]:
    """
    创建 Refresh Token
    
    返回: (token, expires_at)
    """
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    return token, expires_at


def create_token_pair(
    user_id: str,
    provider: AuthProvider,
    tier: str = "free",
) -> Tuple[TokenPair, str, datetime]:
    """
    创建 Token 对
    
    返回: (TokenPair, refresh_token_raw, refresh_expires_at)
    """
    access_token = create_access_token(user_id, provider, tier)
    refresh_token, refresh_expires_at = create_refresh_token()
    
    token_pair = TokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
    
    return token_pair, refresh_token, refresh_expires_at


def decode_access_token(token: str) -> Optional[JWTPayload]:
    """
    解码 Access Token
    
    返回 None 表示 Token 无效或过期
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return JWTPayload(
            sub=payload["sub"],
            exp=payload["exp"],
            iat=payload["iat"],
            provider=AuthProvider(payload["provider"]),
            tier=payload.get("tier", "free"),
        )
    except JWTError as e:
        logger.debug(f"JWT decode error: {e}")
        return None


def is_token_expired(payload: JWTPayload) -> bool:
    """检查 Token 是否过期"""
    return datetime.utcnow().timestamp() > payload.exp


# =============================================================================
# IP 限流配置
# =============================================================================

# 注册/验证码限流：每IP每分钟最大次数
IP_RATE_LIMIT_PER_MINUTE = 1
# 注册/验证码限流：每IP每天最大次数
IP_RATE_LIMIT_PER_DAY = 3

# 登录限流（较宽松，允许输错密码）
LOGIN_RATE_LIMIT_PER_MINUTE = 5
LOGIN_RATE_LIMIT_PER_DAY = 50

# 密码最小长度
MIN_PASSWORD_LENGTH = 8


# =============================================================================
# 认证服务类 - PostgreSQL版本
# =============================================================================

class AuthService:
    """
    认证服务 - PostgreSQL持久化版本
    
    提供用户认证相关的业务逻辑，数据持久化到PostgreSQL。
    """
    
    def __init__(self):
        pass  # 不再使用内存存储
    
    # =========================================================================
    # IP 限流检查
    # =========================================================================
    
    async def check_ip_rate_limit(
        self, 
        ip_address: str, 
        action_type: str,
        db: AsyncSession,
        per_minute_limit: int = IP_RATE_LIMIT_PER_MINUTE,
        per_day_limit: int = IP_RATE_LIMIT_PER_DAY,
    ) -> None:
        """
        检查IP限流
        
        Args:
            ip_address: 客户端IP
            action_type: 动作类型 (signup/send_code/login)
            db: 数据库会话
            per_minute_limit: 每分钟最大次数
            per_day_limit: 每天最大次数
        
        Raises:
            ValueError: 超过限流
        """
        # 使用UTC日期避免时区问题
        now = datetime.utcnow()
        today = now.date()
        
        # 查询今天的记录（使用 FOR UPDATE 防止竞态条件）
        stmt = select(IPRateLimit).where(
            and_(
                IPRateLimit.ip_address == ip_address,
                IPRateLimit.action_type == action_type,
                IPRateLimit.action_date == today
            )
        ).with_for_update()
        result = await db.execute(stmt)
        rate_limit = result.scalar_one_or_none()
        
        if rate_limit:
            # 检查每日限制
            if rate_limit.daily_count >= per_day_limit:
                raise ValueError(f"今日操作次数已达上限（{per_day_limit}次），请明日再试")
            
            # 检查每分钟限制
            if rate_limit.last_action_at:
                time_diff = (now - rate_limit.last_action_at).total_seconds()
                interval = 60 / per_minute_limit  # 动态计算间隔
                if time_diff < interval:
                    wait_seconds = int(interval - time_diff)
                    raise ValueError(f"操作过于频繁，请等待{wait_seconds}秒后再试")
            
            # 更新记录
            rate_limit.daily_count += 1
            rate_limit.last_action_at = now
        else:
            # 创建新记录
            rate_limit = IPRateLimit(
                ip_address=ip_address,
                action_type=action_type,
                action_date=today,
                daily_count=1,
                last_action_at=now
            )
            db.add(rate_limit)
        
        await db.flush()
    
    # =========================================================================
    # 邮箱注册/登录
    # =========================================================================
    
    async def email_signup(
        self,
        email: str,
        password: str,
        name: Optional[str] = None,
        ip_address: Optional[str] = None,
    ) -> TokenPair:
        """
        邮箱注册 - PostgreSQL版本
        
        开发模式下自动验证邮箱。
        """
        email = email.lower().strip()
        
        # 密码强度验证
        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValueError(f"密码长度不能少于{MIN_PASSWORD_LENGTH}位")
        
        async with async_session_maker() as db:
            # IP限流检查（管理员跳过）
            if ip_address and not is_admin_email(email):
                await self.check_ip_rate_limit(ip_address, "signup", db)
            
            # 检查邮箱是否已存在
            stmt = select(User).where(User.email == email)
            result = await db.execute(stmt)
            existing_user = result.scalar_one_or_none()
            
            if existing_user:
                raise ValueError("邮箱已被注册")
            
            # 创建用户
            user_id = generate_user_id()
            auth_id = generate_auth_id()
            now = datetime.utcnow()
            
            # 创建User记录
            user = User(
                user_id=user_id,
                org_id=derive_org_id_from_user_id(user_id),
                email=email,
                name=name or email.split("@")[0],
                provider=AuthProvider.EMAIL,
                tier="free",
            )
            db.add(user)
            
            # 创建AuthCredential记录（created_at/updated_at由Base自动设置）
            credential = AuthCredential(
                auth_id=auth_id,
                user_id=user_id,
                provider=AuthProvider.EMAIL,
                email=email,
                email_verified=DEV_MODE,
                password_hash=hash_password(password),
                last_login_at=now,
            )
            db.add(credential)
            
            # 生成 Token
            token_pair, refresh_token_raw, refresh_expires_at = create_token_pair(
                user_id, AuthProvider.EMAIL, "free"
            )
            
            # 创建RefreshToken记录（created_at/updated_at由Base自动设置）
            refresh_token_record = RefreshToken(
                token_id=generate_token_id(),
                user_id=user_id,
                token_hash=hash_token(refresh_token_raw),
                expires_at=refresh_expires_at,
                revoked=False,
            )
            db.add(refresh_token_record)
            
            await db.commit()
            
            # PII minimization: do not log raw email or secrets.
            logger.info("New user registered: %s", user_id)
            return token_pair
    
    async def email_login(
        self,
        email: str,
        password: str,
        ip_address: Optional[str] = None,
    ) -> TokenPair:
        """邮箱登录 - PostgreSQL版本"""
        email = email.lower().strip()
        
        async with async_session_maker() as db:
            # IP限流检查（管理员跳过）
            if ip_address and not is_admin_email(email):
                await self.check_ip_rate_limit(
                    ip_address, 
                    "login", 
                    db,
                    per_minute_limit=LOGIN_RATE_LIMIT_PER_MINUTE,
                    per_day_limit=LOGIN_RATE_LIMIT_PER_DAY,
                )
            
            # 查找认证信息
            stmt = select(AuthCredential).where(AuthCredential.email == email)
            result = await db.execute(stmt)
            credential = result.scalar_one_or_none()
            
            if not credential:
                raise ValueError("邮箱或密码错误")
            
            # 验证密码
            if not verify_password(password, credential.password_hash):
                raise ValueError("邮箱或密码错误")
            
            # 检查邮箱验证
            if not credential.email_verified and not DEV_MODE:
                raise ValueError("请先验证邮箱")
            
            # 查找用户
            stmt = select(User).where(User.user_id == credential.user_id)
            result = await db.execute(stmt)
            user = result.scalar_one_or_none()
            
            if not user:
                raise ValueError("用户不存在")
            
            # 更新最后登录时间
            credential.last_login_at = datetime.utcnow()
            
            # 生成 Token
            token_pair, refresh_token_raw, refresh_expires_at = create_token_pair(
                user.user_id, AuthProvider.EMAIL, user.tier
            )
            
            # 创建RefreshToken记录（created_at/updated_at由Base自动设置）
            refresh_token_record = RefreshToken(
                token_id=generate_token_id(),
                user_id=user.user_id,
                token_hash=hash_token(refresh_token_raw),
                expires_at=refresh_expires_at,
                revoked=False,
            )
            db.add(refresh_token_record)
            
            await db.commit()
            
            logger.info(f"User logged in: {user.user_id}")
            return token_pair
    
    # =========================================================================
    # 邮箱验证
    # =========================================================================
    
    async def send_verification_code(
        self, 
        email: str,
        ip_address: Optional[str] = None,
    ) -> str:
        """
        发送验证码 - PostgreSQL版本
        
        开发模式下返回验证码（不实际发送邮件）
        """
        email = email.lower().strip()
        
        async with async_session_maker() as db:
            # IP限流检查（管理员跳过）
            if ip_address and not is_admin_email(email):
                await self.check_ip_rate_limit(ip_address, "send_code", db)
            
            code = generate_verification_code()
            expires_at = datetime.utcnow() + timedelta(minutes=VERIFICATION_CODE_EXPIRE_MINUTES)
            
            # 删除旧的验证码
            stmt = select(EmailVerification).where(
                and_(
                    EmailVerification.email == email,
                    EmailVerification.used == False
                )
            )
            result = await db.execute(stmt)
            old_codes = result.scalars().all()
            for old_code in old_codes:
                old_code.used = True
            
            # 创建新验证码（created_at/updated_at由Base自动设置）
            verification = EmailVerification(
                id=f"ev_{secrets.token_hex(6)}",
                email=email,
                code=code,
                purpose="signup",
                expires_at=expires_at,
                used=False,
            )
            db.add(verification)
            
            await db.commit()
            
            if DEV_MODE:
                # PII/secret minimization: return code to caller, but do not log it.
                logger.info("[DEV MODE] Verification code generated")
                return code
            else:
                # TODO: 实际发送邮件
                logger.info("Verification code sent")
                return ""
    
    async def verify_email(self, email: str, code: str) -> bool:
        """验证邮箱 - PostgreSQL版本"""
        email = email.lower().strip()
        
        async with async_session_maker() as db:
            # 查找该邮箱的未使用验证码（使用FOR UPDATE锁定）
            stmt = select(EmailVerification).where(
                and_(
                    EmailVerification.email == email,
                    EmailVerification.used == False
                )
            ).with_for_update()
            result = await db.execute(stmt)
            verification = result.scalar_one_or_none()
            
            if not verification:
                raise ValueError("验证码不存在或已使用")
            
            # 检查尝试次数
            if verification.attempts >= MAX_VERIFICATION_ATTEMPTS:
                verification.used = True  # 标记为已使用，防止继续尝试
                await db.commit()
                raise ValueError("验证码尝试次数过多，请重新获取")
            
            # 检查过期
            if datetime.utcnow() > verification.expires_at:
                raise ValueError("验证码已过期")
            
            # 检查验证码是否匹配
            if verification.code != code:
                verification.attempts += 1
                await db.commit()
                remaining = MAX_VERIFICATION_ATTEMPTS - verification.attempts
                raise ValueError(f"验证码错误，剩余{remaining}次尝试机会")
            
            # 验证成功，标记为已使用
            verification.used = True
            
            # 更新认证信息的邮箱验证状态
            stmt = select(AuthCredential).where(AuthCredential.email == email)
            result = await db.execute(stmt)
            credential = result.scalar_one_or_none()
            
            if credential:
                credential.email_verified = True
            
            await db.commit()
            return True
    
    # =========================================================================
    # Token 管理
    # =========================================================================
    
    async def refresh_access_token(self, refresh_token: str) -> TokenPair:
        """刷新 Access Token - PostgreSQL版本"""
        token_hash_value = hash_token(refresh_token)
        
        async with async_session_maker() as db:
            # 查找Token记录
            stmt = select(RefreshToken).where(RefreshToken.token_hash == token_hash_value)
            result = await db.execute(stmt)
            token_record = result.scalar_one_or_none()
            
            if not token_record:
                raise ValueError("无效的 Refresh Token")
            
            if token_record.revoked:
                raise ValueError("Token 已被撤销")
            
            if datetime.utcnow() > token_record.expires_at:
                raise ValueError("Refresh Token 已过期")
            
            # 查找用户
            stmt = select(User).where(User.user_id == token_record.user_id)
            result = await db.execute(stmt)
            user = result.scalar_one_or_none()
            
            if not user:
                raise ValueError("用户不存在")
            
            # 撤销旧 Token
            token_record.revoked = True
            
            # 生成新 Token
            new_token_pair, new_refresh_token_raw, new_expires_at = create_token_pair(
                user.user_id, user.provider, user.tier
            )
            
            # 创建新RefreshToken记录（created_at/updated_at由Base自动设置）
            new_token_record = RefreshToken(
                token_id=generate_token_id(),
                user_id=user.user_id,
                token_hash=hash_token(new_refresh_token_raw),
                expires_at=new_expires_at,
                revoked=False,
            )
            db.add(new_token_record)
            
            await db.commit()
            return new_token_pair
    
    async def logout(self, refresh_token: str) -> bool:
        """登出（撤销 Token）- PostgreSQL版本"""
        token_hash_value = hash_token(refresh_token)
        
        async with async_session_maker() as db:
            stmt = select(RefreshToken).where(RefreshToken.token_hash == token_hash_value)
            result = await db.execute(stmt)
            token_record = result.scalar_one_or_none()
            
            if token_record:
                token_record.revoked = True
                await db.commit()
            
            return True
    
    # =========================================================================
    # 用户信息
    # =========================================================================
    
    async def get_user_info(self, user_id: str) -> Optional[UserInfo]:
        """获取用户信息 - PostgreSQL版本"""
        async with async_session_maker() as db:
            stmt = select(User).where(User.user_id == user_id)
            result = await db.execute(stmt)
            user = result.scalar_one_or_none()
            
            if not user:
                return None
            
            return UserInfo(
                user_id=user.user_id,
                org_id=user.org_id or derive_org_id_from_user_id(user.user_id),
                email=user.email,
                name=user.name,
                provider=user.provider,
                tier=user.tier,
                created_at=user.created_at,
            )
    
    async def get_current_user(self, token: str) -> Optional[UserInfo]:
        """从 Token 获取当前用户"""
        payload = decode_access_token(token)
        if not payload:
            return None
        
        if is_token_expired(payload):
            return None
        
        return await self.get_user_info(payload.sub)


# 全局服务实例
_auth_service: Optional[AuthService] = None


def get_auth_service() -> AuthService:
    """获取认证服务实例"""
    global _auth_service
    if _auth_service is None:
        _auth_service = AuthService()
    return _auth_service
