"""
Weekly Playbook Job

每周日 21:00 生成周 Playbook。

流程:
1. 查询活跃用户（7天内有登录）
2. 聚合用户本周 Insight
3. 调用 PlaybookGenerator 生成周报
4. 保存周 Playbook

对照 roadmap: .kiro/docs/ls_implementation_roadmap.md §2.4.3
"""

import logging
from datetime import date, datetime, timedelta
from typing import List, Optional

from sqlalchemy import select, and_
from sqlalchemy.sql import func

from backend.db.session import async_session_maker

logger = logging.getLogger(__name__)

BATCH_SIZE = 50
MIN_INSIGHTS_FOR_WEEKLY = 3  # 生成周报需要的最少 Insight 数


async def run_weekly_playbook() -> dict:
    """
    执行周 Playbook 批量生成
    
    Returns:
        执行报告
    """
    start_time = datetime.utcnow()
    
    # 计算本周范围
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    
    logger.info(f"Starting weekly playbook generation for {week_start} - {week_end}")
    
    report = {
        "week_start": week_start.isoformat(),
        "week_end": week_end.isoformat(),
        "total_users": 0,
        "generated": 0,
        "skipped": 0,
        "failed": [],
        "duration_seconds": 0,
    }
    
    try:
        # 获取活跃用户
        user_ids = await _get_active_users(days=7)
        report["total_users"] = len(user_ids)
        
        if not user_ids:
            logger.info("No active users, skipping")
            return report
        
        # 分批处理
        for i in range(0, len(user_ids), BATCH_SIZE):
            batch = user_ids[i:i + BATCH_SIZE]
            
            for user_id in batch:
                try:
                    # 检查用户本周是否有足够数据
                    insight_count = await _get_user_week_insight_count(
                        user_id, week_start, week_end
                    )
                    
                    if insight_count < MIN_INSIGHTS_FOR_WEEKLY:
                        # 数据不足，跳过
                        report["skipped"] += 1
                        logger.debug(f"Skipping user {user_id}: only {insight_count} insights")
                        continue
                    
                    # 生成周 Playbook
                    playbook_id = await _generate_weekly_playbook(user_id, week_start, week_end)
                    if playbook_id:
                        report["generated"] += 1
                    else:
                        report["skipped"] += 1
                    
                except Exception as e:
                    logger.error(f"Failed to generate weekly playbook for {user_id}: {e}")
                    report["failed"].append(user_id)
            
            logger.info(
                f"Processed batch {i // BATCH_SIZE + 1}, "
                f"generated: {report['generated']}, skipped: {report['skipped']}"
            )
    
    except Exception as e:
        logger.error(f"Weekly playbook generation failed: {e}")
        raise
    
    finally:
        report["duration_seconds"] = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"Weekly playbook completed: {report}")
    
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
            # 查询有最近活动的用户
            # 方法1: 从 UserProfile 的 last_login 获取
            user_result = await session.execute(
                select(UserProfile.user_id)
                .where(UserProfile.last_login >= cutoff)
                .distinct()
            )
            active_from_login = set(row[0] for row in user_result.fetchall())
            
            # 方法2: 从 TODO 条目获取
            todo_result = await session.execute(
                select(TodoEntry.user_id)
                .where(TodoEntry.created_at >= cutoff)
                .distinct()
            )
            active_from_todo = set(row[0] for row in todo_result.fetchall())
            
            # 合并
            all_active = active_from_login | active_from_todo
            
            logger.info(
                f"Found {len(all_active)} active users "
                f"(login: {len(active_from_login)}, todo: {len(active_from_todo)})"
            )
            
            return list(all_active)
    
    except Exception as e:
        logger.warning(f"Failed to get active users from DB, returning empty: {e}")
        return []


async def _get_user_week_insight_count(
    user_id: str,
    week_start: date,
    week_end: date,
) -> int:
    """获取用户本周 Insight 数量"""
    try:
        from backend.services.memory import MemoryService
        
        memory_service = MemoryService()
        
        # 获取时间范围内的 insights
        start_dt = datetime.combine(week_start, datetime.min.time())
        insights = await memory_service.get_insights(user_id)
        
        # 过滤本周的
        week_insights = [
            ins for ins in insights
            if hasattr(ins, 'created_at') and ins.created_at >= start_dt
        ]
        
        return len(week_insights) if week_insights else 0
    
    except Exception as e:
        logger.warning(f"Failed to count insights for {user_id}: {e}")
        return 0


async def _generate_weekly_playbook(
    user_id: str,
    week_start: date,
    week_end: date,
) -> Optional[str]:
    """
    生成周 Playbook
    
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
        
        # 生成周报
        playbook = await generator.generate(
            user_id=user_id,
            playbook_type=PlaybookType.WEEKLY,
            target_date=week_end,  # 使用周末作为目标日期
            use_cache=False,  # 批量生成不使用缓存
        )
        
        # 保存到记忆层（作为 Insight）
        await _save_playbook_as_insight(user_id, playbook)
        
        logger.info(f"Generated weekly playbook {playbook.playbook_id} for user {user_id}")
        return playbook.playbook_id
    
    except Exception as e:
        logger.error(f"Failed to generate weekly playbook for {user_id}: {e}")
        return None


async def _save_playbook_as_insight(user_id: str, playbook) -> Optional[str]:
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
            event_type="weekly_playbook_generated",
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
            summary=f"周报 ({playbook.date_range}): {playbook.summary[:100]}",
            source_events=[event_id],
            confidence=0.9,
            dimension="playbook",
            privacy_level=PrivacyLevel.PRIVATE,
        )
        
        logger.info(f"Saved playbook as insight {insight_id}")
        return insight_id
    
    except Exception as e:
        logger.warning(f"Failed to save playbook as insight: {e}")
        return None
