# scripts/logic_chain_builder/tests/test_semantic_refiner_pbt.py
"""
Property-Based Tests for SemanticClusterRefiner

Tests the semantic clustering refinement functionality using Hypothesis.
"""

from typing import List, Set

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.semantic_refiner import (
    SemanticClusterRefiner,
    MAX_SNIPPETS_PER_NODE,
    MAX_UNIQUE_TRIGGERS,
)
from scripts.logic_chain_builder.models import (
    LogicNode,
    LogicEdge,
    LogicChain,
    SnippetRole,
    EdgeRelation,
    SourceMetadata,
)
from scripts.schema_extractor.models import (
    NarrativeSnippet,
    SnippetRole as ExtractorSnippetRole,
)


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
    max_size=30,
    alphabet=st.characters(
        whitelist_categories=('L', 'N'),
        whitelist_characters=' '
    )
).filter(lambda x: x.strip())

# Strategy for snippet text (non-empty)
snippet_text_strategy = st.text(
    min_size=5,
    max_size=100,
    alphabet=st.characters(
        whitelist_categories=('L', 'N'),
        whitelist_characters=' '
    )
).filter(lambda x: x.strip())

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
def snippet_strategy(draw, snippet_id: str = None, trigger: str = None):
    """Generate a valid NarrativeSnippet."""
    return NarrativeSnippet(
        snippet_id=snippet_id if snippet_id else draw(snippet_id_strategy),
        trigger=trigger if trigger else draw(trigger_strategy),
        factor_trigger=draw(st.one_of(st.none(), trigger_strategy)),
        role=draw(snippet_role_strategy),
        snippet_text=draw(snippet_text_strategy),
        source_ref=draw(source_ref_strategy),
    )


@st.composite
def heterogeneous_node_strategy(draw, min_snippets=6, max_snippets=15):
    """
    Generate a heterogeneous node with multiple different triggers.
    
    Creates a node that should be identified as heterogeneous due to:
    - Having more than MAX_SNIPPETS_PER_NODE snippets
    - Having more than MAX_UNIQUE_TRIGGERS unique triggers
    """
    # Generate multiple unique triggers
    num_triggers = draw(st.integers(min_value=4, max_value=8))
    triggers = []
    for i in range(num_triggers):
        trigger = draw(trigger_strategy)
        # Ensure uniqueness by appending index
        triggers.append(f"{trigger}_{i}")
    
    # Generate snippets with different triggers
    num_snippets = draw(st.integers(min_value=min_snippets, max_value=max_snippets))
    snippets = []
    
    for i in range(num_snippets):
        trigger = triggers[i % len(triggers)]
        snippet = NarrativeSnippet(
            snippet_id=f"ns_test_{i:03d}",
            trigger=trigger,
            factor_trigger=None,
            role=draw(snippet_role_strategy),
            snippet_text=draw(snippet_text_strategy),
            source_ref="《测试》#章节",
        )
        snippets.append(snippet)
    
    # Create the node
    node = LogicNode(
        node_id="n_test_chapter_0",
        snippet_ids=[s.snippet_id for s in snippets],
        role=SnippetRole.MAIN,
        condition=None,
        summary="测试节点",
        metadata={"source_ref": "《测试》#章节"},
    )
    
    return node, snippets


@st.composite
def homogeneous_node_strategy(draw, min_snippets=1, max_snippets=4):
    """
    Generate a homogeneous node with same trigger and limited role variation.
    
    Creates a node that should NOT be identified as heterogeneous.
    A truly homogeneous node has:
    - Same trigger for all snippets
    - At most 2 different roles (implementation considers >2 roles as heterogeneous)
    - Few snippets (<=5)
    """
    # Use single trigger for all snippets
    trigger = draw(trigger_strategy)
    
    # Use at most 2 roles to avoid being flagged as heterogeneous
    # Pick 1-2 roles and use only those
    available_roles = [ExtractorSnippetRole.MAIN, ExtractorSnippetRole.MAIN_DEPENDENCY]
    role_to_use = draw(st.sampled_from(available_roles))
    
    num_snippets = draw(st.integers(min_value=min_snippets, max_value=max_snippets))
    snippets = []
    
    for i in range(num_snippets):
        snippet = NarrativeSnippet(
            snippet_id=f"ns_test_{i:03d}",
            trigger=trigger,
            factor_trigger=None,
            role=role_to_use,
            snippet_text=draw(snippet_text_strategy),
            source_ref="《测试》#章节",
        )
        snippets.append(snippet)
    
    node = LogicNode(
        node_id="n_test_chapter_0",
        snippet_ids=[s.snippet_id for s in snippets],
        role=SnippetRole.MAIN,
        condition=None,
        summary="测试节点",
        metadata={"source_ref": "《测试》#章节"},
    )
    
    return node, snippets


