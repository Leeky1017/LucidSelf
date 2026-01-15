"""
SemanticQueryService - 语义查询服务

Feature: cross-book-knowledge-graph
Requirement Refs: Req 4.1, Req 4.2, Req 4.3, Req 4.4, Req 4.5, Req 4.6, Req 4.7, Req 4.8, Req 4.9, Req 4.10
Design Refs: Design.md#查询接口
"""

import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Set

from scripts.knowledge_graph_builder.models import (
    BatchQueryRequest,
    BatchQueryResult,
    ConceptNode,
    ConflictWarning,
    Dimension,
    DivinationSystem,
    KnowledgeGraph,
    QueryResult,
    QueryResultItem,
    RelationType,
    SemanticQuery,
)
from scripts.knowledge_graph_builder.query.traversal import GraphTraversal

logger = logging.getLogger(__name__)


class SemanticQueryService:
    """
    语义查询服务 - 为FusionEngine提供只读查询接口
    
    功能：
    - 因子匹配查询
    - 维度/体系过滤
    - 关系遍历
    - 分页支持
    - 批量查询
    """
    
    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph
        self._traversal = GraphTraversal(graph)
        
        # 确保索引已构建
        if not self.graph._concept_index:
            self.graph.build_indices()
    
    def query(self, request: SemanticQuery) -> QueryResult:
        """
        执行语义查询
        
        Args:
            request: 查询请求
            
        Returns:
            QueryResult: 查询结果
        """
        start_time = time.perf_counter()
        
        # 1. 获取候选概念
        candidates = self._get_candidates(request)
        
        # 2. 应用过滤
        filtered = self._apply_filters(candidates, request)
        
        # 3. 遍历相关概念（如果需要）
        if request.traversal_depth > 0:
            filtered = self._expand_with_traversal(filtered, request)
        
        # 4. 排序（按权威性降序）
        sorted_concepts = sorted(
            filtered,
            key=lambda c: c.authority_score,
            reverse=True
        )
        
        # 5. 分页
        total_count = len(sorted_concepts)
        start_idx = (request.page - 1) * request.page_size
        end_idx = start_idx + request.page_size
        page_concepts = sorted_concepts[start_idx:end_idx]
        
        # 6. 构建结果项
        items = self._build_result_items(page_concepts)
        
        query_time_ms = (time.perf_counter() - start_time) * 1000
        
        return QueryResult(
            items=items,
            total_count=total_count,
            page=request.page,
            page_size=request.page_size,
            has_more=end_idx < total_count,
            query_time_ms=query_time_ms,
        )
    
    def batch_query(
        self,
        request: BatchQueryRequest,
        max_workers: int = 4,
    ) -> BatchQueryResult:
        """
        批量查询（并行执行）
        
        Args:
            request: 批量查询请求
            max_workers: 最大并行数
            
        Returns:
            BatchQueryResult: 批量结果
        """
        start_time = time.perf_counter()
        results: List[QueryResult] = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(self.query, q)
                for q in request.queries
            ]
            
            for future in futures:
                try:
                    results.append(future.result())
                except Exception as e:
                    logger.error(f"Query failed: {e}")
                    # 返回空结果
                    results.append(QueryResult(
                        items=[],
                        total_count=0,
                        page=1,
                        page_size=20,
                        has_more=False,
                        query_time_ms=0.0,
                    ))
        
        total_time_ms = (time.perf_counter() - start_time) * 1000
        
        return BatchQueryResult(
            results=results,
            total_time_ms=total_time_ms,
        )
    
    def _get_candidates(self, request: SemanticQuery) -> List[ConceptNode]:
        """获取候选概念"""
        if request.factor_ids:
            # 使用因子索引
            return self._query_by_factors(request.factor_ids)
        else:
            # 返回所有概念
            return list(self.graph.concepts)
    
    def _query_by_factors(self, factor_ids: List[str]) -> List[ConceptNode]:
        """按因子查询概念"""
        # 使用图谱的内置方法
        return self.graph.query_by_factors(factor_ids)
    
    def _apply_filters(
        self,
        concepts: List[ConceptNode],
        request: SemanticQuery,
    ) -> List[ConceptNode]:
        """应用过滤条件"""
        filtered = concepts
        
        # 维度过滤
        if request.dimension:
            filtered = [c for c in filtered if c.dimension == request.dimension]
        
        # 体系过滤
        if request.divination_system:
            filtered = [
                c for c in filtered 
                if c.divination_system == request.divination_system
            ]
        
        # 权威性阈值过滤
        if request.authority_threshold > 0:
            filtered = [
                c for c in filtered 
                if c.authority_score >= request.authority_threshold
            ]
        
        return filtered
    
    def _expand_with_traversal(
        self,
        concepts: List[ConceptNode],
        request: SemanticQuery,
    ) -> List[ConceptNode]:
        """通过遍历扩展相关概念"""
        seen_ids: Set[str] = {c.concept_id for c in concepts}
        expanded = list(concepts)
        
        for concept in concepts:
            result = self._traversal.bfs_traverse(
                start_concept_id=concept.concept_id,
                max_depth=request.traversal_depth,
                relation_types=request.filter_relation_types,
            )
            
            for related in result.concepts:
                if related.concept_id not in seen_ids:
                    seen_ids.add(related.concept_id)
                    expanded.append(related)
        
        return expanded
    
    def _build_result_items(
        self,
        concepts: List[ConceptNode],
    ) -> List[QueryResultItem]:
        """构建结果项"""
        items = []
        
        for concept in concepts:
            # 收集snippet_ids
            snippet_ids = []
            for source in concept.source_nodes:
                if hasattr(source, 'snippet_ids') and source.snippet_ids:
                    snippet_ids.extend(source.snippet_ids)
            
            # 检查冲突警告
            warnings = self._get_conflict_warnings(concept)
            
            items.append(QueryResultItem(
                concept=concept,
                relevance_score=concept.authority_score,  # 简化：使用authority作为relevance
                related_snippet_ids=snippet_ids[:10],  # 限制数量
                conflict_warnings=warnings,
            ))
        
        return items
    
    def _get_conflict_warnings(self, concept: ConceptNode) -> List[ConflictWarning]:
        """获取概念的冲突警告"""
        warnings = []
        
        if concept.conflict_summary and concept.conflict_summary.conflict_count > 0:
            # 确定严重程度
            if concept.conflict_summary.conflict_count >= 3:
                severity = "HIGH"
            elif concept.conflict_summary.conflict_count >= 2:
                severity = "MEDIUM"
            else:
                severity = "LOW"
            
            # Find conflicting concepts from graph edges
            conflicting_ids = self._find_conflicting_concept_ids(concept.concept_id)
            for conflicting_id in conflicting_ids:
                warnings.append(ConflictWarning(
                    concept_id=concept.concept_id,
                    conflicting_concept_id=conflicting_id,
                    conflict_type=concept.conflict_summary.conflict_types[0] if concept.conflict_summary.conflict_types else "unknown",
                    severity=severity,
                    resolution_hint=f"参考 {concept.conflict_summary.highest_authority_source or '最高权威来源'}",
                ))
            
            # If no edges found but conflict_summary exists, create a self-reference warning
            if not conflicting_ids:
                warnings.append(ConflictWarning(
                    concept_id=concept.concept_id,
                    conflicting_concept_id=concept.concept_id,
                    conflict_type=concept.conflict_summary.conflict_types[0] if concept.conflict_summary.conflict_types else "unknown",
                    severity=severity,
                    resolution_hint=f"参考 {concept.conflict_summary.highest_authority_source or '最高权威来源'}",
                ))
        
        return warnings
    
    def _find_conflicting_concept_ids(self, concept_id: str) -> List[str]:
        """Find concept IDs that conflict with the given concept"""
        conflicting = []
        for edge in self.graph.edges:
            if edge.relation_type == RelationType.CONFLICTS_WITH:
                if edge.source_concept_id == concept_id:
                    conflicting.append(edge.target_concept_id)
                elif edge.target_concept_id == concept_id:
                    conflicting.append(edge.source_concept_id)
        return conflicting
    
    def query_related(
        self,
        concept_id: str,
        depth: int = 1,
        relation_types: Optional[List[RelationType]] = None,
    ) -> List[ConceptNode]:
        """
        查询相关概念（便捷方法）
        
        Args:
            concept_id: 起始概念ID
            depth: 遍历深度
            relation_types: 限制边类型
            
        Returns:
            相关概念列表
        """
        result = self._traversal.bfs_traverse(
            start_concept_id=concept_id,
            max_depth=depth,
            relation_types=relation_types,
        )
        return result.concepts
