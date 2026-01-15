"""
ConceptSelector Pydantic模型 - 筛选漏斗相关模型

Feature: cross-book-knowledge-graph
Requirement Refs: Req 12.1, Req 12.3, Req 12.5
Design Refs: Design.md#筛选漏斗接口
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    DivinationSystem,
)


# ============ 默认配额 ============

DEFAULT_SYSTEM_QUOTAS: Dict[DivinationSystem, int] = {
    DivinationSystem.BAZI: 15,
    DivinationSystem.ASTRO: 10,
    DivinationSystem.ZIWEI: 8,
    DivinationSystem.TAROT: 5,
    DivinationSystem.DREAM: 5,
    DivinationSystem.YIJING: 4,
    DivinationSystem.PSYCHOLOGY: 3,
    DivinationSystem.CROSS_SYSTEM: 5,
}


class SystemQuota(BaseModel):
    """
    体系配额 - 定义每个占卜体系的概念选择上限
    """
    system: DivinationSystem = Field(..., description="占卜体系")
    quota: int = Field(
        ...,
        ge=0,
        description="该体系的概念配额上限"
    )
    selected_count: int = Field(
        default=0,
        ge=0,
        description="实际选中的概念数量"
    )
    
    @property
    def remaining(self) -> int:
        """剩余配额"""
        return max(0, self.quota - self.selected_count)
    
    @property
    def is_exhausted(self) -> bool:
        """配额是否已耗尽"""
        return self.selected_count >= self.quota


class FunnelStats(BaseModel):
    """
    漏斗统计 - 记录筛选漏斗各阶段的概念数量
    
    漏斗阶段：
    1. factor_match: 因子匹配后的数量
    2. dimension_filter: 维度过滤后的数量
    3. authority_rank: 权威性排序后的数量
    4. quota_apply: 配额应用后的数量
    5. total_truncate: 总数截断后的数量
    """
    stage_factor_match: int = Field(
        default=0,
        ge=0,
        description="因子匹配阶段后的概念数量"
    )
    stage_dimension_filter: int = Field(
        default=0,
        ge=0,
        description="维度过滤阶段后的概念数量"
    )
    stage_authority_rank: int = Field(
        default=0,
        ge=0,
        description="权威性排序阶段后的概念数量"
    )
    stage_quota_apply: int = Field(
        default=0,
        ge=0,
        description="配额应用阶段后的概念数量"
    )
    stage_total_truncate: int = Field(
        default=0,
        ge=0,
        description="总数截断阶段后的概念数量（最终结果）"
    )
    
    def validate_monotonicity(self) -> bool:
        """
        验证漏斗单调性：各阶段数量应递减
        """
        return (
            self.stage_factor_match >= self.stage_dimension_filter >= 
            self.stage_authority_rank >= self.stage_quota_apply >= 
            self.stage_total_truncate
        )


class ConceptSelectionResult(BaseModel):
    """
    概念选择结果 - ConceptSelector的输出
    """
    selected_concepts: List[ConceptNode] = Field(
        default_factory=list,
        description="选中的概念列表"
    )
    funnel_stats: FunnelStats = Field(
        default_factory=FunnelStats,
        description="漏斗统计"
    )
    system_quotas: Dict[str, SystemQuota] = Field(
        default_factory=dict,
        description="各体系的配额使用情况"
    )
    truncated_systems: List[DivinationSystem] = Field(
        default_factory=list,
        description="因配额限制被截断的体系列表"
    )
    selection_time_ms: float = Field(
        default=0.0,
        ge=0.0,
        description="选择耗时（毫秒）"
    )
    
    @property
    def total_selected(self) -> int:
        """总选中数量"""
        return len(self.selected_concepts)


class SelectorConfig(BaseModel):
    """
    选择器配置 - 从selector_config.yaml加载
    """
    default_quotas: Dict[str, int] = Field(
        default_factory=lambda: {s.value: q for s, q in DEFAULT_SYSTEM_QUOTAS.items()},
        description="各体系的默认配额"
    )
    total_max_concepts: int = Field(
        default=50,
        ge=1,
        description="最大概念总数"
    )
    min_authority_score: float = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        description="最低权威性分数阈值"
    )
    include_conflicted: bool = Field(
        default=True,
        description="是否包含有冲突的概念"
    )
    selection_timeout_ms: float = Field(
        default=50.0,
        ge=0.0,
        description="选择超时（毫秒），目标<50ms"
    )
    
    def get_quota(self, system: DivinationSystem) -> int:
        """获取指定体系的配额"""
        return self.default_quotas.get(system.value, 5)
