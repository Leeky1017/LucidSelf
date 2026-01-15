# backend/core/contracts/tests/test_validation.py
"""
Tests for FactorMatrix Validation Tools

Tests validation of:
- Factor ID naming convention ({system}_*)
- Required field presence (confidence, source)
- Engine ID consistency

Requirements: 10.1, 10.2, 10.3, 10.4
"""

import pytest
from datetime import datetime

from backend.core.contracts import (
    FactorMatrix,
    FactorValue,
    VALID_SYSTEM_PREFIXES,
    VALID_SOURCES,
    ValidationError,
    ValidationResult,
    validate_factor_id_format,
    validate_factor_value,
    validate_factor_matrix,
    get_system_from_factor_id,
    is_valid_factor_id,
)


# =============================================================================
# validate_factor_id_format Tests
# =============================================================================


class TestValidateFactorIdFormat:
    """Tests for validate_factor_id_format function."""

    def test_valid_bazi_factor_ids(self):
        """Test valid bazi factor IDs."""
        valid_ids = [
            "bazi_day_master_jia",
            "bazi_season_spring",
            "bazi_strength_strong",
            "bazi_element_wood_score",
            "bazi_ten_god_zhengguan",
            "bazi_pillar_year_stem",
        ]
        for factor_id in valid_ids:
            assert validate_factor_id_format(factor_id) is None, f"Expected valid: {factor_id}"

    def test_valid_ziwei_factor_ids(self):
        """Test valid ziwei factor IDs."""
        valid_ids = [
            "ziwei_palace_ming",
            "ziwei_star_ziwei",
            "ziwei_sihua_lu",
        ]
        for factor_id in valid_ids:
            assert validate_factor_id_format(factor_id) is None, f"Expected valid: {factor_id}"

    def test_valid_astro_factor_ids(self):
        """Test valid astro factor IDs."""
        valid_ids = [
            "astro_sun_in_aries",
            "astro_moon_house_1",
            "astro_mars_retrograde",
            "astro_ascendant",
            "astro_sun_conjunction_moon",
        ]
        for factor_id in valid_ids:
            assert validate_factor_id_format(factor_id) is None, f"Expected valid: {factor_id}"

    def test_valid_tarot_factor_ids(self):
        """Test valid tarot factor IDs."""
        valid_ids = [
            "tarot_major_the_fool_upright",
            "tarot_wands_ace_reversed",
            "tarot_spread_three_card",
            "tarot_position_past_the_fool",
            "tarot_card_number_0",
        ]
        for factor_id in valid_ids:
            assert validate_factor_id_format(factor_id) is None, f"Expected valid: {factor_id}"

    def test_valid_dream_factor_ids(self):
        """Test valid dream factor IDs."""
        valid_ids = [
            "dream_symbol_animal_dog",
            "dream_theme_chase",
            "dream_emotion_fear",
        ]
        for factor_id in valid_ids:
            assert validate_factor_id_format(factor_id) is None, f"Expected valid: {factor_id}"

    def test_valid_yijing_factor_ids(self):
        """Test valid yijing factor IDs."""
        valid_ids = [
            "yijing_gua_qian",
            "yijing_upper_trigram",
            "yijing_lower_trigram",
            "yijing_mutual_kun",
            "yijing_moving_yao_1",
            "yijing_changed_kun",
        ]
        for factor_id in valid_ids:
            assert validate_factor_id_format(factor_id) is None, f"Expected valid: {factor_id}"

    def test_invalid_empty_factor_id(self):
        """Test empty factor ID."""
        error = validate_factor_id_format("")
        assert error is not None
        assert "empty" in error.lower()

    def test_invalid_no_underscore(self):
        """Test factor ID without underscore."""
        error = validate_factor_id_format("bazidaymaster")
        assert error is not None
        assert "two segments" in error.lower()

    def test_invalid_system_prefix(self):
        """Test invalid system prefix."""
        error = validate_factor_id_format("invalid_factor_id")
        assert error is not None
        assert "invalid system prefix" in error.lower()
        assert "invalid" in error

    def test_invalid_uppercase(self):
        """Test factor ID with uppercase."""
        error = validate_factor_id_format("bazi_DayMaster_jia")
        assert error is not None
        assert "pattern" in error.lower()

    def test_invalid_special_characters(self):
        """Test factor ID with special characters."""
        invalid_ids = [
            "bazi-day-master",  # hyphens
            "bazi.day.master",  # dots
            "bazi day master",  # spaces
            "bazi_day@master",  # @ symbol
        ]
        for factor_id in invalid_ids:
            error = validate_factor_id_format(factor_id)
            assert error is not None, f"Expected invalid: {factor_id}"


# =============================================================================
# validate_factor_value Tests
# =============================================================================


class TestValidateFactorValue:
    """Tests for validate_factor_value function."""

    def test_valid_factor_value(self):
        """Test valid FactorValue."""
        fv = FactorValue(
            factor_id="bazi_day_master_jia",
            value=True,
            confidence=1.0,
            source="calculator",
        )
        errors = validate_factor_value("bazi_day_master_jia", fv)
        assert len(errors) == 0

    def test_factor_id_mismatch(self):
        """Test factor ID mismatch between key and value."""
        fv = FactorValue(
            factor_id="bazi_day_master_yi",  # Different from key
            value=True,
            confidence=1.0,
            source="calculator",
        )
        errors = validate_factor_value("bazi_day_master_jia", fv)
        assert len(errors) == 1
        assert "mismatch" in errors[0].message.lower()

    def test_valid_sources(self):
        """Test all valid source values."""
        for source in VALID_SOURCES:
            fv = FactorValue(
                factor_id="bazi_test",
                value=True,
                confidence=1.0,
                source=source,
            )
            errors = validate_factor_value("bazi_test", fv)
            assert len(errors) == 0, f"Source '{source}' should be valid"


