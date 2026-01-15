"""
Versions Route

人生版本 API 端点。

改造说明 (2025-12):
- 接入 LLMOrchestrator，提供基于 TOON + 典籍的人生导航建议
- 新增 /navigate 端点，替代旧的字符串拼接 Prompt

对照文档: docs/ls_roadmap_executable.md Task 3.5
"""

import logging
import time
import uuid
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from backend.core.contracts import FusionResult, RuntimeRuleResult
from backend.core.llm import get_orchestrator, ScenarioType
from backend.core.contracts.life_version_models import (
    LifeVersion,
    LifeVersionSet,
    VersionComparison,
    VersionSelectionRecord,
)
from backend.core.contracts.version_tree_models import (
    VersionTree,
    TreeTraversalPath,
)
from backend.services.life_version import LifeVersionGenerator, VersionComparator
from backend.services.version_tree import VersionTreeService
from backend.services.memory.background_writer import (
    spawn_memory_write,
    record_version_selection,
    record_version_navigation,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/versions", tags=["Life Versions"])


# ==================== 存储 (MVP: 内存存储) ====================

# 版本集合存储
_version_sets: dict[str, LifeVersionSet] = {}
# 选择记录存储
_selections: list[VersionSelectionRecord] = []

# 服务实例
_generator = LifeVersionGenerator()
_comparator = VersionComparator()
_tree_service = VersionTreeService()


# ==================== 请求/响应模型 ====================

class VersionSetResponse(BaseModel):
    """版本集合响应"""
    version_set: LifeVersionSet
    comparison: Optional[VersionComparison] = None


class SelectVersionRequest(BaseModel):
    """选择版本请求"""
    version_id: str = Field(..., description="选中的版本 ID")
    notes: Optional[str] = Field(None, max_length=200, description="用户备注")


class SelectVersionResponse(BaseModel):
    """选择版本响应"""
    success: bool
    record_id: str
    message: str


class TreeResponse(BaseModel):
    """版本树响应"""
    tree: VersionTree
    current_path: TreeTraversalPath


class NavigateRequest(BaseModel):
    """人生导航请求"""
    selected_version_id: Optional[str] = Field(None, description="用户选择的版本 ID（可能偏离推荐）")
    user_context: Optional[dict] = Field(None, description="用户上下文（如当前状态、关注点）")
    deviation_reason: Optional[str] = Field(None, max_length=500, description="偏离推荐的原因")


class NavigateResponse(BaseModel):
    """人生导航响应"""
    narrative: str = Field(..., description="LLM 生成的导航建议")
    model_used: str = Field(..., description="使用的模型")
    tokens_used: int = Field(..., description="消耗的 token 数")
    snippets_count: int = Field(default=0, description="引用的典籍条数")
    processing_time_ms: float = Field(..., description="处理耗时(ms)")


# ==================== API 端点 ====================

@router.get("/{set_id}", response_model=VersionSetResponse)
async def get_version_set(set_id: str):
    """
    获取版本集合
    
    返回指定 ID 的版本集合及其对比视图。
    """
    version_set = _version_sets.get(set_id)
    if not version_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Version set not found: {set_id}"
        )
    
    # 生成对比视图
    comparison = _comparator.compare(version_set)
    
    return VersionSetResponse(
        version_set=version_set,
        comparison=comparison,
    )


@router.get("/{set_id}/compare", response_model=VersionComparison)
async def get_comparison(set_id: str):
    """
    获取版本对比视图
    
    返回版本间的对比矩阵和摘要。
    """
    version_set = _version_sets.get(set_id)
    if not version_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Version set not found: {set_id}"
        )
    
    return _comparator.compare(version_set)


