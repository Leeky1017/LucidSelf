"""
Authentication Models for LucidSelf Contracts

认证层模型定义。

对照文档: .kiro/docs/api_contracts.md §2.1
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# =============================================================================
# ID 格式常量
# =============================================================================

AUTH_ID_PATTERN = r"^auth_[a-z0-9]{12}$"
SESSION_ID_PATTERN = r"^sess_[a-z0-9]{16}$"
ORG_ID_PATTERN = r"^org_[a-z0-9]{12}$"


# =============================================================================
# 枚举定义
# =============================================================================


class AuthProvider(str, Enum):
    """认证提供商"""
    APPLE = "apple"
    GOOGLE = "google"
    EMAIL = "email"


# =============================================================================
# 数据模型
# =============================================================================


class AuthCredential(BaseModel):
    """
    认证凭证
    
    存储用户的认证信息，支持多种登录方式。
    """
    model_config = ConfigDict(str_strip_whitespace=True)
    
    auth_id: str = Field(
        ..., 
        pattern=AUTH_ID_PATTERN,
        description="认证ID，格式 auth_xxxxxxxxxxxx"
    )
    user_id: str = Field(
        ..., 
        max_length=64,
        description="关联的用户ID"
    )
    provider: AuthProvider = Field(
        ...,
        description="认证提供商"
    )
    provider_user_id: Optional[str] = Field(
        None, 
        max_length=256,
        description="第三方用户ID（Apple/Google）"
    )
    email: Optional[EmailStr] = Field(
        None,
        description="用户邮箱"
    )
    email_verified: bool = Field(
        default=False,
        description="邮箱是否已验证"
    )
    password_hash: Optional[str] = Field(
        None, 
        exclude=True,  # 不序列化到 JSON
        description="密码哈希（仅邮箱登录）"
    )
    created_at: datetime = Field(
        ...,
        description="创建时间"
    )
    last_login_at: Optional[datetime] = Field(
        None,
        description="最后登录时间"
    )


class TokenPair(BaseModel):
    """
    Token 对
    
    JWT Token 响应格式。
    """
    access_token: str = Field(
        ...,
        description="访问令牌"
    )
    refresh_token: str = Field(
        ...,
        description="刷新令牌"
    )
    token_type: str = Field(
        default="Bearer",
        description="Token 类型"
    )
    expires_in: int = Field(
        ...,
        description="Access Token 过期秒数",
        ge=60
    )


class JWTPayload(BaseModel):
    """
    JWT Payload
    
    Access Token 的载荷内容。
    """
    sub: str = Field(
        ...,
        description="用户ID (subject)"
    )
    exp: int = Field(
        ...,
        description="过期时间戳"
    )
    iat: int = Field(
        ...,
        description="签发时间戳"
    )
    provider: AuthProvider = Field(
        ...,
        description="认证提供商"
    )
    tier: str = Field(
        default="free",
        description="会员等级"
    )


# =============================================================================
# 请求/响应模型
# =============================================================================


class AppleSignInRequest(BaseModel):
    """Apple 登录请求"""
    identity_token: str = Field(
        ...,
        description="Apple 返回的 JWT identity_token"
    )
    authorization_code: str = Field(
        ...,
        description="Apple 返回的 authorization_code"
    )
    user_info: Optional[dict] = Field(
        None,
        description="首次登录时 Apple 返回的用户信息"
    )


class GoogleSignInRequest(BaseModel):
    """Google 登录请求"""
    id_token: str = Field(
        ...,
        description="Google OAuth 返回的 id_token"
    )
    access_token: Optional[str] = Field(
        None,
        description="Google OAuth 返回的 access_token"
    )


class EmailSignupRequest(BaseModel):
    """邮箱注册请求"""
    email: EmailStr = Field(
        ...,
        description="用户邮箱"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="密码（8-128字符）"
    )
    name: Optional[str] = Field(
        None,
        max_length=64,
        description="用户姓名"
    )


class EmailLoginRequest(BaseModel):
    """邮箱登录请求"""
    email: EmailStr = Field(
        ...,
        description="用户邮箱"
    )
    password: str = Field(
        ...,
        description="密码"
    )


class SendCodeRequest(BaseModel):
    """发送验证码请求"""
    email: EmailStr = Field(
        ...,
        description="用户邮箱"
    )


class EmailVerifyRequest(BaseModel):
    """邮箱验证请求"""
    email: EmailStr = Field(
        ...,
        description="用户邮箱"
    )
    code: str = Field(
        ...,
        min_length=6,
        max_length=6,
        description="6位验证码"
    )


class RefreshTokenRequest(BaseModel):
    """刷新 Token 请求"""
    refresh_token: str = Field(
        ...,
        description="刷新令牌"
    )


class UserInfo(BaseModel):
    """用户信息响应"""
    user_id: str = Field(
        ...,
        description="用户ID"
    )
    org_id: str = Field(
        ...,
        pattern=ORG_ID_PATTERN,
        description="组织/租户ID"
    )
    email: Optional[str] = Field(
        None,
        description="用户邮箱"
    )
    name: Optional[str] = Field(
        None,
        description="用户姓名"
    )
    provider: AuthProvider = Field(
        ...,
        description="认证提供商"
    )
    tier: str = Field(
        default="free",
        description="会员等级"
    )
    created_at: datetime = Field(
        ...,
        description="注册时间"
    )
