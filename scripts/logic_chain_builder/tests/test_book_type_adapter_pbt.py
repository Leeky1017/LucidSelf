"""
Property-Based Tests for BookTypeAdapter

Tests the book type classification and entry node heuristics using Hypothesis.

**Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
**Validates: Requirements 11.1**
"""

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.book_type_adapter import (
    BookTypeAdapter,
    BookType,
    BOOK_TYPE_MAP,
    ARGUMENT_PATTERNS,
    ENTRY_NODE_KEYWORDS,
)
from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.constants import TARGET_BOOKS


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for valid book types
book_type_strategy = st.sampled_from(list(BookType))

# Strategy for valid book IDs from the 21 target books
valid_book_id_strategy = st.sampled_from(TARGET_BOOKS)

# Strategy for invalid book IDs
invalid_book_id_strategy = st.text(
    min_size=1,
    max_size=50,
    alphabet=st.characters(whitelist_categories=('L', 'N'), whitelist_characters='_-')
).filter(lambda x: x not in TARGET_BOOKS and x.strip())


@st.composite
def logic_node_strategy(draw, summary: str = None):
    """Generate a valid LogicNode for testing."""
    node_id = draw(st.from_regex(r"n_[a-z]+_[a-z0-9]+_\d+", fullmatch=True))
    role = draw(st.sampled_from(list(SnippetRole)))
    
    if summary is None:
        summary = draw(st.text(min_size=1, max_size=50, alphabet=st.characters(
            whitelist_categories=('L', 'N', 'P'),
            whitelist_characters=' '
        )).filter(lambda x: x.strip()))
    
    return LogicNode(
        node_id=node_id,
        snippet_ids=[],
        role=role,
        summary=summary,
    )


@st.composite
def logic_node_with_keyword_strategy(draw, book_type: BookType):
    """Generate a LogicNode with a keyword from the specified book type."""
    keywords = ENTRY_NODE_KEYWORDS.get(book_type, [])
    assume(len(keywords) > 0)
    
    keyword = draw(st.sampled_from(keywords))
    # Create summary containing the keyword
    prefix = draw(st.text(min_size=0, max_size=10, alphabet=st.characters(
        whitelist_categories=('L',),
    )))
    suffix = draw(st.text(min_size=0, max_size=10, alphabet=st.characters(
        whitelist_categories=('L',),
    )))
    summary = f"{prefix}{keyword}{suffix}"[:50]  # Ensure max 50 chars
    
    return draw(logic_node_strategy(summary=summary))


# =============================================================================
# Property 12: Book Type Classification Completeness
# =============================================================================

