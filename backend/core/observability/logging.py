"""
Structured Logging

结构化日志配置。

对照 design.md §5.3 结构化日志
对照 Requirements R-6-5-07 ~ R-6-5-09
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
from typing import Any, Dict, Optional

# 尝试导入 structlog
try:
    import structlog
    STRUCTLOG_AVAILABLE = True
except ImportError:
    STRUCTLOG_AVAILABLE = False

from backend.core.observability.tracing import get_trace_id
from backend.core.observability.context import get_context as get_observability_context
from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id

# =============================================================================
# Redaction (PII/Secrets)
# =============================================================================

REDACTED_VALUE = "***REDACTED***"

_EMAIL_PATTERN = re.compile(r"(?i)(?P<email>[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})")

# Keys are matched case-insensitively after normalization.
_SENSITIVE_KEYS = {
    "authorization",
    "cookie",
    "set-cookie",
    "x-api-key",
    "api_key",
    "apikey",
    "access_token",
    "refresh_token",
    "token",
    "password",
    "passwd",
    "pwd",
    "secret",
    "jwt",
    # PII
    "email",
    "phone",
    "address",
    "ssn",
    "birth_date",
    "birthday",
    "身份证",
}

# 敏感数据模式
SENSITIVE_PATTERNS = [
    # 匹配 key=value 或 key: value 格式
    (re.compile(r"(password|passwd|pwd|secret|token|api_key|apikey)\s*[:=]\s*['\"]?([^'\"\s,}]+)", re.I), r"\1=***MASKED***"),
    # 匹配敏感字段名（仅标记）
    (re.compile(r"(birth_date|birthday|phone|email|address|ssn|身份证)[:=]\s*['\"]?([^'\"\s,}]+)", re.I), r"\1=***MASKED***"),
    # 匹配 JSON 风格 "key": "value"
    (re.compile(r"(\"?(password|passwd|pwd|secret|token|api_key|apikey)\"?\s*:\s*)\"([^\"]+)\"", re.I), r"\1\"***MASKED***\""),
    (re.compile(r"(\"?(birth_date|birthday|phone|email|address|ssn)\"?\s*:\s*)\"([^\"]+)\"", re.I), r"\1\"***MASKED***\""),
]


def mask_sensitive_data(text: str) -> str:
    """
    脱敏敏感数据
    
    对照 R-6-5-09
    """
    if not isinstance(text, str):
        return text
    
    result = text
    for pattern, replacement in SENSITIVE_PATTERNS:
        result = pattern.sub(replacement, result)

    # Email-like content (best-effort)
    result = _EMAIL_PATTERN.sub("***MASKED_EMAIL***", result)
    
    return result


def _normalize_key(key: str) -> str:
    return key.strip().lower().replace("-", "_")


def redact_log_data(value: Any) -> Any:
    """
    Redact secrets/PII from structured log payloads.

    This is intentionally conservative: sensitive keys are always replaced
    with a constant marker, and obvious email-like strings are masked.
    """
    if isinstance(value, dict):
        redacted: Dict[str, Any] = {}
        for k, v in value.items():
            k_norm = _normalize_key(str(k))
            if k_norm in _SENSITIVE_KEYS:
                redacted[k] = REDACTED_VALUE
                continue
            redacted[k] = redact_log_data(v)
        return redacted

    if isinstance(value, list):
        return [redact_log_data(v) for v in value]

    if isinstance(value, tuple):
        return [redact_log_data(v) for v in value]

    if isinstance(value, str):
        # Keyed redaction is preferred; fallback to best-effort masking.
        return mask_sensitive_data(value)

    return value


def log_event(
    logger: logging.Logger,
    level: int,
    event: str,
    **fields: Any,
) -> Dict[str, Any]:
    """
    Emit a structured JSON log line with unified correlation fields.

    Always includes (possibly null):
    - request_id/trace_id/user_id/org_id/engine_id/version_id
    """
    payload: Dict[str, Any] = {
        "event": event,
        **get_observability_context(),
        "trace_id": get_trace_id(),
        **fields,
    }

    # Default version_id when not explicitly set.
    if payload.get("version_id") is None:
        payload["version_id"] = resolve_version_id()

    # Default corpus_release_id when not explicitly set.
    if payload.get("corpus_release_id") is None:
        payload["corpus_release_id"] = resolve_corpus_release_id()

    payload = redact_log_data(payload)
    logger.log(level, json.dumps(payload, ensure_ascii=False))
    return payload


def add_trace_context(
    logger: Any,
    method_name: str,
    event_dict: Dict[str, Any],
) -> Dict[str, Any]:
    """
    添加 trace_id 到日志
    
    对照 R-6-5-07
    """
    trace_id = get_trace_id()
    if trace_id:
        event_dict["trace_id"] = trace_id
    
    return event_dict


def mask_processor(
    logger: Any,
    method_name: str,
    event_dict: Dict[str, Any],
) -> Dict[str, Any]:
    """
    敏感数据脱敏处理器
    """
    # 脱敏 event 字段
    if "event" in event_dict and isinstance(event_dict["event"], str):
        event_dict["event"] = mask_sensitive_data(event_dict["event"])
    
    # 脱敏其他字符串字段
    for key, value in list(event_dict.items()):
        if isinstance(value, str):
            event_dict[key] = mask_sensitive_data(value)
    
    return event_dict


def configure_logging(
    level: str = "INFO",
    json_format: bool = True,
    add_trace_id: bool = True,
    mask_sensitive: bool = True,
) -> None:
    """
    配置结构化日志
    
    对照 R-6-5-07 ~ R-6-5-09
    
    Args:
        level: 日志级别
        json_format: 是否输出 JSON 格式
        add_trace_id: 是否添加 trace_id
        mask_sensitive: 是否脱敏敏感数据
    """
    if not STRUCTLOG_AVAILABLE:
        # Fallback 到标准 logging
        logging.basicConfig(
            level=getattr(logging, level.upper()),
            format="%(asctime)s %(levelname)s %(name)s - %(message)s",
            handlers=[logging.StreamHandler(sys.stdout)],
        )
        return
    
    # 构建处理器链
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
    ]
    
    if add_trace_id:
        processors.append(add_trace_context)
    
    if mask_sensitive:
        processors.append(mask_processor)
    
    # 输出格式
    if json_format:
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer())
    
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, level.upper())
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str) -> Any:
    """
    获取 logger
    
    Args:
        name: logger 名称
        
    Returns:
        structlog logger 或标准 logger
    """
    if STRUCTLOG_AVAILABLE:
        return structlog.get_logger(name)
    else:
        return logging.getLogger(name)


class LogContext:
    """
    日志上下文管理器
    
    用于在日志中添加额外上下文信息。
    """
    
    def __init__(self, **kwargs):
        self.context = kwargs
        self._token = None
    
    def __enter__(self):
        if STRUCTLOG_AVAILABLE:
            import structlog
            self._token = structlog.contextvars.bind_contextvars(**self.context)
        return self
    
    def __exit__(self, *args):
        if STRUCTLOG_AVAILABLE and self._token:
            import structlog
            structlog.contextvars.unbind_contextvars(*self.context.keys())
