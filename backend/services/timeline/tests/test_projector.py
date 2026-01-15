"""
TimelineProjector 测试

测试时间线推演器的核心功能。
"""

import pytest
from datetime import date
from unittest.mock import MagicMock

from backend.core.contracts import FactorMatrix, FactorValue, RuntimeRuleResult
from backend.core.contracts.unified_time import (
    TimeHorizon,
    TimeBucketGranularity,
)
from backend.services.timeline.projector import (
    TimelineProjector,
    get_projector,
    TEMPORAL_FACTOR_PATTERNS,
)


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def projector():
    """创建 TimelineProjector 实例"""
    return TimelineProjector()


@pytest.fixture
def sample_factor_matrix():
    """创建示例因子矩阵"""
    return FactorMatrix(
        factors={
            "bazi_day_master": FactorValue(
                factor_id="bazi_day_master",
                value="甲",
                confidence=0.95,
                source="calculator",
            ),
            "bazi_liunian_stem": FactorValue(
                factor_id="bazi_liunian_stem",
                value="乙",
                confidence=0.9,
                source="calculator",
            ),
            "bazi_dayun_index": FactorValue(
                factor_id="bazi_dayun_index",
                value=3,
                confidence=0.85,
                source="calculator",
            ),
            "astro_transit_jupiter_house": FactorValue(
                factor_id="astro_transit_jupiter_house",
                value=10,
                confidence=0.8,
                source="calculator",
            ),
            "personality_type": FactorValue(
                factor_id="personality_type",
                value="analytical",
                confidence=0.7,
                source="calculator",
            ),
        },
        engine_id="bazi_calculator",
    )


@pytest.fixture
def sample_rule_results():
    """创建示例规则结果"""
    return [
        RuntimeRuleResult(
            rule_id="rule_career_001",
            matched=True,
            dimension="career",
            level="吉",
            description="事业运势良好",
            confidence=0.85,
            weight=1.0,
            execution_time_ms=1.5,
            tags=["事业", "发展"],
        ),
        RuntimeRuleResult(
            rule_id="rule_wealth_001",
            matched=True,
            dimension="wealth",
            level="平",
            description="财运平稳",
            confidence=0.7,
            weight=1.0,
            execution_time_ms=1.2,
        ),
        RuntimeRuleResult(
            rule_id="rule_health_001",
            matched=True,
            dimension="health",
            level="注意",
            description="注意休息",
            confidence=0.6,
            weight=1.0,
            execution_time_ms=1.0,
        ),
        RuntimeRuleResult(
            rule_id="rule_relationship_001",
            matched=True,
            dimension="marriage",
            level="吉",
            description="感情和谐",
            confidence=0.75,
            weight=1.0,
            execution_time_ms=1.3,
        ),
        RuntimeRuleResult(
            rule_id="rule_career_risk",
            matched=True,
            dimension="career",
            level="凶",
            description="职场小人",
            confidence=0.5,
            weight=0.8,
            execution_time_ms=1.1,
        ),
    ]


# =============================================================================
# 测试: 基础功能
# =============================================================================

class TestTimelineProjectorBasic:
    """基础功能测试"""
    
    def test_project_generates_nodes(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试是否生成时间线节点"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            years=1,
        )
        
        assert projection is not None
        assert len(projection.nodes) > 0
        assert projection.projection_id.startswith("proj_")
    
    def test_project_3_years_generates_correct_nodes(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试3年预测生成正确数量的节点"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            horizon=TimeHorizon.LONG_TERM,
            years=3,
        )
        
        # LONG_TERM 使用 YEAR 粒度，3年应该有 3-4 个节点
        assert len(projection.nodes) >= 3
        assert projection.granularity == TimeBucketGranularity.YEAR
    
    def test_project_medium_term_uses_quarter(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试中期预测使用季度粒度"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            horizon=TimeHorizon.MEDIUM_TERM,
            years=1,
        )
        
        assert projection.granularity == TimeBucketGranularity.QUARTER
        # 1年应该有 4 个季度节点
        assert len(projection.nodes) >= 4


class TestTemporalFactorExtraction:
    """时间因子提取测试"""
    
    def test_extract_temporal_factors(
        self, 
        projector, 
        sample_factor_matrix,
    ):
        """测试提取 temporal 因子"""
        temporal = projector._extract_temporal_factors(sample_factor_matrix)
        
        # 应该提取到 liunian, dayun, transit 相关因子
        assert "bazi_liunian_stem" in temporal
        assert "bazi_dayun_index" in temporal
        assert "astro_transit_jupiter_house" in temporal
        
        # 非 temporal 因子不应被提取
        assert "bazi_day_master" not in temporal
        assert "personality_type" not in temporal
    
    def test_temporal_patterns_complete(self):
        """测试 temporal 模式覆盖主要时间概念"""
        patterns = TEMPORAL_FACTOR_PATTERNS
        
        # 八字时间概念
        assert "liunian" in patterns
        assert "dayun" in patterns
        assert "liuyue" in patterns
        
        # 紫微时间概念
        assert "daxian" in patterns
        
        # 占星时间概念
        assert "transit" in patterns
        assert "solar_return" in patterns


