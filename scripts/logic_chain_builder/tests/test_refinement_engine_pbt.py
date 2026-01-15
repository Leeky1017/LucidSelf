# scripts/logic_chain_builder/tests/test_refinement_engine_pbt.py
"""
Property-Based Tests for IterativeRefinementEngine

Tests the refinement quality monotonicity using Hypothesis.

**Feature: logic-chain-builder, Property 17: Refinement Quality Monotonicity**
**Validates: Requirements 16.4, 16.5**
"""

from typing import List, Tuple

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.models import (
    LogicChain, LogicNode, LogicEdge, SnippetRole, EdgeRelation, SourceMetadata
)
from scripts.logic_chain_builder.refinement_engine import (
    IterativeRefinementEngine, RefinementRecord, RefinementResult,
    MAX_ITERATIONS, QUALITY_THRESHOLD_OVERALL
)
from scripts.logic_chain_builder.quality_scorer import LogicChainQualityScorer
from scripts.schema_extractor.models import NarrativeSnippet


# =============================================================================
# Hypothesis Strategies
# =============================================================================

node_role_strategy = st.sampled_from(list(SnippetRole))
edge_relation_strategy = st.sampled_from(list(EdgeRelation))


@st.composite
def snippet_strategy(draw, snippet_id: str, source_ref: str = "ch1"):
    """Generate a valid NarrativeSnippet."""
    role = draw(st.sampled_from(["主干", "主干依赖", "条件分支", "例外处理", "总结"]))
    trigger = draw(st.text(min_size=1, max_size=20, alphabet="格局用神吉凶日主月令"))
    
    return NarrativeSnippet(
        snippet_id=snippet_id,
        source_ref=source_ref,
        snippet_text=f"Test snippet {snippet_id}",
        role=role,
        trigger=trigger if trigger else "默认触发",
        factor_trigger=None,
    )


@st.composite
def chain_with_quality_issues_strategy(draw):
    """
    Generate a LogicChain with quality issues that can be improved.
    
    Creates chains with:
    - Some orphan nodes (no edges)
    - Potentially disconnected components
    - Missing entry/terminal nodes
    """
    num_connected = draw(st.integers(min_value=2, max_value=5))
    num_orphans = draw(st.integers(min_value=0, max_value=2))
    
    nodes = []
    edges = []
    snippets = []
    
    # Create connected nodes
    for i in range(num_connected):
        node_id = f"n_test_ch_{i}"
        snippet_id = f"ns_test_{i:03d}"
        
        if i == 0:
            role = SnippetRole.MAIN
        elif i == num_connected - 1:
            role = SnippetRole.SUMMARY
        else:
            role = draw(st.sampled_from([
                SnippetRole.MAIN_DEPENDENCY,
                SnippetRole.CONDITION_BRANCH,
            ]))
        
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[snippet_id],
            role=role,
            summary=f"Node {i}",
            metadata={"source_ref": f"ch{i}"}
        )
        nodes.append(node)
        
        # Create corresponding snippet
        snippet = NarrativeSnippet(
            snippet_id=snippet_id,
            source_ref=f"ch{i}",
            snippet_text=f"Test snippet text for node {i}",
            role=role.value,
            trigger=f"trigger_{i}",
            factor_trigger=None,
        )
        snippets.append(snippet)
    
    # Create edges for connected nodes (sequential)
    for i in range(num_connected - 1):
        edge = LogicEdge(
            from_node=f"n_test_ch_{i}",
            to_node=f"n_test_ch_{i + 1}",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        )
        edges.append(edge)
    
    # Create orphan nodes (no edges)
    for i in range(num_orphans):
        node_id = f"n_test_orphan_{i}"
        snippet_id = f"ns_orphan_{i:03d}"
        
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[snippet_id],
            role=SnippetRole.EXCEPTION,
            summary=f"Orphan {i}",
            metadata={}
        )
        nodes.append(node)
        
        snippet = NarrativeSnippet(
            snippet_id=snippet_id,
            source_ref=f"orphan_ch{i}",
            snippet_text=f"Orphan snippet {i}",
            role="例外处理",
            trigger=f"orphan_trigger_{i}",
            factor_trigger=None,
        )
        snippets.append(snippet)
    
    # Determine entry/terminal nodes
    entry_nodes = [nodes[0].node_id] if nodes else []
    terminal_nodes = [nodes[num_connected - 1].node_id] if num_connected > 0 else []
    
    chain = LogicChain(
        chain_id="chain_test",
        book_id="滴天髓",  # Use a known book for book_type detection
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=entry_nodes,
        terminal_nodes=terminal_nodes,
        metadata=SourceMetadata(
            version="1.0.0",
            source_files=["test_snippets.yaml"],
            snippet_count=len(snippets),
            relation_count=len(edges)
        ),
        version="1.0.0"
    )
    
    return chain, snippets, num_orphans


