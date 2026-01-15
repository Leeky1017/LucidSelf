"""
Cascade Router

级联路由器，按成本/延迟/能力选择模型，支持 fallback。

对照 pitfalls.md 1.3: Fallback 无限循环
关键: 设置 max_retries，明确失败
"""

import asyncio
import logging
from typing import Dict, List, Optional

from backend.core.llm.models import LLMRequest, LLMResponse, ModelCapability, ModelConfig
from backend.core.llm.providers.base import (
    LLMProvider,
    LLMProviderError,
    RateLimitError,
)

logger = logging.getLogger(__name__)


class AllProvidersFailedError(Exception):
    """所有 Provider 都失败"""
    def __init__(self, message: str, attempts: int):
        super().__init__(message)
        self.attempts = attempts


class CascadeRouter:
    """
    级联路由器
    
    功能:
    - 按能力/成本/延迟选择模型
    - 支持 fallback 链
    - 指数退避重试
    - 明确的失败处理
    
    对照 requirements.md 1.2.1-1.2.4
    """
    
    MAX_RETRIES = 3
    BASE_RETRY_DELAY = 1.0  # 秒
    
    def __init__(self, providers: Optional[Dict[str, LLMProvider]] = None):
        """
        初始化路由器
        
        Args:
            providers: Provider 字典，key 为 provider name
        """
        self._providers: Dict[str, LLMProvider] = providers or {}
        self._model_configs: Dict[str, ModelConfig] = {}
        self._fallback_chains: Dict[str, List[str]] = {}
        
        # 默认 fallback 链
        self._default_fallback_chain = [
            "gpt-4o-mini",
            "gpt-3.5-turbo",
        ]
    
    def register_provider(self, provider: LLMProvider) -> None:
        """注册 Provider"""
        self._providers[provider.name] = provider
        logger.info(f"Registered provider: {provider.name}")
    
    def register_model(self, config: ModelConfig) -> None:
        """注册模型配置"""
        self._model_configs[config.model_id] = config
        logger.info(f"Registered model: {config.model_id} ({config.provider})")
    
    def set_fallback_chain(self, model: str, fallbacks: List[str]) -> None:
        """设置 fallback 链"""
        self._fallback_chains[model] = fallbacks
    
    def select(
        self,
        model_hint: Optional[str] = None,
        capability: Optional[ModelCapability] = None,
        prefer_low_cost: bool = False,
        prefer_low_latency: bool = False,
    ) -> tuple[LLMProvider, str]:
        """
        选择最优模型
        
        Args:
            model_hint: 模型提示
            capability: 需要的能力
            prefer_low_cost: 优先低成本
            prefer_low_latency: 优先低延迟
            
        Returns:
            (Provider, model_id) 元组
        """
        # 如果指定了模型，直接返回
        if model_hint:
            provider = self._get_provider_for_model(model_hint)
            if provider:
                return provider, model_hint
        
        # 根据条件筛选
        candidates = list(self._model_configs.values())
        
        if capability:
            candidates = [c for c in candidates if capability in c.capabilities]
        
        candidates = [c for c in candidates if c.enabled]
        
        if not candidates:
            # 回退到默认
            return self._get_default_provider()
        
        # 排序
        if prefer_low_cost:
            candidates.sort(key=lambda c: c.cost_per_1k_input_tokens)
        elif prefer_low_latency:
            candidates.sort(key=lambda c: c.avg_latency_ms)
        else:
            candidates.sort(key=lambda c: c.priority)
        
        best = candidates[0]
        provider = self._providers.get(best.provider)
        if provider:
            return provider, best.model_id
        
        return self._get_default_provider()
    
    async def complete_with_fallback(
        self,
        request: LLMRequest,
        attempt: int = 0,
    ) -> LLMResponse:
        """
        带 fallback 的请求
        
        按 fallback 链尝试，指数退避重试。
        
        Args:
            request: LLM 请求
            attempt: 当前重试次数
            
        Returns:
            LLM 响应
            
        Raises:
            AllProvidersFailedError: 所有 Provider 都失败
        """
        if attempt >= self.MAX_RETRIES:
            raise AllProvidersFailedError(
                f"All providers failed after {self.MAX_RETRIES} attempts",
                attempts=self.MAX_RETRIES,
            )
        
        # 获取 fallback 链
        model = request.model or "gpt-4o-mini"
        fallback_chain = self._fallback_chains.get(model, self._default_fallback_chain)
        
        # 确保主模型在链首
        if model not in fallback_chain:
            fallback_chain = [model] + fallback_chain
        
        errors = []
        
        for fallback_model in fallback_chain:
            provider = self._get_provider_for_model(fallback_model)
            if not provider:
                continue
            
            try:
                # 修改请求使用当前模型
                current_request = LLMRequest(
                    **{
                        **request.model_dump(),
                        "model": fallback_model,
                    }
                )
                
                response = await provider.complete(current_request)
                
                # 标记是否为 fallback
                if fallback_model != model:
                    response = LLMResponse(
                        **{
                            **response.model_dump(),
                            "is_fallback": True,
                        }
                    )
                
                return response
            
            except RateLimitError as e:
                logger.warning(f"Rate limit for {fallback_model}: {e}")
                errors.append((fallback_model, e))
                # 等待后重试
                await asyncio.sleep(self.BASE_RETRY_DELAY * (2 ** attempt))
                continue
            
            except LLMProviderError as e:
                logger.warning(f"Provider error for {fallback_model}: {e}")
                errors.append((fallback_model, e))
                continue
        
        # 所有模型都失败，重试
        logger.warning(f"All models failed on attempt {attempt + 1}, retrying...")
        return await self.complete_with_fallback(request, attempt + 1)
    
    def get_provider(self, name: str) -> Optional[LLMProvider]:
        """获取指定 Provider"""
        return self._providers.get(name)
    
    def list_providers(self) -> List[str]:
        """列出所有 Provider"""
        return list(self._providers.keys())
    
    def list_models(self) -> List[str]:
        """列出所有模型"""
        return list(self._model_configs.keys())
    
    def _get_provider_for_model(self, model: str) -> Optional[LLMProvider]:
        """获取模型对应的 Provider"""
        # 先查配置
        config = self._model_configs.get(model)
        if config:
            return self._providers.get(config.provider)
        
        # 按模型名称前缀推断
        if model.startswith("gpt-"):
            return self._providers.get("openai")
        elif model.startswith("claude-"):
            return self._providers.get("anthropic")
        
        # 查找支持该模型的 Provider
        for provider in self._providers.values():
            if provider.supports_model(model):
                return provider
        
        return None
    
    def _get_default_provider(self) -> tuple[LLMProvider, str]:
        """获取默认 Provider 和模型"""
        # 优先 OpenAI
        if "openai" in self._providers:
            return self._providers["openai"], "gpt-4o-mini"
        
        # 返回第一个可用的
        for name, provider in self._providers.items():
            if provider.supported_models:
                return provider, provider.supported_models[0]
        
        raise LLMProviderError("No available LLM provider")