@router.post("/{set_id}/select/{version_id}", response_model=SelectVersionResponse)
async def select_version(
    set_id: str, 
    version_id: str,
    request: Optional[SelectVersionRequest] = None,
):
    """
    用户选择版本
    
    记录用户的版本选择到 Memory 系统。
    """
    version_set = _version_sets.get(set_id)
    if not version_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Version set not found: {set_id}"
        )
    
    # 验证版本存在
    version_ids = [v.version_id for v in version_set.versions]
    if version_id not in version_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Version not found in set: {version_id}"
        )
    
    # 创建选择记录
    import uuid
    from datetime import datetime
    
    record = VersionSelectionRecord(
        record_id=f"sel_{uuid.uuid4().hex[:12]}",
        user_id=version_set.user_id,
        set_id=set_id,
        version_id=version_id,
        notes=request.notes if request else None,
        selected_at=datetime.now(),
    )
    
    _selections.append(record)
    
    # 更新推荐版本
    version_set.recommended_version_id = version_id
    
    # WP-05: Phase 7 Task 7.2 - 异步非阻塞写入 MemoryService
    selected_v = next((v for v in version_set.versions if v.version_id == version_id), None)
    spawn_memory_write(
        lambda: record_version_selection(
            user_id=version_set.user_id,
            set_id=set_id,
            version_id=version_id,
            recommended_id=version_set.recommended_version_id,
            notes=request.notes if request else None,
            selected_title=selected_v.title if selected_v else None,
        ),
        context_name="version_selection",
        user_id=version_set.user_id,
    )
    
    logger.info(
        f"User {version_set.user_id} selected version {version_id} "
        f"from set {set_id}"
    )
    
    return SelectVersionResponse(
        success=True,
        record_id=record.record_id,
        message=f"Version {version_id} selected successfully",
    )


@router.get("/{set_id}/tree", response_model=TreeResponse)
async def get_version_tree(set_id: str):
    """
    获取版本树
    
    返回版本集合对应的决策树和当前路径。
    """
    version_set = _version_sets.get(set_id)
    if not version_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Version set not found: {set_id}"
        )
    
    # 查找或创建版本树
    user_trees = await _tree_service.get_user_trees(version_set.user_id)
    tree = next(
        (t for t in user_trees if t.scenario_id == version_set.scenario_id),
        None
    )
    
    if not tree:
        # 创建新树
        tree = await _tree_service.create_tree(
            user_id=version_set.user_id,
            version_set=version_set,
        )
    
    # 获取当前路径
    current_path = await _tree_service.get_current_path(tree.tree_id)
    
    return TreeResponse(
        tree=tree,
        current_path=current_path,
    )


@router.post("/{set_id}/navigate", response_model=NavigateResponse)
async def navigate_version(
    set_id: str,
    request: Optional[NavigateRequest] = None,
):
    """
    人生版本导航
    
    使用 LLMOrchestrator 生成人生导航建议：
    1. 识别用户选择与命理推荐的偏离
    2. 分析可能的风险和机会
    3. 提供替代路线或风险规避建议
    4. 引用典籍作为依据
    """
    start_time = time.perf_counter()
    
    version_set = _version_sets.get(set_id)
    if not version_set:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Version set not found: {set_id}"
        )
    
    try:
        # 1. 构建 FusionResult
        fusion_result = _build_version_fusion_result(
            version_set=version_set,
            selected_version_id=request.selected_version_id if request else None,
        )
        
        # 2. 构建用户上下文
        user_context = {
            "user_id": version_set.user_id,
            "场景": version_set.scenario_id,
            "领域": version_set.domain.value,
        }
        if request and request.user_context:
            user_context.update(request.user_context)
        
        # 3. 构建额外上下文（偏离原因）
        extra_context = None
        if request:
            selected_id = request.selected_version_id
            recommended_id = version_set.recommended_version_id
            
            if selected_id and selected_id != recommended_id:
                selected_v = next((v for v in version_set.versions if v.version_id == selected_id), None)
                recommended_v = next((v for v in version_set.versions if v.version_id == recommended_id), None)
                
                extra_context = f"用户选择了「{selected_v.title if selected_v else selected_id}」，"
                extra_context += f"但系统推荐的是「{recommended_v.title if recommended_v else recommended_id}」。"
                
                if request.deviation_reason:
                    extra_context += f"\n用户选择的原因：{request.deviation_reason}"
        
        # 4. 调用 LLMOrchestrator
        orchestrator = get_orchestrator()
        result = await orchestrator.generate(
            scenario=ScenarioType.LIFE_VERSION,
            fusion_result=fusion_result,
            user_context=user_context,
            extra_context=extra_context,
        )
        
        elapsed_ms = (time.perf_counter() - start_time) * 1000
        
        logger.info(
            f"Life version navigation generated: model={result.model_used}, "
            f"tokens={result.tokens_used}, snippets={result.snippets_count}, "
            f"latency={elapsed_ms:.1f}ms"
        )
        
        # WP-05: Phase 7 Task 7.4 - 异步非阻塞写入导航事件
        spawn_memory_write(
            lambda: record_version_navigation(
                user_id=version_set.user_id,
                set_id=set_id,
                selected_version_id=request.selected_version_id if request else None,
                tokens_used=result.tokens_used,
            ),
            context_name="version_navigation",
            user_id=version_set.user_id,
        )
        
        return NavigateResponse(
            narrative=result.content,
            model_used=result.model_used,
            tokens_used=result.tokens_used,
            snippets_count=result.snippets_count,
            processing_time_ms=elapsed_ms,
        )
        
    except Exception as e:
        logger.exception("Life version navigation failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Navigation generation failed: {str(e)}"
        )


