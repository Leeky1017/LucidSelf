"""
Scheduler Base

APScheduler 配置和初始化。
"""

import logging
import os
from typing import Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.executors.pool import ThreadPoolExecutor

logger = logging.getLogger(__name__)

# 全局调度器实例
scheduler: Optional[AsyncIOScheduler] = None


def get_job_stores() -> dict:
    """
    获取任务存储配置
    
    优先使用 Redis（支持分布式锁），
    Redis 不可用时回退到内存存储。
    """
    redis_url = os.getenv("REDIS_URL")
    
    if redis_url:
        try:
            # 解析 Redis URL
            # 格式: redis://:password@host:port/db
            from urllib.parse import urlparse
            parsed = urlparse(redis_url)
            
            return {
                "default": RedisJobStore(
                    host=parsed.hostname or "localhost",
                    port=parsed.port or 6379,
                    db=int(parsed.path.lstrip("/") or 0),
                    password=parsed.password,
                ),
            }
        except Exception as e:
            logger.warning(f"Failed to configure Redis job store: {e}, using memory")
    
    return {"default": MemoryJobStore()}


def get_executors() -> dict:
    """获取执行器配置"""
    return {
        "default": AsyncIOExecutor(),
        "threadpool": ThreadPoolExecutor(max_workers=5),
    }


def get_job_defaults() -> dict:
    """获取任务默认配置"""
    return {
        "coalesce": True,  # 合并错过的任务
        "max_instances": 1,  # 同一任务最多一个实例
        "misfire_grace_time": 60 * 60,  # 错过1小时内仍执行
    }


def init_scheduler() -> AsyncIOScheduler:
    """
    初始化调度器
    
    在应用启动时调用。
    """
    global scheduler
    
    if scheduler is not None:
        logger.warning("Scheduler already initialized")
        return scheduler
    
    scheduler = AsyncIOScheduler(
        jobstores=get_job_stores(),
        executors=get_executors(),
        job_defaults=get_job_defaults(),
        timezone="Asia/Shanghai",  # 使用中国时区
    )
    
    logger.info("Scheduler initialized")
    return scheduler


def start_scheduler() -> None:
    """启动调度器"""
    global scheduler
    
    if scheduler is None:
        scheduler = init_scheduler()
    
    if not scheduler.running:
        scheduler.start()
        logger.info("Scheduler started")


def shutdown_scheduler() -> None:
    """关闭调度器"""
    global scheduler
    
    if scheduler is not None and scheduler.running:
        scheduler.shutdown(wait=True)
        logger.info("Scheduler shutdown")
    
    scheduler = None


def get_scheduler() -> AsyncIOScheduler:
    """
    获取调度器实例
    
    如果未初始化则自动初始化。
    """
    global scheduler
    
    if scheduler is None:
        scheduler = init_scheduler()
    
    return scheduler
