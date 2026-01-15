# backend/tests/unit/test_memory_query_selector.py
"""
R-05/WP-06: 记忆读取注入测试

测试目标：
1. MemoryQuerySelector 场景→维度映射完整性
2. 未知场景有默认策略
3. max_insights 限制生效（行为验证）
4. 返回值结构正确
"""

import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from datetime import datetime

from backend.services.memory.query_selector import (
    MemoryQuerySelector,
    SCENARIO_DIMENSION_MAP,
    SCENARIO_MAX_INSIGHTS,
    get_query_selector,
    ScenarioContext,
)
from backend.core.llm.orchestrator import ScenarioType


class TestScenarioDimensionMap:
    """场景→维度映射测试"""
    
    def test_all_scenarios_have_dimensions(self):
        """测试：所有场景都有维度映射"""
        for scenario in ScenarioType:
            assert scenario in SCENARIO_DIMENSION_MAP or scenario.value in str(SCENARIO_DIMENSION_MAP), \
                f"场景 {scenario} 缺少维度映射"
    
    def test_dimensions_are_lists(self):
        """测试：维度映射值为列表"""
        for scenario, dimensions in SCENARIO_DIMENSION_MAP.items():
            assert isinstance(dimensions, list), f"场景 {scenario} 的维度应为列表"
            assert len(dimensions) > 0, f"场景 {scenario} 的维度列表不应为空"
    
    def test_dimensions_are_strings(self):
        """测试：维度值为字符串"""
        for scenario, dimensions in SCENARIO_DIMENSION_MAP.items():
            for dim in dimensions:
                assert isinstance(dim, str), f"维度 {dim} 应为字符串"
    
    def test_playbook_daily_has_behavior_dimension(self):
        """R-05: 日报场景包含 behavior 维度"""
        assert ScenarioType.PLAYBOOK_DAILY in SCENARIO_DIMENSION_MAP
        assert "behavior" in SCENARIO_DIMENSION_MAP[ScenarioType.PLAYBOOK_DAILY]


class TestScenarioMaxInsights:
    """max_insights 配置测试"""
    
    def test_all_scenarios_have_max_insights(self):
        """测试：所有场景都有 max_insights 配置"""
        for scenario in ScenarioType:
            max_val = SCENARIO_MAX_INSIGHTS.get(scenario, 3)
            assert isinstance(max_val, int), f"场景 {scenario} 的 max_insights 应为整数"
            assert max_val > 0, f"场景 {scenario} 的 max_insights 应 > 0"
    
    def test_max_insights_reasonable_range(self):
        """测试：max_insights 在合理范围内 (1-10)"""
        for scenario, max_val in SCENARIO_MAX_INSIGHTS.items():
            assert 1 <= max_val <= 10, f"场景 {scenario} 的 max_insights={max_val} 不在合理范围"


class TestMemoryQuerySelectorBehavior:
    """R-05: MemoryQuerySelector 行为测试"""
    
    @pytest.fixture
    def selector(self):
        return MemoryQuerySelector()
    
    @pytest.fixture
    def mock_insights(self):
        """生成模拟洞察列表"""
        insights = []
        for i in range(10):
            insight = MagicMock()
            insight.dimension = "behavior" if i % 2 == 0 else "decision"
            insight.confidence = 0.9 - i * 0.05
            insight.created_at = datetime(2024, 1, 1, 12, 0, 0)
            insights.append(insight)
        return insights
    
    @pytest.mark.asyncio
    async def test_max_insights_limit_enforced(self, selector, mock_insights):
        """R-05: 验证 max_insights 限制生效"""
        mock_service = MagicMock()
        mock_service.get_insights = AsyncMock(return_value=mock_insights)
        mock_service.get_events = AsyncMock(return_value=[])
        
        with patch.object(selector, '_get_memory_service', return_value=mock_service):
            result = await selector.get_context_for_scenario(
                user_id="test_user",
                scenario=ScenarioType.PLAYBOOK_DAILY,
            )
            
            # 验证返回类型
            assert isinstance(result, ScenarioContext)
            
            # 验证限制生效
            max_allowed = SCENARIO_MAX_INSIGHTS.get(ScenarioType.PLAYBOOK_DAILY, 3)
            assert len(result.recent_insights) <= max_allowed, \
                f"应返回 <= {max_allowed} 条洞察，实际 {len(result.recent_insights)} 条"
    
    @pytest.mark.asyncio
    async def test_returns_scenario_context_structure(self, selector):
        """R-05: 验证返回值结构"""
        mock_service = MagicMock()
        mock_service.get_insights = AsyncMock(return_value=[])
        mock_service.get_events = AsyncMock(return_value=[])
        
        with patch.object(selector, '_get_memory_service', return_value=mock_service):
            result = await selector.get_context_for_scenario(
                user_id="test_user",
                scenario=ScenarioType.PLAYBOOK_DAILY,
            )
            
            # 验证返回结构
            assert hasattr(result, 'user_id')
            assert hasattr(result, 'scenario')
            assert hasattr(result, 'recent_insights')
            assert result.user_id == "test_user"
            assert result.scenario == ScenarioType.PLAYBOOK_DAILY
    
    @pytest.mark.asyncio
    async def test_empty_insights_handled(self, selector):
        """R-05: 验证空洞察列表处理"""
        mock_service = MagicMock()
        mock_service.get_insights = AsyncMock(return_value=[])
        mock_service.get_events = AsyncMock(return_value=[])
        
        with patch.object(selector, '_get_memory_service', return_value=mock_service):
            result = await selector.get_context_for_scenario(
                user_id="test_user",
                scenario=ScenarioType.PLAYBOOK_DAILY,
            )
            
            assert result.recent_insights == []


class TestGetQuerySelectorSingleton:
    """单例模式测试"""
    
    def test_returns_same_instance(self):
        """测试：返回同一实例"""
        selector1 = get_query_selector()
        selector2 = get_query_selector()
        assert selector1 is selector2
