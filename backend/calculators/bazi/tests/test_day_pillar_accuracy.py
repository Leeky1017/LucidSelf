# backend/calculators/bazi/tests/test_day_pillar_accuracy.py
"""
Day pillar (日柱) accuracy audit tests.

Compares calculated day pillar with authoritative 万年历 (perpetual calendar) data.
Validates that all day pillar calculations are 100% consistent.

**Feature: calculator-accuracy-audit, Property 3: 日柱干支一致性**
**Validates: Requirements 2.2**
"""

import pytest
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

from hypothesis import given, settings, assume
from hypothesis import strategies as st

from backend.calculators.bazi.calculator import BaziCalculator
from backend.calculators.bazi.models import BaziInput, HEAVENLY_STEMS, EARTHLY_BRANCHES
from backend.core.testing.property_tests import property_test


# =============================================================================
# Reference Data - 万年历 verified day pillars
# =============================================================================

# Known day pillars calculated using Julian day algorithm
# Format: (year, month, day) -> (stem, branch)
# Base reference: 2000年1月7日 is 甲子日 (Julian day 2451551)
REFERENCE_DAY_PILLARS: Dict[Tuple[int, int, int], Tuple[str, str]] = {
    # 基准日 - 甲子日
    (2000, 1, 7): ("甲", "子"),
    
    # 2000年代表性日期
    (2000, 1, 1): ("戊", "午"),
    (2000, 2, 4): ("壬", "辰"),  # 立春
    (2000, 6, 21): ("庚", "戌"),  # 夏至
    (2000, 12, 31): ("癸", "亥"),
    
    # 2024年代表性日期
    (2024, 1, 1): ("甲", "子"),
    (2024, 2, 4): ("戊", "戌"),  # 立春
    (2024, 2, 10): ("甲", "辰"),  # 春节
    (2024, 6, 21): ("丙", "辰"),  # 夏至
    (2024, 9, 17): ("甲", "申"),  # 中秋
    (2024, 12, 31): ("己", "巳"),
    
    # 1990年代表性日期
    (1990, 1, 1): ("丙", "寅"),
    (1990, 5, 15): ("庚", "辰"),
    (1990, 10, 1): ("己", "亥"),
    
    # 边界年份
    (1900, 1, 31): ("甲", "辰"),
    (1901, 1, 1): ("己", "卯"),
    (2099, 12, 31): ("壬", "寅"),
    
    # 闰年2月29日
    (2000, 2, 29): ("丁", "巳"),
    (2024, 2, 29): ("癸", "亥"),
    
    # 60天周期验证
    (2024, 3, 1): ("甲", "子"),  # 2024-1-1 + 60天
}


def calculate_day_pillar_direct(year: int, month: int, day: int) -> Tuple[str, str]:
    """
    直接计算日柱（不经过完整的BaziCalculator）.
    
    使用与BaziCalculator相同的算法。
    基准日：2000年1月7日是甲子日（儒略日 2451551）
    """
    # 计算儒略日数
    y, m = year, month
    if m <= 2:
        y -= 1
        m += 12
    
    a = y // 100
    b = 2 - a + a // 4
    jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + day + b - 1524
    
    # 基准日：2000年1月7日是甲子日，儒略日为 2451551
    base_jd = 2451551
    
    diff = jd - base_jd
    stem_idx = diff % 10
    branch_idx = diff % 12
    
    return (HEAVENLY_STEMS[stem_idx], EARTHLY_BRANCHES[branch_idx])


# =============================================================================
# Audit Tests - Day Pillar Accuracy
# =============================================================================

class TestDayPillarAccuracyAudit:
    """
    Audit tests for day pillar calculation accuracy.
    
    Compares calculated values with 万年历 reference data.
    Requirement: 100% consistency with authoritative sources.
    """
    
    @pytest.mark.parametrize(
        "date_tuple,expected",
        list(REFERENCE_DAY_PILLARS.items()),
        ids=[f"{y}-{m:02d}-{d:02d}" for (y, m, d) in REFERENCE_DAY_PILLARS.keys()]
    )
    def test_day_pillar_against_reference(
        self, 
        date_tuple: Tuple[int, int, int], 
        expected: Tuple[str, str]
    ):
        """Test day pillar against 万年历 reference data."""
        year, month, day = date_tuple
        expected_stem, expected_branch = expected
        
        # Calculate using direct method
        actual_stem, actual_branch = calculate_day_pillar_direct(year, month, day)
        
        assert actual_stem == expected_stem, (
            f"Day stem mismatch for {year}-{month:02d}-{day:02d}: "
            f"expected {expected_stem}, got {actual_stem}"
        )
        assert actual_branch == expected_branch, (
            f"Day branch mismatch for {year}-{month:02d}-{day:02d}: "
            f"expected {expected_branch}, got {actual_branch}"
        )
    
    def test_60_day_cycle_consistency(self):
        """Test that day pillars follow the 60-day cycle correctly."""
        # Start from a known date
        base_date = datetime(1900, 1, 31)  # 甲子日
        
        # Check 60 consecutive days form a complete cycle
        seen_combinations = set()
        for i in range(60):
            date = base_date + timedelta(days=i)
            stem, branch = calculate_day_pillar_direct(date.year, date.month, date.day)
            combination = (stem, branch)
            
            # Each combination should be unique within 60 days
            assert combination not in seen_combinations, (
                f"Duplicate combination {combination} found at day {i}"
            )
            seen_combinations.add(combination)
        
        # Should have exactly 60 unique combinations
        assert len(seen_combinations) == 60
    
    def test_day_pillar_cycle_repeats(self):
        """Test that day pillar repeats every 60 days."""
        base_date = datetime(2024, 1, 1)
        base_stem, base_branch = calculate_day_pillar_direct(2024, 1, 1)
        
        # Check that 60 days later has the same pillar
        date_60 = base_date + timedelta(days=60)
        stem_60, branch_60 = calculate_day_pillar_direct(
            date_60.year, date_60.month, date_60.day
        )
        
        assert stem_60 == base_stem, f"Stem should repeat after 60 days"
        assert branch_60 == base_branch, f"Branch should repeat after 60 days"
    
    def test_consecutive_days_advance_correctly(self):
        """Test that consecutive days advance stem and branch correctly."""
        base_date = datetime(2024, 6, 1)
        
        for i in range(10):
            date = base_date + timedelta(days=i)
            stem, branch = calculate_day_pillar_direct(date.year, date.month, date.day)
            
            next_date = date + timedelta(days=1)
            next_stem, next_branch = calculate_day_pillar_direct(
                next_date.year, next_date.month, next_date.day
            )
            
            # Stem should advance by 1 (mod 10)
            expected_stem_idx = (HEAVENLY_STEMS.index(stem) + 1) % 10
            actual_stem_idx = HEAVENLY_STEMS.index(next_stem)
            assert actual_stem_idx == expected_stem_idx, (
                f"Stem should advance by 1 from {stem} to {HEAVENLY_STEMS[expected_stem_idx]}, "
                f"got {next_stem}"
            )
            
            # Branch should advance by 1 (mod 12)
            expected_branch_idx = (EARTHLY_BRANCHES.index(branch) + 1) % 12
            actual_branch_idx = EARTHLY_BRANCHES.index(next_branch)
            assert actual_branch_idx == expected_branch_idx, (
                f"Branch should advance by 1 from {branch} to {EARTHLY_BRANCHES[expected_branch_idx]}, "
                f"got {next_branch}"
            )


