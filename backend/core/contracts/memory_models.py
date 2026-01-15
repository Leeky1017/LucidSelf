"""
Memory Models for LucidSelf Contracts

记忆层模型定义，包括事件、洞察和用户画像。
对照文档: docs/数据契约_Schema定义规范_v1.md §9.6
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

from backend.core.contracts.base import EVENT_ID_PATTERN, INSIGHT_ID_PATTERN


# =============================================================================
# 隐私级别枚举 (§9.6)
# =============================================================================


class PrivacyLevel(str, Enum):
    """
    隐私级别枚举
    
    对照文档 §9.6 PrivacyLevel
    """
    PUBLIC = "public"       # 可以用于匿名统计/模型训练
    PRIVATE = "private"     # 仅该用户可见
    SENSITIVE = "sensitive" # 禁止用于训练，需加密存储


# =============================================================================
# 记忆基类 (§9.6)
# =============================================================================


class MemoryBase(BaseModel):
    """
    记忆基类
    
    所有记忆模型的基类，包含隐私级别。
    """
    privacy: PrivacyLevel = Field(
        default=PrivacyLevel.PRIVATE, 
        description="隐私级别"
    )


# =============================================================================
# 敏感字段定义 (§9.6)
# =============================================================================


SENSITIVE_FIELDS: Dict[str, List[str]] = {
    "UserProfile": [
        "real_name", 
        "phone_number", 
        "email", 
        "address", 
        "id_number"
    ],
    "Event.payload": [
        "location_detail", 
        "contacts", 
        "medical_history"
    ]
}
"""敏感字段映射表，这些字段在 SENSITIVE 级别时需要加密存储"""


# =============================================================================
# Event 层：原始事件 (§9.6)
# =============================================================================


class Event(MemoryBase):
    """
    原始事件记录
    
    Event 层只存原始事实，不做推断。
    对照文档 §9.6 Event
    """
    event_id: str = Field(
        ..., 
        pattern=EVENT_ID_PATTERN,
        description="事件ID，格式 evt_xxxxxxxxxxxx"
    )
    user_id: str = Field(..., description="用户ID")
    timestamp: datetime = Field(..., description="事件时间")
    
    kind: Literal[
        "dream_record",      # 梦境记录
        "reading_request",   # 解读请求
        "feedback",          # 用户反馈
        "profile_edit",      # 档案编辑
        "preference_change", # 偏好调整
        "system_action"      # 系统动作
    ] = Field(..., description="事件类型")
    
    payload: Dict[str, Any] = Field(
        ..., 
        description="事件载荷，仅边界 JSON，内部转换成专门类型"
    )
    source_channel: Literal["app", "web", "miniapp", "partner_api"] = Field(
        ..., 
        description="来源渠道"
    )
    sensitive: bool = Field(default=False, description="是否包含敏感信息")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "event_id": "evt_abc123456789",
                "user_id": "user_12345",
                "timestamp": "2025-11-25T14:00:00",
                "kind": "dream_record",
                "payload": {"dream_text": "梦到飞在天空"},
                "source_channel": "app",
                "sensitive": False,
                "privacy": "private"
            }
        }
    )


# =============================================================================
# 洞察维度枚举 (Phase 10 Task 10.1)
# =============================================================================


class InsightDimension(str, Enum):
    """
    洞察维度枚举
    
    用于 MemoryQuerySelector 按场景过滤
    对照 design.md §6.8
    """
    BEHAVIOR = "behavior"    # 行为模式
    DREAM = "dream"          # 梦境分析
    DECISION = "decision"    # 决策倾向
    EMOTION = "emotion"      # 情绪状态
    DESTINY = "destiny"      # 命理相关


# =============================================================================
# Insight 层：结构化洞察 (§9.6)
# =============================================================================


class Insight(MemoryBase):
    """
    结构化洞察
    
    Insight 层只存结构化洞察，禁止直接存 LLM 自然语言段落。
    对照文档 §9.6 Insight
    """
    insight_id: str = Field(
        ..., 
        pattern=INSIGHT_ID_PATTERN,
        description="洞察ID，格式 ins_xxxxxxxxxxxx"
    )
    user_id: str = Field(..., description="用户ID")
    created_at: datetime = Field(..., description="创建时间")
    
    # 来源关联
    factors: List[str] = Field(
        default_factory=list, 
        description="关联的 factor_id 列表"
    )
    rules: List[str] = Field(
        default_factory=list, 
        description="关联的 rule_id 列表"
    )
    themes: List[str] = Field(
        default_factory=list, 
        description="主题标签，如：事业突破窗口、情感风险"
    )
    
    # 核心内容
    summary_zh: str = Field(
        ..., 
        max_length=100, 
        description="结构化短句"
    )
    strength: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="置信度 0.0-1.0"
    )
    time_scope: Literal["past", "present", "near_future", "long_term"] = Field(
        ..., 
        description="时间范围"
    )
    
    # Phase 10 Task 10.1: 新增字段
    dimension: Optional[str] = Field(
        default=None,
        description="洞察维度 (behavior, dream, decision, emotion, destiny)"
    )
    source_engine: Optional[str] = Field(
        default=None,
        description="来源引擎 ID，如 bazi-calculator, dream-extractor"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "insight_id": "ins_xyz987654321",
                "user_id": "user_12345",
                "created_at": "2025-11-25T14:00:00",
                "factors": ["day_master_jia", "season_spring"],
                "rules": ["dts_jia_spring_001"],
                "themes": ["事业突破", "领导力提升"],
                "summary_zh": "事业发展进入突破期",
                "strength": 0.85,
                "time_scope": "near_future",
                "dimension": "destiny",
                "source_engine": "bazi-calculator",
                "privacy": "private"
            }
        }
    )


# =============================================================================
# Profile 层：长期画像 (§9.6)
# =============================================================================


class UserProfile(MemoryBase):
    """
    用户长期画像
    
    Profile 层只存稳定 trait/偏好，不存一次性情绪。
    对照文档 §9.6 UserProfile
    """
    user_id: str = Field(..., description="用户ID")
    
    # 稳定特质
    traits: Dict[str, float] = Field(
        default_factory=dict, 
        description="性格特质，如 risk_tolerance: 0.7"
    )
    
    # 偏好设置
    preferences: Dict[str, Any] = Field(
        default_factory=dict, 
        description="引擎偏好、语言偏好、叙事风格等"
    )
    
    # 长期主轴
    long_term_themes: List[str] = Field(
        default_factory=list, 
        description="长期叙事主轴"
    )
    
    # 元信息
    last_updated: datetime = Field(..., description="最后更新时间")
    update_count: int = Field(default=0, description="更新次数")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "user_id": "user_12345",
                "traits": {"risk_tolerance": 0.7, "creativity": 0.9},
                "preferences": {"language": "zh", "tone": "friendly"},
                "long_term_themes": ["事业发展", "家庭平衡"],
                "last_updated": "2025-11-25T14:00:00",
                "update_count": 5,
                "privacy": "private"
            }
        }
    )
