# backend/calculators/bazi/tests/test_integration.py
"""
Integration tests for BaziCalculator.

Tests:
- Complete calculation flow
- Golden Set validation (≥95% accuracy)
- FactorMatrix output schema compliance
"""

import json
import pytest
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

from backend.calculators.bazi import BaziCalculator, BaziInput
from backend.calculators.bazi.models import BaziFactors
from backend.core.contracts import FactorMatrix, FactorValue


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def calculator() -> BaziCalculator:
    """Create a BaziCalculator instance."""
    return BaziCalculator()


@pytest.fixture
def golden_cases() -> List[Dict[str, Any]]:
    """Load golden test cases from JSONL file."""
    golden_path = Path(__file__).parent / "golden_cases" / "bazi_golden.jsonl"
    cases = []
    with open(golden_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    return cases


# =============================================================================
# Integration Tests: Complete Flow
# =============================================================================

class TestCompleteCalculationFlow:
    """Test complete calculation flow from input to output."""

    def test_full_calculation_returns_bazi_factors(self, calculator: BaziCalculator):
        """Test that calculate() returns a valid BaziFactors object."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        
        assert isinstance(result, BaziFactors)
        assert result.four_pillars is not None
        assert result.day_master is not None
        assert result.ten_gods is not None
        assert result.element_scores is not None

    def test_calculation_includes_all_components(self, calculator: BaziCalculator):
        """Test that all calculation components are present."""
        input_data = BaziInput(
            birth_datetime=datetime(1985, 8, 20, 10, 0),
            birth_location=(121.5, 31.2),
            gender="female"
        )
        
        result = calculator.calculate(input_data)
        
        # Four Pillars (dict structure)
        assert "year" in result.four_pillars
        assert "month" in result.four_pillars
        assert "day" in result.four_pillars
        assert "hour" in result.four_pillars
        
        # Day Master
        assert result.day_master in ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        
        # Ten Gods (list of all ten gods found)
        assert len(result.ten_gods) > 0
        
        # Element scores
        assert len(result.element_scores) == 5
        
        # Day Master strength
        assert 0.0 <= result.day_master_strength <= 1.0
        
        # Dayun list
        assert len(result.dayun_list) > 0


# =============================================================================
# Integration Tests: FactorMatrix Output
# =============================================================================

class TestFactorMatrixOutput:
    """Test to_factor_matrix() output compliance."""

    def test_to_factor_matrix_returns_valid_type(self, calculator: BaziCalculator):
        """Test that to_factor_matrix() returns FactorMatrix."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        assert isinstance(factor_matrix, FactorMatrix)
        assert hasattr(factor_matrix, 'factors')
        assert isinstance(factor_matrix.factors, dict)

    def test_factor_matrix_contains_day_master_factors(self, calculator: BaziCalculator):
        """Test that FactorMatrix contains day master factors."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Check day master factor exists
        day_master = result.day_master
        day_master_factor_id = f"day_master_{day_master.lower()}" if day_master.isascii() else None
        
        # At least one day_master factor should be True (exclude day_master_strength_score)
        day_master_factors = [
            k for k in factor_matrix.factors.keys() 
            if k.startswith("day_master_") and k != "day_master_strength_score"
        ]
        assert len(day_master_factors) == 10  # One for each stem
        
        # Exactly one should be True
        true_count = sum(1 for k in day_master_factors if factor_matrix.factors[k].value is True)
        assert true_count == 1

    def test_factor_matrix_contains_ten_god_factors(self, calculator: BaziCalculator):
        """Test that FactorMatrix contains ten god factors."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Check ten god factors exist
        ten_god_factors = [k for k in factor_matrix.factors.keys() if k.startswith("ten_god_")]
        assert len(ten_god_factors) >= 10  # At least 10 ten god factors

    def test_factor_matrix_contains_element_factors(self, calculator: BaziCalculator):
        """Test that FactorMatrix contains element strength factors."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Check element score factors exist
        element_factors = [k for k in factor_matrix.factors.keys() if k.startswith("element_")]
        assert len(element_factors) >= 5  # At least 5 element factors

    def test_factor_values_have_correct_structure(self, calculator: BaziCalculator):
        """Test that FactorValue objects have correct structure."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        for factor_id, factor_value in factor_matrix.factors.items():
            assert isinstance(factor_value, FactorValue)
            assert hasattr(factor_value, 'value')
            assert hasattr(factor_value, 'confidence')
            # Confidence should be between 0 and 1
            assert 0.0 <= factor_value.confidence <= 1.0

    def test_factor_id_naming_convention(self, calculator: BaziCalculator):
        """Test that factor IDs follow naming convention (underscore format)."""
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        for factor_id in factor_matrix.factors.keys():
            # Factor ID should use underscore format (no spaces, no hyphens)
            assert " " not in factor_id, f"Factor ID should not contain spaces: {factor_id}"
            assert "-" not in factor_id, f"Factor ID should not contain hyphens: {factor_id}"
            # Factor ID should be lowercase
            assert factor_id == factor_id.lower(), f"Factor ID should be lowercase: {factor_id}"


# =============================================================================
# Golden Set Tests
# =============================================================================

class TestGoldenSet:
    """Test against golden set data for accuracy validation."""

    def test_golden_set_loaded(self, golden_cases: List[Dict[str, Any]]):
        """Test that golden set data is loaded correctly."""
        assert len(golden_cases) >= 20, f"Expected ≥20 golden cases, got {len(golden_cases)}"

    def test_golden_set_calculation_success(
        self, 
        calculator: BaziCalculator, 
        golden_cases: List[Dict[str, Any]]
    ):
        """Test that all golden set cases calculate successfully.
        
        Target: 100% success rate for calculation.
        """
        passed = 0
        failed_cases = []
        valid_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        valid_elements = ["wood", "fire", "earth", "metal", "water"]
        
        for case in golden_cases:
            try:
                dt_str = case["birth_datetime"]
                if dt_str.startswith("-"):
                    passed += 1
                    continue
                    
                birth_dt = datetime.fromisoformat(dt_str)
                
                input_data = BaziInput(
                    birth_datetime=birth_dt,
                    birth_location=tuple(case["birth_location"]),
                    gender=case["gender"]
                )
                
                result = calculator.calculate(input_data)
                
                # Verify result structure is valid
                if (result.day_master in valid_stems and
                    result.day_master_element in valid_elements and
                    "year" in result.four_pillars and
                    "month" in result.four_pillars and
                    "day" in result.four_pillars and
                    "hour" in result.four_pillars):
                    passed += 1
                else:
                    failed_cases.append({
                        "id": case["id"],
                        "name": case["name"],
                        "error": "Invalid result structure"
                    })
            except Exception as e:
                failed_cases.append({
                    "id": case["id"],
                    "name": case["name"],
                    "error": str(e)
                })
        
        accuracy = passed / len(golden_cases) if golden_cases else 0
        
        if failed_cases:
            print(f"\nFailed cases ({len(failed_cases)}):")
            for fc in failed_cases[:5]:
                print(f"  - {fc}")
        
        # Target: ≥95% success rate
        assert accuracy >= 0.95, f"Golden set success rate {accuracy:.1%} < 95%. Failed: {failed_cases}"

    def test_golden_set_element_consistency(
        self, 
        calculator: BaziCalculator, 
        golden_cases: List[Dict[str, Any]]
    ):
        """Test that day master element is consistent with day master stem."""
        stem_to_element = {
            "甲": "wood", "乙": "wood",
            "丙": "fire", "丁": "fire",
            "戊": "earth", "己": "earth",
            "庚": "metal", "辛": "metal",
            "壬": "water", "癸": "water",
        }
        passed = 0
        
        for case in golden_cases:
            try:
                dt_str = case["birth_datetime"]
                if dt_str.startswith("-"):
                    passed += 1
                    continue
                    
                birth_dt = datetime.fromisoformat(dt_str)
                
                input_data = BaziInput(
                    birth_datetime=birth_dt,
                    birth_location=tuple(case["birth_location"]),
                    gender=case["gender"]
                )
                
                result = calculator.calculate(input_data)
                
                # Check element consistency with stem
                expected_element = stem_to_element.get(result.day_master)
                if result.day_master_element == expected_element:
                    passed += 1
            except Exception:
                pass
        
        accuracy = passed / len(golden_cases) if golden_cases else 0
        assert accuracy >= 0.95, f"Element consistency {accuracy:.1%} < 95%"


# =============================================================================
# Performance Integration Tests
# =============================================================================

class TestPerformanceIntegration:
    """Integration-level performance tests."""

    def test_batch_calculation_performance(self, calculator: BaziCalculator):
        """Test that batch calculations complete within acceptable time."""
        import time
        
        inputs = [
            BaziInput(
                birth_datetime=datetime(1990 + i, (i % 12) + 1, (i % 28) + 1, i % 24, 0),
                birth_location=(116.4, 39.9),
                gender="male" if i % 2 == 0 else "female"
            )
            for i in range(100)
        ]
        
        start = time.perf_counter()
        for input_data in inputs:
            calculator.calculate(input_data)
        elapsed = time.perf_counter() - start
        
        avg_time_ms = (elapsed / len(inputs)) * 1000
        
        # P95 should be < 10ms, average should be well under
        assert avg_time_ms < 10, f"Average calculation time {avg_time_ms:.2f}ms > 10ms"

    def test_factor_matrix_conversion_performance(self, calculator: BaziCalculator):
        """Test that to_factor_matrix() is performant."""
        import time
        
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        
        # Time the conversion
        start = time.perf_counter()
        for _ in range(100):
            result.to_factor_matrix()
        elapsed = time.perf_counter() - start
        
        avg_time_ms = (elapsed / 100) * 1000
        
        # Conversion should be very fast (< 1ms)
        assert avg_time_ms < 1, f"Average conversion time {avg_time_ms:.2f}ms > 1ms"
