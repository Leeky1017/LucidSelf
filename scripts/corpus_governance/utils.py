from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path
from typing import Iterable, Optional, Tuple


def safe_run_git(args: list[str]) -> Optional[str]:
    try:
        out = subprocess.check_output(["git", *args], stderr=subprocess.DEVNULL)
        return out.decode("utf-8").strip()
    except Exception:
        return None


def git_object_id_for_path(path: Path) -> Optional[str]:
    """
    Return git object id for a tracked path at HEAD.
    - file -> blob hash
    - dir  -> tree hash
    """
    rel = path.as_posix().lstrip("./")
    if not rel:
        return None
    return safe_run_git(["rev-parse", f"HEAD:{rel}"])


def walk_stats(path: Path) -> Tuple[int, int]:
    """
    (file_count, size_bytes) for file/dir. For dir, walks recursively.
    """
    if path.is_file():
        return (1, path.stat().st_size)
    file_count = 0
    size_bytes = 0
    for p in sorted(path.rglob("*")):
        if p.is_file():
            file_count += 1
            size_bytes += p.stat().st_size
    return (file_count, size_bytes)


def file_digest_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def dir_digest_sha256(path: Path, *, exclude_globs: Optional[Iterable[str]] = None) -> str:
    """
    Compute a stable sha256 for a directory by hashing relative paths + per-file sha256.
    Intended as a fallback when git is unavailable.
    """
    exclude = tuple(exclude_globs or [])
    h = hashlib.sha256()
    for p in sorted(path.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(path).as_posix()
        if exclude and any(p.match(g) or rel.startswith(g.rstrip("/")) for g in exclude):
            continue
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(file_digest_sha256(p).encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()