class TestBookTypeClassificationCompleteness:
    """
    **Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
    **Validates: Requirements 11.1**
    
    *For any* of the 21 target books, the BookTypeAdapter should return a valid 
    book_type in {命理, 占卜, 梦学, 西方占星}.
    """

    def test_all_21_books_have_classification(self):
        """
        **Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
        **Validates: Requirements 11.1**
        
        Property: All 21 target books must have a valid book type classification.
        """
        adapter = BookTypeAdapter()
        valid_types = {BookType.MINGLI, BookType.DIVINATION, BookType.DREAM, BookType.WESTERN_ASTROLOGY}
        
        for book_id in TARGET_BOOKS:
            book_type = adapter.get_book_type(book_id)
            assert book_type is not None, f"Book '{book_id}' has no type classification"
            assert book_type in valid_types, f"Book '{book_id}' has invalid type: {book_type}"

    def test_exactly_21_books_classified(self):
        """
        **Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
        **Validates: Requirements 11.1**
        
        Property: Exactly 21 books should be classified across all types.
        """
        all_classified_books = []
        for book_type, books in BOOK_TYPE_MAP.items():
            all_classified_books.extend(books)
        
        assert len(all_classified_books) == 21, (
            f"Expected 21 books, got {len(all_classified_books)}"
        )
        
        # No duplicates
        assert len(all_classified_books) == len(set(all_classified_books)), (
            "Duplicate books found in classification"
        )

    def test_book_type_map_matches_target_books(self):
        """
        **Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
        **Validates: Requirements 11.1**
        
        Property: BOOK_TYPE_MAP should contain exactly the TARGET_BOOKS.
        """
        all_classified_books = set()
        for books in BOOK_TYPE_MAP.values():
            all_classified_books.update(books)
        
        target_set = set(TARGET_BOOKS)
        
        assert all_classified_books == target_set, (
            f"Mismatch between BOOK_TYPE_MAP and TARGET_BOOKS.\n"
            f"In BOOK_TYPE_MAP but not TARGET_BOOKS: {all_classified_books - target_set}\n"
            f"In TARGET_BOOKS but not BOOK_TYPE_MAP: {target_set - all_classified_books}"
        )

    @settings(max_examples=100)
    @given(book_id=valid_book_id_strategy)
    def test_valid_book_returns_valid_type(self, book_id: str):
        """
        **Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
        **Validates: Requirements 11.1**
        
        Property: Any valid book_id should return a valid BookType.
        """
        adapter = BookTypeAdapter()
        book_type = adapter.get_book_type(book_id)
        
        assert book_type is not None, f"Book '{book_id}' returned None type"
        assert isinstance(book_type, BookType), f"Expected BookType, got {type(book_type)}"
        assert book_type.value in {"命理", "占卜", "梦学", "西方占星"}, (
            f"Invalid book type value: {book_type.value}"
        )

    @settings(max_examples=50)
    @given(book_id=invalid_book_id_strategy)
    def test_invalid_book_returns_none(self, book_id: str):
        """
        **Feature: logic-chain-builder, Property 12: Book Type Classification Completeness**
        **Validates: Requirements 11.1**
        
        Property: Invalid book_ids should return None.
        """
        adapter = BookTypeAdapter()
        book_type = adapter.get_book_type(book_id)
        
        assert book_type is None, f"Invalid book '{book_id}' should return None, got {book_type}"


class TestBookTypeCategories:
    """
    Tests for specific book type categories.
    
    **Validates: Requirements 11.1**
    """

    def test_mingli_books_count(self):
        """Property: 命理 category should have exactly 6 books."""
        assert len(BOOK_TYPE_MAP[BookType.MINGLI]) == 6

    def test_divination_books_count(self):
        """Property: 占卜 category should have exactly 5 books."""
        assert len(BOOK_TYPE_MAP[BookType.DIVINATION]) == 5

    def test_dream_books_count(self):
        """Property: 梦学 category should have exactly 4 books."""
        assert len(BOOK_TYPE_MAP[BookType.DREAM]) == 4

    def test_western_astrology_books_count(self):
        """Property: 西方占星 category should have exactly 6 books."""
        assert len(BOOK_TYPE_MAP[BookType.WESTERN_ASTROLOGY]) == 6

    def test_chinese_classics_in_mingli(self):
        """Property: Chinese fate calculation classics should be in 命理."""
        adapter = BookTypeAdapter()
        chinese_mingli = ["滴天髓", "子平真诠", "穷通宝鉴", "渊海子平", "三命通会", "紫微斗数全书"]
        
        for book_id in chinese_mingli:
            assert adapter.get_book_type(book_id) == BookType.MINGLI, (
                f"'{book_id}' should be classified as 命理"
            )

    def test_tarot_books_in_divination(self):
        """Property: Tarot books should be in 占卜."""
        adapter = BookTypeAdapter()
        tarot_books = [
            "the_book_of_thoth",
            "78_degrees_of_wisdom",
            "waite_pictorial_key_to_the_tarot",
            "learning_the_tarot",
        ]
        
        for book_id in tarot_books:
            assert adapter.get_book_type(book_id) == BookType.DIVINATION, (
                f"'{book_id}' should be classified as 占卜"
            )

    def test_western_astrology_books(self):
        """Property: Western astrology books should be in 西方占星."""
        adapter = BookTypeAdapter()
        western_astro = [
            "the_inner_sky",
            "planets_in_transit",
            "the_astrological_houses",
            "astrology_of_personality",
            "tetrabiblos",
            "christian_astrology,_vol._1_and_2",
        ]
        
        for book_id in western_astro:
            assert adapter.get_book_type(book_id) == BookType.WESTERN_ASTROLOGY, (
                f"'{book_id}' should be classified as 西方占星"
            )