@st.composite
def node_with_varied_triggers_strategy(draw, num_triggers: int, snippets_per_trigger: int):
    """
    Generate a node with a specific number of triggers and snippets per trigger.
    
    This allows precise control for testing split behavior.
    """
    snippets = []
    snippet_counter = 0
    
    for t in range(num_triggers):
        trigger = f"trigger_{t}"
        for s in range(snippets_per_trigger):
            snippet = NarrativeSnippet(
                snippet_id=f"ns_test_{snippet_counter:03d}",
                trigger=trigger,
                factor_trigger=None,
                role=draw(snippet_role_strategy),
                snippet_text=f"Text for trigger {t}, snippet {s}",
                source_ref="《测试》#章节",
            )
            snippets.append(snippet)
            snippet_counter += 1
    
    node = LogicNode(
        node_id="n_test_chapter_0",
        snippet_ids=[s.snippet_id for s in snippets],
        role=SnippetRole.MAIN,
        condition=None,
        summary="测试节点",
        metadata={"source_ref": "《测试》#章节"},
    )
    
    return node, snippets


# =============================================================================
# Property 15: Node Split Preserves Snippets
# =============================================================================

class TestNodeSplitPreservesSnippets:
    """
    **Feature: logic-chain-builder, Property 15: Node Split Preserves Snippets**
    **Validates: Requirements 14.3, 14.4**
    
    *For any* node split operation, the union of snippet_ids in all resulting 
    nodes should equal the original node's snippet_ids (no snippets lost or duplicated).
    """

    @settings(max_examples=100)
    @given(data=st.data())
    def test_split_preserves_all_snippet_ids(self, data):
        """
        **Feature: logic-chain-builder, Property 15: Node Split Preserves Snippets**
        **Validates: Requirements 14.3, 14.4**
        
        Property: After splitting a node, all original snippet_ids should be 
        present in exactly one of the resulting nodes.
        """
        # Generate a node with multiple triggers (will be split)
        num_triggers = data.draw(st.integers(min_value=2, max_value=5))
        snippets_per_trigger = data.draw(st.integers(min_value=1, max_value=3))
        
        node, snippets = data.draw(
            node_with_varied_triggers_strategy(num_triggers, snippets_per_trigger)
        )
        
        original_snippet_ids = set(node.snippet_ids)
        
        refiner = SemanticClusterRefiner()
        new_nodes = refiner.split_node(node, snippets)
        
        # Collect all snippet_ids from new nodes
        result_snippet_ids: Set[str] = set()
        for new_node in new_nodes:
            result_snippet_ids.update(new_node.snippet_ids)
        
        # Property: No snippets lost
        assert original_snippet_ids == result_snippet_ids, (
            f"Snippet IDs mismatch after split.\n"
            f"Original: {original_snippet_ids}\n"
            f"Result: {result_snippet_ids}\n"
            f"Lost: {original_snippet_ids - result_snippet_ids}\n"
            f"Extra: {result_snippet_ids - original_snippet_ids}"
        )

    @settings(max_examples=100)
    @given(data=st.data())
    def test_split_no_duplicate_snippets(self, data):
        """
        **Feature: logic-chain-builder, Property 15: Node Split Preserves Snippets**
        **Validates: Requirements 14.3, 14.4**
        
        Property: After splitting, no snippet_id should appear in multiple nodes.
        """
        num_triggers = data.draw(st.integers(min_value=2, max_value=5))
        snippets_per_trigger = data.draw(st.integers(min_value=1, max_value=3))
        
        node, snippets = data.draw(
            node_with_varied_triggers_strategy(num_triggers, snippets_per_trigger)
        )
        
        refiner = SemanticClusterRefiner()
        new_nodes = refiner.split_node(node, snippets)
        
        # Check for duplicates across nodes
        all_snippet_ids: List[str] = []
        for new_node in new_nodes:
            all_snippet_ids.extend(new_node.snippet_ids)
        
        # Property: No duplicates
        assert len(all_snippet_ids) == len(set(all_snippet_ids)), (
            f"Duplicate snippet_ids found after split: "
            f"{[sid for sid in all_snippet_ids if all_snippet_ids.count(sid) > 1]}"
        )

    @settings(max_examples=50)
    @given(node_snippets=heterogeneous_node_strategy(min_snippets=6, max_snippets=12))
    def test_heterogeneous_node_split_preserves_count(self, node_snippets):
        """
        **Feature: logic-chain-builder, Property 15: Node Split Preserves Snippets**
        **Validates: Requirements 14.3, 14.4**
        
        Property: Total snippet count should be preserved after split.
        """
        node, snippets = node_snippets
        original_count = len(node.snippet_ids)
        
        refiner = SemanticClusterRefiner()
        new_nodes = refiner.split_node(node, snippets)
        
        # Count total snippets in new nodes
        total_in_new_nodes = sum(len(n.snippet_ids) for n in new_nodes)
        
        assert total_in_new_nodes == original_count, (
            f"Snippet count changed: {original_count} -> {total_in_new_nodes}"
        )

    def test_split_single_trigger_returns_original(self):
        """
        **Feature: logic-chain-builder, Property 15: Node Split Preserves Snippets**
        **Validates: Requirements 14.3**
        
        Property: A node with only one trigger group should not be split.
        """
        # Create node with single trigger
        snippets = [
            NarrativeSnippet(
                snippet_id=f"ns_test_{i:03d}",
                trigger="same_trigger",
                factor_trigger=None,
                role=ExtractorSnippetRole.MAIN,
                snippet_text=f"Text {i}",
                source_ref="《测试》#章节",
            )
            for i in range(5)
        ]
        
        node = LogicNode(
            node_id="n_test_chapter_0",
            snippet_ids=[s.snippet_id for s in snippets],
            role=SnippetRole.MAIN,
            condition=None,
            summary="测试节点",
            metadata={},
        )
        
        refiner = SemanticClusterRefiner()
        new_nodes = refiner.split_node(node, snippets)
        
        # Should return single node (no split)
        assert len(new_nodes) == 1
        assert set(new_nodes[0].snippet_ids) == set(node.snippet_ids)

    def test_split_empty_node_returns_original(self):
        """
        **Feature: logic-chain-builder, Property 15: Node Split Preserves Snippets**
        **Validates: Requirements 14.3**
        
        Property: An empty node should not be split.
        """
        node = LogicNode(
            node_id="n_test_chapter_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            condition=None,
            summary="空节点",
            metadata={},
        )
        
        refiner = SemanticClusterRefiner()
        new_nodes = refiner.split_node(node, [])
        
        assert len(new_nodes) == 1
        assert new_nodes[0].node_id == node.node_id


