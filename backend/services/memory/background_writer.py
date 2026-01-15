# backend/services/memory/background_writer.py
"""
P0-1: 后台记忆写入器

将所有 MemoryService 写入逻辑从 routes 移到服务层，
确保 routes 目录下无 await memory_service 调用。
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional

from backend.models.memory import PrivacyLevel
from backend.services.memory import get_memory_service

logger = logging.getLogger(__name__)


async def _execute_memory_write(
    write_fn: str,
    user_id: str,
    context_name: str,
    **kwargs: Any,
) -> Optional[str]:
    """
    执行 MemoryService 写入操作
    
    Returns:
        event_id 或 insight_id（如果成功），None（如果失败）
    """
    try:
        memory_service = get_memory_service()
        if write_fn == "record_event":
            result = await memory_service.record_event(
                user_id=user_id,
                **kwargs,
            )
            logger.debug(f"Memory event recorded: context={context_name}, user={user_id}")
            return result
        elif write_fn == "create_insight":
            result = await memory_service.create_insight(
                user_id=user_id,
                **kwargs,
            )
            logger.debug(f"Memory insight created: context={context_name}, user={user_id}")
            return result
    except Exception as e:
        logger.warning(
            f"Background memory write failed: context={context_name}, user={user_id}, error={e}",
            extra={
                "structured": {
                    "context_name": context_name,
                    "user_id": user_id,
                    "write_fn": write_fn,
                    "exception_type": type(e).__name__,
                    "exception_message": str(e),
                }
            },
        )
    return None


# =============================================================================
# TODO 模块后台写入
# =============================================================================

async def record_todo_event(
    user_id: str,
    todo_id: str,
    content: str,
    entry_type: str,
) -> None:
    """记录 TODO 事件到 MemoryService"""
    await _execute_memory_write(
        write_fn="record_event",
        user_id=user_id,
        context_name="todo_event",
        event_type="todo_entry",
        data={
            "todo_id": todo_id,
            "content": content,
            "entry_type": entry_type,
        },
        privacy_level=PrivacyLevel.PRIVATE,
    )


# =============================================================================
# Versions 模块后台写入
# =============================================================================

async def record_version_selection(
    user_id: str,
    set_id: str,
    version_id: str,
    recommended_id: Optional[str],
    notes: Optional[str],
    selected_title: Optional[str],
) -> None:
    """记录版本选择事件到 MemoryService"""
    is_deviation = version_id != recommended_id
    
    event_id = await _execute_memory_write(
        write_fn="record_event",
        user_id=user_id,
        context_name="version_selection",
        event_type="version_selection",
        data={
            "set_id": set_id,
            "version_id": version_id,
            "recommended_id": recommended_id,
            "is_deviation": is_deviation,
            "notes": notes,
        },
        privacy_level=PrivacyLevel.PRIVATE,
    )
    
    # 如果偏离推荐，创建决策洞察
    if is_deviation and event_id:
        await _execute_memory_write(
            write_fn="create_insight",
            user_id=user_id,
            context_name="version_deviation_insight",
            summary=f"选择「{selected_title or version_id}」而非推荐版本",
            source_events=[event_id],
            confidence=0.9,
            dimension="decision",
            privacy_level=PrivacyLevel.PRIVATE,
        )


async def record_version_navigation(
    user_id: str,
    set_id: str,
    selected_version_id: Optional[str],
    tokens_used: int,
) -> None:
    """记录版本导航事件到 MemoryService"""
    await _execute_memory_write(
        write_fn="record_event",
        user_id=user_id,
        context_name="version_navigation",
        event_type="version_navigation",
        data={
            "set_id": set_id,
            "selected_version_id": selected_version_id,
            "tokens_used": tokens_used,
        },
        privacy_level=PrivacyLevel.PRIVATE,
    )


# =============================================================================
# Dream 模块后台写入
# =============================================================================

async def create_dream_insight(
    user_id: str,
    themes: Optional[List[str]],
    mood: Optional[str],
) -> None:
    """创建梦境洞察"""
    await _execute_memory_write(
        write_fn="create_insight",
        user_id=user_id,
        context_name="dream_insight",
        summary=f"梦境解读完成，主题: {', '.join(themes) if themes else mood}",
        source_events=[],
        confidence=0.75,
        dimension="dream",
        privacy_level=PrivacyLevel.PRIVATE,
    )


async def record_dream_event(
    user_id: str,
    dream_id: str,
    raw_input: Optional[str],
    mood: Optional[str],
    tags: Optional[List[str]],
    has_generated_content: bool,
) -> None:
    """记录梦境事件到 MemoryService"""
    event_id = await _execute_memory_write(
        write_fn="record_event",
        user_id=user_id,
        context_name="dream_record",
        event_type="dream_record",
        data={
            "dream_id": dream_id,
            "raw_input": (raw_input[:200] if raw_input else ""),
            "mood": mood,
            "tags": tags or [],
        },
        privacy_level=PrivacyLevel.SENSITIVE,
    )
    
    # 如果有生成内容，创建洞察
    if has_generated_content and raw_input and event_id:
        try:
            from backend.calculators.dream import DreamExtractor
            from backend.calculators.dream.models import DreamInput
            
            extractor = DreamExtractor()
            extract_result = extractor.extract(DreamInput(dream_text=raw_input))
            themes = [str(s.category) for s in extract_result.symbols[:3]]
            
            await _execute_memory_write(
                write_fn="create_insight",
                user_id=user_id,
                context_name="dream_content_insight",
                summary=f"梦境主题: {', '.join(themes) if themes else mood}",
                source_events=[event_id],
                confidence=0.8,
                dimension="dream",
                privacy_level=PrivacyLevel.PRIVATE,
            )
        except Exception as e:
            logger.warning(f"Failed to create dream insight: user={user_id}, error={e}")


# =============================================================================
# 统一后台投递入口
# =============================================================================

def spawn_memory_write(
    coro_factory: callable,
    *,
    context_name: str,
    user_id: str,
) -> None:
    """
    统一后台写入投递入口
    
    Args:
        coro_factory: 返回协程的工厂函数（避免提前创建协程）
        context_name: 上下文名称（用于日志）
        user_id: 用户 ID
    """
    async def _wrapper() -> None:
        try:
            await coro_factory()
        except Exception as e:
            logger.warning(
                f"Background memory write failed: context={context_name}, user={user_id}, error={e}",
                extra={
                    "structured": {
                        "context_name": context_name,
                        "user_id": user_id,
                        "exception_type": type(e).__name__,
                        "exception_message": str(e),
                    }
                },
            )
    
    asyncio.create_task(_wrapper())
