from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id
from scripts.corpus_governance.models import CorpusManifest
from scripts.corpus_governance.utils import (
    dir_digest_sha256,
    file_digest_sha256,
    git_object_id_for_path,
    walk_stats,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_manifest(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def compile_manifest(raw: dict, repo_root: Path) -> dict:
    manifest = CorpusManifest(**raw)
    manifest.version_id = manifest.version_id or resolve_version_id()
    manifest.corpus_release_id = manifest.corpus_release_id or resolve_corpus_release_id()
    manifest.generated_at = utc_now_iso()

    license_ids = {l.license_id for l in manifest.licenses}
    assets_by_id = {a.asset_id: a for a in manifest.assets}

    for asset in manifest.assets:
        if asset.license_id not in license_ids:
            raise SystemExit(f"Unknown license_id referenced by asset {asset.asset_id}: {asset.license_id}")
        for parent in asset.derived_from:
            if parent not in assets_by_id:
                raise SystemExit(f"Unknown derived_from reference in {asset.asset_id}: {parent}")

        abs_path = repo_root / asset.path
        if not abs_path.exists():
            raise SystemExit(f"Asset path does not exist: {asset.asset_id} -> {asset.path}")

        # Governance tracks all assets, but only release_included assets require
        # stable size + digest computation (to keep gate runs fast).
        if not asset.release_included:
            continue

        file_count, size_bytes = walk_stats(abs_path)
        asset.file_count = file_count
        asset.size_bytes = size_bytes

        git_oid = git_object_id_for_path(Path(asset.path))
        if git_oid:
            asset.digest_algorithm = "git"
            asset.digest = git_oid
        else:
            if abs_path.is_file():
                asset.digest_algorithm = "sha256_file"
                asset.digest = file_digest_sha256(abs_path)
            else:
                asset.digest_algorithm = "sha256_dir"
                asset.digest = dir_digest_sha256(abs_path, exclude_globs=["**/__pycache__/**", "**/.pytest_cache/**"])

    return manifest.model_dump(mode="json")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate compiled corpus governance manifest")
    p.add_argument("--input", default="data/governance/corpus_manifest.v1.yaml")
    p.add_argument("--output", default="artifacts/corpus_governance/corpus_manifest.compiled.json")
    return p


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path.cwd()
    input_path = Path(args.input)
    output_path = Path(args.output)

    raw = load_manifest(input_path)
    compiled = compile_manifest(raw, repo_root)
    write_json(output_path, compiled)
    print(str(output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
