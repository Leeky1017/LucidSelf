# backend/core/testing/property_tests.py
"""
Property-based testing utilities for Calculator accuracy audit.

Uses Hypothesis library for property-based testing.
Each property test validates a correctness property from the design document.
"""

from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Type
from datetime import datetime
import json

from hypothesis import given, settings, Verbosity, Phase
from hypothesis import strategies as st
from pydantic import BaseModel


# Default settings for property tests
DEFAULT_MAX_EXAMPLES = 100
DEFAULT_DEADLINE = None  # No deadline for complex calculations


class PropertyTestResult(BaseModel):
    """Result of a property test run."""
    
    property_id: str
    property_name: str
    validates_requirements: List[str]
    passed: bool
    examples_run: int
    failing_example: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    execution_time_ms: float = 0.0


class PropertyTestRegistry:
    """Registry for property tests."""
    
    _tests: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def register(
        cls,
        property_id: str,
        property_name: str,
        validates: List[str],
        feature: str = "calculator-accuracy-audit",
    ):
        """
        Decorator to register a property test.
        
        Args:
            property_id: Property identifier (e.g., "2" for Property 2)
            property_name: Human-readable property name
            validates: List of requirement IDs this property validates
            feature: Feature name for the spec
            
        Usage:
            @PropertyTestRegistry.register(
                property_id="2",
                property_name="节气计算精度",
                validates=["2.1"],
            )
            @given(year=st.integers(min_value=1900, max_value=2100))
            def test_solar_term_accuracy(year):
                ...
        """
        def decorator(func):
            cls._tests[property_id] = {
                "property_id": property_id,
                "property_name": property_name,
                "validates": validates,
                "feature": feature,
                "func": func,
            }
            
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            # Add metadata to function for pytest discovery
            wrapper._property_id = property_id
            wrapper._property_name = property_name
            wrapper._validates = validates
            wrapper._feature = feature
            
            return wrapper
        
        return decorator
    
    @classmethod
    def get_all_tests(cls) -> Dict[str, Dict[str, Any]]:
        """Get all registered property tests."""
        return cls._tests.copy()
    
    @classmethod
    def get_tests_for_requirement(cls, requirement_id: str) -> List[Dict[str, Any]]:
        """Get all property tests that validate a specific requirement."""
        return [
            test for test in cls._tests.values()
            if requirement_id in test["validates"]
        ]


def property_test(
    property_id: str,
    property_name: str,
    validates: List[str],
    max_examples: int = DEFAULT_MAX_EXAMPLES,
    feature: str = "calculator-accuracy-audit",
):
    """
    Combined decorator for property tests.
    
    Applies both Hypothesis settings and property registration.
    
    Usage:
        @property_test(
            property_id="2",
            property_name="节气计算精度",
            validates=["2.1"],
        )
        @given(year=st.integers(min_value=1900, max_value=2100))
        def test_solar_term_accuracy(year):
            ...
    """
    def decorator(func):
        # Apply Hypothesis settings
        configured_func = settings(
            max_examples=max_examples,
            deadline=DEFAULT_DEADLINE,
            verbosity=Verbosity.normal,
            phases=[Phase.generate, Phase.target, Phase.shrink],
        )(func)
        
        # Register the property test
        registered_func = PropertyTestRegistry.register(
            property_id=property_id,
            property_name=property_name,
            validates=validates,
            feature=feature,
        )(configured_func)
        
        return registered_func
    
    return decorator


# Common strategies for Calculator testing

def datetime_strategy(
    min_year: int = 1900,
    max_year: int = 2100,
) -> st.SearchStrategy[datetime]:
    """Strategy for generating valid datetime values."""
    return st.datetimes(
        min_value=datetime(min_year, 1, 1),
        max_value=datetime(max_year, 12, 31, 23, 59, 59),
    )


def location_strategy() -> st.SearchStrategy[tuple]:
    """Strategy for generating valid (longitude, latitude) pairs."""
    return st.tuples(
        st.floats(min_value=-180.0, max_value=180.0),
        st.floats(min_value=-90.0, max_value=90.0),
    )


def gender_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating gender values."""
    return st.sampled_from(["male", "female"])


def heavenly_stem_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating heavenly stems (天干)."""
    return st.sampled_from(["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"])


def earthly_branch_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating earthly branches (地支)."""
    return st.sampled_from([
        "子", "丑", "寅", "卯", "辰", "巳", 
        "午", "未", "申", "酉", "戌", "亥"
    ])


def hexagram_lines_strategy() -> st.SearchStrategy[List[int]]:
    """Strategy for generating hexagram lines (6=老阴, 7=少阳, 8=少阴, 9=老阳)."""
    return st.lists(
        st.sampled_from([6, 7, 8, 9]),
        min_size=6,
        max_size=6,
    )


def tarot_card_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating tarot card IDs."""
    major_arcana = [f"major_{i:02d}" for i in range(22)]
    minor_suits = ["wands", "cups", "swords", "pentacles"]
    minor_ranks = ["ace"] + [str(i) for i in range(2, 11)] + ["page", "knight", "queen", "king"]
    minor_arcana = [f"minor_{suit}_{rank}" for suit in minor_suits for rank in minor_ranks]
    return st.sampled_from(major_arcana + minor_arcana)


def zodiac_sign_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating zodiac signs."""
    return st.sampled_from([
        "aries", "taurus", "gemini", "cancer", 
        "leo", "virgo", "libra", "scorpio",
        "sagittarius", "capricorn", "aquarius", "pisces"
    ])


def planet_strategy() -> st.SearchStrategy[str]:
    """Strategy for generating planet names."""
    return st.sampled_from([
        "sun", "moon", "mercury", "venus", "mars",
        "jupiter", "saturn", "uranus", "neptune", "pluto"
    ])


# Assertion helpers

def assert_within_tolerance(
    actual: float,
    expected: float,
    tolerance: float,
    message: str = "",
) -> None:
    """Assert that actual value is within tolerance of expected."""
    diff = abs(actual - expected)
    assert diff <= tolerance, (
        f"{message}: Expected {expected} ± {tolerance}, got {actual} (diff: {diff})"
    )


def assert_exact_match(
    actual: Any,
    expected: Any,
    message: str = "",
) -> None:
    """Assert exact match between actual and expected."""
    assert actual == expected, f"{message}: Expected {expected}, got {actual}"


def assert_probability_distribution(
    counts: Dict[str, int],
    expected_probs: Dict[str, float],
    tolerance: float = 0.05,
    message: str = "",
) -> None:
    """
    Assert that observed counts match expected probability distribution.
    
    Args:
        counts: Observed counts for each category
        expected_probs: Expected probability for each category
        tolerance: Allowed deviation from expected probability
        message: Error message prefix
    """
    total = sum(counts.values())
    for category, expected_prob in expected_probs.items():
        actual_prob = counts.get(category, 0) / total
        assert abs(actual_prob - expected_prob) <= tolerance, (
            f"{message}: Category '{category}' expected prob {expected_prob:.3f}, "
            f"got {actual_prob:.3f} (diff: {abs(actual_prob - expected_prob):.3f})"
        )
