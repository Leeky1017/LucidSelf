# backend/core/testing/factor_matching.py
"""
Factor matching precision validation utilities.

Validates that factor matching follows the exact match principle:
- Only exact matches are allowed
- No fuzzy matching or similarity matching
- Trigger conditions must be precisely satisfied

**Feature: calculator-accuracy-audit, Property 13: 因子匹配精确性**
**Validates: Requirements 12.1, 12.2**
"""

import re
from typing import Any, Dict, List, Optional, Set, Tuple
from pydantic import BaseModel

from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Trigger Condition Parsing
# =============================================================================

class TriggerCondition(BaseModel):
    """Parsed trigger condition."""
    
    raw_condition: str
    factor_conditions: Dict[str, Any]  # factor_id -> expected value or set of values
    operator: str = "AND"  # AND or OR
    
    def matches(self, factor_matrix: FactorMatrix) -> bool:
        """
        Check if the factor matrix satisfies this trigger condition.
        
        Uses EXACT matching only - no fuzzy or similarity matching.
        """
        if self.operator == "AND":
            return all(
                self._check_single_condition(factor_id, expected, factor_matrix)
                for factor_id, expected in self.factor_conditions.items()
            )
        else:  # OR
            return any(
                self._check_single_condition(factor_id, expected, factor_matrix)
                for factor_id, expected in self.factor_conditions.items()
            )
    
    def _check_single_condition(
        self, 
        factor_id: str, 
        expected: Any, 
        factor_matrix: FactorMatrix
    ) -> bool:
        """Check a single factor condition with EXACT matching."""
        factor = factor_matrix.get(factor_id)
        
        if factor is None:
            return False
        
        actual_value = factor.value
        
        # Handle set membership (e.g., month∈[寅,卯])
        if isinstance(expected, (set, list)):
            return actual_value in expected
        
        # Exact match only
        return actual_value == expected


def parse_trigger_condition(condition_str: str) -> TriggerCondition:
    """
    Parse a trigger condition string into a TriggerCondition object.
    
    Supported formats:
    - "factor_id=value"
    - "factor_id=value AND factor_id2=value2"
    - "factor_id∈[value1,value2]"
    
    Args:
        condition_str: The trigger condition string
        
    Returns:
        TriggerCondition object
    """
    factor_conditions = {}
    operator = "AND"
    
    # Detect operator
    if " OR " in condition_str:
        operator = "OR"
        parts = condition_str.split(" OR ")
    elif " AND " in condition_str:
        operator = "AND"
        parts = condition_str.split(" AND ")
    else:
        parts = [condition_str]
    
    for part in parts:
        part = part.strip()
        
        # Handle set membership: factor_id∈[value1,value2]
        if "∈" in part:
            match = re.match(r"(\w+)∈\[([^\]]+)\]", part)
            if match:
                factor_id = match.group(1)
                values_str = match.group(2)
                values = {v.strip() for v in values_str.split(",")}
                factor_conditions[factor_id] = values
        
        # Handle equality: factor_id=value
        elif "=" in part:
            factor_id, value = part.split("=", 1)
            factor_id = factor_id.strip()
            value = value.strip()
            
            # Try to convert to appropriate type
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif value.isdigit():
                value = int(value)
            
            factor_conditions[factor_id] = value
    
    return TriggerCondition(
        raw_condition=condition_str,
        factor_conditions=factor_conditions,
        operator=operator,
    )


# =============================================================================
# Exact Match Validation
# =============================================================================

class MatchResult(BaseModel):
    """Result of a matching operation."""
    
    matched: bool
    trigger_condition: str
    matched_factors: List[str]
    missing_factors: List[str]
    mismatched_factors: Dict[str, Dict[str, Any]]  # factor_id -> {expected, actual}


class MatchingValidationResult(BaseModel):
    """Result of matching validation."""
    
    is_exact_match: bool
    fuzzy_matches_detected: List[str]
    similarity_matches_detected: List[str]
    warnings: List[str]


