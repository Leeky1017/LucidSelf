"""
LLM Providers

Provider 实现模块，提供多种 LLM Provider 的统一封装。

设计原则:
- 不直接依赖 SDK，使用 httpx 调用 API
- 统一接口，便于切换和 fallback
"""

from backend.core.llm.providers.base import LLMProvider
from backend.core.llm.providers.openai import OpenAIProvider

__all__ = [
    "LLMProvider",
    "OpenAIProvider",
]
