"""
LLM Models Tests
"""

import pytest
from datetime import datetime

from backend.core.llm.models import (
    LLMRequest,
    LLMResponse,
    LLMUsage,
    LLMUsageRecord,
    ModelCapability,
    ModelConfig,
)


class TestLLMRequest:
    """LLMRequest 测试"""
    
    def test_basic_request(self):
        """测试基本请求创建"""
        request = LLMRequest(prompt="Hello")
        
        assert request.prompt == "Hello"
        assert request.max_tokens == 1000
        assert request.temperature == 0.7
        assert request.timeout == 30.0
    
    def test_request_with_all_fields(self):
        """测试完整字段请求"""
        request = LLMRequest(
            prompt="Test prompt",
            system_prompt="System prompt",
            model="gpt-4o",
            max_tokens=500,
            temperature=0.5,
            top_p=0.9,
            timeout=60.0,
            stream=True,
            response_format="json",
            user_id="user_123",
            request_id="req_abc",
            metadata={"key": "value"},
        )
        
        assert request.prompt == "Test prompt"
        assert request.system_prompt == "System prompt"
        assert request.model == "gpt-4o"
        assert request.stream is True
        assert request.response_format == "json"
    
    def test_request_validation(self):
        """测试请求验证"""
        # max_tokens 范围
        with pytest.raises(ValueError):
            LLMRequest(prompt="Test", max_tokens=0)
        
        with pytest.raises(ValueError):
            LLMRequest(prompt="Test", max_tokens=20000)
        
        # temperature 范围
        with pytest.raises(ValueError):
            LLMRequest(prompt="Test", temperature=-0.1)


class TestLLMResponse:
    """LLMResponse 测试"""
    
    def test_basic_response(self):
        """测试基本响应"""
        response = LLMResponse(
            content="Hello, world!",
            model_used="gpt-4o-mini",
            provider_used="openai",
        )
        
        assert response.content == "Hello, world!"
        assert response.model_used == "gpt-4o-mini"
        assert response.is_fallback is False
    
    def test_response_with_usage(self):
        """测试带用量的响应"""
        usage = LLMUsage(
            prompt_tokens=100,
            completion_tokens=50,
            total_tokens=150,
        )
        
        response = LLMResponse(
            content="Response",
            usage=usage,
            model_used="gpt-4o",
            provider_used="openai",
            latency_ms=1234.5,
        )
        
        assert response.usage.total_tokens == 150
        assert response.latency_ms == 1234.5


class TestLLMUsage:
    """LLMUsage 测试"""
    
    def test_usage_creation(self):
        """测试用量创建"""
        usage = LLMUsage(
            prompt_tokens=100,
            completion_tokens=200,
            total_tokens=300,
        )
        
        assert usage.prompt_tokens == 100
        assert usage.completion_tokens == 200
        assert usage.total_tokens == 300
    
    def test_estimated_cost(self):
        """测试成本估算"""
        usage = LLMUsage(
            prompt_tokens=1000,
            completion_tokens=1000,
            total_tokens=2000,
        )
        
        cost = usage.estimated_cost
        # GPT-4o: $2.50/1M input, $10.00/1M output
        expected = 1000 * 2.50 / 1_000_000 + 1000 * 10.00 / 1_000_000
        assert abs(cost - expected) < 0.0001


class TestLLMUsageRecord:
    """LLMUsageRecord 测试"""
    
    def test_record_creation(self):
        """测试记录创建"""
        record = LLMUsageRecord(
            record_id="rec_123",
            request_id="req_456",
            model="gpt-4o-mini",
            provider="openai",
            tokens_in=100,
            tokens_out=50,
            cost_usd=0.001,
        )
        
        assert record.record_id == "rec_123"
        assert record.success is True
        assert isinstance(record.timestamp, datetime)
    
    def test_record_with_error(self):
        """测试错误记录"""
        record = LLMUsageRecord(
            record_id="rec_err",
            request_id="req_err",
            model="gpt-4o",
            provider="openai",
            success=False,
            error_type="RateLimitError",
        )
        
        assert record.success is False
        assert record.error_type == "RateLimitError"


class TestModelConfig:
    """ModelConfig 测试"""
    
    def test_config_creation(self, sample_model_config):
        """测试配置创建"""
        config = sample_model_config
        
        assert config.provider == "openai"
        assert config.model_id == "gpt-4o-mini"
        assert ModelCapability.FAST in config.capabilities
        assert config.enabled is True
    
    def test_config_immutable(self, sample_model_config):
        """测试配置不可变"""
        with pytest.raises(Exception):  # frozen=True
            sample_model_config.model_id = "changed"
