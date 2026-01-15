# backend/services/cache/__init__.py
"""
Cache Service

Redis 缓存服务模块。

Phase 12 Task 12.2: 实现 Redis 缓存客户端
"""

from backend.services.cache.redis_client import (
    RedisCache,
    get_redis_cache,
    reset_redis_cache,
)

__all__ = [
    "RedisCache",
    "get_redis_cache",
    "reset_redis_cache",
]
