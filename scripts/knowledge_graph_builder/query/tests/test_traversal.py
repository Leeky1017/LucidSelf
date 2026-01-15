"""
GraphTraversal测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 4.6, Req 4.7
"""

import pytest

from datetime import datetime

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    DivinationSystem,
    GraphMetadata,
    KnowledgeGraph,
    RelationType,
    SemanticEdge,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.query.traversal import GraphTraversal


def create_test_graph():
    """创建测试图谱"""
    concepts = [
        ConceptNode(
            concept_id=f"concept_{i}",
            canonical_label_zh=f"概念{i}",
            divination_system=DivinationSystem.BAZI,
            source_nodes=[SourceNodeRef(book_id="test", node_id=f"node_{i}")],
        )
        for i in range(5)
    ]
    
    # 创建边: 0 -> 1 -> 2 -> 3, 0 -> 4
    edges = [
        SemanticEdge(
            edge_id="edge_0_1",
            source_concept_id="concept_0",
            target_concept_id="concept_1",
            relation_type=RelationType.ENTAILS,
        ),
        SemanticEdge(
            edge_id="edge_1_2",
            source_concept_id="concept_1",
            target_concept_id="concept_2",
            relation_type=RelationType.ENTAILS,
        ),
        SemanticEdge(
            edge_id="edge_2_3",
            source_concept_id="concept_2",
            target_concept_id="concept_3",
            relation_type=RelationType.SPECIALIZES,
        ),
        SemanticEdge(
            edge_id="edge_0_4",
            source_concept_id="concept_0",
            target_concept_id="concept_4",
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


class TestGraphTraversal:
    """图遍历测试"""
    
    def test_bfs_depth_0(self):
        """深度0只返回起始节点"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.bfs_traverse("concept_0", max_depth=0)
        
        assert len(result.concepts) == 1
        assert result.concepts[0].concept_id == "concept_0"
    
    def test_bfs_depth_1(self):
        """深度1返回直接邻居"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.bfs_traverse("concept_0", max_depth=1)
        
        ids = {c.concept_id for c in result.concepts}
        assert "concept_0" in ids
        assert "concept_1" in ids
        assert "concept_4" in ids
        assert len(ids) == 3
    
    def test_bfs_depth_2(self):
        """深度2返回2跳内的节点"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.bfs_traverse("concept_0", max_depth=2)
        
        ids = {c.concept_id for c in result.concepts}
        assert "concept_0" in ids
        assert "concept_1" in ids
        assert "concept_2" in ids
        assert "concept_4" in ids
    
    def test_bfs_depth_capped_at_3(self):
        """深度最大为3"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.bfs_traverse("concept_0", max_depth=10)
        
        # 应该被限制在3
        assert result.max_depth_reached <= 3
    
    def test_bfs_with_relation_filter(self):
        """边类型过滤"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.bfs_traverse(
            "concept_0",
            max_depth=2,
            relation_types=[RelationType.ENTAILS],
        )
        
        ids = {c.concept_id for c in result.concepts}
        # 只能通过ENTAILS边遍历
        assert "concept_1" in ids
        assert "concept_2" in ids
        # concept_4通过COMPLEMENTS边连接，应被过滤
        assert "concept_4" not in ids
    
    def test_dfs_traverse(self):
        """DFS遍历"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.dfs_traverse("concept_0", max_depth=3)
        
        ids = {c.concept_id for c in result.concepts}
        # 应该能遍历到所有节点
        assert len(ids) == 5
    
    def test_find_path(self):
        """查找路径"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        path = traversal.find_path("concept_0", "concept_3", max_depth=3)
        
        assert path is not None
        assert path[0] == "concept_0"
        assert path[-1] == "concept_3"
    
    def test_find_path_not_found(self):
        """无路径"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        # concept_3没有出边
        path = traversal.find_path("concept_3", "concept_0", max_depth=3)
        
        assert path is None
    
    def test_get_neighbors(self):
        """获取直接邻居"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        neighbors = traversal.get_neighbors("concept_0")
        
        neighbor_ids = {n[0].concept_id for n in neighbors}
        assert neighbor_ids == {"concept_1", "concept_4"}
    
    def test_path_recorded(self):
        """路径记录"""
        graph = create_test_graph()
        traversal = GraphTraversal(graph)
        
        result = traversal.bfs_traverse("concept_0", max_depth=3)
        
        # 检查concept_3的路径
        path = result.paths.get("concept_3")
        assert path is not None
        assert path[0] == "concept_0"
        assert path[-1] == "concept_3"
