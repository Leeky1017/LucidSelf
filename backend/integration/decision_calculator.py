"""
规则→决策维度映射与分数计算

解决 GAP-04: RuntimeRuleResult.dimension 到决策维度的映射缺失问题

对照文档: docs/ls_roadmap_executable.md §GAP-04
"""

from collections import defaultdict
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from backend.core.contracts.unified_dimensions import (
    AnalysisDimension,
    DecisionAxis,
    DOMAIN_TO_DECISION_AXES,
    DimensionRegistry,
    LifeDomain,
)


# =============================================================================
# 分析维度到决策维度的映射
# =============================================================================

# AnalysisDimension → 对应影响的 DecisionAxis.axis_id 及影响权重
ANALYSIS_TO_DECISION: Dict[AnalysisDimension, Dict[str, float]] = {
    # 事业维度影响的决策轴
    AnalysisDimension.CAREER: {
        "income_ceiling": 0.9,
        "stability": 0.7,
        "autonomy": 0.6,
        "growth_potential": 0.9,
        "social_exposure": 0.5,
        "work_life_balance": 0.4,
    },
    
    # 财富维度影响的决策轴
    AnalysisDimension.WEALTH: {
        "income_ceiling": 0.9,
        "income_growth": 0.9,
        "asset_security": 0.8,
        "liquidity": 0.6,
        "risk_tolerance": 0.7,
        "stability": 0.5,
    },
    
    # 婚姻维度影响的决策轴
    AnalysisDimension.MARRIAGE: {
        "emotional_depth": 0.9,
        "compatibility": 0.9,
        "independence": 0.6,
        "social_harmony": 0.7,
        "future_planning": 0.8,
    },
    
    # 健康维度影响的决策轴
    AnalysisDimension.HEALTH: {
        "physical_vitality": 0.9,
        "mental_wellness": 0.8,
        "lifestyle_sustainability": 0.9,
        "work_life_balance": 0.6,
    },
    
    # 性格维度影响的决策轴
    AnalysisDimension.PERSONALITY: {
        "compatibility": 0.8,
        "autonomy": 0.7,
        "independence": 0.8,
        "social_exposure": 0.6,
    },
    
    # 运势维度影响的决策轴 (通用加成)
    AnalysisDimension.FORTUNE: {
        "income_ceiling": 0.4,
        "income_growth": 0.5,
        "growth_potential": 0.5,
        "stability": 0.3,
    },
    
    # 预兆维度影响的决策轴
    AnalysisDimension.OMEN: {
        "risk_tolerance": 0.6,
        "stability": 0.4,
        "future_planning": 0.5,
    },
    
    # 指引维度影响的决策轴
    AnalysisDimension.GUIDANCE: {
        "growth_potential": 0.7,
        "future_planning": 0.7,
        "autonomy": 0.5,
    },
    
    # 潜意识维度影响的决策轴
    AnalysisDimension.UNCONSCIOUS: {
        "emotional_depth": 0.7,
        "mental_wellness": 0.7,
        "independence": 0.5,
    },
    
    # 通用维度 (弱影响)
    AnalysisDimension.GENERAL: {},
}


class DecisionContribution(BaseModel):
    """决策轴贡献"""
    axis_id: str
    raw_score: float = Field(..., description="原始累计分数")
    weighted_score: float = Field(..., description="加入影响权重后的分数")
    rule_count: int = Field(default=0, description="贡献规则数量")
    source_dimensions: List[str] = Field(default_factory=list)


class DecisionScores(BaseModel):
    """决策维度分数集合"""
    domain: LifeDomain
    scores: Dict[str, float] = Field(
        default_factory=dict,
        description="axis_id → normalized score (0-1)"
    )
    contributions: Dict[str, DecisionContribution] = Field(
        default_factory=dict,
        description="axis_id → 详细贡献信息"
    )
    confidence: float = Field(..., ge=0.0, le=1.0)


