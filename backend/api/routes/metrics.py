"""
Metrics Route

Expose Prometheus metrics for Gate-0 observability.
"""

from __future__ import annotations

from fastapi import APIRouter
from starlette.responses import JSONResponse, Response

router = APIRouter(tags=["Metrics"])


@router.get("/metrics")
async def metrics() -> Response:
    try:
        from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
    except ImportError:
        return JSONResponse(
            status_code=503,
            content={"error": "prometheus_client not installed"},
        )

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )

