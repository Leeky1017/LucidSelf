"""
Integration Layer Internal Models

内部使用的数据模型，不对外暴露。

对照 design.md §3.1 WeightedResult
"""

from pydantic import BaseModel, Field

from backend.core.contracts import RuntimeRuleResult


class WeightedResult(BaseModel):
    """
    加权结果 - 内部使用
    
    封装 RuntimeRuleResult 及其权重信息，用于融合计算。
    
    对照 design.md §3.1
    对照 Requirements 1.2.1
    """
    result: RuntimeRuleResult = Field(..., description="原始规则结果")
    engine_id: str = Field(..., description="来源引擎ID")
    engine_weight: float = Field(
        ..., 
        ge=0.0, 
        le=10.0, 
        description="引擎权重 [0.0, 10.0]"
    )
    final_score: float = Field(
        ..., 
        ge=0.0, 
        description="最终分数 = confidence * weight * engine_weight"
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "result": {},
                "engine_id": "bazi_rule_engine",
                "engine_weight": 1.5,
                "final_score": 1.275
            }
        }
    }


# 级别映射表 (用于交叉验证)
LEVEL_MAP = {
    "大吉": 2,
    "吉": 1,
    "中等": 0,
    "凶": -1,
    "大凶": -2,
}
"""级别到数值的映射，用于计算一致性"""
