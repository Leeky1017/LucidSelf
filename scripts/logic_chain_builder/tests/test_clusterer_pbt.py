# scripts/logic_chain_builder/tests/test_clusterer_pbt.py
"""
Property-Based Tests for SnippetClusterer

Tests the core clustering and node creation functionality using Hypothesis.
"""

import re
from typing import List

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.clusterer import SnippetClusterer, EMPTY_SOURCE_REF_PLACEHOLDER
from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.constants import ROLE_PRIORITY, MAX_SUMMARY_LENGTH
from scripts.schema_extractor.models import NarrativeSnippet, SnippetRole as ExtractorSnippetRole


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for valid snippet roles
snippet_role_strategy = st.sampled_from([role for role in ExtractorSnippetRole])

# Strategy for snippet IDs
snippet_id_strategy = st.from_regex(r"ns_[a-z]{2,5}_\d{3}", fullmatch=True)

# Strategy for trigger text (non-empty)
trigger_strategy = st.text(
    min_size=1, 
    max_size=50, 
    alphabet=st.characters(
        whitelist_categories=('L', 'N', 'P'),
        whitelist_characters=' '
    )
).filter(lambda x: x.strip())

# Strategy for snippet text (non-empty)
snippet_text_strategy = st.text(
    min_size=5, 
    max_size=200, 
    alphabet=st.characters(
        whitelist_categories=('L', 'N', 'P'),
        whitelist_characters=' '
    )
).filter(lambda x: x.strip())

# Strategy for source reference (Chinese format)
source_ref_chinese_strategy = st.builds(
    lambda book, chapter: f"《{book}》#{chapter}",
    book=st.text(min_size=2, max_size=10, alphabet=st.characters(
        whitelist_categories=('L',),
    )).filter(lambda x: x.strip()),
    chapter=st.text(min_size=1, max_size=20, alphabet=st.characters(
        whitelist_categories=('L', 'N'),
    )).filter(lambda x: x.strip())
)

# Strategy for source reference (English format)
source_ref_english_strategy = st.builds(
    lambda book, chapter: f"{book}#Chapter {chapter}",
    book=st.text(min_size=2, max_size=20, alphabet=st.characters(
        whitelist_categories=('L',),
        whitelist_characters=' _'
    )).filter(lambda x: x.strip()),
    chapter=st.integers(min_value=1, max_value=100)
)

# Combined source_ref strategy
source_ref_strategy = st.one_of(source_ref_chinese_strategy, source_ref_english_strategy)


@st.composite
def snippet_strategy(draw, source_ref=None):
    """Generate a valid NarrativeSnippet."""
    return NarrativeSnippet(
        snippet_id=draw(snippet_id_strategy),
        trigger=draw(trigger_strategy),
        factor_trigger=draw(st.one_of(st.none(), trigger_strategy)),
        role=draw(snippet_role_strategy),
        snippet_text=draw(snippet_text_strategy),
        source_ref=source_ref if source_ref else draw(source_ref_strategy),
    )


@st.composite
def snippets_with_same_source_ref_strategy(draw, min_size=1, max_size=5):
    """Generate a list of snippets with the same source_ref."""
    source_ref = draw(source_ref_strategy)
    count = draw(st.integers(min_value=min_size, max_value=max_size))
    snippets = []
    for i in range(count):
        snippet = draw(snippet_strategy(source_ref=source_ref))
        # Ensure unique snippet_ids
        snippet.snippet_id = f"ns_test_{i:03d}"
        snippets.append(snippet)
    return snippets


@st.composite
def snippets_with_multiple_source_refs_strategy(draw, min_groups=2, max_groups=5):
    """Generate snippets with multiple different source_refs."""
    num_groups = draw(st.integers(min_value=min_groups, max_value=max_groups))
    all_snippets = []
    snippet_counter = 0
    
    for _ in range(num_groups):
        source_ref = draw(source_ref_strategy)
        group_size = draw(st.integers(min_value=1, max_value=3))
        
        for _ in range(group_size):
            snippet = draw(snippet_strategy(source_ref=source_ref))
            snippet.snippet_id = f"ns_test_{snippet_counter:03d}"
            snippet_counter += 1
            all_snippets.append(snippet)
    
    return all_snippets


# =============================================================================
# Property 1: Snippet Grouping Consistency
# =============================================================================

