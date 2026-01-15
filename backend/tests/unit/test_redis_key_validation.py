# backend/tests/unit/test_redis_key_validation.py
"""
R-07/WP-09: Redis 键前缀运行时校验测试

测试目标：
1. 合法 key 操作成功
2. 非法 key 抛出异常
3. 降级不掩盖非法 key
4. TTL 配置正确
"""

import pytest
from datetime import timedelta

from backend.services.cache.redis_client import (
    RedisCache,
    validate_cache_key,
    InvalidCacheKeyError,
    VALID_KEY_PATTERNS,
)


class TestValidateCacheKey:
    """R-07: key 校验函数测试"""
    
    def test_valid_user_key(self):
        """R-07: 合法 user: key 通过校验"""
        validate_cache_key("user:123:today_context:2024-01-01")
        validate_cache_key("user:abc:active_insights")
        validate_cache_key("user:test_user:anything")
    
    def test_valid_playbook_key(self):
        """R-07: 合法 playbook: key 通过校验"""
        validate_cache_key("playbook:123:daily:2024-01-01")
        validate_cache_key("playbook:abc:weekly:2024-W01")
    
    def test_valid_session_key(self):
        """R-07: 合法 session: key 通过校验"""
        validate_cache_key("session:sess_123abc")
    
    def test_valid_factors_key(self):
        """R-07: 合法 factors: key 通过校验"""
        validate_cache_key("factors:user123:2024-01-01")
    
    def test_invalid_key_raises_exception(self):
        """R-07: 非法 key 抛出 InvalidCacheKeyError"""
        with pytest.raises(InvalidCacheKeyError):
            validate_cache_key("invalid_key")
        
        with pytest.raises(InvalidCacheKeyError):
            validate_cache_key("random:data")
        
        with pytest.raises(InvalidCacheKeyError):
            validate_cache_key("foo:bar:baz")
    
    def test_empty_key_raises_exception(self):
        """R-07: 空 key 抛出异常"""
        with pytest.raises(InvalidCacheKeyError):
            validate_cache_key("")


class TestRedisCacheKeyValidation:
    """R-07: RedisCache 运行时校验测试"""
    
    @pytest.fixture
    def cache(self):
        return RedisCache()
    
    @pytest.mark.asyncio
    async def test_get_valid_key_succeeds(self, cache):
        """R-07: get 合法 key 成功"""
        result = await cache.get("user:123:today_context:2024-01-01")
        assert result is None  # key 不存在返回 None
    
    @pytest.mark.asyncio
    async def test_get_invalid_key_raises(self, cache):
        """R-07: get 非法 key 抛出异常"""
        with pytest.raises(InvalidCacheKeyError):
            await cache.get("invalid_key_format")
    
    @pytest.mark.asyncio
    async def test_set_valid_key_succeeds(self, cache):
        """R-07: set 合法 key 成功"""
        result = await cache.set("user:123:test:data", "value", timedelta(seconds=60))
        assert result is True
    
    @pytest.mark.asyncio
    async def test_set_invalid_key_raises(self, cache):
        """R-07: set 非法 key 抛出异常"""
        with pytest.raises(InvalidCacheKeyError):
            await cache.set("bad_key", "value")
    
    @pytest.mark.asyncio
    async def test_exists_invalid_key_raises(self, cache):
        """R-07: exists 非法 key 抛出异常"""
        with pytest.raises(InvalidCacheKeyError):
            await cache.exists("random_key")
    
    @pytest.mark.asyncio
    async def test_delete_invalid_key_raises(self, cache):
        """R-07: delete 非法 key 抛出异常"""
        with pytest.raises(InvalidCacheKeyError):
            await cache.delete("another_bad_key")


class TestRedisCacheTTL:
    """Redis TTL 配置测试"""
    
    def test_ttl_constants_exist(self):
        """测试：TTL 常量存在"""
        assert hasattr(RedisCache, 'TTL_TODAY_CONTEXT')
        assert hasattr(RedisCache, 'TTL_ACTIVE_INSIGHTS')
        assert hasattr(RedisCache, 'TTL_DAILY_PLAYBOOK')
        assert hasattr(RedisCache, 'TTL_FACTORS')
    
    def test_ttl_values_reasonable(self):
        """测试：TTL 值在合理范围"""
        assert RedisCache.TTL_TODAY_CONTEXT >= timedelta(hours=1)
        assert RedisCache.TTL_ACTIVE_INSIGHTS >= timedelta(days=1)
        assert RedisCache.TTL_DAILY_PLAYBOOK >= timedelta(hours=1)
        assert RedisCache.TTL_FACTORS >= timedelta(hours=1)


class TestRedisCacheFallback:
    """Redis 降级机制测试"""
    
    @pytest.fixture
    def cache(self):
        return RedisCache()
    
    def test_memory_cache_exists(self, cache):
        """测试：内存降级缓存存在"""
        assert hasattr(cache, '_memory_cache')
    
    def test_is_connected_property(self, cache):
        """测试：连接状态属性存在"""
        assert hasattr(cache, 'is_connected')
        assert isinstance(cache.is_connected, bool)
    
    @pytest.mark.asyncio
    async def test_fallback_with_valid_key(self, cache):
        """R-07: 降级时合法 key 正常工作"""
        # 使用合法 key 测试降级
        await cache.set("user:123:test:fallback", "value", timedelta(seconds=60))
        result = await cache.get("user:123:test:fallback")
        assert result == "value"
    
    @pytest.mark.asyncio
    async def test_fallback_does_not_mask_invalid_key(self, cache):
        """R-07: 降级不掩盖非法 key 错误"""
        # 即使 Redis 不可用，非法 key 仍应抛出异常
        with pytest.raises(InvalidCacheKeyError):
            await cache.get("invalid_during_fallback")
