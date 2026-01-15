"""
Tests for Cache Module

缓存模块测试。
"""

import time
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from backend.core.cache.semantic_cache import SemanticCache, CacheStats, CacheEntry
from backend.core.cache.rule_cache import RuleResultCache
from backend.core.cache.invalidator import CacheInvalidator


class TestCacheStats:
    """CacheStats 测试"""
    
    def test_initial_stats(self):
        """测试初始统计"""
        stats = CacheStats()
        
        assert stats.hits == 0
        assert stats.misses == 0
        assert stats.hit_ratio == 0.0
    
    def test_record_hit(self):
        """测试记录命中"""
        stats = CacheStats()
        stats.record_hit()
        stats.record_hit()
        
        assert stats.hits == 2
    
    def test_record_miss(self):
        """测试记录未命中"""
        stats = CacheStats()
        stats.record_miss()
        
        assert stats.misses == 1
    
    def test_hit_ratio(self):
        """测试命中率计算"""
        stats = CacheStats()
        stats.hits = 7
        stats.misses = 3
        
        assert stats.hit_ratio == pytest.approx(0.7)


class TestCacheEntry:
    """CacheEntry 测试"""
    
    def test_not_expired_without_ttl(self):
        """测试无 TTL 时不过期"""
        entry = CacheEntry(value="test")
        
        assert entry.is_expired() is False
    
    def test_expired_with_ttl(self):
        """测试 TTL 过期"""
        entry = CacheEntry(value="test", ttl_seconds=0.01)
        
        # 等待过期
        time.sleep(0.02)
        
        assert entry.is_expired() is True
    
    def test_touch_updates_last_accessed(self):
        """测试 touch 更新最后访问时间"""
        entry = CacheEntry(value="test")
        original = entry.last_accessed
        
        time.sleep(0.01)
        entry.touch()
        
        assert entry.last_accessed > original


class TestSemanticCache:
    """SemanticCache 测试"""
    
    def test_set_and_get(self):
        """测试设置和获取"""
        cache = SemanticCache[str](max_size=100)
        
        cache.set("key1", "value1")
        result = cache.get("key1")
        
        assert result == "value1"
    
    def test_get_nonexistent(self):
        """测试获取不存在的键"""
        cache = SemanticCache[str](max_size=100)
        
        result = cache.get("nonexistent")
        
        assert result is None
    
    def test_lru_eviction(self):
        """测试 LRU 淘汰"""
        cache = SemanticCache[str](max_size=3)
        
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")
        
        # 访问 key1，使其成为最近访问
        cache.get("key1")
        
        # 添加新条目，触发淘汰
        cache.set("key4", "value4")
        
        # key2 应该被淘汰（最久未访问）
        assert cache.get("key2") is None
        assert cache.get("key1") == "value1"
        assert cache.get("key3") == "value3"
        assert cache.get("key4") == "value4"
    
    def test_ttl_expiration(self):
        """测试 TTL 过期"""
        cache = SemanticCache[str](max_size=100, ttl_seconds=0.01)
        
        cache.set("key1", "value1")
        
        # 立即获取应该成功
        assert cache.get("key1") == "value1"
        
        # 等待过期
        time.sleep(0.02)
        
        # 过期后应返回 None
        assert cache.get("key1") is None
    
    def test_delete(self):
        """测试删除"""
        cache = SemanticCache[str](max_size=100)
        
        cache.set("key1", "value1")
        assert cache.delete("key1") is True
        assert cache.get("key1") is None
        
        assert cache.delete("nonexistent") is False
    
    def test_clear(self):
        """测试清空"""
        cache = SemanticCache[str](max_size=100)
        
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        
        count = cache.clear()
        
        assert count == 2
        assert cache.size() == 0
    
    def test_has(self):
        """测试 has"""
        cache = SemanticCache[str](max_size=100)
        
        cache.set("key1", "value1")
        
        assert cache.has("key1") is True
        assert cache.has("nonexistent") is False
    
    def test_stats_tracking(self):
        """测试统计追踪"""
        cache = SemanticCache[str](max_size=100)
        
        cache.set("key1", "value1")
        cache.get("key1")  # hit
        cache.get("nonexistent")  # miss
        
        stats = cache.stats
        assert stats.hits == 1
        assert stats.misses == 1
    
    def test_cleanup_expired(self):
        """测试清理过期条目"""
        cache = SemanticCache[str](max_size=100, ttl_seconds=0.01)
        
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        
        time.sleep(0.02)
        
        count = cache.cleanup_expired()
        
        assert count == 2
        assert cache.size() == 0


