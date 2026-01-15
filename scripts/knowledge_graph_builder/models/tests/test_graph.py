"""
KnowledgeGraph模型测试

Feature: cross-book-knowledge-graph, Property 9: Query Traversal Depth Bound
Requirement Refs: Req 1.7, Req 4.5, Req 4.6
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.edge import (
    RelationType,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)


# ============ Fixtures ============

@pytest.fixture
def sample_metadata():
    """示例元数据"""
    return GraphMetadata(
        version="1.0.0",
        build_timestamp=datetime.now(),
    )


@pytest.fixture
def sample_concept():
    """示例概念节点"""
    return ConceptNode(
        concept_id="concept_bazi_daymaster_strong",
        canonical_label_zh="日主强旺",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.PERSONALITY,
        source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="node_001")],
        factor_refs=["bazi_daymaster", "bazi_strength"],
        authority_score=0.9,
    )


def create_concept(concept_id: str, system: DivinationSystem = DivinationSystem.BAZI,
                   factor_refs: list = None) -> ConceptNode:
    """创建测试概念的辅助函数"""
    return ConceptNode(
        concept_id=concept_id,
        canonical_label_zh=f"测试概念_{concept_id}",
        divination_system=system,
        source_nodes=[SourceNodeRef(book_id="test", node_id="node_001")],
        factor_refs=factor_refs or [],
    )


def create_edge(source_id: str, target_id: str, 
                relation: RelationType = RelationType.ENTAILS) -> SemanticEdge:
    """创建测试边的辅助函数"""
    return SemanticEdge(
        edge_id=f"edge_{source_id.split('_')[-1]}_{target_id.split('_')[-1]}",
        source_concept_id=source_id,
        target_concept_id=target_id,
        relation_type=relation,
    )


# ============ GraphMetadata Tests ============

class TestGraphMetadata:
    """GraphMetadata模型测试"""
    
    def test_valid_creation(self):
        """有效数据创建成功"""
        meta = GraphMetadata(
            version="1.0.0",
            build_timestamp=datetime.now(),
        )
        assert meta.version == "1.0.0"
        assert meta.graph_status == "valid"
    
    def test_invalid_version_format_rejected(self):
        """无效版本格式被拒绝"""
        with pytest.raises(ValidationError):
            GraphMetadata(
                version="1.0",  # 缺少patch版本
                build_timestamp=datetime.now(),
            )
    
    def test_default_values(self):
        """默认值正确"""
        meta = GraphMetadata(
            version="0.1.0",
            build_timestamp=datetime.now(),
        )
        assert meta.total_concepts == 0
        assert meta.total_edges == 0
        assert meta.books_included == []
        assert meta.systems_covered == []
        assert meta.quality_metrics == {}
        assert meta.graph_status == "valid"
        assert meta.last_validated_at is None
        assert meta.validation_passed is False


# ============ KnowledgeGraph Tests ============

class TestKnowledgeGraph:
    """KnowledgeGraph模型测试"""
    
    def test_empty_graph_creation(self, sample_metadata):
        """空图谱创建成功"""
        graph = KnowledgeGraph(metadata=sample_metadata)
        assert len(graph.concepts) == 0
        assert len(graph.edges) == 0
    
    def test_graph_with_concepts(self, sample_metadata, sample_concept):
        """带概念的图谱创建"""
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=[sample_concept],
        )
        assert len(graph.concepts) == 1
        assert graph.concepts[0].concept_id == "concept_bazi_daymaster_strong"
    
    def test_build_indices(self, sample_metadata):
        """索引构建测试"""
        concepts = [
            create_concept("concept_bazi_a", DivinationSystem.BAZI, ["factor_1", "factor_2"]),
            create_concept("concept_bazi_b", DivinationSystem.BAZI, ["factor_2", "factor_3"]),
            create_concept("concept_astro_c", DivinationSystem.ASTRO, ["factor_3"]),
        ]
        
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=concepts)
        
        # 验证concept_index
        assert graph.get_concept("concept_bazi_a") is not None
        assert graph.get_concept("concept_bazi_b") is not None
        assert graph.get_concept("concept_nonexistent") is None
    
    def test_query_by_factors(self, sample_metadata):
        """因子查询测试"""
        concepts = [
            create_concept("concept_bazi_a", factor_refs=["factor_1", "factor_2"]),
            create_concept("concept_bazi_b", factor_refs=["factor_2", "factor_3"]),
            create_concept("concept_bazi_c", factor_refs=["factor_4"]),
        ]
        
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=concepts)
        
        # 查询factor_2（应返回a和b）
        result = graph.query_by_factors(["factor_2"])
        assert len(result) == 2
        result_ids = {c.concept_id for c in result}
        assert "concept_bazi_a" in result_ids
        assert "concept_bazi_b" in result_ids
        
        # 查询factor_4（应返回c）
        result = graph.query_by_factors(["factor_4"])
        assert len(result) == 1
        assert result[0].concept_id == "concept_bazi_c"
        
        # 查询不存在的factor
        result = graph.query_by_factors(["factor_nonexistent"])
        assert len(result) == 0
    
    def test_query_by_dimension(self, sample_metadata):
        """维度查询测试"""
        c1 = create_concept("concept_bazi_a")
        c1.dimension = Dimension.CAREER
        c2 = create_concept("concept_bazi_b")
        c2.dimension = Dimension.CAREER
        c3 = create_concept("concept_bazi_c")
        c3.dimension = Dimension.HEALTH
        
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=[c1, c2, c3])
        
        career_concepts = graph.query_by_dimension(Dimension.CAREER)
        assert len(career_concepts) == 2
        
        health_concepts = graph.query_by_dimension(Dimension.HEALTH)
        assert len(health_concepts) == 1
    
    def test_query_by_system(self, sample_metadata):
        """体系查询测试"""
        concepts = [
            create_concept("concept_bazi_a", DivinationSystem.BAZI),
            create_concept("concept_bazi_b", DivinationSystem.BAZI),
            create_concept("concept_astro_c", DivinationSystem.ASTRO),
        ]
        
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=concepts)
        
        bazi_concepts = graph.query_by_system(DivinationSystem.BAZI)
        assert len(bazi_concepts) == 2
        
        astro_concepts = graph.query_by_system(DivinationSystem.ASTRO)
        assert len(astro_concepts) == 1
    
    def test_get_edges_from(self, sample_metadata):
        """出边获取测试"""
        concepts = [
            create_concept("concept_bazi_a"),
            create_concept("concept_bazi_b"),
            create_concept("concept_bazi_c"),
        ]
        edges = [
            create_edge("concept_bazi_a", "concept_bazi_b"),
            create_edge("concept_bazi_a", "concept_bazi_c"),
        ]
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=concepts,
            edges=edges,
        )
        
        edges_from_a = graph.get_edges_from("concept_bazi_a")
        assert len(edges_from_a) == 2
        
        edges_from_b = graph.get_edges_from("concept_bazi_b")
        assert len(edges_from_b) == 0
    
    def test_add_concept(self, sample_metadata):
        """添加概念测试"""
        graph = KnowledgeGraph(metadata=sample_metadata)
        
        concept = create_concept("concept_bazi_new", factor_refs=["factor_new"])
        graph.add_concept(concept)
        
        assert len(graph.concepts) == 1
        assert graph.get_concept("concept_bazi_new") is not None
        
        # 验证因子索引也更新了
        result = graph.query_by_factors(["factor_new"])
        assert len(result) == 1
    
    def test_add_edge(self, sample_metadata):
        """添加边测试"""
        concepts = [
            create_concept("concept_bazi_a"),
            create_concept("concept_bazi_b"),
        ]
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=concepts)
        
        edge = create_edge("concept_bazi_a", "concept_bazi_b")
        graph.add_edge(edge)
        
        assert len(graph.edges) == 1
        edges_from_a = graph.get_edges_from("concept_bazi_a")
        assert len(edges_from_a) == 1
    
    def test_update_metadata(self, sample_metadata):
        """元数据更新测试"""
        concepts = [
            create_concept("concept_bazi_a", DivinationSystem.BAZI),
            create_concept("concept_astro_b", DivinationSystem.ASTRO),
        ]
        edges = [create_edge("concept_bazi_a", "concept_astro_b")]
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=concepts,
            edges=edges,
        )
        graph.update_metadata()
        
        assert graph.metadata.total_concepts == 2
        assert graph.metadata.total_edges == 1
        assert len(graph.metadata.systems_covered) == 2


# ============ Traversal Tests ============

class TestGraphTraversal:
    """图遍历测试"""
    
    @pytest.fixture
    def chain_graph(self, sample_metadata):
        """
        创建链式图：A -> B -> C -> D
        """
        concepts = [
            create_concept("concept_bazi_a"),
            create_concept("concept_bazi_b"),
            create_concept("concept_bazi_c"),
            create_concept("concept_bazi_d"),
        ]
        edges = [
            create_edge("concept_bazi_a", "concept_bazi_b"),
            create_edge("concept_bazi_b", "concept_bazi_c"),
            create_edge("concept_bazi_c", "concept_bazi_d"),
        ]
        return KnowledgeGraph(metadata=sample_metadata, concepts=concepts, edges=edges)
    
    @pytest.fixture
    def star_graph(self, sample_metadata):
        """
        创建星形图：A -> B, A -> C, A -> D
        """
        concepts = [
            create_concept("concept_bazi_a"),
            create_concept("concept_bazi_b"),
            create_concept("concept_bazi_c"),
            create_concept("concept_bazi_d"),
        ]
        edges = [
            create_edge("concept_bazi_a", "concept_bazi_b"),
            create_edge("concept_bazi_a", "concept_bazi_c"),
            create_edge("concept_bazi_a", "concept_bazi_d"),
        ]
        return KnowledgeGraph(metadata=sample_metadata, concepts=concepts, edges=edges)
    
    def test_traverse_depth_1(self, chain_graph):
        """深度1遍历只返回直接邻居"""
        result = chain_graph.traverse_related("concept_bazi_a", depth=1)
        assert len(result) == 1
        assert result[0].concept_id == "concept_bazi_b"
    
    def test_traverse_depth_2(self, chain_graph):
        """深度2遍历返回2跳内的节点"""
        result = chain_graph.traverse_related("concept_bazi_a", depth=2)
        assert len(result) == 2
        result_ids = {c.concept_id for c in result}
        assert "concept_bazi_b" in result_ids
        assert "concept_bazi_c" in result_ids
    
    def test_traverse_depth_3(self, chain_graph):
        """深度3遍历返回3跳内的节点"""
        result = chain_graph.traverse_related("concept_bazi_a", depth=3)
        assert len(result) == 3
        result_ids = {c.concept_id for c in result}
        assert "concept_bazi_b" in result_ids
        assert "concept_bazi_c" in result_ids
        assert "concept_bazi_d" in result_ids
    
    def test_traverse_does_not_exceed_depth(self, chain_graph):
        """遍历不超过指定深度"""
        # 深度1时不应返回C和D
        result = chain_graph.traverse_related("concept_bazi_a", depth=1)
        result_ids = {c.concept_id for c in result}
        assert "concept_bazi_c" not in result_ids
        assert "concept_bazi_d" not in result_ids
    
    def test_traverse_star_graph(self, star_graph):
        """星形图遍历"""
        result = star_graph.traverse_related("concept_bazi_a", depth=1)
        assert len(result) == 3  # B, C, D都是直接邻居
    
    def test_traverse_nonexistent_start(self, chain_graph):
        """不存在的起始节点返回空列表"""
        result = chain_graph.traverse_related("concept_nonexistent", depth=1)
        assert len(result) == 0
    
    def test_traverse_with_relation_filter(self, sample_metadata):
        """带关系类型过滤的遍历"""
        concepts = [
            create_concept("concept_bazi_a"),
            create_concept("concept_bazi_b"),
            create_concept("concept_bazi_c"),
        ]
        edges = [
            create_edge("concept_bazi_a", "concept_bazi_b", RelationType.ENTAILS),
            create_edge("concept_bazi_a", "concept_bazi_c", RelationType.SYNONYM),
        ]
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=concepts, edges=edges)
        
        # 只遍历ENTAILS关系
        result = graph.traverse_related(
            "concept_bazi_a", 
            depth=1, 
            relation_types=[RelationType.ENTAILS]
        )
        assert len(result) == 1
        assert result[0].concept_id == "concept_bazi_b"
    
    def test_traverse_no_duplicates(self, sample_metadata):
        """
        遍历不返回重复节点
        图结构：A -> B, A -> C, B -> C
        """
        concepts = [
            create_concept("concept_bazi_a"),
            create_concept("concept_bazi_b"),
            create_concept("concept_bazi_c"),
        ]
        edges = [
            create_edge("concept_bazi_a", "concept_bazi_b"),
            create_edge("concept_bazi_a", "concept_bazi_c"),
            create_edge("concept_bazi_b", "concept_bazi_c"),
        ]
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=concepts, edges=edges)
        
        result = graph.traverse_related("concept_bazi_a", depth=2)
        result_ids = [c.concept_id for c in result]
        # C应该只出现一次
        assert result_ids.count("concept_bazi_c") == 1


# ============ Property-Based Testing ============

class TestGraphPropertyBased:
    """
    Property 9: Query Traversal Depth Bound
    使用hypothesis进行属性测试
    """
    
    @settings(max_examples=100)
    @given(depth=st.integers(min_value=0, max_value=10))
    def test_traverse_respects_depth_limit(self, depth):
        """验证遍历深度限制"""
        # 创建长链图
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        concepts = [create_concept(f"concept_bazi_{i}") for i in range(10)]
        edges = [
            create_edge(f"concept_bazi_{i}", f"concept_bazi_{i+1}")
            for i in range(9)
        ]
        graph = KnowledgeGraph(metadata=metadata, concepts=concepts, edges=edges)
        
        result = graph.traverse_related("concept_bazi_0", depth=depth)
        
        # 深度被限制在[1, 3]范围内
        effective_depth = max(1, min(3, depth))
        
        # 结果数量不应超过有效深度
        assert len(result) <= effective_depth
    
    @settings(max_examples=100)
    @given(depth=st.integers(min_value=1, max_value=3))
    def test_traverse_returns_nodes_within_depth(self, depth):
        """验证返回的节点都在指定深度内"""
        # 创建链图：0 -> 1 -> 2 -> 3 -> 4
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        concepts = [create_concept(f"concept_bazi_{i}") for i in range(5)]
        edges = [
            create_edge(f"concept_bazi_{i}", f"concept_bazi_{i+1}")
            for i in range(4)
        ]
        graph = KnowledgeGraph(metadata=metadata, concepts=concepts, edges=edges)
        
        result = graph.traverse_related("concept_bazi_0", depth=depth)
        
        # 验证返回的节点ID
        result_ids = {c.concept_id for c in result}
        
        # 深度d时应该返回节点1到d
        for i in range(1, depth + 1):
            if i < 5:  # 不超过图的大小
                assert f"concept_bazi_{i}" in result_ids
        
        # 不应返回超过深度的节点
        for i in range(depth + 1, 5):
            assert f"concept_bazi_{i}" not in result_ids
