# backend/tests/unit/test_memory_async_write.py
"""
R-01/R-02: 记忆写入异步化测试

测试目标：
1. spawn_background 非阻塞行为验证
2. 异常被捕获并记录结构化日志
3. 主流程不等待后台任务
"""

import asyncio
import logging
import time
import pytest
from unittest.mock import MagicMock, AsyncMock, patch

from backend.core.async_utils import spawn_background, create_background_task


class TestSpawnBackgroundNonBlocking:
    """spawn_background 非阻塞行为测试"""
    
    @pytest.mark.asyncio
    async def test_spawn_background_returns_immediately(self):
        """测试：spawn_background 立即返回，不等待协程完成"""
        execution_started = asyncio.Event()
        execution_finished = asyncio.Event()
        
        async def slow_task():
            execution_started.set()
            await asyncio.sleep(0.5)
            execution_finished.set()
        
        start_time = time.perf_counter()
        await spawn_background(slow_task(), name="slow_task", user_id="test_user")
        elapsed = time.perf_counter() - start_time
        
        # spawn_background 应该立即返回（< 50ms）
        assert elapsed < 0.05, f"spawn_background 阻塞了 {elapsed:.3f}s，应该立即返回"
        
        # 等待后台任务开始执行
        await asyncio.sleep(0.1)
        assert execution_started.is_set(), "后台任务应该已经开始执行"
        
        # 此时后台任务应该还在运行
        assert not execution_finished.is_set(), "后台任务应该还在运行"
        
        # 等待后台任务完成
        await asyncio.sleep(0.5)
        assert execution_finished.is_set(), "后台任务应该已完成"
    
    @pytest.mark.asyncio
    async def test_spawn_background_with_slow_service(self):
        """测试：使用慢速 memory service 时主流程不阻塞"""
        async def slow_memory_write():
            await asyncio.sleep(0.3)
            return "written"
        
        start_time = time.perf_counter()
        await spawn_background(
            slow_memory_write(),
            name="memory_write",
            user_id="test_user",
            context={"event_type": "dream_record"},
        )
        elapsed = time.perf_counter() - start_time
        
        # 主流程应该立即返回
        assert elapsed < 0.05, f"主流程被阻塞 {elapsed:.3f}s"


class TestSpawnBackgroundExceptionHandling:
    """spawn_background 异常处理测试"""
    
    @pytest.mark.asyncio
    async def test_exception_logged_with_structured_context(self, caplog):
        """测试：异常被捕获并记录包含完整上下文的日志"""
        caplog.set_level(logging.WARNING)
        
        async def failing_task():
            raise ValueError("Database connection failed")
        
        await spawn_background(
            failing_task(),
            name="record_dream",
            user_id="user_123",
            context={"dream_id": "dream_456", "event_type": "dream_record"},
        )
        
        # 等待后台任务执行完成
        await asyncio.sleep(0.1)
        
        # 验证日志记录
        warning_logs = [r for r in caplog.records if r.levelno >= logging.WARNING]
        assert len(warning_logs) >= 1, "应该记录警告日志"
        
        log_message = warning_logs[0].message
        assert "record_dream" in log_message, "日志应包含任务名称"
        assert "failed" in log_message.lower(), "日志应包含失败信息"
    
    @pytest.mark.asyncio
    async def test_exception_does_not_propagate(self, caplog):
        """测试：后台任务异常不传播到主流程"""
        caplog.set_level(logging.WARNING)
        
        async def exploding_task():
            raise RuntimeError("Kaboom!")
        
        # 记录调用前时间戳
        import time
        start_time = time.perf_counter()
        
        # 不应该抛出异常
        await spawn_background(
            exploding_task(),
            name="exploding",
            user_id="test_user",
        )
        
        # P1-1: 强断言 - spawn_background 必须立即返回（<50ms）
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        assert elapsed_ms < 50, f"spawn_background 应立即返回，实际耗时 {elapsed_ms:.1f}ms"
        
        # 等待后台任务执行
        await asyncio.sleep(0.1)
        
        # P1-1: 强断言 - 异常被日志捕获并包含关键字段
        warning_logs = [r for r in caplog.records if r.levelno >= logging.WARNING]
        assert len(warning_logs) >= 1, "异常应被记录为警告日志"
        assert "exploding" in warning_logs[0].message, "日志应包含任务名称"
        assert "Kaboom" in warning_logs[0].message, "日志应包含异常信息"
    
    @pytest.mark.asyncio
    async def test_multiple_exceptions_all_logged(self, caplog):
        """测试：多个后台任务异常都被记录"""
        caplog.set_level(logging.WARNING)
        
        async def fail_with_message(msg: str):
            raise Exception(msg)
        
        await spawn_background(fail_with_message("Error 1"), name="task_1", user_id="u1")
        await spawn_background(fail_with_message("Error 2"), name="task_2", user_id="u2")
        await spawn_background(fail_with_message("Error 3"), name="task_3", user_id="u3")
        
        await asyncio.sleep(0.1)
        
        warning_logs = [r for r in caplog.records if r.levelno >= logging.WARNING]
        assert len(warning_logs) >= 3, f"应该记录 3 条警告，实际 {len(warning_logs)} 条"


class TestCreateBackgroundTask:
    """create_background_task 测试"""
    
    @pytest.mark.asyncio
    async def test_returns_task_object(self):
        """测试：返回可跟踪的 Task 对象"""
        async def simple_task():
            await asyncio.sleep(0.1)
            return "done"
        
        task = create_background_task(
            simple_task(),
            name="trackable_task",
            user_id="test_user",
        )
        
        assert isinstance(task, asyncio.Task), "应该返回 Task 对象"
        
        # 等待任务完成
        await asyncio.sleep(0.15)
        assert task.done(), "任务应该已完成"
    
    @pytest.mark.asyncio
    async def test_task_exception_handled(self, caplog):
        """测试：Task 异常被处理"""
        caplog.set_level(logging.WARNING)
        
        async def failing():
            raise Exception("Task failed")
        
        task = create_background_task(
            failing(),
            name="failing_task",
            user_id="test_user",
        )
        
        await asyncio.sleep(0.1)
        
        # Task 完成但异常被内部处理
        assert task.done()
        # 日志应该记录
        assert any("failing_task" in r.message for r in caplog.records)
