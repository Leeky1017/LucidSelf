"""
Authentication API Routes

认证相关 API 端点。

对照契约: backend/core/contracts/auth_models.py
对照文档: .kiro/docs/api_contracts.md §3.1
"""

import asyncio
import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Header, Request, status

from backend.core.contracts.auth_models import (
    EmailLoginRequest,
    EmailSignupRequest,
    EmailVerifyRequest,
    RefreshTokenRequest,
    SendCodeRequest,
    TokenPair,
    UserInfo,
)
from backend.services.auth import AuthService, get_auth_service, decode_access_token
from backend.core.observability.logging import log_event
from backend.core.audit import create_audit_event, write_audit_event_async

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


# =============================================================================
# 依赖注入
# =============================================================================

async def get_current_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserInfo:
    """
    获取当前用户依赖
    
    用法:
    ```python
    @router.get("/protected")
    async def protected_route(user: UserInfo = Depends(get_current_user)):
        ...
    ```
    """
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": "AUTH_MISSING_TOKEN", "message": "缺少认证信息"},
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 解析 Bearer Token
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": "AUTH_INVALID_TOKEN", "message": "无效的认证格式"},
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = parts[1]
    user = await auth_service.get_current_user(token)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": "AUTH_INVALID_TOKEN", "message": "Token 无效或已过期"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 绑定到 request.state，供中间件/日志关联
    request.state.user_id = user.user_id
    request.state.org_id = getattr(user, "org_id", None)

    return user


async def get_optional_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    auth_service: AuthService = Depends(get_auth_service),
) -> Optional[UserInfo]:
    """获取可选的当前用户（不强制认证）"""
    if not authorization:
        return None
    
    try:
        return await get_current_user(
            request=request,
            authorization=authorization,
            auth_service=auth_service,
        )
    except HTTPException:
        return None


# =============================================================================
# 邮箱认证
# =============================================================================

def get_client_ip(request: Request) -> str:
    """获取客户端IP地址"""
    # 优先从 X-Forwarded-For 头获取（代理场景）
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    # 其次从 X-Real-IP 获取
    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip
    # 最后从连接获取
    return request.client.host if request.client else "unknown"


def mask_ip(ip: str) -> str:
    if not ip:
        return ip
    if "." in ip:
        parts = ip.split(".")
        if len(parts) == 4:
            return ".".join(parts[:3] + ["0"])
        return ip
    if ":" in ip:
        parts = ip.split(":")
        return ":".join(parts[:4]) + "::"
    return ip


@router.post(
    "/email/signup",
    response_model=TokenPair,
    status_code=status.HTTP_201_CREATED,
    summary="邮箱注册",
    description="使用邮箱和密码注册新用户",
)
async def email_signup(
    request: EmailSignupRequest,
    http_request: Request,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenPair:
    """
    邮箱注册
    
    - **email**: 用户邮箱
    - **password**: 密码（至少8位）
    - **name**: 用户姓名（可选）
    
    限流规则：每IP每分钟1次，每天最多3次。
    开发模式下自动验证邮箱，生产环境需要邮箱验证。
    """
    client_ip = get_client_ip(http_request)
    try:
        token_pair = await auth_service.email_signup(
            email=request.email,
            password=request.password,
            name=request.name,
            ip_address=client_ip,
        )
        payload = decode_access_token(token_pair.access_token)
        http_request.state.user_id = payload.sub if payload else None
        log_event(
            logger,
            logging.INFO,
            "auth_signup",
            provider="email",
            client_ip=mask_ip(client_ip),
        )
        
        # Phase 11 Task 11.3: 触发新用户 Playbook（异步，不阻塞注册）
        try:
            from backend.scheduler.jobs.playbook_trigger import trigger_new_user_playbook
            # 从 token 中提取 user_id
            user_id = payload.sub if payload else None
            if user_id:
                asyncio.create_task(trigger_new_user_playbook(user_id))
                logger.debug(f"Triggered new user playbook for: {user_id}")
        except Exception as e:
            logger.warning(f"Failed to trigger new user playbook: {e}")
            # 不阻塞注册流程
        
        return token_pair
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "AUTH_SIGNUP_FAILED", "message": str(e)},
        )


