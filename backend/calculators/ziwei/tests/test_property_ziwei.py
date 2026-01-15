# backend/calculators/ziwei/tests/test_property_ziwei.py
"""
Property-based tests for ZiweiCalculator accuracy audit.

Tests validate correctness properties from the design document:
- Property 5: 紫微星位置一致性
- Property 6: 四化表一致性
- Property 19: 紫微天府对称关系
- Property 20: 紫微大限方向正确性

**Feature: calculator-accuracy-audit**
"""

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st
from datetime import datetime
from typing import Dict, Tuple

from backend.calculators.ziwei.star_placement import (
    ZIWEI_TABLE,
    calculate_ziwei_position,
    calculate_tianfu_position,
    place_ziwei_group,
    place_tianfu_group,
    calculate_five_element,
    FIVE_ELEMENT_TABLE,
)
from backend.calculators.ziwei.sihua import (
    SIHUA_TABLE,
    get_sihua_stars,
)
from backend.calculators.ziwei.decade import (
    get_decade_direction,
)
from backend.calculators.ziwei.models import (
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
)
from backend.core.testing.property_tests import (
    property_test,
    heavenly_stem_strategy,
    earthly_branch_strategy,
    gender_strategy,
)


# =============================================================================
# Reference Data: 《紫微斗数全书》标准
# =============================================================================

# 紫微星安置表 - 根据《紫微斗数全书》安星法
# 格式: REFERENCE_ZIWEI_TABLE[五行局数][农历日] = 紫微星地支索引
# 地支索引: 0=子, 1=丑, 2=寅, 3=卯, 4=辰, 5=巳, 6=午, 7=未, 8=申, 9=酉, 10=戌, 11=亥
REFERENCE_ZIWEI_TABLE = {
    2: {  # 水二局
        1: 2, 2: 3, 3: 1, 4: 2, 5: 3, 6: 4, 7: 2, 8: 3, 9: 4, 10: 5,
        11: 3, 12: 4, 13: 5, 14: 6, 15: 4, 16: 5, 17: 6, 18: 7, 19: 5, 20: 6,
        21: 7, 22: 8, 23: 6, 24: 7, 25: 8, 26: 9, 27: 7, 28: 8, 29: 9, 30: 10,
    },
    3: {  # 木三局
        1: 2, 2: 2, 3: 3, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 2, 10: 2,
        11: 3, 12: 4, 13: 5, 14: 3, 15: 3, 16: 4, 17: 5, 18: 6, 19: 4, 20: 4,
        21: 5, 22: 6, 23: 7, 24: 5, 25: 5, 26: 6, 27: 7, 28: 8, 29: 6, 30: 6,
    },
    4: {  # 金四局
        1: 2, 2: 2, 3: 2, 4: 3, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 4,
        11: 2, 12: 2, 13: 2, 14: 3, 15: 4, 16: 5, 17: 3, 18: 3, 19: 3, 20: 4,
        21: 5, 22: 6, 23: 4, 24: 4, 25: 4, 26: 5, 27: 6, 28: 7, 29: 5, 30: 5,
    },
    5: {  # 土五局
        1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 1, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 3, 12: 4, 13: 2, 14: 2, 15: 2, 16: 2, 17: 3, 18: 4, 19: 5, 20: 3,
        21: 3, 22: 3, 23: 3, 24: 4, 25: 5, 26: 6, 27: 4, 28: 4, 29: 4, 30: 4,
    },
    6: {  # 火六局
        1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3, 7: 1, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 3, 14: 4, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 3,
        21: 4, 22: 5, 23: 3, 24: 3, 25: 3, 26: 3, 27: 3, 28: 4, 29: 5, 30: 6,
    },
}

