"""
Test Rule Engine

规则引擎测试 - 验证规则注册、执行、错误隔离。

对照 tasks.md Task 1.3, 1.4, 1.7-1.10:
- Property 1: Rule Registration Completeness
- Property 9: Error Isolation
- Validates: Requirements 1.1-1.10
"""

import pytest
from hypothesis import given, strategies as st, settings
from unittest.mock import MagicMock, patch

from backend.core.contracts import FactorMatrix, FactorValue, RuntimeRuleResult
from backend.core.decorators import register_rule, clear_registry
from backend.rules.engine import RuleEngine, RuleExecutionError
from backend.rules.context import RuleContext


@pytest.fixture(autouse=True)
def clean_registry():
    """每个测试前清空全局注册表"""
    clear_registry()
    yield
    clear_registry()


@pytest.fixture
def sample_factor_matrix():
    """创建示例因子矩阵"""
    return FactorMatrix(
        engine_id="bazi-calculator",
        factors={
            "day_master": FactorValue(
                factor_id="day_master",
                value="甲",
                confidence=1.0,
                source="bazi-calculator",
            ),
            "month_branch": FactorValue(
                factor_id="month_branch",
                value="寅",
                confidence=1.0,
                source="bazi-calculator",
            ),
            "strength": FactorValue(
                factor_id="strength",
                value=0.7,
                confidence=0.9,
                source="bazi-calculator",
            ),
        },
    )


