"""
Authentication Database Models

认证相关的 SQLAlchemy 模型。

对照契约: backend/core/contracts/auth_models.py
"""

import uuid
from datetime import datetime, date
from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Enum, String, Text, Integer, Date, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.db.base import Base
from backend.core.contracts.auth_models import AuthProvider


class SexAtBirth(str, PyEnum):
    """出生性别"""
    MALE = "male"
    FEMALE = "female"


class AuthCredential(Base):
    """
    认证凭证表
    
    存储用户的认证信息，支持多种登录方式。
    一个用户可以有多个认证方式（Apple + Email 等）。
    
    注意：继承Base的created_at/updated_at字段
    """
    __tablename__ = "auth_credentials"

    # 主键
    auth_id: Mapped[str] = mapped_column(
        String(64), 
        primary_key=True,
        comment="认证ID，格式 auth_xxxxxxxxxxxx"
    )
    
    # 关联用户
    user_id: Mapped[str] = mapped_column(
        String(64), 
        nullable=False, 
        index=True,
        comment="关联的用户ID"
    )
    
    # 认证提供商
    provider: Mapped[AuthProvider] = mapped_column(
        Enum(AuthProvider),
        nullable=False,
        comment="认证提供商: apple/google/email"
    )
    
    # 第三方用户ID（Apple/Google）
    provider_user_id: Mapped[Optional[str]] = mapped_column(
        String(256),
        nullable=True,
        comment="第三方平台的用户ID"
    )
    
    # 邮箱
    email: Mapped[Optional[str]] = mapped_column(
        String(256),
        nullable=True,
        unique=True,
        index=True,
        comment="用户邮箱"
    )
    
    # 邮箱验证状态
    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        comment="邮箱是否已验证"
    )
    
    # 密码哈希（仅邮箱登录）
    password_hash: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="密码哈希（bcrypt）"
    )
    
    # 最后登录时间（业务字段，非Base的通用字段）
    last_login_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="最后登录时间"
    )

    def __repr__(self) -> str:
        return f"<AuthCredential {self.auth_id} provider={self.provider}>"


class RefreshToken(Base):
    """
    刷新令牌表
    
    存储 Refresh Token，支持 Token 轮换和撤销。
    
    注意：继承Base的created_at/updated_at字段
    """
    __tablename__ = "refresh_tokens"

    # 主键
    token_id: Mapped[str] = mapped_column(
        String(64),
        primary_key=True,
        comment="Token ID"
    )
    
    # 关联用户
    user_id: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
        comment="用户ID"
    )
    
    # Token 哈希（不存储明文）
    token_hash: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        unique=True,
        comment="Token 哈希值"
    )
    
    # 过期时间
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        comment="过期时间"
    )
    
    # 是否已撤销
    revoked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        comment="是否已撤销"
    )
    
    # 设备信息（可选）
    device_info: Mapped[Optional[str]] = mapped_column(
        String(512),
        nullable=True,
        comment="设备信息"
    )

    def __repr__(self) -> str:
        return f"<RefreshToken {self.token_id} user={self.user_id}>"


class EmailVerification(Base):
    """
    邮箱验证码表
    
    存储邮箱验证码，支持注册和密码重置。
    
    注意：继承Base的created_at/updated_at字段
    """
    __tablename__ = "email_verifications"

    # 主键
    id: Mapped[str] = mapped_column(
        String(64),
        primary_key=True,
        comment="记录ID"
    )
    
    # 邮箱
    email: Mapped[str] = mapped_column(
        String(256),
        nullable=False,
        index=True,
        comment="邮箱"
    )
    
    # 验证码
    code: Mapped[str] = mapped_column(
        String(6),
        nullable=False,
        comment="6位验证码"
    )
    
    # 用途
    purpose: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="signup",
        comment="用途: signup/reset_password"
    )
    
    # 过期时间
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        comment="过期时间"
    )
    
    # 是否已使用
    used: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        comment="是否已使用"
    )
    
    # 尝试次数（防暴力破解）
    attempts: Mapped[int] = mapped_column(
        Integer,
        default=0,
        comment="验证尝试次数"
    )

    def __repr__(self) -> str:
        return f"<EmailVerification {self.email} purpose={self.purpose}>"


class User(Base):
    """
    用户表
    
    存储用户基本信息。
    """
    __tablename__ = "users"

    # 主键
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    
    # 用户ID（外部标识）
    user_id: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
        comment="用户ID，格式 user_xxxxxxxxxxxx"
    )

    # 组织/租户ID（多租户隔离边界）
    org_id: Mapped[Optional[str]] = mapped_column(
        String(64),
        nullable=True,
        index=True,
        comment="组织/租户ID，格式 org_xxxxxxxxxxxx（缺省时可由 user_id 派生）",
    )
    
    # 邮箱
    email: Mapped[Optional[str]] = mapped_column(
        String(256),
        nullable=True,
        unique=True,
        index=True,
        comment="用户邮箱"
    )
    
    # 姓名
    name: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=True,
        comment="用户姓名"
    )
    
    # 出生性别（命理计算必需）
    sex_at_birth: Mapped[Optional[str]] = mapped_column(
        Enum(SexAtBirth),
        nullable=True,
        comment="出生性别: male/female"
    )
    
    # 认证提供商
    provider: Mapped[str] = mapped_column(
        Enum(AuthProvider),
        nullable=False,
        default=AuthProvider.EMAIL,
        comment="认证提供商"
    )
    
    # 会员等级
    tier: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="free",
        comment="会员等级: free/pro/premium"
    )

    def __repr__(self) -> str:
        return f"<User {self.user_id} email={self.email}>"


class IPRateLimit(Base):
    """
    IP限流表
    
    防恶意注册：记录每个IP的注册/验证码发送次数。
    规则：每IP每分钟1次，每天最多3次。
    """
    __tablename__ = "ip_rate_limits"

    # 主键
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    
    # IP地址
    ip_address: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
        comment="客户端IP地址"
    )
    
    # 动作类型
    action_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        comment="动作类型: signup/send_code/login"
    )
    
    # 日期
    action_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="动作日期"
    )
    
    # 当日总次数
    daily_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        comment="当日总次数"
    )
    
    # 最后一次动作时间
    last_action_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="最后一次动作时间"
    )
    
    # 唯一约束：每个IP每种动作每天一条记录
    __table_args__ = (
        UniqueConstraint("ip_address", "action_type", "action_date", name="uq_ip_action_date"),
    )

    def __repr__(self) -> str:
        return f"<IPRateLimit {self.ip_address} {self.action_type} count={self.daily_count}>"
