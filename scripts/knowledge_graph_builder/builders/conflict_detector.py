"""
ConflictDetector - 冲突检测器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 3.1, Req 3.4, Req 3.5, Req 3.6, Req 3.7
Design Refs: Design.md#ConflictDetector
"""

import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    ConflictOutput,
    ConflictSummary,
    ConflictType,
    Dimension,
    DivinationSystem,
    RelationType,
    ResolutionStrategy,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.conflict import ConceptSummary

logger = logging.getLogger(__name__)


@dataclass
class ConflictCandidate:
    """冲突候选"""
    concept_a: ConceptNode
    concept_b: ConceptNode
    dimension: Dimension
    conflict_type: ConflictType
    severity: str  # LOW, MEDIUM, HIGH
    evidence: List[str] = field(default_factory=list)
    

class ConflictDetector:
    """
    冲突检测器 - 检测概念间的冲突关系
    
    冲突类型：
    1. DIRECT_CONTRADICTION: 直接矛盾
    2. CONDITIONAL_EXCEPTION: 条件例外
    3. SCOPE_DIFFERENCE: 范围差异
    4. CROSS_SYSTEM_DIVERGENCE: 跨体系分歧
    """
    
    # 矛盾关键词
    CONTRADICTION_KEYWORDS = {
        ("喜", "忌"),
        ("吉", "凶"),
        ("强", "弱"),
        ("旺", "衰"),
        ("利", "害"),
        ("宜", "忌"),
        ("好", "坏"),
        ("positive", "negative"),
        ("benefit", "harm"),
    }
    
    def __init__(self):
        self._conflict_cache: Dict[Tuple[str, str], Optional[ConflictCandidate]] = {}
    
    def detect_conflicts(
        self,
        concepts: List[ConceptNode],
    ) -> Tuple[List[SemanticEdge], List[ConflictOutput]]:
        """
        检测概念间的冲突
        
        Args:
            concepts: 概念列表
            
        Returns:
            (conflict_edges, conflict_outputs): 冲突边和冲突输出
        """
        conflict_edges: List[SemanticEdge] = []
        conflict_outputs: List[ConflictOutput] = []
        
        # 按维度分组
        by_dimension: Dict[Dimension, List[ConceptNode]] = {}
        for concept in concepts:
            if concept.dimension not in by_dimension:
                by_dimension[concept.dimension] = []
            by_dimension[concept.dimension].append(concept)
        
        # 在每个维度内检测冲突
        for dimension, dim_concepts in by_dimension.items():
            conflicts = self._detect_dimension_conflicts(dim_concepts, dimension)
            
            for candidate in conflicts:
                # 创建冲突边
                edge = self._create_conflict_edge(candidate)
                conflict_edges.append(edge)
                
                # 创建冲突输出
                output = self._create_conflict_output(candidate)
                conflict_outputs.append(output)
        
        # 检测跨体系冲突
        cross_conflicts = self._detect_cross_system_conflicts(concepts)
        for candidate in cross_conflicts:
            edge = self._create_conflict_edge(candidate)
            conflict_edges.append(edge)
            output = self._create_conflict_output(candidate)
            conflict_outputs.append(output)
        
        logger.info(f"Detected {len(conflict_edges)} conflicts")
        return conflict_edges, conflict_outputs
    
    def _detect_dimension_conflicts(
        self,
        concepts: List[ConceptNode],
        dimension: Dimension,
    ) -> List[ConflictCandidate]:
        """检测同维度内的冲突"""
        conflicts: List[ConflictCandidate] = []
        
        # 按体系分组
        by_system: Dict[DivinationSystem, List[ConceptNode]] = {}
        for concept in concepts:
            if concept.divination_system not in by_system:
                by_system[concept.divination_system] = []
            by_system[concept.divination_system].append(concept)
        
        # 同体系内检测冲突
        for system, system_concepts in by_system.items():
            for i, a in enumerate(system_concepts):
                for b in system_concepts[i+1:]:
                    candidate = self._check_conflict(a, b, dimension)
                    if candidate:
                        conflicts.append(candidate)
        
        return conflicts
    
    def _detect_cross_system_conflicts(
        self,
        concepts: List[ConceptNode],
    ) -> List[ConflictCandidate]:
        """检测跨体系冲突"""
        conflicts: List[ConflictCandidate] = []
        
        # 按维度分组
        by_dimension: Dict[Dimension, Dict[DivinationSystem, List[ConceptNode]]] = {}
        for concept in concepts:
            if concept.dimension not in by_dimension:
                by_dimension[concept.dimension] = {}
            if concept.divination_system not in by_dimension[concept.dimension]:
                by_dimension[concept.dimension][concept.divination_system] = []
            by_dimension[concept.dimension][concept.divination_system].append(concept)
        
        # 在每个维度内，检测不同体系间的冲突
        for dimension, systems in by_dimension.items():
            system_list = list(systems.keys())
            for i, sys_a in enumerate(system_list):
                for sys_b in system_list[i+1:]:
                    for concept_a in systems[sys_a]:
                        for concept_b in systems[sys_b]:
                            candidate = self._check_cross_system_conflict(
                                concept_a, concept_b, dimension
                            )
                            if candidate:
                                conflicts.append(candidate)
        
        return conflicts
    
    def _check_conflict(
        self,
        a: ConceptNode,
        b: ConceptNode,
        dimension: Dimension,
    ) -> Optional[ConflictCandidate]:
        """检查两个概念是否冲突"""
        cache_key = tuple(sorted([a.concept_id, b.concept_id]))
        if cache_key in self._conflict_cache:
            return self._conflict_cache[cache_key]
        
        # 检测直接矛盾
        if self._has_contradiction(a.canonical_label_zh, b.canonical_label_zh):
            candidate = ConflictCandidate(
                concept_a=a,
                concept_b=b,
                dimension=dimension,
                conflict_type=ConflictType.DIRECT_CONTRADICTION,
                severity="HIGH",
            )
            self._conflict_cache[cache_key] = candidate
            return candidate
        
        # TODO: 更复杂的冲突检测逻辑
        
        self._conflict_cache[cache_key] = None
        return None
    
    def _check_cross_system_conflict(
        self,
        a: ConceptNode,
        b: ConceptNode,
        dimension: Dimension,
    ) -> Optional[ConflictCandidate]:
        """检查跨体系冲突"""
        if a.divination_system == b.divination_system:
            return None
        
        # 检测跨体系的直接矛盾
        if self._has_contradiction(a.canonical_label_zh, b.canonical_label_zh):
            return ConflictCandidate(
                concept_a=a,
                concept_b=b,
                dimension=dimension,
                conflict_type=ConflictType.CROSS_SYSTEM_DIVERGENCE,
                severity="MEDIUM",
            )
        
        return None
    
    def _has_contradiction(self, text_a: str, text_b: str) -> bool:
        """检测文本是否包含矛盾关键词"""
        for pos, neg in self.CONTRADICTION_KEYWORDS:
            if (pos in text_a and neg in text_b) or (neg in text_a and pos in text_b):
                return True
        return False
    
    def _create_conflict_edge(self, candidate: ConflictCandidate) -> SemanticEdge:
        """创建冲突边"""
        return SemanticEdge(
            edge_id=f"edge_conflict_{candidate.concept_a.concept_id[:20]}_{candidate.concept_b.concept_id[:20]}",
            source_concept_id=candidate.concept_a.concept_id,
            target_concept_id=candidate.concept_b.concept_id,
            relation_type=RelationType.CONFLICTS_WITH,
            conflict_type=candidate.conflict_type,
            confidence=0.8,
        )
    
    def _create_conflict_output(self, candidate: ConflictCandidate) -> ConflictOutput:
        """创建冲突输出"""
        # 确定resolution策略
        if candidate.conflict_type == ConflictType.CROSS_SYSTEM_DIVERGENCE:
            strategy = ResolutionStrategy.PRESENT_BOTH
            hint = "跨体系分歧，建议同时呈现双方观点"
        elif candidate.concept_a.authority_score > candidate.concept_b.authority_score + 0.2:
            strategy = ResolutionStrategy.AUTHORITY_BASED
            hint = f"以{candidate.concept_a.source_nodes[0].book_id if candidate.concept_a.source_nodes else '高权威来源'}为准"
        else:
            strategy = ResolutionStrategy.SYNTHESIS
            hint = "建议综合双方观点"
        
        return ConflictOutput(
            viewpoint_a=ConceptSummary(
                concept_id=candidate.concept_a.concept_id,
                label_zh=candidate.concept_a.canonical_label_zh,
                book_source=candidate.concept_a.source_nodes[0].book_id if candidate.concept_a.source_nodes else "",
                authority_score=candidate.concept_a.authority_score,
            ),
            viewpoint_b=ConceptSummary(
                concept_id=candidate.concept_b.concept_id,
                label_zh=candidate.concept_b.canonical_label_zh,
                book_source=candidate.concept_b.source_nodes[0].book_id if candidate.concept_b.source_nodes else "",
                authority_score=candidate.concept_b.authority_score,
            ),
            conflict_type=candidate.conflict_type,
            dimension=candidate.dimension.value,
            resolution_strategy=strategy,
            resolution_hint=hint,
        )
    
    def update_conflict_summaries(
        self,
        concepts: List[ConceptNode],
        conflict_edges: List[SemanticEdge],
    ) -> None:
        """
        更新概念的conflict_summary字段
        """
        # 构建冲突计数
        conflict_counts: Dict[str, int] = {}
        conflict_types_map: Dict[str, Set[str]] = {}
        
        for edge in conflict_edges:
            if edge.relation_type == RelationType.CONFLICTS_WITH:
                for cid in [edge.source_concept_id, edge.target_concept_id]:
                    conflict_counts[cid] = conflict_counts.get(cid, 0) + 1
                    if cid not in conflict_types_map:
                        conflict_types_map[cid] = set()
                    if edge.conflict_type:
                        conflict_types_map[cid].add(edge.conflict_type.value)
        
        # 更新概念
        for concept in concepts:
            count = conflict_counts.get(concept.concept_id, 0)
            if count > 0:
                concept.conflict_summary = ConflictSummary(
                    conflict_count=count,
                    highest_authority_source=concept.source_nodes[0].book_id if concept.source_nodes else None,
                    conflict_types=list(conflict_types_map.get(concept.concept_id, [])),
                    resolution_status="unresolved",
                )
