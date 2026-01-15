"""
Playbook Route

Playbook 命理解读端点。

缓存策略:
- day: 当天生成一次，24小时内返回缓存
- week: 当周生成一次，周日6点或首次访问时生成
- month: 当月最后一天生成下月内容，或首次访问时生成
- year: 当年生成一次
"""

import logging
import time
import uuid
from datetime import datetime, date, timedelta
from typing import Any, Dict, List, Optional

from backend.services.memory.query_selector import get_query_selector

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from backend.api.models import BirthData
from backend.pipeline import Pipeline, PipelineInput, BirthDataInput
from backend.pipeline.orchestrator import get_pipeline
from backend.core.llm import get_orchestrator, ScenarioType
from backend.services.playbook.cache import PlaybookCache

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/playbook", tags=["Playbook"])

# 全局缓存实例
_playbook_cache: Optional[PlaybookCache] = None


def get_playbook_cache() -> PlaybookCache:
    """获取 Playbook 缓存单例"""
    global _playbook_cache
    if _playbook_cache is None:
        _playbook_cache = PlaybookCache(memory_ttl=3600)  # 1小时内存TTL
    return _playbook_cache


def get_cache_key_date(time_scope: str) -> str:
    """
    根据时间范围获取缓存键日期部分
    
    - day: 2024-12-08
    - week: 2024-W49
    - month: 2024-12
    - year: 2024
    """
    today = date.today()
    
    if time_scope == "day":
        return today.isoformat()
    elif time_scope == "week":
        year, week, _ = today.isocalendar()
        return f"{year}-W{week:02d}"
    elif time_scope == "month":
        return today.strftime("%Y-%m")
    elif time_scope == "year":
        return str(today.year)
    else:
        return today.isoformat()


def get_cache_ttl(time_scope: str) -> int:
    """
    根据时间范围获取缓存TTL（秒）
    
    - day: 到第二天0点的剩余时间
    - week: 到下周日的剩余时间  
    - month: 到下月1号的剩余时间
    - year: 到明年1月1号的剩余时间
    """
    now = datetime.now()
    
    if time_scope == "day":
        # 到第二天0点
        tomorrow = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        return int((tomorrow - now).total_seconds())
    elif time_scope == "week":
        # 到下周一0点
        days_until_monday = (7 - now.weekday()) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        next_monday = datetime.combine(now.date() + timedelta(days=days_until_monday), datetime.min.time())
        return int((next_monday - now).total_seconds())
    elif time_scope == "month":
        # 到下月1号
        if now.month == 12:
            next_month = datetime(now.year + 1, 1, 1)
        else:
            next_month = datetime(now.year, now.month + 1, 1)
        return int((next_month - now).total_seconds())
    elif time_scope == "year":
        # 到明年1月1号
        next_year = datetime(now.year + 1, 1, 1)
        return int((next_year - now).total_seconds())
    else:
        return 3600 * 24  # 默认24小时


# ==================== 请求/响应模型 ====================

class PlaybookReadingRequest(BaseModel):
    """Playbook解读请求"""
    user_id: str = Field(..., description="用户ID")
    birth_data: BirthData = Field(..., description="出生数据")
    engines: List[str] = Field(
        default=["bazi", "ziwei", "astro", "tarot"],
        description="启用的引擎"
    )
    time_scope: str = Field(default="day", description="时间范围: day/week/month/year")
    language: str = Field(default="zh", description="输出语言: zh/en/es/de/ja/ko/fr/ar/it/da/pt")


class InlineSource(BaseModel):
    """内联来源标记"""
    start: int
    end: int
    sources: List[str]


class ReadingParagraph(BaseModel):
    """解读段落"""
    text: str
    inline_sources: List[InlineSource] = []


class SourceInfo(BaseModel):
    """来源信息"""
    name: str
    color: str
    description: str
    philosophy: str


class PlaybookReadingResponse(BaseModel):
    """Playbook解读响应"""
    reading_id: str
    time_scope: str
    paragraphs: List[ReadingParagraph]
    sources_used: dict  # engine_id -> SourceInfo
    engines_used: List[str]
    generated_at: str
    processing_time_ms: float


class EngineInfo(BaseModel):
    """引擎信息"""
    id: str
    name: str
    category: str  # eastern/western
    enabled: bool


class EnginesResponse(BaseModel):
    """引擎列表响应"""
    engines: List[EngineInfo]


