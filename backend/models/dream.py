"""
Dream Model

梦境记录数据模型。
"""

import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, Text, Integer, JSON, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db.base import Base


class DreamRecord(Base):
    """梦境记录表"""
    
    __tablename__ = "dream_records"
    
    # 主键
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    
    # 用户关联
    user_id: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
    )

    # 组织/租户ID（多租户隔离边界）
    org_id: Mapped[Optional[str]] = mapped_column(
        String(64),
        nullable=True,
        index=True,
        comment="组织/租户ID（缺省时视为 legacy 记录）",
    )
    
    # 状态和模式
    status: Mapped[str] = mapped_column(
        String(20),
        default="draft",
        nullable=False,
    )  # draft, published
    
    mode: Mapped[str] = mapped_column(
        String(20),
        default="quick",
        nullable=False,
    )  # quick, detailed
    
    # 内容
    raw_input: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    
    generated_content: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    
    final_content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    
    # 元数据
    title: Mapped[Optional[str]] = mapped_column(
        String(200),
        nullable=True,
    )
    
    mood: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )
    
    clarity: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
    )  # 1-5
    
    tags: Mapped[List[str]] = mapped_column(
        ARRAY(String),
        default=list,
        nullable=False,
    )
    
    # 分析结果 (JSON)
    analysis: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
    )
    
    # 生成计数
    generate_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    
    # 发布时间
    published_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True,
    )
    
    # 索引
    __table_args__ = (
        Index("ix_dream_records_org_user_created", "org_id", "user_id", "created_at"),
    )
    
    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "org_id": self.org_id,
            "status": self.status,
            "mode": self.mode,
            "raw_input": self.raw_input,
            "generated_content": self.generated_content,
            "final_content": self.final_content,
            "title": self.title,
            "mood": self.mood,
            "clarity": self.clarity,
            "tags": self.tags,
            "analysis": self.analysis,
            "generate_count": self.generate_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "published_at": self.published_at.isoformat() if self.published_at else None,
        }
