"""
Versioning (version_id + corpus_release_id)

Centralizes runtime identifier resolution for:
- version_id (immutable build/runtime version)
- corpus_release_id (corpus release identifier)
"""

from backend.core.versioning.ids import (
    VersioningError,
    clear_versioning_caches,
    resolve_corpus_release_id,
    resolve_version_id,
    validate_corpus_release_id_or_raise,
    validate_version_id_or_raise,
)

__all__ = [
    "VersioningError",
    "clear_versioning_caches",
    "resolve_corpus_release_id",
    "resolve_version_id",
    "validate_corpus_release_id_or_raise",
    "validate_version_id_or_raise",
]

