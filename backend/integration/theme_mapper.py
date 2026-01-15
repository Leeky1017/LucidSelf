"""
Theme Mapper - 跨体系主题映射器

从多引擎结果中提取共通主题。

对照 design.md §2.4 ThemeMapper
对照 Requirements 3.1-3.5

更新: 使用 unified_dimensions 模块的 DimensionRegistry
"""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import Dict, List, Optional

from backend.core.contracts.unified_dimensions import (
    AnalysisDimension,
    ANALYSIS_DIMENSION_LABELS,
    DimensionRegistry,
)
from backend.integration.models import WeightedResult

logger = logging.getLogger(__name__)


class ThemeMapper:
    """
    跨体系主题映射器
    
    使用 DimensionRegistry 进行维度标准化。
    
    职责：
    - 提取跨体系共通主题 (Requirement 3.1)
    - 支持 10 种标准维度映射 (Requirement 3.2)
    - 主题聚类与去重 (Requirement 3.3)
    - 主题排序 (Requirement 3.4)
    
    对照 design.md §2.4
    """
    
    MAX_THEMES: int = 5
    """最大主题数量 (Requirement 7.2: 1-5 个)"""
    
    def __init__(self):
        """初始化主题映射器"""
        pass  # 使用 DimensionRegistry 静态方法，无需实例变量
    
    def extract_themes(
        self,
        weighted_results: List[WeightedResult],
    ) -> List[str]:
        """
        提取主要主题
        
        按维度聚合分数，返回分数最高的主题。
        
        对照 Requirement 3.1, 3.4
        对照 design.md §2.4 extract_themes
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            主题列表 (1-5 个，按分数排序)
        """
        if not weighted_results:
            return []
        
        # 按维度聚合分数 (Requirement 3.1)
        dimension_scores: Dict[str, float] = defaultdict(float)
        
        for wr in weighted_results:
            if wr.result.dimension:
                # 使用 DimensionRegistry 进行标准化 (Requirement 3.2)
                dim = DimensionRegistry.normalize_dimension(wr.result.dimension)
                dimension_scores[dim.value] += wr.final_score
        
        if not dimension_scores:
            return []
        
        # 按分数排序 (Requirement 3.4)
        sorted_dims = sorted(
            dimension_scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        
        # 返回前 MAX_THEMES 个主题（转中文标签）
        themes = []
        for dim_value, _ in sorted_dims[:self.MAX_THEMES]:
            try:
                dim_enum = AnalysisDimension(dim_value)
                label = DimensionRegistry.get_analysis_dimension_label(dim_enum, "zh")
                themes.append(label)
            except ValueError:
                themes.append(dim_value)  # fallback
        
        # 去重 (Requirement 3.3)
        return self._deduplicate_themes(themes)
    
    def _deduplicate_themes(self, themes: List[str]) -> List[str]:
        """
        主题去重
        
        保持顺序的去重。
        
        对照 Requirement 3.3
        
        Args:
            themes: 主题列表
            
        Returns:
            去重后的主题列表
        """
        seen = set()
        deduped = []
        
        for theme in themes:
            if theme not in seen:
                seen.add(theme)
                deduped.append(theme)
        
        return deduped
    
    def get_dimension_breakdown(
        self,
        weighted_results: List[WeightedResult],
    ) -> Dict[str, Dict[str, float]]:
        """
        获取维度分解
        
        返回每个维度的引擎贡献详情。
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            维度 → {引擎ID → 分数} 的映射
        """
        breakdown: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
        
        for wr in weighted_results:
            if wr.result.dimension:
                dim = DimensionRegistry.normalize_dimension(wr.result.dimension)
                breakdown[dim.value][wr.engine_id] += wr.final_score
        
        return {dim: dict(engines) for dim, engines in breakdown.items()}

