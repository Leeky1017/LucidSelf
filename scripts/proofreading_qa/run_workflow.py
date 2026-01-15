from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw:
                continue
            yield json.loads(raw)


def sha12(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def entry_ids_digest_sha256(entry_ids: Iterable[str]) -> str:
    joined = "\n".join(sorted(str(x) for x in entry_ids))
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()


def stable_sort(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def score(entry: dict[str, Any]) -> tuple[str, str]:
        entry_id = str(entry.get("entry_id", ""))
        return sha12(entry_id), entry_id

    return sorted(entries, key=score)


def stable_sample(entries: list[dict[str, Any]], *, take: int) -> list[dict[str, Any]]:
    if take <= 0:
        return []
    return stable_sort(entries)[:take]


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    scope = dict(report.get("scope", {}) or {})
    coverage = dict(report.get("coverage", {}) or {})
    lines: list[str] = []
    lines.append("# Proofreading QA Report")
    lines.append("")
    lines.append(f"- version_id: `{report['version_id']}`")
    lines.append(f"- corpus_release_id: `{report['corpus_release_id']}`")
    lines.append(f"- policy_id: `{report['policy_id']}`")
    if coverage.get("mode"):
        lines.append(f"- coverage_mode: `{coverage.get('mode')}`")
    if scope.get("books_included") is not None:
        lines.append(f"- books_included: {len(list(scope.get('books_included') or []))}")
    if scope.get("missing_books"):
        lines.append(f"- missing_books: {', '.join(scope.get('missing_books') or [])}")
    lines.append(f"- verdict: **{summary['verdict'].upper()}**")
    lines.append("")
    lines.append("## Totals")
    lines.append(f"- tasks_total: {summary['tasks_total']}")
    for status, count in sorted(summary["by_status"].items()):
        lines.append(f"- {status}: {count}")
    lines.append("")
    lines.append("## Thresholds")
    for t in summary["thresholds"]:
        status = t["status"].upper()
        lines.append(f"- `{t['name']}`: {t['value']} <= {t['max']} => **{status}**")
    lines.append("")
    lines.append("## Artifacts")
    lines.append(f"- queue: `{report['paths']['queue']}`")
    lines.append(f"- report: `{report['paths']['json']}`")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Proofreading QA workflow tool (v2)")
    sub = p.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Generate QA queue and report")
    run.add_argument("--policy", default="data/proofreading_qa/qa_policy.v1.yaml")
    run.add_argument(
        "--normalized-entries",
        default="",
        help="Path to normalized_entries.jsonl (default: $LS_ARTIFACT_DIR/text_normalization_alignment/normalized_entries.jsonl)",
    )
    run.add_argument("--output-dir", default="", help="Output directory (default: $LS_ARTIFACT_DIR/proofreading_qa)")

    review = sub.add_parser("review", help="Record a QA decision for a task_id")
    review.add_argument("--queue", default="", help="Path to qa_queue.json (default: $LS_ARTIFACT_DIR/proofreading_qa/qa_queue.json)")
    review.add_argument("--task-id", required=True)
    review.add_argument("--decision", choices=["approved", "rejected", "exception_approved"], required=True)
    review.add_argument("--reviewed-by", default=os.getenv("USER", "unknown"))
    review.add_argument("--note", default="")

    report = sub.add_parser("report", help="Generate QA report from an existing queue")
    report.add_argument("--policy", default="data/proofreading_qa/qa_policy.v1.yaml")
    report.add_argument("--queue", default="", help="Path to qa_queue.json (default: $LS_ARTIFACT_DIR/proofreading_qa/qa_queue.json)")
    report.add_argument("--output-dir", default="", help="Output directory (default: $LS_ARTIFACT_DIR/proofreading_qa)")

    return p


def resolve_paths(*, args: argparse.Namespace) -> tuple[Path, Path, Path]:
    artifact_root = Path(os.getenv("LS_ARTIFACT_DIR", "artifacts"))
    output_dir = Path(args.output_dir or (artifact_root / "proofreading_qa"))
    output_dir.mkdir(parents=True, exist_ok=True)

    normalized_entries = getattr(args, "normalized_entries", "") or str(
        artifact_root / "text_normalization_alignment" / "normalized_entries.jsonl"
    )
    normalized_entries_path = Path(normalized_entries)

    queue_path = Path(args.queue) if getattr(args, "queue", "") else (output_dir / "qa_queue.json")
    return normalized_entries_path, output_dir, queue_path


def cmd_run(args: argparse.Namespace) -> int:
    policy_path = Path(args.policy)
    policy = load_yaml(policy_path)
    policy_id = str(policy.get("policy_id", "unknown"))

    scope = dict(policy.get("scope", {}) or {})
    include_books = [str(b) for b in (scope.get("include_books") or [])]
    exclude_books = {str(b) for b in (scope.get("exclude_books") or [])}

    coverage = dict(policy.get("coverage", {}) or {})
    coverage_mode = str(coverage.get("mode", "sample")).strip().lower()
    if coverage_mode not in {"sample", "full"}:
        coverage_mode = "sample"

    sampling = dict(policy.get("sampling", {}) or {})
    per_book = int(sampling.get("per_book", 5))
    if coverage_mode == "full":
        per_book = 0

    thresholds = dict(policy.get("thresholds", {}) or {})
    require_books_present = bool(scope.get("require_books_present", thresholds.get("require_books_present", False)))

    normalized_entries_path, output_dir, queue_path = resolve_paths(args=args)
    if not normalized_entries_path.exists():
        raise SystemExit(f"Missing normalized entries file: {normalized_entries_path}")

    entries_by_book: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in read_jsonl(normalized_entries_path):
        book_id = str(entry.get("book_id", "unknown"))
        if book_id in exclude_books:
            continue
        if include_books and book_id not in include_books:
            continue
        entries_by_book[book_id].append(entry)

    missing_books: list[str] = []
    if include_books:
        missing_books = sorted(b for b in include_books if b not in entries_by_book and b not in exclude_books)
        if missing_books and require_books_present:
            print(f"WARN: missing books in normalized entries: {', '.join(missing_books)}")

    selected_by_book: dict[str, list[dict[str, Any]]] = {}
    tasks: list[dict[str, Any]] = []
    for book_id, entries in sorted(entries_by_book.items(), key=lambda x: x[0]):
        picked = stable_sort(entries) if coverage_mode == "full" else stable_sample(entries, take=per_book)
        selected_by_book[book_id] = picked
        for entry in picked:
            entry_id = str(entry.get("entry_id", ""))
            task_id = f"qa_{sha12(entry_id)}"
            tasks.append(
                {
                    "task_id": task_id,
                    "status": "pending",
                    "entry_id": entry_id,
                    "book_id": str(entry.get("book_id", "")),
                    "node_id": str(entry.get("node_id", "")),
                    "source_ref": str(entry.get("source_ref", "")),
                    "snippet_ids": list(entry.get("snippet_ids", []) or []),
                    "created_at": utc_now(),
                    "review": None,
                }
            )

    version_id = resolve_version_id()
    corpus_release_id = resolve_corpus_release_id()
    qa_session_id = f"qa_{version_id}_{corpus_release_id}"

    expected_by_book = {book: len(items) for book, items in selected_by_book.items()}
    expected_tasks_total = sum(expected_by_book.values())
    expected_digest = entry_ids_digest_sha256(
        (str(e.get("entry_id", "")) for items in selected_by_book.values() for e in items)
    )

    queue = {
        "qa_queue_version": "1.1",
        "qa_session_id": qa_session_id,
        "policy_id": policy_id,
        "version_id": version_id,
        "corpus_release_id": corpus_release_id,
        "created_at": utc_now(),
        "inputs": {
            "normalized_entries": str(normalized_entries_path),
            "policy_path": str(policy_path),
        },
        "scope": {
            "include_books": include_books or None,
            "exclude_books": sorted(exclude_books),
            "books_included": [b for b, _ in sorted(entries_by_book.items(), key=lambda x: x[0])],
            "missing_books": missing_books,
        },
        "coverage": {
            "mode": coverage_mode,
            "expected_by_book": expected_by_book,
            "expected_tasks_total": expected_tasks_total,
            "expected_entries_digest_sha256": expected_digest,
        },
        "sampling": {
            "mode": coverage_mode,
            "per_book": per_book,
            "method": "full coverage (all entries in scope)"
            if coverage_mode == "full"
            else "sha256(entry_id) asc, take first N per book",
        },
        "tasks": tasks,
    }

    write_json(queue_path, queue)
    return cmd_report(argparse.Namespace(policy=args.policy, queue=str(queue_path), output_dir=str(output_dir)))


def cmd_review(args: argparse.Namespace) -> int:
    _, output_dir, queue_path = resolve_paths(args=args)
    if not queue_path.exists():
        raise SystemExit(f"Missing queue file: {queue_path}")

    payload = json.loads(queue_path.read_text(encoding="utf-8"))
    policy_path = str(((payload.get("inputs") or {}).get("policy_path")) or "data/proofreading_qa/qa_policy.v1.yaml")
    tasks: list[dict[str, Any]] = list(payload.get("tasks", []) or [])

    updated = False
    for task in tasks:
        if task.get("task_id") != args.task_id:
            continue
        task["status"] = args.decision
        task["review"] = {
            "decision": args.decision,
            "reviewed_by": args.reviewed_by,
            "reviewed_at": utc_now(),
            "note": args.note,
        }
        updated = True
        break

    if not updated:
        raise SystemExit(f"Unknown task_id: {args.task_id}")

    payload["tasks"] = tasks
    write_json(queue_path, payload)

    return cmd_report(argparse.Namespace(policy=policy_path, queue=str(queue_path), output_dir=str(output_dir)))


def cmd_report(args: argparse.Namespace) -> int:
    policy_path = Path(args.policy)
    policy = load_yaml(policy_path)
    policy_id = str(policy.get("policy_id", "unknown"))

    thresholds = dict(policy.get("thresholds", {}) or {})
    min_tasks_total = int(thresholds.get("min_tasks_total", 1))
    max_rejected = int(thresholds.get("max_rejected", 0))
    require_reviewed = bool(thresholds.get("require_reviewed", False))
    require_full_coverage = bool(thresholds.get("require_full_coverage", False))
    require_books_present = bool(thresholds.get("require_books_present", False))

    _, output_dir, queue_path = resolve_paths(args=args)
    if not queue_path.exists():
        raise SystemExit(f"Missing queue file: {queue_path}")

    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    tasks = list(queue.get("tasks", []) or [])
    by_status = Counter(str(t.get("status", "unknown")) for t in tasks)

    scope = dict(queue.get("scope", {}) or {})
    missing_books = list(scope.get("missing_books", []) or [])

    coverage = dict(queue.get("coverage", {}) or {})
    expected_by_book = dict(coverage.get("expected_by_book", {}) or {})
    expected_tasks_total = coverage.get("expected_tasks_total")
    expected_digest = str(coverage.get("expected_entries_digest_sha256", "") or "")

    actual_entry_ids = [str(t.get("entry_id", "")) for t in tasks]
    actual_digest = entry_ids_digest_sha256(actual_entry_ids)
    duplicates = len(actual_entry_ids) - len(set(actual_entry_ids))
    actual_by_book = Counter(str(t.get("book_id", "")) for t in tasks)

    rejected = by_status.get("rejected", 0)
    pending = by_status.get("pending", 0)
    in_review = by_status.get("in_review", 0)

    thresholds_result = [
        {
            "name": "max_rejected",
            "value": rejected,
            "max": max_rejected,
            "status": "pass" if rejected <= max_rejected else "fail",
        },
        {
            "name": "min_tasks_total",
            "value": len(tasks),
            "max": min_tasks_total,
            "status": "pass" if len(tasks) >= min_tasks_total else "fail",
        },
    ]

    if require_books_present:
        thresholds_result.append(
            {
                "name": "missing_books_in_scope",
                "value": len(missing_books),
                "max": 0,
                "status": "pass" if len(missing_books) == 0 else "fail",
            }
        )

    if require_full_coverage:
        mismatches = 0
        if expected_tasks_total is None:
            mismatches += 1
        else:
            if int(expected_tasks_total) != len(tasks):
                mismatches += 1

        if expected_by_book:
            for book, expected in expected_by_book.items():
                if int(expected) != int(actual_by_book.get(book, 0)):
                    mismatches += 1
            extra_books = [b for b in actual_by_book.keys() if b not in expected_by_book]
            if extra_books:
                mismatches += 1

        if expected_digest and expected_digest != actual_digest:
            mismatches += 1

        if duplicates > 0:
            mismatches += 1

        thresholds_result.append(
            {
                "name": "full_coverage_mismatches",
                "value": mismatches,
                "max": 0,
                "status": "pass" if mismatches == 0 else "fail",
            }
        )

    if require_reviewed:
        thresholds_result.append(
            {
                "name": "require_reviewed",
                "value": pending + in_review,
                "max": 0,
                "status": "pass" if (pending + in_review) == 0 else "fail",
            }
        )

    verdict = "pass" if all(t["status"] == "pass" for t in thresholds_result) else "fail"

    report_path = output_dir / "qa_report.json"
    md_path = output_dir / "qa_report.md"

    report = {
        "qa_report_version": "1.0",
        "qa_session_id": queue.get("qa_session_id"),
        "policy_id": policy_id,
        "version_id": queue.get("version_id"),
        "corpus_release_id": queue.get("corpus_release_id"),
        "created_at": utc_now(),
        "scope": {
            "include_books": scope.get("include_books"),
            "exclude_books": scope.get("exclude_books"),
            "books_included": scope.get("books_included"),
            "missing_books": missing_books,
        },
        "coverage": {
            "mode": coverage.get("mode"),
            "expected_tasks_total": expected_tasks_total,
            "actual_tasks_total": len(tasks),
            "expected_entries_digest_sha256": expected_digest or None,
            "actual_entries_digest_sha256": actual_digest,
            "expected_by_book": expected_by_book or None,
            "actual_by_book": dict(actual_by_book),
        },
        "summary": {
            "tasks_total": len(tasks),
            "by_status": dict(by_status),
            "thresholds": thresholds_result,
            "verdict": verdict,
        },
        "paths": {
            "queue": str(queue_path),
            "json": str(report_path),
            "markdown": str(md_path),
        },
    }

    write_json(report_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    if verdict != "pass":
        print(f"FAIL: {report_path}")
        return 2
    print(f"OK: {report_path}")
    return 0


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "run":
        return cmd_run(args)
    if args.command == "review":
        return cmd_review(args)
    if args.command == "report":
        return cmd_report(args)
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