# 四化表 - 根据《紫微斗数全书》标准四化表
# 格式: REFERENCE_SIHUA_TABLE[天干] = (化禄星, 化权星, 化科星, 化忌星)
REFERENCE_SIHUA_TABLE: Dict[str, Tuple[str, str, str, str]] = {
    "甲": ("廉贞", "破军", "武曲", "太阳"),
    "乙": ("天机", "天梁", "紫微", "太阴"),
    "丙": ("天同", "天机", "文昌", "廉贞"),
    "丁": ("太阴", "天同", "天机", "巨门"),
    "戊": ("贪狼", "太阴", "右弼", "天机"),
    "己": ("武曲", "贪狼", "天梁", "文曲"),
    "庚": ("太阳", "武曲", "太阴", "天同"),
    "辛": ("巨门", "太阳", "文曲", "文昌"),
    "壬": ("天梁", "紫微", "左辅", "武曲"),
    "癸": ("破军", "巨门", "太阴", "贪狼"),
}


# =============================================================================
# Property 5: 紫微星位置一致性
# =============================================================================

class TestProperty5ZiweiStarPosition:
    """
    **Feature: calculator-accuracy-audit, Property 5: 紫微星位置一致性**
    **Validates: Requirements 3.1**
    
    *对于任意* 有效的农历日和五行局组合，紫微计算器计算的紫微星位置
    应与《紫微斗数全书》安星法100%一致。
    """
    
    @property_test(
        property_id="5",
        property_name="紫微星位置一致性",
        validates=["3.1"],
        max_examples=100,
    )
    @given(
        five_element_num=st.sampled_from([2, 3, 4, 5, 6]),
        lunar_day=st.integers(min_value=1, max_value=30),
    )
    def test_ziwei_position_matches_reference(
        self, five_element_num: int, lunar_day: int
    ):
        """
        Test that Ziwei star position matches reference table.
        
        **Feature: calculator-accuracy-audit, Property 5: 紫微星位置一致性**
        **Validates: Requirements 3.1**
        """
        # Get expected position from reference table
        expected_position = REFERENCE_ZIWEI_TABLE[five_element_num][lunar_day] % 12
        
        # Get actual position from calculator
        actual_position = calculate_ziwei_position(lunar_day, five_element_num)
        
        assert actual_position == expected_position, (
            f"Ziwei position mismatch for 五行局={five_element_num}, 农历日={lunar_day}: "
            f"expected {EARTHLY_BRANCHES[expected_position]}, "
            f"got {EARTHLY_BRANCHES[actual_position]}"
        )
    
    def test_ziwei_table_completeness(self):
        """
        Test that ZIWEI_TABLE covers all valid combinations.
        
        **Feature: calculator-accuracy-audit, Property 5: 紫微星位置一致性**
        **Validates: Requirements 3.1**
        """
        for five_element_num in [2, 3, 4, 5, 6]:
            for lunar_day in range(1, 31):
                assert five_element_num in ZIWEI_TABLE, (
                    f"Missing five element {five_element_num} in ZIWEI_TABLE"
                )
                assert lunar_day in ZIWEI_TABLE[five_element_num], (
                    f"Missing day {lunar_day} for five element {five_element_num}"
                )
    
    def test_ziwei_table_matches_reference(self):
        """
        Test that implementation table matches reference table exactly.
        
        **Feature: calculator-accuracy-audit, Property 5: 紫微星位置一致性**
        **Validates: Requirements 3.1**
        """
        for five_element_num in [2, 3, 4, 5, 6]:
            for lunar_day in range(1, 31):
                impl_value = ZIWEI_TABLE[five_element_num][lunar_day]
                ref_value = REFERENCE_ZIWEI_TABLE[five_element_num][lunar_day]
                assert impl_value == ref_value, (
                    f"Table mismatch at 五行局={five_element_num}, 日={lunar_day}: "
                    f"impl={impl_value}, ref={ref_value}"
                )


# =============================================================================
# Property 6: 四化表一致性
# =============================================================================

