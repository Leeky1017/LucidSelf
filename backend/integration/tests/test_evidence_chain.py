"""
EvidenceChainBuilder Tests

证据链构建器测试。

对照 tasks.md Task 7.3, 7.5
对照 Requirements 4.1-4.5
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult
from backend.integration import EvidenceChainBuilder
from backend.integration.models import WeightedResult


class TestEvidenceChainBuilderBasic:
    """EvidenceChainBuilder 基础测试"""
    
    def test_build_basic(self, evidence_builder):
        """测试基础证据链构建"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.8,
                    weight=1.5,
                    tags=["事业"],
                    evidence_factors=["day_master"],
                    source_book="子平真诠",
                    l1_anchor="官印相生章",
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.5,
            ),
        ]
        
        evidence = evidence_builder.build(weighted)
        
        assert len(evidence) == 1
        assert evidence[0].rule_id == "rule_1"
        assert evidence[0].source_book == "子平真诠"
    
    def test_build_empty_input(self, evidence_builder):
        """测试空输入"""
        evidence = evidence_builder.build([])
        
        assert evidence == []
    
    def test_build_sorted_by_score(self, evidence_builder):
        """测试按分数排序 (Requirement 4.3)"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_low",
                    matched=True,
                    confidence=0.5,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.3,
            ),
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_high",
                    matched=True,
                    confidence=0.9,
                    weight=2.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_b",
                engine_weight=1.0,
                final_score=0.7,
            ),
        ]
        
        evidence = evidence_builder.build(weighted)
        
        # 高分在前
        assert evidence[0].rule_id == "rule_high"
        assert evidence[1].rule_id == "rule_low"
    
    def test_build_max_limit(self, evidence_builder):
        """测试证据数量限制 (Requirement 7.3)"""
        # 创建超过 20 条证据
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=f"rule_{i}",
                    matched=True,
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.1,
            )
            for i in range(30)
        ]
        
        evidence = evidence_builder.build(weighted)
        
        assert len(evidence) <= 20


class TestEvidenceChainDeduplication:
    """证据去重测试"""
    
    def test_no_duplicate_rule_ids(self, evidence_builder):
        """
        测试证据去重
        
        Property P4: Evidence Uniqueness
        对照 Requirement 4.4
        """
        # 相同 rule_id 的重复结果
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",  # 相同 ID
                    matched=True,
                    confidence=0.8,
                    weight=1.5,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.6,
            ),
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",  # 相同 ID
                    matched=True,
                    confidence=0.7,
                    weight=1.2,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_b",
                engine_weight=1.0,
                final_score=0.4,
            ),
        ]
        
        evidence = evidence_builder.build(weighted)
        
        # 应该只有一条证据
        assert len(evidence) == 1
        rule_ids = [e.rule_id for e in evidence]
        assert len(rule_ids) == len(set(rule_ids))  # 无重复


class TestEvidenceChainTraceability:
    """溯源信息测试"""
    
    def test_traceability_preserved(self, evidence_builder):
        """测试溯源信息保留 (Requirement 4.2)"""
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id="rule_1",
                    matched=True,
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=["factor_1", "factor_2"],
                    source_book="子平真诠",
                    l1_anchor="论十神",
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=0.5,
            ),
        ]
        
        evidence = evidence_builder.build(weighted)
        
        assert evidence[0].source_book == "子平真诠"
        assert evidence[0].l1_anchor == "论十神"
        assert evidence[0].evidence_factors == ["factor_1", "factor_2"]
    
    def test_source_breakdown(self, evidence_builder):
        """测试来源分解统计"""
        evidence = [
            RuntimeRuleResult(
                rule_id="rule_1",
                matched=True,
                confidence=0.8,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                source_book="子平真诠",
                execution_time_ms=1.0,
            ),
            RuntimeRuleResult(
                rule_id="rule_2",
                matched=True,
                confidence=0.8,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                source_book="子平真诠",
                execution_time_ms=1.0,
            ),
            RuntimeRuleResult(
                rule_id="rule_3",
                matched=True,
                confidence=0.8,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                source_book="Tetrabiblos",
                execution_time_ms=1.0,
            ),
        ]
        
        breakdown = evidence_builder.get_source_breakdown(evidence)
        
        assert breakdown["子平真诠"] == 2
        assert breakdown["Tetrabiblos"] == 1


class TestEvidenceChainPropertyTests:
    """属性测试"""
    
    @given(st.lists(
        st.text(min_size=5, max_size=20, alphabet="abcdefghijklmnopqrstuvwxyz0123456789_"),
        min_size=1,
        max_size=30,
        unique=True,  # 确保 rule_id 唯一
    ))
    @settings(max_examples=20)
    def test_evidence_uniqueness_property(self, rule_ids):
        """
        属性测试：证据链无重复 rule_id
        
        Property P4: Evidence Uniqueness
        """
        builder = EvidenceChainBuilder()
        
        weighted = [
            WeightedResult(
                result=RuntimeRuleResult(
                    rule_id=rule_id,
                    matched=True,
                    confidence=0.8,
                    weight=1.0,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                engine_id="engine_a",
                engine_weight=1.0,
                final_score=1.0 / len(rule_ids),
            )
            for rule_id in rule_ids
        ]
        
        evidence = builder.build(weighted)
        
        # 证据链 rule_id 应该唯一
        evidence_ids = [e.rule_id for e in evidence]
        assert len(evidence_ids) == len(set(evidence_ids))
        
        # 证据链长度不超过 20
        assert len(evidence) <= 20
