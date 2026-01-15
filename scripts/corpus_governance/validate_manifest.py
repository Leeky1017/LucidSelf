from __future__ import annotations

import argparse
import json
from pathlib import Path

from backend.core.versioning.ids import validate_corpus_release_id_or_raise, validate_version_id_or_raise
from scripts.corpus_governance.models import CorpusManifest


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Validate compiled corpus governance manifest")
    p.add_argument("path", help="Path to compiled manifest JSON")
    p.add_argument("--strict", action="store_true")
    return p


def main() -> int:
    args = build_parser().parse_args()
    path = Path(args.path)
    payload = load(path)
    manifest = CorpusManifest(**payload)

    validate_version_id_or_raise(manifest.version_id)
    validate_corpus_release_id_or_raise(manifest.corpus_release_id)

    license_ids = {l.license_id for l in manifest.licenses}
    asset_ids = {a.asset_id for a in manifest.assets}

    if not manifest.assets:
        raise SystemExit("Manifest assets list is empty")

    for asset in manifest.assets:
        if asset.license_id not in license_ids:
            raise SystemExit(f"Unknown license_id referenced: {asset.asset_id} -> {asset.license_id}")
        for parent in asset.derived_from:
            if parent not in asset_ids:
                raise SystemExit(f"Unknown derived_from reference: {asset.asset_id} -> {parent}")

        abs_path = Path.cwd() / asset.path
        if not abs_path.exists():
            raise SystemExit(f"Non-resolvable asset path: {asset.asset_id} -> {asset.path}")

        if args.strict and asset.release_included:
            if not asset.digest or not asset.digest_algorithm:
                raise SystemExit(f"Missing digest fields for asset: {asset.asset_id}")
            if asset.file_count is None or asset.size_bytes is None:
                raise SystemExit(f"Missing stats fields for asset: {asset.asset_id}")

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
