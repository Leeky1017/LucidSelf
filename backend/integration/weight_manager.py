"""
Weight Manager - 权重管理器

负责管理各引擎的融合权重，支持用户自定义权重覆盖。

对照 design.md §2.2 WeightManager
对照 Requirements 1.2.1-1.2.4
"""

from __future__ import annotations

import logging
from typing import Dict, List, Optional

from backend.core.contracts import RuntimeRuleResult
from backend.core.engines import EngineManager
from backend.integration.models import WeightedResult

logger = logging.getLogger(__name__)


class WeightManager:
    """
    权重管理器
    
    职责：
    - 管理各引擎的融合权重 (Requirement 1.2.1)
    - 支持用户自定义权重覆盖 (Requirement 1.2.2)
    - 权重归一化处理 (Requirement 1.2.3)
    
    对照 design.md §2.2
    """
    
    DEFAULT_WEIGHT: float = 1.0
    """默认引擎权重 (Requirement 1.1.5: 等权融合策略)"""
    
    def __init__(self, engine_registry: Optional[EngineManager] = None):
        """
        初始化权重管理器
        
        Args:
            engine_registry: 引擎注册表，用于获取引擎默认权重
        """
        self.engine_registry = engine_registry
    
    def apply_weights(
        self,
        results: Dict[str, List[RuntimeRuleResult]],
        user_weights: Optional[Dict[str, float]] = None,
    ) -> List[WeightedResult]:
        """
        应用权重并归一化
        
        对照 Requirement 1.2.1-1.2.3
        
        Args:
            results: 引擎ID → 规则结果列表的映射
            user_weights: 用户自定义权重覆盖
            
        Returns:
            加权后的结果列表
        """
        weighted_results: List[WeightedResult] = []
        
        for engine_id, rule_results in results.items():
            # 获取权重: 用户 > 引擎默认 > 全局默认
            weight = self._get_weight(engine_id, user_weights)
            
            for result in rule_results:
                if result.matched:
                    # 计算最终分数
                    final_score = result.confidence * result.weight * weight
                    
                    weighted_results.append(WeightedResult(
                        result=result,
                        engine_id=engine_id,
                        engine_weight=weight,
                        final_score=final_score,
                    ))
        
        # 归一化 (Requirement 1.2.3)
        return self._normalize(weighted_results)
    
    def _get_weight(
        self,
        engine_id: str,
        user_weights: Optional[Dict[str, float]] = None,
    ) -> float:
        """
        获取引擎权重
        
        优先级: 用户自定义 > 引擎默认 > 全局默认
        
        Args:
            engine_id: 引擎ID
            user_weights: 用户自定义权重
            
        Returns:
            权重值 [0.0, 10.0]
        """
        # 1. 用户自定义权重优先
        if user_weights and engine_id in user_weights:
            weight = user_weights[engine_id]
            # 确保在有效范围内
            return max(0.0, min(10.0, weight))
        
        # 2. 从引擎注册表获取默认权重
        if self.engine_registry:
            try:
                descriptor = self.engine_registry.get_engine(engine_id)
                if descriptor:
                    return descriptor.default_weight
            except Exception:
                pass
        
        # 3. 全局默认权重
        return self.DEFAULT_WEIGHT
    
    def _normalize(
        self,
        weighted_results: List[WeightedResult],
    ) -> List[WeightedResult]:
        """
        归一化权重
        
        使所有 final_score 的和为 1.0（如果有结果）
        
        对照 Requirement 1.2.3
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            归一化后的结果列表
        """
        if not weighted_results:
            return weighted_results
        
        total_score = sum(wr.final_score for wr in weighted_results)
        
        if total_score <= 0:
            return weighted_results
        
        # 创建新的归一化结果列表
        normalized = []
        for wr in weighted_results:
            normalized.append(WeightedResult(
                result=wr.result,
                engine_id=wr.engine_id,
                engine_weight=wr.engine_weight,
                final_score=wr.final_score / total_score,
            ))
        
        return normalized
