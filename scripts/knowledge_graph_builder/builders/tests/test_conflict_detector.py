"""
ConflictDetector测试

Feature: cross-book-knowledge-graph, Property 6: Conflict Preservation
Requirement Refs: Req 3.1, Req 3.4, Req 3.5, Req 3.7
"""

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.builders.conflict_detector import (
    ConflictDetector,
)
from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    ConflictType,
    Dimension,
    DivinationSystem,
    RelationType,
    SourceNodeRef,
)


def create_concept(
    concept_id: str,
    label: str,
    dimension: Dimension,
    system: DivinationSystem,
    book_id: str,
    authority: float = 0.7,
) -> ConceptNode:
    """创建测试概念"""
    return ConceptNode(
        concept_id=concept_id,
        canonical_label_zh=label,
        divination_system=system,
        dimension=dimension,
        source_nodes=[SourceNodeRef(book_id=book_id, node_id="node_001")],
        authority_score=authority,
    )


class TestConflictDetector:
    """ConflictDetector测试"""
    
    def test_detect_direct_contradiction(self):
        """检测直接矛盾"""
        detector = ConflictDetector()
        
        concepts = [
            create_concept(
                "concept_a", "日主喜火", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_a"
            ),
            create_concept(
                "concept_b", "日主忌火", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_b"
            ),
        ]
        
        edges, outputs = detector.detect_conflicts(concepts)
        
        assert len(edges) >= 1
        assert edges[0].relation_type == RelationType.CONFLICTS_WITH
        assert edges[0].conflict_type == ConflictType.DIRECT_CONTRADICTION
    
    def test_detect_cross_system_divergence(self):
        """检测跨体系分歧"""
        detector = ConflictDetector()
        
        concepts = [
            create_concept(
                "concept_a", "事业运吉", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_a"
            ),
            create_concept(
                "concept_b", "事业运凶", 
                Dimension.CAREER, DivinationSystem.ASTRO, "book_b"
            ),
        ]
        
        edges, outputs = detector.detect_conflicts(concepts)
        
        # 应该检测到跨体系分歧
        cross_system_edges = [
            e for e in edges 
            if e.conflict_type == ConflictType.CROSS_SYSTEM_DIVERGENCE
        ]
        assert len(cross_system_edges) >= 1
    
    def test_no_conflict_different_dimension(self):
        """不同维度不冲突"""
        detector = ConflictDetector()
        
        concepts = [
            create_concept(
                "concept_a", "事业喜火", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_a"
            ),
            create_concept(
                "concept_b", "健康忌火", 
                Dimension.HEALTH, DivinationSystem.BAZI, "book_b"
            ),
        ]
        
        edges, outputs = detector.detect_conflicts(concepts)
        
        # 不同维度不应冲突
        assert len(edges) == 0
    
    def test_conflict_output_generated(self):
        """生成冲突输出"""
        detector = ConflictDetector()
        
        concepts = [
            create_concept(
                "concept_a", "财运吉", 
                Dimension.WEALTH, DivinationSystem.BAZI, "book_a", 0.9
            ),
            create_concept(
                "concept_b", "财运凶", 
                Dimension.WEALTH, DivinationSystem.BAZI, "book_b", 0.6
            ),
        ]
        
        edges, outputs = detector.detect_conflicts(concepts)
        
        assert len(outputs) >= 1
        output = outputs[0]
        assert output.viewpoint_a.concept_id in ["concept_a", "concept_b"]
        assert output.viewpoint_b.concept_id in ["concept_a", "concept_b"]
        assert output.resolution_hint  # 有解决提示
    
    def test_update_conflict_summaries(self):
        """更新冲突摘要"""
        detector = ConflictDetector()
        
        concepts = [
            create_concept(
                "concept_a", "喜金", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_a"
            ),
            create_concept(
                "concept_b", "忌金", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_b"
            ),
        ]
        
        edges, _ = detector.detect_conflicts(concepts)
        detector.update_conflict_summaries(concepts, edges)
        
        # 两个概念都应有conflict_summary
        for concept in concepts:
            assert concept.conflict_summary is not None
            assert concept.conflict_summary.conflict_count >= 1


class TestConflictDetectorPropertyBased:
    """属性测试"""
    
    @settings(max_examples=50)
    @given(
        authority_a=st.floats(min_value=0.1, max_value=1.0, allow_nan=False),
        authority_b=st.floats(min_value=0.1, max_value=1.0, allow_nan=False),
    )
    def test_conflict_preservation_property(self, authority_a, authority_b):
        """
        Property 6: Conflict Preservation
        验证冲突双方都被保留
        """
        detector = ConflictDetector()
        
        concepts = [
            create_concept(
                "concept_a", "喜用神", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_a", authority_a
            ),
            create_concept(
                "concept_b", "忌用神", 
                Dimension.CAREER, DivinationSystem.BAZI, "book_b", authority_b
            ),
        ]
        
        edges, outputs = detector.detect_conflicts(concepts)
        
        if edges:
            # 冲突边应包含双方
            edge = edges[0]
            involved = {edge.source_concept_id, edge.target_concept_id}
            assert "concept_a" in involved
            assert "concept_b" in involved
            
            # 输出应包含双方
            output = outputs[0]
            output_ids = {output.viewpoint_a.concept_id, output.viewpoint_b.concept_id}
            assert "concept_a" in output_ids
            assert "concept_b" in output_ids
