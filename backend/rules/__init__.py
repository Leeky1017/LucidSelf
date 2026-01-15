"""
LucidSelf Rules Module

规则引擎核心模块。

包含:
- RuleEngine: 规则引擎核心
- RuleContext: 规则执行上下文
- ConditionEvaluator: 条件评估器
- Operator: 运算符枚举
- ConflictResolver: 冲突解决器
- ExclusiveGroups: 互斥组管理器
- RuleReloader: 规则热重载器
"""

from backend.rules.context import RuleContext
from backend.rules.engine import RuleEngine, RuleExecutionError
from backend.rules.condition import ConditionEvaluator, Operator
from backend.rules.conflict import (
    ConflictResolver,
    ExclusiveGroups,
    ConflictWarning,
    ConflictSeverity,
    ResolutionStrategy,
)
from backend.rules.reloader import RuleReloader, ReloadEvent
from backend.rules.dimension import DimensionMapper, get_dimension_mapper
from backend.rules.coverage import CoverageReporter
from backend.rules.changelog import RuleChangeLogger, get_change_logger

__all__ = [
    "RuleContext",
    "RuleEngine",
    "RuleExecutionError",
    "ConditionEvaluator",
    "Operator",
    "ConflictResolver",
    "ExclusiveGroups",
    "ConflictWarning",
    "ConflictSeverity",
    "ResolutionStrategy",
    "RuleReloader",
    "ReloadEvent",
    "DimensionMapper",
    "get_dimension_mapper",
    "CoverageReporter",
    "RuleChangeLogger",
    "get_change_logger",
]
