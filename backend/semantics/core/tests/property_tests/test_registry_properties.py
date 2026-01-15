"""
Property Tests for SemanticRegistry

测试 SemanticRegistry 注册中心的属性不变性。
对照 semantic-core spec Requirements 2.1-2.5, 11.2

Property 清单:
- Property 5: Registration Uniqueness (Req 2.2)
- Property 6: Query Consistency - by_book (Req 2.3, 2.5)
- Property 7: Query Consistency - by_factor (Req 2.3, 2.5)
"""

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from backend.core.contracts import SnippetRole, SourceMetadata
from backend.semantics.core.base import (
    SEMANTIC_ID_PATTERN,
    VALID_ENGINES,
    InvertedIndex,
    NarrativeSnippetExtended,
    SemanticEntry,
    SemanticRegistry,
)


# =============================================================================
# Hypothesis Strategies
# =============================================================================

valid_book_id_strategy = st.sampled_from([
    "ditianshui", "sanmingtonghui", "yuanhaiziping",
    "menglinxuanjie", "zhougongjiemeng", "zhouyi",
])

valid_engine_id_strategy = st.sampled_from(list(VALID_ENGINES))

valid_factor_id_strategy = st.from_regex(
    r"^[a-z][a-z0-9_]{2,15}$",
    fullmatch=True,
)


# =============================================================================
# Helper Functions
# =============================================================================

def make_semantic_id(book_abbr: str, topic: str, number: int) -> str:
    """生成有效的 semantic_id"""
    return f"{book_abbr}_v1_{topic}_{number:03d}"


def create_entry_class(
    original_text: str = "测试原文",
    normalized_text_zh: str = "测试释义",
    subject: str = "测试主题",
    factor_refs: list = None,
    narrative_snippets: list = None,
):
    """创建 SemanticEntry 子类"""
    
    class TestEntry(SemanticEntry):
        pass
    
    # 设置类属性
    TestEntry.__annotations__ = SemanticEntry.__annotations__.copy()
    
    # 返回一个可以实例化的类
    return type(
        "TestEntry",
        (SemanticEntry,),
        {
            "original_text": original_text,
            "normalized_text_zh": normalized_text_zh,
            "subject": subject,
            "factor_refs": factor_refs or [],
            "narrative_snippets": narrative_snippets or [],
        }
    )


# =============================================================================
# Property 5: Registration Uniqueness (Task 4.4)
# Validates: Requirements 2.2
# =============================================================================

