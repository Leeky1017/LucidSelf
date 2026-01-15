"""
Analyze Route

核心分析端点。

对照 tasks.md 13.3:
- Requirements: 6.1.1, 6.2.1
- ⚠️ 陷阱: 确保超时处理
"""

import asyncio
import logging
import os
import time
import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status

from backend.api.models import AnalyzeRequest, AnalyzeResponse
from backend.core.contracts import FusionResult, RuntimeRuleResult
from backend.core.engines.governance import EngineIdGovernanceError
from backend.core.observability.logging import log_event

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Analysis"])

# 超时配置
ANALYZE_TIMEOUT_SECONDS = 30.0

# 是否使用真实 Pipeline (环境变量控制，便于测试)
USE_REAL_PIPELINE = os.getenv("USE_REAL_PIPELINE", "false").lower() == "true"


def _create_mock_fusion_result(request: AnalyzeRequest) -> FusionResult:
    """
    创建模拟融合结果 (用于测试和开发)
    """
    themes = []
    engines = []
    
    if request.birth_data:
        themes.extend(["命理分析", "运势预测"])
        engines.append("bazi")
    
    if request.dream_text:
        themes.append("梦境解析")
        engines.append("dream")
    
    if request.tarot_spread:
        themes.append("塔罗指引")
        engines.append("tarot")
    
    if not themes:
        themes = ["综合分析"]
        engines = ["default"]
    
    rule_result = RuntimeRuleResult(
        rule_id="mock_rule_001",
        matched=True,
        dimension="综合",
        level="中",
        confidence=0.75,
        weight=1.0,
        execution_time_ms=10.0,
    )
    
    return FusionResult(
        fusion_id=f"fus_{uuid.uuid4().hex[:12]}",
        primary_themes=themes[:5],
        evidence_chain=[rule_result],
        cross_validation_score=0.75,
        confidence_matrix={"default": 0.75},
        conflicts=[],
        contributing_engines=engines,
        fusion_time_ms=50.0,
    )


async def _execute_real_pipeline(request: AnalyzeRequest) -> tuple:
    """
    执行真实 L1-L5 Pipeline
    
    Returns:
        (fusion_result, narrative, disclaimer)
    """
    from backend.pipeline import Pipeline, PipelineInput, BirthDataInput, TarotInput
    from backend.pipeline.orchestrator import get_pipeline
    
    # 构建 Pipeline 输入
    birth_data = None
    if request.birth_data:
        birth_data = BirthDataInput(
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
    
    tarot = None
    if request.tarot_spread:
        tarot = TarotInput(
            cards=request.tarot_spread.cards,
            positions=request.tarot_spread.positions,
            spread_type=request.tarot_spread.spread_type,
        )
    
    pipeline_input = PipelineInput(
        user_id=request.user_id,
        birth_data=birth_data,
        dream_text=request.dream_text,
        tarot=tarot,
        question=request.question,
        engines=request.engines,
        include_narrative=request.include_narrative,
        language=request.language,
    )
    
    # 执行 Pipeline
    pipeline = get_pipeline()
    output = await pipeline.execute(pipeline_input)
    
    return output.fusion_result, output.narrative, output.disclaimer


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest, http_request: Request) -> AnalyzeResponse:
    """
    核心分析端点
    
    接受多类型输入，返回融合分析结果和可选叙事。
    
    ⚠️ 设置超时防止长时间阻塞
    """
    start_time = time.perf_counter()

    # Correlation (set by RequestLoggingMiddleware; fallback for non-HTTP execution)
    request_id = getattr(http_request.state, "request_id", None) or f"req_{uuid.uuid4().hex[:12]}"
    trace_id = getattr(http_request.state, "trace_id", None)
    http_request.state.request_id = request_id
    if trace_id:
        http_request.state.trace_id = trace_id

    # Best-effort engine_id for request-level correlation
    http_request.state.engine_id = "cross-system-fusion"

    log_event(
        logger,
        logging.INFO,
        "analyze_start",
        user_id=request.user_id,
        engine_id=http_request.state.engine_id,
        engines=request.engines,
    )
    
    try:
        # 设置总超时
        async with asyncio.timeout(ANALYZE_TIMEOUT_SECONDS):
            if USE_REAL_PIPELINE:
                # 使用真实 L1-L5 Pipeline
                fusion_result, narrative, disclaimer = await _execute_real_pipeline(request)
            else:
                # 使用 Mock (测试/开发)
                fusion_result = _create_mock_fusion_result(request)
                narrative = None
                disclaimer = None
                
                if request.include_narrative:
                    narrative = _generate_mock_narrative(
                        fusion_result,
                        request.question,
                        request.language,
                    )
            
            processing_time_ms = (time.perf_counter() - start_time) * 1000
            
            log_event(
                logger,
                logging.INFO,
                "analyze_complete",
                engine_id=http_request.state.engine_id,
                processing_time_ms=round(processing_time_ms, 2),
            )
            return AnalyzeResponse(
                request_id=request_id,
                fusion_id=fusion_result.fusion_id,
                primary_themes=fusion_result.primary_themes,
                cross_validation_score=fusion_result.cross_validation_score,
                contributing_engines=fusion_result.contributing_engines,
                narrative=narrative,
                processing_time_ms=processing_time_ms,
                disclaimer=disclaimer,
            )
    
    except asyncio.TimeoutError:
        log_event(logger, logging.ERROR, "analyze_timeout")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Analysis timeout, please try again",
        )
    except EngineIdGovernanceError as e:
        http_request.state.engine_id = e.engine_id
        log_event(
            logger,
            logging.WARNING,
            "analyze_blocked_engine_id_governance",
            user_id=request.user_id,
            code=e.code,
            engine_id=e.engine_id,
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": e.code,
                "message": e.message,
                "engine_id": e.engine_id,
            },
        )
    except Exception as e:
        log_event(logger, logging.ERROR, "analyze_error", error_type=type(e).__name__)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


def _generate_mock_narrative(
    fusion: FusionResult,
    question: Optional[str],
    language: str,
) -> str:
    """生成模拟叙事"""
    themes_text = "、".join(fusion.primary_themes[:3])
    
    if language == "zh":
        return f"""## 分析报告

根据综合分析，您当前的主要特点为：{themes_text}。

交叉验证分数为 {fusion.cross_validation_score:.0%}，分析结果可信度较高。

本次分析综合了 {len(fusion.contributing_engines)} 个分析引擎的结果。

---

*以上解读仅供参考，请结合实际情况理性看待。*"""
    else:
        themes_text_en = ", ".join(fusion.primary_themes[:3])
        return f"""## Analysis Report

Based on comprehensive analysis, your main characteristics are: {themes_text_en}.

Cross-validation score is {fusion.cross_validation_score:.0%}, indicating reliable results.

This analysis integrates results from {len(fusion.contributing_engines)} engines.

---

*The above interpretation is for reference only.*"""
