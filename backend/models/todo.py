"""
TODO Database Models

TODO/DONE 行为记录的 SQLAlchemy 模型。

对照契约: backend/core/contracts/todo_models.py
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Enum, Index, JSON, String, Text
from sqlalchemy.orm import relationship

from backend.db.base import Base
from backend.core.contracts.todo_models import TodoType, TodoStatus


class TodoEntry(Base):
    """
    TODO 条目表
    
    存储用户的每日行为记录（TO-DO/DONE）。
    每条记录限制在 0-100 字以内。
    """
    __tablename__ = "todo_entries"

    # 主键
    todo_id = Column(
        String(64), 
        primary_key=True,
        comment="TODO ID，格式 todo_xxxxxxxxxxxx"
    )
    
    # 关联用户
    user_id = Column(
        String(64), 
        nullable=False, 
        index=True,
        comment="用户ID"
    )
    
    # 内容（限制100字）
    content = Column(
        String(100),
        nullable=False,
        comment="内容，最大100字符"
    )
    
    # 条目类型
    entry_type = Column(
        Enum(TodoType),
        nullable=False,
        comment="类型: todo/done"
    )
    
    # 状态
    status = Column(
        Enum(TodoStatus),
        nullable=False,
        default=TodoStatus.PENDING,
        comment="状态: pending/completed/cancelled"
    )
    
    # 时间戳
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="创建时间"
    )
    
    completed_at = Column(
        DateTime,
        nullable=True,
        comment="完成时间"
    )
    
    # 批处理填充字段
    extracted_intent = Column(
        JSON,
        nullable=True,
        comment="LLM 提取的意图结构"
    )
    
    linked_insight_id = Column(
        String(64),
        nullable=True,
        comment="关联的 Insight ID"
    )

    # 复合索引：用户ID + 创建日期（用于日期查询）
    __table_args__ = (
        Index('ix_todo_user_date', 'user_id', 'created_at'),
    )

    def __repr__(self) -> str:
        return f"<TodoEntry {self.todo_id} type={self.entry_type}>"

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "todo_id": self.todo_id,
            "user_id": self.user_id,
            "content": self.content,
            "entry_type": self.entry_type.value if self.entry_type else None,
            "status": self.status.value if self.status else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "extracted_intent": self.extracted_intent,
            "linked_insight_id": self.linked_insight_id,
        }
