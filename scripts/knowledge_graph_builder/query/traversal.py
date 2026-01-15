"""
GraphTraversal - 图遍历算法

Feature: cross-book-knowledge-graph
Requirement Refs: Req 4.6, Req 4.7
Design Refs: Design.md#KnowledgeGraph.traverse_related
"""

import logging
from collections import deque
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    KnowledgeGraph,
    RelationType,
    SemanticEdge,
)

logger = logging.getLogger(__name__)


@dataclass
class TraversalStep:
    """遍历步骤"""
    concept_id: str
    depth: int
    path: List[str] = field(default_factory=list)
    edge_type: Optional[RelationType] = None


@dataclass
class TraversalResult:
    """遍历结果"""
    concepts: List[ConceptNode]
    paths: Dict[str, List[str]]  # concept_id -> path from start
    depths: Dict[str, int]  # concept_id -> depth
    edges_traversed: int
    max_depth_reached: int


class GraphTraversal:
    """
    图遍历器 - BFS/DFS实现
    
    支持：
    - BFS广度优先遍历（默认，更适合层级关系）
    - DFS深度优先遍历（可选）
    - depth限制（max=3）
    - relation_types过滤
    - visited集合避免重复
    """
    
    MAX_DEPTH = 3
    
    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph
        self._adjacency: Dict[str, List[Tuple[str, SemanticEdge]]] = {}
        self._build_adjacency()
    
    def _build_adjacency(self) -> None:
        """构建邻接表"""
        for edge in self.graph.edges:
            # 正向边
            if edge.source_concept_id not in self._adjacency:
                self._adjacency[edge.source_concept_id] = []
            self._adjacency[edge.source_concept_id].append(
                (edge.target_concept_id, edge)
            )
            
            # 如果是双向边，添加反向
            if edge.bidirectional:
                if edge.target_concept_id not in self._adjacency:
                    self._adjacency[edge.target_concept_id] = []
                self._adjacency[edge.target_concept_id].append(
                    (edge.source_concept_id, edge)
                )
    
    def bfs_traverse(
        self,
        start_concept_id: str,
        max_depth: int = 1,
        relation_types: Optional[List[RelationType]] = None,
        include_start: bool = False,
    ) -> TraversalResult:
        """
        BFS广度优先遍历
        
        Args:
            start_concept_id: 起始概念ID
            max_depth: 最大遍历深度 (1-3)
            relation_types: 限制遍历的边类型，None则不限制
            include_start: 是否在结果中包含起始节点，默认False（仅返回相关节点）
            
        Returns:
            TraversalResult: 遍历结果（不包含起始节点，除非include_start=True）
        """
        # 限制深度
        max_depth = min(max_depth, self.MAX_DEPTH)
        
        # 初始化
        visited: Set[str] = {start_concept_id}
        queue: deque[TraversalStep] = deque([
            TraversalStep(
                concept_id=start_concept_id,
                depth=0,
                path=[start_concept_id],
            )
        ])
        
        result_concepts: List[ConceptNode] = []
        paths: Dict[str, List[str]] = {start_concept_id: [start_concept_id]}
        depths: Dict[str, int] = {start_concept_id: 0}
        edges_traversed = 0
        max_depth_reached = 0
        
        # 获取起始概念 - only include if explicitly requested
        if include_start:
            start_concept = self._get_concept(start_concept_id)
            if start_concept:
                result_concepts.append(start_concept)
        
        # BFS遍历
        while queue:
            step = queue.popleft()
            
            if step.depth >= max_depth:
                continue
            
            # 获取邻居
            neighbors = self._adjacency.get(step.concept_id, [])
            
            for neighbor_id, edge in neighbors:
                # 检查边类型过滤
                if relation_types and edge.relation_type not in relation_types:
                    continue
                
                edges_traversed += 1
                
                # 跳过已访问
                if neighbor_id in visited:
                    continue
                
                visited.add(neighbor_id)
                new_depth = step.depth + 1
                new_path = step.path + [neighbor_id]
                
                # 记录路径和深度
                paths[neighbor_id] = new_path
                depths[neighbor_id] = new_depth
                max_depth_reached = max(max_depth_reached, new_depth)
                
                # 获取概念
                concept = self._get_concept(neighbor_id)
                if concept:
                    result_concepts.append(concept)
                
                # 加入队列继续遍历
                queue.append(TraversalStep(
                    concept_id=neighbor_id,
                    depth=new_depth,
                    path=new_path,
                    edge_type=edge.relation_type,
                ))
        
        return TraversalResult(
            concepts=result_concepts,
            paths=paths,
            depths=depths,
            edges_traversed=edges_traversed,
            max_depth_reached=max_depth_reached,
        )
    
    def dfs_traverse(
        self,
        start_concept_id: str,
        max_depth: int = 1,
        relation_types: Optional[List[RelationType]] = None,
        include_start: bool = False,
    ) -> TraversalResult:
        """
        DFS深度优先遍历
        
        Args:
            start_concept_id: 起始概念ID
            max_depth: 最大遍历深度 (1-3)
            relation_types: 限制遍历的边类型
            include_start: 是否在结果中包含起始节点，默认False
            
        Returns:
            TraversalResult: 遍历结果（不包含起始节点，除非include_start=True）
        """
        max_depth = min(max_depth, self.MAX_DEPTH)
        
        visited: Set[str] = set()
        result_concepts: List[ConceptNode] = []
        paths: Dict[str, List[str]] = {}
        depths: Dict[str, int] = {}
        edges_traversed = [0]  # 使用列表以便在递归中修改
        max_depth_reached = [0]
        
        def dfs(concept_id: str, depth: int, path: List[str], is_start: bool = False) -> None:
            if depth > max_depth or concept_id in visited:
                return
            
            visited.add(concept_id)
            current_path = path + [concept_id]
            paths[concept_id] = current_path
            depths[concept_id] = depth
            max_depth_reached[0] = max(max_depth_reached[0], depth)
            
            # Only add to results if not start node, or if include_start is True
            if not is_start or include_start:
                concept = self._get_concept(concept_id)
                if concept:
                    result_concepts.append(concept)
            
            neighbors = self._adjacency.get(concept_id, [])
            for neighbor_id, edge in neighbors:
                if relation_types and edge.relation_type not in relation_types:
                    continue
                
                edges_traversed[0] += 1
                
                if neighbor_id not in visited:
                    dfs(neighbor_id, depth + 1, current_path, is_start=False)
        
        dfs(start_concept_id, 0, [], is_start=True)
        
        return TraversalResult(
            concepts=result_concepts,
            paths=paths,
            depths=depths,
            edges_traversed=edges_traversed[0],
            max_depth_reached=max_depth_reached[0],
        )
    
    def find_path(
        self,
        start_id: str,
        end_id: str,
        max_depth: int = 3,
    ) -> Optional[List[str]]:
        """
        查找两个概念间的最短路径
        
        Args:
            start_id: 起始概念ID
            end_id: 目标概念ID
            max_depth: 最大搜索深度
            
        Returns:
            路径列表，如果不可达则返回None
        """
        if start_id == end_id:
            return [start_id]
        
        result = self.bfs_traverse(start_id, max_depth)
        return result.paths.get(end_id)
    
    def get_neighbors(
        self,
        concept_id: str,
        relation_types: Optional[List[RelationType]] = None,
    ) -> List[Tuple[ConceptNode, SemanticEdge]]:
        """
        获取直接邻居
        
        Args:
            concept_id: 概念ID
            relation_types: 限制边类型
            
        Returns:
            (概念, 边) 元组列表
        """
        neighbors = self._adjacency.get(concept_id, [])
        result = []
        
        for neighbor_id, edge in neighbors:
            if relation_types and edge.relation_type not in relation_types:
                continue
            
            concept = self._get_concept(neighbor_id)
            if concept:
                result.append((concept, edge))
        
        return result
    
    def _get_concept(self, concept_id: str) -> Optional[ConceptNode]:
        """从图谱获取概念"""
        # 使用图谱的索引（如果有）
        if hasattr(self.graph, '_concept_index') and self.graph._concept_index:
            return self.graph._concept_index.get(concept_id)
        
        # 线性查找（备用）
        for concept in self.graph.concepts:
            if concept.concept_id == concept_id:
                return concept
        return None
