"""
场景模型定义

对照文档: docs/ls_roadmap_executable.md §四、场景系统设计
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from backend.core.contracts.unified_dimensions import (
    DecisionAxis,
    LifeDomain,
)


class ScenarioKeywords(BaseModel):
    """场景关键词配置"""
    primary: List[str] = Field(default_factory=list, description="主要关键词")
    synonyms: List[str] = Field(default_factory=list, description="同义词")
    negative: List[str] = Field(default_factory=list, description="否定词，排除该场景")
    weight: float = Field(default=1.0, ge=0.0, le=2.0, description="关键词权重")


class ScenarioTemplate(BaseModel):
    """
    场景模板配置
    
    定义每个场景的：
    - 决策维度
    - 因子筛选规则
    - 规则分类
    - 关联关系
    """
    scenario_id: str = Field(..., pattern=r"^scn_[a-z_]+$")
    domain: LifeDomain
    
    # 关键词配置
    keywords: ScenarioKeywords
    
    # 决策维度（6-8个）
    decision_axes: List[DecisionAxis] = Field(default_factory=list)
    
    # 因子筛选规则
    factor_include_patterns: List[str] = Field(
        default_factory=list,
        description="包含的因子ID模式（通配符）"
    )
    factor_exclude_patterns: List[str] = Field(
        default_factory=list,
        description="排除的因子ID模式"
    )
    factor_always_include: List[str] = Field(
        default_factory=list,
        description="始终包含的因子ID"
    )
    
    # 规则分类
    rule_categories: List[str] = Field(
        default_factory=list,
        description="适用的规则分类"
    )
    
    # 关联场景
    related_scenarios: List[str] = Field(
        default_factory=list,
        description="关联的场景ID"
    )
    
    # 元数据
    label_zh: str
    label_en: str
    description: str = ""


class ScenarioContext(BaseModel):
    """
    场景上下文
    
    由 ScenarioRouter 生成，传递给后续 Pipeline 组件
    """
    scenario_id: str
    domain: LifeDomain
    decision_axes: List[DecisionAxis] = Field(default_factory=list)
    
    # 路由结果
    confidence: float = Field(..., ge=0.0, le=1.0)
    matched_keywords: List[str] = Field(default_factory=list)
    router_method: str = Field(
        default="keyword",
        description="路由方法: keyword | semantic | llm"
    )
    
    # 混合场景
    is_mixed: bool = Field(default=False, description="是否为混合场景")
    secondary_domains: List[LifeDomain] = Field(
        default_factory=list,
        description="次要场景领域"
    )
    
    # 筛选配置
    factor_filter: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="因子筛选配置 {include, exclude, always}"
    )
    rule_categories: List[str] = Field(
        default_factory=list,
        description="适用的规则分类"
    )


class ScenarioRoutingResult(BaseModel):
    """场景路由结果"""
    primary: ScenarioContext
    secondary: Optional[ScenarioContext] = None
    alternatives: List[ScenarioContext] = Field(
        default_factory=list,
        max_length=3
    )
    routing_time_ms: float = 0.0
