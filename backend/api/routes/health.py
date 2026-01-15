"""
Health & Version Routes

健康检查和版本信息端点。

对照 tasks.md 13.5:
- Requirements: 6.1.3, 6.1.4
"""

import logging
import os
from datetime import datetime, timezone

from fastapi import APIRouter
from starlette.responses import JSONResponse

from backend.api.models import HealthResponse, VersionResponse
from backend.core.boot.checks import get_boot_requirements, run_boot_checks
from backend.core.observability.logging import log_event
from backend.core.observability.metrics import record_block
from backend.core.audit import create_audit_event, write_audit_event_async
from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id

router = APIRouter(tags=["Health"])
logger = logging.getLogger(__name__)

# 版本信息
VERSION = os.getenv("APP_VERSION", "1.0.0")
BUILD = os.getenv("APP_BUILD", None)
API_VERSION = "v1"


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    健康检查
    
    返回服务状态。
    """
    return HealthResponse(
        status="ok",
        timestamp=datetime.utcnow(),
        version=VERSION,
        version_id=resolve_version_id(),
        corpus_release_id=resolve_corpus_release_id(),
    )


@router.get("/version", response_model=VersionResponse)
async def version_info() -> VersionResponse:
    """
    版本信息
    
    返回 API 版本和构建信息。
    """
    return VersionResponse(
        version=VERSION,
        build=BUILD,
        api_version=API_VERSION,
        version_id=resolve_version_id(),
        corpus_release_id=resolve_corpus_release_id(),
    )


@router.get("/ready")
async def readiness_check() -> dict:
    """
    就绪检查
    
    用于 Kubernetes 等编排系统。
    """
    requirements = get_boot_requirements()
    ready, checks, startup_checks = await run_boot_checks(requirements=requirements)

    if not ready:
        # Record a blocking signal (metrics/log). Audit is handled by the audit module (if configured).
        for name, status in checks.items():
            if status.get("required") and not status.get("ok"):
                record_block(block_type=f"dependency_{name}_unavailable", capability="readiness")
        try:
            await write_audit_event_async(
                create_audit_event(
                    event_type="SLO_BREACH",
                    result="BLOCK",
                    capability="observability-slos",
                    rejection_reason_code="DEPENDENCY_UNAVAILABLE",
                )
            )
        except Exception as e:
            log_event(
                logger=logger,
                level=logging.ERROR,
                event="audit_write_failed",
                error_type=type(e).__name__,
            )

    log_event(
        logger=logger,
        level=logging.INFO if ready else logging.WARNING,
        event="readiness_check",
        ready=ready,
        checks=checks,
    )

    return JSONResponse(
        status_code=200 if ready else 503,
        content={
            "ready": ready,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "version_id": resolve_version_id(),
            "corpus_release_id": resolve_corpus_release_id(),
            "checks": checks,
            "startup_checks": [c.model_dump(mode="json") for c in startup_checks],
            "env": requirements.env,
        },
    )


@router.get("/live")
async def liveness_check() -> dict:
    """
    存活检查
    
    用于 Kubernetes 等编排系统。
    """
    return {"alive": True}
