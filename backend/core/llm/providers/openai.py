"""
OpenAI Provider

使用 httpx 直接调用 OpenAI API，避免 SDK 锁定。

对照 pitfalls.md 1.1: Provider SDK 锁定
"""

import json
import logging
import os
import time
from typing import AsyncIterator, Optional

import httpx

from backend.core.llm.models import LLMRequest, LLMResponse, LLMUsage
from backend.core.llm.providers.base import (
    LLMProvider,
    LLMProviderError,
    RateLimitError,
    AuthenticationError,
    InvalidRequestError,
    ModelNotFoundError,
    ContextLengthExceededError,
)

logger = logging.getLogger(__name__)


class OpenAIProvider(LLMProvider):
    """
    OpenAI Provider
    
    使用 httpx 直接调用 API，不依赖 openai SDK。
    支持 gpt-4o, gpt-4o-mini 等模型。
    """
    
    BASE_URL = "https://api.openai.com/v1"
    
    SUPPORTED_MODELS = [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-4",
        "gpt-3.5-turbo",
    ]
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        default_model: str = "gpt-4o-mini",
    ):
        """
        初始化 OpenAI Provider
        
        Args:
            api_key: API 密钥，默认从环境变量 OPENAI_API_KEY 获取
            base_url: API 基础 URL，默认从 OPENAI_BASE_URL 获取或使用官方 URL
            default_model: 默认模型
        """
        self._api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self._api_key:
            raise AuthenticationError("OPENAI_API_KEY not set")
        
        # 支持从环境变量读取 base_url (灵芽中转站等)
        self._base_url = base_url or os.getenv("OPENAI_BASE_URL") or self.BASE_URL
        self._default_model = default_model
        
        # 日志记录使用的 base_url
        if self._base_url != self.BASE_URL:
            logger.info(f"Using custom base_url: {self._base_url}")
    
    @property
    def name(self) -> str:
        return "openai"
    
    @property
    def supported_models(self) -> list[str]:
        return self.SUPPORTED_MODELS
    
    async def complete(self, request: LLMRequest) -> LLMResponse:
        """
        完成请求
        
        使用 httpx 直接调用 OpenAI Chat Completions API。
        """
        start_time = time.perf_counter()
        
        model = request.model or self._default_model
        
        # 构建请求体
        payload = self._build_payload(request, model)
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self._base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload,
                    timeout=request.timeout,
                )
                
                latency_ms = (time.perf_counter() - start_time) * 1000
                
                if response.status_code == 200:
                    return self._parse_response(
                        response.json(),
                        model,
                        latency_ms,
                        request.request_id,
                    )
                else:
                    self._handle_error(response)
        
        except httpx.TimeoutException:
            raise LLMProviderError(f"Request timeout after {request.timeout}s")
        except httpx.RequestError as e:
            raise LLMProviderError(f"Request failed: {e}")
    
    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        """
        流式响应
        
        使用 SSE (Server-Sent Events) 接收流式数据。
        """
        model = request.model or self._default_model
        
        payload = self._build_payload(request, model)
        payload["stream"] = True
        
        try:
            async with httpx.AsyncClient() as client:
                async with client.stream(
                    "POST",
                    f"{self._base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload,
                    timeout=request.timeout,
                ) as response:
                    if response.status_code != 200:
                        error_body = await response.aread()
                        self._handle_error_body(response.status_code, error_body)
                    
                    async for line in response.aiter_lines():
                        if line.startswith("data: "):
                            data = line[6:]
                            if data == "[DONE]":
                                break
                            try:
                                chunk = json.loads(data)
                                delta = chunk.get("choices", [{}])[0].get("delta", {})
                                content = delta.get("content", "")
                                if content:
                                    yield content
                            except json.JSONDecodeError:
                                continue
        
        except httpx.TimeoutException:
            raise LLMProviderError(f"Stream timeout after {request.timeout}s")
        except httpx.RequestError as e:
            raise LLMProviderError(f"Stream failed: {e}")
    
    def _get_headers(self) -> dict:
        """获取请求头"""
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
    
    def _build_payload(self, request: LLMRequest, model: str) -> dict:
        """构建请求体"""
        messages = []
        
        if request.system_prompt:
            messages.append({
                "role": "system",
                "content": request.system_prompt,
            })
        
        messages.append({
            "role": "user",
            "content": request.prompt,
        })
        
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "top_p": request.top_p,
        }
        
        if request.response_format == "json":
            payload["response_format"] = {"type": "json_object"}
        
        return payload
    
    def _parse_response(
        self,
        data: dict,
        model: str,
        latency_ms: float,
        request_id: Optional[str],
    ) -> LLMResponse:
        """解析响应"""
        choice = data.get("choices", [{}])[0]
        message = choice.get("message", {})
        usage_data = data.get("usage", {})
        
        usage = LLMUsage(
            prompt_tokens=usage_data.get("prompt_tokens", 0),
            completion_tokens=usage_data.get("completion_tokens", 0),
            total_tokens=usage_data.get("total_tokens", 0),
        )
        
        return LLMResponse(
            content=message.get("content", ""),
            usage=usage,
            model_used=data.get("model", model),
            provider_used=self.name,
            latency_ms=latency_ms,
            finish_reason=choice.get("finish_reason"),
            request_id=request_id,
        )
    
    def _handle_error(self, response: httpx.Response) -> None:
        """处理错误响应"""
        self._handle_error_body(response.status_code, response.content)
    
    def _handle_error_body(self, status_code: int, body: bytes) -> None:
        """处理错误响应体"""
        try:
            error_data = json.loads(body)
            error_msg = error_data.get("error", {}).get("message", "Unknown error")
            error_type = error_data.get("error", {}).get("type", "")
        except json.JSONDecodeError:
            error_msg = body.decode("utf-8", errors="replace")
            error_type = ""
        
        if status_code == 401:
            raise AuthenticationError(f"Authentication failed: {error_msg}")
        elif status_code == 429:
            raise RateLimitError(f"Rate limit exceeded: {error_msg}")
        elif status_code == 400:
            if "context_length" in error_msg.lower():
                raise ContextLengthExceededError(error_msg)
            raise InvalidRequestError(f"Invalid request: {error_msg}")
        elif status_code == 404:
            raise ModelNotFoundError(f"Model not found: {error_msg}")
        else:
            raise LLMProviderError(f"OpenAI error ({status_code}): {error_msg}")
