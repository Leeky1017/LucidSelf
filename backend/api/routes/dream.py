"""
Dream Route

Dream Journal 梦境日志端点。

改造说明 (2025-12):  
- 接入 LLMOrchestrator，替换原有硬编码模板
- 使用 FusionResult + TOON 上下文注入
- 典籍引用通过 NarrativeSnippet 实现
"""

import logging
import time
import uuid
from datetime import datetime
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.contracts import FusionResult, RuntimeRuleResult
from backend.core.contracts.auth_models import UserInfo
from backend.core.llm import get_orchestrator, ScenarioType
from backend.db.session import get_db
from backend.api.services.dream_service import DreamService
from backend.api.routes.auth import get_current_user
from backend.services.memory.background_writer import (
    spawn_memory_write,
    create_dream_insight,
    record_dream_event,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/dream", tags=["Dream Journal"])


# ==================== 请求/响应模型 ====================

class BaziProfile(BaseModel):
    """八字信息"""
    day_master: str = Field(..., alias="dayMaster")
    current_luck: str = Field(..., alias="currentLuck")
    
    class Config:
        populate_by_name = True


class UserProfile(BaseModel):
    """用户档案"""
    bazi: Optional[BaziProfile] = None
    lunar_phase: Optional[str] = Field(None, alias="lunarPhase")
    
    class Config:
        populate_by_name = True


class DreamPattern(BaseModel):
    """梦境模式"""
    pattern: str


class DreamGenerateRequest(BaseModel):
    """梦境生成请求 - 对齐前端 GenerateRequest"""
    keywords: str = Field(..., description="关键词，逗号分隔")
    mood: str = Field(..., description="心情（必需）")
    user_profile: Optional[UserProfile] = Field(None, alias="userProfile")
    dream_history: Optional[List[DreamPattern]] = Field(None, alias="dreamHistory")
    canonical_symbols: Optional[Dict[str, str]] = Field(None, alias="canonicalSymbols")
    
    class Config:
        populate_by_name = True


class DreamGenerateResponse(BaseModel):
    """梦境生成响应 - 对齐前端 GenerateResponse"""
    success: bool
    narrative: Optional[str] = None
    tokens_used: Optional[int] = Field(None, alias="tokensUsed")
    model: Optional[str] = None
    error: Optional[str] = None
    
    class Config:
        populate_by_name = True


class SymbolInfo(BaseModel):
    """符号信息"""
    symbol: str
    meaning: str
    category: str
    confidence: float


class EmotionInfo(BaseModel):
    """情绪信息"""
    emotion: str
    intensity: float


class DreamAnalyzeRequest(BaseModel):
    """梦境分析请求"""
    dream_text: str = Field(..., description="梦境文本")
    user_id: Optional[str] = None


class DreamAnalyzeResponse(BaseModel):
    """梦境分析响应"""
    symbols: List[SymbolInfo]
    themes: List[str]
    emotions: List[EmotionInfo]
    factors: Dict


class DreamEntryCreate(BaseModel):
    """创建梦境条目"""
    user_id: Optional[str] = None
    title: Optional[str] = None
    raw_input: str = Field(..., alias="rawInput")
    final_content: str = Field(..., alias="finalContent")
    generated_content: Optional[str] = Field(None, alias="generatedContent")
    mood: Optional[str] = None
    tags: List[str] = []
    clarity: Optional[int] = Field(None, ge=1, le=5)
    status: str = "draft"
    mode: str = "quick"
    
    class Config:
        populate_by_name = True


class DreamEntry(BaseModel):
    """梦境条目"""
    id: str
    user_id: str
    status: str
    mode: str
    raw_input: str
    generated_content: Optional[str] = None
    final_content: str
    title: Optional[str] = None
    date: Optional[str] = None
    clarity: Optional[int] = None
    tags: List[str] = []
    mood: Optional[str] = None
    generate_count: int = 0
    created_at: str
    updated_at: str
    published_at: Optional[str] = None


class DreamEntriesResponse(BaseModel):
    """梦境列表响应"""
    entries: List[DreamEntry]
    total: int
    has_more: bool


class DreamEntryCreateResponse(BaseModel):
    """创建梦境响应"""
    entry_id: str
    created_at: str


# ==================== 数据库依赖 ====================

async def get_dream_service(db: AsyncSession = Depends(get_db)) -> DreamService:
    """获取DreamService依赖"""
    return DreamService(db)


# ==================== API端点 ====================

@router.post("/generate", response_model=DreamGenerateResponse)
async def generate_dream_narrative(request: DreamGenerateRequest):
    """
    生成梦境叙事
    
    使用 LLMOrchestrator 生成有深度的梦境解读：
    1. DreamExtractor 提取符号和情绪
    2. 构造 FusionResult（将符号、情绪转为证据链）
    3. 调用 orchestrator.generate(scenario=ScenarioType.DREAM)
    4. LLM 引用典籍（如《周公解梦》）生成解读
    """
    start_time = time.perf_counter()
    
    try:
        # 解析关键词
        keywords_list = [k.strip() for k in request.keywords.split(",") if k.strip()]
        
        if not keywords_list:
            return DreamGenerateResponse(
                success=False,
                error="请提供至少一个关键词"
            )
        
        # 1. 使用 DreamExtractor 提取符号
        from backend.calculators.dream import DreamExtractor
        from backend.calculators.dream.models import DreamInput
        
        initial_text = f"我梦见了{', '.join(keywords_list)}。当时的心情是{request.mood}。"
        
        extractor = DreamExtractor()
        dream_input = DreamInput(dream_text=initial_text)
        extract_result = extractor.extract(dream_input)
        
        # 2. 构造 FusionResult
        fusion_result = _build_dream_fusion_result(
            extract_result,
            keywords_list,
            request.mood,
            request.user_profile,
        )
        
        # 3. 构建用户上下文
        user_context = {}
        if request.user_profile:
            if request.user_profile.bazi:
                user_context["日主"] = request.user_profile.bazi.day_master
                user_context["当前运势"] = request.user_profile.bazi.current_luck
            if request.user_profile.lunar_phase:
                user_context["月相"] = request.user_profile.lunar_phase
        
        # 4. 构建额外上下文（梦境原文）
        extra_context = f"用户梦境描述：{initial_text}"
        if request.dream_history:
            recent_patterns = [p.pattern for p in request.dream_history[:3]]
            if recent_patterns:
                extra_context += f"\n\n近期梦境模式：{'、'.join(recent_patterns)}"
        
        # 5. 调用 LLMOrchestrator 生成叙事
        orchestrator = get_orchestrator()
        result = await orchestrator.generate(
            scenario=ScenarioType.DREAM,
            fusion_result=fusion_result,
            user_context=user_context if user_context else None,
            extra_context=extra_context,
        )
        
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        logger.info(
            f"Dream narrative generated: model={result.model_used}, "
            f"tokens={result.tokens_used}, snippets={result.snippets_count}, "
            f"latency={elapsed_ms:.1f}ms"
        )
        
        # R-02: 生成后写入 Insight (非阻塞)
        themes = [str(s.category) for s in extract_result.symbols[:3]]
        user_id = "anonymous"
        if request.user_profile and request.user_profile.bazi:
            user_id = request.user_profile.bazi.day_master
        
        spawn_memory_write(
            lambda: create_dream_insight(
                user_id=user_id,
                themes=themes,
                mood=request.mood,
            ),
            context_name="create_dream_insight",
            user_id=user_id,
        )
        
        return DreamGenerateResponse(
            success=True,
            narrative=result.content,
            tokens_used=result.tokens_used,
            model=result.model_used,
        )
        
    except Exception as e:
        logger.exception("Dream generation failed")
        # 降级到简单模板
        try:
            narrative = _generate_fallback_narrative(keywords_list, request.mood)
            return DreamGenerateResponse(
                success=True,
                narrative=narrative,
                tokens_used=0,
                model="fallback-template",
            )
        except Exception:
            return DreamGenerateResponse(
                success=False,
                error=str(e)
            )


@router.post("/analyze", response_model=DreamAnalyzeResponse)
async def analyze_dream(request: DreamAnalyzeRequest):
    """
    分析梦境
    
    提取梦境中的符号、主题和情绪。
    """
    try:
        from backend.calculators.dream import DreamExtractor
        from backend.calculators.dream.models import DreamInput
        
        extractor = DreamExtractor()
        dream_input = DreamInput(dream_text=request.dream_text)
        result = extractor.extract(dream_input)
        
        # 转换符号
        symbols = [
            SymbolInfo(
                symbol=s.symbol,
                meaning=s.matched_text or s.symbol,  # 使用matched_text作为meaning
                category=str(s.category) if s.category else "general",
                confidence=s.confidence
            )
            for s in result.symbols
        ]
        
        # 提取主题
        themes = list(set([str(s.category) for s in result.symbols if s.category]))
        
        # 提取情绪
        emotions = [
            EmotionInfo(emotion=e.emotion, intensity=e.intensity)
            for e in result.emotions
        ]
        
        # 构建因子
        factors = {
            "symbols": [s.symbol for s in result.symbols],
            "themes": themes,
            "primary_emotion": emotions[0].emotion if emotions else "neutral"
        }
        
        return DreamAnalyzeResponse(
            symbols=symbols,
            themes=themes,
            emotions=emotions,
            factors=factors
        )
        
    except Exception as e:
        logger.exception("Dream analysis failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Analysis failed: {str(e)}"
        )


@router.get("/entries", response_model=DreamEntriesResponse)
async def get_dream_entries(
    limit: int = 20,
    offset: int = 0,
    user: UserInfo = Depends(get_current_user),
    dream_service: DreamService = Depends(get_dream_service),
):
    """获取用户的梦境列表"""
    dreams, total = await dream_service.list_dreams(
        user_id=user.user_id,
        org_id=user.org_id,
        limit=limit,
        offset=offset,
    )
    
    entries = [
        DreamEntry(
            id=f"dream_{d.id}",
            user_id=d.user_id,
            status=d.status,
            mode=d.mode,
            raw_input=d.raw_input,
            generated_content=d.generated_content,
            final_content=d.final_content,
            title=d.title,
            date=d.created_at.date().isoformat() if d.created_at else None,
            clarity=d.clarity,
            tags=d.tags or [],
            mood=d.mood,
            generate_count=d.generate_count,
            created_at=d.created_at.isoformat() if d.created_at else "",
            updated_at=d.updated_at.isoformat() if d.updated_at else "",
        )
        for d in dreams
    ]
    
    return DreamEntriesResponse(
        entries=entries,
        total=total,
        has_more=(offset + limit) < total
    )


@router.post("/entries", response_model=DreamEntryCreateResponse)
async def create_dream_entry(
    request: DreamEntryCreate,
    user: UserInfo = Depends(get_current_user),
    dream_service: DreamService = Depends(get_dream_service),
):
    """保存梦境条目"""
    if request.user_id and request.user_id != user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": "CROSS_TENANT_ACCESS",
                "message": "user_id mismatch for authenticated request",
            },
        )

    # 1. 保存到 DB
    dream = await dream_service.create_dream(
        user_id=user.user_id,
        org_id=user.org_id,
        raw_input=request.raw_input,
        final_content=request.final_content,
        generated_content=request.generated_content,
        title=request.title,
        mood=request.mood,
        tags=request.tags,
        clarity=request.clarity,
        status=request.status,
        mode=request.mode,
    )
    
    # 提交事务
    await dream_service.db.commit()
    
    # WP-05: Phase 7 Task 7.1 - 异步非阻塞写入 MemoryService
    spawn_memory_write(
        lambda: record_dream_event(
            user_id=user.user_id,
            dream_id=str(dream.id),
            raw_input=request.raw_input,
            mood=request.mood,
            tags=request.tags,
            has_generated_content=bool(request.generated_content),
        ),
        context_name="record_dream_event",
        user_id=user.user_id,
    )
    
    return DreamEntryCreateResponse(
        entry_id=f"dream_{dream.id}",
        created_at=dream.created_at.isoformat() if dream.created_at else datetime.utcnow().isoformat()
    )


