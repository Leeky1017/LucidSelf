"""
Health Checker

健康检查模块。

对照 design.md §7.2 健康检查
对照 Requirements R-6-4-04, R-6-4-05
"""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


class HealthStatus(str, Enum):
    """健康状态"""
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"
    UNKNOWN = "unknown"


@dataclass
class HealthCheckResult:
    """健康检查结果"""
    name: str
    status: HealthStatus
    duration_ms: float
    message: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)
    checked_at: datetime = field(default_factory=datetime.now)


@dataclass
class OverallHealth:
    """整体健康状态"""
    status: HealthStatus
    checks: List[HealthCheckResult]
    healthy_count: int
    unhealthy_count: int
    degraded_count: int


class HealthChecker:
    """
    健康检查器
    
    对照 R-6-4-04: 多维度健康检查
    对照 R-6-4-05: 自动恢复触发
    """
    
    def __init__(
        self,
        check_interval_seconds: float = 10.0,
        unhealthy_threshold: int = 3,
        recovery_callback: Optional[Callable[[], None]] = None,
    ):
        """
        初始化健康检查器
        
        Args:
            check_interval_seconds: 检查间隔秒数
            unhealthy_threshold: 连续不健康次数阈值（触发恢复）
            recovery_callback: 恢复回调函数
        """
        self._check_interval = check_interval_seconds
        self._unhealthy_threshold = unhealthy_threshold
        self._recovery_callback = recovery_callback
        
        self._checks: Dict[str, Callable[[], HealthCheckResult]] = {}
        self._last_results: Dict[str, HealthCheckResult] = {}
        self._unhealthy_counts: Dict[str, int] = {}
        
        self._running = False
        self._task = None
    
    def register_check(
        self,
        name: str,
        check_fn: Callable[[], HealthCheckResult],
    ) -> None:
        """
        注册健康检查
        
        Args:
            name: 检查名称
            check_fn: 检查函数
        """
        self._checks[name] = check_fn
        self._unhealthy_counts[name] = 0
        logger.info(f"Registered health check: {name}")
    
    def unregister_check(self, name: str) -> bool:
        """取消注册健康检查"""
        if name in self._checks:
            del self._checks[name]
            self._unhealthy_counts.pop(name, None)
            self._last_results.pop(name, None)
            return True
        return False
    
    def run_check(self, name: str) -> Optional[HealthCheckResult]:
        """
        运行单个健康检查
        
        Args:
            name: 检查名称
            
        Returns:
            检查结果
        """
        if name not in self._checks:
            return None
        
        start_time = time.perf_counter()
        
        try:
            result = self._checks[name]()
        except Exception as e:
            result = HealthCheckResult(
                name=name,
                status=HealthStatus.UNHEALTHY,
                duration_ms=(time.perf_counter() - start_time) * 1000,
                message=str(e),
            )
        
        self._last_results[name] = result
        self._update_unhealthy_count(name, result.status)
        
        return result
    
    def run_all_checks(self) -> OverallHealth:
        """
        运行所有健康检查
        
        Returns:
            整体健康状态
        """
        results = []
        healthy_count = 0
        unhealthy_count = 0
        degraded_count = 0
        
        for name in self._checks:
            result = self.run_check(name)
            if result:
                results.append(result)
                
                if result.status == HealthStatus.HEALTHY:
                    healthy_count += 1
                elif result.status == HealthStatus.UNHEALTHY:
                    unhealthy_count += 1
                elif result.status == HealthStatus.DEGRADED:
                    degraded_count += 1
        
        # 确定整体状态
        if unhealthy_count > 0:
            overall_status = HealthStatus.UNHEALTHY
        elif degraded_count > 0:
            overall_status = HealthStatus.DEGRADED
        elif healthy_count > 0:
            overall_status = HealthStatus.HEALTHY
        else:
            overall_status = HealthStatus.UNKNOWN
        
        return OverallHealth(
            status=overall_status,
            checks=results,
            healthy_count=healthy_count,
            unhealthy_count=unhealthy_count,
            degraded_count=degraded_count,
        )
    
    def get_last_result(self, name: str) -> Optional[HealthCheckResult]:
        """获取最后一次检查结果"""
        return self._last_results.get(name)
    
    def get_all_last_results(self) -> Dict[str, HealthCheckResult]:
        """获取所有最后检查结果"""
        return self._last_results.copy()
    
    def _update_unhealthy_count(self, name: str, status: HealthStatus) -> None:
        """更新不健康计数"""
        if status == HealthStatus.UNHEALTHY:
            self._unhealthy_counts[name] = self._unhealthy_counts.get(name, 0) + 1
            
            # 检查是否触发恢复
            if self._unhealthy_counts[name] >= self._unhealthy_threshold:
                logger.warning(
                    f"Health check {name} unhealthy {self._unhealthy_counts[name]} times, "
                    "triggering recovery"
                )
                if self._recovery_callback:
                    try:
                        self._recovery_callback()
                    except Exception as e:
                        logger.error(f"Recovery callback failed: {e}")
                
                self._unhealthy_counts[name] = 0
        else:
            # 重置计数
            self._unhealthy_counts[name] = 0


# =============================================================================
# 预定义健康检查
# =============================================================================

def create_database_check(connection_fn: Callable[[], bool]) -> Callable[[], HealthCheckResult]:
    """创建数据库健康检查"""
    def check() -> HealthCheckResult:
        start_time = time.perf_counter()
        try:
            healthy = connection_fn()
            return HealthCheckResult(
                name="database",
                status=HealthStatus.HEALTHY if healthy else HealthStatus.UNHEALTHY,
                duration_ms=(time.perf_counter() - start_time) * 1000,
            )
        except Exception as e:
            return HealthCheckResult(
                name="database",
                status=HealthStatus.UNHEALTHY,
                duration_ms=(time.perf_counter() - start_time) * 1000,
                message=str(e),
            )
    return check


def create_redis_check(ping_fn: Callable[[], bool]) -> Callable[[], HealthCheckResult]:
    """创建 Redis 健康检查"""
    def check() -> HealthCheckResult:
        start_time = time.perf_counter()
        try:
            healthy = ping_fn()
            return HealthCheckResult(
                name="redis",
                status=HealthStatus.HEALTHY if healthy else HealthStatus.UNHEALTHY,
                duration_ms=(time.perf_counter() - start_time) * 1000,
            )
        except Exception as e:
            return HealthCheckResult(
                name="redis",
                status=HealthStatus.UNHEALTHY,
                duration_ms=(time.perf_counter() - start_time) * 1000,
                message=str(e),
            )
    return check


def create_memory_check(threshold_percent: float = 90.0) -> Callable[[], HealthCheckResult]:
    """创建内存健康检查"""
    def check() -> HealthCheckResult:
        start_time = time.perf_counter()
        try:
            import psutil
            memory = psutil.virtual_memory()
            used_percent = memory.percent
            
            if used_percent > threshold_percent:
                status = HealthStatus.UNHEALTHY
            elif used_percent > threshold_percent * 0.8:
                status = HealthStatus.DEGRADED
            else:
                status = HealthStatus.HEALTHY
            
            return HealthCheckResult(
                name="memory",
                status=status,
                duration_ms=(time.perf_counter() - start_time) * 1000,
                details={"used_percent": used_percent},
            )
        except ImportError:
            return HealthCheckResult(
                name="memory",
                status=HealthStatus.UNKNOWN,
                duration_ms=(time.perf_counter() - start_time) * 1000,
                message="psutil not installed",
            )
    return check
