"""
Narrative Generator

叙事生成器。

对照 tasks.md 9.3, 9.4, 9.5:
- Requirements: 3.1.1-3.1.4, 3.3.1, 3.3.2
- ⚠️ 陷阱: 不能完全依赖幻觉检测，只做辅助

设计原则:
- 整合 LLMClient + PromptBuilder + SafetyModerator
- 幻觉检测只做辅助，不阻止输出
- 输出前安全检查
"""

import logging
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

from backend.core.contracts import FusionResult
from backend.core.engines.governance import validate_engine_ids_or_raise
from backend.core.llm.client import LLMClient
from backend.services.narrative.prompt_builder import PromptBuilder
from backend.services.safety.moderator import SafetyModerator, SafetyResult

logger = logging.getLogger(__name__)


@dataclass
class HallucinationWarning:
    """幻觉警告"""
    type: str
    detail: str
    severity: str = "low"  # low, medium, high


@dataclass
class NarrativeOutput:
    """叙事输出"""
    narrative_id: str
    content: str
    fusion_id: str
    language: str
    generation_time_ms: float
    token_usage: Dict[str, int] = field(default_factory=dict)
    hallucination_warnings: List[HallucinationWarning] = field(default_factory=list)
    safety_result: Optional[SafetyResult] = None
    disclaimer: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)


class HallucinationDetector:
    """
    幻觉检测器
    
    检测叙事与融合结果的不一致。
    
    ⚠️ 重要:
    - 只做辅助检测，不能完全依赖
    - 检测结果作为警告，不阻止输出
    """
    
    def check(
        self,
        narrative: str,
        fusion_result: FusionResult,
    ) -> List[HallucinationWarning]:
        """
        检测幻觉
        
        Args:
            narrative: 生成的叙事
            fusion_result: 原始融合结果
            
        Returns:
            幻觉警告列表
        """
        warnings = []
        
        # 1. 检查主题一致性
        for theme in fusion_result.primary_themes:
            # 简单检查：主题应该在叙事中被提及
            # 注意：这是非常粗略的检测，不能完全依赖
            if theme not in narrative:
                # 可能只是表述不同，标记为 low severity
                warnings.append(HallucinationWarning(
                    type="theme_not_mentioned",
                    detail=f"Theme '{theme}' not found in narrative",
                    severity="low",
                ))
        
        # 2. 检查是否出现了明显的虚构内容
        # 例如：提及了不存在的具体日期或数字
        # 这里只做非常保守的检测
        
        # 3. 检查置信度是否被过度夸大
        # 如果融合结果置信度较低，但叙事表述过于肯定
        if fusion_result.cross_validation_score < 0.5:
            certainty_words = ["一定", "肯定", "必然", "绝对", "definitely", "certainly", "absolutely"]
            for word in certainty_words:
                if word in narrative.lower():
                    warnings.append(HallucinationWarning(
                        type="overconfidence",
                        detail=f"Narrative uses certain language '{word}' despite low confidence",
                        severity="medium",
                    ))
                    break
        
        return warnings