@router.get("/entries/{dream_id}", response_model=DreamEntry)
async def get_dream_entry(
    dream_id: str,
    user: UserInfo = Depends(get_current_user),
    dream_service: DreamService = Depends(get_dream_service),
):
    """获取单个梦境"""
    dream = await dream_service.get_dream(dream_id, user.user_id, user.org_id)
    if not dream:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dream entry not found"
        )
    
    return DreamEntry(
        id=f"dream_{dream.id}",
        user_id=dream.user_id,
        status=dream.status,
        mode=dream.mode,
        raw_input=dream.raw_input,
        generated_content=dream.generated_content,
        final_content=dream.final_content,
        title=dream.title,
        date=dream.created_at.date().isoformat() if dream.created_at else None,
        clarity=dream.clarity,
        tags=dream.tags or [],
        mood=dream.mood,
        generate_count=dream.generate_count,
        created_at=dream.created_at.isoformat() if dream.created_at else "",
        updated_at=dream.updated_at.isoformat() if dream.updated_at else "",
    )


@router.delete("/entries/{dream_id}")
async def delete_dream_entry(
    dream_id: str,
    user: UserInfo = Depends(get_current_user),
    dream_service: DreamService = Depends(get_dream_service),
):
    """删除梦境"""
    deleted = await dream_service.delete_dream(dream_id, user.user_id, user.org_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dream entry not found"
        )
    
    await dream_service.db.commit()
    return {"success": True}