# =============================================================================
# validate_factor_matrix Tests
# =============================================================================


class TestValidateFactorMatrix:
    """Tests for validate_factor_matrix function."""

    def test_valid_bazi_matrix(self):
        """Test valid BaziCalculator output."""
        matrix = FactorMatrix(
            factors={
                "bazi_day_master_jia": FactorValue(
                    factor_id="bazi_day_master_jia",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
                "bazi_season_spring": FactorValue(
                    factor_id="bazi_season_spring",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="bazi-calculator",
        )
        result = validate_factor_matrix(matrix)
        assert result.valid is True
        assert result.factor_count == 2
        assert "bazi" in result.systems_found

    def test_valid_astro_matrix(self):
        """Test valid AstroCalculator output."""
        matrix = FactorMatrix(
            factors={
                "astro_sun_in_aries": FactorValue(
                    factor_id="astro_sun_in_aries",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
                "astro_moon_house_1": FactorValue(
                    factor_id="astro_moon_house_1",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="astro-calculator",
        )
        result = validate_factor_matrix(matrix)
        assert result.valid is True
        assert "astro" in result.systems_found

    def test_empty_matrix(self):
        """Test empty factor matrix."""
        matrix = FactorMatrix(
            factors={},
            engine_id="test-calculator",
        )
        result = validate_factor_matrix(matrix)
        assert result.valid is True
        assert result.factor_count == 0

    def test_missing_engine_id(self):
        """Test matrix with empty engine_id."""
        matrix = FactorMatrix(
            factors={},
            engine_id="",
        )
        result = validate_factor_matrix(matrix)
        assert result.valid is False
        assert any("engine" in e.field.lower() for e in result.errors)

    def test_invalid_factor_id_in_matrix(self):
        """Test matrix with invalid factor ID."""
        matrix = FactorMatrix(
            factors={
                "invalid_factor": FactorValue(
                    factor_id="invalid_factor",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="test-calculator",
        )
        result = validate_factor_matrix(matrix)
        assert result.valid is False
        assert any("invalid system prefix" in e.message.lower() for e in result.errors)

    def test_expected_system_validation(self):
        """Test validation with expected system."""
        matrix = FactorMatrix(
            factors={
                "bazi_day_master_jia": FactorValue(
                    factor_id="bazi_day_master_jia",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="bazi-calculator",
        )
        
        # Should pass with correct expected system
        result = validate_factor_matrix(matrix, expected_system="bazi")
        assert result.valid is True
        
        # Should fail with wrong expected system
        result = validate_factor_matrix(matrix, expected_system="astro")
        assert result.valid is False
        assert any("expected 'astro'" in e.message.lower() for e in result.errors)

    def test_multiple_systems_warning(self):
        """Test warning for multiple systems in one matrix."""
        matrix = FactorMatrix(
            factors={
                "bazi_day_master_jia": FactorValue(
                    factor_id="bazi_day_master_jia",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
                "astro_sun_in_aries": FactorValue(
                    factor_id="astro_sun_in_aries",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                ),
            },
            engine_id="mixed-calculator",
        )
        
        # Non-strict mode: warning only
        result = validate_factor_matrix(matrix, strict=False)
        assert result.valid is True
        assert len(result.warnings) > 0
        assert any("multiple system" in w.message.lower() for w in result.warnings)
        
        # Strict mode: error
        result = validate_factor_matrix(matrix, strict=True)
        assert result.valid is False


# =============================================================================
# Helper Function Tests
# =============================================================================


class TestHelperFunctions:
    """Tests for helper functions."""

    def test_get_system_from_factor_id(self):
        """Test get_system_from_factor_id function."""
        assert get_system_from_factor_id("bazi_day_master_jia") == "bazi"
        assert get_system_from_factor_id("astro_sun_in_aries") == "astro"
        assert get_system_from_factor_id("tarot_major_fool") == "tarot"
        assert get_system_from_factor_id("dream_symbol_dog") == "dream"
        assert get_system_from_factor_id("yijing_gua_qian") == "yijing"
        assert get_system_from_factor_id("ziwei_palace_ming") == "ziwei"
        
        # Invalid cases
        assert get_system_from_factor_id("invalid_factor") is None
        assert get_system_from_factor_id("nounderscore") is None
        assert get_system_from_factor_id("") is None

    def test_is_valid_factor_id(self):
        """Test is_valid_factor_id function."""
        assert is_valid_factor_id("bazi_day_master_jia") is True
        assert is_valid_factor_id("astro_sun_in_aries") is True
        
        assert is_valid_factor_id("invalid_factor") is False
        assert is_valid_factor_id("") is False
        assert is_valid_factor_id("BAZI_DAY_MASTER") is False


# =============================================================================
# Constants Tests
# =============================================================================


class TestConstants:
    """Tests for validation constants."""

    def test_valid_system_prefixes(self):
        """Test that all expected system prefixes are defined."""
        expected = {"bazi", "ziwei", "astro", "tarot", "dream", "yijing"}
        assert VALID_SYSTEM_PREFIXES == expected

    def test_valid_sources(self):
        """Test that all expected sources are defined."""
        expected = {"calculator", "semantic", "manual", "llm_infer"}
        assert VALID_SOURCES == expected
