"""
Playbook Cache

两层缓存实现：Memory -> Redis

技术栈：PostgreSQL + MongoDB + Redis
- Memory: 快速访问层，进程内缓存 (5分钟TTL)
- Redis: 持久化层，服务重启后数据不丢失

注意：不使用 SQLite，所有持久化走 Redis/PostgreSQL/MongoDB
"""

import json
import logging
import os
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Generic, Optional, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


def get_redis_url() -> str:
    """获取 Redis URL（延迟读取，确保 .env 已加载）"""
    return os.getenv("REDIS_URL", "redis://localhost:6379/0")


@dataclass
class CacheEntry(Generic[T]):
    """缓存条目"""
    value: T
    created_at: float
    ttl: float  # 秒
    
    @property
    def is_expired(self) -> bool:
        """是否过期"""
        return time.time() > self.created_at + self.ttl


class MemoryCache(Generic[T]):
    """
    内存缓存 (L1)
    
    最快但容量有限，进程重启后丢失。
    """
    
    DEFAULT_TTL = 300  # 5 分钟
    MAX_SIZE = 1000
    
    def __init__(self, ttl: float = DEFAULT_TTL, max_size: int = MAX_SIZE):
        self.ttl = ttl
        self.max_size = max_size
        self._cache: Dict[str, CacheEntry[T]] = {}
    
    def get(self, key: str) -> Optional[T]:
        """获取缓存"""
        entry = self._cache.get(key)
        if entry is None:
            return None
        if entry.is_expired:
            del self._cache[key]
            return None
        return entry.value
    
    def set(self, key: str, value: T, ttl: Optional[float] = None) -> None:
        """设置缓存"""
        # 检查容量
        if len(self._cache) >= self.max_size:
            self._evict()
        
        self._cache[key] = CacheEntry(
            value=value,
            created_at=time.time(),
            ttl=ttl or self.ttl,
        )
    
    def delete(self, key: str) -> bool:
        """删除缓存"""
        if key in self._cache:
            del self._cache[key]
            return True
        return False
    
    def clear(self) -> None:
        """清空缓存"""
        self._cache.clear()
    
    def _evict(self) -> None:
        """驱逐过期或最旧的条目"""
        now = time.time()
        
        # 先删除过期的
        expired_keys = [
            k for k, v in self._cache.items()
            if v.is_expired
        ]
        for key in expired_keys:
            del self._cache[key]
        
        # 如果还是超过容量，删除最旧的
        if len(self._cache) >= self.max_size:
            oldest_key = min(
                self._cache.keys(),
                key=lambda k: self._cache[k].created_at,
            )
            del self._cache[oldest_key]


class RedisCache:
    """
    Redis 持久化缓存层
    
    用于跨服务重启保持缓存数据。
    """
    
    _client = None
    
    @classmethod
    def get_client(cls):
        """获取 Redis 客户端（延迟初始化）"""
        if cls._client is None:
            try:
                import redis
                redis_url = get_redis_url()
                cls._client = redis.from_url(redis_url, decode_responses=True)
                # 测试连接
                cls._client.ping()
                logger.info(f"Redis connection established: {redis_url.split('@')[-1] if '@' in redis_url else redis_url}")
            except Exception as e:
                logger.warning(f"Redis connection failed: {e}, falling back to memory-only cache")
                cls._client = None
        return cls._client
    
    @classmethod
    def get(cls, key: str) -> Optional[Any]:
        """从 Redis 获取缓存"""
        client = cls.get_client()
        if client is None:
            return None
        
        try:
            value = client.get(key)
            if value:
                return json.loads(value)
        except Exception as e:
            logger.warning(f"Redis get failed: {e}")
        return None
    
    @classmethod
    def set(cls, key: str, value: Any, ttl: int) -> bool:
        """写入 Redis 缓存"""
        client = cls.get_client()
        if client is None:
            return False
        
        try:
            client.setex(key, ttl, json.dumps(value, ensure_ascii=False))
            return True
        except Exception as e:
            logger.warning(f"Redis set failed: {e}")
            return False
    
    @classmethod
    def delete(cls, key: str) -> bool:
        """删除 Redis 缓存"""
        client = cls.get_client()
        if client is None:
            return False
        
        try:
            client.delete(key)
            return True
        except Exception as e:
            logger.warning(f"Redis delete failed: {e}")
            return False


