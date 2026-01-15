"""
SemanticQueryService测试

Feature: cross-book-knowledge-graph, Property 7: Query Factor Matching
Requirement Refs: Req 4.1, Req 4.2, Req 4.3, Req 4.4, Req 4.5
"""

from datetime import datetime

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models import (
    BatchQueryRequest,
    ConceptNode,
    Dimension,
    DivinationSystem,
    GraphMetadata,
    KnowledgeGraph,
    RelationType,
    SemanticEdge,
    SemanticQuery,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.query.service import SemanticQueryService


def create_test_graph():
    """创建测试图谱"""
    concepts = [
        ConceptNode(
            concept_id="concept_bazi_wealth",
            canonical_label_zh="财运",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.WEALTH,
            source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="node_1")],
            factor_refs=["bazi_wealth", "bazi_daymaster"],
            authority_score=0.9,
        ),
        ConceptNode(
            concept_id="concept_bazi_career",
            canonical_label_zh="事业",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="子平真诠", node_id="node_2")],
            factor_refs=["bazi_career", "bazi_daymaster"],
            authority_score=0.8,
        ),
        ConceptNode(
            concept_id="concept_astro_career",
            canonical_label_zh="事业运势",
            divination_system=DivinationSystem.ASTRO,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="the_inner_sky", node_id="node_3")],
            factor_refs=["astro_sun", "astro_career"],
            authority_score=0.7,
        ),
    ]
    
    edges = [
        SemanticEdge(
            edge_id="edge_1",
            source_concept_id="concept_bazi_wealth",
            target_concept_id="concept_bazi_career",
            relation_type=RelationType.COMPLEMENTS,
        ),
    ]
    
    graph = KnowledgeGraph(
        concepts=concepts,
        edges=edges,
        metadata=GraphMetadata(version="1.0.0", build_timestamp=datetime.now()),
    )
    graph.build_indices()
    return graph


class TestSemanticQueryService:
    """SemanticQueryService测试"""
    
    def test_query_by_factors(self):
        """按因子查询"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        query = SemanticQuery(factor_ids=["bazi_daymaster"])
        result = service.query(query)
        
        # 应返回两个八字概念
        assert result.total_count == 2
        ids = {item.concept.concept_id for item in result.items}
        assert "concept_bazi_wealth" in ids
        assert "concept_bazi_career" in ids
    
    def test_query_by_dimension(self):
        """按维度过滤"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        query = SemanticQuery(dimension=Dimension.CAREER)
        result = service.query(query)
        
        assert result.total_count == 2
        for item in result.items:
            assert item.concept.dimension == Dimension.CAREER
    
    def test_query_by_system(self):
        """按体系过滤"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        query = SemanticQuery(divination_system=DivinationSystem.ASTRO)
        result = service.query(query)
        
        assert result.total_count == 1
        assert result.items[0].concept.divination_system == DivinationSystem.ASTRO
    
    def test_query_pagination(self):
        """分页"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        query = SemanticQuery(page=1, page_size=2)
        result = service.query(query)
        
        assert len(result.items) <= 2
        assert result.page == 1
        assert result.page_size == 2
    
    def test_query_authority_threshold(self):
        """权威性阈值"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        # 不使用遍历扩展，确保只返回满足阈值的概念
        query = SemanticQuery(authority_threshold=0.75, traversal_depth=0)
        result = service.query(query)
        
        for item in result.items:
            assert item.concept.authority_score >= 0.75
    
    def test_query_sorted_by_authority(self):
        """按权威性排序"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        query = SemanticQuery()
        result = service.query(query)
        
        scores = [item.concept.authority_score for item in result.items]
        assert scores == sorted(scores, reverse=True)
    
    def test_batch_query(self):
        """批量查询"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        request = BatchQueryRequest(
            queries=[
                SemanticQuery(factor_ids=["bazi_wealth"]),
                SemanticQuery(dimension=Dimension.CAREER),
            ]
        )
        
        result = service.batch_query(request)
        
        assert len(result.results) == 2
    
    def test_query_with_traversal(self):
        """带遍历的查询"""
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        query = SemanticQuery(
            factor_ids=["bazi_wealth"],
            traversal_depth=1,
        )
        result = service.query(query)
        
        # 应该包含concept_bazi_wealth和其邻居concept_bazi_career
        ids = {item.concept.concept_id for item in result.items}
        assert "concept_bazi_wealth" in ids
        assert "concept_bazi_career" in ids


class TestQueryServicePropertyBased:
    """属性测试"""
    
    @settings(max_examples=50)
    @given(
        factor_id=st.sampled_from(["bazi_wealth", "bazi_career", "bazi_daymaster", "astro_sun"]),
    )
    def test_query_factor_matching_property(self, factor_id):
        """
        Property 7: Query Factor Matching
        验证返回的概念都包含查询的factor_id（不使用遍历时）
        """
        graph = create_test_graph()
        service = SemanticQueryService(graph)
        
        # 不使用遍历扩展
        query = SemanticQuery(factor_ids=[factor_id], traversal_depth=0)
        result = service.query(query)
        
        for item in result.items:
            assert factor_id in item.concept.factor_refs
