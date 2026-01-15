"""
SemanticEdge Pydantic模型 - 跨书知识图谱的语义边

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.2, Req 1.4, Req 3.1
Design Refs: Design.md#SemanticEdge
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, model_validator


class RelationType(str, Enum):
    """
    语义关系类型 - 定义概念间的7种语义关系
    
    关系方向说明:
    - ENTAILS: source蕴含target (A→B: A成立则B成立)
    - CONFLICTS_WITH: source与target冲突
    - SPECIALIZES: source是target的特化 (A→B: A是B的子概念)
    - GENERALIZES: source是target的泛化 (A→B: A是B的父概念)
    """
    SYNONYM = "synonym"                       # 同义关系 (双向)
    ENTAILS = "entails"                       # 蕴含关系 (单向)
    CONFLICTS_WITH = "conflicts_with"         # 冲突关系
    COMPLEMENTS = "complements"               # 互补关系
    SPECIALIZES = "specializes"               # 特化关系 (单向)
    GENERALIZES = "generalizes"               # 泛化关系 (单向)
    CROSS_SYSTEM_EQUIVALENT = "cross_system_equivalent"  # 跨体系等价 (双向)


class ConflictType(str, Enum):
    """
    冲突类型 - 定义4种冲突类型
    
    冲突类型说明:
    - DIRECT_CONTRADICTION: 直接矛盾，如"日主强喜泄"vs"日主强喜克"
    - CONDITIONAL_EXCEPTION: 条件例外，如"一般忌X，但若Y则喜X"
    - SCOPE_DIFFERENCE: 范围差异，如"本命vs流年"的不同适用范围
    - CROSS_SYSTEM_DIVERGENCE: 跨体系分歧，如"八字预测吉vs占星预测凶"
    """
    DIRECT_CONTRADICTION = "direct_contradiction"
    CONDITIONAL_EXCEPTION = "conditional_exception"
    SCOPE_DIFFERENCE = "scope_difference"
    CROSS_SYSTEM_DIVERGENCE = "cross_system_divergence"


# 双向关系类型
BIDIRECTIONAL_RELATIONS = {
    RelationType.SYNONYM,
    RelationType.CROSS_SYSTEM_EQUIVALENT,
}


class SemanticEdge(BaseModel):
    """
    语义边 - 概念间的语义关系
    
    SemanticEdge连接两个ConceptNode，表示它们之间的语义关系。
    支持7种关系类型，其中SYNONYM和CROSS_SYSTEM_EQUIVALENT是双向关系。
    当relation_type为CONFLICTS_WITH时，必须指定conflict_type。
    """
    
    # ============ 标识 ============
    edge_id: str = Field(
        ..., 
        pattern=r"^edge_[a-z0-9_]+$",
        description="边ID，格式为edge_<unique_suffix>"
    )
    
    # ============ 关系端点 ============
    source_concept_id: str = Field(
        ...,
        pattern=r"^concept_[a-z0-9_]+$",
        description="源概念ID"
    )
    target_concept_id: str = Field(
        ...,
        pattern=r"^concept_[a-z0-9_]+$",
        description="目标概念ID"
    )
    
    # ============ 关系类型 ============
    relation_type: RelationType = Field(
        ...,
        description="语义关系类型"
    )
    
    # ============ 冲突详情 ============
    conflict_type: Optional[ConflictType] = Field(
        None,
        description="冲突类型，仅当relation_type为conflicts_with时使用"
    )
    
    # ============ 置信度 ============
    confidence: float = Field(
        default=0.8, 
        ge=0.0, 
        le=1.0,
        description="关系置信度"
    )
    
    # ============ 证据 ============
    evidence_refs: List[str] = Field(
        default_factory=list,
        description="EvidenceChainEntry ID列表，用于追溯关系来源"
    )
    
    # ============ 方向性 ============
    bidirectional: bool = Field(
        default=False,
        description="是否双向关系（如synonym）"
    )
    
    # ============ 元数据 ============
    created_at: datetime = Field(default_factory=datetime.now)
    
    @model_validator(mode='after')
    def validate_edge_consistency(self) -> 'SemanticEdge':
        """
        验证边的一致性:
        1. source和target不能相同
        2. conflicts_with类型必须有conflict_type
        3. 双向关系自动设置bidirectional=True
        """
        # 1. 检查自环
        if self.source_concept_id == self.target_concept_id:
            raise ValueError("source_concept_id and target_concept_id cannot be the same")
        
        # 2. 检查冲突类型
        if self.relation_type == RelationType.CONFLICTS_WITH:
            if self.conflict_type is None:
                raise ValueError("conflict_type is required when relation_type is 'conflicts_with'")
        else:
            # 非冲突关系不应有conflict_type（可以有，但会被忽略）
            pass
        
        # 3. 自动设置双向关系
        if self.relation_type in BIDIRECTIONAL_RELATIONS:
            object.__setattr__(self, 'bidirectional', True)
        
        return self
    
    def is_bidirectional(self) -> bool:
        """判断该边是否为双向关系"""
        return self.bidirectional or self.relation_type in BIDIRECTIONAL_RELATIONS
    
    def get_reverse_edge(self) -> Optional['SemanticEdge']:
        """
        获取反向边（仅对双向关系有效）
        
        Returns:
            反向边，如果是单向关系则返回None
        """
        if not self.is_bidirectional():
            return None
        
        return SemanticEdge(
            edge_id=f"{self.edge_id}_reverse",
            source_concept_id=self.target_concept_id,
            target_concept_id=self.source_concept_id,
            relation_type=self.relation_type,
            conflict_type=self.conflict_type,
            confidence=self.confidence,
            evidence_refs=self.evidence_refs.copy(),
            bidirectional=True,
            created_at=self.created_at,
        )


def create_edge_id(source_id: str, target_id: str, relation: RelationType) -> str:
    """
    生成标准化的edge_id
    
    格式: edge_{source_suffix}_{target_suffix}_{relation}
    """
    # 提取concept_id的后缀
    source_suffix = source_id.replace("concept_", "")[:20]
    target_suffix = target_id.replace("concept_", "")[:20]
    relation_suffix = relation.value[:10]
    
    return f"edge_{source_suffix}_{target_suffix}_{relation_suffix}"