class TestEdgeUpdateAfterSplit:
    """
    Tests for edge updates after node splits.
    
    **Validates: Requirements 14.4**
    """

    def test_edges_to_split_node_updated(self):
        """
        Property: Edges pointing TO a split node should be updated to point 
        to all new nodes.
        """
        # Create original edges
        edges = [
            LogicEdge(
                from_node="n_other_0",
                to_node="n_test_chapter_0",
                relation=EdgeRelation.LEADS_TO,
                condition=None,
                metadata={},
            )
        ]
        
        # Create new nodes from split
        new_nodes = [
            LogicNode(
                node_id="n_test_chapter_0_split0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                condition=None,
                summary="Split 0",
                metadata={},
            ),
            LogicNode(
                node_id="n_test_chapter_0_split1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.MAIN,
                condition=None,
                summary="Split 1",
                metadata={},
            ),
        ]
        
        refiner = SemanticClusterRefiner()
        updated_edges = refiner.update_edges_after_split(
            edges, "n_test_chapter_0", new_nodes
        )
        
        # Should have 2 edges (one to each new node)
        assert len(updated_edges) == 2
        
        to_nodes = {e.to_node for e in updated_edges}
        assert to_nodes == {"n_test_chapter_0_split0", "n_test_chapter_0_split1"}

    def test_edges_from_split_node_updated(self):
        """
        Property: Edges pointing FROM a split node should be updated to point 
        from the first new node.
        """
        edges = [
            LogicEdge(
                from_node="n_test_chapter_0",
                to_node="n_other_0",
                relation=EdgeRelation.LEADS_TO,
                condition=None,
                metadata={},
            )
        ]
        
        new_nodes = [
            LogicNode(
                node_id="n_test_chapter_0_split0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                condition=None,
                summary="Split 0",
                metadata={},
            ),
            LogicNode(
                node_id="n_test_chapter_0_split1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.MAIN,
                condition=None,
                summary="Split 1",
                metadata={},
            ),
        ]
        
        refiner = SemanticClusterRefiner()
        updated_edges = refiner.update_edges_after_split(
            edges, "n_test_chapter_0", new_nodes
        )
        
        # Should have 1 edge from first new node
        assert len(updated_edges) == 1
        assert updated_edges[0].from_node == "n_test_chapter_0_split0"
        assert updated_edges[0].to_node == "n_other_0"

    def test_unrelated_edges_unchanged(self):
        """
        Property: Edges not involving the split node should remain unchanged.
        """
        edges = [
            LogicEdge(
                from_node="n_other_0",
                to_node="n_other_1",
                relation=EdgeRelation.SUPPORTS,
                condition="some_condition",
                metadata={"key": "value"},
            )
        ]
        
        new_nodes = [
            LogicNode(
                node_id="n_test_chapter_0_split0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                condition=None,
                summary="Split 0",
                metadata={},
            ),
        ]
        
        refiner = SemanticClusterRefiner()
        updated_edges = refiner.update_edges_after_split(
            edges, "n_test_chapter_0", new_nodes
        )
        
        # Edge should be unchanged
        assert len(updated_edges) == 1
        assert updated_edges[0].from_node == "n_other_0"
        assert updated_edges[0].to_node == "n_other_1"
        assert updated_edges[0].condition == "some_condition"


