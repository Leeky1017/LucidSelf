"""
SemanticEdge模型测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.2, Req 1.4, Req 3.1
"""

import pytest
from pydantic import ValidationError

from scripts.knowledge_graph_builder.models.edge import (
    ConflictType,
    RelationType,
    SemanticEdge,
    BIDIRECTIONAL_RELATIONS,
    create_edge_id,
)


class TestRelationType:
    """RelationType枚举测试"""
    
    def test_contains_seven_relation_types(self):
        """验证包含7种关系类型"""
        relations = list(RelationType)
        assert len(relations) == 7
        assert RelationType.SYNONYM in relations
        assert RelationType.ENTAILS in relations
        assert RelationType.CONFLICTS_WITH in relations
        assert RelationType.COMPLEMENTS in relations
        assert RelationType.SPECIALIZES in relations
        assert RelationType.GENERALIZES in relations
        assert RelationType.CROSS_SYSTEM_EQUIVALENT in relations


class TestConflictType:
    """ConflictType枚举测试"""
    
    def test_contains_four_conflict_types(self):
        """验证包含4种冲突类型"""
        conflicts = list(ConflictType)
        assert len(conflicts) == 4
        assert ConflictType.DIRECT_CONTRADICTION in conflicts
        assert ConflictType.CONDITIONAL_EXCEPTION in conflicts
        assert ConflictType.SCOPE_DIFFERENCE in conflicts
        assert ConflictType.CROSS_SYSTEM_DIVERGENCE in conflicts


class TestSemanticEdge:
    """SemanticEdge模型测试"""
    
    @pytest.fixture
    def valid_edge_data(self):
        """有效的SemanticEdge数据"""
        return {
            "edge_id": "edge_bazi_concept1_concept2_entails",
            "source_concept_id": "concept_bazi_daymaster_strong",
            "target_concept_id": "concept_bazi_wealth_favorable",
            "relation_type": RelationType.ENTAILS,
        }
    
    def test_valid_edge_creation(self, valid_edge_data):
        """有效数据实例化成功"""
        edge = SemanticEdge(**valid_edge_data)
        assert edge.edge_id == "edge_bazi_concept1_concept2_entails"
        assert edge.source_concept_id == "concept_bazi_daymaster_strong"
        assert edge.target_concept_id == "concept_bazi_wealth_favorable"
        assert edge.relation_type == RelationType.ENTAILS
    
    def test_invalid_edge_id_format_rejected(self, valid_edge_data):
        """无效edge_id格式被拒绝"""
        valid_edge_data["edge_id"] = "invalid_edge_id"
        with pytest.raises(ValidationError) as exc_info:
            SemanticEdge(**valid_edge_data)
        assert "edge_id" in str(exc_info.value)
    
    def test_invalid_concept_id_format_rejected(self, valid_edge_data):
        """无效concept_id格式被拒绝"""
        valid_edge_data["source_concept_id"] = "invalid_concept"
        with pytest.raises(ValidationError):
            SemanticEdge(**valid_edge_data)
    
    def test_self_loop_rejected(self, valid_edge_data):
        """自环被拒绝"""
        valid_edge_data["target_concept_id"] = valid_edge_data["source_concept_id"]
        with pytest.raises(ValidationError) as exc_info:
            SemanticEdge(**valid_edge_data)
        assert "cannot be the same" in str(exc_info.value)
    
    def test_confidence_out_of_range_rejected(self, valid_edge_data):
        """confidence超出[0.0, 1.0]范围被拒绝"""
        valid_edge_data["confidence"] = 1.5
        with pytest.raises(ValidationError):
            SemanticEdge(**valid_edge_data)
        
        valid_edge_data["confidence"] = -0.1
        with pytest.raises(ValidationError):
            SemanticEdge(**valid_edge_data)
    
    def test_conflicts_with_requires_conflict_type(self, valid_edge_data):
        """conflicts_with关系必须有conflict_type"""
        valid_edge_data["relation_type"] = RelationType.CONFLICTS_WITH
        with pytest.raises(ValidationError) as exc_info:
            SemanticEdge(**valid_edge_data)
        assert "conflict_type is required" in str(exc_info.value)
    
    def test_conflicts_with_with_conflict_type(self, valid_edge_data):
        """conflicts_with关系带conflict_type创建成功"""
        valid_edge_data["relation_type"] = RelationType.CONFLICTS_WITH
        valid_edge_data["conflict_type"] = ConflictType.DIRECT_CONTRADICTION
        edge = SemanticEdge(**valid_edge_data)
        assert edge.relation_type == RelationType.CONFLICTS_WITH
        assert edge.conflict_type == ConflictType.DIRECT_CONTRADICTION
    
    def test_default_values(self, valid_edge_data):
        """默认值正确"""
        edge = SemanticEdge(**valid_edge_data)
        assert edge.confidence == 0.8
        assert edge.evidence_refs == []
        assert edge.bidirectional is False
        assert edge.conflict_type is None
    
    def test_synonym_is_bidirectional(self, valid_edge_data):
        """SYNONYM关系自动设置为双向"""
        valid_edge_data["relation_type"] = RelationType.SYNONYM
        edge = SemanticEdge(**valid_edge_data)
        assert edge.bidirectional is True
        assert edge.is_bidirectional() is True
    
    def test_cross_system_equivalent_is_bidirectional(self, valid_edge_data):
        """CROSS_SYSTEM_EQUIVALENT关系自动设置为双向"""
        valid_edge_data["relation_type"] = RelationType.CROSS_SYSTEM_EQUIVALENT
        edge = SemanticEdge(**valid_edge_data)
        assert edge.bidirectional is True
        assert edge.is_bidirectional() is True
    
    def test_entails_is_not_bidirectional(self, valid_edge_data):
        """ENTAILS关系是单向的"""
        edge = SemanticEdge(**valid_edge_data)
        assert edge.bidirectional is False
        assert edge.is_bidirectional() is False
    
    def test_get_reverse_edge_for_bidirectional(self, valid_edge_data):
        """双向关系可获取反向边"""
        valid_edge_data["relation_type"] = RelationType.SYNONYM
        edge = SemanticEdge(**valid_edge_data)
        reverse = edge.get_reverse_edge()
        
        assert reverse is not None
        assert reverse.source_concept_id == edge.target_concept_id
        assert reverse.target_concept_id == edge.source_concept_id
        assert reverse.relation_type == edge.relation_type
    
    def test_get_reverse_edge_for_unidirectional(self, valid_edge_data):
        """单向关系返回None"""
        edge = SemanticEdge(**valid_edge_data)
        reverse = edge.get_reverse_edge()
        assert reverse is None
    
    def test_evidence_refs(self, valid_edge_data):
        """evidence_refs测试"""
        valid_edge_data["evidence_refs"] = ["evidence_001", "evidence_002"]
        edge = SemanticEdge(**valid_edge_data)
        assert len(edge.evidence_refs) == 2


