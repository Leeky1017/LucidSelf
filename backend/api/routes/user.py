"""
User Route

用户档案和限制端点。
"""

import logging
from datetime import datetime, date
from typing import Dict, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/user", tags=["User"])


# ==================== 请求/响应模型 ====================

class BirthData(BaseModel):
    """出生数据"""
    year: int = Field(..., ge=1900, le=2100)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(default=0, ge=0, le=59)
    timezone: str = Field(default="Asia/Shanghai")
    gender: str = Field(default="male")
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class UserPreferences(BaseModel):
    """用户偏好"""
    language: str = Field(default="zh")
    theme: str = Field(default="light")
    enabled_engines: list = Field(default_factory=lambda: ["bazi", "ziwei", "astro", "tarot"])
    notification_enabled: bool = Field(default=True)


class UserProfile(BaseModel):
    """用户档案"""
    user_id: str
    birth_data: Optional[BirthData] = None
    preferences: UserPreferences = Field(default_factory=UserPreferences)
    created_at: str
    updated_at: str


class UserProfileUpdateRequest(BaseModel):
    """更新用户档案请求"""
    birth_data: Optional[BirthData] = None
    preferences: Optional[UserPreferences] = None


class UserLimits(BaseModel):
    """用户限制"""
    daily_dreams: int = Field(default=5, description="每日梦境记录限制")
    daily_readings: int = Field(default=10, description="每日解读限制")
    dreams_used_today: int = Field(default=0)
    readings_used_today: int = Field(default=0)
    dreams_remaining: int = Field(default=5)
    readings_remaining: int = Field(default=10)
    last_reset_date: str


# ==================== 数据仓库 ====================

from backend.repositories.user_repository import UserRepository


# ==================== API端点 ====================

@router.get("/profile")
async def get_user_profile(user_id: str):
    """获取用户档案"""
    profile = await UserRepository.get_or_create_profile(user_id)
    return profile.to_dict()


@router.put("/profile")
async def update_user_profile(user_id: str, request: UserProfileUpdateRequest):
    """更新用户档案"""
    # 确保档案存在
    await UserRepository.get_or_create_profile(user_id)
    
    # 更新档案
    profile = await UserRepository.update_profile(
        user_id=user_id,
        birth_data=request.birth_data.model_dump() if request.birth_data else None,
        preferences=request.preferences.model_dump() if request.preferences else None,
    )
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found"
        )
    
    return profile.to_dict()


@router.get("/limits")
async def get_user_limits(user_id: str):
    """获取用户限制"""
    limit = await UserRepository.get_or_create_limits(user_id)
    
    # 计算剩余量
    dreams_remaining = -1 if limit.daily_dreams == -1 else (limit.daily_dreams - limit.dreams_used)
    readings_remaining = -1 if limit.daily_readings == -1 else (limit.daily_readings - limit.readings_used)
    
    return {
        "daily_dreams": limit.daily_dreams,
        "daily_readings": limit.daily_readings,
        "dreams_used_today": limit.dreams_used,
        "readings_used_today": limit.readings_used,
        "dreams_remaining": max(0, dreams_remaining) if dreams_remaining != -1 else -1,
        "readings_remaining": max(0, readings_remaining) if readings_remaining != -1 else -1,
        "last_reset_date": limit.limit_date.isoformat(),
        "unlimited_dreams": limit.daily_dreams == -1,
        "unlimited_readings": limit.daily_readings == -1,
    }


@router.post("/limits/consume")
async def consume_limit(user_id: str, limit_type: str):
    """
    消费限制额度
    
    limit_type: 'dream' 或 'reading'
    """
    # 映射类型
    usage_type = "dreams" if limit_type == "dream" else "readings" if limit_type == "reading" else None
    
    if not usage_type:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "INVALID_LIMIT_TYPE", "message": f"Unknown limit type: {limit_type}"}
        )
    
    # 尝试增加使用量
    success = await UserRepository.increment_usage(user_id, usage_type)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"code": "LIMIT_EXCEEDED", "message": f"Daily {limit_type} limit reached"}
        )
    
    # 返回剩余量
    check_result = await UserRepository.check_limit(user_id, usage_type)
    
    return {
        "success": True,
        "remaining": check_result["remaining"],
        "unlimited": check_result["unlimited"],
    }


@router.get("/limits/check")
async def check_user_limit(user_id: str, limit_type: str):
    """
    检查用户限制（不消费）
    """
    usage_type = "dreams" if limit_type == "dream" else "readings" if limit_type == "reading" else None
    
    if not usage_type:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "INVALID_LIMIT_TYPE", "message": f"Unknown limit type: {limit_type}"}
        )
    
    return await UserRepository.check_limit(user_id, usage_type)