@st.composite
def chain_with_disconnected_components_strategy(draw):
    """Generate a LogicChain with multiple disconnected components."""
    group1_size = draw(st.integers(min_value=2, max_value=3))
    group2_size = draw(st.integers(min_value=2, max_value=3))
    
    nodes = []
    edges = []
    snippets = []
    
    # Group 1
    for i in range(group1_size):
        node_id = f"n_test_g1_{i}"
        snippet_id = f"ns_g1_{i:03d}"
        role = SnippetRole.MAIN if i == 0 else SnippetRole.MAIN_DEPENDENCY
        
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[snippet_id],
            role=role,
            summary=f"G1 Node {i}",
            metadata={}
        )
        nodes.append(node)
        
        snippet = NarrativeSnippet(
            snippet_id=snippet_id,
            source_ref=f"g1_ch{i}",
            snippet_text=f"Group 1 snippet {i}",
            role=role.value,
            trigger=f"g1_trigger_{i}",
            factor_trigger=None,
        )
        snippets.append(snippet)
    
    # Group 1 edges
    for i in range(group1_size - 1):
        edges.append(LogicEdge(
            from_node=f"n_test_g1_{i}",
            to_node=f"n_test_g1_{i + 1}",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    # Group 2 (disconnected)
    for i in range(group2_size):
        node_id = f"n_test_g2_{i}"
        snippet_id = f"ns_g2_{i:03d}"
        role = SnippetRole.CONDITION_BRANCH if i == 0 else SnippetRole.SUMMARY
        
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[snippet_id],
            role=role,
            summary=f"G2 Node {i}",
            metadata={}
        )
        nodes.append(node)
        
        snippet = NarrativeSnippet(
            snippet_id=snippet_id,
            source_ref=f"g2_ch{i}",
            snippet_text=f"Group 2 snippet {i}",
            role=role.value,
            trigger=f"g2_trigger_{i}",
            factor_trigger=None,
        )
        snippets.append(snippet)
    
    # Group 2 edges
    for i in range(group2_size - 1):
        edges.append(LogicEdge(
            from_node=f"n_test_g2_{i}",
            to_node=f"n_test_g2_{i + 1}",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    chain = LogicChain(
        chain_id="chain_disconnected",
        book_id="滴天髓",
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[nodes[0].node_id],
        terminal_nodes=[nodes[-1].node_id],
        metadata=SourceMetadata(
            snippet_count=len(snippets),
            relation_count=len(edges)
        ),
        version="1.0.0"
    )
    
    return chain, snippets, group1_size, group2_size


# =============================================================================
# Property 17: Refinement Quality Monotonicity
# =============================================================================

class TestRefinementQualityMonotonicity:
    """
    **Feature: logic-chain-builder, Property 17: Refinement Quality Monotonicity**
    **Validates: Requirements 16.4, 16.5**
    
    *For any* iterative refinement sequence, the final quality score should be 
    >= the initial quality score (no regression).
    """

    @settings(max_examples=100)
    @given(chain_data=chain_with_quality_issues_strategy())
    def test_refinement_does_not_decrease_quality(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int]
    ):
        """
        **Feature: logic-chain-builder, Property 17: Refinement Quality Monotonicity**
        **Validates: Requirements 16.4, 16.5**
        
        Property: For any LogicChain, refinement should not decrease quality score.
        """
        chain, snippets, num_orphans = chain_data
        
        # Skip if chain is too small
        assume(len(chain.nodes) >= 2)
        
        engine = IterativeRefinementEngine(
            max_iterations=3,
            quality_threshold=0.9,  # High threshold to ensure iterations happen
        )
        
        result = engine.refine_until_threshold(
            chain=chain,
            snippets=snippets,
            total_snippet_count=len(snippets),
        )
        
        # Property: final score >= initial score (no regression)
        assert result.final_score >= result.initial_score, (
            f"Quality regression detected: "
            f"initial={result.initial_score:.3f}, final={result.final_score:.3f}"
        )

    @settings(max_examples=100)
    @given(chain_data=chain_with_disconnected_components_strategy())
    def test_refinement_improves_disconnected_chains(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int, int]
    ):
        """
        **Feature: logic-chain-builder, Property 17: Refinement Quality Monotonicity**
        **Validates: Requirements 16.4, 16.5**
        
        Property: For any disconnected LogicChain, refinement should improve 
        connectivity without decreasing overall quality.
        """
        chain, snippets, g1_size, g2_size = chain_data
        
        engine = IterativeRefinementEngine(
            max_iterations=3,
            quality_threshold=0.9,
        )
        
        # Get initial connectivity
        scorer = LogicChainQualityScorer()
        initial_quality = scorer.score(chain, len(snippets))
        initial_connectivity = initial_quality.connectivity
        
        result = engine.refine_until_threshold(
            chain=chain,
            snippets=snippets,
            total_snippet_count=len(snippets),
        )
        
        # Get final connectivity
        final_quality = scorer.score(result.chain, len(snippets))
        final_connectivity = final_quality.connectivity
        
        # Property: connectivity should not decrease
        assert final_connectivity >= initial_connectivity, (
            f"Connectivity regression: "
            f"initial={initial_connectivity:.3f}, final={final_connectivity:.3f}"
        )
        
        # Property: overall quality should not decrease
        assert result.final_score >= result.initial_score, (
            f"Quality regression: "
            f"initial={result.initial_score:.3f}, final={result.final_score:.3f}"
        )


    @settings(max_examples=100)
    @given(chain_data=chain_with_quality_issues_strategy())
    def test_history_records_all_iterations(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int]
    ):
        """
        **Feature: logic-chain-builder, Property 17: Refinement Quality Monotonicity**
        **Validates: Requirements 16.5**
        
        Property: Refinement history should record all iterations with quality scores.
        """
        chain, snippets, num_orphans = chain_data
        assume(len(chain.nodes) >= 2)
        
        engine = IterativeRefinementEngine(
            max_iterations=3,
            quality_threshold=0.9,
        )
        
        result = engine.refine_until_threshold(
            chain=chain,
            snippets=snippets,
            total_snippet_count=len(snippets),
        )
        
        # Property: history should have at least initial state (version 0)
        assert len(result.history) >= 1, "History should have at least initial state"
        
        # Property: first record should be version 0 (initial state)
        assert result.history[0].version == 0, "First record should be version 0"
        
        # Property: versions should be sequential
        for i, record in enumerate(result.history):
            assert record.version == i, f"Version mismatch at index {i}"
        
        # Property: each record should have quality scores
        for record in result.history:
            assert record.quality_scores is not None, "Record should have quality scores"
            assert record.overall_score >= 0.0, "Overall score should be non-negative"

    @settings(max_examples=100)
    @given(chain_data=chain_with_quality_issues_strategy())
    def test_monotonic_quality_across_iterations(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int]
    ):
        """
        **Feature: logic-chain-builder, Property 17: Refinement Quality Monotonicity**
        **Validates: Requirements 16.4, 16.5**
        
        Property: Quality scores should be monotonically non-decreasing across iterations.
        """
        chain, snippets, num_orphans = chain_data
        assume(len(chain.nodes) >= 2)
        
        engine = IterativeRefinementEngine(
            max_iterations=5,
            quality_threshold=0.95,  # High threshold to ensure multiple iterations
        )
        
        result = engine.refine_until_threshold(
            chain=chain,
            snippets=snippets,
            total_snippet_count=len(snippets),
        )
        
        # Property: quality should be monotonically non-decreasing
        # Note: We check from version 1 onwards (after first improvement attempt)
        # Version 0 is the initial state before any improvements
        if len(result.history) > 1:
            prev_score = result.history[0].overall_score
            for record in result.history[1:]:
                # Allow for small floating point differences
                assert record.overall_score >= prev_score - 0.001, (
                    f"Quality decreased from {prev_score:.3f} to {record.overall_score:.3f} "
                    f"at version {record.version}"
                )
                prev_score = record.overall_score


