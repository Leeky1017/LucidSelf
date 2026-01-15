"""
Subscription Database Models

订阅/会员相关的 SQLAlchemy 模型。

对照契约: backend/core/contracts/subscription_models.py
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Enum, Index, String, Text
from sqlalchemy.orm import relationship

from backend.db.base import Base
from backend.core.contracts.subscription_models import (
    MembershipTier,
    SubscriptionProvider,
    SubscriptionStatus,
)


class Subscription(Base):
    """
    订阅记录表
    
    存储用户的订阅信息。
    """
    __tablename__ = "subscriptions"

    # 主键
    subscription_id = Column(
        String(64), 
        primary_key=True,
        comment="订阅ID，格式 sub_xxxxxxxxxxxx"
    )
    
    # 关联用户
    user_id = Column(
        String(64), 
        nullable=False, 
        unique=True,
        index=True,
        comment="用户ID（一个用户只能有一个有效订阅）"
    )
    
    # 会员等级
    tier = Column(
        Enum(MembershipTier),
        nullable=False,
        default=MembershipTier.FREE,
        comment="会员等级: free/plus"
    )
    
    # 订阅提供商
    provider = Column(
        Enum(SubscriptionProvider),
        nullable=True,
        comment="订阅提供商: apple/google/stripe"
    )
    
    # 外部订阅ID
    provider_subscription_id = Column(
        String(256),
        nullable=True,
        comment="外部订阅ID（App Store/Google Play）"
    )
    
    # 订阅状态
    status = Column(
        Enum(SubscriptionStatus),
        nullable=False,
        default=SubscriptionStatus.ACTIVE,
        comment="订阅状态"
    )
    
    # 时间戳
    started_at = Column(
        DateTime,
        nullable=True,
        comment="订阅开始时间"
    )
    
    expires_at = Column(
        DateTime,
        nullable=True,
        comment="订阅到期时间"
    )
    
    cancelled_at = Column(
        DateTime,
        nullable=True,
        comment="取消时间"
    )
    
    # 自动续订
    auto_renew = Column(
        Boolean,
        default=True,
        comment="是否自动续订"
    )
    
    # 创建/更新时间
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="创建时间"
    )
    
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
        comment="更新时间"
    )

    # 复合索引 - 优化付费用户查询
    __table_args__ = (
        Index('ix_sub_status_tier_expires', 'status', 'tier', 'expires_at'),
    )

    def __repr__(self) -> str:
        return f"<Subscription {self.subscription_id} tier={self.tier}>"

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "subscription_id": self.subscription_id,
            "user_id": self.user_id,
            "tier": self.tier.value if self.tier else None,
            "provider": self.provider.value if self.provider else None,
            "provider_subscription_id": self.provider_subscription_id,
            "status": self.status.value if self.status else None,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "cancelled_at": self.cancelled_at.isoformat() if self.cancelled_at else None,
            "auto_renew": self.auto_renew,
        }
