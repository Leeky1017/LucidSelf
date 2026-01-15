"""
LLM Core Models

LLM 请求/响应/用量记录等数据契约。

对照 requirements.md 1.4.1-1.4.3
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class ModelCapability(str, Enum):
    """模型能力标签"""
    CODING = "coding"
    REASONING = "reasoning"
    CREATIVE = "creative"
    FAST = "fast"
    VISION = "vision"
    FUNCTION_CALLING = "function_calling"


class ModelConfig(BaseModel):
    """
    模型配置
    
    用于 CascadeRouter 选择模型。
    """
    provider: str = Field(..., description="Provider 名称 (openai, anthropic, local)")
    model_id: str = Field(..., description="模型 ID (gpt-4o, claude-3-sonnet, etc.)")
    capabilities: List[ModelCapability] = Field(
        default_factory=list,
        description="模型能力标签",
    )
    cost_per_1k_input_tokens: float = Field(
        default=0.0,
        description="每 1000 输入 token 成本 (USD)",
    )
    cost_per_1k_output_tokens: float = Field(
        default=0.0,
        description="每 1000 输出 token 成本 (USD)",
    )
    avg_latency_ms: float = Field(
        default=1000.0,
        description="平均延迟 (ms)",
    )
    max_context_tokens: int = Field(
        default=4096,
        description="最大上下文窗口",
    )
    priority: int = Field(
        default=1,
        description="优先级 (1=主选, 2=备选, etc.)",
    )
    enabled: bool = Field(default=True, description="是否启用")
    
    model_config = ConfigDict(frozen=True)


class LLMRequest(BaseModel):
    """
    LLM 请求
    
    对照 requirements.md 1.4.1
    """
    prompt: str = Field(..., description="用户 prompt")
    system_prompt: Optional[str] = Field(
        default=None,
        description="系统 prompt",
    )
    model: Optional[str] = Field(
        default=None,
        description="指定模型 (为空则由 router 选择)",
    )
    max_tokens: int = Field(
        default=1000,
        ge=1,
        le=16000,
        description="最大输出 token 数",
    )
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
        description="温度参数",
    )
    top_p: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Top-p 采样",
    )
    timeout: float = Field(
        default=30.0,
        ge=1.0,
        le=120.0,
        description="超时时间 (秒)",
    )
    stream: bool = Field(
        default=False,
        description="是否流式响应",
    )
    response_format: Optional[Literal["json", "text"]] = Field(
        default=None,
        description="响应格式",
    )
    user_id: Optional[str] = Field(
        default=None,
        description="用户 ID (用于成本追踪)",
    )
    request_id: Optional[str] = Field(
        default=None,
        description="请求 ID (用于追踪)",
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="额外元数据",
    )


class LLMUsage(BaseModel):
    """Token 用量"""
    prompt_tokens: int = Field(default=0, ge=0)
    completion_tokens: int = Field(default=0, ge=0)
    total_tokens: int = Field(default=0, ge=0)
    
    @property
    def estimated_cost(self) -> float:
        """估算成本 (基于 GPT-4o 价格)"""
        # GPT-4o: $2.50/1M input, $10.00/1M output
        input_cost = self.prompt_tokens * 2.50 / 1_000_000
        output_cost = self.completion_tokens * 10.00 / 1_000_000
        return input_cost + output_cost


class LLMResponse(BaseModel):
    """
    LLM 响应
    
    对照 requirements.md 1.4.2
    """
    content: str = Field(..., description="响应内容")
    usage: LLMUsage = Field(
        default_factory=LLMUsage,
        description="Token 用量",
    )
    model_used: str = Field(..., description="实际使用的模型")
    provider_used: str = Field(..., description="实际使用的 Provider")
    latency_ms: float = Field(
        default=0.0,
        ge=0.0,
        description="请求延迟 (ms)",
    )
    finish_reason: Optional[str] = Field(
        default=None,
        description="完成原因 (stop, length, etc.)",
    )
    request_id: Optional[str] = Field(
        default=None,
        description="请求 ID",
    )
    is_fallback: bool = Field(
        default=False,
        description="是否为 fallback 响应",
    )
    error: Optional[str] = Field(
        default=None,
        description="错误信息 (如有)",
    )


class LLMUsageRecord(BaseModel):
    """
    LLM 用量记录
    
    用于持久化和成本追踪。
    对照 requirements.md 1.4.3
    """
    record_id: str = Field(..., description="记录 ID")
    request_id: str = Field(..., description="关联请求 ID")
    user_id: Optional[str] = Field(default=None, description="用户 ID")
    model: str = Field(..., description="使用的模型")
    provider: str = Field(..., description="使用的 Provider")
    tokens_in: int = Field(default=0, ge=0, description="输入 token 数")
    tokens_out: int = Field(default=0, ge=0, description="输出 token 数")
    cost_usd: float = Field(default=0.0, ge=0.0, description="成本 (USD)")
    latency_ms: float = Field(default=0.0, ge=0.0, description="延迟 (ms)")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="记录时间",
    )
    success: bool = Field(default=True, description="是否成功")
    error_type: Optional[str] = Field(default=None, description="错误类型")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="额外元数据",
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "record_id": "rec_abc123",
                    "request_id": "req_xyz789",
                    "user_id": "user_001",
                    "model": "gpt-4o",
                    "provider": "openai",
                    "tokens_in": 150,
                    "tokens_out": 500,
                    "cost_usd": 0.0054,
                    "latency_ms": 1234.5,
                    "timestamp": "2025-12-06T12:00:00Z",
                    "success": True,
                }
            ]
        }
    )
