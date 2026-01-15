from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id
from scripts.codegen.semantic_generator import SemanticMigrationTool

_WARNING_RE = re.compile(
    r"^(?P<file>.+?):(?P<line>\d+):(?P<column>\d+):\s+(?P<error_type>[^:]+):\s+(?P<message>.+)$"
)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_error_id(file: str, error_type: str, message: str) -> str:
    raw = f"{file}|{error_type}|{message}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
    return f"err_{digest}"


def parse_warning(text: str) -> dict[str, Any] | None:
    match = _WARNING_RE.match(text.strip())
    if not match:
        return None
    return {
        "file": match.group("file"),
        "line": int(match.group("line")),
        "column": int(match.group("column")),
        "error_type": match.group("error_type").strip(),
        "message": match.group("message").strip(),
    }


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines: list[str] = []
    lines.append("# Semantic Extraction Quality Report")
    lines.append("")
    lines.append(f"- version_id: `{report['version_id']}`")
    lines.append(f"- corpus_release_id: `{report['corpus_release_id']}`")
    lines.append(f"- ruleset_id: `{report['ruleset']['ruleset_id']}`")
    lines.append(f"- verdict: **{summary['verdict'].upper()}**")
    lines.append("")
    lines.append("## Totals")
    lines.append(f"- total_books: {summary['total_books']}")
    lines.append(f"- migrated_books: {summary['migrated_books']}")
    lines.append(f"- total_errors: {summary['total_errors']}")
    lines.append(f"- total_warnings: {summary['total_warnings']}")
    lines.append("")
    lines.append("## Thresholds")
    for item in summary["thresholds"]:
        status = item["status"].upper()
        lines.append(f"- `{item['name']}`: {item['value']} <= {item['max']} => **{status}**")
    lines.append("")
    lines.append("## Top Warning Types (sampled)")
    for k, v in summary["warnings_by_type_top"].items():
        lines.append(f"- `{k}`: {v}")
    lines.append("")
    lines.append("## Artifacts")
    lines.append(f"- JSON: `{report['paths']['json']}`")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run semantic extraction quality gates (Gate-1)")
    p.add_argument(
        "--rules",
        default="data/quality_gates/semantic_extraction_rules.v1.yaml",
        help="Path to semantic extraction quality rules YAML",
    )
    p.add_argument(
        "--output-dir",
        default="",
        help="Output directory (default: $LS_ARTIFACT_DIR/semantic_extraction_quality)",
    )
    p.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Parallelism for dry-run migration (default: 1 for determinism)",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    logging.getLogger().setLevel(logging.ERROR)

    rules_path = Path(args.rules)
    rules = load_yaml(rules_path)
    ruleset_id = str(rules.get("ruleset_id", "unknown"))
    blocking_enabled = bool((rules.get("blocking", {}) or {}).get("enabled", True))

    thresholds = dict(rules.get("thresholds", {}) or {})
    max_total_errors = int(thresholds.get("max_total_errors", 0))
    max_total_warnings = int(thresholds.get("max_total_warnings", 0))

    exception_path_value = (rules.get("exceptions", {}) or {}).get("path")
    exceptions_path = Path(exception_path_value) if exception_path_value else None
    exceptions_payload = load_yaml(exceptions_path) if exceptions_path else {}
    exceptions: list[dict[str, Any]] = list(exceptions_payload.get("exceptions", []) or [])
    exception_ids = {str(e.get("error_id")) for e in exceptions if e.get("error_id")}

    output_dir = Path(
        args.output_dir or (Path(os.getenv("LS_ARTIFACT_DIR", "artifacts")) / "semantic_extraction_quality")
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    version_id = resolve_version_id()
    corpus_release_id = resolve_corpus_release_id()

    tool = SemanticMigrationTool()
    tool.migrate_all(dry_run=True, parallel=args.parallel)
    migration_report = tool.get_report()

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    raw_total_warnings = 0

    for book_id, result in migration_report.results.items():
        for err in result.errors:
            error_id = make_error_id(err.file, err.error_type, err.message)
            errors.append(
                {
                    "error_id": error_id,
                    "book_id": book_id,
                    "file": err.file,
                    "line": err.line,
                    "column": err.column,
                    "error_type": err.error_type,
                    "message": err.message,
                    "suggestion": err.suggestion,
                    "severity": err.severity,
                }
            )
        for w in result.warnings:
            raw_total_warnings += 1
            parsed = parse_warning(w)
            if not parsed:
                continue
            warnings.append(
                {
                    "warning_id": make_error_id(parsed["file"], parsed["error_type"], parsed["message"]),
                    "book_id": book_id,
                    **parsed,
                }
            )

    applied_exceptions = [e for e in errors if e["error_id"] in exception_ids]
    effective_errors = [e for e in errors if e["error_id"] not in exception_ids]

    warnings_by_type = Counter(w["error_type"] for w in warnings)
    warnings_by_type_top = dict(warnings_by_type.most_common(10))

    thresholds_result = [
        {
            "name": "max_total_errors",
            "value": len(effective_errors),
            "max": max_total_errors,
            "status": "pass" if len(effective_errors) <= max_total_errors else "fail",
        },
        {
            "name": "max_total_warnings",
            "value": raw_total_warnings,
            "max": max_total_warnings,
            "status": "pass" if raw_total_warnings <= max_total_warnings else "fail",
        },
    ]

    verdict = "pass" if all(t["status"] == "pass" for t in thresholds_result) else "fail"
    if not blocking_enabled:
        verdict = "pass"

    json_path = output_dir / "quality_report.json"
    md_path = output_dir / "quality_report.md"

    report = {
        "report_version": "1.0",
        "version_id": version_id,
        "corpus_release_id": corpus_release_id,
        "ruleset": {
            "ruleset_id": ruleset_id,
            "path": str(rules_path),
            "blocking_enabled": blocking_enabled,
        },
        "inputs": {
            "parallel": args.parallel,
            "exceptions_path": str(exceptions_path) if exceptions_path else None,
        },
        "summary": {
            "total_books": migration_report.total_books,
            "migrated_books": migration_report.migrated_books,
            "coverage_percentage": migration_report.coverage_percentage,
            "overall_success_rate": migration_report.overall_success_rate,
            "total_errors": len(effective_errors),
            "total_warnings": raw_total_warnings,
            "parsed_warnings": len(warnings),
            "warnings_by_type_top": warnings_by_type_top,
            "thresholds": thresholds_result,
            "verdict": verdict,
        },
        "exceptions": {
            "applied": applied_exceptions,
        },
        "errors": effective_errors[: int((rules.get("reporting", {}) or {}).get("max_error_samples", 200))],
        "warnings": warnings[: int((rules.get("reporting", {}) or {}).get("max_warning_samples", 200))],
        "paths": {
            "json": str(json_path),
            "markdown": str(md_path),
        },
    }

    write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    if verdict != "pass":
        print(f"FAIL: {json_path}")
        return 2
    print(f"OK: {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
