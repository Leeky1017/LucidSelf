"""
Engine Models for LucidSelf Contracts

引擎注册表模型定义，统一管理多体系引擎的元信息与状态。
对照文档: docs/数据契约_Schema定义规范_v1.md §9.5
"""

from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

from backend.core.contracts.base import ENGINE_ID_PATTERN, VERSION_PATTERN, StatusEnum


# =============================================================================
# 引擎描述符 (§9.5)
# =============================================================================


class EngineDescriptor(BaseModel):
    """
    引擎描述符 - 引擎注册表核心模型
    
    用于统一管理所有引擎的元信息与状态。
    对照文档 §9.5 EngineDescriptor
    """
    engine_id: str = Field(
        ...,
        pattern=ENGINE_ID_PATTERN,
        description="引擎唯一标识，小写字母开头"
    )
    
    kind: Literal["calculator", "semantic", "rule", "fusion"] = Field(
        ...,
        description="引擎类型：calculator(L1)/semantic(L2)/rule(L3)/fusion(L4)"
    )
    
    # 能力声明
    supported_dimensions: List[str] = Field(
        ...,
        description="支持的维度：事业、财富、婚姻、健康等"
    )
    
    supported_systems: List[str] = Field(
        ...,
        description="支持的体系：bazi/tarot/astro/dream/ziwei/yijing"
    )
    
    # 依赖声明
    depends_on: List[str] = Field(
        default_factory=list,
        description="依赖的引擎ID列表，如fusion引擎依赖哪些rule引擎"
    )
    
    # 默认配置
    default_weight: float = Field(
        default=1.0,
        ge=0.0,
        le=10.0,
        description="融合时的默认权重"
    )
    
    # 状态管理
    status: StatusEnum = Field(
        default=StatusEnum.ACTIVE,
        description="引擎状态"
    )
    
    # 责任归属
    owner_team: str = Field(
        ...,
        description="负责团队：content/engine/product"
    )
    
    # 版本信息
    version: str = Field(
        ..., 
        pattern=VERSION_PATTERN,
        description="引擎版本 x.y.z"
    )
    created_at: datetime = Field(
        default_factory=datetime.now, 
        description="创建时间"
    )
    updated_at: datetime = Field(
        default_factory=datetime.now, 
        description="更新时间"
    )
    
    # 性能指标
    avg_execution_time_ms: Optional[float] = Field(
        None,
        ge=0.0,
        description="平均执行时间（毫秒）"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "engine_id": "bazi_rule_engine",
                "kind": "rule",
                "supported_dimensions": ["事业", "财富", "婚姻", "健康"],
                "supported_systems": ["bazi"],
                "depends_on": ["bazi_calculator", "bazi_semantic"],
                "default_weight": 1.5,
                "status": "active",
                "owner_team": "content",
                "version": "1.2.0",
                "created_at": "2025-01-01T00:00:00",
                "updated_at": "2025-11-25T00:00:00",
                "avg_execution_time_ms": 15.5
            }
        }
    )


# =============================================================================
# 引擎注册约束 (§9.5)
# =============================================================================

ENGINE_REGISTRY_CONSTRAINTS: List[str] = [
    "PreferenceManager和FusionEngine只接受engine_id属于注册表中的引擎",
    "新增体系（例如新塔罗引擎）必须先在EngineDescriptor注册",
    "引擎状态变更必须通过版本升级体现",
    "deprecated引擎必须保留至少两个版本周期",
    "所有ConfigFactor和ConfigRuleDefinition必须指定engine_id",
]
"""引擎注册约束规则"""


# =============================================================================
# 预定义引擎类型 (§9.5)
# =============================================================================

ENGINE_KINDS: List[str] = [
    "calculator",  # Layer 1: 计算器（因子提取）
    "semantic",    # Layer 2: 语义引擎（语义解析）
    "rule",        # Layer 3: 规则引擎（推理匹配）
    "fusion",      # Layer 4: 融合引擎（多引擎融合）
]
"""引擎类型列表"""

SUPPORTED_SYSTEMS: List[str] = [
    "bazi",        # 八字
    "ziwei",       # 紫微斗数
    "yijing",      # 易经
    "astro",       # 占星 (对齐 backend/calculators/astro/)
    "tarot",       # 塔罗
    "dream",       # 解梦
    "psychology",  # 心理学（跨体系底层）
]
"""支持的体系列表"""
