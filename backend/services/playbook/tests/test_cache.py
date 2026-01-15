"""
Playbook Cache Tests

对照 tasks.md 15.3:
- Requirements: 7.2.1-7.2.3, 8.1.1
"""

import pytest
import time

from backend.services.playbook.cache import (
    MemoryCache,
    CacheEntry,
    PlaybookCache,
)


class TestCacheEntry:
    """CacheEntry 测试"""
    
    def test_not_expired(self):
        """测试未过期"""
        entry = CacheEntry(
            value="test",
            created_at=time.time(),
            ttl=60,
        )
        
        assert entry.is_expired is False
    
    def test_expired(self):
        """测试已过期"""
        entry = CacheEntry(
            value="test",
            created_at=time.time() - 100,
            ttl=60,
        )
        
        assert entry.is_expired is True


class TestMemoryCache:
    """MemoryCache 测试"""
    
    def test_get_set(self):
        """测试基本 get/set"""
        cache = MemoryCache[str]()
        
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"
    
    def test_get_missing(self):
        """测试获取不存在的 key"""
        cache = MemoryCache[str]()
        
        assert cache.get("missing") is None
    
    def test_get_expired(self):
        """测试获取过期的 key"""
        cache = MemoryCache[str](ttl=0.1)
        
        cache.set("key1", "value1")
        time.sleep(0.15)
        
        assert cache.get("key1") is None
    
    def test_delete(self):
        """测试删除"""
        cache = MemoryCache[str]()
        
        cache.set("key1", "value1")
        assert cache.delete("key1") is True
        assert cache.get("key1") is None
    
    def test_clear(self):
        """测试清空"""
        cache = MemoryCache[str]()
        
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.clear()
        
        assert cache.get("key1") is None
        assert cache.get("key2") is None
    
    def test_eviction(self):
        """测试容量驱逐"""
        cache = MemoryCache[str](ttl=60, max_size=3)
        
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")
        cache.set("key4", "value4")  # 触发驱逐
        
        # 至少有一个被驱逐
        present = sum(1 for k in ["key1", "key2", "key3", "key4"] if cache.get(k))
        assert present <= 3


class TestPlaybookCache:
    """PlaybookCache 测试"""
    
    def test_get_set(self):
        """测试基本 get/set"""
        cache = PlaybookCache()
        
        cache.set("test_key", {"data": "value"}, playbook_type="daily")
        result = cache.get("test_key")
        
        assert result == {"data": "value"}
    
    def test_cache_miss(self):
        """测试缓存未命中"""
        cache = PlaybookCache()
        
        result = cache.get("missing_key")
        
        assert result is None
    
    def test_invalidate(self):
        """测试使缓存失效"""
        cache = PlaybookCache()
        
        cache.set("test_key", "value")
        cache.invalidate("test_key")
        
        assert cache.get("test_key") is None
    
    def test_invalidate_user(self):
        """测试使用户缓存失效"""
        cache = PlaybookCache()
        
        cache.set("playbook:user1:daily:2024-12-06", "value1")
        cache.set("playbook:user1:weekly:2024-W49", "value2")
        cache.set("playbook:user2:daily:2024-12-06", "value3")
        
        count = cache.invalidate_user("user1")
        
        assert count == 2
        assert cache.get("playbook:user1:daily:2024-12-06") is None
        assert cache.get("playbook:user2:daily:2024-12-06") == "value3"
    
    def test_make_key(self):
        """测试生成缓存键"""
        key = PlaybookCache.make_key("user1", "daily", "2024-12-06")
        
        assert key == "playbook:user1:daily:2024-12-06"
