# backend/core/testing/output_validation.py
"""
Calculator output validation utilities.

Validates that Calculator outputs conform to the structural-only constraint:
- Calculator layer should only produce structural factors (factor_id + value)
- No semantic fields (description, meaning, interpretation) should be present

**Feature: calculator-accuracy-audit, Property 1: Calculator 输出不包含语义字段**
**Validates: Requirements 1.1, 1.2**
"""

from typing import Any, Dict, List, Optional, Set, Tuple
from pydantic import BaseModel

from backend.core.contracts import FactorValue, FactorMatrix


# =============================================================================
# Semantic Field Detection
# =============================================================================

# Fields that indicate semantic content (should NOT be in Calculator output)
SEMANTIC_FIELD_NAMES: Set[str] = {
    # Direct semantic fields
    "description",
    "meaning",
    "interpretation",
    "explanation",
    "significance",
    "symbolism",
    "narrative",
    "text",
    "commentary",
    
    # Chinese semantic field names
    "含义",
    "解释",
    "说明",
    "释义",
    "象征",
    "寓意",
    "注解",
    "注释",
    
    # Semantic reference fields
    "semantic_entry",
    "semantic_ref",
    "semantic_content",
    "narrative_snippet",
    "gua_ci",  # 卦辞
    "yao_ci",  # 爻辞
    "card_meaning",
    "symbol_meaning",
}

# Patterns that suggest semantic content in field names
SEMANTIC_FIELD_PATTERNS: List[str] = [
    "_meaning",
    "_description",
    "_interpretation",
    "_explanation",
    "_text",
    "_narrative",
    "_commentary",
]


class OutputValidationResult(BaseModel):
    """Result of output validation."""
    
    is_valid: bool
    semantic_fields_found: List[str]
    invalid_factor_ids: List[str]
    warnings: List[str]
    
    def __bool__(self) -> bool:
        return self.is_valid


def is_semantic_field_name(field_name: str) -> bool:
    """
    Check if a field name indicates semantic content.
    
    Args:
        field_name: The field name to check
        
    Returns:
        True if the field name suggests semantic content
    """
    # Direct match
    if field_name.lower() in SEMANTIC_FIELD_NAMES:
        return True
    
    # Pattern match
    field_lower = field_name.lower()
    for pattern in SEMANTIC_FIELD_PATTERNS:
        if pattern in field_lower:
            return True
    
    return False


def check_value_for_semantic_content(value: Any, path: str = "") -> List[str]:
    """
    Recursively check a value for semantic content.
    
    Args:
        value: The value to check
        path: Current path for error reporting
        
    Returns:
        List of paths where semantic content was found
    """
    semantic_paths = []
    
    if isinstance(value, dict):
        for key, val in value.items():
            current_path = f"{path}.{key}" if path else key
            
            # Check if key is a semantic field
            if is_semantic_field_name(key):
                semantic_paths.append(current_path)
            
            # Recursively check nested values
            semantic_paths.extend(check_value_for_semantic_content(val, current_path))
    
    elif isinstance(value, list):
        for i, item in enumerate(value):
            current_path = f"{path}[{i}]"
            semantic_paths.extend(check_value_for_semantic_content(item, current_path))
    
    return semantic_paths


def validate_factor_value_no_semantics(factor: FactorValue) -> Tuple[bool, List[str]]:
    """
    Validate that a FactorValue contains no semantic fields.
    
    Args:
        factor: The FactorValue to validate
        
    Returns:
        Tuple of (is_valid, list of semantic field paths found)
    """
    semantic_paths = []
    
    # Check the value itself for nested semantic content
    if isinstance(factor.value, (dict, list)):
        paths = check_value_for_semantic_content(factor.value, f"factors[{factor.factor_id}].value")
        semantic_paths.extend(paths)
    
    return len(semantic_paths) == 0, semantic_paths


def validate_factor_matrix_no_semantics(matrix: FactorMatrix) -> OutputValidationResult:
    """
    Validate that a FactorMatrix contains no semantic fields.
    
    This is the main validation function for Property 1.
    
    Args:
        matrix: The FactorMatrix to validate
        
    Returns:
        OutputValidationResult with validation details
    """
    semantic_fields_found = []
    invalid_factor_ids = []
    warnings = []
    
    for factor_id, factor in matrix.factors.items():
        is_valid, paths = validate_factor_value_no_semantics(factor)
        
        if not is_valid:
            semantic_fields_found.extend(paths)
            invalid_factor_ids.append(factor_id)
    
    return OutputValidationResult(
        is_valid=len(semantic_fields_found) == 0,
        semantic_fields_found=semantic_fields_found,
        invalid_factor_ids=invalid_factor_ids,
        warnings=warnings,
    )


def validate_calculator_output(output: Any) -> OutputValidationResult:
    """
    Validate any Calculator output for semantic content.
    
    Handles both FactorMatrix and raw dict outputs.
    
    Args:
        output: Calculator output (FactorMatrix, dict, or Pydantic model)
        
    Returns:
        OutputValidationResult with validation details
    """
    semantic_fields_found = []
    invalid_factor_ids = []
    warnings = []
    
    # Convert to dict if needed
    if isinstance(output, FactorMatrix):
        return validate_factor_matrix_no_semantics(output)
    
    if hasattr(output, "model_dump"):
        output_dict = output.model_dump()
    elif hasattr(output, "__dict__"):
        output_dict = output.__dict__
    elif isinstance(output, dict):
        output_dict = output
    else:
        warnings.append(f"Unknown output type: {type(output)}")
        return OutputValidationResult(
            is_valid=True,
            semantic_fields_found=[],
            invalid_factor_ids=[],
            warnings=warnings,
        )
    
    # Check all fields recursively
    semantic_paths = check_value_for_semantic_content(output_dict)
    semantic_fields_found.extend(semantic_paths)
    
    return OutputValidationResult(
        is_valid=len(semantic_fields_found) == 0,
        semantic_fields_found=semantic_fields_found,
        invalid_factor_ids=invalid_factor_ids,
        warnings=warnings,
    )


# =============================================================================
# Assertion Helpers
# =============================================================================

def assert_no_semantic_fields(output: Any, message: str = "") -> None:
    """
    Assert that Calculator output contains no semantic fields.
    
    Args:
        output: Calculator output to validate
        message: Optional message prefix for assertion error
        
    Raises:
        AssertionError: If semantic fields are found
    """
    result = validate_calculator_output(output)
    
    if not result.is_valid:
        error_msg = f"{message}: " if message else ""
        error_msg += f"Found semantic fields in Calculator output: {result.semantic_fields_found}"
        raise AssertionError(error_msg)


def assert_factor_matrix_structural_only(matrix: FactorMatrix, message: str = "") -> None:
    """
    Assert that a FactorMatrix contains only structural factors.
    
    Args:
        matrix: FactorMatrix to validate
        message: Optional message prefix for assertion error
        
    Raises:
        AssertionError: If semantic fields are found
    """
    result = validate_factor_matrix_no_semantics(matrix)
    
    if not result.is_valid:
        error_msg = f"{message}: " if message else ""
        error_msg += (
            f"FactorMatrix contains semantic fields. "
            f"Invalid factors: {result.invalid_factor_ids}. "
            f"Semantic paths: {result.semantic_fields_found}"
        )
        raise AssertionError(error_msg)
