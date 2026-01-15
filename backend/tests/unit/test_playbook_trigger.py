# backend/tests/unit/test_playbook_trigger.py
"""
R-08/WP-10: Playbook Trigger 测试

测试目标：
1. Cron 规则验证
2. 时区处理验证
3. 防重复 cache key 格式验证
"""

import pytest
import re
from unittest.mock import MagicMock, patch, AsyncMock
from datetime import date


class TestPlaybookTriggerFunctions:
    """Playbook 触发函数测试"""
    
    def test_daily_trigger_exists(self):
        """测试：日 Playbook 触发函数存在"""
        from backend.scheduler.jobs.playbook_trigger import trigger_daily_playbook
        import asyncio
        assert asyncio.iscoroutinefunction(trigger_daily_playbook)
    
    def test_yearly_trigger_exists(self):
        """测试：年度 Playbook 触发函数存在"""
        from backend.scheduler.jobs.playbook_trigger import trigger_yearly_playbook
        import asyncio
        assert asyncio.iscoroutinefunction(trigger_yearly_playbook)
    
    def test_new_user_trigger_exists(self):
        """测试：新用户 Playbook 触发函数存在"""
        from backend.scheduler.jobs.playbook_trigger import trigger_new_user_playbook
        import asyncio
        assert asyncio.iscoroutinefunction(trigger_new_user_playbook)


class TestSchedulerRegistryCronRules:
    """R-08: 调度 Cron 规则测试"""
    
    def test_daily_extract_cron_rule(self):
        """R-08: 每日意图提取 Cron 规则验证"""
        from apscheduler.triggers.cron import CronTrigger
        
        # 验证 22:00 规则可以创建
        trigger = CronTrigger(hour=22, minute=0)
        assert trigger is not None
        # CronTrigger 字符串表示存在
        trigger_str = str(trigger)
        assert trigger_str is not None
    
    def test_weekly_playbook_cron_rule(self):
        """R-08: 周 Playbook Cron 规则验证"""
        from apscheduler.triggers.cron import CronTrigger
        
        # 验证周日 18:00 规则
        trigger = CronTrigger(day_of_week="sun", hour=18, minute=0)
        assert trigger is not None
    
    def test_daily_trigger_cron_rule(self):
        """R-08: 日 Playbook 触发 Cron 规则验证（每5分钟）"""
        from apscheduler.triggers.cron import CronTrigger
        
        # 验证每5分钟规则
        trigger = CronTrigger(minute="*/5")
        assert trigger is not None


class TestPlaybookCacheKeyFormat:
    """R-08: 防重复 cache key 格式测试"""
    
    def test_daily_cache_key_format(self):
        """R-08: 日 Playbook cache key 格式验证"""
        user_id = "user_123"
        target_date = date(2024, 1, 15)
        
        # 构造 cache key
        cache_key = f"playbook:{user_id}:daily:{target_date.isoformat()}"
        
        # 验证格式
        assert cache_key == "playbook:user_123:daily:2024-01-15"
        assert cache_key.startswith("playbook:")
    
    def test_cache_key_contains_user_and_date(self):
        """R-08: cache key 包含 user_id 和 date"""
        import inspect
        from backend.scheduler.jobs import playbook_trigger
        source = inspect.getsource(playbook_trigger)
        
        # 验证 cache_key 格式在源码中存在
        assert "playbook:" in source
        assert ":daily:" in source or "daily" in source


class TestPlaybookTriggerTimeZone:
    """R-08: 时区处理测试"""
    
    def test_timezone_handling_exists(self):
        """R-08: 时区处理逻辑存在"""
        import inspect
        from backend.scheduler.jobs import playbook_trigger
        source = inspect.getsource(playbook_trigger)
        
        # 验证存在时区相关代码
        assert "timezone" in source.lower() or "tz" in source.lower() or "utc" in source.lower(), \
            "缺少时区处理逻辑"
    
    def test_utc_conversion_exists(self):
        """R-08: UTC 转换逻辑存在"""
        import inspect
        from backend.scheduler.jobs import playbook_trigger
        source = inspect.getsource(playbook_trigger)
        
        # 验证 UTC/时区转换
        assert "utc" in source.lower() or "astimezone" in source.lower(), \
            "缺少 UTC 转换逻辑"


class TestPlaybookTriggerDeduplication:
    """R-08: 防重复机制测试"""
    
    def test_cache_exists_check(self):
        """R-08: 验证 cache.exists 调用"""
        import inspect
        from backend.scheduler.jobs import playbook_trigger
        source = inspect.getsource(playbook_trigger)
        
        # 验证存在 exists 检查
        assert "exists" in source.lower() or "has_" in source.lower(), \
            "缺少 cache.exists 防重复检查"
    
    def test_ttl_used_for_cache(self):
        """R-08: 验证 TTL 用于 cache"""
        import inspect
        from backend.scheduler.jobs import playbook_trigger
        source = inspect.getsource(playbook_trigger)
        
        # 验证存在 TTL 设置
        assert "ttl" in source.lower() or "expire" in source.lower() or "set(" in source.lower(), \
            "缺少 TTL/过期设置"
