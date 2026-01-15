"""
LucidSelf API Layer

FastAPI 应用层。

对照 design.md, tasks.md 5-7
"""

from __future__ import annotations

from typing import Any


def __getattr__(name: str) -> Any:
    if name in {"create_app", "app"}:
        from backend.api.main import app, create_app

        value = create_app if name == "create_app" else app
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ["create_app", "app"]
