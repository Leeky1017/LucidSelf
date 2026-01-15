"""
ConceptAligner测试

Feature: cross-book-knowledge-graph, Property 3: Alignment Similarity Threshold Enforcement
Feature: cross-book-knowledge-graph, Property 4: Same-System Alignment Priority
Requirement Refs: Req 2.2, Req 2.3, Req 2.6, Req 2.7
"""

import tempfile
from pathlib import Path

import pytest

from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.builders.alignment import (
    AlignmentCandidate,
    AlignmentThresholds,
    ConceptAligner,
    prioritize_alignments,
)
from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    DivinationSystem,
    SourceNodeRef,
)


# ============ Fixtures ============

def create_concept(
    concept_id: str,
    label: str,
    system: DivinationSystem,
    book_id: str,
    factor_refs: list,
) -> ConceptNode:
    """创建测试概念"""
    return ConceptNode(
        concept_id=concept_id,
        canonical_label_zh=label,
        divination_system=system,
        source_nodes=[SourceNodeRef(book_id=book_id, node_id="node_001")],
        factor_refs=factor_refs,
    )


@pytest.fixture
def sample_concepts():
    """示例概念列表"""
    return [
        create_concept(
            "concept_bazi_daymaster_strong",
            "日主强旺",
            DivinationSystem.BAZI,
            "滴天髓",
            ["bazi_daymaster", "bazi_strength", "bazi_fire"],
        ),
        create_concept(
            "concept_bazi_daymaster_weak",
            "日主弱势",
            DivinationSystem.BAZI,
            "子平真诠",
            ["bazi_daymaster", "bazi_weakness", "bazi_water"],
        ),
        create_concept(
            "concept_bazi_wealth",
            "财星为用",
            DivinationSystem.BAZI,
            "穷通宝鉴",
            ["bazi_wealth", "bazi_daymaster"],
        ),
        create_concept(
            "concept_astro_sun_strong",
            "太阳强势",
            DivinationSystem.ASTRO,
            "the_inner_sky",
            ["astro_sun", "astro_strength", "astro_fire"],
        ),
    ]


# ============ AlignmentThresholds Tests ============

class TestAlignmentThresholds:
    """对齐阈值测试"""
    
    def test_default_thresholds(self):
        """默认阈值"""
        thresholds = AlignmentThresholds()
        assert thresholds.factor_overlap_threshold == 0.7
        assert thresholds.text_similarity_threshold == 0.8
        assert thresholds.cross_system_threshold == 0.6
    
    def test_get_threshold_same_system(self):
        """同体系阈值"""
        thresholds = AlignmentThresholds(
            factor_overlap_threshold=0.7,
            cross_system_threshold=0.5,
        )
        assert thresholds.get_threshold(is_same_system=True) == 0.7
    
    def test_get_threshold_cross_system(self):
        """跨体系阈值"""
        thresholds = AlignmentThresholds(
            factor_overlap_threshold=0.7,
            cross_system_threshold=0.5,
        )
        assert thresholds.get_threshold(is_same_system=False) == 0.5


# ============ ConceptAligner Tests ============

class TestConceptAligner:
    """ConceptAligner测试"""
    
    def test_find_alignments_empty(self):
        """空概念列表"""
        aligner = ConceptAligner()
        candidates = aligner.find_alignments([])
        assert len(candidates) == 0
    
    def test_find_alignments_single_concept(self):
        """单个概念"""
        aligner = ConceptAligner()
        concept = create_concept(
            "concept_bazi_test",
            "测试",
            DivinationSystem.BAZI,
            "test",
            ["factor_a"],
        )
        candidates = aligner.find_alignments([concept])
        assert len(candidates) == 0
    
    def test_find_alignments_with_shared_factors(self, sample_concepts):
        """有共享因子的概念"""
        aligner = ConceptAligner(
            thresholds=AlignmentThresholds(
                factor_overlap_threshold=0.2,  # 低阈值以便匹配
                cross_system_threshold=0.1,
            )
        )
        candidates = aligner.find_alignments(sample_concepts)
        
        # 应该找到一些对齐候选（有共享的bazi_daymaster）
        assert len(candidates) > 0
    
    def test_compute_factor_overlap(self):
        """因子重叠计算"""
        aligner = ConceptAligner()
        
        # 完全重叠
        overlap = aligner._compute_factor_overlap(
            ["a", "b", "c"],
            ["a", "b", "c"],
        )
        assert overlap == 1.0
        
        # 无重叠
        overlap = aligner._compute_factor_overlap(
            ["a", "b"],
            ["c", "d"],
        )
        assert overlap == 0.0
        
        # 部分重叠
        overlap = aligner._compute_factor_overlap(
            ["a", "b", "c"],
            ["b", "c", "d"],
        )
        assert 0.4 < overlap < 0.6  # 2/4 = 0.5
    
    def test_compute_text_similarity(self):
        """文本相似度计算"""
        aligner = ConceptAligner()
        
        # 相同文本
        sim = aligner._compute_text_similarity("日主强旺", "日主强旺")
        assert sim == 1.0
        
        # 完全不同
        sim = aligner._compute_text_similarity("ABC", "XYZ")
        assert sim == 0.0
        
        # 部分相似
        sim = aligner._compute_text_similarity("日主强", "日主弱")
        assert 0.5 <= sim < 1.0  # 2/4 = 0.5
    
    def test_same_source_excluded(self):
        """同来源概念不对齐"""
        aligner = ConceptAligner()
        
        concepts = [
            create_concept(
                "concept_bazi_a",
                "概念A",
                DivinationSystem.BAZI,
                "滴天髓",
                ["factor_a", "factor_b"],
            ),
            create_concept(
                "concept_bazi_b",
                "概念B",
                DivinationSystem.BAZI,
                "滴天髓",  # 同一本书
                ["factor_a", "factor_b"],
            ),
        ]
        
        candidates = aligner.find_alignments(concepts)
        assert len(candidates) == 0
    
    def test_below_threshold_not_proposed(self):
        """低于阈值不提议对齐"""
        aligner = ConceptAligner(
            thresholds=AlignmentThresholds(
                factor_overlap_threshold=0.9,  # 高阈值
                cross_system_threshold=0.9,
            )
        )
        
        concepts = [
            create_concept(
                "concept_bazi_a",
                "概念A",
                DivinationSystem.BAZI,
                "book_a",
                ["factor_a", "factor_b", "factor_c"],
            ),
            create_concept(
                "concept_bazi_b",
                "概念B",
                DivinationSystem.BAZI,
                "book_b",
                ["factor_a"],  # 只有一个共享因子
            ),
        ]
        
        candidates = aligner.find_alignments(concepts)
        # 因为重叠率低于0.9，不应该有候选
        assert len(candidates) == 0


