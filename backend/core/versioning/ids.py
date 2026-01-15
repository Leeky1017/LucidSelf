"""
Version ID + Corpus Release ID

This module provides a single source of truth for runtime identifiers used for:
- traceability (logs/audit)
- regression reproducibility (artifacts)

It is intentionally dependency-light.
"""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
from dataclasses import dataclass
from typing import Optional


VERSION_ID_ENV = "LS_VERSION_ID"
CORPUS_RELEASE_ID_ENV = "LS_CORPUS_RELEASE_ID"

# Recommended (OpenSpec) patterns; implementations should normalize into these.
_VERSION_ID_RE = re.compile(r"^ver_[a-z0-9]{12,}$")
_CORPUS_RELEASE_ID_RE = re.compile(r"^cr_[a-z0-9]{12,}$")


class VersioningError(ValueError):
    """Deterministic versioning validation error."""

    def __init__(self, code: str, message: str, *, value: Optional[str] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.value = value


def _sha12(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def _derive_version_id(seed: str) -> str:
    return f"ver_{_sha12(seed.strip() or 'unknown')}"


def _derive_corpus_release_id(seed: str) -> str:
    return f"cr_{_sha12(seed.strip() or 'unknown')}"


def _safe_run_git(args: list[str]) -> Optional[str]:
    try:
        out = subprocess.check_output(["git", *args], stderr=subprocess.DEVNULL)
        return out.decode("utf-8").strip()
    except Exception:
        return None


@dataclass(frozen=True)
class _CacheEntry:
    env_value: Optional[str]
    resolved: str


_version_id_cache: Optional[_CacheEntry] = None
_corpus_release_id_cache: Optional[_CacheEntry] = None


def clear_versioning_caches() -> None:
    global _version_id_cache, _corpus_release_id_cache
    _version_id_cache = None
    _corpus_release_id_cache = None


def resolve_version_id() -> str:
    """
    Resolve the current version_id.

    Priority:
    1) LS_VERSION_ID (normalized to ver_*)
    2) Build/CI envs (APP_BUILD/GITHUB_SHA/GIT_SHA)
    3) git commit (if available)
    4) APP_VERSION (hashed)
    """
    global _version_id_cache
    env = os.getenv(VERSION_ID_ENV, "").strip() or None
    if _version_id_cache is not None and _version_id_cache.env_value == env:
        return _version_id_cache.resolved

    if env and _VERSION_ID_RE.match(env):
        _version_id_cache = _CacheEntry(env_value=env, resolved=env)
        return env

    for key in ("APP_BUILD", "GITHUB_SHA", "GIT_SHA", "SOURCE_VERSION"):
        raw = os.getenv(key, "").strip()
        if raw:
            resolved = _derive_version_id(raw)
            _version_id_cache = _CacheEntry(env_value=None, resolved=resolved)
            return resolved

    git_sha = _safe_run_git(["rev-parse", "--short=12", "HEAD"])
    if git_sha:
        resolved = f"ver_{git_sha.lower()}"
        _version_id_cache = _CacheEntry(env_value=None, resolved=resolved)
        return resolved

    app_version = os.getenv("APP_VERSION", "").strip() or "unknown"
    resolved = _derive_version_id(app_version)
    _version_id_cache = _CacheEntry(env_value=None, resolved=resolved)
    return resolved


def resolve_corpus_release_id() -> str:
    """
    Resolve the current corpus_release_id.

    Priority:
    1) LS_CORPUS_RELEASE_ID (normalized to cr_*)
    2) git tree hash for data/ at HEAD (fast proxy for corpus snapshot)
    3) APP_VERSION (hashed)
    """
    global _corpus_release_id_cache
    env = os.getenv(CORPUS_RELEASE_ID_ENV, "").strip() or None
    if _corpus_release_id_cache is not None and _corpus_release_id_cache.env_value == env:
        return _corpus_release_id_cache.resolved

    if env and _CORPUS_RELEASE_ID_RE.match(env):
        _corpus_release_id_cache = _CacheEntry(env_value=env, resolved=env)
        return env

    tree = _safe_run_git(["rev-parse", "HEAD:data"])
    if tree:
        resolved = f"cr_{tree[:12].lower()}"
        _corpus_release_id_cache = _CacheEntry(env_value=None, resolved=resolved)
        return resolved

    app_version = os.getenv("APP_VERSION", "").strip() or "unknown"
    resolved = _derive_corpus_release_id(app_version)
    _corpus_release_id_cache = _CacheEntry(env_value=None, resolved=resolved)
    return resolved


def validate_version_id_or_raise(version_id: Optional[str]) -> str:
    if not version_id or not str(version_id).strip():
        raise VersioningError("MISSING_VERSION_ID", "version_id is required", value=version_id)
    raw = str(version_id).strip()
    if not _VERSION_ID_RE.match(raw):
        raise VersioningError("INVALID_VERSION_ID", "version_id is invalid", value=version_id)
    return raw


def validate_corpus_release_id_or_raise(corpus_release_id: Optional[str]) -> str:
    if not corpus_release_id or not str(corpus_release_id).strip():
        raise VersioningError("VALIDATION_FAILED", "corpus_release_id is required", value=corpus_release_id)
    raw = str(corpus_release_id).strip()
    if not _CORPUS_RELEASE_ID_RE.match(raw):
        raise VersioningError("VALIDATION_FAILED", "corpus_release_id is invalid", value=corpus_release_id)
    return raw