@router.post(
    "/email/login",
    response_model=TokenPair,
    summary="邮箱登录",
    description="使用邮箱和密码登录",
)
async def email_login(
    request: EmailLoginRequest,
    http_request: Request,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenPair:
    """
    邮箱登录
    
    - **email**: 用户邮箱
    - **password**: 密码
    
    限流规则：每IP每分钟5次，防止暴力破解。
    """
    client_ip = get_client_ip(http_request)
    try:
        token_pair = await auth_service.email_login(
            email=request.email,
            password=request.password,
            ip_address=client_ip,
        )
        payload = decode_access_token(token_pair.access_token)
        http_request.state.user_id = payload.sub if payload else None
        log_event(
            logger,
            logging.INFO,
            "auth_login",
            provider="email",
            client_ip=mask_ip(client_ip),
        )
        return token_pair
    except ValueError as e:
        # 记录失败尝试
        log_event(
            logger,
            logging.WARNING,
            "auth_login_failed",
            provider="email",
            client_ip=mask_ip(client_ip),
            reason=str(e),
        )
        try:
            await write_audit_event_async(
                create_audit_event(
                    event_type="ACCESS_CONTROL",
                    result="DENY",
                    capability="security-privacy-compliance",
                    rejection_reason_code="UNAUTHORIZED",
                    summary="email login failed",
                )
            )
        except Exception:
            # Do not block auth flow on audit failures (Gate-0 verification covers this separately).
            pass
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": "AUTH_LOGIN_FAILED", "message": str(e)},
        )


@router.post(
    "/email/send-code",
    summary="发送验证码",
    description="发送邮箱验证码",
)
async def send_verification_code(
    request: SendCodeRequest,
    http_request: Request,
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    """
    发送验证码
    
    - **email**: 用户邮箱（通过POST body传递，避免在URL中泄露）
    
    限流规则：每IP每分钟1次，每天最多3次。
    开发模式下返回验证码（便于测试）
    """
    client_ip = get_client_ip(http_request)
    try:
        code = await auth_service.send_verification_code(request.email, ip_address=client_ip)
        
        response = {"success": True, "message": "验证码已发送"}
        
        # 开发模式返回验证码
        from backend.services.auth import DEV_MODE
        if DEV_MODE and code:
            response["dev_code"] = code
        
        return response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"code": "RATE_LIMIT_EXCEEDED", "message": str(e)},
        )


@router.post(
    "/email/verify",
    summary="验证邮箱",
    description="使用验证码验证邮箱",
)
async def verify_email(
    request: EmailVerifyRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    """
    验证邮箱
    
    - **email**: 用户邮箱
    - **code**: 6位验证码
    """
    try:
        await auth_service.verify_email(request.email, request.code)
        return {"success": True, "message": "邮箱验证成功"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "AUTH_VERIFY_FAILED", "message": str(e)},
        )


# =============================================================================
# Token 管理
# =============================================================================

@router.post(
    "/refresh",
    response_model=TokenPair,
    summary="刷新 Token",
    description="使用 Refresh Token 获取新的 Access Token",
)
async def refresh_token(
    request: RefreshTokenRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenPair:
    """
    刷新 Token
    
    - **refresh_token**: 刷新令牌
    
    旧的 Refresh Token 会被撤销，返回新的 Token 对。
    """
    try:
        token_pair = await auth_service.refresh_access_token(request.refresh_token)
        return token_pair
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"code": "AUTH_REFRESH_FAILED", "message": str(e)},
        )


@router.post(
    "/logout",
    summary="登出",
    description="撤销 Token，登出当前会话",
)
async def logout(
    request: RefreshTokenRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    """
    登出
    
    - **refresh_token**: 要撤销的刷新令牌
    """
    await auth_service.logout(request.refresh_token)
    return {"success": True, "message": "已登出"}


# =============================================================================
# 用户信息
# =============================================================================

@router.get(
    "/me",
    response_model=UserInfo,
    summary="获取当前用户",
    description="获取当前登录用户的信息",
)
async def get_me(
    user: UserInfo = Depends(get_current_user),
) -> UserInfo:
    """
    获取当前用户信息
    
    需要 Bearer Token 认证
    """
    return user


# =============================================================================
# Apple / Google 登录（预留）
# =============================================================================

@router.post(
    "/apple",
    response_model=TokenPair,
    summary="Apple 登录",
    description="使用 Apple ID 登录",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def apple_sign_in() -> TokenPair:
    """Apple 登录（待实现）"""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail={"code": "NOT_IMPLEMENTED", "message": "Apple 登录功能开发中"},
    )


@router.post(
    "/google",
    response_model=TokenPair,
    summary="Google 登录",
    description="使用 Google 账号登录",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def google_sign_in() -> TokenPair:
    """Google 登录（待实现）"""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail={"code": "NOT_IMPLEMENTED", "message": "Google 登录功能开发中"},
    )
