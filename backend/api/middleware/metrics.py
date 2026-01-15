"""
Metrics Middleware

Record Gate-0 request metrics for observability-slos.
"""

from __future__ import annotations

import time
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from backend.core.observability.metrics import record_request_metrics


class MetricsMiddleware(BaseHTTPMiddleware):
    """HTTP request metrics collection (Prometheus)."""

    SKIP_PATHS = {"/metrics"}

    @staticmethod
    def _endpoint_label(request: Request) -> str:
        route = request.scope.get("route")
        route_path = getattr(route, "path", None)
        if isinstance(route_path, str) and route_path:
            return route_path
        return request.url.path

    @staticmethod
    def _result_label(status_code: int) -> str:
        if status_code < 400:
            return "success"
        if status_code < 500:
            return "client_error"
        return "server_error"

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if request.url.path in self.SKIP_PATHS:
            return await call_next(request)

        start_time = time.perf_counter()
        method = request.method

        try:
            response = await call_next(request)
        except Exception as e:
            duration_ms = (time.perf_counter() - start_time) * 1000
            record_request_metrics(
                endpoint=self._endpoint_label(request),
                method=method,
                result="exception",
                duration_ms=duration_ms,
                error_type=type(e).__name__,
            )
            raise

        duration_ms = (time.perf_counter() - start_time) * 1000
        status_code = getattr(response, "status_code", 0) or 0
        result = self._result_label(status_code)
        error_type = f"http_{status_code}" if status_code >= 500 else None

        record_request_metrics(
            endpoint=self._endpoint_label(request),
            method=method,
            result=result,
            duration_ms=duration_ms,
            error_type=error_type,
        )

        return response

