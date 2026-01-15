"""
Memory Service

统一记忆访问服务。

对照 design.md 2.4, tasks.md 5.5:
- Requirements: 4.3.1-4.3.3
- ⚠️ 陷阱: 所有访问必须经过 service，不能直接访问存储

设计原则:
- 封装存储细节
- 自动加密 SENSITIVE 数据
- 统一访问控制

v2.0 更新: 支持数据库持久化 (persist=True) 和内存模式 (persist=False)
"""

import json
import logging
import uuid
from datetime import datetime, timedelta
from threading import Lock
from typing import Any, Dict, List, Optional

from backend.services.memory.models import (
    PrivacyLevel,
    MemoryEvent,
    MemoryInsight,
    UserProfile,
)
from backend.services.memory.encryption import EncryptionHelper, EncryptionError

logger = logging.getLogger(__name__)


class AccessDeniedError(Exception):
    """访问被拒绝"""
    pass


class RecordNotFoundError(Exception):
    """记录不存在"""
    pass


class MemoryService:
    """
    记忆服务
    
    三层记忆架构的统一访问接口:
    - Event: 原始事件记录
    - Insight: 归纳洞察
    - Profile: 用户画像
    
    支持两种模式:
    - persist=True: 使用数据库持久化 (生产环境)
    - persist=False: 使用内存存储 (测试/开发)
    
    ⚠️ 重要:
    - 所有访问必须经过此 service
    - SENSITIVE 数据自动加密
    - 不直接暴露存储
    """
    
    # 需要加密的字段
    SENSITIVE_FIELDS = {"data", "summary", "traits", "preferences"}
    
    def __init__(
        self,
        encryption_helper: Optional[EncryptionHelper] = None,
        persist: bool = True,
    ):
        """
        初始化记忆服务
        
        Args:
            encryption_helper: 加密助手，为 None 时自动创建
            persist: 是否使用数据库持久化
        """
        self._encryption = encryption_helper
        self._persist = persist
        self._repository = None
        
        # 内存存储 (仅当 persist=False 时使用)
        self._events: Dict[str, MemoryEvent] = {}
        self._insights: Dict[str, MemoryInsight] = {}
        self._profiles: Dict[str, UserProfile] = {}
        self._lock = Lock()
        
        if persist:
            try:
                from backend.repositories.memory_repository import get_memory_repository
                self._repository = get_memory_repository()
                logger.info("MemoryService initialized with database persistence")
            except Exception as e:
                logger.warning(f"Failed to initialize repository, falling back to memory: {e}")
                self._persist = False
    
    # ==================== Event 操作 ====================
    
    async def record_event(
        self,
        user_id: str,
        event_type: str,
        data: Dict[str, Any],
        privacy_level: PrivacyLevel = PrivacyLevel.PRIVATE,
    ) -> str:
        """
        记录事件
        
        Args:
            user_id: 用户 ID
            event_type: 事件类型
            data: 事件数据
            privacy_level: 隐私级别
            
        Returns:
            事件 ID
        """
        # SENSITIVE 数据加密
        stored_data = self._maybe_encrypt(data, privacy_level)
        
        if self._persist and self._repository:
            event_id = await self._repository.create_event(
                user_id=user_id,
                event_type=event_type,
                data=stored_data,
                privacy_level=privacy_level,
            )
            logger.info(
                "Recorded event (DB): event_id=%s, user_id=%s, type=%s",
                event_id, user_id, event_type,
            )
            return event_id
        
        # 内存模式
        event_id = f"evt_{uuid.uuid4().hex[:12]}"
        
        event = MemoryEvent(
            event_id=event_id,
            user_id=user_id,
            event_type=event_type,
            data=stored_data,
            privacy_level=privacy_level,
        )
        
        with self._lock:
            self._events[event_id] = event
        
        logger.info(
            "Recorded event (memory): event_id=%s, user_id=%s, type=%s",
            event_id, user_id, event_type,
        )
        
        return event_id
    
    async def get_event(
        self,
        event_id: str,
        user_id: str,
    ) -> MemoryEvent:
        """
        获取事件
        
        Args:
            event_id: 事件 ID
            user_id: 请求者用户 ID (用于访问控制)
            
        Returns:
            事件 (解密后)
            
        Raises:
            RecordNotFoundError: 事件不存在
            AccessDeniedError: 无权访问
        """
        if self._persist and self._repository:
            event = await self._repository.get_event(event_id)
            if event is None:
                raise RecordNotFoundError(f"Event not found: {event_id}")
        else:
            with self._lock:
                event = self._events.get(event_id)
            if event is None:
                raise RecordNotFoundError(f"Event not found: {event_id}")
        
        # 访问控制
        self._check_access(user_id, event.user_id, event.privacy_level)
        
        # 解密
        decrypted_data = self._maybe_decrypt(event.data, event.privacy_level)
        
        return MemoryEvent(
            event_id=event.event_id,
            user_id=event.user_id,
            event_type=event.event_type,
            data=decrypted_data,
            privacy_level=event.privacy_level,
            created_at=event.created_at,
        )
    
    async def get_events(
        self,
        user_id: str,
        since: Optional[datetime] = None,
        event_type: Optional[str] = None,
        limit: int = 100,
    ) -> List[MemoryEvent]:
        """
        获取用户事件列表
        
        Args:
            user_id: 用户 ID
            since: 起始时间
            event_type: 事件类型过滤
            limit: 最大返回数量
            
        Returns:
            事件列表 (解密后)
        """
        if self._persist and self._repository:
            events = await self._repository.get_events(
                user_id=user_id,
                since=since,
                event_type=event_type,
                limit=limit,
            )
            # 解密
            return [
                MemoryEvent(
                    event_id=e.event_id,
                    user_id=e.user_id,
                    event_type=e.event_type,
                    data=self._maybe_decrypt(e.data, e.privacy_level),
                    privacy_level=e.privacy_level,
                    created_at=e.created_at,
                )
                for e in events
            ]
        
        # 内存模式
        results = []
        
        with self._lock:
            for event in self._events.values():
                if event.user_id != user_id:
                    continue
                if since and event.created_at < since:
                    continue
                if event_type and event.event_type != event_type:
                    continue
                
                # 解密
                decrypted_data = self._maybe_decrypt(event.data, event.privacy_level)
                results.append(MemoryEvent(
                    event_id=event.event_id,
                    user_id=event.user_id,
                    event_type=event.event_type,
                    data=decrypted_data,
                    privacy_level=event.privacy_level,
                    created_at=event.created_at,
                ))
                
                if len(results) >= limit:
                    break
        
        return results
    
    # ==================== Insight 操作 ====================
    
    async def create_insight(
        self,
        user_id: str,
        summary: str,
        source_events: List[str],
        confidence: float = 0.5,
        dimension: Optional[str] = None,
        source_engine: Optional[str] = None,  # Phase 10 Task 10.1: 新增
        privacy_level: PrivacyLevel = PrivacyLevel.PRIVATE,
    ) -> str:
        """
        创建洞察
        
        Args:
            user_id: 用户 ID
            summary: 洞察摘要
            source_events: 来源事件 ID 列表
            confidence: 置信度
            dimension: 相关维度 (behavior, dream, decision, emotion, destiny)
            source_engine: 来源引擎 ID (如 bazi-calculator, dream-extractor)
            privacy_level: 隐私级别
            
        Returns:
            洞察 ID
        """
        # SENSITIVE 摘要加密
        stored_summary = self._maybe_encrypt_str(summary, privacy_level)
        
        if self._persist and self._repository:
            insight_id = await self._repository.create_insight(
                user_id=user_id,
                summary=stored_summary,
                source_events=source_events,
                confidence=confidence,
                dimension=dimension,
                source_engine=source_engine,
                privacy_level=privacy_level,
            )
            logger.info(
                "Created insight (DB): insight_id=%s, user_id=%s, dimension=%s, engine=%s",
                insight_id, user_id, dimension, source_engine,
            )
            return insight_id
        
        # 内存模式
        insight_id = f"ins_{uuid.uuid4().hex[:12]}"
        
        insight = MemoryInsight(
            insight_id=insight_id,
            user_id=user_id,
            source_events=source_events,
            summary=stored_summary,
            confidence=confidence,
            dimension=dimension,
            source_engine=source_engine,
            privacy_level=privacy_level,
        )
        
        with self._lock:
            self._insights[insight_id] = insight
        
        logger.info(
            "Created insight (memory): insight_id=%s, user_id=%s, dimension=%s, engine=%s",
            insight_id, user_id, dimension, source_engine,
        )
        
        return insight_id
    
    async def get_insights(
        self,
        user_id: str,
        dimension: Optional[str] = None,
        min_confidence: float = 0.0,
    ) -> List[MemoryInsight]:
        """
        获取用户洞察列表
        
        Args:
            user_id: 用户 ID
            dimension: 维度过滤
            min_confidence: 最低置信度
            
        Returns:
            洞察列表 (解密后)
        """
        if self._persist and self._repository:
            insights = await self._repository.get_insights(
                user_id=user_id,
                dimension=dimension,
                min_confidence=min_confidence,
            )
            # 解密
            return [
                MemoryInsight(
                    insight_id=i.insight_id,
                    user_id=i.user_id,
                    source_events=i.source_events,
                    summary=self._maybe_decrypt_str(i.summary, i.privacy_level),
                    confidence=i.confidence,
                    dimension=i.dimension,
                    source_engine=getattr(i, 'source_engine', None),
                    privacy_level=i.privacy_level,
                    created_at=i.created_at,
                )
                for i in insights
            ]
        
        # 内存模式
        results = []
        
        with self._lock:
            for insight in self._insights.values():
                if insight.user_id != user_id:
                    continue
                if dimension and insight.dimension != dimension:
                    continue
                if insight.confidence < min_confidence:
                    continue
                
                # 解密
                decrypted_summary = self._maybe_decrypt_str(
                    insight.summary, insight.privacy_level
                )
                results.append(MemoryInsight(
                    insight_id=insight.insight_id,
                    user_id=insight.user_id,
                    source_events=insight.source_events,
                    summary=decrypted_summary,
                    confidence=insight.confidence,
                    dimension=insight.dimension,
                    source_engine=insight.source_engine,
                    privacy_level=insight.privacy_level,
                    created_at=insight.created_at,
                ))
        
        return results
    
    # ==================== Profile 操作 ====================
    
    async def update_profile(
        self,
        user_id: str,
        traits: Optional[Dict[str, float]] = None,
        preferences: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        更新用户画像
        
        Args:
            user_id: 用户 ID
            traits: 特征更新
            preferences: 偏好更新
        """
        if self._persist and self._repository:
            await self._repository.update_profile(
                user_id=user_id,
                traits=traits,
                preferences=preferences,
            )
            logger.info("Updated profile (DB): user_id=%s", user_id)
            return
        
        # 内存模式
        with self._lock:
            profile = self._profiles.get(user_id)
            
            if profile is None:
                profile = UserProfile(
                    user_id=user_id,
                    traits={},
                    preferences={},
                )
            
            # 合并更新
            if traits:
                profile.traits.update(traits)
            if preferences:
                profile.preferences.update(preferences)
            
            profile.last_updated = datetime.utcnow()
            self._profiles[user_id] = profile
        
        logger.info("Updated profile (memory): user_id=%s", user_id)
    
    async def get_profile(self, user_id: str) -> Optional[UserProfile]:
        """
        获取用户画像
        
        Args:
            user_id: 用户 ID
            
        Returns:
            用户画像，不存在则返回 None
        """
        if self._persist and self._repository:
            return await self._repository.get_profile(user_id)
        
        with self._lock:
            return self._profiles.get(user_id)
    
    # ==================== 内部方法 ====================
    
    def _check_access(
        self,
        requester_id: str,
        owner_id: str,
        privacy_level: PrivacyLevel,
    ) -> None:
        """检查访问权限"""
        # 只有 owner 可以访问 PRIVATE 和 SENSITIVE
        if privacy_level in (PrivacyLevel.PRIVATE, PrivacyLevel.SENSITIVE):
            if requester_id != owner_id:
                raise AccessDeniedError(
                    f"Access denied: {privacy_level.value} data requires owner access"
                )
    
    def _maybe_encrypt(
        self,
        data: Dict[str, Any],
        privacy_level: PrivacyLevel,
    ) -> Dict[str, Any]:
        """按需加密字典数据"""
        if privacy_level != PrivacyLevel.SENSITIVE:
            return data
        
        if self._encryption is None:
            return data
        
        # 序列化后加密
        json_str = json.dumps(data, ensure_ascii=False, default=str)
        encrypted = self._encryption.encrypt(json_str)
        return {"__encrypted__": encrypted}
    
    def _maybe_decrypt(
        self,
        data: Dict[str, Any],
        privacy_level: PrivacyLevel,
    ) -> Dict[str, Any]:
        """按需解密字典数据"""
        if "__encrypted__" not in data:
            return data
        
        if self._encryption is None:
            return data
        
        encrypted = data["__encrypted__"]
        json_str = self._encryption.decrypt(encrypted)
        return json.loads(json_str)
    
    def _maybe_encrypt_str(
        self,
        text: str,
        privacy_level: PrivacyLevel,
    ) -> str:
        """按需加密字符串"""
        if privacy_level != PrivacyLevel.SENSITIVE:
            return text
        
        if self._encryption is None:
            return text
        
        return self._encryption.encrypt(text)
    
    def _maybe_decrypt_str(
        self,
        text: str,
        privacy_level: PrivacyLevel,
    ) -> str:
        """按需解密字符串"""
        if privacy_level != PrivacyLevel.SENSITIVE:
            return text
        
        if self._encryption is None:
            return text
        
        try:
            return self._encryption.decrypt(text)
        except Exception:
            # 可能未加密
            return text
    
    # 测试辅助方法
    def reset(self) -> None:
        """重置状态（用于测试）"""
        self._events.clear()
        self._insights.clear()
        self._profiles.clear()


# =============================================================================
# 便捷函数
# =============================================================================

_service: Optional[MemoryService] = None


def get_memory_service(persist: bool = True) -> MemoryService:
    """获取记忆服务单例"""
    global _service
    if _service is None:
        _service = MemoryService(persist=persist)
    return _service
