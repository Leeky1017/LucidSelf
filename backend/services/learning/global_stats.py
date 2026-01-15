"""
全局规则统计

收集和汇总规则执行统计数据。

对照文档: docs/ls_roadmap_executable.md §GAP-06
"""

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class RuleStats(BaseModel):
    """单条规则统计"""
    rule_id: str
    engine_id: str
    
    # 执行统计
    total_executions: int = 0
    hit_count: int = 0
    miss_count: int = 0
    hit_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    
    # 时间统计
    avg_execution_time_ms: float = 0.0
    
    # 反馈统计
    feedback_positive: int = 0
    feedback_negative: int = 0
    effectiveness: float = Field(default=0.5, ge=0.0, le=1.0)
    
    # 元数据
    first_seen: datetime = Field(default_factory=datetime.now)
    last_seen: datetime = Field(default_factory=datetime.now)


class EngineStats(BaseModel):
    """引擎统计"""
    engine_id: str
    
    total_rules: int = 0
    total_executions: int = 0
    avg_hit_rate: float = 0.0
    avg_effectiveness: float = 0.5
    
    last_updated: datetime = Field(default_factory=datetime.now)


class GlobalStats(BaseModel):
    """全局统计"""
    total_rules: int = 0
    total_executions: int = 0
    total_feedback: int = 0
    
    avg_hit_rate: float = 0.0
    avg_effectiveness: float = 0.5
    
    engines: Dict[str, EngineStats] = Field(default_factory=dict)
    top_rules: List[str] = Field(default_factory=list)
    bottom_rules: List[str] = Field(default_factory=list)
    
    last_updated: datetime = Field(default_factory=datetime.now)


class RuleStatsCollector:
    """
    规则统计收集器
    
    职责:
    - 收集规则执行数据
    - 汇总统计信息
    - 识别高效/低效规则
    """
    
    def __init__(self):
        """初始化收集器"""
        self._rule_stats: Dict[str, RuleStats] = {}
        self._daily_executions: Dict[str, int] = defaultdict(int)
    
    def record_execution(
        self,
        rule_id: str,
        engine_id: str,
        matched: bool,
        execution_time_ms: float = 0.0,
    ) -> None:
        """
        记录规则执行
        
        Args:
            rule_id: 规则 ID
            engine_id: 引擎 ID
            matched: 是否匹配
            execution_time_ms: 执行时间（毫秒）
        """
        if rule_id not in self._rule_stats:
            self._rule_stats[rule_id] = RuleStats(
                rule_id=rule_id,
                engine_id=engine_id,
            )
        
        stats = self._rule_stats[rule_id]
        stats.total_executions += 1
        
        if matched:
            stats.hit_count += 1
        else:
            stats.miss_count += 1
        
        # 更新命中率
        stats.hit_rate = stats.hit_count / stats.total_executions
        
        # 更新平均执行时间
        if execution_time_ms > 0:
            old_avg = stats.avg_execution_time_ms
            n = stats.total_executions
            stats.avg_execution_time_ms = (old_avg * (n - 1) + execution_time_ms) / n
        
        stats.last_seen = datetime.now()
        
        # 更新日统计
        today = datetime.now().strftime("%Y-%m-%d")
        self._daily_executions[today] += 1
    
    def record_feedback(
        self,
        rule_id: str,
        is_positive: bool,
    ) -> None:
        """
        记录规则反馈
        
        Args:
            rule_id: 规则 ID
            is_positive: 是否正面反馈
        """
        if rule_id not in self._rule_stats:
            return
        
        stats = self._rule_stats[rule_id]
        
        if is_positive:
            stats.feedback_positive += 1
        else:
            stats.feedback_negative += 1
        
        # 更新有效性
        total_feedback = stats.feedback_positive + stats.feedback_negative
        if total_feedback > 0:
            stats.effectiveness = stats.feedback_positive / total_feedback
    
    def get_rule_stats(self, rule_id: str) -> Optional[RuleStats]:
        """获取规则统计"""
        return self._rule_stats.get(rule_id)
    
    def get_engine_stats(self, engine_id: str) -> EngineStats:
        """获取引擎统计"""
        rules = [s for s in self._rule_stats.values() if s.engine_id == engine_id]
        
        if not rules:
            return EngineStats(engine_id=engine_id)
        
        return EngineStats(
            engine_id=engine_id,
            total_rules=len(rules),
            total_executions=sum(r.total_executions for r in rules),
            avg_hit_rate=sum(r.hit_rate for r in rules) / len(rules),
            avg_effectiveness=sum(r.effectiveness for r in rules) / len(rules),
            last_updated=datetime.now(),
        )
    
    def get_global_stats(self) -> GlobalStats:
        """获取全局统计"""
        all_rules = list(self._rule_stats.values())
        
        if not all_rules:
            return GlobalStats()
        
        # 按有效性排序
        sorted_by_effectiveness = sorted(
            all_rules,
            key=lambda r: r.effectiveness,
            reverse=True,
        )
        
        # 汇总引擎统计
        engine_ids = set(r.engine_id for r in all_rules)
        engines = {eid: self.get_engine_stats(eid) for eid in engine_ids}
        
        return GlobalStats(
            total_rules=len(all_rules),
            total_executions=sum(r.total_executions for r in all_rules),
            total_feedback=sum(
                r.feedback_positive + r.feedback_negative for r in all_rules
            ),
            avg_hit_rate=sum(r.hit_rate for r in all_rules) / len(all_rules),
            avg_effectiveness=sum(r.effectiveness for r in all_rules) / len(all_rules),
            engines=engines,
            top_rules=[r.rule_id for r in sorted_by_effectiveness[:5]],
            bottom_rules=[r.rule_id for r in sorted_by_effectiveness[-5:]],
            last_updated=datetime.now(),
        )
    
    def get_top_rules(self, n: int = 10) -> List[RuleStats]:
        """获取最高效规则"""
        sorted_rules = sorted(
            self._rule_stats.values(),
            key=lambda r: r.effectiveness,
            reverse=True,
        )
        return sorted_rules[:n]
    
    def get_bottom_rules(self, n: int = 10) -> List[RuleStats]:
        """获取最低效规则"""
        sorted_rules = sorted(
            self._rule_stats.values(),
            key=lambda r: r.effectiveness,
        )
        return sorted_rules[:n]
    
    def reset(self) -> None:
        """重置状态（用于测试）"""
        self._rule_stats.clear()
        self._daily_executions.clear()
