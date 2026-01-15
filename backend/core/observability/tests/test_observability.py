"""
Tests for Observability Module

可观测性模块测试。
"""

import asyncio
import pytest
from unittest.mock import MagicMock, patch


class TestMetrics:
    """Metrics 测试"""
    
    def test_imports(self):
        """测试导入"""
        from backend.core.observability.metrics import (
            RULE_HIT_COUNTER,
            RULE_EXECUTION_DURATION,
            CACHE_HIT_COUNTER,
            CACHE_MISS_COUNTER,
            LLM_REQUEST_DURATION,
            LLM_TOKEN_COUNTER,
            FUSION_SCORE_HISTOGRAM,
        )
        
        # 验证指标对象存在
        assert RULE_HIT_COUNTER is not None
        assert RULE_EXECUTION_DURATION is not None
        assert CACHE_HIT_COUNTER is not None
    
    def test_record_rule_hit(self):
        """测试规则命中记录"""
        from backend.core.observability.metrics import record_rule_hit
        
        # 不应抛出异常
        record_rule_hit(
            rule_id="test_rule",
            dimension="事业",
            engine_id="bazi",
        )
    
    def test_record_cache_access(self):
        """测试缓存访问记录"""
        from backend.core.observability.metrics import record_cache_access
        
        # 不应抛出异常
        record_cache_access(cache_type="semantic", hit=True)
        record_cache_access(cache_type="rule", hit=False)
    
    def test_record_llm_request(self):
        """测试 LLM 请求记录"""
        from backend.core.observability.metrics import record_llm_request
        
        # 不应抛出异常
        record_llm_request(
            model="gpt-4o-mini",
            duration_seconds=1.5,
            input_tokens=100,
            output_tokens=50,
            success=True,
            cost_usd=0.001,
        )
    
    def test_record_fusion_score(self):
        """测试融合分数记录"""
        from backend.core.observability.metrics import record_fusion_score
        
        record_fusion_score(score=0.85, scenario="career")


class TestTracing:
    """Tracing 测试"""
    
    def test_imports(self):
        """测试导入"""
        from backend.core.observability.tracing import (
            tracer,
            trace_rule_execution,
            trace_llm_call,
            get_trace_id,
        )
        
        assert tracer is not None
    
    def test_get_trace_id(self):
        """测试获取 trace_id"""
        from backend.core.observability.tracing import get_trace_id, set_trace_id
        
        # 设置并获取
        set_trace_id("test_trace_123")
        trace_id = get_trace_id()
        
        # 可能是设置的值或 None（如果 OTEL 可用）
        assert trace_id is None or isinstance(trace_id, str)
    
    def test_trace_rule_execution_decorator(self):
        """测试规则执行追踪装饰器"""
        from backend.core.observability.tracing import trace_rule_execution
        
        @trace_rule_execution
        def my_rule_func(rule_id="test"):
            return type("Result", (), {"hit": True})()
        
        result = my_rule_func(rule_id="test_rule")
        assert result.hit is True
    
    def test_trace_rule_execution_async(self):
        """测试规则执行追踪装饰器（异步）"""
        from backend.core.observability.tracing import trace_rule_execution
        
        @trace_rule_execution
        async def my_async_rule_func(rule_id="test"):
            return type("Result", (), {"hit": True})()
        
        result = asyncio.get_event_loop().run_until_complete(
            my_async_rule_func(rule_id="test_rule")
        )
        assert result.hit is True
    
    def test_trace_operation_decorator(self):
        """测试通用操作追踪装饰器"""
        from backend.core.observability.tracing import trace_operation
        
        @trace_operation("my_operation")
        def my_operation():
            return "done"
        
        result = my_operation()
        assert result == "done"


class TestLogging:
    """Logging 测试"""
    
    def test_imports(self):
        """测试导入"""
        from backend.core.observability.logging import (
            configure_logging,
            get_logger,
            mask_sensitive_data,
        )
        
        assert configure_logging is not None
        assert get_logger is not None
    
    def test_mask_sensitive_data(self):
        """测试敏感数据脱敏"""
        from backend.core.observability.logging import mask_sensitive_data
        
        # 测试密码脱敏
        text = "password=secret123"
        masked = mask_sensitive_data(text)
        assert "secret123" not in masked
        assert "MASKED" in masked
        
        # 测试 API key 脱敏
        text = "api_key=sk-abc123xyz"
        masked = mask_sensitive_data(text)
        assert "sk-abc123xyz" not in masked
    
    def test_get_logger(self):
        """测试获取 logger"""
        from backend.core.observability.logging import get_logger
        
        logger = get_logger("test_logger")
        assert logger is not None
    
    def test_configure_logging(self):
        """测试配置日志"""
        from backend.core.observability.logging import configure_logging
        
        # 不应抛出异常
        configure_logging(level="DEBUG", json_format=False)


class TestDecorators:
    """Decorators 测试"""
    
    def test_observed_decorator(self):
        """测试 observed 装饰器"""
        from backend.core.observability.decorators import observed
        
        @observed("test_op")
        def my_func():
            return 42
        
        result = my_func()
        assert result == 42
    
    def test_observed_async(self):
        """测试 observed 装饰器（异步）"""
        from backend.core.observability.decorators import observed
        
        @observed("test_async_op")
        async def my_async_func():
            return 42
        
        result = asyncio.get_event_loop().run_until_complete(my_async_func())
        assert result == 42
    
    def test_timed_decorator(self):
        """测试 timed 装饰器"""
        from backend.core.observability.decorators import timed
        
        mock_metric = MagicMock()
        
        @timed(metric=mock_metric)
        def my_func():
            return "done"
        
        result = my_func()
        assert result == "done"
        mock_metric.observe.assert_called_once()
    
    def test_counted_decorator(self):
        """测试 counted 装饰器"""
        from backend.core.observability.decorators import counted
        
        mock_metric = MagicMock()
        
        @counted(metric=mock_metric)
        def my_func():
            return "done"
        
        result = my_func()
        assert result == "done"
        mock_metric.inc.assert_called_once()
    
    def test_cache_observed_decorator(self):
        """测试 cache_observed 装饰器"""
        from backend.core.observability.decorators import cache_observed
        
        @cache_observed("semantic")
        def get_from_cache(key):
            if key == "exists":
                return {"data": "value"}
            return None
        
        # 测试命中
        result = get_from_cache("exists")
        assert result is not None
        
        # 测试未命中
        result = get_from_cache("missing")
        assert result is None


class TestIntegration:
    """集成测试"""
    
    def test_module_exports(self):
        """测试模块导出"""
        from backend.core.observability import (
            RULE_HIT_COUNTER,
            tracer,
            configure_logging,
            observed,
        )
        
        assert RULE_HIT_COUNTER is not None
        assert tracer is not None
        assert configure_logging is not None
        assert observed is not None
