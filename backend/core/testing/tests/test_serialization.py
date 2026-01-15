# backend/core/testing/tests/test_serialization.py
"""
Property-based tests for FactorMatrix serialization round-trip consistency.

**Feature: calculator-accuracy-audit, Property 14: FactorMatrix 序列化往返一致性**
**Validates: Requirements 13.1-13.6**

Tests that all FactorMatrix instances can be serialized and deserialized
without data loss across all calculator types.
"""

import pytest
from datetime import datetime
from typing import Any, Dict, List

from hypothesis import given, settings
from hypothesis import strategies as st

from backend.core.contracts import FactorValue, FactorMatrix
from backend.core.testing.serialization import (
    validate_round_trip,
    validate_round_trip_json,
    validate_round_trip_dict,
    assert_round_trip_consistency,
    assert_json_round_trip,
)
from backend.core.testing.property_tests import property_test


# =============================================================================
# Hypothesis Strategies for FactorMatrix Generation
# =============================================================================

def factor_id_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating valid factor IDs."""
    prefixes = [
        "bazi", "ziwei", "yijing", "astro", "tarot", "dream",
        "day_master", "pillar", "element", "ten_god", "season",
        "strength", "dayun", "ziwei_star", "ziwei_palace",
        "yijing_gua", "yijing_line", "astro_sun", "astro_moon",
        "tarot_major", "tarot_minor", "dream_symbol", "dream_theme"
    ]
    suffixes = [
        "jia", "yi", "bing", "ding", "wu", "ji", "geng", "xin", "ren", "gui",
        "zi", "chou", "yin", "mao", "chen", "si", "wu", "wei", "shen", "you",
        "spring", "summer", "autumn", "winter", "strong", "weak", "neutral",
        "qian", "kun", "zhen", "xun", "kan", "li", "gen", "dui",
        "aries", "taurus", "gemini", "cancer", "leo", "virgo",
        "upright", "reversed", "animal", "person", "scene"
    ]
    return st.builds(
        lambda prefix, suffix: f"{prefix}_{suffix}",
        st.sampled_from(prefixes),
        st.sampled_from(suffixes)
    )


def factor_value_strategy() -> st.SearchStrategy[Any]:
    """Strategy for generating valid factor values."""
    return st.one_of(
        st.booleans(),
        st.integers(min_value=-1000, max_value=1000),
        st.floats(min_value=-1000.0, max_value=1000.0, allow_nan=False, allow_infinity=False),
        st.text(min_size=1, max_size=50, alphabet=st.characters(
            whitelist_categories=('L', 'N'),
            whitelist_characters='_-'
        )),
        st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=10),
        st.lists(st.text(min_size=1, max_size=20, alphabet=st.characters(
            whitelist_categories=('L', 'N'),
            whitelist_characters='_-'
        )), min_size=0, max_size=5),
    )


def factor_value_model_strategy() -> st.SearchStrategy[FactorValue]:
    """Strategy for generating FactorValue instances."""
    return st.builds(
        FactorValue,
        factor_id=factor_id_strategy(),
        value=factor_value_strategy(),
        confidence=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        source=st.sampled_from(["calculator", "semantic", "manual"]),
    )


def engine_id_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating engine IDs."""
    return st.sampled_from([
        "bazi-calculator",
        "ziwei-calculator",
        "yijing-calculator",
        "astro-calculator",
        "tarot-interpreter",
        "dream-extractor",
    ])


def factor_matrix_strategy(
    min_factors: int = 1,
    max_factors: int = 50
) -> st.SearchStrategy[FactorMatrix]:
    """Strategy for generating FactorMatrix instances."""
    return st.builds(
        lambda factors_list, engine_id: FactorMatrix(
            factors={f.factor_id: f for f in factors_list},
            timestamp=datetime.now(),
            engine_id=engine_id,
        ),
        factors_list=st.lists(
            factor_value_model_strategy(),
            min_size=min_factors,
            max_size=max_factors,
            unique_by=lambda f: f.factor_id,
        ),
        engine_id=engine_id_strategy(),
    )


# =============================================================================
# Property Tests
# =============================================================================

@property_test(
    property_id="14",
    property_name="FactorMatrix 序列化往返一致性",
    validates=["13.1", "13.2", "13.3", "13.4", "13.5", "13.6"],
    max_examples=100,
)
@given(matrix=factor_matrix_strategy())
def test_factor_matrix_round_trip_consistency(matrix: FactorMatrix):
    """
    Property 14: FactorMatrix 序列化往返一致性
    
    *对于任意* 有效的 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14: FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.1-13.6**
    """
    result = validate_round_trip(matrix)
    
    assert result.is_valid, (
        f"Round-trip validation failed. "
        f"Missing: {result.missing_factors}, "
        f"Extra: {result.extra_factors}, "
        f"Mismatched: {result.mismatched_factors}, "
        f"Warnings: {result.warnings}"
    )


