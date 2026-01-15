# backend/core/testing/cross_validation.py
"""
Cross-source validation framework for Calculator accuracy audit.

Validates Calculator outputs against multiple authoritative data sources
to ensure accuracy and consistency.
"""

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Protocol
from pydantic import BaseModel, Field
import json


class ValidationStatus(str, Enum):
    """Status of cross-validation."""
    PASSED = "passed"
    FAILED = "failed"
    DISCREPANCY = "discrepancy"
    PENDING_RESOLUTION = "pending_resolution"
    RESOLVED = "resolved"


class CrossValidationConfig(BaseModel):
    """Configuration for cross-source validation."""
    
    calculator_type: str = Field(..., description="Calculator type")
    primary_source: str = Field(..., description="Primary authoritative source")
    validation_sources: List[str] = Field(
        default_factory=list,
        description="Additional sources for validation"
    )
    tolerance: Dict[str, float] = Field(
        default_factory=dict,
        description="Tolerance values for numeric comparisons"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "calculator_type": "bazi",
                "primary_source": "香港天文台",
                "validation_sources": ["中国科学院紫金山天文台", "万年历"],
                "tolerance": {"solar_term_time": 60}
            }
        }


class Discrepancy(BaseModel):
    """A discrepancy found during cross-validation."""
    
    field: str = Field(..., description="Field with discrepancy")
    primary_value: Any = Field(..., description="Value from primary source")
    validation_values: Dict[str, Any] = Field(
        ..., 
        description="Values from validation sources"
    )
    calculated_value: Any = Field(..., description="Value from calculator")
    severity: str = Field(default="medium", description="Severity: low/medium/high")
    notes: Optional[str] = None


class CrossValidationResult(BaseModel):
    """Result of cross-source validation."""
    
    case_id: str = Field(..., description="Test case identifier")
    calculator_type: str = Field(..., description="Calculator type")
    status: ValidationStatus = Field(..., description="Validation status")
    
    # Results from each source
    primary_result: Dict[str, Any] = Field(
        default_factory=dict,
        description="Result from primary source"
    )
    validation_results: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="Results from validation sources"
    )
    calculated_result: Dict[str, Any] = Field(
        default_factory=dict,
        description="Result from calculator"
    )
    
    # Discrepancies
    discrepancies: List[Discrepancy] = Field(
        default_factory=list,
        description="List of discrepancies found"
    )
    
    # Resolution
    resolution: Optional[str] = Field(None, description="Resolution decision")
    resolved_by: Optional[str] = Field(None, description="Person who resolved")
    resolved_at: Optional[datetime] = Field(None, description="Resolution timestamp")
    
    # Metadata
    validated_at: datetime = Field(default_factory=datetime.now)


class DataSourceProvider(Protocol):
    """Protocol for data source providers."""
    
    def get_value(self, input_data: Dict[str, Any], field: str) -> Any:
        """Get value for a field from this data source."""
        ...
    
    @property
    def source_name(self) -> str:
        """Name of this data source."""
        ...


