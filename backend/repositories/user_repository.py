"""
User Repository

用户数据访问层，支持高并发场景。
"""

import logging
from datetime import datetime, date
from typing import Optional, Dict, Any

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert as pg_insert

from backend.db.session import async_session_maker
from backend.models.user import UserProfile, UserLimit

logger = logging.getLogger(__name__)


class UserRepository:
    """用户数据仓库"""
    
    # =========================================================================
    # 用户档案 CRUD
    # =========================================================================
    
    @staticmethod
    async def get_profile(user_id: str) -> Optional[UserProfile]:
        """获取用户档案"""
        async with async_session_maker() as session:
            result = await session.execute(
                select(UserProfile).where(UserProfile.user_id == user_id)
            )
            return result.scalar_one_or_none()
    
    @staticmethod
    async def get_or_create_profile(user_id: str) -> UserProfile:
        """
        获取或创建用户档案
        
        使用 PostgreSQL UPSERT 保证并发安全。
        """
        async with async_session_maker() as session:
            # 先尝试获取
            result = await session.execute(
                select(UserProfile).where(UserProfile.user_id == user_id)
            )
            profile = result.scalar_one_or_none()
            
            if profile:
                return profile
            
            # 不存在则创建（使用 UPSERT 防止并发冲突）
            now = datetime.utcnow()
            stmt = pg_insert(UserProfile).values(
                user_id=user_id,
                created_at=now,
                updated_at=now,
            ).on_conflict_do_nothing(index_elements=["user_id"])
            
            await session.execute(stmt)
            await session.commit()
            
            # 再次获取
            result = await session.execute(
                select(UserProfile).where(UserProfile.user_id == user_id)
            )
            return result.scalar_one()
    
    @staticmethod
    async def update_profile(
        user_id: str,
        birth_data: Optional[Dict[str, Any]] = None,
        preferences: Optional[Dict[str, Any]] = None,
    ) -> Optional[UserProfile]:
        """更新用户档案"""
        async with async_session_maker() as session:
            # 构建更新字段
            update_values: Dict[str, Any] = {"updated_at": datetime.utcnow()}
            
            # birth_data 和 preferences 作为 JSON 字段直接存储
            if birth_data is not None:
                update_values["birth_data"] = birth_data
            
            if preferences is not None:
                update_values["preferences"] = preferences
            
            # 执行更新
            await session.execute(
                update(UserProfile)
                .where(UserProfile.user_id == user_id)
                .values(**update_values)
            )
            await session.commit()
            
            # 返回更新后的档案
            result = await session.execute(
                select(UserProfile).where(UserProfile.user_id == user_id)
            )
            return result.scalar_one_or_none()
    
    @staticmethod
    async def delete_profile(user_id: str) -> bool:
        """删除用户档案"""
        async with async_session_maker() as session:
            result = await session.execute(
                delete(UserProfile).where(UserProfile.user_id == user_id)
            )
            await session.commit()
            return result.rowcount > 0
    
    # =========================================================================
    # 用户限制
    # =========================================================================
    
    @staticmethod
    async def get_user_limits(user_id: str, limit_date: date = None) -> Optional[UserLimit]:
        """获取用户指定日期的限制"""
        if limit_date is None:
            limit_date = date.today()
        
        async with async_session_maker() as session:
            result = await session.execute(
                select(UserLimit)
                .where(UserLimit.user_id == user_id)
                .where(UserLimit.limit_date == limit_date)
            )
            return result.scalar_one_or_none()
    
    @staticmethod
    async def get_or_create_limits(user_id: str, membership_tier: str = "free") -> UserLimit:
        """
        获取或创建今日用户限制
        
        使用 PostgreSQL UPSERT 保证并发安全。
        """
        today = date.today()
        
        # 根据会员等级获取限制
        tier_limits = {
            "free": {"daily_dreams": 3, "daily_readings": 5},
            "plus": {"daily_dreams": -1, "daily_readings": -1},  # -1 表示无限
        }
        limits = tier_limits.get(membership_tier, tier_limits["free"])
        
        async with async_session_maker() as session:
            # 先尝试获取
            result = await session.execute(
                select(UserLimit)
                .where(UserLimit.user_id == user_id)
                .where(UserLimit.limit_date == today)
            )
            limit = result.scalar_one_or_none()
            
            if limit:
                return limit
            
            # 不存在则创建（使用 UPSERT 防止并发冲突）
            stmt = pg_insert(UserLimit).values(
                user_id=user_id,
                limit_date=today,
                daily_dreams=limits["daily_dreams"],
                daily_readings=limits["daily_readings"],
                dreams_used=0,
                readings_used=0,
            ).on_conflict_do_nothing(
                constraint="uq_user_limit_date"
            )
            
            await session.execute(stmt)
            await session.commit()
            
            # 再次获取
            result = await session.execute(
                select(UserLimit)
                .where(UserLimit.user_id == user_id)
                .where(UserLimit.limit_date == today)
            )
            return result.scalar_one()
    
    @staticmethod
    async def increment_usage(
        user_id: str,
        usage_type: str,  # "dreams" | "readings"
    ) -> bool:
        """
        增加使用计数
        
        使用数据库原子操作保证并发安全。
        
        Returns:
            True 如果成功增加，False 如果已达上限
        """
        today = date.today()
        
        async with async_session_maker() as session:
            # 获取限制（带行级锁）
            result = await session.execute(
                select(UserLimit)
                .where(UserLimit.user_id == user_id)
                .where(UserLimit.limit_date == today)
                .with_for_update()  # 行级锁，防止并发问题
            )
            limit = result.scalar_one_or_none()
            
            if not limit:
                # 自动创建今日限制
                limit = await UserRepository.get_or_create_limits(user_id)
                # 重新获取带锁的记录
                result = await session.execute(
                    select(UserLimit)
                    .where(UserLimit.user_id == user_id)
                    .where(UserLimit.limit_date == today)
                    .with_for_update()
                )
                limit = result.scalar_one_or_none()
                if not limit:
                    return False
            
            # 检查是否已达上限（-1 表示无限）
            if usage_type == "dreams":
                if limit.daily_dreams != -1 and limit.dreams_used >= limit.daily_dreams:
                    return False
                limit.dreams_used += 1
            elif usage_type == "readings":
                if limit.daily_readings != -1 and limit.readings_used >= limit.daily_readings:
                    return False
                limit.readings_used += 1
            else:
                return False
            
            await session.commit()
            return True
    
    @staticmethod
    async def check_limit(user_id: str, usage_type: str) -> Dict[str, Any]:
        """
        检查用户限制
        
        Returns:
            {
                "allowed": bool,
                "used": int,
                "limit": int,
                "remaining": int,
                "unlimited": bool,
            }
        """
        limit = await UserRepository.get_or_create_limits(user_id)
        
        if usage_type == "dreams":
            used = limit.dreams_used
            total = limit.daily_dreams
        elif usage_type == "readings":
            used = limit.readings_used
            total = limit.daily_readings
        else:
            return {"allowed": False, "used": 0, "limit": 0, "remaining": 0, "unlimited": False}
        
        # -1 表示无限
        if total == -1:
            return {
                "allowed": True,
                "used": used,
                "limit": -1,
                "remaining": -1,
                "unlimited": True,
            }
        
        remaining = max(0, total - used)
        
        return {
            "allowed": remaining > 0,
            "used": used,
            "limit": total,
            "remaining": remaining,
            "unlimited": False,
        }
    
    # =========================================================================
    # 批量操作（用于定时任务）
    # =========================================================================
    
    @staticmethod
    async def get_active_users(days: int = 7) -> list[str]:
        """获取活跃用户列表"""
        from datetime import timedelta
        
        cutoff = datetime.utcnow() - timedelta(days=days)
        
        async with async_session_maker() as session:
            result = await session.execute(
                select(UserProfile.user_id)
                .where(UserProfile.updated_at >= cutoff)
            )
            return [row[0] for row in result.fetchall()]
    
    @staticmethod
    async def update_membership_limits(user_id: str, tier: str) -> bool:
        """
        更新用户会员等级对应的限制
        
        会员升级时更新今日限制。
        """
        tier_limits = {
            "free": {"daily_dreams": 3, "daily_readings": 5},
            "plus": {"daily_dreams": -1, "daily_readings": -1},
        }
        limits = tier_limits.get(tier, tier_limits["free"])
        today = date.today()
        
        async with async_session_maker() as session:
            result = await session.execute(
                update(UserLimit)
                .where(UserLimit.user_id == user_id)
                .where(UserLimit.limit_date == today)
                .values(
                    daily_dreams=limits["daily_dreams"],
                    daily_readings=limits["daily_readings"],
                )
            )
            await session.commit()
            return result.rowcount > 0
