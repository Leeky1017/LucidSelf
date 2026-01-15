"""
Schema Models - 与数据契约对齐的Pydantic模型
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator


# ============== Enums ==============

class FactorStatus(str, Enum):
    """因子状态"""
    EXISTING = "existing"
    NEW_CANDIDATE = "new_candidate"
    DEPRECATED = "deprecated"


class SnippetRole(str, Enum):
    """叙事素材角色"""
    MAIN = "主干"
    MAIN_DEPENDENCY = "主干依赖"
    CONDITION_BRANCH = "条件分支"
    EXCEPTION = "例外处理"
    SUMMARY = "总结"


class RelationType(str, Enum):
    """关系类型"""
    HIERARCHY = "hierarchy"
    COOPERATION = "cooperation"
    CONDITIONAL = "conditional"
    GATEWAY = "gateway"
    TRIAD = "triad"
    BEHAVIOR = "behavior"
    DYNAMIC = "dynamic"
    WUXING_SHENGKE = "wuxing_shengke"
    DEPENDENCY = "dependency"


class EffectDirection(str, Enum):
    """效果方向"""
    POSITIVE = "增益"
    NEGATIVE = "损害"
    RESTRICT = "限制"
    NEUTRAL = "中性"
    MIXED = "混合"
    MASTER_SLAVE = "主从"
    CONTAIN = "包含"
    MANDATORY = "强制"
    CONDITIONAL = "条件依赖"
    GATEWAY = "通则吉滞则凶"
    DOMINANT = "主导"
    KEY = "关键"
    DYNAMIC = "动态"
    POSITIVE_ENHANCE = "正向增强"


# ============== Core Models ==============

class ConfigFactor(BaseModel):
    """配置态因子 - 对应数据契约§1.1"""
    factor_type: str = Field(..., description="因子类型：结构类/时间类/状态类/态势类/边界类/五行类")
    factor_label: str = Field(..., description="因子标签（人话）")
    factor_id: str = Field(..., description="因子ID", pattern=r"^[a-z][a-z0-9_]*$")
    factor_source: str = Field(..., description="因子来源：existing/new_candidate")
    role_position: str = Field(..., description="角色/位置")
    value_constraint: str = Field(..., description="取值/约束")
    engine_id: str = Field(..., description="引擎归属")
    notes: str = Field(default="", description="备注")
    
    # 溯源信息
    source_book: Optional[str] = None
    source_chapter: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.now)

    @field_validator('factor_id')
    @classmethod
    def validate_factor_id(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("factor_id不能为空")
        return v.lower().strip()


class NarrativeSnippet(BaseModel):
    """叙事素材 - 对应数据契约§3.4"""
    snippet_id: str = Field(..., description="片段ID，格式：ns_书名缩写_序号")
    trigger: str = Field(..., description="触发条件")
    factor_trigger: Optional[str] = Field(None, description="因子触发条件")
    role: SnippetRole = Field(..., description="角色：主干/主干依赖/条件分支/例外处理/总结")
    snippet_text: str = Field(..., description="片段内容")
    source_ref: str = Field(..., description="来源引用，格式：《书名》#章节")
    
    # 溯源信息
    source_book: Optional[str] = None
    source_chapter: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.now)


class TermGlossary(BaseModel):
    """术语表条目 - L2术语对齐"""
    term_zh: str = Field(..., description="中文术语")
    term_en: str = Field(..., description="英文术语")
    definition_zh: str = Field(..., description="中文定义")
    definition_en: str = Field(..., description="英文定义")
    factor_id: str = Field(..., description="关联因子ID")
    status: FactorStatus = Field(..., description="状态：existing/new_candidate")
    
    # 溯源信息
    source_book: Optional[str] = None
    source_chapter: Optional[str] = None


class ConfigRelation(BaseModel):
    """因子关系 - 对应数据契约§1.5.1"""
    relation_id: str = Field(..., description="关系ID，格式：rel_书缩写_序号")
    relation_type: str = Field(..., description="关系类型")
    factor_a: str = Field(..., description="因子A")
    factor_b: str = Field(..., description="因子B")
    relation_nature: str = Field(..., description="关系性质")
    condition_constraint: str = Field(..., description="条件约束")
    effect_direction: str = Field(..., description="效果方向")
    source_ref: str = Field(..., description="来源引用")
    
    # 溯源信息
    source_book: Optional[str] = None
    source_chapter: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.now)


class EvidenceChainEntry(BaseModel):
    """推理溯源层 - 对应数据契约§1.5.2"""
    evidence_id: str = Field(..., description="证据ID，格式：evi_书缩写_序号")
    original_anchor: str = Field(..., description="原文锚点")
    involved_factors: List[str] = Field(..., description="涉及因子列表")
    reasoning_steps: str = Field(..., description="推理步骤")
    conclusion_direction: str = Field(..., description="结论方向")
    confidence: str = Field(..., description="置信度：高/中/低")
    can_generate_rule: bool = Field(..., description="是否可生成规则")
    target_rule_id: Optional[str] = Field(None, description="目标规则ID")
    
    # 溯源信息
    source_book: Optional[str] = None
    source_chapter: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.now)


class CrossSystemMapping(BaseModel):
    """跨体系概念映射 - 对应数据契约§1.5.3"""
    concept_id: str = Field(..., description="概念ID")
    common_semantics: str = Field(..., description="共通语义")
    bazi_mapping: str = Field(..., description="八字对应")
    astro_mapping: str = Field(..., description="占星对应")
    dream_mapping: str = Field(..., description="梦学对应")
    psychology_mapping: str = Field(..., description="心理学对应")
    notes: str = Field(default="", description="备注")
    
    # 溯源信息
    source_book: Optional[str] = None
    source_chapter: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.now)


# ============== Extraction Result ==============

class ExtractionResult(BaseModel):
    """提取结果"""
    source_file: str
    book_id: str
    chapter: Optional[str] = None
    
    factors: List[ConfigFactor] = Field(default_factory=list)
    snippets: List[NarrativeSnippet] = Field(default_factory=list)
    terms: List[TermGlossary] = Field(default_factory=list)
    relations: List[ConfigRelation] = Field(default_factory=list)
    evidence_chains: List[EvidenceChainEntry] = Field(default_factory=list)
    cross_mappings: List[CrossSystemMapping] = Field(default_factory=list)
    
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    
    extracted_at: datetime = Field(default_factory=datetime.now)
    
    @property
    def is_success(self) -> bool:
        return len(self.errors) == 0
    
    @property
    def total_items(self) -> int:
        return (
            len(self.factors) + 
            len(self.snippets) + 
            len(self.terms) +
            len(self.relations) + 
            len(self.evidence_chains) + 
            len(self.cross_mappings)
        )
