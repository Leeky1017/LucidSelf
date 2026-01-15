"""
Tests for Cross Domain Models

对照文档: openspec/specs/schema-core/spec.md §Requirement 4
"""

import pytest
from pydantic import ValidationError

from backend.core.contracts.cross_domain_models import CrossDomainAxes


class TestCrossDomainAxes:
    """CrossDomainAxes 模型测试"""
    
    def test_valid_instance_full(self):
        """测试完整有效实例创建"""
        axes = CrossDomainAxes(
            life_domain=["career", "health"],
            time_horizon="short_term",
            advice_type=["action", "reflection"]
        )
        assert axes.life_domain == ["career", "health"]
        assert axes.time_horizon == "short_term"
        assert axes.advice_type == ["action", "reflection"]
    
    def test_empty_instance(self):
        """测试空实例（全部默认值）"""
        axes = CrossDomainAxes()
        assert axes.life_domain == []
        assert axes.time_horizon is None
        assert axes.advice_type == []
    
    def test_partial_instance(self):
        """测试部分填充实例"""
        axes = CrossDomainAxes(
            life_domain=["career"]
        )
        assert axes.life_domain == ["career"]
        assert axes.time_horizon is None
        assert axes.advice_type == []
    
    def test_time_horizon_enum_values(self):
        """测试 time_horizon 枚举值"""
        valid_horizons = ["short_term", "medium_term", "long_term"]
        for horizon in valid_horizons:
            axes = CrossDomainAxes(time_horizon=horizon)
            assert axes.time_horizon == horizon
    
    def test_time_horizon_invalid(self):
        """测试无效的 time_horizon 值"""
        with pytest.raises(ValidationError):
            CrossDomainAxes(time_horizon="invalid_horizon")
    
    def test_life_domain_multiple_values(self):
        """测试 life_domain 多个值"""
        axes = CrossDomainAxes(
            life_domain=["career", "health", "relationship", "wealth"]
        )
        assert len(axes.life_domain) == 4
    
    def test_advice_type_multiple_values(self):
        """测试 advice_type 多个值"""
        axes = CrossDomainAxes(
            advice_type=["action", "reflection", "warning", "opportunity"]
        )
        assert len(axes.advice_type) == 4
    
    def test_json_serialization(self):
        """测试 JSON 序列化"""
        axes = CrossDomainAxes(
            life_domain=["career"],
            time_horizon="long_term",
            advice_type=["reflection"]
        )
        json_data = axes.model_dump()
        assert json_data["life_domain"] == ["career"]
        assert json_data["time_horizon"] == "long_term"
        assert json_data["advice_type"] == ["reflection"]
