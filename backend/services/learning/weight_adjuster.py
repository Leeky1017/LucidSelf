"""
权重调整器

基于用户反馈调整各引擎和规则的权重。

对照文档: docs/ls_roadmap_executable.md §GAP-06
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class RuleWeight(BaseModel):
    """规则权重"""
    rule_id: str
    weight: float = Field(default=1.0, ge=0.1, le=3.0)
    hit_count: int = 0
    positive_count: int = 0
    negative_count: int = 0
    effectiveness: float = Field(default=0.5, ge=0.0, le=1.0)
    last_updated: datetime = Field(default_factory=datetime.now)


class EngineWeight(BaseModel):
    """引擎权重"""
    engine_id: str
    weight: float = Field(default=1.0, ge=0.1, le=2.0)
    total_rules: int = 0
    avg_effectiveness: float = Field(default=0.5, ge=0.0, le=1.0)
    last_updated: datetime = Field(default_factory=datetime.now)


class WeightAdjuster:
    """
    权重调整器
    
    职责:
    - 追踪规则命中和反馈
    - 计算规则有效性
    - 调整规则和引擎权重
    """
    
    # 调整常数
    INITIAL_WEIGHT = 1.0
    POSITIVE_ADJUSTMENT = 0.05
    NEGATIVE_ADJUSTMENT = -0.08
    DECAY_FACTOR = 0.99  # 时间衰减
    
    def __init__(self):
        """初始化调整器"""
        self._rule_weights: Dict[str, RuleWeight] = {}
        self._engine_weights: Dict[str, EngineWeight] = {}
    
    def record_rule_hit(self, rule_id: str, engine_id: str) -> None:
        """
        记录规则命中
        
        Args:
            rule_id: 规则 ID
            engine_id: 引擎 ID
        """
        if rule_id not in self._rule_weights:
            self._rule_weights[rule_id] = RuleWeight(rule_id=rule_id)
        
        self._rule_weights[rule_id].hit_count += 1
        self._rule_weights[rule_id].last_updated = datetime.now()
        
        # 确保引擎存在
        if engine_id not in self._engine_weights:
            self._engine_weights[engine_id] = EngineWeight(engine_id=engine_id)
    
    def record_rule_feedback(
        self,
        rule_id: str,
        is_positive: bool,
    ) -> None:
        """
        记录规则反馈
        
        Args:
            rule_id: 规则 ID
            is_positive: 是否正面反馈
        """
        if rule_id not in self._rule_weights:
            self._rule_weights[rule_id] = RuleWeight(rule_id=rule_id)
        
        rw = self._rule_weights[rule_id]
        
        if is_positive:
            rw.positive_count += 1
            rw.weight = min(3.0, rw.weight + self.POSITIVE_ADJUSTMENT)
        else:
            rw.negative_count += 1
            rw.weight = max(0.1, rw.weight + self.NEGATIVE_ADJUSTMENT)
        
        # 重新计算有效性
        total_feedback = rw.positive_count + rw.negative_count
        if total_feedback > 0:
            rw.effectiveness = rw.positive_count / total_feedback
        
        rw.last_updated = datetime.now()
        logger.debug(f"Rule {rule_id} weight adjusted to {rw.weight:.3f}")
    
    def get_rule_weight(self, rule_id: str) -> float:
        """获取规则权重"""
        if rule_id in self._rule_weights:
            return self._rule_weights[rule_id].weight
        return self.INITIAL_WEIGHT
    
    def get_rule_effectiveness(self, rule_id: str) -> float:
        """获取规则有效性"""
        if rule_id in self._rule_weights:
            return self._rule_weights[rule_id].effectiveness
        return 0.5
    
    def get_engine_weight(self, engine_id: str) -> float:
        """获取引擎权重"""
        if engine_id in self._engine_weights:
            return self._engine_weights[engine_id].weight
        return self.INITIAL_WEIGHT
    
    def update_engine_weights(self) -> None:
        """
        更新引擎权重
        
        基于其规则的平均有效性
        """
        # 统计每个引擎的规则有效性
        engine_stats: Dict[str, List[float]] = {}
        
        for rule_id, rw in self._rule_weights.items():
            # 简单假设规则ID前缀是引擎ID
            engine_id = rule_id.split("_")[0] if "_" in rule_id else "default"
            
            if engine_id not in engine_stats:
                engine_stats[engine_id] = []
            engine_stats[engine_id].append(rw.effectiveness)
        
        for engine_id, effectiveness_list in engine_stats.items():
            if engine_id not in self._engine_weights:
                self._engine_weights[engine_id] = EngineWeight(engine_id=engine_id)
            
            ew = self._engine_weights[engine_id]
            ew.total_rules = len(effectiveness_list)
            ew.avg_effectiveness = sum(effectiveness_list) / len(effectiveness_list)
            
            # 有效性高的引擎权重提升
            ew.weight = 0.5 + ew.avg_effectiveness
            ew.last_updated = datetime.now()
    
    def get_all_rule_weights(self) -> Dict[str, RuleWeight]:
        """获取所有规则权重"""
        return dict(self._rule_weights)
    
    def get_all_engine_weights(self) -> Dict[str, EngineWeight]:
        """获取所有引擎权重"""
        return dict(self._engine_weights)
    
    def reset(self) -> None:
        """重置状态（用于测试）"""
        self._rule_weights.clear()
        self._engine_weights.clear()
