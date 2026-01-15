"""
Version Calibration Job

定期校准版本树，检测行为偏差并生成新分支。

流程:
1. 查询有行为偏差的用户
2. 对比实际行为与预测版本
3. 调用 VersionTreeService 生成新分支
4. 更新用户的当前版本路径
5. 通知用户（Insight 推送）

对照 roadmap: .kiro/docs/ls_implementation_roadmap.md §2.4.4
"""

import logging
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional, Tuple

from sqlalchemy import select

from backend.db.session import async_session_maker

logger = logging.getLogger(__name__)

BATCH_SIZE = 50
DEVIATION_THRESHOLD = 0.3  # 偏差阈值，超过此值认为需要校准
MIN_ACTIONS_FOR_CALIBRATION = 5  # 校准需要的最少行为记录数


async def run_version_calibration() -> dict:
    """
    执行版本树校准
    
    通常每周执行一次，检测用户实际行为与版本预测的偏差。
    
    Returns:
        执行报告
    """
    start_time = datetime.utcnow()
    
    # 计算校准检查周期（过去7天）
    today = date.today()
    period_start = today - timedelta(days=7)
    
    logger.info(f"Starting version calibration for period {period_start} - {today}")
    
    report = {
        "period_start": period_start.isoformat(),
        "period_end": today.isoformat(),
        "total_users": 0,
        "checked_users": 0,
        "calibrated_users": 0,
        "new_branches": 0,
        "skipped_users": 0,
        "failed_users": [],
        "duration_seconds": 0,
    }
    
    try:
        # 获取有版本树的用户
        user_ids = await _get_users_with_trees()
        report["total_users"] = len(user_ids)
        
        if not user_ids:
            logger.info("No users with version trees, skipping calibration")
            return report
        
        # 分批处理
        for i in range(0, len(user_ids), BATCH_SIZE):
            batch = user_ids[i:i + BATCH_SIZE]
            
            for user_id in batch:
                try:
                    # 检查用户是否有足够的行为数据
                    action_count = await _get_user_action_count(user_id, period_start)
                    
                    if action_count < MIN_ACTIONS_FOR_CALIBRATION:
                        report["skipped_users"] += 1
                        logger.debug(f"Skipping user {user_id}: only {action_count} actions")
                        continue
                    
                    report["checked_users"] += 1
                    
                    # 计算偏差度
                    deviation = await _calculate_deviation(user_id, period_start, today)
                    
                    if deviation < DEVIATION_THRESHOLD:
                        # 偏差在可接受范围内，无需校准
                        continue
                    
                    # 需要校准 - 创建新分支
                    branch_created = await _calibrate_user_version(
                        user_id=user_id,
                        deviation=deviation,
                        period_start=period_start,
                    )
                    
                    if branch_created:
                        report["calibrated_users"] += 1
                        report["new_branches"] += 1
                    
                except Exception as e:
                    logger.error(f"Failed to calibrate user {user_id}: {e}")
                    report["failed_users"].append(user_id)
            
            logger.info(
                f"Processed batch {i // BATCH_SIZE + 1}, "
                f"checked: {report['checked_users']}, calibrated: {report['calibrated_users']}"
            )
    
    except Exception as e:
        logger.error(f"Version calibration failed: {e}")
        raise
    
    finally:
        report["duration_seconds"] = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"Version calibration completed: {report}")
    
    return report


async def _get_users_with_trees() -> List[str]:
    """获取有版本树的用户列表"""
    try:
        from backend.models.version_tree import VersionTree
        
        async with async_session_maker() as session:
            result = await session.execute(
                select(VersionTree.user_id).distinct()
            )
            user_ids = [row[0] for row in result.fetchall()]
            
            logger.info(f"Found {len(user_ids)} users with version trees")
            return user_ids
    
    except Exception as e:
        logger.warning(f"Failed to get users with trees: {e}")
        return []


