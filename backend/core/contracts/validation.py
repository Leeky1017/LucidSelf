# backend/core/contracts/validation.py
"""
FactorMatrix Validation Tools

Validates FactorMatrix outputs from all Calculators for:
- Factor ID naming convention compliance ({system}_*)
- Required field presence (confidence, source)
- Engine ID consistency

Follows:
- Requirements 10.1, 10.2, 10.3, 10.4 from calculator-integration spec
- Data Contract §1.1 FactorValue/FactorMatrix
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional, Set

from backend.core.contracts.runtime_models import FactorMatrix, FactorValue


# =============================================================================
# Constants: Valid System Prefixes
# =============================================================================

VALID_SYSTEM_PREFIXES = frozenset([
    "bazi",      # BaziCalculator
    "ziwei",     # ZiweiCalculator
    "astro",     # AstroCalculator
    "tarot",     # TarotInterpreter
    "dream",     # DreamExtractor
    "yijing",    # YijingCalculator
])
"""Valid system prefixes for factor IDs per data contract §4.1."""

VALID_SOURCES = frozenset([
    "calculator",
    "semantic",
    "manual",
    "llm_infer",
])
"""Valid source values for FactorValue."""

# Factor ID pattern: {system}_{rest} where rest uses lowercase alphanumeric and underscores
FACTOR_ID_PATTERN = re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+)*$")
"""Pattern for valid factor IDs: lowercase alphanumeric with underscores."""


# =============================================================================
# Validation Result Models
# =============================================================================

@dataclass
class ValidationError:
    """Single validation error."""
    factor_id: Optional[str]
    field: str
    message: str
    severity: str = "error"  # "error" or "warning"


@dataclass
class ValidationResult:
    """Result of FactorMatrix validation."""
    valid: bool
    errors: List[ValidationError] = field(default_factory=list)
    warnings: List[ValidationError] = field(default_factory=list)
    factor_count: int = 0
    systems_found: Set[str] = field(default_factory=set)
    
    def add_error(self, factor_id: Optional[str], field: str, message: str) -> None:
        """Add a validation error."""
        self.errors.append(ValidationError(factor_id, field, message, "error"))
        self.valid = False
    
    def add_warning(self, factor_id: Optional[str], field: str, message: str) -> None:
        """Add a validation warning."""
        self.warnings.append(ValidationError(factor_id, field, message, "warning"))


# =============================================================================
# Validation Functions
# =============================================================================

def validate_factor_id_format(factor_id: str) -> Optional[str]:
    """
    Validate factor ID format.
    
    Rules:
    - Must start with a valid system prefix
    - Must use lowercase alphanumeric characters and underscores
    - Must follow pattern: {system}_{component}_{...}
    
    Args:
        factor_id: The factor ID to validate
        
    Returns:
        Error message if invalid, None if valid
    """
    if not factor_id:
        return "Factor ID cannot be empty"
    
    # Check overall pattern
    if not FACTOR_ID_PATTERN.match(factor_id):
        return f"Factor ID '{factor_id}' does not match pattern (lowercase alphanumeric with underscores)"
    
    # Extract system prefix (first segment before underscore)
    parts = factor_id.split("_")
    if len(parts) < 2:
        return f"Factor ID '{factor_id}' must have at least two segments (system_component)"
    
    system_prefix = parts[0]
    if system_prefix not in VALID_SYSTEM_PREFIXES:
        return (
            f"Factor ID '{factor_id}' has invalid system prefix '{system_prefix}'. "
            f"Valid prefixes: {sorted(VALID_SYSTEM_PREFIXES)}"
        )
    
    return None


def validate_factor_value(factor_id: str, factor_value: FactorValue) -> List[ValidationError]:
    """
    Validate a single FactorValue.
    
    Checks:
    - factor_id consistency (key matches value.factor_id)
    - confidence is in valid range [0.0, 1.0]
    - source is a valid value
    
    Args:
        factor_id: The key in the factors dict
        factor_value: The FactorValue to validate
        
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    # Check factor_id consistency
    if factor_value.factor_id != factor_id:
        errors.append(ValidationError(
            factor_id=factor_id,
            field="factor_id",
            message=f"Factor ID mismatch: key='{factor_id}', value.factor_id='{factor_value.factor_id}'"
        ))
    
    # Check confidence range (Pydantic should enforce this, but double-check)
    if not (0.0 <= factor_value.confidence <= 1.0):
        errors.append(ValidationError(
            factor_id=factor_id,
            field="confidence",
            message=f"Confidence {factor_value.confidence} out of range [0.0, 1.0]"
        ))
    
    # Check source validity
    if factor_value.source not in VALID_SOURCES:
        errors.append(ValidationError(
            factor_id=factor_id,
            field="source",
            message=f"Invalid source '{factor_value.source}'. Valid sources: {sorted(VALID_SOURCES)}"
        ))
    
    return errors


