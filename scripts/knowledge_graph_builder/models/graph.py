"""
KnowledgeGraph Pydantic模型 - 跨书知识图谱的完整图结构

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.7, Req 4.5, Req 4.6
Design Refs: Design.md#KnowledgeGraph
"""

from collections import deque
from datetime import datetime
from typing import Dict, List, Literal, Optional, Set

from pydantic import BaseModel, Field, PrivateAttr, field_validator

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
)
from scripts.knowledge_graph_builder.models.edge import (
    RelationType,
    SemanticEdge,
)


class GraphMetadata(BaseModel):
    """
    图谱元数据 - 记录图谱的构建信息和状态
    """
    version: str = Field(
        ..., 
        pattern=r"^\d+\.\d+\.\d+$",
        description="图谱版本，格式为major.minor.patch"
    )
    build_timestamp: datetime = Field(
        ...,
        description="构建时间戳"
    )
    total_concepts: int = Field(
        default=0,
        ge=0,
        description="概念节点总数"
    )
    total_edges: int = Field(
        default=0,
        ge=0,
        description="语义边总数"
    )
    books_included: List[str] = Field(
        default_factory=list,
        description="包含的典籍ID列表"
    )
    systems_covered: List[DivinationSystem] = Field(
        default_factory=list,
        description="覆盖的占卜体系"
    )
    quality_metrics: dict = Field(
        default_factory=dict,
        description="质量指标，如平均权威性分数、冲突比例等"
    )
    graph_status: Literal["valid", "invalid", "building"] = Field(
        default="valid",
        description="图谱状态"
    )
    last_validated_at: Optional[datetime] = Field(
        None,
        description="最后验证时间"
    )
    validation_passed: bool = Field(
        default=False,
        description="是否通过验证"
    )


