# backend/core/testing/serialization.py
"""
FactorMatrix serialization round-trip validation utilities.

Validates that all FactorMatrix instances can be serialized and deserialized
without data loss, ensuring data integrity across the system.

**Feature: calculator-accuracy-audit, Property 14: FactorMatrix 序列化往返一致性**
**Validates: Requirements 13.1-13.6**
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Type
import json

from pydantic import BaseModel

from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Serialization Validation Result
# =============================================================================

class SerializationValidationResult(BaseModel):
    """Result of serialization round-trip validation."""
    
    is_valid: bool
    original_factor_count: int
    restored_factor_count: int
    mismatched_factors: List[str]
    missing_factors: List[str]
    extra_factors: List[str]
    value_mismatches: List[Dict[str, Any]]
    warnings: List[str]
    
    def __bool__(self) -> bool:
        return self.is_valid


# =============================================================================
# Serialization Utilities
# =============================================================================

def serialize_factor_matrix(matrix: FactorMatrix) -> str:
    """
    Serialize a FactorMatrix to JSON string.
    
    Args:
        matrix: The FactorMatrix to serialize
        
    Returns:
        JSON string representation
    """
    return matrix.model_dump_json()


def deserialize_factor_matrix(json_str: str) -> FactorMatrix:
    """
    Deserialize a JSON string to FactorMatrix.
    
    Args:
        json_str: JSON string representation
        
    Returns:
        Restored FactorMatrix instance
    """
    return FactorMatrix.model_validate_json(json_str)


def serialize_factor_matrix_to_dict(matrix: FactorMatrix) -> Dict[str, Any]:
    """
    Serialize a FactorMatrix to dictionary.
    
    Args:
        matrix: The FactorMatrix to serialize
        
    Returns:
        Dictionary representation
    """
    return matrix.model_dump()


def deserialize_factor_matrix_from_dict(data: Dict[str, Any]) -> FactorMatrix:
    """
    Deserialize a dictionary to FactorMatrix.
    
    Args:
        data: Dictionary representation
        
    Returns:
        Restored FactorMatrix instance
    """
    return FactorMatrix.model_validate(data)


# =============================================================================
# Value Comparison Utilities
# =============================================================================

def compare_values(original: Any, restored: Any, tolerance: float = 1e-9) -> bool:
    """
    Compare two values for equality, with tolerance for floats.
    
    Args:
        original: Original value
        restored: Restored value
        tolerance: Tolerance for float comparison
        
    Returns:
        True if values are equal (within tolerance for floats)
    """
    if type(original) != type(restored):
        # Handle int/float comparison
        if isinstance(original, (int, float)) and isinstance(restored, (int, float)):
            return abs(float(original) - float(restored)) < tolerance
        return False
    
    if isinstance(original, float):
        return abs(original - restored) < tolerance
    
    if isinstance(original, dict):
        if set(original.keys()) != set(restored.keys()):
            return False
        return all(
            compare_values(original[k], restored[k], tolerance)
            for k in original.keys()
        )
    
    if isinstance(original, list):
        if len(original) != len(restored):
            return False
        return all(
            compare_values(o, r, tolerance)
            for o, r in zip(original, restored)
        )
    
    return original == restored


def compare_factor_values(
    original: FactorValue, 
    restored: FactorValue,
    tolerance: float = 1e-9
) -> Tuple[bool, Optional[str]]:
    """
    Compare two FactorValue instances for equality.
    
    Args:
        original: Original FactorValue
        restored: Restored FactorValue
        tolerance: Tolerance for float comparison
        
    Returns:
        Tuple of (is_equal, error_message)
    """
    if original.factor_id != restored.factor_id:
        return False, f"factor_id mismatch: {original.factor_id} != {restored.factor_id}"
    
    if not compare_values(original.value, restored.value, tolerance):
        return False, f"value mismatch for {original.factor_id}: {original.value} != {restored.value}"
    
    if abs(original.confidence - restored.confidence) > tolerance:
        return False, f"confidence mismatch for {original.factor_id}: {original.confidence} != {restored.confidence}"
    
    if original.source != restored.source:
        return False, f"source mismatch for {original.factor_id}: {original.source} != {restored.source}"
    
    return True, None


# =============================================================================
# Round-Trip Validation
# =============================================================================

def validate_round_trip_json(matrix: FactorMatrix) -> SerializationValidationResult:
    """
    Validate JSON serialization round-trip for a FactorMatrix.
    
    Args:
        matrix: The FactorMatrix to validate
        
    Returns:
        SerializationValidationResult with validation details
    """
    mismatched_factors = []
    missing_factors = []
    extra_factors = []
    value_mismatches = []
    warnings = []
    
    try:
        # Serialize to JSON
        json_str = serialize_factor_matrix(matrix)
        
        # Deserialize back
        restored = deserialize_factor_matrix(json_str)
        
        # Compare factor counts
        original_keys = set(matrix.factors.keys())
        restored_keys = set(restored.factors.keys())
        
        missing_factors = list(original_keys - restored_keys)
        extra_factors = list(restored_keys - original_keys)
        
        # Compare each factor
        for factor_id in original_keys & restored_keys:
            original_factor = matrix.factors[factor_id]
            restored_factor = restored.factors[factor_id]
            
            is_equal, error_msg = compare_factor_values(original_factor, restored_factor)
            if not is_equal:
                mismatched_factors.append(factor_id)
                value_mismatches.append({
                    "factor_id": factor_id,
                    "error": error_msg,
                    "original": original_factor.model_dump(),
                    "restored": restored_factor.model_dump(),
                })
        
        # Check engine_id
        if matrix.engine_id != restored.engine_id:
            warnings.append(f"engine_id mismatch: {matrix.engine_id} != {restored.engine_id}")
        
        is_valid = (
            len(missing_factors) == 0 and
            len(extra_factors) == 0 and
            len(mismatched_factors) == 0
        )
        
        return SerializationValidationResult(
            is_valid=is_valid,
            original_factor_count=len(matrix.factors),
            restored_factor_count=len(restored.factors),
            mismatched_factors=mismatched_factors,
            missing_factors=missing_factors,
            extra_factors=extra_factors,
            value_mismatches=value_mismatches,
            warnings=warnings,
        )
        
    except Exception as e:
        return SerializationValidationResult(
            is_valid=False,
            original_factor_count=len(matrix.factors),
            restored_factor_count=0,
            mismatched_factors=[],
            missing_factors=list(matrix.factors.keys()),
            extra_factors=[],
            value_mismatches=[],
            warnings=[f"Serialization error: {str(e)}"],
        )


def validate_round_trip_dict(matrix: FactorMatrix) -> SerializationValidationResult:
    """
    Validate dictionary serialization round-trip for a FactorMatrix.
    
    Args:
        matrix: The FactorMatrix to validate
        
    Returns:
        SerializationValidationResult with validation details
    """
    mismatched_factors = []
    missing_factors = []
    extra_factors = []
    value_mismatches = []
    warnings = []
    
    try:
        # Serialize to dict
        data = serialize_factor_matrix_to_dict(matrix)
        
        # Deserialize back
        restored = deserialize_factor_matrix_from_dict(data)
        
        # Compare factor counts
        original_keys = set(matrix.factors.keys())
        restored_keys = set(restored.factors.keys())
        
        missing_factors = list(original_keys - restored_keys)
        extra_factors = list(restored_keys - original_keys)
        
        # Compare each factor
        for factor_id in original_keys & restored_keys:
            original_factor = matrix.factors[factor_id]
            restored_factor = restored.factors[factor_id]
            
            is_equal, error_msg = compare_factor_values(original_factor, restored_factor)
            if not is_equal:
                mismatched_factors.append(factor_id)
                value_mismatches.append({
                    "factor_id": factor_id,
                    "error": error_msg,
                    "original": original_factor.model_dump(),
                    "restored": restored_factor.model_dump(),
                })
        
        # Check engine_id
        if matrix.engine_id != restored.engine_id:
            warnings.append(f"engine_id mismatch: {matrix.engine_id} != {restored.engine_id}")
        
        is_valid = (
            len(missing_factors) == 0 and
            len(extra_factors) == 0 and
            len(mismatched_factors) == 0
        )
        
        return SerializationValidationResult(
            is_valid=is_valid,
            original_factor_count=len(matrix.factors),
            restored_factor_count=len(restored.factors),
            mismatched_factors=mismatched_factors,
            missing_factors=missing_factors,
            extra_factors=extra_factors,
            value_mismatches=value_mismatches,
            warnings=warnings,
        )
        
    except Exception as e:
        return SerializationValidationResult(
            is_valid=False,
            original_factor_count=len(matrix.factors),
            restored_factor_count=0,
            mismatched_factors=[],
            missing_factors=list(matrix.factors.keys()),
            extra_factors=[],
            value_mismatches=[],
            warnings=[f"Serialization error: {str(e)}"],
        )


def validate_round_trip(matrix: FactorMatrix) -> SerializationValidationResult:
    """
    Validate both JSON and dict serialization round-trip for a FactorMatrix.
    
    This is the main validation function for Property 14.
    
    Args:
        matrix: The FactorMatrix to validate
        
    Returns:
        SerializationValidationResult with validation details
    """
    # Validate JSON round-trip
    json_result = validate_round_trip_json(matrix)
    if not json_result.is_valid:
        return json_result
    
    # Validate dict round-trip
    dict_result = validate_round_trip_dict(matrix)
    if not dict_result.is_valid:
        return dict_result
    
    # Both passed
    return json_result


# =============================================================================
# Assertion Helpers
# =============================================================================

def assert_round_trip_consistency(matrix: FactorMatrix, message: str = "") -> None:
    """
    Assert that a FactorMatrix maintains consistency through serialization round-trip.
    
    Args:
        matrix: FactorMatrix to validate
        message: Optional message prefix for assertion error
        
    Raises:
        AssertionError: If round-trip validation fails
    """
    result = validate_round_trip(matrix)
    
    if not result.is_valid:
        error_msg = f"{message}: " if message else ""
        error_msg += "FactorMatrix serialization round-trip failed. "
        
        if result.missing_factors:
            error_msg += f"Missing factors: {result.missing_factors}. "
        if result.extra_factors:
            error_msg += f"Extra factors: {result.extra_factors}. "
        if result.mismatched_factors:
            error_msg += f"Mismatched factors: {result.mismatched_factors}. "
        if result.value_mismatches:
            error_msg += f"Value mismatches: {result.value_mismatches}. "
        if result.warnings:
            error_msg += f"Warnings: {result.warnings}. "
        
        raise AssertionError(error_msg)


def assert_json_round_trip(matrix: FactorMatrix, message: str = "") -> None:
    """
    Assert that a FactorMatrix maintains consistency through JSON round-trip.
    
    Args:
        matrix: FactorMatrix to validate
        message: Optional message prefix for assertion error
        
    Raises:
        AssertionError: If JSON round-trip validation fails
    """
    result = validate_round_trip_json(matrix)
    
    if not result.is_valid:
        error_msg = f"{message}: " if message else ""
        error_msg += "FactorMatrix JSON round-trip failed. "
        
        if result.missing_factors:
            error_msg += f"Missing factors: {result.missing_factors}. "
        if result.extra_factors:
            error_msg += f"Extra factors: {result.extra_factors}. "
        if result.mismatched_factors:
            error_msg += f"Mismatched factors: {result.mismatched_factors}. "
        
        raise AssertionError(error_msg)
