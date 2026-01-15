#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Gate-1: Bootability + Regression Baseline

Usage:
  bash scripts/gates/gate1_boot_regression.sh [--skip-openspec] [--skip-pytest]

Runs:
  - openspec validate --specs --strict --no-interactive
  - pytest backend/tests/gate1_boot_regression backend/tests/integration/test_pipeline_e2e.py

Artifacts:
  - Exports LS_ARTIFACT_DIR (default: artifacts)
  - Drift report + summaries: artifacts/regression/*.json
  - Version manifest: artifacts/versioning/version_manifest.json
  - JUnit XML: artifacts/gate1_boot_regression/pytest-junit.xml
  - Version link report: artifacts/regression/version_link_report.json
  - Regression suite baseline: artifacts/regression/regression_suite_baseline.json

Environment:
  - Uses .venv/bin/{python,pytest} if present; otherwise falls back to python3/python.
  - Sets PYTHONPATH=. to run tests from repo root.
USAGE
}

SKIP_OPENSPEC=0
SKIP_PYTEST=0

for arg in "$@"; do
  case "$arg" in
    -h|--help)
      usage
      exit 0
      ;;
    --skip-openspec)
      SKIP_OPENSPEC=1
      ;;
    --skip-pytest)
      SKIP_PYTEST=1
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo >&2
      usage >&2
      exit 2
      ;;
  esac
done

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN=""
if [[ -x ".venv/bin/python" ]]; then
  PYTHON_BIN=".venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Missing python interpreter (expected .venv/bin/python, python3, or python)" >&2
  exit 127
fi

PYTEST_BIN=""
if [[ -x ".venv/bin/pytest" ]]; then
  PYTEST_BIN=".venv/bin/pytest"
else
  PYTEST_BIN="$PYTHON_BIN -m pytest"
fi

if [[ -z "${LS_ARTIFACT_DIR:-}" ]]; then
  export LS_ARTIFACT_DIR="artifacts"
fi
mkdir -p "$LS_ARTIFACT_DIR/gate1_boot_regression" "$LS_ARTIFACT_DIR/regression" "$LS_ARTIFACT_DIR/versioning"

if [[ -z "${LS_VERSION_ID:-}" ]] && command -v git >/dev/null 2>&1; then
  SHA="$(git rev-parse --short=12 HEAD 2>/dev/null || true)"
  if [[ -n "$SHA" ]]; then
    export LS_VERSION_ID="ver_${SHA}"
  fi
fi

if [[ -z "${LS_CORPUS_RELEASE_ID:-}" ]] && command -v git >/dev/null 2>&1; then
  TREE="$(git rev-parse HEAD:data 2>/dev/null || true)"
  if [[ -n "$TREE" ]]; then
    export LS_CORPUS_RELEASE_ID="cr_${TREE:0:12}"
  fi
fi

if [[ "$SKIP_OPENSPEC" -eq 0 ]]; then
  if ! command -v openspec >/dev/null 2>&1; then
    echo "Missing 'openspec' CLI in PATH" >&2
    exit 127
  fi
  echo "\$ openspec validate --specs --strict --no-interactive"
  openspec validate --specs --strict --no-interactive
fi

if [[ "$SKIP_PYTEST" -eq 0 ]]; then
  echo "\$ PYTHONPATH=. ${PYTEST_BIN} backend/tests/gate1_boot_regression backend/tests/integration/test_pipeline_e2e.py -q --junitxml=${LS_ARTIFACT_DIR}/gate1_boot_regression/pytest-junit.xml"
  PYTHONPATH=. $PYTEST_BIN \
    backend/tests/gate1_boot_regression \
    backend/tests/integration/test_pipeline_e2e.py \
    -q \
    --junitxml="${LS_ARTIFACT_DIR}/gate1_boot_regression/pytest-junit.xml"
fi

echo "\$ ${PYTHON_BIN} -c '<write regression suite baseline + version link report>'"
PYTHONPATH=. $PYTHON_BIN - <<'PY'
import os
import uuid
from pathlib import Path

from backend.core.versioning.artifacts import write_regression_suite_baseline, write_version_link_report, write_startup_checks
from backend.core.versioning.ids import resolve_version_id
from backend.core.versioning.models import RegressionSuiteBaseline, VersionLinkArtifact, VersionLinkReport
from backend.core.boot.checks import get_boot_requirements, run_boot_checks

artifact_root = Path(os.getenv("LS_ARTIFACT_DIR", "artifacts"))
regression_dir = artifact_root / "regression"
regression_dir.mkdir(parents=True, exist_ok=True)

version_id = resolve_version_id()

baseline = RegressionSuiteBaseline(
    suite_id="gate1_boot_regression",
    version_id=version_id,
    tests=[
        "backend/tests/gate1_boot_regression",
        "backend/tests/integration/test_pipeline_e2e.py",
    ],
    pass_threshold="all tests must pass (pytest exit code 0)",
)
write_regression_suite_baseline(baseline, regression_dir / "regression_suite_baseline.json")

requirements = get_boot_requirements()
import asyncio
_, _, startup_checks = asyncio.run(run_boot_checks(requirements=requirements))
write_startup_checks(startup_checks, regression_dir / "startup_checks.json")

report = VersionLinkReport(
    report_id=f"vlr_{uuid.uuid4().hex[:12]}",
    version_id=version_id,
    artifacts=[
        VersionLinkArtifact(type="junit", id="pytest", path=str(artifact_root / "gate1_boot_regression" / "pytest-junit.xml")),
        VersionLinkArtifact(type="deviation_report", id="pipeline_bazi", path=str(regression_dir / "deviation_report.json")),
        VersionLinkArtifact(type="regression_suite_baseline", id="gate1_boot_regression", path=str(regression_dir / "regression_suite_baseline.json")),
        VersionLinkArtifact(type="startup_checks", id="readiness", path=str(regression_dir / "startup_checks.json")),
        VersionLinkArtifact(type="version_manifest", id="versioning", path=str(artifact_root / "versioning" / "version_manifest.json")),
    ],
)
write_version_link_report(report, regression_dir / "version_link_report.json")
print(str(regression_dir / "version_link_report.json"))
PY