class TestSnippetGroupingConsistency:
    """
    **Feature: logic-chain-builder, Property 1: Snippet Grouping Consistency**
    **Validates: Requirements 2.1, 2.2**
    
    *For any* set of snippets with the same `source_ref`, all their `snippet_id`s 
    should appear in exactly one LogicNode's `snippet_ids` list.
    """

    @settings(max_examples=100)
    @given(snippets=snippets_with_same_source_ref_strategy(min_size=1, max_size=10))
    def test_same_source_ref_grouped_together(self, snippets: List[NarrativeSnippet]):
        """
        **Feature: logic-chain-builder, Property 1: Snippet Grouping Consistency**
        **Validates: Requirements 2.1, 2.2**
        
        Property: All snippets with the same source_ref should be grouped together.
        """
        clusterer = SnippetClusterer()
        groups = clusterer.cluster_by_source_ref(snippets)
        
        # All snippets have the same source_ref, so there should be exactly 1 group
        assert len(groups) == 1
        
        # The group should contain all snippets
        group_snippets = list(groups.values())[0]
        assert len(group_snippets) == len(snippets)
        
        # All snippet_ids should be present
        input_ids = {s.snippet_id for s in snippets}
        output_ids = {s.snippet_id for s in group_snippets}
        assert input_ids == output_ids

    @settings(max_examples=100)
    @given(snippets=snippets_with_multiple_source_refs_strategy(min_groups=2, max_groups=5))
    def test_different_source_refs_grouped_separately(self, snippets: List[NarrativeSnippet]):
        """
        **Feature: logic-chain-builder, Property 1: Snippet Grouping Consistency**
        **Validates: Requirements 2.1, 2.2**
        
        Property: Snippets with different source_refs should be in different groups.
        """
        clusterer = SnippetClusterer()
        groups = clusterer.cluster_by_source_ref(snippets)
        
        # Count unique source_refs in input
        unique_refs = set(s.source_ref for s in snippets)
        
        # Number of groups should equal number of unique source_refs
        assert len(groups) == len(unique_refs)
        
        # Each snippet should appear in exactly one group
        all_grouped_ids = []
        for group in groups.values():
            all_grouped_ids.extend(s.snippet_id for s in group)
        
        input_ids = [s.snippet_id for s in snippets]
        assert sorted(all_grouped_ids) == sorted(input_ids)

    @settings(max_examples=100)
    @given(snippets=st.lists(snippet_strategy(), min_size=1, max_size=20))
    def test_no_snippet_lost_or_duplicated(self, snippets: List[NarrativeSnippet]):
        """
        **Feature: logic-chain-builder, Property 1: Snippet Grouping Consistency**
        **Validates: Requirements 2.1, 2.2**
        
        Property: After grouping, no snippet should be lost or duplicated.
        """
        # Ensure unique snippet_ids
        for i, s in enumerate(snippets):
            s.snippet_id = f"ns_test_{i:03d}"
        
        clusterer = SnippetClusterer()
        groups = clusterer.cluster_by_source_ref(snippets)
        
        # Collect all snippet_ids from groups
        grouped_ids = []
        for group in groups.values():
            grouped_ids.extend(s.snippet_id for s in group)
        
        # Should have same count (no loss)
        assert len(grouped_ids) == len(snippets)
        
        # Should have no duplicates
        assert len(grouped_ids) == len(set(grouped_ids))
        
        # Should match input ids
        input_ids = {s.snippet_id for s in snippets}
        assert set(grouped_ids) == input_ids