class TestRuleResultCache:
    """RuleResultCache 测试"""
    
    def test_compute_key(self):
        """测试键计算"""
        cache = RuleResultCache(max_size=100)
        
        key1 = cache.compute_key("bazi", {"day_master": "甲"})
        key2 = cache.compute_key("bazi", {"day_master": "甲"})
        key3 = cache.compute_key("bazi", {"day_master": "乙"})
        
        # 相同参数应产生相同的键
        assert key1 == key2
        # 不同参数应产生不同的键
        assert key1 != key3
    
    def test_get_set_by_factors(self):
        """测试通过因子获取和设置"""
        cache = RuleResultCache(max_size=100)
        
        factors = {"day_master": "甲", "season": "spring"}
        results = [{"rule_id": "rule1", "hit": True}]
        
        cache.set_by_factors("bazi", factors, results)
        retrieved = cache.get_by_factors("bazi", factors)
        
        assert retrieved == results
    
    def test_invalidate_by_engine(self):
        """测试按引擎失效"""
        cache = RuleResultCache(max_size=100)
        
        cache.set_by_factors("bazi", {"a": 1}, [{"x": 1}])
        cache.set_by_factors("ziwei", {"b": 2}, [{"y": 2}])
        
        count = cache.invalidate_by_engine("bazi")
        
        # 当前实现清空所有
        assert cache.size() == 0


class TestCacheInvalidator:
    """CacheInvalidator 测试"""
    
    def test_initialization(self):
        """测试初始化"""
        semantic_cache = SemanticCache[str](max_size=100)
        rule_cache = RuleResultCache(max_size=100)
        
        invalidator = CacheInvalidator(
            semantic_cache=semantic_cache,
            rule_cache=rule_cache,
            auto_subscribe=False,
        )
        
        assert invalidator.semantic_cache is semantic_cache
        assert invalidator.rule_cache is rule_cache
    
    def test_invalidate_rule_cache(self):
        """测试失效规则缓存"""
        rule_cache = RuleResultCache(max_size=100)
        rule_cache.set("key1", [{"a": 1}])
        
        invalidator = CacheInvalidator(
            rule_cache=rule_cache,
            auto_subscribe=False,
        )
        
        count = invalidator.invalidate_rule_cache()
        
        assert count == 1
        assert rule_cache.size() == 0
    
    def test_invalidate_semantic_cache(self):
        """测试失效语义缓存"""
        semantic_cache = SemanticCache[str](max_size=100)
        semantic_cache.set("key1", "value1")
        
        invalidator = CacheInvalidator(
            semantic_cache=semantic_cache,
            auto_subscribe=False,
        )
        
        count = invalidator.invalidate_semantic_cache()
        
        assert count == 1
    
    def test_invalidate_all(self):
        """测试失效所有缓存"""
        semantic_cache = SemanticCache[str](max_size=100)
        rule_cache = RuleResultCache(max_size=100)
        
        semantic_cache.set("s1", "v1")
        rule_cache.set("r1", [{"a": 1}])
        
        invalidator = CacheInvalidator(
            semantic_cache=semantic_cache,
            rule_cache=rule_cache,
            auto_subscribe=False,
        )
        
        count = invalidator.invalidate_all()
        
        assert count == 2
    
    def test_invalidate_by_key(self):
        """测试按键失效"""
        semantic_cache = SemanticCache[str](max_size=100)
        semantic_cache.set("key1", "value1")
        
        invalidator = CacheInvalidator(
            semantic_cache=semantic_cache,
            auto_subscribe=False,
        )
        
        result = invalidator.invalidate_by_key("key1")
        
        assert result is True
        assert semantic_cache.get("key1") is None
    
    def test_get_stats(self):
        """测试获取统计"""
        semantic_cache = SemanticCache[str](max_size=100)
        rule_cache = RuleResultCache(max_size=100)
        
        semantic_cache.set("key1", "value1")
        semantic_cache.get("key1")  # hit
        
        invalidator = CacheInvalidator(
            semantic_cache=semantic_cache,
            rule_cache=rule_cache,
            auto_subscribe=False,
        )
        
        stats = invalidator.get_stats()
        
        assert "semantic" in stats
        assert stats["semantic"]["hits"] == 1
    
    def test_on_reload_rules(self):
        """测试规则文件重载回调"""
        rule_cache = RuleResultCache(max_size=100)
        rule_cache.set("key1", [{"a": 1}])
        
        invalidator = CacheInvalidator(
            rule_cache=rule_cache,
            auto_subscribe=False,
        )
        
        # 模拟规则文件变更
        invalidator._on_reload(Path("/some/path/rules/test.jsonl"))
        
        assert rule_cache.size() == 0


class TestIntegration:
    """集成测试"""
    
    def test_module_exports(self):
        """测试模块导出"""
        from backend.core.cache import (
            SemanticCache,
            CacheStats,
            RuleResultCache,
            CacheInvalidator,
        )
        
        assert SemanticCache is not None
        assert CacheStats is not None
        assert RuleResultCache is not None
        assert CacheInvalidator is not None
