# backend/calculators/bazi/tests/test_solar_terms_accuracy.py
"""
Solar terms accuracy audit tests.

Compares calculated solar term times with authoritative reference data.
Validates that all solar term calculations are within 1 minute of reference.

**Feature: calculator-accuracy-audit, Property 2: 节气计算精度**
**Validates: Requirements 2.1**
"""

import json
import pytest
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Tuple

from hypothesis import given, settings, assume
from hypothesis import strategies as st

from backend.calculators.bazi.solar_terms import get_solar_term_date
from backend.core.testing.property_tests import (
    property_test,
    assert_within_tolerance,
)


# =============================================================================
# Reference Data Loading
# =============================================================================

# Mapping from Chinese term names to pinyin names in JSON
# NOTE: The JSON file has a naming bug where each term name is shifted by one position.
# The actual mapping based on dates is:
# - JSON "Dahan" (Jan 6) is actually 小寒 (Xiaohan)
# - JSON "Lichun" (Jan 20) is actually 大寒 (Dahan)
# - JSON "Yushui" (Feb 4) is actually 立春 (Lichun)
# etc.
# So we map Chinese names to the SHIFTED JSON keys:
TERM_NAME_MAPPING = {
    "小寒": "Dahan",      # JSON "Dahan" is actually 小寒 (Jan 6)
    "大寒": "Lichun",     # JSON "Lichun" is actually 大寒 (Jan 20)
    "立春": "Yushui",     # JSON "Yushui" is actually 立春 (Feb 4)
    "雨水": "Jingzhe",    # JSON "Jingzhe" is actually 雨水 (Feb 19)
    "惊蛰": "Chunfen",    # JSON "Chunfen" is actually 惊蛰 (Mar 5)
    "春分": "Qingming",   # JSON "Qingming" is actually 春分 (Mar 20)
    "清明": "Guyu",       # JSON "Guyu" is actually 清明 (Apr 4)
    "谷雨": "Lixia",      # JSON "Lixia" is actually 谷雨 (Apr 19)
    "立夏": "Xiaoman",    # JSON "Xiaoman" is actually 立夏 (May 5)
    "小满": "Mangzhong",  # JSON "Mangzhong" is actually 小满 (May 20)
    "芒种": "Xiazhi",     # JSON "Xiazhi" is actually 芒种 (Jun 5)
    "夏至": "Xiaoshu",    # JSON "Xiaoshu" is actually 夏至 (Jun 21)
    "小暑": "Dashu",      # JSON "Dashu" is actually 小暑 (Jul 6)
    "大暑": "Liqiu",      # JSON "Liqiu" is actually 大暑 (Jul 22)
    "立秋": "Chushu",     # JSON "Chushu" is actually 立秋 (Aug 7)
    "处暑": "Bailu",      # JSON "Bailu" is actually 处暑 (Aug 22)
    "白露": "Qiufen",     # JSON "Qiufen" is actually 白露 (Sep 7)
    "秋分": "Hanlu",      # JSON "Hanlu" is actually 秋分 (Sep 22)
    "寒露": "Shuangjiang", # JSON "Shuangjiang" is actually 寒露 (Oct 8)
    "霜降": "Lidong",     # JSON "Lidong" is actually 霜降 (Oct 23)
    "立冬": "Xiaoxue",    # JSON "Xiaoxue" is actually 立冬 (Nov 7)
    "小雪": "Daxue",      # JSON "Daxue" is actually 小雪 (Nov 22)
    "大雪": "Dongzhi",    # JSON "Dongzhi" is actually 大雪 (Dec 6)
    "冬至": "Xiaohan",    # JSON "Xiaohan" is actually 冬至 (Dec 21)
}


