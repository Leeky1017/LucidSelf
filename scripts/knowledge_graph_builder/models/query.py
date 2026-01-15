"""
SemanticQuery和QueryResult Pydantic模型 - 语义查询接口

Feature: cross-book-knowledge-graph
Requirement Refs: Req 4.1, Req 4.2, Req 4.3, Req 4.4, Req 4.9, Req 4.10
Design Refs: Design.md#查询接口
"""

from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, field_validator

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
)
from scripts.knowledge_graph_builder.models.edge import RelationType


class ConflictSeverity(str, Enum):
    """冲突严重程度"""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class ConflictWarning(BaseModel):
    """
    冲突警告 - 附加在查询结果中，提示概念间存在冲突
    """
    concept_id: str = Field(..., description="涉及冲突的概念ID")
    conflicting_concept_id: str = Field(..., description="冲突对方的概念ID")
    conflict_type: str = Field(..., description="冲突类型")
    severity: ConflictSeverity = Field(
        default=ConflictSeverity.MEDIUM,
        description="冲突严重程度"
    )
    resolution_hint: str = Field(
        default="",
        description="解决建议"
    )


class SemanticQuery(BaseModel):
    """
    语义查询 - FusionEngine用于查询知识图谱的请求对象
    
    支持多种过滤条件：
    - factor_ids: 因子ID列表
    - dimension: 命理维度
    - divination_system: 占卜体系
    - authority_threshold: 最低权威性阈值
    
    支持图遍历：
    - traversal_depth: 遍历深度[0, 3]
    - filter_relation_types: 遍历时过滤的关系类型
    
    支持分页：
    - page: 页码
    - page_size: 每页数量[1, 100]
    """
    
    # ============ 过滤条件 ============
    factor_ids: List[str] = Field(
        default_factory=list,
        description="要查询的factor_id列表"
    )
    dimension: Optional[Dimension] = Field(
        None,
        description="命理维度过滤"
    )
    divination_system: Optional[DivinationSystem] = Field(
        None,
        description="占卜体系过滤"
    )
    authority_threshold: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="最低权威性阈值"
    )
    
    # ============ 遍历选项 ============
    traversal_depth: int = Field(
        default=1,
        description="图遍历深度，0表示不遍历，自动截断到[0, 3]"
    )
    filter_relation_types: Optional[List[RelationType]] = Field(
        None,
        description="遍历时只考虑的关系类型"
    )
    
    # ============ 分页 ============
    page: int = Field(
        default=1,
        ge=1,
        description="页码，从1开始"
    )
    page_size: int = Field(
        default=20,
        description="每页数量，自动截断到[1, 100]"
    )
    
    # ============ 其他选项 ============
    include_conflicts: bool = Field(
        default=True,
        description="是否包含有冲突的概念"
    )
    include_related_snippets: bool = Field(
        default=True,
        description="是否返回关联的NarrativeSnippet IDs"
    )
    
    @field_validator('traversal_depth')
    @classmethod
    def validate_traversal_depth(cls, v: int) -> int:
        """确保遍历深度在有效范围内"""
        return max(0, min(3, v))
    
    @field_validator('page_size')
    @classmethod
    def validate_page_size(cls, v: int) -> int:
        """确保页大小在有效范围内"""
        return max(1, min(100, v))


class QueryResultItem(BaseModel):
    """
    查询结果项 - 包含概念节点和相关信息
    """
    concept: ConceptNode = Field(..., description="概念节点")
    relevance_score: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="相关性得分"
    )
    traversal_depth: int = Field(
        default=0,
        ge=0,
        description="从查询起点的遍历深度"
    )
    related_snippet_ids: List[str] = Field(
        default_factory=list,
        description="关联的NarrativeSnippet IDs"
    )
    conflict_warnings: List[ConflictWarning] = Field(
        default_factory=list,
        description="冲突警告列表"
    )


class QueryResult(BaseModel):
    """
    查询结果 - SemanticQuery的返回对象
    
    包含分页信息和结果项列表
    """
    items: List[QueryResultItem] = Field(
        default_factory=list,
        description="结果项列表"
    )
    total_count: int = Field(
        default=0,
        ge=0,
        description="总匹配数量"
    )
    page: int = Field(
        default=1,
        ge=1,
        description="当前页码"
    )
    page_size: int = Field(
        default=20,
        ge=1,
        description="每页数量"
    )
    has_more: bool = Field(
        default=False,
        description="是否有更多结果"
    )
    
    # ============ 查询元信息 ============
    query_time_ms: float = Field(
        default=0.0,
        ge=0.0,
        description="查询耗时（毫秒）"
    )
    filtered_by_authority: int = Field(
        default=0,
        ge=0,
        description="因权威性阈值被过滤的数量"
    )
    
    def model_post_init(self, __context) -> None:
        """自动计算has_more"""
        if self.total_count > 0:
            self.has_more = (self.page * self.page_size) < self.total_count


class BatchQueryRequest(BaseModel):
    """批量查询请求"""
    queries: List[SemanticQuery] = Field(
        ...,
        min_length=1,
        max_length=10,
        description="查询列表，最多10个"
    )


class BatchQueryResult(BaseModel):
    """批量查询结果"""
    results: List[QueryResult] = Field(
        default_factory=list,
        description="查询结果列表，与请求一一对应"
    )
    total_time_ms: float = Field(
        default=0.0,
        ge=0.0,
        description="总查询耗时（毫秒）"
    )
