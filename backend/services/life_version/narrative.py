"""
Version Narrative Service

版本叙事生成服务，使用分层 LLM 生成版本对比叙事。

对照文档: docs/ls_roadmap_executable.md Task 3.4

⚠️ 弃用警告 (2025-12):
此服务的核心功能已被 LLMOrchestrator 替代。
新代码应使用：
    from backend.core.llm import get_orchestrator, ScenarioType
    orchestrator = get_orchestrator()
    result = await orchestrator.generate(
        scenario=ScenarioType.LIFE_VERSION,
        fusion_result=fusion_result,
    )

此文件保留以支持向后兼容，但不再推荐使用。
"""

import logging
import warnings
from typing import Optional

from backend.core.contracts.life_version_models import (
    LifeVersionSet,
    VersionComparison,
)
from backend.core.llm import (
    LLMLayer,
    LLMRequest,
    get_layered_router,
)

logger = logging.getLogger(__name__)


class VersionNarrativeService:
    """
    版本叙事生成服务
    
    ⚠️ DEPRECATED: 此类已被弃用，请使用 LLMOrchestrator 代替。
    
    功能:
    - 从版本集合生成对比叙事
    - 支持中英文双语生成
    - 使用分层 LLM 优化成本
    
    迁移指南:
        # 旧代码
        service = VersionNarrativeService()
        narrative = await service.generate_comparison_narrative(version_set, comparison)
        
        # 新代码
        from backend.core.llm import get_orchestrator, ScenarioType
        from backend.api.routes.versions import _build_version_fusion_result
        
        fusion_result = _build_version_fusion_result(version_set)
        orchestrator = get_orchestrator()
        result = await orchestrator.generate(
            scenario=ScenarioType.LIFE_VERSION,
            fusion_result=fusion_result,
        )
        narrative = result.content
    """
    
    def __init__(self, language: str = "zh"):
        """
        初始化服务
        
        Args:
            language: 目标语言 ("zh" 或 "en")
        """
        warnings.warn(
            "VersionNarrativeService is deprecated. "
            "Use LLMOrchestrator with ScenarioType.LIFE_VERSION instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.language = language
        self._router = get_layered_router()
    
    async def generate_comparison_narrative(
        self,
        version_set: LifeVersionSet,
        comparison: VersionComparison,
        max_tokens: int = 1500,
    ) -> str:
        """
        生成版本对比叙事
        
        Args:
            version_set: 人生版本集合
            comparison: 版本对比视图
            max_tokens: 最大输出 token
            
        Returns:
            版本对比叙事文本
        """
        if not self._router.is_available:
            logger.warning("LLM router not available, using template")
            return self._generate_template_narrative(version_set, comparison)
        
        # 构建 Prompt
        system_prompt, user_prompt = self._build_prompts(version_set, comparison)
        
        # 选择生成层模型
        layer = LLMLayer.LAYER_B_CN if self.language == "zh" else LLMLayer.LAYER_B_EN
        provider, model = self._router.select(layer)
        
        if not provider:
            logger.warning("No provider available, using template")
            return self._generate_template_narrative(version_set, comparison)
        
        # 获取层配置
        layer_config = self._router.get_layer_config(layer)
        temperature = layer_config.temperature if layer_config else 0.7
        
        # 构建请求
        request = LLMRequest(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        
        try:
            # 调用 LLM
            response = await provider.complete(request)
            
            # 记录 token 使用
            self._router.record_tokens(layer, response.usage.total_tokens)
            
            logger.info(
                f"Generated version narrative: "
                f"model={response.model_used}, "
                f"tokens={response.usage.total_tokens}, "
                f"latency={response.latency_ms:.1f}ms"
            )
            
            return response.content
            
        except Exception as e:
            logger.error(f"Failed to generate narrative: {e}")
            return self._generate_template_narrative(version_set, comparison)
    
    async def generate_version_summary(
        self,
        version_set: LifeVersionSet,
        version_id: str,
    ) -> str:
        """
        生成单个版本的摘要
        
        Args:
            version_set: 版本集合
            version_id: 目标版本 ID
            
        Returns:
            版本摘要文本
        """
        # 查找目标版本
        version = next(
            (v for v in version_set.versions if v.version_id == version_id),
            None
        )
        if not version:
            return ""
        
        if not self._router.is_available:
            return self._generate_template_summary(version)
        
        # 构建 Prompt
        if self.language == "zh":
            system_prompt = "你是一位专业的人生规划顾问，请用简洁的语言总结这个人生版本。"
            user_prompt = f"""请为以下人生版本生成一段100字左右的摘要：

标题：{version.title}
副标题：{version.subtitle}
策略：{', '.join(version.strategy)}
风险：{', '.join(version.risks[:3])}
适合人群：{', '.join(version.suitable_for[:3])}"""
        else:
            system_prompt = "You are a professional life planning consultant. Summarize this life version concisely."
            user_prompt = f"""Generate a ~50 word summary for this life version:

Title: {version.title}
Subtitle: {version.subtitle}
Strategy: {', '.join(version.strategy)}
Risks: {', '.join(version.risks[:3])}
Best for: {', '.join(version.suitable_for[:3])}"""
        
        # 选择模型
        layer = LLMLayer.LAYER_B_CN if self.language == "zh" else LLMLayer.LAYER_B_EN
        provider, model = self._router.select(layer)
        
        if not provider:
            return self._generate_template_summary(version)
        
        request = LLMRequest(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_tokens=200,
            temperature=0.5,
        )
        
        try:
            response = await provider.complete(request)
            self._router.record_tokens(layer, response.usage.total_tokens)
            return response.content
        except Exception as e:
            logger.error(f"Failed to generate summary: {e}")
            return self._generate_template_summary(version)
    
    def _build_prompts(
        self,
        version_set: LifeVersionSet,
        comparison: VersionComparison,
    ) -> tuple[str, str]:
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
        
        if self.language == "zh":
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
        else:
            system_prompt = """You are a professional life planning consultant.
Generate an objective, insightful comparison analysis based on the provided life version information.

Requirements:
1. Analyze pros and cons of each version impartially
2. Highlight core differences between versions
3. Help users understand potential consequences of different choices
4. Use a warm, encouraging tone
5. Avoid absolute judgments, respect user autonomy"""

            user_prompt = f"""Compare the following {len(version_set.versions)} life versions:

## Version List
{versions_text}

## Comparison Axes
{', '.join(comparison.axes)}

## Comparison Matrix
{matrix_text}

Generate a 200-300 word comparison analysis."""
        
        return system_prompt, user_prompt
    
    def _generate_template_narrative(
        self,
        version_set: LifeVersionSet,
        comparison: VersionComparison,
    ) -> str:
        """生成模板叙事 (无 LLM 时的降级方案)"""
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

### Comparison Axes
We compare across: {', '.join(comparison.axes[:5])}.

### Suggestion
Each version has its applicable scenarios. Please make your choice based on your situation and values."""
    
    def _generate_template_summary(self, version) -> str:
        """生成模板摘要"""
        if self.language == "zh":
            return f"{version.title}：{version.subtitle}。主要策略包括{'、'.join(version.strategy[:2])}。"
        else:
            return f"{version.title}: {version.subtitle}. Key strategies include {', '.join(version.strategy[:2])}."
