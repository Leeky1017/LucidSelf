"""
Tests for Decision Score Calculator

对照文档: docs/ls_roadmap_executable.md §GAP-04
"""

from unittest.mock import MagicMock

import pytest

from backend.core.contracts.unified_dimensions import (
    AnalysisDimension,
    LifeDomain,
)
from backend.integration.decision_calculator import (
    ANALYSIS_TO_DECISION,
    DecisionScoreCalculator,
    DecisionScores,
)


class MockRuleResult:
    """模拟规则结果"""
    def __init__(self, dimension: str, score: float, matched: bool = True):
        self.dimension = dimension
        self.score = score
        self.matched = matched


class TestAnalysisToDecisionMapping:
    """ANALYSIS_TO_DECISION 映射测试"""
    
    def test_all_dimensions_have_mapping(self):
        """测试所有分析维度都有映射（可为空）"""
        for dim in AnalysisDimension:
            assert dim in ANALYSIS_TO_DECISION
    
    def test_career_dimension_maps_to_career_axes(self):
        """测试事业维度映射到事业决策轴"""
        career_axes = ANALYSIS_TO_DECISION[AnalysisDimension.CAREER]
        assert "income_ceiling" in career_axes
        assert "growth_potential" in career_axes
        assert "stability" in career_axes
    
    def test_marriage_dimension_maps_to_relationship_axes(self):
        """测试婚姻维度映射到感情决策轴"""
        marriage_axes = ANALYSIS_TO_DECISION[AnalysisDimension.MARRIAGE]
        assert "emotional_depth" in marriage_axes
        assert "compatibility" in marriage_axes
    
    def test_weights_in_valid_range(self):
        """测试所有权重在有效范围内"""
        for dim, axes in ANALYSIS_TO_DECISION.items():
            for axis_id, weight in axes.items():
                assert 0.0 <= weight <= 1.0, f"{dim.value}.{axis_id} weight out of range"


class TestDecisionScoreCalculator:
    """DecisionScoreCalculator 测试"""
    
    @pytest.fixture
    def calculator(self):
        return DecisionScoreCalculator()
    
    @pytest.fixture
    def career_rules(self):
        """模拟事业相关规则结果"""
        return [
            MockRuleResult("career", 0.8),
            MockRuleResult("career", 0.7),
            MockRuleResult("fortune", 0.6),
        ]
    
    @pytest.fixture
    def relationship_rules(self):
        """模拟感情相关规则结果"""
        return [
            MockRuleResult("marriage", 0.75),
            MockRuleResult("personality", 0.65),
        ]
    
    def test_calculate_returns_decision_scores(self, calculator, career_rules):
        """测试计算返回决策分数"""
        result = calculator.calculate(career_rules, LifeDomain.CAREER)
        
        assert isinstance(result, DecisionScores)
        assert result.domain == LifeDomain.CAREER
        assert len(result.scores) > 0
    
    def test_calculate_career_scores(self, calculator, career_rules):
        """测试事业场景分数计算"""
        result = calculator.calculate(career_rules, LifeDomain.CAREER)
        
        # 应该有事业相关的决策维度
        assert "income_ceiling" in result.scores
        assert "growth_potential" in result.scores
        
        # 分数应在有效范围内
        for axis_id, score in result.scores.items():
            assert 0.0 <= score <= 1.0
    
    def test_calculate_relationship_scores(self, calculator, relationship_rules):
        """测试感情场景分数计算"""
        result = calculator.calculate(relationship_rules, LifeDomain.RELATIONSHIP)
        
        assert "emotional_depth" in result.scores
        assert "compatibility" in result.scores
    
    def test_contributions_tracked(self, calculator, career_rules):
        """测试贡献追踪"""
        result = calculator.calculate(career_rules, LifeDomain.CAREER)
        
        # 应该记录贡献信息
        for axis_id, contrib in result.contributions.items():
            assert contrib.axis_id == axis_id
            assert isinstance(contrib.rule_count, int)
    
    def test_confidence_based_on_rule_count(self, calculator):
        """测试置信度基于规则数量"""
        # 少量规则 - 低置信度
        few_rules = [MockRuleResult("career", 0.8)]
        result_few = calculator.calculate(few_rules, LifeDomain.CAREER)
        
        # 多量规则 - 高置信度
        many_rules = [MockRuleResult("career", 0.8) for _ in range(15)]
        result_many = calculator.calculate(many_rules, LifeDomain.CAREER)
        
        assert result_few.confidence <= result_many.confidence
    
    def test_unmatched_rules_ignored(self, calculator):
        """测试未匹配规则被忽略"""
        rules = [
            MockRuleResult("career", 0.8, matched=True),
            MockRuleResult("career", 0.9, matched=False),  # 应被忽略
        ]
        result = calculator.calculate(rules, LifeDomain.CAREER)
        
        # 只有1条匹配规则
        total_count = sum(c.rule_count for c in result.contributions.values())
        assert total_count <= 6  # 1条规则最多影响6个维度
    
    def test_empty_rules_returns_default_scores(self, calculator):
        """测试空规则列表返回默认分数"""
        result = calculator.calculate([], LifeDomain.CAREER)
        
        # 应该有默认分数
        for axis_id, score in result.scores.items():
            assert score == 0.5  # 默认中等
    
    def test_get_domain_axes(self, calculator):
        """测试获取领域决策维度"""
        axes = calculator.get_domain_axes(LifeDomain.CAREER)
        assert len(axes) >= 5
        
        axis_ids = [a.axis_id for a in axes]
        assert "income_ceiling" in axis_ids
