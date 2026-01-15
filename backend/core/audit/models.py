"""
Audit Models

Minimal audit event model for Gate-0 requirements:
- NDJSON export
- Required fields presence
- PII minimization (enforced at writer layer)
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AuditEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audit_id: str = Field(..., description="Unique audit record identifier")
    created_at: datetime = Field(..., description="ISO-8601 timestamp (UTC)")
    event_type: str = Field(..., description="Controlled vocabulary event type")
    result: str = Field(..., description="ALLOW/DENY/BLOCK")

    rejection_reason_code: Optional[str] = None

    # Correlation / scoping identifiers (optional)
    capability: Optional[str] = None
    user_id: Optional[str] = None
    org_id: Optional[str] = None
    version_id: Optional[str] = None
    request_id: Optional[str] = None
    trace_id: Optional[str] = None
    engine_id: Optional[str] = None
    corpus_release_id: Optional[str] = None

    # Human-readable minimal summary (must be redacted)
    summary: Optional[str] = None
