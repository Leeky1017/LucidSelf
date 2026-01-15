# backend/calculators/ziwei/tests/test_calculator.py
"""
Unit tests for ZiweiCalculator.

Tests cover:
- Basic calculation flow
- Lunar calendar conversion
- Palace placement
- Star placement
- Sihua (four transformations)
- Decade calculation
- Input validation
- Factor matrix output
"""

import pytest
from datetime import datetime

from backend.calculators.ziwei import (
    ZiweiCalculator,
    ZiweiInput,
    ZiweiFactors,
)


class TestZiweiCalculator:
    """Tests for ZiweiCalculator main class."""
    
    @pytest.fixture
    def calculator(self):
        return ZiweiCalculator()
    
    @pytest.fixture
    def sample_input(self):
        return ZiweiInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
    
    def test_basic_calculation(self, calculator, sample_input):
        """Test basic calculation returns valid result."""
        result = calculator.calculate(sample_input)
        
        assert isinstance(result, ZiweiFactors)
        assert result.lunar_year == 1990
        assert result.lunar_month == 4
        assert result.lunar_day == 21
        assert result.year_stem == "庚"
        assert result.year_branch == "午"
    
    def test_five_element_calculation(self, calculator, sample_input):
        """Test five element type calculation."""
        result = calculator.calculate(sample_input)
        
        assert result.five_element_type in [
            "水二局", "木三局", "金四局", "土五局", "火六局"
        ]
        assert result.five_element_number in [2, 3, 4, 5, 6]

    
    def test_palace_placement(self, calculator, sample_input):
        """Test twelve palaces are correctly placed."""
        result = calculator.calculate(sample_input)
        
        # Should have 12 palaces
        assert len(result.palaces) == 12
        
        # Check palace names
        expected_palaces = [
            "命宫", "兄弟宫", "夫妻宫", "子女宫", "财帛宫", "疾厄宫",
            "迁移宫", "交友宫", "官禄宫", "田宅宫", "福德宫", "父母宫"
        ]
        for palace_name in expected_palaces:
            assert palace_name in result.palaces
    
    def test_main_stars_placement(self, calculator, sample_input):
        """Test fourteen main stars are placed."""
        result = calculator.calculate(sample_input)
        
        # Should have 14 main stars
        assert len(result.main_stars) == 14
        
        # Check key stars exist
        expected_stars = ["紫微", "天机", "太阳", "武曲", "天同", "廉贞",
                         "天府", "太阴", "贪狼", "巨门", "天相", "天梁",
                         "七杀", "破军"]
        for star in expected_stars:
            assert star in result.main_stars
    
    def test_natal_sihua(self, calculator, sample_input):
        """Test natal sihua (four transformations) calculation."""
        result = calculator.calculate(sample_input)
        
        # Should have 4 sihua
        assert len(result.sihua_natal) == 4
        
        # Check sihua types
        assert "化禄" in result.sihua_natal
        assert "化权" in result.sihua_natal
        assert "化科" in result.sihua_natal
        assert "化忌" in result.sihua_natal
        
        # For 庚年, sihua should be: 太阳化禄, 武曲化权, 太阴化科, 天同化忌
        assert result.sihua_natal["化禄"] == "太阳"
        assert result.sihua_natal["化权"] == "武曲"
        assert result.sihua_natal["化科"] == "太阴"
        assert result.sihua_natal["化忌"] == "天同"
    
    def test_decade_calculation(self, calculator, sample_input):
        """Test decade (大限) calculation."""
        result = calculator.calculate(sample_input)
        
        # Should have decade list
        assert len(result.decade_list) > 0
        
        # Check decade direction
        assert result.decade_direction in ["forward", "backward"]
        
        # Check start decade age
        assert result.start_decade_age >= 1
        assert result.start_decade_age <= 5
    
    def test_factor_matrix_output(self, calculator, sample_input):
        """Test to_factor_matrix() output."""
        result = calculator.calculate(sample_input)
        factor_matrix = result.to_factor_matrix()
        
        # Check engine ID
        assert factor_matrix.engine_id == "ziwei-calculator"
        
        # Check factors exist
        assert len(factor_matrix.factors) > 0
        
        # Check key factors
        assert "ziwei_five_element_type" in factor_matrix.factors
        assert "ziwei_ming_palace_branch" in factor_matrix.factors
        assert "ziwei_body_palace" in factor_matrix.factors
    
    def test_calculation_performance(self, calculator, sample_input):
        """Test calculation completes within 50ms."""
        result = calculator.calculate(sample_input)
        
        # Should complete within 50ms
        assert result.calculation_time_ms < 50


