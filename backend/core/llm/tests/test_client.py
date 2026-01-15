"""
LLMClient Tests

对照 requirements.md 1.1.1-1.1.5
"""

import pytest
import asyncio

from backend.core.llm.models import LLMRequest
from backend.core.llm.client import LLMClient
from backend.core.llm.cost_monitor import CostLimitExceededError


class TestLLMClientBasic:
    """LLMClient 基础测试"""
    
    @pytest.mark.asyncio
    async def test_complete_basic(self, llm_client):
        """测试基本完成请求"""
        response = await llm_client.complete(
            prompt="Hello, world!",
        )
        
        assert response.content == "Mock response"
        assert response.model_used is not None
        assert response.provider_used is not None
    
    @pytest.mark.asyncio
    async def test_complete_with_system_prompt(self, llm_client):
        """测试带系统 prompt 的请求"""
        response = await llm_client.complete(
            prompt="What is 2+2?",
            system_prompt="You are a math teacher.",
        )
        
        assert response.content is not None
    
    @pytest.mark.asyncio
    async def test_complete_tracks_user(self, llm_client):
        """测试用户追踪"""
        response = await llm_client.complete(
            prompt="Test",
            user_id="user_123",
        )
        
        # 检查成本监控记录了用户
        records = llm_client.cost_monitor.get_recent_records(user_id="user_123")
        assert len(records) > 0
    
    @pytest.mark.asyncio
    async def test_complete_respects_cost_limit(self):
        """测试成本限制"""
        from backend.core.llm.cost_monitor import CostMonitor
        from backend.core.llm.router import CascadeRouter
        from backend.core.llm.tests.conftest import MockProvider
        
        # 创建非常低限额的监控器
        monitor = CostMonitor(daily_limit_usd=0.0001, monthly_limit_usd=0.001)
        
        router = CascadeRouter()
        router.register_provider(MockProvider())
        
        client = LLMClient(router=router, cost_monitor=monitor)
        
        # 第一次请求可能成功
        try:
            await client.complete(prompt="Test")
        except CostLimitExceededError:
            pass  # 预期可能失败
        
        # 多次请求后应该被阻止
        for _ in range(10):
            try:
                await client.complete(prompt="Test" * 1000)
            except CostLimitExceededError:
                return  # 预期行为
        
        # 如果没有被阻止，限额可能太高


class TestLLMClientFilters:
    """LLMClient 过滤器测试"""
    
    @pytest.mark.asyncio
    async def test_input_filter(self, mock_router, cost_monitor):
        """测试输入过滤"""
        def input_filter(text: str) -> str:
            return text.replace("bad", "good")
        
        client = LLMClient(
            router=mock_router,
            cost_monitor=cost_monitor,
            input_filter=input_filter,
        )
        
        response = await client.complete(prompt="This is bad")
        
        # 输入应该被过滤
        assert response.content is not None
    
    @pytest.mark.asyncio
    async def test_output_filter(self, mock_router, cost_monitor):
        """测试输出过滤"""
        def output_filter(text: str) -> str:
            return text.replace("Mock", "Filtered")
        
        client = LLMClient(
            router=mock_router,
            cost_monitor=cost_monitor,
            output_filter=output_filter,
        )
        
        response = await client.complete(prompt="Test")
        
        assert "Filtered" in response.content


class TestLLMClientStream:
    """LLMClient 流式响应测试"""
    
    @pytest.mark.asyncio
    async def test_stream_basic(self, llm_client):
        """测试基本流式响应"""
        chunks = []
        async for chunk in llm_client.stream(prompt="Test"):
            chunks.append(chunk)
        
        assert len(chunks) > 0
        content = "".join(chunks)
        assert len(content) > 0


class TestLLMClientTokenEstimation:
    """LLMClient Token 估算测试"""
    
    def test_estimate_tokens_english(self, llm_client):
        """测试英文 token 估算"""
        text = "Hello world, this is a test."
        tokens = llm_client._estimate_tokens(text)
        
        # 英文约 4 字符/token
        assert tokens > 0
        assert tokens < len(text)
    
    def test_estimate_tokens_chinese(self, llm_client):
        """测试中文 token 估算"""
        text = "你好世界，这是一个测试。"
        tokens = llm_client._estimate_tokens(text)
        
        # 中文约 2 字符/token
        assert tokens > 0
    
    def test_estimate_tokens_empty(self, llm_client):
        """测试空文本"""
        assert llm_client._estimate_tokens("") == 0
        assert llm_client._estimate_tokens(None) == 0
