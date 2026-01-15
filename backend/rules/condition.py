"""
Condition Evaluator

条件评估器 - 支持 11 种运算符和复合条件表达式。

对照 requirements.md Requirement 1.8:
支持运算符: ==, !=, >, <, >=, <=, in, not_in, exists, not_exists, between

对照 design.md §3 ConditionEvaluator
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Union


class Operator(str, Enum):
    """
    条件运算符枚举
    
    支持 11 种运算符 (Requirement 1.8)
    """
    EQ = "=="
    NE = "!="
    GT = ">"
    LT = "<"
    GE = ">="
    LE = "<="
    IN = "in"
    NOT_IN = "not_in"
    EXISTS = "exists"
    NOT_EXISTS = "not_exists"
    BETWEEN = "between"
    
    # 复合逻辑运算符
    AND = "AND"
    OR = "OR"
    NOT = "NOT"


class ConditionEvaluator:
    """
    条件评估器
    
    用于评估 ConfigRuleDefinition 中的 condition 字段。
    支持简单条件和复合条件（AND/OR/NOT）。
    
    对照 design.md:
    - 支持 11 种运算符
    - 支持 AND/OR/NOT 复合条件
    - 返回 bool 结果
    """
    
    @staticmethod
    def evaluate(
        condition: Dict[str, Any],
        factors: Dict[str, Any],
    ) -> bool:
        """
        评估条件表达式
        
        Args:
            condition: 条件定义
                简单条件: {"factor_id": ..., "operator": ..., "value": ...}
                复合条件: {"operator": "AND/OR/NOT", "conditions": [...]}
            factors: 因子值字典 {factor_id: value}
        
        Returns:
            条件是否满足
        
        Examples:
            # 简单条件
            >>> ConditionEvaluator.evaluate(
            ...     {"factor_id": "day_master", "operator": "==", "value": "甲"},
            ...     {"day_master": "甲"}
            ... )
            True
            
            # 复合条件 AND
            >>> ConditionEvaluator.evaluate(
            ...     {"operator": "AND", "conditions": [
            ...         {"factor_id": "day_master", "operator": "==", "value": "甲"},
            ...         {"factor_id": "month_branch", "operator": "in", "value": ["寅", "卯"]}
            ...     ]},
            ...     {"day_master": "甲", "month_branch": "寅"}
            ... )
            True
        """
        operator = condition.get("operator")
        
        # 复合逻辑运算符
        if operator == "AND":
            conditions = condition.get("conditions", [])
            if not conditions:
                return True  # 空条件列表视为 True
            return all(
                ConditionEvaluator.evaluate(c, factors)
                for c in conditions
            )
        
        elif operator == "OR":
            conditions = condition.get("conditions", [])
            if not conditions:
                return False  # 空条件列表视为 False
            return any(
                ConditionEvaluator.evaluate(c, factors)
                for c in conditions
            )
        
        elif operator == "NOT":
            # NOT 可以接受单个 condition 或 conditions 列表的第一个
            sub_condition = condition.get("condition")
            if sub_condition is None:
                conditions = condition.get("conditions", [])
                sub_condition = conditions[0] if conditions else {}
            return not ConditionEvaluator.evaluate(sub_condition, factors)
        
        # 简单条件
        factor_id = condition.get("factor_id")
        value = condition.get("value")
        factor_value = factors.get(factor_id)
        
        return ConditionEvaluator._evaluate_simple(operator, factor_value, value)
    
    @staticmethod
    def _evaluate_simple(
        operator: str,
        factor_value: Any,
        target_value: Any,
    ) -> bool:
        """
        评估简单条件
        
        Args:
            operator: 运算符字符串
            factor_value: 因子实际值
            target_value: 目标值
        
        Returns:
            条件是否满足
        """
        # == 等于
        if operator == "==" or operator == Operator.EQ:
            return factor_value == target_value
        
        # != 不等于
        elif operator == "!=" or operator == Operator.NE:
            return factor_value != target_value
        
        # > 大于
        elif operator == ">" or operator == Operator.GT:
            if factor_value is None:
                return False
            return factor_value > target_value
        
        # < 小于
        elif operator == "<" or operator == Operator.LT:
            if factor_value is None:
                return False
            return factor_value < target_value
        
        # >= 大于等于
        elif operator == ">=" or operator == Operator.GE:
            if factor_value is None:
                return False
            return factor_value >= target_value
        
        # <= 小于等于
        elif operator == "<=" or operator == Operator.LE:
            if factor_value is None:
                return False
            return factor_value <= target_value
        
        # in 包含于
        elif operator == "in" or operator == Operator.IN:
            if target_value is None:
                return False
            return factor_value in target_value
        
        # not_in 不包含于
        elif operator == "not_in" or operator == Operator.NOT_IN:
            if target_value is None:
                return True
            return factor_value not in target_value
        
        # exists 存在
        elif operator == "exists" or operator == Operator.EXISTS:
            return factor_value is not None
        
        # not_exists 不存在
        elif operator == "not_exists" or operator == Operator.NOT_EXISTS:
            return factor_value is None
        
        # between 区间
        elif operator == "between" or operator == Operator.BETWEEN:
            if factor_value is None:
                return False
            if not isinstance(target_value, (list, tuple)) or len(target_value) != 2:
                return False
            lower, upper = target_value
            return lower <= factor_value <= upper
        
        else:
            raise ValueError(f"Unknown operator: {operator}")
    
    @staticmethod
    def get_required_factors(condition: Dict[str, Any]) -> List[str]:
        """
        从条件中提取所需的因子 ID 列表
        
        Args:
            condition: 条件定义
        
        Returns:
            因子 ID 列表
        """
        factors = []
        operator = condition.get("operator")
        
        if operator in ("AND", "OR"):
            for sub_cond in condition.get("conditions", []):
                factors.extend(ConditionEvaluator.get_required_factors(sub_cond))
        elif operator == "NOT":
            sub_condition = condition.get("condition")
            if sub_condition is None:
                conditions = condition.get("conditions", [])
                sub_condition = conditions[0] if conditions else {}
            factors.extend(ConditionEvaluator.get_required_factors(sub_condition))
        else:
            factor_id = condition.get("factor_id")
            if factor_id:
                factors.append(factor_id)
        
        return list(set(factors))  # 去重
    
    @staticmethod
    def validate_condition(condition: Dict[str, Any]) -> List[str]:
        """
        验证条件定义的合法性
        
        Args:
            condition: 条件定义
        
        Returns:
            错误消息列表（空列表表示验证通过）
        """
        errors = []
        operator = condition.get("operator")
        
        if operator is None:
            errors.append("Missing 'operator' field in condition")
            return errors
        
        # 复合条件验证
        if operator in ("AND", "OR"):
            conditions = condition.get("conditions")
            if not isinstance(conditions, list):
                errors.append(f"{operator} condition requires 'conditions' list")
            else:
                for i, sub_cond in enumerate(conditions):
                    sub_errors = ConditionEvaluator.validate_condition(sub_cond)
                    errors.extend([f"{operator}[{i}]: {e}" for e in sub_errors])
        
        elif operator == "NOT":
            sub_condition = condition.get("condition") or \
                           (condition.get("conditions", [{}])[0] if condition.get("conditions") else None)
            if sub_condition is None:
                errors.append("NOT condition requires 'condition' or 'conditions'")
            else:
                sub_errors = ConditionEvaluator.validate_condition(sub_condition)
                errors.extend([f"NOT: {e}" for e in sub_errors])
        
        # 简单条件验证
        else:
            valid_operators = ["==", "!=", ">", "<", ">=", "<=", "in", "not_in", "exists", "not_exists", "between"]
            if operator not in valid_operators:
                errors.append(f"Unknown operator: {operator}")
            
            # exists 和 not_exists 不需要 value
            if operator not in ("exists", "not_exists"):
                if "factor_id" not in condition:
                    errors.append(f"Missing 'factor_id' for operator {operator}")
                if "value" not in condition and operator != "exists" and operator != "not_exists":
                    errors.append(f"Missing 'value' for operator {operator}")
            else:
                if "factor_id" not in condition:
                    errors.append(f"Missing 'factor_id' for operator {operator}")
            
            # between 需要两元素列表
            if operator == "between":
                value = condition.get("value")
                if not isinstance(value, (list, tuple)) or len(value) != 2:
                    errors.append("'between' operator requires [lower, upper] value")
        
        return errors