class TestRuleEngineRegistration:
    """规则注册测试"""
    
    def test_register_rule(self, sample_factor_matrix):
        """测试规则注册"""
        engine = RuleEngine()
        
        @register_rule(
            rule_id="test_rule_001",
            category="test",
            engine_id="bazi-calculator",
        )
        def test_rule(context: RuleContext) -> RuntimeRuleResult:
            return RuntimeRuleResult(
                rule_id="test_rule_001",
                matched=True,
                dimension="general",
                confidence=1.0,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(test_rule)
        
        assert engine.get_rule_count() == 1
        assert engine.get_rule("test_rule_001") is test_rule
        assert "test" in engine.get_categories()
    
    def test_register_multiple_rules(self, sample_factor_matrix):
        """测试多规则注册"""
        engine = RuleEngine()
        
        @register_rule(rule_id="rule_a", category="cat1", engine_id="bazi-calculator")
        def rule_a(ctx):
            return RuntimeRuleResult(
                rule_id="rule_a", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="rule_b", category="cat1", engine_id="bazi-calculator")
        def rule_b(ctx):
            return RuntimeRuleResult(
                rule_id="rule_b", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="rule_c", category="cat2", engine_id="bazi-calculator")
        def rule_c(ctx):
            return RuntimeRuleResult(
                rule_id="rule_c", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(rule_a)
        engine.register(rule_b)
        engine.register(rule_c)
        
        assert engine.get_rule_count() == 3
        assert set(engine.get_categories()) == {"cat1", "cat2"}
        assert len(engine.get_rules_by_category("cat1")) == 2
        assert len(engine.get_rules_by_category("cat2")) == 1
    
    def test_register_without_decorator(self):
        """测试注册无装饰器的函数应失败"""
        engine = RuleEngine()
        
        def plain_function(ctx):
            return None
        
        with pytest.raises(ValueError, match="missing @register_rule"):
            engine.register(plain_function)
    
    def test_unregister_rule(self, sample_factor_matrix):
        """测试取消注册"""
        engine = RuleEngine()
        
        @register_rule(rule_id="temp_rule", category="temp", engine_id="bazi-calculator")
        def temp_rule(ctx):
            return RuntimeRuleResult(
                rule_id="temp_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(temp_rule)
        assert engine.get_rule_count() == 1
        
        result = engine.unregister("temp_rule")
        assert result is True
        assert engine.get_rule_count() == 0
        assert engine.get_rule("temp_rule") is None
    
    def test_unregister_nonexistent(self):
        """测试取消注册不存在的规则"""
        engine = RuleEngine()
        result = engine.unregister("nonexistent")
        assert result is False


class TestRuleEngineExecution:
    """规则执行测试"""
    
    def test_execute_all(self, sample_factor_matrix):
        """测试执行所有规则"""
        engine = RuleEngine()
        
        @register_rule(rule_id="exec_test", category="test", engine_id="bazi-calculator")
        def exec_test(context: RuleContext) -> RuntimeRuleResult:
            day_master = context.get_factor_value("day_master")
            return RuntimeRuleResult(
                rule_id="exec_test",
                matched=day_master == "甲",
                dimension="general",
                confidence=1.0,
                weight=1.0,
                tags=["test"],
                evidence_factors=["day_master"],
                execution_time_ms=0.0,
            )
        
        engine.register(exec_test)
        results = engine.execute_all(sample_factor_matrix)
        
        assert len(results) == 1
        assert results[0].rule_id == "exec_test"
        assert results[0].matched is True
        assert results[0].execution_time_ms > 0  # 自动填充
    
    def test_execute_with_category_filter(self, sample_factor_matrix):
        """测试按分类过滤执行"""
        engine = RuleEngine()
        
        @register_rule(rule_id="cat_a", category="category_a", engine_id="bazi-calculator")
        def rule_cat_a(ctx):
            return RuntimeRuleResult(
                rule_id="cat_a", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="cat_b", category="category_b", engine_id="bazi-calculator")
        def rule_cat_b(ctx):
            return RuntimeRuleResult(
                rule_id="cat_b", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(rule_cat_a)
        engine.register(rule_cat_b)
        
        # 仅执行 category_a
        results = engine.execute_all(sample_factor_matrix, categories=["category_a"])
        assert len(results) == 1
        assert results[0].rule_id == "cat_a"
    
    def test_execute_matched(self, sample_factor_matrix):
        """测试仅返回匹配的结果"""
        engine = RuleEngine()
        
        @register_rule(rule_id="matched_rule", category="test", engine_id="bazi-calculator")
        def matched_rule(ctx):
            return RuntimeRuleResult(
                rule_id="matched_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="unmatched_rule", category="test", engine_id="bazi-calculator")
        def unmatched_rule(ctx):
            return RuntimeRuleResult(
                rule_id="unmatched_rule", matched=False, dimension="general",
                confidence=1.0, weight=0.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(matched_rule)
        engine.register(unmatched_rule)
        
        results = engine.execute_matched(sample_factor_matrix)
        assert len(results) == 1
        assert results[0].rule_id == "matched_rule"


class TestRuleEngineErrorIsolation:
    """
    错误隔离测试
    
    **Feature: layer3-rules, Property 9: Error Isolation**
    **Validates: Requirements 1.6**
    """
    
    def test_error_isolation_exception(self, sample_factor_matrix):
        """测试异常不影响其他规则执行"""
        engine = RuleEngine()
        
        @register_rule(rule_id="good_rule", category="test", engine_id="bazi-calculator")
        def good_rule(ctx):
            return RuntimeRuleResult(
                rule_id="good_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="bad_rule", category="test", engine_id="bazi-calculator")
        def bad_rule(ctx):
            raise RuntimeError("Intentional error")
        
        @register_rule(rule_id="another_good_rule", category="test", engine_id="bazi-calculator")
        def another_good_rule(ctx):
            return RuntimeRuleResult(
                rule_id="another_good_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(good_rule)
        engine.register(bad_rule)
        engine.register(another_good_rule)
        
        # 应该不抛出异常，且返回 2 个成功结果
        results = engine.execute_all(sample_factor_matrix)
        assert len(results) == 2
        rule_ids = {r.rule_id for r in results}
        assert "good_rule" in rule_ids
        assert "another_good_rule" in rule_ids
        assert "bad_rule" not in rule_ids
    
    def test_error_isolation_not_implemented(self, sample_factor_matrix):
        """测试 NotImplementedError 被正确处理"""
        engine = RuleEngine()
        
        @register_rule(rule_id="stub_rule", category="test", engine_id="bazi-calculator")
        def stub_rule(ctx):
            raise NotImplementedError("Complex rule not implemented")
        
        @register_rule(rule_id="normal_rule", category="test", engine_id="bazi-calculator")
        def normal_rule(ctx):
            return RuntimeRuleResult(
                rule_id="normal_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(stub_rule)
        engine.register(normal_rule)
        
        results = engine.execute_all(sample_factor_matrix)
        assert len(results) == 1
        assert results[0].rule_id == "normal_rule"


class TestRuleEnginePerformance:
    """性能测试"""
    
    def test_execution_time_tracking(self, sample_factor_matrix):
        """测试执行时间跟踪"""
        engine = RuleEngine()
        
        @register_rule(rule_id="timed_rule", category="test", engine_id="bazi-calculator")
        def timed_rule(ctx):
            return RuntimeRuleResult(
                rule_id="timed_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.0,  # 初始为 0
            )
        
        engine.register(timed_rule)
        results = engine.execute_all(sample_factor_matrix)
        
        assert len(results) == 1
        # execution_time_ms 应该被自动填充
        assert results[0].execution_time_ms > 0
    
    def test_profiling(self, sample_factor_matrix):
        """测试性能分析"""
        engine = RuleEngine()
        engine.enable_profiling(True)
        
        @register_rule(rule_id="profiled_rule", category="test", engine_id="bazi-calculator")
        def profiled_rule(ctx):
            return RuntimeRuleResult(
                rule_id="profiled_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(profiled_rule)
        
        # 执行多次
        for _ in range(5):
            engine.execute_all(sample_factor_matrix)
        
        stats = engine.get_profiling_stats()
        assert "profiled_rule" in stats
        assert stats["profiled_rule"]["count"] == 5
        assert stats["profiled_rule"]["avg_ms"] > 0


class TestRuleEngineMetadata:
    """元数据测试"""
    
    def test_get_metadata(self, sample_factor_matrix):
        """测试获取引擎元数据"""
        engine = RuleEngine()
        
        @register_rule(rule_id="meta_rule", category="meta_cat", exclusive_group="group1", engine_id="bazi-calculator")
        def meta_rule(ctx):
            return RuntimeRuleResult(
                rule_id="meta_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(meta_rule)
        
        metadata = engine.get_metadata()
        assert metadata["rule_count"] == 1
        assert "meta_cat" in metadata["categories"]
        assert "group1" in metadata["exclusive_groups"]


class TestRuleEnginePropertyBased:
    """属性测试 - Property 1: Rule Registration Completeness"""
    
    @given(
        rule_ids=st.lists(
            st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Ll', 'Nd'))),
            min_size=1,
            max_size=10,
            unique=True,
        )
    )
    @settings(max_examples=50)
    def test_registration_completeness(self, rule_ids):
        """
        **Feature: layer3-rules, Property 1: Rule Registration Completeness**
        
        测试所有注册的规则都可以被检索
        """
        clear_registry()
        engine = RuleEngine()
        
        registered_funcs = {}
        for rule_id in rule_ids:
            # 创建规则函数
            @register_rule(rule_id=rule_id, category="test", engine_id="bazi-calculator")
            def rule_func(ctx, rid=rule_id):
                return RuntimeRuleResult(
                    rule_id=rid, matched=True, dimension="general",
                    confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                    execution_time_ms=0.1,
                )
            
            engine.register(rule_func)
            registered_funcs[rule_id] = rule_func
        
        # 验证所有规则都可检索
        assert engine.get_rule_count() == len(rule_ids)
        for rule_id in rule_ids:
            assert engine.get_rule(rule_id) is not None


class TestRuleExecutionError:
    """RuleExecutionError 测试"""
    
    def test_error_attributes(self):
        """测试错误属性"""
        cause = ValueError("original error")
        error = RuleExecutionError(
            rule_id="test_rule",
            message="execution failed",
            cause=cause,
        )
        
        assert error.rule_id == "test_rule"
        assert error.message == "execution failed"
        assert error.cause is cause
        assert "test_rule" in str(error)
        assert "execution failed" in str(error)


class TestRuleEngineLayerIntegration:
    """
    Layer Integration 测试
    
    对照 Task 7: Layer Integration (Requirement 10.5)
    """
    
    @pytest.mark.asyncio
    async def test_execute_all_async(self, sample_factor_matrix):
        """测试异步执行"""
        engine = RuleEngine()
        
        @register_rule(rule_id="async_rule", category="test", engine_id="bazi-calculator")
        def async_rule(ctx):
            return RuntimeRuleResult(
                rule_id="async_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(async_rule)
        
        results = await engine.execute_all_async(sample_factor_matrix)
        assert len(results) == 1
        assert results[0].rule_id == "async_rule"
    
    def test_execute_batch(self, sample_factor_matrix):
        """测试批量执行"""
        engine = RuleEngine()
        
        @register_rule(rule_id="batch_rule", category="test", engine_id="bazi-calculator")
        def batch_rule(ctx):
            return RuntimeRuleResult(
                rule_id="batch_rule", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(batch_rule)
        
        # 创建第二个因子矩阵
        matrix2 = FactorMatrix(
            engine_id="astro-calculator",
            factors={
                "planet": FactorValue(
                    factor_id="planet",
                    value="Sun",
                    confidence=1.0,
                    source="astro-calculator",
                ),
            },
        )
        
        results = engine.execute_batch([sample_factor_matrix, matrix2])
        
        assert "bazi-calculator" in results
        assert "astro-calculator" in results
    
    def test_execute_with_partial_results(self, sample_factor_matrix):
        """测试部分结果返回"""
        engine = RuleEngine()
        
        @register_rule(rule_id="good_partial", category="test", engine_id="bazi-calculator")
        def good_partial(ctx):
            return RuntimeRuleResult(
                rule_id="good_partial", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="bad_partial", category="test", engine_id="bazi-calculator")
        def bad_partial(ctx):
            raise RuntimeError("Intentional error")
        
        engine.register(good_partial)
        engine.register(bad_partial)
        
        result = engine.execute_with_partial_results(sample_factor_matrix)
        
        # 应该有成功结果
        assert len(result["results"]) >= 1
        
        # 应该有执行时间
        assert result["execution_time_ms"] > 0
    
    def test_get_metadata(self, sample_factor_matrix):
        """测试获取元数据"""
        engine = RuleEngine()
        
        @register_rule(rule_id="meta_rule_1", category="cat1", exclusive_group="group1", engine_id="bazi-calculator")
        def meta_rule_1(ctx):
            return RuntimeRuleResult(
                rule_id="meta_rule_1", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        @register_rule(rule_id="meta_rule_2", category="cat2", engine_id="bazi-calculator")
        def meta_rule_2(ctx):
            return RuntimeRuleResult(
                rule_id="meta_rule_2", matched=True, dimension="general",
                confidence=1.0, weight=1.0, tags=[], evidence_factors=[],
                execution_time_ms=0.1,
            )
        
        engine.register(meta_rule_1)
        engine.register(meta_rule_2)
        
        metadata = engine.get_metadata()
        
        assert metadata["rule_count"] == 2
        assert "cat1" in metadata["categories"]
        assert "cat2" in metadata["categories"]
        assert "group1" in metadata["exclusive_groups"]
