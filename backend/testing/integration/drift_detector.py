"""
Drift Detector

漂移检测器，用于检测 GoldenCase 结果漂移。

对照 design.md §2.1 目录结构
对照 Requirements R-6-1-09 ~ R-6-1-11
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class DriftReport:
    """漂移报告"""
    total_drift: float
    engine_drifts: Dict[str, float]
    field_diffs: List[Dict[str, Any]]
    passed: bool
    max_drift: float


class DriftDetector:
    """
    漂移检测器
    
    对照 Requirements R-6-1-09 ~ R-6-1-11
    
    用于检测 GoldenCase 结果与基线的漂移。
    """
    
    def __init__(
        self,
        default_max_drift: float = 0.1,
        numeric_tolerance: float = 0.01,
    ):
        """
        初始化漂移检测器
        
        Args:
            default_max_drift: 默认最大漂移阈值
            numeric_tolerance: 数值比较容差
        """
        self.default_max_drift = default_max_drift
        self.numeric_tolerance = numeric_tolerance
    
    def detect(
        self,
        expected: Dict[str, Any],
        actual: Dict[str, Any],
        max_drift: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        检测漂移
        
        Args:
            expected: 期望结果
            actual: 实际结果
            max_drift: 最大允许漂移
            
        Returns:
            漂移报告字典
        """
        if max_drift is None:
            max_drift = self.default_max_drift
        
        engine_drifts = {}
        field_diffs = []
        
        # 遍历所有 key
        all_keys = set(expected.keys()) | set(actual.keys())
        
        for key in all_keys:
            exp_val = expected.get(key)
            act_val = actual.get(key)
            
            if key not in expected:
                field_diffs.append({
                    "field": key,
                    "type": "added",
                    "expected": None,
                    "actual": act_val,
                })
                engine_drifts[key] = 1.0
            elif key not in actual:
                field_diffs.append({
                    "field": key,
                    "type": "removed",
                    "expected": exp_val,
                    "actual": None,
                })
                engine_drifts[key] = 1.0
            else:
                # 计算字段漂移
                drift = self._calculate_field_drift(exp_val, act_val)
                engine_drifts[key] = drift
                
                if drift > 0:
                    field_diffs.append({
                        "field": key,
                        "type": "changed",
                        "expected": exp_val,
                        "actual": act_val,
                        "drift": drift,
                    })
        
        # 计算总漂移
        total_drift = self.calculate_drift(expected, actual)
        
        return {
            "total_drift": total_drift,
            "engine_drifts": engine_drifts,
            "field_diffs": field_diffs,
            "passed": total_drift <= max_drift,
            "max_drift": max_drift,
        }
    
    def calculate_drift(
        self,
        expected: Dict[str, Any],
        actual: Dict[str, Any],
    ) -> float:
        """
        计算两个结果之间的总漂移
        
        Args:
            expected: 期望结果
            actual: 实际结果
            
        Returns:
            漂移值 [0, 1]
        """
        if not expected and not actual:
            return 0.0
        if not expected or not actual:
            return 1.0
        
        all_keys = set(expected.keys()) | set(actual.keys())
        if not all_keys:
            return 0.0
        
        total_diff = 0.0
        
        for key in all_keys:
            exp_val = expected.get(key)
            act_val = actual.get(key)
            
            field_drift = self._calculate_field_drift(exp_val, act_val)
            total_diff += field_drift
        
        return total_diff / len(all_keys)
    
    def _calculate_field_drift(
        self,
        expected: Any,
        actual: Any,
    ) -> float:
        """
        计算单个字段的漂移
        
        Returns:
            漂移值 [0, 1]
        """
        if expected == actual:
            return 0.0
        
        if expected is None or actual is None:
            return 1.0
        
        # 数值比较
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            if expected == 0:
                return 1.0 if abs(actual) > self.numeric_tolerance else 0.0
            diff = abs(expected - actual) / max(abs(expected), abs(actual))
            return min(diff, 1.0)
        
        # 列表比较
        if isinstance(expected, list) and isinstance(actual, list):
            return self._calculate_list_drift(expected, actual)
        
        # 字典比较
        if isinstance(expected, dict) and isinstance(actual, dict):
            return self.calculate_drift(expected, actual)
        
        # 字符串或其他类型
        return 0.0 if str(expected) == str(actual) else 1.0
    
    def _calculate_list_drift(
        self,
        expected: List[Any],
        actual: List[Any],
    ) -> float:
        """计算列表漂移"""
        if not expected and not actual:
            return 0.0
        if not expected or not actual:
            return 1.0
        
        # 使用 Jaccard 相似度
        exp_set = set(str(x) for x in expected)
        act_set = set(str(x) for x in actual)
        
        intersection = len(exp_set & act_set)
        union = len(exp_set | act_set)
        
        if union == 0:
            return 0.0
        
        similarity = intersection / union
        return 1.0 - similarity
    
    def to_report(
        self,
        expected: Dict[str, Any],
        actual: Dict[str, Any],
        max_drift: Optional[float] = None,
    ) -> DriftReport:
        """生成漂移报告对象"""
        result = self.detect(expected, actual, max_drift)
        return DriftReport(
            total_drift=result["total_drift"],
            engine_drifts=result["engine_drifts"],
            field_diffs=result["field_diffs"],
            passed=result["passed"],
            max_drift=result["max_drift"],
        )
