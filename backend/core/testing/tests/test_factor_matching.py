# backend/core/testing/tests/test_factor_matching.py
"""
Property-based tests for factor matching precision.

Validates that factor matching follows the exact match principle:
- Only exact matches are allowed
- No fuzzy matching or similarity matching
- Trigger conditions must be precisely satisfied

**Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
**Validates: Requirements 12.1, 12.2**
"""

import pytest
from datetime import datetime
from typing import Any, Dict, List, Optional

from hypothesis import given, settings, assume
from hypothesis import strategies as st

from backend.core.contracts import FactorValue, FactorMatrix
from backend.core.testing.factor_matching import (
    TriggerCondition,
    MatchResult,
    parse_trigger_condition,
    validate_exact_match,
    ExactMatchSnippetIndex,
    assert_exact_match_only,
    assert_no_similar_matches,
)
from backend.core.testing.property_tests import property_test


# =============================================================================
# Hypothesis Strategies
# =============================================================================

def factor_id_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating factor IDs."""
    return st.sampled_from([
        "day_master", "month", "season", "element_score",
        "pillar_year_stem", "pillar_month_branch",
        "yijing_gua", "ziwei_star_position",
    ])


def heavenly_stem_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating heavenly stems (天干)."""
    return st.sampled_from(["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"])


def earthly_branch_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating earthly branches (地支)."""
    return st.sampled_from([
        "子", "丑", "寅", "卯", "辰", "巳", 
        "午", "未", "申", "酉", "戌", "亥"
    ])


def season_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating seasons."""
    return st.sampled_from(["spring", "summer", "autumn", "winter"])


def factor_value_simple_strategy() -> st.SearchStrategy[Any]:
    """Strategy for generating simple factor values."""
    return st.one_of(
        heavenly_stem_strategy(),
        earthly_branch_strategy(),
        season_strategy(),
        st.booleans(),
        st.integers(min_value=0, max_value=10),
    )


def trigger_condition_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating trigger condition strings."""
    # Simple equality conditions
    simple_conditions = st.builds(
        lambda fid, val: f"{fid}={val}",
        factor_id_strategy(),
        factor_value_simple_strategy(),
    )
    
    # Set membership conditions
    set_conditions = st.builds(
        lambda fid, vals: f"{fid}∈[{','.join(str(v) for v in vals)}]",
        factor_id_strategy(),
        st.lists(factor_value_simple_strategy(), min_size=2, max_size=4, unique=True),
    )
    
    return st.one_of(simple_conditions, set_conditions)


def create_factor_matrix(
    factors_dict: Dict[str, Any],
    engine_id: str = "test_engine"
) -> FactorMatrix:
    """Helper to create a FactorMatrix from a simple dict."""
    factors = {
        fid: FactorValue(
            factor_id=fid,
            value=val,
            confidence=1.0,
            source="calculator"
        )
        for fid, val in factors_dict.items()
    }
    return FactorMatrix(
        factors=factors,
        timestamp=datetime.now(),
        engine_id=engine_id,
    )


def factor_matrix_from_condition(
    condition: str,
    should_match: bool = True
) -> FactorMatrix:
    """Create a FactorMatrix that matches or doesn't match a condition."""
    parsed = parse_trigger_condition(condition)
    factors_dict = {}
    
    for factor_id, expected in parsed.factor_conditions.items():
        if should_match:
            # Use the expected value (or first value if it's a set)
            if isinstance(expected, set):
                factors_dict[factor_id] = list(expected)[0]
            else:
                factors_dict[factor_id] = expected
        else:
            # Use a different value
            if isinstance(expected, set):
                # Use a value not in the set
                all_values = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
                for v in all_values:
                    if v not in expected:
                        factors_dict[factor_id] = v
                        break
            elif isinstance(expected, str):
                # Use a different string
                factors_dict[factor_id] = expected + "_different"
            elif isinstance(expected, bool):
                factors_dict[factor_id] = not expected
            elif isinstance(expected, int):
                factors_dict[factor_id] = expected + 100
            else:
                factors_dict[factor_id] = "different_value"
    
    return create_factor_matrix(factors_dict)


# =============================================================================
# Property Tests
# =============================================================================

