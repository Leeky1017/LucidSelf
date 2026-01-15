"""
Request Logging Middleware

请求日志中间件。

对照 tasks.md 13.8:
- Requirements: 6.3.2, 8.2.1
"""

import logging
import time
import uuid
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from backend.core.observability.context import bind_context, reset_context
from backend.core.observability.logging import log_event
from backend.core.observability.tracing import bind_trace_id, reset_trace_id
from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    请求日志中间件
    
    记录:
    - 请求信息 (method, path, headers)
    - 响应信息 (status, latency)
    - 结构化 JSON 日志
    """
    
    # 不记录日志的路径（仍会回写 correlation headers）
    SKIP_LOG_PATHS = {"/health", "/ready", "/live"}

    # 仅允许记录的 headers（避免 PII/secret 泄露与高噪声）
    ALLOWED_HEADERS = {"user-agent", "content-type", "accept", "accept-language"}

    @staticmethod
    def _mask_ip(ip: str | None) -> str | None:
        if not ip:
            return None
        # IPv4: mask last octet; IPv6: keep prefix only (best-effort).
        if "." in ip:
            parts = ip.split(".")
            if len(parts) == 4:
                return ".".join(parts[:3] + ["0"])
            return ip
        if ":" in ip:
            parts = ip.split(":")
            return ":".join(parts[:4]) + "::"
        return ip
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # 生成/传播关联标识符
        request_id = request.headers.get("X-Request-ID") or f"req_{uuid.uuid4().hex[:12]}"
        trace_id = request.headers.get("X-Trace-ID") or uuid.uuid4().hex
        version_id = resolve_version_id()
        corpus_release_id = resolve_corpus_release_id()

        request.state.request_id = request_id
        request.state.trace_id = trace_id
        request.state.version_id = version_id
        request.state.corpus_release_id = corpus_release_id
        
        # 记录请求开始
        start_time = time.perf_counter()

        trace_token = bind_trace_id(trace_id)
        ctx_tokens = bind_context(
            request_id=request_id,
            version_id=version_id,
            corpus_release_id=corpus_release_id,
        )

        try:
            # 跳过健康检查日志
            if request.url.path not in self.SKIP_LOG_PATHS:
                safe_headers = {
                    k.lower(): v
                    for k, v in request.headers.items()
                    if k.lower() in self.ALLOWED_HEADERS
                }
                query_keys = list(request.query_params.keys()) if request.query_params else []
                log_event(
                    logger,
                    logging.INFO,
                    "request_start",
                    method=request.method,
                    path=request.url.path,
                    query_keys=query_keys or None,
                    client_ip=self._mask_ip(request.client.host if request.client else None),
                    headers=safe_headers or None,
                )
        
        # 执行请求
            response = await call_next(request)
            
            # 记录请求完成
            latency_ms = (time.perf_counter() - start_time) * 1000

            completion_tokens = bind_context(
                user_id=getattr(request.state, "user_id", None),
                org_id=getattr(request.state, "org_id", None),
                engine_id=getattr(request.state, "engine_id", None),
                version_id=getattr(request.state, "version_id", None),
            )
            ctx_tokens.update(completion_tokens)

            if request.url.path not in self.SKIP_LOG_PATHS:
                log_event(
                    logger,
                    logging.WARNING if response.status_code >= 400 else logging.INFO,
                    "request_complete",
                    method=request.method,
                    path=request.url.path,
                    status_code=response.status_code,
                    latency_ms=round(latency_ms, 2),
                )
            
            # 添加关联标识符到响应头
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Trace-ID"] = trace_id
            response.headers["X-Response-Time"] = f"{latency_ms:.2f}ms"
            
            return response
        
        except Exception as e:
            latency_ms = (time.perf_counter() - start_time) * 1000

            error_tokens = bind_context(
                user_id=getattr(request.state, "user_id", None),
                org_id=getattr(request.state, "org_id", None),
                engine_id=getattr(request.state, "engine_id", None),
                version_id=getattr(request.state, "version_id", None),
            )
            ctx_tokens.update(error_tokens)

            if request.url.path not in self.SKIP_LOG_PATHS:
                log_event(
                    logger,
                    logging.ERROR,
                    "request_error",
                    method=request.method,
                    path=request.url.path,
                    error_type=type(e).__name__,
                    error=str(e),
                    latency_ms=round(latency_ms, 2),
                )
            raise
        finally:
            reset_context(ctx_tokens)
            reset_trace_id(trace_token)
