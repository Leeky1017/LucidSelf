"""
Rule Context

规则执行上下文 - 封装因子矩阵访问和语义缓存。

对照 requirements.md Requirement 1.3:
- get_factor(), get_factor_value(), get_factors(), has_factor()

对照 requirements.md Requirement 1.4:
- get_semantic_entry(), resolve_semantic_refs()
- SemanticCache 集成

对照 design.md §2 RuleContext
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from backend.core.contracts import FactorMatrix, FactorValue

if TYPE_CHECKING:
    from backend.semantics.core.base import SemanticEntry
    from backend.semantics.core.cache import SemanticCache
    from backend.semantics.core.query import SemanticQueryEngine

logger = logging.getLogger(__name__)


class RuleContext:
    """
    规则执行上下文
    
    封装因子矩阵访问，提供简化的因子查询接口。
    支持语义条目懒加载和访问日志。
    
    对照 design.md:
    - 因子访问方法缓存
    - 语义条目懒加载
    - 访问日志（用于热点分析）
    """
    
    def __init__(
        self,
        factor_matrix: FactorMatrix,
        semantic_cache: Optional["SemanticCache"] = None,
        query_engine: Optional["SemanticQueryEngine"] = None,
    ):
        """
        初始化规则上下文
        
        Args:
            factor_matrix: 因子矩阵（来自 L1 Calculator）
            semantic_cache: 语义缓存（可选）
            query_engine: 语义查询引擎（可选）
        """
        self.factor_matrix = factor_matrix
        self.semantic_cache = semantic_cache
        self._query_engine = query_engine
        
        # 因子值缓存（批量查询优化）
        self._factors_cache: Dict[tuple, Dict[str, Any]] = {}
        
        # 语义条目缓存（懒加载）
        self._semantic_entries_cache: Dict[str, "SemanticEntry"] = {}
        
        # 访问日志（热点分析）
        self._semantic_access_log: List[Dict[str, Any]] = []
    
    # =========================================================================
    # 因子访问方法 (Requirement 1.3)
    # =========================================================================
    
    def get_factor(self, factor_id: str) -> Optional[FactorValue]:
        """
        获取单个因子
        
        Args:
            factor_id: 因子 ID
        
        Returns:
            FactorValue 实例，未找到返回 None
        """
        return self.factor_matrix.get(factor_id)
    
    def get_factor_value(self, factor_id: str, default: Any = None) -> Any:
        """
        获取因子值
        
        Args:
            factor_id: 因子 ID
            default: 默认值
        
        Returns:
            因子值，未找到返回 default
        """
        fv = self.factor_matrix.get(factor_id)
        return fv.value if fv else default
    
    def get_factors(self, factor_ids: List[str]) -> Dict[str, Any]:
        """
        批量获取因子值
        
        Args:
            factor_ids: 因子 ID 列表
        
        Returns:
            {factor_id: value} 字典
        """
        cache_key = tuple(sorted(factor_ids))
        
        if cache_key in self._factors_cache:
            return self._factors_cache[cache_key]
        
        result = {}
        for fid in factor_ids:
            fv = self.factor_matrix.get(fid)
            result[fid] = fv.value if fv else None
        
        self._factors_cache[cache_key] = result
        return result
    
    def has_factor(self, factor_id: str) -> bool:
        """
        检查因子是否存在
        
        Args:
            factor_id: 因子 ID
        
        Returns:
            是否存在
        """
        return self.factor_matrix.has(factor_id)
    
    def get(self, factor_id: str) -> Any:
        """
        快捷方法：直接获取因子值
        
        用于条件表达式中: context.get("factor_id")
        
        Args:
            factor_id: 因子 ID
        
        Returns:
            因子值，未找到返回 None
        """
        return self.get_factor_value(factor_id)
    
    # =========================================================================
    # 语义条目访问 (Requirement 1.4)
    # =========================================================================
    
    def get_semantic_entry(self, semantic_id: str) -> Optional["SemanticEntry"]:
        """
        获取语义条目（支持懒加载）
        
        首次访问时触发加载，加载后缓存。
        
        Args:
            semantic_id: 语义条目 ID
        
        Returns:
            SemanticEntry 实例，未找到返回 None
        """
        # 1. 检查本地缓存
        if semantic_id in self._semantic_entries_cache:
            self._log_semantic_access(semantic_id, "local_cache")
            return self._semantic_entries_cache[semantic_id]
        
        # 2. 检查 SemanticCache
        if self.semantic_cache:
            try:
                entry = self.semantic_cache.get_sync(semantic_id)
                if entry:
                    self._semantic_entries_cache[semantic_id] = entry
                    self._log_semantic_access(semantic_id, "semantic_cache")
                    return entry
            except Exception as e:
                logger.debug(f"SemanticCache lookup failed: {e}")
        
        # 3. 通过 Registry 直接查询
        try:
            from backend.semantics.core.base import SemanticRegistry
            entry = SemanticRegistry.get(semantic_id)
            if entry:
                # 写入缓存
                if self.semantic_cache:
                    try:
                        self.semantic_cache.set_sync(semantic_id, entry)
                    except Exception:
                        pass  # 缓存写入失败不影响主流程
                self._semantic_entries_cache[semantic_id] = entry
                self._log_semantic_access(semantic_id, "registry")
                return entry
        except Exception as e:
            logger.debug(f"SemanticRegistry lookup failed: {e}")
        
        self._log_semantic_access(semantic_id, "not_found")
        return None
    
    def resolve_semantic_refs(
        self,
        semantic_refs: List[str],
    ) -> List["SemanticEntry"]:
        """
        批量解析 semantic_refs 为 SemanticEntry 实例
        
        Args:
            semantic_refs: 语义条目 ID 列表
        
        Returns:
            已解析的 SemanticEntry 列表（跳过未找到的）
        """
        entries = []
        for ref in semantic_refs:
            entry = self.get_semantic_entry(ref)
            if entry:
                entries.append(entry)
        return entries
    
    def _log_semantic_access(
        self,
        semantic_id: str,
        source: str,
        rule_id: Optional[str] = None,
    ) -> None:
        """
        记录语义条目访问日志
        
        用于缓存优化和热点分析。
        
        Args:
            semantic_id: 语义条目 ID
            source: 来源（local_cache/semantic_cache/registry/not_found）
            rule_id: 关联的规则 ID（可选）
        """
        log_entry = {
            "semantic_id": semantic_id,
            "rule_id": rule_id,
            "timestamp": datetime.now().isoformat(),
            "source": source,
        }
        self._semantic_access_log.append(log_entry)
        
        # DEBUG 级别输出
        logger.debug(f"Semantic access: {json.dumps(log_entry)}")
    
    def get_semantic_access_log(self) -> List[Dict[str, Any]]:
        """
        获取语义访问日志
        
        Returns:
            访问日志列表
        """
        return self._semantic_access_log.copy()
    
    def clear_caches(self) -> None:
        """清空所有缓存"""
        self._factors_cache.clear()
        self._semantic_entries_cache.clear()
        self._semantic_access_log.clear()