class TestBidirectionalRelations:
    """双向关系常量测试"""
    
    def test_bidirectional_relations_set(self):
        """验证双向关系集合正确"""
        assert RelationType.SYNONYM in BIDIRECTIONAL_RELATIONS
        assert RelationType.CROSS_SYSTEM_EQUIVALENT in BIDIRECTIONAL_RELATIONS
        assert len(BIDIRECTIONAL_RELATIONS) == 2
        
        # 确认其他关系不在集合中
        assert RelationType.ENTAILS not in BIDIRECTIONAL_RELATIONS
        assert RelationType.CONFLICTS_WITH not in BIDIRECTIONAL_RELATIONS


class TestCreateEdgeId:
    """create_edge_id函数测试"""
    
    def test_create_edge_id_basic(self):
        """基本edge_id生成"""
        edge_id = create_edge_id(
            "concept_bazi_daymaster",
            "concept_bazi_wealth",
            RelationType.ENTAILS
        )
        assert edge_id.startswith("edge_")
        assert "bazi_daymaster" in edge_id
        assert "bazi_wealth" in edge_id
    
    def test_create_edge_id_format(self):
        """edge_id格式正确"""
        edge_id = create_edge_id(
            "concept_a",
            "concept_b",
            RelationType.SYNONYM
        )
        # 应该可以用于SemanticEdge
        edge = SemanticEdge(
            edge_id=edge_id,
            source_concept_id="concept_a",
            target_concept_id="concept_b",
            relation_type=RelationType.SYNONYM
        )
        assert edge.edge_id == edge_id
