"""
EngineDescriptor Tests

测试引擎描述符模型的验证功能。
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from backend.core.contracts.engine_models import EngineDescriptor
from backend.core.engines.constraints import (
    validate_engine_descriptor,
    validate_engine_id,
    validate_version,
    validate_supported_systems,
    validate_default_weight,
    validate_status,
)


class TestEngineDescriptorCreation:
    """测试 EngineDescriptor 创建"""
    
    def test_valid_calculator_engine(self):
        """测试创建有效的 Calculator 引擎"""
        descriptor = EngineDescriptor(
            engine_id="bazi_calculator",
            kind="calculator",
            supported_dimensions=["事业", "财富", "婚姻", "健康"],
            supported_systems=["bazi"],
            default_weight=1.0,
            status="active",
            owner_team="engine",
            version="1.0.0",
        )
        assert descriptor.engine_id == "bazi_calculator"
        assert descriptor.kind == "calculator"
        assert descriptor.status.value == "active"
    
    def test_valid_fusion_engine_with_depends_on(self):
        """测试创建有效的 Fusion 引擎（含依赖）"""
        descriptor = EngineDescriptor(
            engine_id="cross_system_fusion",
            kind="fusion",
            supported_dimensions=["事业", "财富"],
            supported_systems=["bazi", "astro"],
            depends_on=["bazi_rule_engine", "astro_rule_engine"],
            default_weight=1.5,
            status="active",
            owner_team="engine",
            version="1.0.0",
        )
        assert descriptor.depends_on == ["bazi_rule_engine", "astro_rule_engine"]
    
    def test_default_values(self):
        """测试默认值"""
        descriptor = EngineDescriptor(
            engine_id="test_engine",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            owner_team="engine",
            version="1.0.0",
        )
        assert descriptor.default_weight == 1.0
        assert descriptor.depends_on == []
        assert descriptor.avg_execution_time_ms is None


class TestEngineIdValidation:
    """测试 engine_id 验证"""
    
    def test_valid_engine_ids(self):
        """测试有效的 engine_id"""
        valid_ids = [
            "bazi_calculator",
            "bazi-calculator",
            "ziwei_semantic",
            "a",
            "abc123",
            "test_engine_v2",
        ]
        for engine_id in valid_ids:
            assert validate_engine_id(engine_id) is None
    
    def test_invalid_engine_id_uppercase(self):
        """测试大写字母拒绝"""
        error = validate_engine_id("Bazi_Calculator")
        assert error is not None
        assert "must match pattern" in error
    
    def test_invalid_engine_id_whitespace(self):
        """测试空格拒绝"""
        error = validate_engine_id("bazi calculator")
        assert error is not None
    
    def test_invalid_engine_id_starts_with_number(self):
        """测试数字开头拒绝"""
        error = validate_engine_id("123engine")
        assert error is not None
    
    def test_invalid_engine_id_empty(self):
        """测试空字符串拒绝"""
        error = validate_engine_id("")
        assert error is not None
        assert "cannot be empty" in error
    
    def test_pydantic_rejects_invalid_engine_id(self):
        """测试 Pydantic 模型拒绝无效 engine_id"""
        with pytest.raises(ValidationError):
            EngineDescriptor(
                engine_id="Invalid-ID",
                kind="calculator",
                supported_dimensions=["事业"],
                supported_systems=["bazi"],
                owner_team="engine",
                version="1.0.0",
            )


class TestVersionValidation:
    """测试版本号验证"""
    
    def test_valid_versions(self):
        """测试有效版本号"""
        valid_versions = ["1.0.0", "0.1.0", "10.20.30", "1.0.1"]
        for version in valid_versions:
            assert validate_version(version) is None
    
    def test_invalid_version_format(self):
        """测试无效版本格式"""
        invalid_versions = ["1.0", "v1.0.0", "1.0.0-beta", "1.0.0.0"]
        for version in invalid_versions:
            error = validate_version(version)
            assert error is not None
    
    def test_pydantic_rejects_invalid_version(self):
        """测试 Pydantic 模型拒绝无效版本"""
        with pytest.raises(ValidationError):
            EngineDescriptor(
                engine_id="test_engine",
                kind="calculator",
                supported_dimensions=["事业"],
                supported_systems=["bazi"],
                owner_team="engine",
                version="invalid",
            )


class TestWeightValidation:
    """测试权重验证"""
    
    def test_valid_weights(self):
        """测试有效权重"""
        valid_weights = [0.0, 1.0, 5.5, 10.0]
        for weight in valid_weights:
            assert validate_default_weight(weight) is None
    
    def test_boundary_weight_0(self):
        """测试边界值 0.0"""
        descriptor = EngineDescriptor(
            engine_id="test_engine",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            default_weight=0.0,
            owner_team="engine",
            version="1.0.0",
        )
        assert descriptor.default_weight == 0.0
    
    def test_boundary_weight_10(self):
        """测试边界值 10.0"""
        descriptor = EngineDescriptor(
            engine_id="test_engine",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            default_weight=10.0,
            owner_team="engine",
            version="1.0.0",
        )
        assert descriptor.default_weight == 10.0
    
    def test_invalid_weight_negative(self):
        """测试负数权重拒绝"""
        error = validate_default_weight(-1.0)
        assert error is not None
    
    def test_invalid_weight_too_high(self):
        """测试超出上限拒绝"""
        error = validate_default_weight(10.1)
        assert error is not None
    
    def test_pydantic_rejects_invalid_weight(self):
        """测试 Pydantic 模型拒绝无效权重"""
        with pytest.raises(ValidationError):
            EngineDescriptor(
                engine_id="test_engine",
                kind="calculator",
                supported_dimensions=["事业"],
                supported_systems=["bazi"],
                default_weight=15.0,
                owner_team="engine",
                version="1.0.0",
            )


class TestSupportedSystemsValidation:
    """测试支持体系验证"""
    
    def test_valid_systems(self):
        """测试有效体系"""
        assert validate_supported_systems(["bazi"]) is None
        assert validate_supported_systems(["bazi", "ziwei"]) is None
    
    def test_empty_systems_rejected(self):
        """测试空列表拒绝"""
        error = validate_supported_systems([])
        assert error is not None
        assert "cannot be empty" in error


class TestStatusValidation:
    """测试状态验证"""
    
    def test_valid_statuses(self):
        """测试有效状态"""
        for status in ["active", "experimental", "deprecated"]:
            assert validate_status(status) is None
    
    def test_invalid_status(self):
        """测试无效状态"""
        error = validate_status("unknown")
        assert error is not None


class TestDependsOnField:
    """测试 depends_on 字段"""
    
    def test_empty_depends_on(self):
        """测试空依赖列表"""
        descriptor = EngineDescriptor(
            engine_id="test_engine",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            depends_on=[],
            owner_team="engine",
            version="1.0.0",
        )
        assert descriptor.depends_on == []
    
    def test_multiple_dependencies(self):
        """测试多个依赖"""
        descriptor = EngineDescriptor(
            engine_id="fusion_engine",
            kind="fusion",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            depends_on=["bazi_calculator", "bazi_semantic", "bazi_rule_engine"],
            owner_team="engine",
            version="1.0.0",
        )
        assert len(descriptor.depends_on) == 3


class TestValidateEngineDescriptor:
    """测试完整描述符验证"""
    
    def test_valid_descriptor_no_violations(self):
        """测试有效描述符无违规"""
        descriptor = EngineDescriptor(
            engine_id="test_engine",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            owner_team="engine",
            version="1.0.0",
        )
        violations = validate_engine_descriptor(descriptor)
        assert violations == []
