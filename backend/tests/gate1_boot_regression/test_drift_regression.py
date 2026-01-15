from __future__ import annotations

import hashlib
import json
import os
import uuid
from pathlib import Path

import pytest

from backend.core.versioning.artifacts import write_deviation_report, write_version_manifest
from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id
from backend.core.versioning.models import DeviationReport, VersionManifestEntry
from backend.pipeline.orchestrator import BirthDataInput, Pipeline, PipelineInput
from backend.testing.integration.drift_detector import DriftDetector


BASELINE_PATH = Path(__file__).parent / "baselines" / "pipeline_bazi_summary.v1.json"


def _sha12_json(data: object) -> str:
    blob = json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:12]


def _artifact_root(tmp_path: Path) -> Path:
    root = os.getenv("LS_ARTIFACT_DIR", "").strip()
    if root:
        return Path(root)
    return tmp_path / "artifacts"


def _load_baseline() -> tuple[dict, float]:
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    expected = data["expected"]
    max_drift = float(data.get("max_drift", 0.1))
    return expected, max_drift


def _summarize_pipeline_output(output) -> dict:
    return {
        "engine_results": {k: {"rule_count": len(v)} for k, v in output.engine_results.items()},
        "fusion": {
            "primary_themes": list(output.fusion_result.primary_themes),
            "cross_validation_score": round(float(output.fusion_result.cross_validation_score), 4),
            "contributing_engines": list(output.fusion_result.contributing_engines),
        },
        "raw_factors": {
            k: {
                "has_four_pillars": hasattr(v, "four_pillars"),
                "has_day_master": hasattr(v, "day_master"),
            }
            for k, v in output.raw_factors.items()
        },
    }


@pytest.mark.asyncio
async def test_pipeline_bazi_drift_regression(tmp_path: Path):
    expected, max_drift = _load_baseline()
    version_id = resolve_version_id()
    corpus_release_id = resolve_corpus_release_id()
    baseline_version_id = f"ver_{_sha12_json(expected)}"

    pipeline = Pipeline()
    birth = BirthDataInput(
        year=1990,
        month=5,
        day=15,
        hour=14,
        minute=30,
        timezone="Asia/Shanghai",
        gender="male",
        latitude=39.9042,
        longitude=116.4074,
    )
    output = await pipeline.execute(
        PipelineInput(
            user_id="test_user",
            birth_data=birth,
            engines=["bazi"],
            include_narrative=False,
        )
    )

    actual = _summarize_pipeline_output(output)

    artifact_root = _artifact_root(tmp_path)
    regression_dir = artifact_root / "regression"
    versioning_dir = artifact_root / "versioning"
    regression_dir.mkdir(parents=True, exist_ok=True)
    versioning_dir.mkdir(parents=True, exist_ok=True)

    (regression_dir / "baseline_summary.json").write_text(
        json.dumps(expected, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (regression_dir / "actual_summary.json").write_text(
        json.dumps(actual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    detector = DriftDetector(default_max_drift=max_drift)
    drift = detector.detect(expected=expected, actual=actual, max_drift=max_drift)

    report = DeviationReport(
        report_id=f"devr_{uuid.uuid4().hex[:12]}",
        version_id=version_id,
        baseline_version_id=baseline_version_id,
        deviation_type="NO_DEVIATION" if drift["passed"] else "OUTPUT_DRIFT",
        summary="drift within threshold" if drift["passed"] else "drift exceeds threshold",
        drift={
            **drift,
            "corpus_release_id": corpus_release_id,
        },
    )

    write_deviation_report(report, regression_dir / "deviation_report.json")

    write_version_manifest(
        [
            VersionManifestEntry(
                version_id=baseline_version_id,
                engine_id="bazi-calculator",
                status="BASELINE",
                notes="baseline summary for drift regression",
            ),
            VersionManifestEntry(
                version_id=version_id,
                engine_id="bazi-calculator",
                status="ACTIVE",
                notes=f"corpus_release_id={corpus_release_id}",
            ),
        ],
        versioning_dir / "version_manifest.json",
    )

    assert drift["passed"], f"Drift {drift['total_drift']:.3f} exceeds max {max_drift:.3f}"

