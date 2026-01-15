"""
Memory Database Models

记忆层的 SQLAlchemy 模型，用于持久化 Event、Insight、Profile。

对照 Pydantic 模型: backend/services/memory/models.py
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Index,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from backend.db.base import Base
from backend.services.memory.models import PrivacyLevel


class MemoryEventDB(Base):
    """
    事件表
    
    存储用户的原始事件记录。
    """
    __tablename__ = "memory_events"

    # 主键
    event_id = Column(
        String(64), 
        primary_key=True,
        comment="事件ID，格式 evt_xxxxxxxxxxxx"
    )
    
    # 用户
    user_id = Column(
        String(64), 
        nullable=False, 
        index=True,
        comment="用户ID"
    )
    
    # 事件类型
    event_type = Column(
        String(64),
        nullable=False,
        index=True,
        comment="事件类型 (analysis, playbook, qa, daily_todo_summary, user_intent, etc)"
    )
    
    # 事件数据 (JSON, 可能加密)
    data = Column(
        JSON,
        nullable=False,
        default=dict,
        comment="事件数据，SENSITIVE级别会加密"
    )
    
    # 隐私级别
    privacy_level = Column(
        SQLEnum(PrivacyLevel),
        nullable=False,
        default=PrivacyLevel.PRIVATE,
        comment="隐私级别: public/private/sensitive"
    )
    
    # 时间戳
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="创建时间"
    )

    # 索引
    __table_args__ = (
        Index('ix_event_user_type', 'user_id', 'event_type'),
        Index('ix_event_user_time', 'user_id', 'created_at'),
    )

    def __repr__(self) -> str:
        return f"<MemoryEvent {self.event_id} type={self.event_type}>"


class MemoryInsightDB(Base):
    """
    洞察表
    
    存储归纳提炼的洞察。
    """
    __tablename__ = "memory_insights"

    # 主键
    insight_id = Column(
        String(64), 
        primary_key=True,
        comment="洞察ID，格式 ins_xxxxxxxxxxxx"
    )
    
    # 用户
    user_id = Column(
        String(64), 
        nullable=False, 
        index=True,
        comment="用户ID"
    )
    
    # 来源事件 (JSON 数组)
    source_events = Column(
        JSON,
        nullable=False,
        default=list,
        comment="来源事件 ID 列表"
    )
    
    # 摘要 (可能加密)
    summary = Column(
        Text,
        nullable=False,
        comment="洞察摘要，SENSITIVE级别会加密"
    )
    
    # 置信度
    confidence = Column(
        Float,
        nullable=False,
        default=0.5,
        comment="置信度 0.0-1.0"
    )
    
    # 维度
    dimension = Column(
        String(32),
        nullable=True,
        index=True,
        comment="洞察维度 (behavior, dream, decision, emotion, destiny)"
    )
    
    # Phase 10 Task 10.1: 来源引擎
    source_engine = Column(
        String(64),
        nullable=True,
        index=True,
        comment="来源引擎 ID，如 bazi-calculator, dream-extractor"
    )
    
    # 隐私级别
    privacy_level = Column(
        SQLEnum(PrivacyLevel),
        nullable=False,
        default=PrivacyLevel.PRIVATE,
        comment="隐私级别"
    )
    
    # 时间戳
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="创建时间"
    )

    # 索引
    __table_args__ = (
        Index('ix_insight_user_dim', 'user_id', 'dimension'),
        Index('ix_insight_user_conf', 'user_id', 'confidence'),
    )

    def __repr__(self) -> str:
        return f"<MemoryInsight {self.insight_id} dim={self.dimension}>"


class UserProfileDB(Base):
    """
    用户画像表
    
    存储用户的长期特征和偏好。
    每个用户只有一条画像记录。
    """
    __tablename__ = "user_profiles_memory"  # 避免与 user.py 的 user_profiles 冲突

    # 使用 user_id 作为主键（一对一）
    user_id = Column(
        String(64), 
        primary_key=True,
        comment="用户ID（主键）"
    )
    
    # 特征 (JSON: trait_name → strength 0-1)
    traits = Column(
        JSON,
        nullable=False,
        default=dict,
        comment="特征强度映射"
    )
    
    # 偏好 (JSON)
    preferences = Column(
        JSON,
        nullable=False,
        default=dict,
        comment="偏好设置"
    )
    
    # 标签（便于查询）
    tags = Column(
        JSON,
        nullable=False,
        default=list,
        comment="用户标签列表"
    )
    
    # 时间戳
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="创建时间"
    )
    
    last_updated = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
        comment="最后更新时间"
    )

    def __repr__(self) -> str:
        return f"<UserProfileMemory {self.user_id}>"
