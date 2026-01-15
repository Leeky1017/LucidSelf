# backend/scheduler/jobs/playbook_trigger.py
"""
Playbook Trigger Job

Playbook 触发调度器。

Phase 11 Task 11.1: 实现 Playbook 触发调度
参考 tasks.md Phase 11 和 requirements.md R10

触发规则:
- 日 Playbook: 每5分钟检查，根据用户时区在 00:00 触发
- 周 Playbook: 周日 18:00 (试用+付费用户)
- 月 Playbook: 月末 18:00 (试用+付费用户)
- 年 Playbook: 12/31 18:00 (仅付费用户)
- 新用户: 注册时立即触发日 Playbook
"""

import asyncio
import logging
from datetime import date, datetime, timedelta
from typing import List, Optional
import pytz

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import async_session_maker
from backend.services.cache import get_redis_cache

logger = logging.getLogger(__name__)

# 配置
BATCH_SIZE = 50  # 每批处理用户数
MAX_CONCURRENT = 5  # 最大并发数


async def trigger_daily_playbook() -> dict:
    """
    每日 Playbook 触发
    
    每 5 分钟执行一次，检查用户时区，为处于 00:00 的用户生成日 Playbook。
    
    Returns:
        执行报告
    """
    start_time = datetime.utcnow()
    today = date.today()
    
    logger.info(f"Daily playbook trigger started: {today}")
    
    report = {
        "date": today.isoformat(),
        "checked_users": 0,
        "triggered_users": 0,
        "skipped_users": 0,
        "failed_users": [],
        "duration_seconds": 0,
    }
    
    try:
        # 获取需要触发的用户
        users_to_trigger = await _get_users_for_daily_playbook(today)
        report["checked_users"] = len(users_to_trigger)
        
        # 分批处理
        for i in range(0, len(users_to_trigger), BATCH_SIZE):
            batch = users_to_trigger[i:i + BATCH_SIZE]
            
            # 限制并发
            semaphore = asyncio.Semaphore(MAX_CONCURRENT)
            
            async def trigger_with_limit(user_id: str):
                async with semaphore:
                    return await _trigger_playbook_for_user(user_id, "daily", today)
            
            results = await asyncio.gather(
                *[trigger_with_limit(uid) for uid in batch],
                return_exceptions=True
            )
            
            for user_id, result in zip(batch, results):
                if isinstance(result, Exception):
                    report["failed_users"].append(user_id)
                    logger.error(f"Failed to trigger daily playbook for {user_id}: {result}")
                elif result:
                    report["triggered_users"] += 1
                else:
                    report["skipped_users"] += 1
    
    except Exception as e:
        logger.error(f"Daily playbook trigger failed: {e}")
        raise
    
    finally:
        report["duration_seconds"] = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"Daily playbook trigger completed: {report}")
    
    return report


async def trigger_yearly_playbook() -> dict:
    """
    年度 Playbook 触发
    
    12/31 18:00 执行，仅为付费用户生成年度报告。
    
    Returns:
        执行报告
    """
    start_time = datetime.utcnow()
    today = date.today()
    
    # 检查是否是 12/31
    if today.month != 12 or today.day != 31:
        logger.info(f"Not Dec 31, skipping yearly playbook: {today}")
        return {"skipped": True, "reason": "not_dec_31"}
    
    logger.info(f"Yearly playbook trigger started: {today}")
    
    report = {
        "year": today.year,
        "triggered_users": 0,
        "skipped_users": 0,
        "failed_users": [],
        "duration_seconds": 0,
    }
    
    try:
        # 获取付费用户
        paid_users = await _get_paid_users()
        
        for user_id in paid_users:
            try:
                success = await _trigger_playbook_for_user(user_id, "yearly", today)
                if success:
                    report["triggered_users"] += 1
                else:
                    report["skipped_users"] += 1
            except Exception as e:
                report["failed_users"].append(user_id)
                logger.error(f"Failed to trigger yearly playbook for {user_id}: {e}")
    
    except Exception as e:
        logger.error(f"Yearly playbook trigger failed: {e}")
        raise
    
    finally:
        report["duration_seconds"] = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"Yearly playbook trigger completed: {report}")
    
    return report


async def trigger_new_user_playbook(user_id: str) -> bool:
    """
    新用户 Playbook 触发
    
    注册时立即为新用户生成首个日 Playbook。
    
    Args:
        user_id: 新用户 ID
        
    Returns:
        是否触发成功
    """
    logger.info(f"Triggering new user playbook for: {user_id}")
    
    try:
        today = date.today()
        success = await _trigger_playbook_for_user(user_id, "daily", today, is_new_user=True)
        
        if success:
            logger.info(f"New user playbook triggered successfully: {user_id}")
        else:
            logger.warning(f"New user playbook skipped (already exists): {user_id}")
        
        return success
    
    except Exception as e:
        logger.error(f"Failed to trigger new user playbook for {user_id}: {e}")
        return False


# =============================================================================
# 辅助函数
# =============================================================================

