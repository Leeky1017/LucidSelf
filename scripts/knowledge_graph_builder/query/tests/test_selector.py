"""
ConceptSelector测试

Feature: cross-book-knowledge-graph
Property 19: Selector Funnel Stage Monotonicity
Property 20: Selector Quota Enforcement
Requirement Refs: Req 12.2, Req 12.3, Req 12.4
"""

from datetime import datetime

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    Dimension,
    DivinationSystem,
    GraphMetadata,
    KnowledgeGraph,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.selector import DEFAULT_SYSTEM_QUOTAS
from scripts.knowledge_graph_builder.query.selector import ConceptSelector


def create_test_graph(num_per_system: int = 20):
    """创建测试图谱，每个体系num_per_system个概念"""
    concepts = []
    
    for system in [DivinationSystem.BAZI, DivinationSystem.ASTRO, DivinationSystem.TAROT]:
        for i in range(num_per_system):
            concepts.append(ConceptNode(
                concept_id=f"concept_{system.value}_{i}",
                canonical_label_zh=f"{system.value}概念{i}",
                divination_system=system,
                dimension=Dimension.CAREER if i % 2 == 0 else Dimension.WEALTH,
                source_nodes=[SourceNodeRef(book_id="test", node_id=f"node_{i}")],
                factor_refs=[f"factor_{system.value}", f"factor_common"],
                authority_score=0.9 - i * 0.01,
            ))
    
    graph = KnowledgeGraph(
        concepts=concepts,
        metadata=GraphMetadata(version="1.0.0", build_timestamp=datetime.now()),
    )
    graph.build_indices()
    return graph


class TestConceptSelector:
    """ConceptSelector测试"""
    
    def test_factor_match_stage(self):
        """Stage 1: 因子匹配"""
        graph = create_test_graph()
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_bazi"],
        )
        
        # 只有bazi概念应该被选中
        for concept in result.selected_concepts:
            assert "factor_bazi" in concept.factor_refs
    
    def test_dimension_filter_stage(self):
        """Stage 2: 维度过滤"""
        graph = create_test_graph()
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
            target_dimensions=[Dimension.CAREER],
        )
        
        # 只有CAREER维度的概念
        for concept in result.selected_concepts:
            assert concept.dimension == Dimension.CAREER
    
    def test_authority_rank_stage(self):
        """Stage 3: 权威性排序"""
        graph = create_test_graph()
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_bazi"],  # 只选择一个体系
        )
        
        # 同体系内按权威性排序
        scores = [c.authority_score for c in result.selected_concepts]
        assert scores == sorted(scores, reverse=True)
    
    def test_quota_apply_stage(self):
        """Stage 4: 配额应用"""
        graph = create_test_graph(num_per_system=30)
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
        )
        
        # 检查每个体系不超过配额
        by_system = {}
        for concept in result.selected_concepts:
            sys = concept.divination_system
            by_system[sys] = by_system.get(sys, 0) + 1
        
        for system, count in by_system.items():
            quota = DEFAULT_SYSTEM_QUOTAS.get(system, 5)
            assert count <= quota
    
    def test_total_truncate_stage(self):
        """Stage 5: 总数截断"""
        graph = create_test_graph(num_per_system=30)
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
            total_max_concepts=20,
        )
        
        assert len(result.selected_concepts) <= 20
    
    def test_funnel_stats_monotonicity(self):
        """漏斗各阶段单调递减"""
        graph = create_test_graph(num_per_system=30)
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
            target_dimensions=[Dimension.CAREER],
        )
        
        stats = result.funnel_stats
        assert stats.validate_monotonicity()
    
    def test_truncated_systems_recorded(self):
        """记录被截断的体系"""
        graph = create_test_graph(num_per_system=30)
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
        )
        
        # 如果有体系被截断，应该记录
        if len(result.truncated_systems) > 0:
            for system in result.truncated_systems:
                assert isinstance(system, DivinationSystem)


class TestSelectorPropertyBased:
    """属性测试"""
    
    @settings(max_examples=50)
    @given(
        num_concepts=st.integers(min_value=5, max_value=30),
    )
    def test_funnel_monotonicity_property(self, num_concepts):
        """
        Property 19: Selector Funnel Stage Monotonicity
        验证漏斗各阶段数量单调递减
        """
        graph = create_test_graph(num_per_system=num_concepts)
        selector = ConceptSelector(graph)
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
            target_dimensions=[Dimension.CAREER],
        )
        
        stats = result.funnel_stats
        assert stats.stage_factor_match >= stats.stage_dimension_filter
        assert stats.stage_dimension_filter >= stats.stage_authority_rank
        assert stats.stage_authority_rank >= stats.stage_quota_apply
        assert stats.stage_quota_apply >= stats.stage_total_truncate
    
    @settings(max_examples=50)
    @given(
        quota=st.integers(min_value=1, max_value=10),
    )
    def test_quota_enforcement_property(self, quota):
        """
        Property 20: Selector Quota Enforcement
        验证每个体系不超过配额
        """
        graph = create_test_graph(num_per_system=30)
        selector = ConceptSelector(graph)
        
        # 使用自定义配额
        custom_quotas = {
            DivinationSystem.BAZI: quota,
            DivinationSystem.ASTRO: quota,
            DivinationSystem.TAROT: quota,
        }
        
        result = selector.select(
            activated_factor_ids=["factor_common"],
            custom_quotas=custom_quotas,
        )
        
        # 检查每个体系不超过配额
        by_system = {}
        for concept in result.selected_concepts:
            sys = concept.divination_system
            by_system[sys] = by_system.get(sys, 0) + 1
        
        for system, count in by_system.items():
            assert count <= quota
