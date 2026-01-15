"""
Engine ID Governance

Runtime validation helpers for engine_id:
- Presence (MISSING_ENGINE_ID)
- Format (INVALID_ENGINE_ID)
- Registry membership (ENGINE_ID_NOT_FOUND)

This module is intentionally small and dependency-light so it can be used in:
- pipeline
- rule engine
- fusion
- narrative
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional, Sequence

from backend.core.engines.constraints import validate_engine_id as validate_engine_id_format
from backend.core.engines.manager import EngineManager

logger = logging.getLogger(__name__)


class EngineIdGovernanceError(ValueError):
    """Deterministic engine_id validation error."""

    def __init__(
        self,
        code: str,
        message: str,
        *,
        engine_id: Optional[str] = None,
    ):
        super().__init__(message)
        self.code = code
        self.engine_id = engine_id
        self.message = message


@dataclass(frozen=True)
class EngineIdValidation:
    engine_id: str


_manager: Optional[EngineManager] = None


def get_engine_manager() -> EngineManager:
    global _manager
    if _manager is None:
        _manager = EngineManager()
    return _manager


def validate_engine_id_or_raise(
    engine_id: Optional[str],
    *,
    manager: Optional[EngineManager] = None,
) -> EngineIdValidation:
    if not engine_id:
        raise EngineIdGovernanceError(
            "MISSING_ENGINE_ID",
            "engine_id is required",
            engine_id=engine_id,
        )

    fmt_error = validate_engine_id_format(engine_id)
    if fmt_error:
        raise EngineIdGovernanceError(
            "INVALID_ENGINE_ID",
            fmt_error,
            engine_id=engine_id,
        )

    registry = manager or get_engine_manager()
    if not registry.validate_engine_id(engine_id):
        raise EngineIdGovernanceError(
            "ENGINE_ID_NOT_FOUND",
            f"engine_id '{engine_id}' not found in registry",
            engine_id=engine_id,
        )

    return EngineIdValidation(engine_id=engine_id)


def validate_engine_ids_or_raise(
    engine_ids: Optional[Sequence[str]],
    *,
    manager: Optional[EngineManager] = None,
) -> Optional[list[str]]:
    if engine_ids is None:
        return None

    validated: list[str] = []
    for engine_id in engine_ids:
        validated.append(validate_engine_id_or_raise(engine_id, manager=manager).engine_id)
    return validated

