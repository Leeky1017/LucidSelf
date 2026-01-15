"""
Runtime Models for LucidSelf Contracts

运行态模型定义，用于 Engine Layer 1-4 执行时的数据结构。
对照文档: docs/数据契约_Schema定义规范_v1.md §1.1, §2.1

v0.9.0 更新：
- RuntimeRuleResult 新增 cross_domain_axes 字段（schema-core spec v0.4.0 要求）
"""

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from backend.core.contracts.cross_domain_models import CrossDomainAxes

# 延迟导入，避免循环依赖
def _get_cross_domain_axes():
    from backend.core.contracts.cross_domain_models import CrossDomainAxes
    return CrossDomainAxes


# =============================================================================
# 因子运行态模型 (§1.1)
# =============================================================================


class FactorValue(BaseModel):
    """
    运行态因子值
    
    Calculator 层计算产出的单个因子值。
    对照文档 §1.1 FactorValue
    """
    factor_id: str = Field(..., description="因子ID")
    value: Any = Field(..., description="因子值，类型取决于 ConfigFactor.value_type")
    confidence: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="置信度 0.0-1.0"
    )
    source: str = Field(
        ..., 
        description="计算源：calculator/semantic/manual"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "factor_id": "day_master_jia",
                "value": True,
                "confidence": 1.0,
                "source": "calculator"
            }
        }
    )


class FactorMatrix(BaseModel):
    """
    运行态因子矩阵
    
    完整的因子集合，聚合多个 Calculator 的输出。
    对照文档 §1.1 FactorMatrix
    """
    factors: Dict[str, FactorValue] = Field(
        ..., 
        description="因子字典，按 factor_id 索引"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now, 
        description="计算时间戳"
    )
    engine_id: str = Field(..., description="主引擎ID")

    def get(self, factor_id: str) -> Optional[FactorValue]:
        """获取指定因子值"""
        return self.factors.get(factor_id)

    def has(self, factor_id: str) -> bool:
        """检查因子是否存在"""
        return factor_id in self.factors

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "factors": {
                    "day_master_jia": {
                        "factor_id": "day_master_jia",
                        "value": True,
                        "confidence": 1.0,
                        "source": "calculator"
                    },
                    "season": {
                        "factor_id": "season",
                        "value": "spring",
                        "confidence": 1.0,
                        "source": "calculator"
                    }
                },
                "timestamp": "2025-11-25T14:00:00",
                "engine_id": "bazi_calculator"
            }
        }
    )


# =============================================================================
# 规则运行态模型 (§2.1)
# =============================================================================


class RuntimeRuleResult(BaseModel):
    """
    运行态规则执行结果
    
    Rule Engine 实际返回的结果，包含执行时元数据。
    对照文档 §2.1 RuntimeRuleResult
    """
    rule_id: str = Field(..., description="规则ID")
    matched: bool = Field(..., description="是否匹配")
    
    # 仅匹配时填充
    dimension: Optional[str] = Field(None, description="维度")
    level: Optional[str] = Field(None, description="吉凶等级")
    description: Optional[str] = Field(
        None, 
        description="模板渲染后的成品文案"
    )
    
    # 运行时元数据
    confidence: float = Field(..., ge=0.0, le=1.0, description="置信度 0.0-1.0")
    weight: float = Field(..., ge=0.0, le=10.0, description="权重 0.0-10.0")
    tags: List[str] = Field(default_factory=list, description="标签列表")
    evidence_factors: List[str] = Field(
        default_factory=list, 
        description="证据因子ID列表"
    )
    semantic_refs: List[str] = Field(
        default_factory=list, 
        description="关联的语义条目ID"
    )
    
    # 溯源信息
    source_book: Optional[str] = Field(None, description="来源书籍")
    l1_anchor: Optional[str] = Field(None, description="L1 锚点")
    execution_time_ms: float = Field(..., description="执行耗时（毫秒）")
    
    # 跨域轴标注（schema-core spec v0.4.0 要求）
    cross_domain_axes: Optional["CrossDomainAxes"] = Field(
        None,
        description="跨域轴标注，用于多体系结果融合"
    )

    @classmethod
    def not_matched(cls, rule_id: str, execution_time_ms: float) -> "RuntimeRuleResult":
        """创建未匹配结果的快捷方法"""
        return cls(
            rule_id=rule_id,
            matched=False,
            confidence=1.0,
            weight=0.0,
            tags=[],
            evidence_factors=[],
            execution_time_ms=execution_time_ms
        )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "rule_id": "dts_jia_spring_001",
                "matched": True,
                "dimension": "personality",
                "level": "吉",
                "description": "甲木生于春季，木气当令，性格积极向上",
                "confidence": 0.85,
                "weight": 1.5,
                "tags": ["personality", "positive"],
                "evidence_factors": ["day_master_jia", "season_spring"],
                "semantic_refs": ["bazi_semantic_001"],
                "source_book": "ditianshui",
                "l1_anchor": "DTS_L1_025",
                "execution_time_ms": 2.5,
                "cross_domain_axes": {
                    "life_domain": ["career"],
                    "time_horizon": "long_term",
                    "advice_type": ["reflection"]
                }
            }
        }
    )


# 导入并重建模型以解析前向引用
from backend.core.contracts.cross_domain_models import CrossDomainAxes  # noqa: E402
RuntimeRuleResult.model_rebuild()
