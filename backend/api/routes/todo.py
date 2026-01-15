"""
TODO API Routes

TODO/DONE 行为记录 API 端点。

对照契约: backend/core/contracts/todo_models.py
对照文档: .kiro/docs/api_contracts.md §3.3
"""

import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from backend.core.contracts.auth_models import UserInfo
from backend.core.contracts.todo_models import (
    TodoType,
    TodoStatus,
    TodoEntry,
    TodoCreateRequest,
    TodoUpdateRequest,
    TodoListResponse,
    TodoDailySummary,
    TODO_CONTENT_MAX_LENGTH,
    TODO_DAILY_LIMIT,
)
from backend.services.todo import TodoService, get_todo_service
from backend.api.routes.auth import get_current_user
from backend.services.memory.background_writer import spawn_memory_write, record_todo_event

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/todo", tags=["todo"])


# =============================================================================
# CRUD 端点
# =============================================================================

@router.post(
    "",
    response_model=TodoEntry,
    status_code=status.HTTP_201_CREATED,
    summary="创建 TODO 条目",
    description=f"创建新的 TODO 或 DONE 条目，内容限制 {TODO_CONTENT_MAX_LENGTH} 字",
)
async def create_todo(
    request: TodoCreateRequest,
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoEntry:
    """
    创建 TODO 条目
    
    - **content**: 内容（1-100字符）
    - **entry_type**: 类型（todo/done）
    
    每日上限 50 条。
    """
    try:
        entry = await todo_service.create(
            user_id=user.user_id,
            content=request.content,
            entry_type=request.entry_type,
        )
        
        # Phase 7 Task 7.3: 异步写入 MemoryService（不阻塞主流程）
        spawn_memory_write(
            lambda: record_todo_event(
                user_id=user.user_id,
                todo_id=entry.todo_id,
                content=request.content,
                entry_type=request.entry_type.value,
            ),
            context_name="todo_event",
            user_id=user.user_id,
        )
        
        return entry
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "TODO_CREATE_FAILED", "message": str(e)},
        )


@router.get(
    "",
    response_model=TodoListResponse,
    summary="获取 TODO 列表",
    description="获取当前用户的 TODO 列表，支持日期和状态过滤",
)
async def list_todos(
    date: Optional[str] = Query(None, description="日期过滤，YYYY-MM-DD"),
    entry_type: Optional[TodoType] = Query(None, description="类型过滤"),
    todo_status: Optional[TodoStatus] = Query(None, alias="status", description="状态过滤"),
    limit: int = Query(50, ge=1, le=100, description="每页条数"),
    offset: int = Query(0, ge=0, description="偏移量"),
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoListResponse:
    """
    获取 TODO 列表
    
    - **date**: 日期过滤（YYYY-MM-DD），默认返回所有
    - **entry_type**: 类型过滤（todo/done）
    - **status**: 状态过滤（pending/completed/cancelled）
    - **limit**: 每页条数（1-100）
    - **offset**: 偏移量
    """
    entries, total, has_more = await todo_service.list(
        user_id=user.user_id,
        date_filter=date,
        entry_type=entry_type,
        status=todo_status,
        limit=limit,
        offset=offset,
    )
    
    return TodoListResponse(
        entries=entries,
        total=total,
        has_more=has_more,
    )


@router.get(
    "/summary",
    response_model=TodoDailySummary,
    summary="获取每日汇总",
    description="获取指定日期的 TODO 汇总统计",
)
async def get_summary(
    date: Optional[str] = Query(None, description="日期，YYYY-MM-DD，默认今天"),
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoDailySummary:
    """
    获取每日汇总
    
    - **date**: 日期（YYYY-MM-DD），默认今天
    
    返回当日的 TODO/DONE 统计和条目列表。
    """
    return await todo_service.get_summary(
        user_id=user.user_id,
        date_filter=date,
    )


@router.get(
    "/{todo_id}",
    response_model=TodoEntry,
    summary="获取单条 TODO",
    description="根据 ID 获取 TODO 详情",
)
async def get_todo(
    todo_id: str,
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoEntry:
    """获取单条 TODO"""
    entry = await todo_service.get(todo_id)
    
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "TODO_NOT_FOUND", "message": "条目不存在"},
        )
    
    # 验证归属
    if entry.user_id != user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"code": "TODO_FORBIDDEN", "message": "无权访问"},
        )
    
    return entry


@router.patch(
    "/{todo_id}",
    response_model=TodoEntry,
    summary="更新 TODO",
    description="更新 TODO 的内容或状态",
)
async def update_todo(
    todo_id: str,
    request: TodoUpdateRequest,
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoEntry:
    """
    更新 TODO
    
    - **content**: 新内容（可选）
    - **status**: 新状态（可选）
    """
    # 先检查存在和归属
    existing = await todo_service.get(todo_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "TODO_NOT_FOUND", "message": "条目不存在"},
        )
    
    if existing.user_id != user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"code": "TODO_FORBIDDEN", "message": "无权操作"},
        )
    
    try:
        entry = await todo_service.update(
            todo_id=todo_id,
            content=request.content,
            status=request.status,
        )
        return entry
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "TODO_UPDATE_FAILED", "message": str(e)},
        )


@router.delete(
    "/{todo_id}",
    summary="删除 TODO",
    description="删除指定的 TODO 条目",
)
async def delete_todo(
    todo_id: str,
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> dict:
    """删除 TODO"""
    # 先检查存在和归属
    existing = await todo_service.get(todo_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "TODO_NOT_FOUND", "message": "条目不存在"},
        )
    
    if existing.user_id != user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"code": "TODO_FORBIDDEN", "message": "无权操作"},
        )
    
    await todo_service.delete(todo_id)
    return {"success": True, "message": "已删除"}


# =============================================================================
# 快捷操作
# =============================================================================

@router.post(
    "/{todo_id}/complete",
    response_model=TodoEntry,
    summary="标记完成",
    description="将 TODO 标记为已完成",
)
async def complete_todo(
    todo_id: str,
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoEntry:
    """标记为完成"""
    existing = await todo_service.get(todo_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "TODO_NOT_FOUND", "message": "条目不存在"},
        )
    
    if existing.user_id != user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"code": "TODO_FORBIDDEN", "message": "无权操作"},
        )
    
    entry = await todo_service.update(
        todo_id=todo_id,
        status=TodoStatus.COMPLETED,
    )
    return entry


@router.post(
    "/{todo_id}/cancel",
    response_model=TodoEntry,
    summary="取消 TODO",
    description="将 TODO 标记为已取消",
)
async def cancel_todo(
    todo_id: str,
    user: UserInfo = Depends(get_current_user),
    todo_service: TodoService = Depends(get_todo_service),
) -> TodoEntry:
    """取消 TODO"""
    existing = await todo_service.get(todo_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "TODO_NOT_FOUND", "message": "条目不存在"},
        )
    
    if existing.user_id != user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"code": "TODO_FORBIDDEN", "message": "无权操作"},
        )
    
    entry = await todo_service.update(
        todo_id=todo_id,
        status=TodoStatus.CANCELLED,
    )
    return entry


# P0-1: 辅助函数已移至 backend/services/memory/background_writer.py
