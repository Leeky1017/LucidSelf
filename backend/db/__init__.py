"""
Database Module

数据库连接和会话管理。
"""

from backend.db.session import (
    get_db,
    engine,
    async_session_maker,
    init_db,
)
from backend.db.base import Base
from backend.db.timescale import (
    init_timescale,
    create_hypertable,
    add_retention_policy,
    enable_compression,
    setup_timescale_for_memory,
    is_timescale_available,
)

__all__ = [
    "get_db",
    "engine",
    "async_session_maker",
    "init_db",
    "Base",
    # TimescaleDB
    "init_timescale",
    "create_hypertable",
    "add_retention_policy",
    "enable_compression",
    "setup_timescale_for_memory",
    "is_timescale_available",
]
