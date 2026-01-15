"""
Property-Based Tests for IntelligentSummaryGenerator

Tests the intelligent summary generation functionality using Hypothesis.

**Feature: logic-chain-builder, Property 16: Summary Semantic Completeness**
**Validates: Requirements 15.2, 15.3, 15.5**
"""

from typing import List, Set

import pytest
from hypothesis import given, settings, assume, HealthCheck
from hypothesis import strategies as st

from scripts.logic_chain_builder.summary_generator import (
    IntelligentSummaryGenerator,
    DOMAIN_KEYWORDS,
    ROLE_PREFIXES,
    get_summary_generator,
)
from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.constants import MAX_SUMMARY_LENGTH
from scripts.schema_extractor.models import (
    NarrativeSnippet,
    SnippetRole as ExtractorSnippetRole,
)


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for valid snippet roles
snippet_role_strategy = st.sampled_from([role for role in ExtractorSnippetRole])

# Strategy for node roles
node_role_strategy = st.sampled_from([role for role in SnippetRole])

# Strategy for book types
book_type_strategy = st.sampled_from(["命理", "占卜", "梦学", "西方占星"])

# Strategy for snippet IDs
snippet_id_strategy = st.from_regex(r"ns_[a-z]{2,5}_\d{3}", fullmatch=True)

# Strategy for source reference
source_ref_strategy = st.builds(
    lambda book, chapter: f"《{book}》#{chapter}",
    book=st.text(min_size=2, max_size=8, alphabet=st.characters(
        whitelist_categories=('L',),
    )).filter(lambda x: x.strip()),
    chapter=st.text(min_size=1, max_size=10, alphabet=st.characters(
        whitelist_categories=('L', 'N'),
    )).filter(lambda x: x.strip())
)


@st.composite
def trigger_with_keyword_strategy(draw, book_type: str):
    """
    Generate a trigger that contains a domain keyword for the given book type.
    
    This ensures the generated summary will contain a domain keyword.
    """
    keywords = DOMAIN_KEYWORDS.get(book_type, [])
    if not keywords:
        # Fallback to generic text
        return draw(st.text(min_size=2, max_size=20).filter(lambda x: x.strip()))
    
    keyword = draw(st.sampled_from(keywords))
    # Optionally add prefix/suffix
    prefix = draw(st.text(min_size=0, max_size=5, alphabet=st.characters(
        whitelist_categories=('L',),
    )))
    suffix = draw(st.text(min_size=0, max_size=5, alphabet=st.characters(
        whitelist_categories=('L',),
    )))
    
    return f"{prefix}{keyword}{suffix}".strip() or keyword


@st.composite
def snippet_with_keyword_strategy(draw, book_type: str):
    """
    Generate a NarrativeSnippet with trigger containing a domain keyword.
    """
    trigger = draw(trigger_with_keyword_strategy(book_type))
    
    return NarrativeSnippet(
        snippet_id=draw(snippet_id_strategy),
        trigger=trigger,
        factor_trigger=draw(st.one_of(st.none(), st.text(min_size=1, max_size=20))),
        role=draw(snippet_role_strategy),
        snippet_text=f"Text about {trigger}",
        source_ref=draw(source_ref_strategy),
    )


@st.composite
def node_with_snippets_strategy(draw, book_type: str, min_snippets: int = 1, max_snippets: int = 5):
    """
    Generate a LogicNode with associated snippets containing domain keywords.
    """
    num_snippets = draw(st.integers(min_value=min_snippets, max_value=max_snippets))
    
    snippets = []
    for i in range(num_snippets):
        snippet = draw(snippet_with_keyword_strategy(book_type))
        # Ensure unique snippet_ids
        snippet.snippet_id = f"ns_test_{i:03d}"
        snippets.append(snippet)
    
    node_role = draw(node_role_strategy)
    
    node = LogicNode(
        node_id=f"n_test_chapter_{draw(st.integers(min_value=0, max_value=99))}",
        snippet_ids=[s.snippet_id for s in snippets],
        role=node_role,
        condition=None,
        summary="placeholder",  # Will be replaced by generator
        metadata={"source_ref": "《测试》#章节"},
    )
    
    return node, snippets, book_type


@st.composite
def snippet_text_with_keyword_strategy(draw, book_type: str):
    """
    Generate snippet text that contains a domain keyword.
    """
    keywords = DOMAIN_KEYWORDS.get(book_type, [])
    if not keywords:
        return draw(st.text(min_size=10, max_size=50).filter(lambda x: x.strip()))
    
    keyword = draw(st.sampled_from(keywords))
    prefix = draw(st.text(min_size=5, max_size=20, alphabet=st.characters(
        whitelist_categories=('L', 'N'),
        whitelist_characters=' '
    )))
    suffix = draw(st.text(min_size=5, max_size=20, alphabet=st.characters(
        whitelist_categories=('L', 'N'),
        whitelist_characters=' '
    )))
    
    return f"{prefix} {keyword} {suffix}".strip()


# =============================================================================
# Property 16: Summary Semantic Completeness
# =============================================================================