def validate_factor_matrix(
    matrix: FactorMatrix,
    expected_system: Optional[str] = None,
    strict: bool = True
) -> ValidationResult:
    """
    Validate a FactorMatrix for compliance with data contract.
    
    Validates:
    - All factor IDs follow naming convention ({system}_*)
    - All FactorValues have required fields (confidence, source)
    - Factor ID consistency (key matches value.factor_id)
    - Engine ID is present
    - Optionally: all factors belong to expected system
    
    Args:
        matrix: The FactorMatrix to validate
        expected_system: If provided, all factors must use this system prefix
        strict: If True, treat warnings as errors
        
    Returns:
        ValidationResult with errors and warnings
        
    Example:
        >>> from backend.core.contracts import FactorMatrix, FactorValue
        >>> matrix = FactorMatrix(
        ...     factors={"bazi_day_master_jia": FactorValue(
        ...         factor_id="bazi_day_master_jia",
        ...         value=True,
        ...         confidence=1.0,
        ...         source="calculator"
        ...     )},
        ...     engine_id="bazi-calculator"
        ... )
        >>> result = validate_factor_matrix(matrix)
        >>> result.valid
        True
    """
    result = ValidationResult(valid=True, factor_count=len(matrix.factors))
    
    # Validate engine_id
    if not matrix.engine_id:
        result.add_error(None, "engine_id", "Engine ID is required")
    
    # Validate each factor
    for factor_id, factor_value in matrix.factors.items():
        # Validate factor ID format
        format_error = validate_factor_id_format(factor_id)
        if format_error:
            result.add_error(factor_id, "factor_id", format_error)
        else:
            # Extract system prefix for tracking
            system = factor_id.split("_")[0]
            result.systems_found.add(system)
            
            # Check expected system if specified
            if expected_system and system != expected_system:
                result.add_error(
                    factor_id,
                    "factor_id",
                    f"Factor '{factor_id}' uses system '{system}' but expected '{expected_system}'"
                )
        
        # Validate FactorValue fields
        value_errors = validate_factor_value(factor_id, factor_value)
        for error in value_errors:
            result.add_error(error.factor_id, error.field, error.message)
    
    # Warn if multiple systems found (unusual but not necessarily wrong)
    if len(result.systems_found) > 1:
        result.add_warning(
            None,
            "systems",
            f"Multiple system prefixes found: {sorted(result.systems_found)}. "
            "This is unusual for a single Calculator output."
        )
    
    # In strict mode, warnings become errors
    if strict and result.warnings:
        for warning in result.warnings:
            result.add_error(warning.factor_id, warning.field, warning.message)
        result.warnings = []
    
    return result


def get_system_from_factor_id(factor_id: str) -> Optional[str]:
    """
    Extract system prefix from a factor ID.
    
    Args:
        factor_id: The factor ID to parse
        
    Returns:
        System prefix if valid, None otherwise
    """
    if not factor_id or "_" not in factor_id:
        return None
    
    system = factor_id.split("_")[0]
    return system if system in VALID_SYSTEM_PREFIXES else None


def is_valid_factor_id(factor_id: str) -> bool:
    """
    Quick check if a factor ID is valid.
    
    Args:
        factor_id: The factor ID to check
        
    Returns:
        True if valid, False otherwise
    """
    return validate_factor_id_format(factor_id) is None
