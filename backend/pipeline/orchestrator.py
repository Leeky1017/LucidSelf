"""
Pipeline Orchestrator

L1-L5 完整链路编排。

流程:
1. 用户输入 → L1 Calculator → FactorMatrix
2. FactorMatrix → L3 RuleEngine → List[RuntimeRuleResult]
3. Multi-Engine Results → L4 FusionEngine → FusionResult
4. FusionResult → L5 NarrativeGenerator → Narrative (optional)
"""

import logging
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from backend.core.contracts import (
    FactorMatrix,
    FusionResult,
    RuntimeRuleResult,
)
from backend.core.contracts.unified_time import TimelineProjection
from backend.core.constants import normalize_engine_ids
from backend.core.engines.governance import (
    EngineIdGovernanceError,
    validate_engine_ids_or_raise,
)
from backend.core.versioning.ids import resolve_corpus_release_id, resolve_version_id

logger = logging.getLogger(__name__)


@dataclass
class BirthDataInput:
    """出生数据输入"""
    year: int
    month: int
    day: int
    hour: int
    minute: int = 0
    timezone: str = "Asia/Shanghai"
    gender: str = "male"  # male or female
    location: Optional[str] = None  # 地名，如'北京'
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class TarotInput:
    """塔罗输入"""
    cards: List[str]
    positions: Optional[List[str]] = None
    spread_type: str = "single"


@dataclass
class PipelineInput:
    """Pipeline 输入"""
    user_id: str
    birth_data: Optional[BirthDataInput] = None
    dream_text: Optional[str] = None
    tarot: Optional[TarotInput] = None
    question: Optional[str] = None
    engines: Optional[List[str]] = None  # 指定使用的引擎
    include_narrative: bool = True
    include_timeline: bool = False  # 是否生成时间线推演
    timeline_years: int = 3  # 预测年数
    language: str = "zh"


@dataclass
class PipelineOutput:
    """Pipeline 输出"""
    request_id: str
    version_id: str
    corpus_release_id: str
    fusion_result: FusionResult
    narrative: Optional[str] = None
    disclaimer: Optional[str] = None
    timeline_projection: Optional[TimelineProjection] = None
    engine_results: Dict[str, List[RuntimeRuleResult]] = field(default_factory=dict)
    factor_matrices: List[FactorMatrix] = field(default_factory=list)
    processing_time_ms: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
    # 新增: 原始 Factors 对象 (BaziFactors, AstroFactors 等)
    # key: 标准引擎 ID (bazi-calculator, astro-calculator, ...)
    raw_factors: Dict[str, Any] = field(default_factory=dict)


