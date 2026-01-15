"""
Timeline Route

时间线端点 - 聚合梦境、分析结果、洞察数据。
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

router = APIRouter(prefix="/timeline", tags=["Timeline"])


# ==================== 模型定义 ====================

class TimelineEvent(BaseModel):
    """时间线事件"""
    id: str
    type: str  # dream, reading, insight, note
    title: str
    summary: str
    timestamp: str
    metadata: Dict = Field(default_factory=dict)


class PersonalEntry(BaseModel):
    """个人记录"""
    id: str
    type: str  # dream, note, mood
    content: str
    timestamp: str
    tags: List[str] = []


class LucidInsight(BaseModel):
    """Lucid洞察"""
    id: str
    source: str  # bazi, astro, dream_pattern
    title: str
    content: str
    timestamp: str
    relevance: float = Field(ge=0.0, le=1.0)


class TimelineResponse(BaseModel):
    """时间线响应"""
    personal: List[PersonalEntry]
    insights: List[LucidInsight]
    events: List[TimelineEvent]
    correlations: List[Dict] = []
    time_range: Dict[str, str]


# ==================== 数据库依赖 ====================

async def get_dream_service(db: AsyncSession = Depends(get_db)) -> DreamService:
    return DreamService(db)


# ==================== API端点 ====================

@router.get("/combined", response_model=TimelineResponse)
async def get_combined_timeline(
    user_id: str = Query(..., description="用户ID"),
    scale: str = Query(default="day", description="时间粒度: hour/day/week/month/year"),
    start: Optional[str] = Query(None, description="开始时间 ISO格式"),
    end: Optional[str] = Query(None, description="结束时间 ISO格式"),
    limit: int = Query(default=50, ge=1, le=200),
    dream_service: DreamService = Depends(get_dream_service),
):
    """
    获取合并时间线
    
    聚合用户的梦境记录、命理解读、洞察等数据。
    """
    # 计算时间范围
    now = datetime.utcnow()
    if end:
        end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
    else:
        end_dt = now
    
    if start:
        start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
    else:
        # 根据scale计算默认范围
        scale_deltas = {
            "hour": timedelta(hours=24),
            "day": timedelta(days=7),
            "week": timedelta(weeks=4),
            "month": timedelta(days=90),
            "year": timedelta(days=365),
        }
        start_dt = end_dt - scale_deltas.get(scale, timedelta(days=7))
    
    # 获取梦境记录
    dreams, _ = await dream_service.list_dreams(user_id, limit=limit, offset=0)
    
    personal_entries = []
    events = []
    
    for dream in dreams:
        dream_id = f"dream_{dream.id}"
        content = dream.final_content or ""
        created_at = dream.created_at.isoformat() if dream.created_at else datetime.utcnow().isoformat()
        
        # 转换为PersonalEntry
        personal_entries.append(PersonalEntry(
            id=dream_id,
            type="dream",
            content=content[:100] + "..." if len(content) > 100 else content,
            timestamp=created_at,
            tags=dream.tags or [],
        ))
        
        # 转换为TimelineEvent
        events.append(TimelineEvent(
            id=dream_id,
            type="dream",
            title=dream.title or "梦境记录",
            summary=content[:50] + "..." if len(content) > 50 else content,
            timestamp=created_at,
            metadata={"mood": dream.mood, "clarity": dream.clarity}
        ))
    
    # 生成示例洞察
    insights = _generate_sample_insights(user_id, scale)
    
    # 计算关联
    correlations = _find_correlations(personal_entries, insights)
    
    return TimelineResponse(
        personal=personal_entries[:limit],
        insights=insights[:limit],
        events=events[:limit],
        correlations=correlations,
        time_range={
            "start": start_dt.isoformat(),
            "end": end_dt.isoformat(),
            "scale": scale,
        }
    )


@router.get("/personal", response_model=List[PersonalEntry])
async def get_personal_timeline(
    user_id: str,
    limit: int = Query(default=20, ge=1, le=100),
    dream_service: DreamService = Depends(get_dream_service),
):
    """获取个人记录时间线"""
    dreams, _ = await dream_service.list_dreams(user_id, limit=limit, offset=0)
    
    entries = []
    for dream in dreams:
        content = dream.final_content or ""
        created_at = dream.created_at.isoformat() if dream.created_at else datetime.utcnow().isoformat()
        entries.append(PersonalEntry(
            id=f"dream_{dream.id}",
            type="dream",
            content=content,
            timestamp=created_at,
            tags=dream.tags or [],
        ))
    
    return entries


@router.get("/insights", response_model=List[LucidInsight])
async def get_insights_timeline(
    user_id: str,
    limit: int = Query(default=10, ge=1, le=50),
):
    """获取洞察时间线"""
    return _generate_sample_insights(user_id, "day")[:limit]


# ==================== 辅助函数 ====================

def _generate_sample_insights(user_id: str, scale: str) -> List[LucidInsight]:
    """生成示例洞察（后续接入真实分析）"""
    now = datetime.utcnow()
    
    insights = [
        LucidInsight(
            id=f"insight_{user_id}_1",
            source="bazi",
            title="今日运势提示",
            content="今日适宜深度思考，不宜仓促决策。",
            timestamp=now.isoformat(),
            relevance=0.85,
        ),
        LucidInsight(
            id=f"insight_{user_id}_2",
            source="dream_pattern",
            title="梦境模式发现",
            content="近期梦境中多次出现水元素，可能与情绪流动有关。",
            timestamp=(now - timedelta(days=1)).isoformat(),
            relevance=0.72,
        ),
        LucidInsight(
            id=f"insight_{user_id}_3",
            source="astro",
            title="星象提示",
            content="本周水星逆行，注意沟通表达。",
            timestamp=(now - timedelta(days=2)).isoformat(),
            relevance=0.68,
        ),
    ]
    
    return insights


def _find_correlations(personal: List[PersonalEntry], insights: List[LucidInsight]) -> List[Dict]:
    """发现记录与洞察的关联"""
    correlations = []
    
    # 简单关联：时间接近的记录和洞察
    for entry in personal[:5]:
        for insight in insights[:3]:
            correlations.append({
                "personal_id": entry.id,
                "insight_id": insight.id,
                "correlation_type": "temporal",
                "strength": 0.6,
            })
    
    return correlations[:10]