# ==================== 引擎配置 ====================

ENGINE_CONFIG = {
    "bazi": EngineInfo(id="bazi", name="八字", category="eastern", enabled=True),
    "ziwei": EngineInfo(id="ziwei", name="紫微斗数", category="eastern", enabled=True),
    "astro": EngineInfo(id="astro", name="Astrology", category="western", enabled=True),
    "tarot": EngineInfo(id="tarot", name="Tarot", category="western", enabled=True),
    "yijing": EngineInfo(id="yijing", name="易经", category="eastern", enabled=True),
    "dream": EngineInfo(id="dream", name="Dream", category="western", enabled=True),
    "psych": EngineInfo(id="psych", name="Psychology", category="western", enabled=True),
}

SOURCE_INFO = {
    "bazi": SourceInfo(
        name="八字命理",
        color="#C5A572",
        description="基于四柱八字的传统命理分析",
        philosophy="阴阳五行、天干地支"
    ),
    "ziwei": SourceInfo(
        name="紫微斗数",
        color="#7C4DFF",
        description="以紫微星为主的星曜命理系统",
        philosophy="星曜宫位、四化飞星"
    ),
    "astro": SourceInfo(
        name="西方占星",
        color="#00BFA5",
        description="基于星座和行星的占星分析",
        philosophy="行星相位、宫位守护"
    ),
    "tarot": SourceInfo(
        name="塔罗牌",
        color="#FF6B9D",
        description="通过牌阵解读的象征系统",
        philosophy="大小阿卡那、元素对应"
    ),
}


# ==================== API端点 ====================

@router.get("/engines", response_model=EnginesResponse)
async def get_engines():
    """获取可用引擎列表"""
    return EnginesResponse(engines=list(ENGINE_CONFIG.values()))


@router.post("/reading", response_model=PlaybookReadingResponse)
async def create_reading(request: PlaybookReadingRequest):
    """
    生成Playbook解读
    
    缓存策略：
    - 同一用户+时间范围+日期内只生成一次
    - day: 当天有效
    - week: 当周有效
    - month: 当月有效
    - year: 当年有效
    """
    start_time = time.perf_counter()
    
    # ===== 1. 检查缓存 =====
    cache = get_playbook_cache()
    cache_date = get_cache_key_date(request.time_scope)
    cache_key = PlaybookCache.make_key(request.user_id, request.time_scope, cache_date)
    
    cached_response = cache.get(cache_key)
    if cached_response:
        logger.info(f"Playbook cache HIT: {cache_key}")
        # 返回缓存数据，更新 processing_time
        cached_response["processing_time_ms"] = (time.perf_counter() - start_time) * 1000
        return PlaybookReadingResponse(**cached_response)
    
    logger.info(f"Playbook cache MISS: {cache_key}, generating...")
    
    try:
        # ===== 2. 生成新内容 =====
        birth_data_input = BirthDataInput(
            year=request.birth_data.year,
            month=request.birth_data.month,
            day=request.birth_data.day,
            hour=request.birth_data.hour,
            minute=request.birth_data.minute,
            timezone=request.birth_data.timezone,
            gender=request.birth_data.gender,
            location=request.birth_data.location,
            latitude=request.birth_data.latitude,
            longitude=request.birth_data.longitude,
        )
        
        pipeline_input = PipelineInput(
            user_id=request.user_id,
            birth_data=birth_data_input,
            engines=request.engines,
            include_narrative=False,
            language=request.language,
        )
        
        # 执行Pipeline (L1-L4)
        pipeline = get_pipeline()
        result = await pipeline.execute(pipeline_input)
        
        # 使用 Orchestrator 生成叙事 (L5)
        narrative = await _generate_narrative_by_scope(
            result.fusion_result,
            request.time_scope,
            request.user_id,
            request.language,
            raw_factors=result.raw_factors,
        )
        
        # 转换为Playbook格式
        paragraphs = _transform_to_paragraphs(result, request.engines, narrative)
        sources_used = {
            eid: SOURCE_INFO[eid].model_dump()
            for eid in request.engines
            if eid in SOURCE_INFO
        }
        
        elapsed = (time.perf_counter() - start_time) * 1000
        
        response_data = {
            "reading_id": f"rd_{uuid.uuid4().hex[:12]}",
            "time_scope": request.time_scope,
            "paragraphs": [p.model_dump() for p in paragraphs],
            "sources_used": sources_used,
            "engines_used": result.fusion_result.contributing_engines,
            "generated_at": result.created_at.isoformat(),
            "processing_time_ms": elapsed,
        }
        
        # ===== 3. 写入缓存 =====
        cache.set(cache_key, response_data, playbook_type=request.time_scope)
        logger.info(f"Playbook cached: {cache_key}, ttl={get_cache_ttl(request.time_scope)}s")
        
        return PlaybookReadingResponse(**response_data)
        
    except Exception as e:
        logger.exception("Playbook reading failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate reading: {str(e)}"
        )


