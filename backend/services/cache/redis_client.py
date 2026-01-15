# backend/services/cache/redis_client.py
"""
Redis Cache Client

Redis 缓存客户端，支持连接失败降级到内存缓存。

Phase 12 Task 12.2: 实现 Redis 缓存客户端
参考 tasks.md Phase 12 和 requirements.md R11.3-R11.5

缓存键设计:
- user:{uid}:today_context:{date} - 今日上下文 (TTL: 24h)
- user:{uid}:active_insights - 活跃洞察 (TTL: 7d)
- playbook:{uid}:daily:{date} - 日 Playbook (TTL: 25h)
- factors:{uid}:{date} - 因子缓存 (TTL: 25h)
"""

import json
import logging
import os
import re
from datetime import date, datetime, timedelta
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


# R-07: 合法 key 前缀正则模式
VALID_KEY_PATTERNS = [
    re.compile(r"^user:[^:]+:"),           # user:{uid}:*
    re.compile(r"^playbook:[^:]+:"),        # playbook:{uid}:*
    re.compile(r"^session:[^:]+$"),         # session:{sid}
    re.compile(r"^factors:[^:]+:"),         # factors:{uid}:*
]


class InvalidCacheKeyError(Exception):
    """R-07: 非法缓存键异常"""
    pass


def validate_cache_key(key: str) -> None:
    """
    R-07: 验证缓存键是否合法
    
    合法前缀:
    - user:{uid}:*
    - playbook:{uid}:*
    - session:{sid}
    - factors:{uid}:*
    
    Raises:
        InvalidCacheKeyError: 如果 key 不合法
    """
    if not key:
        raise InvalidCacheKeyError("Cache key cannot be empty")
    
    for pattern in VALID_KEY_PATTERNS:
        if pattern.match(key):
            return
    
    raise InvalidCacheKeyError(
        f"Invalid cache key: '{key}'. Must match one of: "
        f"user:{{uid}}:*, playbook:{{uid}}:*, session:{{sid}}, factors:{{uid}}:*"
    )


