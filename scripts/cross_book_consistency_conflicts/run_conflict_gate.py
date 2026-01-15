from __future__ import annotations

import argparse
import hashlib
import json
import os
import logging
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id
from scripts.knowledge_graph_builder.builders.graph_builder import GraphBuilder
from scripts.knowledge_graph_builder.models.edge import RelationType


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_conflict_id(*, conflict_type: str, dimension: str, concept_ids: tuple[str, str]) -> str:
    a, b = sorted(concept_ids)
    raw = f"{conflict_type}|{dimension}|{a}|{b}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
    return f"conf_{digest}"


def is_cross_book(conflict: dict[str, Any]) -> bool:
    return len(set(conflict.get("books", []))) >= 2


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines: list[str] = []
    lines.append("# Cross-Book Conflict Report")
    lines.append("")
    lines.append(f"- version_id: `{report['version_id']}`")
    lines.append(f"- corpus_release_id: `{report['corpus_release_id']}`")
    lines.append(f"- policy_id: `{report['policy']['policy_id']}`")
    lines.append(f"- verdict: **{summary['verdict'].upper()}**")
    lines.append("")
    lines.append("## Counts")
    lines.append(f"- total_conflicts: {summary['total_conflicts']}")
    lines.append(f"- suppressed_by_exceptions: {summary['suppressed_by_exceptions']}")
    lines.append(f"- effective_conflicts: {summary['effective_conflicts']}")
    lines.append("")
    lines.append("### By Type")
    for k, v in sorted(summary["counts_by_type"].items()):
        lines.append(f"- `{k}`: {v}")
    lines.append("")
    lines.append("### By Severity")
    for k, v in sorted(summary["counts_by_severity"].items()):
        lines.append(f"- `{k}`: {v}")
    lines.append("")
    lines.append("## Thresholds")
    for item in summary["thresholds"]:
        status = item["status"].upper()
        lines.append(f"- `{item['name']}`: {item['count']} <= {item['max_count']} => **{status}**")
    lines.append("")
    if summary["verdict"] != "pass":
        lines.append("## Action Items")
        for item in summary["thresholds"]:
            if item["status"] != "pass":
                lines.append(f"- `{item['name']}` breached: {item['count']} > {item['max_count']}")
        lines.append("")
    lines.append("## Artifacts")
    lines.append(f"- JSON: `{report['paths']['json']}`")
    lines.append(f"- Exceptions Applied: `{report['paths']['exceptions_applied']}`")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate a cross-book conflict report and enforce blocking thresholds")
    p.add_argument(
        "--policy",
        default="data/knowledge_graph/conflict_gate_policy.v1.yaml",
        help="Path to conflict gate policy YAML",
    )
    p.add_argument(
        "--logic-chains-dir",
        default="data/logic_chains",
        help="Logic chains directory",
    )
    p.add_argument(
        "--authority-config",
        default="data/knowledge_graph/authority_config.yaml",
        help="Authority config YAML for GraphBuilder",
    )
    p.add_argument(
        "--output-dir",
        default="",
        help="Output directory (default: $LS_ARTIFACT_DIR/cross_book_conflicts)",
    )
    p.add_argument(
        "--input-report",
        default="",
        help="Use an existing conflict_report.json as input (skips graph build)",
    )
    p.add_argument(
        "--include-intra-book",
        action="store_true",
        help="Include conflicts whose sources are from a single book",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    logging.getLogger().setLevel(logging.ERROR)

    policy_path = Path(args.policy)
    policy = load_yaml(policy_path)
    policy_id = str(policy.get("policy_id", "unknown"))

    severity_map: dict[str, str] = dict(policy.get("severity_map", {}) or {})
    thresholds: list[dict[str, Any]] = list(policy.get("thresholds", []) or [])

    blocking_enabled = bool((policy.get("blocking", {}) or {}).get("enabled", True))
    cross_book_only = bool((policy.get("scope", {}) or {}).get("cross_book_only", True))
    max_conflicts = int((policy.get("reporting", {}) or {}).get("max_conflicts", 5000))

    exceptions_path_value = (policy.get("exceptions", {}) or {}).get("path")
    exceptions_path = Path(exceptions_path_value) if exceptions_path_value else None
    exceptions_payload = load_yaml(exceptions_path) if exceptions_path else {}
    exceptions: list[dict[str, Any]] = list(exceptions_payload.get("exceptions", []) or [])
    exceptions_by_conflict_id = {str(e.get("conflict_id")): e for e in exceptions if e.get("conflict_id")}

    output_dir = Path(args.output_dir or (Path(os.getenv("LS_ARTIFACT_DIR", "artifacts")) / "cross_book_conflicts"))
    output_dir.mkdir(parents=True, exist_ok=True)

    version_id = resolve_version_id()
    corpus_release_id = resolve_corpus_release_id()

    books_included: list[str] = []

    if args.input_report:
        src = json.loads(Path(args.input_report).read_text(encoding="utf-8"))
        conflicts = list(src.get("conflicts", []) or [])
        books_included = list((src.get("inputs", {}) or {}).get("books_included", []) or [])
        # Ensure policy-driven sorting/determinism.
        for c in conflicts:
            if "severity" not in c and "conflict_type" in c:
                c["severity"] = severity_map.get(c["conflict_type"], "UNKNOWN")
        for c in conflicts:
            if "conflict_id" not in c and all(k in c for k in ("conflict_type", "dimension", "concept_a", "concept_b")):
                c["conflict_id"] = make_conflict_id(
                    conflict_type=str(c["conflict_type"]),
                    dimension=str(c["dimension"]),
                    concept_ids=(str(c["concept_a"]["concept_id"]), str(c["concept_b"]["concept_id"])),
                )
    else:
        tmp_dir = output_dir / "_kg_build"
        tmp_dir.mkdir(parents=True, exist_ok=True)

        builder = GraphBuilder(
            logic_chains_dir=Path(args.logic_chains_dir),
            knowledge_graph_dir=tmp_dir,
            authority_config_path=Path(args.authority_config),
        )
        graph = builder.build_full(dry_run=False)
        books_included = list(graph.metadata.books_included)

        concept_by_id = {c.concept_id: c for c in graph.concepts}
        conflict_edges = [e for e in graph.edges if e.relation_type == RelationType.CONFLICTS_WITH]

        conflicts = []
        for edge in conflict_edges:
            if not edge.conflict_type:
                continue

            a = concept_by_id.get(edge.source_concept_id)
            b = concept_by_id.get(edge.target_concept_id)
            if not a or not b:
                continue

            books = sorted({*(s.book_id for s in a.source_nodes), *(s.book_id for s in b.source_nodes)})
            if not args.include_intra_book and cross_book_only and len(books) < 2:
                continue

            conflict_type = edge.conflict_type.value
            severity = severity_map.get(conflict_type, "UNKNOWN")
            dimension = a.dimension.value
            conflict_id = make_conflict_id(
                conflict_type=conflict_type, dimension=dimension, concept_ids=(a.concept_id, b.concept_id)
            )

            conflicts.append(
                {
                    "conflict_id": conflict_id,
                    "conflict_type": conflict_type,
                    "severity": severity,
                    "dimension": dimension,
                    "books": books,
                    "concept_a": {
                        "concept_id": a.concept_id,
                        "label_zh": a.canonical_label_zh,
                        "book_sources": sorted({s.book_id for s in a.source_nodes}),
                        "node_ids": sorted({s.node_id for s in a.source_nodes}),
                        "snippet_ids": sorted({sid for s in a.source_nodes for sid in s.snippet_ids}),
                    },
                    "concept_b": {
                        "concept_id": b.concept_id,
                        "label_zh": b.canonical_label_zh,
                        "book_sources": sorted({s.book_id for s in b.source_nodes}),
                        "node_ids": sorted({s.node_id for s in b.source_nodes}),
                        "snippet_ids": sorted({sid for s in b.source_nodes for sid in s.snippet_ids}),
                    },
                }
            )

    conflicts.sort(key=lambda c: (c["conflict_type"], c["severity"], c["dimension"], c["conflict_id"]))

    applied_exceptions: list[dict[str, Any]] = []
    suppressed_ids: set[str] = set()
    for conflict in conflicts:
        ex = exceptions_by_conflict_id.get(conflict["conflict_id"])
        if not ex:
            continue
        suppressed_ids.add(conflict["conflict_id"])
        applied_exceptions.append(ex)

    effective_conflicts = [c for c in conflicts if c["conflict_id"] not in suppressed_ids]

    counts_by_type = Counter(c["conflict_type"] for c in effective_conflicts)
    counts_by_severity = Counter(c["severity"] for c in effective_conflicts)
    counts_by_type_severity = Counter(f"{c['conflict_type']}/{c['severity']}" for c in effective_conflicts)
    counts_by_dimension = Counter(c["dimension"] for c in effective_conflicts)

    conflict_index_by_bucket: dict[str, list[str]] = defaultdict(list)
    for conflict in effective_conflicts:
        bucket = f"{conflict['conflict_type']}/{conflict['severity']}"
        conflict_index_by_bucket[bucket].append(conflict["conflict_id"])

    threshold_results: list[dict[str, Any]] = []
    verdict = "pass"
    for threshold in thresholds:
        name = str(threshold.get("name", "unnamed"))
        match = dict(threshold.get("match", {}) or {})
        max_count = int(threshold.get("max_count", 0))

        def matches(conflict: dict[str, Any]) -> bool:
            t = match.get("conflict_type")
            s = match.get("severity")
            if t and conflict["conflict_type"] != t:
                return False
            if s and conflict["severity"] != s:
                return False
            return True

        count = sum(1 for c in effective_conflicts if matches(c))
        status = "pass" if count <= max_count else "fail"
        if status != "pass":
            verdict = "fail"
        threshold_results.append(
            {
                "name": name,
                "match": match,
                "count": count,
                "max_count": max_count,
                "status": status,
            }
        )

    if not blocking_enabled:
        verdict = "pass"

    json_path = output_dir / "conflict_report.json"
    md_path = output_dir / "conflict_report.md"
    exceptions_applied_path = output_dir / "exceptions_applied.json"

    report = {
        "report_version": "1.0",
        "version_id": version_id,
        "corpus_release_id": corpus_release_id,
        "policy": {
            "policy_id": policy_id,
            "path": str(policy_path),
            "blocking_enabled": blocking_enabled,
        },
        "inputs": {
            "logic_chains_dir": str(args.logic_chains_dir) if not args.input_report else None,
            "books_included": books_included,
            "input_report": args.input_report or None,
        },
        "summary": {
            "total_conflicts": len(conflicts),
            "suppressed_by_exceptions": len(suppressed_ids),
            "effective_conflicts": len(effective_conflicts),
            "counts_by_type": dict(sorted(counts_by_type.items())),
            "counts_by_severity": dict(sorted(counts_by_severity.items())),
            "counts_by_type_severity": dict(sorted(counts_by_type_severity.items())),
            "counts_by_dimension": dict(sorted(counts_by_dimension.items())),
            "thresholds": threshold_results,
            "verdict": verdict,
        },
        "exceptions": {
            "path": str(exceptions_path) if exceptions_path else None,
            "applied": applied_exceptions,
            "unmatched": [
                e for e in exceptions if str(e.get("conflict_id")) not in {c["conflict_id"] for c in conflicts}
            ],
        },
        "conflicts": effective_conflicts[:max_conflicts],
        "paths": {
            "json": str(json_path),
            "markdown": str(md_path),
            "exceptions_applied": str(exceptions_applied_path),
        },
    }

    write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")
    write_json(
        exceptions_applied_path,
        {
            "version_id": version_id,
            "corpus_release_id": corpus_release_id,
            "policy_id": policy_id,
            "exceptions_path": str(exceptions_path) if exceptions_path else None,
            "applied": applied_exceptions,
        },
    )

    if verdict != "pass":
        print(f"FAIL: {json_path}")
        return 2
    print(f"OK: {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
