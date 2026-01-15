"""
Property Tests for SemanticEntry

测试 SemanticEntry 基类的属性不变性。
对照 semantic-core spec Requirements 1.1-1.6, 9.1-9.2, 10.1-10.4

Property 清单:
- Property 1: SemanticEntry Field Validation (Req 1.1, 1.2, 9.1)
- Property 2: Factor ID Format Validation (Req 1.4, 9.2)
- Property 15: Parse-Print Round-Trip (Req 10.2, 10.4)
- Property 19: to_factor_refs Completeness (Req 1.5)
"""

import re

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st
from pydantic import ValidationError

from backend.core.contracts import (
    FACTOR_ID_PATTERN,
    SnippetRole,
    SourceMetadata,
)
from backend.semantics.core.base import (
    SEMANTIC_ID_PATTERN,
    VALID_ENGINES,
    NarrativeSnippetExtended,
    SemanticEntry,
)


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# 有效的 factor_id 策略
valid_factor_id_strategy = st.from_regex(
    r"^[a-z][a-z0-9_]{0,29}$",  # 限制长度避免过长
    fullmatch=True,
)

# 无效的 factor_id 策略（以数字开头或包含大写）
invalid_factor_id_strategy = st.one_of(
    st.from_regex(r"^[0-9][a-z0-9_]*$", fullmatch=True),  # 数字开头
    st.from_regex(r"^[A-Z][a-zA-Z0-9_]*$", fullmatch=True),  # 大写开头
    st.text(min_size=1, max_size=10).filter(lambda x: not re.match(FACTOR_ID_PATTERN, x)),
)

# 有效的 semantic_id 策略
valid_semantic_id_strategy = st.from_regex(
    r"^[a-z]{3,10}_v[0-9]_[a-z0-9_]{3,15}_[0-9]{3}$",
    fullmatch=True,
)

# 有效的 engine_id 策略
valid_engine_id_strategy = st.sampled_from(list(VALID_ENGINES))

# 有效的版本号策略
valid_version_strategy = st.from_regex(r"^[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}$", fullmatch=True)


# =============================================================================
# Property 1: SemanticEntry Field Validation (Task 2.3)
# Validates: Requirements 1.1, 1.2, 9.1
# =============================================================================

class TestSemanticEntryFieldValidation:
    """Property 1: SemanticEntry 字段验证"""
    
    @given(
        semantic_id=valid_semantic_id_strategy,
        engine_id=valid_engine_id_strategy,
        version=valid_version_strategy,
        factor_refs=st.lists(valid_factor_id_strategy, min_size=0, max_size=5, unique=True),
    )
    @settings(max_examples=100)
    def test_valid_fields_instantiation_succeeds(
        self,
        semantic_id: str,
        engine_id: str,
        version: str,
        factor_refs: list,
    ):
        """有效字段组合应能成功实例化 SemanticEntry"""
        entry = SemanticEntry(
            semantic_id=semantic_id,
            book_id="ditianshui",
            engine_id=engine_id,
            original_text="测试原文",
            normalized_text_zh="测试释义",
            subject="测试主题",
            factor_refs=factor_refs,
            version=version,
        )
        
        # 验证必填字段存在
        assert entry.semantic_id == semantic_id
        assert entry.book_id == "ditianshui"
        assert entry.engine_id == engine_id
        assert entry.version == version
        assert entry.factor_refs == factor_refs
    
    def test_default_values(self):
        """默认值应正确设置"""
        entry = SemanticEntry()
        
        assert entry.semantic_id == ""
        assert entry.book_id == ""
        assert entry.engine_id == "bazi"
        assert entry.original_text == ""
        assert entry.normalized_text_zh == ""
        assert entry.normalized_text_en is None
        assert entry.subject == ""
        assert entry.factor_refs == []
        assert entry.related_semantics == []
        assert entry.evidence_refs == []
        assert entry.cross_domain_refs == []
        assert entry.narrative_snippets == []
        assert entry.cross_domain_axes is None
        assert entry.metadata is None
        assert entry.version == "1.0.0"
    
    def test_invalid_semantic_id_pattern_rejected(self):
        """无效的 semantic_id 格式应被拒绝"""
        invalid_ids = [
            "UPPERCASE_v1_test_001",  # 大写
            "dts_1_test_001",  # 缺少 v
            "dts_v1_test_01",  # 序号不足3位
            "dts_v1_TEST_001",  # 大写
            "",  # 空字符串也应该允许（默认值）
        ]
        
        for invalid_id in invalid_ids[:-1]:  # 排除空字符串
            with pytest.raises(ValidationError):
                SemanticEntry(semantic_id=invalid_id)


# =============================================================================
# Property 2: Factor ID Format Validation (Task 2.4)
# Validates: Requirements 1.4, 9.2
# =============================================================================

