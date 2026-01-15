"""
Subscription Service

订阅/会员服务实现。

对照契约: backend/core/contracts/subscription_models.py
"""

import logging
import secrets
from datetime import datetime, timedelta
from typing import List, Optional

from backend.core.contracts.subscription_models import (
    MembershipTier,
    SubscriptionProvider,
    SubscriptionStatus,
    TierLimits,
    TIER_LIMITS,
    SubscriptionStatusResponse,
    PlanInfo,
)

logger = logging.getLogger(__name__)


# =============================================================================
# ID 生成
# =============================================================================

def generate_subscription_id() -> str:
    """生成订阅ID: sub_xxxxxxxxxxxx"""
    return f"sub_{secrets.token_hex(6)}"


# =============================================================================
# 套餐定义
# =============================================================================

PLANS: List[PlanInfo] = [
    PlanInfo(
        plan_id="plus_monthly",
        name="Plus 月度",
        tier=MembershipTier.PLUS,
        price=28.0,
        currency="CNY",
        period="monthly",
        features=[
            "无限梦境解读",
            "无限 Playbook 生成",
            "永久历史记录",
            "高级命理引擎",
            "数据导出",
            "批量操作",
        ],
    ),
    PlanInfo(
        plan_id="plus_yearly",
        name="Plus 年度",
        tier=MembershipTier.PLUS,
        price=198.0,
        currency="CNY",
        period="yearly",
        features=[
            "无限梦境解读",
            "无限 Playbook 生成",
            "永久历史记录",
            "高级命理引擎",
            "数据导出",
            "批量操作",
            "年度专属优惠（省120元）",
        ],
    ),
]


# =============================================================================
# 订阅服务
# =============================================================================

class SubscriptionService:
    """
    订阅服务
    
    提供订阅状态查询、验证和管理功能。
    """
    
    def __init__(self):
        # 内存存储（开发用，生产环境使用数据库）
        self._subscriptions: dict = {}  # user_id -> subscription_data
    
    # =========================================================================
    # 状态查询
    # =========================================================================
    
    async def get_status(self, user_id: str) -> SubscriptionStatusResponse:
        """
        获取用户订阅状态
        
        返回当前订阅状态和对应的功能限制。
        """
        sub = self._subscriptions.get(user_id)
        
        if not sub:
            # 默认 Free 用户
            return SubscriptionStatusResponse(
                tier=MembershipTier.FREE,
                status=SubscriptionStatus.ACTIVE,
                provider=None,
                expires_at=None,
                auto_renew=False,
                limits=TIER_LIMITS[MembershipTier.FREE],
            )
        
        # 检查是否过期
        if sub.get("expires_at") and datetime.utcnow() > sub["expires_at"]:
            sub["status"] = SubscriptionStatus.EXPIRED
            sub["tier"] = MembershipTier.FREE
        
        tier = sub.get("tier", MembershipTier.FREE)
        
        return SubscriptionStatusResponse(
            tier=tier,
            status=sub.get("status", SubscriptionStatus.ACTIVE),
            provider=sub.get("provider"),
            expires_at=sub.get("expires_at"),
            auto_renew=sub.get("auto_renew", False),
            limits=TIER_LIMITS[tier],
        )
    
    async def get_tier(self, user_id: str) -> MembershipTier:
        """获取用户会员等级"""
        status = await self.get_status(user_id)
        return status.tier
    
    async def get_limits(self, user_id: str) -> TierLimits:
        """获取用户功能限制"""
        status = await self.get_status(user_id)
        return status.limits
    
    async def is_plus(self, user_id: str) -> bool:
        """检查用户是否为 Plus 会员"""
        tier = await self.get_tier(user_id)
        return tier == MembershipTier.PLUS
    
    # =========================================================================
    # 套餐
    # =========================================================================
    
    async def get_plans(self) -> List[PlanInfo]:
        """获取可用套餐列表"""
        return PLANS
    
    # =========================================================================
    # 订阅管理
    # =========================================================================
    
    async def activate_subscription(
        self,
        user_id: str,
        tier: MembershipTier,
        provider: SubscriptionProvider,
        provider_subscription_id: str,
        expires_at: Optional[datetime] = None,
    ) -> SubscriptionStatusResponse:
        """
        激活订阅
        
        用于收据验证成功后激活用户订阅。
        """
        now = datetime.utcnow()
        
        self._subscriptions[user_id] = {
            "subscription_id": generate_subscription_id(),
            "user_id": user_id,
            "tier": tier,
            "provider": provider,
            "provider_subscription_id": provider_subscription_id,
            "status": SubscriptionStatus.ACTIVE,
            "started_at": now,
            "expires_at": expires_at,
            "auto_renew": True,
            "created_at": now,
        }
        
        logger.info(f"Subscription activated: {user_id} -> {tier}")
        return await self.get_status(user_id)
    
    async def cancel_subscription(self, user_id: str) -> bool:
        """
        取消订阅
        
        标记取消但保留权益直到到期。
        """
        sub = self._subscriptions.get(user_id)
        if not sub:
            return False
        
        sub["status"] = SubscriptionStatus.CANCELLED
        sub["cancelled_at"] = datetime.utcnow()
        sub["auto_renew"] = False
        
        logger.info(f"Subscription cancelled: {user_id}")
        return True
    
    # =========================================================================
    # 收据验证（预留）
    # =========================================================================
    
    async def verify_apple_receipt(
        self,
        user_id: str,
        receipt_data: str,
        transaction_id: Optional[str] = None,
    ) -> dict:
        """
        验证 Apple 收据
        
        TODO: 集成 App Store Server API
        """
        # 开发模式：模拟成功
        logger.warning("Apple receipt verification not implemented, using mock")
        
        # 模拟激活
        expires_at = datetime.utcnow() + timedelta(days=30)
        await self.activate_subscription(
            user_id=user_id,
            tier=MembershipTier.PLUS,
            provider=SubscriptionProvider.APPLE,
            provider_subscription_id=transaction_id or "mock_apple_sub",
            expires_at=expires_at,
        )
        
        return {
            "success": True,
            "tier": MembershipTier.PLUS,
            "expires_at": expires_at,
        }
    
    async def verify_google_purchase(
        self,
        user_id: str,
        purchase_token: str,
        product_id: str,
    ) -> dict:
        """
        验证 Google 购买
        
        TODO: 集成 Google Play Developer API
        """
        # 开发模式：模拟成功
        logger.warning("Google purchase verification not implemented, using mock")
        
        # 模拟激活
        expires_at = datetime.utcnow() + timedelta(days=30)
        await self.activate_subscription(
            user_id=user_id,
            tier=MembershipTier.PLUS,
            provider=SubscriptionProvider.GOOGLE,
            provider_subscription_id=purchase_token,
            expires_at=expires_at,
        )
        
        return {
            "success": True,
            "tier": MembershipTier.PLUS,
            "expires_at": expires_at,
        }


# =============================================================================
# 全局实例
# =============================================================================

_subscription_service: Optional[SubscriptionService] = None


def get_subscription_service() -> SubscriptionService:
    """获取订阅服务实例"""
    global _subscription_service
    if _subscription_service is None:
        _subscription_service = SubscriptionService()
    return _subscription_service
