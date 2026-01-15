#!/usr/bin/env python3
"""
Export audit logs as NDJSON (newline-delimited JSON).

Usage:
  python scripts/export_audit_log.py --capability security-privacy-compliance --validate
  python scripts/export_audit_log.py --capability observability-slos --output /tmp/audit.ndjson
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Export LucidSelf audit logs (NDJSON)")
    parser.add_argument(
        "--capability",
        required=True,
        help="Capability name (e.g. security-privacy-compliance, observability-slos)",
    )
    parser.add_argument(
        "--output",
        default="-",
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate JSON and required fields during export",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from backend.core.audit import export_audit_log

    if args.output == "-":
        export_audit_log(capability=args.capability, output=sys.stdout, validate=args.validate)
        return 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        export_audit_log(capability=args.capability, output=f, validate=args.validate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

