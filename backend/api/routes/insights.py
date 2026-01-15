"""
Insights Route

深度洞察端点 - 基于历史数据生成个性化洞察。
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import get_db
from backend.api.services.dream_service import DreamService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/insights", tags=["Insights"])


# ==================== 模型定义 ====================

class InsightSource(BaseModel):
    """洞察来源"""
    type: str  # pattern, dream, reading, correlation
    id: str
    title: str


class DeepInsight(BaseModel):
    """深度洞察"""
    id: str
    title: str
    content: str
    category: str  # self_awareness, growth, warning, opportunity
    depth: str  # surface, medium, deep
    confidence: float = Field(ge=0.0, le=1.0)
    sources: List[InsightSource]
    created_at: str
    actionable: bool = True
    action_suggestions: List[str] = []


class InsightsResponse(BaseModel):
    """洞察列表响应"""
    insights: List[DeepInsight]
    summary: str
    total: int
    generated_at: str


class InsightFeedback(BaseModel):
    """洞察反馈"""
    insight_id: str
    helpful: bool
    comment: Optional[str] = None


# ==================== 数据库依赖 ====================

async def get_dream_service(db: AsyncSession = Depends(get_db)) -> DreamService:
    return DreamService(db)


# ==================== API端点 ====================

@router.get("/deep", response_model=InsightsResponse)
async def get_deep_insights(
    user_id: str = Query(..., description="用户ID"),
    category: Optional[str] = Query(None, description="分类过滤"),
    depth: Optional[str] = Query(None, description="深度过滤: surface/medium/deep"),
    limit: int = Query(default=10, ge=1, le=50),
    dream_service: DreamService = Depends(get_dream_service),
):
    """
    获取深度洞察
    
    基于用户的历史数据（梦境、模式、命理解读）生成个性化洞察。
    """
    insights = await _generate_deep_insights_async(user_id, dream_service)
    
    # 过滤
    if category:
        insights = [i for i in insights if i.category == category]
    if depth:
        insights = [i for i in insights if i.depth == depth]
    
    # 按置信度排序
    insights.sort(key=lambda x: x.confidence, reverse=True)
    
    # 生成摘要
    summary = _generate_summary(insights)
    
    return InsightsResponse(
        insights=insights[:limit],
        summary=summary,
        total=len(insights),
        generated_at=datetime.utcnow().isoformat(),
    )


@router.get("/daily", response_model=DeepInsight)
async def get_daily_insight(
    user_id: str,
    dream_service: DreamService = Depends(get_dream_service),
):
    """获取今日洞察"""
    insights = await _generate_deep_insights_async(user_id, dream_service)
    
    # 返回置信度最高的一个
    if insights:
        return max(insights, key=lambda x: x.confidence)
    
    # 默认洞察
    return DeepInsight(
        id=f"daily_{user_id}_{datetime.utcnow().date().isoformat()}",
        title="今日觉察",
        content="保持对内在声音的倾听，每一个梦境和感受都是了解自己的窗口。",
        category="self_awareness",
        depth="surface",
        confidence=0.5,
        sources=[],
        created_at=datetime.utcnow().isoformat(),
        actionable=True,
        action_suggestions=["记录今晚的梦境", "花5分钟静心冥想"],
    )


@router.post("/feedback")
async def submit_insight_feedback(feedback: InsightFeedback):
    """提交洞察反馈"""
    # TODO: 存储反馈用于改进洞察生成
    logger.info(f"Insight feedback: {feedback.insight_id}, helpful={feedback.helpful}")
    return {"success": True, "message": "感谢您的反馈"}


# ==================== 辅助函数 ====================

async def _generate_deep_insights_async(user_id: str, dream_service: DreamService) -> List[DeepInsight]:
    """生成深度洞察"""
    now = datetime.utcnow()
    insights = []
    
    # 从梦境数据生成洞察
    dreams, total = await dream_service.list_dreams(user_id, limit=50, offset=0)
    
    if dreams:
        insights.append(DeepInsight(
            id=f"insight_{user_id}_dream_summary",
            title="梦境主题洞察",
            content=f"根据你记录的{len(dreams)}个梦境，发现了一些值得关注的主题。",
            category="self_awareness",
            depth="medium",
            confidence=0.75,
            sources=[
                InsightSource(type="dream", id=f"dream_{d.id}", title=d.title or "梦境记录")
                for d in dreams[:3]
            ],
            created_at=now.isoformat(),
            actionable=True,
            action_suggestions=[
                "继续保持梦境记录的习惯",
                "尝试在清醒时回顾梦境细节",
            ],
        ))
    
    # 从模式生成洞察
    from backend.api.routes.patterns import _get_or_generate_patterns_async
    patterns = await _get_or_generate_patterns_async(user_id, dream_service)
    
    for pattern in patterns[:2]:  # 前2个模式
        insights.append(DeepInsight(
            id=f"insight_{user_id}_pattern_{pattern.id}",
            title=f"关于「{pattern.name}」的洞察",
            content=f"{pattern.description}。这个模式的强度为{pattern.strength:.0%}，值得你进一步关注。",
            category="growth",
            depth="deep" if pattern.strength > 0.7 else "medium",
            confidence=pattern.strength,
            sources=[
                InsightSource(type="pattern", id=pattern.id, title=pattern.name)
            ],
            created_at=now.isoformat(),
            actionable=True,
            action_suggestions=[
                f"观察日常生活中与{pattern.name}相关的事件",
                "记录你对这个模式的感受和想法",
            ],
        ))
    
    # 添加通用洞察
    insights.extend(_get_general_insights(user_id))
    
    return insights


def _get_general_insights(user_id: str) -> List[DeepInsight]:
    """获取通用洞察"""
    now = datetime.utcnow()
    
    return [
        DeepInsight(
            id=f"insight_{user_id}_awareness",
            title="内在觉察",
            content="自我觉察是成长的第一步。通过记录梦境和日常感受，你正在建立与内在自我的连接。",
            category="self_awareness",
            depth="surface",
            confidence=0.6,
            sources=[],
            created_at=now.isoformat(),
            actionable=True,
            action_suggestions=[
                "每天花几分钟回顾一天的感受",
                "注意身体发出的信号",
            ],
        ),
        DeepInsight(
            id=f"insight_{user_id}_growth",
            title="成长机会",
            content="每一个重复出现的模式都是成长的机会。不要回避它们，而是好奇地探索。",
            category="opportunity",
            depth="medium",
            confidence=0.65,
            sources=[],
            created_at=now.isoformat(),
            actionable=True,
            action_suggestions=[
                "对重复出现的主题保持开放态度",
                "尝试从不同角度理解这些模式",
            ],
        ),
    ]


def _generate_summary(insights: List[DeepInsight]) -> str:
    """生成洞察摘要"""
    if not insights:
        return "暂无足够数据生成洞察，请继续记录你的梦境和感受。"
    
    categories = set(i.category for i in insights)
    high_confidence = [i for i in insights if i.confidence > 0.7]
    
    summary_parts = []
    summary_parts.append(f"共发现{len(insights)}个洞察")
    
    if high_confidence:
        summary_parts.append(f"其中{len(high_confidence)}个高置信度")
    
    if "self_awareness" in categories:
        summary_parts.append("包含自我觉察相关内容")
    
    if "opportunity" in categories:
        summary_parts.append("发现成长机会")
    
    return "。".join(summary_parts) + "。"
