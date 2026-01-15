"""
Tests for Configuration Models

对照文档: docs/数据契约_Schema定义规范_v1.md §1.1, §2.1
"""

import pytest
from pydantic import ValidationError

from backend.core.contracts import (
    ConfigFactor,
    ConfigRuleDefinition,
    ConfigRuleResult,
    FactorCategory,
    LogicalExpression,
    RuleCondition,
    SourceMetadata,
    StatusEnum,
)


# =============================================================================
# SourceMetadata 辅助函数
# =============================================================================


def make_metadata(**kwargs) -> SourceMetadata:
    """创建测试用 SourceMetadata"""
    defaults = {
        "book_id": "test_book",
        "chapter": "卷一",
        "l1_anchor": "TEST_L1_001",
    }
    defaults.update(kwargs)
    return SourceMetadata(**defaults)


# =============================================================================
# ConfigFactor 测试
# =============================================================================


class TestConfigFactor:
    """ConfigFactor 模型测试"""

    def test_valid_boolean_factor(self):
        """测试有效的 boolean 类型因子"""
        factor = ConfigFactor(
            factor_id="day_master_jia",
            label_zh="甲木日主",
            label_en="Day Master Jia Wood",
            category=FactorCategory.STRUCTURE,
            value_type="boolean",
            status=StatusEnum.ACTIVE,
            description_zh="日柱天干为甲木",
            knowledge_ref=["sanmingtonghui:卷一:论日主"],
            version="1.0.0",
            engine_id="bazi_calculator",
            metadata=make_metadata(),
        )
        assert factor.factor_id == "day_master_jia"
        assert factor.value_type == "boolean"
        assert factor.enum_values is None

    def test_valid_enum_factor(self):
        """测试有效的 enum 类型因子"""
        factor = ConfigFactor(
            factor_id="season",
            label_zh="季节",
            category=FactorCategory.TIME,
            value_type="enum",
            enum_values=["spring", "summer", "autumn", "winter"],
            description_zh="当前季节",
            version="1.0.0",
            engine_id="bazi_calculator",
            metadata=make_metadata(),
        )
        assert factor.value_type == "enum"
        assert "spring" in factor.enum_values

    def test_enum_without_values_raises_error(self):
        """测试 enum 类型未提供 enum_values 时抛出错误"""
        with pytest.raises(ValueError, match="enum_values required"):
            ConfigFactor(
                factor_id="bad_enum",
                label_zh="错误枚举",
                category=FactorCategory.STATE,
                value_type="enum",
                # enum_values 缺失
                description_zh="测试",
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_non_enum_with_values_raises_error(self):
        """测试非 enum 类型提供 enum_values 时抛出错误"""
        with pytest.raises(ValueError, match="only valid when value_type is enum"):
            ConfigFactor(
                factor_id="bad_boolean",
                label_zh="错误布尔",
                category=FactorCategory.STATE,
                value_type="boolean",
                enum_values=["yes", "no"],  # 不应该有
                description_zh="测试",
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_invalid_factor_id_pattern(self):
        """测试无效的 factor_id 格式"""
        with pytest.raises(ValidationError):
            ConfigFactor(
                factor_id="InvalidId",  # 不能大写开头
                label_zh="测试",
                category=FactorCategory.STATE,
                value_type="boolean",
                description_zh="测试",
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_factor_id_with_numbers(self):
        """测试 factor_id 可以包含数字"""
        factor = ConfigFactor(
            factor_id="factor_123_test",
            label_zh="测试",
            category=FactorCategory.STATE,
            value_type="boolean",
            description_zh="测试",
            version="1.0.0",
            engine_id="test",
            metadata=make_metadata(),
        )
        assert factor.factor_id == "factor_123_test"

    def test_invalid_version_format(self):
        """测试无效的版本格式"""
        with pytest.raises(ValidationError):
            ConfigFactor(
                factor_id="test_factor",
                label_zh="测试",
                category=FactorCategory.STATE,
                value_type="boolean",
                description_zh="测试",
                version="1.0",  # 缺少 patch 版本
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_all_categories(self):
        """测试所有因子类别"""
        for cat in FactorCategory:
            factor = ConfigFactor(
                factor_id=f"test_{cat.value}",
                label_zh=f"测试{cat.value}",
                category=cat,
                value_type="boolean",
                description_zh="测试",
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )
            assert factor.category == cat

    def test_all_status_values(self):
        """测试所有状态值"""
        for status in StatusEnum:
            factor = ConfigFactor(
                factor_id=f"test_{status.value}",
                label_zh=f"测试{status.value}",
                category=FactorCategory.STATE,
                value_type="boolean",
                status=status,
                description_zh="测试",
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )
            assert factor.status == status


# =============================================================================
# RuleCondition 测试
# =============================================================================


class TestRuleCondition:
    """RuleCondition 模型测试"""

    def test_valid_equality_condition(self):
        """测试有效的等式条件"""
        cond = RuleCondition(
            factor_id="day_master_jia",
            operator="==",
            value=True,
        )
        assert cond.operator == "=="
        assert cond.value is True

    def test_all_operators(self):
        """测试所有操作符"""
        operators = ["==", "!=", ">", "<", ">=", "<=", "in", "exists"]
        for op in operators:
            cond = RuleCondition(
                factor_id="test_factor",
                operator=op,
                value="test" if op == "in" else True,
            )
            assert cond.operator == op

    def test_invalid_operator(self):
        """测试无效的操作符"""
        with pytest.raises(ValidationError):
            RuleCondition(
                factor_id="test_factor",
                operator="like",  # 不支持
                value="test",
            )

    def test_in_operator_with_list(self):
        """测试 in 操作符使用列表值"""
        cond = RuleCondition(
            factor_id="season",
            operator="in",
            value=["spring", "summer"],
        )
        assert cond.operator == "in"
        assert isinstance(cond.value, list)

    def test_factor_id_pattern_validation(self):
        """测试 factor_id 正则验证"""
        with pytest.raises(ValidationError):
            RuleCondition(
                factor_id="123_invalid",  # 不能数字开头
                operator="==",
                value=True,
            )


# =============================================================================
# LogicalExpression 测试
# =============================================================================


class TestLogicalExpression:
    """LogicalExpression 模型测试"""

    def test_simple_and_expression(self):
        """测试简单 AND 表达式"""
        expr = LogicalExpression(
            operator="AND",
            conditions=[
                RuleCondition(factor_id="factor_a", operator="==", value=True),
                RuleCondition(factor_id="factor_b", operator="==", value=True),
            ],
        )
        assert expr.operator == "AND"
        assert len(expr.conditions) == 2

    def test_nested_expression(self):
        """测试嵌套表达式"""
        expr = LogicalExpression(
            operator="OR",
            conditions=[
                LogicalExpression(
                    operator="AND",
                    conditions=[
                        RuleCondition(factor_id="factor_a", operator="==", value=True),
                        RuleCondition(factor_id="factor_b", operator=">", value=0.5),
                    ],
                ),
                RuleCondition(factor_id="factor_c", operator="exists", value=True),
            ],
        )
        assert expr.operator == "OR"
        assert isinstance(expr.conditions[0], LogicalExpression)
        assert isinstance(expr.conditions[1], RuleCondition)

    def test_not_expression(self):
        """测试 NOT 表达式"""
        expr = LogicalExpression(
            operator="NOT",
            conditions=[
                RuleCondition(factor_id="factor_a", operator="==", value=True),
            ],
        )
        assert expr.operator == "NOT"

    def test_invalid_operator(self):
        """测试无效的逻辑操作符"""
        with pytest.raises(ValidationError):
            LogicalExpression(
                operator="XOR",  # 不支持
                conditions=[
                    RuleCondition(factor_id="factor_a", operator="==", value=True),
                ],
            )


# =============================================================================
# ConfigRuleResult 测试
# =============================================================================


class TestConfigRuleResult:
    """ConfigRuleResult 模型测试"""

    def test_valid_result(self):
        """测试有效的规则结果"""
        result = ConfigRuleResult(
            dimension="事业",
            level="吉",
            conclusion_template_zh="由于{day_master}生于{season}，发展顺利。",
            weight=1.5,
            confidence=0.85,
            tags=["事业", "领导力"],
            evidence_factors=["day_master_jia", "season_spring"],
        )
        assert result.dimension == "事业"
        assert result.level == "吉"
        assert "{day_master}" in result.conclusion_template_zh

    def test_weight_bounds(self):
        """测试权重边界"""
        # 有效边界
        result = ConfigRuleResult(
            dimension="测试",
            level="中等",
            conclusion_template_zh="测试",
            weight=0.0,
        )
        assert result.weight == 0.0

        result = ConfigRuleResult(
            dimension="测试",
            level="中等",
            conclusion_template_zh="测试",
            weight=10.0,
        )
        assert result.weight == 10.0

        # 超出边界
        with pytest.raises(ValidationError):
            ConfigRuleResult(
                dimension="测试",
                level="中等",
                conclusion_template_zh="测试",
                weight=11.0,
            )

    def test_confidence_bounds(self):
        """测试置信度边界"""
        # 有效边界
        result = ConfigRuleResult(
            dimension="测试",
            level="中等",
            conclusion_template_zh="测试",
            confidence=0.0,
        )
        assert result.confidence == 0.0

        result = ConfigRuleResult(
            dimension="测试",
            level="中等",
            conclusion_template_zh="测试",
            confidence=1.0,
        )
        assert result.confidence == 1.0

        # 超出边界
        with pytest.raises(ValidationError):
            ConfigRuleResult(
                dimension="测试",
                level="中等",
                conclusion_template_zh="测试",
                confidence=1.5,
            )

    def test_all_levels(self):
        """测试所有吉凶等级"""
        levels = ["大吉", "吉", "中等", "凶", "大凶"]
        for level in levels:
            result = ConfigRuleResult(
                dimension="测试",
                level=level,
                conclusion_template_zh="测试",
            )
            assert result.level == level


# =============================================================================
# ConfigRuleDefinition 测试
# =============================================================================


class TestConfigRuleDefinition:
    """ConfigRuleDefinition 模型测试"""

    def test_valid_simple_rule(self):
        """测试有效的简单规则"""
        rule = ConfigRuleDefinition(
            rule_id="dts_jia_spring_001",
            human_label="甲木春生得时",
            category="身强身弱",
            condition=RuleCondition(
                factor_id="day_master_jia",
                operator="==",
                value=True,
            ),
            required_factors=["day_master_jia"],
            result=ConfigRuleResult(
                dimension="personality",
                level="吉",
                conclusion_template_zh="甲木生于春季，性格积极",
            ),
            version="1.0.0",
            engine_id="bazi_rule_engine",
            metadata=make_metadata(),
        )
        assert rule.rule_id == "dts_jia_spring_001"
        assert rule.is_complex_logic is False
        assert rule.priority == 500  # 默认值

    def test_valid_complex_rule(self):
        """测试有效的复杂规则（需要 Python handler）"""
        rule = ConfigRuleDefinition(
            rule_id="complex_tiangan_chong",
            human_label="天干相冲复杂判断",
            category="冲合",
            condition=RuleCondition(
                factor_id="tiangan_chong_flag",
                operator="exists",
                value=True,
            ),
            required_factors=["tiangan_chong_flag"],
            is_complex_logic=True,
            python_handler_ref="evaluate_tiangan_chong",
            result=ConfigRuleResult(
                dimension="运势",
                level="凶",
                conclusion_template_zh="天干相冲",
            ),
            version="1.0.0",
            engine_id="bazi_rule_engine",
            metadata=make_metadata(),
        )
        assert rule.is_complex_logic is True
        assert rule.python_handler_ref == "evaluate_tiangan_chong"

    def test_complex_rule_without_handler_raises_error(self):
        """测试复杂规则未指定 handler 时抛出错误"""
        with pytest.raises(ValueError, match="python_handler_ref required"):
            ConfigRuleDefinition(
                rule_id="bad_complex_rule",
                human_label="错误的复杂规则",
                category="测试",
                condition=RuleCondition(
                    factor_id="test",
                    operator="==",
                    value=True,
                ),
                required_factors=["test"],
                is_complex_logic=True,
                # python_handler_ref 缺失
                result=ConfigRuleResult(
                    dimension="测试",
                    level="中等",
                    conclusion_template_zh="测试",
                ),
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_rule_with_logical_expression(self):
        """测试使用复合逻辑表达式的规则"""
        rule = ConfigRuleDefinition(
            rule_id="compound_rule",
            human_label="复合规则",
            category="测试",
            condition=LogicalExpression(
                operator="AND",
                conditions=[
                    RuleCondition(factor_id="factor_a", operator="==", value=True),
                    RuleCondition(factor_id="factor_b", operator=">", value=0.5),
                ],
            ),
            required_factors=["factor_a", "factor_b"],
            result=ConfigRuleResult(
                dimension="测试",
                level="吉",
                conclusion_template_zh="测试",
            ),
            version="1.0.0",
            engine_id="test",
            metadata=make_metadata(),
        )
        assert isinstance(rule.condition, LogicalExpression)

    def test_invalid_rule_id_pattern(self):
        """测试无效的 rule_id 格式"""
        with pytest.raises(ValidationError):
            ConfigRuleDefinition(
                rule_id="Invalid-Rule-ID",  # 不能包含连字符
                human_label="测试",
                category="测试",
                condition=RuleCondition(
                    factor_id="test",
                    operator="==",
                    value=True,
                ),
                required_factors=["test"],
                result=ConfigRuleResult(
                    dimension="测试",
                    level="中等",
                    conclusion_template_zh="测试",
                ),
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_priority_bounds(self):
        """测试优先级边界"""
        # 有效边界
        rule = ConfigRuleDefinition(
            rule_id="test_priority_min",
            human_label="测试",
            category="测试",
            condition=RuleCondition(factor_id="test", operator="==", value=True),
            required_factors=["test"],
            result=ConfigRuleResult(
                dimension="测试", level="中等", conclusion_template_zh="测试"
            ),
            priority=0,
            version="1.0.0",
            engine_id="test",
            metadata=make_metadata(),
        )
        assert rule.priority == 0

        rule = ConfigRuleDefinition(
            rule_id="test_priority_max",
            human_label="测试",
            category="测试",
            condition=RuleCondition(factor_id="test", operator="==", value=True),
            required_factors=["test"],
            result=ConfigRuleResult(
                dimension="测试", level="中等", conclusion_template_zh="测试"
            ),
            priority=999,
            version="1.0.0",
            engine_id="test",
            metadata=make_metadata(),
        )
        assert rule.priority == 999

        # 超出边界
        with pytest.raises(ValidationError):
            ConfigRuleDefinition(
                rule_id="test_priority_over",
                human_label="测试",
                category="测试",
                condition=RuleCondition(factor_id="test", operator="==", value=True),
                required_factors=["test"],
                result=ConfigRuleResult(
                    dimension="测试", level="中等", conclusion_template_zh="测试"
                ),
                priority=1000,
                version="1.0.0",
                engine_id="test",
                metadata=make_metadata(),
            )

    def test_exclusive_group(self):
        """测试互斥组"""
        rule = ConfigRuleDefinition(
            rule_id="test_exclusive",
            human_label="测试",
            category="测试",
            condition=RuleCondition(factor_id="test", operator="==", value=True),
            required_factors=["test"],
            result=ConfigRuleResult(
                dimension="测试", level="中等", conclusion_template_zh="测试"
            ),
            exclusive_group="day_master_strength",
            version="1.0.0",
            engine_id="test",
            metadata=make_metadata(),
        )
        assert rule.exclusive_group == "day_master_strength"