class PlaybookCache:
    """
    Playbook 两层缓存
    
    层级:
    - L1: Memory (快，容量小，5分钟过期)
    - L2: Redis (持久化，服务重启后数据保留)
    """
    
    # 不同类型的 TTL (秒)
    TTL_CONFIG = {
        "day": 3600 * 24,      # 24 小时
        "week": 3600 * 24 * 7, # 7 天
        "month": 3600 * 24 * 31, # 31 天
        "year": 3600 * 24 * 365, # 365 天
    }
    
    def __init__(self, memory_ttl: float = 300):
        """
        初始化缓存
        
        Args:
            memory_ttl: 内存缓存 TTL（秒）
        """
        self._l1 = MemoryCache[Any](ttl=memory_ttl)
    
    def get(self, key: str) -> Optional[Any]:
        """
        获取缓存 (L1 -> L2)
        
        Args:
            key: 缓存键
            
        Returns:
            缓存值或 None
        """
        # L1: Memory
        value = self._l1.get(key)
        if value is not None:
            logger.debug("Cache hit L1 (memory): %s", key)
            return value
        
        # L2: Redis
        value = RedisCache.get(key)
        if value is not None:
            logger.info("Cache hit L2 (redis): %s", key)
            # 回填 L1
            self._l1.set(key, value, ttl=300)
            return value
        
        logger.debug("Cache miss: %s", key)
        return None
    
    def set(
        self,
        key: str,
        value: Any,
        playbook_type: str = "day",
    ) -> None:
        """
        设置缓存 (写入所有层)
        
        Args:
            key: 缓存键
            value: 缓存值
            playbook_type: Playbook 类型 (用于确定 TTL)
        """
        ttl = self.TTL_CONFIG.get(playbook_type, 3600 * 24)
        
        # L1: Memory (最长 5 分钟)
        self._l1.set(key, value, ttl=min(ttl, 300))
        
        # L2: Redis (完整 TTL)
        if RedisCache.set(key, value, ttl):
            logger.info("Cache set to Redis: %s (ttl=%ds)", key, ttl)
        
        # L3: DB (TODO)
        # if self._db:
        #     self._db.set(key, value, ttl)
        
        logger.debug("Cache set: %s (type=%s)", key, playbook_type)
    
    def invalidate(self, key: str) -> None:
        """
        使缓存失效
        
        Args:
            key: 缓存键
        """
        self._l1.delete(key)
        RedisCache.delete(key)
        
        logger.debug("Cache invalidated: %s", key)
    
    def invalidate_user(self, user_id: str) -> int:
        """
        使用户所有缓存失效
        
        Args:
            user_id: 用户 ID
            
        Returns:
            删除的条目数
        """
        # L1: 遍历内存缓存删除
        keys_to_delete = [
            k for k in list(self._l1._cache.keys())
            if k.startswith(f"playbook:{user_id}:")
        ]
        
        for key in keys_to_delete:
            self._l1.delete(key)
            RedisCache.delete(key)
        
        return len(keys_to_delete)
    
    @staticmethod
    def make_key(user_id: str, playbook_type: str, date: str) -> str:
        """
        生成缓存键
        
        Args:
            user_id: 用户 ID
            playbook_type: Playbook 类型
            date: 日期 (YYYY-MM-DD 或 YYYY-Wxx)
            
        Returns:
            缓存键
        """
        return f"playbook:{user_id}:{playbook_type}:{date}"
