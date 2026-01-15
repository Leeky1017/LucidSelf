"""
L2.5 Bridge Layer Models for LucidSelf Contracts

L2.5 桥接层 Schema 定义，包括因子关系、证据链和跨体系映射。
对照文档: docs/数据契约_Schema定义规范_v1.md §1.5

v1.1 新增内容：
- ConfigRelation: 因子关系（§1.5.1）
- EvidenceChainEntry: 证据链条目（§1.5.2）
- CrossSystemMapping: 跨体系概念映射（§1.5.3）
"""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

from backend.core.contracts.base import (
    VERSION_PATTERN,
    SourceMetadata,
)


# =============================================================================
# L2.5 正则模式
# =============================================================================

RELATION_ID_PATTERN = r"^rel_[a-z0-9_]+_\d{3}$"
"""关系ID正则: rel_书籍简称_序号，如 rel_dts_001"""

EVIDENCE_ID_PATTERN = r"^evi_[a-z0-9_]+_\d{3}$"
"""证据ID正则: evi_书籍简称_序号，如 evi_dts_001"""

CONCEPT_ID_PATTERN = r"^concept_[a-z0-9_]+$"
"""概念ID正则: concept_语义标签，如 concept_authority_pressure"""


# =============================================================================
# L2.5 枚举定义 (§1.5.1, §1.5.2)
# =============================================================================


class RelationType(str, Enum):
    """
    关系类型枚举
    
    对照文档 §1.5.1 RelationType
    """
    WUXING_SHENGKE = "wuxing_shengke"              # 五行生克
    DIZHI_INTERACTION = "dizhi_interaction"        # 地支刑冲合害
    TEN_GOD_RELATION = "ten_god_relation"          # 十神关系
    PLANET_HOUSE = "planet_house"                  # 行星-宫位关系
    PLANET_ASPECT = "planet_aspect"                # 行星相位关系
    DREAM_SYMBOL_RELATION = "dream_symbol_relation"    # 梦境符号关系
    PSYCH_ARCHETYPE_RELATION = "psych_archetype_relation"  # 心理原型关系
    CROSS_SYSTEM = "cross_system"                  # 跨体系映射关系


class EffectDirection(str, Enum):
    """
    效果方向枚举
    
    对照文档 §1.5.1 EffectDirection
    """
    BENEFICIAL = "增益"
    HARMFUL = "损害"
    RESTRICTIVE = "限制"
    NEUTRAL = "中性"
    MIXED = "混合"


class ConfidenceLevel(str, Enum):
    """
    置信度等级枚举
    
    对照文档 §1.5.2 ConfidenceLevel
    """
    HIGH = "高"      # 原文明确陈述
    MEDIUM = "中"    # 原文有隐含暗示
    LOW = "低"       # 需要结合多处推断


# =============================================================================
# ConfigRelation (§1.5.1)
# =============================================================================


class ConfigRelation(BaseModel):
    """
    配置态因子关系
    
    对应 L2.5 因子关系层表格，描述两个因子之间的关系。
    对照文档 §1.5.1 ConfigRelation
    """
    # 标识
    relation_id: str = Field(
        ...,
        pattern=RELATION_ID_PATTERN,
        description="关系ID，格式：rel_书籍简称_序号"
    )
    
    # 关系定义
    relation_type: RelationType = Field(..., description="关系类型")
    factor_a: str = Field(..., description="因子A的factor_id")
    factor_b: str = Field(..., description="因子B的factor_id")
    relation_nature: str = Field(
        ..., 
        description="关系性质，如：生、克、冲、合"
    )
    condition_constraint: Optional[str] = Field(
        None, 
        description="条件约束，如：春季限定"
    )
    effect_direction: EffectDirection = Field(..., description="效果方向")
    
    # 溯源
    source_ref: str = Field(
        ..., 
        description="来源引用，格式：《书名》#章节"
    )
    metadata: SourceMetadata = Field(..., description="溯源元数据")
    
    # 版本
    version: str = Field(
        ..., 
        pattern=VERSION_PATTERN,
        description="版本号 x.y.z"
    )
    engine_id: str = Field(..., description="所属引擎ID")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "relation_id": "rel_dts_001",
                "relation_type": "wuxing_shengke",
                "factor_a": "day_master_jia",
                "factor_b": "element_fire",
                "relation_nature": "生",
                "condition_constraint": None,
                "effect_direction": "增益",
                "source_ref": "《滴天髓》#甲木条",
                "metadata": {
                    "book_id": "ditianshui",
                    "chapter": "通神论",
                    "l1_anchor": "DTS_L1_001"
                },
                "version": "1.0.0",
                "engine_id": "bazi_semantic"
            }
        }
    )


# =============================================================================
# EvidenceChainEntry (§1.5.2)
# =============================================================================