@property_test(
    property_id="14.1",
    property_name="FactorMatrix JSON 序列化往返一致性",
    validates=["13.1", "13.2", "13.3", "13.4", "13.5", "13.6"],
    max_examples=100,
)
@given(matrix=factor_matrix_strategy())
def test_factor_matrix_json_round_trip(matrix: FactorMatrix):
    """
    Property 14.1: FactorMatrix JSON 序列化往返一致性
    
    *对于任意* 有效的 FactorMatrix，JSON 序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.1: FactorMatrix JSON 序列化往返一致性**
    **Validates: Requirements 13.1-13.6**
    """
    result = validate_round_trip_json(matrix)
    
    assert result.is_valid, (
        f"JSON round-trip validation failed. "
        f"Missing: {result.missing_factors}, "
        f"Extra: {result.extra_factors}, "
        f"Mismatched: {result.mismatched_factors}"
    )


@property_test(
    property_id="14.2",
    property_name="FactorMatrix Dict 序列化往返一致性",
    validates=["13.1", "13.2", "13.3", "13.4", "13.5", "13.6"],
    max_examples=100,
)
@given(matrix=factor_matrix_strategy())
def test_factor_matrix_dict_round_trip(matrix: FactorMatrix):
    """
    Property 14.2: FactorMatrix Dict 序列化往返一致性
    
    *对于任意* 有效的 FactorMatrix，Dict 序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.2: FactorMatrix Dict 序列化往返一致性**
    **Validates: Requirements 13.1-13.6**
    """
    result = validate_round_trip_dict(matrix)
    
    assert result.is_valid, (
        f"Dict round-trip validation failed. "
        f"Missing: {result.missing_factors}, "
        f"Extra: {result.extra_factors}, "
        f"Mismatched: {result.mismatched_factors}"
    )


# =============================================================================
# Calculator-Specific Round-Trip Tests
# =============================================================================

def specific_engine_factor_matrix_strategy(
    engine_id: str,
    min_factors: int = 1,
    max_factors: int = 50
) -> st.SearchStrategy[FactorMatrix]:
    """Strategy for generating FactorMatrix instances with a specific engine_id."""
    return st.builds(
        lambda factors_list: FactorMatrix(
            factors={f.factor_id: f for f in factors_list},
            timestamp=datetime.now(),
            engine_id=engine_id,
        ),
        factors_list=st.lists(
            factor_value_model_strategy(),
            min_size=min_factors,
            max_size=max_factors,
            unique_by=lambda f: f.factor_id,
        ),
    )


@property_test(
    property_id="14.3",
    property_name="八字 FactorMatrix 序列化往返一致性",
    validates=["13.1"],
    max_examples=50,
)
@given(matrix=specific_engine_factor_matrix_strategy("bazi-calculator"))
def test_bazi_factor_matrix_round_trip(matrix: FactorMatrix):
    """
    Property 14.3: 八字 FactorMatrix 序列化往返一致性
    
    *对于任意* 八字 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.3: 八字 FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.1**
    """
    result = validate_round_trip(matrix)
    assert result.is_valid, f"Bazi round-trip failed: {result.warnings}"


@property_test(
    property_id="14.4",
    property_name="紫微 FactorMatrix 序列化往返一致性",
    validates=["13.2"],
    max_examples=50,
)
@given(matrix=specific_engine_factor_matrix_strategy("ziwei-calculator"))
def test_ziwei_factor_matrix_round_trip(matrix: FactorMatrix):
    """
    Property 14.4: 紫微 FactorMatrix 序列化往返一致性
    
    *对于任意* 紫微 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.4: 紫微 FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.2**
    """
    result = validate_round_trip(matrix)
    assert result.is_valid, f"Ziwei round-trip failed: {result.warnings}"


@property_test(
    property_id="14.5",
    property_name="易经 FactorMatrix 序列化往返一致性",
    validates=["13.3"],
    max_examples=50,
)
@given(matrix=specific_engine_factor_matrix_strategy("yijing-calculator"))
def test_yijing_factor_matrix_round_trip(matrix: FactorMatrix):
    """
    Property 14.5: 易经 FactorMatrix 序列化往返一致性
    
    *对于任意* 易经 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.5: 易经 FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.3**
    """
    result = validate_round_trip(matrix)
    assert result.is_valid, f"Yijing round-trip failed: {result.warnings}"


