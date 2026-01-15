# backend/core/testing/__init__.py
"""
Testing utilities for Calculator accuracy audit.

This package provides:
- Golden Set testing framework
- Property-based testing utilities
- Cross-source validation framework
"""

from backend.core.testing.golden_set import (
    GoldenSetCase,
    GoldenSetRegistry,
    GoldenSetLoader,
    GoldenSetRunner,
    golden_set_test,
)

from backend.core.testing.property_tests import (
    PropertyTestResult,
    PropertyTestRegistry,
    property_test,
    datetime_strategy,
    location_strategy,
    gender_strategy,
    heavenly_stem_strategy,
    earthly_branch_strategy,
    hexagram_lines_strategy,
    tarot_card_strategy,
    zodiac_sign_strategy,
    planet_strategy,
    assert_within_tolerance,
    assert_exact_match,
    assert_probability_distribution,
)

from backend.core.testing.cross_validation import (
    ValidationStatus,
    CrossValidationConfig,
    Discrepancy,
    CrossValidationResult,
    CrossValidator,
    BAZI_VALIDATION_CONFIG,
    ZIWEI_VALIDATION_CONFIG,
    ASTRO_VALIDATION_CONFIG,
    YIJING_VALIDATION_CONFIG,
    TAROT_VALIDATION_CONFIG,
    DREAM_VALIDATION_CONFIG,
)

from backend.core.testing.output_validation import (
    SEMANTIC_FIELD_NAMES,
    SEMANTIC_FIELD_PATTERNS,
    OutputValidationResult,
    is_semantic_field_name,
    check_value_for_semantic_content,
    validate_factor_value_no_semantics,
    validate_factor_matrix_no_semantics,
    validate_calculator_output,
    assert_no_semantic_fields,
    assert_factor_matrix_structural_only,
)

from backend.core.testing.factor_matching import (
    TriggerCondition,
    MatchResult,
    MatchingValidationResult,
    parse_trigger_condition,
    validate_exact_match,
    check_no_fuzzy_matching,
    ExactMatchSnippetIndex,
    assert_exact_match_only,
    assert_no_similar_matches,
)

__all__ = [
    # Golden Set
    "GoldenSetCase",
    "GoldenSetRegistry",
    "GoldenSetLoader",
    "GoldenSetRunner",
    "golden_set_test",
    # Property Tests
    "PropertyTestResult",
    "PropertyTestRegistry",
    "property_test",
    "datetime_strategy",
    "location_strategy",
    "gender_strategy",
    "heavenly_stem_strategy",
    "earthly_branch_strategy",
    "hexagram_lines_strategy",
    "tarot_card_strategy",
    "zodiac_sign_strategy",
    "planet_strategy",
    "assert_within_tolerance",
    "assert_exact_match",
    "assert_probability_distribution",
    # Cross Validation
    "ValidationStatus",
    "CrossValidationConfig",
    "Discrepancy",
    "CrossValidationResult",
    "CrossValidator",
    "BAZI_VALIDATION_CONFIG",
    "ZIWEI_VALIDATION_CONFIG",
    "ASTRO_VALIDATION_CONFIG",
    "YIJING_VALIDATION_CONFIG",
    "TAROT_VALIDATION_CONFIG",
    "DREAM_VALIDATION_CONFIG",
    # Output Validation
    "SEMANTIC_FIELD_NAMES",
    "SEMANTIC_FIELD_PATTERNS",
    "OutputValidationResult",
    "is_semantic_field_name",
    "check_value_for_semantic_content",
    "validate_factor_value_no_semantics",
    "validate_factor_matrix_no_semantics",
    "validate_calculator_output",
    "assert_no_semantic_fields",
    "assert_factor_matrix_structural_only",
    # Factor Matching
    "TriggerCondition",
    "MatchResult",
    "MatchingValidationResult",
    "parse_trigger_condition",
    "validate_exact_match",
    "check_no_fuzzy_matching",
    "ExactMatchSnippetIndex",
    "assert_exact_match_only",
    "assert_no_similar_matches",
]
