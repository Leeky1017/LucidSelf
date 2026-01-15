# backend/calculators/bazi/tests/test_calculator.py
"""
Unit tests for BaziCalculator.

覆盖目标: ≥ 85%
"""

import pytest
from datetime import datetime

from backend.calculators.bazi import BaziCalculator, BaziInput, BaziFactors
from backend.calculators.bazi.models import (
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
    STEM_ELEMENT,
    TEN_GOD_NAMES,
)
from backend.core.contracts import FactorMatrix, FactorValue


class TestBaziCalculator:
    """BaziCalculator 主类测试."""
    
    @pytest.fixture
    def calculator(self):
        return BaziCalculator()
    
    @pytest.fixture
    def sample_input(self):
        """测试用输入: 1990年5月15日14:30 北京"""
        return BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
    
    def test_calculate_returns_bazi_factors(self, calculator, sample_input):
        """测试计算返回正确类型."""
        result = calculator.calculate(sample_input)
        assert isinstance(result, BaziFactors)
    
    def test_four_pillars_structure(self, calculator, sample_input):
        """测试四柱结构完整性."""
        result = calculator.calculate(sample_input)
        
        # 四柱都存在
        assert "year" in result.four_pillars
        assert "month" in result.four_pillars
        assert "day" in result.four_pillars
        assert "hour" in result.four_pillars
        
        # 每柱都有干支
        for pillar in ["year", "month", "day", "hour"]:
            assert "stem" in result.four_pillars[pillar]
            assert "branch" in result.four_pillars[pillar]
            assert result.four_pillars[pillar]["stem"] in HEAVENLY_STEMS
            assert result.four_pillars[pillar]["branch"] in EARTHLY_BRANCHES
    
    def test_day_master_info(self, calculator, sample_input):
        """测试日主信息."""
        result = calculator.calculate(sample_input)
        
        assert result.day_master in HEAVENLY_STEMS
        assert result.day_master_element in ["wood", "fire", "earth", "metal", "water"]
        assert result.day_master_yinyang in ["yin", "yang"]
    
    def test_ten_god_counts(self, calculator, sample_input):
        """测试十神统计."""
        result = calculator.calculate(sample_input)
        
        # 所有十神都有计数
        for god_name in TEN_GOD_NAMES:
            assert god_name in result.ten_god_counts
            assert isinstance(result.ten_god_counts[god_name], int)
            assert result.ten_god_counts[god_name] >= 0
    
    def test_element_scores(self, calculator, sample_input):
        """测试五行强度."""
        result = calculator.calculate(sample_input)
        
        # 五行都有分数
        for element in ["wood", "fire", "earth", "metal", "water"]:
            assert element in result.element_scores
            assert 0.0 <= result.element_scores[element] <= 1.0
        
        # 分数之和约等于1（归一化后）
        total = sum(result.element_scores.values())
        assert 0.99 <= total <= 1.01
    
    def test_day_master_strength(self, calculator, sample_input):
        """测试日主强度."""
        result = calculator.calculate(sample_input)
        
        assert 0.0 <= result.day_master_strength <= 1.0
        assert result.strength_category in ["strong", "weak", "neutral"]
    
    def test_birth_season(self, calculator, sample_input):
        """测试出生季节."""
        result = calculator.calculate(sample_input)
        assert result.birth_season in ["spring", "summer", "autumn", "winter"]
    
    def test_dayun_list(self, calculator, sample_input):
        """测试大运列表."""
        result = calculator.calculate(sample_input)
        
        assert len(result.dayun_list) > 0
        assert result.dayun_direction in ["forward", "backward"]
        
        for dayun in result.dayun_list:
            assert "stem" in dayun
            assert "branch" in dayun
            assert "start_age" in dayun
            assert "end_age" in dayun
    
    def test_calculation_time(self, calculator, sample_input):
        """测试计算时间 < 10ms."""
        result = calculator.calculate(sample_input)
        
        # 单次计算应该 < 10ms
        assert result.calculation_time_ms < 10.0
    
    def test_to_factor_matrix(self, calculator, sample_input):
        """测试转换为 FactorMatrix."""
        result = calculator.calculate(sample_input)
        factor_matrix = result.to_factor_matrix()
        
        assert isinstance(factor_matrix, FactorMatrix)
        assert factor_matrix.engine_id == "bazi-calculator"
        
        # 检查关键因子
        assert "day_master_jia" in factor_matrix.factors
        assert "season_spring" in factor_matrix.factors
        assert "ten_god_zhengguan" in factor_matrix.factors
        assert "element_wood_score" in factor_matrix.factors