class TestSummarySemanticCompleteness:
    """
    **Feature: logic-chain-builder, Property 16: Summary Semantic Completeness**
    **Validates: Requirements 15.2, 15.3, 15.5**
    
    *For any* agent-generated summary, it should be <= 50 characters and 
    contain at least one domain keyword relevant to the book type.
    """

    @settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
    @given(data=st.data())
    def test_summary_length_constraint(self, data):
        """
        **Feature: logic-chain-builder, Property 16: Summary Semantic Completeness**
        **Validates: Requirements 15.2**
        
        Property: All generated summaries should be <= 50 characters.
        """
        book_type = data.draw(book_type_strategy)
        node, snippets, _ = data.draw(node_with_snippets_strategy(book_type))
        
        generator = IntelligentSummaryGenerator()
        summary = generator.generate_summary(
            node=node,
            snippets=snippets,
            book_type=book_type,
            include_role_prefix=True
        )
        
        assert len(summary) <= MAX_SUMMARY_LENGTH, (
            f"Summary exceeds max length: '{summary}' ({len(summary)} chars)"
        )

    @settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
    @given(data=st.data())
    def test_summary_contains_domain_keyword_when_present_in_input(self, data):
        """
        **Feature: logic-chain-builder, Property 16: Summary Semantic Completeness**
        **Validates: Requirements 15.5**
        
        Property: When snippets contain domain keywords, the generated summary
        should contain at least one domain keyword.
        """
        book_type = data.draw(book_type_strategy)
        node, snippets, _ = data.draw(node_with_snippets_strategy(book_type))
        
        # Verify input contains keywords (our strategy guarantees this)
        keywords = DOMAIN_KEYWORDS.get(book_type, [])
        assume(len(keywords) > 0)
        
        generator = IntelligentSummaryGenerator()
        summary = generator.generate_summary(
            node=node,
            snippets=snippets,
            book_type=book_type,
            include_role_prefix=True
        )
        
        # Check if summary contains any domain keyword
        has_keyword = generator.has_domain_keyword(summary, book_type)
        
        assert has_keyword, (
            f"Summary '{summary}' does not contain any domain keyword for {book_type}.\n"
            f"Available keywords: {keywords[:10]}...\n"
            f"Snippet triggers: {[s.trigger for s in snippets]}"
        )

    @settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
    @given(data=st.data())
    def test_summary_reflects_role_when_prefix_enabled(self, data):
        """
        **Feature: logic-chain-builder, Property 16: Summary Semantic Completeness**
        **Validates: Requirements 15.3**
        
        Property: When role prefix is enabled, summary should contain the role prefix.
        """
        book_type = data.draw(book_type_strategy)
        node, snippets, _ = data.draw(node_with_snippets_strategy(book_type))
        
        generator = IntelligentSummaryGenerator()
        summary = generator.generate_summary(
            node=node,
            snippets=snippets,
            book_type=book_type,
            include_role_prefix=True
        )
        
        expected_prefix = ROLE_PREFIXES.get(node.role, "")
        
        # If there's an expected prefix and summary is long enough
        if expected_prefix:
            # The prefix should be at the start of the summary
            # (unless truncation removed it, which shouldn't happen for short prefixes)
            assert summary.startswith(expected_prefix) or len(summary) < len(expected_prefix), (
                f"Summary '{summary}' should start with role prefix '{expected_prefix}' "
                f"for role {node.role}"
            )


