"""
Testing Assertions Library

测试断言库，提供三层测试金字塔的专用断言方法。

对照 design.md §2.3 断言库设计
对照 Requirements R-6-1-05 ~ R-6-1-08
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union


@dataclass
class AssertionDiff:
    """断言差异详情"""
    field: str
    expected: Any
    actual: Any
    message: str


class AssertionError(Exception):
    """断言失败异常"""
    
    def __init__(
        self,
        message: str,
        diffs: Optional[List[AssertionDiff]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.diffs = diffs or []
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "diffs": [
                {
                    "field": d.field,
                    "expected": d.expected,
                    "actual": d.actual,
                    "message": d.message,
                }
                for d in self.diffs
            ],
        }


class RuleAssertions:
    """
    规则断言
    
    对照 Requirements R-6-1-05
    用于验证规则命中结果。
    """
    
    @staticmethod
    def assert_rule_hit(
        result: Any,
        expected_hit: bool = True,
        expected_dimension: Optional[str] = None,
        expected_level: Optional[str] = None,
        confidence_range: Tuple[float, float] = (0.0, 1.0),
    ) -> None:
        """
        断言规则命中
        
        Args:
            result: RuntimeRuleResult 或具有相应属性的对象
            expected_hit: 是否期望命中
            expected_dimension: 期望维度
            expected_level: 期望等级
            confidence_range: 置信度范围 (min, max)
            
        Raises:
            AssertionError: 断言失败
        """
        diffs: List[AssertionDiff] = []
        
        # 检查命中状态
        actual_hit = getattr(result, "hit", None)
        if actual_hit is None:
            actual_hit = getattr(result, "matched", None)
        
        if actual_hit != expected_hit:
            diffs.append(AssertionDiff(
                field="hit",
                expected=expected_hit,
                actual=actual_hit,
                message=f"Expected hit={expected_hit}, got {actual_hit}",
            ))
        
        # 仅在期望命中时检查其他字段
        if expected_hit and actual_hit:
            # 检查维度
            if expected_dimension is not None:
                actual_dim = getattr(result, "dimension", None)
                if actual_dim != expected_dimension:
                    diffs.append(AssertionDiff(
                        field="dimension",
                        expected=expected_dimension,
                        actual=actual_dim,
                        message=f"Expected dimension={expected_dimension}, got {actual_dim}",
                    ))
            
            # 检查等级
            if expected_level is not None:
                actual_level = getattr(result, "level", None)
                if actual_level != expected_level:
                    diffs.append(AssertionDiff(
                        field="level",
                        expected=expected_level,
                        actual=actual_level,
                        message=f"Expected level={expected_level}, got {actual_level}",
                    ))
            
            # 检查置信度
            actual_conf = getattr(result, "confidence", None)
            if actual_conf is not None:
                min_conf, max_conf = confidence_range
                if not (min_conf <= actual_conf <= max_conf):
                    diffs.append(AssertionDiff(
                        field="confidence",
                        expected=f"[{min_conf}, {max_conf}]",
                        actual=actual_conf,
                        message=f"Expected confidence in [{min_conf}, {max_conf}], got {actual_conf}",
                    ))
        
        if diffs:
            raise AssertionError(
                f"Rule assertion failed with {len(diffs)} difference(s)",
                diffs=diffs,
            )
    
    @staticmethod
    def assert_rule_not_hit(result: Any) -> None:
        """断言规则未命中"""
        RuleAssertions.assert_rule_hit(result, expected_hit=False)
    
    @staticmethod
    def assert_hit_count(
        results: List[Any],
        expected_count: int,
        tolerance: int = 0,
    ) -> None:
        """
        断言命中规则数量
        
        Args:
            results: 规则结果列表
            expected_count: 期望命中数量
            tolerance: 允许的误差范围
        """
        actual_count = sum(
            1 for r in results 
            if getattr(r, "hit", False) or getattr(r, "matched", False)
        )
        
        if abs(actual_count - expected_count) > tolerance:
            raise AssertionError(
                f"Expected {expected_count}±{tolerance} hits, got {actual_count}",
                diffs=[AssertionDiff(
                    field="hit_count",
                    expected=f"{expected_count}±{tolerance}",
                    actual=actual_count,
                    message=f"Hit count mismatch",
                )],
            )


class FusionAssertions:
    """
    融合断言
    
    对照 Requirements R-6-1-06
    用于验证 FusionResult。
    """
    
    @staticmethod
    def assert_fusion_result(
        result: Any,
        expected_themes: Optional[List[str]] = None,
        forbidden_themes: Optional[List[str]] = None,
        min_cross_validation: float = 0.0,
        max_drift: float = 1.0,
    ) -> None:
        """
        断言融合结果
        
        Args:
            result: FusionResult 或具有相应属性的对象
            expected_themes: 必须包含的主题
            forbidden_themes: 不能包含的主题
            min_cross_validation: 最低交叉验证分数
            max_drift: 最大允许漂移
            
        Raises:
            AssertionError: 断言失败
        """
        diffs: List[AssertionDiff] = []
        
        # 获取实际主题
        actual_themes = getattr(result, "themes", [])
        if not isinstance(actual_themes, list):
            actual_themes = list(actual_themes) if actual_themes else []
        
        # 检查必须包含的主题
        if expected_themes:
            missing = [t for t in expected_themes if t not in actual_themes]
            if missing:
                diffs.append(AssertionDiff(
                    field="themes",
                    expected=expected_themes,
                    actual=actual_themes,
                    message=f"Missing themes: {missing}",
                ))
        
        # 检查不能包含的主题
        if forbidden_themes:
            found = [t for t in forbidden_themes if t in actual_themes]
            if found:
                diffs.append(AssertionDiff(
                    field="themes",
                    expected=f"not {forbidden_themes}",
                    actual=actual_themes,
                    message=f"Forbidden themes found: {found}",
                ))
        
        # 检查交叉验证分数
        actual_score = getattr(result, "cross_validation_score", None)
        if actual_score is not None and actual_score < min_cross_validation:
            diffs.append(AssertionDiff(
                field="cross_validation_score",
                expected=f">= {min_cross_validation}",
                actual=actual_score,
                message=f"Cross validation score too low",
            ))
        
        if diffs:
            raise AssertionError(
                f"Fusion assertion failed with {len(diffs)} difference(s)",
                diffs=diffs,
            )
    
    @staticmethod
    def assert_drift(
        expected: Dict[str, Any],
        actual: Dict[str, Any],
        max_drift: float = 0.1,
    ) -> float:
        """
        断言漂移在允许范围内
        
        Args:
            expected: 期望结果
            actual: 实际结果
            max_drift: 最大允许漂移 (0.1 = 10%)
            
        Returns:
            float: 实际漂移值
            
        Raises:
            AssertionError: 漂移超过阈值
        """
        drift = FusionAssertions._calculate_drift(expected, actual)
        
        if drift > max_drift:
            raise AssertionError(
                f"Drift {drift:.2%} exceeds max {max_drift:.2%}",
                diffs=[AssertionDiff(
                    field="drift",
                    expected=f"<= {max_drift:.2%}",
                    actual=f"{drift:.2%}",
                    message=f"Result drifted beyond threshold",
                )],
            )
        
        return drift
    
    @staticmethod
    def _calculate_drift(
        expected: Dict[str, Any],
        actual: Dict[str, Any],
    ) -> float:
        """计算两个结果之间的漂移"""
        if not expected and not actual:
            return 0.0
        if not expected or not actual:
            return 1.0
        
        all_keys = set(expected.keys()) | set(actual.keys())
        if not all_keys:
            return 0.0
        
        diff_count = 0
        for key in all_keys:
            exp_val = expected.get(key)
            act_val = actual.get(key)
            
            if exp_val != act_val:
                diff_count += 1
        
        return diff_count / len(all_keys)


class NarrativeAssertions:
    """
    叙事断言
    
    对照 Requirements R-6-1-07
    用于验证 NarrativeGolden。
    """
    
    @staticmethod
    def assert_narrative_quality(
        narrative: str,
        must_include_themes: Optional[List[str]] = None,
        forbidden_expressions: Optional[List[str]] = None,
        min_length: int = 0,
        max_length: Optional[int] = None,
    ) -> None:
        """
        断言叙事质量
        
        Args:
            narrative: 叙事文本
            must_include_themes: 必须包含的主题关键字
            forbidden_expressions: 禁用的表述
            min_length: 最小长度
            max_length: 最大长度
            
        Raises:
            AssertionError: 断言失败
        """
        diffs: List[AssertionDiff] = []
        
        # 检查长度
        actual_len = len(narrative)
        if actual_len < min_length:
            diffs.append(AssertionDiff(
                field="length",
                expected=f">= {min_length}",
                actual=actual_len,
                message=f"Narrative too short",
            ))
        
        if max_length is not None and actual_len > max_length:
            diffs.append(AssertionDiff(
                field="length",
                expected=f"<= {max_length}",
                actual=actual_len,
                message=f"Narrative too long",
            ))
        
        # 检查必须包含的主题
        if must_include_themes:
            missing = [t for t in must_include_themes if t not in narrative]
            if missing:
                diffs.append(AssertionDiff(
                    field="themes",
                    expected=must_include_themes,
                    actual="[not found]",
                    message=f"Missing themes: {missing}",
                ))
        
        # 检查禁用表述
        if forbidden_expressions:
            found = [e for e in forbidden_expressions if e in narrative]
            if found:
                diffs.append(AssertionDiff(
                    field="expressions",
                    expected=f"not {forbidden_expressions}",
                    actual=found,
                    message=f"Forbidden expressions found: {found}",
                ))
        
        if diffs:
            raise AssertionError(
                f"Narrative assertion failed with {len(diffs)} difference(s)",
                diffs=diffs,
            )
    
    @staticmethod
    def assert_quality_score(
        score: float,
        min_score: float = 0.8,
        historical_avg: Optional[float] = None,
    ) -> None:
        """
        断言质量评分
        
        Args:
            score: 实际评分
            min_score: 最低分数
            historical_avg: 历史平均分 (如提供，不能低于此值)
        """
        diffs: List[AssertionDiff] = []
        
        if score < min_score:
            diffs.append(AssertionDiff(
                field="quality_score",
                expected=f">= {min_score}",
                actual=score,
                message=f"Quality score below minimum",
            ))
        
        if historical_avg is not None and score < historical_avg:
            diffs.append(AssertionDiff(
                field="quality_score",
                expected=f">= {historical_avg} (historical avg)",
                actual=score,
                message=f"Quality score below historical average",
            ))
        
        if diffs:
            raise AssertionError(
                f"Quality score assertion failed",
                diffs=diffs,
            )


# 便捷函数
def assert_rule_hit(result: Any, **kwargs) -> None:
    """便捷函数：断言规则命中"""
    RuleAssertions.assert_rule_hit(result, **kwargs)


def assert_fusion_result(result: Any, **kwargs) -> None:
    """便捷函数：断言融合结果"""
    FusionAssertions.assert_fusion_result(result, **kwargs)


def assert_narrative_quality(narrative: str, **kwargs) -> None:
    """便捷函数：断言叙事质量"""
    NarrativeAssertions.assert_narrative_quality(narrative, **kwargs)
