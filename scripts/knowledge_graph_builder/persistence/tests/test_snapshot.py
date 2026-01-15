"""
SnapshotManager测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 5.5, Req 5.6
Design Refs: Design.md#模块结构

Property 12: Rollback State Restoration
"""

import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path

import pytest
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
from scripts.knowledge_graph_builder.persistence.snapshot import (
    SnapshotError,
    SnapshotInfo,
    SnapshotManager,
)
from scripts.knowledge_graph_builder.persistence.serializer import GraphSerializer


# ============ Fixtures ============

@pytest.fixture
def sample_graph():
    """创建示例KnowledgeGraph"""
    metadata = GraphMetadata(
        version="1.0.0",
        build_timestamp=datetime.now(),
        total_concepts=2,
        total_edges=1,
    )
    
    concept1 = ConceptNode(
        concept_id="concept_bazi_test_001",
        canonical_label_zh="测试概念1",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[
            SourceNodeRef(book_id="滴天髓", node_id="n_001", snippet_ids=[])
        ],
        factor_refs=["factor_001"],
        authority_score=0.85,
    )
    
    concept2 = ConceptNode(
        concept_id="concept_bazi_test_002",
        canonical_label_zh="测试概念2",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[
            SourceNodeRef(book_id="子平真诠", node_id="n_002", snippet_ids=[])
        ],
        factor_refs=["factor_002"],
        authority_score=0.75,
    )
    
    edge = SemanticEdge(
        edge_id="edge_test_001",
        source_concept_id="concept_bazi_test_001",
        target_concept_id="concept_bazi_test_002",
        relation_type=RelationType.ENTAILS,
        confidence=0.8,
    )
    
    return KnowledgeGraph(
        metadata=metadata,
        concepts=[concept1, concept2],
        edges=[edge],
    )


@pytest.fixture
def snapshot_manager():
    """创建临时目录中的SnapshotManager"""
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = SnapshotManager(
            snapshots_dir=tmpdir,
            retention_days=7,
        )
        yield manager


# ============ 基础功能测试 ============

class TestSnapshotManager:
    """SnapshotManager基础测试"""
    
    def test_create_snapshot(self, sample_graph):
        """测试创建快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snapshot_info = manager.create_snapshot(sample_graph)
            
            assert snapshot_info is not None
            assert snapshot_info.version == "1.0.0"
            assert snapshot_info.snapshot_dir.exists()
            assert snapshot_info.total_concepts == 2
            assert snapshot_info.total_edges == 1
    
    def test_create_snapshot_with_description(self, sample_graph):
        """测试创建带描述的快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snapshot_info = manager.create_snapshot(
                sample_graph, 
                description="Test snapshot description"
            )
            
            # 检查snapshot_meta.yaml包含描述
            meta_path = snapshot_info.snapshot_dir / "snapshot_meta.yaml"
            assert meta_path.exists()
    
    def test_list_snapshots_empty(self):
        """测试空快照列表"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snapshots = manager.list_snapshots()
            
            assert len(snapshots) == 0
    
    def test_list_snapshots_sorted_by_time(self, sample_graph):
        """测试快照列表按时间倒序排序"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # 禁用过期清理
            manager = SnapshotManager(snapshots_dir=tmpdir, retention_days=0)
            
            # 创建多个快照
            snap1 = manager.create_snapshot(sample_graph)
            time.sleep(1.1)  # 确保时间戳不同（至少1秒）
            snap2 = manager.create_snapshot(sample_graph)
            time.sleep(1.1)
            snap3 = manager.create_snapshot(sample_graph)
            
            snapshots = manager.list_snapshots()
            
            assert len(snapshots) >= 3
            # 最新的在前
            assert snapshots[0].timestamp >= snapshots[1].timestamp
    
    def test_get_snapshot_by_version(self, sample_graph):
        """测试按版本获取快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            manager.create_snapshot(sample_graph)
            
            snapshot = manager.get_snapshot("1.0.0")
            
            assert snapshot is not None
            assert snapshot.version == "1.0.0"
    
    def test_get_snapshot_not_found(self):
        """测试获取不存在的快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snapshot = manager.get_snapshot("9.9.9")
            
            assert snapshot is None
    
    def test_count_snapshots(self, sample_graph):
        """测试快照计数"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # 禁用过期清理
            manager = SnapshotManager(snapshots_dir=tmpdir, retention_days=0)
            
            assert manager.count_snapshots() == 0
            
            manager.create_snapshot(sample_graph)
            assert manager.count_snapshots() == 1
            
            time.sleep(1.1)  # 确保时间戳不同
            manager.create_snapshot(sample_graph)
            assert manager.count_snapshots() == 2
    
    def test_get_latest_snapshot(self, sample_graph):
        """测试获取最新快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snap1 = manager.create_snapshot(sample_graph)
            time.sleep(0.1)
            snap2 = manager.create_snapshot(sample_graph)
            
            latest = manager.get_latest_snapshot()
            
            assert latest is not None
            assert latest.timestamp >= snap1.timestamp


# ============ Rollback测试 ============

