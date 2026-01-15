"""
因子更新器

接收用户反馈，更新因子权重和有效性评分。

对照文档: docs/ls_roadmap_executable.md §GAP-06
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class FeedbackRecord(BaseModel):
    """用户反馈记录"""
    feedback_id: str = Field(..., pattern=r"^fb_[a-z0-9]{12}$")
    user_id: str
    action_item_id: str
    
    # 反馈类型
    feedback_type: str = Field(
        ...,
        pattern=r"^(positive|negative|partial|skip)$",
        description="正面/负面/部分/跳过"
    )
    
    # 反馈详情
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = None
    
    # 关联的因子和规则
    source_factors: List[str] = Field(default_factory=list)
    source_rules: List[str] = Field(default_factory=list)
    
    # 时间戳
    created_at: datetime = Field(default_factory=datetime.now)


class FactorAdjustment(BaseModel):
    """因子调整记录"""
    factor_id: str
    old_weight: float
    new_weight: float
    adjustment_reason: str
    feedback_ids: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)


class FactorUpdater:
    """
    因子更新器
    
    职责:
    - 接收用户反馈
    - 计算因子权重调整
    - 更新因子有效性评分
    """
    
    # 调整幅度
    POSITIVE_BOOST = 0.02    # 正面反馈加成
    NEGATIVE_PENALTY = -0.03  # 负面反馈惩罚
    PARTIAL_BOOST = 0.01      # 部分反馈加成
    
    # 权重边界
    MIN_WEIGHT = 0.1
    MAX_WEIGHT = 2.0
    
    def __init__(self):
        """初始化更新器"""
        # 内存存储，生产环境应持久化
        self._feedback_records: List[FeedbackRecord] = []
        self._factor_weights: Dict[str, float] = {}  # factor_id → weight
        self._adjustments: List[FactorAdjustment] = []
    
    def record_feedback(self, feedback: FeedbackRecord) -> None:
        """
        记录用户反馈
        
        Args:
            feedback: 反馈记录
        """
        self._feedback_records.append(feedback)
        logger.info(
            f"Recorded feedback {feedback.feedback_id} "
            f"type={feedback.feedback_type} for action={feedback.action_item_id}"
        )
        
        # 处理反馈
        self._process_feedback(feedback)
    
    def _process_feedback(self, feedback: FeedbackRecord) -> None:
        """处理单条反馈"""
        if not feedback.source_factors:
            return
        
        # 计算调整量
        if feedback.feedback_type == "positive":
            adjustment = self.POSITIVE_BOOST
        elif feedback.feedback_type == "negative":
            adjustment = self.NEGATIVE_PENALTY
        elif feedback.feedback_type == "partial":
            adjustment = self.PARTIAL_BOOST
        else:
            return  # skip 类型不调整
        
        # 应用到相关因子
        for factor_id in feedback.source_factors:
            self._adjust_factor_weight(factor_id, adjustment, feedback.feedback_id)
    
    def _adjust_factor_weight(
        self,
        factor_id: str,
        adjustment: float,
        feedback_id: str,
    ) -> None:
        """调整因子权重"""
        old_weight = self._factor_weights.get(factor_id, 1.0)
        new_weight = old_weight + adjustment
        
        # 约束边界
        new_weight = max(self.MIN_WEIGHT, min(self.MAX_WEIGHT, new_weight))
        
        if new_weight != old_weight:
            self._factor_weights[factor_id] = new_weight
            
            record = FactorAdjustment(
                factor_id=factor_id,
                old_weight=old_weight,
                new_weight=new_weight,
                adjustment_reason=f"feedback adjustment",
                feedback_ids=[feedback_id],
            )
            self._adjustments.append(record)
            
            logger.debug(
                f"Adjusted factor {factor_id}: {old_weight:.3f} → {new_weight:.3f}"
            )
    
    def get_factor_weight(self, factor_id: str) -> float:
        """获取因子当前权重"""
        return self._factor_weights.get(factor_id, 1.0)
    
    def get_factor_weights(self) -> Dict[str, float]:
        """获取所有因子权重"""
        return dict(self._factor_weights)
    
    def get_adjustments(self, factor_id: Optional[str] = None) -> List[FactorAdjustment]:
        """获取调整历史"""
        if factor_id:
            return [a for a in self._adjustments if a.factor_id == factor_id]
        return list(self._adjustments)
    
    def get_feedback_count(self) -> int:
        """获取反馈总数"""
        return len(self._feedback_records)
    
    def reset(self) -> None:
        """重置状态（用于测试）"""
        self._feedback_records.clear()
        self._factor_weights.clear()
        self._adjustments.clear()
