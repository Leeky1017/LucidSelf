"""
ConceptAggregator - 概念聚合器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 11.2, Req 11.3, Req 11.4, Req 11.6
Design Refs: Design.md#ConceptAggregator
"""

import logging
from typing import Dict, List, Optional, Set

from scripts.knowledge_graph_builder.builders.alignment import AlignmentCandidate
from scripts.knowledge_graph_builder.models import (
    AggregationStrategy,
    ConceptAggregationRule,
    ConceptNode,
    ConflictSummary,
    DivinationSystem,
    LabelSelectionStrategy,
    SourceNodeRef,
)

logger = logging.getLogger(__name__)


class ConceptAggregator:
    """
    概念聚合器 - 将对齐的概念合并为统一概念
    
    聚合策略：
    1. MERGE_ALL: 合并所有来源节点
    2. HIGHEST_AUTHORITY_ONLY: 仅保留最高权威性的来源
    3. SAME_SYSTEM_MERGE: 仅合并同体系的节点
    4. MANUAL: 需人工审核决定
    """
    
    def __init__(self, default_rule: Optional[ConceptAggregationRule] = None):
        self.default_rule = default_rule or ConceptAggregationRule(
            rule_id="rule_default",
            name="默认聚合规则",
            aggregation_strategy=AggregationStrategy.MERGE_ALL,
            label_selection_strategy=LabelSelectionStrategy.HIGHEST_AUTHORITY,
        )
    
    def aggregate_concepts(
        self,
        concepts: List[ConceptNode],
        alignments: List[AlignmentCandidate],
        rule: Optional[ConceptAggregationRule] = None,
    ) -> List[ConceptNode]:
        """
        根据对齐关系聚合概念
        
        Args:
            concepts: 原始概念列表
            alignments: 对齐候选列表
            rule: 聚合规则
            
        Returns:
            聚合后的概念列表
        """
        rule = rule or self.default_rule
        
        # 构建概念索引
        concept_map: Dict[str, ConceptNode] = {c.concept_id: c for c in concepts}
        
        # 构建连通分量（Union-Find）
        parent: Dict[str, str] = {c.concept_id: c.concept_id for c in concepts}
        
        def find(x: str) -> str:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: str, y: str) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # 根据对齐关系合并
        for alignment in alignments:
            if alignment.is_false_positive:
                continue
            
            if alignment.concept_a_id in concept_map and alignment.concept_b_id in concept_map:
                union(alignment.concept_a_id, alignment.concept_b_id)
        
        # 按根节点分组
        groups: Dict[str, List[ConceptNode]] = {}
        for concept in concepts:
            root = find(concept.concept_id)
            if root not in groups:
                groups[root] = []
            groups[root].append(concept)
        
        # 聚合每个组
        aggregated: List[ConceptNode] = []
        for root, group in groups.items():
            if len(group) == 1:
                aggregated.append(group[0])
            else:
                merged = self._merge_group(group, rule)
                aggregated.append(merged)
        
        logger.info(f"Aggregated {len(concepts)} concepts into {len(aggregated)}")
        return aggregated
    
    def _merge_group(
        self,
        group: List[ConceptNode],
        rule: ConceptAggregationRule,
    ) -> ConceptNode:
        """
        合并一组概念
        """
        strategy = rule.aggregation_strategy
        
        if strategy == AggregationStrategy.HIGHEST_AUTHORITY_ONLY:
            return self._merge_highest_authority(group, rule)
        elif strategy == AggregationStrategy.SAME_SYSTEM_MERGE:
            return self._merge_same_system(group, rule)
        else:
            return self._merge_all(group, rule)
    
    def _merge_all(
        self,
        group: List[ConceptNode],
        rule: ConceptAggregationRule,
    ) -> ConceptNode:
        """
        合并所有来源
        """
        # 选择标签
        label = self._select_label(group, rule.label_selection_strategy)
        
        # 合并来源节点
        all_sources: List[SourceNodeRef] = []
        for concept in group:
            all_sources.extend(concept.source_nodes)
        
        # 合并因子
        all_factors: Set[str] = set()
        for concept in group:
            all_factors.update(concept.factor_refs)
        
        # 选择体系（使用最常见的）
        system_counts: Dict[DivinationSystem, int] = {}
        for concept in group:
            system_counts[concept.divination_system] = system_counts.get(
                concept.divination_system, 0
            ) + 1
        primary_system = max(system_counts, key=system_counts.get)
        
        # 计算平均权威性
        avg_authority = sum(c.authority_score for c in group) / len(group)
        
        # 检测冲突
        conflict_summary = self._detect_conflicts(group)
        
        # 使用第一个概念的ID作为基础
        base_id = sorted([c.concept_id for c in group])[0]
        
        return ConceptNode(
            concept_id=base_id,
            canonical_label_zh=label,
            divination_system=primary_system,
            dimension=group[0].dimension,
            source_nodes=all_sources,
            factor_refs=list(all_factors),
            authority_score=avg_authority,
            conflict_summary=conflict_summary,
            aggregation_rule_id=rule.rule_id,
            alignment_method="factor_overlap",
        )
    
    def _merge_highest_authority(
        self,
        group: List[ConceptNode],
        rule: ConceptAggregationRule,
    ) -> ConceptNode:
        """
        仅使用最高权威性的来源
        """
        # 按权威性排序
        sorted_group = sorted(group, key=lambda c: c.authority_score, reverse=True)
        highest = sorted_group[0]
        
        # 记录其他来源作为冲突
        conflict_summary = None
        if len(sorted_group) > 1:
            conflict_summary = ConflictSummary(
                conflict_count=len(sorted_group) - 1,
                highest_authority_source=highest.source_nodes[0].book_id if highest.source_nodes else None,
                conflict_types=["aggregation_override"],
                resolution_status="authority_based",
            )
        
        return ConceptNode(
            concept_id=highest.concept_id,
            canonical_label_zh=highest.canonical_label_zh,
            divination_system=highest.divination_system,
            dimension=highest.dimension,
            source_nodes=highest.source_nodes,
            factor_refs=highest.factor_refs,
            authority_score=highest.authority_score,
            conflict_summary=conflict_summary,
            aggregation_rule_id=rule.rule_id,
        )
    
    def _merge_same_system(
        self,
        group: List[ConceptNode],
        rule: ConceptAggregationRule,
    ) -> ConceptNode:
        """
        只合并同体系的概念
        """
        # 按体系分组
        by_system: Dict[DivinationSystem, List[ConceptNode]] = {}
        for concept in group:
            if concept.divination_system not in by_system:
                by_system[concept.divination_system] = []
            by_system[concept.divination_system].append(concept)
        
        # 选择最大的组
        largest_system = max(by_system, key=lambda s: len(by_system[s]))
        largest_group = by_system[largest_system]
        
        if len(largest_group) == 1:
            return largest_group[0]
        
        # 合并最大组
        return self._merge_all(largest_group, rule)
    
    def _select_label(
        self,
        group: List[ConceptNode],
        strategy: LabelSelectionStrategy,
    ) -> str:
        """
        选择规范标签
        """
        if strategy == LabelSelectionStrategy.HIGHEST_AUTHORITY:
            highest = max(group, key=lambda c: c.authority_score)
            return highest.canonical_label_zh
        
        elif strategy == LabelSelectionStrategy.MOST_COMMON:
            # 统计标签出现次数
            label_counts: Dict[str, int] = {}
            for concept in group:
                label = concept.canonical_label_zh
                label_counts[label] = label_counts.get(label, 0) + 1
            return max(label_counts, key=label_counts.get)
        
        else:  # MANUAL_OVERRIDE
            return group[0].canonical_label_zh
    
    def _detect_conflicts(self, group: List[ConceptNode]) -> Optional[ConflictSummary]:
        """
        检测组内冲突
        """
        if len(group) <= 1:
            return None
        
        # 检查是否有不同的summary/label
        labels = set(c.canonical_label_zh for c in group)
        
        if len(labels) > 1:
            highest = max(group, key=lambda c: c.authority_score)
            return ConflictSummary(
                conflict_count=len(labels) - 1,
                highest_authority_source=highest.source_nodes[0].book_id if highest.source_nodes else None,
                conflict_types=["label_divergence"],
                resolution_status="authority_based",
            )
        
        return None
