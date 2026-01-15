"""
ConceptNode模型测试

Feature: cross-book-knowledge-graph, Property 1: Schema Validation Consistency
Requirement Refs: Req 1.1, Req 1.3, Req 1.6
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    ConflictSummary,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
    SYSTEM_ALLOWED_DIMENSIONS,
    validate_dimension_for_system,
)


# ============ 基础测试 ============

class TestDivinationSystem:
    """DivinationSystem枚举测试"""
    
    def test_contains_seven_systems_plus_cross(self):
        """验证包含7个体系+cross_system"""
        systems = list(DivinationSystem)
        assert len(systems) == 8
        assert DivinationSystem.BAZI in systems
        assert DivinationSystem.ZIWEI in systems
        assert DivinationSystem.ASTRO in systems
        assert DivinationSystem.TAROT in systems
        assert DivinationSystem.DREAM in systems
        assert DivinationSystem.YIJING in systems
        assert DivinationSystem.PSYCHOLOGY in systems
        assert DivinationSystem.CROSS_SYSTEM in systems


class TestDimension:
    """Dimension枚举测试"""
    
    def test_contains_ten_dimensions(self):
        """验证包含10个维度"""
        dimensions = list(Dimension)
        assert len(dimensions) == 10
        assert Dimension.CAREER in dimensions
        assert Dimension.HEALTH in dimensions
        assert Dimension.MARRIAGE in dimensions
        assert Dimension.WEALTH in dimensions
        assert Dimension.PERSONALITY in dimensions
        assert Dimension.FORTUNE in dimensions
        assert Dimension.OMEN in dimensions
        assert Dimension.GUIDANCE in dimensions
        assert Dimension.UNCONSCIOUS in dimensions
        assert Dimension.GENERAL in dimensions


class TestSourceNodeRef:
    """SourceNodeRef模型测试"""
    
    def test_valid_creation(self):
        """有效数据创建成功"""
        ref = SourceNodeRef(
            book_id="滴天髓",
            node_id="node_001"
        )
        assert ref.book_id == "滴天髓"
        assert ref.node_id == "node_001"
        assert ref.snippet_ids == []
    
    def test_with_snippet_ids(self):
        """带snippet_ids创建"""
        ref = SourceNodeRef(
            book_id="子平真诠",
            node_id="node_002",
            snippet_ids=["snippet_001", "snippet_002"]
        )
        assert len(ref.snippet_ids) == 2


class TestConflictSummary:
    """ConflictSummary模型测试"""
    
    def test_default_values(self):
        """默认值正确"""
        summary = ConflictSummary()
        assert summary.conflict_count == 0
        assert summary.highest_authority_source is None
        assert summary.conflict_types == []
        assert summary.resolution_status == "unresolved"
    
    def test_negative_conflict_count_rejected(self):
        """负数冲突计数被拒绝"""
        with pytest.raises(ValidationError):
            ConflictSummary(conflict_count=-1)


class TestConceptNode:
    """ConceptNode模型测试"""
    
    @pytest.fixture
    def valid_concept_data(self):
        """有效的ConceptNode数据"""
        return {
            "concept_id": "concept_bazi_daymaster_strong",
            "canonical_label_zh": "日主强旺",
            "divination_system": DivinationSystem.BAZI,
            "source_nodes": [
                SourceNodeRef(book_id="滴天髓", node_id="node_001")
            ]
        }
    
    def test_valid_concept_creation(self, valid_concept_data):
        """有效数据实例化成功"""
        concept = ConceptNode(**valid_concept_data)
        assert concept.concept_id == "concept_bazi_daymaster_strong"
        assert concept.canonical_label_zh == "日主强旺"
        assert concept.divination_system == DivinationSystem.BAZI
        assert len(concept.source_nodes) == 1
    
    def test_invalid_concept_id_format_rejected(self, valid_concept_data):
        """无效concept_id格式被拒绝"""
        valid_concept_data["concept_id"] = "invalid_concept_id"
        with pytest.raises(ValidationError) as exc_info:
            ConceptNode(**valid_concept_data)
        assert "concept_id" in str(exc_info.value)
    
    def test_concept_id_must_start_with_concept(self, valid_concept_data):
        """concept_id必须以concept_开头"""
        valid_concept_data["concept_id"] = "node_bazi_test"
        with pytest.raises(ValidationError):
            ConceptNode(**valid_concept_data)
    
    def test_empty_source_nodes_rejected(self, valid_concept_data):
        """空source_nodes被拒绝"""
        valid_concept_data["source_nodes"] = []
        with pytest.raises(ValidationError) as exc_info:
            ConceptNode(**valid_concept_data)
        assert "source_nodes" in str(exc_info.value)
    
    def test_authority_score_out_of_range_rejected(self, valid_concept_data):
        """authority_score超出[0.0, 1.0]范围被拒绝"""
        # 测试大于1.0
        valid_concept_data["authority_score"] = 1.5
        with pytest.raises(ValidationError):
            ConceptNode(**valid_concept_data)
        
        # 测试小于0.0
        valid_concept_data["authority_score"] = -0.1
        with pytest.raises(ValidationError):
            ConceptNode(**valid_concept_data)
    
    def test_valid_authority_score_boundaries(self, valid_concept_data):
        """authority_score边界值有效"""
        valid_concept_data["authority_score"] = 0.0
        concept = ConceptNode(**valid_concept_data)
        assert concept.authority_score == 0.0
        
        valid_concept_data["authority_score"] = 1.0
        concept = ConceptNode(**valid_concept_data)
        assert concept.authority_score == 1.0
    
    def test_default_dimension_is_general(self, valid_concept_data):
        """默认dimension为GENERAL"""
        concept = ConceptNode(**valid_concept_data)
        assert concept.dimension == Dimension.GENERAL
    
    def test_valid_concept_id_prefixes(self):
        """测试各种有效的concept_id前缀"""
        valid_prefixes = [
            ("concept_star_ziwei", DivinationSystem.ZIWEI),
            ("concept_palace_career", DivinationSystem.ZIWEI),
            ("concept_bazi_daymaster", DivinationSystem.BAZI),
            ("concept_gua_qian", DivinationSystem.YIJING),
            ("concept_card_fool", DivinationSystem.TAROT),
            ("concept_symbol_water", DivinationSystem.DREAM),
            ("concept_sign_aries", DivinationSystem.ASTRO),
            ("concept_aspect_conjunction", DivinationSystem.ASTRO),
            ("concept_general_fortune", DivinationSystem.CROSS_SYSTEM),
            ("concept_cross_wealth", DivinationSystem.CROSS_SYSTEM),
        ]
        
        for concept_id, system in valid_prefixes:
            concept = ConceptNode(
                concept_id=concept_id,
                canonical_label_zh="测试概念",
                divination_system=system,
                source_nodes=[SourceNodeRef(book_id="test", node_id="node_001")]
            )
            assert concept.concept_id == concept_id
    
    def test_optional_fields(self, valid_concept_data):
        """可选字段测试"""
        concept = ConceptNode(**valid_concept_data)
        assert concept.canonical_label_en is None
        assert concept.subdimension is None
        assert concept.conflict_summary is None
        assert concept.aggregation_rule_id is None
    
    def test_full_concept_with_all_fields(self, valid_concept_data):
        """包含所有字段的完整ConceptNode"""
        full_data = {
            **valid_concept_data,
            "canonical_label_en": "Strong Day Master",
            "dimension": Dimension.PERSONALITY,
            "subdimension": "本命特质",
            "factor_refs": ["bazi_daymaster", "bazi_strength"],
            "authority_score": 0.9,
            "conflict_summary": ConflictSummary(
                conflict_count=2,
                highest_authority_source="滴天髓",
                conflict_types=["direct_contradiction"],
                resolution_status="authority_based"
            ),
            "alignment_method": "text_similarity",
            "aggregation_rule_id": "rule_001",
            "confidence": 0.95,
        }
        concept = ConceptNode(**full_data)
        assert concept.canonical_label_en == "Strong Day Master"
        assert concept.dimension == Dimension.PERSONALITY
        assert concept.subdimension == "本命特质"
        assert len(concept.factor_refs) == 2
        assert concept.authority_score == 0.9
        assert concept.conflict_summary.conflict_count == 2


class TestSystemDimensionConstraints:
    """体系-维度约束测试"""
    
    def test_bazi_allowed_dimensions(self):
        """八字允许的维度"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS[DivinationSystem.BAZI]
        assert Dimension.CAREER in allowed
        assert Dimension.FORTUNE in allowed
        assert Dimension.OMEN not in allowed
        assert Dimension.UNCONSCIOUS not in allowed
    
    def test_dream_allowed_dimensions(self):
        """解梦允许的维度"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS[DivinationSystem.DREAM]
        assert Dimension.OMEN in allowed
        assert Dimension.UNCONSCIOUS in allowed
        assert Dimension.GUIDANCE in allowed
        assert Dimension.GENERAL in allowed
        assert Dimension.CAREER not in allowed
    
    def test_tarot_allowed_dimensions(self):
        """塔罗允许的维度"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS[DivinationSystem.TAROT]
        assert Dimension.GUIDANCE in allowed
        assert Dimension.FORTUNE in allowed
        assert Dimension.GENERAL in allowed
        assert len(allowed) == 3
    
    def test_cross_system_allows_all_dimensions(self):
        """跨体系允许所有维度"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS[DivinationSystem.CROSS_SYSTEM]
        assert len(allowed) == len(list(Dimension))
    
    def test_validate_dimension_for_system_function(self):
        """validate_dimension_for_system函数测试"""
        assert validate_dimension_for_system(DivinationSystem.BAZI, Dimension.CAREER) is True
        assert validate_dimension_for_system(DivinationSystem.DREAM, Dimension.OMEN) is True
        assert validate_dimension_for_system(DivinationSystem.BAZI, Dimension.OMEN) is False
        assert validate_dimension_for_system(DivinationSystem.CROSS_SYSTEM, Dimension.OMEN) is True


# ============ Property-Based Testing (hypothesis) ============

class TestConceptNodePropertyBased:
    """
    Property 1: Schema Validation Consistency
    使用hypothesis进行属性测试
    """
    
    @settings(max_examples=100)
    @given(
        authority_score=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
        confidence=st.floats(min_value=0.0, max_value=1.0, allow_nan=False),
    )
    def test_valid_scores_accepted(self, authority_score, confidence):
        """有效的分数值应被接受"""
        concept = ConceptNode(
            concept_id="concept_bazi_test",
            canonical_label_zh="测试",
            divination_system=DivinationSystem.BAZI,
            source_nodes=[SourceNodeRef(book_id="test", node_id="node_001")],
            authority_score=authority_score,
            confidence=confidence,
        )
        assert 0.0 <= concept.authority_score <= 1.0
        assert 0.0 <= concept.confidence <= 1.0
    
    @settings(max_examples=100)
    @given(
        invalid_score=st.floats().filter(lambda x: x < 0.0 or x > 1.0)
    )
    def test_invalid_authority_score_rejected(self, invalid_score):
        """无效的authority_score应被拒绝"""
        if not (invalid_score != invalid_score):  # 排除NaN
            with pytest.raises(ValidationError):
                ConceptNode(
                    concept_id="concept_bazi_test",
                    canonical_label_zh="测试",
                    divination_system=DivinationSystem.BAZI,
                    source_nodes=[SourceNodeRef(book_id="test", node_id="node_001")],
                    authority_score=invalid_score,
                )
    
    @settings(max_examples=100)
    @given(
        system=st.sampled_from(list(DivinationSystem)),
        dimension=st.sampled_from(list(Dimension)),
    )
    def test_system_dimension_consistency(self, system, dimension):
        """验证体系-维度一致性检查函数"""
        result = validate_dimension_for_system(system, dimension)
        assert isinstance(result, bool)
        
        # 跨体系应该允许所有维度
        if system == DivinationSystem.CROSS_SYSTEM:
            assert result is True
