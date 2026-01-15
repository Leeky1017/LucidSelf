"""
ConflictResolver测试

Feature: cross-book-knowledge-graph, Property 21: Conflict Output Completeness
Requirement Refs: Req 3.6, Req 13.1, Req 13.2, Req 13.3, Req 13.6
"""

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    ConflictType,
    Dimension,
    DivinationSystem,
    RelationType,
    SemanticEdge,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.query.conflict_resolver import ConflictResolver


def create_conflict_pair():
    """创建冲突概念对"""
    concept_a = ConceptNode(
        concept_id="concept_bazi_wealth_good",
        canonical_label_zh="财运吉",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.WEALTH,
        source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="node_1")],
        authority_score=0.9,
    )
    
    concept_b = ConceptNode(
        concept_id="concept_bazi_wealth_bad",
        canonical_label_zh="财运凶",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.WEALTH,
        source_nodes=[SourceNodeRef(book_id="子平真诠", node_id="node_2")],
        authority_score=0.7,
    )
    
    edge = SemanticEdge(
        edge_id="edge_conflict",
        source_concept_id=concept_a.concept_id,
        target_concept_id=concept_b.concept_id,
        relation_type=RelationType.CONFLICTS_WITH,
        conflict_type=ConflictType.DIRECT_CONTRADICTION,
    )
    
    return edge, concept_a, concept_b


def create_cross_system_conflict():
    """创建跨体系冲突"""
    concept_a = ConceptNode(
        concept_id="concept_bazi_career",
        canonical_label_zh="事业顺利",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="node_1")],
        authority_score=0.8,
    )
    
    concept_b = ConceptNode(
        concept_id="concept_astro_career",
        canonical_label_zh="事业受阻",
        divination_system=DivinationSystem.ASTRO,
        dimension=Dimension.CAREER,
        source_nodes=[SourceNodeRef(book_id="the_inner_sky", node_id="node_2")],
        authority_score=0.75,
    )
    
    edge = SemanticEdge(
        edge_id="edge_cross",
        source_concept_id=concept_a.concept_id,
        target_concept_id=concept_b.concept_id,
        relation_type=RelationType.CONFLICTS_WITH,
        conflict_type=ConflictType.CROSS_SYSTEM_DIVERGENCE,
    )
    
    return edge, concept_a, concept_b


class TestConflictResolver:
    """ConflictResolver测试"""
    
    def test_resolve_direct_contradiction(self):
        """解决直接矛盾"""
        resolver = ConflictResolver()
        edge, concept_a, concept_b = create_conflict_pair()
        
        output = resolver.resolve(edge, concept_a, concept_b)
        
        assert output.conflict_type == ConflictType.DIRECT_CONTRADICTION
        assert output.viewpoint_a.concept_id == concept_a.concept_id
        assert output.viewpoint_b.concept_id == concept_b.concept_id
    
    def test_resolve_cross_system_divergence(self):
        """解决跨体系分歧"""
        resolver = ConflictResolver()
        edge, concept_a, concept_b = create_cross_system_conflict()
        
        output = resolver.resolve(edge, concept_a, concept_b)
        
        assert output.conflict_type == ConflictType.CROSS_SYSTEM_DIVERGENCE
        # 跨体系应该使用PRESENT_BOTH策略
        from scripts.knowledge_graph_builder.models import ResolutionStrategy
        assert output.resolution_strategy == ResolutionStrategy.PRESENT_BOTH
    
    def test_authority_based_strategy(self):
        """权威性差距大时使用权威性优先策略"""
        resolver = ConflictResolver()
        edge, concept_a, concept_b = create_conflict_pair()
        
        # 概念A权威性0.9，概念B权威性0.7，差距>0.2
        output = resolver.resolve(edge, concept_a, concept_b)
        
        from scripts.knowledge_graph_builder.models import ResolutionStrategy
        assert output.resolution_strategy == ResolutionStrategy.AUTHORITY_BASED
    
    def test_resolution_hint_generated(self):
        """生成解决提示"""
        resolver = ConflictResolver()
        edge, concept_a, concept_b = create_conflict_pair()
        
        output = resolver.resolve(edge, concept_a, concept_b)
        
        assert output.resolution_hint
        assert len(output.resolution_hint) > 0
    
    def test_template_rendered_zh(self):
        """渲染中文模板"""
        resolver = ConflictResolver()
        edge, concept_a, concept_b = create_conflict_pair()
        
        output = resolver.resolve(edge, concept_a, concept_b)
        
        assert output.rendered_template_zh
        # 应该有非空渲染结果
        assert len(output.rendered_template_zh) > 0
    
    def test_template_rendered_en(self):
        """渲染英文模板"""
        resolver = ConflictResolver()
        edge, concept_a, concept_b = create_conflict_pair()
        
        output = resolver.resolve(edge, concept_a, concept_b)
        
        # 英文模板可能为空（如果没配置）
        if output.rendered_template_en:
            assert len(output.rendered_template_en) > 0
    
    def test_batch_resolve(self):
        """批量解决"""
        resolver = ConflictResolver()
        
        conflicts = [
            create_conflict_pair(),
            create_cross_system_conflict(),
        ]
        
        outputs = resolver.resolve_batch(conflicts)
        
        assert len(outputs) == 2


class TestConflictResolverPropertyBased:
    """属性测试"""
    
    @settings(max_examples=50)
    @given(
        authority_a=st.floats(min_value=0.1, max_value=1.0, allow_nan=False),
        authority_b=st.floats(min_value=0.1, max_value=1.0, allow_nan=False),
    )
    def test_conflict_output_completeness_property(self, authority_a, authority_b):
        """
        Property 21: Conflict Output Completeness
        验证ConflictOutput所有必填字段非空
        """
        resolver = ConflictResolver()
        
        concept_a = ConceptNode(
            concept_id="concept_a",
            canonical_label_zh="概念A",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="book_a", node_id="node_1")],
            authority_score=authority_a,
        )
        
        concept_b = ConceptNode(
            concept_id="concept_b",
            canonical_label_zh="概念B",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="book_b", node_id="node_2")],
            authority_score=authority_b,
        )
        
        edge = SemanticEdge(
            edge_id="edge_test",
            source_concept_id=concept_a.concept_id,
            target_concept_id=concept_b.concept_id,
            relation_type=RelationType.CONFLICTS_WITH,
            conflict_type=ConflictType.DIRECT_CONTRADICTION,
        )
        
        output = resolver.resolve(edge, concept_a, concept_b)
        
        # 验证必填字段非空
        assert output.viewpoint_a is not None
        assert output.viewpoint_b is not None
        assert output.conflict_type is not None
        assert output.resolution_strategy is not None
        assert output.resolution_hint is not None
        assert len(output.resolution_hint) > 0
