"""
Rule Decorators

规则函数装饰器，用于规则注册和元数据管理。
"""

from __future__ import annotations

import functools
from typing import Any, Callable, Dict, List, Optional, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

# 全局规则注册表
_RULE_REGISTRY: Dict[str, Dict[str, Any]] = {}


def register_rule(
    rule_id: str,
    category: str,
    exclusive_group: Optional[str] = None,
    priority: int = 500,
    tags: Optional[List[str]] = None,
    engine_id: Optional[str] = None,
) -> Callable[[F], F]:
    """
    规则注册装饰器
    
    用于标记和注册规则函数，支持元数据查询和冲突检测。
    
    Args:
        rule_id: 规则唯一标识
        category: 规则分类
        exclusive_group: 互斥组ID（同组规则不应同时触发）
        priority: 优先级 0-999
        tags: 标签列表
        engine_id: 规则所属引擎ID（如 bazi_rule_engine, tarot_rule_engine）
    
    Example:
        @register_rule(
            rule_id="dts_jia_spring_001",
            category="身强身弱",
            priority=100,
            engine_id="bazi_rule_engine"
        )
        def dts_jia_spring_001_evaluate(context: RuleContext) -> RuntimeRuleResult:
            ...
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        
        # 注册元数据
        metadata = {
            "rule_id": rule_id,
            "category": category,
            "exclusive_group": exclusive_group or "",
            "priority": priority,
            "tags": tags or [],
            "engine_id": engine_id or "unknown",
            "func": wrapper,
            "module": func.__module__,
        }
        
        _RULE_REGISTRY[rule_id] = metadata
        
        # 附加元数据到函数
        wrapper._rule_metadata = metadata  # type: ignore
        
        return wrapper  # type: ignore
    
    return decorator


def get_rule(rule_id: str) -> Optional[Callable]:
    """获取已注册的规则函数"""
    entry = _RULE_REGISTRY.get(rule_id)
    return entry["func"] if entry else None


def get_all_rules() -> Dict[str, Dict[str, Any]]:
    """获取所有已注册的规则"""
    return _RULE_REGISTRY.copy()


def get_rules_by_category(category: str) -> List[Dict[str, Any]]:
    """按分类获取规则"""
    return [r for r in _RULE_REGISTRY.values() if r["category"] == category]


def get_exclusive_group(group_id: str) -> List[Dict[str, Any]]:
    """获取互斥组内的所有规则"""
    return [r for r in _RULE_REGISTRY.values() if r["exclusive_group"] == group_id]


def clear_registry() -> None:
    """清空注册表（用于测试）"""
    _RULE_REGISTRY.clear()
