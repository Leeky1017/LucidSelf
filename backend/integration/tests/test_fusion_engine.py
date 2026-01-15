"""
FusionEngine Tests

融合引擎单元测试和属性测试。

对照 tasks.md Task 1.7, 1.9
对照 Requirements 1.1.1-1.1.6, 7.1-7.6, 8.1, 8.5
"""

import re
import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult, FusionResult
from backend.integration import FusionEngine


class TestFusionEngineBasic:
    """FusionEngine 基础测试"""
    
    def test_fuse_single_engine(self, fusion_engine, sample_rule_result):
        """测试单引擎融合"""
        results = {"bazi-calculator": [sample_rule_result]}
        
        fusion_result = fusion_engine.fuse_results(results)
        
        assert isinstance(fusion_result, FusionResult)
        assert "bazi-calculator" in fusion_result.contributing_engines
        assert len(fusion_result.evidence_chain) >= 1
        assert len(fusion_result.primary_themes) >= 1
    
    def test_fuse_multi_engine(self, fusion_engine, sample_results_multi_engine):
        """测试多引擎融合 (Requirement 1.1.1)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert isinstance(fusion_result, FusionResult)
        assert len(fusion_result.contributing_engines) == 3
        assert "bazi-calculator" in fusion_result.contributing_engines
        assert "astro-calculator" in fusion_result.contributing_engines
        assert "tarot-interpreter" in fusion_result.contributing_engines
    
    def test_fuse_empty_input(self, fusion_engine):
        """测试空输入"""
        results = {}
        
        fusion_result = fusion_engine.fuse_results(results)
        
        assert isinstance(fusion_result, FusionResult)
        assert fusion_result.contributing_engines == []
        assert len(fusion_result.primary_themes) >= 1  # 默认主题
    
    def test_fusion_id_format(self, fusion_engine, sample_results_multi_engine):
        """测试 fusion_id 格式 (Requirement 7.1)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        # 格式: fus_[a-z0-9]{12}
        pattern = r"^fus_[a-f0-9]{12}$"
        assert re.match(pattern, fusion_result.fusion_id)
    
    def test_fusion_time_recorded(self, fusion_engine, sample_results_multi_engine):
        """测试融合时间记录 (Requirement 6.6)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert fusion_result.fusion_time_ms >= 0
        assert fusion_result.fusion_time_ms < 1000  # 应该很快
    
    def test_primary_themes_limit(self, fusion_engine, sample_results_multi_engine):
        """测试主题数量限制 (Requirement 7.2)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert 1 <= len(fusion_result.primary_themes) <= 5
    
    def test_evidence_chain_limit(self, fusion_engine, sample_results_multi_engine):
        """测试证据链数量限制 (Requirement 7.3)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert 1 <= len(fusion_result.evidence_chain) <= 20
    
    def test_cross_validation_score_bounds(self, fusion_engine, sample_results_multi_engine):
        """测试交叉验证分数边界 (Requirement 7.4)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert 0.0 <= fusion_result.cross_validation_score <= 1.0


class TestFusionEngineWithWeights:
    """带权重的融合测试"""
    
    def test_user_weights_applied(self, fusion_engine, sample_results_multi_engine):
        """测试用户权重应用 (Requirement 1.1.4)"""
        # 给 bazi 高权重
        user_weights = {
            "bazi-calculator": 5.0,
            "astro-calculator": 1.0,
            "tarot-interpreter": 0.5,
        }
        
        fusion_result = fusion_engine.fuse_results(
            sample_results_multi_engine,
            engine_weights=user_weights,
        )
        
        assert isinstance(fusion_result, FusionResult)
        # bazi 应该在证据链前面（因为权重高）
        assert len(fusion_result.evidence_chain) > 0
    
    def test_default_equal_weight(self, fusion_engine, sample_results_multi_engine):
        """测试默认等权融合 (Requirement 1.1.5)"""
        # 不传权重
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert isinstance(fusion_result, FusionResult)


class TestFusionEngineDeterminism:
    """融合确定性测试"""
    
    def test_same_input_same_output(self, fusion_engine, sample_results_multi_engine):
        """
        测试相同输入产生相同输出
        
        Property P1: Fusion Determinism
        对照 Requirements 1.1.2
        """
        result1 = fusion_engine.fuse_results(sample_results_multi_engine)
        result2 = fusion_engine.fuse_results(sample_results_multi_engine)
        
        # 主题应该相同
        assert result1.primary_themes == result2.primary_themes
        
        # 证据链应该相同（顺序和内容）
        assert len(result1.evidence_chain) == len(result2.evidence_chain)
        for e1, e2 in zip(result1.evidence_chain, result2.evidence_chain):
            assert e1.rule_id == e2.rule_id
        
        # 置信度矩阵应该相同
        assert result1.confidence_matrix == result2.confidence_matrix
        
        # 交叉验证分数应该相同
        assert result1.cross_validation_score == result2.cross_validation_score


class TestFusionEnginePropertyTests:
    """属性测试"""
    
    @given(st.lists(
        st.builds(
            RuntimeRuleResult,
            rule_id=st.text(min_size=5, max_size=20, alphabet="abcdefghijklmnopqrstuvwxyz0123456789_"),
            matched=st.just(True),
            dimension=st.sampled_from(["career", "wealth", "health", "marriage", "fortune"]),
            level=st.sampled_from(["大吉", "吉", "中等", "凶", "大凶"]),
            confidence=st.floats(min_value=0.0, max_value=1.0),
            weight=st.floats(min_value=0.0, max_value=10.0),
            tags=st.just([]),
            evidence_factors=st.just([]),
            execution_time_ms=st.floats(min_value=0.0, max_value=100.0),
        ),
        min_size=1,
        max_size=10,
    ))
    @settings(max_examples=20)
    def test_fusion_always_produces_valid_result(self, results_list):
        """
        属性测试：融合总是产生有效结果
        
        Property P1, P3, P5
        """
        engine = FusionEngine()
        results = {"bazi-calculator": results_list}
        
        fusion_result = engine.fuse_results(results)
        
        # P3: 主题数量在范围内
        assert 1 <= len(fusion_result.primary_themes) <= 5
        
        # P5: 交叉验证分数在范围内
        assert 0.0 <= fusion_result.cross_validation_score <= 1.0
        
        # 证据链在范围内
        assert len(fusion_result.evidence_chain) <= 20