class KnowledgeGraph(BaseModel):
    """
    知识图谱 - 完整的跨书知识网络
    
    KnowledgeGraph是跨书知识图谱的核心数据结构，包含：
    - 概念节点列表 (concepts)
    - 语义边列表 (edges)
    - 元数据 (metadata)
    - 运行时索引 (私有属性，用于高效查询)
    
    索引策略：
    1. _concept_index: concept_id -> ConceptNode (O(1)查找)
    2. _factor_index: factor_id -> List[ConceptNode] (倒排索引)
    3. _dimension_index: dimension -> List[ConceptNode]
    4. _system_index: divination_system -> List[ConceptNode]
    5. _edge_index: concept_id -> List[SemanticEdge] (邻接表)
    """
    
    metadata: GraphMetadata
    concepts: List[ConceptNode] = Field(default_factory=list)
    edges: List[SemanticEdge] = Field(default_factory=list)
    
    # 私有属性 - 运行时索引，不序列化
    _concept_index: Dict[str, ConceptNode] = PrivateAttr(default_factory=dict)
    _factor_index: Dict[str, List[ConceptNode]] = PrivateAttr(default_factory=dict)
    _dimension_index: Dict[str, List[ConceptNode]] = PrivateAttr(default_factory=dict)
    _system_index: Dict[str, List[ConceptNode]] = PrivateAttr(default_factory=dict)
    _edge_index: Dict[str, List[SemanticEdge]] = PrivateAttr(default_factory=dict)
    _indices_built: bool = PrivateAttr(default=False)
    
    def model_post_init(self, __context) -> None:
        """模型初始化后自动构建索引"""
        if self.concepts or self.edges:
            self.build_indices()
    
    def build_indices(self) -> None:
        """
        构建运行时索引 - 性能保障机制
        
        索引构建时间: O(n) where n = concepts + edges
        """
        # 清空旧索引
        self._concept_index = {}
        self._factor_index = {}
        self._dimension_index = {}
        self._system_index = {}
        self._edge_index = {}
        
        # 构建concept_index
        for concept in self.concepts:
            self._concept_index[concept.concept_id] = concept
        
        # 构建factor_index (倒排索引)
        for concept in self.concepts:
            for factor_id in concept.factor_refs:
                if factor_id not in self._factor_index:
                    self._factor_index[factor_id] = []
                self._factor_index[factor_id].append(concept)
        
        # 构建dimension_index
        for concept in self.concepts:
            dim_key = concept.dimension.value
            if dim_key not in self._dimension_index:
                self._dimension_index[dim_key] = []
            self._dimension_index[dim_key].append(concept)
        
        # 构建system_index
        for concept in self.concepts:
            sys_key = concept.divination_system.value
            if sys_key not in self._system_index:
                self._system_index[sys_key] = []
            self._system_index[sys_key].append(concept)
        
        # 构建edge_index (邻接表)
        for edge in self.edges:
            # 出边索引
            if edge.source_concept_id not in self._edge_index:
                self._edge_index[edge.source_concept_id] = []
            self._edge_index[edge.source_concept_id].append(edge)
            
            # 双向边也添加到目标节点的索引
            if edge.is_bidirectional():
                if edge.target_concept_id not in self._edge_index:
                    self._edge_index[edge.target_concept_id] = []
                # 创建反向引用（不是完整的反向边，只是引用）
                self._edge_index[edge.target_concept_id].append(edge)
        
        self._indices_built = True
    
    def get_concept(self, concept_id: str) -> Optional[ConceptNode]:
        """
        通过concept_id获取概念节点 - O(1)复杂度
        """
        if not self._indices_built:
            self.build_indices()
        return self._concept_index.get(concept_id)
    
    def query_by_factors(self, factor_ids: List[str]) -> List[ConceptNode]:
        """
        通过因子ID查询概念 - O(k)复杂度
        
        使用倒排索引实现高效查询，满足100ms性能要求
        
        Args:
            factor_ids: 要查询的factor_id列表
            
        Returns:
            匹配任一factor_id的概念列表（去重）
        """
        if not self._indices_built:
            self.build_indices()
        
        result_ids: Set[str] = set()
        for factor_id in factor_ids:
            if factor_id in self._factor_index:
                for concept in self._factor_index[factor_id]:
                    result_ids.add(concept.concept_id)
        
        return [self._concept_index[cid] for cid in result_ids if cid in self._concept_index]
    
    def query_by_dimension(self, dimension: Dimension) -> List[ConceptNode]:
        """通过维度查询概念"""
        if not self._indices_built:
            self.build_indices()
        return self._dimension_index.get(dimension.value, [])
    
    def query_by_system(self, system: DivinationSystem) -> List[ConceptNode]:
        """通过占卜体系查询概念"""
        if not self._indices_built:
            self.build_indices()
        return self._system_index.get(system.value, [])
    
    def get_edges_from(self, concept_id: str) -> List[SemanticEdge]:
        """获取从指定概念出发的所有边"""
        if not self._indices_built:
            self.build_indices()
        return self._edge_index.get(concept_id, [])
    
    def traverse_related(
        self,
        start_concept_id: str,
        depth: int = 1,
        relation_types: Optional[List[RelationType]] = None,
    ) -> List[ConceptNode]:
        """
        遍历相关概念 - BFS实现
        
        从起始概念出发，遍历指定深度内的相关概念。
        使用BFS确保按深度顺序返回，visited集合避免重复访问。
        
        Args:
            start_concept_id: 起始概念ID
            depth: 遍历深度，范围[1, 3]
            relation_types: 要遍历的关系类型，None表示所有类型
            
        Returns:
            在指定深度内可达的概念列表（不包含起始概念）
        """
        if not self._indices_built:
            self.build_indices()
        
        # 深度限制
        depth = max(1, min(3, depth))
        
        if start_concept_id not in self._concept_index:
            return []
        
        visited: Set[str] = {start_concept_id}
        result: List[ConceptNode] = []
        
        # BFS队列: (concept_id, current_depth)
        queue: deque = deque([(start_concept_id, 0)])
        
        while queue:
            current_id, current_depth = queue.popleft()
            
            # 已达到最大深度，不再扩展
            if current_depth >= depth:
                continue
            
            # 获取出边
            edges = self.get_edges_from(current_id)
            
            for edge in edges:
                # 过滤关系类型
                if relation_types is not None and edge.relation_type not in relation_types:
                    continue
                
                # 确定目标节点
                if edge.source_concept_id == current_id:
                    target_id = edge.target_concept_id
                else:
                    # 双向边从target遍历到source
                    target_id = edge.source_concept_id
                
                # 避免重复访问
                if target_id in visited:
                    continue
                
                visited.add(target_id)
                target_concept = self.get_concept(target_id)
                
                if target_concept:
                    result.append(target_concept)
                    queue.append((target_id, current_depth + 1))
        
        return result
    
    def add_concept(self, concept: ConceptNode) -> None:
        """添加概念节点"""
        self.concepts.append(concept)
        # 增量更新索引
        if self._indices_built:
            self._concept_index[concept.concept_id] = concept
            for factor_id in concept.factor_refs:
                if factor_id not in self._factor_index:
                    self._factor_index[factor_id] = []
                self._factor_index[factor_id].append(concept)
            dim_key = concept.dimension.value
            if dim_key not in self._dimension_index:
                self._dimension_index[dim_key] = []
            self._dimension_index[dim_key].append(concept)
            sys_key = concept.divination_system.value
            if sys_key not in self._system_index:
                self._system_index[sys_key] = []
            self._system_index[sys_key].append(concept)
    
    def add_edge(self, edge: SemanticEdge) -> None:
        """添加语义边"""
        self.edges.append(edge)
        # 增量更新索引
        if self._indices_built:
            if edge.source_concept_id not in self._edge_index:
                self._edge_index[edge.source_concept_id] = []
            self._edge_index[edge.source_concept_id].append(edge)
            if edge.is_bidirectional():
                if edge.target_concept_id not in self._edge_index:
                    self._edge_index[edge.target_concept_id] = []
                self._edge_index[edge.target_concept_id].append(edge)
    
    def update_metadata(self) -> None:
        """更新元数据中的统计信息"""
        self.metadata.total_concepts = len(self.concepts)
        self.metadata.total_edges = len(self.edges)
        
        # 收集books和systems
        books = set()
        systems = set()
        for concept in self.concepts:
            for source in concept.source_nodes:
                books.add(source.book_id)
            systems.add(concept.divination_system)
        
        self.metadata.books_included = sorted(books)
        self.metadata.systems_covered = sorted(systems, key=lambda x: x.value)
