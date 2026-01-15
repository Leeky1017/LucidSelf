"""
Cross Validator - 多体系交叉验证器

计算不同体系对同一维度判断的一致性。

对照 design.md §2.3 CrossValidator
对照 Requirements 2.1-2.5
"""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import Dict, List, Tuple

from backend.integration.models import LEVEL_MAP, WeightedResult

logger = logging.getLogger(__name__)


class CrossValidator:
    """
    多体系交叉验证器
    
    职责：
    - 计算多体系一致性分数 (Requirement 2.1)
    - 维度级别一致性检查 (Requirement 2.2)
    - 生成置信度矩阵 (Requirement 2.3)
    - 标记高/低置信度维度 (Requirement 2.4, 2.5)
    
    对照 design.md §2.3
    """
    
    HIGH_CONFIDENCE_THRESHOLD: int = 3
    """≥3 个引擎一致时标记 HIGH (Requirement 2.4)"""
    
    LOW_CONSISTENCY_THRESHOLD: float = 0.5
    """一致性 <0.5 时生成警告 (Requirement 2.5)"""
    
    def validate(
        self,
        weighted_results: List[WeightedResult],
    ) -> Tuple[float, Dict[str, float]]:
        """
        计算交叉验证分数和置信度矩阵
        
        对照 Requirement 2.1, 2.3
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            Tuple of (cv_score, confidence_matrix)
            - cv_score: 综合一致性分数 [0.0, 1.0]
            - confidence_matrix: 维度 → 置信度的映射
        """
        # 按维度分组
        by_dimension = self._group_by_dimension(weighted_results)
        
        # 计算每个维度的一致性
        confidence_matrix: Dict[str, float] = {}
        consistencies: List[float] = []
        
        for dim, results in by_dimension.items():
            engines = set(r.engine_id for r in results)
            
            # 至少需要 2 个引擎才能计算一致性
            if len(engines) >= 2:
                consistency = self._calculate_consistency(results)
                confidence_matrix[dim] = consistency
                consistencies.append(consistency)
            elif len(engines) == 1:
                # 单引擎，使用该引擎的置信度
                avg_confidence = sum(r.result.confidence for r in results) / len(results)
                confidence_matrix[dim] = avg_confidence
        
        # 综合分数 (Requirement 2.1)
        cv_score = sum(consistencies) / len(consistencies) if consistencies else 0.0
        
        return cv_score, confidence_matrix
    
    def _group_by_dimension(
        self,
        weighted_results: List[WeightedResult],
    ) -> Dict[str, List[WeightedResult]]:
        """
        按维度分组结果
        
        对照 Requirement 2.2
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            维度 → 结果列表的映射
        """
        by_dimension: Dict[str, List[WeightedResult]] = defaultdict(list)
        
        for wr in weighted_results:
            if wr.result.dimension:
                by_dimension[wr.result.dimension].append(wr)
        
        return dict(by_dimension)
    
    def _calculate_consistency(
        self,
        results: List[WeightedResult],
    ) -> float:
        """
        计算同一维度不同引擎的一致性
        
        使用级别方差的反向指标：
        - 所有引擎给出相同级别 → 一致性 = 1.0
        - 级别差异越大 → 一致性越低
        
        对照 Requirement 2.1
        对照 design.md §2.3 _calculate_consistency
        
        Args:
            results: 同一维度的结果列表
            
        Returns:
            一致性分数 [0.0, 1.0]
        """
        levels = [r.result.level for r in results if r.result.level]
        
        if not levels:
            return 0.0
        
        # 级别转数值
        level_values = [LEVEL_MAP.get(level, 0) for level in levels]
        
        if len(level_values) <= 1:
            return 1.0  # 单个值，完全一致
        
        # 计算方差
        mean_val = sum(level_values) / len(level_values)
        variance = sum((v - mean_val) ** 2 for v in level_values) / len(level_values)
        
        # 归一化到 [0, 1]
        # 最大可能方差 = (2 - (-2))^2 / 2 = 8 (大吉 vs 大凶)
        max_variance = 8.0
        consistency = max(0.0, 1.0 - variance / max_variance)
        
        return consistency
    
    def get_high_confidence_dimensions(
        self,
        weighted_results: List[WeightedResult],
    ) -> List[str]:
        """
        获取高置信度维度列表
        
        ≥3 个引擎对同一维度给出一致判断时标记 HIGH
        
        对照 Requirement 2.4
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            高置信度维度列表
        """
        by_dimension = self._group_by_dimension(weighted_results)
        high_confidence_dims: List[str] = []
        
        for dim, results in by_dimension.items():
            engines = set(r.engine_id for r in results)
            
            if len(engines) >= self.HIGH_CONFIDENCE_THRESHOLD:
                consistency = self._calculate_consistency(results)
                if consistency >= 0.8:  # 高一致性阈值
                    high_confidence_dims.append(dim)
        
        return high_confidence_dims
    
    def get_low_consistency_warnings(
        self,
        confidence_matrix: Dict[str, float],
    ) -> List[str]:
        """
        获取低一致性警告列表
        
        对照 Requirement 2.5
        
        Args:
            confidence_matrix: 维度 → 置信度的映射
            
        Returns:
            低一致性维度列表
        """
        return [
            dim for dim, consistency in confidence_matrix.items()
            if consistency < self.LOW_CONSISTENCY_THRESHOLD
        ]