class CrossValidator:
    """Cross-source validator for Calculator outputs."""
    
    def __init__(
        self,
        config: CrossValidationConfig,
        calculator_factory: Callable[[str], Any],
        source_providers: Optional[Dict[str, DataSourceProvider]] = None,
    ):
        """
        Initialize cross-validator.
        
        Args:
            config: Validation configuration
            calculator_factory: Factory to create calculator instances
            source_providers: Dict of source name -> provider
        """
        self.config = config
        self.calculator_factory = calculator_factory
        self.source_providers = source_providers or {}
        self.results: List[CrossValidationResult] = []
    
    def validate(
        self,
        case_id: str,
        input_data: Dict[str, Any],
        fields_to_validate: List[str],
        primary_values: Dict[str, Any],
        validation_values: Optional[Dict[str, Dict[str, Any]]] = None,
    ) -> CrossValidationResult:
        """
        Validate calculator output against multiple sources.
        
        Args:
            case_id: Test case identifier
            input_data: Input data for calculator
            fields_to_validate: Fields to validate
            primary_values: Expected values from primary source
            validation_values: Expected values from validation sources
            
        Returns:
            CrossValidationResult
        """
        # Get calculator result
        calculator = self.calculator_factory(self.config.calculator_type)
        try:
            calc_result = calculator.calculate(input_data)
            calculated_values = self._extract_values(calc_result, fields_to_validate)
        except Exception as e:
            return CrossValidationResult(
                case_id=case_id,
                calculator_type=self.config.calculator_type,
                status=ValidationStatus.FAILED,
                discrepancies=[Discrepancy(
                    field="calculation",
                    primary_value=None,
                    validation_values={},
                    calculated_value=str(e),
                    severity="high",
                    notes="Calculator raised exception",
                )],
            )
        
        # Compare with sources
        discrepancies = []
        validation_values = validation_values or {}
        
        for field in fields_to_validate:
            primary_value = primary_values.get(field)
            calc_value = calculated_values.get(field)
            
            # Check against primary source
            if not self._values_match(primary_value, calc_value, field):
                discrepancies.append(Discrepancy(
                    field=field,
                    primary_value=primary_value,
                    validation_values={
                        src: vals.get(field) 
                        for src, vals in validation_values.items()
                    },
                    calculated_value=calc_value,
                    severity=self._determine_severity(field),
                ))
        
        # Determine status
        if not discrepancies:
            status = ValidationStatus.PASSED
        else:
            status = ValidationStatus.DISCREPANCY
        
        result = CrossValidationResult(
            case_id=case_id,
            calculator_type=self.config.calculator_type,
            status=status,
            primary_result=primary_values,
            validation_results=validation_values,
            calculated_result=calculated_values,
            discrepancies=discrepancies,
        )
        
        self.results.append(result)
        return result
    
    def _extract_values(
        self, 
        result: Any, 
        fields: List[str]
    ) -> Dict[str, Any]:
        """Extract field values from calculator result."""
        if hasattr(result, "model_dump"):
            result_dict = result.model_dump()
        elif hasattr(result, "__dict__"):
            result_dict = result.__dict__
        elif isinstance(result, dict):
            result_dict = result
        else:
            return {}
        
        values = {}
        for field in fields:
            if field in result_dict:
                values[field] = result_dict[field]
            else:
                # Try nested lookup
                values[field] = self._find_nested(result_dict, field)
        
        return values
    
    def _find_nested(self, data: Dict, key: str) -> Any:
        """Find value in nested dict."""
        if key in data:
            return data[key]
        for v in data.values():
            if isinstance(v, dict):
                result = self._find_nested(v, key)
                if result is not None:
                    return result
        return None
    
    def _values_match(
        self, 
        expected: Any, 
        actual: Any, 
        field: str
    ) -> bool:
        """Check if values match within tolerance."""
        if expected is None or actual is None:
            return expected == actual
        
        # Numeric comparison with tolerance
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            tolerance = self.config.tolerance.get(field, 0)
            return abs(expected - actual) <= tolerance
        
        # Exact comparison
        return expected == actual
    
    def _determine_severity(self, field: str) -> str:
        """Determine severity of discrepancy based on field."""
        high_severity_fields = [
            "year_stem", "year_branch", "month_stem", "month_branch",
            "day_stem", "day_branch", "hour_stem", "hour_branch",
            "hexagram_id", "ziwei_star_position",
        ]
        if field in high_severity_fields:
            return "high"
        return "medium"
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary of all validation results."""
        passed = sum(1 for r in self.results if r.status == ValidationStatus.PASSED)
        failed = sum(1 for r in self.results if r.status == ValidationStatus.FAILED)
        discrepancy = sum(1 for r in self.results if r.status == ValidationStatus.DISCREPANCY)
        
        return {
            "calculator_type": self.config.calculator_type,
            "total": len(self.results),
            "passed": passed,
            "failed": failed,
            "discrepancy": discrepancy,
            "pass_rate": passed / len(self.results) if self.results else 0,
        }
    
    def save_results(self, file_path: Path) -> None:
        """Save validation results to JSON file."""
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(
                [r.model_dump() for r in self.results],
                f,
                ensure_ascii=False,
                indent=2,
                default=str,
            )
    
    def load_results(self, file_path: Path) -> None:
        """Load validation results from JSON file."""
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.results = [CrossValidationResult(**r) for r in data]


# Pre-configured validation configs for each calculator type

BAZI_VALIDATION_CONFIG = CrossValidationConfig(
    calculator_type="bazi",
    primary_source="香港天文台",
    validation_sources=["中国科学院紫金山天文台", "万年历"],
    tolerance={"solar_term_time": 60},  # 60 seconds tolerance
)

ZIWEI_VALIDATION_CONFIG = CrossValidationConfig(
    calculator_type="ziwei",
    primary_source="紫微斗数全书",
    validation_sources=["开源紫微排盘A", "开源紫微排盘B"],
    tolerance={},  # Exact match required
)

ASTRO_VALIDATION_CONFIG = CrossValidationConfig(
    calculator_type="astro",
    primary_source="Swiss Ephemeris",
    validation_sources=["Astro.com", "Solar Fire"],
    tolerance={"longitude": 0.0167},  # 1 arcminute = 0.0167 degrees
)

YIJING_VALIDATION_CONFIG = CrossValidationConfig(
    calculator_type="yijing",
    primary_source="周易",
    validation_sources=[],
    tolerance={},  # Exact match required
)

TAROT_VALIDATION_CONFIG = CrossValidationConfig(
    calculator_type="tarot",
    primary_source="塔罗图像密钥",
    validation_sources=["托特塔罗"],
    tolerance={},
)

DREAM_VALIDATION_CONFIG = CrossValidationConfig(
    calculator_type="dream",
    primary_source="梦林玄解",
    validation_sources=["周公解梦"],
    tolerance={},
)
