# backend/core/testing/tests/test_output_validation.py
"""
Property-based tests for Calculator output validation.

Validates that all Calculator outputs conform to the structural-only constraint:
- Calculator layer should only produce structural factors (factor_id + value)
- No semantic fields (description, meaning, interpretation) should be present

**Feature: calculator-accuracy-audit, Property 1: Calculator 输出不包含语义字段**
**Validates: Requirements 1.1, 1.2**
"""

import pytest
from datetime import datetime
from typing import Any, Dict

from hypothesis import given, settings, assume
from hypothesis import strategies as st

from backend.core.contracts import FactorValue, FactorMatrix
from backend.core.testing.output_validation import (
    SEMANTIC_FIELD_NAMES,
    is_semantic_field_name,
    check_value_for_semantic_content,
    validate_factor_value_no_semantics,
    validate_factor_matrix_no_semantics,
    validate_calculator_output,
    assert_no_semantic_fields,
    assert_factor_matrix_structural_only,
)
from backend.core.testing.property_tests import property_test


# =============================================================================
# Hypothesis Strategies
# =============================================================================

def valid_factor_id_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating valid factor IDs."""
    prefixes = ["bazi", "ziwei", "yijing", "astro", "tarot", "dream"]
    suffixes = ["_value", "_score", "_count", "_type", "_id", "_position"]
    
    return st.builds(
        lambda prefix, middle, suffix: f"{prefix}_{middle}{suffix}",
        st.sampled_from(prefixes),
        st.text(alphabet="abcdefghijklmnopqrstuvwxyz_", min_size=1, max_size=10),
        st.sampled_from(suffixes),
    )


def structural_value_strategy() -> st.SearchStrategy[Any]:
    """Strategy for generating valid structural values (no semantic content)."""
    return st.one_of(
        st.booleans(),
        st.integers(min_value=-1000, max_value=1000),
        st.floats(min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False),
        st.text(alphabet="abcdefghijklmnopqrstuvwxyz_", min_size=1, max_size=20),
        st.lists(st.integers(min_value=1, max_value=6), min_size=0, max_size=6),
    )


def factor_value_strategy() -> st.SearchStrategy[FactorValue]:
    """Strategy for generating valid FactorValue objects."""
    return st.builds(
        FactorValue,
        factor_id=valid_factor_id_strategy(),
        value=structural_value_strategy(),
        confidence=st.floats(min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False),
        source=st.sampled_from(["calculator", "semantic", "manual"]),
    )


def factor_matrix_strategy() -> st.SearchStrategy[FactorMatrix]:
    """Strategy for generating valid FactorMatrix objects."""
    return st.builds(
        lambda factors_list: FactorMatrix(
            factors={f.factor_id: f for f in factors_list},
            timestamp=datetime.now(),
            engine_id="test-calculator",
        ),
        st.lists(factor_value_strategy(), min_size=1, max_size=20),
    )


# =============================================================================
# Unit Tests for Validation Functions
# =============================================================================

class TestSemanticFieldDetection:
    """Tests for semantic field detection functions."""
    
    def test_known_semantic_fields_detected(self):
        """Known semantic field names should be detected."""
        for field_name in ["description", "meaning", "interpretation", "explanation"]:
            assert is_semantic_field_name(field_name), f"{field_name} should be detected"
    
    def test_chinese_semantic_fields_detected(self):
        """Chinese semantic field names should be detected."""
        for field_name in ["含义", "解释", "说明", "释义"]:
            assert is_semantic_field_name(field_name), f"{field_name} should be detected"
    
    def test_structural_fields_not_detected(self):
        """Structural field names should not be detected as semantic."""
        structural_fields = [
            "factor_id", "value", "confidence", "source",
            "stem", "branch", "position", "count", "score",
        ]
        for field_name in structural_fields:
            assert not is_semantic_field_name(field_name), f"{field_name} should not be detected"
    
    def test_pattern_matching(self):
        """Field names with semantic patterns should be detected."""
        assert is_semantic_field_name("card_meaning")
        assert is_semantic_field_name("symbol_description")
        assert is_semantic_field_name("gua_interpretation")
    
    def test_nested_semantic_content_detection(self):
        """Nested semantic content should be detected."""
        nested_dict = {
            "structural_field": "value",
            "nested": {
                "description": "This is semantic content",
            }
        }
        paths = check_value_for_semantic_content(nested_dict)
        assert len(paths) == 1
        assert "nested.description" in paths[0]


class TestFactorValueValidation:
    """Tests for FactorValue validation."""
    
    def test_valid_factor_value(self):
        """Valid FactorValue should pass validation."""
        factor = FactorValue(
            factor_id="bazi_day_master",
            value="甲",
            confidence=1.0,
            source="calculator"
        )
        is_valid, paths = validate_factor_value_no_semantics(factor)
        assert is_valid
        assert len(paths) == 0
    
    def test_factor_value_with_nested_semantic(self):
        """FactorValue with nested semantic content should fail validation."""
        factor = FactorValue(
            factor_id="test_factor",
            value={"description": "This is semantic content"},
            confidence=1.0,
            source="calculator"
        )
        is_valid, paths = validate_factor_value_no_semantics(factor)
        assert not is_valid
        assert len(paths) > 0


class TestFactorMatrixValidation:
    """Tests for FactorMatrix validation."""
    
    def test_valid_factor_matrix(self):
        """Valid FactorMatrix should pass validation."""
        matrix = FactorMatrix(
            factors={
                "bazi_day_master": FactorValue(
                    factor_id="bazi_day_master",
                    value="甲",
                    confidence=1.0,
                    source="calculator"
                ),
                "bazi_season": FactorValue(
                    factor_id="bazi_season",
                    value="spring",
                    confidence=1.0,
                    source="calculator"
                ),
            },
            timestamp=datetime.now(),
            engine_id="bazi-calculator"
        )
        result = validate_factor_matrix_no_semantics(matrix)
        assert result.is_valid
        assert len(result.semantic_fields_found) == 0
    
    def test_factor_matrix_with_semantic_content(self):
        """FactorMatrix with semantic content should fail validation."""
        matrix = FactorMatrix(
            factors={
                "test_factor": FactorValue(
                    factor_id="test_factor",
                    value={"meaning": "This is semantic"},
                    confidence=1.0,
                    source="calculator"
                ),
            },
            timestamp=datetime.now(),
            engine_id="test-calculator"
        )
        result = validate_factor_matrix_no_semantics(matrix)
        assert not result.is_valid
        assert len(result.semantic_fields_found) > 0


# =============================================================================
# Property-Based Tests
# =============================================================================

@property_test(
    property_id="1",
    property_name="Calculator 输出不包含语义字段",
    validates=["1.1", "1.2"],
    max_examples=100,
)
@given(matrix=factor_matrix_strategy())
def test_property_calculator_output_no_semantics(matrix: FactorMatrix):
    """
    **Feature: calculator-accuracy-audit, Property 1: Calculator 输出不包含语义字段**
    **Validates: Requirements 1.1, 1.2**
    
    Property: For any FactorMatrix produced by a Calculator,
    no FactorValue should contain semantic fields (description, meaning, etc.).
    
    This test generates random FactorMatrix objects with structural values only
    and verifies they pass validation.
    """
    # Validate the generated matrix
    result = validate_factor_matrix_no_semantics(matrix)
    
    # The generated matrix should always be valid since we use structural_value_strategy
    assert result.is_valid, (
        f"Generated FactorMatrix should be valid. "
        f"Found semantic fields: {result.semantic_fields_found}"
    )


@property_test(
    property_id="1b",
    property_name="语义字段检测完整性",
    validates=["1.1", "1.2"],
    max_examples=50,
)
@given(
    field_name=st.sampled_from(list(SEMANTIC_FIELD_NAMES)),
    value=st.text(min_size=1, max_size=50),
)
def test_property_semantic_fields_always_detected(field_name: str, value: str):
    """
    Property: All known semantic field names should always be detected.
    
    This ensures our detection logic is complete for known semantic fields.
    """
    # Create a dict with the semantic field
    test_dict = {field_name: value}
    
    # Check that it's detected
    paths = check_value_for_semantic_content(test_dict)
    
    assert len(paths) > 0, (
        f"Semantic field '{field_name}' should be detected but wasn't"
    )


# =============================================================================
# Integration Tests with Real Calculators
# =============================================================================

class TestRealCalculatorOutputValidation:
    """Integration tests validating real Calculator outputs."""
    
    def test_bazi_calculator_output_no_semantics(self):
        """BaziCalculator output should contain no semantic fields."""
        from backend.calculators.bazi import BaziCalculator, BaziInput
        
        calculator = BaziCalculator()
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Validate no semantic fields
        validation_result = validate_factor_matrix_no_semantics(factor_matrix)
        assert validation_result.is_valid, (
            f"BaziCalculator output contains semantic fields: "
            f"{validation_result.semantic_fields_found}"
        )
    
    def test_yijing_calculator_output_no_semantics(self):
        """YijingCalculator output should contain no semantic fields."""
        from backend.calculators.yijing import YijingCalculator, YijingInput
        
        calculator = YijingCalculator()
        input_data = YijingInput(
            divination_method="manual",
            manual_lines=[7, 8, 9, 7, 6, 8]
        )
        
        result = calculator.calculate(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Validate no semantic fields
        validation_result = validate_factor_matrix_no_semantics(factor_matrix)
        assert validation_result.is_valid, (
            f"YijingCalculator output contains semantic fields: "
            f"{validation_result.semantic_fields_found}"
        )
    
    def test_bazi_factors_raw_output_no_semantics(self):
        """BaziFactors raw output should contain no semantic fields."""
        from backend.calculators.bazi import BaziCalculator, BaziInput
        
        calculator = BaziCalculator()
        input_data = BaziInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            gender="male"
        )
        
        result = calculator.calculate(input_data)
        
        # Validate raw output (before conversion to FactorMatrix)
        validation_result = validate_calculator_output(result)
        assert validation_result.is_valid, (
            f"BaziFactors raw output contains semantic fields: "
            f"{validation_result.semantic_fields_found}"
        )
    
    def test_yijing_factors_raw_output_no_semantics(self):
        """YijingFactors raw output should contain no semantic fields."""
        from backend.calculators.yijing import YijingCalculator, YijingInput
        
        calculator = YijingCalculator()
        input_data = YijingInput(
            divination_method="coin"
        )
        
        result = calculator.calculate(input_data)
        
        # Validate raw output (before conversion to FactorMatrix)
        validation_result = validate_calculator_output(result)
        assert validation_result.is_valid, (
            f"YijingFactors raw output contains semantic fields: "
            f"{validation_result.semantic_fields_found}"
        )
