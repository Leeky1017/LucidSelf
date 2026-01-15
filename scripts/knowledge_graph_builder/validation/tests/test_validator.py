"""
GraphValidator测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 6.1~6.10
Design Refs: Design.md#错误分类

Property 13: Validation Reference Resolution
Property 14: Circular Dependency Detection
"""

import tempfile
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.edge import (
    ConflictType,
    RelationType,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)
from scripts.knowledge_graph_builder.validation import (
    GraphValidator,
    IssueSeverity,
    IssueType,
    ValidationReport,
)


# ============ Fixtures ============

@pytest.fixture
def sample_metadata():
    return GraphMetadata(
        version="1.0.0",
        build_timestamp=datetime.now(),
    )


@pytest.fixture
def sample_concept():
    return ConceptNode(
        concept_id="concept_bazi_test_001",
        canonical_label_zh="测试概念",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[
            SourceNodeRef(book_id="滴天髓", node_id="n_test_001", snippet_ids=[])
        ],
        factor_refs=["bazi_day_master"],
        authority_score=0.85,
    )


@pytest.fixture
def connected_graph(sample_metadata):
    """创建有连接的图谱"""
    concept1 = ConceptNode(
        concept_id="concept_bazi_a_001",
        canonical_label_zh="概念A",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="n_001", snippet_ids=[])],
    )
    concept2 = ConceptNode(
        concept_id="concept_bazi_b_001",
        canonical_label_zh="概念B",
        divination_system=DivinationSystem.BAZI,
        dimension=Dimension.CAREER,
        source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="n_002", snippet_ids=[])],
    )
    edge = SemanticEdge(
        edge_id="edge_a_b_001",
        source_concept_id="concept_bazi_a_001",
        target_concept_id="concept_bazi_b_001",
        relation_type=RelationType.ENTAILS,
        confidence=0.8,
    )
    
    return KnowledgeGraph(
        metadata=sample_metadata,
        concepts=[concept1, concept2],
        edges=[edge],
    )


@pytest.fixture
def validator():
    return GraphValidator()


# ============ 基础功能测试 ============

class TestGraphValidator:
    """GraphValidator基础测试"""
    
    def test_validate_empty_graph(self, sample_metadata, validator):
        """测试空图谱验证"""
        graph = KnowledgeGraph(metadata=sample_metadata, concepts=[], edges=[])
        report = validator.validate(graph)
        
        assert report.is_valid()
        assert len(report.issues) == 1
        assert report.issues[0].issue_type == IssueType.EMPTY_GRAPH
        assert report.issues[0].severity == IssueSeverity.INFO
    
    def test_validate_valid_graph(self, connected_graph, validator):
        """测试有效图谱验证"""
        report = validator.validate(connected_graph)
        
        # 有效图谱应该没有ERROR
        assert report.error_count == 0
        assert report.is_valid()
    
    def test_detect_duplicate_concept_ids(self, sample_metadata, validator):
        """测试检测重复concept_id"""
        concept1 = ConceptNode(
            concept_id="concept_bazi_dup_001",
            canonical_label_zh="概念1",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
        )
        concept2 = ConceptNode(
            concept_id="concept_bazi_dup_001",  # 重复ID
            canonical_label_zh="概念2",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_002", snippet_ids=[])],
        )
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=[concept1, concept2],
            edges=[],
        )
        
        report = validator.validate(graph)
        
        duplicate_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.DUPLICATE_CONCEPT_ID
        ]
        assert len(duplicate_issues) == 1
        assert duplicate_issues[0].severity == IssueSeverity.ERROR
    
    def test_detect_invalid_edge_refs(self, sample_metadata, validator):
        """测试检测无效边引用"""
        concept = ConceptNode(
            concept_id="concept_bazi_valid_001",
            canonical_label_zh="有效概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
        )
        
        # 边引用不存在的概念
        edge = SemanticEdge(
            edge_id="edge_invalid_001",
            source_concept_id="concept_bazi_valid_001",
            target_concept_id="concept_nonexistent_001",  # 不存在
            relation_type=RelationType.ENTAILS,
            confidence=0.8,
        )
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=[concept],
            edges=[edge],
        )
        
        report = validator.validate(graph)
        
        invalid_ref_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.INVALID_EDGE_CONCEPT_REF
        ]
        assert len(invalid_ref_issues) == 1
        assert invalid_ref_issues[0].severity == IssueSeverity.ERROR
    
    def test_detect_orphan_concepts(self, sample_metadata, validator):
        """测试检测孤立节点"""
        concept1 = ConceptNode(
            concept_id="concept_bazi_conn_001",
            canonical_label_zh="连接的概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
        )
        concept2 = ConceptNode(
            concept_id="concept_bazi_conn_002",
            canonical_label_zh="连接的概念2",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_002", snippet_ids=[])],
        )
        concept_orphan = ConceptNode(
            concept_id="concept_bazi_orphan_001",
            canonical_label_zh="孤立概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_003", snippet_ids=[])],
        )
        
        edge = SemanticEdge(
            edge_id="edge_conn_001",
            source_concept_id="concept_bazi_conn_001",
            target_concept_id="concept_bazi_conn_002",
            relation_type=RelationType.ENTAILS,
            confidence=0.8,
        )
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=[concept1, concept2, concept_orphan],
            edges=[edge],
        )
        
        report = validator.validate(graph)
        
        orphan_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.ORPHAN_CONCEPT
        ]
        assert len(orphan_issues) == 1
        assert orphan_issues[0].severity == IssueSeverity.WARNING
        assert "concept_bazi_orphan_001" in orphan_issues[0].affected_ids
    
    def test_save_report(self, connected_graph, validator):
        """测试保存验证报告"""
        report = validator.validate(connected_graph)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "report.json"
            saved_path = validator.save_report(report, output_path)
            
            assert saved_path.exists()
            import json
            with open(saved_path) as f:
                data = json.load(f)
            assert 'error_count' in data
            assert 'warning_count' in data


