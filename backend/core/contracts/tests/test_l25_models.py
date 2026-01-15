"""
Tests for L2.5 Bridge Layer Models

对照文档: docs/数据契约_Schema定义规范_v1.md §1.5
"""

import pytest
from pydantic import ValidationError

from backend.core.contracts.l25_models import (
    RELATION_ID_PATTERN,
    EVIDENCE_ID_PATTERN,
    CONCEPT_ID_PATTERN,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
    ConfigRelation,
    EvidenceChainEntry,
    CrossSystemMapping,
)
from backend.core.contracts.base import SourceMetadata


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def sample_metadata():
    return SourceMetadata(
        book_id="ditianshui",
        chapter="通神论",
        l1_anchor="DTS_L1_001"
    )


# =============================================================================
# Enum Tests
# =============================================================================

class TestRelationType:
    """RelationType 枚举测试"""
    
    def test_enum_count(self):
        """验证枚举值数量"""
        assert len(RelationType) == 8
    
    def test_enum_values(self):
        """验证所有枚举值存在"""
        expected = [
            "wuxing_shengke",
            "dizhi_interaction", 
            "ten_god_relation",
            "planet_house",
            "planet_aspect",
            "dream_symbol_relation",
            "psych_archetype_relation",
            "cross_system",
        ]
        actual = [e.value for e in RelationType]
        assert set(actual) == set(expected)


class TestEffectDirection:
    """EffectDirection 枚举测试"""
    
    def test_enum_count(self):
        """验证枚举值数量"""
        assert len(EffectDirection) == 5
    
    def test_enum_values(self):
        """验证所有枚举值存在（中文值）"""
        expected = ["增益", "损害", "限制", "中性", "混合"]
        actual = [e.value for e in EffectDirection]
        assert set(actual) == set(expected)


class TestConfidenceLevel:
    """ConfidenceLevel 枚举测试"""
    
    def test_enum_count(self):
        """验证枚举值数量"""
        assert len(ConfidenceLevel) == 3
    
    def test_enum_values(self):
        """验证所有枚举值存在（中文值）"""
        expected = ["高", "中", "低"]
        actual = [e.value for e in ConfidenceLevel]
        assert set(actual) == set(expected)


# =============================================================================
# ConfigRelation Tests
# =============================================================================

class TestConfigRelation:
    """ConfigRelation 模型测试"""
    
    def test_valid_instance(self, sample_metadata):
        """测试有效实例创建"""
        relation = ConfigRelation(
            relation_id="rel_dts_001",
            relation_type=RelationType.WUXING_SHENGKE,
            factor_a="day_master_jia",
            factor_b="element_fire",
            relation_nature="生",
            effect_direction=EffectDirection.BENEFICIAL,
            source_ref="《滴天髓》#甲木条",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="bazi_semantic"
        )
        assert relation.relation_id == "rel_dts_001"
        assert relation.relation_type == RelationType.WUXING_SHENGKE
        assert relation.effect_direction == EffectDirection.BENEFICIAL
    
    def test_relation_id_regex_valid(self, sample_metadata):
        """测试有效的 relation_id 格式"""
        valid_ids = ["rel_dts_001", "rel_zpzq_123", "rel_inner_sky_999"]
        for rid in valid_ids:
            relation = ConfigRelation(
                relation_id=rid,
                relation_type=RelationType.WUXING_SHENGKE,
                factor_a="a",
                factor_b="b",
                relation_nature="生",
                effect_direction=EffectDirection.BENEFICIAL,
                source_ref="test",
                metadata=sample_metadata,
                version="1.0.0",
                engine_id="test"
            )
            assert relation.relation_id == rid
    
    def test_relation_id_regex_invalid(self, sample_metadata):
        """测试无效的 relation_id 格式"""
        invalid_ids = ["dts_001", "rel_DTS_001", "rel_dts_1", "rel-dts-001"]
        for rid in invalid_ids:
            with pytest.raises(ValidationError):
                ConfigRelation(
                    relation_id=rid,
                    relation_type=RelationType.WUXING_SHENGKE,
                    factor_a="a",
                    factor_b="b",
                    relation_nature="生",
                    effect_direction=EffectDirection.BENEFICIAL,
                    source_ref="test",
                    metadata=sample_metadata,
                    version="1.0.0",
                    engine_id="test"
                )
    
    def test_optional_condition_constraint(self, sample_metadata):
        """测试可选的 condition_constraint"""
        relation = ConfigRelation(
            relation_id="rel_dts_001",
            relation_type=RelationType.WUXING_SHENGKE,
            factor_a="a",
            factor_b="b",
            relation_nature="生",
            condition_constraint="春季限定",
            effect_direction=EffectDirection.BENEFICIAL,
            source_ref="test",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="test"
        )
        assert relation.condition_constraint == "春季限定"


# =============================================================================
# EvidenceChainEntry Tests
# =============================================================================

