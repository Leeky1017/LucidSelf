"""
Graceful Shutdown

优雅关闭模块。

对照 design.md §7.3 优雅关闭
对照 Requirements R-6-4-06, R-6-4-07, R-6-4-08
"""

from __future__ import annotations

import asyncio
import logging
import signal
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, List, Optional

logger = logging.getLogger(__name__)


class ShutdownPhase(str, Enum):
    """关闭阶段"""
    RUNNING = "running"
    DRAINING = "draining"      # 排空请求
    TERMINATING = "terminating"  # 终止处理
    STOPPED = "stopped"


@dataclass
class ShutdownHook:
    """关闭钩子"""
    name: str
    callback: Callable[[], None]
    priority: int = 0  # 优先级，数字越小越先执行
    timeout_seconds: float = 10.0


@dataclass
class ShutdownResult:
    """关闭结果"""
    success: bool
    phase: ShutdownPhase
    duration_ms: float
    hooks_executed: List[str]
    hooks_failed: List[str]


class GracefulShutdown:
    """
    优雅关闭管理器
    
    对照 R-6-4-06: 请求排空
    对照 R-6-4-07: 关闭钩子
    对照 R-6-4-08: 超时强制终止
    """
    
    def __init__(
        self,
        drain_timeout_seconds: float = 30.0,
        force_timeout_seconds: float = 60.0,
        register_signals: bool = True,
    ):
        """
        初始化优雅关闭管理器
        
        Args:
            drain_timeout_seconds: 排空超时秒数
            force_timeout_seconds: 强制终止超时秒数
            register_signals: 是否注册信号处理
        """
        self._drain_timeout = drain_timeout_seconds
        self._force_timeout = force_timeout_seconds
        
        self._phase = ShutdownPhase.RUNNING
        self._hooks: List[ShutdownHook] = []
        self._active_requests = 0
        self._lock = threading.RLock()
        
        self._shutdown_event = threading.Event()
        self._drain_complete = threading.Event()
        
        if register_signals:
            self._register_signal_handlers()
    
    @property
    def phase(self) -> ShutdownPhase:
        """获取当前阶段"""
        return self._phase
    
    @property
    def is_shutting_down(self) -> bool:
        """是否正在关闭"""
        return self._phase != ShutdownPhase.RUNNING
    
    @property
    def active_requests(self) -> int:
        """获取活跃请求数"""
        return self._active_requests
    
    def register_hook(
        self,
        name: str,
        callback: Callable[[], None],
        priority: int = 0,
        timeout_seconds: float = 10.0,
    ) -> None:
        """
        注册关闭钩子
        
        对照 R-6-4-07
        """
        hook = ShutdownHook(
            name=name,
            callback=callback,
            priority=priority,
            timeout_seconds=timeout_seconds,
        )
        
        with self._lock:
            self._hooks.append(hook)
            # 按优先级排序
            self._hooks.sort(key=lambda h: h.priority)
        
        logger.info(f"Registered shutdown hook: {name} (priority={priority})")
    
    def unregister_hook(self, name: str) -> bool:
        """取消注册关闭钩子"""
        with self._lock:
            for i, hook in enumerate(self._hooks):
                if hook.name == name:
                    self._hooks.pop(i)
                    return True
        return False
    
    def request_start(self) -> bool:
        """
        标记请求开始
        
        Returns:
            True 如果请求被接受，False 如果正在关闭
        """
        with self._lock:
            if self._phase != ShutdownPhase.RUNNING:
                return False
            self._active_requests += 1
            return True
    
    def request_end(self) -> None:
        """标记请求结束"""
        with self._lock:
            self._active_requests = max(0, self._active_requests - 1)
            
            if self._phase == ShutdownPhase.DRAINING and self._active_requests == 0:
                self._drain_complete.set()
    
    def shutdown(self) -> ShutdownResult:
        """
        执行优雅关闭
        
        对照 R-6-4-06, R-6-4-07, R-6-4-08
        """
        start_time = time.perf_counter()
        hooks_executed = []
        hooks_failed = []
        
        # Phase 1: 开始排空
        with self._lock:
            self._phase = ShutdownPhase.DRAINING
        
        logger.info(f"Starting graceful shutdown (active requests: {self._active_requests})")
        
        # 等待请求排空
        if self._active_requests > 0:
            drain_success = self._drain_complete.wait(timeout=self._drain_timeout)
            if not drain_success:
                logger.warning(
                    f"Drain timeout, {self._active_requests} requests still active"
                )
        
        # Phase 2: 执行关闭钩子
        with self._lock:
            self._phase = ShutdownPhase.TERMINATING
        
        for hook in self._hooks:
            try:
                logger.info(f"Executing shutdown hook: {hook.name}")
                
                # 使用线程执行带超时
                thread = threading.Thread(target=hook.callback)
                thread.start()
                thread.join(timeout=hook.timeout_seconds)
                
                if thread.is_alive():
                    logger.warning(f"Hook {hook.name} timed out")
                    hooks_failed.append(hook.name)
                else:
                    hooks_executed.append(hook.name)
                    
            except Exception as e:
                logger.error(f"Hook {hook.name} failed: {e}")
                hooks_failed.append(hook.name)
        
        # Phase 3: 完成
        with self._lock:
            self._phase = ShutdownPhase.STOPPED
        
        self._shutdown_event.set()
        
        duration_ms = (time.perf_counter() - start_time) * 1000
        
        result = ShutdownResult(
            success=len(hooks_failed) == 0,
            phase=ShutdownPhase.STOPPED,
            duration_ms=duration_ms,
            hooks_executed=hooks_executed,
            hooks_failed=hooks_failed,
        )
        
        logger.info(
            f"Shutdown complete: {len(hooks_executed)} hooks executed, "
            f"{len(hooks_failed)} failed ({duration_ms:.2f}ms)"
        )
        
        return result
    
    def wait_for_shutdown(self, timeout: Optional[float] = None) -> bool:
        """
        等待关闭完成
        
        Returns:
            True 如果关闭完成
        """
        return self._shutdown_event.wait(timeout=timeout)
    
    def _register_signal_handlers(self) -> None:
        """注册信号处理器"""
        try:
            signal.signal(signal.SIGTERM, self._signal_handler)
            signal.signal(signal.SIGINT, self._signal_handler)
            logger.info("Registered signal handlers (SIGTERM, SIGINT)")
        except Exception as e:
            logger.warning(f"Failed to register signal handlers: {e}")
    
    def _signal_handler(self, signum: int, frame: Any) -> None:
        """信号处理器"""
        sig_name = signal.Signals(signum).name
        logger.info(f"Received signal {sig_name}, initiating shutdown")
        
        # 在新线程中执行关闭，避免阻塞信号处理
        thread = threading.Thread(target=self.shutdown)
        thread.start()


class RequestGuard:
    """
    请求守卫上下文管理器
    
    用于自动管理请求生命周期。
    """
    
    def __init__(self, shutdown_manager: GracefulShutdown):
        self._manager = shutdown_manager
        self._accepted = False
    
    def __enter__(self) -> bool:
        self._accepted = self._manager.request_start()
        return self._accepted
    
    def __exit__(self, *args) -> None:
        if self._accepted:
            self._manager.request_end()
