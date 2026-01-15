"""
Versioning Artifact Writers

Writes machine-readable artifacts used by Gate-0/1 acceptance.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from backend.core.versioning.models import (
    DeviationReport,
    RegressionSuiteBaseline,
    StartupCheckItem,
    VersionLinkReport,
    VersionManifestEntry,
)


def write_version_manifest(entries: Iterable[VersionManifestEntry], path: Path) -> Path:
    items = [e.model_dump(mode="json") for e in entries]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_deviation_report(report: DeviationReport, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report.model_dump(mode="json"), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_startup_checks(checks: list[StartupCheckItem], path: Path) -> Path:
    items = [c.model_dump(mode="json") for c in checks]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_regression_suite_baseline(baseline: RegressionSuiteBaseline, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(baseline.model_dump(mode="json"), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_version_link_report(report: VersionLinkReport, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report.model_dump(mode="json"), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path

