"""
Prompt Builder Tests

对照 tasks.md 9.2:
- Requirements: 3.2.1-3.2.3, 8.1.1
"""

import pytest

from backend.services.narrative.prompt_builder import PromptBuilder


class TestPromptBuilderBasic:
    """基础测试"""
    
    def test_build_prompt(self, prompt_builder_zh, sample_fusion_result):
        """测试构建 Prompt"""
        result = prompt_builder_zh.build(sample_fusion_result)
        
        assert "system_prompt" in result
        assert "user_prompt" in result
        assert len(result["system_prompt"]) > 0
        assert len(result["user_prompt"]) > 0
    
    def test_prompt_contains_themes(self, prompt_builder_zh, sample_fusion_result):
        """测试 Prompt 包含主题"""
        result = prompt_builder_zh.build(sample_fusion_result)
        
        for theme in sample_fusion_result.primary_themes:
            assert theme in result["user_prompt"]
    
    def test_prompt_contains_score(self, prompt_builder_zh, sample_fusion_result):
        """测试 Prompt 包含分数"""
        result = prompt_builder_zh.build(sample_fusion_result)
        
        assert "0.87" in result["user_prompt"]
    
    def test_prompt_with_question(self, prompt_builder_zh, sample_fusion_result):
        """测试带问题的 Prompt"""
        result = prompt_builder_zh.build(
            sample_fusion_result,
            question="我今年适合换工作吗？",
        )
        
        assert "换工作" in result["user_prompt"]


class TestPromptBuilderLanguage:
    """多语言测试"""
    
    def test_chinese_prompt(self, prompt_builder_zh, sample_fusion_result):
        """测试中文 Prompt"""
        result = prompt_builder_zh.build(sample_fusion_result)
        
        assert "命理分析师" in result["system_prompt"]
        assert "融合分析结果" in result["user_prompt"]
    
    def test_english_prompt(self, prompt_builder_en, sample_fusion_result):
        """测试英文 Prompt"""
        result = prompt_builder_en.build(sample_fusion_result)
        
        assert "professional analyst" in result["system_prompt"]
        assert "Fusion Analysis Results" in result["user_prompt"]


class TestPromptBuilderTokenControl:
    """Token 控制测试"""
    
    def test_estimate_tokens_chinese(self, prompt_builder_zh):
        """测试中文 Token 估算"""
        text = "你好世界"
        tokens = prompt_builder_zh.estimate_tokens(text)
        
        # 中文约 2 字符/token
        assert tokens > 0
        assert tokens < len(text)
    
    def test_estimate_tokens_english(self, prompt_builder_en):
        """测试英文 Token 估算"""
        text = "Hello world this is a test"
        tokens = prompt_builder_en.estimate_tokens(text)
        
        # 英文约 4 字符/token
        assert tokens > 0
        assert tokens < len(text)
    
    def test_long_context_truncated(self, prompt_builder_zh, sample_fusion_result):
        """测试长上下文被截断"""
        long_context = "历史对话内容" * 1000
        
        result = prompt_builder_zh.build_with_context(
            sample_fusion_result,
            context=long_context,
        )
        
        # 上下文应该被截断
        assert len(result["user_prompt"]) < len(long_context)