class TestArgumentPatterns:
    """
    Tests for argument pattern retrieval.
    
    **Validates: Requirements 11.2, 11.3, 11.4**
    """

    def test_all_book_types_have_patterns(self):
        """Property: All book types should have argument patterns defined."""
        for book_type in BookType:
            assert book_type in ARGUMENT_PATTERNS, (
                f"Book type {book_type} missing argument pattern"
            )

    @settings(max_examples=100)
    @given(book_id=valid_book_id_strategy)
    def test_valid_book_has_argument_pattern(self, book_id: str):
        """
        Property: Any valid book should return a non-empty argument pattern.
        """
        adapter = BookTypeAdapter()
        pattern = adapter.get_argument_pattern(book_id)
        
        assert pattern is not None
        assert len(pattern) > 0
        assert pattern != "通用"  # Valid books should have specific patterns

    def test_mingli_pattern(self):
        """Property: 命理 books should have 格局→用神→吉凶 pattern."""
        adapter = BookTypeAdapter()
        assert adapter.get_argument_pattern("滴天髓") == "格局→用神→吉凶"

    def test_divination_pattern(self):
        """Property: 占卜 books should have 符号→意象→诠释 pattern."""
        adapter = BookTypeAdapter()
        assert adapter.get_argument_pattern("周易") == "符号→意象→诠释"

    def test_dream_pattern(self):
        """Property: 梦学 books should have 象征→心理→解析 pattern."""
        adapter = BookTypeAdapter()
        assert adapter.get_argument_pattern("周公解梦") == "象征→心理→解析"

    def test_western_astrology_pattern(self):
        """Property: 西方占星 books should have 星体→宫位→相位→诠释 pattern."""
        adapter = BookTypeAdapter()
        assert adapter.get_argument_pattern("the_inner_sky") == "星体→宫位→相位→诠释"

    def test_unknown_book_returns_generic_pattern(self):
        """Property: Unknown books should return 通用 pattern."""
        adapter = BookTypeAdapter()
        assert adapter.get_argument_pattern("unknown_book") == "通用"


class TestEntryNodeHeuristics:
    """
    Tests for entry node heuristics.
    
    **Validates: Requirements 11.2, 11.3, 11.4, 11.5**
    """

    def test_all_book_types_have_keywords(self):
        """Property: All book types should have entry node keywords defined."""
        for book_type in BookType:
            assert book_type in ENTRY_NODE_KEYWORDS, (
                f"Book type {book_type} missing entry node keywords"
            )
            assert len(ENTRY_NODE_KEYWORDS[book_type]) > 0, (
                f"Book type {book_type} has empty keywords list"
            )

    def test_main_role_increases_score(self):
        """
        **Validates: Requirements 11.2, 11.3, 11.4, 11.5**
        
        Property: Nodes with MAIN role should have higher entry node score.
        """
        adapter = BookTypeAdapter()
        
        main_node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            summary="测试节点",
        )
        
        summary_node = LogicNode(
            node_id="n_test_ch_1",
            snippet_ids=[],
            role=SnippetRole.SUMMARY,
            summary="测试节点",
        )
        
        for book_id in TARGET_BOOKS:
            main_score = adapter.score_entry_node(main_node, book_id)
            summary_score = adapter.score_entry_node(summary_node, book_id)
            
            assert main_score > summary_score, (
                f"MAIN role should score higher than SUMMARY for {book_id}"
            )

    def test_keyword_in_summary_increases_score(self):
        """
        **Validates: Requirements 11.2, 11.3, 11.4, 11.5**
        
        Property: Nodes with book-type keywords in summary should score higher.
        """
        adapter = BookTypeAdapter()
        
        # Test for 命理 book with 格局 keyword
        node_with_keyword = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.CONDITION_BRANCH,
            summary="论格局之法",
        )
        
        node_without_keyword = LogicNode(
            node_id="n_test_ch_1",
            snippet_ids=[],
            role=SnippetRole.CONDITION_BRANCH,
            summary="其他内容",
        )
        
        score_with = adapter.score_entry_node(node_with_keyword, "滴天髓")
        score_without = adapter.score_entry_node(node_without_keyword, "滴天髓")
        
        assert score_with > score_without, (
            "Node with keyword should score higher"
        )

    @settings(max_examples=50)
    @given(book_type=book_type_strategy)
    def test_keyword_matching_for_book_type(self, book_type: BookType):
        """
        **Validates: Requirements 11.2, 11.3, 11.4, 11.5**
        
        Property: Nodes with type-specific keywords should be entry candidates.
        """
        adapter = BookTypeAdapter()
        books = BOOK_TYPE_MAP[book_type]
        assume(len(books) > 0)
        
        book_id = books[0]
        keywords = ENTRY_NODE_KEYWORDS[book_type]
        assume(len(keywords) > 0)
        
        keyword = keywords[0]
        
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            summary=f"关于{keyword}的论述",
        )
        
        score = adapter.score_entry_node(node, book_id)
        assert score >= 1.0, (
            f"Node with MAIN role and keyword '{keyword}' should score >= 1.0"
        )


