"""
ConflictOutput Pydantic模型 - 冲突输出和消解模板

Feature: cross-book-knowledge-graph
Requirement Refs: Req 3.4, Req 3.5, Req 13.1, Req 13.2, Req 13.3, Req 13.4, Req 13.6
Design Refs: Design.md#冲突输出接口
"""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from scripts.knowledge_graph_builder.models.edge import ConflictType


class ResolutionStrategy(str, Enum):
    """
    消解策略 - 4种冲突消解方式
    
    - AUTHORITY_BASED: 以权威性高的来源为准
    - CONDITION_BASED: 根据条件选择适用的观点
    - SYNTHESIS: 综合双方观点
    - PRESENT_BOTH: 同时呈现双方观点
    """
    AUTHORITY_BASED = "authority_based"
    CONDITION_BASED = "condition_based"
    SYNTHESIS = "synthesis"
    PRESENT_BOTH = "present_both"


class ConceptSummary(BaseModel):
    """
    概念摘要 - 用于冲突输出中的简化概念信息
    """
    concept_id: str = Field(..., description="概念ID")
    label_zh: str = Field(..., description="中文标签")
    label_en: Optional[str] = Field(None, description="英文标签")
    book_source: str = Field(..., description="主要来源典籍")
    authority_score: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="权威性分数"
    )
    summary_text: str = Field(
        default="",
        description="核心观点摘要"
    )


class ConflictOutput(BaseModel):
    """
    冲突输出 - 供叙事层使用的结构化冲突信息
    
    包含冲突双方的观点、消解策略、解决提示和可选的预渲染模板。
    FusionEngine通过此结构获取冲突信息并决定如何呈现给用户。
    """
    
    # ============ 冲突双方 ============
    viewpoint_a: ConceptSummary = Field(
        ...,
        description="观点A（通常是权威性较高的一方）"
    )
    viewpoint_b: ConceptSummary = Field(
        ...,
        description="观点B"
    )
    
    # ============ 冲突信息 ============
    conflict_type: ConflictType = Field(
        ...,
        description="冲突类型"
    )
    dimension: str = Field(
        ...,
        description="冲突所在维度，如'事业'、'健康'"
    )
    
    # ============ 消解信息 ============
    resolution_strategy: ResolutionStrategy = Field(
        ...,
        description="建议的消解策略"
    )
    resolution_hint: str = Field(
        ...,
        min_length=1,
        description="消解提示，向叙事层说明如何处理此冲突"
    )
    resolution_template_id: Optional[str] = Field(
        None,
        description="消解模板ID，指向conflict_templates.yaml中的模板"
    )
    
    # ============ 预渲染模板 ============
    rendered_template_zh: Optional[str] = Field(
        None,
        description="预渲染的中文模板，可直接用于叙事生成"
    )
    rendered_template_en: Optional[str] = Field(
        None,
        description="预渲染的英文模板"
    )
    
    # ============ 元数据 ============
    evidence_refs: List[str] = Field(
        default_factory=list,
        description="支持证据的引用ID列表"
    )
    
    def get_authority_winner(self) -> ConceptSummary:
        """获取权威性较高的观点"""
        if self.viewpoint_a.authority_score >= self.viewpoint_b.authority_score:
            return self.viewpoint_a
        return self.viewpoint_b
    
    def get_authority_difference(self) -> float:
        """获取权威性差异"""
        return abs(self.viewpoint_a.authority_score - self.viewpoint_b.authority_score)


class ConflictTemplate(BaseModel):
    """
    冲突模板 - conflict_templates.yaml中的模板定义
    """
    template_id: str = Field(..., description="模板ID")
    conflict_type: ConflictType = Field(..., description="适用的冲突类型")
    resolution_strategy: ResolutionStrategy = Field(..., description="消解策略")
    template_zh: str = Field(..., description="中文模板，支持占位符")
    template_en: Optional[str] = Field(None, description="英文模板")
    placeholders: List[str] = Field(
        default_factory=list,
        description="模板中的占位符列表，如['source_a', 'source_b', 'dimension']"
    )
