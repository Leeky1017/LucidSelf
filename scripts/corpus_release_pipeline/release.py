from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from backend.core.versioning.ids import (
    resolve_corpus_release_id,
    resolve_version_id,
    validate_corpus_release_id_or_raise,
    validate_version_id_or_raise,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Corpus release pipeline tool (v1)")
    sub = p.add_subparsers(dest="command", required=True)

    publish = sub.add_parser("publish", help="Build a reproducible corpus release package")
    publish.add_argument("--artifact-root", default=os.getenv("LS_ARTIFACT_DIR", "artifacts"))
    publish.add_argument("--release-root", default="", help="Default: $LS_ARTIFACT_DIR/corpus_releases")
    publish.add_argument("--corpus-release-id", default="")
    publish.add_argument("--version-id", default="")
    publish.add_argument("--force", action="store_true")

    validate = sub.add_parser("validate", help="Validate an existing corpus release package")
    validate.add_argument("--release-root", default="", help="Default: $LS_ARTIFACT_DIR/corpus_releases")
    validate.add_argument("--corpus-release-id", default="")
    validate.add_argument("--release-dir", default="")

    rollback = sub.add_parser("rollback", help="Rollback active release pointer")
    rollback.add_argument("--release-root", default="", help="Default: $LS_ARTIFACT_DIR/corpus_releases")
    rollback.add_argument("--to", required=True, help="Target corpus_release_id")
    rollback.add_argument("--reason", default="manual_rollback")

    return p


def resolve_release_root(args: argparse.Namespace) -> Path:
    artifact_root = Path(os.getenv("LS_ARTIFACT_DIR", "artifacts"))
    release_root = Path(args.release_root) if args.release_root else (artifact_root / "corpus_releases")
    release_root.mkdir(parents=True, exist_ok=True)
    return release_root


def required_sources(artifact_root: Path) -> list[tuple[str, Path, str]]:
    return [
        ("corpus_manifest", artifact_root / "corpus_governance" / "corpus_manifest.compiled.json", "reports/corpus_manifest.compiled.json"),
        ("normalized_entries", artifact_root / "text_normalization_alignment" / "normalized_entries.jsonl", "reports/normalized_entries.jsonl"),
        ("normalization_summary", artifact_root / "text_normalization_alignment" / "normalization_summary.json", "reports/normalization_summary.json"),
        ("alignment_report_json", artifact_root / "text_normalization_alignment" / "alignment_report.json", "reports/alignment_report.json"),
        ("alignment_report_md", artifact_root / "text_normalization_alignment" / "alignment_report.md", "reports/alignment_report.md"),
        ("conflict_report_json", artifact_root / "cross_book_conflicts" / "conflict_report.json", "reports/conflict_report.json"),
        ("conflict_report_md", artifact_root / "cross_book_conflicts" / "conflict_report.md", "reports/conflict_report.md"),
        ("quality_report_json", artifact_root / "semantic_extraction_quality" / "quality_report.json", "reports/quality_report.json"),
        ("quality_report_md", artifact_root / "semantic_extraction_quality" / "quality_report.md", "reports/quality_report.md"),
        ("qa_queue", artifact_root / "proofreading_qa" / "qa_queue.json", "reports/qa_queue.json"),
        ("qa_report_json", artifact_root / "proofreading_qa" / "qa_report.json", "reports/qa_report.json"),
        ("qa_report_md", artifact_root / "proofreading_qa" / "qa_report.md", "reports/qa_report.md"),
    ]


def cmd_publish(args: argparse.Namespace) -> int:
    artifact_root = Path(args.artifact_root)
    release_root = resolve_release_root(args)

    corpus_release_id = args.corpus_release_id or resolve_corpus_release_id()
    version_id = args.version_id or resolve_version_id()
    validate_corpus_release_id_or_raise(corpus_release_id)
    validate_version_id_or_raise(version_id)

    release_dir = release_root / corpus_release_id
    if release_dir.exists() and not args.force:
        raise SystemExit(f"Release directory already exists (use --force to overwrite): {release_dir}")
    if release_dir.exists() and args.force:
        shutil.rmtree(release_dir)
    release_dir.mkdir(parents=True, exist_ok=True)

    copied: list[dict[str, Any]] = []
    for artifact_id, src, dest_rel in required_sources(artifact_root):
        if not src.exists():
            raise SystemExit(f"Missing required artifact: {artifact_id} -> {src}")
        dest = release_dir / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied.append(
            {
                "artifact_id": artifact_id,
                "source_path": str(src),
                "path": dest_rel,
                "sha256": sha256_file(dest),
                "bytes": dest.stat().st_size,
            }
        )

    hashes_path = release_dir / "hashes.json"
    hashes = {"hashes_version": "1.0", "items": copied}
    write_json(hashes_path, hashes)

    digest_seed = "\n".join(f"{i['path']}:{i['sha256']}" for i in sorted(copied, key=lambda x: x["path"]))
    package_digest = hashlib.sha256(digest_seed.encode("utf-8")).hexdigest()

    manifest_path = release_dir / "release_manifest.json"
    manifest = {
        "release_manifest_version": "1.0",
        "version_id": version_id,
        "corpus_release_id": corpus_release_id,
        "created_at": utc_now(),
        "package_digest_sha256": package_digest,
        "hashes_path": "hashes.json",
        "artifacts": copied,
    }
    write_json(manifest_path, manifest)

    active_path = release_root / "active_release.json"
    active = {
        "active_release_version": "1.0",
        "active_corpus_release_id": corpus_release_id,
        "package_digest_sha256": package_digest,
        "updated_at": utc_now(),
    }
    write_json(active_path, active)

    registry_path = release_root / "release_registry.ndjson"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with registry_path.open("a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "event": "PUBLISH",
                    "created_at": utc_now(),
                    "version_id": version_id,
                    "corpus_release_id": corpus_release_id,
                    "package_digest_sha256": package_digest,
                    "release_dir": str(release_dir),
                },
                ensure_ascii=False,
            )
            + "\n"
        )

    print(str(release_dir))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    release_root = resolve_release_root(args)
    if args.release_dir:
        release_dir = Path(args.release_dir)
    else:
        corpus_release_id = args.corpus_release_id or resolve_corpus_release_id()
        release_dir = release_root / corpus_release_id

    manifest_path = release_dir / "release_manifest.json"
    hashes_path = release_dir / "hashes.json"
    if not manifest_path.exists() or not hashes_path.exists():
        raise SystemExit(f"Missing release manifest/hashes: {release_dir}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_version_id_or_raise(manifest.get("version_id"))
    validate_corpus_release_id_or_raise(manifest.get("corpus_release_id"))

    hashes = json.loads(hashes_path.read_text(encoding="utf-8"))
    items = list(hashes.get("items", []) or [])
    for item in items:
        rel_path = Path(str(item["path"]))
        abs_path = release_dir / rel_path
        if not abs_path.exists():
            raise SystemExit(f"Missing release file: {abs_path}")
        actual = sha256_file(abs_path)
        if actual != item["sha256"]:
            raise SystemExit(f"Hash mismatch: {rel_path} expected={item['sha256']} actual={actual}")

    print("OK")
    return 0


def cmd_rollback(args: argparse.Namespace) -> int:
    release_root = resolve_release_root(args)
    target = str(args.to).strip()
    validate_corpus_release_id_or_raise(target)
    target_dir = release_root / target
    if not target_dir.exists():
        raise SystemExit(f"Unknown release id (missing dir): {target_dir}")

    active_path = release_root / "active_release.json"
    previous = None
    if active_path.exists():
        payload = json.loads(active_path.read_text(encoding="utf-8"))
        previous = payload.get("active_corpus_release_id")

    write_json(
        active_path,
        {
            "active_release_version": "1.0",
            "active_corpus_release_id": target,
            "updated_at": utc_now(),
            "rollback_from": previous,
            "rollback_reason": args.reason,
        },
    )

    rollback_record = target_dir / "rollback_record.json"
    write_json(
        rollback_record,
        {
            "rollback_version": "1.0",
            "created_at": utc_now(),
            "from_corpus_release_id": previous,
            "to_corpus_release_id": target,
            "reason": args.reason,
            "version_id": resolve_version_id(),
        },
    )

    print("OK")
    return 0


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "publish":
        return cmd_publish(args)
    if args.command == "validate":
        return cmd_validate(args)
    if args.command == "rollback":
        return cmd_rollback(args)
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

