"""
Fusion Engine - 多体系融合引擎

Layer 4 的核心组件，负责融合多个引擎的结果。

对照 design.md §2.1 FusionEngine
对照 Requirements 1.1.1-1.1.6
"""

from __future__ import annotations

import logging
import secrets
import time
from typing import Dict, List, Optional

from backend.core.contracts import (
    FusionResult,
    RuntimeRuleResult,
    ConflictWarning,  # 契约版本 (BaseModel)
)
from backend.rules.conflict import ConflictResolver
from backend.rules.conflict import ConflictWarning as L3ConflictWarning  # 内部 dataclass

from backend.integration.models import WeightedResult
from backend.integration.weight_manager import WeightManager
from backend.integration.cross_validator import CrossValidator
from backend.integration.theme_mapper import ThemeMapper
from backend.integration.evidence_chain import EvidenceChainBuilder
from backend.core.engines.governance import validate_engine_ids_or_raise

logger = logging.getLogger(__name__)


class FusionEngine:
    """
    多体系融合引擎 - MVP-0 核心
    
    职责：
    - 接收多引擎 RuntimeRuleResult 列表 (Requirement 1.1.1)
    - 输出符合 FusionResult 契约的标准结果 (Requirement 1.1.2)
    - 融合计算时间 <20ms (Requirement 1.1.3)
    - 支持用户权重偏好 (Requirement 1.1.4)
    - 默认等权融合策略 (Requirement 1.1.5)
    - 返回 contributing_engines 列表 (Requirement 1.1.6)
    
    对照 design.md §2.1
    """
    
    def __init__(
        self,
        weight_manager: Optional[WeightManager] = None,
        theme_mapper: Optional[ThemeMapper] = None,
        cross_validator: Optional[CrossValidator] = None,
        evidence_builder: Optional[EvidenceChainBuilder] = None,
        conflict_resolver: Optional[ConflictResolver] = None,
    ):
        """
        初始化融合引擎
        
        所有组件都是可选的，默认创建新实例。
        
        Args:
            weight_manager: 权重管理器
            theme_mapper: 主题映射器
            cross_validator: 交叉验证器
            evidence_builder: 证据链构建器
            conflict_resolver: 冲突解决器 (复用 Layer 3)
        """
        self.weight_manager = weight_manager or WeightManager()
        self.theme_mapper = theme_mapper or ThemeMapper()
        self.cross_validator = cross_validator or CrossValidator()
        self.evidence_builder = evidence_builder or EvidenceChainBuilder()
        self.conflict_resolver = conflict_resolver or ConflictResolver()
    
    def fuse_results(
        self,
        results: Dict[str, List[RuntimeRuleResult]],
        engine_weights: Optional[Dict[str, float]] = None,
    ) -> FusionResult:
        """
        融合多引擎结果
        
        对照 Requirement 1.1.1-1.1.6
        对照 design.md §2.1 fuse_results
        
        Args:
            results: 引擎ID → 规则结果列表的映射
            engine_weights: 用户自定义权重（可选）
            
        Returns:
            FusionResult 融合结果
        """
        start_time = time.perf_counter()

        # Gate-0: engine_id 格式 + registry 校验（确定性拒绝原因）
        if results:
            validate_engine_ids_or_raise(list(results.keys()))
        
        # 1. 应用权重 (Requirement 1.2.1-1.2.3)
        weighted = self.weight_manager.apply_weights(results, engine_weights)
        
        # 2. 提取主题 (Requirement 3.1-3.4)
        themes = self.theme_mapper.extract_themes(weighted)
        
        # 3. 交叉验证 (Requirement 2.1-2.5)
        cv_score, confidence_matrix = self.cross_validator.validate(weighted)
        
        # 4. 检测冲突 (Requirement 5.1-5.5)
        conflicts = self._detect_and_convert_conflicts(weighted)
        
        # 5. 构建证据链 (Requirement 4.1-4.4)
        evidence_chain = self.evidence_builder.build(weighted)
        
        # 计算融合时间 (Requirement 6.6)
        fusion_time = (time.perf_counter() - start_time) * 1000
        
        # 确保至少有一个主题
        if not themes:
            themes = ["通用"]
        
        # 确保至少有一条证据 (Requirement 7.3: 1-20 条)
        if not evidence_chain:
            if weighted:
                evidence_chain = [weighted[0].result]
            else:
                # 空输入时创建占位证据
                evidence_chain = [RuntimeRuleResult(
                    rule_id="placeholder_no_results",
                    matched=False,
                    confidence=0.0,
                    weight=0.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=0.0,
                )]
        
        return FusionResult(
            fusion_id=self._generate_fusion_id(),
            primary_themes=themes[:5],  # Requirement 7.2
            evidence_chain=evidence_chain[:20],  # Requirement 7.3
            confidence_matrix=confidence_matrix,
            cross_validation_score=cv_score,
            contributing_engines=list(results.keys()),  # Requirement 1.1.6
            conflicts=conflicts,
            fusion_time_ms=fusion_time,
        )
    
    def _generate_fusion_id(self) -> str:
        """
        生成融合ID
        
        格式: fus_[a-z0-9]{12}
        
        对照 Requirement 7.1
        
        Returns:
            fusion_id
        """
        # 生成 12 位随机字符串
        random_part = secrets.token_hex(6)  # 12 个十六进制字符
        return f"fus_{random_part}"
    
    def _detect_and_convert_conflicts(
        self,
        weighted: List[WeightedResult],
    ) -> List[ConflictWarning]:
        """
        检测冲突并转换为契约版本
        
        L3 dataclass → L4 Pydantic ConflictWarning 转换
        
        对照 Requirement 5.1-5.2
        对照 design.md §2.1 _detect_and_convert_conflicts
        
        Args:
            weighted: 加权结果列表
            
        Returns:
            冲突警告列表 (Pydantic 版本)
        """
        # 提取所有 RuntimeRuleResult
        all_results = [wr.result for wr in weighted]
        
        if not all_results:
            return []
        
        # 使用 L3 冲突解决器
        self.conflict_resolver.resolve_all(all_results)
        
        # 获取警告并转换为契约版本
        l3_warnings = self.conflict_resolver.get_warnings()
        
        return [
            ConflictWarning(
                group=w.group,
                conflicting_rules=w.conflicting_rules,
                severity=w.severity.value,
                resolution_strategy=w.resolution_strategy,
            )
            for w in l3_warnings
        ]


async def fuse_results_async(
    fusion_engine: FusionEngine,
    results: Dict[str, List[RuntimeRuleResult]],
    engine_weights: Optional[Dict[str, float]] = None,
) -> FusionResult:
    """
    异步融合结果
    
    对照 Requirement 6.2
    对照 design.md §6.2
    
    Args:
        fusion_engine: 融合引擎实例
        results: 引擎ID → 规则结果列表的映射
        engine_weights: 用户自定义权重（可选）
        
    Returns:
        FusionResult 融合结果
    """
    import asyncio
    
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        lambda: fusion_engine.fuse_results(results, engine_weights),
    )
