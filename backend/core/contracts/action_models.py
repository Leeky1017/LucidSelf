"""
Action Models for LucidSelf Contracts

行动层模型定义，包括 ActionProject、ActionItem、编译状态等。

对照 Phase 5.5 Spec:
- requirements.md §1: Action Contracts 需求
- design.md §2: 数据模型设计

设计原则:
- Action 层与 Memory 层解耦，不继承 MemoryBase
- 通过 ActionSourceRef 引用建立与 Insight/Playbook 的关系
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


# =============================================================================
# ID 格式常量
# =============================================================================

ACTION_PROJECT_ID_PATTERN = r"^proj_[a-z0-9]{12}$"
ACTION_ITEM_ID_PATTERN = r"^item_[a-z0-9]{12}$"


# =============================================================================
# 枚举定义 (Requirements 1.5)
# =============================================================================


class ActionSourceKind(str, Enum):
    """
    行动来源类型
    
    对照 Requirements 1.5.5
    """
    PLAYBOOK = "playbook"   # Playbook 建议
    DREAM = "dream"         # 梦境解析
    ASTRO = "astro"         # 命盘分析
    HEALTH = "health"       # 健康建议
    MANUAL = "manual"       # 手动添加
    INSIGHT = "insight"     # 洞察派生


class ActionTimeScope(str, Enum):
    """
    行动时间范围
    
    对照 Requirements 1.5.1
    """
    TODAY = "today"
    THIS_WEEK = "this_week"
    THIS_MONTH = "this_month"


class ActionContext(str, Enum):
    """
    行动执行场景
    
    对照 Requirements 1.5.2
    """
    DESK = "desk"           # 需要电脑/桌面
    PHONE = "phone"         # 手机即可
    OUTDOOR = "outdoor"     # 需要外出
    TALK = "talk"           # 需要与人沟通
    REST = "rest"           # 休息/放松类


class ActionStatus(str, Enum):
    """
    行动状态
    
    对照 Requirements 1.5.3
    状态流转: TODO → DOING → DONE/SKIPPED/EXPIRED
    """
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    SKIPPED = "skipped"
    EXPIRED = "expired"


class EffortEstimate(str, Enum):
    """
    预估耗时
    
    对照 Requirements 1.5.4
    """
    QUICK = "15min"
    SHORT = "30min"
    MEDIUM = "60min"
    LONG = "90min+"


class InsightCompileStatus(str, Enum):
    """
    Insight 的编译状态
    
    对照 Requirements 2.3.1
    在 Action 层独立维护，不扩展 MemoryInsight 模型
    """
    NEW = "new"                     # 新生成，未编译
    COMPILED = "compiled"           # 已编译为 Action（短期 Insight）
    TEMPLATE_CREATED = "template"   # 已创建模板（长期 Insight）
    ARCHIVED = "archived"           # 已归档，不再参与编译


# =============================================================================
# ActionBase 轻量基类 (Requirements 1.1)
# =============================================================================


class ActionBase(BaseModel):
    """
    Action 层的轻量基类
    
    设计原则：与 MemoryBase 解耦，避免 Memory 层变化影响 Action 层
    
    对照 Requirements 1.1.1-1.1.3:
    - 不继承 MemoryBase
    - 子类使用专用 ID 字段 (project_id, item_id)
    """
    user_id: str = Field(..., description="用户ID")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "user_id": "user_12345",
                "created_at": "2025-12-06T15:00:00",
                "updated_at": "2025-12-06T15:00:00",
            }
        }
    )


# =============================================================================
# ActionSourceRef 来源引用 (Requirements 1.2)
# =============================================================================


class ActionSourceRef(BaseModel):
    """
    行动来源引用
    
    通过引用而非继承建立与 Insight/Playbook 的关系
    
    对照 Requirements 1.2.1-1.2.3
    """
    kind: ActionSourceKind = Field(..., description="来源类型")
    source_id: str = Field(..., description="来源记录ID")
    source_summary: str = Field(
        ..., 
        max_length=100, 
        description="来源摘要，如'命盘显示本周沟通运强'"
    )
    
    # 可选的细粒度追溯
    factor_ids: List[str] = Field(
        default_factory=list, 
        description="关联的因子ID列表"
    )
    rule_ids: List[str] = Field(
        default_factory=list, 
        description="关联的规则ID列表"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "kind": "playbook",
                "source_id": "pb_abc123456789",
                "source_summary": "每周运势建议加强沟通",
                "factor_ids": ["day_master_jia"],
                "rule_ids": ["dts_jia_spring_001"],
            }
        }
    )


# =============================================================================
# ActionProject 行动项目 (Requirements 1.3)
# =============================================================================


class ActionProject(ActionBase):
    """
    行动项目
    
    一个 Project 代表一个目标领域，如"LS引擎开发"、"身体恢复"
    
    对照 Requirements 1.3.1-1.3.5
    """
    project_id: str = Field(
        ..., 
        pattern=ACTION_PROJECT_ID_PATTERN,
        description="项目ID，格式 proj_xxxxxxxxxxxx"
    )
    
    # 基本信息
    title: str = Field(
        ..., 
        max_length=50, 
        description="项目标题，如'本周沟通突破'"
    )
    time_scope: ActionTimeScope = Field(..., description="时间范围")
    
    # 来源（可多源聚合）
    sources: List[ActionSourceRef] = Field(
        default_factory=list, 
        description="来源引用列表，支持多源聚合"
    )
    
    # 状态
    status: Literal["active", "completed", "archived"] = Field(
        default="active", 
        description="项目状态"
    )
    
    # 生成元信息
    llm_generated: bool = Field(
        default=True, 
        description="是否由 LLM 生成"
    )
    llm_call_id: Optional[str] = Field(
        None, 
        description="关联的 LLM 调用记录ID，用于追溯"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "project_id": "proj_abc123456789",
                "user_id": "user_12345",
                "title": "本周沟通突破",
                "time_scope": "this_week",
                "sources": [
                    {
                        "kind": "playbook",
                        "source_id": "pb_xyz",
                        "source_summary": "沟通运强",
                    }
                ],
                "status": "active",
                "llm_generated": True,
                "created_at": "2025-12-06T15:00:00",
                "updated_at": "2025-12-06T15:00:00",
            }
        }
    )


# =============================================================================
# ActionItem 行动条目 (Requirements 1.4)
# =============================================================================


class ActionItem(ActionBase):
    """
    行动条目（Level 1 版本）
    
    包含内联的反馈字段，避免早期引入独立 Feedback 表
    
    对照 Requirements 1.4.1-1.4.6
    """
    item_id: str = Field(
        ..., 
        pattern=ACTION_ITEM_ID_PATTERN,
        description="条目ID，格式 item_xxxxxxxxxxxx"
    )
    project_id: str = Field(..., description="所属项目ID")
    
    # 核心内容
    title: str = Field(
        ..., 
        max_length=60, 
        description="行为动词开头，如'联系张经理讨论合作'"
    )
    description: Optional[str] = Field(
        None, 
        max_length=200, 
        description="详细描述（可选）"
    )
    reason: str = Field(
        ..., 
        max_length=100, 
        description="追溯来源，如'命盘显示本周沟通运强'"
    )
    
    # 执行约束
    effort_estimate: EffortEstimate = Field(..., description="预估耗时")
    context: ActionContext = Field(..., description="执行场景")
    suggested_time_scope: ActionTimeScope = Field(
        default=ActionTimeScope.TODAY, 
        description="建议时间范围"
    )
    priority: int = Field(
        default=5, 
        ge=1, 
        le=10, 
        description="优先级 1-10，10最高"
    )
    
    # 来源追溯
    source: ActionSourceRef = Field(..., description="来源引用")
    
    # 状态
    status: ActionStatus = Field(
        default=ActionStatus.TODO, 
        description="当前状态"
    )
    
    # 生成元信息
    llm_generated: bool = Field(
        default=True, 
        description="是否由 LLM 生成"
    )
    
    # 时间戳
    completed_at: Optional[datetime] = Field(None, description="完成时间")
    expired_at: Optional[datetime] = Field(None, description="过期时间")
    
    # ========== 内联反馈（Level 1）==========
    # 对照 Requirements 1.4.6
    feedback_status: Optional[Literal["done", "partial", "skipped", "expired"]] = Field(
        None, 
        description="反馈状态"
    )
    feedback_note: Optional[str] = Field(
        None, 
        max_length=200, 
        description="反馈备注（可选）"
    )
    feedback_at: Optional[datetime] = Field(None, description="反馈时间")
    actual_effort_minutes: Optional[int] = Field(
        None, 
        ge=0,
        description="实际耗时（分钟）"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "item_id": "item_abc123456789",
                "project_id": "proj_abc123456789",
                "user_id": "user_12345",
                "title": "联系张经理讨论合作",
                "reason": "命盘显示本周沟通运强",
                "effort_estimate": "30min",
                "context": "talk",
                "suggested_time_scope": "today",
                "priority": 7,
                "source": {
                    "kind": "playbook",
                    "source_id": "pb_xyz",
                    "source_summary": "沟通运强",
                },
                "status": "todo",
                "llm_generated": True,
                "created_at": "2025-12-06T15:00:00",
                "updated_at": "2025-12-06T15:00:00",
            }
        }
    )


# =============================================================================
# InsightCompileRecord 编译记录 (Requirements 2.3.5)
# =============================================================================


class InsightCompileRecord(BaseModel):
    """
    Insight 编译记录
    
    在 Action 层独立维护，不扩展 MemoryInsight 模型
    
    对照 Requirements 2.3.5
    """
    insight_id: str = Field(..., description="关联的 Insight ID")
    status: InsightCompileStatus = Field(
        default=InsightCompileStatus.NEW,
        description="编译状态"
    )
    compiled_at: Optional[datetime] = Field(None, description="编译时间")
    compile_session_id: Optional[str] = Field(
        None, 
        description="编译会话 ID，用于追溯"
    )
    created_at: datetime = Field(
        default_factory=datetime.now, 
        description="记录创建时间"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "insight_id": "ins_xyz987654321",
                "status": "compiled",
                "compiled_at": "2025-12-06T15:00:00",
                "compile_session_id": "sess_abc123",
                "created_at": "2025-12-06T14:00:00",
            }
        }
    )


# =============================================================================
# AvoidanceInsight 回避洞察 (Requirements 3.4)
# =============================================================================


class AvoidanceInsight(BaseModel):
    """
    回避型 Insight，供 Playbook 读取
    
    当连续 3 周回避同类 Action 时生成
    
    对照 Requirements 3.4.1-3.4.3
    """
    insight_id: str = Field(..., description="洞察ID")
    user_id: str = Field(..., description="用户ID")
    insight_type: Literal["avoidance_pattern"] = Field(
        default="avoidance_pattern",
        description="洞察类型，固定为 avoidance_pattern"
    )
    
    # 回避模式
    pattern: str = Field(
        ..., 
        description="回避模式: desk_avoidance | health_avoidance | effort_avoidance | source_bias"
    )
    confidence: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="置信度 0.0-1.0"
    )
    
    # 详细信息
    affected_contexts: List[str] = Field(
        default_factory=list, 
        description="受影响的场景"
    )
    affected_areas: List[str] = Field(
        default_factory=list, 
        description="受影响的领域"
    )
    affected_efforts: List[str] = Field(
        default_factory=list, 
        description="受影响的耗时等级"
    )
    low_completion_sources: List[str] = Field(
        default_factory=list, 
        description="低完成率的来源"
    )
    
    # 统计依据
    sample_period_weeks: int = Field(..., description="样本周期（周）")
    sample_count: int = Field(..., description="样本数量")
    completion_rate: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="完成率 0.0-1.0"
    )
    
    # 时间戳
    detected_at: datetime = Field(..., description="检测时间")
    
    # 可被 Playbook 消费
    playbook_consumable: bool = Field(
        default=True, 
        description="是否可被 Playbook 消费"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "insight_id": "ins_avoid123456",
                "user_id": "user_12345",
                "insight_type": "avoidance_pattern",
                "pattern": "desk_avoidance",
                "confidence": 0.85,
                "affected_contexts": ["desk"],
                "affected_areas": [],
                "affected_efforts": [],
                "low_completion_sources": [],
                "sample_period_weeks": 3,
                "sample_count": 12,
                "completion_rate": 0.25,
                "detected_at": "2025-12-06T15:00:00",
                "playbook_consumable": True,
            }
        }
    )
