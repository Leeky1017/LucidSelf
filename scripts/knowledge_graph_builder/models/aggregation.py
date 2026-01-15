"""
ConceptAggregationRule Pydantic模型 - 概念聚合规则

Feature: cross-book-knowledge-graph
Requirement Refs: Req 11.1, Req 11.5
Design Refs: Design.md#概念聚合接口
"""

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from scripts.knowledge_graph_builder.models.concept import DivinationSystem


class AggregationStrategy(str, Enum):
    """
    聚合策略 - 定义如何将多个LogicNode合并为一个ConceptNode
    
    - MERGE_ALL: 合并所有来源节点
    - HIGHEST_AUTHORITY_ONLY: 仅保留最高权威性的来源
    - SAME_SYSTEM_MERGE: 仅合并同体系的节点
    - MANUAL: 需人工审核决定
    """
    MERGE_ALL = "merge_all"
    HIGHEST_AUTHORITY_ONLY = "highest_authority_only"
    SAME_SYSTEM_MERGE = "same_system_merge"
    MANUAL = "manual"


class LabelSelectionStrategy(str, Enum):
    """
    标签选择策略 - 定义如何选择ConceptNode的canonical_label
    
    - HIGHEST_AUTHORITY: 使用权威性最高来源的标签
    - MOST_COMMON: 使用出现次数最多的标签
    - MANUAL_OVERRIDE: 使用人工指定的标签
    """
    HIGHEST_AUTHORITY = "highest_authority"
    MOST_COMMON = "most_common"
    MANUAL_OVERRIDE = "manual_override"


class ConceptAggregationRule(BaseModel):
    """
    概念聚合规则 - 定义如何将对齐的LogicNode聚合为ConceptNode
    
    支持全局规则和体系专属覆盖。
    """
    rule_id: str = Field(
        ...,
        pattern=r"^rule_[a-z0-9_]+$",
        description="规则ID"
    )
    name: str = Field(
        ...,
        min_length=1,
        description="规则名称"
    )
    description: Optional[str] = Field(
        None,
        description="规则描述"
    )
    
    # ============ 聚合策略 ============
    aggregation_strategy: AggregationStrategy = Field(
        default=AggregationStrategy.MERGE_ALL,
        description="聚合策略"
    )
    label_selection_strategy: LabelSelectionStrategy = Field(
        default=LabelSelectionStrategy.HIGHEST_AUTHORITY,
        description="标签选择策略"
    )
    
    # ============ 阈值配置 ============
    min_similarity_score: float = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        description="最低相似度阈值"
    )
    min_factor_overlap: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="最低因子重叠率"
    )
    
    # ============ 体系专属覆盖 ============
    system_overrides: Dict[str, Dict] = Field(
        default_factory=dict,
        description="体系专属规则覆盖，key为divination_system值"
    )
    
    # ============ 冲突处理 ============
    allow_conflicting_summaries: bool = Field(
        default=True,
        description="是否允许聚合带有矛盾summary的节点"
    )
    record_conflicts: bool = Field(
        default=True,
        description="是否记录聚合过程中发现的冲突"
    )
    
    def get_strategy_for_system(
        self, 
        system: DivinationSystem
    ) -> AggregationStrategy:
        """获取指定体系的聚合策略"""
        override = self.system_overrides.get(system.value, {})
        strategy_str = override.get('aggregation_strategy')
        if strategy_str:
            try:
                return AggregationStrategy(strategy_str)
            except ValueError:
                pass
        return self.aggregation_strategy
    
    def get_label_strategy_for_system(
        self,
        system: DivinationSystem
    ) -> LabelSelectionStrategy:
        """获取指定体系的标签选择策略"""
        override = self.system_overrides.get(system.value, {})
        strategy_str = override.get('label_selection_strategy')
        if strategy_str:
            try:
                return LabelSelectionStrategy(strategy_str)
            except ValueError:
                pass
        return self.label_selection_strategy


class AggregationRulesConfig(BaseModel):
    """
    聚合规则配置 - aggregation_rules.yaml的根结构
    """
    global_rule: ConceptAggregationRule = Field(
        ...,
        description="全局默认规则"
    )
    dimension_rules: Dict[str, ConceptAggregationRule] = Field(
        default_factory=dict,
        description="维度专属规则，key为dimension值"
    )
    
    def get_rule_for_dimension(self, dimension: str) -> ConceptAggregationRule:
        """获取指定维度的规则，无则返回全局规则"""
        return self.dimension_rules.get(dimension, self.global_rule)
