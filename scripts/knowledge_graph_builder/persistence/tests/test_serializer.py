"""
GraphSerializer测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.5, Req 8.1, Req 8.2, Req 8.3, Req 8.4, Req 8.5
Design Refs: Design.md#存储格式

Property 2: YAML Round-Trip Consistency
"""

import tempfile
from datetime import datetime
from pathlib import Path

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    ConflictSummary,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.edge import (
    ConflictType,
    RelationType,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)
from scripts.knowledge_graph_builder.persistence.serializer import (
    DeserializationError,
    GraphSerializer,
    LazyKnowledgeGraph,
    SerializationError,
)


# ============ Fixtures ============

@pytest.fixture
def sample_concept():
    """创建示例ConceptNode"""
    return ConceptNode(
        concept_id="concept_bazi_test_001",
        canonical_label_zh="测试概念",
        canonical_label_en="Test Concept",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        subdimension="流年运势",
        source_nodes=[
            SourceNodeRef(
                book_id="滴天髓",
                node_id="n_滴天髓_第1条_0",
                snippet_ids=["ns_dts_001", "ns_dts_002"],
            ),
            SourceNodeRef(
                book_id="子平真诠",
                node_id="n_子平真诠_甲木_1",
                snippet_ids=["ns_zpzq_001"],
            ),
        ],
        factor_refs=["bazi_day_master_jia", "bazi_season_spring"],
        authority_score=0.85,
        alignment_method="factor_overlap",
        confidence=0.9,
    )


@pytest.fixture
def sample_edge():
    """创建示例SemanticEdge"""
    return SemanticEdge(
        edge_id="edge_test_entails_001",
        source_concept_id="concept_bazi_source_001",
        target_concept_id="concept_bazi_target_001",
        relation_type=RelationType.ENTAILS,
        confidence=0.85,
        evidence_refs=["evi_001", "evi_002"],
    )


@pytest.fixture
def sample_conflict_edge():
    """创建带冲突类型的SemanticEdge"""
    return SemanticEdge(
        edge_id="edge_conflict_001",
        source_concept_id="concept_bazi_a_001",
        target_concept_id="concept_bazi_b_001",
        relation_type=RelationType.CONFLICTS_WITH,
        conflict_type=ConflictType.DIRECT_CONTRADICTION,
        confidence=0.75,
    )


@pytest.fixture
def sample_metadata():
    """创建示例GraphMetadata"""
    return GraphMetadata(
        version="1.0.0",
        build_timestamp=datetime(2025, 12, 4, 10, 0, 0),
        total_concepts=10,
        total_edges=5,
        books_included=["滴天髓", "子平真诠"],
        systems_covered=[DivinationSystem.BAZI, DivinationSystem.ASTRO],
        quality_metrics={"average_authority": 0.8, "conflict_ratio": 0.1},
        graph_status="valid",
        validation_passed=True,
    )


@pytest.fixture
def sample_graph(sample_concept, sample_edge, sample_metadata):
    """创建示例KnowledgeGraph"""
    concept2 = ConceptNode(
        concept_id="concept_bazi_target_001",
        canonical_label_zh="目标概念",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[
            SourceNodeRef(book_id="滴天髓", node_id="n_滴天髓_第2条_0", snippet_ids=[])
        ],
        factor_refs=["bazi_day_master_yi"],
        authority_score=0.75,
    )
    
    # 修改source_concept_id以匹配
    edge = SemanticEdge(
        edge_id="edge_test_001",
        source_concept_id=sample_concept.concept_id,
        target_concept_id=concept2.concept_id,
        relation_type=RelationType.ENTAILS,
        confidence=0.85,
    )
    
    return KnowledgeGraph(
        metadata=sample_metadata,
        concepts=[sample_concept, concept2],
        edges=[edge],
    )


@pytest.fixture
def serializer():
    """创建GraphSerializer"""
    return GraphSerializer()


# ============ 基础功能测试 ============

