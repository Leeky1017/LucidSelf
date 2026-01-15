"""
Test Condition Evaluator

条件评估器测试 - 验证 11 种运算符和复合条件。

对照 tasks.md Task 1.1, 1.2:
- Property 3: Condition Evaluation Correctness
- Validates: Requirements 1.8
"""

import pytest
from hypothesis import given, strategies as st, settings, assume

from backend.rules.condition import ConditionEvaluator, Operator


class TestConditionEvaluatorSimple:
    """简单条件测试"""
    
    def test_equality_operator(self):
        """测试 == 运算符"""
        condition = {"factor_id": "day_master", "operator": "==", "value": "甲"}
        
        assert ConditionEvaluator.evaluate(condition, {"day_master": "甲"}) is True
        assert ConditionEvaluator.evaluate(condition, {"day_master": "乙"}) is False
        assert ConditionEvaluator.evaluate(condition, {"day_master": None}) is False
    
    def test_not_equal_operator(self):
        """测试 != 运算符"""
        condition = {"factor_id": "day_master", "operator": "!=", "value": "甲"}
        
        assert ConditionEvaluator.evaluate(condition, {"day_master": "乙"}) is True
        assert ConditionEvaluator.evaluate(condition, {"day_master": "甲"}) is False
    
    def test_greater_than_operator(self):
        """测试 > 运算符"""
        condition = {"factor_id": "strength", "operator": ">", "value": 0.5}
        
        assert ConditionEvaluator.evaluate(condition, {"strength": 0.8}) is True
        assert ConditionEvaluator.evaluate(condition, {"strength": 0.5}) is False
        assert ConditionEvaluator.evaluate(condition, {"strength": 0.3}) is False
        assert ConditionEvaluator.evaluate(condition, {"strength": None}) is False
    
    def test_less_than_operator(self):
        """测试 < 运算符"""
        condition = {"factor_id": "strength", "operator": "<", "value": 0.5}
        
        assert ConditionEvaluator.evaluate(condition, {"strength": 0.3}) is True
        assert ConditionEvaluator.evaluate(condition, {"strength": 0.5}) is False
        assert ConditionEvaluator.evaluate(condition, {"strength": 0.8}) is False
        assert ConditionEvaluator.evaluate(condition, {"strength": None}) is False
    
    def test_greater_equal_operator(self):
        """测试 >= 运算符"""
        condition = {"factor_id": "count", "operator": ">=", "value": 3}
        
        assert ConditionEvaluator.evaluate(condition, {"count": 5}) is True
        assert ConditionEvaluator.evaluate(condition, {"count": 3}) is True
        assert ConditionEvaluator.evaluate(condition, {"count": 2}) is False
    
    def test_less_equal_operator(self):
        """测试 <= 运算符"""
        condition = {"factor_id": "count", "operator": "<=", "value": 3}
        
        assert ConditionEvaluator.evaluate(condition, {"count": 2}) is True
        assert ConditionEvaluator.evaluate(condition, {"count": 3}) is True
        assert ConditionEvaluator.evaluate(condition, {"count": 5}) is False
    
    def test_in_operator(self):
        """测试 in 运算符"""
        condition = {"factor_id": "branch", "operator": "in", "value": ["寅", "卯", "辰"]}
        
        assert ConditionEvaluator.evaluate(condition, {"branch": "寅"}) is True
        assert ConditionEvaluator.evaluate(condition, {"branch": "卯"}) is True
        assert ConditionEvaluator.evaluate(condition, {"branch": "巳"}) is False
    
    def test_not_in_operator(self):
        """测试 not_in 运算符"""
        condition = {"factor_id": "branch", "operator": "not_in", "value": ["寅", "卯", "辰"]}
        
        assert ConditionEvaluator.evaluate(condition, {"branch": "巳"}) is True
        assert ConditionEvaluator.evaluate(condition, {"branch": "寅"}) is False
    
    def test_exists_operator(self):
        """测试 exists 运算符"""
        condition = {"factor_id": "wealth_star", "operator": "exists"}
        
        assert ConditionEvaluator.evaluate(condition, {"wealth_star": "正财"}) is True
        assert ConditionEvaluator.evaluate(condition, {"wealth_star": 0}) is True
        assert ConditionEvaluator.evaluate(condition, {"wealth_star": None}) is False
        assert ConditionEvaluator.evaluate(condition, {}) is False
    
    def test_not_exists_operator(self):
        """测试 not_exists 运算符"""
        condition = {"factor_id": "wealth_star", "operator": "not_exists"}
        
        assert ConditionEvaluator.evaluate(condition, {"wealth_star": None}) is True
        assert ConditionEvaluator.evaluate(condition, {}) is True
        assert ConditionEvaluator.evaluate(condition, {"wealth_star": "正财"}) is False
    
    def test_between_operator(self):
        """测试 between 运算符"""
        condition = {"factor_id": "score", "operator": "between", "value": [0.3, 0.7]}
        
        assert ConditionEvaluator.evaluate(condition, {"score": 0.5}) is True
        assert ConditionEvaluator.evaluate(condition, {"score": 0.3}) is True
        assert ConditionEvaluator.evaluate(condition, {"score": 0.7}) is True
        assert ConditionEvaluator.evaluate(condition, {"score": 0.2}) is False
        assert ConditionEvaluator.evaluate(condition, {"score": 0.8}) is False
        assert ConditionEvaluator.evaluate(condition, {"score": None}) is False