class TestProperty6SihuaTable:
    """
    **Feature: calculator-accuracy-audit, Property 6: 四化表一致性**
    **Validates: Requirements 3.3**
    
    *对于任意* 天干，紫微计算器返回的四化应与《紫微斗数全书》标准四化表100%一致。
    """
    
    @property_test(
        property_id="6",
        property_name="四化表一致性",
        validates=["3.3"],
        max_examples=100,
    )
    @given(stem=heavenly_stem_strategy())
    def test_sihua_matches_reference(self, stem: str):
        """
        Test that sihua for each stem matches reference table.
        
        **Feature: calculator-accuracy-audit, Property 6: 四化表一致性**
        **Validates: Requirements 3.3**
        """
        # Get expected sihua from reference
        expected = REFERENCE_SIHUA_TABLE[stem]
        expected_dict = {
            "化禄": expected[0],
            "化权": expected[1],
            "化科": expected[2],
            "化忌": expected[3],
        }
        
        # Get actual sihua from calculator
        actual_dict = get_sihua_stars(stem)
        
        for sihua_type in ["化禄", "化权", "化科", "化忌"]:
            assert actual_dict[sihua_type] == expected_dict[sihua_type], (
                f"Sihua mismatch for {stem}年 {sihua_type}: "
                f"expected {expected_dict[sihua_type]}, got {actual_dict[sihua_type]}"
            )
    
    def test_sihua_table_completeness(self):
        """
        Test that SIHUA_TABLE covers all 10 heavenly stems.
        
        **Feature: calculator-accuracy-audit, Property 6: 四化表一致性**
        **Validates: Requirements 3.3**
        """
        for stem in HEAVENLY_STEMS:
            assert stem in SIHUA_TABLE, f"Missing stem {stem} in SIHUA_TABLE"
            sihua = SIHUA_TABLE[stem]
            assert len(sihua) == 4, f"Sihua for {stem} should have 4 elements"
    
    def test_sihua_table_matches_reference(self):
        """
        Test that implementation table matches reference table exactly.
        
        **Feature: calculator-accuracy-audit, Property 6: 四化表一致性**
        **Validates: Requirements 3.3**
        """
        for stem in HEAVENLY_STEMS:
            impl_sihua = SIHUA_TABLE[stem]
            ref_sihua = REFERENCE_SIHUA_TABLE[stem]
            assert impl_sihua == ref_sihua, (
                f"Sihua table mismatch for {stem}: impl={impl_sihua}, ref={ref_sihua}"
            )


# =============================================================================
# Property 19: 紫微天府对称关系
# =============================================================================