class TestGraphSerializer:
    """GraphSerializer基础测试"""
    
    def test_serialize_creates_files(self, serializer, sample_graph):
        """测试serialize生成三个YAML文件"""
        with tempfile.TemporaryDirectory() as tmpdir:
            concepts_path, edges_path, metadata_path = serializer.serialize(
                sample_graph, output_dir=tmpdir
            )
            
            assert concepts_path.exists()
            assert edges_path.exists()
            assert metadata_path.exists()
            
            assert concepts_path.name == "concepts.yaml"
            assert edges_path.name == "edges.yaml"
            assert metadata_path.name == "metadata.yaml"
    
    def test_deserialize_rebuilds_graph(self, serializer, sample_graph):
        """测试deserialize正确重建图谱"""
        with tempfile.TemporaryDirectory() as tmpdir:
            serializer.serialize(sample_graph, output_dir=tmpdir)
            restored = serializer.deserialize(input_dir=tmpdir)
            
            assert len(restored.concepts) == len(sample_graph.concepts)
            assert len(restored.edges) == len(sample_graph.edges)
            assert restored.metadata.version == sample_graph.metadata.version
    
    def test_round_trip_preserves_concept_ids(self, serializer, sample_graph):
        """测试往返后concept_id保持不变"""
        restored = serializer.round_trip(sample_graph)
        
        original_ids = {c.concept_id for c in sample_graph.concepts}
        restored_ids = {c.concept_id for c in restored.concepts}
        
        assert original_ids == restored_ids
    
    def test_round_trip_preserves_edge_ids(self, serializer, sample_graph):
        """测试往返后edge_id保持不变"""
        restored = serializer.round_trip(sample_graph)
        
        original_ids = {e.edge_id for e in sample_graph.edges}
        restored_ids = {e.edge_id for e in restored.edges}
        
        assert original_ids == restored_ids
    
    def test_round_trip_preserves_authority_score(self, serializer, sample_graph):
        """测试往返后authority_score保持不变"""
        restored = serializer.round_trip(sample_graph)
        
        for original in sample_graph.concepts:
            restored_concept = next(
                c for c in restored.concepts if c.concept_id == original.concept_id
            )
            assert abs(original.authority_score - restored_concept.authority_score) < 0.001
    
    def test_round_trip_preserves_factor_refs(self, serializer, sample_graph):
        """测试往返后factor_refs保持不变"""
        restored = serializer.round_trip(sample_graph)
        
        for original in sample_graph.concepts:
            restored_concept = next(
                c for c in restored.concepts if c.concept_id == original.concept_id
            )
            assert set(original.factor_refs) == set(restored_concept.factor_refs)
    
    def test_round_trip_preserves_source_nodes(self, serializer, sample_graph):
        """测试往返后source_nodes保持不变"""
        restored = serializer.round_trip(sample_graph)
        
        for original in sample_graph.concepts:
            restored_concept = next(
                c for c in restored.concepts if c.concept_id == original.concept_id
            )
            assert len(original.source_nodes) == len(restored_concept.source_nodes)
    
    def test_verify_round_trip_returns_true(self, serializer, sample_graph):
        """测试verify_round_trip返回True"""
        assert serializer.verify_round_trip(sample_graph) is True


# ============ 冲突边序列化测试 ============

class TestConflictEdgeSerialization:
    """冲突边序列化测试"""
    
    def test_conflict_edge_round_trip(self, serializer, sample_metadata):
        """测试冲突边的往返序列化"""
        concept_a = ConceptNode(
            concept_id="concept_bazi_a_001",
            canonical_label_zh="概念A",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[
                SourceNodeRef(book_id="滴天髓", node_id="n_001", snippet_ids=[])
            ],
        )
        concept_b = ConceptNode(
            concept_id="concept_bazi_b_001",
            canonical_label_zh="概念B",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[
                SourceNodeRef(book_id="子平真诠", node_id="n_002", snippet_ids=[])
            ],
        )
        conflict_edge = SemanticEdge(
            edge_id="edge_conflict_001",
            source_concept_id="concept_bazi_a_001",
            target_concept_id="concept_bazi_b_001",
            relation_type=RelationType.CONFLICTS_WITH,
            conflict_type=ConflictType.CONDITIONAL_EXCEPTION,
            confidence=0.7,
        )
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=[concept_a, concept_b],
            edges=[conflict_edge],
        )
        
        restored = serializer.round_trip(graph)
        restored_edge = restored.edges[0]
        
        assert restored_edge.relation_type == RelationType.CONFLICTS_WITH
        assert restored_edge.conflict_type == ConflictType.CONDITIONAL_EXCEPTION


# ============ 错误处理测试 ============