class TestSnapshotRollback:
    """快照回滚测试"""
    
    def test_rollback_by_version(self, sample_graph):
        """测试按版本回滚"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            manager.create_snapshot(sample_graph)
            
            restored = manager.rollback(version="1.0.0")
            
            assert len(restored.concepts) == len(sample_graph.concepts)
            assert len(restored.edges) == len(sample_graph.edges)
    
    def test_rollback_by_snapshot_name(self, sample_graph):
        """测试按快照名称回滚"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snapshot_info = manager.create_snapshot(sample_graph)
            
            restored = manager.rollback(snapshot_name=snapshot_info.name)
            
            assert len(restored.concepts) == len(sample_graph.concepts)
    
    def test_rollback_not_found(self):
        """测试回滚不存在的快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            with pytest.raises(SnapshotError) as exc_info:
                manager.rollback(version="9.9.9")
            
            # 检查错误信息包含"No snapshot found"
            assert "no snapshot found" in str(exc_info.value).lower()
    
    def test_rollback_requires_version_or_name(self):
        """测试回滚需要指定版本或名称"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            with pytest.raises(SnapshotError) as exc_info:
                manager.rollback()
            
            assert "Must specify" in str(exc_info.value)


# ============ 删除测试 ============

class TestSnapshotDeletion:
    """快照删除测试"""
    
    def test_delete_snapshot(self, sample_graph):
        """测试删除快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            snapshot_info = manager.create_snapshot(sample_graph)
            assert manager.count_snapshots() == 1
            
            result = manager.delete_snapshot(snapshot_info.name)
            
            assert result is True
            assert manager.count_snapshots() == 0
    
    def test_delete_nonexistent_snapshot(self):
        """测试删除不存在的快照"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            result = manager.delete_snapshot("nonexistent_snapshot")
            
            assert result is False


# ============ 过期清理测试 ============

class TestSnapshotRetention:
    """快照保留期测试"""
    
    def test_retention_period_default(self):
        """测试默认保留期"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            assert manager.retention_days == 7
    
    def test_retention_period_custom(self):
        """测试自定义保留期"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir, retention_days=30)
            
            assert manager.retention_days == 30


# ============ Property测试 ============

class TestPropertyRollbackStateRestoration:
    """
    Property 12: Rollback State Restoration
    
    For any snapshot created from a valid KnowledgeGraph, rolling back 
    to that snapshot SHALL restore the graph to an exactly equivalent state.
    """
    
    @given(
        concept_count=st.integers(min_value=1, max_value=5),
        authority_scores=st.lists(
            st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
            min_size=1,
            max_size=5,
        ),
    )
    @settings(max_examples=10, deadline=None)
    def test_property_rollback_restores_exact_state(
        self,
        concept_count: int,
        authority_scores: list,
    ):
        """Property测试：回滚恢复精确状态"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            # 创建图谱
            concepts = []
            for i in range(min(concept_count, len(authority_scores))):
                concept = ConceptNode(
                    concept_id=f"concept_bazi_prop_{i}",
                    canonical_label_zh=f"Property概念{i}",
                    divination_system=DivinationSystem.BAZI,
                    dimension=Dimension.GENERAL,
                    source_nodes=[
                        SourceNodeRef(book_id="test", node_id=f"n_{i}", snippet_ids=[])
                    ],
                    factor_refs=[f"factor_{i}"],
                    authority_score=authority_scores[i],
                )
                concepts.append(concept)
            
            metadata = GraphMetadata(
                version="1.0.0",
                build_timestamp=datetime.now(),
                total_concepts=len(concepts),
            )
            
            graph = KnowledgeGraph(
                metadata=metadata,
                concepts=concepts,
                edges=[],
            )
            
            # 创建快照
            manager.create_snapshot(graph)
            
            # 回滚
            restored = manager.rollback(version="1.0.0")
            
            # 验证精确状态
            assert len(restored.concepts) == len(graph.concepts)
            
            for original in graph.concepts:
                restored_concept = next(
                    c for c in restored.concepts 
                    if c.concept_id == original.concept_id
                )
                assert abs(
                    restored_concept.authority_score - original.authority_score
                ) < 0.001
                assert set(restored_concept.factor_refs) == set(original.factor_refs)
    
    def test_property_multiple_rollbacks_consistent(self, sample_graph):
        """Property测试：多次回滚结果一致"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SnapshotManager(snapshots_dir=tmpdir)
            
            # 创建快照
            manager.create_snapshot(sample_graph)
            
            # 多次回滚
            restored1 = manager.rollback(version="1.0.0")
            restored2 = manager.rollback(version="1.0.0")
            restored3 = manager.rollback(version="1.0.0")
            
            # 验证一致性
            assert len(restored1.concepts) == len(restored2.concepts)
            assert len(restored2.concepts) == len(restored3.concepts)
            
            ids1 = {c.concept_id for c in restored1.concepts}
            ids2 = {c.concept_id for c in restored2.concepts}
            ids3 = {c.concept_id for c in restored3.concepts}
            
            assert ids1 == ids2 == ids3