# ==================== 辅助函数 ====================

def register_version_set(version_set: LifeVersionSet) -> None:
    """
    注册版本集合到存储
    
    由其他服务调用，将生成的版本集合注册到 API 可访问的存储中。
    """
    _version_sets[version_set.set_id] = version_set
    logger.info(f"Registered version set: {version_set.set_id}")


def get_user_selections(user_id: str) -> list[VersionSelectionRecord]:
    """获取用户的所有选择记录"""
    return [s for s in _selections if s.user_id == user_id]


def _build_version_fusion_result(
    version_set: LifeVersionSet,
    selected_version_id: Optional[str] = None,
) -> FusionResult:
    """
    从版本集合构建 FusionResult
    
    将 LifeVersionSet 的信息转换为 FusionResult，
    使其可以被 LLMOrchestrator 处理。
    """
    evidence_chain = []
    
    # 1. 为每个版本生成证据
    for i, version in enumerate(version_set.versions):
        is_recommended = version.version_id == version_set.recommended_version_id
        is_selected = version.version_id == selected_version_id
        
        # 版本策略证据
        evidence = RuntimeRuleResult(
            rule_id=f"version_strategy_{i:03d}",
            matched=True,
            dimension="人生版本",
            level="推荐" if is_recommended else "备选",
            description=f"「{version.title}」：{version.subtitle}。策略：{'；'.join(version.strategy[:3])}",
            confidence=version.confidence,
            weight=1.5 if is_recommended else 1.0,
            tags=["life_version", version.title.lower().replace("版", "")],
            evidence_factors=version.source_factors[:5] if version.source_factors else [],
            semantic_refs=version.source_rules[:3] if version.source_rules else [],
            source_book="life_version_engine",
            execution_time_ms=0.0,
        )
        evidence_chain.append(evidence)
        
        # 如果是被选中但非推荐的版本，添加偏离证据
        if is_selected and not is_recommended:
            deviation_evidence = RuntimeRuleResult(
                rule_id=f"version_deviation_{i:03d}",
                matched=True,
                dimension="路径偏离",
                level="提醒",
                description=f"用户选择了「{version.title}」而非推荐版本，可能面临风险：{'；'.join(version.risks[:2])}",
                confidence=0.8,
                weight=1.2,
                tags=["deviation", "risk"],
                evidence_factors=[],
                source_book="life_version_engine",
                execution_time_ms=0.0,
            )
            evidence_chain.append(deviation_evidence)
    
    # 2. 添加领域证据
    domain_evidence = RuntimeRuleResult(
        rule_id="version_domain_001",
        matched=True,
        dimension="决策领域",
        level="信息",
        description=f"当前决策领域：{version_set.domain.value}，对比维度：{'、'.join(version_set.comparison_axes[:5])}",
        confidence=1.0,
        weight=0.5,
        tags=["domain", version_set.domain.value],
        evidence_factors=[],
        source_book="life_version_engine",
        execution_time_ms=0.0,
    )
    evidence_chain.append(domain_evidence)
    
    # 确保至少有一条证据
    if not evidence_chain:
        evidence_chain.append(RuntimeRuleResult(
            rule_id="version_default_001",
            matched=True,
            dimension="人生版本",
            level="信息",
            description="人生版本导航",
            confidence=0.5,
            weight=0.5,
            tags=["life_version"],
            evidence_factors=[],
            source_book="life_version_engine",
            execution_time_ms=0.0,
        ))
    
    # 构建主题
    primary_themes = ["人生版本对比"]
    if selected_version_id and selected_version_id != version_set.recommended_version_id:
        primary_themes.append("路径偏离分析")
    primary_themes.append(f"{version_set.domain.value}决策")
    
    # 构建置信度矩阵
    confidence_matrix = {}
    for version in version_set.versions:
        confidence_matrix[version.title] = version.confidence
    
    return FusionResult(
        fusion_id=f"fus_{uuid.uuid4().hex[:12]}",
        primary_themes=primary_themes[:5],
        evidence_chain=evidence_chain,
        confidence_matrix=confidence_matrix,
        cross_validation_score=0.8,
        contributing_engines=["life-version-engine"],
        conflicts=[],
        fusion_time_ms=0.0,
    )


# P0-1: 辅助函数已移至 backend/services/memory/background_writer.py