async def _get_user_action_count(user_id: str, since: date) -> int:
    """获取用户指定周期内的行为数量"""
    try:
        from backend.models.todo import TodoEntry
        
        start_dt = datetime.combine(since, datetime.min.time())
        
        async with async_session_maker() as session:
            result = await session.execute(
                select(TodoEntry.todo_id)
                .where(TodoEntry.user_id == user_id)
                .where(TodoEntry.created_at >= start_dt)
            )
            return len(result.fetchall())
    
    except Exception as e:
        logger.warning(f"Failed to count actions for {user_id}: {e}")
        return 0


async def _calculate_deviation(
    user_id: str,
    period_start: date,
    period_end: date,
) -> float:
    """
    计算用户实际行为与版本预测的偏差度
    
    偏差度计算逻辑:
    1. 获取用户当前版本的预测特征
    2. 获取用户本周期的实际行为特征
    3. 计算两者的余弦相似度
    4. 返回 1 - similarity 作为偏差度
    
    Returns:
        偏差度 [0, 1]，值越大偏差越大
    """
    try:
        # 获取用户当前版本的预测维度分数
        predicted_scores = await _get_predicted_dimension_scores(user_id)
        
        # 获取用户实际行为的维度分数
        actual_scores = await _get_actual_dimension_scores(
            user_id, period_start, period_end
        )
        
        if not predicted_scores or not actual_scores:
            return 0.0  # 数据不足，不触发校准
        
        # 计算偏差
        deviation = _calculate_dimension_deviation(predicted_scores, actual_scores)
        
        logger.debug(
            f"User {user_id} deviation: {deviation:.3f} "
            f"(predicted={predicted_scores}, actual={actual_scores})"
        )
        
        return deviation
    
    except Exception as e:
        logger.warning(f"Failed to calculate deviation for {user_id}: {e}")
        return 0.0


async def _get_predicted_dimension_scores(user_id: str) -> Dict[str, float]:
    """获取用户当前版本的预测维度分数"""
    try:
        from backend.services.version_tree.service import get_version_tree_service
        
        service = get_version_tree_service(persist=True)
        trees = await service.get_user_trees(user_id)
        
        if not trees:
            return {}
        
        # 取最近更新的树
        latest_tree = max(trees, key=lambda t: t.updated_at)
        current_node = latest_tree.nodes.get(latest_tree.current_node_id)
        
        if not current_node:
            return {}
        
        # 从版本 ID 推断维度分数（简化实现）
        # 实际应该从 LifeVersion 模型获取详细分数
        return {
            "career": 0.5,
            "wealth": 0.5,
            "relationship": 0.5,
            "health": 0.5,
        }
    
    except Exception as e:
        logger.warning(f"Failed to get predicted scores for {user_id}: {e}")
        return {}


async def _get_actual_dimension_scores(
    user_id: str,
    period_start: date,
    period_end: date,
) -> Dict[str, float]:
    """
    获取用户实际行为的维度分数
    
    从用户的 TODO/DONE 条目中提取意图，计算各维度的活跃度。
    """
    try:
        from backend.services.memory import MemoryService
        
        memory_service = MemoryService(persist=True)
        
        start_dt = datetime.combine(period_start, datetime.min.time())
        
        # 获取用户意图事件
        events = await memory_service.get_events(
            user_id=user_id,
            since=start_dt,
            event_type="user_intent",
        )
        
        if not events:
            return {}
        
        # 统计各类别的行为数量
        category_counts: Dict[str, int] = {}
        for event in events:
            category = event.data.get("category", "other")
            category_counts[category] = category_counts.get(category, 0) + 1
        
        total = sum(category_counts.values())
        if total == 0:
            return {}
        
        # 映射到维度分数
        dimension_mapping = {
            "work": "career",
            "learning": "career",
            "health": "health",
            "social": "relationship",
            "leisure": "relationship",
        }
        
        dimension_scores: Dict[str, float] = {
            "career": 0.0,
            "wealth": 0.0,
            "relationship": 0.0,
            "health": 0.0,
        }
        
        for category, count in category_counts.items():
            dimension = dimension_mapping.get(category)
            if dimension:
                dimension_scores[dimension] += count / total
        
        return dimension_scores
    
    except Exception as e:
        logger.warning(f"Failed to get actual scores for {user_id}: {e}")
        return {}


