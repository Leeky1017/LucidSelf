"""
Golden Case Runner

GoldenCase 执行器，用于多引擎集成测试。

对照 design.md §2.2.3 GoldenCaseRunner
对照 Requirements R-6-1-02, R-6-1-09
"""

from __future__ import annotations

import hashlib
import json
import logging
import time
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from backend.core.contracts import GoldenCase
from backend.testing.framework.runner import TestResult, TestRunner
from backend.testing.integration.drift_detector import DriftDetector

if TYPE_CHECKING:
    from backend.rules.engine import RuleEngine

logger = logging.getLogger(__name__)


class GoldenCaseRunner(TestRunner[GoldenCase]):
    """
    黄金用例执行器
    
    对照 design.md §2.2.3 GoldenCaseRunner
    对照 Requirements R-6-1-02, R-6-1-09
    
    用于执行 GoldenCase，验证多引擎集成结果。
    """
    
    def __init__(
        self,
        calculators: Optional[Dict[str, Any]] = None,
        rule_engines: Optional[Dict[str, "RuleEngine"]] = None,
        fusion_engine: Optional[Any] = None,
        name: str = "GoldenCaseRunner",
    ):
        """
        初始化黄金用例执行器
        
        Args:
            calculators: 计算器字典 {engine_id: Calculator}
            rule_engines: 规则引擎字典 {engine_id: RuleEngine}
            fusion_engine: 融合引擎
            name: 执行器名称
        """
        super().__init__(name)
        self.calculators = calculators or {}
        self.rule_engines = rule_engines or {}
        self.fusion_engine = fusion_engine
        self.drift_detector = DriftDetector()
    
    async def run(self, test_case: GoldenCase) -> TestResult:
        """
        执行单个黄金用例
        
        Args:
            test_case: GoldenCase 实例
            
        Returns:
            TestResult: 测试结果
        """
        start_time = time.perf_counter()
        
        try:
            # 1. 执行完整链路
            actual_results = await self._execute_pipeline(test_case.birth_data)
            
            # 2. 漂移检测
            drift_report = self.drift_detector.detect(
                expected=test_case.expected_results,
                actual=actual_results,
            )
            
            # 3. 检查融合结果漂移
            fusion_drift = 0.0
            if test_case.expected_fusion and actual_results.get("fusion"):
                fusion_drift = self.drift_detector.calculate_drift(
                    test_case.expected_fusion,
                    actual_results["fusion"],
                )
            
            # 4. 综合漂移
            total_drift = max(drift_report["total_drift"], fusion_drift)
            passed = total_drift <= test_case.max_drift
            
            duration = (time.perf_counter() - start_time) * 1000
            
            details = {
                "total_drift": total_drift,
                "max_drift": test_case.max_drift,
                "engine_drifts": drift_report["engine_drifts"],
                "fusion_drift": fusion_drift,
                "baseline_hash": test_case.baseline_hash,
                "actual_hash": self._compute_hash(actual_results),
            }
            
            if passed:
                return TestResult.success(
                    test_id=test_case.case_id,
                    duration_ms=duration,
                    details=details,
                    runner_name=self.name,
                )
            else:
                return TestResult.failure(
                    test_id=test_case.case_id,
                    duration_ms=duration,
                    error=f"Drift {total_drift:.2%} exceeds max {test_case.max_drift:.2%}",
                    details=details,
                    runner_name=self.name,
                )
                
        except Exception as e:
            duration = (time.perf_counter() - start_time) * 1000
            logger.error(f"Golden case {test_case.case_id} error: {e}", exc_info=True)
            return TestResult.create_error(
                test_id=test_case.case_id,
                duration_ms=duration,
                error_msg=str(e),
                error_type=type(e).__name__,
                runner_name=self.name,
            )
    
    async def _execute_pipeline(
        self,
        birth_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        执行完整推理链路
        
        Args:
            birth_data: 出生数据
            
        Returns:
            各引擎结果
        """
        results = {}
        
        # 执行各引擎
        for engine_id, calculator in self.calculators.items():
            try:
                # 计算因子
                if hasattr(calculator, "calculate"):
                    factor_matrix = await self._safe_call(
                        calculator.calculate, birth_data
                    )
                else:
                    factor_matrix = None
                
                # 执行规则
                if engine_id in self.rule_engines and factor_matrix:
                    rule_engine = self.rule_engines[engine_id]
                    if hasattr(rule_engine, "execute"):
                        rule_results = rule_engine.execute(factor_matrix)
                        results[f"{engine_id}_rule_engine"] = {
                            "hit_count": sum(
                                1 for r in rule_results 
                                if getattr(r, "hit", False)
                            ),
                            "top_dimensions": self._extract_top_dimensions(rule_results),
                        }
            except Exception as e:
                logger.warning(f"Engine {engine_id} error: {e}")
                results[f"{engine_id}_rule_engine"] = {"error": str(e)}
        
        # 执行融合
        if self.fusion_engine and results:
            try:
                if hasattr(self.fusion_engine, "fuse"):
                    fusion_result = await self._safe_call(
                        self.fusion_engine.fuse, results
                    )
                    results["fusion"] = {
                        "primary_themes": getattr(fusion_result, "themes", []),
                        "cross_validation_score": getattr(
                            fusion_result, "cross_validation_score", 0.0
                        ),
                    }
            except Exception as e:
                logger.warning(f"Fusion error: {e}")
                results["fusion"] = {"error": str(e)}
        
        return results
    
    async def _safe_call(self, func, *args, **kwargs) -> Any:
        """安全调用（支持同步和异步）"""
        import asyncio
        
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return func(*args, **kwargs)
    
    def _extract_top_dimensions(
        self,
        results: List[Any],
        top_n: int = 3,
    ) -> List[str]:
        """提取命中最多的维度"""
        from collections import Counter
        
        dimensions = []
        for r in results:
            if getattr(r, "hit", False):
                dim = getattr(r, "dimension", None)
                if dim:
                    dimensions.append(dim)
        
        counter = Counter(dimensions)
        return [dim for dim, _ in counter.most_common(top_n)]
    
    def _compute_hash(self, data: Dict[str, Any]) -> str:
        """计算结果哈希"""
        content = json.dumps(data, sort_keys=True, default=str)
        return hashlib.sha256(content.encode()).hexdigest()[:16]