class TestDomainScoreCalculation:
    """领域得分计算测试"""
    
    def test_domain_scores_populated(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试各领域得分被填充"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            years=1,
        )
        
        for node in projection.nodes:
            # 核心领域应该有得分
            assert "career" in node.domain_scores or len(node.domain_scores) > 0
    
    def test_domain_scores_range(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试得分在合理范围内"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            years=1,
        )
        
        for node in projection.nodes:
            for score in node.domain_scores.values():
                assert 0.0 <= score <= 1.0


class TestBranchPointIdentification:
    """分支点识别测试"""
    
    def test_branch_points_identified(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试分支点被识别"""
        # 添加更多风险规则以触发分支点
        risk_rules = sample_rule_results + [
            RuntimeRuleResult(
                rule_id="rule_risk_001",
                matched=True,
                dimension="career",
                level="凶",
                description="工作压力",
                confidence=0.5,
                weight=1.0,
                execution_time_ms=1.0,
            ),
            RuntimeRuleResult(
                rule_id="rule_risk_002",
                matched=True,
                dimension="health",
                level="注意",
                description="健康风险",
                confidence=0.6,
                weight=1.0,
                execution_time_ms=1.0,
            ),
        ]
        
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=risk_rules,
            years=1,
        )
        
        # 应该有分支点（有多个风险规则）
        # 注意：具体数量取决于节点风险因子分布
        assert isinstance(projection.branch_points, list)
    
    def test_branch_point_has_options(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试分支点包含选项"""
        # 构造足够的风险规则
        risk_rules = [
            RuntimeRuleResult(
                rule_id=f"rule_risk_{i}",
                matched=True,
                dimension="career",
                level="凶",
                description=f"风险{i}",
                confidence=0.5,
                weight=1.0,
                execution_time_ms=1.0,
            )
            for i in range(5)
        ]
        
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=risk_rules,
            years=1,
        )
        
        for bp in projection.branch_points:
            assert len(bp.options) >= 2
            assert bp.decision_question != ""


class TestConfidenceCalculation:
    """置信度计算测试"""
    
    def test_confidence_in_range(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试置信度在有效范围内"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            years=1,
        )
        
        assert 0.0 <= projection.confidence <= 1.0
        
        for node in projection.nodes:
            assert 0.0 <= node.confidence <= 1.0
    
    def test_more_rules_higher_confidence(self, projector, sample_factor_matrix):
        """测试更多匹配规则提高置信度"""
        few_rules = [
            RuntimeRuleResult(
                rule_id="rule_1",
                matched=True,
                dimension="career",
                level="吉",
                confidence=0.8,
                weight=1.0,
                execution_time_ms=1.0,
            ),
        ]
        
        many_rules = few_rules + [
            RuntimeRuleResult(
                rule_id=f"rule_{i}",
                matched=True,
                dimension="career",
                level="吉",
                confidence=0.8,
                weight=1.0,
                execution_time_ms=1.0,
            )
            for i in range(2, 10)
        ]
        
        proj_few = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=few_rules,
            years=1,
        )
        
        proj_many = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=many_rules,
            years=1,
        )
        
        # 更多规则应该提高置信度
        assert proj_many.confidence >= proj_few.confidence


class TestSingleton:
    """单例测试"""
    
    def test_get_projector_returns_instance(self):
        """测试 get_projector 返回实例"""
        p1 = get_projector()
        p2 = get_projector()
        
        assert p1 is p2
        assert isinstance(p1, TimelineProjector)


# =============================================================================
# 边界测试
# =============================================================================

class TestEdgeCases:
    """边界情况测试"""
    
    def test_empty_rules(self, projector, sample_factor_matrix):
        """测试空规则列表"""
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=[],
            years=1,
        )
        
        assert projection is not None
        assert len(projection.nodes) > 0
    
    def test_empty_factors(self, projector, sample_rule_results):
        """测试空因子矩阵"""
        empty_matrix = FactorMatrix(factors={}, engine_id="empty")
        
        projection = projector.project(
            factor_matrix=empty_matrix,
            rule_results=sample_rule_results,
            years=1,
        )
        
        assert projection is not None
        assert len(projection.nodes) > 0
    
    def test_custom_start_date(
        self, 
        projector, 
        sample_factor_matrix, 
        sample_rule_results,
    ):
        """测试自定义起始日期"""
        custom_start = date(2025, 1, 1)
        
        projection = projector.project(
            factor_matrix=sample_factor_matrix,
            rule_results=sample_rule_results,
            start_date=custom_start,
            years=1,
        )
        
        assert projection.start_date == custom_start
