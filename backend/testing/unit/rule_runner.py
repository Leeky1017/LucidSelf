"""
Rule Test Runner

RuleTestCase 执行器，用于单条规则测试。

对照 design.md §2.2.2 RuleTestRunner
对照 Requirements R-6-1-01, R-6-1-05
"""

from __future__ import annotations

import logging
import time
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from backend.core.contracts import FactorMatrix, RuleTestCase
from backend.testing.framework.assertions import RuleAssertions
from backend.testing.framework.runner import TestResult, TestRunner, TestStatus

if TYPE_CHECKING:
    from backend.rules.engine import RuleEngine

logger = logging.getLogger(__name__)


class RuleTestRunner(TestRunner[RuleTestCase]):
    """
    规则测试执行器
    
    对照 design.md §2.2.2 RuleTestRunner
    对照 Requirements R-6-1-01, R-6-1-05
    
    用于执行 RuleTestCase，验证单条规则的匹配逻辑。
    """
    
    def __init__(
        self,
        rule_engine: Optional["RuleEngine"] = None,
        name: str = "RuleTestRunner",
    ):
        """
        初始化规则测试执行器
        
        Args:
            rule_engine: 规则引擎实例 (如不提供则懒加载)
            name: 执行器名称
        """
        super().__init__(name)
        self._rule_engine = rule_engine
    
    @property
    def rule_engine(self) -> "RuleEngine":
        """获取规则引擎"""
        if self._rule_engine is None:
            from backend.rules.engine import RuleEngine
            self._rule_engine = RuleEngine()
        return self._rule_engine
    
    async def run(self, test_case: RuleTestCase) -> TestResult:
        """
        执行单个规则测试用例
        
        Args:
            test_case: RuleTestCase 实例
            
        Returns:
            TestResult: 测试结果
        """
        start_time = time.perf_counter()
        
        try:
            # 1. 构建 FactorMatrix
            factor_matrix = self._build_factor_matrix(test_case)
            
            # 2. 执行目标规则
            result = await self._execute_rule(
                test_case.target_rule_id,
                factor_matrix,
            )
            
            # 3. 验证结果
            validation = self._validate_result(test_case, result)
            
            duration = (time.perf_counter() - start_time) * 1000
            
            if validation["passed"]:
                return TestResult.success(
                    test_id=test_case.test_id,
                    duration_ms=duration,
                    details=validation["details"],
                    runner_name=self.name,
                )
            else:
                return TestResult.failure(
                    test_id=test_case.test_id,
                    duration_ms=duration,
                    error=validation["error"],
                    details=validation["details"],
                    runner_name=self.name,
                )
                
        except Exception as e:
            duration = (time.perf_counter() - start_time) * 1000
            logger.error(f"Rule test {test_case.test_id} error: {e}", exc_info=True)
            return TestResult.create_error(
                test_id=test_case.test_id,
                duration_ms=duration,
                error_msg=str(e),
                error_type=type(e).__name__,
                runner_name=self.name,
            )
    
    def _build_factor_matrix(self, test_case: RuleTestCase) -> FactorMatrix:
        """
        从测试用例构建 FactorMatrix
        
        Args:
            test_case: 测试用例
            
        Returns:
            FactorMatrix
        """
        # 从 target_rule_id 推断 engine_id
        engine_id = self._infer_engine_id(test_case.target_rule_id)
        
        return FactorMatrix(
            engine_id=engine_id,
            factors=test_case.mock_factors,
            computed_at=datetime.now(),
            source="rule_test_runner",
        )
    
    def _infer_engine_id(self, rule_id: str) -> str:
        """从规则ID推断引擎ID"""
        # 规则ID格式: {book_prefix}_{content}_{seq}
        # 例如: dts_jia_spring_001 -> bazi
        prefix_map = {
            "dts": "bazi",  # 滴天髓
            "qptbj": "bazi",  # 穷通宝鉴
            "smth": "bazi",  # 三命通会
            "ziwei": "ziwei",
            "zw": "ziwei",
            "astro": "astro",
            "tarot": "tarot",
            "dream": "dream",
            "yijing": "yijing",
        }
        
        for prefix, engine in prefix_map.items():
            if rule_id.lower().startswith(prefix):
                return engine
        
        # 默认
        return "bazi"
    
    async def _execute_rule(
        self,
        rule_id: str,
        factor_matrix: FactorMatrix,
    ) -> Any:
        """
        执行单条规则
        
        Args:
            rule_id: 规则ID
            factor_matrix: 因子矩阵
            
        Returns:
            规则执行结果
        """
        # 调用规则引擎
        if hasattr(self.rule_engine, "execute_single"):
            return self.rule_engine.execute_single(rule_id, factor_matrix)
        elif hasattr(self.rule_engine, "execute"):
            results = self.rule_engine.execute(factor_matrix)
            # 从结果中找到目标规则
            for r in results:
                if getattr(r, "rule_id", None) == rule_id:
                    return r
            # 未找到，返回未命中结果
            return type("MockResult", (), {"hit": False, "rule_id": rule_id})()
        else:
            raise RuntimeError("RuleEngine does not have execute_single or execute method")
    
    def _validate_result(
        self,
        test_case: RuleTestCase,
        result: Any,
    ) -> Dict[str, Any]:
        """
        验证规则执行结果
        
        Args:
            test_case: 测试用例
            result: 规则执行结果
            
        Returns:
            验证结果字典
        """
        details = {
            "target_rule_id": test_case.target_rule_id,
            "test_type": test_case.test_type,
            "expected_hit": test_case.expect_hit,
            "actual_hit": getattr(result, "hit", None),
        }
        
        # 检查命中状态
        actual_hit = getattr(result, "hit", False)
        if actual_hit != test_case.expect_hit:
            return {
                "passed": False,
                "error": f"Expected hit={test_case.expect_hit}, got {actual_hit}",
                "details": details,
            }
        
        # 如果期望命中，检查其他字段
        if test_case.expect_hit and actual_hit:
            # 检查维度
            if test_case.expected_dimension:
                actual_dim = getattr(result, "dimension", None)
                if actual_dim != test_case.expected_dimension:
                    details["expected_dimension"] = test_case.expected_dimension
                    details["actual_dimension"] = actual_dim
                    return {
                        "passed": False,
                        "error": f"Expected dimension={test_case.expected_dimension}, got {actual_dim}",
                        "details": details,
                    }
            
            # 检查等级
            if test_case.expected_level:
                actual_level = getattr(result, "level", None)
                if actual_level != test_case.expected_level:
                    details["expected_level"] = test_case.expected_level
                    details["actual_level"] = actual_level
                    return {
                        "passed": False,
                        "error": f"Expected level={test_case.expected_level}, got {actual_level}",
                        "details": details,
                    }
            
            # 检查置信度
            actual_conf = getattr(result, "confidence", None)
            if actual_conf is not None:
                min_conf = test_case.expected_confidence_min
                max_conf = test_case.expected_confidence_max
                if not (min_conf <= actual_conf <= max_conf):
                    details["expected_confidence_range"] = [min_conf, max_conf]
                    details["actual_confidence"] = actual_conf
                    return {
                        "passed": False,
                        "error": f"Expected confidence in [{min_conf}, {max_conf}], got {actual_conf}",
                        "details": details,
                    }
        
        # 所有检查通过
        details["actual_dimension"] = getattr(result, "dimension", None)
        details["actual_level"] = getattr(result, "level", None)
        details["actual_confidence"] = getattr(result, "confidence", None)
        
        return {
            "passed": True,
            "error": None,
            "details": details,
        }
