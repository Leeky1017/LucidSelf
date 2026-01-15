"""
Rule Engine

规则引擎核心 - 执行规则匹配和推理。

对照 requirements.md Requirement 1:
- 执行规则并返回 RuntimeRuleResult 列表
- 支持 @register_rule 装饰器注册
- 支持按 category 和 engine_id 过滤
- 错误隔离，单规则失败不影响其他规则
- execution_time_ms 跟踪

对照 design.md §1 RuleEngine
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Set

from backend.core.contracts import FactorMatrix, RuntimeRuleResult
from backend.core.engines.governance import (
    EngineIdGovernanceError,
    validate_engine_id_or_raise,
    validate_engine_ids_or_raise,
)
from backend.rules.context import RuleContext

if TYPE_CHECKING:
    from backend.rules.conflict import ConflictResolver
    from backend.semantics.core.cache import SemanticCache

logger = logging.getLogger(__name__)


class RuleExecutionError(Exception):
    """规则执行错误"""
    
    def __init__(
        self,
        rule_id: str,
        message: str,
        cause: Optional[Exception] = None,
    ):
        self.rule_id = rule_id
        self.message = message
        self.cause = cause
        super().__init__(f"Rule {rule_id} failed: {message}")


class RuleEngine:
    """
    规则引擎核心
    
    职责：
    - 管理规则注册表（按 rule_id、category、engine_id 索引）
    - 执行规则并收集结果
    - 集成冲突解决器
    - 支持性能监控
    
    对照 design.md 设计:
    - O(1) 规则查找
    - 错误隔离
    - execution_time_ms 跟踪
    """
    
    def __init__(
        self,
        semantic_cache: Optional["SemanticCache"] = None,
        conflict_resolver: Optional["ConflictResolver"] = None,
    ):
        """
        初始化规则引擎
        
        Args:
            semantic_cache: 语义缓存（用于 RuleContext）
            conflict_resolver: 冲突解决器
        """
        # 规则注册表 - O(1) 查找
        self._rules: Dict[str, Callable] = {}  # rule_id -> rule_func
        self._rules_by_category: Dict[str, List[Callable]] = {}
        self._rules_by_engine: Dict[str, List[Callable]] = {}
        
        # 依赖注入
        self.semantic_cache = semantic_cache
        self.conflict_resolver = conflict_resolver
        
        # 性能监控
        self._profiling_enabled = False
        self._execution_stats: Dict[str, List[float]] = {}
    
    def register(self, rule_func: Callable) -> None:
        """
        注册规则函数
        
        规则函数必须使用 @register_rule 装饰器标注元数据。
        
        对照 Requirement 1.2:
        - 自动注册 rule_id, category, priority, exclusive_group
        
        对照 Requirement 1.10:
        - 按 rule_id 和 category 索引，O(1) 查找
        
        Args:
            rule_func: 带 @register_rule 装饰器的规则函数
        
        Raises:
            ValueError: 如果函数缺少 @register_rule 装饰器
        """
        if not hasattr(rule_func, "_rule_metadata"):
            raise ValueError(
                f"Rule function {rule_func.__name__} missing @register_rule decorator"
            )
        
        metadata = rule_func._rule_metadata
        rule_id = metadata["rule_id"]
        category = metadata.get("category", "default")
        engine_id = metadata.get("engine_id", "unknown")

        if not engine_id or engine_id == "unknown":
            raise EngineIdGovernanceError(
                "MISSING_ENGINE_ID",
                f"Rule '{rule_id}' must declare a valid engine_id",
                engine_id=engine_id,
            )
        validate_engine_id_or_raise(engine_id)
        
        # 检查重复注册
        if rule_id in self._rules:
            logger.warning(f"Rule {rule_id} already registered, overwriting")
        
        # 注册到主索引
        self._rules[rule_id] = rule_func
        
        # 注册到 category 索引
        if category not in self._rules_by_category:
            self._rules_by_category[category] = []
        if rule_func not in self._rules_by_category[category]:
            self._rules_by_category[category].append(rule_func)
        
        # 注册到 engine_id 索引
        if engine_id not in self._rules_by_engine:
            self._rules_by_engine[engine_id] = []
        if rule_func not in self._rules_by_engine[engine_id]:
            self._rules_by_engine[engine_id].append(rule_func)
        
        logger.debug(
            f"Registered rule: {rule_id} (category={category}, engine={engine_id})"
        )
    
    def unregister(self, rule_id: str) -> bool:
        """
        取消注册规则
        
        Args:
            rule_id: 规则 ID
        
        Returns:
            是否成功取消注册
        """
        if rule_id not in self._rules:
            return False
        
        rule_func = self._rules[rule_id]
        metadata = rule_func._rule_metadata
        category = metadata.get("category", "default")
        engine_id = metadata.get("engine_id", "unknown")
        
        # 从所有索引中移除
        del self._rules[rule_id]
        
        if category in self._rules_by_category:
            self._rules_by_category[category] = [
                r for r in self._rules_by_category[category]
                if r._rule_metadata["rule_id"] != rule_id
            ]
        
        if engine_id in self._rules_by_engine:
            self._rules_by_engine[engine_id] = [
                r for r in self._rules_by_engine[engine_id]
                if r._rule_metadata["rule_id"] != rule_id
            ]
        
        logger.debug(f"Unregistered rule: {rule_id}")
        return True
    
    def load_from_registry(self) -> int:
        """
        从全局装饰器注册表加载所有规则
        
        调用此方法会将 @register_rule 装饰的规则加载到引擎中。
        
        Returns:
            加载的规则数量
        """
        from backend.core.decorators import get_all_rules
        
        all_rules = get_all_rules()
        count = 0
        
        for rule_id, metadata in all_rules.items():
            if rule_id not in self._rules:
                rule_func = metadata["func"]
                self.register(rule_func)
                count += 1
        
        logger.info(f"Loaded {count} rules from global registry")
        return count
    
    def execute_all(
        self,
        factor_matrix: FactorMatrix,
        categories: Optional[List[str]] = None,
        engine_ids: Optional[List[str]] = None,
        resolve_conflicts: bool = True,
    ) -> List[RuntimeRuleResult]:
        """
        执行所有匹配的规则
        
        对照 Requirement 1.1:
        - 在 10ms 内执行最多 100 条规则
        
        对照 Requirement 1.5:
        - 支持按 category 过滤
        
        对照 Requirement 1.6:
        - 错误隔离，单规则失败不影响其他规则
        
        对照 Requirement 1.7:
        - 每个结果包含 execution_time_ms
        
        Args:
            factor_matrix: 因子矩阵（来自 L1 Calculator）
            categories: 可选，仅执行指定分类的规则
            engine_ids: 可选，仅执行指定引擎的规则
            resolve_conflicts: 是否解决互斥冲突
        
        Returns:
            规则执行结果列表
        """
        start_time = time.perf_counter()
        
        # Gate-0: engine_id 格式 + registry 校验（确定性拒绝原因）
        engine_ids = validate_engine_ids_or_raise(engine_ids)

        # 创建执行上下文
        context = RuleContext(
            factor_matrix=factor_matrix,
            semantic_cache=self.semantic_cache,
        )
        
        # 确定要执行的规则
        rules_to_run = self._select_rules(categories, engine_ids)
        
        # 执行规则（错误隔离）
        results: List[RuntimeRuleResult] = []
        for rule_func in rules_to_run:
            result = self._execute_rule_safe(rule_func, context)
            if result is not None:
                results.append(result)
        
        # 冲突解决
        if resolve_conflicts and self.conflict_resolver:
            results = self.conflict_resolver.resolve_all(results)
        
        total_time = (time.perf_counter() - start_time) * 1000
        logger.debug(f"Executed {len(rules_to_run)} rules in {total_time:.2f}ms")
        
        return results
    
    def execute_matched(
        self,
        factor_matrix: FactorMatrix,
        categories: Optional[List[str]] = None,
        engine_ids: Optional[List[str]] = None,
    ) -> List[RuntimeRuleResult]:
        """
        仅返回匹配的规则结果
        
        Args:
            factor_matrix: 因子矩阵
            categories: 可选，仅执行指定分类的规则
            engine_ids: 可选，仅执行指定引擎的规则
        
        Returns:
            匹配的规则结果列表
        """
        all_results = self.execute_all(
            factor_matrix, categories, engine_ids, resolve_conflicts=True
        )
        return [r for r in all_results if r.matched]
    
    def _execute_rule_safe(
        self,
        rule_func: Callable,
        context: RuleContext,
    ) -> Optional[RuntimeRuleResult]:
        """
        安全执行单个规则
        
        对照 Requirement 1.6:
        - 捕获异常，记录错误但继续执行其他规则
        
        对照 Requirement 1.9:
        - 对于 is_complex_logic=True 的规则，委托给 python_handler_ref
        
        Args:
            rule_func: 规则函数
            context: 执行上下文
        
        Returns:
            规则结果，如果执行失败返回 None
        """
        rule_id = rule_func._rule_metadata.get("rule_id", "unknown")
        
        try:
            rule_start = time.perf_counter()
            result = rule_func(context)
            rule_end = time.perf_counter()
            
            # 确保 execution_time_ms 被设置
            execution_time_ms = (rule_end - rule_start) * 1000
            if hasattr(result, 'execution_time_ms') and result.execution_time_ms == 0:
                # 创建新的结果对象以更新 execution_time_ms
                result = RuntimeRuleResult(
                    rule_id=result.rule_id,
                    matched=result.matched,
                    dimension=result.dimension,
                    level=result.level,
                    description=result.description,
                    confidence=result.confidence,
                    weight=result.weight,
                    tags=result.tags,
                    evidence_factors=result.evidence_factors,
                    semantic_refs=result.semantic_refs,
                    cross_domain_axes=result.cross_domain_axes,
                    source_book=result.source_book,
                    l1_anchor=result.l1_anchor,
                    execution_time_ms=execution_time_ms,
                )
            
            # 性能统计
            if self._profiling_enabled:
                if rule_id not in self._execution_stats:
                    self._execution_stats[rule_id] = []
                self._execution_stats[rule_id].append(execution_time_ms)
            
            return result
            
        except NotImplementedError as e:
            # 复杂规则未实现，记录警告但不中断
            logger.warning(f"Rule {rule_id} not implemented: {e}")
            return None
            
        except Exception as e:
            # 其他错误，记录错误但继续执行
            logger.error(f"Rule {rule_id} execution failed: {e}", exc_info=True)
            return None
    
    def _select_rules(
        self,
        categories: Optional[List[str]],
        engine_ids: Optional[List[str]],
    ) -> List[Callable]:
        """
        选择要执行的规则
        
        Args:
            categories: 分类过滤
            engine_ids: 引擎过滤
        
        Returns:
            规则函数列表
        """
        if categories is None and engine_ids is None:
            return list(self._rules.values())
        
        selected: Set[Callable] = set()
        
        if categories:
            for cat in categories:
                selected.update(self._rules_by_category.get(cat, []))
        
        if engine_ids:
            for eid in engine_ids:
                selected.update(self._rules_by_engine.get(eid, []))
        
        return list(selected)
    
    # =========================================================================
    # 查询接口 (Requirement 1.10)
    # =========================================================================
    
    def get_rule(self, rule_id: str) -> Optional[Callable]:
        """
        O(1) 规则查找
        
        Args:
            rule_id: 规则 ID
        
        Returns:
            规则函数，未找到返回 None
        """
        return self._rules.get(rule_id)
    
    def get_rule_count(self) -> int:
        """获取注册规则总数"""
        return len(self._rules)
    
    def get_categories(self) -> List[str]:
        """获取所有规则分类"""
        return list(self._rules_by_category.keys())
    
    def get_engine_ids(self) -> List[str]:
        """获取所有引擎 ID"""
        return list(self._rules_by_engine.keys())
    
    def get_rules_by_category(self, category: str) -> List[Callable]:
        """按分类获取规则"""
        return self._rules_by_category.get(category, []).copy()
    
    def get_rules_by_engine(self, engine_id: str) -> List[Callable]:
        """按引擎获取规则"""
        return self._rules_by_engine.get(engine_id, []).copy()
    
    # =========================================================================
    # 性能监控
    # =========================================================================
    
    def enable_profiling(self, enabled: bool = True) -> None:
        """启用/禁用性能分析"""
        self._profiling_enabled = enabled
        if not enabled:
            self._execution_stats.clear()
    
    def get_profiling_stats(self) -> Dict[str, Dict[str, float]]:
        """
        获取性能统计
        
        Returns:
            {rule_id: {"avg_ms": ..., "min_ms": ..., "max_ms": ..., "count": ...}}
        """
        stats = {}
        for rule_id, times in self._execution_stats.items():
            if times:
                stats[rule_id] = {
                    "avg_ms": sum(times) / len(times),
                    "min_ms": min(times),
                    "max_ms": max(times),
                    "count": len(times),
                }
        return stats
    
    def clear_profiling_stats(self) -> None:
        """清空性能统计"""
        self._execution_stats.clear()
    
    # =========================================================================
    # 元数据接口 (Requirement 10.5.6)
    # =========================================================================
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        获取规则引擎元数据（内省 API）
        
        Returns:
            引擎元数据字典
        """
        exclusive_groups: Set[str] = set()
        for rule_func in self._rules.values():
            group = rule_func._rule_metadata.get("exclusive_group", "")
            if group:
                exclusive_groups.add(group)
        
        return {
            "rule_count": self.get_rule_count(),
            "categories": self.get_categories(),
            "engine_ids": self.get_engine_ids(),
            "exclusive_groups": list(exclusive_groups),
        }
    
    # =========================================================================
    # Layer Integration (Requirement 10.5)
    # =========================================================================
    
    async def execute_all_async(
        self,
        factor_matrix: FactorMatrix,
        categories: Optional[List[str]] = None,
        engine_ids: Optional[List[str]] = None,
    ) -> List[RuntimeRuleResult]:
        """
        异步执行规则（用于 FastAPI 集成）
        
        对照 Requirement 10.5.8:
        - 异步包装同步执行
        - 用于 FastAPI async endpoints
        
        Args:
            factor_matrix: 因子矩阵
            categories: 可选，仅执行指定分类的规则
            engine_ids: 可选，仅执行指定引擎的规则
        
        Returns:
            规则执行结果列表
        """
        import asyncio
        
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: self.execute_all(factor_matrix, categories, engine_ids)
        )
    
    def execute_batch(
        self,
        factor_matrices: List[FactorMatrix],
        categories: Optional[List[str]] = None,
    ) -> Dict[str, List[RuntimeRuleResult]]:
        """
        批量执行多个体系的 FactorMatrix
        
        对照 Requirement 10.5.4:
        - 接受 List[FactorMatrix]
        - 返回 Dict[engine_id, List[RuntimeRuleResult]]
        
        Args:
            factor_matrices: 因子矩阵列表（来自多个体系）
            categories: 可选，仅执行指定分类的规则
        
        Returns:
            {engine_id: List[RuntimeRuleResult]} 字典
        """
        results: Dict[str, List[RuntimeRuleResult]] = {}
        
        for matrix in factor_matrices:
            engine_id = matrix.engine_id
            validate_engine_id_or_raise(engine_id)
            engine_results = self.execute_all(
                matrix,
                categories=categories,
                engine_ids=[engine_id] if engine_id else None,
            )
            results[engine_id] = engine_results
        
        return results
    
    def execute_with_partial_results(
        self,
        factor_matrix: FactorMatrix,
        categories: Optional[List[str]] = None,
        engine_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        执行规则，返回成功结果和错误信息
        
        对照 Requirement 10.5.9:
        - 部分结果 + 错误元数据
        
        Args:
            factor_matrix: 因子矩阵
            categories: 可选分类过滤
            engine_ids: 可选引擎过滤
        
        Returns:
            {
                "results": List[RuntimeRuleResult],
                "errors": List[Dict],
                "execution_time_ms": float
            }
        """
        start_time = time.perf_counter()
        
        context = RuleContext(
            factor_matrix=factor_matrix,
            semantic_cache=self.semantic_cache,
        )
        
        rules_to_run = self._select_rules(categories, engine_ids)
        
        results: List[RuntimeRuleResult] = []
        errors: List[Dict[str, Any]] = []
        
        for rule_func in rules_to_run:
            rule_id = rule_func._rule_metadata.get("rule_id", "unknown")
            
            try:
                result = self._execute_rule_safe(rule_func, context)
                if result is not None:
                    results.append(result)
            except Exception as e:
                errors.append({
                    "rule_id": rule_id,
                    "error_type": type(e).__name__,
                    "message": str(e),
                })
        
        # 冲突解决
        if self.conflict_resolver:
            results = self.conflict_resolver.resolve_all(results)
        
        total_time = (time.perf_counter() - start_time) * 1000
        
        return {
            "results": results,
            "errors": errors,
            "execution_time_ms": total_time,
        }
