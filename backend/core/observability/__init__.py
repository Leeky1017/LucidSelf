"""
LucidSelf Observability

可观测性模块，包含：
- Prometheus 指标收集
- OpenTelemetry 分布式追踪
- 结构化日志

对照 .kiro/specs/testing-ops/design.md §5 可观测性设计
对照 Requirements R-6-5-01 ~ R-6-5-10
"""

# 延迟导入避免循环依赖
def __getattr__(name: str):
    """延迟导入"""
    if name in (
        "RULE_HIT_COUNTER",
        "RULE_EXECUTION_DURATION",
        "CACHE_HIT_COUNTER",
        "CACHE_MISS_COUNTER",
        "LLM_REQUEST_DURATION",
        "LLM_TOKEN_COUNTER",
        "FUSION_SCORE_HISTOGRAM",
    ):
        from backend.core.observability.metrics import (
            RULE_HIT_COUNTER,
            RULE_EXECUTION_DURATION,
            CACHE_HIT_COUNTER,
            CACHE_MISS_COUNTER,
            LLM_REQUEST_DURATION,
            LLM_TOKEN_COUNTER,
            FUSION_SCORE_HISTOGRAM,
        )
        return locals()[name]
    
    if name in ("tracer", "trace_rule_execution", "trace_llm_call", "get_trace_id"):
        from backend.core.observability.tracing import (
            tracer,
            trace_rule_execution,
            trace_llm_call,
            get_trace_id,
        )
        return locals()[name]
    
    if name in ("configure_logging", "get_logger", "add_trace_context"):
        from backend.core.observability.logging import (
            configure_logging,
            get_logger,
            add_trace_context,
        )
        return locals()[name]
    
    if name in ("observed", "timed", "counted"):
        from backend.core.observability.decorators import (
            observed,
            timed,
            counted,
        )
        return locals()[name]
    
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    # Metrics
    "RULE_HIT_COUNTER",
    "RULE_EXECUTION_DURATION",
    "CACHE_HIT_COUNTER",
    "CACHE_MISS_COUNTER",
    "LLM_REQUEST_DURATION",
    "LLM_TOKEN_COUNTER",
    "FUSION_SCORE_HISTOGRAM",
    # Tracing
    "tracer",
    "trace_rule_execution",
    "trace_llm_call",
    "get_trace_id",
    # Logging
    "configure_logging",
    "get_logger",
    "add_trace_context",
    # Decorators
    "observed",
    "timed",
    "counted",
]
