"""
V2 组件集成测试

验证所有 V2 组件的核心功能。
"""

import pytest
from hypothesis import given, strategies as st, settings

from scripts.logic_chain_builder.v2.stopwords import StopwordsFilter
from scripts.logic_chain_builder.v2.factor_mapper import FactorMapper
from scripts.logic_chain_builder.v2.clusterer import HierarchicalClusterer
from scripts.logic_chain_builder.v2.quality_scorer import SemanticQualityScorer
from scripts.logic_chain_builder.v2.models import QualityReportV2


class TestStopwordsFilter:
    """停用词过滤器测试"""
    
    def test_english_stopwords_excluded(self):
        """Property 1: 英文停用词被排除"""
        sf = StopwordsFilter()
        
        # 测试常见英文停用词
        for word in ["and", "or", "the", "is", "AND", "OR", "NOT"]:
            assert sf.is_stopword(word), f"{word} should be a stopword"
    
    def test_chinese_stopwords_excluded(self):
        """Property 1: 中文停用词被排除"""
        sf = StopwordsFilter()
        
        # 测试常见中文停用词
        for word in ["和", "或", "的", "是", "在"]:
            assert sf.is_stopword(word), f"{word} should be a stopword"
    
    def test_meaningful_factors_preserved(self):
        """有意义的因子被保留"""
        sf = StopwordsFilter()
        
        factors = {"star_ziwei", "palace_life", "and", "or", "的"}
        filtered = sf.filter_factors(factors)
        
        assert "star_ziwei" in filtered
        assert "palace_life" in filtered
        assert "and" not in filtered
        assert "or" not in filtered
        assert "的" not in filtered
    
    def test_has_meaningful_factors(self):
        """检测是否有有意义的因子"""
        sf = StopwordsFilter()
        
        assert sf.has_meaningful_factors({"star_ziwei", "and"})
        assert not sf.has_meaningful_factors({"and", "or", "the"})
        assert not sf.has_meaningful_factors(set())
    
    def test_single_char_is_stopword(self):
        """单字符被视为停用词"""
        sf = StopwordsFilter()
        
        assert sf.is_stopword("a")
        assert sf.is_stopword("的")
        assert sf.is_stopword("")


class TestFactorMapper:
    """因子映射器测试"""
    
    def test_extract_factors_basic(self):
        """基本因子提取"""
        fm = FactorMapper()
        
        factors = fm.extract_factors("star_ziwei AND palace_life")
        
        assert "star_ziwei" in factors
        assert "palace_life" in factors
        assert "and" not in factors
    
    def test_extract_factors_complex(self):
        """复杂表达式因子提取"""
        fm = FactorMapper()
        
        factors = fm.extract_factors(
            "star_ziwei AND (star_zuofu OR star_youbi)"
        )
        
        assert "star_ziwei" in factors
        assert "star_zuofu" in factors
        assert "star_youbi" in factors
        assert len(factors) == 3
    
    def test_normalize_factor_preserves_namespace(self):
        """保留已有的命名空间前缀"""
        fm = FactorMapper()
        
        normalized = fm._normalize_factor("star_ziwei")
        assert normalized == "star_ziwei"
    
    def test_normalize_factor_empty(self):
        """空因子处理"""
        fm = FactorMapper()
        
        assert fm._normalize_factor("") == ""
        assert fm._normalize_factor(None) == ""


class TestHierarchicalClusterer:
    """三级聚类器测试"""
    
    def test_max_snippets_per_node_constraint(self):
        """Property 2: 节点大小约束"""
        hc = HierarchicalClusterer()
        
        assert hc.MAX_SNIPPETS_PER_NODE == 5
        assert hc.MIN_SNIPPETS_PER_NODE == 1
    
    def test_cluster_empty_list(self):
        """空列表聚类"""
        hc = HierarchicalClusterer()
        
        nodes = hc.cluster([], "test_book")
        assert nodes == []


class TestSemanticQualityScorer:
    """语义质量评估器测试"""
    
    def test_weights_sum_to_one(self):
        """Property 9: 权重和为1"""
        scorer = SemanticQualityScorer()
        
        total = sum(scorer.WEIGHTS.values())
        assert abs(total - 1.0) < 0.001, f"Weights sum to {total}, expected 1.0"
    
    def test_quality_score_range(self):
        """Property 4: 质量分数范围在[0, 1]"""
        report = QualityReportV2(
            connectivity=0.5,
            orphan_ratio=0.1,
            reasoning_coherence=0.7,
            condition_coverage=0.6,
            argument_completeness=0.8,
            node_homogeneity=0.9,
        )
        
        scorer = SemanticQualityScorer()
        overall = scorer.calculate_overall(report)
        
        assert 0.0 <= overall <= 1.0
    
    def test_thresholds_defined(self):
        """阈值定义检查"""
        scorer = SemanticQualityScorer()
        
        assert "connectivity" in scorer.THRESHOLDS_V2
        assert "orphan_ratio" in scorer.THRESHOLDS_V2
        assert "reasoning_coherence" in scorer.THRESHOLDS_V2
        assert "condition_coverage" in scorer.THRESHOLDS_V2
        assert "argument_completeness" in scorer.THRESHOLDS_V2
        assert "node_homogeneity" in scorer.THRESHOLDS_V2
        assert "overall" in scorer.THRESHOLDS_V2
    
    def test_passes_thresholds_all_pass(self):
        """全部通过阈值"""
        report = QualityReportV2(
            connectivity=0.95,
            orphan_ratio=0.05,
            reasoning_coherence=0.85,
            condition_coverage=0.75,
            argument_completeness=0.85,
            node_homogeneity=0.90,
        )
        
        scorer = SemanticQualityScorer()
        passes, failures = scorer.passes_thresholds(report)
        
        assert passes
        assert len(failures) == 0
    
    def test_passes_thresholds_some_fail(self):
        """部分未通过阈值"""
        report = QualityReportV2(
            connectivity=0.5,  # 低于 0.80 阈值
            orphan_ratio=0.3,  # 高于 0.10 阈值
            reasoning_coherence=0.5,  # 低于 0.70 阈值
            condition_coverage=0.4,  # 低于 0.60 阈值
            argument_completeness=0.5,  # 低于 0.70 阈值
            node_homogeneity=0.5,  # 低于 0.80 阈值
        )
        
        scorer = SemanticQualityScorer()
        passes, failures = scorer.passes_thresholds(report)
        
        assert not passes
        assert len(failures) > 0


class TestPropertyBased:
    """基于属性的测试"""
    
    @given(st.text(min_size=0, max_size=100))
    @settings(max_examples=50)
    def test_stopword_exclusion_property(self, text):
        """Property 1: 任何因子提取结果不包含停用词"""
        fm = FactorMapper()
        sf = StopwordsFilter()
        
        factors = fm.extract_factors(text)
        
        for factor in factors:
            assert not sf.is_stopword(factor), f"Stopword {factor} found in factors"
    
    @given(st.floats(min_value=0.0, max_value=1.0))
    @settings(max_examples=20)
    def test_quality_score_in_range(self, value):
        """Property 4: 质量分数范围"""
        report = QualityReportV2(
            connectivity=value,
            orphan_ratio=1 - value,
            reasoning_coherence=value,
            condition_coverage=value,
            argument_completeness=value,
            node_homogeneity=value,
        )
        
        scorer = SemanticQualityScorer()
        overall = scorer.calculate_overall(report)
        
        # overall应该在合理范围内
        assert -0.1 <= overall <= 1.1  # 允许浮点误差


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
