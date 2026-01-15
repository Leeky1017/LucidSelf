"""
Semantic Cache

语义缓存层。

对照架构文档:
- docs/ls_engine_architecture_v3.md §6.3 三层缓存策略
"""

from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from backend.semantics.core.base import SemanticEntry

logger = logging.getLogger(__name__)


@dataclass
class CacheStats:
    """缓存统计"""
    hits: int = 0
    misses: int = 0
    size: int = 0
    evictions: int = 0
    
    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0


@dataclass
class CacheEntry:
    """缓存条目"""
    key: str
    value: Any
    created_at: float = field(default_factory=time.time)
    accessed_at: float = field(default_factory=time.time)
    ttl: float = 300.0  # 5 minutes default


class SemanticCache:
    """
    语义缓存
    
    实现LRU+TTL缓存策略。
    
    对照架构v3 §6.3:
    - 缓存热点语义条目
    - 支持TTL过期
    - LRU淘汰策略
    """
    
    def __init__(
        self,
        max_size: int = 1000,
        default_ttl: float = 300.0,
    ):
        """
        初始化缓存
        
        Args:
            max_size: 最大缓存条目数
            default_ttl: 默认TTL（秒）
        """
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._cache: Dict[str, CacheEntry] = {}
        self._stats = CacheStats()
    
    def get(self, key: str) -> Optional[Any]:
        """
        获取缓存值
        
        Args:
            key: 缓存键
            
        Returns:
            缓存值，不存在或过期返回None
        """
        entry = self._cache.get(key)
        
        if entry is None:
            self._stats.misses += 1
            return None
        
        # 检查TTL
        if time.time() - entry.created_at > entry.ttl:
            del self._cache[key]
            self._stats.misses += 1
            return None
        
        # 更新访问时间
        entry.accessed_at = time.time()
        self._stats.hits += 1
        return entry.value
    
    def set(
        self,
        key: str,
        value: Any,
        ttl: Optional[float] = None,
    ) -> None:
        """
        设置缓存值
        
        Args:
            key: 缓存键
            value: 缓存值
            ttl: TTL（秒），None使用默认值
        """
        # LRU淘汰
        if len(self._cache) >= self.max_size and key not in self._cache:
            self._evict_lru()
        
        self._cache[key] = CacheEntry(
            key=key,
            value=value,
            ttl=ttl or self.default_ttl,
        )
        self._stats.size = len(self._cache)
    
    def _evict_lru(self) -> None:
        """淘汰最久未使用的条目"""
        if not self._cache:
            return
        
        # 找到最久未访问的条目
        oldest_key = min(
            self._cache.keys(),
            key=lambda k: self._cache[k].accessed_at
        )
        del self._cache[oldest_key]
        self._stats.evictions += 1
    
    def invalidate(self, key: str) -> bool:
        """
        失效指定缓存
        
        Args:
            key: 缓存键
            
        Returns:
            是否成功删除
        """
        if key in self._cache:
            del self._cache[key]
            self._stats.size = len(self._cache)
            return True
        return False
    
    def invalidate_by_prefix(self, prefix: str) -> int:
        """
        按前缀失效缓存
        
        Args:
            prefix: 键前缀
            
        Returns:
            删除的条目数
        """
        keys_to_delete = [k for k in self._cache if k.startswith(prefix)]
        for k in keys_to_delete:
            del self._cache[k]
        self._stats.size = len(self._cache)
        return len(keys_to_delete)
    
    def clear(self) -> None:
        """清空缓存"""
        self._cache.clear()
        self._stats.size = 0
    
    def get_stats(self) -> CacheStats:
        """获取缓存统计"""
        self._stats.size = len(self._cache)
        return self._stats
    
    @staticmethod
    def make_key(*args) -> str:
        """
        生成缓存键
        
        Args:
            *args: 键组成部分
            
        Returns:
            哈希后的缓存键
        """
        content = ":".join(str(a) for a in args)
        return hashlib.md5(content.encode()).hexdigest()
