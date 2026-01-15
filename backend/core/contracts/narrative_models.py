"""
Narrative and Fusion Models for LucidSelf Contracts

叙事配置与融合结果模型定义。
对照文档: docs/数据契约_Schema定义规范_v1.md §3.1, §3.3
"""

from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

from backend.core.contracts.base import FUSION_ID_PATTERN, LOCALE_PATTERN
from backend.core.contracts.runtime_models import RuntimeRuleResult


# =============================================================================
# 叙事配置模型 (§3.1)
# =============================================================================


class NarrativeConfig(BaseModel):
    """
    叙事配置
    
    控制叙事生成的风格、长度和证据展示方式。
    对照文档 §3.1 NarrativeConfig
    """
    config_id: str = Field(
        ..., 
        pattern="^[a-z][a-z0-9_]*$",
        description="配置ID，小写字母开头"
    )
    target_rule_patterns: List[str] = Field(
        ..., 
        description="目标规则模式，支持通配符"
    )
    
    # 风格
    tone: Literal["professional", "friendly", "mystical", "scientific"] = Field(
        ..., 
        description="叙事风格"
    )
    audience_level: Literal["beginner", "intermediate", "advanced"] = Field(
        ..., 
        description="受众水平"
    )
    
    # 多语言/多产品线支持
    locale: str = Field(
        default="zh-CN", 
        pattern=LOCALE_PATTERN,
        description="地区代码，如 zh-CN"
    )
    product_line: str = Field(default="default", description="产品线")
    channel: Literal["app", "web", "miniapp", "api"] = Field(
        default="app", 
        description="渠道"
    )
    risk_disclosure: Literal["none", "brief", "detailed"] = Field(
        default="brief", 
        description="风险提示级别"
    )
    
    # 长度
    min_length: int = Field(default=50, ge=10, description="最小长度")
    max_length: int = Field(default=500, le=2000, description="最大长度")
    
    # 证据展示
    show_evidence: bool = Field(default=True, description="是否展示证据")
    evidence_detail_level: Literal["simple", "detailed", "full"] = Field(
        default="simple", 
        description="证据详细程度"
    )
    
    # Prompt 模板
    prompt_templates: Dict[str, str] = Field(
        default_factory=dict, 
        description="Prompt 模板字典"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "config_id": "bazi_career_friendly",
                "target_rule_patterns": ["bazi_career_*"],
                "tone": "friendly",
                "audience_level": "intermediate",
                "locale": "zh-CN",
                "product_line": "default",
                "channel": "app",
                "risk_disclosure": "brief",
                "min_length": 50,
                "max_length": 500,
                "show_evidence": True,
                "evidence_detail_level": "simple",
                "prompt_templates": {
                    "opening": "让我们一起探讨您的事业发展...",
                    "evidence": "根据您的命盘显示...",
                    "conclusion": "综合来看..."
                }
            }
        }
    )


# =============================================================================
# 冲突警告模型 (§3.3)
# =============================================================================


class ConflictWarning(BaseModel):
    """
    冲突警告
    
    记录规则冲突信息。
    对照文档 §3.3 ConflictWarning
    """
    group: str = Field(..., description="互斥组ID")
    conflicting_rules: List[str] = Field(
        ..., 
        description="冲突的规则ID列表"
    )
    severity: Literal["LOW", "MEDIUM", "HIGH"] = Field(
        ..., 
        description="严重程度"
    )
    resolution_strategy: str = Field(..., description="解决策略")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "group": "body_strength_group",
                "conflicting_rules": ["rule_strong_001", "rule_weak_001"],
                "severity": "MEDIUM",
                "resolution_strategy": "priority_based"
            }
        }
    )


# =============================================================================
# 融合结果模型 (§3.3)
# =============================================================================


class FusionResult(BaseModel):
    """
    融合结果契约
    
    Layer4 融合层的标准输出，被 TOON 序列化和叙事生成使用。
    对照文档 §3.3 FusionResult
    """
    fusion_id: str = Field(
        ..., 
        pattern=FUSION_ID_PATTERN,
        description="融合ID，格式 fus_xxxxxxxxxxxx"
    )
    
    # 核心输出
    primary_themes: List[str] = Field(
        ..., 
        min_length=1,
        max_length=5, 
        description="主要主题，1-5 个"
    )
    evidence_chain: List[RuntimeRuleResult] = Field(
        ..., 
        min_length=1,
        max_length=20, 
        description="证据链，1-20 条"
    )
    
    # 置信度矩阵
    confidence_matrix: Dict[str, float] = Field(
        ..., 
        description="维度→置信度映射，如 {'事业': 0.85}"
    )
    
    # 交叉验证
    cross_validation_score: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="多引擎一致性分数 0.0-1.0"
    )
    contributing_engines: List[str] = Field(
        default_factory=list, 
        description="参与融合的引擎ID"
    )
    
    # 冲突信息
    conflicts: List[ConflictWarning] = Field(
        default_factory=list, 
        description="冲突警告列表"
    )
    
    # 元数据
    fusion_time_ms: float = Field(..., description="融合耗时（毫秒）")
    created_at: datetime = Field(
        default_factory=datetime.now, 
        description="创建时间"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "fusion_id": "fus_abc123456789",
                "primary_themes": ["事业突破", "财富积累", "人际拓展"],
                "evidence_chain": [],
                "confidence_matrix": {"事业": 0.85, "健康": 0.72},
                "cross_validation_score": 0.87,
                "contributing_engines": ["bazi_rule_engine", "tarot_semantic"],
                "conflicts": [],
                "fusion_time_ms": 45.2,
                "created_at": "2025-11-25T14:00:00"
            }
        }
    )