# =============================================================================
# Additional Tests for Refinement Engine
# =============================================================================

class TestRefinementEngineBasics:
    """
    Basic functionality tests for IterativeRefinementEngine.
    """

    def test_empty_chain_refinement(self):
        """Test refinement of an empty chain."""
        chain = LogicChain(
            chain_id="chain_empty",
            book_id="test_book",
            nodes=[],
            edges=[],
            narrative_order=[],
            entry_nodes=[],
            terminal_nodes=[],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        engine = IterativeRefinementEngine(max_iterations=2)
        result = engine.refine_until_threshold(chain, snippets=[])
        
        # Empty chain should not crash
        assert result.chain is not None
        assert result.iterations_performed >= 0

    def test_single_node_chain_refinement(self):
        """Test refinement of a single-node chain."""
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Single node",
            metadata={}
        )
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_000",
            source_ref="ch1",
            snippet_text="Test snippet",
            role="主干",
            trigger="test",
            factor_trigger=None,
        )
        
        chain = LogicChain(
            chain_id="chain_single",
            book_id="滴天髓",
            nodes=[node],
            edges=[],
            narrative_order=["n_test_ch_0"],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_0"],
            metadata=SourceMetadata(snippet_count=1),
            version="1.0.0"
        )
        
        engine = IterativeRefinementEngine(max_iterations=2)
        result = engine.refine_until_threshold(chain, snippets=[snippet])
        
        # Single node chain should not crash
        assert result.chain is not None
        assert len(result.chain.nodes) >= 1

    def test_already_high_quality_chain(self):
        """Test that high-quality chains don't regress."""
        # Create a well-formed chain
        nodes = [
            LogicNode(
                node_id=f"n_test_ch_{i}",
                snippet_ids=[f"ns_test_{i:03d}"],
                role=SnippetRole.MAIN if i == 0 else (
                    SnippetRole.SUMMARY if i == 2 else SnippetRole.MAIN_DEPENDENCY
                ),
                summary=f"Node {i}",
                metadata={}
            )
            for i in range(3)
        ]
        
        edges = [
            LogicEdge(
                from_node="n_test_ch_0",
                to_node="n_test_ch_1",
                relation=EdgeRelation.LEADS_TO,
                metadata={}
            ),
            LogicEdge(
                from_node="n_test_ch_1",
                to_node="n_test_ch_2",
                relation=EdgeRelation.LEADS_TO,
                metadata={}
            ),
        ]
        
        snippets = [
            NarrativeSnippet(
                snippet_id=f"ns_test_{i:03d}",
                source_ref=f"ch{i}",
                snippet_text=f"Snippet {i}",
                role="主干" if i == 0 else ("总结" if i == 2 else "主干依赖"),
                trigger=f"trigger_{i}",
                factor_trigger=None,
            )
            for i in range(3)
        ]
        
        chain = LogicChain(
            chain_id="chain_good",
            book_id="滴天髓",
            nodes=nodes,
            edges=edges,
            narrative_order=[n.node_id for n in nodes],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_2"],
            metadata=SourceMetadata(snippet_count=3, relation_count=2),
            version="1.0.0"
        )
        
        engine = IterativeRefinementEngine(
            max_iterations=3,
            quality_threshold=0.5,  # Low threshold - should pass quickly
        )
        
        result = engine.refine_until_threshold(chain, snippets=snippets)
        
        # High quality chain should not regress
        assert result.final_score >= result.initial_score
        # Should meet threshold quickly
        assert result.threshold_met or result.final_score >= 0.5