def validate_exact_match(
    trigger_condition: str,
    factor_matrix: FactorMatrix,
) -> MatchResult:
    """
    Validate that a trigger condition matches a factor matrix using EXACT matching.
    
    Args:
        trigger_condition: The trigger condition string
        factor_matrix: The factor matrix to match against
        
    Returns:
        MatchResult with detailed matching information
    """
    parsed = parse_trigger_condition(trigger_condition)
    
    matched_factors = []
    missing_factors = []
    mismatched_factors = {}
    
    for factor_id, expected in parsed.factor_conditions.items():
        factor = factor_matrix.get(factor_id)
        
        if factor is None:
            missing_factors.append(factor_id)
            continue
        
        actual = factor.value
        
        # Check exact match
        if isinstance(expected, (set, list)):
            if actual in expected:
                matched_factors.append(factor_id)
            else:
                mismatched_factors[factor_id] = {
                    "expected": list(expected) if isinstance(expected, set) else expected,
                    "actual": actual,
                }
        else:
            if actual == expected:
                matched_factors.append(factor_id)
            else:
                mismatched_factors[factor_id] = {
                    "expected": expected,
                    "actual": actual,
                }
    
    # Determine overall match
    if parsed.operator == "AND":
        matched = len(missing_factors) == 0 and len(mismatched_factors) == 0
    else:  # OR
        matched = len(matched_factors) > 0
    
    return MatchResult(
        matched=matched,
        trigger_condition=trigger_condition,
        matched_factors=matched_factors,
        missing_factors=missing_factors,
        mismatched_factors=mismatched_factors,
    )


def check_no_fuzzy_matching(
    trigger_condition: str,
    factor_matrix: FactorMatrix,
    candidate_snippets: List[Any],
    get_snippet_condition: callable,
) -> MatchingValidationResult:
    """
    Validate that no fuzzy or similarity matching is used.
    
    This function checks that:
    1. Only exact matches are returned
    2. No "similar" but non-matching snippets are included
    
    Args:
        trigger_condition: The trigger condition to match
        factor_matrix: The factor matrix
        candidate_snippets: List of candidate snippets
        get_snippet_condition: Function to extract trigger_condition from snippet
        
    Returns:
        MatchingValidationResult
    """
    fuzzy_matches = []
    similarity_matches = []
    warnings = []
    
    parsed_target = parse_trigger_condition(trigger_condition)
    
    for snippet in candidate_snippets:
        snippet_condition = get_snippet_condition(snippet)
        parsed_snippet = parse_trigger_condition(snippet_condition)
        
        # Check if this snippet should match
        should_match = parsed_snippet.matches(factor_matrix)
        
        # Check for fuzzy matching (partial factor matches)
        if not should_match:
            # Check if any factors partially match
            for factor_id, expected in parsed_snippet.factor_conditions.items():
                factor = factor_matrix.get(factor_id)
                if factor is not None:
                    actual = factor.value
                    
                    # Check for string similarity (fuzzy match indicator)
                    if isinstance(actual, str) and isinstance(expected, str):
                        if actual != expected and (
                            actual.lower() == expected.lower() or
                            actual in expected or
                            expected in actual
                        ):
                            fuzzy_matches.append(
                                f"Fuzzy match detected: {factor_id}={actual} vs {expected}"
                            )
    
    return MatchingValidationResult(
        is_exact_match=len(fuzzy_matches) == 0 and len(similarity_matches) == 0,
        fuzzy_matches_detected=fuzzy_matches,
        similarity_matches_detected=similarity_matches,
        warnings=warnings,
    )


# =============================================================================
# Snippet Index for Exact Matching
# =============================================================================

