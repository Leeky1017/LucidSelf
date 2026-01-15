"""
WeightManager Tests

权重管理器测试。

对照 tasks.md Task 1.4
对照 Requirements 1.2.1-1.2.4
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult
from backend.integration import WeightManager
from backend.integration.models import WeightedResult


class TestWeightManagerBasic:
    """WeightManager 基础测试"""
    
    def test_apply_weights_default(self, weight_manager, sample_rule_result):
        """测试默认权重应用"""
        results = {"test_engine": [sample_rule_result]}
        
        weighted = weight_manager.apply_weights(results)
        
        assert len(weighted) == 1
        assert isinstance(weighted[0], WeightedResult)
        assert weighted[0].engine_id == "test_engine"
        assert weighted[0].engine_weight == 1.0  # 默认权重
    
    def test_apply_user_weights(self, weight_manager, sample_rule_result):
        """测试用户自定义权重 (Requirement 1.2.2)"""
        results = {"test_engine": [sample_rule_result]}
        user_weights = {"test_engine": 2.5}
        
        weighted = weight_manager.apply_weights(results, user_weights)
        
        assert len(weighted) == 1
        assert weighted[0].engine_weight == 2.5
    
    def test_weight_clamping(self, weight_manager, sample_rule_result):
        """测试权重范围限制 (Requirement 1.2.1)"""
        results = {"test_engine": [sample_rule_result]}
        
        # 超出范围的权重
        user_weights = {"test_engine": 15.0}  # 超过 10.0
        weighted = weight_manager.apply_weights(results, user_weights)
        assert weighted[0].engine_weight == 10.0
        
        user_weights = {"test_engine": -5.0}  # 低于 0.0
        weighted = weight_manager.apply_weights(results, user_weights)
        assert weighted[0].engine_weight == 0.0
    
    def test_only_matched_results(self, weight_manager):
        """测试只处理匹配的结果"""
        matched = RuntimeRuleResult(
            rule_id="rule_1",
            matched=True,
            confidence=0.8,
            weight=1.0,
            tags=[],
            evidence_factors=[],
            execution_time_ms=1.0,
        )
        unmatched = RuntimeRuleResult(
            rule_id="rule_2",
            matched=False,
            confidence=0.8,
            weight=1.0,
            tags=[],
            evidence_factors=[],
            execution_time_ms=1.0,
        )
        results = {"test_engine": [matched, unmatched]}
        
        weighted = weight_manager.apply_weights(results)
        
        assert len(weighted) == 1
        assert weighted[0].result.rule_id == "rule_1"
    
    def test_final_score_calculation(self, weight_manager, sample_rule_result):
        """测试最终分数计算"""
        results = {"test_engine": [sample_rule_result]}
        user_weights = {"test_engine": 2.0}
        
        weighted = weight_manager.apply_weights(results, user_weights)
        
        # final_score 应该被归一化，所以不检查具体值
        assert weighted[0].final_score >= 0


class TestWeightNormalization:
    """权重归一化测试"""
    
    def test_normalization_sum_to_one(self, weight_manager):
        """
        测试归一化后总和为 1
        
        Property P2: Weight Normalization
        对照 Requirement 1.2.3
        """
        results = {
            "engine_a": [
                RuntimeRuleResult(
                    rule_id="rule_a",
                    matched=True,
                    confidence=0.8,
                    weight=1.5,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                )
            ],
            "engine_b": [
                RuntimeRuleResult(
                    rule_id="rule_b",
                    matched=True,
                    confidence=0.9,
                    weight=1.2,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                )
            ],
        }
        
        weighted = weight_manager.apply_weights(results)
        
        total_score = sum(wr.final_score for wr in weighted)
        assert abs(total_score - 1.0) < 0.001  # 允许浮点误差
    
    def test_empty_results_no_error(self, weight_manager):
        """测试空结果不报错"""
        results = {}
        weighted = weight_manager.apply_weights(results)
        assert weighted == []
    
    @given(st.lists(
        st.floats(min_value=0.1, max_value=1.0),
        min_size=2,
        max_size=10,
    ))
    @settings(max_examples=20)
    def test_normalization_property(self, confidences):
        """
        属性测试：归一化后分数总和为 1
        
        Property P2: Weight Normalization
        """
        manager = WeightManager()
        
        results = {
            "test_engine": [
                RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    confidence=conf,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                )
                for i, conf in enumerate(confidences)
            ]
        }
        
        weighted = manager.apply_weights(results)
        
        if weighted:
            total_score = sum(wr.final_score for wr in weighted)
            assert abs(total_score - 1.0) < 0.001
