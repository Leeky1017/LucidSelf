import json
import logging
import os
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.middleware.metrics import MetricsMiddleware
from backend.api.middleware.request_logging import RequestLoggingMiddleware
from backend.api.routes.health import router as health_router
from backend.api.routes.metrics import router as metrics_router
from backend.api.routes.auth import router as auth_router
from backend.core.audit import export_audit_log
from backend.core.observability.context import bind_context, reset_context
from backend.core.observability.logging import log_event
from backend.core.observability.tracing import bind_trace_id, reset_trace_id
from backend.services.auth.service import get_auth_service


def test_log_event_includes_required_fields_and_redacts(caplog: pytest.LogCaptureFixture):
    trace_token = bind_trace_id("trace_test_123")
    ctx_tokens = bind_context(
        request_id="req_test_123",
        user_id="user_test",
        org_id="org_test",
        engine_id="cross-system-fusion",
        version_id="1.2.3",
    )
    try:
        with caplog.at_level(logging.INFO):
            payload = log_event(
                logging.getLogger("test"),
                logging.INFO,
                "test_event",
                email="alice@example.com",
                token="sk-abc123",
            )
    finally:
        reset_context(ctx_tokens)
        reset_trace_id(trace_token)

    # Unified correlation keys (may be null in other contexts, but must exist).
    for k in ("request_id", "trace_id", "user_id", "org_id", "engine_id", "version_id"):
        assert k in payload

    # PII/secrets should not be present in the emitted log line.
    assert "alice@example.com" not in caplog.text
    assert "sk-abc123" not in caplog.text


def test_metrics_endpoint_exports_core_metrics():
    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    app.add_middleware(MetricsMiddleware)
    app.include_router(metrics_router)

    @app.get("/ping")
    async def ping():
        return {"ok": True}

    client = TestClient(app)
    assert client.get("/ping").status_code == 200

    resp = client.get("/metrics")
    assert resp.status_code == 200
    body = resp.text

    assert "ls_requests_total" in body
    assert "ls_request_duration_ms" in body
    assert 'endpoint="/ping"' in body
    assert 'method="GET"' in body


def test_ready_blocks_and_writes_audit(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ENV", "production")
    monkeypatch.delenv("REDIS_URL", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("AUDIT_LOG_DIR", str(tmp_path))

    # Force DB check to fail quickly without making real network calls.
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
    app.add_middleware(RequestLoggingMiddleware)
    app.include_router(health_router)
    client = TestClient(app)

    resp = client.get("/ready")
    assert resp.status_code == 503
    body = resp.json()
    assert body["ready"] is False
    assert body["checks"]["db"]["required"] is True
    assert body["checks"]["db"]["ok"] is False
    assert body["checks"]["redis"]["required"] is True
    assert body["checks"]["llm_provider"]["required"] is True

    audit_path = tmp_path / "observability-slos.ndjson"
    assert audit_path.exists()
    first = json.loads(audit_path.read_text(encoding="utf-8").splitlines()[0])
    for field in ("audit_id", "created_at", "event_type", "result"):
        assert field in first
    assert first["result"] == "BLOCK"


def test_auth_login_failure_writes_security_audit_and_no_email_in_logs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
):
    monkeypatch.setenv("AUDIT_LOG_DIR", str(tmp_path))

    class FakeAuthService:
        async def email_login(self, email: str, password: str, ip_address: str | None = None):
            raise ValueError("邮箱或密码错误")

    app = FastAPI()
    app.dependency_overrides[get_auth_service] = lambda: FakeAuthService()
    app.add_middleware(RequestLoggingMiddleware)
    app.include_router(auth_router, prefix="/api/v1")

    client = TestClient(app)

    with caplog.at_level(logging.INFO):
        resp = client.post(
            "/api/v1/auth/email/login",
            json={"email": "alice@example.com", "password": "wrong-password"},
        )

    assert resp.status_code == 401
    assert "alice@example.com" not in caplog.text

    audit_path = tmp_path / "security-privacy-compliance.ndjson"
    assert audit_path.exists()

    # Validate export function (NDJSON + required fields).
    out_lines: list[str] = []

    class _Collector:
        def write(self, s: str) -> int:
            out_lines.append(s)
            return len(s)

    export_audit_log(capability="security-privacy-compliance", output=_Collector(), validate=True)
    assert out_lines

