"""
Scheduler API Routes

调度器管理 API（仅限管理员）。
"""

import logging
from typing import List

from fastapi import APIRouter, HTTPException, status

from backend.scheduler.registry import list_jobs, trigger_job_now

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/scheduler", tags=["scheduler"])


@router.get(
    "/jobs",
    summary="列出所有定时任务",
    description="获取所有已注册的定时任务及其下次执行时间",
)
async def get_jobs() -> List[dict]:
    """列出所有定时任务"""
    return list_jobs()


@router.post(
    "/jobs/{job_id}/trigger",
    summary="立即触发任务",
    description="手动触发指定的定时任务（用于测试）",
)
async def trigger_job(job_id: str) -> dict:
    """立即触发指定任务"""
    success = trigger_job_now(job_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "JOB_NOT_FOUND", "message": f"任务不存在: {job_id}"},
        )
    
    return {"success": True, "message": f"任务 {job_id} 已触发"}