class TestConditionEvaluatorCompound:
    """复合条件测试"""
    
    def test_and_condition(self):
        """测试 AND 复合条件"""
        condition = {
            "operator": "AND",
            "conditions": [
                {"factor_id": "day_master", "operator": "==", "value": "甲"},
                {"factor_id": "month_branch", "operator": "in", "value": ["寅", "卯"]},
            ]
        }
        
        # 两个都满足
        assert ConditionEvaluator.evaluate(
            condition, {"day_master": "甲", "month_branch": "寅"}
        ) is True
        
        # 第一个不满足
        assert ConditionEvaluator.evaluate(
            condition, {"day_master": "乙", "month_branch": "寅"}
        ) is False
        
        # 第二个不满足
        assert ConditionEvaluator.evaluate(
            condition, {"day_master": "甲", "month_branch": "巳"}
        ) is False
    
    def test_or_condition(self):
        """测试 OR 复合条件"""
        condition = {
            "operator": "OR",
            "conditions": [
                {"factor_id": "day_master", "operator": "==", "value": "甲"},
                {"factor_id": "day_master", "operator": "==", "value": "乙"},
            ]
        }
        
        assert ConditionEvaluator.evaluate(condition, {"day_master": "甲"}) is True
        assert ConditionEvaluator.evaluate(condition, {"day_master": "乙"}) is True
        assert ConditionEvaluator.evaluate(condition, {"day_master": "丙"}) is False
    
    def test_not_condition(self):
        """测试 NOT 复合条件"""
        condition = {
            "operator": "NOT",
            "condition": {"factor_id": "day_master", "operator": "==", "value": "甲"}
        }
        
        assert ConditionEvaluator.evaluate(condition, {"day_master": "乙"}) is True
        assert ConditionEvaluator.evaluate(condition, {"day_master": "甲"}) is False
    
    def test_nested_conditions(self):
        """测试嵌套条件"""
        condition = {
            "operator": "AND",
            "conditions": [
                {"factor_id": "day_master", "operator": "==", "value": "甲"},
                {
                    "operator": "OR",
                    "conditions": [
                        {"factor_id": "month_branch", "operator": "==", "value": "寅"},
                        {"factor_id": "month_branch", "operator": "==", "value": "卯"},
                    ]
                }
            ]
        }
        
        assert ConditionEvaluator.evaluate(
            condition, {"day_master": "甲", "month_branch": "寅"}
        ) is True
        assert ConditionEvaluator.evaluate(
            condition, {"day_master": "甲", "month_branch": "卯"}
        ) is True
        assert ConditionEvaluator.evaluate(
            condition, {"day_master": "甲", "month_branch": "巳"}
        ) is False
    
    def test_empty_and_condition(self):
        """测试空 AND 条件"""
        condition = {"operator": "AND", "conditions": []}
        assert ConditionEvaluator.evaluate(condition, {}) is True
    
    def test_empty_or_condition(self):
        """测试空 OR 条件"""
        condition = {"operator": "OR", "conditions": []}
        assert ConditionEvaluator.evaluate(condition, {}) is False


