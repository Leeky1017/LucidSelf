"""
Evidence Chain Builder - 证据链构建器

构建支持融合结论的证据链。

对照 design.md §2.5 EvidenceChainBuilder
对照 Requirements 4.1-4.5
"""

from __future__ import annotations

import logging
from typing import List, Set

from backend.core.contracts import RuntimeRuleResult
from backend.integration.models import WeightedResult

logger = logging.getLogger(__name__)


class EvidenceChainBuilder:
    """
    证据链构建器
    
    职责：
    - 构建完整证据链 (Requirement 4.1)
    - 支持 L1 典籍溯源 (Requirement 4.2)
    - 证据排序 (Requirement 4.3)
    - 证据去重 (Requirement 4.4)
    
    对照 design.md §2.5
    """
    
    MAX_EVIDENCE: int = 20
    """最大证据数量 (Requirement 7.3: 1-20 条)"""
    
    def build(
        self,
        weighted_results: List[WeightedResult],
    ) -> List[RuntimeRuleResult]:
        """
        构建证据链
        
        按 final_score 降序排序，去重后返回。
        
        对照 Requirement 4.1, 4.3, 4.4
        对照 design.md §2.5 build
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            证据链 (1-20 条 RuntimeRuleResult)
        """
        if not weighted_results:
            return []
        
        # 按 final_score 排序 (Requirement 4.3)
        sorted_results = sorted(
            weighted_results,
            key=lambda x: x.final_score,
            reverse=True,
        )
        
        # 去重 (Requirement 4.4: 相同 rule_id 不重复)
        seen_rules: Set[str] = set()
        evidence_chain: List[RuntimeRuleResult] = []
        
        for wr in sorted_results:
            if wr.result.rule_id not in seen_rules:
                seen_rules.add(wr.result.rule_id)
                evidence_chain.append(wr.result)
                
                if len(evidence_chain) >= self.MAX_EVIDENCE:
                    break
        
        return evidence_chain
    
    def build_with_traceability(
        self,
        weighted_results: List[WeightedResult],
    ) -> List[RuntimeRuleResult]:
        """
        构建带溯源信息的证据链
        
        确保每条证据都包含 L1 溯源信息。
        
        对照 Requirement 4.2
        
        Args:
            weighted_results: 加权结果列表
            
        Returns:
            带溯源的证据链
        """
        evidence_chain = self.build(weighted_results)
        
        # 记录缺失溯源信息的证据
        for evidence in evidence_chain:
            if not evidence.source_book and not evidence.l1_anchor:
                logger.warning(
                    f"Evidence {evidence.rule_id} missing traceability info"
                )
        
        return evidence_chain
    
    def get_source_breakdown(
        self,
        evidence_chain: List[RuntimeRuleResult],
    ) -> dict:
        """
        获取证据来源分解
        
        统计各典籍的证据贡献。
        
        Args:
            evidence_chain: 证据链
            
        Returns:
            来源统计 {source_book: count}
        """
        source_counts: dict = {}
        
        for evidence in evidence_chain:
            source = evidence.source_book or "unknown"
            source_counts[source] = source_counts.get(source, 0) + 1
        
        return source_counts