class TestEmptySourceRefHandling:
    """
    Tests for edge cases with empty/None source_ref.
    
    **Validates: Requirements 2.1**
    """

    def test_empty_source_ref_grouped_together(self):
        """Property: Snippets with empty source_ref should be grouped together."""
        snippets = [
            NarrativeSnippet(
                snippet_id="ns_test_001",
                trigger="trigger1",
                role=ExtractorSnippetRole.MAIN,
                snippet_text="text1",
                source_ref=""
            ),
            NarrativeSnippet(
                snippet_id="ns_test_002",
                trigger="trigger2",
                role=ExtractorSnippetRole.SUMMARY,
                snippet_text="text2",
                source_ref=""
            ),
        ]
        
        clusterer = SnippetClusterer()
        groups = clusterer.cluster_by_source_ref(snippets)
        
        # Should have exactly 1 group (empty source_refs grouped together)
        assert len(groups) == 1
        assert EMPTY_SOURCE_REF_PLACEHOLDER in groups
        assert len(groups[EMPTY_SOURCE_REF_PLACEHOLDER]) == 2

    def test_whitespace_source_ref_treated_as_empty(self):
        """Property: Whitespace-only source_ref should be treated as empty."""
        snippets = [
            NarrativeSnippet(
                snippet_id="ns_test_001",
                trigger="trigger1",
                role=ExtractorSnippetRole.MAIN,
                snippet_text="text1",
                source_ref="   "
            ),
            NarrativeSnippet(
                snippet_id="ns_test_002",
                trigger="trigger2",
                role=ExtractorSnippetRole.SUMMARY,
                snippet_text="text2",
                source_ref="\t\n"
            ),
        ]
        
        clusterer = SnippetClusterer()
        groups = clusterer.cluster_by_source_ref(snippets)
        
        # Should have exactly 1 group
        assert len(groups) == 1
        assert EMPTY_SOURCE_REF_PLACEHOLDER in groups


# =============================================================================
# Property 2: Node ID Format Compliance
# =============================================================================

class TestNodeIdFormatCompliance:
    """
    **Feature: logic-chain-builder, Property 2: Node ID Format Compliance**
    **Validates: Requirements 2.3**
    
    *For any* generated LogicNode, its `node_id` should match the pattern
    `n_{book_abbr}_{chapter}_{seq}` where:
    - book_abbr: lowercase alphanumeric or Chinese characters
    - chapter: lowercase alphanumeric, Chinese characters, or underscores
    - seq: non-negative integer
    """

    # Pattern that allows Chinese characters in book_abbr and chapter
    NODE_ID_PATTERN = re.compile(
        r'^n_[a-z0-9\u4e00-\u9fff]+_[a-z0-9_\u4e00-\u9fff]+_\d+$'
    )

    @settings(max_examples=100)
    @given(
        book_abbr=st.one_of(
            st.from_regex(r"[a-z][a-z0-9_]*", fullmatch=True),
            st.text(min_size=2, max_size=10, alphabet=st.characters(
                whitelist_categories=('L',),
                min_codepoint=0x4e00,
                max_codepoint=0x9fff
            ))
        ),
        chapter=st.one_of(
            st.from_regex(r"[a-z][a-z0-9_]*", fullmatch=True),
            st.text(min_size=1, max_size=10, alphabet=st.characters(
                whitelist_categories=('L',),
                min_codepoint=0x4e00,
                max_codepoint=0x9fff
            ))
        ),
        seq=st.integers(min_value=0, max_value=9999),
        snippets=snippets_with_same_source_ref_strategy(min_size=1, max_size=5)
    )
    def test_node_id_matches_pattern(
        self, 
        book_abbr: str, 
        chapter: str, 
        seq: int, 
        snippets: List[NarrativeSnippet]
    ):
        """
        **Feature: logic-chain-builder, Property 2: Node ID Format Compliance**
        **Validates: Requirements 2.3**
        
        Property: Generated node_id should match the expected pattern.
        """
        assume(book_abbr.strip())  # Non-empty book_abbr
        assume(chapter.strip())    # Non-empty chapter
        
        clusterer = SnippetClusterer()
        node = clusterer.create_node(book_abbr, chapter, seq, snippets)
        
        # Node ID should match the pattern
        assert self.NODE_ID_PATTERN.match(node.node_id), (
            f"Node ID '{node.node_id}' does not match expected pattern"
        )
        
        # Node ID should contain the sequence number at the end
        assert node.node_id.endswith(f"_{seq}"), (
            f"Node ID '{node.node_id}' should end with '_{seq}'"
        )

    @settings(max_examples=50)
    @given(
        seq=st.integers(min_value=0, max_value=9999),
        snippets=snippets_with_same_source_ref_strategy(min_size=1, max_size=3)
    )
    def test_node_id_unique_per_seq(
        self, 
        seq: int, 
        snippets: List[NarrativeSnippet]
    ):
        """
        **Feature: logic-chain-builder, Property 2: Node ID Format Compliance**
        **Validates: Requirements 2.3**
        
        Property: Different seq values should produce different node_ids.
        """
        clusterer = SnippetClusterer()
        
        node1 = clusterer.create_node("test", "chapter", seq, snippets)
        node2 = clusterer.create_node("test", "chapter", seq + 1, snippets)
        
        assert node1.node_id != node2.node_id


