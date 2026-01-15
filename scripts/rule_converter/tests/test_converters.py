"""
Tests for Converters

Requirement Refs: Req 4-7
"""

import pytest

from scripts.rule_converter.converters.condition_inferer import (
    ConditionInferer,
    LogicalExpression,
    RuleCondition,
)
from scripts.rule_converter.converters.metadata_mapper import (
    MetadataMapper,
    SourceMetadata,
)
from scripts.rule_converter.converters.result_builder import (
    ConfigRuleResult,
    ResultBuilder,
)
from scripts.rule_converter.converters.rule_id_generator import (
    RuleIdGenerator,
)
from scripts.rule_converter.loaders.factor_ontology import FactorDef, FactorOntology
from scripts.rule_converter.loaders.logic_chain_loader import LogicChainNode
from scripts.rule_converter.loaders.snippet_store import Snippet


# ===========================================================================
# Test ConditionInferer
# ===========================================================================

class TestRuleCondition:
    """测试 RuleCondition"""
    
    def test_to_dict(self):
        """测试转换为字典"""
        cond = RuleCondition(factor_id="day_master", operator="==", value=True)
        d = cond.to_dict()
        
        assert d["factor_id"] == "day_master"
        assert d["operator"] == "=="
        assert d["value"] is True
    
    def test_to_dict_without_value(self):
        """测试无值条件"""
        cond = RuleCondition(factor_id="day_master", operator="exists")
        d = cond.to_dict()
        
        assert d["factor_id"] == "day_master"
        assert d["operator"] == "exists"
        assert "value" not in d


class TestLogicalExpression:
    """测试 LogicalExpression"""
    
    def test_to_dict(self):
        """测试转换为字典"""
        expr = LogicalExpression(
            operator="AND",
            conditions=[
                RuleCondition(factor_id="f1", operator="exists"),
                RuleCondition(factor_id="f2", operator="==", value=True),
            ],
        )
        d = expr.to_dict()
        
        assert d["operator"] == "AND"
        assert len(d["conditions"]) == 2
        assert d["conditions"][0]["factor_id"] == "f1"


class TestConditionInferer:
    """测试 ConditionInferer"""
    
    @pytest.fixture
    def mock_ontology(self):
        """创建模拟因子本体"""
        ontology = FactorOntology.__new__(FactorOntology)
        ontology._factors = {
            "day_master_strength": FactorDef(
                id="day_master_strength",
                value_type="numeric",
                applicable_systems=["bazi"],
            ),
            "bazi_deling": FactorDef(
                id="bazi_deling",
                value_type="boolean",
                applicable_systems=["bazi"],
            ),
            "day_master": FactorDef(
                id="day_master",
                value_type="enum",
                value_range=["甲", "乙", "丙", "丁"],
                applicable_systems=["bazi"],
            ),
        }
        ontology._loaded = True
        return ontology
    
    def test_infer_no_factor_refs(self, mock_ontology):
        """测试无 factor_refs 的节点"""
        inferer = ConditionInferer(mock_ontology)
        node = LogicChainNode(node_id="test")
        
        result = inferer.infer(node)
        
        assert result.condition is None
        assert result.confidence == 0.0
    
    def test_infer_single_boolean_factor(self, mock_ontology):
        """测试单个 boolean 因子"""
        inferer = ConditionInferer(mock_ontology)
        node = LogicChainNode(
            node_id="test",
            factor_refs=["bazi_deling"],
        )
        
        result = inferer.infer(node)
        
        assert result.confidence == 0.8
        assert isinstance(result.condition, RuleCondition)
        assert result.condition.factor_id == "bazi_deling"
        assert result.condition.operator == "=="
        assert result.condition.value is True
    
    def test_infer_single_numeric_factor(self, mock_ontology):
        """测试单个 numeric 因子"""
        inferer = ConditionInferer(mock_ontology)
        node = LogicChainNode(
            node_id="test",
            factor_refs=["day_master_strength"],
        )
        
        result = inferer.infer(node)
        
        assert result.confidence == 0.8
        assert isinstance(result.condition, RuleCondition)
        assert result.condition.operator == "exists"  # 无法推断具体值
    
    def test_infer_multiple_factors(self, mock_ontology):
        """测试多个因子"""
        inferer = ConditionInferer(mock_ontology)
        node = LogicChainNode(
            node_id="test",
            factor_refs=["bazi_deling", "day_master_strength"],
        )
        
        result = inferer.infer(node)
        
        assert result.confidence == 0.7
        assert isinstance(result.condition, LogicalExpression)
        assert result.condition.operator == "AND"
        assert len(result.condition.conditions) == 2
    
    def test_infer_unknown_factor(self, mock_ontology):
        """测试未知因子"""
        inferer = ConditionInferer(mock_ontology)
        node = LogicChainNode(
            node_id="test",
            factor_refs=["unknown_factor"],
        )
        
        result = inferer.infer(node)
        
        assert result.confidence == 0.6  # 未认证因子降低置信度
        assert result.condition.operator == "exists"
    
    def test_infer_with_explicit_condition(self, mock_ontology):
        """测试有显式 condition 的节点"""
        inferer = ConditionInferer(mock_ontology)
        node = LogicChainNode(
            node_id="test",
            condition="日主为甲木",
            factor_refs=["day_master"],
        )
        
        result = inferer.infer(node)
        
        # 显式 condition 需要特殊处理
        assert result.confidence == 1.0


