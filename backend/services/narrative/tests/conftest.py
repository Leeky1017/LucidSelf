"""
Narrative Generator Test Fixtures
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from backend.core.contracts import FusionResult, RuntimeRuleResult
from backend.core.llm.models import LLMResponse, LLMUsage
from backend.services.narrative.prompt_builder import PromptBuilder
from backend.services.narrative.generator import NarrativeGenerator


@pytest.fixture
def sample_rule_result():
    """创建示例规则结果"""
    return RuntimeRuleResult(
        rule_id="bazi_career_001",
        matched=True,
        dimension="事业",
        level="吉",
        confidence=0.85,
        weight=1.5,
        execution_time_ms=1.0,
        evidence_factors=["day_master", "season"],
    )


@pytest.fixture
def sample_fusion_result(sample_rule_result):
    """创建示例融合结果"""
    return FusionResult(
        fusion_id="fus_abc123456789",
        primary_themes=["事业突破", "财富积累", "人际和谐"],
        evidence_chain=[sample_rule_result],
        cross_validation_score=0.87,
        confidence_matrix={"career": 0.85},
        conflicts=[],
        contributing_engines=["bazi-calculator", "astro-calculator"],
        fusion_time_ms=15.0,
    )


@pytest.fixture
def prompt_builder_zh():
    """中文 Prompt 构建器"""
    return PromptBuilder(language="zh")


@pytest.fixture
def prompt_builder_en():
    """英文 Prompt 构建器"""
    return PromptBuilder(language="en")


@pytest.fixture
def mock_llm_client():
    """Mock LLM 客户端"""
    client = MagicMock()
    client.complete = AsyncMock(return_value=LLMResponse(
        content="这是测试生成的叙事内容。您的事业运势良好。",
        usage=LLMUsage(prompt_tokens=100, completion_tokens=50, total_tokens=150),
        model_used="gpt-4o-mini",
        provider_used="openai",
        latency_ms=500,
    ))
    return client


@pytest.fixture
def narrative_generator(mock_llm_client):
    """带 Mock LLM 的叙事生成器"""
    return NarrativeGenerator(
        llm_client=mock_llm_client,
        language="zh",
    )


@pytest.fixture
def narrative_generator_no_llm():
    """无 LLM 的叙事生成器"""
    return NarrativeGenerator(
        llm_client=None,
        language="zh",
    )