def _calculate_dimension_deviation(
    predicted: Dict[str, float],
    actual: Dict[str, float],
) -> float:
    """
    计算维度分数偏差
    
    使用均方误差计算偏差度。
    """
    all_dims = set(predicted.keys()) | set(actual.keys())
    if not all_dims:
        return 0.0
    
    total_diff = 0.0
    for dim in all_dims:
        pred_val = predicted.get(dim, 0.0)
        actual_val = actual.get(dim, 0.0)
        total_diff += (pred_val - actual_val) ** 2
    
    mse = total_diff / len(all_dims)
    # 归一化到 [0, 1]
    return min(1.0, mse ** 0.5)


async def _calibrate_user_version(
    user_id: str,
    deviation: float,
    period_start: date,
) -> bool:
    """
    校准用户版本 - 创建新分支
    
    Args:
        user_id: 用户 ID
        deviation: 偏差度
        period_start: 校准周期开始日期
        
    Returns:
        是否成功创建分支
    """
    try:
        from backend.services.version_tree.service import get_version_tree_service
        from backend.services.memory import MemoryService, PrivacyLevel
        from backend.core.contracts.life_version_models import LifeVersion
        
        # 获取当前版本树
        tree_service = get_version_tree_service(persist=True)
        trees = await tree_service.get_user_trees(user_id)
        
        if not trees:
            return False
        
        latest_tree = max(trees, key=lambda t: t.updated_at)
        
        # 创建新的校准版本
        calibrated_version = LifeVersion(
            version_id=f"ver_{datetime.utcnow().strftime('%Y%m%d')}_{user_id[:8]}",
            name=f"校准版本 ({period_start.isoformat()})",
            description=f"基于行为偏差({deviation:.2f})自动校准生成",
            dimension_weights={},
            factor_adjustments={},
        )
        
        # 添加分支
        new_node = await tree_service.add_branch(
            tree_id=latest_tree.tree_id,
            parent_node_id=latest_tree.current_node_id,
            version=calibrated_version,
        )
        
        # 记录决策
        await tree_service.record_decision(
            tree_id=latest_tree.tree_id,
            node_id=new_node.node_id,
            option=f"auto_calibration_{deviation:.2f}",
            context={
                "deviation": deviation,
                "period_start": period_start.isoformat(),
                "trigger": "scheduled_calibration",
            },
        )
        
        # 生成 Insight 通知
        memory_service = MemoryService(persist=True)
        
        await memory_service.create_insight(
            user_id=user_id,
            summary=f"系统检测到您近期的行为与原有版本预测存在{deviation*100:.0f}%的偏差，"
                    f"已自动为您生成一个更贴合当前状态的新版本分支。",
            source_events=[],
            confidence=0.85,
            dimension="version_calibration",
            privacy_level=PrivacyLevel.PRIVATE,
        )
        
        logger.info(
            f"Calibrated version for user {user_id}: "
            f"deviation={deviation:.3f}, new_node={new_node.node_id}"
        )
        
        return True
    
    except Exception as e:
        logger.error(f"Failed to calibrate version for {user_id}: {e}")
        return False


# =============================================================================
# 便捷函数
# =============================================================================

async def calibrate_single_user(user_id: str) -> Optional[float]:
    """
    校准单个用户（手动触发）
    
    Returns:
        偏差度，或 None 如果校准失败
    """
    period_start = date.today() - timedelta(days=7)
    period_end = date.today()
    
    deviation = await _calculate_deviation(user_id, period_start, period_end)
    
    if deviation >= DEVIATION_THRESHOLD:
        await _calibrate_user_version(user_id, deviation, period_start)
    
    return deviation
