"""
LLM Core Test Fixtures
"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from typing import AsyncIterator

from backend.core.llm.models import (
    LLMRequest,
    LLMResponse,
    LLMUsage,
    ModelCapability,
    ModelConfig,
)
from backend.core.llm.providers.base import LLMProvider
from backend.core.llm.router import CascadeRouter
from backend.core.llm.cost_monitor import CostMonitor
from backend.core.llm.client import LLMClient


class MockProvider(LLMProvider):
    """Mock LLM Provider for testing"""
    
    def __init__(self, name: str = "mock", response_content: str = "Mock response"):
        self._name = name
        self._response_content = response_content
        self._call_count = 0
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def supported_models(self) -> list[str]:
        return ["mock-model", "mock-fast"]
    
    async def complete(self, request: LLMRequest) -> LLMResponse:
        self._call_count += 1
        return LLMResponse(
            content=self._response_content,
            usage=LLMUsage(
                prompt_tokens=len(request.prompt) // 4,
                completion_tokens=len(self._response_content) // 4,
                total_tokens=len(request.prompt) // 4 + len(self._response_content) // 4,
            ),
            model_used=request.model or "mock-model",
            provider_used=self._name,
            latency_ms=100.0,
            finish_reason="stop",
            request_id=request.request_id,
        )
    
    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        self._call_count += 1
        for word in self._response_content.split():
            yield word + " "


@pytest.fixture
def mock_provider():
    """创建 Mock Provider"""
    return MockProvider()


@pytest.fixture
def mock_router(mock_provider):
    """创建带 Mock Provider 的 Router"""
    router = CascadeRouter()
    router.register_provider(mock_provider)
    return router


@pytest.fixture
def cost_monitor():
    """创建 CostMonitor"""
    return CostMonitor(
        daily_limit_usd=10.0,
        monthly_limit_usd=100.0,
    )


@pytest.fixture
def llm_client(mock_router, cost_monitor):
    """创建 LLMClient"""
    return LLMClient(
        router=mock_router,
        cost_monitor=cost_monitor,
    )


@pytest.fixture
def sample_request():
    """创建示例请求"""
    return LLMRequest(
        prompt="What is the meaning of life?",
        system_prompt="You are a helpful assistant.",
        max_tokens=100,
        temperature=0.7,
        user_id="test_user",
    )


@pytest.fixture
def sample_model_config():
    """创建示例模型配置"""
    return ModelConfig(
        provider="openai",
        model_id="gpt-4o-mini",
        capabilities=[ModelCapability.FAST, ModelCapability.REASONING],
        cost_per_1k_input_tokens=0.15,
        cost_per_1k_output_tokens=0.60,
        avg_latency_ms=500,
        max_context_tokens=128000,
        priority=1,
    )