# =============================================================================
# Property 3: Summary Length Constraint
# =============================================================================

class TestSummaryLengthConstraint:
    """
    **Feature: logic-chain-builder, Property 3: Summary Length Constraint**
    **Validates: Requirements 2.4**
    
    *For any* generated LogicNode, its `summary` field should have length <= 50 characters.
    """

    @settings(max_examples=100)
    @given(snippets=snippets_with_same_source_ref_strategy(min_size=1, max_size=10))
    def test_summary_length_within_limit(self, snippets: List[NarrativeSnippet]):
        """
        **Feature: logic-chain-builder, Property 3: Summary Length Constraint**
        **Validates: Requirements 2.4**
        
        Property: Node summary should never exceed 50 characters.
        """
        clusterer = SnippetClusterer()
        node = clusterer.create_node("test", "chapter", 0, snippets)
        
        assert len(node.summary) <= MAX_SUMMARY_LENGTH, (
            f"Summary length {len(node.summary)} exceeds max {MAX_SUMMARY_LENGTH}"
        )

    @settings(max_examples=50)
    @given(
        trigger_length=st.integers(min_value=51, max_value=200),
        text_length=st.integers(min_value=51, max_value=200)
    )
    def test_long_content_truncated(self, trigger_length: int, text_length: int):
        """
        **Feature: logic-chain-builder, Property 3: Summary Length Constraint**
        **Validates: Requirements 2.4**
        
        Property: Even with very long trigger/text, summary should be truncated.
        """
        # Create snippet with long content
        long_trigger = "测" * trigger_length
        long_text = "内" * text_length
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger=long_trigger,
            role=ExtractorSnippetRole.MAIN,
            snippet_text=long_text,
            source_ref="《测试》#章节"
        )
        
        clusterer = SnippetClusterer()
        node = clusterer.create_node("test", "chapter", 0, [snippet])
        
        assert len(node.summary) <= MAX_SUMMARY_LENGTH, (
            f"Summary length {len(node.summary)} exceeds max {MAX_SUMMARY_LENGTH}"
        )

    def test_empty_snippets_has_valid_summary(self):
        """Property: Empty snippet list should produce a valid summary."""
        clusterer = SnippetClusterer()
        node = clusterer.create_node("test", "chapter", 0, [])
        
        assert len(node.summary) <= MAX_SUMMARY_LENGTH
        assert node.summary  # Should not be empty

    def test_snippets_without_trigger_uses_text(self):
        """Property: Snippets without trigger should use snippet_text for summary."""
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="",  # Empty trigger
            role=ExtractorSnippetRole.MAIN,
            snippet_text="这是一段测试内容",
            source_ref="《测试》#章节"
        )
        
        clusterer = SnippetClusterer()
        node = clusterer.create_node("test", "chapter", 0, [snippet])
        
        assert len(node.summary) <= MAX_SUMMARY_LENGTH
        # Summary should come from snippet_text since trigger is empty
        assert "测试" in node.summary or node.summary == "无内容"


# =============================================================================
# Property 4: Role Priority Resolution
# =============================================================================