# ===========================================================================
# Test ResultBuilder
# ===========================================================================

class TestResultBuilder:
    """测试 ResultBuilder"""
    
    def test_infer_dimension_career(self):
        """测试推断事业维度"""
        builder = ResultBuilder()
        
        text = "正官透出，主有官运，适合仕途发展"
        dimension = builder._infer_dimension(text)
        
        assert dimension == "career"
    
    def test_infer_dimension_wealth(self):
        """测试推断财富维度"""
        builder = ResultBuilder()
        
        text = "财星得位，财运亨通"
        dimension = builder._infer_dimension(text)
        
        assert dimension == "wealth"
    
    def test_infer_dimension_default(self):
        """测试默认维度"""
        builder = ResultBuilder()
        
        text = "此为普通命格"
        dimension = builder._infer_dimension(text)
        
        assert dimension == "guidance"  # 默认
    
    def test_infer_level_daji(self):
        """测试推断大吉"""
        builder = ResultBuilder()
        
        text = "大贵之命，功名显达"
        level = builder._infer_level(text)
        
        assert level == "大吉"
    
    def test_infer_level_ji(self):
        """测试推断吉"""
        builder = ResultBuilder()
        
        text = "此命吉利，事业顺遂"
        level = builder._infer_level(text)
        
        assert level == "吉"
    
    def test_infer_level_xiong(self):
        """测试推断凶"""
        builder = ResultBuilder()
        
        text = "此命不利，多有损伤"
        level = builder._infer_level(text)
        
        assert level == "凶"
    
    def test_infer_level_default(self):
        """测试默认等级"""
        builder = ResultBuilder()
        
        text = "此为普通命格"
        level = builder._infer_level(text)
        
        assert level == "中等"
    
    def test_build_with_snippets(self):
        """测试完整构建"""
        builder = ResultBuilder()
        
        node = LogicChainNode(
            node_id="test",
            role="主干",
            summary="测试节点",
            factor_refs=["factor1", "factor2"],
        )
        
        snippets = [
            Snippet(
                snippet_id="ns_001",
                trigger="正官透出",
                factor_trigger="zheng_guan",
                role="主干",
                content="正官透出，主有官运，仕途顺利吉祥",  # 添加 "顺利" 和 "吉" 关键词
                source_ref="《测试》#1",
            ),
        ]
        
        result = builder.build(node, snippets)
        
        assert result.dimension == "career"
        assert result.level == "吉"  # 现在应该能检测到 "吉" 或 "顺"
        assert "官运" in result.conclusion_template_zh
        assert result.weight >= 2.0  # 主干角色权重
        assert "factor1" in result.evidence_factors
    
    def test_compute_weight(self):
        """测试权重计算"""
        builder = ResultBuilder()
        
        # 主干角色
        assert builder._compute_weight("主干", 1) == 2.0
        assert builder._compute_weight("主干", 3) == 2.2  # +0.2 bonus
        
        # 条件分支角色
        assert builder._compute_weight("条件分支", 1) == 1.2


