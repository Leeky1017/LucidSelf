# backend/core/contracts/tests/test_validation_pbt.py
"""
Property-Based Tests for FactorMatrix Output Consistency

**Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
**Validates: Requirements 10.1, 10.2, 10.3**

Tests that all Calculator outputs produce valid FactorMatrix with:
- Factor IDs following {system}_* naming convention
- Required fields (confidence, source) present
- Engine ID consistency
"""

import pytest
from datetime import datetime
from typing import Dict, List, Optional

from hypothesis import given, settings, assume
from hypothesis import strategies as st

from backend.core.contracts import (
    FactorMatrix,
    FactorValue,
    VALID_SYSTEM_PREFIXES,
    VALID_SOURCES,
    validate_factor_matrix,
    is_valid_factor_id,
)


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for valid system prefixes
system_prefix_strategy = st.sampled_from(list(VALID_SYSTEM_PREFIXES))

# Strategy for valid source values
source_strategy = st.sampled_from(list(VALID_SOURCES))

# Strategy for valid confidence values
confidence_strategy = st.floats(min_value=0.0, max_value=1.0, allow_nan=False)

# Strategy for factor ID suffixes (lowercase alphanumeric with underscores)
factor_suffix_strategy = st.from_regex(r"[a-z][a-z0-9]*(_[a-z0-9]+)*", fullmatch=True)

# Strategy for factor values (various types)
factor_value_strategy = st.one_of(
    st.booleans(),
    st.integers(min_value=-1000, max_value=1000),
    st.floats(min_value=-1000.0, max_value=1000.0, allow_nan=False, allow_infinity=False),
    st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=('L', 'N'))),
)


@st.composite
def valid_factor_id_strategy(draw):
    """Generate a valid factor ID with system prefix."""
    system = draw(system_prefix_strategy)
    suffix = draw(factor_suffix_strategy)
    return f"{system}_{suffix}"


@st.composite
def valid_factor_value_strategy(draw, factor_id: Optional[str] = None):
    """Generate a valid FactorValue."""
    if factor_id is None:
        factor_id = draw(valid_factor_id_strategy())
    
    return FactorValue(
        factor_id=factor_id,
        value=draw(factor_value_strategy),
        confidence=draw(confidence_strategy),
        source=draw(source_strategy),
    )


@st.composite
def valid_factor_matrix_strategy(draw, system: Optional[str] = None, min_factors: int = 0, max_factors: int = 20):
    """Generate a valid FactorMatrix."""
    if system is None:
        system = draw(system_prefix_strategy)
    
    num_factors = draw(st.integers(min_value=min_factors, max_value=max_factors))
    
    factors: Dict[str, FactorValue] = {}
    for _ in range(num_factors):
        suffix = draw(factor_suffix_strategy)
        factor_id = f"{system}_{suffix}"
        
        # Avoid duplicate factor IDs
        if factor_id in factors:
            continue
            
        factors[factor_id] = FactorValue(
            factor_id=factor_id,
            value=draw(factor_value_strategy),
            confidence=draw(confidence_strategy),
            source=draw(source_strategy),
        )
    
    engine_id = f"{system}-calculator"
    
    return FactorMatrix(
        factors=factors,
        engine_id=engine_id,
    )


# =============================================================================
# Property-Based Tests
# =============================================================================


class TestFactorMatrixOutputConsistency:
    """
    **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
    **Validates: Requirements 10.1, 10.2, 10.3**
    
    *For any* Calculator, the to_factor_matrix() method must return a valid 
    FactorMatrix with factor IDs following the {system}_* naming convention.
    """

    @settings(max_examples=100)
    @given(matrix=valid_factor_matrix_strategy())
    def test_valid_matrix_passes_validation(self, matrix: FactorMatrix):
        """
        **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
        **Validates: Requirements 10.1, 10.2, 10.3**
        
        Property: Any FactorMatrix generated with valid system prefixes and 
        required fields should pass validation.
        """
        result = validate_factor_matrix(matrix, strict=False)
        
        assert result.valid, (
            f"Valid matrix should pass validation. Errors: "
            f"{[e.message for e in result.errors]}"
        )

    @settings(max_examples=100)
    @given(matrix=valid_factor_matrix_strategy(min_factors=1))
    def test_all_factor_ids_have_valid_system_prefix(self, matrix: FactorMatrix):
        """
        **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
        **Validates: Requirements 10.2**
        
        Property: All factor IDs in a FactorMatrix must start with a valid 
        system prefix (bazi_, ziwei_, astro_, tarot_, dream_, yijing_).
        """
        for factor_id in matrix.factors.keys():
            assert is_valid_factor_id(factor_id), (
                f"Factor ID '{factor_id}' should have valid system prefix"
            )

    @settings(max_examples=100)
    @given(matrix=valid_factor_matrix_strategy(min_factors=1))
    def test_all_factor_values_have_required_fields(self, matrix: FactorMatrix):
        """
        **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
        **Validates: Requirements 10.1, 10.3**
        
        Property: All FactorValues must have confidence in [0.0, 1.0] and 
        a valid source value.
        """
        for factor_id, factor_value in matrix.factors.items():
            # Check confidence range
            assert 0.0 <= factor_value.confidence <= 1.0, (
                f"Factor '{factor_id}' has invalid confidence: {factor_value.confidence}"
            )
            
            # Check source validity
            assert factor_value.source in VALID_SOURCES, (
                f"Factor '{factor_id}' has invalid source: {factor_value.source}"
            )

    @settings(max_examples=100)
    @given(matrix=valid_factor_matrix_strategy(min_factors=1))
    def test_factor_id_consistency(self, matrix: FactorMatrix):
        """
        **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
        **Validates: Requirements 10.3**
        
        Property: The factor_id in FactorValue must match the key in the 
        factors dictionary.
        """
        for key, factor_value in matrix.factors.items():
            assert key == factor_value.factor_id, (
                f"Factor ID mismatch: key='{key}', value.factor_id='{factor_value.factor_id}'"
            )

    @settings(max_examples=100)
    @given(matrix=valid_factor_matrix_strategy())
    def test_engine_id_is_present(self, matrix: FactorMatrix):
        """
        **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
        **Validates: Requirements 10.1**
        
        Property: Every FactorMatrix must have a non-empty engine_id.
        """
        assert matrix.engine_id, "FactorMatrix must have a non-empty engine_id"

    @settings(max_examples=100)
    @given(system=system_prefix_strategy)
    def test_single_system_per_calculator(self, system: str):
        """
        **Feature: calculator-integration, Property 10: FactorMatrix Output Consistency**
        **Validates: Requirements 10.2**
        
        Property: A single Calculator should produce factors with only one 
        system prefix.
        """
        # Generate a matrix for a specific system
        factors = {
            f"{system}_factor_1": FactorValue(
                factor_id=f"{system}_factor_1",
                value=True,
                confidence=1.0,
                source="calculator",
            ),
            f"{system}_factor_2": FactorValue(
                factor_id=f"{system}_factor_2",
                value=False,
                confidence=0.9,
                source="calculator",
            ),
        }
        
        matrix = FactorMatrix(
            factors=factors,
            engine_id=f"{system}-calculator",
        )
        
        result = validate_factor_matrix(matrix, expected_system=system)
        assert result.valid, (
            f"Matrix with system '{system}' should pass validation with "
            f"expected_system='{system}'. Errors: {[e.message for e in result.errors]}"
        )