class TestInputValidation:
    """Tests for input validation."""
    
    @pytest.fixture
    def calculator(self):
        return ZiweiCalculator()
    
    def test_invalid_year_too_early(self, calculator):
        """Test rejection of dates before 1900."""
        input_data = ZiweiInput(
            birth_datetime=datetime(1899, 1, 1, 12, 0),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        with pytest.raises(ValueError, match="out of supported range"):
            calculator.calculate(input_data)
    
    def test_invalid_year_too_late(self, calculator):
        """Test rejection of dates after 2100."""
        input_data = ZiweiInput(
            birth_datetime=datetime(2101, 1, 1, 12, 0),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        with pytest.raises(ValueError, match="out of supported range"):
            calculator.calculate(input_data)
    
    def test_invalid_longitude(self, calculator):
        """Test rejection of invalid longitude."""
        input_data = ZiweiInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(200.0, 39.9),  # Invalid longitude
            gender="male"
        )
        
        with pytest.raises(ValueError, match="Longitude out of range"):
            calculator.calculate(input_data)
    
    def test_invalid_latitude(self, calculator):
        """Test rejection of invalid latitude."""
        input_data = ZiweiInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 100.0),  # Invalid latitude
            gender="male"
        )
        
        with pytest.raises(ValueError, match="Latitude out of range"):
            calculator.calculate(input_data)



class TestTimezoneConversion:
    """Tests for timezone conversion."""
    
    @pytest.fixture
    def calculator(self):
        return ZiweiCalculator()
    
    def test_timezone_conversion_new_york(self, calculator):
        """Test timezone conversion from New York."""
        # New York is UTC-5 (or UTC-4 in DST)
        # 2024-06-15 10:00 New York = 2024-06-15 22:00 Beijing
        input_data = ZiweiInput(
            birth_datetime=datetime(2024, 6, 15, 10, 0),
            birth_location=(-74.0, 40.7),  # New York
            gender="female",
            timezone="America/New_York"
        )
        
        result = calculator.calculate(input_data)
        
        # Should calculate based on Beijing time
        assert isinstance(result, ZiweiFactors)
    
    def test_no_timezone_assumes_beijing(self, calculator):
        """Test that no timezone assumes Beijing time."""
        input_data = ZiweiInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
            # No timezone specified
        )
        
        result = calculator.calculate(input_data)
        
        # Should work without timezone
        assert result.hour_branch == "未"  # 14:30 is 未时


class TestDifferentBirthYears:
    """Tests for different birth years to verify accuracy."""
    
    @pytest.fixture
    def calculator(self):
        return ZiweiCalculator()
    
    def test_jia_year_sihua(self, calculator):
        """Test sihua for 甲 year."""
        # 1984 is 甲子年
        input_data = ZiweiInput(
            birth_datetime=datetime(1984, 3, 15, 12, 0),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        
        # 甲年四化: 廉贞化禄, 破军化权, 武曲化科, 太阳化忌
        assert result.sihua_natal["化禄"] == "廉贞"
        assert result.sihua_natal["化权"] == "破军"
        assert result.sihua_natal["化科"] == "武曲"
        assert result.sihua_natal["化忌"] == "太阳"
    
    def test_yi_year_sihua(self, calculator):
        """Test sihua for 乙 year."""
        # 1985 is 乙丑年
        input_data = ZiweiInput(
            birth_datetime=datetime(1985, 3, 15, 12, 0),
            birth_location=(116.4, 39.9),
            gender="female"
        )
        
        result = calculator.calculate(input_data)
        
        # 乙年四化: 天机化禄, 天梁化权, 紫微化科, 太阴化忌
        assert result.sihua_natal["化禄"] == "天机"
        assert result.sihua_natal["化权"] == "天梁"
        assert result.sihua_natal["化科"] == "紫微"
        assert result.sihua_natal["化忌"] == "太阴"
    
    def test_decade_direction_yang_male(self, calculator):
        """Test decade direction for yang year male (should be forward)."""
        # 1984 甲子年 is yang year
        input_data = ZiweiInput(
            birth_datetime=datetime(1984, 3, 15, 12, 0),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        
        # Yang year + male = forward
        assert result.decade_direction == "forward"
    
    def test_decade_direction_yang_female(self, calculator):
        """Test decade direction for yang year female (should be backward)."""
        # 1984 甲子年 is yang year
        input_data = ZiweiInput(
            birth_datetime=datetime(1984, 3, 15, 12, 0),
            birth_location=(116.4, 39.9),
            gender="female"
        )
        
        result = calculator.calculate(input_data)
        
        # Yang year + female = backward
        assert result.decade_direction == "backward"
