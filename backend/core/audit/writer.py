"""
Audit Writer + Export

Implements minimal Gate-0 audit logging:
- write NDJSON (newline-delimited JSON) audit records
- export + validate NDJSON
"""

from __future__ import annotations

import asyncio
import json
import os
import uuid
from datetime import datetime, timezone
from typing import IO, Any, Dict, Iterable, Optional

from backend.core.audit.models import AuditEvent
from backend.core.observability.context import get_context as get_observability_context
from backend.core.observability.logging import redact_log_data
from backend.core.observability.metrics import AUDIT_RECORDS_TOTAL
from backend.core.observability.tracing import get_trace_id
from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id

AUDIT_LOG_DIR_ENV = "AUDIT_LOG_DIR"
DEFAULT_AUDIT_LOG_DIR = "data/audit"


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _generate_audit_id() -> str:
    return f"aud_{uuid.uuid4().hex[:12]}"


def _audit_log_dir() -> str:
    return os.getenv(AUDIT_LOG_DIR_ENV, DEFAULT_AUDIT_LOG_DIR).strip() or DEFAULT_AUDIT_LOG_DIR


def _capability_log_path(capability: str) -> str:
    base_dir = _audit_log_dir()
    return os.path.join(base_dir, f"{capability}.ndjson")


def create_audit_event(
    *,
    event_type: str,
    result: str,
    capability: str,
    rejection_reason_code: Optional[str] = None,
    summary: Optional[str] = None,
    user_id: Optional[str] = None,
    org_id: Optional[str] = None,
    engine_id: Optional[str] = None,
    version_id: Optional[str] = None,
    corpus_release_id: Optional[str] = None,
    request_id: Optional[str] = None,
    trace_id: Optional[str] = None,
) -> AuditEvent:
    ctx = get_observability_context()
    return AuditEvent(
        audit_id=_generate_audit_id(),
        created_at=_utc_now(),
        event_type=event_type,
        result=result,
        rejection_reason_code=rejection_reason_code,
        capability=capability,
        user_id=user_id or ctx.get("user_id"),
        org_id=org_id or ctx.get("org_id"),
        engine_id=engine_id or ctx.get("engine_id"),
        version_id=version_id or ctx.get("version_id") or resolve_version_id(),
        corpus_release_id=corpus_release_id or ctx.get("corpus_release_id") or resolve_corpus_release_id(),
        request_id=request_id or ctx.get("request_id"),
        trace_id=trace_id or get_trace_id(),
        summary=summary,
    )


def _serialize_audit_record(event: AuditEvent) -> Dict[str, Any]:
    """
    Serialize to the capability-specific field set.

    - security-privacy-compliance: audit_id/created_at/event_type/result/rejection_reason_code/user_id/org_id/version_id/request_id/trace_id/summary
    - observability-slos: audit_id/created_at/event_type/result/rejection_reason_code/capability/version_id/request_id/trace_id/engine_id/user_id
    """
    data = event.model_dump(mode="json", exclude_none=True)
    capability = event.capability or "unknown"

    if capability == "security-privacy-compliance":
        keys = [
            "audit_id",
            "created_at",
            "event_type",
            "result",
            "rejection_reason_code",
            "user_id",
            "org_id",
            "version_id",
            "corpus_release_id",
            "request_id",
            "trace_id",
            "summary",
        ]
        return {k: data.get(k) for k in keys if k in data}

    if capability == "observability-slos":
        keys = [
            "audit_id",
            "created_at",
            "event_type",
            "result",
            "rejection_reason_code",
            "capability",
            "version_id",
            "corpus_release_id",
            "request_id",
            "trace_id",
            "engine_id",
            "user_id",
        ]
        return {k: data.get(k) for k in keys if k in data}

    # Fallback: emit the full (redacted) record.
    return data


def write_audit_event(event: AuditEvent) -> str:
    """
    Append one audit record (NDJSON). Returns the written file path.
    """
    if not event.capability:
        raise ValueError("AuditEvent.capability is required")

    record = _serialize_audit_record(event)

    # Required fields
    for field in ("audit_id", "created_at", "event_type", "result"):
        if not record.get(field):
            raise ValueError(f"Audit record missing required field: {field}")

    record = redact_log_data(record)

    path = _capability_log_path(event.capability)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # Metrics (best-effort)
    try:
        AUDIT_RECORDS_TOTAL.labels(result=event.result, capability=event.capability).inc()
    except Exception:
        pass

    return path


async def write_audit_event_async(event: AuditEvent) -> str:
    return await asyncio.to_thread(write_audit_event, event)


def iter_audit_records(path: str) -> Iterable[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def export_audit_log(
    *,
    capability: str,
    output: Optional[IO[str]] = None,
    validate: bool = True,
) -> str:
    """
    Export audit records for a capability (NDJSON).

    Returns the source audit log path.
    """
    src = _capability_log_path(capability)
    if not os.path.exists(src):
        raise FileNotFoundError(src)

    out = output
    if out is None:
        import sys
        out = sys.stdout

    for record in iter_audit_records(src):
        if validate:
            for field in ("audit_id", "created_at", "event_type", "result"):
                if field not in record:
                    raise ValueError(f"Audit export record missing required field: {field}")
        out.write(json.dumps(record, ensure_ascii=False) + "\n")

    return src
