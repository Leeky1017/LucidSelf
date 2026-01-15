"""
Memory Repository

记忆层数据访问层，封装所有数据库操作。

对照模型: backend/models/memory.py
对照服务: backend/services/memory/service.py
"""

import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlalchemy import select, update, delete, and_, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import async_session_maker
from backend.models.memory import (
    MemoryEventDB,
    MemoryInsightDB,
    UserProfileDB,
)
from backend.services.memory.models import (
    MemoryEvent,
    MemoryInsight,
    UserProfile,
    PrivacyLevel,
)

logger = logging.getLogger(__name__)


def _gen_id(prefix: str) -> str:
    """生成唯一 ID"""
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


class MemoryRepository:
    """
    记忆层数据访问仓库
    
    提供 Event、Insight、Profile 的 CRUD 操作，
    将 Pydantic 模型与 SQLAlchemy 模型相互转换。
    """
    
    # =========================================================================
    # Event 操作
    # =========================================================================
    
    async def create_event(
        self,
        user_id: str,
        event_type: str,
        data: Dict[str, Any],
        privacy_level: PrivacyLevel = PrivacyLevel.PRIVATE,
    ) -> str:
        """
        创建事件
        
        Returns:
            event_id
        """
        event_id = _gen_id("evt")
        
        async with async_session_maker() as session:
            event = MemoryEventDB(
                event_id=event_id,
                user_id=user_id,
                event_type=event_type,
                data=data,
                privacy_level=privacy_level,
            )
            session.add(event)
            await session.commit()
            
            logger.debug(f"Created event {event_id} for user {user_id}")
            return event_id
    
    async def get_event(self, event_id: str) -> Optional[MemoryEvent]:
        """获取单个事件"""
        async with async_session_maker() as session:
            result = await session.execute(
                select(MemoryEventDB)
                .where(MemoryEventDB.event_id == event_id)
            )
            event = result.scalar_one_or_none()
            
            if not event:
                return None
            
            return self._to_pydantic_event(event)
    
    async def get_events(
        self,
        user_id: str,
        since: Optional[datetime] = None,
        event_type: Optional[str] = None,
        limit: int = 100,
    ) -> List[MemoryEvent]:
        """获取用户事件列表"""
        async with async_session_maker() as session:
            query = (
                select(MemoryEventDB)
                .where(MemoryEventDB.user_id == user_id)
            )
            
            if since:
                query = query.where(MemoryEventDB.created_at >= since)
            if event_type:
                query = query.where(MemoryEventDB.event_type == event_type)
            
            query = query.order_by(desc(MemoryEventDB.created_at)).limit(limit)
            
            result = await session.execute(query)
            events = result.scalars().all()
            
            return [self._to_pydantic_event(e) for e in events]
    
    async def delete_event(self, event_id: str) -> bool:
        """删除事件"""
        async with async_session_maker() as session:
            result = await session.execute(
                delete(MemoryEventDB)
                .where(MemoryEventDB.event_id == event_id)
            )
            await session.commit()
            return result.rowcount > 0
    
    # =========================================================================
    # Insight 操作
    # =========================================================================
    
    async def create_insight(
        self,
        user_id: str,
        summary: str,
        source_events: List[str],
        confidence: float = 0.5,
        dimension: Optional[str] = None,
        source_engine: Optional[str] = None,
        privacy_level: PrivacyLevel = PrivacyLevel.PRIVATE,
    ) -> str:
        """
        创建洞察
        
        Returns:
            insight_id
        """
        insight_id = _gen_id("ins")
        
        async with async_session_maker() as session:
            insight = MemoryInsightDB(
                insight_id=insight_id,
                user_id=user_id,
                source_events=source_events,
                summary=summary,
                confidence=confidence,
                dimension=dimension,
                source_engine=source_engine,
                privacy_level=privacy_level,
            )
            session.add(insight)
            await session.commit()
            
            logger.debug(f"Created insight {insight_id} for user {user_id}")
            return insight_id
    
    async def get_insight(self, insight_id: str) -> Optional[MemoryInsight]:
        """获取单个洞察"""
        async with async_session_maker() as session:
            result = await session.execute(
                select(MemoryInsightDB)
                .where(MemoryInsightDB.insight_id == insight_id)
            )
            insight = result.scalar_one_or_none()
            
            if not insight:
                return None
            
            return self._to_pydantic_insight(insight)
    
    async def get_insights(
        self,
        user_id: str,
        dimension: Optional[str] = None,
        min_confidence: float = 0.0,
        since: Optional[datetime] = None,
        limit: int = 100,
    ) -> List[MemoryInsight]:
        """获取用户洞察列表"""
        async with async_session_maker() as session:
            query = (
                select(MemoryInsightDB)
                .where(MemoryInsightDB.user_id == user_id)
                .where(MemoryInsightDB.confidence >= min_confidence)
            )
            
            if dimension:
                query = query.where(MemoryInsightDB.dimension == dimension)
            if since:
                query = query.where(MemoryInsightDB.created_at >= since)
            
            query = query.order_by(desc(MemoryInsightDB.created_at)).limit(limit)
            
            result = await session.execute(query)
            insights = result.scalars().all()
            
            return [self._to_pydantic_insight(i) for i in insights]
    
    async def update_insight_confidence(
        self,
        insight_id: str,
        confidence: float,
    ) -> bool:
        """更新洞察置信度"""
        async with async_session_maker() as session:
            result = await session.execute(
                update(MemoryInsightDB)
                .where(MemoryInsightDB.insight_id == insight_id)
                .values(confidence=confidence)
            )
            await session.commit()
            return result.rowcount > 0
    
    async def delete_insight(self, insight_id: str) -> bool:
        """删除洞察"""
        async with async_session_maker() as session:
            result = await session.execute(
                delete(MemoryInsightDB)
                .where(MemoryInsightDB.insight_id == insight_id)
            )
            await session.commit()
            return result.rowcount > 0
    
    # =========================================================================
    # Profile 操作
    # =========================================================================
    
    async def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """获取用户画像"""
        async with async_session_maker() as session:
            result = await session.execute(
                select(UserProfileDB)
                .where(UserProfileDB.user_id == user_id)
            )
            profile = result.scalar_one_or_none()
            
            if not profile:
                return None
            
            return self._to_pydantic_profile(profile)
    
    async def update_profile(
        self,
        user_id: str,
        traits: Optional[Dict[str, float]] = None,
        preferences: Optional[Dict[str, Any]] = None,
    ) -> None:
        """更新用户画像（不存在则创建）"""
        async with async_session_maker() as session:
            # 获取现有画像
            result = await session.execute(
                select(UserProfileDB)
                .where(UserProfileDB.user_id == user_id)
            )
            profile = result.scalar_one_or_none()
            
            if profile is None:
                # 创建新画像
                profile = UserProfileDB(
                    user_id=user_id,
                    traits=traits or {},
                    preferences=preferences or {},
                )
                session.add(profile)
            else:
                # 合并更新
                if traits:
                    current_traits = profile.traits or {}
                    current_traits.update(traits)
                    profile.traits = current_traits
                if preferences:
                    current_prefs = profile.preferences or {}
                    current_prefs.update(preferences)
                    profile.preferences = current_prefs
                profile.last_updated = datetime.utcnow()
            
            await session.commit()
            logger.debug(f"Updated profile for user {user_id}")
    
    async def delete_profile(self, user_id: str) -> bool:
        """删除用户画像"""
        async with async_session_maker() as session:
            result = await session.execute(
                delete(UserProfileDB)
                .where(UserProfileDB.user_id == user_id)
            )
            await session.commit()
            return result.rowcount > 0
    
    # =========================================================================
    # 转换辅助方法
    # =========================================================================
    
    def _to_pydantic_event(self, model: MemoryEventDB) -> MemoryEvent:
        """SQLAlchemy 模型转 Pydantic 模型"""
        return MemoryEvent(
            event_id=model.event_id,
            user_id=model.user_id,
            event_type=model.event_type,
            data=model.data or {},
            privacy_level=model.privacy_level,
            created_at=model.created_at,
        )
    
    def _to_pydantic_insight(self, model: MemoryInsightDB) -> MemoryInsight:
        """SQLAlchemy 模型转 Pydantic 模型"""
        return MemoryInsight(
            insight_id=model.insight_id,
            user_id=model.user_id,
            source_events=model.source_events or [],
            summary=model.summary,
            confidence=model.confidence,
            dimension=model.dimension,
            source_engine=getattr(model, 'source_engine', None),
            privacy_level=model.privacy_level,
            created_at=model.created_at,
        )
    
    def _to_pydantic_profile(self, model: UserProfileDB) -> UserProfile:
        """SQLAlchemy 模型转 Pydantic 模型"""
        return UserProfile(
            user_id=model.user_id,
            traits=model.traits or {},
            preferences=model.preferences or {},
            last_updated=model.last_updated,
        )


# =============================================================================
# 单例 / 便捷函数
# =============================================================================

_repository: Optional[MemoryRepository] = None


def get_memory_repository() -> MemoryRepository:
    """获取记忆层仓库单例"""
    global _repository
    if _repository is None:
        _repository = MemoryRepository()
    return _repository
