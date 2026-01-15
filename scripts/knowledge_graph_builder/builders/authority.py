"""
AuthorityScorer - 权威性计算器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 3.2, Req 15.1, Req 15.2, Req 15.3, Req 15.4, Req 15.5, Req 15.6
Design Refs: Design.md#AuthorityScorer
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from scripts.knowledge_graph_builder.models import ConceptNode

logger = logging.getLogger(__name__)


class AuthorityScorer:
    """
    权威性计算器 - 计算概念的authority_score
    
    计算公式 (Req 15.1):
    authority_score = book_authority_weight * 0.5 + node_quality_score * 0.3 + source_count_factor * 0.2
    
    其中:
    - node_quality_score = (reasoning_coherence + node_homogeneity) / 2 (Req 15.2)
    - source_count_factor = min(1.0, len(source_nodes) / 3) (Req 15.3)
    
    惩罚因子 (Req 15.5):
    - 当 reasoning_coherence < 0.7 OR node_homogeneity < 0.5 时应用0.8惩罚
    """
    
    # 公式权重
    BOOK_WEIGHT = 0.5
    QUALITY_WEIGHT = 0.3
    SOURCE_COUNT_WEIGHT = 0.2
    
    # 质量阈值
    COHERENCE_THRESHOLD = 0.7
    HOMOGENEITY_THRESHOLD = 0.5
    PENALTY_FACTOR = 0.8
    
    def __init__(
        self,
        authority_config_path: Optional[Path] = None,
        quality_metrics: Optional[Dict[str, Dict[str, float]]] = None,
    ):
        """
        Args:
            authority_config_path: 权威性配置文件路径
            quality_metrics: 典籍质量指标 {book_id: {reasoning_coherence, node_homogeneity}}
        """
        self.authority_config_path = authority_config_path or Path(
            'data/knowledge_graph/authority_config.yaml'
        )
        self._book_weights: Optional[Dict[str, float]] = None
        self._quality_metrics = quality_metrics or {}
        self._score_cache: Dict[str, float] = {}
    
    @property
    def book_weights(self) -> Dict[str, float]:
        """懒加载典籍权威性权重"""
        if self._book_weights is None:
            self._book_weights = self._load_book_weights()
        return self._book_weights
    
    def _load_book_weights(self) -> Dict[str, float]:
        """加载典籍权威性权重"""
        if self.authority_config_path.exists():
            with open(self.authority_config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                return config.get('book_authority_weights', {})
        return {}
    
    def set_quality_metrics(
        self,
        book_id: str,
        reasoning_coherence: float,
        node_homogeneity: float,
    ) -> None:
        """
        设置典籍的质量指标
        
        Args:
            book_id: 典籍ID
            reasoning_coherence: 推理一致性分数
            node_homogeneity: 节点同质性分数
        """
        self._quality_metrics[book_id] = {
            'reasoning_coherence': reasoning_coherence,
            'node_homogeneity': node_homogeneity,
        }
        # 清除缓存
        self._score_cache = {}
    
    def compute_authority_score(
        self,
        concept: ConceptNode,
    ) -> float:
        """
        计算概念的权威性分数
        
        Args:
            concept: 概念节点
            
        Returns:
            权威性分数 [0.0, 1.0]
        """
        # 检查缓存
        if concept.concept_id in self._score_cache:
            return self._score_cache[concept.concept_id]
        
        if not concept.source_nodes:
            return 0.5
        
        # 1. 计算book_authority_weight
        book_weights = []
        for source in concept.source_nodes:
            weight = self.book_weights.get(
                source.book_id,
                self.book_weights.get('_default', 0.7)
            )
            book_weights.append(weight)
        avg_book_weight = sum(book_weights) / len(book_weights)
        
        # 2. 计算node_quality_score
        quality_scores = []
        apply_penalty = False
        
        for source in concept.source_nodes:
            metrics = self._quality_metrics.get(source.book_id, {})
            coherence = metrics.get('reasoning_coherence', 0.8)  # 默认0.8
            homogeneity = metrics.get('node_homogeneity', 0.7)  # 默认0.7
            
            quality = (coherence + homogeneity) / 2
            quality_scores.append(quality)
            
            # 检查是否需要惩罚
            if coherence < self.COHERENCE_THRESHOLD or homogeneity < self.HOMOGENEITY_THRESHOLD:
                apply_penalty = True
        
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0.75
        
        # 3. 计算source_count_factor
        source_count_factor = min(1.0, len(concept.source_nodes) / 3)
        
        # 4. 综合计算
        score = (
            avg_book_weight * self.BOOK_WEIGHT +
            avg_quality * self.QUALITY_WEIGHT +
            source_count_factor * self.SOURCE_COUNT_WEIGHT
        )
        
        # 5. 应用惩罚因子
        if apply_penalty:
            score *= self.PENALTY_FACTOR
        
        # 确保范围
        score = max(0.0, min(1.0, score))
        
        # 缓存
        self._score_cache[concept.concept_id] = score
        
        return score
    
    def update_concept_authorities(
        self,
        concepts: List[ConceptNode],
    ) -> None:
        """
        批量更新概念的权威性分数
        
        Args:
            concepts: 概念列表
        """
        for concept in concepts:
            score = self.compute_authority_score(concept)
            concept.authority_score = score
        
        logger.info(f"Updated authority scores for {len(concepts)} concepts")
    
    def get_top_authority_concepts(
        self,
        concepts: List[ConceptNode],
        top_n: int = 10,
    ) -> List[ConceptNode]:
        """
        获取权威性最高的N个概念
        """
        sorted_concepts = sorted(
            concepts,
            key=lambda c: c.authority_score,
            reverse=True
        )
        return sorted_concepts[:top_n]
    
    def clear_cache(self) -> None:
        """清除分数缓存"""
        self._score_cache = {}
