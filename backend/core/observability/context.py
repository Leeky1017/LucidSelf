"""
Observability Context

Request-scoped context (contextvars) for correlating logs/metrics/audit.
"""

from __future__ import annotations

from contextvars import ContextVar, Token
from typing import Any, Dict, Optional

_request_id: ContextVar[Optional[str]] = ContextVar("ls_request_id", default=None)
_user_id: ContextVar[Optional[str]] = ContextVar("ls_user_id", default=None)
_org_id: ContextVar[Optional[str]] = ContextVar("ls_org_id", default=None)
_engine_id: ContextVar[Optional[str]] = ContextVar("ls_engine_id", default=None)
_version_id: ContextVar[Optional[str]] = ContextVar("ls_version_id", default=None)
_corpus_release_id: ContextVar[Optional[str]] = ContextVar("ls_corpus_release_id", default=None)


def bind_context(
    *,
    request_id: Optional[str] = None,
    user_id: Optional[str] = None,
    org_id: Optional[str] = None,
    engine_id: Optional[str] = None,
    version_id: Optional[str] = None,
    corpus_release_id: Optional[str] = None,
) -> Dict[str, Token]:
    tokens: Dict[str, Token] = {}
    if request_id is not None:
        tokens["request_id"] = _request_id.set(request_id)
    if user_id is not None:
        tokens["user_id"] = _user_id.set(user_id)
    if org_id is not None:
        tokens["org_id"] = _org_id.set(org_id)
    if engine_id is not None:
        tokens["engine_id"] = _engine_id.set(engine_id)
    if version_id is not None:
        tokens["version_id"] = _version_id.set(version_id)
    if corpus_release_id is not None:
        tokens["corpus_release_id"] = _corpus_release_id.set(corpus_release_id)
    return tokens


def reset_context(tokens: Dict[str, Token]) -> None:
    if (token := tokens.get("request_id")) is not None:
        _request_id.reset(token)
    if (token := tokens.get("user_id")) is not None:
        _user_id.reset(token)
    if (token := tokens.get("org_id")) is not None:
        _org_id.reset(token)
    if (token := tokens.get("engine_id")) is not None:
        _engine_id.reset(token)
    if (token := tokens.get("version_id")) is not None:
        _version_id.reset(token)
    if (token := tokens.get("corpus_release_id")) is not None:
        _corpus_release_id.reset(token)


def get_context() -> Dict[str, Optional[str]]:
    return {
        "request_id": _request_id.get(),
        "user_id": _user_id.get(),
        "org_id": _org_id.get(),
        "engine_id": _engine_id.get(),
        "version_id": _version_id.get(),
        "corpus_release_id": _corpus_release_id.get(),
    }
