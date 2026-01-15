#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Gate-1: Cross-Book Conflicts + Semantic Extraction Quality Gates

Usage:
  bash scripts/gates/gate1_cross_book_conflicts_and_quality.sh [--skip-openspec]

Runs:
  - openspec validate --specs --strict --no-interactive
  - scripts/cross_book_consistency_conflicts/run_conflict_gate.py
  - scripts/semantic_extraction_quality_gates/run_quality_gate.py

Artifacts:
  - Exports LS_ARTIFACT_DIR (default: artifacts)
  - Cross-book conflicts:
      artifacts/cross_book_conflicts/conflict_report.json
      artifacts/cross_book_conflicts/conflict_report.md
      artifacts/cross_book_conflicts/exceptions_applied.json
  - Semantic extraction quality:
      artifacts/semantic_extraction_quality/quality_report.json
      artifacts/semantic_extraction_quality/quality_report.md
USAGE
}

SKIP_OPENSPEC=0

for arg in "$@"; do
  case "$arg" in
    -h|--help)
      usage
      exit 0
      ;;
    --skip-openspec)
      SKIP_OPENSPEC=1
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

if [[ -z "${LS_ARTIFACT_DIR:-}" ]]; then
  export LS_ARTIFACT_DIR="artifacts"
fi
mkdir -p "$LS_ARTIFACT_DIR/cross_book_conflicts" "$LS_ARTIFACT_DIR/semantic_extraction_quality"

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

echo "\$ ${PYTHON_BIN} scripts/cross_book_consistency_conflicts/run_conflict_gate.py --output-dir ${LS_ARTIFACT_DIR}/cross_book_conflicts"
PYTHONPATH=. $PYTHON_BIN scripts/cross_book_consistency_conflicts/run_conflict_gate.py \
  --output-dir "${LS_ARTIFACT_DIR}/cross_book_conflicts"

echo "\$ ${PYTHON_BIN} scripts/semantic_extraction_quality_gates/run_quality_gate.py --output-dir ${LS_ARTIFACT_DIR}/semantic_extraction_quality --parallel 1"
PYTHONPATH=. $PYTHON_BIN scripts/semantic_extraction_quality_gates/run_quality_gate.py \
  --output-dir "${LS_ARTIFACT_DIR}/semantic_extraction_quality" \
  --parallel 1