class TestHeterogeneousNodeIdentification:
    """
    Tests for heterogeneous node identification.
    
    **Validates: Requirements 14.1, 14.2**
    """

    @settings(max_examples=50)
    @given(node_snippets=heterogeneous_node_strategy(min_snippets=6, max_snippets=10))
    def test_heterogeneous_node_identified(self, node_snippets):
        """
        Property: Nodes with many snippets and varied triggers should be 
        identified as heterogeneous.
        """
        node, snippets = node_snippets
        
        refiner = SemanticClusterRefiner()
        heterogeneous = refiner.identify_heterogeneous_nodes([node], snippets)
        
        # Should identify the node as heterogeneous
        assert len(heterogeneous) == 1
        assert heterogeneous[0].node_id == node.node_id

    @settings(max_examples=50)
    @given(node_snippets=homogeneous_node_strategy(min_snippets=1, max_snippets=4))
    def test_homogeneous_node_not_identified(self, node_snippets):
        """
        Property: Nodes with few snippets and same trigger should NOT be 
        identified as heterogeneous.
        """
        node, snippets = node_snippets
        
        refiner = SemanticClusterRefiner()
        heterogeneous = refiner.identify_heterogeneous_nodes([node], snippets)
        
        # Should NOT identify the node as heterogeneous
        assert len(heterogeneous) == 0

    def test_empty_node_not_heterogeneous(self):
        """
        Property: Empty nodes should not be identified as heterogeneous.
        """
        node = LogicNode(
            node_id="n_test_chapter_0",
            snippet_ids=[],
            role=SnippetRole.MAIN,
            condition=None,
            summary="空节点",
            metadata={},
        )
        
        refiner = SemanticClusterRefiner()
        heterogeneous = refiner.identify_heterogeneous_nodes([node], [])
        
        assert len(heterogeneous) == 0