class TestFactorIdFormatValidation:
    """Property 2: Factor ID 格式验证"""
    
    @given(factor_ids=st.lists(valid_factor_id_strategy, min_size=1, max_size=5, unique=True))
    @settings(max_examples=100)
    def test_valid_factor_ids_accepted(self, factor_ids: list):
        """有效的 factor_id 格式应通过验证"""
        entry = SemanticEntry(factor_refs=factor_ids)
        assert entry.factor_refs == factor_ids
    
    def test_invalid_factor_id_rejected(self):
        """无效的 factor_id 格式应被拒绝"""
        invalid_factor_ids = [
            ["1invalid"],  # 数字开头
            ["Invalid"],  # 大写开头
            ["has space"],  # 包含空格
            ["has-dash"],  # 包含连字符
        ]
        
        for invalid_refs in invalid_factor_ids:
            with pytest.raises(ValidationError) as exc_info:
                SemanticEntry(factor_refs=invalid_refs)
            assert "Invalid factor_id format" in str(exc_info.value)
    
    @given(valid_id=valid_factor_id_strategy)
    @settings(max_examples=50)
    def test_valid_factor_id_matches_pattern(self, valid_id: str):
        """有效的 factor_id 应匹配正则模式"""
        assert re.match(FACTOR_ID_PATTERN, valid_id) is not None


# =============================================================================
# Property 15: Parse-Print Round-Trip (Task 2.8)
# Validates: Requirements 10.2, 10.4
# =============================================================================

class TestParsePrintRoundTrip:
    """Property 15: to_markdown 输出验证"""
    
    def test_to_markdown_contains_subject(self, sample_semantic_entry):
        """to_markdown 输出应包含 subject"""
        md = sample_semantic_entry.to_markdown()
        assert f"# {sample_semantic_entry.subject}" in md
    
    def test_to_markdown_contains_original_text(self, sample_semantic_entry):
        """to_markdown 输出应包含原文"""
        md = sample_semantic_entry.to_markdown()
        assert sample_semantic_entry.original_text in md
    
    def test_to_markdown_contains_normalized_text(self, sample_semantic_entry):
        """to_markdown 输出应包含释义"""
        md = sample_semantic_entry.to_markdown()
        assert sample_semantic_entry.normalized_text_zh in md
    
    def test_to_markdown_contains_factor_refs(self, sample_semantic_entry):
        """to_markdown 输出应包含所有 factor_refs"""
        md = sample_semantic_entry.to_markdown()
        for factor_id in sample_semantic_entry.factor_refs:
            assert factor_id in md
    
    def test_to_markdown_contains_snippets(self, sample_semantic_entry):
        """to_markdown 输出应包含叙事素材"""
        md = sample_semantic_entry.to_markdown()
        for snippet in sample_semantic_entry.narrative_snippets:
            assert snippet.snippet_id in md
            assert snippet.snippet_text in md
            assert snippet.trigger_condition in md
    
    def test_to_markdown_contains_metadata(self, sample_semantic_entry):
        """to_markdown 输出应包含元数据"""
        md = sample_semantic_entry.to_markdown()
        assert sample_semantic_entry.version in md
        assert sample_semantic_entry.engine_id in md
        if sample_semantic_entry.metadata:
            assert sample_semantic_entry.metadata.book_id in md
    
    @given(
        subject=st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=("L", "N"))),
        original_text=st.text(min_size=1, max_size=100, alphabet=st.characters(whitelist_categories=("L", "N", "P"))),
        normalized_text=st.text(min_size=1, max_size=200, alphabet=st.characters(whitelist_categories=("L", "N", "P"))),
    )
    @settings(max_examples=50)
    def test_to_markdown_roundtrip_preserves_key_fields(
        self,
        subject: str,
        original_text: str,
        normalized_text: str,
    ):
        """to_markdown 应保留关键字段"""
        assume(len(subject.strip()) > 0)
        assume(len(original_text.strip()) > 0)
        assume(len(normalized_text.strip()) > 0)
        
        entry = SemanticEntry(
            subject=subject,
            original_text=original_text,
            normalized_text_zh=normalized_text,
        )
        
        md = entry.to_markdown()
        
        # 验证关键字段在输出中
        assert subject in md
        assert original_text in md
        assert normalized_text in md


# =============================================================================
# Property 19: to_factor_refs Completeness (Task 2.6)
# Validates: Requirements 1.5
# =============================================================================

