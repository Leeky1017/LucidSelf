# backend/services/memory/query_selector.py
"""
Memory Query Selector

按场景读取用户记忆上下文。

Phase 8 Task 8.1: 实现 MemoryQuerySelector
参考 tasks.md Phase 8 和 design.md §6.3
"""

import logging
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import List, Optional

from backend.core.llm import ScenarioType
from backend.services.memory.service import MemoryService, get_memory_service
from backend.services.memory.models import MemoryInsight

logger = logging.getLogger(__name__)


@dataclass
class ScenarioContext:
    """场景上下文"""
    user_id: str
    scenario: ScenarioType
    recent_insights: List[MemoryInsight] = field(default_factory=list)
    recent_events_count: int = 0
    target_date: Optional[date] = None


# 场景到洞察维度的映射
SCENARIO_DIMENSION_MAP = {
    # Playbook 场景 - 主要关注行为洞察
    ScenarioType.PLAYBOOK_DAILY: ["behavior"],
    ScenarioType.PLAYBOOK_WEEKLY: ["behavior", "decision"],
    ScenarioType.PLAYBOOK_MONTHLY: ["behavior", "decision", "emotion"],
    ScenarioType.PLAYBOOK_YEARLY: ["behavior", "decision", "emotion", "destiny"],
    
    # 梦境场景 - 关注梦境和情绪
    ScenarioType.DREAM: ["dream", "emotion"],
    
    # 人生版本 - 关注决策和命理
    ScenarioType.LIFE_VERSION: ["decision", "destiny"],
}

# 场景到最大洞察数的映射
SCENARIO_MAX_INSIGHTS = {
    ScenarioType.PLAYBOOK_DAILY: 3,
    ScenarioType.PLAYBOOK_WEEKLY: 5,
    ScenarioType.PLAYBOOK_MONTHLY: 5,
    ScenarioType.PLAYBOOK_YEARLY: 7,
    ScenarioType.DREAM: 3,
    ScenarioType.LIFE_VERSION: 5,
}


class MemoryQuerySelector:
    """
    记忆查询选择器
    
    按场景筛选用户记忆数据:
    - Playbook Daily: 只读取行为洞察
    - Playbook Weekly: 读取行为和决策洞察
    - Dream: 读取梦境和情绪洞察
    - Life Version: 读取决策和命理洞察
    """
    
    def __init__(self, memory_service: Optional[MemoryService] = None):
        """
        初始化
        
        Args:
            memory_service: 记忆服务实例，为 None 时自动获取
        """
        self._memory = memory_service
    
    def _get_memory_service(self) -> MemoryService:
        """获取记忆服务"""
        if self._memory is None:
            self._memory = get_memory_service()
        return self._memory
    
    async def get_context_for_scenario(
        self,
        user_id: str,
        scenario: ScenarioType,
        target_date: Optional[date] = None,
    ) -> ScenarioContext:
        """
        根据场景获取所需上下文
        
        Args:
            user_id: 用户 ID
            scenario: 场景类型
            target_date: 目标日期 (可选，默认今天)
            
        Returns:
            ScenarioContext 包含筛选后的洞察列表
        """
        memory_service = self._get_memory_service()
        
        # 获取场景配置
        dimensions = SCENARIO_DIMENSION_MAP.get(scenario, ["behavior"])
        max_insights = SCENARIO_MAX_INSIGHTS.get(scenario, 3)
        
        # 收集各维度的洞察
        all_insights: List[MemoryInsight] = []
        
        try:
            for dimension in dimensions:
                insights = await memory_service.get_insights(
                    user_id=user_id,
                    dimension=dimension,
                    min_confidence=0.5,
                )
                all_insights.extend(insights)
        except Exception as e:
            logger.warning(f"Failed to get insights for scenario {scenario}: {e}")
            # 降级返回空上下文
            return ScenarioContext(
                user_id=user_id,
                scenario=scenario,
                target_date=target_date,
            )
        
        # 按置信度和时间排序，取最近最相关的
        all_insights.sort(
            key=lambda i: (getattr(i, 'confidence', 0.5), getattr(i, 'created_at', datetime.min)),
            reverse=True
        )
        
        # 限制数量
        recent_insights = all_insights[:max_insights]
        
        # 获取事件计数 (用于判断用户活跃度)
        events_count = 0
        try:
            since = datetime.now() - timedelta(days=7)
            events = await memory_service.get_events(user_id=user_id, since=since, limit=100)
            events_count = len(events)
        except Exception:
            pass
        
        logger.debug(
            f"MemoryQuerySelector: user={user_id}, scenario={scenario}, "
            f"insights={len(recent_insights)}, events={events_count}"
        )
        
        return ScenarioContext(
            user_id=user_id,
            scenario=scenario,
            recent_insights=recent_insights,
            recent_events_count=events_count,
            target_date=target_date,
        )
    
    async def get_daily_context(self, user_id: str) -> ScenarioContext:
        """获取日 Playbook 上下文 (便捷方法)"""
        return await self.get_context_for_scenario(
            user_id=user_id,
            scenario=ScenarioType.PLAYBOOK_DAILY,
        )
    
    async def get_dream_context(self, user_id: str) -> ScenarioContext:
        """获取梦境场景上下文 (便捷方法)"""
        return await self.get_context_for_scenario(
            user_id=user_id,
            scenario=ScenarioType.DREAM,
        )


# 便捷函数
_selector: Optional[MemoryQuerySelector] = None


def get_query_selector() -> MemoryQuerySelector:
    """获取查询选择器单例"""
    global _selector
    if _selector is None:
        _selector = MemoryQuerySelector()
    return _selector
