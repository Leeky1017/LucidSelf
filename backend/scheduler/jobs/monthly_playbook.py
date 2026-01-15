"""
Monthly Playbook Job

每月1日 20:00 生成月 Playbook。

流程:
1. 查询活跃用户（30天内有登录）
2. 聚合用户上月 Insight
3. 调用 PlaybookGenerator 生成月报
4. 保存月 Playbook

对照 roadmap: .kiro/docs/ls_implementation_roadmap.md §2.4.3
"""

import logging
from calendar import monthrange
from datetime import date, datetime, timedelta
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.sql import func

from backend.db.session import async_session_maker

logger = logging.getLogger(__name__)

BATCH_SIZE = 50
MIN_INSIGHTS_FOR_MONTHLY = 7  # 生成月报需要的最少 Insight 数


async def run_monthly_playbook() -> dict:
    """
    执行月 Playbook 批量生成
    
    在月初执行，生成上月的 Playbook。
    
    Returns:
        执行报告
    """
    start_time = datetime.utcnow()
    
    # 计算上月范围（月初执行，生成上月数据）
    today = date.today()
    
    # 上月第一天和最后一天
    first_of_this_month = today.replace(day=1)
    last_of_prev_month = first_of_this_month - timedelta(days=1)
    first_of_prev_month = last_of_prev_month.replace(day=1)
    
    month_start = first_of_prev_month
    month_end = last_of_prev_month
    
    logger.info(f"Starting monthly playbook generation for {month_start} - {month_end}")
    
    report = {
        "month_start": month_start.isoformat(),
        "month_end": month_end.isoformat(),
        "total_users": 0,
        "generated": 0,
        "skipped": 0,
        "failed": [],
        "duration_seconds": 0,
    }
    
    try:
        # 获取活跃用户（30天活跃）
        user_ids = await _get_active_users(days=30)
        report["total_users"] = len(user_ids)
        
        if not user_ids:
            logger.info("No active users, skipping")
            return report
        
        # 分批处理
        for i in range(0, len(user_ids), BATCH_SIZE):
            batch = user_ids[i:i + BATCH_SIZE]
            
            for user_id in batch:
                try:
                    # 检查用户上月是否有足够数据
                    insight_count = await _get_user_month_insight_count(
                        user_id, month_start, month_end
                    )
                    
                    if insight_count < MIN_INSIGHTS_FOR_MONTHLY:
                        # 数据不足，跳过
                        report["skipped"] += 1
                        logger.debug(f"Skipping user {user_id}: only {insight_count} insights")
                        continue
                    
                    # 生成月 Playbook
                    playbook_id = await _generate_monthly_playbook(
                        user_id, month_start, month_end
                    )
                    if playbook_id:
                        report["generated"] += 1
                    else:
                        report["skipped"] += 1
                    
                except Exception as e:
                    logger.error(f"Failed to generate monthly playbook for {user_id}: {e}")
                    report["failed"].append(user_id)
            
            logger.info(
                f"Processed batch {i // BATCH_SIZE + 1}, "
                f"generated: {report['generated']}, skipped: {report['skipped']}"
            )
    
    except Exception as e:
        logger.error(f"Monthly playbook generation failed: {e}")
        raise
    
    finally:
        report["duration_seconds"] = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"Monthly playbook completed: {report}")
    
    return report


async def _get_active_users(days: int) -> List[str]:
    """
    获取近 N 天活跃的用户
    
    活跃定义：有登录记录或有 TODO/DONE 条目
    """
    try:
        from backend.models.user import UserProfile
        from backend.models.todo import TodoEntry
        
        cutoff = datetime.utcnow() - timedelta(days=days)
        
        async with async_session_maker() as session:
            # 从 UserProfile 的 last_login 获取
            user_result = await session.execute(
                select(UserProfile.user_id)
                .where(UserProfile.last_login >= cutoff)
                .distinct()
            )
            active_from_login = set(row[0] for row in user_result.fetchall())
            
            # 从 TODO 条目获取
            todo_result = await session.execute(
                select(TodoEntry.user_id)
                .where(TodoEntry.created_at >= cutoff)
                .distinct()
            )
            active_from_todo = set(row[0] for row in todo_result.fetchall())
            
            # 合并
            all_active = active_from_login | active_from_todo
            
            logger.info(
                f"Found {len(all_active)} active users (30d) "
                f"(login: {len(active_from_login)}, todo: {len(active_from_todo)})"
            )
            
            return list(all_active)
    
    except Exception as e:
        logger.warning(f"Failed to get active users from DB, returning empty: {e}")
        return []