# ==================== 辅助函数 ====================

def _build_dream_fusion_result(
    extract_result,
    keywords: List[str],
    mood: str,
    user_profile: Optional[UserProfile],
) -> FusionResult:
    """
    从梦境提取结果构建 FusionResult
    
    将 DreamExtractor 的输出转换为 FusionResult，
    使其可以被 LLMOrchestrator 处理。
    """
    # 构建证据链
    evidence_chain = []
    
    # 1. 符号证据
    for i, symbol in enumerate(extract_result.symbols[:5]):
        evidence = RuntimeRuleResult(
            rule_id=f"dream_symbol_{i:03d}",
            matched=True,
            dimension="梦境符号",
            level="中性",
            description=f"梦境中出现「{symbol.symbol}」（{symbol.category}类符号）",
            confidence=symbol.confidence,
            weight=1.0,
            tags=["dream", "symbol", symbol.category],
            evidence_factors=[f"dream_symbol_{symbol.category}_{symbol.symbol}"],
            source_book="dream_symbols",
            execution_time_ms=0.0,
        )
        evidence_chain.append(evidence)
    
    # 2. 情绪证据
    for i, emotion in enumerate(extract_result.emotions[:3]):
        evidence = RuntimeRuleResult(
            rule_id=f"dream_emotion_{i:03d}",
            matched=True,
            dimension="梦境情绪",
            level="中性",
            description=f"梦境整体情绪倾向为「{emotion.emotion}」",
            confidence=emotion.intensity,
            weight=0.8,
            tags=["dream", "emotion"],
            evidence_factors=[f"dream_emotion_{emotion.emotion}"],
            source_book="dream_emotions",
            execution_time_ms=0.0,
        )
        evidence_chain.append(evidence)
    
    # 3. 主题证据
    for i, theme in enumerate(extract_result.themes[:3]):
        evidence = RuntimeRuleResult(
            rule_id=f"dream_theme_{i:03d}",
            matched=True,
            dimension="梦境主题",
            level="中性",
            description=f"识别到梦境主题「{theme}」",
            confidence=0.8,
            weight=0.7,
            tags=["dream", "theme"],
            evidence_factors=[f"dream_theme_{theme}"],
            source_book="dream_themes",
            execution_time_ms=0.0,
        )
        evidence_chain.append(evidence)
    
    # 确保至少有一条证据
    if not evidence_chain:
        evidence_chain.append(RuntimeRuleResult(
            rule_id="dream_default_001",
            matched=True,
            dimension="梦境",
            level="中性",
            description=f"用户梦见了{', '.join(keywords)}，心情{mood}",
            confidence=0.5,
            weight=0.5,
            tags=["dream"],
            evidence_factors=["dream_general"],
            source_book="dream_default",
            execution_time_ms=0.0,
        ))
    
    # 构建主题
    primary_themes = []
    if extract_result.symbols:
        primary_themes.append("梦境符号解读")
    if extract_result.emotions:
        primary_themes.append("情绪映射分析")
    if extract_result.themes:
        primary_themes.append("主题象征探索")
    if not primary_themes:
        primary_themes = ["梦境解读"]
    
    # 构建置信度矩阵
    confidence_matrix = {
        "符号": sum(s.confidence for s in extract_result.symbols[:5]) / max(len(extract_result.symbols[:5]), 1),
        "情绪": sum(e.intensity for e in extract_result.emotions[:3]) / max(len(extract_result.emotions[:3]), 1) if extract_result.emotions else 0.5,
        "主题": 0.8 if extract_result.themes else 0.3,
    }
    
    return FusionResult(
        fusion_id=f"fus_{uuid.uuid4().hex[:12]}",
        primary_themes=primary_themes[:5],
        evidence_chain=evidence_chain,
        confidence_matrix=confidence_matrix,
        cross_validation_score=0.7,
        contributing_engines=["dream-extractor"],
        conflicts=[],
        fusion_time_ms=0.0,
    )


def _generate_fallback_narrative(keywords: List[str], mood: str) -> str:
    """
    降级叙事生成（LLM 不可用时的备选方案）
    
    注意：这是一个简化版本，仅用于系统降级场景。
    正常情况下应使用 LLMOrchestrator 生成更有深度的解读。
    """
    mood_descriptions = {
        "激动": "带着激动的心情",
        "幸福": "沉浸在幸福的氛围中",
        "紧张": "心跳加速，紧张不安",
        "害怕": "恐惧笼罩着",
        "崩溃": "情绪崩溃的边缘",
        "平静": "平静地",
        "好奇": "好奇地探索着",
    }
    
    mood_desc = mood_descriptions.get(mood, f"怀着{mood}的心情")
    
    return (
        f"在这个梦境中，你{mood_desc}经历了一段独特的旅程。"
        f"梦中出现了{', '.join(keywords)}，这些元素交织在一起，构成了一幅意义深远的画面。"
        f"\n\n建议你记录下这个梦境，日后回顾时可能会发现更多的启示。"
        f"\n\n[提示：系统暂时繁忙，已提供简化解读。请稍后重试以获取更详细的分析。]"
    )


# P0-1: 辅助函数已移至 backend/services/memory/background_writer.py