class TestProperty19ZiweiTianfuSymmetry:
    """
    **Feature: calculator-accuracy-audit, Property 19: 紫微天府对称关系**
    **Validates: Requirements 3.2**
    
    *对于任意* 有效的紫微星位置，天府星位置应与紫微星保持正确的对称关系。
    
    紫微天府对称规则（基于寅申轴对称）：
    - 紫微在子(0)，天府在辰(4)
    - 紫微在丑(1)，天府在卯(3)
    - 紫微在寅(2)，天府在寅(2) - 轴心点
    - 紫微在卯(3)，天府在丑(1)
    - 紫微在辰(4)，天府在子(0)
    - 紫微在巳(5)，天府在亥(11)
    - 紫微在午(6)，天府在戌(10)
    - 紫微在未(7)，天府在酉(9)
    - 紫微在申(8)，天府在申(8) - 轴心点
    - 紫微在酉(9)，天府在未(7)
    - 紫微在戌(10)，天府在午(6)
    - 紫微在亥(11)，天府在巳(5)
    """
    
    # Reference symmetry table: ziwei_position -> tianfu_position
    # Based on 寅申轴 (Yin-Shen axis) symmetry from《紫微斗数全书》
    ZIWEI_TIANFU_SYMMETRY = {
        0: 4,   # 子 -> 辰
        1: 3,   # 丑 -> 卯
        2: 2,   # 寅 -> 寅 (axis point)
        3: 1,   # 卯 -> 丑
        4: 0,   # 辰 -> 子
        5: 11,  # 巳 -> 亥
        6: 10,  # 午 -> 戌
        7: 9,   # 未 -> 酉
        8: 8,   # 申 -> 申 (axis point)
        9: 7,   # 酉 -> 未
        10: 6,  # 戌 -> 午
        11: 5,  # 亥 -> 巳
    }
    
    @property_test(
        property_id="19",
        property_name="紫微天府对称关系",
        validates=["3.2"],
        max_examples=100,
    )
    @given(ziwei_position=st.integers(min_value=0, max_value=11))
    def test_tianfu_symmetry(self, ziwei_position: int):
        """
        Test that Tianfu position maintains correct symmetry with Ziwei.
        
        **Feature: calculator-accuracy-audit, Property 19: 紫微天府对称关系**
        **Validates: Requirements 3.2**
        """
        # Get expected Tianfu position from symmetry table
        expected_tianfu = self.ZIWEI_TIANFU_SYMMETRY[ziwei_position]
        
        # Get actual Tianfu position from calculator
        actual_tianfu = calculate_tianfu_position(ziwei_position)
        
        assert actual_tianfu == expected_tianfu, (
            f"Tianfu symmetry error: Ziwei at {EARTHLY_BRANCHES[ziwei_position]}, "
            f"expected Tianfu at {EARTHLY_BRANCHES[expected_tianfu]}, "
            f"got {EARTHLY_BRANCHES[actual_tianfu]}"
        )
    
    @property_test(
        property_id="19",
        property_name="紫微天府对称关系",
        validates=["3.2"],
        max_examples=100,
    )
    @given(
        five_element_num=st.sampled_from([2, 3, 4, 5, 6]),
        lunar_day=st.integers(min_value=1, max_value=30),
    )
    def test_tianfu_symmetry_in_full_calculation(
        self, five_element_num: int, lunar_day: int
    ):
        """
        Test Tianfu symmetry in full star placement calculation.
        
        **Feature: calculator-accuracy-audit, Property 19: 紫微天府对称关系**
        **Validates: Requirements 3.2**
        """
        # Calculate Ziwei position
        ziwei_pos = calculate_ziwei_position(lunar_day, five_element_num)
        
        # Place Ziwei group and Tianfu group
        ziwei_group = place_ziwei_group(ziwei_pos)
        tianfu_pos = calculate_tianfu_position(ziwei_pos)
        tianfu_group = place_tianfu_group(tianfu_pos)
        
        # Verify Ziwei is at expected position
        assert ziwei_group["紫微"] == ziwei_pos
        
        # Verify Tianfu is at expected symmetric position
        expected_tianfu = self.ZIWEI_TIANFU_SYMMETRY[ziwei_pos]
        assert tianfu_group["天府"] == expected_tianfu, (
            f"Tianfu symmetry error in full calc: "
            f"五行局={five_element_num}, 日={lunar_day}, "
            f"Ziwei at {EARTHLY_BRANCHES[ziwei_pos]}, "
            f"expected Tianfu at {EARTHLY_BRANCHES[expected_tianfu]}, "
            f"got {EARTHLY_BRANCHES[tianfu_group['天府']]}"
        )


# =============================================================================
# Property 20: 紫微大限方向正确性
# =============================================================================

