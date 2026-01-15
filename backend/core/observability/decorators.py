"""
Observability Decorators

可观测性装饰器，用于自动添加指标和追踪。

对照 design.md §5 可观测性设计
"""

from __future__ import annotations

import functools
import time
from typing import Any, Callable, Optional, TypeVar

from backend.core.observability.metrics import (
    RULE_EXECUTION_DURATION,
    CACHE_HIT_COUNTER,
    CACHE_MISS_COUNTER,
)
from backend.core.observability.tracing import tracer, get_trace_id

F = TypeVar("F", bound=Callable[..., Any])


def observed(
    operation_name: Optional[str] = None,
    record_duration: bool = True,
    record_trace: bool = True,
):
    """
    综合可观测性装饰器
    
    同时添加指标和追踪。
    
    Args:
        operation_name: 操作名称 (默认使用函数名)
        record_duration: 是否记录执行时长
        record_trace: 是否添加追踪
    """
    def decorator(func: F) -> F:
        name = operation_name or func.__name__
        
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            
            if record_trace:
                with tracer.start_as_current_span(name) as span:
                    try:
                        result = await func(*args, **kwargs)
                        return result
                    finally:
                        if record_duration:
                            duration = time.perf_counter() - start_time
                            span.set_attribute("duration_seconds", duration)
            else:
                return await func(*args, **kwargs)
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            
            if record_trace:
                with tracer.start_as_current_span(name) as span:
                    try:
                        result = func(*args, **kwargs)
                        return result
                    finally:
                        if record_duration:
                            duration = time.perf_counter() - start_time
                            span.set_attribute("duration_seconds", duration)
            else:
                return func(*args, **kwargs)
        
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def timed(
    metric: Any = None,
    labels: Optional[dict] = None,
):
    """
    计时装饰器
    
    记录函数执行时长到 Prometheus Histogram。
    
    Args:
        metric: Prometheus Histogram 指标
        labels: 标签字典
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                duration = time.perf_counter() - start_time
                if metric:
                    if labels:
                        metric.labels(**labels).observe(duration)
                    else:
                        metric.observe(duration)
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                duration = time.perf_counter() - start_time
                if metric:
                    if labels:
                        metric.labels(**labels).observe(duration)
                    else:
                        metric.observe(duration)
        
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def counted(
    metric: Any = None,
    labels: Optional[dict] = None,
    count_exceptions: bool = True,
):
    """
    计数装饰器
    
    记录函数调用次数到 Prometheus Counter。
    
    Args:
        metric: Prometheus Counter 指标
        labels: 标签字典
        count_exceptions: 是否计数异常调用
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                if metric:
                    if labels:
                        metric.labels(**labels).inc()
                    else:
                        metric.inc()
                return result
            except Exception:
                if count_exceptions and metric:
                    if labels:
                        metric.labels(**{**labels, "status": "error"}).inc()
                raise
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if metric:
                    if labels:
                        metric.labels(**labels).inc()
                    else:
                        metric.inc()
                return result
            except Exception:
                if count_exceptions and metric:
                    if labels:
                        metric.labels(**{**labels, "status": "error"}).inc()
                raise
        
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def cache_observed(cache_type: str):
    """
    缓存可观测性装饰器
    
    自动记录缓存命中/未命中。
    
    Args:
        cache_type: 缓存类型 (semantic, rule, narrative)
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if result is not None:
                CACHE_HIT_COUNTER.labels(cache_type=cache_type).inc()
            else:
                CACHE_MISS_COUNTER.labels(cache_type=cache_type).inc()
            
            return result
        
        return wrapper
    
    return decorator
