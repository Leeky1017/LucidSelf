"""
ConceptNode Pydantic模型 - 跨书知识图谱的核心概念节点

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.1, Req 1.3, Req 1.6, Req 14.1, Req 14.2
Design Refs: Design.md#ConceptNode
"""

from datetime import datetime
from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, field_validator


class DivinationSystem(str, Enum):
    """七大占卜体系 + 跨体系"""
    BAZI = "bazi"              # 八字
    ZIWEI = "ziwei"            # 紫微斗数
    ASTRO = "astro"            # 西方占星
    TAROT = "tarot"            # 塔罗牌
    DREAM = "dream"            # 解梦
    YIJING = "yijing"          # 周易
    PSYCHOLOGY = "psychology"  # 心理学
    CROSS_SYSTEM = "cross_system"  # 跨体系概念


class Dimension(str, Enum):
    """命理维度（扩展后共10个维度）"""
    CAREER = "事业"
    HEALTH = "健康"
    MARRIAGE = "婚姻"
    WEALTH = "财富"
    PERSONALITY = "性格"
    FORTUNE = "运势"        # 占星/八字流年
    OMEN = "预兆"           # 梦境预兆
    GUIDANCE = "指引"       # 塔罗当下指引
    UNCONSCIOUS = "潜意识"  # 梦境/心理学
    GENERAL = "通用"


class SourceNodeRef(BaseModel):
    """LogicNode引用 - 记录ConceptNode来源于哪些LogicChain节点"""
    book_id: str = Field(..., description="典籍ID，如'滴天髓'")
    node_id: str = Field(..., description="LogicNode的node_id")
    snippet_ids: List[str] = Field(default_factory=list, description="关联的叙事片段ID")


class ConflictSummary(BaseModel):
    """冲突摘要 - 记录与该概念相关的冲突信息"""
    conflict_count: int = Field(default=0, ge=0)
    highest_authority_source: Optional[str] = Field(
        None, 
        description="最高权威来源的book_id"
    )
    conflict_types: List[str] = Field(default_factory=list)
    resolution_status: Literal["unresolved", "authority_based", "condition_based", "manual"] = "unresolved"


class ConceptNode(BaseModel):
    """
    概念节点 - 跨书统一的语义概念
    
    ConceptNode是知识图谱的核心节点，代表一个跨越多本典籍的统一语义概念。
    每个ConceptNode可以关联多个LogicNode（通过source_nodes），
    并记录其所属的占卜体系、命理维度、权威性分数等信息。
    """
    
    # ============ 标识 ============
    concept_id: str = Field(
        ..., 
        pattern=r"^concept_[a-z0-9_]+$",
        description="概念ID，必须以concept_开头，遵循因子本体命名空间"
    )
    
    # ============ 标签 ============
    canonical_label_zh: str = Field(
        ..., 
        min_length=1,
        description="规范中文标签"
    )
    canonical_label_en: Optional[str] = Field(
        None, 
        description="规范英文标签"
    )
    
    # ============ 分类 ============
    divination_system: DivinationSystem = Field(
        ...,
        description="所属占卜体系"
    )
    dimension: Dimension = Field(
        default=Dimension.GENERAL,
        description="命理维度"
    )
    subdimension: Optional[str] = Field(
        None, 
        description="体系专属子维度，如'流年运势'、'本命特质'、'当下指引'"
    )
    
    # ============ 来源 ============
    source_nodes: List[SourceNodeRef] = Field(
        ..., 
        min_length=1,
        description="关联的LogicNode引用列表，至少需要一个来源"
    )
    
    # ============ 因子关联 ============
    factor_refs: List[str] = Field(
        default_factory=list,
        description="关联的factor_id列表"
    )
    
    # ============ 权威性 ============
    authority_score: float = Field(
        default=0.5, 
        ge=0.0, 
        le=1.0,
        description="权威性分数，范围[0.0, 1.0]"
    )
    
    # ============ 冲突 ============
    conflict_summary: Optional[ConflictSummary] = Field(
        None,
        description="冲突摘要，仅当存在冲突时填充"
    )
    
    # ============ 元数据 ============
    alignment_method: Literal[
        "factor_overlap", 
        "text_similarity", 
        "snippet_pattern", 
        "manual", 
        "l2.5_import",
        "orphaned"  # 来源LogicChain被删除时标记 (Req 5.7)
    ] = Field(
        default="factor_overlap",
        description="对齐方法"
    )
    aggregation_rule_id: Optional[str] = Field(
        None, 
        description="应用的聚合规则ID"
    )
    confidence: float = Field(
        default=0.8, 
        ge=0.0, 
        le=1.0,
        description="置信度"
    )
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    @field_validator('concept_id')
    @classmethod
    def validate_concept_id_namespace(cls, v: str) -> str:
        """
        验证concept_id遵循因子本体命名空间
        
        有效前缀包括：
        - concept_star_: 紫微斗数星曜
        - concept_palace_: 紫微斗数宫位
        - concept_state_: 状态/条件
        - concept_bazi_: 八字相关
        - concept_gua_: 周易卦象
        - concept_card_: 塔罗牌
        - concept_symbol_: 梦境符号
        - concept_sign_: 占星星座
        - concept_aspect_: 占星相位
        - concept_general_: 通用概念
        - concept_cross_: 跨体系概念
        """
        valid_prefixes = [
            'concept_star_', 'concept_palace_', 'concept_state_', 
            'concept_bazi_', 'concept_gua_', 'concept_card_', 
            'concept_symbol_', 'concept_sign_', 'concept_aspect_',
            'concept_general_', 'concept_cross_'
        ]
        # 检查是否匹配任一有效前缀
        if not any(v.startswith(p) for p in valid_prefixes):
            # 至少必须以concept_开头
            if not v.startswith('concept_'):
                raise ValueError(f"concept_id must start with 'concept_', got '{v}'")
        return v
    
    @field_validator('subdimension')
    @classmethod
    def validate_subdimension_consistency(cls, v: Optional[str], info) -> Optional[str]:
        """验证subdimension与divination_system的一致性"""
        if v is None:
            return v
        
        # 获取divination_system（如果已设置）
        divination_system = info.data.get('divination_system')
        if divination_system is None:
            return v
            
        # 定义体系专属子维度映射
        system_subdimensions = {
            DivinationSystem.BAZI: ['流年运势', '本命特质', '大运趋势', '日主分析'],
            DivinationSystem.ZIWEI: ['命宫特质', '流年运程', '十二宫分析'],
            DivinationSystem.ASTRO: ['本命盘', '行运', '推运', '相位影响'],
            DivinationSystem.TAROT: ['当下指引', '过去影响', '未来趋势', '建议行动'],
            DivinationSystem.DREAM: ['预兆解读', '潜意识分析', '符号意义'],
            DivinationSystem.YIJING: ['卦象解读', '爻辞分析', '变卦指引'],
            DivinationSystem.PSYCHOLOGY: ['人格分析', '行为模式', '潜意识探索'],
        }
        
        # 跨体系概念允许任意子维度
        if divination_system == DivinationSystem.CROSS_SYSTEM:
            return v
            
        # 验证子维度是否属于该体系（如果有定义）
        valid_subdims = system_subdimensions.get(divination_system, [])
        if valid_subdims and v not in valid_subdims:
            # 仅警告，不阻止（允许扩展）
            pass
            
        return v


