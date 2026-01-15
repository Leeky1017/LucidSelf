"""
Configuration Models for LucidSelf Contracts

配置态模型定义，用于 Markdown 提取和 Codegen 输入。
对照文档: docs/数据契约_Schema定义规范_v1.md §1.1, §2.1
"""

from __future__ import annotations

from typing import Any, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator

from backend.core.contracts.base import (
    FACTOR_ID_PATTERN,
    RULE_ID_PATTERN,
    VERSION_PATTERN,
    FactorCategory,
    SourceMetadata,
    StatusEnum,
)


# =============================================================================
# 因子配置模型 (§1.1)
# =============================================================================


class ConfigFactor(BaseModel):
    """
    配置态因子定义
    
    对应 Markdown 表格中的每一行因子定义。
    对照文档 §1.1 ConfigFactor
    """
    # 标识
    factor_id: str = Field(
        ..., 
        pattern=FACTOR_ID_PATTERN,
        description="因子唯一标识，小写字母开头"
    )
    label_zh: str = Field(..., description="中文标签")
    label_en: Optional[str] = Field(None, description="英文标签")
    
    # 分类
    category: FactorCategory = Field(..., description="因子类别")
    value_type: Literal["boolean", "float", "enum", "string"] = Field(
        ..., 
        description="值类型"
    )
    enum_values: Optional[List[str]] = Field(
        None, 
        description="仅 value_type=enum 时必填"
    )
    status: StatusEnum = Field(
        default=StatusEnum.ACTIVE,
        description="因子状态"
    )
    
    # 描述
    description_zh: str = Field(..., description="中文描述")
    knowledge_ref: List[str] = Field(
        default_factory=list,
        description="知识引用，格式：book_id:chapter[:section]"
    )
    
    # 版本与归属
    version: str = Field(
        ..., 
        pattern=VERSION_PATTERN,
        description="语义包版本 x.y.z"
    )
    engine_id: str = Field(..., description="所属引擎ID")
    
    # 溯源
    metadata: SourceMetadata = Field(..., description="溯源元数据")

    @field_validator("enum_values", mode="before")
    @classmethod
    def check_enum_values(cls, v: Optional[List[str]], info) -> Optional[List[str]]:
        """确保 enum 类型必须提供 enum_values"""
        # 注意：在 Pydantic v2 中，info.data 包含已验证的字段
        # 但 value_type 可能还未验证，所以我们在模型验证后检查
        return v

    def model_post_init(self, __context: Any) -> None:
        """模型初始化后校验 enum_values"""
        if self.value_type == "enum" and not self.enum_values:
            raise ValueError("enum_values required when value_type is enum")
        if self.enum_values and self.value_type != "enum":
            raise ValueError("enum_values only valid when value_type is enum")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "factor_id": "day_master_jia",
                "label_zh": "甲木日主",
                "label_en": "Day Master Jia Wood",
                "category": "structure",
                "value_type": "boolean",
                "status": "active",
                "description_zh": "日柱天干为甲木",
                "knowledge_ref": ["sanmingtonghui:卷一:论日主"],
                "version": "1.0.0",
                "engine_id": "bazi_calculator",
                "metadata": {
                    "book_id": "sanmingtonghui",
                    "chapter": "卷一",
                    "l1_anchor": "SMTH_L1_001"
                }
            }
        }
    )


# =============================================================================
# 规则条件模型 (§2.1)
# =============================================================================


class RuleCondition(BaseModel):
    """
    规则触发条件
    
    单个条件表达式，支持 11 种操作符。
    对照文档 §2.1 RuleCondition + design.md Requirement 1.8
    """
    factor_id: str = Field(
        ..., 
        pattern=FACTOR_ID_PATTERN,
        description="目标因子ID，小写字母开头"
    )
    operator: Literal[
        "==", "!=", ">", "<", ">=", "<=", 
        "in", "not_in", "exists", "not_exists", "between"
    ] = Field(
        ..., 
        description="比较操作符（11种）"
    )
    value: Any = Field(default=None, description="比较值（exists/not_exists 可选）")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "factor_id": "day_master_jia",
                "operator": "==",
                "value": True
            }
        }
    )


class LogicalExpression(BaseModel):
    """
    复合逻辑表达式
    
    支持 AND/OR/NOT 递归组合。
    对照文档 §2.1 LogicalExpression
    """
    operator: Literal["AND", "OR", "NOT"] = Field(..., description="逻辑操作符")
    conditions: List[Union[RuleCondition, "LogicalExpression"]] = Field(
        ..., 
        description="子条件列表"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "operator": "AND",
                "conditions": [
                    {"factor_id": "day_master_jia", "operator": "==", "value": True},
                    {"factor_id": "season", "operator": "==", "value": "spring"}
                ]
            }
        }
    )