class TestArgumentPatternStages:
    """
    Tests for argument pattern stage parsing.
    
    **Validates: Requirements 11.2, 11.3, 11.4**
    """

    def test_mingli_stages(self):
        """Property: 命理 pattern should have 3 stages."""
        adapter = BookTypeAdapter()
        stages = adapter.get_argument_pattern_stages("滴天髓")
        
        assert stages == ["格局", "用神", "吉凶"]

    def test_divination_stages(self):
        """Property: 占卜 pattern should have 3 stages."""
        adapter = BookTypeAdapter()
        stages = adapter.get_argument_pattern_stages("周易")
        
        assert stages == ["符号", "意象", "诠释"]

    def test_dream_stages(self):
        """Property: 梦学 pattern should have 3 stages."""
        adapter = BookTypeAdapter()
        stages = adapter.get_argument_pattern_stages("周公解梦")
        
        assert stages == ["象征", "心理", "解析"]

    def test_western_astrology_stages(self):
        """Property: 西方占星 pattern should have 4 stages."""
        adapter = BookTypeAdapter()
        stages = adapter.get_argument_pattern_stages("the_inner_sky")
        
        assert stages == ["星体", "宫位", "相位", "诠释"]

    def test_unknown_book_returns_empty_stages(self):
        """Property: Unknown books should return empty stages list."""
        adapter = BookTypeAdapter()
        stages = adapter.get_argument_pattern_stages("unknown_book")
        
        assert stages == []


class TestNodeClassificationByStage:
    """
    Tests for node classification by argument stage.
    
    **Validates: Requirements 11.2, 11.3, 11.4**
    """

    def test_classify_mingli_node(self):
        """Property: Node with 格局 in summary should be classified as 格局 stage."""
        adapter = BookTypeAdapter()
        
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            summary="论格局高低",
        )
        
        stage = adapter.classify_node_by_argument_stage(node, "滴天髓")
        assert stage == "格局"

    def test_classify_divination_node(self):
        """Property: Node with 符号 in summary should be classified as 符号 stage."""
        adapter = BookTypeAdapter()
        
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            summary="符号之义",
        )
        
        stage = adapter.classify_node_by_argument_stage(node, "周易")
        assert stage == "符号"

    def test_no_match_returns_none(self):
        """Property: Node without stage keywords should return None."""
        adapter = BookTypeAdapter()
        
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            summary="其他内容",
        )
        
        stage = adapter.classify_node_by_argument_stage(node, "滴天髓")
        assert stage is None

    def test_unknown_book_returns_none(self):
        """Property: Unknown book should return None for stage classification."""
        adapter = BookTypeAdapter()
        
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            summary="格局论",
        )
        
        stage = adapter.classify_node_by_argument_stage(node, "unknown_book")
        assert stage is None
