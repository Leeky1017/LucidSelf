"""
Test Runner Base Classes

测试执行器基类，定义三层测试金字塔的通用接口。

对照 design.md §2.2 核心类设计
对照 Requirements R-6-1-01 ~ R-6-1-04
"""

from __future__ import annotations

import asyncio
import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class TestStatus(str, Enum):
    """测试状态"""
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ERROR = "error"


class TestResult(BaseModel):
    """
    测试结果
    
    对照 design.md §2.2.1 TestResult
    """
    test_id: str = Field(..., description="测试用例ID")
    status: TestStatus = Field(..., description="测试状态")
    passed: bool = Field(..., description="是否通过")
    duration_ms: float = Field(..., description="执行时长(毫秒)")
    
    # 详细信息
    details: Dict[str, Any] = Field(default_factory=dict, description="详细结果")
    error: Optional[str] = Field(None, description="错误信息")
    error_type: Optional[str] = Field(None, description="错误类型")
    
    # 元数据
    executed_at: datetime = Field(default_factory=datetime.now, description="执行时间")
    runner_name: str = Field(default="", description="执行器名称")
    
    @classmethod
    def success(
        cls,
        test_id: str,
        duration_ms: float,
        details: Optional[Dict[str, Any]] = None,
        runner_name: str = "",
    ) -> "TestResult":
        """创建成功结果"""
        return cls(
            test_id=test_id,
            status=TestStatus.PASSED,
            passed=True,
            duration_ms=duration_ms,
            details=details or {},
            runner_name=runner_name,
        )
    
    @classmethod
    def failure(
        cls,
        test_id: str,
        duration_ms: float,
        error: str,
        details: Optional[Dict[str, Any]] = None,
        runner_name: str = "",
    ) -> "TestResult":
        """创建失败结果"""
        return cls(
            test_id=test_id,
            status=TestStatus.FAILED,
            passed=False,
            duration_ms=duration_ms,
            error=error,
            details=details or {},
            runner_name=runner_name,
        )
    
    @classmethod
    def create_error(
        cls,
        test_id: str,
        duration_ms: float,
        error_msg: str,
        error_type: str = "Exception",
        runner_name: str = "",
    ) -> "TestResult":
        """创建错误结果"""
        return cls(
            test_id=test_id,
            status=TestStatus.ERROR,
            passed=False,
            duration_ms=duration_ms,
            error=error_msg,
            error_type=error_type,
            runner_name=runner_name,
        )
    
    @classmethod
    def skipped(
        cls,
        test_id: str,
        reason: str = "",
        runner_name: str = "",
    ) -> "TestResult":
        """创建跳过结果"""
        return cls(
            test_id=test_id,
            status=TestStatus.SKIPPED,
            passed=True,  # 跳过不算失败
            duration_ms=0.0,
            details={"skip_reason": reason},
            runner_name=runner_name,
        )


class BatchResult(BaseModel):
    """批量测试结果"""
    results: List[TestResult] = Field(default_factory=list)
    total_duration_ms: float = Field(0.0)
    started_at: datetime = Field(default_factory=datetime.now)
    finished_at: Optional[datetime] = None
    
    @property
    def total(self) -> int:
        return len(self.results)
    
    @property
    def passed_count(self) -> int:
        return sum(1 for r in self.results if r.passed)
    
    @property
    def failed_count(self) -> int:
        return sum(1 for r in self.results if not r.passed and r.status == TestStatus.FAILED)
    
    @property
    def error_count(self) -> int:
        return sum(1 for r in self.results if r.status == TestStatus.ERROR)
    
    @property
    def skipped_count(self) -> int:
        return sum(1 for r in self.results if r.status == TestStatus.SKIPPED)
    
    @property
    def pass_rate(self) -> float:
        if self.total == 0:
            return 0.0
        return self.passed_count / self.total
    
    @property
    def all_passed(self) -> bool:
        return all(r.passed for r in self.results)
    
    def add(self, result: TestResult) -> None:
        self.results.append(result)
    
    def finish(self) -> None:
        self.finished_at = datetime.now()
        self.total_duration_ms = sum(r.duration_ms for r in self.results)


class TestRunner(ABC, Generic[T]):
    """
    测试执行器抽象基类
    
    对照 design.md §2.2.1 TestRunner 基类
    对照 Requirements R-6-1-01 ~ R-6-1-03
    
    类型参数 T: 测试用例类型 (RuleTestCase, GoldenCase, NarrativeGolden)
    """
    
    def __init__(self, name: Optional[str] = None):
        self.name = name or self.__class__.__name__
        self._setup_done = False
    
    async def setup(self) -> None:
        """
        测试前置设置
        
        子类可覆盖此方法进行初始化。
        """
        self._setup_done = True
    
    async def teardown(self) -> None:
        """
        测试后置清理
        
        子类可覆盖此方法进行清理。
        """
        self._setup_done = False
    
    @abstractmethod
    async def run(self, test_case: T) -> TestResult:
        """
        执行单个测试用例
        
        Args:
            test_case: 测试用例
            
        Returns:
            TestResult: 测试结果
        """
        ...
    
    async def run_batch(
        self,
        test_cases: List[T],
        fail_fast: bool = False,
        max_concurrency: int = 1,
    ) -> BatchResult:
        """
        批量执行测试用例
        
        Args:
            test_cases: 测试用例列表
            fail_fast: 遇到失败时是否立即停止
            max_concurrency: 最大并发数 (1=串行)
            
        Returns:
            BatchResult: 批量测试结果
        """
        batch = BatchResult()
        
        if not self._setup_done:
            await self.setup()
        
        try:
            if max_concurrency == 1:
                # 串行执行
                for tc in test_cases:
                    result = await self._run_safe(tc)
                    batch.add(result)
                    
                    if fail_fast and not result.passed:
                        logger.info(f"Fail-fast: stopping after {tc}")
                        break
            else:
                # 并发执行
                semaphore = asyncio.Semaphore(max_concurrency)
                
                async def run_with_semaphore(tc: T) -> TestResult:
                    async with semaphore:
                        return await self._run_safe(tc)
                
                tasks = [run_with_semaphore(tc) for tc in test_cases]
                results = await asyncio.gather(*tasks)
                
                for result in results:
                    batch.add(result)
        finally:
            batch.finish()
        
        return batch
    
    async def _run_safe(self, test_case: T) -> TestResult:
        """安全执行测试，捕获异常"""
        start_time = time.perf_counter()
        test_id = self._get_test_id(test_case)
        
        try:
            result = await self.run(test_case)
            result.runner_name = self.name
            return result
        except AssertionError as e:
            duration = (time.perf_counter() - start_time) * 1000
            logger.warning(f"Test {test_id} assertion failed: {e}")
            return TestResult.failure(
                test_id=test_id,
                duration_ms=duration,
                error=str(e),
                runner_name=self.name,
            )
        except Exception as e:
            duration = (time.perf_counter() - start_time) * 1000
            logger.error(f"Test {test_id} error: {e}", exc_info=True)
            return TestResult.create_error(
                test_id=test_id,
                duration_ms=duration,
                error_msg=str(e),
                error_type=type(e).__name__,
                runner_name=self.name,
            )
    
    def _get_test_id(self, test_case: T) -> str:
        """从测试用例获取ID"""
        # 尝试常见的 ID 字段名
        for field in ["test_id", "case_id", "golden_id", "id"]:
            if hasattr(test_case, field):
                return getattr(test_case, field)
        return str(id(test_case))
