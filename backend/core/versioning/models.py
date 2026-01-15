"""
Versioning Artifact Models

Minimal machine-readable artifacts for:
- Version manifest entries
- Deviation reports
- Boot/regression link artifacts (shared with Gate-1)
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class VersionManifestEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    version_id: str
    engine_id: str
    created_at: datetime = Field(default_factory=_utc_now)
    status: str = Field(default="ACTIVE")
    notes: Optional[str] = None


class DeviationReport(BaseModel):
    model_config = ConfigDict(extra="allow")

    report_id: str
    version_id: str
    baseline_version_id: str
    deviation_type: str
    summary: str
    created_at: datetime = Field(default_factory=_utc_now)

    # Optional diagnostic payload (allowed by extra="allow")
    drift: Optional[dict[str, Any]] = None


class StartupCheckItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    check_id: str
    name: str
    required: bool
    status: str
    reason_code: Optional[str] = None


class RegressionSuiteBaseline(BaseModel):
    model_config = ConfigDict(extra="forbid")

    suite_id: str
    version_id: str
    tests: list[str]
    pass_threshold: str


class VersionLinkArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    id: str
    path: Optional[str] = None


class VersionLinkReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    report_id: str
    version_id: str
    artifacts: list[VersionLinkArtifact]
    created_at: datetime = Field(default_factory=_utc_now)