class TestFactorIdNamingConvention:
    """
    Tests for factor ID naming convention compliance.
    
    **Validates: Requirements 10.2**
    """

    @settings(max_examples=100)
    @given(
        system=system_prefix_strategy,
        suffix=factor_suffix_strategy,
    )
    def test_valid_factor_id_format(self, system: str, suffix: str):
        """
        Property: Factor IDs with valid system prefix and lowercase 
        alphanumeric suffix should be valid.
        """
        factor_id = f"{system}_{suffix}"
        assert is_valid_factor_id(factor_id), (
            f"Factor ID '{factor_id}' should be valid"
        )

    @settings(max_examples=50)
    @given(
        invalid_prefix=st.sampled_from([
            "foo", "bar", "test", "invalid", "unknown", "custom", 
            "xyz", "abc", "qwerty", "hello", "world", "factor",
            "calc", "engine", "system", "prefix", "data", "value"
        ]),
        suffix=factor_suffix_strategy,
    )
    def test_invalid_system_prefix_rejected(self, invalid_prefix: str, suffix: str):
        """
        Property: Factor IDs with invalid system prefix should be rejected.
        """
        factor_id = f"{invalid_prefix}_{suffix}"
        
        assert not is_valid_factor_id(factor_id), (
            f"Factor ID '{factor_id}' with invalid prefix should be rejected"
        )


class TestCalculatorSpecificFactorIds:
    """
    Tests for calculator-specific factor ID patterns.
    
    **Validates: Requirements 10.2, 10.3**
    """

    @settings(max_examples=50)
    @given(
        stem=st.sampled_from(["jia", "yi", "bing", "ding", "wu", "ji", "geng", "xin", "ren", "gui"]),
    )
    def test_bazi_day_master_factor_ids(self, stem: str):
        """Property: BaziCalculator day_master factor IDs should be valid."""
        factor_id = f"bazi_day_master_{stem}"
        assert is_valid_factor_id(factor_id)

    @settings(max_examples=50)
    @given(
        planet=st.sampled_from(["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]),
        sign=st.sampled_from(["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]),
    )
    def test_astro_planet_sign_factor_ids(self, planet: str, sign: str):
        """Property: AstroCalculator planet-in-sign factor IDs should be valid."""
        factor_id = f"astro_{planet}_in_{sign}"
        assert is_valid_factor_id(factor_id)

    @settings(max_examples=50)
    @given(
        category=st.sampled_from(["animal", "person", "scene", "object", "nature", "body"]),
        symbol=st.from_regex(r"[a-z][a-z0-9]*", fullmatch=True),
    )
    def test_dream_symbol_factor_ids(self, category: str, symbol: str):
        """Property: DreamExtractor symbol factor IDs should be valid."""
        factor_id = f"dream_symbol_{category}_{symbol}"
        assert is_valid_factor_id(factor_id)

    @settings(max_examples=50)
    @given(
        gua=st.sampled_from(["qian", "kun", "zhen", "xun", "kan", "li", "gen", "dui"]),
    )
    def test_yijing_gua_factor_ids(self, gua: str):
        """Property: YijingCalculator gua factor IDs should be valid."""
        factor_id = f"yijing_gua_{gua}"
        assert is_valid_factor_id(factor_id)

    @settings(max_examples=50)
    @given(
        card_number=st.integers(min_value=0, max_value=77),
    )
    def test_tarot_card_number_factor_ids(self, card_number: int):
        """Property: TarotInterpreter card number factor IDs should be valid."""
        factor_id = f"tarot_card_number_{card_number}"
        assert is_valid_factor_id(factor_id)