# =============================================================================
# 规则结果模型 (§2.1)
# =============================================================================


class ConfigRuleResult(BaseModel):
    """
    配置态规则结果
    
    规则定义时的静态配置，包含结论模板。
    对照文档 §2.1 ConfigRuleResult
    """
    dimension: str = Field(..., description="维度：事业/健康/婚姻等")
    level: Literal["大吉", "吉", "中吉", "中等", "中性", "小凶", "凶", "大凶"] = Field(
        ..., 
        description="吉凶等级：大吉/吉/中吉/中等/中性/小凶/凶/大凶"
    )
    conclusion_template_zh: str = Field(
        ..., 
        description="中文结论模板，支持 {factor_id} 变量插值"
    )
    weight: float = Field(
        default=1.0, 
        ge=0.0, 
        le=10.0, 
        description="权重 0.0-10.0"
    )
    confidence: float = Field(
        default=0.8, 
        ge=0.0, 
        le=1.0, 
        description="置信度 0.0-1.0"
    )
    tags: List[str] = Field(default_factory=list, description="标签列表")
    evidence_factors: List[str] = Field(
        default_factory=list, 
        description="证据因子ID列表"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "dimension": "事业",
                "level": "吉",
                "conclusion_template_zh": "由于{day_master}生于{season}，五行能量{energy_state}，适合发展领导才能。",
                "weight": 1.5,
                "confidence": 0.85,
                "tags": ["事业", "领导力"],
                "evidence_factors": ["day_master_jia", "season_spring"]
            }
        }
    )


# =============================================================================
# 规则定义模型 (§2.1)
# =============================================================================


class ConfigRuleDefinition(BaseModel):
    """
    配置态规则定义
    
    完整的规则配置，包含条件、结果和元信息。
    对照文档 §2.1 ConfigRuleDefinition
    """
    rule_id: str = Field(
        ..., 
        pattern=RULE_ID_PATTERN,
        description="规则唯一标识"
    )
    human_label: str = Field(..., description="人话规则名")
    category: str = Field(..., description="规则分类")
    
    # 触发条件
    condition: Union[RuleCondition, LogicalExpression] = Field(
        ..., 
        description="触发条件"
    )
    required_factors: List[str] = Field(
        ..., 
        description="依赖的因子ID列表"
    )
    
    # 复杂逻辑标记（逃生舱）
    is_complex_logic: bool = Field(
        default=False, 
        description="是否为复杂逻辑，需人工 Python 实现"
    )
    python_handler_ref: Optional[str] = Field(
        None, 
        description="复杂规则的 Python 函数名"
    )
    
    # 结果与优先级
    result: ConfigRuleResult = Field(..., description="规则结果配置")
    priority: int = Field(
        default=500, 
        ge=0, 
        le=999, 
        description="优先级 0-999，默认 500"
    )
    
    # 互斥组（冲突解决）
    exclusive_group: Optional[str] = Field(
        None, 
        description="互斥组ID，同组规则不应同时触发"
    )
    
    # 版本与归属
    version: str = Field(
        ..., 
        pattern=VERSION_PATTERN,
        description="规则包版本"
    )
    status: StatusEnum = Field(
        default=StatusEnum.ACTIVE,
        description="规则状态"
    )
    engine_id: str = Field(..., description="所属引擎ID")
    
    # 溯源
    metadata: SourceMetadata = Field(..., description="溯源元数据")

    def model_post_init(self, __context: Any) -> None:
        """复杂规则必须指定 handler"""
        if self.is_complex_logic and not self.python_handler_ref:
            raise ValueError("python_handler_ref required when is_complex_logic is True")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "rule_id": "dts_jia_spring_001",
                "human_label": "甲木春生得时",
                "category": "身强身弱",
                "condition": {
                    "operator": "AND",
                    "conditions": [
                        {"factor_id": "day_master_jia", "operator": "==", "value": True},
                        {"factor_id": "season", "operator": "==", "value": "spring"}
                    ]
                },
                "required_factors": ["day_master_jia", "season"],
                "is_complex_logic": False,
                "result": {
                    "dimension": "personality",
                    "level": "吉",
                    "conclusion_template_zh": "甲木生于春季，木气当令，性格积极向上",
                    "weight": 1.5,
                    "confidence": 0.85
                },
                "priority": 100,
                "version": "1.0.0",
                "status": "active",
                "engine_id": "bazi_rule_engine",
                "metadata": {
                    "book_id": "ditianshui",
                    "chapter": "下卷",
                    "l1_anchor": "DTS_L1_025"
                }
            }
        }
    )


# 支持递归类型
LogicalExpression.model_rebuild()