class RedisCache:
    """
    Redis 缓存客户端
    
    支持:
    - 异步操作
    - 连接失败降级到内存缓存
    - 自动重连
    - 跨日边界降级 (00:00-00:30)
    """
    
    # TTL 常量
    TTL_TODAY_CONTEXT = timedelta(hours=24)
    TTL_ACTIVE_INSIGHTS = timedelta(days=7)
    TTL_DAILY_PLAYBOOK = timedelta(hours=25)
    TTL_FACTORS = timedelta(hours=25)
    TTL_SHORT = timedelta(hours=1)
    
    def __init__(self, redis_url: Optional[str] = None):
        """
        初始化 Redis 缓存
        
        Args:
            redis_url: Redis 连接 URL，为 None 时从环境变量读取
        """
        self._redis_url = redis_url or os.getenv("REDIS_URL", "")
        self._redis = None
        self._connected = False
        
        # 内存降级缓存
        self._memory_cache: Dict[str, tuple] = {}  # key -> (value, expire_at)
        
        if self._redis_url:
            self._init_redis()
        else:
            logger.warning("Redis URL not configured, using memory fallback")
    
    def _init_redis(self) -> None:
        """初始化 Redis 连接"""
        try:
            import redis.asyncio as aioredis
            self._redis = aioredis.from_url(
                self._redis_url,
                encoding="utf-8",
                decode_responses=True,
            )
            self._connected = True
            logger.info(f"Redis cache initialized: {self._redis_url[:30]}...")
        except ImportError:
            logger.warning("redis package not installed, using memory fallback")
            self._connected = False
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            self._connected = False
    
    @property
    def is_connected(self) -> bool:
        """检查 Redis 是否连接"""
        return self._connected and self._redis is not None
    
    # =========================================================================
    # 通用操作
    # =========================================================================
    
    async def get(self, key: str) -> Optional[str]:
        """
        获取缓存值
        
        Args:
            key: 缓存键
            
        Returns:
            缓存值，不存在返回 None
            
        Raises:
            InvalidCacheKeyError: 如果 key 不合法
        """
        # R-07: 运行时校验 key
        validate_cache_key(key)
        
        if self.is_connected:
            try:
                return await self._redis.get(key)
            except Exception as e:
                logger.warning(f"Redis get failed for {key}: {e}")
        
        # 降级到内存缓存
        return self._memory_get(key)
    
    async def set(
        self,
        key: str,
        value: str,
        ttl: Optional[timedelta] = None,
    ) -> bool:
        """
        设置缓存值
        
        Args:
            key: 缓存键
            value: 缓存值
            ttl: 过期时间
            
        Returns:
            是否成功
            
        Raises:
            InvalidCacheKeyError: 如果 key 不合法
        """
        # R-07: 运行时校验 key
        validate_cache_key(key)
        
        if self.is_connected:
            try:
                if ttl:
                    await self._redis.setex(key, int(ttl.total_seconds()), value)
                else:
                    await self._redis.set(key, value)
                return True
            except Exception as e:
                logger.warning(f"Redis set failed for {key}: {e}")
        
        # 降级到内存缓存
        return self._memory_set(key, value, ttl)
    
    async def exists(self, key: str) -> bool:
        """
        检查键是否存在
        
        Raises:
            InvalidCacheKeyError: 如果 key 不合法
        """
        # R-07: 运行时校验 key
        validate_cache_key(key)
        
        if self.is_connected:
            try:
                return await self._redis.exists(key) > 0
            except Exception as e:
                logger.warning(f"Redis exists failed for {key}: {e}")
        
        return self._memory_exists(key)
    
    async def delete(self, key: str) -> bool:
        """
        删除缓存键
        
        Raises:
            InvalidCacheKeyError: 如果 key 不合法
        """
        # R-07: 运行时校验 key
        validate_cache_key(key)
        
        if self.is_connected:
            try:
                await self._redis.delete(key)
                return True
            except Exception as e:
                logger.warning(f"Redis delete failed for {key}: {e}")
        
        return self._memory_delete(key)
    
    # =========================================================================
    # 业务方法
    # =========================================================================
    
    async def get_today_context(self, user_id: str) -> Optional[dict]:
        """
        获取今日上下文
        
        支持跨日边界降级 (00:00-00:30 回退读昨日)
        """
        today = date.today().isoformat()
        key = f"user:{user_id}:today_context:{today}"
        
        ctx = await self.get(key)
        if ctx:
            return json.loads(ctx)
        
        # 跨日降级 (00:00-00:30)
        now = datetime.now()
        if now.hour == 0 and now.minute < 30:
            yesterday = (date.today() - timedelta(days=1)).isoformat()
            key_yesterday = f"user:{user_id}:today_context:{yesterday}"
            ctx = await self.get(key_yesterday)
            if ctx:
                logger.debug(f"Using yesterday's context for user {user_id}")
                return json.loads(ctx)
        
        return None
    
    async def set_today_context(self, user_id: str, context: dict) -> bool:
        """设置今日上下文"""
        today = date.today().isoformat()
        key = f"user:{user_id}:today_context:{today}"
        return await self.set(key, json.dumps(context), self.TTL_TODAY_CONTEXT)
    
    async def get_active_insights(self, user_id: str, dimension: Optional[str] = None) -> Optional[list]:
        """获取活跃洞察"""
        key = f"user:{user_id}:active_insights"
        if dimension:
            key = f"{key}:{dimension}"
        
        data = await self.get(key)
        if data:
            return json.loads(data)
        return None
    
    async def set_active_insights(
        self,
        user_id: str,
        insights: list,
        dimension: Optional[str] = None,
    ) -> bool:
        """设置活跃洞察"""
        key = f"user:{user_id}:active_insights"
        if dimension:
            key = f"{key}:{dimension}"
        return await self.set(key, json.dumps(insights), self.TTL_ACTIVE_INSIGHTS)
    
    async def has_daily_playbook(self, user_id: str, date_str: str) -> bool:
        """检查今日 Playbook 是否已生成"""
        key = f"playbook:{user_id}:daily:{date_str}"
        return await self.exists(key)
    
    async def cache_daily_playbook(self, user_id: str, date_str: str, content: str) -> bool:
        """缓存日 Playbook"""
        key = f"playbook:{user_id}:daily:{date_str}"
        return await self.set(key, content, self.TTL_DAILY_PLAYBOOK)
    
    async def get_cached_factors(self, user_id: str, date_str: str) -> Optional[dict]:
        """获取因子缓存"""
        key = f"factors:{user_id}:{date_str}"
        data = await self.get(key)
        if data:
            return json.loads(data)
        return None
    
    async def cache_factors(self, user_id: str, date_str: str, factors: dict) -> bool:
        """缓存因子数据"""
        key = f"factors:{user_id}:{date_str}"
        return await self.set(key, json.dumps(factors), self.TTL_FACTORS)
    
    # =========================================================================
    # 内存降级缓存
    # =========================================================================
    
    def _memory_get(self, key: str) -> Optional[str]:
        """内存缓存获取"""
        if key in self._memory_cache:
            value, expire_at = self._memory_cache[key]
            if expire_at is None or datetime.now() < expire_at:
                return value
            # 已过期，删除
            del self._memory_cache[key]
        return None
    
    def _memory_set(self, key: str, value: str, ttl: Optional[timedelta] = None) -> bool:
        """内存缓存设置"""
        expire_at = datetime.now() + ttl if ttl else None
        self._memory_cache[key] = (value, expire_at)
        return True
    
    def _memory_exists(self, key: str) -> bool:
        """内存缓存存在检查"""
        return self._memory_get(key) is not None
    
    def _memory_delete(self, key: str) -> bool:
        """内存缓存删除"""
        if key in self._memory_cache:
            del self._memory_cache[key]
            return True
        return False
    
    def _cleanup_expired(self) -> int:
        """清理过期的内存缓存"""
        now = datetime.now()
        expired_keys = [
            k for k, (_, expire_at) in self._memory_cache.items()
            if expire_at and now >= expire_at
        ]
        for k in expired_keys:
            del self._memory_cache[k]
        return len(expired_keys)
    
    async def close(self) -> None:
        """关闭连接"""
        if self._redis:
            await self._redis.close()
            self._connected = False


# =============================================================================
# 便捷函数
# =============================================================================

_cache: Optional[RedisCache] = None


def get_redis_cache() -> RedisCache:
    """获取 Redis 缓存单例"""
    global _cache
    if _cache is None:
        _cache = RedisCache()
    return _cache


def reset_redis_cache() -> None:
    """重置 Redis 缓存（用于测试）"""
    global _cache
    _cache = None
