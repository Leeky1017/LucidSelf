"""API Routes (lazy exports)

Avoid importing every route module at package import time.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

_ROUTER_EXPORTS: dict[str, tuple[str, str]] = {
    "health_router": ("backend.api.routes.health", "router"),
    "metrics_router": ("backend.api.routes.metrics", "router"),
    "analyze_router": ("backend.api.routes.analyze", "router"),
    "interpret_router": ("backend.api.routes.interpret", "router"),
    "playbook_router": ("backend.api.routes.playbook", "router"),
    "dream_router": ("backend.api.routes.dream", "router"),
    "user_router": ("backend.api.routes.user", "router"),
    "timeline_router": ("backend.api.routes.timeline", "router"),
    "patterns_router": ("backend.api.routes.patterns", "router"),
    "insights_router": ("backend.api.routes.insights", "router"),
    "geocoding_router": ("backend.api.routes.geocoding", "router"),
    "versions_router": ("backend.api.routes.versions", "router"),
    "auth_router": ("backend.api.routes.auth", "router"),
    "todo_router": ("backend.api.routes.todo", "router"),
    "subscription_router": ("backend.api.routes.subscription", "router"),
    "scheduler_router": ("backend.api.routes.scheduler", "router"),
}


def __getattr__(name: str) -> Any:
    export = _ROUTER_EXPORTS.get(name)
    if export is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attr_name = export
    value = getattr(import_module(module_name), attr_name)
    globals()[name] = value
    return value

__all__ = [
    "health_router",
    "metrics_router",
    "analyze_router",
    "interpret_router",
    "playbook_router",
    "dream_router",
    "user_router",
    "timeline_router",
    "patterns_router",
    "insights_router",
    "geocoding_router",
    "versions_router",
    "auth_router",
    "todo_router",
    "subscription_router",
    "scheduler_router",
]
