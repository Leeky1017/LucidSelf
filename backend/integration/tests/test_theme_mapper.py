"""
ThemeMapper Tests

主题映射器测试。

对照 tasks.md Task 5.4, 5.6
对照 Requirements 3.1-3.5
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult
from backend.integration import ThemeMapper, WeightManager
from backend.integration.models import WeightedResult
from backend.rules.dimension import STANDARD_DIMENSIONS


class TestThemeMapperBasic:
    """ThemeMapper 基础测试"""
    
    def test_extract_themes_basic(self, theme_mapper):
        """测试基础主题提取"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.5,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.5,
            ),
        ]
        
        themes = theme_mapper.extract_themes(weighted)
        
        assert len(themes) >= 1
        assert "事业" in themes  # career 的中文标签
    
    def test_extract_themes_multi_dimension(self, theme_mapper):
        """测试多维度主题提取"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.5,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.3,
            ),
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_2",
                    matched=True,
                    dimension="wealth",
                    level="大吉",
                    confidence=0.9,
                    weight=2.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_b",
                engine_weight=1.0,
                final_score=0.7,
            ),
        ]
        
        themes = theme_mapper.extract_themes(weighted)
        
        assert len(themes) >= 2
        # wealth 分数更高，应该排在前面
        assert themes[0] == "财富"
    
    def test_extract_themes_empty_input(self, theme_mapper):
        """测试空输入"""
        themes = theme_mapper.extract_themes([])
        
        assert themes == []
    
    def test_themes_max_limit(self, theme_mapper):
        """
        测试主题数量限制
        
        Property P3: Theme Extraction Consistency
        对照 Requirement 3.1, 7.2
        """
        # 创建超过 5 个维度的结果
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    dimension=dim,
                    level="吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.1,
            )
            for i, dim in enumerate(STANDARD_DIMENSIONS)
        ]
        
        themes = theme_mapper.extract_themes(weighted)
        
        assert 1 <= len(themes) <= 5


class TestThemeMapperNormalization:
    """维度标准化测试"""
    
    def test_chinese_dimension_normalized(self, theme_mapper):
        """测试中文维度标准化"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="事业",  # 中文
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
        ]
        
        themes = theme_mapper.extract_themes(weighted)
        
        assert "事业" in themes
    
    def test_unknown_dimension_fallback(self, theme_mapper):
        """测试未知维度回退"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="unknown_dimension",
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
        ]
        
        themes = theme_mapper.extract_themes(weighted)
        
        # 应该回退到 general
        assert "通用" in themes


class TestThemeMapperDeduplication:
    """主题去重测试"""
    
    def test_no_duplicate_themes(self, theme_mapper):
        """测试主题去重 (Requirement 3.3)"""
        # 多个结果指向同一维度
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
                final_score=0.5,
            )
            for i in range(3)
        ]
        
        themes = theme_mapper.extract_themes(weighted)
        
        # 应该只有一个 "事业"
        assert themes.count("事业") == 1


class TestThemeMapperPropertyTests:
    """属性测试"""
    
    @given(st.lists(
        st.sampled_from(STANDARD_DIMENSIONS),
        min_size=1,
        max_size=15,
    ))
    @settings(max_examples=20)
    def test_themes_always_in_range(self, dimensions):
        """
        属性测试：主题数量总是在 [1, 5] 范围内
        
        Property P3: Theme Extraction Consistency
        """
        mapper = ThemeMapper()
        
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    dimension=dim,
                    level="吉",
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=1.0 / len(dimensions),
            )
            for i, dim in enumerate(dimensions)
        ]
        
        themes = mapper.extract_themes(weighted)
        
        assert 1 <= len(themes) <= 5
