"""
版本对比器

生成版本对比矩阵和摘要。

对照文档: docs/ls_roadmap_executable.md §四、Phase 3: Life Versions 核心
"""

import logging
from typing import Dict, List

from backend.core.contracts.life_version_models import (
    LifeVersionSet,
    VersionComparison,
)

logger = logging.getLogger(__name__)


class VersionComparator:
    """
    版本对比器
    
    职责:
    - 生成对比矩阵
    - 计算差异化指标
    - 生成对比摘要
    """
    
    def compare(self, version_set: LifeVersionSet) -> VersionComparison:
        """
        生成对比视图
        
        Args:
            version_set: 版本集合
            
        Returns:
            VersionComparison 包含对比矩阵和摘要
        """
        # 构建对比矩阵
        matrix = {}
        for version in version_set.versions:
            matrix[version.version_id] = version.expected_outcomes
        
        # 计算差异化得分
        diff_score = self._calculate_overall_differentiation(version_set)
        
        # 生成摘要
        summary = self._generate_summary(version_set, diff_score)
        
        return VersionComparison(
            set_id=version_set.set_id,
            axes=version_set.comparison_axes,
            matrix=matrix,
            differentiation_score=diff_score,
            summary_zh=summary,
        )
    
    def _calculate_overall_differentiation(
        self, 
        version_set: LifeVersionSet,
    ) -> float:
        """计算整体差异化得分"""
        if len(version_set.versions) < 2:
            return 0.0
        
        total_diff = 0.0
        pair_count = 0
        
        versions = version_set.versions
        axes = version_set.comparison_axes
        
        for i, v1 in enumerate(versions):
            for j, v2 in enumerate(versions[i+1:], i+1):
                pair_diff = 0.0
                axis_count = 0
                
                for axis_id in axes:
                    s1 = v1.expected_outcomes.get(axis_id, 0.5)
                    s2 = v2.expected_outcomes.get(axis_id, 0.5)
                    pair_diff += abs(s1 - s2)
                    axis_count += 1
                
                if axis_count > 0:
                    total_diff += pair_diff / axis_count
                    pair_count += 1
        
        return total_diff / pair_count if pair_count > 0 else 0.0
    
    def _generate_summary(
        self, 
        version_set: LifeVersionSet,
        diff_score: float,
    ) -> str:
        """生成对比摘要"""
        domain_labels = {
            "career": "事业",
            "wealth": "财务",
            "relationship": "感情",
            "health": "健康",
            "family": "家庭",
            "creativity": "创造力",
            "spiritual": "精神",
        }
        
        domain_label = domain_labels.get(
            version_set.domain.value, 
            version_set.domain.value
        )
        
        version_count = len(version_set.versions)
        
        # 找出差异最大的维度
        max_diff_axis = self._find_max_diff_axis(version_set)
        
        # 基础摘要
        base_summary = f"针对{domain_label}场景，系统为您生成了{version_count}个可选方案。"
        
        # 差异化描述
        if diff_score > 0.3:
            diff_desc = "各方案在策略和预期结果上有明显差异。"
        elif diff_score > 0.15:
            diff_desc = "各方案各有侧重，适合不同偏好。"
        else:
            diff_desc = "各方案较为相似，可根据个人情况微调。"
        
        # 关键差异描述
        if max_diff_axis:
            key_diff = f"主要差异体现在「{max_diff_axis}」维度。"
        else:
            key_diff = ""
        
        return f"{base_summary}{diff_desc}{key_diff}"
    
    def _find_max_diff_axis(self, version_set: LifeVersionSet) -> str:
        """找出差异最大的维度"""
        if len(version_set.versions) < 2:
            return ""
        
        axis_diffs: Dict[str, float] = {}
        
        for axis_id in version_set.comparison_axes:
            scores = [
                v.expected_outcomes.get(axis_id, 0.5) 
                for v in version_set.versions
            ]
            axis_diffs[axis_id] = max(scores) - min(scores)
        
        if not axis_diffs:
            return ""
        
        max_axis = max(axis_diffs, key=axis_diffs.get)
        
        # 维度标签映射
        axis_labels = {
            "income_ceiling": "收入上限",
            "stability": "稳定性",
            "autonomy": "自主性",
            "growth_potential": "成长性",
            "work_life_balance": "工作生活平衡",
            "emotional_depth": "情感深度",
            "compatibility": "匹配度",
        }
        
        return axis_labels.get(max_axis, max_axis)
    
    def get_version_ranking(
        self,
        version_set: LifeVersionSet,
        priority_axes: List[str],
    ) -> List[str]:
        """
        根据优先维度对版本排序
        
        Args:
            version_set: 版本集合
            priority_axes: 优先考虑的维度 (按重要性排序)
            
        Returns:
            排序后的 version_id 列表
        """
        def score_version(version):
            score = 0.0
            for i, axis_id in enumerate(priority_axes):
                weight = 1.0 / (i + 1)  # 权重递减
                axis_score = version.expected_outcomes.get(axis_id, 0.5)
                score += axis_score * weight
            return score
        
        sorted_versions = sorted(
            version_set.versions,
            key=score_version,
            reverse=True,
        )
        
        return [v.version_id for v in sorted_versions]