class TestConditionEvaluatorProperties:
    """属性测试 - Property 3: Condition Evaluation Correctness"""
    
    @given(
        factor_value=st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False), st.text(max_size=10)),
        target_value=st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False), st.text(max_size=10)),
    )
    @settings(max_examples=100)
    def test_equality_operator_property(self, factor_value, target_value):
        """
        **Feature: layer3-rules, Property 3: Condition Evaluation Correctness**
        
        测试 == 运算符与 Python 原生 == 一致
        """
        condition = {"factor_id": "test", "operator": "==", "value": target_value}
        factors = {"test": factor_value}
        
        result = ConditionEvaluator.evaluate(condition, factors)
        expected = factor_value == target_value
        
        assert result == expected
    
    @given(
        factor_value=st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False), st.text(max_size=10)),
        target_value=st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False), st.text(max_size=10)),
    )
    @settings(max_examples=100)
    def test_not_equal_operator_property(self, factor_value, target_value):
        """
        **Feature: layer3-rules, Property 3: Condition Evaluation Correctness**
        
        测试 != 运算符与 Python 原生 != 一致
        """
        condition = {"factor_id": "test", "operator": "!=", "value": target_value}
        factors = {"test": factor_value}
        
        result = ConditionEvaluator.evaluate(condition, factors)
        expected = factor_value != target_value
        
        assert result == expected
    
    @given(
        value=st.floats(allow_nan=False, allow_infinity=False, min_value=-1e6, max_value=1e6),
        lower=st.floats(allow_nan=False, allow_infinity=False, min_value=-1e6, max_value=1e6),
        upper=st.floats(allow_nan=False, allow_infinity=False, min_value=-1e6, max_value=1e6),
    )
    @settings(max_examples=100)
    def test_between_operator_property(self, value, lower, upper):
        """
        **Feature: layer3-rules, Property 3: Condition Evaluation Correctness**
        
        测试 between 运算符的正确性
        """
        # 确保 lower <= upper
        if lower > upper:
            lower, upper = upper, lower
        
        condition = {"factor_id": "test", "operator": "between", "value": [lower, upper]}
        factors = {"test": value}
        
        result = ConditionEvaluator.evaluate(condition, factors)
        expected = lower <= value <= upper
        
        assert result == expected
    
    @given(
        factor_value=st.one_of(st.integers(), st.text(max_size=5)),
        target_list=st.lists(st.one_of(st.integers(), st.text(max_size=5)), min_size=1, max_size=5),
    )
    @settings(max_examples=100)
    def test_in_operator_property(self, factor_value, target_list):
        """
        **Feature: layer3-rules, Property 3: Condition Evaluation Correctness**
        
        测试 in 运算符与 Python 原生 in 一致
        """
        condition = {"factor_id": "test", "operator": "in", "value": target_list}
        factors = {"test": factor_value}
        
        result = ConditionEvaluator.evaluate(condition, factors)
        expected = factor_value in target_list
        
        assert result == expected


class TestConditionEvaluatorUtils:
    """工具方法测试"""
    
    def test_get_required_factors_simple(self):
        """测试从简单条件提取因子"""
        condition = {"factor_id": "day_master", "operator": "==", "value": "甲"}
        
        factors = ConditionEvaluator.get_required_factors(condition)
        assert factors == ["day_master"]
    
    def test_get_required_factors_compound(self):
        """测试从复合条件提取因子"""
        condition = {
            "operator": "AND",
            "conditions": [
                {"factor_id": "day_master", "operator": "==", "value": "甲"},
                {"factor_id": "month_branch", "operator": "in", "value": ["寅", "卯"]},
            ]
        }
        
        factors = ConditionEvaluator.get_required_factors(condition)
        assert set(factors) == {"day_master", "month_branch"}
    
    def test_validate_condition_valid(self):
        """测试验证有效条件"""
        condition = {"factor_id": "day_master", "operator": "==", "value": "甲"}
        
        errors = ConditionEvaluator.validate_condition(condition)
        assert errors == []
    
    def test_validate_condition_missing_operator(self):
        """测试验证缺少运算符的条件"""
        condition = {"factor_id": "day_master", "value": "甲"}
        
        errors = ConditionEvaluator.validate_condition(condition)
        assert len(errors) > 0
        assert "operator" in errors[0].lower()
    
    def test_validate_condition_unknown_operator(self):
        """测试验证未知运算符"""
        condition = {"factor_id": "day_master", "operator": "unknown", "value": "甲"}
        
        errors = ConditionEvaluator.validate_condition(condition)
        assert len(errors) > 0
        assert "unknown" in errors[0].lower()
    
    def test_validate_condition_between_invalid_value(self):
        """测试验证 between 无效值"""
        condition = {"factor_id": "score", "operator": "between", "value": [0.5]}
        
        errors = ConditionEvaluator.validate_condition(condition)
        assert len(errors) > 0
        assert "between" in errors[0].lower()


class TestOperatorEnum:
    """运算符枚举测试"""
    
    def test_operator_values(self):
        """测试所有运算符值"""
        assert Operator.EQ.value == "=="
        assert Operator.NE.value == "!="
        assert Operator.GT.value == ">"
        assert Operator.LT.value == "<"
        assert Operator.GE.value == ">="
        assert Operator.LE.value == "<="
        assert Operator.IN.value == "in"
        assert Operator.NOT_IN.value == "not_in"
        assert Operator.EXISTS.value == "exists"
        assert Operator.NOT_EXISTS.value == "not_exists"
        assert Operator.BETWEEN.value == "between"
    
    def test_eleven_operators(self):
        """测试支持 11 种运算符"""
        basic_operators = [
            Operator.EQ, Operator.NE, Operator.GT, Operator.LT,
            Operator.GE, Operator.LE, Operator.IN, Operator.NOT_IN,
            Operator.EXISTS, Operator.NOT_EXISTS, Operator.BETWEEN,
        ]
        assert len(basic_operators) == 11
