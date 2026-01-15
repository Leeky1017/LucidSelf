"""
Distributed Tracing

OpenTelemetry 分布式追踪集成。

对照 design.md §5.2 追踪集成
对照 Requirements R-6-5-05 ~ R-6-5-06
"""

from __future__ import annotations

import functools
import logging
from contextvars import ContextVar, Token
from typing import Any, Callable, Optional, TypeVar

logger = logging.getLogger(__name__)

# 尝试导入 OpenTelemetry
try:
    from opentelemetry import trace
    from opentelemetry.trace import Tracer, Span, StatusCode
    OTEL_AVAILABLE = True
except ImportError:
    OTEL_AVAILABLE = False
    logger.info("opentelemetry not installed, using stub tracing")
    
    # Stub 实现
    class StubSpan:
        def __enter__(self):
            return self
        
        def __exit__(self, *args):
            pass
        
        def set_attribute(self, key, value):
            pass
        
        def record_exception(self, exc):
            pass
        
        def set_status(self, status):
            pass
        
        def get_span_context(self):
            return StubSpanContext()
    
    class StubSpanContext:
        trace_id = 0
        span_id = 0
    
    class StubTracer:
        def start_as_current_span(self, name, **kwargs):
            return StubSpan()
        
        def start_span(self, name, **kwargs):
            return StubSpan()
    
    class trace:
        @staticmethod
        def get_tracer(name):
            return StubTracer()
        
        @staticmethod
        def get_current_span():
            return StubSpan()
    
    StatusCode = type("StatusCode", (), {"OK": 0, "ERROR": 1})


# 全局 tracer
tracer = trace.get_tracer("lucidself")

# 当前 trace_id (用于无 OTEL 时的手动追踪)
_current_trace_id: ContextVar[Optional[str]] = ContextVar("trace_id", default=None)


def get_trace_id() -> Optional[str]:
    """
    获取当前 trace_id
    
    Returns:
        trace_id 字符串，如无则返回 None
    """
    if OTEL_AVAILABLE:
        span = trace.get_current_span()
        if span:
            ctx = span.get_span_context()
            if ctx.trace_id:
                return format(ctx.trace_id, "032x")
    
    return _current_trace_id.get()


def set_trace_id(trace_id: str) -> None:
    """设置当前 trace_id (用于无 OTEL 时)"""
    _current_trace_id.set(trace_id)


def bind_trace_id(trace_id: str) -> Token:
    """绑定 trace_id 并返回可用于 reset 的 token"""
    return _current_trace_id.set(trace_id)


def reset_trace_id(token: Token) -> None:
    """重置 trace_id 到 bind 之前的状态"""
    _current_trace_id.reset(token)


F = TypeVar("F", bound=Callable[..., Any])


def trace_rule_execution(func: F) -> F:
    """
    规则执行追踪装饰器
    
    对照 design.md §5.2
    """
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        rule_id = kwargs.get("rule_id", "unknown")
        
        with tracer.start_as_current_span(
            f"rule.execute.{func.__name__}",
            attributes={"rule_id": rule_id}
        ) as span:
            try:
                result = await func(*args, **kwargs)
                if hasattr(result, "hit"):
                    span.set_attribute("result.hit", result.hit)
                return result
            except Exception as e:
                span.record_exception(e)
                if OTEL_AVAILABLE:
                    span.set_status(StatusCode.ERROR)
                raise
    
    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        rule_id = kwargs.get("rule_id", "unknown")
        
        with tracer.start_as_current_span(
            f"rule.execute.{func.__name__}",
            attributes={"rule_id": rule_id}
        ) as span:
            try:
                result = func(*args, **kwargs)
                if hasattr(result, "hit"):
                    span.set_attribute("result.hit", result.hit)
                return result
            except Exception as e:
                span.record_exception(e)
                if OTEL_AVAILABLE:
                    span.set_status(StatusCode.ERROR)
                raise
    
    import asyncio
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper


def trace_llm_call(func: F) -> F:
    """
    LLM 调用追踪装饰器
    """
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        model = kwargs.get("model", "unknown")
        
        with tracer.start_as_current_span(
            f"llm.call.{func.__name__}",
            attributes={"llm.model": model}
        ) as span:
            try:
                result = await func(*args, **kwargs)
                if hasattr(result, "usage"):
                    span.set_attribute("llm.tokens.input", result.usage.prompt_tokens)
                    span.set_attribute("llm.tokens.output", result.usage.completion_tokens)
                return result
            except Exception as e:
                span.record_exception(e)
                if OTEL_AVAILABLE:
                    span.set_status(StatusCode.ERROR)
                raise
    
    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        model = kwargs.get("model", "unknown")
        
        with tracer.start_as_current_span(
            f"llm.call.{func.__name__}",
            attributes={"llm.model": model}
        ) as span:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                span.record_exception(e)
                if OTEL_AVAILABLE:
                    span.set_status(StatusCode.ERROR)
                raise
    
    import asyncio
    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper


def trace_operation(operation_name: str):
    """
    通用操作追踪装饰器
    
    Args:
        operation_name: 操作名称
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            with tracer.start_as_current_span(operation_name) as span:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    span.record_exception(e)
                    if OTEL_AVAILABLE:
                        span.set_status(StatusCode.ERROR)
                    raise
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            with tracer.start_as_current_span(operation_name) as span:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    span.record_exception(e)
                    if OTEL_AVAILABLE:
                        span.set_status(StatusCode.ERROR)
                    raise
        
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator
