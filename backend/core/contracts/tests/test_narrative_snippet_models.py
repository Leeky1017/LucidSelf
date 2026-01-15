"""
Tests for Narrative Snippet Models

对照文档: docs/数据契约_Schema定义规范_v1.md §3.4-3.6
"""

import pytest
from pydantic import ValidationError

from backend.core.contracts.narrative_snippet_models import (
    SnippetRole,
    ConflictResolutionStrategy,
    NarrativeOrderStrategy,
    NarrativeSnippet,
    LogicNode,
    LogicEdge,
    LogicChain,
    AssemblyProtocol,
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

class TestSnippetRole:
    """SnippetRole 枚举测试"""
    
    def test_enum_count(self):
        """验证枚举值数量（仅允许5个）"""
        assert len(SnippetRole) == 5
    
    def test_enum_values(self):
        """验证所有枚举值存在（中文值）"""
        expected = ["主干", "主干依赖", "条件分支", "例外处理", "总结"]
        actual = [e.value for e in SnippetRole]
        assert set(actual) == set(expected)


class TestConflictResolutionStrategy:
    """ConflictResolutionStrategy 枚举测试"""
    
    def test_enum_count(self):
        """验证枚举值数量"""
        assert len(ConflictResolutionStrategy) == 5
    
    def test_enum_values(self):
        """验证所有枚举值存在"""
        expected = ["priority_based", "weight_based", "confidence_based", "source_based", "merge"]
        actual = [e.value for e in ConflictResolutionStrategy]
        assert set(actual) == set(expected)


class TestNarrativeOrderStrategy:
    """NarrativeOrderStrategy 枚举测试"""
    
    def test_enum_count(self):
        """验证枚举值数量"""
        assert len(NarrativeOrderStrategy) == 4
    
    def test_enum_values(self):
        """验证所有枚举值存在"""
        expected = ["logic_chain", "confidence_desc", "dimension_group", "chronological"]
        actual = [e.value for e in NarrativeOrderStrategy]
        assert set(actual) == set(expected)


# =============================================================================
# NarrativeSnippet Tests
# =============================================================================

class TestNarrativeSnippet:
    """NarrativeSnippet 模型测试"""
    
    def test_valid_instance(self, sample_metadata):
        """测试有效实例创建"""
        snippet = NarrativeSnippet(
            snippet_id="dts_jia_spring_001",
            trigger_condition="day_master=甲 AND month∈[寅,卯]",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="甲木生于春，得时得令，如参天大树。",
            source_ref="《滴天髓》#通神论#L23",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="bazi_semantic"
        )
        assert snippet.snippet_id == "dts_jia_spring_001"
        assert snippet.role == SnippetRole.MAIN
        assert snippet.primary_lang == "zh-CN"
    
    def test_snippet_id_regex_valid(self, sample_metadata):
        """测试有效的 snippet_id 格式"""
        valid_ids = ["dts_jia_001", "zpzq_career_123", "inner_sky_sun_999"]
        for sid in valid_ids:
            snippet = NarrativeSnippet(
                snippet_id=sid,
                trigger_condition="test",
                role=SnippetRole.MAIN,
                primary_lang="zh-CN",
                snippet_text="这是一段测试文本",
                source_ref="test",
                metadata=sample_metadata,
                version="1.0.0",
                engine_id="test"
            )
            assert snippet.snippet_id == sid
    
    def test_snippet_id_regex_invalid(self, sample_metadata):
        """测试无效的 snippet_id 格式"""
        invalid_ids = ["DTS_jia_001", "dts_jia", "dts-jia-001", "001_dts"]
        for sid in invalid_ids:
            with pytest.raises(ValidationError):
                NarrativeSnippet(
                    snippet_id=sid,
                    trigger_condition="test",
                    role=SnippetRole.MAIN,
                    primary_lang="zh-CN",
                    snippet_text="这是一段测试文本",
                    source_ref="test",
                    metadata=sample_metadata,
                    version="1.0.0",
                    engine_id="test"
                )
    
    def test_snippet_text_min_length(self, sample_metadata):
        """测试 snippet_text 最小长度（5字符）"""
        with pytest.raises(ValidationError):
            NarrativeSnippet(
                snippet_id="dts_jia_001",
                trigger_condition="test",
                role=SnippetRole.MAIN,
                primary_lang="zh-CN",
                snippet_text="1234",  # 4 chars, should fail
                source_ref="test",
                metadata=sample_metadata,
                version="1.0.0",
                engine_id="test"
            )
    
    def test_snippet_text_max_length(self, sample_metadata):
        """测试 snippet_text 最大长度（200字符）"""
        with pytest.raises(ValidationError):
            NarrativeSnippet(
                snippet_id="dts_jia_001",
                trigger_condition="test",
                role=SnippetRole.MAIN,
                primary_lang="zh-CN",
                snippet_text="x" * 201,  # 201 chars, should fail
                source_ref="test",
                metadata=sample_metadata,
                version="1.0.0",
                engine_id="test"
            )
    
    def test_snippet_text_boundary_valid(self, sample_metadata):
        """测试 snippet_text 边界值（5和200字符）"""
        # 5 chars - should pass
        snippet_5 = NarrativeSnippet(
            snippet_id="dts_jia_001",
            trigger_condition="test",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="12345",
            source_ref="test",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="test"
        )
        assert len(snippet_5.snippet_text) == 5
        
        # 200 chars - should pass
        snippet_200 = NarrativeSnippet(
            snippet_id="dts_jia_002",
            trigger_condition="test",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="x" * 200,
            source_ref="test",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="test"
        )
        assert len(snippet_200.snippet_text) == 200
    
    def test_primary_lang_enum(self, sample_metadata):
        """测试 primary_lang 枚举值"""
        # zh-CN
        snippet_zh = NarrativeSnippet(
            snippet_id="dts_jia_001",
            trigger_condition="test",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="中文测试文本",
            source_ref="test",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="test"
        )
        assert snippet_zh.primary_lang == "zh-CN"
        
        # en-US
        snippet_en = NarrativeSnippet(
            snippet_id="inner_sky_001",
            trigger_condition="test",
            role=SnippetRole.MAIN,
            primary_lang="en-US",
            snippet_text="English test text",
            source_ref="test",
            metadata=sample_metadata,
            version="1.0.0",
            engine_id="test"
        )
        assert snippet_en.primary_lang == "en-US"


# =============================================================================
# LogicNode Tests
# =============================================================================

class TestLogicNode:
    """LogicNode 模型测试"""
    
    def test_valid_instance(self):
        """测试有效实例创建"""
        node = LogicNode(
            node_id="n1",
            snippet_ids=["dts_jia_001", "dts_jia_002"],
            role=SnippetRole.MAIN,
            summary="甲木基本特性"
        )
        assert node.node_id == "n1"
        assert len(node.snippet_ids) == 2
        assert node.condition is None
    
    def test_optional_condition(self):
        """测试可选的 condition"""
        node = LogicNode(
            node_id="n1",
            snippet_ids=["dts_jia_001"],
            role=SnippetRole.CONDITIONAL,
            condition="season=spring",
            summary="春季条件"
        )
        assert node.condition == "season=spring"


# =============================================================================
# LogicEdge Tests
# =============================================================================

class TestLogicEdge:
    """LogicEdge 模型测试"""
    
    def test_valid_instance(self):
        """测试有效实例创建"""
        edge = LogicEdge(
            from_node="n1",
            to_node="n2",
            relation="leads_to"
        )
        assert edge.from_node == "n1"
        assert edge.to_node == "n2"
        assert edge.relation == "leads_to"
    
    def test_relation_enum_values(self):
        """测试 relation 枚举值"""
        valid_relations = ["depends_on", "leads_to", "conflicts_with", "supports"]
        for rel in valid_relations:
            edge = LogicEdge(from_node="n1", to_node="n2", relation=rel)
            assert edge.relation == rel
    
    def test_relation_invalid(self):
        """测试无效的 relation 值"""
        with pytest.raises(ValidationError):
            LogicEdge(from_node="n1", to_node="n2", relation="invalid_relation")


# =============================================================================
# LogicChain Tests
# =============================================================================

class TestLogicChain:
    """LogicChain 模型测试"""
    
    def test_valid_instance(self, sample_metadata):
        """测试有效实例创建"""
        chain = LogicChain(
            chain_id="chain_ditianshui",
            book_id="ditianshui",
            nodes=[
                LogicNode(node_id="n1", snippet_ids=["dts_001"], role=SnippetRole.MAIN, summary="主干"),
                LogicNode(node_id="n2", snippet_ids=["dts_002"], role=SnippetRole.CONDITIONAL, summary="条件"),
            ],
            edges=[
                LogicEdge(from_node="n1", to_node="n2", relation="leads_to"),
            ],
            narrative_order=["n1", "n2"],
            entry_nodes=["n1"],
            terminal_nodes=["n2"],
            metadata=sample_metadata,
            version="1.0.0"
        )
        assert chain.chain_id == "chain_ditianshui"
        assert len(chain.nodes) == 2
        assert len(chain.edges) == 1
    
    def test_chain_id_regex_valid(self, sample_metadata):
        """测试有效的 chain_id 格式"""
        valid_ids = ["chain_ditianshui", "chain_zpzq", "chain_inner_sky"]
        for cid in valid_ids:
            chain = LogicChain(
                chain_id=cid,
                book_id="test",
                nodes=[LogicNode(node_id="n1", snippet_ids=["a"], role=SnippetRole.MAIN, summary="test")],
                edges=[],
                narrative_order=["n1"],
                entry_nodes=["n1"],
                terminal_nodes=["n1"],
                metadata=sample_metadata,
                version="1.0.0"
            )
            assert chain.chain_id == cid
    
    def test_chain_id_regex_invalid(self, sample_metadata):
        """测试无效的 chain_id 格式"""
        invalid_ids = ["ditianshui", "Chain_ditianshui", "chain-ditianshui"]
        for cid in invalid_ids:
            with pytest.raises(ValidationError):
                LogicChain(
                    chain_id=cid,
                    book_id="test",
                    nodes=[LogicNode(node_id="n1", snippet_ids=["a"], role=SnippetRole.MAIN, summary="test")],
                    edges=[],
                    narrative_order=["n1"],
                    entry_nodes=["n1"],
                    terminal_nodes=["n1"],
                    metadata=sample_metadata,
                    version="1.0.0"
                )
    
    def test_edge_references_validation_invalid_from(self, sample_metadata):
        """测试边引用不存在的起始节点"""
        with pytest.raises(ValidationError) as exc_info:
            LogicChain(
                chain_id="chain_test",
                book_id="test",
                nodes=[LogicNode(node_id="n1", snippet_ids=["a"], role=SnippetRole.MAIN, summary="test")],
                edges=[LogicEdge(from_node="n_invalid", to_node="n1", relation="leads_to")],
                narrative_order=["n1"],
                entry_nodes=["n1"],
                terminal_nodes=["n1"],
                metadata=sample_metadata,
                version="1.0.0"
            )
        assert "n_invalid" in str(exc_info.value)
    
    def test_edge_references_validation_invalid_to(self, sample_metadata):
        """测试边引用不存在的目标节点"""
        with pytest.raises(ValidationError) as exc_info:
            LogicChain(
                chain_id="chain_test",
                book_id="test",
                nodes=[LogicNode(node_id="n1", snippet_ids=["a"], role=SnippetRole.MAIN, summary="test")],
                edges=[LogicEdge(from_node="n1", to_node="n_invalid", relation="leads_to")],
                narrative_order=["n1"],
                entry_nodes=["n1"],
                terminal_nodes=["n1"],
                metadata=sample_metadata,
                version="1.0.0"
            )
        assert "n_invalid" in str(exc_info.value)


# =============================================================================
# AssemblyProtocol Tests
# =============================================================================

class TestAssemblyProtocol:
    """AssemblyProtocol 模型测试"""
    
    def test_valid_instance(self):
        """测试有效实例创建"""
        protocol = AssemblyProtocol(
            protocol_id="asm_career_standard",
            target_dimensions=["事业", "财富"],
            version="1.0.0"
        )
        assert protocol.protocol_id == "asm_career_standard"
        assert len(protocol.target_dimensions) == 2
        assert protocol.conflict_resolution == ConflictResolutionStrategy.PRIORITY_BASED
        assert protocol.narrative_order == NarrativeOrderStrategy.LOGIC_CHAIN
    
    def test_protocol_id_regex_valid(self):
        """测试有效的 protocol_id 格式"""
        valid_ids = ["asm_career", "asm_career_standard", "asm_health_v2"]
        for pid in valid_ids:
            protocol = AssemblyProtocol(
                protocol_id=pid,
                target_dimensions=["test"],
                version="1.0.0"
            )
            assert protocol.protocol_id == pid
    
    def test_protocol_id_regex_invalid(self):
        """测试无效的 protocol_id 格式"""
        invalid_ids = ["career", "Asm_career", "asm-career"]
        for pid in invalid_ids:
            with pytest.raises(ValidationError):
                AssemblyProtocol(
                    protocol_id=pid,
                    target_dimensions=["test"],
                    version="1.0.0"
                )
    
    def test_max_snippets_per_dimension_range(self):
        """测试 max_snippets_per_dimension 范围（1-20）"""
        # Valid: 1
        p1 = AssemblyProtocol(
            protocol_id="asm_test",
            target_dimensions=["test"],
            max_snippets_per_dimension=1,
            version="1.0.0"
        )
        assert p1.max_snippets_per_dimension == 1
        
        # Valid: 20
        p20 = AssemblyProtocol(
            protocol_id="asm_test",
            target_dimensions=["test"],
            max_snippets_per_dimension=20,
            version="1.0.0"
        )
        assert p20.max_snippets_per_dimension == 20
        
        # Invalid: 0
        with pytest.raises(ValidationError):
            AssemblyProtocol(
                protocol_id="asm_test",
                target_dimensions=["test"],
                max_snippets_per_dimension=0,
                version="1.0.0"
            )
        
        # Invalid: 21
        with pytest.raises(ValidationError):
            AssemblyProtocol(
                protocol_id="asm_test",
                target_dimensions=["test"],
                max_snippets_per_dimension=21,
                version="1.0.0"
            )
    
    def test_default_values(self):
        """测试默认值"""
        protocol = AssemblyProtocol(
            protocol_id="asm_test",
            target_dimensions=["test"],
            version="1.0.0"
        )
        assert protocol.target_engines == []
        assert protocol.conflict_resolution == ConflictResolutionStrategy.PRIORITY_BASED
        assert protocol.narrative_order == NarrativeOrderStrategy.LOGIC_CHAIN
        assert protocol.max_snippets_per_dimension == 5
        assert protocol.include_source_citation is True
        assert protocol.include_confidence_indicator is False
        assert len(protocol.role_priority) == 5
