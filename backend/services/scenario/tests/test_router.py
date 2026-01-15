"""
Tests for Scenario Router

对照文档: docs/ls_roadmap_executable.md §四、场景系统设计
"""

import pytest

from backend.core.contracts.unified_dimensions import LifeDomain
from backend.services.scenario.router import (
    DEFAULT_SCENARIO_KEYWORDS,
    ScenarioRouter,
)
from backend.services.scenario.models import (
    ScenarioContext,
    ScenarioRoutingResult,
)


class TestScenarioRouter:
    """ScenarioRouter 测试"""
    
    @pytest.fixture
    def router(self):
        return ScenarioRouter()
    
    def test_route_career_query(self, router):
        """测试事业相关问题路由"""
        result = router.route("我想换工作，今年的事业运怎么样？")
        assert isinstance(result, ScenarioRoutingResult)
        assert result.primary.domain == LifeDomain.CAREER
        assert result.primary.confidence > 0.3
        assert "工作" in result.primary.matched_keywords or "事业" in result.primary.matched_keywords
    
    def test_route_wealth_query(self, router):
        """测试财运相关问题路由"""
        result = router.route("今年财运如何？适合投资吗？")
        assert result.primary.domain == LifeDomain.WEALTH
        assert result.primary.confidence > 0.3
    
    def test_route_relationship_query(self, router):
        """测试感情相关问题路由"""
        result = router.route("我和男朋友最近总吵架，感情怎么发展？")
        assert result.primary.domain == LifeDomain.RELATIONSHIP
        assert result.primary.confidence > 0.3
    
    def test_route_health_query(self, router):
        """测试健康相关问题路由"""
        result = router.route("最近身体不太好，健康运势如何？")
        assert result.primary.domain == LifeDomain.HEALTH
        assert result.primary.confidence > 0.3
    
    def test_route_mixed_scenario(self, router):
        """测试混合场景识别"""
        result = router.route("想跳槽涨薪，事业和财运怎么看？")
        # 应该识别为事业，同时财运作为次要场景
        assert result.primary.domain in [LifeDomain.CAREER, LifeDomain.WEALTH]
        if result.secondary:
            assert result.secondary.domain in [LifeDomain.CAREER, LifeDomain.WEALTH]
    
    def test_route_low_confidence_fallback(self, router):
        """测试低置信度时的默认路由"""
        result = router.route("今天天气怎么样？")
        # 无明确场景应使用默认路由
        assert result.primary is not None
        assert result.primary.confidence <= 0.4
    
    def test_route_english_keywords(self, router):
        """测试英文关键词识别"""
        result = router.route("How is my career this year?")
        assert result.primary.domain == LifeDomain.CAREER
    
    def test_route_returns_alternatives(self, router):
        """测试返回备选场景"""
        result = router.route("事业财运感情健康都想看看")
        # 多关键词应产生多个备选
        assert len(result.alternatives) >= 1
    
    def test_routing_time_recorded(self, router):
        """测试记录路由时间"""
        result = router.route("事业运势")
        assert result.routing_time_ms >= 0
        assert result.routing_time_ms < 100  # 关键词匹配应该很快


class TestScenarioContext:
    """ScenarioContext 测试"""
    
    def test_context_has_decision_axes(self):
        """测试场景上下文包含决策维度"""
        router = ScenarioRouter()
        result = router.route("事业发展")
        assert len(result.primary.decision_axes) > 0
    
    def test_context_has_router_method(self):
        """测试场景上下文包含路由方法"""
        router = ScenarioRouter()
        result = router.route("财运")
        assert result.primary.router_method in ["keyword", "semantic", "llm", "default"]


class TestDefaultKeywords:
    """默认关键词配置测试"""
    
    def test_all_domains_have_keywords(self):
        """测试所有领域都有关键词配置"""
        for domain in LifeDomain:
            assert domain in DEFAULT_SCENARIO_KEYWORDS
            keywords = DEFAULT_SCENARIO_KEYWORDS[domain]
            assert len(keywords.primary) > 0
    
    def test_keywords_have_weights(self):
        """测试关键词有权重设置"""
        for domain, keywords in DEFAULT_SCENARIO_KEYWORDS.items():
            assert keywords.weight > 0