class ExactMatchSnippetIndex:
    """
    Index for exact matching of narrative snippets.
    
    Implements O(1) or O(log n) exact matching using inverted index.
    NO fuzzy matching or similarity matching is supported.
    """
    
    def __init__(self):
        # Inverted index: factor_id -> set of snippet_ids
        self._index_by_factor: Dict[str, Set[str]] = {}
        # Combination hash index: hash(factors) -> list of snippet_ids
        self._index_by_combination: Dict[str, List[str]] = {}
        # Snippet storage
        self._snippets: Dict[str, Any] = {}
    
    def add_snippet(self, snippet_id: str, trigger_condition: str, snippet: Any) -> None:
        """Add a snippet to the index."""
        self._snippets[snippet_id] = snippet
        
        parsed = parse_trigger_condition(trigger_condition)
        
        # Add to factor index
        for factor_id in parsed.factor_conditions.keys():
            if factor_id not in self._index_by_factor:
                self._index_by_factor[factor_id] = set()
            self._index_by_factor[factor_id].add(snippet_id)
        
        # Add to combination index
        combination_key = self._hash_condition(parsed)
        if combination_key not in self._index_by_combination:
            self._index_by_combination[combination_key] = []
        self._index_by_combination[combination_key].append(snippet_id)
    
    def query_exact(self, factor_matrix: FactorMatrix) -> List[Any]:
        """
        Query snippets using EXACT matching only.
        
        Returns only snippets whose trigger_condition is exactly satisfied.
        NO fuzzy matching or similarity matching.
        """
        results = []
        
        # Get all potentially matching snippets
        candidate_ids = self._get_candidates(factor_matrix)
        
        for snippet_id in candidate_ids:
            snippet = self._snippets.get(snippet_id)
            if snippet is None:
                continue
            
            # Get trigger condition (assuming snippet has this attribute)
            if hasattr(snippet, "trigger_condition"):
                condition = snippet.trigger_condition
            elif isinstance(snippet, dict):
                condition = snippet.get("trigger_condition", "")
            else:
                continue
            
            # Verify exact match
            parsed = parse_trigger_condition(condition)
            if parsed.matches(factor_matrix):
                results.append(snippet)
        
        return results
    
    def _get_candidates(self, factor_matrix: FactorMatrix) -> Set[str]:
        """Get candidate snippet IDs based on factor presence."""
        candidates = set()
        
        for factor_id in factor_matrix.factors.keys():
            if factor_id in self._index_by_factor:
                candidates.update(self._index_by_factor[factor_id])
        
        return candidates
    
    def _hash_condition(self, parsed: TriggerCondition) -> str:
        """Create a hash key for a parsed condition."""
        # Sort factor IDs for consistent hashing
        sorted_factors = sorted(parsed.factor_conditions.keys())
        return "|".join(sorted_factors)


# =============================================================================
# Assertion Helpers
# =============================================================================

def assert_exact_match_only(
    trigger_condition: str,
    factor_matrix: FactorMatrix,
    message: str = "",
) -> None:
    """
    Assert that matching uses exact match only.
    
    Args:
        trigger_condition: The trigger condition
        factor_matrix: The factor matrix
        message: Optional error message prefix
        
    Raises:
        AssertionError: If exact match fails
    """
    result = validate_exact_match(trigger_condition, factor_matrix)
    
    if not result.matched:
        error_msg = f"{message}: " if message else ""
        error_msg += (
            f"Exact match failed for condition '{trigger_condition}'. "
            f"Missing factors: {result.missing_factors}. "
            f"Mismatched factors: {result.mismatched_factors}"
        )
        raise AssertionError(error_msg)


def assert_no_similar_matches(
    expected_matches: List[str],
    actual_matches: List[str],
    message: str = "",
) -> None:
    """
    Assert that only expected matches are returned (no similar/fuzzy matches).
    
    Args:
        expected_matches: List of expected snippet IDs
        actual_matches: List of actually matched snippet IDs
        message: Optional error message prefix
        
    Raises:
        AssertionError: If unexpected matches are found
    """
    expected_set = set(expected_matches)
    actual_set = set(actual_matches)
    
    unexpected = actual_set - expected_set
    
    if unexpected:
        error_msg = f"{message}: " if message else ""
        error_msg += (
            f"Unexpected matches found (possible fuzzy/similarity matching): "
            f"{unexpected}"
        )
        raise AssertionError(error_msg)
