"""
ConceptAggregator测试

Feature: cross-book-knowledge-graph, Property 18: Concept Aggregation Rule Application
Requirement Refs: Req 11.2, Req 11.3, Req 11.4, Req 11.6
"""

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.builders.aggregator import ConceptAggregator
from scripts.knowledge_graph_builder.builders.alignment import AlignmentCandidate
from scripts.knowledge_graph_builder.models import (
    AggregationStrategy,
    ConceptAggregationRule,
    ConceptNode,
    DivinationSystem,
    LabelSelectionStrategy,
    SourceNodeRef,
)


def create_concept(
    concept_id: str,
    label: str,
    authority: float,
    book_id: str,
    system: DivinationSystem = DivinationSystem.BAZI,
) -> ConceptNode:
    """创建测试概念"""
    return ConceptNode(
        concept_id=concept_id,
        canonical_label_zh=label,
        divination_system=system,
        source_nodes=[SourceNodeRef(book_id=book_id, node_id="node_001")],
        authority_score=authority,
    )


class TestConceptAggregator:
    """ConceptAggregator测试"""
    
    def test_no_alignments_no_merge(self):
        """无对齐时不合并"""
        aggregator = ConceptAggregator()
        concepts = [
            create_concept("concept_a", "概念A", 0.8, "book_a"),
            create_concept("concept_b", "概念B", 0.7, "book_b"),
        ]
        
        result = aggregator.aggregate_concepts(concepts, [])
        assert len(result) == 2
    
    def test_merge_aligned_concepts(self):
        """合并对齐的概念"""
        aggregator = ConceptAggregator()
        concepts = [
            create_concept("concept_a", "日主强旺", 0.9, "book_a"),
            create_concept("concept_b", "日主旺盛", 0.7, "book_b"),
        ]
        
        alignments = [
            AlignmentCandidate(
                concept_a_id="concept_a",
                concept_b_id="concept_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.8,
            )
        ]
        
        result = aggregator.aggregate_concepts(concepts, alignments)
        assert len(result) == 1
        # 合并后应有2个source_nodes
        assert len(result[0].source_nodes) == 2
    
    def test_highest_authority_label_selection(self):
        """最高权威性标签选择"""
        rule = ConceptAggregationRule(
            rule_id="rule_test",
            name="测试规则",
            label_selection_strategy=LabelSelectionStrategy.HIGHEST_AUTHORITY,
        )
        aggregator = ConceptAggregator(default_rule=rule)
        
        concepts = [
            create_concept("concept_a", "低权威标签", 0.5, "book_a"),
            create_concept("concept_b", "高权威标签", 0.9, "book_b"),
        ]
        
        alignments = [
            AlignmentCandidate(
                concept_a_id="concept_a",
                concept_b_id="concept_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.8,
            )
        ]
        
        result = aggregator.aggregate_concepts(concepts, alignments, rule)
        assert len(result) == 1
        assert result[0].canonical_label_zh == "高权威标签"
    
    def test_aggregation_rule_id_recorded(self):
        """聚合规则ID被记录"""
        rule = ConceptAggregationRule(
            rule_id="rule_custom",
            name="自定义规则",
        )
        aggregator = ConceptAggregator(default_rule=rule)
        
        concepts = [
            create_concept("concept_a", "概念A", 0.8, "book_a"),
            create_concept("concept_b", "概念B", 0.7, "book_b"),
        ]
        
        alignments = [
            AlignmentCandidate(
                concept_a_id="concept_a",
                concept_b_id="concept_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.8,
            )
        ]
        
        result = aggregator.aggregate_concepts(concepts, alignments, rule)
        assert result[0].aggregation_rule_id == "rule_custom"
    
    def test_highest_authority_only_strategy(self):
        """仅保留最高权威策略"""
        rule = ConceptAggregationRule(
            rule_id="rule_highest",
            name="最高权威规则",
            aggregation_strategy=AggregationStrategy.HIGHEST_AUTHORITY_ONLY,
        )
        aggregator = ConceptAggregator(default_rule=rule)
        
        concepts = [
            create_concept("concept_a", "低权威", 0.5, "book_a"),
            create_concept("concept_b", "高权威", 0.9, "book_b"),
        ]
        
        alignments = [
            AlignmentCandidate(
                concept_a_id="concept_a",
                concept_b_id="concept_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.8,
            )
        ]
        
        result = aggregator.aggregate_concepts(concepts, alignments, rule)
        assert len(result) == 1
        # 应该只有最高权威的来源
        assert len(result[0].source_nodes) == 1
        assert result[0].source_nodes[0].book_id == "book_b"
    
    def test_false_positive_not_merged(self):
        """假阳性不合并"""
        aggregator = ConceptAggregator()
        concepts = [
            create_concept("concept_a", "概念A", 0.8, "book_a"),
            create_concept("concept_b", "概念B", 0.7, "book_b"),
        ]
        
        alignments = [
            AlignmentCandidate(
                concept_a_id="concept_a",
                concept_b_id="concept_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.8,
                is_false_positive=True,  # 标记为假阳性
            )
        ]
        
        result = aggregator.aggregate_concepts(concepts, alignments)
        assert len(result) == 2  # 不应合并


class TestAggregatorPropertyBased:
    """属性测试"""
    
    @settings(max_examples=50)
    @given(
        authority_a=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        authority_b=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
    )
    def test_highest_authority_label_selection_property(self, authority_a, authority_b):
        """
        Property 18: Concept Aggregation Rule Application
        验证highest_authority策略选择正确的label
        """
        rule = ConceptAggregationRule(
            rule_id="rule_test",
            name="测试规则",
            label_selection_strategy=LabelSelectionStrategy.HIGHEST_AUTHORITY,
        )
        aggregator = ConceptAggregator(default_rule=rule)
        
        concepts = [
            create_concept("concept_a", "标签A", authority_a, "book_a"),
            create_concept("concept_b", "标签B", authority_b, "book_b"),
        ]
        
        alignments = [
            AlignmentCandidate(
                concept_a_id="concept_a",
                concept_b_id="concept_b",
                book_a="book_a",
                book_b="book_b",
                system_a=DivinationSystem.BAZI,
                system_b=DivinationSystem.BAZI,
                is_same_system=True,
                confidence=0.8,
            )
        ]
        
        result = aggregator.aggregate_concepts(concepts, alignments, rule)
        
        # 应该选择权威性更高的标签
        expected_label = "标签A" if authority_a >= authority_b else "标签B"
        assert result[0].canonical_label_zh == expected_label
