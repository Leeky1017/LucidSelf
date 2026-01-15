"""
Subscription API Routes

订阅/会员相关 API 端点。

对照契约: backend/core/contracts/subscription_models.py
对照文档: .kiro/docs/api_contracts.md §3.2
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from backend.core.contracts.auth_models import UserInfo
from backend.core.contracts.subscription_models import (
    MembershipTier,
    SubscriptionStatusResponse,
    AppleReceiptRequest,
    GooglePurchaseRequest,
    VerifyResponse,
    PlanInfo,
)
from backend.services.subscription import SubscriptionService, get_subscription_service
from backend.api.routes.auth import get_current_user

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/subscription", tags=["subscription"])


# =============================================================================
# 状态查询
# =============================================================================

@router.get(
    "",
    response_model=SubscriptionStatusResponse,
    summary="获取订阅状态",
    description="获取当前用户的订阅状态和功能限制",
)
async def get_subscription_status(
    user: UserInfo = Depends(get_current_user),
    service: SubscriptionService = Depends(get_subscription_service),
) -> SubscriptionStatusResponse:
    """
    获取订阅状态
    
    返回当前会员等级、订阅状态和功能限制。
    """
    return await service.get_status(user.user_id)


@router.get(
    "/plans",
    response_model=List[PlanInfo],
    summary="获取套餐列表",
    description="获取可用的订阅套餐",
)
async def get_plans(
    service: SubscriptionService = Depends(get_subscription_service),
) -> List[PlanInfo]:
    """
    获取套餐列表
    
    返回所有可用的订阅套餐信息。
    """
    return await service.get_plans()


# =============================================================================
# 收据验证
# =============================================================================

@router.post(
    "/verify/apple",
    response_model=VerifyResponse,
    summary="验证 Apple 收据",
    description="验证 App Store 购买收据并激活订阅",
)
async def verify_apple_receipt(
    request: AppleReceiptRequest,
    user: UserInfo = Depends(get_current_user),
    service: SubscriptionService = Depends(get_subscription_service),
) -> VerifyResponse:
    """
    验证 Apple 收据
    
    - **receipt_data**: Base64 编码的收据数据
    - **transaction_id**: 交易ID（可选）
    
    验证成功后自动激活订阅。
    """
    try:
        result = await service.verify_apple_receipt(
            user_id=user.user_id,
            receipt_data=request.receipt_data,
            transaction_id=request.transaction_id,
        )
        return VerifyResponse(
            success=result["success"],
            tier=result["tier"],
            expires_at=result.get("expires_at"),
        )
    except Exception as e:
        logger.error(f"Apple receipt verification failed: {e}")
        return VerifyResponse(
            success=False,
            tier=MembershipTier.FREE,
            error=str(e),
        )


@router.post(
    "/verify/google",
    response_model=VerifyResponse,
    summary="验证 Google 购买",
    description="验证 Google Play 购买并激活订阅",
)
async def verify_google_purchase(
    request: GooglePurchaseRequest,
    user: UserInfo = Depends(get_current_user),
    service: SubscriptionService = Depends(get_subscription_service),
) -> VerifyResponse:
    """
    验证 Google 购买
    
    - **purchase_token**: Google Play 购买令牌
    - **product_id**: 产品ID
    
    验证成功后自动激活订阅。
    """
    try:
        result = await service.verify_google_purchase(
            user_id=user.user_id,
            purchase_token=request.purchase_token,
            product_id=request.product_id,
        )
        return VerifyResponse(
            success=result["success"],
            tier=result["tier"],
            expires_at=result.get("expires_at"),
        )
    except Exception as e:
        logger.error(f"Google purchase verification failed: {e}")
        return VerifyResponse(
            success=False,
            tier=MembershipTier.FREE,
            error=str(e),
        )


# =============================================================================
# 订阅管理
# =============================================================================

@router.post(
    "/cancel",
    summary="取消订阅",
    description="取消当前订阅（保留权益直到到期）",
)
async def cancel_subscription(
    user: UserInfo = Depends(get_current_user),
    service: SubscriptionService = Depends(get_subscription_service),
) -> dict:
    """
    取消订阅
    
    取消自动续订，权益保留至到期日。
    """
    success = await service.cancel_subscription(user.user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "NO_SUBSCRIPTION", "message": "没有活跃的订阅"},
        )
    return {"success": True, "message": "订阅已取消"}


# =============================================================================
# 功能门控装饰器
# =============================================================================

def require_plus():
    """
    Plus 会员门控依赖
    
    用法:
    ```python
    @router.get("/premium-feature")
    async def premium_feature(
        user: UserInfo = Depends(get_current_user),
        _: None = Depends(require_plus()),
    ):
        ...
    ```
    """
    async def check_plus(
        user: UserInfo = Depends(get_current_user),
        service: SubscriptionService = Depends(get_subscription_service),
    ):
        is_plus = await service.is_plus(user.user_id)
        if not is_plus:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "code": "SUBSCRIPTION_REQUIRED",
                    "message": "此功能需要 Plus 会员",
                },
            )
    return check_plus