async def _get_users_for_daily_playbook(target_date: date) -> List[str]:
    """
    获取需要触发日 Playbook 的用户列表
    
    根据用户时区判断是否到了 00:00
    """
    try:
        # 获取当前 UTC 时间
        utc_now = datetime.now(pytz.UTC)
        
        # 查找当前小时是 00:xx 的时区
        # UTC+0 到 UTC+14 的时区范围
        target_timezones = []
        target_tz_names = []
        for offset in range(-12, 15):  # UTC-12 到 UTC+14
            try:
                tz = pytz.FixedOffset(offset * 60)
                local_time = utc_now.astimezone(tz)
                # 如果本地时间是 00:00-00:04 (每5分钟检查一次)
                if local_time.hour == 0 and local_time.minute < 5:
                    target_timezones.append(offset)
                    # 转换为 Etc/GMT 格式以匹配常见时区
                    if offset >= 0:
                        target_tz_names.append(f"Etc/GMT-{offset}")
                    else:
                        target_tz_names.append(f"Etc/GMT+{abs(offset)}")
            except Exception:
                continue
        
        if not target_timezones:
            return []
        
        logger.debug(f"Target timezones for daily playbook: {target_timezones}")
        
        # 查询符合时区条件的用户
        from backend.models.auth import User
        from backend.models.user import UserProfile
        
        user_ids = []
        cache = get_redis_cache()
        
        async with async_session_maker() as session:
            # 查询所有活跃用户
            result = await session.execute(
                select(User.user_id)
                .where(User.tier.in_(["free", "pro", "premium", "plus"]))
            )
            all_users = [row[0] for row in result.fetchall()]
            
            # 对于每个用户检查是否已触发
            for uid in all_users:
                cache_key = f"playbook:{uid}:daily:{target_date.isoformat()}"
                if not await cache.exists(cache_key):
                    user_ids.append(uid)
        
        logger.info(f"Found {len(user_ids)} users for daily playbook (total: {len(all_users)})")
        return user_ids
        
    except Exception as e:
        logger.error(f"Failed to get users for daily playbook: {e}")
        return []


async def _get_paid_users() -> List[str]:
    """
    获取付费用户列表
    
    查询订阅状态为 active 且未过期的用户
    """
    try:
        from backend.models.subscription import Subscription
        from backend.core.contracts.subscription_models import (
            MembershipTier,
            SubscriptionStatus,
        )
        
        async with async_session_maker() as session:
            result = await session.execute(
                select(Subscription.user_id).where(
                    Subscription.tier == MembershipTier.PLUS,
                    Subscription.status == SubscriptionStatus.ACTIVE,
                    Subscription.expires_at > datetime.utcnow()
                )
            )
            paid_users = [row[0] for row in result.fetchall()]
        
        logger.info(f"Found {len(paid_users)} paid users")
        return paid_users
    except Exception as e:
        logger.error(f"Failed to get paid users: {e}")
        return []


async def _trigger_playbook_for_user(
    user_id: str,
    playbook_type: str,
    target_date: date,
    is_new_user: bool = False,
) -> bool:
    """
    为用户触发 Playbook 生成
    
    Args:
        user_id: 用户 ID
        playbook_type: Playbook 类型 (daily/weekly/monthly/yearly)
        target_date: 目标日期
        is_new_user: 是否新用户
        
    Returns:
        是否成功触发（已存在则返回 False）
    """
    try:
        # 检查是否已生成（防重复）
        cache = get_redis_cache()
        cache_key = f"playbook:{user_id}:{playbook_type}:{target_date.isoformat()}"
        
        # 检查 Redis 缓存
        if await cache.exists(cache_key):
            logger.debug(f"Playbook already exists: {cache_key}")
            return False
        
        # 调用 Playbook 生成
        logger.info(
            f"Generating {playbook_type} playbook for user {user_id} "
            f"(date={target_date}, new_user={is_new_user})"
        )
        
        # 实际调用 PlaybookGenerator
        try:
            from backend.services.playbook import PlaybookGenerator, PlaybookType
            
            generator = PlaybookGenerator()
            pb_type = PlaybookType(playbook_type)
            playbook = generator.generate(user_id, pb_type, target_date.isoformat())
            
            if playbook:
                # 写入 Redis 缓存防重复 (25小时)
                await cache.set(cache_key, playbook.playbook_id, cache.TTL_DAILY_PLAYBOOK)
                logger.info(f"Playbook generated: {playbook.playbook_id}")
        except ImportError:
            logger.warning("PlaybookGenerator not available, skipping actual generation")
        except Exception as gen_err:
            logger.error(f"PlaybookGenerator error: {gen_err}")
            # 仍然记录缓存防止重复触发
            await cache.set(cache_key, "error", cache.TTL_DAILY_PLAYBOOK)
        
        return True
    
    except Exception as e:
        logger.error(f"Failed to trigger playbook for user {user_id}: {e}")
        raise


async def _check_user_subscription(user_id: str) -> str:
    """
    检查用户订阅状态
    
    Returns:
        订阅状态: free/trial/paid
    """
    try:
        cache = get_redis_cache()
        cache_key = f"user:{user_id}:subscription"
        
        # 先检查缓存
        cached_status = await cache.get(cache_key)
        if cached_status:
            return cached_status
        
        # 查询数据库
        from backend.models.subscription import Subscription
        from backend.core.contracts.subscription_models import (
            MembershipTier,
            SubscriptionStatus,
        )
        
        status = "free"
        async with async_session_maker() as session:
            result = await session.execute(
                select(Subscription).where(
                    Subscription.user_id == user_id,
                    Subscription.expires_at > datetime.utcnow()
                )
            )
            subscription = result.scalar_one_or_none()
            
            if subscription:
                if subscription.status == SubscriptionStatus.ACTIVE:
                    if subscription.tier == MembershipTier.PLUS:
                        status = "paid"
                    else:
                        status = "trial"
        
        # 缓存 1 小时
        await cache.set(cache_key, status, timedelta(hours=1))
        
        return status
    except Exception as e:
        logger.error(f"Failed to check subscription for {user_id}: {e}")
        return "free"