class TestRegistrationUniqueness:
    """Property 5: 注册唯一性"""
    
    def test_duplicate_registration_raises_error(self):
        """重复注册相同 semantic_id 应抛出 ValueError"""
        semantic_id = "dts_v1_test_001"
        
        @SemanticRegistry.register(
            semantic_id=semantic_id,
            book_id="ditianshui",
            engine_id="bazi"
        )
        class FirstEntry(SemanticEntry):
            original_text: str = "第一个条目"
            normalized_text_zh: str = "第一个释义"
            subject: str = "第一个主题"
        
        with pytest.raises(ValueError) as exc_info:
            @SemanticRegistry.register(
                semantic_id=semantic_id,  # 重复 ID
                book_id="ditianshui",
                engine_id="bazi"
            )
            class SecondEntry(SemanticEntry):
                original_text: str = "第二个条目"
                normalized_text_zh: str = "第二个释义"
                subject: str = "第二个主题"
        
        assert "Duplicate semantic_id" in str(exc_info.value)
    
    def test_different_ids_can_register(self):
        """不同的 semantic_id 应能成功注册"""
        @SemanticRegistry.register(
            semantic_id="dts_v1_first_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class FirstEntry(SemanticEntry):
            original_text: str = "第一个条目"
            normalized_text_zh: str = "第一个释义"
            subject: str = "第一个主题"
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_second_002",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class SecondEntry(SemanticEntry):
            original_text: str = "第二个条目"
            normalized_text_zh: str = "第二个释义"
            subject: str = "第二个主题"
        
        assert SemanticRegistry.count() == 2
        assert SemanticRegistry.get("dts_v1_first_001") is not None
        assert SemanticRegistry.get("dts_v1_second_002") is not None
    
    def test_invalid_semantic_id_format_rejected(self):
        """无效的 semantic_id 格式应被拒绝"""
        with pytest.raises(ValueError) as exc_info:
            @SemanticRegistry.register(
                semantic_id="INVALID_FORMAT",  # 无效格式
                book_id="ditianshui",
                engine_id="bazi"
            )
            class InvalidEntry(SemanticEntry):
                pass
        
        assert "Invalid semantic_id format" in str(exc_info.value)
    
    def test_invalid_engine_id_rejected(self):
        """无效的 engine_id 应被拒绝"""
        with pytest.raises(ValueError) as exc_info:
            @SemanticRegistry.register(
                semantic_id="dts_v1_test_001",
                book_id="ditianshui",
                engine_id="invalid_engine"  # 无效引擎
            )
            class InvalidEngine(SemanticEntry):
                pass
        
        assert "Invalid engine_id" in str(exc_info.value)


# =============================================================================
# Property 6: Query Consistency - by_book (Task 4.6)
# Validates: Requirements 2.3, 2.5
# =============================================================================

class TestQueryConsistencyByBook:
    """Property 6: get_by_book 查询一致性"""
    
    def test_registered_entry_found_by_book(self):
        """注册后的条目应能通过 get_by_book 查找"""
        book_id = "ditianshui"
        semantic_id = "dts_v1_book_001"
        
        @SemanticRegistry.register(
            semantic_id=semantic_id,
            book_id=book_id,
            engine_id="bazi"
        )
        class BookEntry(SemanticEntry):
            original_text: str = "书籍条目"
            normalized_text_zh: str = "书籍释义"
            subject: str = "书籍主题"
        
        entries = SemanticRegistry.get_by_book(book_id)
        
        assert len(entries) >= 1
        assert any(e.semantic_id == semantic_id for e in entries)
    
    def test_multiple_entries_same_book(self):
        """同一书籍的多个条目应都能查到"""
        book_id = "sanmingtonghui"
        
        @SemanticRegistry.register(
            semantic_id="smth_v1_first_001",
            book_id=book_id,
            engine_id="bazi"
        )
        class Entry1(SemanticEntry):
            original_text: str = "第一个"
            normalized_text_zh: str = "释义1"
            subject: str = "主题1"
        
        @SemanticRegistry.register(
            semantic_id="smth_v1_second_002",
            book_id=book_id,
            engine_id="bazi"
        )
        class Entry2(SemanticEntry):
            original_text: str = "第二个"
            normalized_text_zh: str = "释义2"
            subject: str = "主题2"
        
        entries = SemanticRegistry.get_by_book(book_id)
        
        assert len(entries) == 2
        semantic_ids = {e.semantic_id for e in entries}
        assert "smth_v1_first_001" in semantic_ids
        assert "smth_v1_second_002" in semantic_ids
    
    def test_different_books_isolated(self):
        """不同书籍的条目应相互隔离"""
        @SemanticRegistry.register(
            semantic_id="dts_v1_iso_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class DTSEntry(SemanticEntry):
            original_text: str = "滴天髓"
            normalized_text_zh: str = "释义"
            subject: str = "主题"
        
        @SemanticRegistry.register(
            semantic_id="mlxj_v1_iso_001",
            book_id="menglinxuanjie",
            engine_id="dream"
        )
        class MLXJEntry(SemanticEntry):
            original_text: str = "梦林玄解"
            normalized_text_zh: str = "释义"
            subject: str = "主题"
        
        dts_entries = SemanticRegistry.get_by_book("ditianshui")
        mlxj_entries = SemanticRegistry.get_by_book("menglinxuanjie")
        
        dts_ids = {e.semantic_id for e in dts_entries}
        mlxj_ids = {e.semantic_id for e in mlxj_entries}
        
        assert "dts_v1_iso_001" in dts_ids
        assert "dts_v1_iso_001" not in mlxj_ids
        assert "mlxj_v1_iso_001" in mlxj_ids
        assert "mlxj_v1_iso_001" not in dts_ids


# =============================================================================
# Property 7: Query Consistency - by_factor (Task 4.6)
# Validates: Requirements 2.3, 2.5
# =============================================================================

class TestQueryConsistencyByFactor:
    """Property 7: get_by_factor 查询一致性"""
    
    def test_registered_entry_found_by_factor(self):
        """条目应能通过其 factor_refs 中的任一因子查找"""
        factor_id = "day_master_jia"
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_factor_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class FactorEntry(SemanticEntry):
            original_text: str = "因子条目"
            normalized_text_zh: str = "释义"
            subject: str = "主题"
            factor_refs: list = [factor_id, "element_wood"]
        
        entries = SemanticRegistry.get_by_factor(factor_id)
        
        assert len(entries) >= 1
        assert any(e.semantic_id == "dts_v1_factor_001" for e in entries)
    
    def test_all_factors_findable(self):
        """条目应能通过其所有 factor_refs 查找"""
        factors = ["test_factor_a", "test_factor_b", "test_factor_c"]
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_multi_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class MultiFactorEntry(SemanticEntry):
            original_text: str = "多因子条目"
            normalized_text_zh: str = "释义"
            subject: str = "主题"
            factor_refs: list = factors
        
        for factor_id in factors:
            entries = SemanticRegistry.get_by_factor(factor_id)
            assert any(e.semantic_id == "dts_v1_multi_001" for e in entries), \
                f"Entry not found by factor: {factor_id}"
    
    def test_snippet_factors_indexed(self, sample_source_metadata):
        """snippet.related_factors 也应被索引"""
        snippet = NarrativeSnippetExtended(
            snippet_id="test_snippet_001",
            trigger_condition="snippet_factor_x",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="叙事素材的测试内容。",
            source_ref="《测试》#章节",
            metadata=sample_source_metadata,
            related_factors=["snippet_factor_x", "snippet_factor_y"],
            related_rules=[],
            version="1.0.0",
            engine_id="bazi",
        )
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_snippet_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class SnippetEntry(SemanticEntry):
            original_text: str = "叙事素材条目"
            normalized_text_zh: str = "释义"
            subject: str = "主题"
            factor_refs: list = ["direct_factor"]
            narrative_snippets: list = [snippet]
        
        # 直接因子应能查到
        direct_entries = SemanticRegistry.get_by_factor("direct_factor")
        assert any(e.semantic_id == "dts_v1_snippet_001" for e in direct_entries)
        
        # snippet 因子也应能查到
        snippet_entries = SemanticRegistry.get_by_factor("snippet_factor_x")
        assert any(e.semantic_id == "dts_v1_snippet_001" for e in snippet_entries)


# =============================================================================
# Additional Tests: InvertedIndex
# =============================================================================

class TestInvertedIndex:
    """测试 InvertedIndex 倒排索引"""
    
    def test_add_and_search_any(self):
        """添加后应能通过 any 模式搜索"""
        index = InvertedIndex()
        index.add("entry_1", ["token_a", "token_b"])
        index.add("entry_2", ["token_b", "token_c"])
        
        # any 模式：包含任一 token
        results = index.search(["token_a"], mode="any")
        assert "entry_1" in results
        assert "entry_2" not in results
        
        results = index.search(["token_b"], mode="any")
        assert "entry_1" in results
        assert "entry_2" in results
    
    def test_search_all_mode(self):
        """all 模式应返回交集"""
        index = InvertedIndex()
        index.add("entry_1", ["token_a", "token_b", "token_c"])
        index.add("entry_2", ["token_b", "token_c"])
        index.add("entry_3", ["token_a"])
        
        # all 模式：必须包含所有 tokens
        results = index.search(["token_a", "token_b"], mode="all")
        assert "entry_1" in results
        assert "entry_2" not in results
        assert "entry_3" not in results
        
        results = index.search(["token_b", "token_c"], mode="all")
        assert "entry_1" in results
        assert "entry_2" in results
        assert "entry_3" not in results
    
    def test_remove(self):
        """remove 应移除指定条目的索引"""
        index = InvertedIndex()
        index.add("entry_1", ["token_a", "token_b"])
        index.add("entry_2", ["token_a"])
        
        index.remove("entry_1")
        
        results = index.search(["token_a"], mode="any")
        assert "entry_1" not in results
        assert "entry_2" in results
    
    def test_search_empty_tokens(self):
        """空 tokens 应返回空集"""
        index = InvertedIndex()
        index.add("entry_1", ["token_a"])
        
        results = index.search([], mode="any")
        assert len(results) == 0
    
    def test_clear(self):
        """clear 应清空索引"""
        index = InvertedIndex()
        index.add("entry_1", ["token_a"])
        
        assert len(index) > 0
        
        index.clear()
        
        assert len(index) == 0
        results = index.search(["token_a"], mode="any")
        assert len(results) == 0


# =============================================================================
# Additional Tests: Engine Stats
# =============================================================================

class TestEngineStats:
    """测试引擎统计功能"""
    
    def test_get_engine_stats(self):
        """get_engine_stats 应返回正确的统计信息"""
        @SemanticRegistry.register(
            semantic_id="dts_v1_stats_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class StatsEntry1(SemanticEntry):
            original_text: str = "条目1"
            normalized_text_zh: str = "释义1"
            subject: str = "主题1"
            factor_refs: list = ["factor_a", "factor_b"]
        
        @SemanticRegistry.register(
            semantic_id="smth_v1_stats_001",
            book_id="sanmingtonghui",
            engine_id="bazi"
        )
        class StatsEntry2(SemanticEntry):
            original_text: str = "条目2"
            normalized_text_zh: str = "释义2"
            subject: str = "主题2"
            factor_refs: list = ["factor_b", "factor_c"]
        
        stats = SemanticRegistry.get_engine_stats("bazi")
        
        assert stats["engine_id"] == "bazi"
        assert stats["entry_count"] == 2
        assert set(stats["book_ids"]) == {"ditianshui", "sanmingtonghui"}
        assert stats["factor_count"] == 3  # factor_a, factor_b, factor_c
    
    def test_get_engine_stats_empty(self):
        """空引擎应返回零统计"""
        stats = SemanticRegistry.get_engine_stats("ziwei")
        
        assert stats["engine_id"] == "ziwei"
        assert stats["entry_count"] == 0
        assert stats["book_ids"] == []
        assert stats["factor_count"] == 0


# =============================================================================
# Additional Tests: get_by_trigger
# =============================================================================

class TestGetByTrigger:
    """测试 get_by_trigger 查询"""
    
    def test_get_by_trigger_any(self, sample_source_metadata):
        """get_by_trigger 应能通过 trigger_condition 查找"""
        snippet = NarrativeSnippetExtended(
            snippet_id="trigger_test_001",
            trigger_condition="day_master_jia AND season_spring",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="触发条件测试内容。",
            source_ref="《测试》#章节",
            metadata=sample_source_metadata,
            related_factors=[],
            related_rules=[],
            version="1.0.0",
            engine_id="bazi",
        )
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_trigger_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class TriggerEntry(SemanticEntry):
            original_text: str = "触发条目"
            normalized_text_zh: str = "释义"
            subject: str = "主题"
            narrative_snippets: list = [snippet]
        
        # 搜索单个 token
        entries = SemanticRegistry.get_by_trigger("day_master_jia", mode="any")
        assert any(e.semantic_id == "dts_v1_trigger_001" for e in entries)
        
        # 搜索另一个 token
        entries = SemanticRegistry.get_by_trigger("season_spring", mode="any")
        assert any(e.semantic_id == "dts_v1_trigger_001" for e in entries)
    
    def test_get_by_trigger_all(self, sample_source_metadata):
        """get_by_trigger all 模式应返回包含所有 tokens 的条目"""
        snippet1 = NarrativeSnippetExtended(
            snippet_id="all_test_001",
            trigger_condition="factor_x AND factor_y AND factor_z",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="三因子触发条件测试。",
            source_ref="《测试》#章节",
            metadata=sample_source_metadata,
            related_factors=[],
            related_rules=[],
            version="1.0.0",
            engine_id="bazi",
        )
        
        snippet2 = NarrativeSnippetExtended(
            snippet_id="all_test_002",
            trigger_condition="factor_x AND factor_y",
            role=SnippetRole.MAIN,
            primary_lang="zh-CN",
            snippet_text="双因子触发条件测试。",
            source_ref="《测试》#章节",
            metadata=sample_source_metadata,
            related_factors=[],
            related_rules=[],
            version="1.0.0",
            engine_id="bazi",
        )
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_alltest_001",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class AllEntry1(SemanticEntry):
            original_text: str = "条目1"
            normalized_text_zh: str = "释义1"
            subject: str = "主题1"
            narrative_snippets: list = [snippet1]
        
        @SemanticRegistry.register(
            semantic_id="dts_v1_alltest_002",
            book_id="ditianshui",
            engine_id="bazi"
        )
        class AllEntry2(SemanticEntry):
            original_text: str = "条目2"
            normalized_text_zh: str = "释义2"
            subject: str = "主题2"
            narrative_snippets: list = [snippet2]
        
        # all 模式搜索 x, y, z：只有条目1匹配
        entries = SemanticRegistry.get_by_trigger("factor_x AND factor_y AND factor_z", mode="all")
        semantic_ids = {e.semantic_id for e in entries}
        assert "dts_v1_alltest_001" in semantic_ids
        assert "dts_v1_alltest_002" not in semantic_ids
        
        # all 模式搜索 x, y：两个条目都匹配
        entries = SemanticRegistry.get_by_trigger("factor_x AND factor_y", mode="all")
        semantic_ids = {e.semantic_id for e in entries}
        assert "dts_v1_alltest_001" in semantic_ids
        assert "dts_v1_alltest_002" in semantic_ids
