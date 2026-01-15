"""
Test Schema Models for LucidSelf Contracts

三层测试体系模型定义：Unit(规则级) → Integration(引擎级) → Product(叙事级)
对照文档: docs/数据契约_Schema定义规范_v1.md §8
"""

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


# =============================================================================
# 规则级测试 (§8.1 Unit)
# =============================================================================


class RuleTestCase(BaseModel):
    """
    单条规则测试用例 - Agent自动生成
    
    用于验证单条规则的匹配逻辑是否正确。
    对照文档 §8.1 RuleTestCase
    """
    test_id: str = Field(..., description="测试用例ID")
    target_rule_id: str = Field(..., description="目标规则ID")
    test_type: Literal["positive", "negative", "edge"] = Field(
        ..., 
        description="测试类型：正向/负向/边界"
    )
    
    # 输入数据
    mock_factors: Dict[str, Any] = Field(
        ..., 
        description="模拟因子值，如 {'day_master': 'jia', 'season': 'spring'}"
    )
    
    # 期望结果
    expect_hit: bool = Field(..., description="是否应该触发")
    expected_dimension: Optional[str] = Field(
        None, 
        description="期望维度，仅 expect_hit=True 时需要"
    )
    expected_level: Optional[str] = Field(
        None, 
        description="期望等级，仅 expect_hit=True 时需要"
    )
    expected_confidence_min: float = Field(
        default=0.0, 
        ge=0.0, 
        le=1.0, 
        description="期望置信度下限"
    )
    expected_confidence_max: float = Field(
        default=1.0, 
        ge=0.0, 
        le=1.0, 
        description="期望置信度上限"
    )
    
    # 溯源
    source_book: str = Field(..., description="来源书籍")
    l1_anchor: Optional[str] = Field(None, description="L1 锚点")
    description: str = Field(..., description="测试描述")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "test_id": "test_dts_jia_spring_001",
                "target_rule_id": "dts_jia_spring_001",
                "test_type": "positive",
                "mock_factors": {
                    "day_master": "jia",
                    "season": "spring",
                    "strength": "strong"
                },
                "expect_hit": True,
                "expected_dimension": "事业",
                "expected_level": "吉",
                "expected_confidence_min": 0.8,
                "expected_confidence_max": 1.0,
                "source_book": "ditianshui",
                "l1_anchor": "DTS_L1_025",
                "description": "甲木春生，得时得令，应触发"
            }
        }
    )


# =============================================================================
# 引擎级测试 (§8.2 Integration)
# =============================================================================


class GoldenCase(BaseModel):
    """
    黄金测试用例 - 多引擎集成基线
    
    用于验证多引擎协同工作的集成结果是否符合预期。
    对照文档 §8.2 GoldenCase
    """
    case_id: str = Field(..., description="测试用例ID")
    
    # 完整输入
    birth_data: Dict[str, Any] = Field(
        ..., 
        description="完整的输入数据，如出生时间、地点等"
    )
    
    # 多引擎基线
    expected_results: Dict[str, Any] = Field(
        ...,
        description="各引擎期望输出，key为engine_id"
    )
    
    # 融合基线
    expected_fusion: Dict[str, Any] = Field(
        ...,
        description="FusionResult的themes/cross_validation_score基线"
    )
    
    # 容差
    max_drift: float = Field(
        default=0.1, 
        ge=0.0, 
        le=1.0, 
        description="允许的最大漂移（0.1表示10%）"
    )
    baseline_hash: Optional[str] = Field(
        None, 
        description="基线版本哈希，用于追踪漂移"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "case_id": "golden_bazi_career_001",
                "birth_data": {
                    "year": 1990,
                    "month": 3,
                    "day": 15,
                    "hour": 10,
                    "timezone": "Asia/Shanghai"
                },
                "expected_results": {
                    "bazi_rule_engine": {
                        "hit_count": 5,
                        "top_dimensions": ["事业", "财富"]
                    },
                    "tarot_rule_engine": {
                        "hit_count": 3,
                        "top_dimensions": ["事业"]
                    }
                },
                "expected_fusion": {
                    "primary_themes": ["事业突破", "财富积累"],
                    "cross_validation_score": 0.85
                },
                "max_drift": 0.1,
                "baseline_hash": "abc123"
            }
        }
    )


# =============================================================================
# 叙事级测试 (§8.3 Product)
# =============================================================================


class NarrativeGolden(BaseModel):
    """
    叙事黄金标准 - 产品级质量验收
    
    用于验证最终产出的叙事文本是否符合产品质量标准。
    对照文档 §8.3 NarrativeGolden
    """
    golden_id: str = Field(..., description="黄金标准ID")
    
    # 输入场景
    scenario: Dict[str, Any] = Field(
        ..., 
        description="输入场景，包括用户画像、问题类型等"
    )
    
    # 期望特征
    must_include_themes: List[str] = Field(
        ...,
        description="必须出现的主题关键字"
    )
    
    forbidden_expressions: List[str] = Field(
        default_factory=list,
        description="禁用的偏差表述，如迷信用语"
    )
    
    # 质量阈值
    min_quality_score: float = Field(
        default=0.8, 
        ge=0.0, 
        le=1.0, 
        description="最低质量评分"
    )
    
    # 评估配置
    eval_model: str = Field(
        default="gpt-4", 
        description="使用的Eval-Agent模型"
    )
    
    # 历史基线
    historical_avg_score: float = Field(
        default=0.8, 
        ge=0.0, 
        le=1.0, 
        description="历史版本平均得分"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "golden_id": "narrative_career_advice_001",
                "scenario": {
                    "user_type": "career_seeker",
                    "question": "今年事业发展如何？",
                    "engines": ["bazi", "tarot"]
                },
                "must_include_themes": ["事业发展", "时机把握", "行动建议"],
                "forbidden_expressions": ["命中注定", "绝对会", "一定不会"],
                "min_quality_score": 0.85,
                "eval_model": "gpt-4",
                "historical_avg_score": 0.87
            }
        }
    )


# =============================================================================
# 测试金字塔常量 (§8.4)
# =============================================================================

TEST_PYRAMID_STANDARDS: Dict[str, Dict[str, Any]] = {
    "rule": {
        "layer": "Unit",
        "coverage_target": "100%",
        "run_frequency": "每次提交",
        "failure_action": "阻断合并"
    },
    "golden": {
        "layer": "Integration",
        "coverage_target": "核心场景100%",
        "run_frequency": "每日CI/CD",
        "failure_action": "告警+人工复核"
    },
    "narrative": {
        "layer": "Product",
        "coverage_target": "关键旅程100%",
        "run_frequency": "发布前",
        "failure_action": "阻断发布"
    }
}
"""测试金字塔验收标准"""

RELEASE_CHECKLIST: List[str] = [
    "所有RuleTestCase全部通过",
    "GoldenCase漂移 < max_drift",
    "NarrativeGolden质量 >= min_quality_score且不低于历史均值",
    "性能基准测试无明显退化",
]
"""发布前检查清单"""
