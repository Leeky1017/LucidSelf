"""
CrossValidator Tests

交叉验证器测试。

对照 tasks.md Task 3.4, 3.7
对照 Requirements 2.1-2.5
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult
from backend.integration import CrossValidator, WeightManager
from backend.integration.models import WeightedResult


class TestCrossValidatorBasic:
    """CrossValidator 基础测试"""
    
    def test_validate_single_dimension_multi_engine(self, cross_validator):
        """测试单维度多引擎验证"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.5,
            ),
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_2",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.9,
                    weight=1.2,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_b",
                engine_weight=1.0,
                final_score=0.5,
            ),
        ]
        
        cv_score, confidence_matrix = cross_validator.validate(weighted)
        
        # 两个引擎给出相同级别，一致性应该高
        assert cv_score >= 0.8
        assert "career" in confidence_matrix
        assert confidence_matrix["career"] >= 0.8
    
    def test_validate_conflicting_levels(self, cross_validator):
        """测试冲突级别"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="career",
                    level="大吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.5,
            ),
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_2",
                    matched=True,
                    dimension="career",
                    level="大凶",
                    confidence=0.9,
                    weight=1.2,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_b",
                engine_weight=1.0,
                final_score=0.5,
            ),
        ]
        
        cv_score, confidence_matrix = cross_validator.validate(weighted)
        
        # 大吉 vs 大凶，一致性应该低
        assert cv_score <= 0.5
        assert confidence_matrix["career"] <= 0.5
    
    def test_validate_empty_input(self, cross_validator):
        """测试空输入"""
        cv_score, confidence_matrix = cross_validator.validate([])
        
        assert cv_score == 0.0
        assert confidence_matrix == {}
    
    def test_cv_score_bounds(self, cross_validator, sample_results_multi_engine):
        """
        测试交叉验证分数边界
        
        Property P5: Cross-Validation Bounds
        对照 Requirement 2.1, 7.4
        """
        weight_manager = WeightManager()
        weighted = weight_manager.apply_weights(sample_results_multi_engine)
        
        cv_score, _ = cross_validator.validate(weighted)
        
        assert 0.0 <= cv_score <= 1.0


class TestCrossValidatorConsistency:
    """一致性计算测试"""
    
    def test_perfect_consistency(self, cross_validator):
        """测试完美一致性"""
        # 所有引擎给出相同级别
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id=f"engine_{i}",
                engine_weight=1.0,
                final_score=0.25,
            )
            for i in range(4)
        ]
        
        cv_score, confidence_matrix = cross_validator.validate(weighted)
        
        assert cv_score == 1.0
        assert confidence_matrix["career"] == 1.0
    
    def test_high_confidence_dimensions(self, cross_validator):
        """测试高置信度维度标记 (Requirement 2.4)"""
        # 3 个引擎一致
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.9,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id=f"engine_{i}",
                engine_weight=1.0,
                final_score=0.33,
            )
            for i in range(3)
        ]
        
        high_conf_dims = cross_validator.get_high_confidence_dimensions(weighted)
        
        assert "career" in high_conf_dims
    
    def test_low_consistency_warnings(self, cross_validator):
        """测试低一致性警告 (Requirement 2.5)"""
        confidence_matrix = {
            "career": 0.9,
            "wealth": 0.3,  # 低一致性
            "health": 0.45,  # 低一致性
        }
        
        warnings = cross_validator.get_low_consistency_warnings(confidence_matrix)
        
        assert "wealth" in warnings
        assert "health" in warnings
        assert "career" not in warnings


class TestCrossValidatorPropertyTests:
    """属性测试"""
    
    @given(st.lists(
        st.sampled_from(["大吉", "吉", "中等", "凶", "大凶"]),
        min_size=2,
        max_size=10,
    ))
    @settings(max_examples=20)
    def test_consistency_always_in_bounds(self, levels):
        """
        属性测试：一致性分数总是在 [0, 1] 范围内
        
        Property P5: Cross-Validation Bounds
        """
        validator = CrossValidator()
        
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    dimension="career",
                    level=level,
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id=f"engine_{i}",
                engine_weight=1.0,
                final_score=1.0 / len(levels),
            )
            for i, level in enumerate(levels)
        ]
        
        cv_score, confidence_matrix = validator.validate(weighted)
        
        assert 0.0 <= cv_score <= 1.0
        for dim, conf in confidence_matrix.items():
            assert 0.0 <= conf <= 1.0
