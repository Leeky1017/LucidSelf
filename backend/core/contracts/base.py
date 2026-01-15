"""
Base Types for LucidSelf Contracts

基础类型定义，包括枚举、元数据模型和公共校验器。
对照文档: docs/数据契约_Schema定义规范_v1.md §1.1
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

# =============================================================================
# 公共正则模式
# =============================================================================

FACTOR_ID_PATTERN = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
"""因子ID正则: 字母或下划线开头，允许字母、数字、下划线"""

RULE_ID_PATTERN = r"^[a-z][a-z0-9_]*$"
"""规则ID正则: 与因子ID相同"""

ENGINE_ID_PATTERN = r"^[a-z][a-z0-9_-]*$"
"""引擎ID正则: 小写字母开头，允许字母、数字、下划线、连字符"""

VERSION_PATTERN = r"^\d+\.\d+\.\d+$"
"""版本号正则: 语义化版本 x.y.z"""

FUSION_ID_PATTERN = r"^fus_[a-z0-9]{12}$"
"""融合ID正则: fus_ 前缀 + 12位小写字母数字"""

EVENT_ID_PATTERN = r"^evt_[a-z0-9]{12}$"
"""事件ID正则: evt_ 前缀 + 12位小写字母数字"""

INSIGHT_ID_PATTERN = r"^ins_[a-z0-9]{12}$"
"""洞察ID正则: ins_ 前缀 + 12位小写字母数字"""

LOCALE_PATTERN = r"^[a-z]{2}-[A-Z]{2}$"
"""地区代码正则: xx-XX 格式，如 zh-CN"""


# =============================================================================
# 枚举定义
# =============================================================================


class FactorCategory(str, Enum):
    """
    因子类别枚举
    
    对照文档 §1.1 FactorCategory
    """
    STRUCTURE = "structure"    # 结构类：命盘结构、宫位、牌阵等
    TIME = "time"              # 时间类：季节、流年、大运等
    RELATION = "relation"      # 关系类：十神、相位、牌间关系等
    CONDITION = "condition"    # 条件类：触发条件、状态判断
    ENERGY = "energy"          # 能量类：五行强弱、元素能量
    STATE = "state"            # 状态类：身强身弱、正逆位
    PRINCIPLE = "principle"    # 原理类：核心法则、基础理论


class StatusEnum(str, Enum):
    """
    状态枚举
    
    用于 ConfigFactor, ConfigRuleDefinition 等配置态模型的状态字段
    """
    ACTIVE = "active"              # 活跃：正式使用
    EXPERIMENTAL = "experimental"  # 实验：测试中，可能变更
    DEPRECATED = "deprecated"      # 废弃：保留但不推荐使用


# =============================================================================
# 元数据模型
# =============================================================================


class SourceMetadata(BaseModel):
    """
    溯源元数据
    
    记录因子或规则的来源信息，支持从典籍追溯到具体章节。
    对照文档 §1.1 SourceMetadata
    """
    book_id: str = Field(
        ..., 
        description="来源书籍ID，如 'sanmingtonghui', 'waite_pictorial_key'"
    )
    chapter: Optional[str] = Field(
        None, 
        description="章节标识，如 '卷一', 'Major Arcana'"
    )
    l1_anchor: str = Field(
        ..., 
        description="Content-L1 锚点，精确定位到原文位置"
    )
    extraction_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), 
        description="提取日期 (UTC)"
    )
    extraction_tool_version: Optional[str] = Field(
        None, 
        description="提取工具版本，如 'agent_v1.0', 'manual'"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "book_id": "ditianshui",
                "chapter": "下卷",
                "l1_anchor": "DTS_L1_025",
                "extraction_date": "2025-11-25T13:45:00",
                "extraction_tool_version": "agent_v1.0"
            }
        }
    )