def load_reference_solar_terms() -> Dict[str, Dict[str, datetime]]:
    """Load reference solar term data from JSON file."""
    json_path = Path("data/solar_terms/solar_terms_1900_2100.json")
    
    with open(json_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    # Parse datetime strings
    result = {}
    for year_str, terms in raw_data.items():
        year_data = {}
        for term_pinyin, dt_str in terms.items():
            # Parse ISO format datetime with timezone
            dt = datetime.fromisoformat(dt_str.replace("+08:00", ""))
            year_data[term_pinyin] = dt
        result[year_str] = year_data
    
    return result


# Load reference data once
REFERENCE_DATA = load_reference_solar_terms()


def get_reference_solar_term(year: int, term_name: str) -> datetime:
    """Get reference solar term datetime for a given year and term."""
    year_str = str(year)
    term_pinyin = TERM_NAME_MAPPING.get(term_name)
    
    if year_str not in REFERENCE_DATA:
        raise ValueError(f"Year {year} not in reference data")
    
    if term_pinyin not in REFERENCE_DATA[year_str]:
        raise ValueError(f"Term {term_name} ({term_pinyin}) not in reference data for {year}")
    
    return REFERENCE_DATA[year_str][term_pinyin]


def calculate_time_difference_seconds(dt1: datetime, dt2: datetime) -> float:
    """Calculate absolute time difference in seconds."""
    diff = abs((dt1 - dt2).total_seconds())
    return diff


# =============================================================================
# Audit Tests - Solar Term Accuracy
# =============================================================================

class TestSolarTermAccuracyAudit:
    """
    Audit tests for solar term calculation accuracy.
    
    Compares calculated values with Hong Kong Observatory / authoritative data.
    Requirement: Error < 1 minute for all solar terms 1900-2100.
    """
    
    # Maximum allowed error in seconds (1 minute = 60 seconds)
    MAX_ERROR_SECONDS = 60
    
    @pytest.mark.parametrize("term_name", list(TERM_NAME_MAPPING.keys()))
    def test_solar_term_accuracy_2024(self, term_name: str):
        """Test solar term accuracy for year 2024."""
        year = 2024
        
        # Get calculated value
        calculated = get_solar_term_date(year, term_name)
        
        # Get reference value
        reference = get_reference_solar_term(year, term_name)
        
        # Calculate difference
        diff_seconds = calculate_time_difference_seconds(calculated, reference)
        
        assert diff_seconds <= self.MAX_ERROR_SECONDS, (
            f"Solar term {term_name} for {year}: "
            f"calculated={calculated}, reference={reference}, "
            f"diff={diff_seconds:.1f}s (max allowed: {self.MAX_ERROR_SECONDS}s)"
        )
    
    @pytest.mark.parametrize("year", [1900, 1950, 2000, 2050, 2100])
    def test_lichun_accuracy_across_years(self, year: int):
        """Test 立春 (Li Chun) accuracy across different years."""
        term_name = "立春"
        
        calculated = get_solar_term_date(year, term_name)
        reference = get_reference_solar_term(year, term_name)
        
        diff_seconds = calculate_time_difference_seconds(calculated, reference)
        
        assert diff_seconds <= self.MAX_ERROR_SECONDS, (
            f"立春 for {year}: calculated={calculated}, reference={reference}, "
            f"diff={diff_seconds:.1f}s"
        )
    
    def test_all_terms_1990(self):
        """Test all 24 solar terms for year 1990."""
        year = 1990
        errors = []
        
        for term_name in TERM_NAME_MAPPING.keys():
            try:
                calculated = get_solar_term_date(year, term_name)
                reference = get_reference_solar_term(year, term_name)
                diff_seconds = calculate_time_difference_seconds(calculated, reference)
                
                if diff_seconds > self.MAX_ERROR_SECONDS:
                    errors.append(
                        f"{term_name}: diff={diff_seconds:.1f}s "
                        f"(calc={calculated}, ref={reference})"
                    )
            except Exception as e:
                errors.append(f"{term_name}: ERROR - {e}")
        
        assert len(errors) == 0, f"Solar term accuracy errors:\n" + "\n".join(errors)


# =============================================================================
# Property-Based Test for Solar Term Accuracy
# =============================================================================

@property_test(
    property_id="2",
    property_name="节气计算精度",
    validates=["2.1"],
    max_examples=100,
)
@given(
    year=st.integers(min_value=1900, max_value=2100),
    term_idx=st.integers(min_value=0, max_value=23),
)
def test_property_solar_term_accuracy(year: int, term_idx: int):
    """
    **Feature: calculator-accuracy-audit, Property 2: 节气计算精度**
    **Validates: Requirements 2.1**
    
    Property: For any year in 1900-2100 and any solar term,
    the calculated time should be within 1 minute of reference data.
    """
    term_names = list(TERM_NAME_MAPPING.keys())
    term_name = term_names[term_idx]
    
    # Skip if reference data not available for this year
    year_str = str(year)
    if year_str not in REFERENCE_DATA:
        assume(False)
    
    term_pinyin = TERM_NAME_MAPPING[term_name]
    if term_pinyin not in REFERENCE_DATA[year_str]:
        assume(False)
    
    # Get calculated and reference values
    calculated = get_solar_term_date(year, term_name)
    reference = get_reference_solar_term(year, term_name)
    
    # Calculate difference
    diff_seconds = calculate_time_difference_seconds(calculated, reference)
    
    # Assert within tolerance (1 minute = 60 seconds)
    assert diff_seconds <= 60, (
        f"Solar term {term_name} for {year}: "
        f"calculated={calculated}, reference={reference}, "
        f"diff={diff_seconds:.1f}s (max: 60s)"
    )


# =============================================================================
# Comprehensive Audit Report
# =============================================================================

class TestSolarTermComprehensiveAudit:
    """Comprehensive audit across all years and terms."""
    
    @pytest.mark.slow
    def test_full_audit_sample_years(self):
        """
        Full audit for sample years across the supported range.
        
        Tests every 10th year from 1900 to 2100.
        """
        sample_years = list(range(1900, 2101, 10))
        max_error_seconds = 60
        
        total_tests = 0
        total_errors = 0
        max_diff_found = 0
        worst_case = None
        
        for year in sample_years:
            year_str = str(year)
            if year_str not in REFERENCE_DATA:
                continue
            
            for term_name, term_pinyin in TERM_NAME_MAPPING.items():
                if term_pinyin not in REFERENCE_DATA[year_str]:
                    continue
                
                total_tests += 1
                
                try:
                    calculated = get_solar_term_date(year, term_name)
                    reference = get_reference_solar_term(year, term_name)
                    diff_seconds = calculate_time_difference_seconds(calculated, reference)
                    
                    if diff_seconds > max_diff_found:
                        max_diff_found = diff_seconds
                        worst_case = (year, term_name, calculated, reference, diff_seconds)
                    
                    if diff_seconds > max_error_seconds:
                        total_errors += 1
                        
                except Exception as e:
                    total_errors += 1
        
        # Report
        print(f"\n=== Solar Term Accuracy Audit Report ===")
        print(f"Total tests: {total_tests}")
        print(f"Errors (>60s): {total_errors}")
        print(f"Max difference found: {max_diff_found:.1f}s")
        if worst_case:
            year, term, calc, ref, diff = worst_case
            print(f"Worst case: {year} {term}")
            print(f"  Calculated: {calc}")
            print(f"  Reference:  {ref}")
            print(f"  Difference: {diff:.1f}s")
        
        assert total_errors == 0, (
            f"Found {total_errors} solar term calculations with error > 60s. "
            f"Max diff: {max_diff_found:.1f}s"
        )