class DecisionScoreCalculator:
    """
    决策分数计算器
    
    将规则结果转换为场景决策维度的分数
    """
    
    def __init__(self, mapping: Optional[Dict] = None):
        """
        初始化计算器
        
        Args:
            mapping: 自定义 AnalysisDimension → DecisionAxis 映射
        """
        self._mapping = mapping or ANALYSIS_TO_DECISION
    
    def calculate(
        self,
        rule_results: List,
        domain: LifeDomain,
    ) -> DecisionScores:
        """
        计算场景的决策维度分数
        
        Args:
            rule_results: RuntimeRuleResult 列表
            domain: 目标生活领域
            
        Returns:
            DecisionScores 包含各决策维度的分数
        """
        # 获取该领域的决策维度
        decision_axes = DOMAIN_TO_DECISION_AXES.get(domain, [])
        axis_ids = {a.axis_id for a in decision_axes}
        
        # 累计各维度贡献
        contributions: Dict[str, Dict] = defaultdict(
            lambda: {
                "raw_score": 0.0,
                "weighted_score": 0.0,
                "rule_count": 0,
                "source_dimensions": [],
            }
        )
        
        for rule in rule_results:
            if not hasattr(rule, "dimension") or not rule.dimension:
                continue
            if not hasattr(rule, "matched") or not rule.matched:
                continue
            
            # 标准化维度
            dim = DimensionRegistry.normalize_dimension(rule.dimension)
            
            # 获取规则分数 (处理不同格式)
            rule_score = self._extract_score(rule)
            
            # 查找该分析维度影响的决策维度
            axis_weights = self._mapping.get(dim, {})
            
            for axis_id, weight in axis_weights.items():
                if axis_id not in axis_ids:
                    continue  # 只计算目标领域的决策维度
                
                contributions[axis_id]["raw_score"] += rule_score
                contributions[axis_id]["weighted_score"] += rule_score * weight
                contributions[axis_id]["rule_count"] += 1
                if dim.value not in contributions[axis_id]["source_dimensions"]:
                    contributions[axis_id]["source_dimensions"].append(dim.value)
        
        # 归一化分数到 0-1
        normalized_scores = {}
        result_contributions = {}
        
        for axis_id in axis_ids:
            if axis_id not in contributions:
                normalized_scores[axis_id] = 0.5  # 默认中等
                result_contributions[axis_id] = DecisionContribution(
                    axis_id=axis_id,
                    raw_score=0.0,
                    weighted_score=0.0,
                    rule_count=0,
                )
            else:
                c = contributions[axis_id]
                # 使用加权分数，归一化到 0-1
                # 假设规则 score 范围是 0-1，权重最大是 1.0
                if c["rule_count"] > 0:
                    avg_weighted = c["weighted_score"] / c["rule_count"]
                    normalized = min(1.0, max(0.0, avg_weighted))
                else:
                    normalized = 0.5
                
                normalized_scores[axis_id] = normalized
                result_contributions[axis_id] = DecisionContribution(
                    axis_id=axis_id,
                    raw_score=c["raw_score"],
                    weighted_score=c["weighted_score"],
                    rule_count=c["rule_count"],
                    source_dimensions=c["source_dimensions"],
                )
        
        # 计算置信度 (基于贡献规则数量)
        total_rules = sum(c.rule_count for c in result_contributions.values())
        confidence = min(1.0, total_rules / 10.0)  # 10条规则达到满置信
        
        return DecisionScores(
            domain=domain,
            scores=normalized_scores,
            contributions=result_contributions,
            confidence=confidence,
        )
    
    def _extract_score(self, rule) -> float:
        """从规则结果提取分数"""
        # 尝试多种属性名
        for attr in ["score", "confidence", "strength"]:
            if hasattr(rule, attr):
                val = getattr(rule, attr)
                if isinstance(val, (int, float)):
                    return float(val)
        # 默认
        return 0.5
    
    @staticmethod
    def get_domain_axes(domain: LifeDomain) -> List[DecisionAxis]:
        """获取领域的决策维度列表"""
        return DOMAIN_TO_DECISION_AXES.get(domain, [])
