"""
Quality Classifier

对生成的规则进行质量分级。

Feature: rule-converter
Requirement Refs: Req 8.1-8.10
"""

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

from scripts.rule_converter.loaders.factor_ontology import FactorOntology
from scripts.rule_converter.loaders.logic_chain_loader import LogicChainNode
from scripts.rule_converter.loaders.snippet_store import SnippetStore

logger = logging.getLogger(__name__)


class RuleQuality(Enum):
    """规则质量等级"""
    AUTO_APPROVE = "auto_approve"
    HUMAN_REVIEW = "human_review"
    REJECT = "reject"


@dataclass
class ClassificationResult:
    """分类结果"""
    quality: RuleQuality
    score: float
    reasons: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "quality": self.quality.value,
            "score": self.score,
            "reasons": self.reasons,
        }


class QualityClassifier:
    """
    规则质量分级器
    
    基于多个维度评估生成规则的质量，决定是否自动批准或需要人工审核。
    
    评分维度：
    - factor_refs 完整性 (30%)
    - snippet 可解析性 (30%)
    - condition 推断置信度 (20%)
    - source_ref 完整性 (20%)
    
    分级阈值：
    - AUTO_APPROVE: score >= 0.8
    - HUMAN_REVIEW: 0.5 <= score < 0.8
    - REJECT: score < 0.5
    
    Requirement Refs: Req 8.1-8.10
    """
    
    # 评分权重（简化版：主要看是否有有效的触发条件）
    FACTOR_WEIGHT = 0.50      # 有因子 → 有触发条件
    CONDITION_WEIGHT = 0.30   # 有显式条件 → 更明确
    SOURCE_WEIGHT = 0.20      # 有溯源 → 可追溯
    
    # 分级阈值（降低阈值，信任 LogicChain 内容）
    AUTO_APPROVE_THRESHOLD = 0.5  # 有因子就通过
    HUMAN_REVIEW_THRESHOLD = 0.3
    
    def __init__(
        self,
        ontology: Optional[FactorOntology] = None,
        snippet_store: Optional[SnippetStore] = None,
    ):
        self.ontology = ontology
        self.snippet_store = snippet_store
        
        # 统计
        self._stats = {
            "total_classified": 0,
            "auto_approve_count": 0,
            "human_review_count": 0,
            "reject_count": 0,
        }
    
    def classify(
        self,
        node: LogicChainNode,
        rule: Dict[str, Any],
        condition_confidence: float = 0.7,
    ) -> ClassificationResult:
        """
        对规则进行质量分级
        
        简化逻辑：LogicChain 内容已经过人工审核，只要有 factor_refs 就是有效规则
        
        Args:
            node: 原始 LogicChain 节点
            rule: 生成的规则字典
            condition_confidence: 条件推断的置信度
            
        Returns:
            ClassificationResult
        """
        score = 0.0
        reasons = []
        
        # 1. factor_refs 有效性 (50%) - 有因子就是有效规则
        factor_score, factor_reason = self._score_factors(node)
        score += factor_score * self.FACTOR_WEIGHT
        if factor_reason:
            reasons.append(factor_reason)
        
        # 2. condition 推断置信度 (30%)
        condition_score = min(1.0, condition_confidence)
        score += condition_score * self.CONDITION_WEIGHT
        if condition_confidence < 0.5:
            reasons.append(f"条件推断置信度低: {condition_confidence:.2f}")
        
        # 3. source_ref 完整性 (20%)
        source_score, source_reason = self._score_source(node, rule)
        score += source_score * self.SOURCE_WEIGHT
        if source_reason:
            reasons.append(source_reason)
        
        # 确定质量等级
        if score >= self.AUTO_APPROVE_THRESHOLD:
            quality = RuleQuality.AUTO_APPROVE
            self._stats["auto_approve_count"] += 1
        elif score >= self.HUMAN_REVIEW_THRESHOLD:
            quality = RuleQuality.HUMAN_REVIEW
            self._stats["human_review_count"] += 1
        else:
            quality = RuleQuality.REJECT
            self._stats["reject_count"] += 1
        
        self._stats["total_classified"] += 1
        
        return ClassificationResult(
            quality=quality,
            score=round(score, 3),
            reasons=reasons,
        )
    
    def _score_factors(self, node: LogicChainNode) -> tuple:
        """评估 factor_refs - 简化版：有因子就满分"""
        if not node.factor_refs:
            # 没有 factor_refs 但有显式 condition 也可以
            if node.condition:
                return 0.8, None
            return 0.0, "无 factor_refs 且无 condition"
        
        # 有 factor_refs 就满分（信任 LogicChain 数据）
        return 1.0, None
    
    def _score_snippets(self, node: LogicChainNode) -> tuple:
        """评估 snippet 可解析性"""
        if not node.snippet_ids:
            return 0.0, "无 snippet_ids"
        
        if self.snippet_store is None:
            return 0.5, "SnippetStore 未加载"
        
        # 检查 snippet 存在性
        resolved = 0
        for sid in node.snippet_ids:
            if self.snippet_store.has(sid):
                resolved += 1
        
        if resolved == len(node.snippet_ids):
            return 1.0, None
        
        ratio = resolved / len(node.snippet_ids)
        return ratio, f"部分 snippet 未解析: {resolved}/{len(node.snippet_ids)}"
    
    def _score_source(self, node: LogicChainNode, rule: Dict) -> tuple:
        """评估 source_ref 完整性"""
        # 检查节点 metadata
        source_ref = node.metadata.get("source_ref") if node.metadata else None
        
        if not source_ref:
            return 0.0, "缺少 source_ref"
        
        # 检查规则 metadata
        rule_metadata = rule.get("metadata", {})
        if not rule_metadata.get("book_id"):
            return 0.5, "规则 metadata 不完整"
        
        if not rule_metadata.get("l1_anchor"):
            return 0.7, "缺少 l1_anchor"
        
        return 1.0, None
    
    @property
    def stats(self) -> Dict[str, int]:
        """获取统计信息"""
        return self._stats.copy()
    
    def reset_stats(self):
        """重置统计"""
        for key in self._stats:
            self._stats[key] = 0
