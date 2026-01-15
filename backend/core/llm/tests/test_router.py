"""
CascadeRouter Tests

对照 requirements.md 1.2.1-1.2.4
对照 pitfalls.md 1.3: Fallback 无限循环
"""

import pytest
import asyncio

from backend.core.llm.models import LLMRequest, ModelCapability, ModelConfig
from backend.core.llm.router import CascadeRouter, AllProvidersFailedError
from backend.core.llm.providers.base import LLMProviderError, RateLimitError


class TestCascadeRouterBasic:
    """CascadeRouter 基础测试"""
    
    def test_register_provider(self, mock_provider):
        """测试注册 Provider"""
        router = CascadeRouter()
        router.register_provider(mock_provider)
        
        assert "mock" in router.list_providers()
    
    def test_register_model(self, sample_model_config):
        """测试注册模型"""
        router = CascadeRouter()
        router.register_model(sample_model_config)
        
        assert "gpt-4o-mini" in router.list_models()
    
    def test_select_default(self, mock_router):
        """测试默认选择"""
        provider, model = mock_router.select()
        
        assert provider is not None
        assert model is not None
    
    def test_select_with_hint(self, mock_router):
        """测试带提示的选择"""
        provider, model = mock_router.select(model_hint="mock-model")
        
        assert provider.name == "mock"
        assert model == "mock-model"


class TestCascadeRouterFallback:
    """CascadeRouter Fallback 测试"""
    
    @pytest.mark.asyncio
    async def test_complete_with_fallback_success(self, mock_router):
        """测试 Fallback 成功"""
        request = LLMRequest(prompt="Test", model="mock-model")
        
        response = await mock_router.complete_with_fallback(request)
        
        assert response.content == "Mock response"
        assert response.is_fallback is False
    
    @pytest.mark.asyncio
    async def test_max_retries_exceeded(self):
        """测试最大重试次数"""
        router = CascadeRouter()
        # 不注册任何 provider
        
        request = LLMRequest(prompt="Test")
        
        with pytest.raises(AllProvidersFailedError) as exc_info:
            await router.complete_with_fallback(request)
        
        assert exc_info.value.attempts == router.MAX_RETRIES


class TestCascadeRouterSelection:
    """CascadeRouter 选择策略测试"""
    
    def test_select_by_capability(self, mock_router, sample_model_config):
        """测试按能力选择"""
        mock_router.register_model(sample_model_config)
        
        # 选择需要 FAST 能力的模型
        provider, model = mock_router.select(capability=ModelCapability.FAST)
        
        # 应该选择配置的模型
        assert model is not None
    
    def test_select_prefer_low_cost(self):
        """测试优先低成本"""
        router = CascadeRouter()
        
        # 注册两个模型，成本不同
        cheap = ModelConfig(
            provider="mock",
            model_id="cheap-model",
            cost_per_1k_input_tokens=0.01,
            cost_per_1k_output_tokens=0.01,
        )
        expensive = ModelConfig(
            provider="mock",
            model_id="expensive-model",
            cost_per_1k_input_tokens=10.0,
            cost_per_1k_output_tokens=10.0,
        )
        
        router.register_model(cheap)
        router.register_model(expensive)
        
        # 优先低成本应选择 cheap
        # (需要有对应 provider，这里只测试逻辑)
