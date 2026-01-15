"""
Semantic Indexer

语义索引器。

对照架构文档:
- docs/ls_engine_architecture_v3.md §4.2
"""

from __future__ import annotations

import logging
from typing import Dict, List, Set, Optional

from backend.semantics.core.base import SemanticEntry, SemanticRegistry

logger = logging.getLogger(__name__)


class SemanticIndexer:
    """
    语义索引器
    
    提供高级索引和检索功能。
    """
    
    def __init__(self, registry: type = None):
        """
        初始化索引器
        
        Args:
            registry: 语义注册中心类
        """
        self.registry = registry or SemanticRegistry
        self._term_index: Dict[str, Set[str]] = {}  # term -> semantic_ids
        self._indexed = False
    
    def build_index(self) -> None:
        """
        构建术语索引
        
        从所有已注册的语义条目中提取术语并建立索引。
        """
        logger.info("Building semantic term index...")
        self._term_index.clear()
        
        for semantic_id, entry in self.registry._entries.items():
            # 索引术语
            for term_dict in entry.terms:
                term = term_dict.get("term", "").lower()
                if term:
                    if term not in self._term_index:
                        self._term_index[term] = set()
                    self._term_index[term].add(semantic_id)
            
            # 索引subject
            if entry.subject:
                subject = entry.subject.lower()
                if subject not in self._term_index:
                    self._term_index[subject] = set()
                self._term_index[subject].add(semantic_id)
        
        self._indexed = True
        logger.info(f"Indexed {len(self._term_index)} terms from {len(self.registry._entries)} entries")
    
    def search_by_term(self, term: str, limit: int = 10) -> List[SemanticEntry]:
        """
        按术语搜索
        
        Args:
            term: 搜索术语
            limit: 返回数量限制
            
        Returns:
            匹配的语义条目列表
        """
        if not self._indexed:
            self.build_index()
        
        term_lower = term.lower()
        matching_ids = self._term_index.get(term_lower, set())
        
        # 也搜索包含该术语的键
        for key, ids in self._term_index.items():
            if term_lower in key:
                matching_ids = matching_ids.union(ids)
        
        results = []
        for sid in list(matching_ids)[:limit]:
            entry = self.registry.get(sid)
            if entry:
                results.append(entry)
        
        return results
    
    def get_related_entries(
        self,
        semantic_id: str,
        limit: int = 5,
    ) -> List[SemanticEntry]:
        """
        获取相关语义条目
        
        基于共享因子和术语查找相关条目。
        
        Args:
            semantic_id: 基准语义ID
            limit: 返回数量限制
            
        Returns:
            相关语义条目列表
        """
        entry = self.registry.get(semantic_id)
        if not entry:
            return []
        
        # 基于共享因子查找
        related_ids: Set[str] = set()
        for factor_id in entry.factor_refs:
            ids = self.registry._by_factor.get(factor_id, set())
            related_ids.update(ids)
        
        # 排除自己
        related_ids.discard(semantic_id)
        
        # 按共享因子数量排序
        def score(sid: str) -> int:
            other = self.registry.get(sid)
            if not other:
                return 0
            return len(set(entry.factor_refs) & set(other.factor_refs))
        
        sorted_ids = sorted(related_ids, key=score, reverse=True)[:limit]
        
        return [self.registry.get(sid) for sid in sorted_ids if self.registry.get(sid)]
    
    def get_statistics(self) -> Dict:
        """获取索引统计信息"""
        return {
            "total_entries": len(self.registry._entries),
            "total_books": len(self.registry._by_book),
            "total_engines": len(self.registry._by_engine),
            "total_factors_indexed": len(self.registry._by_factor),
            "total_terms_indexed": len(self._term_index) if self._indexed else 0,
            "indexed": self._indexed,
        }
