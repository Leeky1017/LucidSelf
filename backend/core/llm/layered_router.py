"""
Layered LLM Router

分层 LLM 路由器，实现成本优化的多模型架构。

设计原则:
- Layer A (解析层): gemini-2.5-flash 做解析/拆解/分类
- Layer B (生成层): doubao/grok/gemini 做内容生成
  - B_CN: 中文命理/梦境解读
  - B_EN: 英文占星/塔罗解读
  - B_COMPLEX: 复杂推理/跨文化分析

对照文档: docs/ls_roadmap_executable.md
"""

import logging
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, Tuple

from backend.core.llm.providers.base import LLMProvider
from backend.core.llm.providers.openai import OpenAIProvider

logger = logging.getLogger(__name__)


class LLMLayer(str, Enum):
    """LLM 调用层级"""
    LAYER_A = "layer_a"  # 解析层 - gemini-flash
    LAYER_B_CN = "layer_b_cn"  # 生成层 - 中文 (doubao)
    LAYER_B_EN = "layer_b_en"  # 生成层 - 英文 (gemini/grok)
    LAYER_B_COMPLEX = "layer_b_complex"  # 生成层 - 复杂推理 (grok)


@dataclass
class LayerConfig:
    """层级配置"""
    primary_model: str
    fallback_model: str
    description: str
    max_tokens: int = 1000
    temperature: float = 0.7
    
    # 成本估算 (元/M tokens)
    estimated_cost_per_m: float = 5.0


@dataclass
class LayeredRouterConfig:
    """分层路由配置"""
    api_key: str
    base_url: str = "https://api.lingyaai.cn/v1"
    
    layers: Dict[LLMLayer, LayerConfig] = field(default_factory=dict)
    
    @classmethod
    def from_env(cls) -> "LayeredRouterConfig":
        """从环境变量加载配置"""
        api_key = os.getenv("OPENAI_API_KEY", "")
        base_url = os.getenv("OPENAI_BASE_URL", "https://api.lingyaai.cn/v1")
        
        layers = {
            # A层: 解析层 - 使用 gemini-flash
            LLMLayer.LAYER_A: LayerConfig(
                primary_model=os.getenv("LLM_LAYER_A_MODEL", "gemini-2.5-flash"),
                fallback_model=os.getenv("LLM_LAYER_A_FALLBACK", "gemini-2.5-flash"),
                description="解析层 - 解析/拆解/分类",
                max_tokens=500,
                temperature=0.3,
                estimated_cost_per_m=1.7,
            ),
            # B层-中文: 生成层 - 使用 doubao
            LLMLayer.LAYER_B_CN: LayerConfig(
                primary_model=os.getenv("LLM_LAYER_B_CN_MODEL", "doubao-seed-1.6-thinking"),
                fallback_model=os.getenv("LLM_LAYER_B_CN_FALLBACK", "gemini-2.5-flash"),
                description="生成层(中文) - 命理/梦境解读",
                max_tokens=1500,
                temperature=0.7,
                estimated_cost_per_m=6.2,
            ),
            # B层-英文: 生成层 - 使用 gemini/grok
            LLMLayer.LAYER_B_EN: LayerConfig(
                primary_model=os.getenv("LLM_LAYER_B_EN_MODEL", "gemini-2.5-flash"),
                fallback_model=os.getenv("LLM_LAYER_B_EN_FALLBACK", "grok-4-fast-reasoning"),
                description="生成层(英文) - 占星/塔罗解读",
                max_tokens=1500,
                temperature=0.7,
                estimated_cost_per_m=6.5,
            ),
            # B层-复杂: 生成层 - 使用 grok
            LLMLayer.LAYER_B_COMPLEX: LayerConfig(
                primary_model=os.getenv("LLM_LAYER_B_COMPLEX_MODEL", "grok-4-fast-reasoning"),
                fallback_model=os.getenv("LLM_LAYER_B_COMPLEX_FALLBACK", "doubao-seed-1.6-thinking"),
                description="生成层(复杂) - 跨文化分析/深度解读",
                max_tokens=2000,
                temperature=0.5,
                estimated_cost_per_m=2.25,
            ),
        }
        
        return cls(api_key=api_key, base_url=base_url, layers=layers)


