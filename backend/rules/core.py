"""
Rule Engine Core

规则引擎核心实现，提供规则执行上下文和批量执行能力。

对照 semantic-core spec Task 16: L3 Rule Engine 集成
- RuleContext 新增 semantic_cache 字段
- 支持 semantic_refs 解析和懒加载
- 语义条目访问日志
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional

from backend.core.contracts import (
    FactorMatrix,
    FactorValue,
    RuntimeRuleResult,
)
from backend.core.decorators import register_rule  # noqa: F401

if TYPE_CHECKING:
    from backend.semantics.core.base import SemanticEntry
    from backend.semantics.core.cache import SemanticCache
    from backend.semantics.core.query import SemanticQueryEngine

logger = logging.getLogger(__name__)


class RuleContext:
    """
    规则执行上下文
    
    封装因子矩阵访问，提供简化的因子查询接口。
    
    对照 semantic-core spec Requirements 7.5:
    - semantic_cache: Optional[SemanticCache] 字段
    - 支持 semantic_refs 懒加载解析
    """
    
    def __init__(
        self,
        factor_matrix: FactorMatrix,
        semantic_cache: Optional["SemanticCache"] = None,
        query_engine: Optional["SemanticQueryEngine"] = None,
    ):
        self.factor_matrix = factor_matrix
        self._factors_cache: Dict[str, Any] = {}
        
        # 语义缓存支持 (Task 16.1)
        self.semantic_cache: Optional["SemanticCache"] = semantic_cache
        self._query_engine: Optional["SemanticQueryEngine"] = query_engine
        
        # 语义条目懒加载缓存 (Task 16.3)
        self._semantic_entries_cache: Dict[str, "SemanticEntry"] = {}
        
        # 访问日志 (Task 16.4)
        self._semantic_access_log: List[Dict[str, Any]] = []
    
    def get_factor(self, factor_id: str) -> Optional[FactorValue]:
        """获取单个因子"""
        return self.factor_matrix.get(factor_id)
    
    def get_factor_value(self, factor_id: str, default: Any = None) -> Any:
        """获取因子值"""
        fv = self.factor_matrix.get(factor_id)
        return fv.value if fv else default
    
    def get_factors(self, factor_ids: List[str]) -> Dict[str, Any]:
        """
        批量获取因子值（用于条件表达式）
        
        返回 {factor_id: value} 字典
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
        """检查因子是否存在"""
        return self.factor_matrix.has(factor_id)
    
    def get(self, factor_id: str) -> Any:
        """
        快捷方法：直接获取因子值
        
        用于条件表达式中: factors.get("factor_id")
        """
        return self.get_factor_value(factor_id)
    
    # =========================================================================
    # 语义条目访问 (Task 16.2, 16.3, 16.4)
    # =========================================================================
    
    def get_semantic_entry(self, semantic_id: str) -> Optional["SemanticEntry"]:
        """
        获取语义条目（支持懒加载）
        
        对照 Requirements 7.6: 首次访问时触发加载，加载后缓存
        
        Args:
            semantic_id: 语义条目 ID
        
        Returns:
            SemanticEntry 实例，未找到返回 None
        """
        # 1. 检查本地缓存
        if semantic_id in self._semantic_entries_cache:
            self._log_semantic_access(semantic_id, "local_cache")
            return self._semantic_entries_cache[semantic_id]
        
        # 2. 检查 SemanticCache (L1) - 使用同步方法
        if self.semantic_cache:
            entry = self.semantic_cache.get_sync(semantic_id)
            if entry:
                self._semantic_entries_cache[semantic_id] = entry
                self._log_semantic_access(semantic_id, "semantic_cache")
                return entry
        
        # 3. 通过 Registry 直接查询
        from backend.semantics.core.base import SemanticRegistry
        entry = SemanticRegistry.get(semantic_id)
        if entry:
            # 写入缓存 - 使用同步方法
            if self.semantic_cache:
                self.semantic_cache.set_sync(semantic_id, entry)
            self._semantic_entries_cache[semantic_id] = entry
            self._log_semantic_access(semantic_id, "registry")
            return entry
        
        self._log_semantic_access(semantic_id, "not_found")
        return None
    
    def resolve_semantic_refs(
        self,
        semantic_refs: List[str],
    ) -> List["SemanticEntry"]:
        """
        批量解析 semantic_refs 为 SemanticEntry 实例
        
        对照 Requirements 7.4: 在规则执行时解析 semantic_refs
        
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
        
        对照 Requirements 7.7: 用于缓存优化和热点分析
        
        日志格式: {"semantic_id": ..., "rule_id": ..., "timestamp": ..., "source": ...}
        """
        log_entry = {
            "semantic_id": semantic_id,
            "rule_id": rule_id,
            "timestamp": datetime.now().isoformat(),
            "source": source,
        }
        self._semantic_access_log.append(log_entry)
        
        # 仅 DEBUG 级别输出
        logger.debug(f"Semantic access: {json.dumps(log_entry)}")
    
    def get_semantic_access_log(self) -> List[Dict[str, Any]]:
        """获取语义访问日志（用于热点分析）"""
        return self._semantic_access_log.copy()


class RuleEngine:
    """
    规则引擎
    
    批量执行规则并收集结果。
    """
    
    def __init__(self):
        self._rules: List[Callable] = []
        self._rules_by_category: Dict[str, List[Callable]] = {}
    
    def register(self, rule_func: Callable) -> None:
        """注册规则函数"""
        self._rules.append(rule_func)
        
        # 按分类索引
        if hasattr(rule_func, "_rule_metadata"):
            cat = rule_func._rule_metadata.get("category", "default")
            if cat not in self._rules_by_category:
                self._rules_by_category[cat] = []
            self._rules_by_category[cat].append(rule_func)
    
    def execute_all(
        self,
        factor_matrix: FactorMatrix,
        categories: Optional[List[str]] = None,
    ) -> List[RuntimeRuleResult]:
        """
        执行所有规则
        
        Args:
            factor_matrix: 因子矩阵
            categories: 可选，仅执行指定分类的规则
        
        Returns:
            规则执行结果列表
        """
        context = RuleContext(factor_matrix)
        results: List[RuntimeRuleResult] = []
        
        rules_to_run = self._rules
        if categories:
            rules_to_run = []
            for cat in categories:
                rules_to_run.extend(self._rules_by_category.get(cat, []))
        
        for rule_func in rules_to_run:
            try:
                result = rule_func(context)
                results.append(result)
            except NotImplementedError as e:
                logger.warning(f"Rule not implemented: {e}")
            except Exception as e:
                logger.error(f"Rule execution failed: {e}")
        
        return results
    
    def execute_matched(
        self,
        factor_matrix: FactorMatrix,
        categories: Optional[List[str]] = None,
    ) -> List[RuntimeRuleResult]:
        """仅返回匹配的规则结果"""
        all_results = self.execute_all(factor_matrix, categories)
        return [r for r in all_results if r.matched]
    
    def resolve_conflicts(
        self,
        results: List[RuntimeRuleResult],
    ) -> List[RuntimeRuleResult]:
        """
        解决互斥冲突
        
        同一互斥组内，仅保留优先级最高的规则结果。
        """
        # TODO: 实现互斥组冲突解决
        return results
