# backend/calculators/astro/tests/test_golden_set.py
"""
Golden Set Tests for AstroCalculator

Tests the AstroCalculator against verified golden set cases.

**Feature: calculator-accuracy-audit**
**Validates: Requirements 10.4**
"""

import pytest
from datetime import datetime
from pathlib import Path

from backend.calculators.astro import AstroCalculator, AstroInput
from backend.core.testing.golden_set import GoldenSetLoader, GoldenSetCase


# Load golden set cases
GOLDEN_SET_PATH = Path(__file__).parent / "golden_cases" / "astro_golden_set.jsonl"


def load_golden_cases():
    """Load golden set cases from JSONL file."""
    loader = GoldenSetLoader()
    return loader.load_jsonl(GOLDEN_SET_PATH)


# Get all cases for parametrization
try:
    GOLDEN_CASES = load_golden_cases()
except FileNotFoundError:
    GOLDEN_CASES = []


class TestAstroGoldenSet:
    """
    Golden Set tests for AstroCalculator.
    
    **Feature: calculator-accuracy-audit**
    **Validates: Requirements 10.4**
    """
    
    @pytest.fixture
    def calculator(self):
        """Create AstroCalculator instance."""
        return AstroCalculator()
    
    @pytest.mark.parametrize(
        "case",
        GOLDEN_CASES,
        ids=[c.case_id for c in GOLDEN_CASES],
    )
    def test_golden_case(self, calculator, case: GoldenSetCase):
        """
        Test AstroCalculator against golden set case.
        
        **Feature: calculator-accuracy-audit**
        **Validates: Requirements 10.4**
        """
        # Build input
        input_data = AstroInput(
            birth_datetime=datetime.fromisoformat(case.input_data["birth_datetime"]),
            birth_location=tuple(case.input_data["birth_location"]),
            timezone=case.input_data.get("timezone"),
            house_system=case.input_data.get("house_system", "placidus"),
        )
        
        # Calculate
        result = calculator.calculate(input_data)
        
        # Verify expected outputs
        expected = case.expected_output
        tolerance = case.tolerance or {}
        
        # Check sun sign
        if "sun_sign" in expected:
            assert result.planets["sun"].sign == expected["sun_sign"], (
                f"Case {case.case_id}: Sun sign mismatch - "
                f"expected {expected['sun_sign']}, got {result.planets['sun'].sign}"
            )
        
        # Check moon sign
        if "moon_sign" in expected:
            assert result.planets["moon"].sign == expected["moon_sign"], (
                f"Case {case.case_id}: Moon sign mismatch - "
                f"expected {expected['moon_sign']}, got {result.planets['moon'].sign}"
            )
        
        # Check ascendant sign
        if "ascendant_sign" in expected:
            assert result.ascendant_sign == expected["ascendant_sign"], (
                f"Case {case.case_id}: Ascendant sign mismatch - "
                f"expected {expected['ascendant_sign']}, got {result.ascendant_sign}"
            )
        
        # Check midheaven sign
        if "midheaven_sign" in expected:
            assert result.midheaven_sign == expected["midheaven_sign"], (
                f"Case {case.case_id}: Midheaven sign mismatch - "
                f"expected {expected['midheaven_sign']}, got {result.midheaven_sign}"
            )
        
        # Check sun longitude with tolerance
        if "sun_longitude" in expected:
            long_tolerance = tolerance.get("longitude", 0.0167)  # 1 arcminute default
            diff = abs(result.planets["sun"].longitude - expected["sun_longitude"])
            if diff > 180:
                diff = 360 - diff
            assert diff <= long_tolerance, (
                f"Case {case.case_id}: Sun longitude out of tolerance - "
                f"expected {expected['sun_longitude']}, got {result.planets['sun'].longitude}, "
                f"diff={diff}"
            )
    
    def test_golden_set_coverage(self):
        """
        Verify golden set has adequate coverage.
        
        **Feature: calculator-accuracy-audit**
        **Validates: Requirements 10.4**
        """
        assert len(GOLDEN_CASES) >= 20, (
            f"Golden set should have at least 20 cases, got {len(GOLDEN_CASES)}"
        )
        
        # Check coverage of all zodiac signs
        sun_signs = set()
        for case in GOLDEN_CASES:
            if "sun_sign" in case.expected_output:
                sun_signs.add(case.expected_output["sun_sign"])
        
        expected_signs = {
            "aries", "taurus", "gemini", "cancer", "leo", "virgo",
            "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
        }
        
        # Should cover most signs (at least 10 of 12)
        covered = len(sun_signs & expected_signs)
        assert covered >= 10, (
            f"Golden set should cover at least 10 zodiac signs, got {covered}: {sun_signs}"
        )
    
    def test_golden_set_house_systems(self):
        """
        Verify golden set covers different house systems.
        
        **Feature: calculator-accuracy-audit**
        **Validates: Requirements 10.4**
        """
        house_systems = set()
        for case in GOLDEN_CASES:
            hs = case.input_data.get("house_system", "placidus")
            house_systems.add(hs)
        
        # Should cover at least 3 house systems
        assert len(house_systems) >= 3, (
            f"Golden set should cover at least 3 house systems, got {len(house_systems)}: {house_systems}"
        )
    
    def test_golden_set_geographic_coverage(self):
        """
        Verify golden set covers different geographic regions.
        
        **Feature: calculator-accuracy-audit**
        **Validates: Requirements 10.4**
        """
        # Check for both hemispheres
        northern = False
        southern = False
        
        for case in GOLDEN_CASES:
            lat = case.input_data["birth_location"][1]
            if lat > 0:
                northern = True
            elif lat < 0:
                southern = True
        
        assert northern, "Golden set should include northern hemisphere locations"
        assert southern, "Golden set should include southern hemisphere locations"