class TestEvidenceChainEntry:
    """EvidenceChainEntry 模型测试"""
    
    def test_valid_instance(self, sample_metadata):
        """测试有效实例创建"""
        entry = EvidenceChainEntry(
            evidence_id="evi_dts_001",
            l1_anchor="甲木参天，脱胎要火",
            involved_factors=["day_master_jia", "element_fire"],
            reasoning_step="甲木刚健需火泄秀",
            conclusion_direction="吉",
            confidence=ConfidenceLevel.HIGH,
            can_generate_rule=True,
            target_rule_id="rule_jia_needs_fire",
            source_ref="《滴天髓》#通神论",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="bazi_semantic"
        )
        assert entry.evidence_id == "evi_dts_001"
        assert entry.confidence == ConfidenceLevel.HIGH
        assert entry.can_generate_rule is True
    
    def test_evidence_id_regex_valid(self, sample_metadata):
        """测试有效的 evidence_id 格式"""
        valid_ids = ["evi_dts_001", "evi_zpzq_123", "evi_inner_sky_999"]
        for eid in valid_ids:
            entry = EvidenceChainEntry(
                evidence_id=eid,
                l1_anchor="test",
                involved_factors=["a"],
                reasoning_step="test",
                conclusion_direction="吉",
                confidence=ConfidenceLevel.HIGH,
                can_generate_rule=False,
                source_ref="test",
                metadata=sample_metadata,
                version="1.0.0",
                engine_id="test"
            )
            assert entry.evidence_id == eid
    
    def test_evidence_id_regex_invalid(self, sample_metadata):
        """测试无效的 evidence_id 格式"""
        invalid_ids = ["dts_001", "evi_DTS_001", "evi_dts_1", "evi-dts-001"]
        for eid in invalid_ids:
            with pytest.raises(ValidationError):
                EvidenceChainEntry(
                    evidence_id=eid,
                    l1_anchor="test",
                    involved_factors=["a"],
                    reasoning_step="test",
                    conclusion_direction="吉",
                    confidence=ConfidenceLevel.HIGH,
                    can_generate_rule=False,
                    source_ref="test",
                    metadata=sample_metadata,
                    version="1.0.0",
                    engine_id="test"
                )
    
    def test_optional_target_rule_id(self, sample_metadata):
        """测试可选的 target_rule_id"""
        entry = EvidenceChainEntry(
            evidence_id="evi_dts_001",
            l1_anchor="test",
            involved_factors=["a"],
            reasoning_step="test",
            conclusion_direction="吉",
            confidence=ConfidenceLevel.HIGH,
            can_generate_rule=False,
            target_rule_id=None,
            source_ref="test",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="test"
        )
        assert entry.target_rule_id is None


# =============================================================================
# CrossSystemMapping Tests
# =============================================================================

class TestCrossSystemMapping:
    """CrossSystemMapping 模型测试"""
    
    def test_valid_instance_two_systems(self, sample_metadata):
        """测试有效实例创建（两个体系）"""
        mapping = CrossSystemMapping(
            concept_id="concept_authority_pressure",
            common_semantics="权威压力",
            bazi_factors=["ten_god_qisha"],
            astro_factors=["saturn_square_sun"],
            metadata=sample_metadata,
            version="1.0.0"
        )
        assert mapping.concept_id == "concept_authority_pressure"
        assert len(mapping.bazi_factors) == 1
        assert len(mapping.astro_factors) == 1
    
    def test_valid_instance_multiple_systems(self, sample_metadata):
        """测试有效实例创建（多个体系）"""
        mapping = CrossSystemMapping(
            concept_id="concept_transformation",
            common_semantics="转变与蜕变",
            bazi_factors=["ten_god_qisha"],
            astro_factors=["pluto_conjunct_sun"],
            dream_factors=["dream_theme_death"],
            psych_factors=["psych_archetype_shadow"],
            metadata=sample_metadata,
            version="1.0.0"
        )
        assert len(mapping.bazi_factors) == 1
        assert len(mapping.astro_factors) == 1
        assert len(mapping.dream_factors) == 1
        assert len(mapping.psych_factors) == 1
    
    def test_concept_id_regex_valid(self, sample_metadata):
        """测试有效的 concept_id 格式"""
        valid_ids = ["concept_authority", "concept_authority_pressure", "concept_a1"]
        for cid in valid_ids:
            mapping = CrossSystemMapping(
                concept_id=cid,
                common_semantics="test",
                bazi_factors=["a"],
                astro_factors=["b"],
                metadata=sample_metadata,
                version="1.0.0"
            )
            assert mapping.concept_id == cid
    
    def test_concept_id_regex_invalid(self, sample_metadata):
        """测试无效的 concept_id 格式"""
        invalid_ids = ["authority", "Concept_authority", "concept-authority"]
        for cid in invalid_ids:
            with pytest.raises(ValidationError):
                CrossSystemMapping(
                    concept_id=cid,
                    common_semantics="test",
                    bazi_factors=["a"],
                    astro_factors=["b"],
                    metadata=sample_metadata,
                    version="1.0.0"
                )
    
    def test_at_least_two_systems_validation(self, sample_metadata):
        """测试至少两个体系的校验"""
        # 只有一个体系应该失败
        with pytest.raises(ValidationError) as exc_info:
            CrossSystemMapping(
                concept_id="concept_test",
                common_semantics="test",
                bazi_factors=["a"],
                metadata=sample_metadata,
                version="1.0.0"
            )
        assert "至少两个体系" in str(exc_info.value)
    
    def test_zero_systems_validation(self, sample_metadata):
        """测试零个体系的校验"""
        with pytest.raises(ValidationError) as exc_info:
            CrossSystemMapping(
                concept_id="concept_test",
                common_semantics="test",
                metadata=sample_metadata,
                version="1.0.0"
            )
        assert "至少两个体系" in str(exc_info.value)
    
    def test_optional_notes(self, sample_metadata):
        """测试可选的 notes"""
        mapping = CrossSystemMapping(
            concept_id="concept_test",
            common_semantics="test",
            bazi_factors=["a"],
            astro_factors=["b"],
            notes="这是备注",
            metadata=sample_metadata,
            version="1.0.0"
        )
        assert mapping.notes == "这是备注"