class TestProperty20DecadeDirection:
    """
    **Feature: calculator-accuracy-audit, Property 20: 紫微大限方向正确性**
    **Validates: Requirements 3.5**
    
    *对于任意* 有效的出生年份和性别组合，紫微计算器应正确判断大限方向：
    - 阳年男顺、阴年男逆、阳年女逆、阴年女顺
    
    阳干：甲(0)、丙(2)、戊(4)、庚(6)、壬(8)
    阴干：乙(1)、丁(3)、己(5)、辛(7)、癸(9)
    """
    
    # Yang stems (阳干): 甲丙戊庚壬
    YANG_STEMS = ["甲", "丙", "戊", "庚", "壬"]
    # Yin stems (阴干): 乙丁己辛癸
    YIN_STEMS = ["乙", "丁", "己", "辛", "癸"]
    
    @property_test(
        property_id="20",
        property_name="紫微大限方向正确性",
        validates=["3.5"],
        max_examples=100,
    )
    @given(
        stem=heavenly_stem_strategy(),
        gender=gender_strategy(),
    )
    def test_decade_direction(self, stem: str, gender: str):
        """
        Test that decade direction follows the correct rules.
        
        **Feature: calculator-accuracy-audit, Property 20: 紫微大限方向正确性**
        **Validates: Requirements 3.5**
        
        Rules:
        - 阳年男命：顺行 (forward)
        - 阴年男命：逆行 (backward)
        - 阳年女命：逆行 (backward)
        - 阴年女命：顺行 (forward)
        """
        is_yang_stem = stem in self.YANG_STEMS
        is_male = gender == "male"
        
        # Determine expected direction
        # 阳年男命或阴年女命：顺行
        if is_yang_stem == is_male:
            expected_direction = "forward"
        else:
            expected_direction = "backward"
        
        # Get actual direction from calculator
        actual_direction = get_decade_direction(stem, gender)
        
        assert actual_direction == expected_direction, (
            f"Decade direction error: {stem}年 {gender}, "
            f"expected {expected_direction}, got {actual_direction}"
        )
    
    def test_all_decade_direction_combinations(self):
        """
        Test all 20 combinations of stem and gender.
        
        **Feature: calculator-accuracy-audit, Property 20: 紫微大限方向正确性**
        **Validates: Requirements 3.5**
        """
        expected_results = {
            # Yang stems + male = forward
            ("甲", "male"): "forward",
            ("丙", "male"): "forward",
            ("戊", "male"): "forward",
            ("庚", "male"): "forward",
            ("壬", "male"): "forward",
            # Yang stems + female = backward
            ("甲", "female"): "backward",
            ("丙", "female"): "backward",
            ("戊", "female"): "backward",
            ("庚", "female"): "backward",
            ("壬", "female"): "backward",
            # Yin stems + male = backward
            ("乙", "male"): "backward",
            ("丁", "male"): "backward",
            ("己", "male"): "backward",
            ("辛", "male"): "backward",
            ("癸", "male"): "backward",
            # Yin stems + female = forward
            ("乙", "female"): "forward",
            ("丁", "female"): "forward",
            ("己", "female"): "forward",
            ("辛", "female"): "forward",
            ("癸", "female"): "forward",
        }
        
        for (stem, gender), expected in expected_results.items():
            actual = get_decade_direction(stem, gender)
            assert actual == expected, (
                f"Decade direction error: {stem}年 {gender}, "
                f"expected {expected}, got {actual}"
            )


# =============================================================================
# Lunar Calendar Conversion Tests (Task 3.9)
# =============================================================================

