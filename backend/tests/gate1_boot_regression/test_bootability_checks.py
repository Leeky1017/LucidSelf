from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from backend.api.main import create_app
from backend.core.boot.checks import BootRequirements, run_boot_checks
from backend.core.versioning.ids import CORPUS_RELEASE_ID_ENV, VERSION_ID_ENV


class _Result:
    def __init__(self, value):
        self._value = value

    def scalar_one(self):
        return self._value


class _Conn:
    def __init__(self, revision: str | None, *, fail_db: bool = False):
        self._revision = revision
        self._fail_db = fail_db

    async def __aenter__(self):
        if self._fail_db:
            raise RuntimeError("db down")
        return self

    async def __aexit__(self, *args):
        return False

    async def execute(self, stmt):
        sql = str(stmt)
        if "SELECT 1" in sql:
            return _Result(1)
        if "SELECT version_num FROM alembic_version" in sql:
            if self._revision is None:
                raise RuntimeError("alembic_version missing")
            return _Result(self._revision)
        raise RuntimeError(f"unexpected sql: {sql}")


class _Engine:
    def __init__(self, revision: str | None, *, fail_db: bool = False):
        self._revision = revision
        self._fail_db = fail_db

    def connect(self):
        return _Conn(self._revision, fail_db=self._fail_db)


@pytest.mark.asyncio
async def test_run_boot_checks_detects_migration_mismatch(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(VERSION_ID_ENV, raising=False)
    monkeypatch.delenv(CORPUS_RELEASE_ID_ENV, raising=False)

    req = BootRequirements(
        env="production",
        require_db=True,
        require_redis=False,
        require_llm=False,
        require_migrations=True,
        strict_boot=False,
    )

    ok, checks, _ = await run_boot_checks(requirements=req, engine_override=_Engine("0000"))
    assert ok is False
    assert checks["db"]["required"] is True
    assert checks["db"]["ok"] is True
    assert checks["migrations"]["required"] is True
    assert checks["migrations"]["ok"] is False


@pytest.mark.asyncio
async def test_run_boot_checks_fails_on_invalid_versioning_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(VERSION_ID_ENV, "bad-version")
    monkeypatch.setenv(CORPUS_RELEASE_ID_ENV, "bad-corpus")

    req = BootRequirements(
        env="dev",
        require_db=False,
        require_redis=False,
        require_llm=False,
        require_migrations=False,
        strict_boot=False,
    )

    ok, checks, _ = await run_boot_checks(requirements=req, engine_override=_Engine("0001"))
    assert ok is False
    assert checks["versioning"]["ok"] is False


def test_strict_boot_blocks_startup(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("STRICT_BOOT", "true")
    monkeypatch.setenv("REQUIRE_DB", "true")
    monkeypatch.setenv("REQUIRE_MIGRATIONS", "false")
    monkeypatch.setenv("REQUIRE_REDIS", "false")
    monkeypatch.setenv("REQUIRE_LLM", "false")

    import backend.db.session as db_session

    db_session.engine = _Engine("0001", fail_db=True)  # type: ignore[assignment]

    app = create_app(debug=True, enable_auth=False, enable_rate_limit=False)
    with pytest.raises(RuntimeError):
        with TestClient(app):
            pass