@property_test(
    property_id="13",
    property_name="因子匹配精确性",
    validates=["12.1", "12.2"],
    max_examples=100,
)
@given(condition=trigger_condition_strategy())
def test_exact_match_returns_only_matching_snippets(condition: str):
    """
    **Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
    **Validates: Requirements 12.1, 12.2**
    
    Property: For any factor_matrix and trigger_condition, the system should
    only return snippets whose trigger_condition is exactly satisfied.
    No "similar" but non-matching snippets should be returned.
    """
    # Create a matching factor matrix
    matching_matrix = factor_matrix_from_condition(condition, should_match=True)
    
    # Create a non-matching factor matrix
    non_matching_matrix = factor_matrix_from_condition(condition, should_match=False)
    
    # Create snippet index with test snippets
    index = ExactMatchSnippetIndex()
    
    # Add a snippet with the test condition
    test_snippet = {
        "snippet_id": "test_001",
        "trigger_condition": condition,
        "content": "Test content",
    }
    index.add_snippet("test_001", condition, test_snippet)
    
    # Query with matching matrix - should return the snippet
    matching_results = index.query_exact(matching_matrix)
    assert len(matching_results) >= 1, (
        f"Expected at least 1 match for condition '{condition}' "
        f"with matching matrix, got {len(matching_results)}"
    )
    
    # Query with non-matching matrix - should NOT return the snippet
    non_matching_results = index.query_exact(non_matching_matrix)
    matching_snippet_ids = {
        s.get("snippet_id") if isinstance(s, dict) else getattr(s, "snippet_id", None)
        for s in non_matching_results
    }
    assert "test_001" not in matching_snippet_ids, (
        f"Snippet 'test_001' should NOT match condition '{condition}' "
        f"with non-matching matrix. This indicates fuzzy matching is occurring."
    )


@property_test(
    property_id="13.1",
    property_name="因子匹配精确性 - 相等条件",
    validates=["12.1", "12.2"],
    max_examples=100,
)
@given(
    factor_id=factor_id_strategy(),
    value=factor_value_simple_strategy(),
)
def test_equality_condition_exact_match(factor_id: str, value: Any):
    """
    **Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
    **Validates: Requirements 12.1, 12.2**
    
    Property: For equality conditions (factor_id=value), only exact value
    matches should be accepted. Similar values should be rejected.
    """
    condition = f"{factor_id}={value}"
    
    # Create matching matrix
    matching_matrix = create_factor_matrix({factor_id: value})
    
    # Validate exact match
    result = validate_exact_match(condition, matching_matrix)
    assert result.matched, (
        f"Exact match should succeed for condition '{condition}' "
        f"with value '{value}'"
    )
    
    # Create non-matching matrix with different value
    if isinstance(value, str):
        different_value = value + "_different"
    elif isinstance(value, bool):
        different_value = not value
    elif isinstance(value, int):
        different_value = value + 1
    else:
        different_value = "different"
    
    non_matching_matrix = create_factor_matrix({factor_id: different_value})
    
    # Validate non-match
    result = validate_exact_match(condition, non_matching_matrix)
    assert not result.matched, (
        f"Exact match should fail for condition '{condition}' "
        f"with different value '{different_value}'"
    )


@property_test(
    property_id="13.2",
    property_name="因子匹配精确性 - 集合成员条件",
    validates=["12.1", "12.2"],
    max_examples=100,
)
@given(
    factor_id=factor_id_strategy(),
    values=st.lists(heavenly_stem_strategy(), min_size=2, max_size=4, unique=True),
)
def test_set_membership_exact_match(factor_id: str, values: List[str]):
    """
    **Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
    **Validates: Requirements 12.1, 12.2**
    
    Property: For set membership conditions (factor_id∈[v1,v2,...]),
    only values in the set should match. Values outside the set should
    be rejected, even if they are "similar".
    """
    condition = f"{factor_id}∈[{','.join(values)}]"
    
    # Test each value in the set - should match
    for value in values:
        matching_matrix = create_factor_matrix({factor_id: value})
        result = validate_exact_match(condition, matching_matrix)
        assert result.matched, (
            f"Value '{value}' should match set condition '{condition}'"
        )
    
    # Test a value NOT in the set - should NOT match
    all_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    non_member = None
    for stem in all_stems:
        if stem not in values:
            non_member = stem
            break
    
    if non_member:
        non_matching_matrix = create_factor_matrix({factor_id: non_member})
        result = validate_exact_match(condition, non_matching_matrix)
        assert not result.matched, (
            f"Value '{non_member}' should NOT match set condition '{condition}'"
        )


