"""
Memory Models

三层记忆模型定义。

对照 design.md 2.4:
- MemoryEvent: 事件层 - 原始记录
- MemoryInsight: 洞察层 - 归纳提炼
- UserProfile: 画像层 - 长期特征

对照 tasks.md 5.2, 5.3:
- Requirements: 4.1.1-4.1.3, 4.2.1
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PrivacyLevel(str, Enum):
    """
    隐私级别
    
    对照 design.md 2.4, tasks.md 5.3:
    - PUBLIC: 可公开
    - PRIVATE: 用户私有
    - SENSITIVE: 敏感加密
    """
    PUBLIC = "public"
    PRIVATE = "private"
    SENSITIVE = "sensitive"


class InsightDimension(str, Enum):
    """
    洞察维度
    
    Phase 10 Task 10.1: 定义洞察维度枚举
    用于 MemoryQuerySelector 按场景过滤
    """
    BEHAVIOR = "behavior"    # 行为模式
    DREAM = "dream"          # 梦境分析
    DECISION = "decision"    # 决策倾向
    EMOTION = "emotion"      # 情绪状态
    DESTINY = "destiny"      # 命理相关


class MemoryEvent(BaseModel):
    """
    事件层 - 原始记录
    
    对照 design.md 2.4, tasks.md 5.2:
    - event_id: 事件 ID
    - user_id: 用户 ID
    - event_type: 事件类型
    - data: 事件数据
    - privacy_level: 隐私级别
    - created_at: 创建时间
    """
    event_id: str = Field(..., description="事件 ID")
    user_id: str = Field(..., description="用户 ID")
    event_type: str = Field(..., description="事件类型 (analysis, playbook, qa)")
    data: Dict[str, Any] = Field(default_factory=dict, description="事件数据")
    privacy_level: PrivacyLevel = Field(
        default=PrivacyLevel.PRIVATE,
        description="隐私级别",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="创建时间",
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "event_id": "evt_abc123",
                    "user_id": "user_001",
                    "event_type": "analysis",
                    "data": {"birth_data": "...", "fusion_id": "fus_xyz"},
                    "privacy_level": "private",
                    "created_at": "2025-12-06T12:00:00Z",
                }
            ]
        }
    )


class MemoryInsight(BaseModel):
    """
    洞察层 - 归纳提炼
    
    对照 design.md 2.4, tasks.md 5.2:
    - insight_id: 洞察 ID
    - user_id: 用户 ID
    - source_events: 来源事件 ID 列表
    - summary: 摘要
    - confidence: 置信度
    - privacy_level: 隐私级别
    """
    insight_id: str = Field(..., description="洞察 ID")
    user_id: str = Field(..., description="用户 ID")
    source_events: List[str] = Field(
        default_factory=list,
        description="来源事件 ID 列表",
    )
    summary: str = Field(..., description="洞察摘要")
    confidence: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="置信度",
    )
    dimension: Optional[str] = Field(
        default=None,
        description="洞察维度 (behavior, dream, decision, emotion, destiny)",
    )
    source_engine: Optional[str] = Field(
        default=None,
        description="来源引擎 ID，如 bazi-calculator, dream-extractor",
    )
    privacy_level: PrivacyLevel = Field(
        default=PrivacyLevel.PRIVATE,
        description="隐私级别",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="创建时间",
    )


class UserProfile(BaseModel):
    """
    画像层 - 长期特征
    
    对照 design.md 2.4, tasks.md 5.2:
    - user_id: 用户 ID
    - traits: 特征 → 强度
    - preferences: 偏好设置
    - last_updated: 最后更新时间
    """
    user_id: str = Field(..., description="用户 ID")
    traits: Dict[str, float] = Field(
        default_factory=dict,
        description="特征强度映射 (trait_name → strength 0-1)",
    )
    preferences: Dict[str, Any] = Field(
        default_factory=dict,
        description="偏好设置",
    )
    last_updated: datetime = Field(
        default_factory=datetime.utcnow,
        description="最后更新时间",
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "user_id": "user_001",
                    "traits": {
                        "career_focus": 0.8,
                        "emotional_stability": 0.6,
                    },
                    "preferences": {
                        "language": "zh-CN",
                        "detail_level": "detailed",
                    },
                    "last_updated": "2025-12-06T12:00:00Z",
                }
            ]
        }
    )