# ============ 体系维度约束（用于验证） ============
SYSTEM_ALLOWED_DIMENSIONS: dict[DivinationSystem, list[Dimension]] = {
    DivinationSystem.BAZI: [
        Dimension.CAREER, Dimension.HEALTH, Dimension.MARRIAGE, 
        Dimension.WEALTH, Dimension.PERSONALITY, Dimension.FORTUNE, Dimension.GENERAL
    ],
    DivinationSystem.ZIWEI: [
        Dimension.CAREER, Dimension.HEALTH, Dimension.MARRIAGE, 
        Dimension.WEALTH, Dimension.PERSONALITY, Dimension.FORTUNE, Dimension.GENERAL
    ],
    DivinationSystem.ASTRO: [
        Dimension.CAREER, Dimension.HEALTH, Dimension.MARRIAGE, 
        Dimension.WEALTH, Dimension.PERSONALITY, Dimension.FORTUNE, Dimension.GENERAL
    ],
    DivinationSystem.TAROT: [
        Dimension.GUIDANCE, Dimension.FORTUNE, Dimension.GENERAL
    ],
    DivinationSystem.DREAM: [
        Dimension.OMEN, Dimension.UNCONSCIOUS, Dimension.GUIDANCE, Dimension.GENERAL
    ],
    DivinationSystem.YIJING: [
        Dimension.CAREER, Dimension.HEALTH, Dimension.MARRIAGE, 
        Dimension.WEALTH, Dimension.GUIDANCE, Dimension.GENERAL
    ],
    DivinationSystem.PSYCHOLOGY: [
        Dimension.PERSONALITY, Dimension.UNCONSCIOUS, Dimension.GENERAL
    ],
    DivinationSystem.CROSS_SYSTEM: list(Dimension),  # 跨体系允许所有维度
}


def validate_dimension_for_system(system: DivinationSystem, dimension: Dimension) -> bool:
    """
    验证给定维度是否适用于指定的占卜体系
    
    Args:
        system: 占卜体系
        dimension: 命理维度
        
    Returns:
        bool: 是否有效
    """
    allowed = SYSTEM_ALLOWED_DIMENSIONS.get(system, list(Dimension))
    return dimension in allowed