class TestInputValidation:
    """输入验证测试."""
    
    @pytest.fixture
    def calculator(self):
        return BaziCalculator()
    
    def test_invalid_year_range(self, calculator):
        """测试超出年份范围."""
        with pytest.raises(ValueError, match="Date out of supported range"):
            calculator.calculate(BaziInput(
                birth_datetime=datetime(1800, 5, 15, 14, 30),
                birth_location=(116.4, 39.9),
                gender="male"
            ))
    
    def test_invalid_longitude(self, calculator):
        """测试经度超范围."""
        with pytest.raises(ValueError, match="Longitude out of range"):
            calculator.calculate(BaziInput(
                birth_datetime=datetime(1990, 5, 15, 14, 30),
                birth_location=(200.0, 39.9),
                gender="male"
            ))
    
    def test_invalid_latitude(self, calculator):
        """测试纬度超范围."""
        with pytest.raises(ValueError, match="Latitude out of range"):
            calculator.calculate(BaziInput(
                birth_datetime=datetime(1990, 5, 15, 14, 30),
                birth_location=(116.4, 100.0),
                gender="male"
            ))


class TestKnownBaziCases:
    """已知八字案例测试（Golden Set）."""
    
    @pytest.fixture
    def calculator(self):
        return BaziCalculator()
    
    def test_case_1990_05_15(self, calculator):
        """测试: 1990年5月15日14:30 北京
        
        预期: 庚午年 辛巳月 (待确认日时柱)
        """
        result = calculator.calculate(BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        ))
        
        # 1990年是庚午年
        assert result.four_pillars["year"]["stem"] == "庚"
        assert result.four_pillars["year"]["branch"] == "午"
        
        # 5月15日在立夏之后、芒种之前，属于巳月
        assert result.four_pillars["month"]["branch"] == "巳"
    
    def test_before_lichun(self, calculator):
        """测试立春前出生（属于上一年）.
        
        2000年1月15日，立春在2月4日，应该属于1999年己卯年
        """
        result = calculator.calculate(BaziInput(
            birth_datetime=datetime(2000, 1, 15, 12, 0),
            birth_location=(116.4, 39.9),
            gender="male"
        ))
        
        # 立春前，年柱应该是上一年（1999年己卯年）
        assert result.four_pillars["year"]["stem"] == "己"
        assert result.four_pillars["year"]["branch"] == "卯"


class TestPerformance:
    """性能测试."""
    
    def test_batch_calculation(self):
        """批量计算性能测试."""
        calculator = BaziCalculator()
        
        times = []
        for i in range(100):
            result = calculator.calculate(BaziInput(
                birth_datetime=datetime(1990 + i % 30, (i % 12) + 1, (i % 28) + 1, i % 24, 0),
                birth_location=(116.4, 39.9),
                gender="male" if i % 2 == 0 else "female"
            ))
            times.append(result.calculation_time_ms)
        
        avg_time = sum(times) / len(times)
        p95_time = sorted(times)[95]
        
        # P95 应该 < 10ms
        assert p95_time < 10.0, f"P95 time {p95_time}ms exceeds 10ms"
        
        print(f"\nPerformance: avg={avg_time:.2f}ms, P95={p95_time:.2f}ms")
