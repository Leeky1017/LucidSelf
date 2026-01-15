"""
TODO Models for LucidSelf Contracts

用户行为记录模型（TO-DO/DONE）。

对照文档: 
- .kiro/docs/api_contracts.md §2.3
- docs/创始人兼老板阐述对LS系统的设计理念.md §3.2
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


# =============================================================================
# ID 格式常量
# =============================================================================

TODO_ID_PATTERN = r"^todo_[a-z0-9]{12}$"


# =============================================================================
# 约束常量
# =============================================================================

TODO_CONTENT_MAX_LENGTH = 100
"""TODO 内容最大长度（字符）"""

TODO_DAILY_LIMIT = 50
"""每日 TODO 条数上限"""


# =============================================================================
# 枚举定义
# =============================================================================


class TodoType(str, Enum):
    """
    条目类型
    
    - TODO: 计划要做的事
    - DONE: 已经完成的事
    """
    TODO = "todo"
    DONE = "done"


class TodoStatus(str, Enum):
    """
    条目状态
    
    状态流转: PENDING → COMPLETED/CANCELLED
    """
    PENDING = "pending"      # 待处理
    COMPLETED = "completed"  # 已完成
    CANCELLED = "cancelled"  # 已取消


# =============================================================================
# 数据模型
# =============================================================================


class TodoEntry(BaseModel):
    """
    TODO 条目
    
    用户输入的每日行为记录，每条限制在 0-100 字以内。
    """
    model_config = ConfigDict(str_strip_whitespace=True)
    
    todo_id: str = Field(
        ..., 
        pattern=TODO_ID_PATTERN,
        description="TODO ID，格式 todo_xxxxxxxxxxxx"
    )
    user_id: str = Field(
        ..., 
        max_length=64,
        description="用户ID"
    )
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=TODO_CONTENT_MAX_LENGTH,
        description=f"内容，1-{TODO_CONTENT_MAX_LENGTH}字符"
    )
    entry_type: TodoType = Field(
        ...,
        description="条目类型：todo/done"
    )
    status: TodoStatus = Field(
        default=TodoStatus.PENDING,
        description="条目状态"
    )
    created_at: datetime = Field(
        ...,
        description="创建时间"
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="完成时间"
    )
    
    # 批处理填充字段
    extracted_intent: Optional[Dict[str, Any]] = Field(
        None, 
        description="LLM 提取的意图结构（22:00 批处理填充）"
    )
    linked_insight_id: Optional[str] = Field(
        None,
        description="关联的 Insight ID"
    )
    
    @field_validator('content')
    @classmethod
    def validate_content(cls, v: str) -> str:
        """校验并清理内容"""
        v = v.strip()
        if len(v) > TODO_CONTENT_MAX_LENGTH:
            raise ValueError(f'内容不能超过 {TODO_CONTENT_MAX_LENGTH} 字')
        if len(v) == 0:
            raise ValueError('内容不能为空')
        return v


class TodoDailySummary(BaseModel):
    """
    每日 TODO 汇总
    
    用于展示某一天的 TODO/DONE 统计。
    """
    user_id: str = Field(
        ...,
        description="用户ID"
    )
    date: str = Field(
        ...,
        description="日期，YYYY-MM-DD 格式"
    )
    total_count: int = Field(
        ...,
        description="总条数"
    )
    todo_count: int = Field(
        ...,
        description="TODO 条数"
    )
    done_count: int = Field(
        ...,
        description="DONE 条数"
    )
    completed_count: int = Field(
        ...,
        description="已完成条数"
    )
    entries: List[TodoEntry] = Field(
        default_factory=list,
        description="条目列表"
    )


# =============================================================================
# 请求/响应模型
# =============================================================================


class TodoCreateRequest(BaseModel):
    """创建 TODO 请求"""
    content: str = Field(
        ...,
        min_length=1,
        max_length=TODO_CONTENT_MAX_LENGTH,
        description=f"内容，1-{TODO_CONTENT_MAX_LENGTH}字符"
    )
    entry_type: TodoType = Field(
        ...,
        description="条目类型：todo/done"
    )
    
    @field_validator('content')
    @classmethod
    def validate_content(cls, v: str) -> str:
        return v.strip()


class TodoUpdateRequest(BaseModel):
    """更新 TODO 请求"""
    content: Optional[str] = Field(
        None,
        max_length=TODO_CONTENT_MAX_LENGTH,
        description="更新内容"
    )
    status: Optional[TodoStatus] = Field(
        None,
        description="更新状态"
    )
    
    @field_validator('content')
    @classmethod
    def validate_content(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            return v.strip()
        return v


class TodoListResponse(BaseModel):
    """TODO 列表响应"""
    entries: List[TodoEntry] = Field(
        ...,
        description="条目列表"
    )
    total: int = Field(
        ...,
        description="总条数"
    )
    has_more: bool = Field(
        ...,
        description="是否有更多"
    )


class TodoListParams(BaseModel):
    """TODO 列表查询参数"""
    date: Optional[str] = Field(
        None,
        description="日期过滤，YYYY-MM-DD 格式，默认今天"
    )
    entry_type: Optional[TodoType] = Field(
        None,
        description="类型过滤"
    )
    status: Optional[TodoStatus] = Field(
        None,
        description="状态过滤"
    )
    limit: int = Field(
        default=50,
        ge=1,
        le=100,
        description="每页条数"
    )
    offset: int = Field(
        default=0,
        ge=0,
        description="偏移量"
    )