class TestToFactorRefsCompleteness:
    """Property 19: to_factor_refs 完整性"""
    
    def test_to_factor_refs_includes_factor_refs(self, sample_semantic_entry):
        """to_factor_refs 应包含 factor_refs 中的所有因子"""
        all_refs = sample_semantic_entry.to_factor_refs()
        for factor_id in sample_semantic_entry.factor_refs:
            assert factor_id in all_refs
    
    def test_to_factor_refs_includes_snippet_factors(self, sample_semantic_entry):
        """to_factor_refs 应包含所有 snippet.related_factors"""
        all_refs = sample_semantic_entry.to_factor_refs()
        for snippet in sample_semantic_entry.narrative_snippets:
            for factor_id in snippet.related_factors:
                assert factor_id in all_refs
    
    def test_to_factor_refs_is_complete_union(self, sample_source_metadata):
        """to_factor_refs 应等于 factor_refs 和 snippet.related_factors 的并集"""
        snippet = NarrativeSnippetExtended(
            snippet_id="test_snippet_001",
            trigger_condition="factor_a AND factor_b",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="测试叙事素材内容。",
            source_ref="《测试》#章节",
            metadata=sample_source_metadata,
            related_factors=["factor_a", "factor_b", "factor_c"],
            related_rules=[],
            version="1.0.0",
            engine_id="bazi",
        )
        
        entry = SemanticEntry(
            factor_refs=["factor_x", "factor_y", "factor_a"],  # factor_a 重复
            narrative_snippets=[snippet],
        )
        
        all_refs = set(entry.to_factor_refs())
        expected = {"factor_x", "factor_y", "factor_a", "factor_b", "factor_c"}
        
        assert all_refs == expected
    
    @given(
        direct_factors=st.lists(valid_factor_id_strategy, min_size=0, max_size=3, unique=True),
        snippet_factors=st.lists(valid_factor_id_strategy, min_size=0, max_size=3, unique=True),
    )
    @settings(max_examples=50)
    def test_to_factor_refs_union_property(
        self,
        direct_factors: list,
        snippet_factors: list,
    ):
        """to_factor_refs 应等于 factor_refs ∪ snippet.related_factors"""
        # 内联创建 metadata 而非使用 fixture（避免 hypothesis 健康检查问题）
        from backend.core.contracts import SourceMetadata
        metadata = SourceMetadata(
            book_id="test_book",
            chapter="test_chapter",
            l1_anchor="TEST_L1_001",
        )
        
        snippet = NarrativeSnippetExtended(
            snippet_id="test_prop_001",
            trigger_condition="test_trigger",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="测试叙事素材内容供测试。",
            source_ref="《测试》#章节",
            metadata=metadata,
            related_factors=snippet_factors,
            related_rules=[],
            version="1.0.0",
            engine_id="bazi",
        )
        
        entry = SemanticEntry(
            factor_refs=direct_factors,
            narrative_snippets=[snippet],
        )
        
        result_set = set(entry.to_factor_refs())
        expected_set = set(direct_factors) | set(snippet_factors)
        
        assert result_set == expected_set


# =============================================================================
# Additional Tests: parse_factor_trigger (Task 2.9)
# =============================================================================

class TestParseFactorTrigger:
    """测试 parse_factor_trigger 静态方法"""
    
    def test_parse_single_factor(self):
        """解析单因子"""
        result = SemanticEntry.parse_factor_trigger("day_master_jia")
        assert result["operator"] is None
        assert result["factors"] == ["day_master_jia"]
    
    def test_parse_and_expression(self):
        """解析 AND 表达式"""
        result = SemanticEntry.parse_factor_trigger("day_master_jia AND season_spring")
        assert result["operator"] == "AND"
        assert result["factors"] == ["day_master_jia", "season_spring"]
    
    def test_parse_or_expression(self):
        """解析 OR 表达式"""
        result = SemanticEntry.parse_factor_trigger("element_wood OR element_fire")
        assert result["operator"] == "OR"
        assert result["factors"] == ["element_wood", "element_fire"]
    
    def test_parse_empty_string(self):
        """解析空字符串"""
        result = SemanticEntry.parse_factor_trigger("")
        assert result["operator"] is None
        assert result["factors"] == []
    
    def test_parse_whitespace_only(self):
        """解析仅空白字符"""
        result = SemanticEntry.parse_factor_trigger("   ")
        assert result["operator"] is None
        assert result["factors"] == []
    
    @given(
        factors=st.lists(valid_factor_id_strategy, min_size=2, max_size=4, unique=True),
        operator=st.sampled_from(["AND", "OR"]),
    )
    @settings(max_examples=50)
    def test_parse_factor_trigger_property(self, factors: list, operator: str):
        """parse_factor_trigger 应正确解析 AND/OR 表达式"""
        trigger_str = f" {operator} ".join(factors)
        result = SemanticEntry.parse_factor_trigger(trigger_str)
        
        assert result["operator"] == operator
        assert result["factors"] == factors


# =============================================================================
# Additional Tests: engine_id Validation
# =============================================================================

class TestEngineIdValidation:
    """测试 engine_id 验证"""
    
    @given(engine_id=valid_engine_id_strategy)
    @settings(max_examples=20)
    def test_valid_engine_id_accepted(self, engine_id: str):
        """有效的 engine_id 应被接受"""
        entry = SemanticEntry(engine_id=engine_id)
        assert entry.engine_id == engine_id
    
    def test_invalid_engine_id_rejected(self):
        """无效的 engine_id 应被拒绝"""
        with pytest.raises(ValidationError) as exc_info:
            SemanticEntry(engine_id="invalid_engine")
        assert "Invalid engine_id" in str(exc_info.value)
    
    def test_all_valid_engines(self):
        """所有 7 个有效引擎都应被接受"""
        for engine_id in VALID_ENGINES:
            entry = SemanticEntry(engine_id=engine_id)
            assert entry.engine_id == engine_id
