"""
Performance Tests

性能和异步支持测试。

对照 tasks.md Task 11.2, 11.3
对照 Requirements 1.1.3, 6.1, 6.2
"""

import asyncio
import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult
from backend.integration import FusionEngine
from backend.integration.fusion_engine import fuse_results_async


class TestAsyncSupport:
    """异步支持测试"""
    
    @pytest.mark.asyncio
    async def test_fuse_results_async(self, fusion_engine, sample_results_multi_engine):
        """测试异步融合 (Requirement 6.2)"""
        fusion_result = await fuse_results_async(
            fusion_engine,
            sample_results_multi_engine,
        )
        
        assert fusion_result is not None
        assert len(fusion_result.contributing_engines) == 3
    
    @pytest.mark.asyncio
    async def test_fuse_results_async_with_weights(self, fusion_engine, sample_results_multi_engine):
        """测试带权重的异步融合"""
        user_weights = {"bazi-calculator": 2.0}
        
        fusion_result = await fuse_results_async(
            fusion_engine,
            sample_results_multi_engine,
            engine_weights=user_weights,
        )
        
        assert fusion_result is not None


class TestPerformance:
    """性能测试"""
    
    def test_fusion_time_under_threshold(self, fusion_engine, sample_results_multi_engine):
        """
        测试融合时间在阈值内
        
        Property P6: Performance Bound
        对照 Requirements 1.1.3, 6.1
        """
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        # 融合时间应该 <20ms
        assert fusion_result.fusion_time_ms < 20.0
    
    def test_fusion_time_recorded(self, fusion_engine, sample_results_multi_engine):
        """测试融合时间被记录 (Requirement 6.6)"""
        fusion_result = fusion_engine.fuse_results(sample_results_multi_engine)
        
        assert fusion_result.fusion_time_ms >= 0
        assert isinstance(fusion_result.fusion_time_ms, float)
    
    def test_large_input_performance(self, fusion_engine):
        """测试大输入量性能"""
        # 创建大量规则结果
        engine_ids = [
            "bazi-calculator",
            "astro-calculator",
            "ziwei-calculator",
            "tarot-interpreter",
            "dream-extractor",
        ]
        large_results = {
            engine_id: [
                RuntimeRuleResult(
                    rule_id=f"rule_{engine_id}_{j}",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                )
                for j in range(20)
            ]
            for engine_id in engine_ids
        }
        
        fusion_result = fusion_engine.fuse_results(large_results)
        
        # 即使大输入，融合时间也应该合理
        assert fusion_result.fusion_time_ms < 100.0
        assert len(fusion_result.contributing_engines) == 5


class TestPerformancePropertyTests:
    """性能属性测试"""
    
    @given(st.integers(min_value=1, max_value=50))
    @settings(max_examples=10)
    def test_fusion_time_scales_reasonably(self, num_results):
        """
        属性测试：融合时间随输入规模合理增长
        
        Property P6: Performance Bound
        """
        engine = FusionEngine()
        
        results = {
            "bazi-calculator": [
                RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                )
                for i in range(num_results)
            ]
        }
        
        fusion_result = engine.fuse_results(results)
        
        # 对于合理大小的输入，融合时间应该 <100ms
        assert fusion_result.fusion_time_ms < 100.0
