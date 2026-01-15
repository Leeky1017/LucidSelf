# backend/calculators/ziwei/tests/test_golden.py
"""
Golden Set tests for ZiweiCalculator.

Tests against pre-verified test cases to ensure calculation accuracy.
"""

import json
import pytest
from datetime import datetime
from pathlib import Path

from backend.calculators.ziwei import ZiweiCalculator, ZiweiInput


def load_golden_cases():
    """Load golden test cases from JSONL file."""
    # Use the comprehensive golden set with 35+ cases covering:
    # - All 5 five-element types (水二局, 木三局, 金四局, 土五局, 火六局)
    # - All 10 heavenly stems (甲乙丙丁戊己庚辛壬癸)
    # - All 14 main stars in various palace combinations
    # - Various decade directions (forward/backward)
    # - Different geographic locations
    golden_file = Path(__file__).parent / "golden_cases" / "ziwei_golden_new.jsonl"
    cases = []
    
    with open(golden_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                cases.append(json.loads(line))
    
    return cases


GOLDEN_CASES = load_golden_cases()


class TestGoldenSet:
    """Golden set tests for ZiweiCalculator."""
    
    @pytest.fixture
    def calculator(self):
        return ZiweiCalculator()
    
    @pytest.mark.parametrize("case", GOLDEN_CASES, ids=lambda c: c["id"])
    def test_golden_case(self, calculator, case):
        """Test against golden case."""
        # Parse input
        birth_dt = datetime.fromisoformat(case["birth_datetime"])
        input_data = ZiweiInput(
            birth_datetime=birth_dt,
            birth_location=tuple(case["birth_location"]),
            gender=case["gender"]
        )
        
        # Calculate
        result = calculator.calculate(input_data)
        expected = case["expected"]
        
        # Verify expected fields
        if "lunar_year" in expected:
            assert result.lunar_year == expected["lunar_year"]
        
        if "lunar_month" in expected:
            assert result.lunar_month == expected["lunar_month"]
        
        if "lunar_day" in expected:
            assert result.lunar_day == expected["lunar_day"]
        
        if "year_stem" in expected:
            assert result.year_stem == expected["year_stem"]
        
        if "year_branch" in expected:
            assert result.year_branch == expected["year_branch"]
        
        if "hour_branch" in expected:
            assert result.hour_branch == expected["hour_branch"]
        
        if "sihua_natal" in expected:
            for sihua_type, star in expected["sihua_natal"].items():
                assert result.sihua_natal[sihua_type] == star
        
        if "decade_direction" in expected:
            assert result.decade_direction == expected["decade_direction"]
        
        if "five_element_type" in expected:
            assert result.five_element_type == expected["five_element_type"]
        
        if "ming_palace_branch" in expected:
            assert result.ming_palace_branch == expected["ming_palace_branch"]
        
        if "body_palace_name" in expected:
            assert result.body_palace_name == expected["body_palace_name"]
        
        if "start_decade_age" in expected:
            assert result.start_decade_age == expected["start_decade_age"]
        
        if "main_stars" in expected:
            for star, palace in expected["main_stars"].items():
                assert result.main_stars.get(star) == palace, f"Star {star} expected in {palace}, got {result.main_stars.get(star)}"