# ============ 循环依赖测试 ============

class TestCircularDependency:
    """循环依赖检测测试"""
    
    def test_detect_simple_cycle(self, sample_metadata, validator):
        """测试检测简单循环"""
        concepts = [
            ConceptNode(
                concept_id=f"concept_bazi_cycle_{i}",
                canonical_label_zh=f"循环概念{i}",
                divination_system=DivinationSystem.BAZI,
                dimension=Dimension.CAREER,
                source_nodes=[SourceNodeRef(book_id="test", node_id=f"n_{i}", snippet_ids=[])],
            )
            for i in range(3)
        ]
        
        # A -> B -> C -> A (循环)
        edges = [
            SemanticEdge(
                edge_id="edge_cycle_ab",
                source_concept_id="concept_bazi_cycle_0",
                target_concept_id="concept_bazi_cycle_1",
                relation_type=RelationType.ENTAILS,
                confidence=0.8,
            ),
            SemanticEdge(
                edge_id="edge_cycle_bc",
                source_concept_id="concept_bazi_cycle_1",
                target_concept_id="concept_bazi_cycle_2",
                relation_type=RelationType.ENTAILS,
                confidence=0.8,
            ),
            SemanticEdge(
                edge_id="edge_cycle_ca",
                source_concept_id="concept_bazi_cycle_2",
                target_concept_id="concept_bazi_cycle_0",
                relation_type=RelationType.ENTAILS,  # 形成循环
                confidence=0.8,
            ),
        ]
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=concepts,
            edges=edges,
        )
        
        report = validator.validate(graph)
        
        cycle_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.CIRCULAR_DEPENDENCY
        ]
        assert len(cycle_issues) == 1
        assert cycle_issues[0].severity == IssueSeverity.ERROR
    
    def test_no_cycle_in_bidirectional(self, sample_metadata, validator):
        """测试双向关系不算循环"""
        concepts = [
            ConceptNode(
                concept_id=f"concept_bazi_bidir_{i}",
                canonical_label_zh=f"双向概念{i}",
                divination_system=DivinationSystem.BAZI,
                dimension=Dimension.CAREER,
                source_nodes=[SourceNodeRef(book_id="test", node_id=f"n_{i}", snippet_ids=[])],
            )
            for i in range(2)
        ]
        
        # 同义关系是双向的，不应被检测为循环
        edge = SemanticEdge(
            edge_id="edge_synonym_001",
            source_concept_id="concept_bazi_bidir_0",
            target_concept_id="concept_bazi_bidir_1",
            relation_type=RelationType.SYNONYM,
            confidence=0.9,
        )
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=concepts,
            edges=[edge],
        )
        
        report = validator.validate(graph)
        
        cycle_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.CIRCULAR_DEPENDENCY
        ]
        assert len(cycle_issues) == 0


# ============ Property测试 ============

class TestPropertyValidation:
    """
    Property 13: Validation Reference Resolution
    Property 14: Circular Dependency Detection
    """
    
    def test_property_invalid_refs_detected(self, sample_metadata):
        """Property 13: 验证无效引用被检测"""
        validator = GraphValidator()
        
        concept = ConceptNode(
            concept_id="concept_bazi_prop13_001",
            canonical_label_zh="测试概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
        )
        
        # 引用不存在的概念
        invalid_edge = SemanticEdge(
            edge_id="edge_prop13_001",
            source_concept_id="concept_bazi_prop13_001",
            target_concept_id="concept_nonexistent_prop13",
            relation_type=RelationType.ENTAILS,
            confidence=0.8,
        )
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=[concept],
            edges=[invalid_edge],
        )
        
        report = validator.validate(graph)
        
        # Property 13: 无效引用应被检测为ERROR
        assert not report.is_valid()
        invalid_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.INVALID_EDGE_CONCEPT_REF
        ]
        assert len(invalid_issues) > 0
    
    def test_property_circular_detected_as_error(self, sample_metadata):
        """Property 14: 验证循环依赖被检测为ERROR"""
        validator = GraphValidator()
        
        concepts = [
            ConceptNode(
                concept_id=f"concept_bazi_prop14_{i}",
                canonical_label_zh=f"循环测试{i}",
                divination_system=DivinationSystem.BAZI,
                dimension=Dimension.CAREER,
                source_nodes=[SourceNodeRef(book_id="test", node_id=f"n_{i}", snippet_ids=[])],
            )
            for i in range(3)
        ]
        
        # 创建循环: 0 -> 1 -> 2 -> 0
        edges = [
            SemanticEdge(
                edge_id=f"edge_prop14_{i}",
                source_concept_id=f"concept_bazi_prop14_{i}",
                target_concept_id=f"concept_bazi_prop14_{(i+1)%3}",
                relation_type=RelationType.SPECIALIZES,
                confidence=0.8,
            )
            for i in range(3)
        ]
        
        graph = KnowledgeGraph(
            metadata=sample_metadata,
            concepts=concepts,
            edges=edges,
        )
        
        report = validator.validate(graph)
        
        # Property 14: 循环依赖应被检测为ERROR
        cycle_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.CIRCULAR_DEPENDENCY
        ]
        assert len(cycle_issues) > 0
        assert all(i.severity == IssueSeverity.ERROR for i in cycle_issues)