# ===========================================================================
# Test MetadataMapper
# ===========================================================================

class TestMetadataMapper:
    """测试 MetadataMapper"""
    
    def test_parse_source_ref_format1(self):
        """测试格式1: 《书名·章节》#条目"""
        mapper = MetadataMapper()
        
        metadata = mapper.map("《滴天髓·通天论》#第1条", "node_001")
        
        assert metadata.book_id == "ditianshui"
        assert metadata.chapter == "通天论"
        assert "DTS" in metadata.l1_anchor
    
    def test_parse_source_ref_format2(self):
        """测试格式2: 《书名》章节#条目"""
        mapper = MetadataMapper()
        
        metadata = mapper.map("《滴天髓》通天论#2", "node_001")
        
        assert metadata.book_id == "ditianshui"
        assert "2" in metadata.l1_anchor
    
    def test_parse_source_ref_with_book_hint(self):
        """测试使用 book_id 提示"""
        mapper = MetadataMapper()
        
        metadata = mapper.map(None, "node_001", book_id_hint="滴天髓")
        
        assert "滴天髓" in metadata.book_id or metadata.book_id == "滴天髓"
    
    def test_l1_anchor_uniqueness(self):
        """测试 l1_anchor 唯一性"""
        mapper = MetadataMapper()
        
        m1 = mapper.map("《滴天髓·通天论》#第1条", "node_001")
        m2 = mapper.map("《滴天髓·通天论》#第1条", "node_002")
        
        assert m1.l1_anchor != m2.l1_anchor


# ===========================================================================
# Test RuleIdGenerator
# ===========================================================================

class TestRuleIdGenerator:
    """测试 RuleIdGenerator"""
    
    def test_generate_basic(self):
        """测试基本生成"""
        gen = RuleIdGenerator()
        
        rule_id = gen.generate("ditianshui", "career")
        
        assert rule_id.startswith("bazi_dts_career_")
        assert rule_id.endswith("_001")
    
    def test_generate_sequential(self):
        """测试顺序生成"""
        gen = RuleIdGenerator()
        
        id1 = gen.generate("ditianshui", "career")
        id2 = gen.generate("ditianshui", "career")
        id3 = gen.generate("ditianshui", "career")
        
        assert id1.endswith("_001")
        assert id2.endswith("_002")
        assert id3.endswith("_003")
    
    def test_uniqueness(self):
        """测试唯一性"""
        gen = RuleIdGenerator()
        
        ids = set()
        for _ in range(100):
            rule_id = gen.generate("ditianshui", "career")
            assert rule_id not in ids
            ids.add(rule_id)
    
    def test_is_unique(self):
        """测试唯一性检查"""
        gen = RuleIdGenerator()
        
        rule_id = gen.generate("ditianshui", "career")
        
        assert gen.is_unique(rule_id) is False
        assert gen.is_unique("some_other_id") is True
    
    def test_register(self):
        """测试注册已有ID"""
        gen = RuleIdGenerator()
        
        assert gen.register("existing_rule_001") is True
        assert gen.register("existing_rule_001") is False  # 已存在
    
    def test_get_stats(self):
        """测试获取统计"""
        gen = RuleIdGenerator()
        
        gen.generate("ditianshui", "career")
        gen.generate("ditianshui", "career")
        gen.generate("zipingzhenquan", "wealth")
        
        stats = gen.get_stats()
        
        assert stats["total_generated"] == 3
        assert "bazi_dts_career" in stats["by_prefix"]
        assert stats["by_prefix"]["bazi_dts_career"] == 2
