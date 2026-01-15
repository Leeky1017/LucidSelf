"""
ConceptAligner - 概念对齐器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 2.2, Req 2.3, Req 2.4, Req 2.5, Req 2.6, Req 2.7, Req 2.8
Design Refs: Design.md#ConceptAligner
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    DivinationSystem,
)

logger = logging.getLogger(__name__)


@dataclass
class AlignmentCandidate:
    """
    对齐候选 - 表示两个概念的潜在对齐关系
    """
    concept_a_id: str
    concept_b_id: str
    book_a: str
    book_b: str
    system_a: DivinationSystem
    system_b: DivinationSystem
    
    # 相似度分数
    factor_overlap_score: float = 0.0
    text_similarity_score: float = 0.0
    combined_score: float = 0.0
    
    # 对齐方法
    alignment_method: str = "factor_overlap"
    
    # 是否同体系
    is_same_system: bool = False
    
    # 置信度
    confidence: float = 0.0
    
    # 证据
    evidence_snippets: List[str] = field(default_factory=list)
    shared_factors: List[str] = field(default_factory=list)
    
    # 标记
    is_false_positive: bool = False
    false_positive_reason: Optional[str] = None


class AlignmentThresholds:
    """对齐阈值配置"""
    
    def __init__(
        self,
        factor_overlap_threshold: float = 0.7,
        text_similarity_threshold: float = 0.8,
        cross_system_threshold: float = 0.6,
        min_shared_factors: int = 2,
    ):
        self.factor_overlap_threshold = factor_overlap_threshold
        self.text_similarity_threshold = text_similarity_threshold
        self.cross_system_threshold = cross_system_threshold
        self.min_shared_factors = min_shared_factors
    
    def get_threshold(self, is_same_system: bool) -> float:
        """获取适用的阈值"""
        if is_same_system:
            return self.factor_overlap_threshold
        return self.cross_system_threshold


class ConceptAligner:
    """
    概念对齐器 - 发现跨书概念对齐关系
    
    对齐策略：
    1. 因子重叠：基于factor_refs的Jaccard相似度
    2. 文本相似：基于summary的文本相似度
    3. 片段模式：基于snippet_ids的模式匹配
    
    优先级：
    1. 同体系对齐优先于跨体系对齐
    2. 高相似度优先于低相似度
    """
    
    def __init__(self, thresholds: Optional[AlignmentThresholds] = None):
        self.thresholds = thresholds or AlignmentThresholds()
        self._alignment_cache: Dict[Tuple[str, str], AlignmentCandidate] = {}
    
    def find_alignments(
        self,
        concepts: List[ConceptNode],
        max_candidates: int = 10000,
    ) -> List[AlignmentCandidate]:
        """
        发现所有对齐候选
        
        Args:
            concepts: 概念列表
            max_candidates: 最大候选数限制
            
        Returns:
            对齐候选列表，按置信度排序
        """
        candidates: List[AlignmentCandidate] = []
        concept_index: Dict[str, ConceptNode] = {c.concept_id: c for c in concepts}
        
        # 构建因子索引加速查找
        factor_to_concepts: Dict[str, List[ConceptNode]] = {}
        for concept in concepts:
            for factor in concept.factor_refs:
                if factor not in factor_to_concepts:
                    factor_to_concepts[factor] = []
                factor_to_concepts[factor].append(concept)
        
        # 查找共享因子的概念对
        processed_pairs: Set[Tuple[str, str]] = set()
        
        for concept in concepts:
            # 找到共享因子的候选
            candidate_concepts: Set[str] = set()
            for factor in concept.factor_refs:
                for other in factor_to_concepts.get(factor, []):
                    if other.concept_id != concept.concept_id:
                        candidate_concepts.add(other.concept_id)
            
            # 评估每个候选
            for other_id in candidate_concepts:
                # 避免重复处理
                pair_key = tuple(sorted([concept.concept_id, other_id]))
                if pair_key in processed_pairs:
                    continue
                processed_pairs.add(pair_key)
                
                # 获取另一个概念
                other = concept_index.get(other_id)
                if not other:
                    continue
                
                # 跳过同一来源
                if self._is_same_source(concept, other):
                    continue
                
                # 计算对齐候选
                candidate = self._compute_alignment(concept, other)
                
                if candidate and not candidate.is_false_positive:
                    candidates.append(candidate)
                    
                    if len(candidates) >= max_candidates:
                        break
            
            if len(candidates) >= max_candidates:
                break
        
        # 排序：同体系优先，然后按置信度
        candidates.sort(
            key=lambda c: (c.is_same_system, c.confidence),
            reverse=True
        )
        
        logger.info(f"Found {len(candidates)} alignment candidates")
        return candidates
    
    def _is_same_source(self, a: ConceptNode, b: ConceptNode) -> bool:
        """检查两个概念是否来自同一来源"""
        books_a = {s.book_id for s in a.source_nodes}
        books_b = {s.book_id for s in b.source_nodes}
        return len(books_a & books_b) > 0
    
    def _compute_alignment(
        self,
        a: ConceptNode,
        b: ConceptNode,
    ) -> Optional[AlignmentCandidate]:
        """
        计算两个概念的对齐候选
        
        Returns:
            AlignmentCandidate if above threshold, None otherwise
        """
        # 检查缓存
        cache_key = tuple(sorted([a.concept_id, b.concept_id]))
        if cache_key in self._alignment_cache:
            return self._alignment_cache[cache_key]
        
        is_same_system = a.divination_system == b.divination_system
        threshold = self.thresholds.get_threshold(is_same_system)
        
        # 计算因子重叠
        factor_overlap = self._compute_factor_overlap(a.factor_refs, b.factor_refs)
        shared_factors = list(set(a.factor_refs) & set(b.factor_refs))
        
        # 计算文本相似度（简化版，实际应使用更复杂的算法）
        text_sim = self._compute_text_similarity(
            a.canonical_label_zh, 
            b.canonical_label_zh
        )
        
        # 综合得分：因子重叠权重0.7，文本相似度0.3
        combined = factor_overlap * 0.7 + text_sim * 0.3
        
        # 低于阈值，不提议对齐
        if combined < threshold:
            return None
        
        # 检测假阳性：文本相似但因子矛盾
        is_false_positive, fp_reason = self._detect_false_positive(a, b, shared_factors)
        
        candidate = AlignmentCandidate(
            concept_a_id=a.concept_id,
            concept_b_id=b.concept_id,
            book_a=a.source_nodes[0].book_id if a.source_nodes else "",
            book_b=b.source_nodes[0].book_id if b.source_nodes else "",
            system_a=a.divination_system,
            system_b=b.divination_system,
            factor_overlap_score=factor_overlap,
            text_similarity_score=text_sim,
            combined_score=combined,
            alignment_method="factor_overlap" if factor_overlap > text_sim else "text_similarity",
            is_same_system=is_same_system,
            confidence=combined,
            shared_factors=shared_factors,
            is_false_positive=is_false_positive,
            false_positive_reason=fp_reason,
        )
        
        self._alignment_cache[cache_key] = candidate
        return candidate
    
    def _compute_factor_overlap(
        self,
        factors_a: List[str],
        factors_b: List[str],
    ) -> float:
        """
        计算因子重叠率（Jaccard相似度）
        """
        if not factors_a or not factors_b:
            return 0.0
        
        set_a = set(factors_a)
        set_b = set(factors_b)
        
        intersection = len(set_a & set_b)
        union = len(set_a | set_b)
        
        if union == 0:
            return 0.0
        
        return intersection / union
    
    def _compute_text_similarity(self, text_a: str, text_b: str) -> float:
        """
        计算文本相似度
        
        简化实现：使用字符级Jaccard，实际应使用更复杂的算法
        """
        if not text_a or not text_b:
            return 0.0
        
        # 字符集合
        chars_a = set(text_a)
        chars_b = set(text_b)
        
        intersection = len(chars_a & chars_b)
        union = len(chars_a | chars_b)
        
        if union == 0:
            return 0.0
        
        return intersection / union
    
    def _detect_false_positive(
        self,
        a: ConceptNode,
        b: ConceptNode,
        shared_factors: List[str],
    ) -> Tuple[bool, Optional[str]]:
        """
        检测假阳性：文本相似但因子矛盾
        
        Returns:
            (is_false_positive, reason)
        """
        # 如果共享因子太少但文本相似度高，可能是假阳性
        if len(shared_factors) < self.thresholds.min_shared_factors:
            text_sim = self._compute_text_similarity(
                a.canonical_label_zh,
                b.canonical_label_zh
            )
            if text_sim > 0.5:
                return True, f"Low factor overlap ({len(shared_factors)}) despite text similarity"
        
        # TODO: 更复杂的矛盾检测逻辑
        
        return False, None
    
    def generate_alignment_report(
        self,
        candidates: List[AlignmentCandidate],
        output_path: Path,
    ) -> None:
        """
        生成对齐报告（Markdown格式）
        
        按divination_system分组，包含：
        - 候选对齐列表
        - 置信度和方法
        - 假阳性标记
        """
        # 按体系分组
        by_system: Dict[str, List[AlignmentCandidate]] = {}
        for c in candidates:
            # 使用第一个概念的体系分组
            key = c.system_a.value
            if key not in by_system:
                by_system[key] = []
            by_system[key].append(c)
        
        lines = [
            "# Alignment Report",
            "",
            f"Generated: {datetime.now().isoformat()}",
            f"Total Candidates: {len(candidates)}",
            "",
        ]
        
        # 统计
        same_system_count = sum(1 for c in candidates if c.is_same_system)
        cross_system_count = len(candidates) - same_system_count
        false_positive_count = sum(1 for c in candidates if c.is_false_positive)
        
        lines.extend([
            "## Summary",
            "",
            f"- Same-system alignments: {same_system_count}",
            f"- Cross-system alignments: {cross_system_count}",
            f"- Flagged as false positive: {false_positive_count}",
            "",
        ])
        
        # 按体系输出
        for system in sorted(by_system.keys()):
            system_candidates = by_system[system]
            lines.extend([
                f"## {system.upper()}",
                "",
                f"Found {len(system_candidates)} alignments",
                "",
            ])
            
            for c in system_candidates[:20]:  # 每个体系最多显示20个
                status = "⚠️ FALSE POSITIVE" if c.is_false_positive else ""
                lines.extend([
                    f"### {c.concept_a_id} ↔ {c.concept_b_id} {status}",
                    "",
                    f"- **Books**: {c.book_a} ↔ {c.book_b}",
                    f"- **Method**: {c.alignment_method}",
                    f"- **Confidence**: {c.confidence:.2f}",
                    f"- **Factor Overlap**: {c.factor_overlap_score:.2f}",
                    f"- **Text Similarity**: {c.text_similarity_score:.2f}",
                    f"- **Shared Factors**: {', '.join(c.shared_factors[:5])}...",
                    "",
                ])
                
                if c.is_false_positive:
                    lines.append(f"- **FP Reason**: {c.false_positive_reason}")
                    lines.append("")
            
            if len(system_candidates) > 20:
                lines.append(f"... and {len(system_candidates) - 20} more")
                lines.append("")
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        logger.info(f"Alignment report written to {output_path}")


def prioritize_alignments(candidates: List[AlignmentCandidate]) -> List[AlignmentCandidate]:
    """
    优先级排序对齐候选
    
    规则：
    1. 同体系对齐优先
    2. 高置信度优先
    3. 因子重叠方法优先于文本相似度
    """
    return sorted(
        candidates,
        key=lambda c: (
            c.is_same_system,           # 同体系优先
            c.confidence,               # 高置信度优先
            c.alignment_method == "factor_overlap",  # 因子方法优先
        ),
        reverse=True
    )
