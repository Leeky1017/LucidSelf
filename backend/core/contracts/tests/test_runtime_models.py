"""
Tests for Runtime Models

对照文档: docs/数据契约_Schema定义规范_v1.md §1.1, §2.1
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from backend.core.contracts import (
    FactorMatrix,
    FactorValue,
    RuntimeRuleResult,
)


# =============================================================================
# FactorValue 测试
# =============================================================================


class TestFactorValue:
    """FactorValue 模型测试"""

    def test_valid_boolean_value(self):
        """测试有效的布尔值因子"""
        fv = FactorValue(
            factor_id="day_master_jia",
            value=True,
            confidence=1.0,
            source="calculator",
        )
        assert fv.factor_id == "day_master_jia"
        assert fv.value is True
        assert fv.confidence == 1.0
        assert fv.source == "calculator"

    def test_valid_string_value(self):
        """测试有效的字符串值因子"""
        fv = FactorValue(
            factor_id="season",
            value="spring",
            confidence=0.95,
            source="calculator",
        )
        assert fv.value == "spring"

    def test_valid_float_value(self):
        """测试有效的浮点值因子"""
        fv = FactorValue(
            factor_id="strength_score",
            value=0.75,
            confidence=0.8,
            source="semantic",
        )
        assert fv.value == 0.75

    def test_confidence_bounds(self):
        """测试置信度边界"""
        # 有效边界
        fv = FactorValue(
            factor_id="test",
            value=True,
            confidence=0.0,
            source="test",
        )
        assert fv.confidence == 0.0

        fv = FactorValue(
            factor_id="test",
            value=True,
            confidence=1.0,
            source="test",
        )
        assert fv.confidence == 1.0

        # 超出边界
        with pytest.raises(ValidationError):
            FactorValue(
                factor_id="test",
                value=True,
                confidence=1.5,  # 超出 1.0
                source="test",
            )

        with pytest.raises(ValidationError):
            FactorValue(
                factor_id="test",
                value=True,
                confidence=-0.1,  # 低于 0.0
                source="test",
            )

    def test_different_sources(self):
        """测试不同来源"""
        sources = ["calculator", "semantic", "manual", "llm_infer"]
        for src in sources:
            fv = FactorValue(
                factor_id="test",
                value=True,
                confidence=0.8,
                source=src,
            )
            assert fv.source == src

    def test_complex_value_types(self):
        """测试复杂值类型"""
        # 列表值
        fv = FactorValue(
            factor_id="tiangan_list",
            value=["甲", "乙", "丙"],
            confidence=1.0,
            source="calculator",
        )
        assert len(fv.value) == 3

        # 字典值
        fv = FactorValue(
            factor_id="palace_info",
            value={"name": "命宫", "stars": ["紫微", "天府"]},
            confidence=0.9,
            source="calculator",
        )
        assert fv.value["name"] == "命宫"


# =============================================================================
# FactorMatrix 测试
# =============================================================================


class TestFactorMatrix:
    """FactorMatrix 模型测试"""

    def test_valid_matrix(self):
        """测试有效的因子矩阵"""
        matrix = FactorMatrix(
            factors={
                "day_master_jia": FactorValue(
                    factor_id="day_master_jia",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
                "season": FactorValue(
                    factor_id="season",
                    value="spring",
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="bazi_calculator",
        )
        assert len(matrix.factors) == 2
        assert matrix.engine_id == "bazi_calculator"

    def test_get_method(self):
        """测试 get 方法"""
        matrix = FactorMatrix(
            factors={
                "day_master_jia": FactorValue(
                    factor_id="day_master_jia",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="test",
        )
        
        # 存在的因子
        fv = matrix.get("day_master_jia")
        assert fv is not None
        assert fv.value is True
        
        # 不存在的因子
        fv = matrix.get("non_existent")
        assert fv is None

    def test_has_method(self):
        """测试 has 方法"""
        matrix = FactorMatrix(
            factors={
                "day_master_jia": FactorValue(
                    factor_id="day_master_jia",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="test",
        )
        
        assert matrix.has("day_master_jia") is True
        assert matrix.has("non_existent") is False

    def test_empty_matrix(self):
        """测试空因子矩阵"""
        matrix = FactorMatrix(
            factors={},
            engine_id="test",
        )
        assert len(matrix.factors) == 0
        assert matrix.has("any_factor") is False

    def test_timestamp_default(self):
        """测试时间戳默认值"""
        before = datetime.now()
        matrix = FactorMatrix(
            factors={},
            engine_id="test",
        )
        after = datetime.now()
        
        assert before <= matrix.timestamp <= after

    def test_custom_timestamp(self):
        """测试自定义时间戳"""
        custom_time = datetime(2025, 1, 1, 12, 0, 0)
        matrix = FactorMatrix(
            factors={},
            timestamp=custom_time,
            engine_id="test",
        )
        assert matrix.timestamp == custom_time


# =============================================================================
# RuntimeRuleResult 测试
# =============================================================================


class TestRuntimeRuleResult:
    """RuntimeRuleResult 模型测试"""

    def test_valid_matched_result(self):
        """测试有效的匹配结果"""
        result = RuntimeRuleResult(
            rule_id="dts_jia_spring_001",
            matched=True,
            dimension="personality",
            level="吉",
            description="甲木生于春季，木气当令，性格积极向上",
            confidence=0.85,
            weight=1.5,
            tags=["personality", "positive"],
            evidence_factors=["day_master_jia", "season_spring"],
            semantic_refs=["bazi_semantic_001"],
            source_book="ditianshui",
            l1_anchor="DTS_L1_025",
            execution_time_ms=2.5,
        )
        assert result.rule_id == "dts_jia_spring_001"
        assert result.matched is True
        assert result.dimension == "personality"

    def test_valid_not_matched_result(self):
        """测试有效的未匹配结果"""
        result = RuntimeRuleResult(
            rule_id="dts_jia_spring_001",
            matched=False,
            confidence=1.0,
            weight=0.0,
            execution_time_ms=1.0,
        )
        assert result.matched is False
        assert result.dimension is None
        assert result.level is None

    def test_not_matched_factory(self):
        """测试 not_matched 快捷方法"""
        result = RuntimeRuleResult.not_matched(
            rule_id="test_rule",
            execution_time_ms=0.5,
        )
        assert result.matched is False
        assert result.rule_id == "test_rule"
        assert result.confidence == 1.0
        assert result.weight == 0.0
        assert result.execution_time_ms == 0.5

    def test_confidence_bounds(self):
        """测试置信度边界"""
        # 有效边界
        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            confidence=0.0,
            weight=1.0,
            execution_time_ms=1.0,
        )
        assert result.confidence == 0.0

        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            confidence=1.0,
            weight=1.0,
            execution_time_ms=1.0,
        )
        assert result.confidence == 1.0

        # 超出边界
        with pytest.raises(ValidationError):
            RuntimeRuleResult(
                rule_id="test",
                matched=True,
                confidence=1.5,
                weight=1.0,
                execution_time_ms=1.0,
            )

    def test_weight_bounds(self):
        """测试权重边界"""
        # 有效边界
        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            confidence=0.8,
            weight=0.0,
            execution_time_ms=1.0,
        )
        assert result.weight == 0.0

        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            confidence=0.8,
            weight=10.0,
            execution_time_ms=1.0,
        )
        assert result.weight == 10.0

        # 超出边界
        with pytest.raises(ValidationError):
            RuntimeRuleResult(
                rule_id="test",
                matched=True,
                confidence=0.8,
                weight=11.0,
                execution_time_ms=1.0,
            )

    def test_optional_fields_when_matched(self):
        """测试匹配时的可选字段"""
        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            dimension="事业",
            level="吉",
            description="测试结论",
            confidence=0.8,
            weight=1.0,
            tags=["test"],
            evidence_factors=["factor_a"],
            semantic_refs=["sem_001"],
            source_book="test_book",
            l1_anchor="TEST_001",
            execution_time_ms=1.0,
        )
        assert result.source_book == "test_book"
        assert result.l1_anchor == "TEST_001"

    def test_empty_lists_by_default(self):
        """测试列表字段默认为空"""
        result = RuntimeRuleResult(
            rule_id="test",
            matched=False,
            confidence=1.0,
            weight=0.0,
            execution_time_ms=1.0,
        )
        assert result.tags == []
        assert result.evidence_factors == []
        assert result.semantic_refs == []

    def test_execution_time_required(self):
        """测试 execution_time_ms 是必填字段"""
        with pytest.raises(ValidationError):
            RuntimeRuleResult(
                rule_id="test",
                matched=False,
                confidence=1.0,
                weight=0.0,
                # execution_time_ms 缺失
            )

    def test_all_levels(self):
        """测试各种吉凶等级"""
        levels = ["大吉", "吉", "中等", "凶", "大凶"]
        for level in levels:
            result = RuntimeRuleResult(
                rule_id="test",
                matched=True,
                level=level,
                confidence=0.8,
                weight=1.0,
                execution_time_ms=1.0,
            )
            assert result.level == level

    def test_cross_domain_axes_with_value(self):
        """测试带 cross_domain_axes 的结果（schema-core spec v0.4.0）"""
        from backend.core.contracts.cross_domain_models import CrossDomainAxes
        
        axes = CrossDomainAxes(
            life_domain=["career", "health"],
            time_horizon="short_term",
            advice_type=["action"]
        )
        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            confidence=0.8,
            weight=1.0,
            execution_time_ms=1.0,
            cross_domain_axes=axes,
        )
        assert result.cross_domain_axes is not None
        assert result.cross_domain_axes.life_domain == ["career", "health"]
        assert result.cross_domain_axes.time_horizon == "short_term"

    def test_cross_domain_axes_none_by_default(self):
        """测试 cross_domain_axes 默认为 None（向后兼容）"""
        result = RuntimeRuleResult(
            rule_id="test",
            matched=False,
            confidence=1.0,
            weight=0.0,
            execution_time_ms=1.0,
        )
        assert result.cross_domain_axes is None

    def test_cross_domain_axes_dict_input(self):
        """测试 cross_domain_axes 接受字典输入"""
        result = RuntimeRuleResult(
            rule_id="test",
            matched=True,
            confidence=0.8,
            weight=1.0,
            execution_time_ms=1.0,
            cross_domain_axes={
                "life_domain": ["career"],
                "time_horizon": "long_term",
                "advice_type": ["reflection"]
            },
        )
        assert result.cross_domain_axes is not None
        assert result.cross_domain_axes.time_horizon == "long_term"