class Pipeline:
    """
    L1-L5 Pipeline 编排器
    
    职责:
    - 协调各层组件
    - 管理执行流程
    - 处理错误和降级
    """
    
    def __init__(
        self,
        rule_engine=None,
        fusion_engine=None,
        narrative_generator=None,
        safety_moderator=None,
    ):
        """
        初始化 Pipeline
        
        Args:
            rule_engine: L3 RuleEngine
            fusion_engine: L4 FusionEngine
            narrative_generator: L5 NarrativeGenerator
            safety_moderator: L5 SafetyModerator
        """
        self._rule_engine = rule_engine
        self._fusion_engine = fusion_engine
        self._narrative_generator = narrative_generator
        self._safety_moderator = safety_moderator
        
        # 延迟加载组件
        self._initialized = False
    
    def _import_rule_modules(self) -> None:
        """导入所有编译好的规则模块以触发 @register_rule 装饰器"""
        import importlib
        import pkgutil
        from pathlib import Path
        
        rules_dir = Path(__file__).parent.parent / "generated" / "rules"
        if not rules_dir.exists():
            logger.warning(f"Rules directory not found: {rules_dir}")
            return
        
        imported_count = 0
        # 动态导入所有规则模块
        for module_info in pkgutil.iter_modules([str(rules_dir)]):
            module_name = f"backend.generated.rules.{module_info.name}"
            try:
                importlib.import_module(module_name)
                imported_count += 1
            except Exception as e:
                logger.error(f"Failed to import {module_name}: {e}")
        
        logger.info(f"Imported {imported_count} rule modules from {rules_dir}")
    
    def _ensure_initialized(self) -> None:
        """确保组件已初始化"""
        if self._initialized:
            return
        
        # 延迟导入以避免循环依赖
        if self._rule_engine is None:
            from backend.rules.engine import RuleEngine
            from backend.rules.conflict import ConflictResolver
            self._rule_engine = RuleEngine(conflict_resolver=ConflictResolver())
            
            # 导入编译好的规则模块以触发 @register_rule 装饰器
            self._import_rule_modules()
            
            # 从全局注册表加载规则到引擎
            loaded = self._rule_engine.load_from_registry()
            logger.info(f"Loaded {loaded} rules into RuleEngine")
        
        if self._fusion_engine is None:
            from backend.integration.fusion_engine import FusionEngine
            self._fusion_engine = FusionEngine()
        
        if self._narrative_generator is None:
            from backend.services.narrative import NarrativeGenerator
            self._narrative_generator = NarrativeGenerator()
        
        if self._safety_moderator is None:
            from backend.services.safety import SafetyModerator
            self._safety_moderator = SafetyModerator()
        
        self._initialized = True
    
    async def execute(self, input_data: PipelineInput) -> PipelineOutput:
        """
        执行完整 Pipeline
        
        Args:
            input_data: Pipeline 输入
            
        Returns:
            PipelineOutput
        """
        start_time = time.perf_counter()
        request_id = f"req_{uuid.uuid4().hex[:12]}"
        
        logger.info(
            "Pipeline execute: request_id=%s, user_id=%s",
            request_id, input_data.user_id,
        )
        
        self._ensure_initialized()
        
        try:
            # 标准化引擎 ID (bazi -> bazi-calculator)
            normalized_engines = normalize_engine_ids(input_data.engines)
            if input_data.engines and normalized_engines:
                logger.debug(
                    "Normalized engines: %s -> %s",
                    input_data.engines, normalized_engines
                )

            # Gate-0: engine_id 格式 + registry 校验（确定性拒绝原因）
            validated_engines = validate_engine_ids_or_raise(normalized_engines)
            
            # 1. L1: Calculate Factor Matrices + Raw Factors
            factor_matrices, raw_factors = await self._calculate_factors(input_data)
            
            # 2. L3: Execute Rules (使用标准化后的引擎 ID)
            engine_results = await self._execute_rules(factor_matrices, validated_engines)
            
            # 收集所有规则结果
            all_rule_results = []
            for results in engine_results.values():
                all_rule_results.extend(results)
            
            # 3. L4: Fuse Results
            fusion_result = self._fuse_results(engine_results)
            
            # 4. Timeline Projection (optional)
            timeline_projection = None
            if input_data.include_timeline and factor_matrices:
                timeline_projection = await self._generate_timeline(
                    factor_matrices=factor_matrices,
                    rule_results=all_rule_results,
                    user_id=input_data.user_id,
                    years=input_data.timeline_years,
                )
            
            # 5. L5: Generate Narrative (optional)
            narrative = None
            disclaimer = None
            
            if input_data.include_narrative:
                narrative, disclaimer = await self._generate_narrative(
                    fusion_result,
                    input_data.question,
                    input_data.language,
                )
            
            processing_time_ms = (time.perf_counter() - start_time) * 1000
            version_id = resolve_version_id()
            corpus_release_id = resolve_corpus_release_id()

            return PipelineOutput(
                request_id=request_id,
                version_id=version_id,
                corpus_release_id=corpus_release_id,
                fusion_result=fusion_result,
                narrative=narrative,
                disclaimer=disclaimer,
                timeline_projection=timeline_projection,
                engine_results=engine_results,
                factor_matrices=factor_matrices,
                processing_time_ms=processing_time_ms,
                raw_factors=raw_factors,
            )
        
        except EngineIdGovernanceError as e:
            logger.warning(
                "Pipeline blocked by engine_id governance: request_id=%s user_id=%s code=%s engine_id=%s",
                request_id,
                input_data.user_id,
                e.code,
                e.engine_id,
            )
            raise
        except Exception as e:
            logger.exception("Pipeline execution failed: request_id=%s", request_id)
            raise
    
    async def _calculate_factors(
        self,
        input_data: PipelineInput,
    ) -> Tuple[List[FactorMatrix], Dict[str, Any]]:
        """
        L1: 计算因子矩阵
        
        Returns:
            (factor_matrices, raw_factors)
            - factor_matrices: 转换后的 FactorMatrix 列表
            - raw_factors: 原始 Factors 对象字典，key 为引擎 ID
        """
        matrices = []
        raw_factors = {}
        
        # 八字计算
        if input_data.birth_data:
            matrix, factors = await self._calculate_bazi(input_data.birth_data)
            if matrix and factors:
                matrices.append(matrix)
                raw_factors["bazi-calculator"] = factors
            
            # 如果有经纬度，也计算西占
            if input_data.birth_data.latitude and input_data.birth_data.longitude:
                astro_matrix, astro_factors = await self._calculate_astro(input_data.birth_data)
                if astro_matrix and astro_factors:
                    matrices.append(astro_matrix)
                    raw_factors["astro-calculator"] = astro_factors
        
        # 梦境分析
        if input_data.dream_text:
            matrix, factors = await self._calculate_dream(input_data.dream_text)
            if matrix and factors:
                matrices.append(matrix)
                raw_factors["dream-extractor"] = factors
        
        # 塔罗分析
        if input_data.tarot:
            matrix, factors = await self._calculate_tarot(input_data.tarot)
            if matrix and factors:
                matrices.append(matrix)
                raw_factors["tarot-interpreter"] = factors
        
        return matrices, raw_factors
    
    async def _calculate_bazi(
        self, birth_data: BirthDataInput
    ) -> Tuple[Optional[FactorMatrix], Optional[Any]]:
        """
        计算八字因子矩阵
        
        Returns:
            (FactorMatrix, BaziFactors) 或 (None, None)
        """
        try:
            from datetime import datetime as dt
            from zoneinfo import ZoneInfo
            from backend.calculators import BaziCalculator, BaziInput
            
            # 构造带时区的datetime
            tz = ZoneInfo(birth_data.timezone)
            birth_datetime = dt(
                birth_data.year, birth_data.month, birth_data.day,
                birth_data.hour, birth_data.minute, tzinfo=tz
            )
            
            # 构造位置参数
            birth_location = None
            if birth_data.longitude is not None and birth_data.latitude is not None:
                birth_location = (birth_data.longitude, birth_data.latitude)
            
            calc = BaziCalculator()
            bazi_input = BaziInput(
                birth_datetime=birth_datetime,
                gender=birth_data.gender,
                birth_location=birth_location,
                birth_place=birth_data.location,  # 地名作为备选
            )
            
            factors = calc.calculate(bazi_input)
            return factors.to_factor_matrix(), factors
        
        except Exception as e:
            logger.error("Bazi calculation failed: %s", e)
            return None, None
    
    async def _calculate_astro(
        self, birth_data: BirthDataInput
    ) -> Tuple[Optional[FactorMatrix], Optional[Any]]:
        """
        计算西占因子矩阵
        
        Returns:
            (FactorMatrix, AstroFactors) 或 (None, None)
        """
        try:
            from datetime import datetime as dt
            from zoneinfo import ZoneInfo
            from backend.calculators.astro import AstroCalculator
            from backend.calculators.astro.models import AstroInput
            
            # 构造带时区的datetime
            tz = ZoneInfo(birth_data.timezone)
            birth_datetime = dt(
                birth_data.year, birth_data.month, birth_data.day,
                birth_data.hour, birth_data.minute, tzinfo=tz
            )
            
            # 构造位置参数
            birth_location = None
            if birth_data.longitude is not None and birth_data.latitude is not None:
                birth_location = (birth_data.longitude, birth_data.latitude)
            
            calc = AstroCalculator()
            astro_input = AstroInput(
                birth_datetime=birth_datetime,
                birth_location=birth_location,
                birth_place=birth_data.location,
                timezone=birth_data.timezone,
            )
            
            factors = calc.calculate(astro_input)
            return factors.to_factor_matrix(), factors
        
        except Exception as e:
            logger.error("Astro calculation failed: %s", e)
            return None, None
    
    async def _calculate_dream(
        self, dream_text: str
    ) -> Tuple[Optional[FactorMatrix], Optional[Any]]:
        """
        提取梦境因子矩阵
        
        Returns:
            (FactorMatrix, DreamFactors) 或 (None, None)
        """
        try:
            from backend.calculators.dream import DreamExtractor
            from backend.calculators.dream.models import DreamInput
            
            extractor = DreamExtractor()
            dream_input = DreamInput(dream_text=dream_text)
            
            factors = extractor.extract(dream_input)
            return factors.to_factor_matrix(), factors
        
        except Exception as e:
            logger.error("Dream extraction failed: %s", e)
            return None, None
    
    async def _calculate_tarot(
        self, tarot: TarotInput
    ) -> Tuple[Optional[FactorMatrix], Optional[Any]]:
        """
        解析塔罗因子矩阵
        
        Returns:
            (FactorMatrix, TarotFactors) 或 (None, None)
        """
        try:
            from backend.calculators.tarot import TarotInterpreter
            from backend.calculators.tarot.models import TarotInput as TarotCalcInput, CardInfo
            
            # 将字符串卡牌名转换为CardInfo对象
            card_infos = []
            for i, card_name in enumerate(tarot.cards):
                position = tarot.positions[i] if tarot.positions and i < len(tarot.positions) else None
                card_infos.append(CardInfo(card_name=card_name, position=position))
            
            interpreter = TarotInterpreter()
            tarot_input = TarotCalcInput(
                cards=card_infos,
                spread_type=tarot.spread_type,
            )
            
            factors = interpreter.interpret(tarot_input)
            return factors.to_factor_matrix(), factors
        
        except Exception as e:
            logger.error("Tarot interpretation failed: %s", e)
            return None, None
    
    async def _execute_rules(
        self,
        matrices: List[FactorMatrix],
        engine_filter: Optional[List[str]] = None,
    ) -> Dict[str, List[RuntimeRuleResult]]:
        """
        L3: 执行规则
        """
        if not matrices:
            return {}
        
        # 使用 RuleEngine 的 batch 执行
        results = self._rule_engine.execute_batch(matrices)
        
        # 如果指定了引擎过滤 (engine_filter 应该已经是标准化的 ID)
        if engine_filter:
            filter_set = set(engine_filter)
            results = {
                k: v for k, v in results.items()
                if k in filter_set
            }
        
        return results
    
    def _fuse_results(
        self,
        engine_results: Dict[str, List[RuntimeRuleResult]],
    ) -> FusionResult:
        """
        L4: 融合结果
        """
        return self._fusion_engine.fuse_results(engine_results)
    
    async def _generate_narrative(
        self,
        fusion_result: FusionResult,
        question: Optional[str],
        language: str,
    ) -> tuple[Optional[str], Optional[str]]:
        """
        L5: 生成叙事
        
        Returns:
            (narrative, disclaimer)
        """
        try:
            # 安全检查输入问题
            if question:
                safety_result = self._safety_moderator.check_input(question)
                if not safety_result.passed:
                    logger.warning("Question blocked by safety check")
                    question = None
            
            # 生成叙事
            output = await self._narrative_generator.generate(
                fusion_result=fusion_result,
                question=question,
            )
            
            return output.content, output.disclaimer
        
        except Exception as e:
            logger.error("Narrative generation failed: %s", e)
            return None, None
    
    async def _generate_timeline(
        self,
        factor_matrices: List[FactorMatrix],
        rule_results: List[RuntimeRuleResult],
        user_id: str,
        years: int = 3,
    ) -> Optional[TimelineProjection]:
        """
        生成时间线推演
        
        Args:
            factor_matrices: 因子矩阵列表
            rule_results: 规则结果列表
            user_id: 用户 ID
            years: 预测年数
            
        Returns:
            TimelineProjection or None if generation fails
        """
        try:
            from backend.services.timeline.projector import get_projector
            
            # 合并因子矩阵
            if not factor_matrices:
                return None
            
            # 使用第一个因子矩阵作为主矩阵（后续可改进为合并逻辑）
            primary_matrix = factor_matrices[0]
            
            projector = get_projector()
            projection = projector.project(
                factor_matrix=primary_matrix,
                rule_results=rule_results,
                user_id=user_id,
                years=years,
            )
            
            logger.info(
                "Timeline generated: %d nodes, %d branch points, years=%d",
                len(projection.nodes),
                len(projection.branch_points),
                years,
            )
            
            return projection
        
        except Exception as e:
            logger.error("Timeline generation failed: %s", e)
            return None


# 全局 Pipeline 实例
_pipeline: Optional[Pipeline] = None


def get_pipeline() -> Pipeline:
    """获取全局 Pipeline 实例"""
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline()
    return _pipeline