class TestSummaryGeneratorBasicFunctionality:
    """
    Basic functionality tests for IntelligentSummaryGenerator.
    """

    def test_empty_snippets_returns_placeholder(self):
        """Empty snippet list should return placeholder summary."""
        generator = IntelligentSummaryGenerator()
        
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            condition=None,
            summary="placeholder",
            metadata={},
        )
        
        summary = generator.generate_summary(
            node=node,
            snippets=[],
            book_type="命理",
            include_role_prefix=False
        )
        
        assert summary == "空节点"

    def test_missing_snippets_returns_placeholder(self):
        """Node with snippet_ids not in snippets list should return placeholder."""
        generator = IntelligentSummaryGenerator()
        
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=["ns_missing_001", "ns_missing_002"],
            role=SnippetRole.MAIN,
            condition=None,
            summary="placeholder",
            metadata={},
        )
        
        summary = generator.generate_summary(
            node=node,
            snippets=[],  # No matching snippets
            book_type="命理",
            include_role_prefix=False
        )
        
        assert summary == "空节点"

    def test_truncation_with_ellipsis(self):
        """Long text should be truncated with ellipsis."""
        generator = IntelligentSummaryGenerator(max_length=20)
        
        long_trigger = "这是一个非常非常非常长的触发器文本需要被截断"
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger=long_trigger,
            factor_trigger=None,
            role=ExtractorSnippetRole.MAIN,
            snippet_text="Some text",
            source_ref="《测试》#章节",
        )
        
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            condition=None,
            summary="placeholder",
            metadata={},
        )
        
        summary = generator.generate_summary(
            node=node,
            snippets=[snippet],
            book_type="命理",
            include_role_prefix=False
        )
        
        assert len(summary) <= 20
        assert summary.endswith("...")

    def test_domain_keywords_detection(self):
        """Should correctly detect domain keywords in text."""
        generator = IntelligentSummaryGenerator()
        
        # Test 命理 keywords
        assert generator.has_domain_keyword("格局分析", "命理")
        assert generator.has_domain_keyword("用神选择", "命理")
        assert not generator.has_domain_keyword("普通文本", "命理")
        
        # Test 占卜 keywords
        assert generator.has_domain_keyword("卦象解读", "占卜")
        assert generator.has_domain_keyword("大阿卡纳牌", "占卜")
        
        # Test 梦学 keywords
        assert generator.has_domain_keyword("象征意义", "梦学")
        assert generator.has_domain_keyword("潜意识分析", "梦学")
        
        # Test 西方占星 keywords
        assert generator.has_domain_keyword("行星相位", "西方占星")
        assert generator.has_domain_keyword("transit analysis", "西方占星")

    def test_role_prefix_included(self):
        """Role prefix should be included when enabled."""
        generator = IntelligentSummaryGenerator()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="格局",
            factor_trigger=None,
            role=ExtractorSnippetRole.MAIN,
            snippet_text="格局分析",
            source_ref="《测试》#章节",
        )
        
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            condition=None,
            summary="placeholder",
            metadata={},
        )
        
        summary_with_prefix = generator.generate_summary(
            node=node,
            snippets=[snippet],
            book_type="命理",
            include_role_prefix=True
        )
        
        summary_without_prefix = generator.generate_summary(
            node=node,
            snippets=[snippet],
            book_type="命理",
            include_role_prefix=False
        )
        
        assert summary_with_prefix.startswith("【核心】")
        assert not summary_without_prefix.startswith("【核心】")

    def test_generate_summary_for_book(self):
        """Should correctly look up book type from book_id."""
        generator = IntelligentSummaryGenerator()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="格局",
            factor_trigger=None,
            role=ExtractorSnippetRole.MAIN,
            snippet_text="格局分析",
            source_ref="《滴天髓》#章节",
        )
        
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            condition=None,
            summary="placeholder",
            metadata={},
        )
        
        # 滴天髓 is a 命理 book
        summary = generator.generate_summary_for_book(
            node=node,
            snippets=[snippet],
            book_id="滴天髓",
            include_role_prefix=True
        )
        
        assert len(summary) <= MAX_SUMMARY_LENGTH
        assert generator.has_domain_keyword(summary, "命理")


class TestSummaryImprovement:
    """Tests for summary improvement functionality."""

    def test_improve_existing_summary(self):
        """Should improve summary when new one is better."""
        generator = IntelligentSummaryGenerator()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="格局分析",
            factor_trigger=None,
            role=ExtractorSnippetRole.MAIN,
            snippet_text="格局分析详解",
            source_ref="《测试》#章节",
        )
        
        # Node with poor summary (no keywords, no prefix)
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            condition=None,
            summary="普通文本",  # No domain keywords
            metadata={},
        )
        
        improved_summary, was_changed = generator.improve_existing_summary(
            node=node,
            snippets=[snippet],
            book_type="命理"
        )
        
        # Should be changed because new summary has keywords
        assert was_changed
        assert generator.has_domain_keyword(improved_summary, "命理")

    def test_no_improvement_when_current_is_good(self):
        """Should not change summary when current is already good."""
        generator = IntelligentSummaryGenerator()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="普通触发",
            factor_trigger=None,
            role=ExtractorSnippetRole.MAIN,
            snippet_text="普通文本",
            source_ref="《测试》#章节",
        )
        
        # Node with good summary (has keyword and prefix)
        node = LogicNode(
            node_id="n_test_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            condition=None,
            summary="【核心】格局分析",  # Already has keyword and prefix
            metadata={},
        )
        
        improved_summary, was_changed = generator.improve_existing_summary(
            node=node,
            snippets=[snippet],
            book_type="命理"
        )
        
        # Should not be changed because current is already good
        assert not was_changed
        assert improved_summary == "【核心】格局分析"


class TestDomainKeywordCoverage:
    """Tests to verify domain keyword coverage for all book types."""

    @pytest.mark.parametrize("book_type", ["命理", "占卜", "梦学", "西方占星"])
    def test_each_book_type_has_keywords(self, book_type):
        """Each book type should have domain keywords defined."""
        keywords = DOMAIN_KEYWORDS.get(book_type, [])
        assert len(keywords) > 0, f"No keywords defined for book type: {book_type}"

    @pytest.mark.parametrize("book_type,expected_keyword", [
        ("命理", "格局"),
        ("命理", "用神"),
        ("占卜", "卦象"),
        ("占卜", "塔罗"),
        ("梦学", "象征"),
        ("梦学", "潜意识"),
        ("西方占星", "行星"),
        ("西方占星", "宫位"),
    ])
    def test_specific_keywords_present(self, book_type, expected_keyword):
        """Specific important keywords should be present for each book type."""
        keywords = DOMAIN_KEYWORDS.get(book_type, [])
        assert expected_keyword in keywords, (
            f"Expected keyword '{expected_keyword}' not found in {book_type} keywords"
        )
