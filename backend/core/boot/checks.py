"""
Boot Checks

Defines the "bootability" hard conditions and a shared implementation used by:
- app startup (fail-fast in strict mode)
- /ready endpoint (reflect real readiness)
"""

from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from sqlalchemy import text

from backend.core.versioning.ids import (
    CORPUS_RELEASE_ID_ENV,
    VERSION_ID_ENV,
    validate_corpus_release_id_or_raise,
    validate_version_id_or_raise,
)
from backend.core.versioning.models import StartupCheckItem


@dataclass(frozen=True)
class BootRequirements:
    env: str
    require_db: bool
    require_redis: bool
    require_llm: bool
    require_migrations: bool
    strict_boot: bool


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() == "true"


def get_boot_requirements() -> BootRequirements:
    env = os.getenv("ENV", "dev").strip().lower() or "dev"

    require_db_default = env == "production"
    require_redis_default = env == "production"
    require_llm_default = env == "production" or os.getenv("USE_REAL_PIPELINE", "false").strip().lower() == "true"

    require_db = _env_bool("REQUIRE_DB", require_db_default)
    require_redis = _env_bool("REQUIRE_REDIS", require_redis_default)
    require_llm = _env_bool("REQUIRE_LLM", require_llm_default)

    require_migrations_default = env == "production"
    require_migrations = _env_bool("REQUIRE_MIGRATIONS", require_migrations_default)

    strict_boot_default = env == "production"
    strict_boot = _env_bool("STRICT_BOOT", strict_boot_default)

    return BootRequirements(
        env=env,
        require_db=require_db,
        require_redis=require_redis,
        require_llm=require_llm,
        require_migrations=require_migrations,
        strict_boot=strict_boot,
    )


def _startup_check(
    *,
    check_id: str,
    name: str,
    required: bool,
    ok: bool,
    reason_code: Optional[str] = None,
) -> StartupCheckItem:
    return StartupCheckItem(
        check_id=check_id,
        name=name,
        required=required,
        status="PASS" if ok else ("SKIP" if not required else "FAIL"),
        reason_code=reason_code if (required and not ok) else None,
    )


def _alembic_heads() -> list[str]:
    try:
        from alembic.config import Config
        from alembic.script import ScriptDirectory

        project_root = Path(__file__).resolve().parents[3]
        alembic_ini = project_root / "backend" / "alembic.ini"
        cfg = Config(str(alembic_ini))
        script = ScriptDirectory.from_config(cfg)
        return list(script.get_heads())
    except Exception:
        return []


async def _check_db(engine) -> Tuple[bool, Optional[str]]:
    try:
        async with asyncio.timeout(1.5):
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
        return True, None
    except Exception as e:
        return False, type(e).__name__


async def _check_migrations(engine) -> Tuple[bool, Optional[str], Optional[str], list[str]]:
    """
    Returns: (ok, error_type, current_revision, expected_heads)
    """
    expected_heads = _alembic_heads()
    try:
        async with asyncio.timeout(1.5):
            async with engine.connect() as conn:
                res = await conn.execute(text("SELECT version_num FROM alembic_version"))
                current = res.scalar_one()
        ok = (not expected_heads) or (current in expected_heads)
        return ok, None if ok else "MISMATCH", str(current), expected_heads
    except Exception as e:
        return False, type(e).__name__, None, expected_heads


async def run_boot_checks(
    *,
    requirements: Optional[BootRequirements] = None,
    engine_override: Any = None,
) -> tuple[bool, Dict[str, Any], list[StartupCheckItem]]:
    req = requirements or get_boot_requirements()

    # --- Versioning config (hard invalid env should fail) ---
    versioning_ok = True
    versioning_error: Optional[str] = None
    try:
        raw_vid = os.getenv(VERSION_ID_ENV, "").strip()
        if raw_vid:
            validate_version_id_or_raise(raw_vid)
        raw_cr = os.getenv(CORPUS_RELEASE_ID_ENV, "").strip()
        if raw_cr:
            validate_corpus_release_id_or_raise(raw_cr)
    except Exception as e:
        versioning_ok = False
        versioning_error = type(e).__name__

    checks: Dict[str, Any] = {}
    startup_items: list[StartupCheckItem] = []

    checks["versioning"] = {
        "ok": versioning_ok,
        "required": True,
        "error_type": versioning_error,
    }
    startup_items.append(
        _startup_check(
            check_id="versioning_config",
            name="Versioning config (version_id/corpus_release_id)",
            required=True,
            ok=versioning_ok,
            reason_code="STARTUP_CHECK_FAILED",
        )
    )

    # Resolve engine lazily to support tests.
    engine = engine_override
    if engine is None:
        try:
            from backend.db.session import engine as default_engine

            engine = default_engine
        except Exception:
            engine = None

    # --- DB connectivity ---
    db_ok = False
    db_error = None
    if engine is not None:
        db_ok, db_error = await _check_db(engine)
    checks["db"] = {"ok": db_ok, "required": req.require_db, "error_type": db_error}
    startup_items.append(
        _startup_check(
            check_id="db_connectivity",
            name="Database connectivity",
            required=req.require_db,
            ok=db_ok,
            reason_code="STARTUP_CHECK_FAILED",
        )
    )

    # --- Migrations ---
    migrations_ok = False
    migrations_error = None
    current_revision = None
    expected_heads: list[str] = []
    if req.require_migrations and req.require_db and engine is not None and db_ok:
        migrations_ok, migrations_error, current_revision, expected_heads = await _check_migrations(engine)
    else:
        migrations_ok = not (req.require_migrations and req.require_db)
    checks["migrations"] = {
        "ok": migrations_ok,
        "required": req.require_migrations and req.require_db,
        "current_revision": current_revision,
        "expected_heads": expected_heads,
        "error_type": migrations_error,
    }
    startup_items.append(
        _startup_check(
            check_id="db_migrations",
            name="Database migrations (alembic head)",
            required=req.require_migrations and req.require_db,
            ok=migrations_ok,
            reason_code="STARTUP_CHECK_FAILED",
        )
    )

    # --- Redis ---
    redis_url = os.getenv("REDIS_URL", "").strip()
    redis_configured = bool(redis_url)
    redis_ok = False
    redis_error: Optional[str] = None
    if req.require_redis:
        if not redis_configured:
            redis_ok = False
        else:
            try:
                import redis.asyncio as aioredis

                async with asyncio.timeout(1.0):
                    client = aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)
                    try:
                        await client.ping()
                        redis_ok = True
                    finally:
                        await client.close()
            except Exception as e:
                redis_error = type(e).__name__
    else:
        redis_ok = True

    checks["redis"] = {
        "ok": redis_ok,
        "required": req.require_redis,
        "configured": redis_configured,
        "error_type": redis_error,
    }
    startup_items.append(
        _startup_check(
            check_id="redis_connectivity",
            name="Redis connectivity",
            required=req.require_redis,
            ok=redis_ok,
            reason_code="STARTUP_CHECK_FAILED",
        )
    )

    # --- LLM provider config ---
    llm_key = os.getenv("OPENAI_API_KEY", "").strip()
    llm_ok = bool(llm_key)
    checks["llm_provider"] = {
        "ok": llm_ok,
        "required": req.require_llm,
        "configured": bool(llm_key),
    }
    startup_items.append(
        _startup_check(
            check_id="llm_provider_config",
            name="LLM provider config",
            required=req.require_llm,
            ok=llm_ok,
            reason_code="STARTUP_CHECK_FAILED",
        )
    )

    ready = True
    for name, status in checks.items():
        if status.get("required") and not status.get("ok"):
            ready = False

    return ready, checks, startup_items