class TestRolePriorityResolution:
    """
    **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
    **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**
    
    *For any* LogicNode containing snippets with mixed roles, the node's role 
    should be the highest priority among: 主干 > 主干依赖 > 条件分支 > 例外处理 > 总结.
    """

    # Role priority mapping (lower number = higher priority)
    ROLE_PRIORITY_ORDER = [
        ExtractorSnippetRole.MAIN,           # 主干 (priority 1)
        ExtractorSnippetRole.MAIN_DEPENDENCY, # 主干依赖 (priority 2)
        ExtractorSnippetRole.CONDITION_BRANCH, # 条件分支 (priority 3)
        ExtractorSnippetRole.EXCEPTION,       # 例外处理 (priority 4)
        ExtractorSnippetRole.SUMMARY,         # 总结 (priority 5)
    ]

    def _get_expected_role(self, roles: List[ExtractorSnippetRole]) -> SnippetRole:
        """Get the expected highest priority role from a list of roles."""
        if not roles:
            return SnippetRole.SUMMARY
        
        for priority_role in self.ROLE_PRIORITY_ORDER:
            if priority_role in roles:
                return SnippetRole(priority_role.value)
        
        return SnippetRole.SUMMARY

    @settings(max_examples=100)
    @given(
        roles=st.lists(
            st.sampled_from(list(ExtractorSnippetRole)),
            min_size=1,
            max_size=10
        )
    )
    def test_highest_priority_role_selected(self, roles: List[ExtractorSnippetRole]):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5**
        
        Property: The node role should be the highest priority role among all snippets.
        """
        # Create snippets with the given roles
        snippets = []
        for i, role in enumerate(roles):
            snippet = NarrativeSnippet(
                snippet_id=f"ns_test_{i:03d}",
                trigger=f"trigger_{i}",
                role=role,
                snippet_text=f"text_{i}",
                source_ref="《测试》#章节"
            )
            snippets.append(snippet)
        
        clusterer = SnippetClusterer()
        actual_role = clusterer.determine_node_role(snippets)
        expected_role = self._get_expected_role(roles)
        
        assert actual_role == expected_role, (
            f"Expected role {expected_role} but got {actual_role} "
            f"for roles {[r.value for r in roles]}"
        )

    def test_main_wins_over_all(self):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.1**
        
        Property: 主干 should always win over any other role.
        """
        clusterer = SnippetClusterer()
        
        for other_role in self.ROLE_PRIORITY_ORDER[1:]:  # All roles except MAIN
            snippets = [
                NarrativeSnippet(
                    snippet_id="ns_test_001",
                    trigger="t1",
                    role=ExtractorSnippetRole.MAIN,
                    snippet_text="text1",
                    source_ref="ref"
                ),
                NarrativeSnippet(
                    snippet_id="ns_test_002",
                    trigger="t2",
                    role=other_role,
                    snippet_text="text2",
                    source_ref="ref"
                ),
            ]
            
            role = clusterer.determine_node_role(snippets)
            assert role == SnippetRole.MAIN, (
                f"主干 should win over {other_role.value}, but got {role}"
            )

    def test_main_dependency_wins_over_lower_priority(self):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.2**
        
        Property: 主干依赖 should win over 条件分支, 例外处理, and 总结.
        """
        clusterer = SnippetClusterer()
        
        lower_priority_roles = [
            ExtractorSnippetRole.CONDITION_BRANCH,
            ExtractorSnippetRole.EXCEPTION,
            ExtractorSnippetRole.SUMMARY,
        ]
        
        for other_role in lower_priority_roles:
            snippets = [
                NarrativeSnippet(
                    snippet_id="ns_test_001",
                    trigger="t1",
                    role=ExtractorSnippetRole.MAIN_DEPENDENCY,
                    snippet_text="text1",
                    source_ref="ref"
                ),
                NarrativeSnippet(
                    snippet_id="ns_test_002",
                    trigger="t2",
                    role=other_role,
                    snippet_text="text2",
                    source_ref="ref"
                ),
            ]
            
            role = clusterer.determine_node_role(snippets)
            assert role == SnippetRole.MAIN_DEPENDENCY, (
                f"主干依赖 should win over {other_role.value}, but got {role}"
            )

    def test_condition_branch_wins_over_lower_priority(self):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.3**
        
        Property: 条件分支 should win over 例外处理 and 总结.
        """
        clusterer = SnippetClusterer()
        
        lower_priority_roles = [
            ExtractorSnippetRole.EXCEPTION,
            ExtractorSnippetRole.SUMMARY,
        ]
        
        for other_role in lower_priority_roles:
            snippets = [
                NarrativeSnippet(
                    snippet_id="ns_test_001",
                    trigger="t1",
                    role=ExtractorSnippetRole.CONDITION_BRANCH,
                    snippet_text="text1",
                    source_ref="ref"
                ),
                NarrativeSnippet(
                    snippet_id="ns_test_002",
                    trigger="t2",
                    role=other_role,
                    snippet_text="text2",
                    source_ref="ref"
                ),
            ]
            
            role = clusterer.determine_node_role(snippets)
            assert role == SnippetRole.CONDITION_BRANCH, (
                f"条件分支 should win over {other_role.value}, but got {role}"
            )

    def test_exception_wins_over_summary(self):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.4**
        
        Property: 例外处理 should win over 总结.
        """
        clusterer = SnippetClusterer()
        
        snippets = [
            NarrativeSnippet(
                snippet_id="ns_test_001",
                trigger="t1",
                role=ExtractorSnippetRole.EXCEPTION,
                snippet_text="text1",
                source_ref="ref"
            ),
            NarrativeSnippet(
                snippet_id="ns_test_002",
                trigger="t2",
                role=ExtractorSnippetRole.SUMMARY,
                snippet_text="text2",
                source_ref="ref"
            ),
        ]
        
        role = clusterer.determine_node_role(snippets)
        assert role == SnippetRole.EXCEPTION, (
            f"例外处理 should win over 总结, but got {role}"
        )

    def test_summary_is_lowest_priority(self):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.5**
        
        Property: 总结 should only be selected when no other roles are present.
        """
        clusterer = SnippetClusterer()
        
        # Only summary snippets
        snippets = [
            NarrativeSnippet(
                snippet_id="ns_test_001",
                trigger="t1",
                role=ExtractorSnippetRole.SUMMARY,
                snippet_text="text1",
                source_ref="ref"
            ),
            NarrativeSnippet(
                snippet_id="ns_test_002",
                trigger="t2",
                role=ExtractorSnippetRole.SUMMARY,
                snippet_text="text2",
                source_ref="ref"
            ),
        ]
        
        role = clusterer.determine_node_role(snippets)
        assert role == SnippetRole.SUMMARY

    def test_empty_snippets_returns_summary(self):
        """
        **Feature: logic-chain-builder, Property 4: Role Priority Resolution**
        **Validates: Requirements 3.5**
        
        Property: Empty snippet list should default to 总结 role.
        """
        clusterer = SnippetClusterer()
        role = clusterer.determine_node_role([])
        assert role == SnippetRole.SUMMARY