class NarrativeGenerator:
    """
    叙事生成器
    
    功能:
    - 从 FusionResult 生成叙事
    - 整合 LLMClient, PromptBuilder, SafetyModerator
    - 幻觉检测 (辅助)
    - 安全检查
    """
    
    DEFAULT_MAX_TOKENS = 1500
    DEFAULT_TEMPERATURE = 0.7
    
    def __init__(
        self,
        llm_client: Optional[LLMClient] = None,
        prompt_builder: Optional[PromptBuilder] = None,
        safety_moderator: Optional[SafetyModerator] = None,
        language: str = "zh",
    ):
        """
        初始化叙事生成器
        
        Args:
            llm_client: LLM 客户端
            prompt_builder: Prompt 构建器
            safety_moderator: 安全审核器
            language: 语言
        """
        self.language = language
        self._llm_client = llm_client
        self._prompt_builder = prompt_builder or PromptBuilder(language=language)
        self._safety_moderator = safety_moderator or SafetyModerator(language=language)
        self._hallucination_detector = HallucinationDetector()
    
    async def generate(
        self,
        fusion_result: FusionResult,
        question: Optional[str] = None,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        user_id: Optional[str] = None,
    ) -> NarrativeOutput:
        """
        生成叙事
        
        Args:
            fusion_result: 融合结果
            question: 用户问题
            max_tokens: 最大输出 token
            temperature: 温度参数
            user_id: 用户 ID
            
        Returns:
            NarrativeOutput
        """
        import time
        start_time = time.perf_counter()
        
        narrative_id = f"nar_{uuid.uuid4().hex[:12]}"

        # Gate-0: engine_id 格式 + registry 校验（确定性拒绝原因）
        if getattr(fusion_result, "contributing_engines", None):
            validate_engine_ids_or_raise(fusion_result.contributing_engines)
        
        # 1. 构建 Prompt
        prompts = self._prompt_builder.build(
            fusion_result=fusion_result,
            question=question,
        )
        
        # 2. 调用 LLM 生成
        if self._llm_client is None:
            # 无 LLM 客户端时返回模板输出
            content = self._generate_template_output(fusion_result)
            token_usage = {"prompt_tokens": 0, "completion_tokens": 0}
        else:
            response = await self._llm_client.complete(
                prompt=prompts["user_prompt"],
                system_prompt=prompts["system_prompt"],
                max_tokens=max_tokens,
                temperature=temperature,
                user_id=user_id,
            )
            content = response.content
            token_usage = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            }
        
        # 3. 安全检查输出
        safety_result = self._safety_moderator.check_output(content)
        
        # 处理不安全输出
        if not safety_result.passed:
            content = safety_result.filtered_content or "[内容已过滤]"
        
        # 4. 幻觉检测 (辅助)
        hallucination_warnings = self._hallucination_detector.check(
            content, fusion_result
        )
        
        # 5. 添加 disclaimer (如需要)
        disclaimer = None
        if safety_result.topics:
            disclaimer = safety_result.disclaimer
            if disclaimer:
                content = self._safety_moderator.inject_disclaimer(
                    content, safety_result.topics
                )
        
        generation_time_ms = (time.perf_counter() - start_time) * 1000
        
        return NarrativeOutput(
            narrative_id=narrative_id,
            content=content,
            fusion_id=fusion_result.fusion_id,
            language=self.language,
            generation_time_ms=generation_time_ms,
            token_usage=token_usage,
            hallucination_warnings=hallucination_warnings,
            safety_result=safety_result,
            disclaimer=disclaimer,
        )
    
    def _generate_template_output(self, fusion_result: FusionResult) -> str:
        """
        生成模板输出 (无 LLM 时的降级方案)
        """
        if self.language == "zh":
            themes_text = "、".join(fusion_result.primary_themes[:3])
            return f"""## 分析报告

### 总体概述
根据综合分析，您当前的主要特点为：{themes_text}。
交叉验证分数为 {fusion_result.cross_validation_score:.0%}，整体可信度较高。

### 维度解读
本次分析涵盖了 {len(fusion_result.contributing_engines)} 个分析引擎的综合结果。

### 建议
以上解读仅供参考，具体情况请结合实际。"""
        else:
            themes_text = ", ".join(fusion_result.primary_themes[:3])
            return f"""## Analysis Report

### Overview
Based on comprehensive analysis, your main characteristics are: {themes_text}.
Cross-validation score is {fusion_result.cross_validation_score:.0%}, indicating high overall confidence.

### Dimension Analysis
This analysis integrates results from {len(fusion_result.contributing_engines)} analysis engines.

### Suggestions
The above interpretation is for reference only, please consider your actual situation."""
    
    async def generate_version_narrative(
        self,
        version_set: "LifeVersionSet",
        comparison: "VersionComparison",
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ) -> str:
        """
        生成版本对比叙事
        
        从版本集合和对比结果生成人性化的叙事文本。
        
        Args:
            version_set: 人生版本集合
            comparison: 版本对比视图
            max_tokens: 最大输出 token
            temperature: 温度参数
            
        Returns:
            版本对比叙事文本
        """
        import time
        start_time = time.perf_counter()
        
        # 构建版本对比 Prompt
        prompt = self._build_version_prompt(version_set, comparison)
        
        if self._llm_client is None:
            # 无 LLM 时使用模板
            return self._generate_version_template(version_set, comparison)
        
        response = await self._llm_client.complete(
            prompt=prompt["user_prompt"],
            system_prompt=prompt["system_prompt"],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        
        logger.info(
            f"Generated version narrative in "
            f"{(time.perf_counter() - start_time) * 1000:.1f}ms"
        )
        
        return response.content
    
    def _build_version_prompt(
        self,
        version_set: "LifeVersionSet",
        comparison: "VersionComparison",
    ) -> Dict[str, str]:
        """构建版本对比 Prompt"""
        # 构建版本摘要
        version_summaries = []
        for v in version_set.versions:
            outcomes = ", ".join(
                f"{axis}: {score:.1f}" 
                for axis, score in list(v.expected_outcomes.items())[:3]
            )
            version_summaries.append(
                f"- {v.title} ({v.subtitle}): {outcomes}"
            )
        versions_text = "\n".join(version_summaries)
        
        # 构建对比矩阵描述
        matrix_lines = []
        for vid, scores in comparison.matrix.items():
            matrix_lines.append(f"  {vid}: {scores}")
        matrix_text = "\n".join(matrix_lines)
        
        system_prompt = """你是一位专业的人生规划顾问。
请根据提供的人生版本对比信息，生成一段客观、有洞察力的对比分析。

要求：
1. 不偏不倚地分析每个版本的优劣
2. 突出版本间的核心差异
3. 帮助用户理解不同选择的潜在后果
4. 使用温和、鼓励的语气
5. 不做绝对性判断，尊重用户自主选择"""

        user_prompt = f"""请对以下{len(version_set.versions)}个人生版本进行对比分析：

## 版本列表
{versions_text}

## 对比维度
{', '.join(comparison.axes)}

## 对比矩阵
{matrix_text}

请生成一段300-500字的对比分析。"""

        return {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
        }
    
    def _generate_version_template(
        self,
        version_set: "LifeVersionSet",
        comparison: "VersionComparison",
    ) -> str:
        """生成版本对比模板输出 (无 LLM 时的降级方案)"""
        if self.language == "zh":
            version_names = "、".join(v.title for v in version_set.versions)
            return f"""## 版本对比分析

### 概述
{comparison.summary_zh}

### 可选版本
本次为您生成了 {len(version_set.versions)} 个版本：{version_names}。

### 对比维度
我们从以下维度进行对比：{', '.join(comparison.axes[:5])}。

### 建议
每个版本都有其适用场景，请根据您的实际情况和价值取向做出选择。"""
        else:
            version_names = ", ".join(v.title for v in version_set.versions)
            return f"""## Version Comparison Analysis

### Overview
{comparison.summary_zh}

### Available Versions
We have generated {len(version_set.versions)} versions for you: {version_names}.

### Comparison Dimensions
We compare across: {', '.join(comparison.axes[:5])}.

### Suggestion
Each version has its applicable scenarios. Please make your choice based on your actual situation and values."""
