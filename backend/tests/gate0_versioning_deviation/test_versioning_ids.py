import logging
import re

import pytest

from backend.core.audit import create_audit_event
from backend.core.observability.logging import log_event
from backend.core.versioning.ids import (
    CORPUS_RELEASE_ID_ENV,
    VERSION_ID_ENV,
    VersioningError,
    clear_versioning_caches,
    resolve_corpus_release_id,
    resolve_version_id,
    validate_corpus_release_id_or_raise,
    validate_version_id_or_raise,
)
from backend.core.versioning.artifacts import write_version_manifest
from backend.core.versioning.models import VersionManifestEntry


_VER_RE = re.compile(r"^ver_[a-z0-9]{12,}$")
_CR_RE = re.compile(r"^cr_[a-z0-9]{12,}$")


def test_resolve_version_id_and_corpus_release_id_from_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(VERSION_ID_ENV, "ver_aaaaaaaaaaaa")
    monkeypatch.setenv(CORPUS_RELEASE_ID_ENV, "cr_bbbbbbbbbbbb")
    clear_versioning_caches()

    assert resolve_version_id() == "ver_aaaaaaaaaaaa"
    assert resolve_corpus_release_id() == "cr_bbbbbbbbbbbb"


def test_resolve_version_id_and_corpus_release_id_are_normalized(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(VERSION_ID_ENV, raising=False)
    monkeypatch.delenv(CORPUS_RELEASE_ID_ENV, raising=False)
    clear_versioning_caches()

    assert _VER_RE.match(resolve_version_id())
    assert _CR_RE.match(resolve_corpus_release_id())


def test_validate_version_id_missing_is_deterministic():
    with pytest.raises(VersioningError) as exc:
        validate_version_id_or_raise(None)
    assert exc.value.code == "MISSING_VERSION_ID"


def test_validate_version_id_invalid_is_deterministic():
    with pytest.raises(VersioningError) as exc:
        validate_version_id_or_raise("1.0.0")
    assert exc.value.code == "INVALID_VERSION_ID"


def test_validate_version_id_accepts_ver_format():
    assert validate_version_id_or_raise("ver_aaaaaaaaaaaa") == "ver_aaaaaaaaaaaa"


def test_validate_corpus_release_id_rejects_invalid():
    with pytest.raises(VersioningError) as exc:
        validate_corpus_release_id_or_raise("not-a-cr-id")
    assert exc.value.code == "VALIDATION_FAILED"


def test_log_event_defaults_include_versioning_fields(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(VERSION_ID_ENV, "ver_aaaaaaaaaaaa")
    monkeypatch.setenv(CORPUS_RELEASE_ID_ENV, "cr_bbbbbbbbbbbb")
    clear_versioning_caches()

    payload = log_event(logging.getLogger("test"), logging.INFO, "versioning_test_event")
    assert payload["version_id"] == "ver_aaaaaaaaaaaa"
    assert payload["corpus_release_id"] == "cr_bbbbbbbbbbbb"


def test_audit_event_defaults_include_versioning_fields(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(VERSION_ID_ENV, "ver_aaaaaaaaaaaa")
    monkeypatch.setenv(CORPUS_RELEASE_ID_ENV, "cr_bbbbbbbbbbbb")
    clear_versioning_caches()

    event = create_audit_event(
        event_type="TEST",
        result="ALLOW",
        capability="security-privacy-compliance",
    )
    assert event.version_id == "ver_aaaaaaaaaaaa"
    assert event.corpus_release_id == "cr_bbbbbbbbbbbb"


def test_version_manifest_artifact_is_machine_readable(tmp_path):
    path = write_version_manifest(
        [
            VersionManifestEntry(
                version_id="ver_aaaaaaaaaaaa",
                engine_id="bazi-calculator",
                status="ACTIVE",
                notes="test",
            )
        ],
        tmp_path / "version_manifest.json",
    )

    content = path.read_text(encoding="utf-8")
    assert '"version_id": "ver_aaaaaaaaaaaa"' in content
    assert '"engine_id": "bazi-calculator"' in content
