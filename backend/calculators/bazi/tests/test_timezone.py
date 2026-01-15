"""时区转换测试."""
import pytest
from datetime import datetime
from backend.calculators.bazi import BaziCalculator, BaziInput


class TestTimezoneSupport:
    """测试时区支持."""
    
    def setup_method(self):
        self.calculator = BaziCalculator()
    
    def test_beijing_timezone_explicit(self):
        """显式指定北京时区应与默认行为一致."""
        input_default = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male",
            timezone=None
        )
        input_explicit = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male",
            timezone="Asia/Shanghai"
        )
        
        result_default = self.calculator.calculate(input_default)
        result_explicit = self.calculator.calculate(input_explicit)
        
        assert result_default.day_master == result_explicit.day_master
        assert result_default.four_pillars == result_explicit.four_pillars
    
    def test_new_york_timezone(self):
        """测试纽约时区转换."""
        # 纽约时间 2024-01-15 10:00 = 北京时间 2024-01-15 23:00 (EST, UTC-5)
        input_data = BaziInput(
            birth_datetime=datetime(2024, 1, 15, 10, 0),
            birth_location=(-74.0, 40.7),  # 纽约经纬度
            gender="male",
            timezone="America/New_York"
        )
        
        result = self.calculator.calculate(input_data)
        # 验证计算成功
        assert result.day_master is not None
        assert result.four_pillars is not None
    
    def test_london_timezone(self):
        """测试伦敦时区转换."""
        input_data = BaziInput(
            birth_datetime=datetime(2024, 6, 15, 12, 0),
            birth_location=(0.0, 51.5),  # 伦敦经纬度
            gender="female",
            timezone="Europe/London"
        )
        
        result = self.calculator.calculate(input_data)
        assert result.day_master is not None
    
    def test_sydney_timezone_southern_hemisphere(self):
        """测试悉尼时区（南半球，验证季节不反转）."""
        # 悉尼2月是夏天，但八字仍按北半球节气判断
        input_data = BaziInput(
            birth_datetime=datetime(2024, 2, 15, 10, 0),
            birth_location=(151.2, -33.9),  # 悉尼经纬度
            gender="male",
            timezone="Australia/Sydney"
        )
        
        result = self.calculator.calculate(input_data)
        # 2月15日在立春后，应为寅月（虎月）
        assert result.four_pillars["month"]["branch"] == "寅"
    
    def test_invalid_timezone_raises_error(self):
        """无效时区应抛出错误."""
        with pytest.raises(Exception):
            input_data = BaziInput(
                birth_datetime=datetime(2024, 1, 15, 10, 0),
                birth_location=(116.4, 39.9),
                gender="male",
                timezone="Invalid/Timezone"
            )
            self.calculator.calculate(input_data)
    
    def test_timezone_none_backward_compatible(self):
        """timezone=None 应保持向后兼容."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
            # timezone 不传，默认为 None
        )
        
        result = self.calculator.calculate(input_data)
        assert result.day_master is not None
