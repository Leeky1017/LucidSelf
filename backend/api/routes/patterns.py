"""
Patterns Route

模式识别端点 - 发现用户数据中的规律和模式。
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import get_db
from backend.api.services.dream_service import DreamService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/patterns", tags=["Patterns"])


# ==================== 模型定义 ====================

class PatternEvidence(BaseModel):
    """模式证据"""
    source_id: str
    source_type: str  # dream, reading, note
    excerpt: str
    timestamp: str
    relevance: float


class Pattern(BaseModel):
    """识别到的模式"""
    id: str
    name: str
    category: str  # dream, work, relationship, spiritual, body
    description: str
    frequency: str  # daily, weekly, monthly, rare
    strength: float = Field(ge=0.0, le=1.0)
    first_seen: str
    last_seen: str
    occurrences: int
    evidence: List[PatternEvidence] = []
    tags: List[str] = []


class CorePattern(BaseModel):
    """核心模式（高频、高强度）"""
    id: str
    name: str
    category: str
    description: str
    strength: float
    insight: str


class PatternsResponse(BaseModel):
    """模式列表响应"""
    patterns: List[Pattern]
    core_patterns: List[CorePattern]
    total: int
    categories: Dict[str, int]


class PatternDetailResponse(BaseModel):
    """模式详情响应"""
    pattern: Pattern
    related_patterns: List[str]
    recommendations: List[str]


# ==================== 数据库依赖 ====================

async def get_dream_service(db: AsyncSession = Depends(get_db)) -> DreamService:
    return DreamService(db)


# ==================== 缓存 ====================

_pattern_cache: Dict[str, List[Pattern]] = {}


# ==================== API端点 ====================

@router.get("", response_model=PatternsResponse)
async def get_patterns(
    user_id: str = Query(..., description="用户ID"),
    category: Optional[str] = Query(None, description="分类过滤"),
    min_strength: float = Query(default=0.0, ge=0.0, le=1.0),
    limit: int = Query(default=20, ge=1, le=100),
    dream_service: DreamService = Depends(get_dream_service),
):
    """
    获取用户的模式列表
    
    分析用户历史数据，识别重复出现的模式。
    """
    # 获取或生成用户模式
    patterns = await _get_or_generate_patterns_async(user_id, dream_service)
    
    # 过滤
    if category:
        patterns = [p for p in patterns if p.category == category]
    
    patterns = [p for p in patterns if p.strength >= min_strength]
    
    # 排序（按强度降序）
    patterns.sort(key=lambda x: x.strength, reverse=True)
    
    # 统计分类
    categories: Dict[str, int] = {}
    for p in patterns:
        categories[p.category] = categories.get(p.category, 0) + 1
    
    # 提取核心模式
    core_patterns = [
        CorePattern(
            id=p.id,
            name=p.name,
            category=p.category,
            description=p.description,
            strength=p.strength,
            insight=_generate_pattern_insight(p),
        )
        for p in patterns[:3]  # 前3个作为核心模式
    ]
    
    return PatternsResponse(
        patterns=patterns[:limit],
        core_patterns=core_patterns,
        total=len(patterns),
        categories=categories,
    )


@router.get("/{pattern_id}", response_model=PatternDetailResponse)
async def get_pattern_detail(
    pattern_id: str,
    user_id: str = Query(..., description="用户ID"),
    dream_service: DreamService = Depends(get_dream_service),
):
    """获取模式详情"""
    patterns = await _get_or_generate_patterns_async(user_id, dream_service)
    
    pattern = next((p for p in patterns if p.id == pattern_id), None)
    if not pattern:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pattern not found: {pattern_id}"
        )
    
    # 找到相关模式
    related = [p.id for p in patterns if p.category == pattern.category and p.id != pattern_id][:5]
    
    # 生成建议
    recommendations = _generate_recommendations(pattern)
    
    return PatternDetailResponse(
        pattern=pattern,
        related_patterns=related,
        recommendations=recommendations,
    )


# ==================== 辅助函数 ====================

async def _get_or_generate_patterns_async(user_id: str, dream_service: DreamService) -> List[Pattern]:
    """获取或生成用户模式"""
    if user_id in _pattern_cache:
        return _pattern_cache[user_id]
    
    # 从梦境数据生成模式
    dreams, _ = await dream_service.list_dreams(user_id, limit=100, offset=0)
    
    patterns = []
    now = datetime.utcnow()
    
    # 分析梦境标签和情绪
    tag_counts: Dict[str, int] = {}
    mood_counts: Dict[str, int] = {}
    
    for dream in dreams:
        for tag in (dream.tags or []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        if dream.mood:
            mood_counts[dream.mood] = mood_counts.get(dream.mood, 0) + 1
    
    # 从标签生成模式
    for tag, count in tag_counts.items():
        if count >= 1:  # 出现至少1次
            patterns.append(Pattern(
                id=f"pattern_{user_id}_{tag}",
                name=f"{tag}主题",
                category="dream",
                description=f"你的梦境中经常出现{tag}相关内容",
                frequency="weekly" if count >= 3 else "monthly",
                strength=min(0.5 + count * 0.1, 1.0),
                first_seen=now.isoformat(),
                last_seen=now.isoformat(),
                occurrences=count,
                evidence=[],
                tags=[tag],
            ))
    
    # 从情绪生成模式
    for mood, count in mood_counts.items():
        if count >= 1:
            patterns.append(Pattern(
                id=f"pattern_{user_id}_mood_{mood}",
                name=f"{mood}情绪模式",
                category="spiritual",
                description=f"你经常在{mood}的情绪状态下记录梦境",
                frequency="weekly" if count >= 3 else "monthly",
                strength=min(0.4 + count * 0.15, 1.0),
                first_seen=now.isoformat(),
                last_seen=now.isoformat(),
                occurrences=count,
                evidence=[],
                tags=["emotion", mood],
            ))
    
    # 添加一些示例模式
    if not patterns:
        patterns = _get_sample_patterns(user_id)
    
    _pattern_cache[user_id] = patterns
    return patterns


def _get_sample_patterns(user_id: str) -> List[Pattern]:
    """生成示例模式"""
    now = datetime.utcnow()
    
    return [
        Pattern(
            id=f"pattern_{user_id}_water",
            name="水元素梦境",
            category="dream",
            description="梦境中经常出现水相关场景（大海、河流、雨水）",
            frequency="weekly",
            strength=0.78,
            first_seen=now.isoformat(),
            last_seen=now.isoformat(),
            occurrences=5,
            evidence=[],
            tags=["water", "nature"],
        ),
        Pattern(
            id=f"pattern_{user_id}_flying",
            name="飞翔梦境",
            category="dream",
            description="反复出现飞翔或漂浮的梦境体验",
            frequency="monthly",
            strength=0.65,
            first_seen=now.isoformat(),
            last_seen=now.isoformat(),
            occurrences=3,
            evidence=[],
            tags=["flying", "freedom"],
        ),
        Pattern(
            id=f"pattern_{user_id}_work_stress",
            name="工作压力信号",
            category="work",
            description="梦境和记录中反映出工作相关压力",
            frequency="weekly",
            strength=0.72,
            first_seen=now.isoformat(),
            last_seen=now.isoformat(),
            occurrences=4,
            evidence=[],
            tags=["work", "stress"],
        ),
    ]


def _generate_pattern_insight(pattern: Pattern) -> str:
    """生成模式洞察"""
    insights = {
        "dream": f"这个梦境模式可能反映了你潜意识中的某些重要主题。",
        "work": f"工作相关的模式提示你需要关注职业发展和压力管理。",
        "relationship": f"关系模式可能与你的人际互动方式有关。",
        "spiritual": f"精神层面的模式值得深入探索和反思。",
        "body": f"身体相关的模式提醒你关注健康状态。",
    }
    return insights.get(pattern.category, "这个模式值得进一步关注。")


def _generate_recommendations(pattern: Pattern) -> List[str]:
    """生成模式相关建议"""
    base_recommendations = [
        f"继续记录与「{pattern.name}」相关的经历",
        "尝试在日常中有意识地观察这个模式",
        "考虑这个模式与你当前生活阶段的关联",
    ]
    
    category_recommendations = {
        "dream": ["尝试在入睡前设定意图，探索这个梦境主题"],
        "work": ["设定明确的工作边界", "寻找压力释放的方式"],
        "relationship": ["与信任的人分享你的发现", "反思你的沟通模式"],
        "spiritual": ["尝试冥想或正念练习", "记录你的直觉和感受"],
        "body": ["注意身体发出的信号", "保持规律的作息"],
    }
    
    return base_recommendations + category_recommendations.get(pattern.category, [])
