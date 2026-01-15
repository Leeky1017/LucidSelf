"""
Subscription Models for LucidSelf Contracts

会员订阅模型定义。

对照文档: .kiro/docs/api_contracts.md §2.2
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# =============================================================================
# ID 格式常量
# =============================================================================

SUBSCRIPTION_ID_PATTERN = r"^sub_[a-z0-9]{12}$"


# =============================================================================
# 枚举定义
# =============================================================================


class MembershipTier(str, Enum):
    """会员等级"""
    FREE = "free"
    PLUS = "plus"


class SubscriptionProvider(str, Enum):
    """订阅提供商"""
    APPLE = "apple"      # App Store
    GOOGLE = "google"    # Google Play
    STRIPE = "stripe"    # Web 端


class SubscriptionStatus(str, Enum):
    """订阅状态"""
    ACTIVE = "active"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    GRACE_PERIOD = "grace_period"


# =============================================================================
# 数据模型
# =============================================================================


class Subscription(BaseModel):
    """
    订阅记录
    
    存储用户的订阅信息。
    """
    model_config = ConfigDict(str_strip_whitespace=True)
    
    subscription_id: str = Field(
        ..., 
        pattern=SUBSCRIPTION_ID_PATTERN,
        description="订阅ID，格式 sub_xxxxxxxxxxxx"
    )
    user_id: str = Field(
        ..., 
        max_length=64,
        description="用户ID"
    )
    tier: MembershipTier = Field(
        ...,
        description="会员等级"
    )
    provider: SubscriptionProvider = Field(
        ...,
        description="订阅提供商"
    )
    provider_subscription_id: str = Field(
        ...,
        description="外部订阅ID（App Store/Google Play/Stripe）"
    )
    status: SubscriptionStatus = Field(
        ...,
        description="订阅状态"
    )
    started_at: datetime = Field(
        ...,
        description="订阅开始时间"
    )
    expires_at: Optional[datetime] = Field(
        None,
        description="订阅到期时间"
    )
    cancelled_at: Optional[datetime] = Field(
        None,
        description="取消时间"
    )
    auto_renew: bool = Field(
        default=True,
        description="是否自动续订"
    )


class TierLimits(BaseModel):
    """
    等级限制配置
    
    定义每个会员等级的功能限制。
    """
    tier: MembershipTier = Field(
        ...,
        description="会员等级"
    )
    daily_dreams: int = Field(
        ...,
        description="每日梦境解读次数，-1 表示无限"
    )
    daily_readings: int = Field(
        ...,
        description="每日 Playbook 生成次数，-1 表示无限"
    )
    history_retention_days: int = Field(
        ...,
        description="历史记录保留天数，-1 表示永久"
    )
    advanced_engines: bool = Field(
        ...,
        description="是否可使用高级引擎"
    )
    export_enabled: bool = Field(
        ...,
        description="是否可导出数据"
    )
    batch_enabled: bool = Field(
        ...,
        description="是否可批量操作"
    )


# =============================================================================
# 等级限制常量
# =============================================================================

TIER_LIMITS = {
    MembershipTier.FREE: TierLimits(
        tier=MembershipTier.FREE,
        daily_dreams=3,
        daily_readings=5,
        history_retention_days=30,
        advanced_engines=False,
        export_enabled=False,
        batch_enabled=False,
    ),
    MembershipTier.PLUS: TierLimits(
        tier=MembershipTier.PLUS,
        daily_dreams=-1,  # 无限制
        daily_readings=-1,
        history_retention_days=-1,  # 永久
        advanced_engines=True,
        export_enabled=True,
        batch_enabled=True,
    ),
}


# =============================================================================
# 请求/响应模型
# =============================================================================


class SubscriptionStatusResponse(BaseModel):
    """订阅状态响应"""
    tier: MembershipTier = Field(
        ...,
        description="会员等级"
    )
    status: SubscriptionStatus = Field(
        ...,
        description="订阅状态"
    )
    provider: Optional[SubscriptionProvider] = Field(
        None,
        description="订阅提供商"
    )
    expires_at: Optional[datetime] = Field(
        None,
        description="到期时间"
    )
    auto_renew: bool = Field(
        default=True,
        description="是否自动续订"
    )
    limits: TierLimits = Field(
        ...,
        description="当前等级的功能限制"
    )


class AppleReceiptRequest(BaseModel):
    """Apple 收据验证请求"""
    receipt_data: str = Field(
        ...,
        description="Base64 编码的收据数据"
    )
    transaction_id: Optional[str] = Field(
        None,
        description="交易ID"
    )


class GooglePurchaseRequest(BaseModel):
    """Google 购买验证请求"""
    purchase_token: str = Field(
        ...,
        description="Google Play 购买令牌"
    )
    product_id: str = Field(
        ...,
        description="产品ID"
    )


class VerifyResponse(BaseModel):
    """订阅验证响应"""
    success: bool = Field(
        ...,
        description="是否验证成功"
    )
    tier: MembershipTier = Field(
        ...,
        description="会员等级"
    )
    expires_at: Optional[datetime] = Field(
        None,
        description="到期时间"
    )
    error: Optional[str] = Field(
        None,
        description="错误信息"
    )


class PlanInfo(BaseModel):
    """套餐信息"""
    plan_id: str = Field(
        ...,
        description="套餐ID"
    )
    name: str = Field(
        ...,
        description="套餐名称"
    )
    tier: MembershipTier = Field(
        ...,
        description="会员等级"
    )
    price: float = Field(
        ...,
        description="价格"
    )
    currency: str = Field(
        default="CNY",
        description="货币"
    )
    period: str = Field(
        ...,
        description="周期：monthly/yearly"
    )
    features: List[str] = Field(
        default_factory=list,
        description="套餐功能列表"
    )