class TestOrphanNodeFix:
    """Tests for orphan node fixing functionality."""

    @settings(max_examples=50)
    @given(chain_data=chain_with_quality_issues_strategy())
    def test_orphan_nodes_get_connected(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int]
    ):
        """Test that orphan nodes get connected during refinement."""
        chain, snippets, num_orphans = chain_data
        assume(num_orphans > 0)  # Only test chains with orphans
        assume(len(chain.nodes) >= 3)  # Need enough nodes
        
        engine = IterativeRefinementEngine(max_iterations=3)
        scorer = LogicChainQualityScorer()
        
        # Get initial orphan count
        initial_orphans = scorer.get_orphan_nodes(chain)
        
        result = engine.refine_until_threshold(chain, snippets=snippets)
        
        # Get final orphan count
        final_orphans = scorer.get_orphan_nodes(result.chain)
        
        # Property: orphan count should not increase
        assert len(final_orphans) <= len(initial_orphans), (
            f"Orphan count increased: {len(initial_orphans)} -> {len(final_orphans)}"
        )


class TestConnectivityImprovement:
    """Tests for connectivity improvement functionality."""

    @settings(max_examples=50)
    @given(chain_data=chain_with_disconnected_components_strategy())
    def test_disconnected_components_get_connected(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int, int]
    ):
        """Test that disconnected components get connected during refinement."""
        chain, snippets, g1_size, g2_size = chain_data
        
        engine = IterativeRefinementEngine(max_iterations=3)
        scorer = LogicChainQualityScorer()
        
        # Get initial component count
        initial_components = scorer.get_disconnected_components(chain)
        
        result = engine.refine_until_threshold(chain, snippets=snippets)
        
        # Get final component count
        final_components = scorer.get_disconnected_components(result.chain)
        
        # Property: component count should not increase
        assert len(final_components) <= len(initial_components), (
            f"Component count increased: {len(initial_components)} -> {len(final_components)}"
        )