class EvidenceChainEntry(BaseModel):
    """
    配置态证据链条目
    
    对应 L2.5 推理溯源层表格，记录从原文到结论的推理链。
    对照文档 §1.5.2 EvidenceChainEntry
    """
    # 标识
    evidence_id: str = Field(
        ...,
        pattern=EVIDENCE_ID_PATTERN,
        description="证据ID，格式：evi_书籍简称_序号"
    )
    
    # 证据链内容
    l1_anchor: str = Field(..., description="原文锚点（L1原文片段）")
    involved_factors: List[str] = Field(
        ..., 
        description="涉及的factor_id列表"
    )
    reasoning_step: str = Field(..., description="推理步骤描述")
    conclusion_direction: str = Field(
        ..., 
        description="结论方向，如：吉、凶、中性"
    )
    confidence: ConfidenceLevel = Field(..., description="置信度等级")
    
    # 规则关联
    can_generate_rule: bool = Field(..., description="是否可生成规则")
    target_rule_id: Optional[str] = Field(
        None, 
        description="目标规则ID（如可生成规则）"
    )
    
    # 溯源
    source_ref: str = Field(
        ..., 
        description="来源引用，格式：《书名》#章节"
    )
    metadata: SourceMetadata = Field(..., description="溯源元数据")
    
    # 版本
    version: str = Field(
        ..., 
        pattern=VERSION_PATTERN,
        description="版本号 x.y.z"
    )
    engine_id: str = Field(..., description="所属引擎ID")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "evidence_id": "evi_dts_001",
                "l1_anchor": "甲木参天，脱胎要火",
                "involved_factors": ["day_master_jia", "element_fire"],
                "reasoning_step": "甲木刚健需火泄秀，否则生机郁结",
                "conclusion_direction": "吉",
                "confidence": "高",
                "can_generate_rule": True,
                "target_rule_id": "rule_jia_needs_fire",
                "source_ref": "《滴天髓》#通神论",
                "metadata": {
                    "book_id": "ditianshui",
                    "chapter": "通神论",
                    "l1_anchor": "DTS_L1_001"
                },
                "version": "1.0.0",
                "engine_id": "bazi_semantic"
            }
        }
    )


# =============================================================================
# CrossSystemMapping (§1.5.3)
# =============================================================================


class CrossSystemMapping(BaseModel):
    """
    配置态跨体系概念映射
    
    对应 L2.5 跨体系映射层表格，建立不同体系间的概念桥接。
    对照文档 §1.5.3 CrossSystemMapping
    
    约束：必须涉及至少两个体系（7个 *_factors 列表中至少2个非空）
    """
    # 标识
    concept_id: str = Field(
        ...,
        pattern=CONCEPT_ID_PATTERN,
        description="概念ID，格式：concept_语义标签"
    )
    
    # 共通语义
    common_semantics: str = Field(..., description="共通语义核心描述")
    
    # 各体系对应因子（7个体系）
    bazi_factors: List[str] = Field(
        default_factory=list, 
        description="八字对应factor_id列表"
    )
    astro_factors: List[str] = Field(
        default_factory=list, 
        description="占星对应factor_id列表"
    )
    dream_factors: List[str] = Field(
        default_factory=list, 
        description="梦学对应factor_id列表"
    )
    psych_factors: List[str] = Field(
        default_factory=list, 
        description="心理学对应factor_id列表"
    )
    ziwei_factors: List[str] = Field(
        default_factory=list, 
        description="紫微对应factor_id列表"
    )
    tarot_factors: List[str] = Field(
        default_factory=list, 
        description="塔罗对应factor_id列表"
    )
    yijing_factors: List[str] = Field(
        default_factory=list, 
        description="易经对应factor_id列表"
    )
    
    # 备注
    notes: Optional[str] = Field(None, description="备注说明")
    
    # 溯源
    source_refs: List[str] = Field(
        default_factory=list, 
        description="来源引用列表"
    )
    metadata: SourceMetadata = Field(..., description="溯源元数据")
    
    # 版本
    version: str = Field(
        ..., 
        pattern=VERSION_PATTERN,
        description="版本号 x.y.z"
    )

    @model_validator(mode='after')
    def validate_at_least_two_systems(self) -> 'CrossSystemMapping':
        """跨体系映射必须涉及至少两个体系"""
        systems = [
            self.bazi_factors,
            self.astro_factors,
            self.dream_factors,
            self.psych_factors,
            self.ziwei_factors,
            self.tarot_factors,
            self.yijing_factors,
        ]
        non_empty_count = sum(1 for s in systems if s)
        if non_empty_count < 2:
            raise ValueError('跨体系映射必须涉及至少两个体系')
        return self

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "concept_id": "concept_authority_pressure",
                "common_semantics": "权威压力/父权/社会规范的限制",
                "bazi_factors": ["ten_god_qisha", "ten_god_zhengguan"],
                "astro_factors": ["saturn_square_sun", "saturn_conjunct_mc"],
                "dream_factors": ["dream_symbol_father", "dream_theme_exam"],
                "psych_factors": ["psych_archetype_shadow", "psych_process_shadow_integration"],
                "ziwei_factors": [],
                "tarot_factors": [],
                "yijing_factors": [],
                "notes": "代表来自权威的压力与成长契机",
                "source_refs": ["《滴天髓》#官杀论", "The Inner Sky#Saturn"],
                "metadata": {
                    "book_id": "cross_system",
                    "chapter": "authority_concepts",
                    "l1_anchor": "CS_L1_001"
                },
                "version": "1.0.0"
            }
        }
    )
