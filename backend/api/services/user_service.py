"""
User Service

用户档案和限制业务逻辑。
"""

import logging
import uuid
from datetime import date, datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.user import UserProfile, UserLimit

logger = logging.getLogger(__name__)


class UserService:
    """用户服务"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    # ==================== Profile ====================
    
    async def get_or_create_profile(self, user_id: str) -> UserProfile:
        """获取或创建用户档案"""
        result = await self.db.execute(
            select(UserProfile).where(UserProfile.user_id == user_id)
        )
        profile = result.scalar_one_or_none()
        
        if not profile:
            profile = UserProfile(
                id=uuid.uuid4(),
                user_id=user_id,
                preferences={
                    "language": "zh",
                    "theme": "light",
                    "enabled_engines": ["bazi", "ziwei", "astro", "tarot"],
                    "notification_enabled": True,
                },
            )
            self.db.add(profile)
            await self.db.flush()
            await self.db.refresh(profile)
            logger.info(f"Created profile for user {user_id}")
        
        return profile
    
    async def update_profile(
        self,
        user_id: str,
        birth_data: Optional[dict] = None,
        preferences: Optional[dict] = None,
    ) -> UserProfile:
        """更新用户档案"""
        profile = await self.get_or_create_profile(user_id)
        
        if birth_data is not None:
            profile.birth_data = birth_data
        
        if preferences is not None:
            # 合并偏好设置
            current_prefs = profile.preferences or {}
            current_prefs.update(preferences)
            profile.preferences = current_prefs
        
        profile.updated_at = datetime.utcnow()
        await self.db.flush()
        await self.db.refresh(profile)
        
        return profile
    
    # ==================== Limits ====================
    
    async def get_or_create_limit(self, user_id: str) -> UserLimit:
        """获取或创建今日限制记录"""
        today = date.today()
        
        result = await self.db.execute(
            select(UserLimit).where(
                UserLimit.user_id == user_id,
                UserLimit.limit_date == today,
            )
        )
        limit = result.scalar_one_or_none()
        
        if not limit:
            limit = UserLimit(
                id=uuid.uuid4(),
                user_id=user_id,
                limit_date=today,
                daily_dreams=5,
                daily_readings=10,
                dreams_used=0,
                readings_used=0,
            )
            self.db.add(limit)
            await self.db.flush()
            await self.db.refresh(limit)
            logger.info(f"Created limit record for user {user_id} on {today}")
        
        return limit
    
    async def consume_limit(self, user_id: str, limit_type: str) -> tuple[bool, int]:
        """
        消费配额
        
        Returns:
            (success, remaining)
        """
        limit = await self.get_or_create_limit(user_id)
        
        if limit_type == "dream":
            if limit.dreams_used >= limit.daily_dreams:
                return False, 0
            limit.dreams_used += 1
            remaining = limit.daily_dreams - limit.dreams_used
        elif limit_type == "reading":
            if limit.readings_used >= limit.daily_readings:
                return False, 0
            limit.readings_used += 1
            remaining = limit.daily_readings - limit.readings_used
        else:
            return False, 0
        
        await self.db.flush()
        return True, remaining
    
    async def get_limits_summary(self, user_id: str) -> dict:
        """获取限制摘要"""
        limit = await self.get_or_create_limit(user_id)
        return {
            "daily_dreams": limit.daily_dreams,
            "daily_readings": limit.daily_readings,
            "dreams_used_today": limit.dreams_used,
            "readings_used_today": limit.readings_used,
            "dreams_remaining": limit.daily_dreams - limit.dreams_used,
            "readings_remaining": limit.daily_readings - limit.readings_used,
            "last_reset_date": limit.limit_date.isoformat(),
        }
