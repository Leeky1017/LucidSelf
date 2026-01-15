"""
Semantic Cache

语义条目缓存。

对照 design.md §6.1 三层缓存架构
对照 Requirements R-6-6-01, R-6-6-04, R-6-6-05
"""

from __future__ import annotations

import threading
import time
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Generic, Optional, TypeVar

from backend.core.observability.metrics import (
    CACHE_HIT_COUNTER,
    CACHE_MISS_COUNTER,
    CACHE_SIZE_GAUGE,
    CACHE_HIT_RATIO,
)

T = TypeVar("T")


@dataclass
class CacheStats:
    """缓存统计"""
    hits: int = 0
    misses: int = 0
    evictions: int = 0
    size: int = 0
    
    @property
    def total_requests(self) -> int:
        return self.hits + self.misses
    
    @property
    def hit_ratio(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return self.hits / self.total_requests
    
    def record_hit(self):
        self.hits += 1
    
    def record_miss(self):
        self.misses += 1
    
    def record_eviction(self):
        self.evictions += 1


@dataclass
class CacheEntry(Generic[T]):
    """缓存条目"""
    value: T
    created_at: float = field(default_factory=time.time)
    last_accessed: float = field(default_factory=time.time)
    ttl_seconds: Optional[float] = None
    
    def is_expired(self) -> bool:
        if self.ttl_seconds is None:
            return False
        return (time.time() - self.created_at) > self.ttl_seconds
    
    def touch(self):
        self.last_accessed = time.time()


class SemanticCache(Generic[T]):
    """
    语义条目缓存
    
    对照 R-6-6-01, R-6-6-04, R-6-6-05
    
    特性：
    - LRU 淘汰策略
    - TTL 过期策略
    - 线程安全
    - 可观测指标
    """
    
    def __init__(
        self,
        max_size: int = 10000,
        ttl_seconds: Optional[float] = 3600,
        cache_type: str = "semantic",
    ):
        """
        初始化语义缓存
        
        Args:
            max_size: 最大缓存条目数
            ttl_seconds: TTL 秒数 (None 表示永不过期)
            cache_type: 缓存类型 (用于指标标签)
        """
        self._max_size = max_size
        self._ttl_seconds = ttl_seconds
        self._cache_type = cache_type
        
        self._cache: OrderedDict[str, CacheEntry[T]] = OrderedDict()
        self._lock = threading.RLock()
        self._stats = CacheStats()
    
    @property
    def stats(self) -> CacheStats:
        """获取缓存统计"""
        self._stats.size = len(self._cache)
        return self._stats
    
    def get(self, key: str) -> Optional[T]:
        """
        获取缓存条目
        
        Args:
            key: 缓存键
            
        Returns:
            缓存值，如不存在或已过期则返回 None
        """
        with self._lock:
            if key not in self._cache:
                self._record_miss()
                return None
            
            entry = self._cache[key]
            
            # 检查 TTL
            if entry.is_expired():
                self._evict(key)
                self._record_miss()
                return None
            
            # LRU: 移到末尾
            self._cache.move_to_end(key)
            entry.touch()
            
            self._record_hit()
            return entry.value
    
    def set(
        self,
        key: str,
        value: T,
        ttl_seconds: Optional[float] = None,
    ) -> None:
        """
        设置缓存条目
        
        Args:
            key: 缓存键
            value: 缓存值
            ttl_seconds: TTL 秒数 (None 使用默认值)
        """
        ttl = ttl_seconds if ttl_seconds is not None else self._ttl_seconds
        
        with self._lock:
            # 如果已存在，更新
            if key in self._cache:
                self._cache[key] = CacheEntry(value=value, ttl_seconds=ttl)
                self._cache.move_to_end(key)
                return
            
            # 检查容量
            while len(self._cache) >= self._max_size:
                self._evict_oldest()
            
            # 添加新条目
            self._cache[key] = CacheEntry(value=value, ttl_seconds=ttl)
    
    def delete(self, key: str) -> bool:
        """
        删除缓存条目
        
        Returns:
            True 如果删除成功
        """
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                return True
            return False
    
    def clear(self) -> int:
        """
        清空缓存
        
        Returns:
            清除的条目数
        """
        with self._lock:
            count = len(self._cache)
            self._cache.clear()
            self._stats = CacheStats()
            return count
    
    def has(self, key: str) -> bool:
        """检查键是否存在（不更新 LRU）"""
        with self._lock:
            if key not in self._cache:
                return False
            entry = self._cache[key]
            if entry.is_expired():
                self._evict(key)
                return False
            return True
    
    def keys(self) -> list[str]:
        """获取所有键"""
        with self._lock:
            return list(self._cache.keys())
    
    def size(self) -> int:
        """获取当前缓存大小"""
        return len(self._cache)
    
    def _evict(self, key: str) -> None:
        """淘汰指定条目"""
        if key in self._cache:
            del self._cache[key]
            self._stats.record_eviction()
    
    def _evict_oldest(self) -> None:
        """淘汰最旧条目 (LRU)"""
        if self._cache:
            oldest_key = next(iter(self._cache))
            self._evict(oldest_key)
    
    def _record_hit(self) -> None:
        """记录命中"""
        self._stats.record_hit()
        CACHE_HIT_COUNTER.labels(cache_type=self._cache_type).inc()
        self._update_metrics()
    
    def _record_miss(self) -> None:
        """记录未命中"""
        self._stats.record_miss()
        CACHE_MISS_COUNTER.labels(cache_type=self._cache_type).inc()
        self._update_metrics()
    
    def _update_metrics(self) -> None:
        """更新指标"""
        CACHE_SIZE_GAUGE.labels(cache_type=self._cache_type).set(len(self._cache))
        CACHE_HIT_RATIO.labels(cache_type=self._cache_type).set(self._stats.hit_ratio)
    
    def cleanup_expired(self) -> int:
        """
        清理过期条目
        
        Returns:
            清理的条目数
        """
        with self._lock:
            expired_keys = [
                k for k, v in self._cache.items()
                if v.is_expired()
            ]
            for key in expired_keys:
                self._evict(key)
            return len(expired_keys)