@property_test(
    property_id="13.3",
    property_name="因子匹配精确性 - 缺失因子",
    validates=["12.1", "12.2"],
    max_examples=100,
)
@given(condition=trigger_condition_strategy())
def test_missing_factor_does_not_match(condition: str):
    """
    **Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
    **Validates: Requirements 12.1, 12.2**
    
    Property: If a required factor is missing from the factor matrix,
    the condition should NOT match. No default values or fuzzy matching
    should be applied.
    """
    # Create an empty factor matrix
    empty_matrix = create_factor_matrix({})
    
    # Validate that empty matrix does not match any condition
    result = validate_exact_match(condition, empty_matrix)
    assert not result.matched, (
        f"Empty factor matrix should NOT match condition '{condition}'"
    )
    assert len(result.missing_factors) > 0, (
        f"Missing factors should be reported for condition '{condition}'"
    )


@property_test(
    property_id="13.4",
    property_name="因子匹配精确性 - AND条件",
    validates=["12.1", "12.2"],
    max_examples=100,
)
@given(
    factor_id1=factor_id_strategy(),
    value1=heavenly_stem_strategy(),
    factor_id2=st.sampled_from(["season", "element_score"]),
    value2=st.one_of(season_strategy(), st.integers(min_value=0, max_value=10)),
)
def test_and_condition_requires_all_factors(
    factor_id1: str, value1: str, factor_id2: str, value2: Any
):
    """
    **Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
    **Validates: Requirements 12.1, 12.2**
    
    Property: For AND conditions, ALL factors must match exactly.
    Partial matches should be rejected.
    """
    # Skip if factor IDs are the same
    assume(factor_id1 != factor_id2)
    
    condition = f"{factor_id1}={value1} AND {factor_id2}={value2}"
    
    # Full match - should succeed
    full_matrix = create_factor_matrix({factor_id1: value1, factor_id2: value2})
    result = validate_exact_match(condition, full_matrix)
    assert result.matched, (
        f"Full match should succeed for AND condition '{condition}'"
    )
    
    # Partial match (only first factor) - should fail
    partial_matrix1 = create_factor_matrix({factor_id1: value1})
    result = validate_exact_match(condition, partial_matrix1)
    assert not result.matched, (
        f"Partial match (only {factor_id1}) should fail for AND condition '{condition}'"
    )
    
    # Partial match (only second factor) - should fail
    partial_matrix2 = create_factor_matrix({factor_id2: value2})
    result = validate_exact_match(condition, partial_matrix2)
    assert not result.matched, (
        f"Partial match (only {factor_id2}) should fail for AND condition '{condition}'"
    )


@property_test(
    property_id="13.5",
    property_name="因子匹配精确性 - 无模糊匹配",
    validates=["12.1", "12.2"],
    max_examples=100,
)
@given(
    factor_id=factor_id_strategy(),
    value=heavenly_stem_strategy(),
)
def test_no_fuzzy_matching_for_similar_values(factor_id: str, value: str):
    """
    **Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
    **Validates: Requirements 12.1, 12.2**
    
    Property: Similar but not identical values should NOT match.
    For example, "甲" should NOT match "甲木" or "jia".
    """
    condition = f"{factor_id}={value}"
    
    # Test with exact value - should match
    exact_matrix = create_factor_matrix({factor_id: value})
    result = validate_exact_match(condition, exact_matrix)
    assert result.matched, f"Exact value '{value}' should match"
    
    # Test with similar but different values - should NOT match
    similar_values = [
        value + "木",  # Appended character
        value.lower() if value.isupper() else value.upper(),  # Case change (if applicable)
        f"_{value}_",  # Wrapped with underscores
        value + " ",  # Trailing space
        " " + value,  # Leading space
    ]
    
    for similar in similar_values:
        if similar != value:  # Only test if actually different
            similar_matrix = create_factor_matrix({factor_id: similar})
            result = validate_exact_match(condition, similar_matrix)
            assert not result.matched, (
                f"Similar value '{similar}' should NOT match exact condition "
                f"'{condition}' (expected '{value}')"
            )


