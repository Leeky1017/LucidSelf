#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Asset Gate: corpus-governance + text-normalization-alignment

Usage:
  bash scripts/gates/asset_gate_corpus.sh [--skip-openspec]

Artifacts:
  - Exports LS_ARTIFACT_DIR (default: artifacts)
  - Writes:
      artifacts/corpus_governance/corpus_manifest.compiled.json
      artifacts/text_normalization_alignment/normalized_entries.jsonl
      artifacts/text_normalization_alignment/normalization_summary.json
      artifacts/text_normalization_alignment/alignment_report.json
      artifacts/text_normalization_alignment/alignment_report.md
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
mkdir -p "$LS_ARTIFACT_DIR/corpus_governance" "$LS_ARTIFACT_DIR/text_normalization_alignment"

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

echo "\$ ${PYTHON_BIN} scripts/corpus_governance/generate_manifest.py --input data/governance/corpus_manifest.v1.yaml --output ${LS_ARTIFACT_DIR}/corpus_governance/corpus_manifest.compiled.json"
PYTHONPATH=. $PYTHON_BIN scripts/corpus_governance/generate_manifest.py \
  --input data/governance/corpus_manifest.v1.yaml \
  --output "${LS_ARTIFACT_DIR}/corpus_governance/corpus_manifest.compiled.json"

echo "\$ ${PYTHON_BIN} scripts/corpus_governance/validate_manifest.py ${LS_ARTIFACT_DIR}/corpus_governance/corpus_manifest.compiled.json --strict"
PYTHONPATH=. $PYTHON_BIN scripts/corpus_governance/validate_manifest.py \
  "${LS_ARTIFACT_DIR}/corpus_governance/corpus_manifest.compiled.json" \
  --strict

echo "\$ ${PYTHON_BIN} scripts/text_normalization_alignment/run_pipeline.py --output-dir ${LS_ARTIFACT_DIR}/text_normalization_alignment"
PYTHONPATH=. $PYTHON_BIN scripts/text_normalization_alignment/run_pipeline.py \
  --output-dir "${LS_ARTIFACT_DIR}/text_normalization_alignment" \
  --books "滴天髓,三命通会,子平真诠,渊海子平,穷通宝鉴,紫微斗数全书,梦林玄解,周公解梦,周易" \
  --max-nodes-per-book 0
