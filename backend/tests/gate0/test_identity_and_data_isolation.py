from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.routes.auth import get_current_user
from backend.api.routes.dream import get_dream_service, router as dream_router
from backend.core.contracts.auth_models import AuthProvider, UserInfo


@dataclass
class _FakeDB:
    async def commit(self) -> None:
        return None


@dataclass
class _FakeDream:
    id: uuid.UUID
    user_id: str
    status: str = "draft"
    mode: str = "quick"
    raw_input: str = ""
    generated_content: Optional[str] = None
    final_content: str = ""
    title: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    clarity: Optional[int] = None
    tags: list[str] = None  # type: ignore[assignment]
    mood: Optional[str] = None
    generate_count: int = 0


class _FakeDreamService:
    def __init__(self) -> None:
        self.db = _FakeDB()
        self.last_create_args: dict | None = None
        self.last_list_args: dict | None = None

    async def create_dream(self, *, user_id: str, org_id: str, raw_input: str, final_content: str, **kwargs):
        self.last_create_args = {
            "user_id": user_id,
            "org_id": org_id,
            "raw_input": raw_input,
            "final_content": final_content,
            **kwargs,
        }
        return _FakeDream(
            id=uuid.uuid4(),
            user_id=user_id,
            raw_input=raw_input,
            final_content=final_content,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            tags=kwargs.get("tags") or [],
            mood=kwargs.get("mood"),
            title=kwargs.get("title"),
            clarity=kwargs.get("clarity"),
            status=kwargs.get("status", "draft"),
            mode=kwargs.get("mode", "quick"),
        )

    async def list_dreams(self, *, user_id: str, org_id: str, limit: int = 20, offset: int = 0):
        self.last_list_args = {"user_id": user_id, "org_id": org_id, "limit": limit, "offset": offset}
        return [], 0


def _build_app(fake_service: _FakeDreamService, user: UserInfo) -> FastAPI:
    app = FastAPI()
    app.include_router(dream_router, prefix="/api/v1")

    async def _override_user() -> UserInfo:
        return user

    async def _override_dream_service() -> _FakeDreamService:
        return fake_service

    app.dependency_overrides[get_current_user] = _override_user
    app.dependency_overrides[get_dream_service] = _override_dream_service
    return app


def test_dream_create_rejects_client_user_id_mismatch(monkeypatch):
    fake_service = _FakeDreamService()
    user = UserInfo(
        user_id="user_aaaaaaaaaaaa",
        org_id="org_aaaaaaaaaaaa",
        email=None,
        name=None,
        provider=AuthProvider.EMAIL,
        tier="free",
        created_at=datetime.utcnow(),
    )

    # 避免后台任务影响测试
    from backend.api.routes import dream as dream_module
    monkeypatch.setattr(dream_module, "spawn_memory_write", lambda *args, **kwargs: None)

    client = TestClient(_build_app(fake_service, user))
    resp = client.post(
        "/api/v1/dream/entries",
        json={
            "user_id": "user_bbbbbbbbbbbb",
            "rawInput": "raw",
            "finalContent": "final",
        },
    )

    assert resp.status_code == 403
    body = resp.json()
    assert body["detail"]["code"] == "CROSS_TENANT_ACCESS"


def test_dream_create_uses_authenticated_identity(monkeypatch):
    fake_service = _FakeDreamService()
    user = UserInfo(
        user_id="user_aaaaaaaaaaaa",
        org_id="org_aaaaaaaaaaaa",
        email=None,
        name=None,
        provider=AuthProvider.EMAIL,
        tier="free",
        created_at=datetime.utcnow(),
    )

    from backend.api.routes import dream as dream_module
    monkeypatch.setattr(dream_module, "spawn_memory_write", lambda *args, **kwargs: None)

    client = TestClient(_build_app(fake_service, user))
    resp = client.post(
        "/api/v1/dream/entries",
        json={
            "rawInput": "raw",
            "finalContent": "final",
        },
    )

    assert resp.status_code == 200
    assert fake_service.last_create_args is not None
    assert fake_service.last_create_args["user_id"] == user.user_id
    assert fake_service.last_create_args["org_id"] == user.org_id


def test_dream_list_scopes_by_user_and_org(monkeypatch):
    fake_service = _FakeDreamService()
    user = UserInfo(
        user_id="user_aaaaaaaaaaaa",
        org_id="org_aaaaaaaaaaaa",
        email=None,
        name=None,
        provider=AuthProvider.EMAIL,
        tier="free",
        created_at=datetime.utcnow(),
    )

    from backend.api.routes import dream as dream_module
    monkeypatch.setattr(dream_module, "spawn_memory_write", lambda *args, **kwargs: None)

    client = TestClient(_build_app(fake_service, user))
    resp = client.get("/api/v1/dream/entries")

    assert resp.status_code == 200
    assert fake_service.last_list_args == {
        "user_id": user.user_id,
        "org_id": user.org_id,
        "limit": 20,
        "offset": 0,
    }