@property_test(
    property_id="14.6",
    property_name="占星 FactorMatrix 序列化往返一致性",
    validates=["13.4"],
    max_examples=50,
)
@given(matrix=specific_engine_factor_matrix_strategy("astro-calculator"))
def test_astro_factor_matrix_round_trip(matrix: FactorMatrix):
    """
    Property 14.6: 占星 FactorMatrix 序列化往返一致性
    
    *对于任意* 占星 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.6: 占星 FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.4**
    """
    result = validate_round_trip(matrix)
    assert result.is_valid, f"Astro round-trip failed: {result.warnings}"


@property_test(
    property_id="14.7",
    property_name="塔罗 FactorMatrix 序列化往返一致性",
    validates=["13.5"],
    max_examples=50,
)
@given(matrix=specific_engine_factor_matrix_strategy("tarot-interpreter"))
def test_tarot_factor_matrix_round_trip(matrix: FactorMatrix):
    """
    Property 14.7: 塔罗 FactorMatrix 序列化往返一致性
    
    *对于任意* 塔罗 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.7: 塔罗 FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.5**
    """
    result = validate_round_trip(matrix)
    assert result.is_valid, f"Tarot round-trip failed: {result.warnings}"


@property_test(
    property_id="14.8",
    property_name="梦境 FactorMatrix 序列化往返一致性",
    validates=["13.6"],
    max_examples=50,
)
@given(matrix=specific_engine_factor_matrix_strategy("dream-extractor"))
def test_dream_factor_matrix_round_trip(matrix: FactorMatrix):
    """
    Property 14.8: 梦境 FactorMatrix 序列化往返一致性
    
    *对于任意* 梦境 FactorMatrix，序列化后再反序列化应得到与原始对象相等的结果。
    
    **Feature: calculator-accuracy-audit, Property 14.8: 梦境 FactorMatrix 序列化往返一致性**
    **Validates: Requirements 13.6**
    """
    result = validate_round_trip(matrix)
    assert result.is_valid, f"Dream round-trip failed: {result.warnings}"


# =============================================================================
# Edge Case Tests
# =============================================================================

class TestSerializationEdgeCases:
    """Unit tests for serialization edge cases."""
    
    def test_empty_factor_matrix(self):
        """Test round-trip with empty factors."""
        matrix = FactorMatrix(
            factors={},
            timestamp=datetime.now(),
            engine_id="test-engine",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
        assert result.original_factor_count == 0
        assert result.restored_factor_count == 0
    
    def test_single_factor_matrix(self):
        """Test round-trip with single factor."""
        matrix = FactorMatrix(
            factors={
                "test_factor": FactorValue(
                    factor_id="test_factor",
                    value=True,
                    confidence=1.0,
                    source="calculator",
                )
            },
            timestamp=datetime.now(),
            engine_id="test-engine",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
        assert result.original_factor_count == 1
    
    def test_factor_with_float_value(self):
        """Test round-trip with float values."""
        matrix = FactorMatrix(
            factors={
                "float_factor": FactorValue(
                    factor_id="float_factor",
                    value=0.123456789,
                    confidence=0.95,
                    source="calculator",
                )
            },
            timestamp=datetime.now(),
            engine_id="test-engine",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
    
    def test_factor_with_list_value(self):
        """Test round-trip with list values."""
        matrix = FactorMatrix(
            factors={
                "list_factor": FactorValue(
                    factor_id="list_factor",
                    value=[1, 2, 3, 4, 5],
                    confidence=1.0,
                    source="calculator",
                )
            },
            timestamp=datetime.now(),
            engine_id="test-engine",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
    
    def test_factor_with_dict_value(self):
        """Test round-trip with dict values."""
        matrix = FactorMatrix(
            factors={
                "dict_factor": FactorValue(
                    factor_id="dict_factor",
                    value={"key1": "value1", "key2": 123},
                    confidence=1.0,
                    source="calculator",
                )
            },
            timestamp=datetime.now(),
            engine_id="test-engine",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
    
    def test_factor_with_chinese_characters(self):
        """Test round-trip with Chinese character values."""
        matrix = FactorMatrix(
            factors={
                "chinese_factor": FactorValue(
                    factor_id="chinese_factor",
                    value="甲乙丙丁戊己庚辛壬癸",
                    confidence=1.0,
                    source="calculator",
                )
            },
            timestamp=datetime.now(),
            engine_id="bazi-calculator",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
    
    def test_large_factor_matrix(self):
        """Test round-trip with many factors."""
        factors = {}
        for i in range(100):
            factor_id = f"factor_{i}"
            factors[factor_id] = FactorValue(
                factor_id=factor_id,
                value=i * 0.1,
                confidence=1.0,
                source="calculator",
            )
        
        matrix = FactorMatrix(
            factors=factors,
            timestamp=datetime.now(),
            engine_id="test-engine",
        )
        result = validate_round_trip(matrix)
        assert result.is_valid
        assert result.original_factor_count == 100
