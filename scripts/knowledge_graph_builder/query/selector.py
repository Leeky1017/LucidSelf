"""
ConceptSelector - 概念选择器（筛选漏斗）

Feature: cross-book-knowledge-graph
Requirement Refs: Req 12.1, Req 12.2, Req 12.3, Req 12.4, Req 12.5, Req 12.6, Req 12.7
Design Refs: Design.md#筛选漏斗接口, Design.md#ConceptSelector
"""

import logging
import time
from typing import Dict, List, Optional, Set

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    ConceptSelectionResult,
    ConflictWarning,
    Dimension,
    DivinationSystem,
    FunnelStats,
    KnowledgeGraph,
    SelectorConfig,
    SystemQuota,
)
from scripts.knowledge_graph_builder.models.selector import DEFAULT_SYSTEM_QUOTAS

logger = logging.getLogger(__name__)


class ConceptSelector:
    """
    概念选择器 - 5阶段筛选漏斗
    
    解决"400因子怎么办"的核心问题：
    1. factor_match: 从10000+概念中找到与激活因子匹配的
    2. dimension_filter: 按目标维度过滤
    3. authority_rank: 按权威性排序
    4. quota_apply: 按体系配额分配
    5. total_truncate: 截断到总数限制
    """
    
    def __init__(
        self,
        graph: KnowledgeGraph,
        config: Optional[SelectorConfig] = None,
    ):
        self.graph = graph
        self.config = config or SelectorConfig()
        
        # 确保索引已构建
        if not self.graph._factor_index:
            self.graph.build_indices()
    
    def select(
        self,
        activated_factor_ids: List[str],
        target_dimensions: Optional[List[Dimension]] = None,
        custom_quotas: Optional[Dict[DivinationSystem, int]] = None,
        total_max_concepts: Optional[int] = None,
        include_conflicted: Optional[bool] = None,
    ) -> ConceptSelectionResult:
        """
        执行5阶段筛选漏斗
        
        Args:
            activated_factor_ids: 激活的因子ID列表（通常100-400个）
            target_dimensions: 目标维度过滤
            custom_quotas: 自定义体系配额，None则使用配置默认值
            total_max_concepts: 最终返回的最大概念数
            include_conflicted: 是否包含有冲突的概念
            
        Returns:
            ConceptSelectionResult: 选择结果，包含漏斗统计
        """
        start_time = time.perf_counter()
        
        # 使用配置值或默认值
        max_concepts = total_max_concepts or self.config.total_max_concepts
        include_conflict = include_conflicted if include_conflicted is not None else self.config.include_conflicted
        quotas = custom_quotas or DEFAULT_SYSTEM_QUOTAS
        
        # Stage 1: Factor Match
        stage1 = self._stage_factor_match(activated_factor_ids)
        stage1_count = len(stage1)
        
        # Stage 2: Dimension Filter
        stage2 = self._stage_dimension_filter(stage1, target_dimensions)
        stage2_count = len(stage2)
        
        # Stage 3: Authority Rank (排序，数量不变)
        stage3 = self._stage_authority_rank(stage2)
        stage3_count = len(stage3)
        
        # Stage 4: Quota Apply
        stage4, truncated_systems = self._stage_quota_apply(stage3, quotas)
        stage4_count = len(stage4)
        
        # Stage 5: Total Truncate
        stage5 = self._stage_total_truncate(stage4, max_concepts)
        stage5_count = len(stage5)
        
        # 过滤冲突（可选）
        if not include_conflict:
            stage5 = [
                c for c in stage5 
                if not c.conflict_summary or c.conflict_summary.conflict_count == 0
            ]
        
        # 收集冲突警告
        conflict_warnings = self._collect_conflict_warnings(stage5)
        
        selection_time_ms = (time.perf_counter() - start_time) * 1000
        
        return ConceptSelectionResult(
            selected_concepts=stage5,
            funnel_stats=FunnelStats(
                stage_factor_match=stage1_count,
                stage_dimension_filter=stage2_count,
                stage_authority_rank=stage3_count,
                stage_quota_apply=stage4_count,
                stage_total_truncate=stage5_count,
            ),
            truncated_systems=truncated_systems,
            selection_time_ms=selection_time_ms,
        )
    
    def _stage_factor_match(
        self,
        factor_ids: List[str],
    ) -> List[ConceptNode]:
        """Stage 1: 因子匹配"""
        # 使用图谱的内置方法
        return self.graph.query_by_factors(factor_ids)
    
    def _stage_dimension_filter(
        self,
        concepts: List[ConceptNode],
        target_dimensions: Optional[List[Dimension]],
    ) -> List[ConceptNode]:
        """Stage 2: 维度过滤"""
        if not target_dimensions:
            return concepts
        
        return [
            c for c in concepts
            if c.dimension in target_dimensions
        ]
    
    def _stage_authority_rank(
        self,
        concepts: List[ConceptNode],
    ) -> List[ConceptNode]:
        """Stage 3: 权威性排序"""
        return sorted(
            concepts,
            key=lambda c: c.authority_score,
            reverse=True
        )
    
    def _stage_quota_apply(
        self,
        concepts: List[ConceptNode],
        quotas: Dict[DivinationSystem, int],
    ) -> tuple[List[ConceptNode], List[DivinationSystem]]:
        """
        Stage 4: 配额应用
        
        按体系分组，每个体系不超过配额
        配额不足时不重新分配给其他体系 (Req 12.4)
        """
        # 按体系分组
        by_system: Dict[DivinationSystem, List[ConceptNode]] = {}
        for concept in concepts:
            if concept.divination_system not in by_system:
                by_system[concept.divination_system] = []
            by_system[concept.divination_system].append(concept)
        
        result: List[ConceptNode] = []
        truncated: List[DivinationSystem] = []
        
        for system, system_concepts in by_system.items():
            quota = quotas.get(system, 5)  # 默认配额5
            
            if len(system_concepts) > quota:
                truncated.append(system)
                result.extend(system_concepts[:quota])
            else:
                result.extend(system_concepts)
        
        return result, truncated
    
    def _stage_total_truncate(
        self,
        concepts: List[ConceptNode],
        max_total: int,
    ) -> List[ConceptNode]:
        """Stage 5: 总数截断"""
        # 已经按权威性排序，直接截断
        return concepts[:max_total]
    
    def _collect_conflict_warnings(
        self,
        concepts: List[ConceptNode],
    ) -> List[ConflictWarning]:
        """收集冲突警告"""
        warnings = []
        
        # Build a set of concept IDs for quick lookup
        concept_ids = {c.concept_id for c in concepts}
        
        for concept in concepts:
            if concept.conflict_summary and concept.conflict_summary.conflict_count > 0:
                severity = "HIGH" if concept.conflict_summary.conflict_count >= 3 else \
                          "MEDIUM" if concept.conflict_summary.conflict_count >= 2 else "LOW"
                
                # Find conflicting concepts from edges
                conflicting_ids = self._find_conflicting_in_graph(concept.concept_id, concept_ids)
                
                for conflicting_id in conflicting_ids:
                    warnings.append(ConflictWarning(
                        concept_id=concept.concept_id,
                        conflicting_concept_id=conflicting_id,
                        conflict_type=concept.conflict_summary.conflict_types[0] if concept.conflict_summary.conflict_types else "unknown",
                        severity=severity,
                        resolution_hint=f"参考 {concept.conflict_summary.highest_authority_source or '最高权威来源'}",
                    ))
                
                # If no conflicting edges found but summary exists, create placeholder
                if not conflicting_ids:
                    warnings.append(ConflictWarning(
                        concept_id=concept.concept_id,
                        conflicting_concept_id=concept.concept_id,
                        conflict_type=concept.conflict_summary.conflict_types[0] if concept.conflict_summary.conflict_types else "unknown",
                        severity=severity,
                        resolution_hint=f"参考 {concept.conflict_summary.highest_authority_source or '最高权威来源'}",
                    ))
        
        return warnings
    
    def _find_conflicting_in_graph(
        self,
        concept_id: str,
        valid_concept_ids: Set[str],
    ) -> List[str]:
        """Find conflicting concept IDs from graph edges"""
        from scripts.knowledge_graph_builder.models.edge import RelationType
        
        conflicting = []
        for edge in self.graph.edges:
            if edge.relation_type == RelationType.CONFLICTS_WITH:
                if edge.source_concept_id == concept_id and edge.target_concept_id in valid_concept_ids:
                    conflicting.append(edge.target_concept_id)
                elif edge.target_concept_id == concept_id and edge.source_concept_id in valid_concept_ids:
                    conflicting.append(edge.source_concept_id)
        return conflicting
