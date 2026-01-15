"""
Interpret Route

解读生成端点。

对照 tasks.md 13.4:
- Requirements: 6.1.2
"""

import asyncio
import logging
import time
import uuid
from typing import Optional

from fastapi import APIRouter, HTTPException, status

from backend.api.models import InterpretRequest, InterpretResponse

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Interpretation"])

# 超时配置
INTERPRET_TIMEOUT_SECONDS = 15.0

# 模拟缓存 (TODO: 替换为真实存储)
_fusion_cache: dict = {}


@router.post("/interpret", response_model=InterpretResponse)
async def interpret(request: InterpretRequest) -> InterpretResponse:
    """
    解读生成端点
    
    根据已有的融合结果或请求 ID 生成叙事解读。
    """
    start_time = time.perf_counter()
    request_id = f"req_{uuid.uuid4().hex[:12]}"
    
    logger.info(
        "Interpret request: request_id=%s, user_id=%s, fusion_id=%s",
        request_id, request.user_id, request.fusion_id,
    )
    
    # 验证输入
    if not request.fusion_id and not request.request_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either fusion_id or request_id is required",
        )
    
    try:
        async with asyncio.timeout(INTERPRET_TIMEOUT_SECONDS):
            # 1. 获取融合结果
            fusion_id = request.fusion_id or request.request_id
            
            # TODO: 从缓存/数据库获取真实的 FusionResult
            # fusion_result = await get_fusion_result(fusion_id)
            
            # 2. 生成叙事
            # TODO: 集成 NarrativeGenerator
            narrative = _generate_mock_interpretation(
                fusion_id,
                request.question,
                request.language,
            )
            
            processing_time_ms = (time.perf_counter() - start_time) * 1000
            
            return InterpretResponse(
                request_id=request_id,
                fusion_id=fusion_id,
                narrative=narrative,
                processing_time_ms=processing_time_ms,
                disclaimer="以上解读仅供参考" if request.language == "zh" else "For reference only",
            )
    
    except asyncio.TimeoutError:
        logger.error("Interpret timeout: request_id=%s", request_id)
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Interpretation timeout",
        )
    except Exception as e:
        logger.exception("Interpret error: request_id=%s", request_id)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


def _generate_mock_interpretation(
    fusion_id: str,
    question: Optional[str],
    language: str,
) -> str:
    """生成模拟解读"""
    if language == "zh":
        base = f"""## 详细解读

基于融合分析结果 ({fusion_id})，为您提供以下解读：

### 综合运势
您当前的整体运势处于上升期，各方面都有积极的发展趋势。

### 建议
保持积极心态，把握机遇。"""
        
        if question:
            base += f"\n\n### 针对您的问题\n关于「{question}」，建议您从多角度思考，稳健决策。"
        
        return base
    else:
        base = f"""## Detailed Interpretation

Based on the fusion analysis ({fusion_id}), here is the interpretation:

### Overall Fortune
Your current overall fortune is on an upward trend with positive developments.

### Suggestions
Maintain a positive mindset and seize opportunities."""
        
        if question:
            base += f"\n\n### Regarding Your Question\nAbout \"{question}\", consider multiple perspectives."
        
        return base
