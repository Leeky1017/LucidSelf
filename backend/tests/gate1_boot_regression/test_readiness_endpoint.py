from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.routes.health import router as health_router


def test_ready_reflects_boot_checks_and_emits_startup_checks(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ENV", "production")
    monkeypatch.delenv("REDIS_URL", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("AUDIT_LOG_DIR", str(tmp_path))

    import backend.db.session as db_session

    class _FailingConn:
        async def __aenter__(self):
            raise RuntimeError("db down")

        async def __aexit__(self, *args):
            return False

    class _FailingEngine:
        def connect(self):
            return _FailingConn()

    monkeypatch.setattr(db_session, "engine", _FailingEngine())

    app = FastAPI()
    app.include_router(health_router)
    client = TestClient(app)

    resp = client.get("/ready")
    assert resp.status_code == 503
    body = resp.json()

    assert body["ready"] is False
    assert isinstance(body.get("version_id"), str) and body["version_id"].startswith("ver_")
    assert isinstance(body.get("corpus_release_id"), str) and body["corpus_release_id"].startswith("cr_")

    assert "startup_checks" in body
    startup = {c["check_id"]: c for c in body["startup_checks"]}
    assert startup["db_connectivity"]["status"] == "FAIL"

    audit_path = tmp_path / "observability-slos.ndjson"
    assert audit_path.exists()
    first = json.loads(audit_path.read_text(encoding="utf-8").splitlines()[0])
    assert first["result"] == "BLOCK"