class TestEntryTerminalNodeCandidates:
    """
    Tests for entry and terminal node candidate detection.
    
    **Validates: Requirements 2.5, 3.4**
    """

    def test_main_role_is_entry_candidate(self):
        """Property: Nodes with role=主干 should be entry node candidates."""
        clusterer = SnippetClusterer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="t",
            role=ExtractorSnippetRole.MAIN,
            snippet_text="text",
            source_ref="ref"
        )
        
        node = clusterer.create_node("test", "ch", 0, [snippet])
        assert clusterer.is_entry_node_candidate(node)

    def test_summary_role_is_terminal_candidate(self):
        """Property: Nodes with role=总结 should be terminal node candidates."""
        clusterer = SnippetClusterer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="t",
            role=ExtractorSnippetRole.SUMMARY,
            snippet_text="text",
            source_ref="ref"
        )
        
        node = clusterer.create_node("test", "ch", 0, [snippet])
        assert clusterer.is_terminal_node_candidate(node)

    def test_non_main_not_entry_candidate(self):
        """Property: Nodes without role=主干 should not be entry candidates."""
        clusterer = SnippetClusterer()
        
        for role in [
            ExtractorSnippetRole.MAIN_DEPENDENCY,
            ExtractorSnippetRole.CONDITION_BRANCH,
            ExtractorSnippetRole.EXCEPTION,
            ExtractorSnippetRole.SUMMARY,
        ]:
            snippet = NarrativeSnippet(
                snippet_id="ns_test_001",
                trigger="t",
                role=role,
                snippet_text="text",
                source_ref="ref"
            )
            
            node = clusterer.create_node("test", "ch", 0, [snippet])
            assert not clusterer.is_entry_node_candidate(node), (
                f"Node with role {role.value} should not be entry candidate"
            )

    def test_non_summary_not_terminal_candidate(self):
        """Property: Nodes without role=总结 should not be terminal candidates."""
        clusterer = SnippetClusterer()
        
        for role in [
            ExtractorSnippetRole.MAIN,
            ExtractorSnippetRole.MAIN_DEPENDENCY,
            ExtractorSnippetRole.CONDITION_BRANCH,
            ExtractorSnippetRole.EXCEPTION,
        ]:
            snippet = NarrativeSnippet(
                snippet_id="ns_test_001",
                trigger="t",
                role=role,
                snippet_text="text",
                source_ref="ref"
            )
            
            node = clusterer.create_node("test", "ch", 0, [snippet])
            assert not clusterer.is_terminal_node_candidate(node), (
                f"Node with role {role.value} should not be terminal candidate"
            )