class TestSerializerErrorHandling:
    """序列化器错误处理测试"""
    
    def test_deserialize_missing_file(self, serializer):
        """测试反序列化缺失文件时抛出错误"""
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(DeserializationError) as exc_info:
                serializer.deserialize(input_dir=tmpdir)
            
            assert "not found" in str(exc_info.value)
    
    def test_deserialize_invalid_yaml(self, serializer):
        """测试反序列化无效YAML时抛出错误"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            
            # 创建无效YAML
            (tmppath / "concepts.yaml").write_text("invalid: yaml: content: [")
            (tmppath / "edges.yaml").write_text("[]")
            (tmppath / "metadata.yaml").write_text(
                "version: '1.0.0'\nbuild_timestamp: '2025-12-04T10:00:00'"
            )
            
            with pytest.raises(DeserializationError) as exc_info:
                serializer.deserialize(input_dir=tmpdir)
            
            assert "YAML" in str(exc_info.value) or "parse" in str(exc_info.value).lower()


# ============ 懒加载测试 ============

class TestLazyKnowledgeGraph:
    """懒加载图谱测试"""
    
    def test_lazy_load_metadata_only(self, serializer, sample_graph):
        """测试懒加载仅加载metadata"""
        with tempfile.TemporaryDirectory() as tmpdir:
            serializer.serialize(sample_graph, output_dir=tmpdir)
            
            lazy_graph = LazyKnowledgeGraph(serializer, tmpdir)
            
            # 初始状态：未加载
            assert lazy_graph.is_loaded() == (False, False, False)
            
            # 访问metadata
            _ = lazy_graph.metadata
            assert lazy_graph.is_loaded() == (True, False, False)
    
    def test_lazy_load_concepts_on_demand(self, serializer, sample_graph):
        """测试按需加载concepts"""
        with tempfile.TemporaryDirectory() as tmpdir:
            serializer.serialize(sample_graph, output_dir=tmpdir)
            
            lazy_graph = LazyKnowledgeGraph(serializer, tmpdir)
            
            # 访问concepts
            concepts = lazy_graph.concepts
            assert len(concepts) == len(sample_graph.concepts)
            assert lazy_graph.is_loaded()[1] is True  # concepts_loaded
    
    def test_lazy_load_to_graph(self, serializer, sample_graph):
        """测试转换为完整图谱"""
        with tempfile.TemporaryDirectory() as tmpdir:
            serializer.serialize(sample_graph, output_dir=tmpdir)
            
            lazy_graph = LazyKnowledgeGraph(serializer, tmpdir)
            full_graph = lazy_graph.to_graph()
            
            assert isinstance(full_graph, KnowledgeGraph)
            assert len(full_graph.concepts) == len(sample_graph.concepts)
            assert lazy_graph.is_loaded() == (True, True, True)


# ============ 分片测试 ============

class TestSharding:
    """分片功能测试"""
    
    def test_force_shard_creates_multiple_files(self, serializer, sample_graph):
        """测试强制分片创建多个文件"""
        with tempfile.TemporaryDirectory() as tmpdir:
            files = serializer.serialize_with_sharding(
                sample_graph, output_dir=tmpdir, force_shard=True
            )
            
            # 检查分片文件存在
            tmppath = Path(tmpdir)
            assert (tmppath / "metadata.yaml").exists()
            
            # 至少有一个concepts分片和一个edges分片
            concept_shards = list(tmppath.glob("concepts_*.yaml"))
            edge_shards = list(tmppath.glob("edges_*.yaml"))
            
            assert len(concept_shards) >= 1
            assert len(edge_shards) >= 1
    
    def test_sharded_round_trip(self, serializer, sample_graph):
        """测试分片存储的往返一致性"""
        with tempfile.TemporaryDirectory() as tmpdir:
            serializer.serialize_with_sharding(
                sample_graph, output_dir=tmpdir, force_shard=True
            )
            
            # 使用懒加载恢复
            lazy_graph = LazyKnowledgeGraph(serializer, tmpdir)
            restored = lazy_graph.to_graph()
            
            assert len(restored.concepts) == len(sample_graph.concepts)
            assert len(restored.edges) == len(sample_graph.edges)


# ============ Property测试 ============

class TestPropertyYAMLRoundTrip:
    """
    Property 2: YAML Round-Trip Consistency
    
    For any valid KnowledgeGraph instance, serializing to YAML and 
    deserializing back SHALL produce an equivalent graph where all 
    concept_ids, edge_ids, and cross-references are preserved without data loss.
    """
    
    @given(
        concept_suffix=st.text(
            alphabet="abcdefghijklmnopqrstuvwxyz0123456789_",
            min_size=1,
            max_size=20,
        ).filter(lambda x: x[0].isalpha()),
        authority_score=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        factor_count=st.integers(min_value=0, max_value=5),
    )
    @settings(max_examples=20, deadline=None)
    def test_property_round_trip_preserves_data(
        self,
        concept_suffix: str,
        authority_score: float,
        factor_count: int,
    ):
        """Property测试：往返序列化保持数据完整"""
        serializer = GraphSerializer()
        
        concept_id = f"concept_bazi_{concept_suffix}"
        factor_refs = [f"factor_{i}" for i in range(factor_count)]
        
        concept = ConceptNode(
            concept_id=concept_id,
            canonical_label_zh="测试概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.GENERAL,
            source_nodes=[
                SourceNodeRef(book_id="test_book", node_id="n_test_001", snippet_ids=[])
            ],
            factor_refs=factor_refs,
            authority_score=authority_score,
        )
        
        metadata = GraphMetadata(
            version="1.0.0",
            build_timestamp=datetime.now(),
        )
        
        graph = KnowledgeGraph(
            metadata=metadata,
            concepts=[concept],
            edges=[],
        )
        
        # 往返序列化
        restored = serializer.round_trip(graph)
        restored_concept = restored.concepts[0]
        
        # 验证数据保持
        assert restored_concept.concept_id == concept_id
        assert set(restored_concept.factor_refs) == set(factor_refs)
        assert abs(restored_concept.authority_score - authority_score) < 0.001