async def _get_user_month_insight_count(
    user_id: str,
    month_start: date,
    month_end: date,
) -> int:
    """获取用户指定月份 Insight 数量"""
    try:
        from backend.services.memory import MemoryService
        
        memory_service = MemoryService()
        
        # 获取所有 insights
        start_dt = datetime.combine(month_start, datetime.min.time())
        end_dt = datetime.combine(month_end, datetime.max.time())
        
        insights = await memory_service.get_insights(user_id)
        
        # 过滤指定月份的
        month_insights = [
            ins for ins in insights
            if hasattr(ins, 'created_at') 
            and start_dt <= ins.created_at <= end_dt
        ]
        
        return len(month_insights) if month_insights else 0
    
    except Exception as e:
        logger.warning(f"Failed to count monthly insights for {user_id}: {e}")
        return 0


async def _generate_monthly_playbook(
    user_id: str,
    month_start: date,
    month_end: date,
) -> Optional[str]:
    """
    生成月 Playbook
    
    集成 PlaybookGenerator.generate()
    
    Returns:
        playbook_id 或 None
    """
    try:
        from backend.services.playbook.generator import (
            PlaybookGenerator,
            PlaybookType,
        )
        
        generator = PlaybookGenerator()
        
        # 生成月报
        playbook = await generator.generate(
            user_id=user_id,
            playbook_type=PlaybookType.MONTHLY,
            target_date=month_end,  # 使用月末作为目标日期
            use_cache=False,  # 批量生成不使用缓存
        )
        
        # 保存到记忆层（作为 Insight）
        await _save_playbook_as_insight(user_id, playbook, "monthly")
        
        logger.info(f"Generated monthly playbook {playbook.playbook_id} for user {user_id}")
        return playbook.playbook_id
    
    except Exception as e:
        logger.error(f"Failed to generate monthly playbook for {user_id}: {e}")
        return None


async def _save_playbook_as_insight(
    user_id: str, 
    playbook, 
    playbook_type: str = "monthly"
) -> Optional[str]:
    """
    将 Playbook 保存为 Insight
    
    这样用户可以在 Insights 视图中查看历史 Playbook
    """
    try:
        from backend.services.memory import MemoryService, PrivacyLevel
        
        memory_service = MemoryService()
        
        # 记录事件
        event_id = await memory_service.record_event(
            user_id=user_id,
            event_type=f"{playbook_type}_playbook_generated",
            data={
                "playbook_id": playbook.playbook_id,
                "playbook_type": playbook.playbook_type.value,
                "date_range": playbook.date_range,
                "overall_score": playbook.overall_score,
                "section_count": len(playbook.sections),
            },
            privacy_level=PrivacyLevel.PRIVATE,
        )
        
        # 创建 Insight
        insight_id = await memory_service.create_insight(
            user_id=user_id,
            summary=f"月报 ({playbook.date_range}): {playbook.summary[:100]}",
            source_events=[event_id],
            confidence=0.9,
            dimension="playbook",
            privacy_level=PrivacyLevel.PRIVATE,
        )
        
        logger.info(f"Saved {playbook_type} playbook as insight {insight_id}")
        return insight_id
    
    except Exception as e:
        logger.warning(f"Failed to save playbook as insight: {e}")
        return None


# =============================================================================
# 年度 Playbook（生日触发）
# =============================================================================

async def run_birthday_playbook(user_id: str, birth_date: date) -> Optional[str]:
    """
    生成生日年度 Playbook
    
    在用户生日当天调用。
    
    Args:
        user_id: 用户 ID
        birth_date: 用户出生日期
        
    Returns:
        playbook_id 或 None
    """
    try:
        from backend.services.playbook.generator import (
            PlaybookGenerator,
            PlaybookType,
        )
        
        # 计算过去一年的范围
        today = date.today()
        year_start = today.replace(year=today.year - 1)
        
        generator = PlaybookGenerator()
        
        # 使用 MONTHLY 类型但生成年度内容（后续可扩展 YEARLY 类型）
        playbook = await generator.generate(
            user_id=user_id,
            playbook_type=PlaybookType.MONTHLY,  # TODO: 添加 YEARLY 类型
            target_date=today,
            use_cache=False,
        )
        
        # 记录为年度 Playbook
        await _save_playbook_as_insight(user_id, playbook, "yearly")
        
        logger.info(
            f"Generated birthday playbook {playbook.playbook_id} for user {user_id}"
        )
        return playbook.playbook_id
    
    except Exception as e:
        logger.error(f"Failed to generate birthday playbook for {user_id}: {e}")
        return None