class LayeredLLMRouter:
    """
    分层 LLM 路由器
    
    实现成本优化的多模型架构:
    - A层 (gemini-flash): 解析用户输入，生成结构化数据
    - B层 (doubao/grok/gemini): 生成内容
      - B_CN: 中文命理解读
      - B_EN: 英文占星解读
      - B_COMPLEX: 复杂推理
    
    使用方式:
        router = LayeredLLMRouter.create_default()
        provider, model = router.select(LLMLayer.LAYER_B_CN)
        response = await provider.complete(request)
    """
    
    def __init__(self, config: LayeredRouterConfig):
        """初始化路由器"""
        self._config = config
        self._provider: Optional[OpenAIProvider] = None
        self._stats: Dict[LLMLayer, Dict[str, int]] = {
            layer: {"calls": 0, "tokens": 0, "fallbacks": 0}
            for layer in LLMLayer
        }
        
        # 初始化 Provider
        self._init_provider()
    
    def _init_provider(self) -> None:
        """初始化 LLM Provider"""
        if not self._config.api_key:
            logger.warning("No API key configured, LLM features will be disabled")
            return
        
        try:
            self._provider = OpenAIProvider(
                api_key=self._config.api_key,
                base_url=self._config.base_url,
            )
            logger.info(f"Initialized LayeredLLMRouter with base_url: {self._config.base_url}")
        except Exception as e:
            logger.error(f"Failed to initialize LLM provider: {e}")
    
    @property
    def is_available(self) -> bool:
        """检查路由器是否可用"""
        return self._provider is not None
    
    def select(
        self, 
        layer: LLMLayer,
        use_fallback: bool = False,
    ) -> Tuple[Optional[LLMProvider], str]:
        """
        选择指定层级的 Provider 和模型
        
        Args:
            layer: 目标层级
            use_fallback: 是否使用备选模型
            
        Returns:
            (provider, model_name) 元组
        """
        if not self._provider:
            return None, ""
        
        layer_config = self._config.layers.get(layer)
        if not layer_config:
            logger.warning(f"Layer {layer} not configured")
            return None, ""
        
        model = layer_config.fallback_model if use_fallback else layer_config.primary_model
        
        # 更新统计
        self._stats[layer]["calls"] += 1
        if use_fallback:
            self._stats[layer]["fallbacks"] += 1
        
        return self._provider, model
    
    def select_for_language(self, language: str = "zh") -> Tuple[Optional[LLMProvider], str]:
        """
        根据语言选择生成层模型
        
        Args:
            language: 目标语言 ("zh" 或 "en")
            
        Returns:
            (provider, model_name) 元组
        """
        layer = LLMLayer.LAYER_B_CN if language == "zh" else LLMLayer.LAYER_B_EN
        return self.select(layer)
    
    def get_layer_config(self, layer: LLMLayer) -> Optional[LayerConfig]:
        """获取层级配置"""
        return self._config.layers.get(layer)
    
    def get_stats(self) -> Dict[str, Dict[str, int]]:
        """获取调用统计"""
        return {layer.value: stats for layer, stats in self._stats.items()}
    
    def record_tokens(self, layer: LLMLayer, tokens: int) -> None:
        """记录 token 使用量"""
        self._stats[layer]["tokens"] += tokens
    
    def estimate_cost(self) -> float:
        """估算总成本 (元)"""
        total = 0.0
        for layer, stats in self._stats.items():
            config = self._config.layers.get(layer)
            if config:
                total += (stats["tokens"] / 1_000_000) * config.estimated_cost_per_m
        return total
    
    @classmethod
    def create_default(cls) -> "LayeredLLMRouter":
        """创建默认配置的路由器"""
        config = LayeredRouterConfig.from_env()
        return cls(config)


# =============================================================================
# 便捷函数
# =============================================================================

_default_router: Optional[LayeredLLMRouter] = None


def get_layered_router() -> LayeredLLMRouter:
    """获取默认分层路由器 (单例)"""
    global _default_router
    if _default_router is None:
        _default_router = LayeredLLMRouter.create_default()
    return _default_router


def reset_layered_router() -> None:
    """重置分层路由器 (用于测试)"""
    global _default_router
    _default_router = None


def select_layer(
    layer: LLMLayer,
    use_fallback: bool = False,
) -> Tuple[Optional[LLMProvider], str]:
    """
    便捷函数: 选择指定层级的模型
    
    Args:
        layer: 目标层级
        use_fallback: 是否使用备选模型
        
        
    Returns:
        (provider, model_name) 元组
        
    Example:
        provider, model = select_layer(LLMLayer.LAYER_A)
        if provider:
            response = await provider.complete(request)
    """
    router = get_layered_router()
    return router.select(layer, use_fallback)


def select_for_language(language: str = "zh") -> Tuple[Optional[LLMProvider], str]:
    """
    便捷函数: 根据语言选择生成层模型
    
    Args:
        language: 目标语言 ("zh" 或 "en")
        
    Returns:
        (provider, model_name) 元组
    """
    router = get_layered_router()
    return router.select_for_language(language)
