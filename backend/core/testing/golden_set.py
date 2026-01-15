# backend/core/testing/golden_set.py
"""
Golden Set testing framework for Calculator accuracy audit.

Golden Set is a collection of verified test cases that serve as the
ground truth for Calculator accuracy validation.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Type
from pydantic import BaseModel, Field
import pytest


class GoldenSetCase(BaseModel):
    """Golden Set test case model."""
    
    case_id: str = Field(..., description="Unique case identifier")
    calculator_type: str = Field(..., description="Calculator type: bazi/ziwei/yijing/astro/tarot/dream")
    input_data: Dict[str, Any] = Field(..., description="Input data for calculator")
    expected_output: Dict[str, Any] = Field(..., description="Expected output values")
    
    # Coverage tags for tracking test coverage
    coverage_tags: List[str] = Field(default_factory=list, description="Coverage dimension tags")
    
    # Source and verification info
    source: str = Field(..., description="Data source (e.g., '香港天文台', '万年历')")
    verified_by: str = Field(..., description="Verifier identifier")
    verified_at: datetime = Field(default_factory=datetime.now, description="Verification timestamp")
    
    # Cross-validation sources
    cross_validation_sources: List[str] = Field(
        default_factory=list, 
        description="Sources used for cross-validation"
    )
    
    # Optional tolerance for numeric comparisons
    tolerance: Optional[Dict[str, float]] = Field(
        default=None,
        description="Tolerance values for numeric fields"
    )


class GoldenSetRegistry(BaseModel):
    """Registry for Golden Set test cases."""
    
    calculator_type: str = Field(..., description="Calculator type")
    cases: List[GoldenSetCase] = Field(default_factory=list, description="Test cases")
    coverage_matrix: Dict[str, int] = Field(
        default_factory=dict, 
        description="Coverage dimension -> case count"
    )
    last_updated: datetime = Field(default_factory=datetime.now)
    
    def update_coverage_matrix(self) -> None:
        """Update coverage matrix based on current cases."""
        self.coverage_matrix.clear()
        for case in self.cases:
            for tag in case.coverage_tags:
                self.coverage_matrix[tag] = self.coverage_matrix.get(tag, 0) + 1
    
    def get_coverage_report(self) -> Dict[str, Any]:
        """Generate coverage report."""
        self.update_coverage_matrix()
        return {
            "calculator_type": self.calculator_type,
            "total_cases": len(self.cases),
            "coverage_matrix": self.coverage_matrix,
            "last_updated": self.last_updated.isoformat(),
        }


class GoldenSetLoader:
    """Loader for Golden Set JSONL files."""
    
    def __init__(self, base_path: Optional[Path] = None):
        """
        Initialize loader.
        
        Args:
            base_path: Base path for Golden Set files. 
                      Defaults to backend/calculators/{calculator}/tests/golden_cases/
        """
        self.base_path = base_path or Path("backend/calculators")
    
    def load_jsonl(self, file_path: Path) -> List[GoldenSetCase]:
        """
        Load Golden Set cases from JSONL file.
        
        Args:
            file_path: Path to JSONL file
            
        Returns:
            List of GoldenSetCase objects
        """
        cases = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    case = GoldenSetCase(**data)
                    cases.append(case)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON at line {line_num}: {e}")
                except Exception as e:
                    raise ValueError(f"Invalid case at line {line_num}: {e}")
        return cases
    
    def load_calculator_golden_set(self, calculator_type: str) -> GoldenSetRegistry:
        """
        Load Golden Set for a specific calculator.
        
        Args:
            calculator_type: Calculator type (bazi/ziwei/yijing/astro/tarot/dream)
            
        Returns:
            GoldenSetRegistry with loaded cases
        """
        golden_path = self.base_path / calculator_type / "tests" / "golden_cases"
        
        if not golden_path.exists():
            return GoldenSetRegistry(calculator_type=calculator_type)
        
        cases = []
        for jsonl_file in golden_path.glob("*.jsonl"):
            cases.extend(self.load_jsonl(jsonl_file))
        
        registry = GoldenSetRegistry(
            calculator_type=calculator_type,
            cases=cases,
        )
        registry.update_coverage_matrix()
        return registry
    
    def save_jsonl(self, cases: List[GoldenSetCase], file_path: Path) -> None:
        """
        Save Golden Set cases to JSONL file.
        
        Args:
            cases: List of GoldenSetCase objects
            file_path: Output file path
        """
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            for case in cases:
                f.write(case.model_dump_json() + "\n")


class GoldenSetRunner:
    """Runner for Golden Set tests."""
    
    def __init__(
        self,
        calculator_factory: Callable[[str], Any],
        tolerance_defaults: Optional[Dict[str, float]] = None,
    ):
        """
        Initialize runner.
        
        Args:
            calculator_factory: Factory function that creates calculator by type
            tolerance_defaults: Default tolerance values for numeric comparisons
        """
        self.calculator_factory = calculator_factory
        self.tolerance_defaults = tolerance_defaults or {}
    
    def run_case(self, case: GoldenSetCase) -> Dict[str, Any]:
        """
        Run a single Golden Set case.
        
        Args:
            case: GoldenSetCase to run
            
        Returns:
            Dict with test results
        """
        calculator = self.calculator_factory(case.calculator_type)
        
        # Execute calculation
        try:
            result = calculator.calculate(case.input_data)
            actual_output = self._extract_output(result, case.expected_output.keys())
        except Exception as e:
            return {
                "case_id": case.case_id,
                "passed": False,
                "error": str(e),
                "expected": case.expected_output,
                "actual": None,
            }
        
        # Compare results
        tolerance = case.tolerance or self.tolerance_defaults
        passed, differences = self._compare_outputs(
            case.expected_output, 
            actual_output, 
            tolerance
        )
        
        return {
            "case_id": case.case_id,
            "passed": passed,
            "expected": case.expected_output,
            "actual": actual_output,
            "differences": differences if not passed else None,
        }
    
    def run_registry(self, registry: GoldenSetRegistry) -> Dict[str, Any]:
        """
        Run all cases in a registry.
        
        Args:
            registry: GoldenSetRegistry to run
            
        Returns:
            Dict with aggregated results
        """
        results = []
        passed_count = 0
        failed_count = 0
        
        for case in registry.cases:
            result = self.run_case(case)
            results.append(result)
            if result["passed"]:
                passed_count += 1
            else:
                failed_count += 1
        
        return {
            "calculator_type": registry.calculator_type,
            "total": len(results),
            "passed": passed_count,
            "failed": failed_count,
            "pass_rate": passed_count / len(results) if results else 0,
            "results": results,
        }
    
    def _extract_output(
        self, 
        result: Any, 
        expected_keys: List[str]
    ) -> Dict[str, Any]:
        """Extract relevant output fields from calculator result."""
        if hasattr(result, "model_dump"):
            result_dict = result.model_dump()
        elif hasattr(result, "__dict__"):
            result_dict = result.__dict__
        elif isinstance(result, dict):
            result_dict = result
        else:
            raise ValueError(f"Cannot extract output from {type(result)}")
        
        # Flatten nested structures if needed
        output = {}
        for key in expected_keys:
            if key in result_dict:
                output[key] = result_dict[key]
            else:
                # Try to find in nested structures
                output[key] = self._find_nested_value(result_dict, key)
        
        return output
    
    def _find_nested_value(self, data: Dict, key: str) -> Any:
        """Find value in nested dict structure."""
        if key in data:
            return data[key]
        
        for v in data.values():
            if isinstance(v, dict):
                result = self._find_nested_value(v, key)
                if result is not None:
                    return result
        
        return None
    
    def _compare_outputs(
        self,
        expected: Dict[str, Any],
        actual: Dict[str, Any],
        tolerance: Dict[str, float],
    ) -> tuple[bool, List[Dict[str, Any]]]:
        """
        Compare expected and actual outputs.
        
        Returns:
            Tuple of (passed, differences)
        """
        differences = []
        
        for key, expected_value in expected.items():
            actual_value = actual.get(key)
            
            if actual_value is None:
                differences.append({
                    "field": key,
                    "expected": expected_value,
                    "actual": None,
                    "reason": "missing",
                })
                continue
            
            # Numeric comparison with tolerance
            if isinstance(expected_value, (int, float)) and key in tolerance:
                if abs(expected_value - actual_value) > tolerance[key]:
                    differences.append({
                        "field": key,
                        "expected": expected_value,
                        "actual": actual_value,
                        "tolerance": tolerance[key],
                        "reason": "out_of_tolerance",
                    })
            # Exact comparison
            elif expected_value != actual_value:
                differences.append({
                    "field": key,
                    "expected": expected_value,
                    "actual": actual_value,
                    "reason": "mismatch",
                })
        
        return len(differences) == 0, differences


def golden_set_test(calculator_type: str, case_id: Optional[str] = None):
    """
    Pytest decorator for Golden Set tests.
    
    Usage:
        @golden_set_test("bazi")
        def test_bazi_golden_set(case, calculator):
            result = calculator.calculate(case.input_data)
            assert result.year_stem == case.expected_output["year_stem"]
    """
    def decorator(func):
        loader = GoldenSetLoader()
        registry = loader.load_calculator_golden_set(calculator_type)
        
        cases = registry.cases
        if case_id:
            cases = [c for c in cases if c.case_id == case_id]
        
        @pytest.mark.parametrize(
            "case",
            cases,
            ids=[c.case_id for c in cases],
        )
        def wrapper(case, *args, **kwargs):
            return func(case, *args, **kwargs)
        
        return wrapper
    
    return decorator
