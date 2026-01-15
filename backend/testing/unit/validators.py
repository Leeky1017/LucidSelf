"""
Rule Validators

规则验证器，用于验证规则匹配结果。

对照 design.md §2.1 目录结构
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple


class RuleValidator:
    """
    规则验证器
    
    提供规则结果验证的工具方法。
    """
    
    @staticmethod
    def validate_hit(
        result: Any,
        expected_hit: bool,
    ) -> Tuple[bool, Optional[str]]:
        """
        验证命中状态
        
        Returns:
            (passed, error_message)
        """
        actual_hit = getattr(result, "hit", None)
        if actual_hit is None:
            actual_hit = getattr(result, "matched", False)
        
        if actual_hit != expected_hit:
            return False, f"Expected hit={expected_hit}, got {actual_hit}"
        return True, None
    
    @staticmethod
    def validate_dimension(
        result: Any,
        expected_dimension: str,
    ) -> Tuple[bool, Optional[str]]:
        """验证维度"""
        actual = getattr(result, "dimension", None)
        if actual != expected_dimension:
            return False, f"Expected dimension={expected_dimension}, got {actual}"
        return True, None
    
    @staticmethod
    def validate_level(
        result: Any,
        expected_level: str,
    ) -> Tuple[bool, Optional[str]]:
        """验证等级"""
        actual = getattr(result, "level", None)
        if actual != expected_level:
            return False, f"Expected level={expected_level}, got {actual}"
        return True, None
    
    @staticmethod
    def validate_confidence(
        result: Any,
        min_confidence: float,
        max_confidence: float,
    ) -> Tuple[bool, Optional[str]]:
        """验证置信度范围"""
        actual = getattr(result, "confidence", None)
        if actual is None:
            return True, None  # 无置信度字段，跳过检查
        
        if not (min_confidence <= actual <= max_confidence):
            return False, f"Expected confidence in [{min_confidence}, {max_confidence}], got {actual}"
        return True, None
    
    @staticmethod
    def validate_all(
        result: Any,
        expected_hit: bool,
        expected_dimension: Optional[str] = None,
        expected_level: Optional[str] = None,
        confidence_range: Tuple[float, float] = (0.0, 1.0),
    ) -> Dict[str, Any]:
        """
        完整验证
        
        Returns:
            {passed: bool, errors: List[str], details: Dict}
        """
        errors = []
        
        # 验证命中
        passed, error = RuleValidator.validate_hit(result, expected_hit)
        if not passed:
            errors.append(error)
        
        # 仅在期望命中时验证其他字段
        if expected_hit and getattr(result, "hit", False):
            if expected_dimension:
                passed, error = RuleValidator.validate_dimension(result, expected_dimension)
                if not passed:
                    errors.append(error)
            
            if expected_level:
                passed, error = RuleValidator.validate_level(result, expected_level)
                if not passed:
                    errors.append(error)
            
            passed, error = RuleValidator.validate_confidence(
                result, confidence_range[0], confidence_range[1]
            )
            if not passed:
                errors.append(error)
        
        return {
            "passed": len(errors) == 0,
            "errors": errors,
            "details": {
                "actual_hit": getattr(result, "hit", None),
                "actual_dimension": getattr(result, "dimension", None),
                "actual_level": getattr(result, "level", None),
                "actual_confidence": getattr(result, "confidence", None),
            },
        }