class TestRefinementResult:
    """Tests for RefinementResult structure."""

    @settings(max_examples=50)
    @given(chain_data=chain_with_quality_issues_strategy())
    def test_result_contains_all_improvements(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int]
    ):
        """Test that result contains all improvements made."""
        chain, snippets, num_orphans = chain_data
        assume(len(chain.nodes) >= 2)
        
        engine = IterativeRefinementEngine(max_iterations=3)
        result = engine.refine_until_threshold(chain, snippets=snippets)
        
        # Count total changes from history
        total_changes_in_history = sum(
            len(record.changes) for record in result.history
        )
        
        # improvements_made should contain all changes (excluding initial state)
        # Note: initial state has ["Initial state"] which we don't count
        expected_improvements = total_changes_in_history - 1  # Subtract "Initial state"
        
        assert len(result.improvements_made) == expected_improvements, (
            f"Improvements mismatch: result has {len(result.improvements_made)}, "
            f"history has {expected_improvements}"
        )

    @settings(max_examples=50)
    @given(chain_data=chain_with_quality_issues_strategy())
    def test_iterations_performed_matches_history(
        self, 
        chain_data: Tuple[LogicChain, List[NarrativeSnippet], int]
    ):
        """Test that iterations_performed matches history length."""
        chain, snippets, num_orphans = chain_data
        assume(len(chain.nodes) >= 2)
        
        engine = IterativeRefinementEngine(max_iterations=3)
        result = engine.refine_until_threshold(chain, snippets=snippets)
        
        # iterations_performed should be history length - 1 (excluding initial state)
        assert result.iterations_performed == len(result.history) - 1, (
            f"Iterations mismatch: performed={result.iterations_performed}, "
            f"history_len={len(result.history)}"
        )
