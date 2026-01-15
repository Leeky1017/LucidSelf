"""
Cost Monitor

LLM 成本监控模块，实现请求前检查和用量记录。

对照 pitfalls.md 1.2: 成本失控
关键: 请求前硬检查，不只是记录
"""

import logging
import os
import uuid
from collections import defaultdict
from datetime import datetime, timedelta
from threading import Lock
from typing import Callable, Dict, List, Optional

from backend.core.llm.models import LLMUsage, LLMUsageRecord, ModelConfig

logger = logging.getLogger(__name__)


class CostLimitExceededError(Exception):
    """成本限制超限错误"""
    def __init__(self, message: str, limit_type: str, current: float, limit: float):
        super().__init__(message)
        self.limit_type = limit_type
        self.current = current
        self.limit = limit


class CostMonitor:
    """
    成本监控器
    
    功能:
    - 请求前成本预估和硬限制检查
    - 实时用量统计
    - 每日/每月成本追踪
    - 分用户成本追踪
    - 告警回调
    
    对照 requirements.md 1.3.1-1.3.4
    """
    
    # 模型成本表 (USD per 1M tokens)
    MODEL_COSTS = {
        # GPT-4o
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        # GPT-4
        "gpt-4-turbo": {"input": 10.00, "output": 30.00},
        "gpt-4": {"input": 30.00, "output": 60.00},
        # GPT-3.5
        "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
        # Claude
        "claude-3-opus": {"input": 15.00, "output": 75.00},
        "claude-3-sonnet": {"input": 3.00, "output": 15.00},
        "claude-3-haiku": {"input": 0.25, "output": 1.25},
    }
    
    def __init__(
        self,
        daily_limit_usd: Optional[float] = None,
        monthly_limit_usd: Optional[float] = None,
        alert_threshold: float = 0.8,
        alert_callback: Optional[Callable[[str, float, float], None]] = None,
    ):
        """
        初始化成本监控器
        
        Args:
            daily_limit_usd: 每日成本上限 (USD)，默认从环境变量读取
            monthly_limit_usd: 每月成本上限 (USD)，默认从环境变量读取
            alert_threshold: 告警阈值 (0.0-1.0)，达到此比例时发送告警
            alert_callback: 告警回调函数 (message, current, limit)
        """
        self.daily_limit = daily_limit_usd or float(
            os.getenv("LLM_DAILY_LIMIT_USD", "10.0")
        )
        self.monthly_limit = monthly_limit_usd or float(
            os.getenv("LLM_MONTHLY_LIMIT_USD", "100.0")
        )
        self.alert_threshold = alert_threshold
        self.alert_callback = alert_callback
        
        # 用量存储 (内存，生产环境应使用持久化存储)
        self._daily_costs: Dict[str, Dict[str, float]] = defaultdict(
            lambda: defaultdict(float)
        )  # date_str -> user_id -> cost
        self._monthly_costs: Dict[str, Dict[str, float]] = defaultdict(
            lambda: defaultdict(float)
        )  # month_str -> user_id -> cost
        self._records: List[LLMUsageRecord] = []
        self._lock = Lock()
        
        # 告警状态 (避免重复告警)
        self._alerted: Dict[str, bool] = {}
    
    def check_before_request(
        self,
        user_id: Optional[str],
        estimated_input_tokens: int,
        estimated_output_tokens: int,
        model: str = "gpt-4o-mini",
    ) -> bool:
        """
        请求前检查
        
        在发送 LLM 请求前调用，检查是否会超限。
        
        Args:
            user_id: 用户 ID
            estimated_input_tokens: 预估输入 token 数
            estimated_output_tokens: 预估输出 token 数
            model: 使用的模型
            
        Returns:
            True 如果可以继续请求
            
        Raises:
            CostLimitExceededError: 如果会超限
        """
        user_key = user_id or "__global__"
        estimated_cost = self._estimate_cost(
            estimated_input_tokens,
            estimated_output_tokens,
            model,
        )
        
        now = datetime.utcnow()
        date_str = now.strftime("%Y-%m-%d")
        month_str = now.strftime("%Y-%m")
        
        with self._lock:
            # 检查每日限额
            current_daily = self._daily_costs[date_str][user_key]
            if current_daily + estimated_cost > self.daily_limit:
                raise CostLimitExceededError(
                    f"Daily limit exceeded for {user_key}",
                    limit_type="daily",
                    current=current_daily,
                    limit=self.daily_limit,
                )
            
            # 检查每月限额
            current_monthly = self._monthly_costs[month_str][user_key]
            if current_monthly + estimated_cost > self.monthly_limit:
                raise CostLimitExceededError(
                    f"Monthly limit exceeded for {user_key}",
                    limit_type="monthly",
                    current=current_monthly,
                    limit=self.monthly_limit,
                )
            
            # 检查是否需要发送告警
            self._check_alert(
                user_key,
                current_daily + estimated_cost,
                current_monthly + estimated_cost,
            )
        
        return True
    
    def record(
        self,
        usage: LLMUsage,
        model: str,
        provider: str,
        user_id: Optional[str] = None,
        request_id: Optional[str] = None,
        latency_ms: float = 0.0,
        success: bool = True,
        error_type: Optional[str] = None,
    ) -> LLMUsageRecord:
        """
        记录用量
        
        在 LLM 请求完成后调用。
        
        Args:
            usage: Token 用量
            model: 使用的模型
            provider: 使用的 Provider
            user_id: 用户 ID
            request_id: 请求 ID
            latency_ms: 延迟
            success: 是否成功
            error_type: 错误类型
            
        Returns:
            用量记录
        """
        cost = self._calculate_cost(
            usage.prompt_tokens,
            usage.completion_tokens,
            model,
        )
        
        record = LLMUsageRecord(
            record_id=f"rec_{uuid.uuid4().hex[:12]}",
            request_id=request_id or f"req_{uuid.uuid4().hex[:12]}",
            user_id=user_id,
            model=model,
            provider=provider,
            tokens_in=usage.prompt_tokens,
            tokens_out=usage.completion_tokens,
            cost_usd=cost,
            latency_ms=latency_ms,
            success=success,
            error_type=error_type,
        )
        
        user_key = user_id or "__global__"
        now = datetime.utcnow()
        date_str = now.strftime("%Y-%m-%d")
        month_str = now.strftime("%Y-%m")
        
        with self._lock:
            self._records.append(record)
            self._daily_costs[date_str][user_key] += cost
            self._monthly_costs[month_str][user_key] += cost
        
        logger.debug(
            f"Recorded usage: model={model}, tokens={usage.total_tokens}, "
            f"cost=${cost:.6f}, user={user_id}"
        )
        
        return record
    
    def get_daily_cost(self, user_id: Optional[str] = None) -> float:
        """获取今日成本"""
        user_key = user_id or "__global__"
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        with self._lock:
            return self._daily_costs[date_str][user_key]
    
    def get_monthly_cost(self, user_id: Optional[str] = None) -> float:
        """获取本月成本"""
        user_key = user_id or "__global__"
        month_str = datetime.utcnow().strftime("%Y-%m")
        with self._lock:
            return self._monthly_costs[month_str][user_key]
    
    def get_recent_records(
        self,
        user_id: Optional[str] = None,
        hours: int = 24,
    ) -> List[LLMUsageRecord]:
        """获取最近的用量记录"""
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        with self._lock:
            records = [
                r for r in self._records
                if r.timestamp >= cutoff
                and (user_id is None or r.user_id == user_id)
            ]
        return records
    
    def _estimate_cost(
        self,
        input_tokens: int,
        output_tokens: int,
        model: str,
    ) -> float:
        """预估成本"""
        costs = self.MODEL_COSTS.get(model, {"input": 2.50, "output": 10.00})
        input_cost = input_tokens * costs["input"] / 1_000_000
        output_cost = output_tokens * costs["output"] / 1_000_000
        return input_cost + output_cost
    
    def _calculate_cost(
        self,
        input_tokens: int,
        output_tokens: int,
        model: str,
    ) -> float:
        """计算实际成本"""
        return self._estimate_cost(input_tokens, output_tokens, model)
    
    def _check_alert(
        self,
        user_key: str,
        daily_cost: float,
        monthly_cost: float,
    ) -> None:
        """检查是否需要发送告警"""
        if not self.alert_callback:
            return
        
        # 每日告警
        daily_ratio = daily_cost / self.daily_limit
        alert_key = f"daily_{user_key}_{datetime.utcnow().strftime('%Y-%m-%d')}"
        if daily_ratio >= self.alert_threshold and alert_key not in self._alerted:
            self._alerted[alert_key] = True
            self.alert_callback(
                f"Daily cost for {user_key} reaching {daily_ratio:.0%}",
                daily_cost,
                self.daily_limit,
            )
        
        # 每月告警
        monthly_ratio = monthly_cost / self.monthly_limit
        alert_key = f"monthly_{user_key}_{datetime.utcnow().strftime('%Y-%m')}"
        if monthly_ratio >= self.alert_threshold and alert_key not in self._alerted:
            self._alerted[alert_key] = True
            self.alert_callback(
                f"Monthly cost for {user_key} reaching {monthly_ratio:.0%}",
                monthly_cost,
                self.monthly_limit,
            )
