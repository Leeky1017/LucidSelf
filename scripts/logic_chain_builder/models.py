"""
Data Models - 逻辑链数据模型定义

对应数据契约v1.1中的LogicChain schema。
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator


class SnippetRole(str, Enum):
    """叙事素材角色"""
    MAIN = "主干"
    MAIN_DEPENDENCY = "主干依赖"
    CONDITION_BRANCH = "条件分支"
    EXCEPTION = "例外处理"
    SUMMARY = "总结"


class EdgeRelation(str, Enum):
    """边的关系类型"""
    DEPENDS_ON = "depends_on"
    LEADS_TO = "leads_to"
    CONFLICTS_WITH = "conflicts_with"
    SUPPORTS = "supports"


class SourceMetadata(BaseModel):
    """元数据"""
    version: str = Field(default="1.0.0", description="版本号")
    extracted_at: datetime = Field(default_factory=datetime.now, description="提取时间")
    source_files: List[str] = Field(default_factory=list, description="源文件列表")
    snippet_count: int = Field(default=0, description="叙事素材总数")
    relation_count: int = Field(default=0, description="关系总数")


class LogicNode(BaseModel):
    """
    逻辑节点 - 聚合一组相关的叙事素材
    
    对应数据契约v1.1中的LogicNode schema。
    """
    node_id: str = Field(..., description="节点ID，格式: n_{book_abbr}_{chapter}_{seq}")
    snippet_ids: List[str] = Field(default_factory=list, description="关联的NarrativeSnippet ID列表")
    role: SnippetRole = Field(..., description="节点角色：主干/主干依赖/条件分支/例外处理/总结")
    condition: Optional[str] = Field(None, description="节点激活条件")
    summary: str = Field(..., description="节点语义摘要 (max 50 chars)")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="附加元数据")
    
    @field_validator('summary')
    @classmethod
    def validate_summary_length(cls, v: str) -> str:
        """验证摘要长度不超过50字符"""
        if len(v) > 50:
            return v[:50]
        return v


class LogicEdge(BaseModel):
    """
    逻辑边 - 定义节点间的推理关系
    
    对应数据契约v1.1中的LogicEdge schema。
    """
    from_node: str = Field(..., description="起始节点ID")
    to_node: str = Field(..., description="目标节点ID")
    relation: EdgeRelation = Field(..., description="边的关系类型")
    condition: Optional[str] = Field(None, description="边的激活条件")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="附加元数据")


class LogicChain(BaseModel):
    """
    逻辑链 - 单本典籍的推理结构
    
    由节点(Node)和边(Edge)组成的有向图。
    对应数据契约v1.1中的LogicChain schema。
    """
    chain_id: str = Field(..., description="链ID，格式: chain_{book_abbr}")
    book_id: str = Field(..., description="来源书籍ID")
    nodes: List[LogicNode] = Field(default_factory=list, description="逻辑节点列表")
    edges: List[LogicEdge] = Field(default_factory=list, description="逻辑边列表")
    narrative_order: List[str] = Field(default_factory=list, description="推荐的叙事输出顺序")
    entry_nodes: List[str] = Field(default_factory=list, description="入口节点ID列表")
    terminal_nodes: List[str] = Field(default_factory=list, description="终端节点ID列表")
    metadata: SourceMetadata = Field(default_factory=SourceMetadata, description="元数据")
    version: str = Field(default="1.0.0", description="版本号")


class ValidationError(BaseModel):
    """验证错误"""
    error_type: str = Field(..., description="错误类型")
    message: str = Field(..., description="错误消息")
    details: Dict[str, Any] = Field(default_factory=dict, description="详细信息")


class ValidationResult(BaseModel):
    """验证结果"""
    valid: bool = Field(..., description="是否通过验证")
    errors: List[ValidationError] = Field(default_factory=list, description="错误列表")
    warnings: List[str] = Field(default_factory=list, description="警告列表")
    repairs_made: List[str] = Field(default_factory=list, description="自动修复记录")


class BookQualityScores(BaseModel):
    """书籍质量评分"""
    connectivity: float = Field(default=0.0, description="连通性评分 (0-1)")
    argument_completeness: float = Field(default=0.0, description="论证完整性评分 (0-1)")
    orphan_ratio: float = Field(default=0.0, description="孤立节点比例 (0-1, 越低越好)")
    cycle_count: int = Field(default=0, description="循环数")
    connectivity_pass: bool = Field(default=False, description="连通性是否达标")
    argument_completeness_pass: bool = Field(default=False, description="论证完整性是否达标")
    orphan_ratio_pass: bool = Field(default=False, description="孤立节点比例是否达标")
    overall_pass: bool = Field(default=False, description="整体是否达标")


class BookStats(BaseModel):
    """单本书籍统计"""
    book_id: str = Field(..., description="书籍ID")
    snippet_count: int = Field(default=0, description="叙事素材总数")
    node_count: int = Field(default=0, description="节点数")
    edge_count: int = Field(default=0, description="边数")
    coverage: float = Field(default=0.0, description="snippet覆盖率")
    orphan_snippets: List[str] = Field(default_factory=list, description="未被包含的snippet_ids")
    status: Literal["success", "failed", "skipped"] = Field(default="success", description="处理状态")
    error_message: Optional[str] = Field(None, description="错误消息")
    quality_scores: Optional[BookQualityScores] = Field(None, description="质量评分")


class BuildReport(BaseModel):
    """构建报告"""
    generated_at: datetime = Field(default_factory=datetime.now, description="生成时间")
    total_books: int = Field(default=0, description="总书籍数")
    successful_books: int = Field(default=0, description="成功处理的书籍数")
    failed_books: int = Field(default=0, description="失败的书籍数")
    skipped_books: int = Field(default=0, description="跳过的书籍数")
    book_stats: List[BookStats] = Field(default_factory=list, description="各书籍统计")
    warnings: List[str] = Field(default_factory=list, description="警告列表")
    errors: List[str] = Field(default_factory=list, description="错误列表")