# ============ Prioritization Tests ============

class TestPrioritizeAlignments:
    """对齐优先级测试"""
    
    def test_same_system_priority(self):
        """同体系优先"""
        candidates = [
            AlignmentCandidate(
                concept_a_id="a1",
                concept_b_id="b1",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.ASTRO,
                is_same_system=False,
                confidence=0.9,
            ),
            AlignmentCandidate(
                concept_a_id="a2",
                concept_b_id="b2",
                book_a="book_a",
                book_b="book_c",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.7,  # 较低置信度
            ),
        ]
        
        prioritized = prioritize_alignments(candidates)
        
        # 同体系应该排在前面，尽管置信度较低
        assert prioritized[0].is_same_system is True
    
    def test_confidence_priority_within_system(self):
        """同体系内按置信度排序"""
        candidates = [
            AlignmentCandidate(
                concept_a_id="a1",
                concept_b_id="b1",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.7,
            ),
            AlignmentCandidate(
                concept_a_id="a2",
                concept_b_id="b2",
                book_a="book_a",
                book_b="book_c",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.9,
            ),
        ]
        
        prioritized = prioritize_alignments(candidates)
        
        # 高置信度应该排在前面
        assert prioritized[0].confidence == 0.9


# ============ Property-Based Testing ============

class TestAlignmentPropertyBased:
    """属性测试"""
    
    @settings(max_examples=100)
    @given(
        threshold=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
    )
    def test_below_threshold_not_proposed(self, threshold):
        """
        Property 3: Alignment Similarity Threshold Enforcement
        低于阈值的对齐不被提议
        """
        aligner = ConceptAligner(
            thresholds=AlignmentThresholds(
                factor_overlap_threshold=threshold,
                cross_system_threshold=threshold,
            )
        )
        
        # 创建只有很少共享因子的概念
        concepts = [
            create_concept(
                "concept_bazi_a",
                "概念A",
                DivinationSystem.BAZI,
                "book_a",
                ["factor_unique_a", "factor_shared"],
            ),
            create_concept(
                "concept_bazi_b",
                "概念B",
                DivinationSystem.BAZI,
                "book_b",
                ["factor_unique_b", "factor_shared"],
            ),
        ]
        
        candidates = aligner.find_alignments(concepts)
        
        # 每个候选的置信度都应该 >= 阈值
        for c in candidates:
            assert c.confidence >= threshold
    
    @settings(max_examples=100)
    @given(
        same_system_conf=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        cross_system_conf=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
    )
    def test_same_system_priority_property(self, same_system_conf, cross_system_conf):
        """
        Property 4: Same-System Alignment Priority
        同体系对齐排序优先
        """
        candidates = [
            AlignmentCandidate(
                concept_a_id="cross_a",
                concept_b_id="cross_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.ASTRO,
                is_same_system=False,
                confidence=cross_system_conf,
            ),
            AlignmentCandidate(
                concept_a_id="same_a",
                concept_b_id="same_b",
                book_a="book_a",
                book_b="book_c",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=same_system_conf,
            ),
        ]
        
        prioritized = prioritize_alignments(candidates)
        
        # 同体系的应该总是排在跨体系前面
        first_same_system_idx = next(
            (i for i, c in enumerate(prioritized) if c.is_same_system),
            len(prioritized)
        )
        first_cross_system_idx = next(
            (i for i, c in enumerate(prioritized) if not c.is_same_system),
            len(prioritized)
        )
        
        # 如果存在同体系候选，它应该在跨体系之前
        if first_same_system_idx < len(prioritized) and first_cross_system_idx < len(prioritized):
            assert first_same_system_idx < first_cross_system_idx
