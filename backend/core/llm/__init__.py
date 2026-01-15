"""
LLM Core Module

LLM 集成核心模块，提供统一的 LLM 调用接口。

组件:
- LLMClient: 统一客户端
- CascadeRouter: 级联路由器
- LayeredLLMRouter: 分层路由器 (成本优化)
- CostMonitor: 成本监控
- TOONSerializer: TOON 序列化器
"""

from backend.core.llm.models import (
    LLMRequest,
    LLMResponse,
    LLMUsageRecord,
    ModelCapability,
    ModelConfig,
)
from backend.core.llm.client import LLMClient
from backend.core.llm.router import CascadeRouter
from backend.core.llm.cost_monitor import CostMonitor
from backend.core.llm.toon_serializer import TOONSerializer
from backend.core.llm.layered_router import (
    LayeredLLMRouter,
    LLMLayer,
    LayerConfig,
    get_layered_router,
    reset_layered_router,
    select_layer,
    select_for_language,
)
from backend.core.llm.orchestrator import (
    LLMOrchestrator,
    ScenarioType,
    get_orchestrator,
)

__all__ = [
    # Models
    "LLMRequest",
    "LLMResponse",
    "LLMUsageRecord",
    "ModelCapability",
    "ModelConfig",
    # Core
    "LLMClient",
    "CascadeRouter",
    "CostMonitor",
    "TOONSerializer",
    # Layered Router
    "LayeredLLMRouter",
    "LLMLayer",
    "LayerConfig",
    "get_layered_router",
    "reset_layered_router",
    "select_layer",
    "select_for_language",
    # Orchestrator
    "LLMOrchestrator",
    "ScenarioType",
    "get_orchestrator",
]