# time_scope 到 ScenarioType 的映射
TIME_SCOPE_TO_SCENARIO = {
    "day": ScenarioType.PLAYBOOK_DAILY,
    "week": ScenarioType.PLAYBOOK_WEEKLY,
    "month": ScenarioType.PLAYBOOK_MONTHLY,
    "year": ScenarioType.PLAYBOOK_YEARLY,
}


async def _generate_narrative_by_scope(
    fusion_result,
    time_scope: str,
    user_id: str,
    language: str = "zh",
    raw_factors: Optional[Dict[str, Any]] = None,
) -> Optional[str]:
    """
    根据 time_scope 使用 Orchestrator 生成叙事
    
    Args:
        fusion_result: 融合结果
        time_scope: 时间范围
        user_id: 用户ID
        language: 输出语言代码
        raw_factors: 原始 Factors 对象
    """
    scenario = TIME_SCOPE_TO_SCENARIO.get(time_scope, ScenarioType.PLAYBOOK_DAILY)
    
    try:
        # Phase 8 Task 8.5: 获取用户记忆上下文
        user_insights = None
        try:
            selector = get_query_selector()
            scenario_ctx = await selector.get_context_for_scenario(
                user_id=user_id,
                scenario=scenario,
            )
            user_insights = scenario_ctx.recent_insights if scenario_ctx.recent_insights else None
            if user_insights:
                logger.debug(f"Loaded {len(user_insights)} insights for user {user_id}")
        except Exception as mem_err:
            logger.warning(f"Failed to load user insights: {mem_err}")
        
        orchestrator = get_orchestrator()
        result = await orchestrator.generate(
            scenario=scenario,
            fusion_result=fusion_result,
            user_context={"user_id": user_id},
            language=language,
            raw_factors=raw_factors,
            user_insights=user_insights,  # Phase 8: 传递用户洞察
        )
        
        logger.info(
            f"Orchestrator generated {scenario.value}: "
            f"model={result.model_used}, tokens={result.tokens_used}, "
            f"snippets={result.snippets_count}"
        )
        
        return result.content
    
    except Exception as e:
        logger.error(f"Orchestrator generation failed: {e}")
        return None


def _transform_to_paragraphs(
    result,
    engines: List[str],
    narrative: Optional[str] = None,
) -> List[ReadingParagraph]:
    """
    将Pipeline结果转换为带来源标记的段落
    
    Args:
        result: Pipeline 输出
        engines: 使用的引擎列表
        narrative: Orchestrator 生成的叙事（优先使用）
    """
    paragraphs = []
    
    # 使用 Orchestrator 生成的叙事，或 Pipeline 的叙事
    main_narrative = narrative or result.narrative
    if main_narrative:
        paragraphs.append(ReadingParagraph(
            text=main_narrative,
            inline_sources=[]  # TODO: 添加来源追踪
        ))
    
    # 如果没有叙事，从证据链生成段落
    if not paragraphs:
        for evidence in result.fusion_result.evidence_chain[:5]:  # 限制数量
            if evidence.matched and evidence.description:
                # 确定来源引擎
                source_engine = evidence.source_book.split("_")[0] if evidence.source_book else "default"
                if source_engine not in engines:
                    source_engine = engines[0] if engines else "default"
                
                paragraphs.append(ReadingParagraph(
                    text=evidence.description,
                    inline_sources=[InlineSource(
                        start=0,
                        end=len(evidence.description),
                        sources=[source_engine]
                    )]
                ))
    
    # 如果没有段落，添加默认
    if not paragraphs:
        paragraphs.append(ReadingParagraph(
            text="暂无解读内容，请确保输入正确的出生信息。",
            inline_sources=[]
        ))
    
    return paragraphs
