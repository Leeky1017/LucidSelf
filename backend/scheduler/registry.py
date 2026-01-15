"""
Job Registry

任务注册和管理。
"""

import logging
from typing import Callable, List

from apscheduler.triggers.cron import CronTrigger

from backend.scheduler.base import get_scheduler

logger = logging.getLogger(__name__)


def register_all_jobs() -> None:
    """
    注册所有定时任务
    
    在应用启动时调用。
    """
    scheduler = get_scheduler()
    
    # 导入所有任务
    from backend.scheduler.jobs import (
        daily_extract,
        weekly_playbook,
        monthly_playbook,
        playbook_trigger,  # Phase 11: Playbook 触发
    )
    
    # =========================================================================
    # 每日 22:00 - TO-DO/DONE 意图提取
    # =========================================================================
    scheduler.add_job(
        daily_extract.run_daily_extract,
        trigger=CronTrigger(hour=22, minute=0),
        id="daily_extract",
        name="Daily TO-DO/DONE Intent Extraction",
        replace_existing=True,
    )
    logger.info("Registered job: daily_extract (22:00 daily)")
    
    # =========================================================================
    # 每周日 18:00 - 周 Playbook 生成
    # =========================================================================
    scheduler.add_job(
        weekly_playbook.run_weekly_playbook,
        trigger=CronTrigger(day_of_week="sun", hour=18, minute=0),
        id="weekly_playbook",
        name="Weekly Playbook Generation",
        replace_existing=True,
    )
    logger.info("Registered job: weekly_playbook (Sunday 18:00)")
    
    # =========================================================================
    # 每月最后一天 18:00 - 月 Playbook 生成
    # =========================================================================
    scheduler.add_job(
        monthly_playbook.run_monthly_playbook,
        trigger=CronTrigger(day="last", hour=18, minute=0),
        id="monthly_playbook",
        name="Monthly Playbook Generation",
        replace_existing=True,
    )
    logger.info("Registered job: monthly_playbook (Last day of month 18:00)")
    
    # =========================================================================
    # Phase 11: Playbook 触发调度
    # =========================================================================
    
    # 每 5 分钟 - 日 Playbook 触发（检查用户时区）
    scheduler.add_job(
        playbook_trigger.trigger_daily_playbook,
        trigger=CronTrigger(minute="*/5"),
        id="daily_playbook_trigger",
        name="Daily Playbook Trigger (Timezone Check)",
        replace_existing=True,
    )
    logger.info("Registered job: daily_playbook_trigger (every 5 minutes)")
    
    # 12/31 18:00 - 年度 Playbook 触发（仅付费用户）
    scheduler.add_job(
        playbook_trigger.trigger_yearly_playbook,
        trigger=CronTrigger(month=12, day=31, hour=18, minute=0),
        id="yearly_playbook_trigger",
        name="Yearly Playbook Trigger (Paid Users Only)",
        replace_existing=True,
    )
    logger.info("Registered job: yearly_playbook_trigger (Dec 31 18:00)")
    
    logger.info(f"Total jobs registered: {len(scheduler.get_jobs())}")


def list_jobs() -> List[dict]:
    """列出所有已注册的任务"""
    scheduler = get_scheduler()
    
    jobs = []
    for job in scheduler.get_jobs():
        # APScheduler 4.x 使用不同的属性名
        next_run = None
        if hasattr(job, 'next_run_time') and job.next_run_time:
            next_run = job.next_run_time.isoformat()
        elif hasattr(job, 'next_fire_time') and job.next_fire_time:
            next_run = job.next_fire_time.isoformat()
        
        jobs.append({
            "id": job.id,
            "name": getattr(job, 'name', job.id),
            "next_run": next_run,
            "trigger": str(job.trigger),
        })
    
    return jobs


def trigger_job_now(job_id: str) -> bool:
    """
    立即触发指定任务
    
    用于手动测试。
    """
    scheduler = get_scheduler()
    
    job = scheduler.get_job(job_id)
    if job is None:
        logger.warning(f"Job not found: {job_id}")
        return False
    
    scheduler.modify_job(job_id, next_run_time=None)
    logger.info(f"Triggered job immediately: {job_id}")
    return True
