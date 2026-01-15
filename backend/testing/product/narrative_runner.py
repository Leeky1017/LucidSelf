"""
Narrative Golden Runner

NarrativeGolden 执行器，用于产品级叙事质量验收。

对照 design.md §2.1 目录结构
对照 Requirements R-6-1-03, R-6-1-07
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from backend.core.contracts import NarrativeGolden
from backend.testing.framework.assertions import NarrativeAssertions
from backend.testing.framework.runner import TestResult, TestRunner
from backend.testing.product.eval_agent import EvalAgent

if TYPE_CHECKING:
    from backend.core.llm.client import LLMClient

logger = logging.getLogger(__name__)


class NarrativeGoldenRunner(TestRunner[NarrativeGolden]):
    """
    叙事黄金标准执行器
    
    对照 Requirements R-6-1-03, R-6-1-07
    
    用于执行 NarrativeGolden，验证叙事质量。
    """
    
    def __init__(
        self,
        llm_client: Optional["LLMClient"] = None,
        narrative_service: Optional[Any] = None,
        name: str = "NarrativeGoldenRunner",
    ):
        """
        初始化叙事黄金标准执行器
        
        Args:
            llm_client: LLM 客户端 (用于 EvalAgent)
            narrative_service: 叙事服务 (用于生成叙事)
            name: 执行器名称
        """
        super().__init__(name)
        self._llm_client = llm_client
        self.narrative_service = narrative_service
        self._eval_agent: Optional[EvalAgent] = None
    
    @property
    def eval_agent(self) -> EvalAgent:
        """获取评估代理"""
        if self._eval_agent is None:
            self._eval_agent = EvalAgent(llm_client=self._llm_client)
        return self._eval_agent
    
    async def run(self, test_case: NarrativeGolden) -> TestResult:
        """
        执行单个叙事黄金标准测试
        
        Args:
            test_case: NarrativeGolden 实例
            
        Returns:
            TestResult: 测试结果
        """
        start_time = time.perf_counter()
        
        try:
            # 1. 生成叙事
            narrative = await self._generate_narrative(test_case.scenario)
            
            # 2. 基础检查（主题、禁用表述）
            basic_check = self._check_basic_requirements(test_case, narrative)
            if not basic_check["passed"]:
                duration = (time.perf_counter() - start_time) * 1000
                return TestResult.failure(
                    test_id=test_case.golden_id,
                    duration_ms=duration,
                    error=basic_check["error"],
                    details=basic_check["details"],
                    runner_name=self.name,
                )
            
            # 3. LLM 评估
            eval_result = await self.eval_agent.evaluate(
                narrative=narrative,
                scenario=test_case.scenario,
                model=test_case.eval_model,
            )
            
            # 4. 检查分数
            score = eval_result.get("score", 0.0)
            passed = (
                score >= test_case.min_quality_score and
                score >= test_case.historical_avg_score
            )
            
            duration = (time.perf_counter() - start_time) * 1000
            
            details = {
                "narrative_length": len(narrative),
                "eval_score": score,
                "min_required_score": test_case.min_quality_score,
                "historical_avg": test_case.historical_avg_score,
                "eval_feedback": eval_result.get("feedback", ""),
                "eval_model": test_case.eval_model,
            }
            
            if passed:
                return TestResult.success(
                    test_id=test_case.golden_id,
                    duration_ms=duration,
                    details=details,
                    runner_name=self.name,
                )
            else:
                error_parts = []
                if score < test_case.min_quality_score:
                    error_parts.append(
                        f"Score {score:.2f} < min {test_case.min_quality_score:.2f}"
                    )
                if score < test_case.historical_avg_score:
                    error_parts.append(
                        f"Score {score:.2f} < historical avg {test_case.historical_avg_score:.2f}"
                    )
                
                return TestResult.failure(
                    test_id=test_case.golden_id,
                    duration_ms=duration,
                    error="; ".join(error_parts),
                    details=details,
                    runner_name=self.name,
                )
                
        except Exception as e:
            duration = (time.perf_counter() - start_time) * 1000
            logger.error(
                f"Narrative golden {test_case.golden_id} error: {e}",
                exc_info=True,
            )
            return TestResult.create_error(
                test_id=test_case.golden_id,
                duration_ms=duration,
                error_msg=str(e),
                error_type=type(e).__name__,
                runner_name=self.name,
            )
    
    async def _generate_narrative(
        self,
        scenario: Dict[str, Any],
    ) -> str:
        """
        生成叙事
        
        Args:
            scenario: 场景数据
            
        Returns:
            生成的叙事文本
        """
        if self.narrative_service:
            if hasattr(self.narrative_service, "generate"):
                return await self._safe_call(
                    self.narrative_service.generate, scenario
                )
        
        # Mock 实现
        return f"[Mock narrative for scenario: {scenario.get('question', 'unknown')}]"
    
    async def _safe_call(self, func, *args, **kwargs) -> Any:
        """安全调用（支持同步和异步）"""
        import asyncio
        
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return func(*args, **kwargs)
    
    def _check_basic_requirements(
        self,
        test_case: NarrativeGolden,
        narrative: str,
    ) -> Dict[str, Any]:
        """
        检查基础要求
        
        Args:
            test_case: 测试用例
            narrative: 叙事文本
            
        Returns:
            检查结果
        """
        details = {
            "narrative_length": len(narrative),
            "checked_themes": test_case.must_include_themes,
            "checked_forbidden": test_case.forbidden_expressions,
        }
        
        # 检查必须包含的主题
        missing_themes = [
            t for t in test_case.must_include_themes
            if t not in narrative
        ]
        if missing_themes:
            return {
                "passed": False,
                "error": f"Missing required themes: {missing_themes}",
                "details": {**details, "missing_themes": missing_themes},
            }
        
        # 检查禁用表述
        found_forbidden = [
            e for e in test_case.forbidden_expressions
            if e in narrative
        ]
        if found_forbidden:
            return {
                "passed": False,
                "error": f"Found forbidden expressions: {found_forbidden}",
                "details": {**details, "found_forbidden": found_forbidden},
            }
        
        return {
            "passed": True,
            "error": None,
            "details": details,
        }
