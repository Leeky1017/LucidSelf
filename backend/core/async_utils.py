# backend/core/async_utils.py
"""
R-02: 统一后台投递器

提供 fire-and-forget 异步任务投递，捕获异常并结构化日志。
"""

import asyncio
import logging
from typing import Any, Coroutine, Optional

logger = logging.getLogger(__name__)


async def spawn_background(
    coro: Coroutine[Any, Any, Any],
    *,
    name: str,
    user_id: Optional[str] = None,
    context: Optional[dict] = None,
) -> None:
    """
    Fire-and-forget 异步任务投递器
    
    - 非阻塞：立即返回，不等待协程完成
    - 异常可观测：捕获异常并记录结构化日志
    - 主流程不受影响
    
    Args:
        coro: 要执行的协程
        name: 任务名称（用于日志）
        user_id: 用户 ID（可选，用于日志）
        context: 额外上下文（可选，用于日志）
    """
    async def _wrapper() -> None:
        try:
            await coro
        except Exception as e:
            log_context = {
                "task_name": name,
                "user_id": user_id,
                "context": context,
                "exception_type": type(e).__name__,
                "exception_message": str(e),
            }
            logger.warning(
                f"Background task '{name}' failed: {e}",
                extra={"structured": log_context},
            )
    
    asyncio.create_task(_wrapper())


def create_background_task(
    coro: Coroutine[Any, Any, Any],
    *,
    name: str,
    user_id: Optional[str] = None,
    context: Optional[dict] = None,
) -> asyncio.Task:
    """
    创建后台任务并返回 Task 对象（用于需要跟踪任务的场景）
    
    与 spawn_background 类似，但返回 Task 对象供调用方跟踪。
    """
    async def _wrapper() -> None:
        try:
            await coro
        except Exception as e:
            log_context = {
                "task_name": name,
                "user_id": user_id,
                "context": context,
                "exception_type": type(e).__name__,
                "exception_message": str(e),
            }
            logger.warning(
                f"Background task '{name}' failed: {e}",
                extra={"structured": log_context},
            )
    
    return asyncio.create_task(_wrapper())
