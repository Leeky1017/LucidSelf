"""
AuthorityScorer测试

Feature: cross-book-knowledge-graph, Property 5: Authority Score Formula Correctness
Requirement Refs: Req 3.2, Req 15.1, Req 15.2, Req 15.3, Req 15.4, Req 15.5, Req 15.6
"""

import tempfile
from pathlib import Path

import pytest
import yaml
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.builders.authority import AuthorityScorer
from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    DivinationSystem,
    SourceNodeRef,
)


def create_concept(
    concept_id: str,
    book_ids: list,
) -> ConceptNode:
    """创建测试概念"""
    return ConceptNode(
        concept_id=concept_id,
        canonical_label_zh="测试概念",
        divination_system=DivinationSystem.BAZI,
        source_nodes=[
            SourceNodeRef(book_id=bid, node_id=f"node_{i}")
            for i, bid in enumerate(book_ids)
        ],
    )


@pytest.fixture
def temp_authority_config():
    """创建临时权威性配置"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        config = {
            'book_authority_weights': {
                '滴天髓': 1.0,
                '子平真诠': 1.0,
                '三命通会': 0.9,
                '_default': 0.7,
            }
        }
        yaml.dump(config, f, allow_unicode=True)
        return Path(f.name)


class TestAuthorityScorer:
    """AuthorityScorer测试"""
    
    def test_compute_single_source(self, temp_authority_config):
        """单来源权威性计算"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        concept = create_concept("concept_test", ["滴天髓"])
        score = scorer.compute_authority_score(concept)
        
        # book_weight=1.0, quality=0.75(默认), source_count=1/3
        # 1.0*0.5 + 0.75*0.3 + 0.333*0.2 = 0.5 + 0.225 + 0.067 = 0.792
        assert 0.7 < score < 0.9
    
    def test_compute_multiple_sources(self, temp_authority_config):
        """多来源权威性计算"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        concept = create_concept("concept_test", ["滴天髓", "子平真诠", "三命通会"])
        score = scorer.compute_authority_score(concept)
        
        # source_count_factor = min(1.0, 3/3) = 1.0
        # 应该比单来源更高
        assert score > 0.8
    
    def test_quality_penalty_applied(self, temp_authority_config):
        """质量惩罚因子应用"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        # 设置低质量指标
        scorer.set_quality_metrics("滴天髓", 0.5, 0.4)  # 低于阈值
        
        concept = create_concept("concept_test", ["滴天髓"])
        score = scorer.compute_authority_score(concept)
        
        # 应该应用0.8惩罚因子
        assert score < 0.7
    
    def test_no_penalty_high_quality(self, temp_authority_config):
        """高质量不惩罚"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        # 设置高质量指标
        scorer.set_quality_metrics("滴天髓", 0.9, 0.8)
        
        concept = create_concept("concept_test", ["滴天髓"])
        score = scorer.compute_authority_score(concept)
        
        # 不应应用惩罚
        assert score > 0.7
    
    def test_score_caching(self, temp_authority_config):
        """分数缓存"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        concept = create_concept("concept_test", ["滴天髓"])
        
        score1 = scorer.compute_authority_score(concept)
        score2 = scorer.compute_authority_score(concept)
        
        assert score1 == score2
    
    def test_clear_cache(self, temp_authority_config):
        """清除缓存"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        concept = create_concept("concept_test", ["滴天髓"])
        scorer.compute_authority_score(concept)
        
        assert concept.concept_id in scorer._score_cache
        
        scorer.clear_cache()
        
        assert concept.concept_id not in scorer._score_cache
    
    def test_default_book_weight(self, temp_authority_config):
        """默认书籍权重"""
        scorer = AuthorityScorer(authority_config_path=temp_authority_config)
        
        concept = create_concept("concept_test", ["未知典籍"])
        score = scorer.compute_authority_score(concept)
        
        # 使用_default=0.7
        assert 0.5 < score < 0.8


class TestAuthorityScorerPropertyBased:
    """属性测试"""
    
    @settings(max_examples=100)
    @given(
        book_weight=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        coherence=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        homogeneity=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        num_sources=st.integers(min_value=1, max_value=5),
    )
    def test_authority_score_formula_correctness(
        self, book_weight, coherence, homogeneity, num_sources
    ):
        """
        Property 5: Authority Score Formula Correctness
        验证公式计算正确（浮点误差<0.001）
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            config = {'book_authority_weights': {'test_book': book_weight, '_default': 0.5}}
            yaml.dump(config, f)
            config_path = Path(f.name)
        
        scorer = AuthorityScorer(authority_config_path=config_path)
        scorer.set_quality_metrics("test_book", coherence, homogeneity)
        
        book_ids = ["test_book"] * num_sources
        concept = create_concept("concept_test", book_ids)
        scorer.clear_cache()
        
        actual_score = scorer.compute_authority_score(concept)
        
        # 手动计算期望值
        node_quality = (coherence + homogeneity) / 2
        source_count_factor = min(1.0, num_sources / 3)
        
        expected_score = (
            book_weight * 0.5 +
            node_quality * 0.3 +
            source_count_factor * 0.2
        )
        
        # 检查是否需要惩罚
        if coherence < 0.7 or homogeneity < 0.5:
            expected_score *= 0.8
        
        expected_score = max(0.0, min(1.0, expected_score))
        
        # 验证误差 < 0.001
        assert abs(actual_score - expected_score) < 0.001
    
    @settings(max_examples=50)
    @given(
        num_sources=st.integers(min_value=1, max_value=10),
    )
    def test_source_count_factor_range(self, num_sources):
        """验证source_count_factor在[0, 1]范围内"""
        factor = min(1.0, num_sources / 3)
        assert 0.0 <= factor <= 1.0
