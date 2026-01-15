#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Gate-0: Security/Privacy/Compliance + Observability SLOs

Usage:
  bash scripts/gates/gate0_security_observability.sh [--skip-openspec] [--skip-pytest]

Runs:
  - openspec validate --specs --strict --no-interactive
  - pytest backend/tests/gate0_security_observability

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

if [[ "$SKIP_OPENSPEC" -eq 0 ]]; then
  if ! command -v openspec >/dev/null 2>&1; then
    echo "Missing 'openspec' CLI in PATH" >&2
    exit 127
  fi
  echo "\$ openspec validate --specs --strict --no-interactive"
  openspec validate --specs --strict --no-interactive
fi

if [[ "$SKIP_PYTEST" -eq 0 ]]; then
  echo "\$ PYTHONPATH=. ${PYTEST_BIN} backend/tests/gate0_security_observability -q"
  PYTHONPATH=. $PYTEST_BIN backend/tests/gate0_security_observability -q
fi

