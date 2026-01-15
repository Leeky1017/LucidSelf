"""
Semantic Query Engine

语义查询引擎。

对照架构文档:
- docs/ls_engine_architecture_v3.md §4.2, §5.1
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from backend.core.contracts import FactorMatrix
from backend.semantics.core.base import SemanticEntry, SemanticRegistry

logger = logging.getLogger(__name__)


@dataclass
class QueryMetrics:
    """查询性能指标"""
    query_time_ms: float = 0.0
    entries_scanned: int = 0
    entries_returned: int = 0
    cache_hit: bool = False


class SemanticQueryEngine:
    """
    语义查询引擎
    
    对照架构v3 §5.1:
    - 按因子查询语义
    - 语义搜索
    - 跨领域导航
    """
    
    def __init__(self, registry: type = None):
        """
        初始化查询引擎
        
        Args:
            registry: 语义注册中心类（默认使用全局SemanticRegistry）
        """
        self.registry = registry or SemanticRegistry
        self._cache: Dict[str, List[SemanticEntry]] = {}
        self._cache_ttl = 300  # 5 minutes
    
    async def query_by_factors(
        self,
        factor_ids: List[str],
        limit: int = 10,
    ) -> List[SemanticEntry]:
        """
        按因子ID列表查询相关语义
        
        Args:
            factor_ids: 因子ID列表
            limit: 返回数量限制
            
        Returns:
            语义条目列表（按相关度排序）
        """
        start = time.perf_counter()
        
        entries = self.registry.query_by_factors(factor_ids)
        
        # 按相关度排序（匹配因子数量）
        factor_set = set(factor_ids)
        entries.sort(
            key=lambda e: len(set(e.factor_refs) & factor_set),
            reverse=True
        )
        
        result = entries[:limit]
        
        elapsed = (time.perf_counter() - start) * 1000
        logger.debug(f"query_by_factors: {len(result)} entries in {elapsed:.2f}ms")
        
        return result
    
    async def get_contextual_semantics(
        self,
        factor_matrix: FactorMatrix,
        dimension: Optional[str] = None,
        limit_per_dimension: int = 5,
    ) -> Dict[str, List[SemanticEntry]]:
        """
        获取因子矩阵关联的语义上下文
        
        Args:
            factor_matrix: 因子矩阵
            dimension: 指定维度（可选）
            limit_per_dimension: 每个维度最多返回条目数
            
        Returns:
            按维度分组的语义条目字典
        """
        factor_ids = list(factor_matrix.factors.keys())
        entries = await self.query_by_factors(factor_ids, limit=50)
        
        # 按维度分组（简化实现：按subject分组）
        grouped: Dict[str, List[SemanticEntry]] = {}
        for entry in entries:
            dim = self._infer_dimension(entry)
            if dim not in grouped:
                grouped[dim] = []
            if len(grouped[dim]) < limit_per_dimension:
                grouped[dim].append(entry)
        
        if dimension:
            return {dimension: grouped.get(dimension, [])}
        return grouped
    
    def _infer_dimension(self, entry: SemanticEntry) -> str:
        """
        推断语义条目的维度
        
        根据subject、factor_refs等信息推断维度。
        """
        subject = entry.subject.lower() if entry.subject else ""
        
        # 简单的关键词匹配
        dimension_keywords = {
            "career": ["career", "work", "job", "官", "职", "业"],
            "wealth": ["wealth", "money", "财", "富"],
            "health": ["health", "body", "健康", "身"],
            "relationship": ["love", "marriage", "relationship", "婚", "姻", "情"],
            "personality": ["personality", "character", "性格", "性情"],
        }
        
        for dim, keywords in dimension_keywords.items():
            if any(kw in subject for kw in keywords):
                return dim
        
        return "general"
    
    async def search_text(
        self,
        query: str,
        book_id: Optional[str] = None,
        limit: int = 10,
    ) -> List[SemanticEntry]:
        """
        文本搜索（简化实现）
        
        Args:
            query: 搜索文本
            book_id: 限定书籍
            limit: 返回数量限制
            
        Returns:
            匹配的语义条目列表
        """
        if book_id:
            entries = self.registry.get_by_book(book_id)
        else:
            entries = list(self.registry._entries.values())
        
        # 简单的文本匹配
        results = []
        query_lower = query.lower()
        for entry in entries:
            text = (entry.original_text + entry.normalized_text_zh).lower()
            if query_lower in text:
                results.append(entry)
                if len(results) >= limit:
                    break
        
        return results