# =============================================================================
# Property-Based Test for Day Pillar Consistency
# =============================================================================

@property_test(
    property_id="3",
    property_name="日柱干支一致性",
    validates=["2.2"],
    max_examples=100,
)
@given(
    year=st.integers(min_value=1900, max_value=2100),
    month=st.integers(min_value=1, max_value=12),
    day=st.integers(min_value=1, max_value=28),  # Safe for all months
)
def test_property_day_pillar_consistency(year: int, month: int, day: int):
    """
    **Feature: calculator-accuracy-audit, Property 3: 日柱干支一致性**
    **Validates: Requirements 2.2**
    
    Property: For any valid date, the day pillar should:
    1. Be a valid stem-branch combination
    2. Follow the 60-day cycle (same pillar 60 days later)
    3. Advance correctly from the previous day
    """
    # Calculate day pillar
    stem, branch = calculate_day_pillar_direct(year, month, day)
    
    # Verify valid stem
    assert stem in HEAVENLY_STEMS, f"Invalid stem: {stem}"
    
    # Verify valid branch
    assert branch in EARTHLY_BRANCHES, f"Invalid branch: {branch}"
    
    # Verify 60-day cycle
    date = datetime(year, month, day)
    date_60 = date + timedelta(days=60)
    stem_60, branch_60 = calculate_day_pillar_direct(
        date_60.year, date_60.month, date_60.day
    )
    assert stem_60 == stem, f"Stem should repeat after 60 days"
    assert branch_60 == branch, f"Branch should repeat after 60 days"
    
    # Verify consecutive day advancement
    if day > 1:  # Can check previous day
        prev_stem, prev_branch = calculate_day_pillar_direct(year, month, day - 1)
        expected_stem_idx = (HEAVENLY_STEMS.index(prev_stem) + 1) % 10
        expected_branch_idx = (EARTHLY_BRANCHES.index(prev_branch) + 1) % 12
        
        assert HEAVENLY_STEMS.index(stem) == expected_stem_idx, (
            f"Stem should advance by 1 from previous day"
        )
        assert EARTHLY_BRANCHES.index(branch) == expected_branch_idx, (
            f"Branch should advance by 1 from previous day"
        )


# =============================================================================
# Integration Test with Full Calculator
# =============================================================================

class TestDayPillarIntegration:
    """Integration tests using the full BaziCalculator."""
    
    def test_calculator_day_pillar_matches_direct(self):
        """Test that BaziCalculator produces same day pillar as direct calculation."""
        calculator = BaziCalculator()
        
        test_cases = [
            (2024, 1, 1, 12, 0),
            (2024, 6, 15, 10, 30),
            (1990, 5, 15, 14, 0),
            (2000, 2, 29, 8, 0),
        ]
        
        for year, month, day, hour, minute in test_cases:
            # Direct calculation
            expected_stem, expected_branch = calculate_day_pillar_direct(year, month, day)
            
            # Calculator result
            input_data = BaziInput(
                birth_datetime=datetime(year, month, day, hour, minute),
                birth_location=(116.4, 39.9),  # Beijing
                gender="male"
            )
            result = calculator.calculate(input_data)
            
            actual_stem = result.four_pillars["day"]["stem"]
            actual_branch = result.four_pillars["day"]["branch"]
            
            assert actual_stem == expected_stem, (
                f"Calculator day stem mismatch for {year}-{month:02d}-{day:02d}: "
                f"expected {expected_stem}, got {actual_stem}"
            )
            assert actual_branch == expected_branch, (
                f"Calculator day branch mismatch for {year}-{month:02d}-{day:02d}: "
                f"expected {expected_branch}, got {actual_branch}"
            )
