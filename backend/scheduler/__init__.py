"""
Scheduler Module

定时任务调度系统。

使用 APScheduler 实现：
- 每日 22:00 提取 TO-DO/DONE 生成 Insight
- 每周日生成周 Playbook
- 每月1日生成月 Playbook
- 版本树定期校准
"""

from backend.scheduler.base import scheduler, init_scheduler, shutdown_scheduler
from backend.scheduler.registry import register_all_jobs

__all__ = [
    "scheduler",
    "init_scheduler",
    "shutdown_scheduler",
    "register_all_jobs",
]
