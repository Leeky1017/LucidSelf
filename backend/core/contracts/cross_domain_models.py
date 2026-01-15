"""
Cross Domain Models for LucidSelf Contracts

跨域轴 Schema 定义，用于多体系推理结果的统一维度标记。
对照文档: openspec/specs/schema-core/spec.md §Requirement 4

schema-core spec v0.4.0 要求：
- CrossDomainAxes: 跨域轴标注

更新: 集成 unified_dimensions 和 unified_time 模块
"""

from typing import List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator

from backend.core.contracts.unified_dimensions import LifeDomain
from backend.core.contracts.unified_time import TimeHorizon


class CrossDomainAxes(BaseModel):
    """
    跨域轴标注
    
    支持多体系推理结果的统一维度标记，用于后续 Playbook 生成和主题聚合。
    对照 schema-core spec §Requirement 4: 支持跨域结论轴
    
    可被 Bazi、Dream、Ziwei、Astro、Tarot 等多种体系共用。
    
    更新: life_domain 支持 LifeDomain 枚举，time_horizon 支持 TimeHorizon 枚举
    """
    life_domain: List[Union[LifeDomain, str]] = Field(
        default_factory=list,
        description="生活领域，如 ['career', 'health', 'relationship', 'wealth'] 或 LifeDomain 枚举"
    )
    time_horizon: Optional[Union[TimeHorizon, Literal["short_term", "medium_term", "long_term"]]] = Field(
        None,
        description="时间视野：支持 TimeHorizon 枚举或字符串 short_term/medium_term/long_term"
    )
    advice_type: List[str] = Field(
        default_factory=list,
        description="建议类型，如 ['action', 'reflection', 'warning', 'opportunity']"
    )

    
    @field_validator("life_domain", mode="before")
    @classmethod
    def normalize_life_domain(cls, v):
        """标准化 life_domain 输入，支持字符串和枚举混合"""
        if not v:
            return []
        result = []
        for item in v:
            if isinstance(item, LifeDomain):
                result.append(item)
            elif isinstance(item, str):
                # 尝试转换为 LifeDomain 枚举
                try:
                    result.append(LifeDomain(item.lower()))
                except ValueError:
                    # 未知领域保留为字符串以向后兼容
                    result.append(item)
            else:
                result.append(item)
        return result

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "life_domain": ["career", "health"],
                "time_horizon": "short_term",
                "advice_type": ["action", "reflection"]
            }
        }
    )
