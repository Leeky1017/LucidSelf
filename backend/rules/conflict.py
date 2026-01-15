"""
Conflict Resolver

冲突解决器 - 处理互斥规则组的冲突。

对照 requirements.md Requirement 3:
- 支持 4 种解决策略: priority_based, weight_based, confidence_based, source_based
- 预定义互斥组: body_strength_group, wealth_pattern_group, career_direction_group
- 冲突严重级别: LOW, MEDIUM, HIGH

对照 design.md §4 ConflictResolver
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional, Set

from backend.core.contracts import RuntimeRuleResult
# 复用 contracts 中的统一枚举，避免冗余
from backend.core.contracts import ConflictResolutionStrategy

logger = logging.getLogger(__name__)

# 保持向后兼容的别名
ResolutionStrategy = ConflictResolutionStrategy
"""
冲突解决策略 - 复用 contracts.ConflictResolutionStrategy

对照 Requirement 3.2-3.6
注: MERGE 策略仅在叙事层使用，此处 ConflictResolver 不支持
"""


class ConflictSeverity(str, Enum):
    """
    冲突严重级别
    
    对照 Requirement 3.8
    """
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class ConflictWarning:
    """
    冲突警告
    
    当同一互斥组内有多个规则触发时生成。
    
    对照 Requirement 3.1, 3.8, 3.9
    """
    group: str
    conflicting_rules: List[str]
    severity: ConflictSeverity
    resolution_strategy: str
    selected_rule: str
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "group": self.group,
            "conflicting_rules": self.conflicting_rules,
            "severity": self.severity.value,
            "resolution_strategy": self.resolution_strategy,
            "selected_rule": self.selected_rule,
        }


class ExclusiveGroups:
    """
    互斥组管理器
    
    管理预定义和自定义互斥组。同一互斥组内的规则不应同时触发。
    
    对照 Requirement 3.7, 3.10
    """
    
    # 预定义互斥组 (Requirement 3.7)
    PREDEFINED = {
        "body_strength_group": [
            "rule_body_strong",
            "rule_body_weak",
            "rule_body_neutral",
        ],
        "wealth_pattern_group": [
            "rule_wealth_abundant",
            "rule_wealth_scarce",
            "rule_wealth_broken",
        ],
        "career_direction_group": [
            "rule_career_north",
            "rule_career_south",
            "rule_career_east",
            "rule_career_west",
        ],
    }
    
    # 来源权威性排序（用于 source_based 策略）
    SOURCE_AUTHORITY = [
        "滴天髓",
        "子平真诠",
        "三命通会",
        "渊海子平",
        "穷通宝鉴",
        "紫微斗数全书",
        "周易",
    ]
    
    def __init__(self):
        """初始化互斥组管理器"""
        self._groups: Dict[str, List[str]] = dict(self.PREDEFINED)
        self._rule_to_group: Dict[str, str] = {}
        self._build_index()
    
    def _build_index(self) -> None:
        """构建规则到互斥组的索引"""
        for group_name, rule_ids in self._groups.items():
            for rule_id in rule_ids:
                self._rule_to_group[rule_id] = group_name
    
    def add_group(self, group_name: str, rule_ids: List[str]) -> None:
        """
        添加自定义互斥组
        
        对照 Requirement 3.10
        
        Args:
            group_name: 组名
            rule_ids: 规则 ID 列表
        """
        self._groups[group_name] = rule_ids
        for rule_id in rule_ids:
            self._rule_to_group[rule_id] = group_name
        logger.debug(f"Added exclusive group: {group_name} with {len(rule_ids)} rules")
    
    def remove_group(self, group_name: str) -> bool:
        """
        移除互斥组
        
        Args:
            group_name: 组名
        
        Returns:
            是否成功移除
        """
        if group_name not in self._groups:
            return False
        
        rule_ids = self._groups[group_name]
        del self._groups[group_name]
        
        for rule_id in rule_ids:
            if self._rule_to_group.get(rule_id) == group_name:
                del self._rule_to_group[rule_id]
        
        return True
    
    def get_group(self, rule_id: str) -> Optional[str]:
        """
        获取规则所属的互斥组
        
        Args:
            rule_id: 规则 ID
        
        Returns:
            互斥组名，未找到返回 None
        """
        return self._rule_to_group.get(rule_id)
    
    def get_group_rules(self, group_name: str) -> List[str]:
        """
        获取互斥组内的所有规则
        
        Args:
            group_name: 组名
        
        Returns:
            规则 ID 列表
        """
        return self._groups.get(group_name, []).copy()
    
    def get_all_groups(self) -> Dict[str, List[str]]:
        """获取所有互斥组"""
        return self._groups.copy()
    
    def is_in_group(self, rule_id: str, group_name: str) -> bool:
        """检查规则是否在指定互斥组中"""
        return self._rule_to_group.get(rule_id) == group_name


class ConflictResolver:
    """
    冲突解决器
    
    处理互斥规则组的冲突，支持多种解决策略。
    
    对照 design.md §4 和 Requirement 3
    """
    
    def __init__(
        self,
        default_strategy: ResolutionStrategy = ResolutionStrategy.PRIORITY_BASED,
        exclusive_groups: Optional[ExclusiveGroups] = None,
    ):
        """
        初始化冲突解决器
        
        Args:
            default_strategy: 默认解决策略
            exclusive_groups: 互斥组管理器（可选，默认创建新实例）
        """
        self.default_strategy = default_strategy
        self.exclusive_groups = exclusive_groups or ExclusiveGroups()
        self.warnings: List[ConflictWarning] = []
        
        # 策略函数映射
        self._strategies: Dict[ResolutionStrategy, Callable] = {
            ResolutionStrategy.PRIORITY_BASED: self._resolve_by_priority,
            ResolutionStrategy.WEIGHT_BASED: self._resolve_by_weight,
            ResolutionStrategy.CONFIDENCE_BASED: self._resolve_by_confidence,
            ResolutionStrategy.SOURCE_BASED: self._resolve_by_source,
        }
    
    def resolve_all(
        self,
        results: List[RuntimeRuleResult],
        strategy: Optional[ResolutionStrategy] = None,
    ) -> List[RuntimeRuleResult]:
        """
        解决所有冲突
        
        对照 Requirement 3.1-3.9
        
        Args:
            results: 规则执行结果列表
            strategy: 解决策略，默认使用 default_strategy
        
        Returns:
            解决冲突后的结果列表
        """
        self.warnings.clear()
        strategy = strategy or self.default_strategy
        
        # 分离匹配和未匹配的结果
        matched_results = [r for r in results if r.matched]
        unmatched_results = [r for r in results if not r.matched]
        
        # 按互斥组分组
        groups: Dict[str, List[RuntimeRuleResult]] = {}
        non_grouped: List[RuntimeRuleResult] = []
        
        for result in matched_results:
            group = self.exclusive_groups.get_group(result.rule_id)
            if group:
                if group not in groups:
                    groups[group] = []
                groups[group].append(result)
            else:
                non_grouped.append(result)
        
        # 解决每个组的冲突
        resolved: List[RuntimeRuleResult] = list(non_grouped)
        
        for group_name, group_results in groups.items():
            if len(group_results) > 1:
                # 检测到冲突 (Requirement 3.1)
                selected = self._resolve_group(group_results, strategy)
                
                # 生成警告 (Requirement 3.8)
                warning = ConflictWarning(
                    group=group_name,
                    conflicting_rules=[r.rule_id for r in group_results],
                    severity=self._assess_severity(group_results),
                    resolution_strategy=strategy.value,
                    selected_rule=selected.rule_id,
                )
                self.warnings.append(warning)
                
                logger.info(
                    f"Conflict resolved in {group_name}: "
                    f"selected {selected.rule_id} from {len(group_results)} rules"
                )
                
                resolved.append(selected)
            else:
                resolved.extend(group_results)
        
        # 添加未匹配的结果
        resolved.extend(unmatched_results)
        
        return resolved
    
    def _resolve_group(
        self,
        results: List[RuntimeRuleResult],
        strategy: ResolutionStrategy,
    ) -> RuntimeRuleResult:
        """
        解决单个组的冲突
        
        Args:
            results: 同组规则结果列表
            strategy: 解决策略
        
        Returns:
            选中的规则结果
        """
        resolver = self._strategies.get(strategy, self._resolve_by_priority)
        return resolver(results)
    
    def _resolve_by_priority(self, results: List[RuntimeRuleResult]) -> RuntimeRuleResult:
        """
        按优先级解决 (Requirement 3.3)
        
        使用 weight 字段作为运行态优先级
        """
        return max(results, key=lambda r: r.weight)
    
    def _resolve_by_weight(self, results: List[RuntimeRuleResult]) -> RuntimeRuleResult:
        """
        按权重解决 (Requirement 3.4)
        """
        return max(results, key=lambda r: r.weight)
    
    def _resolve_by_confidence(self, results: List[RuntimeRuleResult]) -> RuntimeRuleResult:
        """
        按置信度解决 (Requirement 3.5)
        """
        return max(results, key=lambda r: r.confidence)
    
    def _resolve_by_source(self, results: List[RuntimeRuleResult]) -> RuntimeRuleResult:
        """
        按来源权威性解决 (Requirement 3.6)
        
        根据预定义的来源权威性排序选择
        """
        def get_authority(result: RuntimeRuleResult) -> int:
            source = result.source_book or ""
            try:
                # 索引越小权威性越高，返回反向值
                return len(ExclusiveGroups.SOURCE_AUTHORITY) - \
                       ExclusiveGroups.SOURCE_AUTHORITY.index(source)
            except ValueError:
                return 0  # 未知来源权威性最低
        
        return max(results, key=get_authority)
    
    def _assess_severity(self, results: List[RuntimeRuleResult]) -> ConflictSeverity:
        """
        评估冲突严重级别 (Requirement 3.8)
        
        Args:
            results: 冲突的规则结果列表
        
        Returns:
            冲突严重级别
        """
        # 3 个以上冲突为高严重
        if len(results) >= 3:
            return ConflictSeverity.HIGH
        
        # 检查结论差异（大吉 vs 大凶）
        levels = set(r.level for r in results if r.level)
        if "大吉" in levels and "大凶" in levels:
            return ConflictSeverity.HIGH
        
        # 不同结论级别为中等严重
        if len(levels) > 1:
            return ConflictSeverity.MEDIUM
        
        return ConflictSeverity.LOW
    
    def get_warnings(self) -> List[ConflictWarning]:
        """
        获取冲突警告列表 (Requirement 3.9)
        
        Returns:
            冲突警告列表（副本）
        """
        return self.warnings.copy()
    
    def clear_warnings(self) -> None:
        """清空冲突警告"""
        self.warnings.clear()
    
    def add_exclusive_group(self, group_name: str, rule_ids: List[str]) -> None:
        """
        添加自定义互斥组 (Requirement 3.10)
        
        Args:
            group_name: 组名
            rule_ids: 规则 ID 列表
        """
        self.exclusive_groups.add_group(group_name, rule_ids)
