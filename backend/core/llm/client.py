"""
LLM Client

统一 LLM 客户端，整合路由、成本监控、安全检查。

对照 requirements.md 1.1.1-1.1.5
"""

import asyncio
import logging
import uuid
from typing import AsyncIterator, Callable, Optional

from backend.core.llm.models import LLMRequest, LLMResponse, LLMUsage
from backend.core.llm.router import CascadeRouter, AllProvidersFailedError
from backend.core.llm.cost_monitor import CostMonitor, CostLimitExceededError
from backend.core.llm.providers.base import LLMProvider, LLMProviderError

logger = logging.getLogger(__name__)


class LLMClient:
    """
    统一 LLM 客户端
    
    功能:
    - 整合 CascadeRouter 和 CostMonitor
    - 请求前成本检查
    - 请求后用量记录
    - 可选的安全检查钩子
    - 重试和超时处理
    
    对照 requirements.md 1.1.1-1.1.5
    """
    
    def __init__(
        self,
        router: Optional[CascadeRouter] = None,
        cost_monitor: Optional[CostMonitor] = None,
        input_filter: Optional[Callable[[str], str]] = None,
        output_filter: Optional[Callable[[str], str]] = None,
    ):
        """
        初始化 LLM 客户端
        
        Args:
            router: 级联路由器
            cost_monitor: 成本监控器
            input_filter: 输入过滤器 (安全检查)
            output_filter: 输出过滤器 (安全检查)
        """
        self.router = router or CascadeRouter()
        self.cost_monitor = cost_monitor or CostMonitor()
        self.input_filter = input_filter
        self.output_filter = output_filter
    
    async def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        model: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        timeout: float = 30.0,
        user_id: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> LLMResponse:
        """
        完成请求
        
        包含完整的成本检查、请求、记录流程。
        
        Args:
            prompt: 用户 prompt
            system_prompt: 系统 prompt
            model: 指定模型
            max_tokens: 最大输出 token
            temperature: 温度参数
            timeout: 超时时间
            user_id: 用户 ID
            metadata: 额外元数据
            
        Returns:
            LLM 响应
            
        Raises:
            CostLimitExceededError: 成本超限
            AllProvidersFailedError: 所有 Provider 失败
            LLMProviderError: Provider 错误
        """
        request_id = f"req_{uuid.uuid4().hex[:12]}"
        
        # 1. 输入过滤
        if self.input_filter:
            prompt = self.input_filter(prompt)
            if system_prompt:
                system_prompt = self.input_filter(system_prompt)
        
        # 2. 预估 token 和成本检查
        estimated_input = self._estimate_tokens(prompt)
        if system_prompt:
            estimated_input += self._estimate_tokens(system_prompt)
        
        self.cost_monitor.check_before_request(
            user_id=user_id,
            estimated_input_tokens=estimated_input,
            estimated_output_tokens=max_tokens,
            model=model or "gpt-4o-mini",
        )
        
        # 3. 选择模型
        provider, selected_model = self.router.select(model_hint=model)
        
        # 4. 构建请求
        request = LLMRequest(
            prompt=prompt,
            system_prompt=system_prompt,
            model=selected_model,
            max_tokens=max_tokens,
            temperature=temperature,
            timeout=timeout,
            user_id=user_id,
            request_id=request_id,
            metadata=metadata or {},
        )
        
        # 5. 执行请求
        try:
            response = await provider.complete(request)
            
            # 6. 输出过滤
            if self.output_filter:
                filtered_content = self.output_filter(response.content)
                if filtered_content != response.content:
                    response = LLMResponse(
                        **{
                            **response.model_dump(),
                            "content": filtered_content,
                        }
                    )
            
            # 7. 记录用量
            self.cost_monitor.record(
                usage=response.usage,
                model=response.model_used,
                provider=response.provider_used,
                user_id=user_id,
                request_id=request_id,
                latency_ms=response.latency_ms,
                success=True,
            )
            
            return response
        
        except (AllProvidersFailedError, LLMProviderError) as e:
            # 记录失败
            self.cost_monitor.record(
                usage=LLMUsage(),
                model=model or "unknown",
                provider="unknown",
                user_id=user_id,
                request_id=request_id,
                success=False,
                error_type=type(e).__name__,
            )
            raise
    
    async def stream(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        model: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        timeout: float = 60.0,
        user_id: Optional[str] = None,
    ) -> AsyncIterator[str]:
        """
        流式响应
        
        Args:
            prompt: 用户 prompt
            system_prompt: 系统 prompt
            model: 指定模型
            max_tokens: 最大输出 token
            temperature: 温度参数
            timeout: 超时时间
            user_id: 用户 ID
            
        Yields:
            响应文本片段
        """
        # 1. 输入过滤
        if self.input_filter:
            prompt = self.input_filter(prompt)
            if system_prompt:
                system_prompt = self.input_filter(system_prompt)
        
        # 2. 成本检查
        estimated_input = self._estimate_tokens(prompt)
        if system_prompt:
            estimated_input += self._estimate_tokens(system_prompt)
        
        self.cost_monitor.check_before_request(
            user_id=user_id,
            estimated_input_tokens=estimated_input,
            estimated_output_tokens=max_tokens,
            model=model or "gpt-4o-mini",
        )
        
        # 3. 构建请求
        request = LLMRequest(
            prompt=prompt,
            system_prompt=system_prompt,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            timeout=timeout,
            stream=True,
            user_id=user_id,
        )
        
        # 4. 选择 Provider
        provider, selected_model = self.router.select(model_hint=model)
        request = LLMRequest(**{**request.model_dump(), "model": selected_model})
        
        # 5. 流式响应
        accumulated_content = []
        async for chunk in provider.stream(request):
            if self.output_filter:
                chunk = self.output_filter(chunk)
            accumulated_content.append(chunk)
            yield chunk
        
        # 6. 记录用量 (估算)
        total_content = "".join(accumulated_content)
        estimated_output = self._estimate_tokens(total_content)
        
        self.cost_monitor.record(
            usage=LLMUsage(
                prompt_tokens=estimated_input,
                completion_tokens=estimated_output,
                total_tokens=estimated_input + estimated_output,
            ),
            model=selected_model,
            provider=provider.name,
            user_id=user_id,
            success=True,
        )
    
    def _estimate_tokens(self, text: str) -> int:
        """
        估算 token 数
        
        简单估算：中文约 2 字符/token，英文约 4 字符/token
        """
        if not text:
            return 0
        
        # 统计中文字符
        chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        other_chars = len(text) - chinese_chars
        
        # 估算
        return (chinese_chars // 2) + (other_chars // 4) + 1
    
    async def complete_json(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        response_schema: Optional[type] = None,
        model: Optional[str] = None,
        max_tokens: int = 2000,
        temperature: float = 0.3,
        timeout: float = 30.0,
        user_id: Optional[str] = None,
    ) -> dict:
        """
        JSON 格式响应的完成请求
        
        专为需要结构化 JSON 输出的场景设计，自动设置 response_format。
        
        Args:
            prompt: 用户 prompt
            system_prompt: 系统 prompt
            response_schema: 可选的 Pydantic 模型，用于验证响应
            model: 指定模型
            max_tokens: 最大输出 token
            temperature: 温度参数（默认较低以保证结构稳定）
            timeout: 超时时间
            user_id: 用户 ID
            
        Returns:
            解析后的 JSON 字典
            
        Raises:
            ValueError: JSON 解析失败或 schema 验证失败
        """
        import json
        
        # 调用普通 complete
        response = await self.complete(
            prompt=prompt,
            system_prompt=system_prompt,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            timeout=timeout,
            user_id=user_id,
            metadata={"response_format": "json"},
        )
        
        # 解析 JSON
        try:
            result = json.loads(response.content)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            raise ValueError(f"Invalid JSON response: {e}")
        
        # 可选的 schema 验证
        if response_schema is not None:
            try:
                validated = response_schema.model_validate(result)
                return validated.model_dump()
            except Exception as e:
                logger.error(f"Schema validation failed: {e}")
                raise ValueError(f"Schema validation failed: {e}")
        
        return result
    
    @classmethod
    def create_default(cls) -> "LLMClient":
        """
        创建默认配置的客户端
        
        使用环境变量配置。
        """
        from backend.core.llm.providers.openai import OpenAIProvider
        
        router = CascadeRouter()
        
        # 注册 OpenAI Provider
        try:
            openai_provider = OpenAIProvider()
            router.register_provider(openai_provider)
        except Exception as e:
            logger.warning(f"Failed to register OpenAI provider: {e}")
        
        cost_monitor = CostMonitor()
        
        return cls(router=router, cost_monitor=cost_monitor)
