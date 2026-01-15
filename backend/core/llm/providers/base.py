"""
LLM Provider Base Class

LLM Provider 抽象基类，定义统一接口。

设计原则:
- 不直接依赖任何 SDK
- 使用 httpx 进行 HTTP 调用
- 支持同步和异步调用
- 支持流式响应
"""

from abc import ABC, abstractmethod
from typing import AsyncIterator, Optional

from backend.core.llm.models import LLMRequest, LLMResponse


class LLMProviderError(Exception):
    """LLM Provider 错误基类"""
    pass


class RateLimitError(LLMProviderError):
    """速率限制错误"""
    def __init__(self, message: str, retry_after: Optional[float] = None):
        super().__init__(message)
        self.retry_after = retry_after


class AuthenticationError(LLMProviderError):
    """认证错误"""
    pass


class InvalidRequestError(LLMProviderError):
    """无效请求错误"""
    pass


class ModelNotFoundError(LLMProviderError):
    """模型不存在错误"""
    pass


class ContextLengthExceededError(LLMProviderError):
    """上下文长度超限错误"""
    pass


class LLMProvider(ABC):
    """
    LLM Provider 抽象基类
    
    所有 Provider 实现必须继承此类。
    避免 Provider 锁定，使用 httpx 直接调用 API。
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Provider 名称"""
        ...
    
    @property
    @abstractmethod
    def supported_models(self) -> list[str]:
        """支持的模型列表"""
        ...
    
    @abstractmethod
    async def complete(self, request: LLMRequest) -> LLMResponse:
        """
        完成请求
        
        Args:
            request: LLM 请求
            
        Returns:
            LLM 响应
            
        Raises:
            RateLimitError: 速率限制
            AuthenticationError: 认证失败
            InvalidRequestError: 无效请求
            LLMProviderError: 其他错误
        """
        ...
    
    @abstractmethod
    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        """
        流式响应
        
        Args:
            request: LLM 请求
            
        Yields:
            响应文本片段
            
        Raises:
            LLMProviderError: 错误
        """
        ...
    
    def supports_model(self, model: str) -> bool:
        """检查是否支持指定模型"""
        return model in self.supported_models
    
    async def health_check(self) -> bool:
        """
        健康检查
        
        Returns:
            True 如果 Provider 可用
        """
        try:
            # 发送最小请求测试
            test_request = LLMRequest(
                prompt="Hello",
                max_tokens=1,
                timeout=5.0,
            )
            response = await self.complete(test_request)
            return response.content is not None
        except Exception:
            return False
