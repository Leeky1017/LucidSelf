"""
TODO Service

TODO/DONE 行为记录服务实现。

对照契约: backend/core/contracts/todo_models.py
"""

import logging
import secrets
from datetime import datetime, date
from typing import List, Optional, Tuple

from backend.core.contracts.todo_models import (
    TODO_CONTENT_MAX_LENGTH,
    TODO_DAILY_LIMIT,
    TodoType,
    TodoStatus,
    TodoEntry,
    TodoDailySummary,
)

logger = logging.getLogger(__name__)


# =============================================================================
# ID 生成
# =============================================================================

def generate_todo_id() -> str:
    """生成 TODO ID: todo_xxxxxxxxxxxx"""
    return f"todo_{secrets.token_hex(6)}"


# =============================================================================
# TODO 服务
# =============================================================================

class TodoService:
    """
    TODO 服务
    
    提供 TODO/DONE 行为记录的 CRUD 操作。
    """
    
    def __init__(self):
        # 内存存储（开发用，生产环境使用数据库）
        self._entries: dict = {}  # todo_id -> entry_data
        self._user_entries: dict = {}  # user_id -> [todo_id, ...]
    
    # =========================================================================
    # CRUD 操作
    # =========================================================================
    
    async def create(
        self,
        user_id: str,
        content: str,
        entry_type: TodoType,
    ) -> TodoEntry:
        """
        创建 TODO 条目
        
        Args:
            user_id: 用户ID
            content: 内容（1-100字符）
            entry_type: 类型（todo/done）
            
        Returns:
            创建的条目
            
        Raises:
            ValueError: 内容校验失败或超出每日限制
        """
        # 校验内容长度
        content = content.strip()
        if len(content) == 0:
            raise ValueError("内容不能为空")
        if len(content) > TODO_CONTENT_MAX_LENGTH:
            raise ValueError(f"内容不能超过 {TODO_CONTENT_MAX_LENGTH} 字")
        
        # 检查每日限制
        today = date.today().isoformat()
        today_count = await self._count_today_entries(user_id)
        if today_count >= TODO_DAILY_LIMIT:
            raise ValueError(f"已达到每日上限（{TODO_DAILY_LIMIT}条）")
        
        # 创建条目
        todo_id = generate_todo_id()
        now = datetime.utcnow()
        
        entry_data = {
            "todo_id": todo_id,
            "user_id": user_id,
            "content": content,
            "entry_type": entry_type,
            "status": TodoStatus.PENDING,
            "created_at": now,
            "completed_at": None,
            "extracted_intent": None,
            "linked_insight_id": None,
        }
        
        # 存储
        self._entries[todo_id] = entry_data
        
        if user_id not in self._user_entries:
            self._user_entries[user_id] = []
        self._user_entries[user_id].append(todo_id)
        
        logger.info(f"Created todo entry: {todo_id} for user {user_id}")
        
        return TodoEntry(**entry_data)
    
    async def get(self, todo_id: str) -> Optional[TodoEntry]:
        """获取单条 TODO"""
        entry_data = self._entries.get(todo_id)
        if not entry_data:
            return None
        return TodoEntry(**entry_data)
    
    async def update(
        self,
        todo_id: str,
        content: Optional[str] = None,
        status: Optional[TodoStatus] = None,
    ) -> Optional[TodoEntry]:
        """
        更新 TODO 条目
        
        Args:
            todo_id: TODO ID
            content: 新内容（可选）
            status: 新状态（可选）
            
        Returns:
            更新后的条目，不存在返回 None
        """
        entry_data = self._entries.get(todo_id)
        if not entry_data:
            return None
        
        # 更新内容
        if content is not None:
            content = content.strip()
            if len(content) == 0:
                raise ValueError("内容不能为空")
            if len(content) > TODO_CONTENT_MAX_LENGTH:
                raise ValueError(f"内容不能超过 {TODO_CONTENT_MAX_LENGTH} 字")
            entry_data["content"] = content
        
        # 更新状态
        if status is not None:
            entry_data["status"] = status
            if status == TodoStatus.COMPLETED:
                entry_data["completed_at"] = datetime.utcnow()
        
        logger.info(f"Updated todo entry: {todo_id}")
        
        return TodoEntry(**entry_data)
    
    async def delete(self, todo_id: str) -> bool:
        """删除 TODO 条目"""
        entry_data = self._entries.get(todo_id)
        if not entry_data:
            return False
        
        user_id = entry_data["user_id"]
        
        # 从存储中移除
        del self._entries[todo_id]
        if user_id in self._user_entries:
            self._user_entries[user_id] = [
                tid for tid in self._user_entries[user_id] if tid != todo_id
            ]
        
        logger.info(f"Deleted todo entry: {todo_id}")
        return True
    
    # =========================================================================
    # 列表查询
    # =========================================================================
    
    async def list(
        self,
        user_id: str,
        date_filter: Optional[str] = None,
        entry_type: Optional[TodoType] = None,
        status: Optional[TodoStatus] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> Tuple[List[TodoEntry], int, bool]:
        """
        获取 TODO 列表
        
        Args:
            user_id: 用户ID
            date_filter: 日期过滤（YYYY-MM-DD）
            entry_type: 类型过滤
            status: 状态过滤
            limit: 每页条数
            offset: 偏移量
            
        Returns:
            (条目列表, 总数, 是否有更多)
        """
        # 获取用户的所有条目
        user_todo_ids = self._user_entries.get(user_id, [])
        entries = []
        
        for todo_id in user_todo_ids:
            entry_data = self._entries.get(todo_id)
            if not entry_data:
                continue
            
            # 日期过滤
            if date_filter:
                entry_date = entry_data["created_at"].date().isoformat()
                if entry_date != date_filter:
                    continue
            
            # 类型过滤
            if entry_type and entry_data["entry_type"] != entry_type:
                continue
            
            # 状态过滤
            if status and entry_data["status"] != status:
                continue
            
            entries.append(entry_data)
        
        # 按创建时间倒序
        entries.sort(key=lambda x: x["created_at"], reverse=True)
        
        total = len(entries)
        has_more = (offset + limit) < total
        
        # 分页
        paged_entries = entries[offset:offset + limit]
        
        return (
            [TodoEntry(**e) for e in paged_entries],
            total,
            has_more,
        )
    
    async def get_summary(
        self,
        user_id: str,
        date_filter: Optional[str] = None,
    ) -> TodoDailySummary:
        """
        获取每日汇总
        
        Args:
            user_id: 用户ID
            date_filter: 日期（YYYY-MM-DD），默认今天
            
        Returns:
            每日汇总
        """
        if not date_filter:
            date_filter = date.today().isoformat()
        
        entries, total, _ = await self.list(
            user_id=user_id,
            date_filter=date_filter,
            limit=100,
        )
        
        todo_count = sum(1 for e in entries if e.entry_type == TodoType.TODO)
        done_count = sum(1 for e in entries if e.entry_type == TodoType.DONE)
        completed_count = sum(1 for e in entries if e.status == TodoStatus.COMPLETED)
        
        return TodoDailySummary(
            user_id=user_id,
            date=date_filter,
            total_count=total,
            todo_count=todo_count,
            done_count=done_count,
            completed_count=completed_count,
            entries=entries,
        )
    
    # =========================================================================
    # 辅助方法
    # =========================================================================
    
    async def _count_today_entries(self, user_id: str) -> int:
        """统计用户今日条目数"""
        today = date.today().isoformat()
        entries, total, _ = await self.list(
            user_id=user_id,
            date_filter=today,
            limit=1000,
        )
        return total
    
    async def get_entries_for_batch(
        self,
        user_id: str,
        date_filter: str,
    ) -> List[TodoEntry]:
        """
        获取待批处理的条目
        
        用于 22:00 批处理，提取意图。
        """
        entries, _, _ = await self.list(
            user_id=user_id,
            date_filter=date_filter,
            limit=1000,
        )
        
        # 过滤出还没有提取意图的条目
        return [e for e in entries if e.extracted_intent is None]
    
    async def update_extracted_intent(
        self,
        todo_id: str,
        extracted_intent: dict,
        linked_insight_id: Optional[str] = None,
    ) -> bool:
        """
        更新提取的意图（批处理调用）
        """
        entry_data = self._entries.get(todo_id)
        if not entry_data:
            return False
        
        entry_data["extracted_intent"] = extracted_intent
        if linked_insight_id:
            entry_data["linked_insight_id"] = linked_insight_id
        
        return True


# =============================================================================
# 全局实例
# =============================================================================

_todo_service: Optional[TodoService] = None


def get_todo_service() -> TodoService:
    """获取 TODO 服务实例"""
    global _todo_service
    if _todo_service is None:
        _todo_service = TodoService()
    return _todo_service