# =============================================================================
# Unit Tests for Edge Cases
# =============================================================================

class TestTriggerConditionParsing:
    """Unit tests for trigger condition parsing."""
    
    def test_parse_simple_equality(self):
        """Test parsing simple equality condition."""
        condition = "day_master=甲"
        parsed = parse_trigger_condition(condition)
        
        assert parsed.factor_conditions == {"day_master": "甲"}
        assert parsed.operator == "AND"
    
    def test_parse_set_membership(self):
        """Test parsing set membership condition."""
        condition = "month∈[寅,卯]"
        parsed = parse_trigger_condition(condition)
        
        assert "month" in parsed.factor_conditions
        assert parsed.factor_conditions["month"] == {"寅", "卯"}
    
    def test_parse_and_condition(self):
        """Test parsing AND condition."""
        condition = "day_master=甲 AND month∈[寅,卯]"
        parsed = parse_trigger_condition(condition)
        
        assert parsed.operator == "AND"
        assert "day_master" in parsed.factor_conditions
        assert "month" in parsed.factor_conditions
    
    def test_parse_boolean_value(self):
        """Test parsing boolean values."""
        condition = "is_strong=true"
        parsed = parse_trigger_condition(condition)
        
        assert parsed.factor_conditions["is_strong"] is True
    
    def test_parse_integer_value(self):
        """Test parsing integer values."""
        condition = "element_score=5"
        parsed = parse_trigger_condition(condition)
        
        assert parsed.factor_conditions["element_score"] == 5


class TestExactMatchSnippetIndex:
    """Unit tests for ExactMatchSnippetIndex."""
    
    def test_add_and_query_snippet(self):
        """Test adding and querying a snippet."""
        index = ExactMatchSnippetIndex()
        
        snippet = {
            "snippet_id": "test_001",
            "trigger_condition": "day_master=甲",
            "content": "Test content",
        }
        index.add_snippet("test_001", "day_master=甲", snippet)
        
        # Query with matching matrix
        matrix = create_factor_matrix({"day_master": "甲"})
        results = index.query_exact(matrix)
        
        assert len(results) == 1
        assert results[0]["snippet_id"] == "test_001"
    
    def test_query_returns_empty_for_non_match(self):
        """Test that query returns empty for non-matching matrix."""
        index = ExactMatchSnippetIndex()
        
        snippet = {
            "snippet_id": "test_001",
            "trigger_condition": "day_master=甲",
            "content": "Test content",
        }
        index.add_snippet("test_001", "day_master=甲", snippet)
        
        # Query with non-matching matrix
        matrix = create_factor_matrix({"day_master": "乙"})
        results = index.query_exact(matrix)
        
        assert len(results) == 0
    
    def test_multiple_snippets_same_condition(self):
        """Test multiple snippets with same condition."""
        index = ExactMatchSnippetIndex()
        
        for i in range(3):
            snippet = {
                "snippet_id": f"test_{i:03d}",
                "trigger_condition": "day_master=甲",
                "content": f"Content {i}",
            }
            index.add_snippet(f"test_{i:03d}", "day_master=甲", snippet)
        
        matrix = create_factor_matrix({"day_master": "甲"})
        results = index.query_exact(matrix)
        
        assert len(results) == 3
    
    def test_no_cross_contamination(self):
        """Test that different conditions don't cross-match."""
        index = ExactMatchSnippetIndex()
        
        # Add snippets with different conditions
        index.add_snippet("jia_001", "day_master=甲", {"snippet_id": "jia_001", "trigger_condition": "day_master=甲"})
        index.add_snippet("yi_001", "day_master=乙", {"snippet_id": "yi_001", "trigger_condition": "day_master=乙"})
        
        # Query for 甲 - should only get jia_001
        matrix_jia = create_factor_matrix({"day_master": "甲"})
        results_jia = index.query_exact(matrix_jia)
        
        assert len(results_jia) == 1
        assert results_jia[0]["snippet_id"] == "jia_001"
        
        # Query for 乙 - should only get yi_001
        matrix_yi = create_factor_matrix({"day_master": "乙"})
        results_yi = index.query_exact(matrix_yi)
        
        assert len(results_yi) == 1
        assert results_yi[0]["snippet_id"] == "yi_001"
