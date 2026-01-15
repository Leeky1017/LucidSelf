"""
Life Version 数据模型

人生版本系统的核心数据模型。

对照文档: docs/ls_roadmap_executable.md §四、Phase 3: Life Versions 核心
"""

from datetime import datetime
from typing import Dict, List, Optional, Tuple

from pydantic import BaseModel, Field

from backend.core.contracts.unified_dimensions import (
    LifeDomain,
)


class LifeVersion(BaseModel):
    """
    人生版本
    
    一个可选的人生方案，包含策略、预期收益、风险和适合人群。
    """
    version_id: str = Field(..., pattern=r"^ver_[a-z0-9]{12}$")
    title: str = Field(..., max_length=20)  # "保守版" / "平衡版" / "进取版"
    subtitle: str = Field(..., max_length=50)  # 一句话描述
    
    # 策略
    strategy: List[str] = Field(..., min_length=1, max_length=5)
    key_actions: List[str] = Field(default_factory=list, max_length=5)
    
    # 预期收益
    expected_outcomes: Dict[str, float] = Field(
        ..., description="决策维度 → 预期得分 (0-1)"
    )
    outcome_ranges: Dict[str, Tuple[float, float]] = Field(
        default_factory=dict, 
        description="决策维度 → (下限, 上限)"
    )
    
    # 风险与代价
    risks: List[str] = Field(default_factory=list, max_length=5)
    costs: List[str] = Field(default_factory=list, max_length=3)
    
    # 适合人群
    suitable_for: List[str] = Field(default_factory=list, max_length=3)
    not_suitable_for: List[str] = Field(default_factory=list, max_length=3)
    
    # 置信度与来源
    confidence: float = Field(..., ge=0.0, le=1.0)
    source_factors: List[str] = Field(default_factory=list)
    source_rules: List[str] = Field(default_factory=list)
    
    # 时间线摘要
    timeline_summary: Optional[str] = Field(
        None, 
        max_length=200,
        description="该版本的时间线概要"
    )


class LifeVersionSet(BaseModel):
    """
    版本集合
    
    用户在某个场景下的 2-4 个可选版本。
    """
    set_id: str = Field(..., pattern=r"^vset_[a-z0-9]{12}$")
    user_id: str
    scenario_id: str
    domain: LifeDomain
    
    # 版本列表
    versions: List[LifeVersion] = Field(
        ..., 
        min_length=2, 
        max_length=4,
        description="2-4 个互斥版本"
    )
    
    # 对比维度
    comparison_axes: List[str] = Field(
        ...,
        description="用于对比的决策维度 axis_id 列表"
    )
    
    # 推荐版本
    recommended_version_id: Optional[str] = Field(
        None,
        description="系统推荐的版本 ID"
    )
    
    # 元数据
    created_at: datetime = Field(default_factory=datetime.now)


class VersionComparison(BaseModel):
    """
    版本对比视图
    
    用于前端展示的对比矩阵。
    """
    set_id: str
    axes: List[str] = Field(..., description="对比维度列表")
    
    # 对比矩阵: version_id → axis_id → score
    matrix: Dict[str, Dict[str, float]] = Field(
        ...,
        description="version_id → axis → score"
    )
    
    # 差异化指标
    differentiation_score: float = Field(
        default=0.0,
        ge=0.0, 
        le=1.0,
        description="版本间差异化程度 (0=相似, 1=完全不同)"
    )
    
    # 定性总结
    summary_zh: str = Field(..., max_length=300)


class VersionSelectionRecord(BaseModel):
    """
    版本选择记录
    
    记录用户对版本的选择。
    """
    record_id: str = Field(..., pattern=r"^vsel_[a-z0-9]{12}$")
    user_id: str
    set_id: str
    selected_version_id: str
    
    # 选择原因 (可选)
    reason: Optional[str] = Field(None, max_length=200)
    
    # 时间
    selected_at: datetime = Field(default_factory=datetime.now)


# =============================================================================
# 版本模板
# =============================================================================

VERSION_TEMPLATES = [
    {
        "name": "conservative",
        "title_zh": "稳健版",
        "title_en": "Conservative",
        "bias_toward": ["stability", "asset_security", "work_life_balance"],
        "bias_away": ["income_ceiling", "growth_potential", "autonomy"],
    },
    {
        "name": "balanced",
        "title_zh": "平衡版",
        "title_en": "Balanced",
        "bias_toward": [],  # 不偏向任何方向
        "bias_away": [],
    },
    {
        "name": "aggressive",
        "title_zh": "进取版",
        "title_en": "Progressive",  # 避免使用"激进"
        "bias_toward": ["income_ceiling", "growth_potential", "autonomy"],
        "bias_away": ["stability", "work_life_balance"],
    },
]