class TestLunarCalendarConversion:
    """
    Tests for lunar calendar conversion accuracy.
    
    Validates Requirements 3.9: 农历转换与权威农历库交叉验证，闰月处理正确
    """
    
    def test_known_lunar_dates(self):
        """
        Test conversion against known lunar dates.
        
        These are verified dates from authoritative sources.
        """
        from backend.calculators.ziwei.lunar_calendar import solar_to_lunar
        
        # Known conversions (verified against multiple sources)
        test_cases = [
            # (solar_date, expected_lunar_year, expected_lunar_month, expected_lunar_day, is_leap)
            (datetime(1990, 5, 15), 1990, 4, 21, False),  # From golden case
            (datetime(2000, 1, 1), 1999, 11, 25, False),  # Y2K
            (datetime(2020, 1, 25), 2020, 1, 1, False),   # Chinese New Year 2020
            (datetime(2021, 2, 12), 2021, 1, 1, False),   # Chinese New Year 2021
            (datetime(2022, 2, 1), 2022, 1, 1, False),    # Chinese New Year 2022
            (datetime(2023, 1, 22), 2023, 1, 1, False),   # Chinese New Year 2023
            (datetime(2024, 2, 10), 2024, 1, 1, False),   # Chinese New Year 2024
        ]
        
        for solar_date, exp_year, exp_month, exp_day, exp_leap in test_cases:
            lunar = solar_to_lunar(solar_date)
            assert lunar.year == exp_year, f"Year mismatch for {solar_date}: expected {exp_year}, got {lunar.year}"
            assert lunar.month == exp_month, f"Month mismatch for {solar_date}: expected {exp_month}, got {lunar.month}"
            assert lunar.day == exp_day, f"Day mismatch for {solar_date}: expected {exp_day}, got {lunar.day}"
            assert lunar.is_leap_month == exp_leap, f"Leap month mismatch for {solar_date}"
    
    def test_year_stem_branch_calculation(self):
        """
        Test year stem and branch calculation.
        
        Verified against traditional Chinese calendar.
        """
        from backend.calculators.ziwei.lunar_calendar import solar_to_lunar
        
        # Known year stems and branches
        test_cases = [
            # (solar_date, expected_stem, expected_branch)
            (datetime(1984, 3, 15), "甲", "子"),  # 甲子年
            (datetime(1985, 3, 15), "乙", "丑"),  # 乙丑年
            (datetime(1990, 5, 15), "庚", "午"),  # 庚午年
            (datetime(2000, 8, 8), "庚", "辰"),   # 庚辰年
            (datetime(2020, 6, 15), "庚", "子"),  # 庚子年
            (datetime(2024, 6, 15), "甲", "辰"),  # 甲辰年
        ]
        
        for solar_date, exp_stem, exp_branch in test_cases:
            lunar = solar_to_lunar(solar_date)
            assert lunar.year_stem == exp_stem, f"Year stem mismatch for {solar_date}: expected {exp_stem}, got {lunar.year_stem}"
            assert lunar.year_branch == exp_branch, f"Year branch mismatch for {solar_date}: expected {exp_branch}, got {lunar.year_branch}"
    
    def test_hour_branch_calculation(self):
        """
        Test hour branch calculation.
        
        子时(23-1), 丑时(1-3), 寅时(3-5), 卯时(5-7), 辰时(7-9), 巳时(9-11),
        午时(11-13), 未时(13-15), 申时(15-17), 酉时(17-19), 戌时(19-21), 亥时(21-23)
        """
        from backend.calculators.ziwei.lunar_calendar import solar_to_lunar
        
        # Test each hour
        expected_branches = {
            0: "子", 1: "丑", 2: "丑", 3: "寅", 4: "寅", 5: "卯",
            6: "卯", 7: "辰", 8: "辰", 9: "巳", 10: "巳", 11: "午",
            12: "午", 13: "未", 14: "未", 15: "申", 16: "申", 17: "酉",
            18: "酉", 19: "戌", 20: "戌", 21: "亥", 22: "亥", 23: "子",
        }
        
        for hour, expected_branch in expected_branches.items():
            dt = datetime(2020, 6, 15, hour, 30)
            lunar = solar_to_lunar(dt)
            assert lunar.hour_branch == expected_branch, (
                f"Hour branch mismatch for hour {hour}: "
                f"expected {expected_branch}, got {lunar.hour_branch}"
            )
    
    @property_test(
        property_id="lunar_conversion",
        property_name="农历转换一致性",
        validates=["3.9"],
        max_examples=50,
    )
    @given(
        year=st.integers(min_value=1901, max_value=2099),
        month=st.integers(min_value=1, max_value=12),
        day=st.integers(min_value=1, max_value=28),  # Safe day range
    )
    def test_lunar_conversion_consistency(self, year: int, month: int, day: int):
        """
        Test that lunar conversion is consistent.
        
        For any valid solar date, the conversion should produce valid lunar date.
        """
        from backend.calculators.ziwei.lunar_calendar import solar_to_lunar
        
        try:
            dt = datetime(year, month, day, 12, 0)
            lunar = solar_to_lunar(dt)
            
            # Verify lunar date is valid
            assert 1900 <= lunar.year <= 2100, f"Lunar year out of range: {lunar.year}"
            assert 1 <= lunar.month <= 12, f"Lunar month out of range: {lunar.month}"
            assert 1 <= lunar.day <= 30, f"Lunar day out of range: {lunar.day}"
            assert lunar.year_stem in HEAVENLY_STEMS, f"Invalid year stem: {lunar.year_stem}"
            assert lunar.year_branch in EARTHLY_BRANCHES, f"Invalid year branch: {lunar.year_branch}"
            assert lunar.hour_branch in EARTHLY_BRANCHES, f"Invalid hour branch: {lunar.hour_branch}"
        except ValueError:
            # Some dates may be invalid (e.g., Feb 30)
            pass
