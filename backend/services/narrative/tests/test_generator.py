"""
Narrative Generator Tests

对照 tasks.md 9.3-9.5:
- Requirements: 3.1.1-3.1.4, 3.3.1, 3.3.2, 8.1.1
"""

import pytest

from backend.services.narrative.generator import (
    NarrativeGenerator,
    NarrativeOutput,
    HallucinationDetector,
    HallucinationWarning,
)
from backend.core.contracts import FusionResult, RuntimeRuleResult


class TestNarrativeGeneratorBasic:
    """基础测试"""
    
    @pytest.mark.asyncio
    async def test_generate_with_llm(self, narrative_generator, sample_fusion_result):
        """测试使用 LLM 生成"""
        output = await narrative_generator.generate(sample_fusion_result)
        
        assert output.narrative_id.startswith("nar_")
        assert len(output.content) > 0
        assert output.fusion_id == sample_fusion_result.fusion_id
    
    @pytest.mark.asyncio
    async def test_generate_without_llm(self, narrative_generator_no_llm, sample_fusion_result):
        """测试无 LLM 时的降级输出"""
        output = await narrative_generator_no_llm.generate(sample_fusion_result)
        
        assert output.narrative_id.startswith("nar_")
        assert len(output.content) > 0
        # 降级输出应该包含主题
        for theme in sample_fusion_result.primary_themes[:3]:
            assert theme in output.content
    
    @pytest.mark.asyncio
    async def test_generate_records_time(self, narrative_generator, sample_fusion_result):
        """测试记录生成时间"""
        output = await narrative_generator.generate(sample_fusion_result)
        
        assert output.generation_time_ms > 0
    
    @pytest.mark.asyncio
    async def test_generate_records_tokens(self, narrative_generator, sample_fusion_result):
        """测试记录 Token 用量"""
        output = await narrative_generator.generate(sample_fusion_result)
        
        assert "prompt_tokens" in output.token_usage
        assert "completion_tokens" in output.token_usage


class TestNarrativeGeneratorSafety:
    """安全检查测试"""
    
    @pytest.mark.asyncio
    async def test_safety_check_applied(self, narrative_generator, sample_fusion_result):
        """测试安全检查被应用"""
        output = await narrative_generator.generate(sample_fusion_result)
        
        assert output.safety_result is not None
    
    @pytest.mark.asyncio
    async def test_sensitive_content_has_disclaimer(self, sample_fusion_result):
        """测试敏感内容有 disclaimer"""
        from unittest.mock import AsyncMock, MagicMock
        from backend.core.llm.models import LLMResponse, LLMUsage
        
        # Mock LLM 返回包含健康相关内容
        client = MagicMock()
        client.complete = AsyncMock(return_value=LLMResponse(
            content="您最近可能有些症状，建议注意健康。",
            usage=LLMUsage(prompt_tokens=100, completion_tokens=50, total_tokens=150),
            model_used="test",
            provider_used="test",
            latency_ms=100,
        ))
        
        generator = NarrativeGenerator(llm_client=client, language="zh")
        output = await generator.generate(sample_fusion_result)
        
        # 应该有健康相关的 disclaimer
        if output.safety_result and output.safety_result.topics:
            assert output.disclaimer is not None or "---" in output.content


class TestHallucinationDetector:
    """幻觉检测测试"""
    
    def test_no_hallucination(self, sample_fusion_result):
        """测试无幻觉情况"""
        detector = HallucinationDetector()
        
        # 叙事包含所有主题
        narrative = "您的主要特点是事业突破、财富积累和人际和谐。"
        
        warnings = detector.check(narrative, sample_fusion_result)
        
        # 所有主题都在，不应有警告
        theme_warnings = [w for w in warnings if w.type == "theme_not_mentioned"]
        assert len(theme_warnings) == 0
    
    def test_missing_theme_warning(self, sample_fusion_result):
        """测试缺失主题警告"""
        detector = HallucinationDetector()
        
        # 叙事只包含部分主题
        narrative = "您的主要特点是事业突破。"
        
        warnings = detector.check(narrative, sample_fusion_result)
        
        # 应该有缺失主题的警告
        theme_warnings = [w for w in warnings if w.type == "theme_not_mentioned"]
        assert len(theme_warnings) > 0
    
    def test_overconfidence_warning(self):
        """测试过度自信警告"""
        detector = HallucinationDetector()
        
        # 创建一个简单的规则结果
        simple_rule = RuntimeRuleResult(
            rule_id="test_001",
            matched=True,
            confidence=0.3,
            weight=1.0,
            execution_time_ms=0.0,
        )
        
        # 低置信度的融合结果
        low_confidence_fusion = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["测试主题"],
            evidence_chain=[simple_rule],  # 至少一个
            cross_validation_score=0.3,  # 低置信度
            confidence_matrix={},
            conflicts=[],
            contributing_engines=["test"],
            fusion_time_ms=1.0,
        )
        
        # 叙事使用了过度肯定的词语
        narrative = "测试主题，这一定会发生。"
        
        warnings = detector.check(narrative, low_confidence_fusion)
        
        overconfidence_warnings = [w for w in warnings if w.type == "overconfidence"]
        assert len(overconfidence_warnings) > 0


class TestNarrativeOutputModel:
    """NarrativeOutput 模型测试"""
    
    def test_narrative_output_creation(self):
        """测试 NarrativeOutput 创建"""
        output = NarrativeOutput(
            narrative_id="nar_test123",
            content="测试内容",
            fusion_id="fus_abc123456789",
            language="zh",
            generation_time_ms=100.0,
        )
        
        assert output.narrative_id == "nar_test123"
        assert output.content == "测试内容"
        assert output.language == "zh"
