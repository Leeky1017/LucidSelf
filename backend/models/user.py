"""
User Model

用户档案和限制数据模型。
"""

import uuid
from datetime import date, datetime
from typing import Optional

from sqlalchemy import String, Integer, Date, JSON, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.db.base import Base


class UserProfile(Base):
    """用户档案表"""
    
    __tablename__ = "user_profiles"
    
    # 主键
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    
    # 用户ID（外部标识）
    user_id: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )
    
    # 出生数据 (JSON)
    birth_data: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
    )
    
    # 用户偏好 (JSON)
    preferences: Mapped[dict] = mapped_column(
        JSON,
        default=dict,
        nullable=False,
    )
    
    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "birth_data": self.birth_data,
            "preferences": self.preferences,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class UserLimit(Base):
    """用户限制表（每日配额）"""
    
    __tablename__ = "user_limits"
    
    # 主键
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    
    # 用户ID
    user_id: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
    )
    
    # 日期
    limit_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    
    # 配额
    daily_dreams: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False,
    )
    
    daily_readings: Mapped[int] = mapped_column(
        Integer,
        default=10,
        nullable=False,
    )
    
    # 已使用
    dreams_used: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    
    readings_used: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    
    # 唯一约束：每个用户每天一条记录
    __table_args__ = (
        UniqueConstraint("user_id", "limit_date", name="uq_user_limit_date"),
    )
    
    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "user_id": self.user_id,
            "limit_date": self.limit_date.isoformat() if self.limit_date else None,
            "daily_dreams": self.daily_dreams,
            "daily_readings": self.daily_readings,
            "dreams_used": self.dreams_used,
            "readings_used": self.readings_used,
            "dreams_remaining": self.daily_dreams - self.dreams_used,
            "readings_remaining": self.daily_readings - self.readings_used,
        }
