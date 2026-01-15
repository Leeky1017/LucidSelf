"""
Review Queue

管理需要人工审核的规则。

Feature: rule-converter
Requirement Refs: Req 12.1-12.6
"""

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class ReviewStatus(Enum):
    """审核状态"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    MODIFIED = "modified"


@dataclass
class ReviewItem:
    """审核项"""
    rule_id: str
    rule: Dict[str, Any]
    status: ReviewStatus = ReviewStatus.PENDING
    
    # 分类信息
    classification_score: float = 0.0
    classification_reasons: List[str] = field(default_factory=list)
    
    # 审核信息
    reviewed_at: Optional[str] = None
    reviewer_comment: Optional[str] = None
    modified_rule: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict:
        return {
            "rule_id": self.rule_id,
            "rule": self.rule,
            "status": self.status.value,
            "classification_score": self.classification_score,
            "classification_reasons": self.classification_reasons,
            "reviewed_at": self.reviewed_at,
            "reviewer_comment": self.reviewer_comment,
            "modified_rule": self.modified_rule,
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "ReviewItem":
        return cls(
            rule_id=data["rule_id"],
            rule=data["rule"],
            status=ReviewStatus(data.get("status", "pending")),
            classification_score=data.get("classification_score", 0.0),
            classification_reasons=data.get("classification_reasons", []),
            reviewed_at=data.get("reviewed_at"),
            reviewer_comment=data.get("reviewer_comment"),
            modified_rule=data.get("modified_rule"),
        )


class ReviewQueue:
    """
    审核队列
    
    管理需要人工审核的规则，支持批准、拒绝、修改操作。
    
    Requirement Refs: Req 12.1-12.6
    """
    
    def __init__(self, queue_path: Optional[Path] = None):
        self.queue_path = Path(queue_path) if queue_path else Path("data/rules/review_queue.json")
        self._items: Dict[str, ReviewItem] = {}
        self._loaded = False
    
    def load(self) -> None:
        """加载审核队列"""
        if not self.queue_path.exists():
            self._items = {}
            self._loaded = True
            return
        
        with open(self.queue_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self._items = {
            item["rule_id"]: ReviewItem.from_dict(item)
            for item in data.get("items", [])
        }
        self._loaded = True
        logger.info(f"Loaded {len(self._items)} review items")
    
    def save(self) -> None:
        """保存审核队列"""
        self.queue_path.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "total": len(self._items),
            "pending": len([i for i in self._items.values() if i.status == ReviewStatus.PENDING]),
            "approved": len([i for i in self._items.values() if i.status == ReviewStatus.APPROVED]),
            "rejected": len([i for i in self._items.values() if i.status == ReviewStatus.REJECTED]),
            "modified": len([i for i in self._items.values() if i.status == ReviewStatus.MODIFIED]),
            "items": [item.to_dict() for item in self._items.values()],
        }
        
        with open(self.queue_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Saved {len(self._items)} review items")
    
    def _ensure_loaded(self) -> None:
        """确保队列已加载"""
        if not self._loaded:
            self.load()
    
    def add(
        self,
        rule: Dict[str, Any],
        classification_score: float = 0.0,
        classification_reasons: Optional[List[str]] = None,
    ) -> ReviewItem:
        """
        添加规则到审核队列
        
        Args:
            rule: 规则字典
            classification_score: 分类得分
            classification_reasons: 分类原因
            
        Returns:
            ReviewItem
        """
        self._ensure_loaded()
        
        rule_id = rule.get("rule_id")
        if not rule_id:
            raise ValueError("Rule must have rule_id")
        
        item = ReviewItem(
            rule_id=rule_id,
            rule=rule,
            classification_score=classification_score,
            classification_reasons=classification_reasons or [],
        )
        
        self._items[rule_id] = item
        return item
    
    def add_batch(
        self,
        rules: List[Dict[str, Any]],
        scores: Optional[List[float]] = None,
        reasons: Optional[List[List[str]]] = None,
    ) -> int:
        """
        批量添加规则
        
        Args:
            rules: 规则列表
            scores: 分类得分列表
            reasons: 分类原因列表
            
        Returns:
            添加的数量
        """
        self._ensure_loaded()
        
        count = 0
        for i, rule in enumerate(rules):
            score = scores[i] if scores and i < len(scores) else 0.0
            reason = reasons[i] if reasons and i < len(reasons) else []
            
            try:
                self.add(rule, score, reason)
                count += 1
            except ValueError as e:
                logger.warning(f"Failed to add rule: {e}")
        
        return count
    
    def approve(self, rule_id: str, comment: Optional[str] = None) -> bool:
        """
        批准规则
        
        Args:
            rule_id: 规则ID
            comment: 审核评论
            
        Returns:
            是否成功
        """
        self._ensure_loaded()
        
        if rule_id not in self._items:
            return False
        
        item = self._items[rule_id]
        item.status = ReviewStatus.APPROVED
        item.reviewed_at = datetime.now(timezone.utc).isoformat()
        item.reviewer_comment = comment
        
        return True
    
    def reject(self, rule_id: str, comment: Optional[str] = None) -> bool:
        """
        拒绝规则
        
        Args:
            rule_id: 规则ID
            comment: 拒绝原因
            
        Returns:
            是否成功
        """
        self._ensure_loaded()
        
        if rule_id not in self._items:
            return False
        
        item = self._items[rule_id]
        item.status = ReviewStatus.REJECTED
        item.reviewed_at = datetime.now(timezone.utc).isoformat()
        item.reviewer_comment = comment
        
        return True
    
    def modify(
        self,
        rule_id: str,
        modified_rule: Dict[str, Any],
        comment: Optional[str] = None,
    ) -> bool:
        """
        修改规则
        
        Args:
            rule_id: 规则ID
            modified_rule: 修改后的规则
            comment: 修改说明
            
        Returns:
            是否成功
        """
        self._ensure_loaded()
        
        if rule_id not in self._items:
            return False
        
        item = self._items[rule_id]
        item.status = ReviewStatus.MODIFIED
        item.reviewed_at = datetime.now(timezone.utc).isoformat()
        item.reviewer_comment = comment
        item.modified_rule = modified_rule
        
        return True
    
    def get(self, rule_id: str) -> Optional[ReviewItem]:
        """获取审核项"""
        self._ensure_loaded()
        return self._items.get(rule_id)
    
    def get_pending(self) -> List[ReviewItem]:
        """获取待审核的项目"""
        self._ensure_loaded()
        return [item for item in self._items.values() if item.status == ReviewStatus.PENDING]
    
    def get_approved(self) -> List[ReviewItem]:
        """获取已批准的项目"""
        self._ensure_loaded()
        return [
            item for item in self._items.values()
            if item.status in [ReviewStatus.APPROVED, ReviewStatus.MODIFIED]
        ]
    
    def get_approved_rules(self) -> List[Dict]:
        """获取已批准的规则"""
        approved = self.get_approved()
        rules = []
        for item in approved:
            if item.status == ReviewStatus.MODIFIED and item.modified_rule:
                rules.append(item.modified_rule)
            else:
                rules.append(item.rule)
        return rules
    
    def get_rejected(self) -> List[ReviewItem]:
        """获取已拒绝的项目"""
        self._ensure_loaded()
        return [item for item in self._items.values() if item.status == ReviewStatus.REJECTED]
    
    def clear_processed(self) -> int:
        """清除已处理的项目（保留待审核的）"""
        self._ensure_loaded()
        
        pending = {k: v for k, v in self._items.items() if v.status == ReviewStatus.PENDING}
        removed = len(self._items) - len(pending)
        self._items = pending
        
        return removed
    
    @property
    def stats(self) -> Dict[str, int]:
        """获取统计信息"""
        self._ensure_loaded()
        return {
            "total": len(self._items),
            "pending": len([i for i in self._items.values() if i.status == ReviewStatus.PENDING]),
            "approved": len([i for i in self._items.values() if i.status == ReviewStatus.APPROVED]),
            "rejected": len([i for i in self._items.values() if i.status == ReviewStatus.REJECTED]),
            "modified": len([i for i in self._items.values() if i.status == ReviewStatus.MODIFIED]),
        }
    
    def __len__(self) -> int:
        self._ensure_loaded()
        return len(self._items)
    
    def __contains__(self, rule_id: str) -> bool:
        self._ensure_loaded()
        return rule_id in self._items
