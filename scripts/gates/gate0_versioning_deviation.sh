#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Gate-0: Versioning + Deviation Detection

Usage:
  bash scripts/gates/gate0_versioning_deviation.sh [--skip-openspec] [--skip-pytest]

Runs:
  - openspec validate --specs --strict --no-interactive
  - pytest backend/tests/gate0_versioning_deviation

Artifacts:
  - Exports LS_ARTIFACT_DIR (default: artifacts)
  - Writes artifacts/versioning/version_manifest.json (smoke)
  - Writes JUnit XML: artifacts/gate0_versioning_deviation/pytest-junit.xml

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
mkdir -p "$LS_ARTIFACT_DIR/gate0_versioning_deviation" "$LS_ARTIFACT_DIR/versioning"

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
  echo "\$ PYTHONPATH=. ${PYTEST_BIN} backend/tests/gate0_versioning_deviation -q --junitxml=${LS_ARTIFACT_DIR}/gate0_versioning_deviation/pytest-junit.xml"
  PYTHONPATH=. $PYTEST_BIN backend/tests/gate0_versioning_deviation -q --junitxml="${LS_ARTIFACT_DIR}/gate0_versioning_deviation/pytest-junit.xml"
fi

echo "\$ ${PYTHON_BIN} -c '<generate version manifest>'"
PYTHONPATH=. $PYTHON_BIN - <<'PY'
import os
from pathlib import Path

from backend.core.versioning.artifacts import write_version_manifest
from backend.core.versioning.ids import resolve_version_id
from backend.core.versioning.models import VersionManifestEntry

root = Path(os.getenv("LS_ARTIFACT_DIR", "artifacts")) / "versioning"
write_version_manifest(
    [
        VersionManifestEntry(
            version_id=resolve_version_id(),
            engine_id="cross-system-fusion",
            status="ACTIVE",
            notes="gate0 smoke manifest",
        )
    ],
    root / "version_manifest.json",
)
print(str(root / "version_manifest.json"))
PY

