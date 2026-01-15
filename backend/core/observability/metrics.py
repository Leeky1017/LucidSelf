"""
Prometheus Metrics

Prometheus 指标定义。

对照 design.md §5.1 指标定义
对照 Requirements R-6-5-01 ~ R-6-5-04
"""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# 尝试导入 prometheus_client，如果未安装则提供 stub
try:
    from prometheus_client import Counter, Histogram, Gauge, Info
    PROMETHEUS_AVAILABLE = True
except ImportError:
    PROMETHEUS_AVAILABLE = False
    logger.info("prometheus_client not installed, using stub metrics")
    
    # Stub 实现
    class StubMetric:
        def __init__(self, *args, **kwargs):
            self._name = args[0] if args else "unknown"
        
        def labels(self, **kwargs):
            return self
        
        def inc(self, amount=1):
            pass
        
        def dec(self, amount=1):
            pass
        
        def set(self, value):
            pass
        
        def observe(self, value):
            pass
    
    Counter = Histogram = Gauge = Info = StubMetric


# =============================================================================
# 规则指标
# =============================================================================

RULE_HIT_COUNTER = Counter(
    "ls_rule_hit_total",
    "Total rule hits",
    ["rule_id", "dimension", "engine_id"]
)

RULE_EXECUTION_DURATION = Histogram(
    "ls_rule_execution_seconds",
    "Rule execution duration in seconds",
    ["engine_id"],
    buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0)
)

RULE_MATCH_COUNTER = Counter(
    "ls_rule_match_total",
    "Total rule matches by type",
    ["engine_id", "match_type"]  # hit, miss, error
)


# =============================================================================
# 缓存指标
# =============================================================================

CACHE_HIT_COUNTER = Counter(
    "ls_cache_hit_total",
    "Cache hit count",
    ["cache_type"]  # semantic, rule, narrative
)

CACHE_MISS_COUNTER = Counter(
    "ls_cache_miss_total",
    "Cache miss count",
    ["cache_type"]
)

CACHE_SIZE_GAUGE = Gauge(
    "ls_cache_size",
    "Current cache size",
    ["cache_type"]
)

CACHE_HIT_RATIO = Gauge(
    "ls_cache_hit_ratio",
    "Cache hit ratio (0-1)",
    ["cache_type"]
)


# =============================================================================
# LLM 指标
# =============================================================================

LLM_REQUEST_DURATION = Histogram(
    "ls_llm_request_seconds",
    "LLM request duration in seconds",
    ["model", "endpoint"],
    buckets=(0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0)
)

LLM_TOKEN_COUNTER = Counter(
    "ls_llm_tokens_total",
    "Total LLM tokens used",
    ["model", "token_type"]  # input, output
)

LLM_REQUEST_COUNTER = Counter(
    "ls_llm_requests_total",
    "Total LLM requests",
    ["model", "status"]  # success, error
)

LLM_COST_COUNTER = Counter(
    "ls_llm_cost_usd_total",
    "Total LLM cost in USD",
    ["model"]
)


# =============================================================================
# 融合指标
# =============================================================================

FUSION_SCORE_HISTOGRAM = Histogram(
    "ls_fusion_score",
    "Fusion cross-validation score distribution",
    ["scenario"],
    buckets=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
)

FUSION_THEME_COUNTER = Counter(
    "ls_fusion_theme_total",
    "Fusion theme occurrences",
    ["theme"]
)

# =============================================================================
# HTTP / Gate-0 核心指标（observability-slos）
# =============================================================================

REQUESTS_TOTAL = Counter(
    "ls_requests_total",
    "Total HTTP requests",
    ["result", "endpoint", "method"],
)

REQUEST_DURATION_MS = Histogram(
    "ls_request_duration_ms",
    "HTTP request duration in milliseconds",
    ["result", "endpoint", "method"],
    buckets=(5, 10, 25, 50, 100, 200, 500, 1000, 2500, 5000, 10000),
)

ERRORS_TOTAL = Counter(
    "ls_errors_total",
    "Total server errors",
    ["error_type", "endpoint"],
)

BLOCKS_TOTAL = Counter(
    "ls_blocks_total",
    "Total blocking events (gates/dependencies)",
    ["block_type", "capability"],
)

AUDIT_RECORDS_TOTAL = Counter(
    "ls_audit_records_total",
    "Total audit records written",
    ["result", "capability"],
)

SLO_BREACHES_TOTAL = Counter(
    "ls_slo_breaches_total",
    "Total SLO breaches",
    ["slo_id", "severity"],
)


# =============================================================================
# 辅助函数
# =============================================================================

def record_rule_hit(
    rule_id: str,
    dimension: str,
    engine_id: str,
) -> None:
    """记录规则命中"""
    RULE_HIT_COUNTER.labels(
        rule_id=rule_id,
        dimension=dimension,
        engine_id=engine_id,
    ).inc()


def record_cache_access(
    cache_type: str,
    hit: bool,
) -> None:
    """记录缓存访问"""
    if hit:
        CACHE_HIT_COUNTER.labels(cache_type=cache_type).inc()
    else:
        CACHE_MISS_COUNTER.labels(cache_type=cache_type).inc()


def record_llm_request(
    model: str,
    duration_seconds: float,
    input_tokens: int,
    output_tokens: int,
    success: bool = True,
    cost_usd: float = 0.0,
) -> None:
    """记录 LLM 请求"""
    status = "success" if success else "error"
    
    LLM_REQUEST_DURATION.labels(model=model, endpoint="chat").observe(duration_seconds)
    LLM_TOKEN_COUNTER.labels(model=model, token_type="input").inc(input_tokens)
    LLM_TOKEN_COUNTER.labels(model=model, token_type="output").inc(output_tokens)
    LLM_REQUEST_COUNTER.labels(model=model, status=status).inc()
    
    if cost_usd > 0:
        LLM_COST_COUNTER.labels(model=model).inc(cost_usd)


def record_fusion_score(
    score: float,
    scenario: str = "default",
) -> None:
    """记录融合分数"""
    FUSION_SCORE_HISTOGRAM.labels(scenario=scenario).observe(score)


def record_request_metrics(
    *,
    endpoint: str,
    method: str,
    result: str,
    duration_ms: float,
    error_type: Optional[str] = None,
) -> None:
    """
    记录 HTTP 请求核心指标（Gate-0 最小集合）
    """
    REQUESTS_TOTAL.labels(result=result, endpoint=endpoint, method=method).inc()
    REQUEST_DURATION_MS.labels(result=result, endpoint=endpoint, method=method).observe(duration_ms)
    if error_type:
        ERRORS_TOTAL.labels(error_type=error_type, endpoint=endpoint).inc()


def record_block(
    *,
    block_type: str,
    capability: str,
) -> None:
    """记录阻断事件（门禁/依赖不可用等）"""
    BLOCKS_TOTAL.labels(block_type=block_type, capability=capability).inc()