class TestRefineChain:
    """
    Integration tests for the refine_chain method.
    
    **Validates: Requirements 14.1, 14.2, 14.3, 14.4, 14.5**
    """

    def test_refine_chain_preserves_all_snippets(self):
        """
        Property: Refining a chain should preserve all snippet_ids across 
        all nodes.
        """
        # Create snippets with multiple triggers
        snippets = []
        for t in range(3):
            for s in range(3):
                idx = t * 3 + s
                snippets.append(NarrativeSnippet(
                    snippet_id=f"ns_test_{idx:03d}",
                    trigger=f"trigger_{t}",
                    factor_trigger=None,
                    role=ExtractorSnippetRole.MAIN,
                    snippet_text=f"Text {idx}",
                    source_ref="《测试》#章节",
                ))
        
        # Create a heterogeneous node
        node = LogicNode(
            node_id="n_test_chapter_0",
            snippet_ids=[s.snippet_id for s in snippets],
            role=SnippetRole.MAIN,
            condition=None,
            summary="测试节点",
            metadata={"source_ref": "《测试》#章节"},
        )
        
        # Create chain
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test",
            nodes=[node],
            edges=[],
            narrative_order=[node.node_id],
            entry_nodes=[node.node_id],
            terminal_nodes=[],
            metadata=SourceMetadata(),
            version="1.0.0",
        )
        
        original_snippet_ids = set(node.snippet_ids)
        
        refiner = SemanticClusterRefiner()
        refined_chain, changes = refiner.refine_chain(chain, snippets)
        
        # Collect all snippet_ids from refined chain
        result_snippet_ids: Set[str] = set()
        for n in refined_chain.nodes:
            result_snippet_ids.update(n.snippet_ids)
        
        assert original_snippet_ids == result_snippet_ids, (
            f"Snippet IDs changed after refine_chain.\n"
            f"Original: {original_snippet_ids}\n"
            f"Result: {result_snippet_ids}"
        )

    def test_refine_chain_updates_narrative_order(self):
        """
        Property: Refining a chain should update narrative_order to include 
        all new node IDs.
        """
        snippets = []
        for t in range(2):
            for s in range(3):
                idx = t * 3 + s
                snippets.append(NarrativeSnippet(
                    snippet_id=f"ns_test_{idx:03d}",
                    trigger=f"trigger_{t}",
                    factor_trigger=None,
                    role=ExtractorSnippetRole.MAIN,
                    snippet_text=f"Text {idx}",
                    source_ref="《测试》#章节",
                ))
        
        node = LogicNode(
            node_id="n_test_chapter_0",
            snippet_ids=[s.snippet_id for s in snippets],
            role=SnippetRole.MAIN,
            condition=None,
            summary="测试节点",
            metadata={"source_ref": "《测试》#章节"},
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test",
            nodes=[node],
            edges=[],
            narrative_order=[node.node_id],
            entry_nodes=[node.node_id],
            terminal_nodes=[],
            metadata=SourceMetadata(),
            version="1.0.0",
        )
        
        refiner = SemanticClusterRefiner()
        refined_chain, changes = refiner.refine_chain(chain, snippets)
        
        # All node IDs should be in narrative_order
        node_ids = {n.node_id for n in refined_chain.nodes}
        narrative_order_ids = set(refined_chain.narrative_order)
        
        assert node_ids == narrative_order_ids, (
            f"narrative_order doesn't match nodes.\n"
            f"Nodes: {node_ids}\n"
            f"Order: {narrative_order_ids}"
        )

    def test_refine_chain_no_changes_for_homogeneous(self):
        """
        Property: A chain with only homogeneous nodes should not be changed.
        """
        snippets = [
            NarrativeSnippet(
                snippet_id=f"ns_test_{i:03d}",
                trigger="same_trigger",
                factor_trigger=None,
                role=ExtractorSnippetRole.MAIN,
                snippet_text=f"Text {i}",
                source_ref="《测试》#章节",
            )
            for i in range(3)
        ]
        
        node = LogicNode(
            node_id="n_test_chapter_0",
            snippet_ids=[s.snippet_id for s in snippets],
            role=SnippetRole.MAIN,
            condition=None,
            summary="测试节点",
            metadata={},
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test",
            nodes=[node],
            edges=[],
            narrative_order=[node.node_id],
            entry_nodes=[node.node_id],
            terminal_nodes=[],
            metadata=SourceMetadata(),
            version="1.0.0",
        )
        
        refiner = SemanticClusterRefiner()
        refined_chain, changes = refiner.refine_chain(chain, snippets)
        
        # Should have no changes
        assert len(changes) == 0
        assert len(refined_chain.nodes) == 1
        assert refined_chain.nodes[0].node_id == node.node_id
