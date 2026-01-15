# scripts/logic_chain_builder/tests/test_quality_scorer_pbt.py
"""
Property-Based Tests for LogicChainQualityScorer

Tests the quality scoring consistency using Hypothesis.

**Feature: logic-chain-builder, Property 13: Quality Score Consistency**
**Validates: Requirements 12.1, 12.2, 12.3**
"""

from collections import defaultdict
from typing import Dict, List, Set, Tuple

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.models import (
    LogicChain, LogicNode, LogicEdge, SnippetRole, EdgeRelation, SourceMetadata
)
from scripts.logic_chain_builder.quality_scorer import (
    LogicChainQualityScorer, QualityReport,
    COVERAGE_THRESHOLD, CONNECTIVITY_THRESHOLD,
    ARGUMENT_COMPLETENESS_THRESHOLD, ORPHAN_RATIO_THRESHOLD
)


# =============================================================================
# Hypothesis Strategies
# =============================================================================

node_role_strategy = st.sampled_from(list(SnippetRole))
edge_relation_strategy = st.sampled_from(list(EdgeRelation))


@st.composite
def valid_logic_chain_strategy(draw, min_nodes=2, max_nodes=10):
    """
    Generate a structurally valid LogicChain.
    
    This strategy ensures:
    - All edge references point to existing nodes
    - Entry nodes have no incoming edges
    - Terminal nodes have no outgoing edges
    - narrative_order contains all node_ids exactly once
    """
    num_nodes = draw(st.integers(min_value=min_nodes, max_value=max_nodes))
    
    # Generate nodes with unique IDs
    nodes = []
    for i in range(num_nodes):
        node_id = f"n_test_ch_{i}"
        # First node is entry (主干), last is terminal (总结)
        if i == 0:
            role = SnippetRole.MAIN
        elif i == num_nodes - 1:
            role = SnippetRole.SUMMARY
        else:
            role = draw(st.sampled_from([
                SnippetRole.MAIN_DEPENDENCY,
                SnippetRole.CONDITION_BRANCH,
                SnippetRole.EXCEPTION
            ]))
        
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_{i:03d}"],
            role=role,
            summary=f"Node {i}",
            metadata={"seq": i}
        )
        nodes.append(node)
    
    node_ids = [n.node_id for n in nodes]
    
    # Generate valid edges (DAG structure, no edges to entry, no edges from terminal)
    edges = []
    entry_node_id = nodes[0].node_id
    terminal_node_id = nodes[-1].node_id
    
    # Create edges only from non-terminal to non-entry nodes (except entry->others)
    for i in range(num_nodes - 1):
        from_node = nodes[i].node_id
        # Can only connect to nodes after this one (DAG) and not back to entry
        possible_targets = [
            nodes[j].node_id for j in range(i + 1, num_nodes)
        ]
        
        if possible_targets:
            # Connect to at least the next node for connectivity
            to_node = possible_targets[0]
            edge = LogicEdge(
                from_node=from_node,
                to_node=to_node,
                relation=draw(edge_relation_strategy),
                metadata={}
            )
            edges.append(edge)
    
    # Entry nodes: nodes with role=主干 or no incoming edges
    entry_nodes = [entry_node_id]
    
    # Terminal nodes: nodes with role=总结 or no outgoing edges
    terminal_nodes = [terminal_node_id]
    
    # narrative_order: valid topological order (all nodes exactly once)
    narrative_order = node_ids.copy()
    
    return LogicChain(
        chain_id="chain_test",
        book_id="test_book",
        nodes=nodes,
        edges=edges,
        narrative_order=narrative_order,
        entry_nodes=entry_nodes,
        terminal_nodes=terminal_nodes,
        metadata=SourceMetadata(
            version="1.0.0",
            source_files=["test_snippets.yaml", "test_relations.yaml"],
            snippet_count=num_nodes,
            relation_count=len(edges)
        ),
        version="1.0.0"
    )


@st.composite
def chain_with_disconnected_components_strategy(draw):
    """Generate a LogicChain with multiple disconnected components."""
    # Create two separate groups of nodes
    group1_size = draw(st.integers(min_value=2, max_value=4))
    group2_size = draw(st.integers(min_value=2, max_value=4))
    
    nodes = []
    edges = []
    
    # Group 1
    for i in range(group1_size):
        node_id = f"n_test_g1_{i}"
        role = SnippetRole.MAIN if i == 0 else SnippetRole.MAIN_DEPENDENCY
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_g1_{i:03d}"],
            role=role,
            summary=f"Group1 Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Group 1 edges (sequential)
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
        role = SnippetRole.CONDITION_BRANCH if i == 0 else SnippetRole.SUMMARY
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_g2_{i:03d}"],
            role=role,
            summary=f"Group2 Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Group 2 edges (sequential)
    for i in range(group2_size - 1):
        edges.append(LogicEdge(
            from_node=f"n_test_g2_{i}",
            to_node=f"n_test_g2_{i + 1}",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    return LogicChain(
        chain_id="chain_disconnected",
        book_id="disconnected_book",
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[nodes[0].node_id],
        terminal_nodes=[nodes[-1].node_id],
        metadata=SourceMetadata(
            snippet_count=len(nodes),
            relation_count=len(edges)
        ),
        version="1.0.0"
    ), group1_size, group2_size


@st.composite
def chain_with_orphan_nodes_strategy(draw):
    """Generate a LogicChain with some orphan nodes (no edges)."""
    connected_count = draw(st.integers(min_value=2, max_value=4))
    orphan_count = draw(st.integers(min_value=1, max_value=3))
    
    nodes = []
    edges = []
    
    # Connected nodes
    for i in range(connected_count):
        node_id = f"n_test_conn_{i}"
        role = SnippetRole.MAIN if i == 0 else (
            SnippetRole.SUMMARY if i == connected_count - 1 else SnippetRole.MAIN_DEPENDENCY
        )
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_conn_{i:03d}"],
            role=role,
            summary=f"Connected Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Connected edges
    for i in range(connected_count - 1):
        edges.append(LogicEdge(
            from_node=f"n_test_conn_{i}",
            to_node=f"n_test_conn_{i + 1}",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    # Orphan nodes (no edges)
    for i in range(orphan_count):
        node_id = f"n_test_orphan_{i}"
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_orphan_{i:03d}"],
            role=SnippetRole.EXCEPTION,
            summary=f"Orphan Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    return LogicChain(
        chain_id="chain_orphans",
        book_id="orphan_book",
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[nodes[0].node_id],
        terminal_nodes=[nodes[connected_count - 1].node_id],
        metadata=SourceMetadata(
            snippet_count=len(nodes),
            relation_count=len(edges)
        ),
        version="1.0.0"
    ), connected_count, orphan_count


@st.composite
def chain_with_cycle_strategy(draw):
    """Generate a LogicChain with a cycle."""
    num_nodes = draw(st.integers(min_value=3, max_value=6))
    
    nodes = []
    for i in range(num_nodes):
        node_id = f"n_test_cycle_{i}"
        role = SnippetRole.MAIN if i == 0 else SnippetRole.MAIN_DEPENDENCY
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_cycle_{i:03d}"],
            role=role,
            summary=f"Cycle Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Create sequential edges
    edges = []
    for i in range(num_nodes - 1):
        edges.append(LogicEdge(
            from_node=f"n_test_cycle_{i}",
            to_node=f"n_test_cycle_{i + 1}",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    # Add back edge to create cycle
    edges.append(LogicEdge(
        from_node=f"n_test_cycle_{num_nodes - 1}",
        to_node=f"n_test_cycle_0",
        relation=EdgeRelation.LEADS_TO,
        metadata={}
    ))
    
    return LogicChain(
        chain_id="chain_cycle",
        book_id="cycle_book",
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[],  # No valid entry in a cycle
        terminal_nodes=[],  # No valid terminal in a cycle
        metadata=SourceMetadata(
            snippet_count=num_nodes,
            relation_count=len(edges)
        ),
        version="1.0.0"
    )


# =============================================================================
# Property 13: Quality Score Consistency
# =============================================================================

class TestQualityScoreConsistency:
    """
    **Feature: logic-chain-builder, Property 13: Quality Score Consistency**
    **Validates: Requirements 12.1, 12.2, 12.3**
    
    *For any* generated LogicChain, the QualityReport's connectivity score should 
    equal the ratio of nodes in the largest connected component to total nodes.
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_connectivity_score_for_connected_chain(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 13: Quality Score Consistency**
        **Validates: Requirements 12.1**
        
        Property: For any fully connected LogicChain, connectivity should be 1.0.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        # A valid chain from our strategy is fully connected
        assert report.connectivity == 1.0, (
            f"Fully connected chain should have connectivity 1.0, got {report.connectivity}"
        )

    @settings(max_examples=100)
    @given(chain_data=chain_with_disconnected_components_strategy())
    def test_connectivity_score_for_disconnected_chain(
        self, 
        chain_data: Tuple[LogicChain, int, int]
    ):
        """
        **Feature: logic-chain-builder, Property 13: Quality Score Consistency**
        **Validates: Requirements 12.1**
        
        Property: For any LogicChain with disconnected components, connectivity
        should equal largest_component_size / total_nodes.
        """
        chain, group1_size, group2_size = chain_data
        
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        # Expected connectivity is largest component / total
        total_nodes = group1_size + group2_size
        largest_component = max(group1_size, group2_size)
        expected_connectivity = largest_component / total_nodes
        
        assert abs(report.connectivity - expected_connectivity) < 0.001, (
            f"Connectivity mismatch: expected {expected_connectivity}, got {report.connectivity}"
        )

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_argument_completeness_for_valid_chain(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 13: Quality Score Consistency**
        **Validates: Requirements 12.2**
        
        Property: For any valid LogicChain with entry, middle, and terminal nodes,
        argument completeness should be 1.0.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        # Valid chains from our strategy have entry, middle (if >2 nodes), and terminal
        if len(chain.nodes) > 2:
            assert report.argument_completeness == 1.0, (
                f"Chain with entry/middle/terminal should have completeness 1.0, "
                f"got {report.argument_completeness}"
            )
        else:
            # For 2-node chains, entry + terminal = 0.66 + 0.34 = 1.0
            assert report.argument_completeness >= 0.66, (
                f"2-node chain should have completeness >= 0.66, "
                f"got {report.argument_completeness}"
            )

    @settings(max_examples=100)
    @given(chain_data=chain_with_orphan_nodes_strategy())
    def test_orphan_ratio_calculation(
        self, 
        chain_data: Tuple[LogicChain, int, int]
    ):
        """
        **Feature: logic-chain-builder, Property 13: Quality Score Consistency**
        **Validates: Requirements 12.3**
        
        Property: For any LogicChain, orphan_ratio should equal
        nodes_without_edges / total_nodes.
        """
        chain, connected_count, orphan_count = chain_data
        
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        # Expected orphan ratio
        total_nodes = connected_count + orphan_count
        expected_orphan_ratio = orphan_count / total_nodes
        
        assert abs(report.orphan_ratio - expected_orphan_ratio) < 0.001, (
            f"Orphan ratio mismatch: expected {expected_orphan_ratio}, "
            f"got {report.orphan_ratio}"
        )

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_orphan_ratio_zero_for_connected_chain(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 13: Quality Score Consistency**
        **Validates: Requirements 12.3**
        
        Property: For any fully connected LogicChain, orphan_ratio should be 0.0.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        assert report.orphan_ratio == 0.0, (
            f"Fully connected chain should have orphan_ratio 0.0, "
            f"got {report.orphan_ratio}"
        )


# =============================================================================
# Cycle Detection Tests
# =============================================================================

class TestCycleDetection:
    """
    Tests for cycle counting functionality.
    
    **Validates: Requirements 12.4**
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_no_cycles_in_dag(self, chain: LogicChain):
        """
        **Validates: Requirements 12.4**
        
        Property: For any DAG LogicChain, cycle_count should be 0.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        assert report.cycle_count == 0, (
            f"DAG should have 0 cycles, got {report.cycle_count}"
        )

    @settings(max_examples=100)
    @given(chain=chain_with_cycle_strategy())
    def test_cycle_detected(self, chain: LogicChain):
        """
        **Validates: Requirements 12.4**
        
        Property: For any LogicChain with a cycle, cycle_count should be > 0.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        assert report.cycle_count > 0, (
            f"Chain with cycle should have cycle_count > 0, got {report.cycle_count}"
        )


# =============================================================================
# Quality Threshold Tests
# =============================================================================

class TestQualityThresholds:
    """
    Tests for quality threshold pass/fail determination.
    
    **Validates: Requirements 12.5**
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=3, max_nodes=10))
    def test_valid_chain_passes_thresholds(self, chain: LogicChain):
        """
        **Validates: Requirements 12.5**
        
        Property: A well-formed LogicChain should pass all quality thresholds.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain, total_snippet_count=len(chain.nodes))
        
        # Valid chains should pass connectivity and argument completeness
        assert report.connectivity_pass, (
            f"Valid chain should pass connectivity threshold, "
            f"got {report.connectivity}"
        )
        assert report.argument_completeness_pass, (
            f"Valid chain should pass argument completeness threshold, "
            f"got {report.argument_completeness}"
        )
        assert report.orphan_ratio_pass, (
            f"Valid chain should pass orphan ratio threshold, "
            f"got {report.orphan_ratio}"
        )

    def test_empty_chain_quality(self):
        """
        Test quality scoring for an empty chain.
        
        **Validates: Requirements 12.1, 12.2, 12.3**
        """
        chain = LogicChain(
            chain_id="chain_empty",
            book_id="empty_book",
            nodes=[],
            edges=[],
            narrative_order=[],
            entry_nodes=[],
            terminal_nodes=[],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        # Empty chain has trivial connectivity
        assert report.connectivity == 1.0
        # Empty chain has no argument pattern
        assert report.argument_completeness == 0.0
        # Empty chain has no orphans
        assert report.orphan_ratio == 0.0
        # Empty chain has no cycles
        assert report.cycle_count == 0

    def test_single_node_chain_quality(self):
        """
        Test quality scoring for a single-node chain.
        
        **Validates: Requirements 12.1, 12.2, 12.3**
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Single node",
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_single",
            book_id="single_book",
            nodes=[node],
            edges=[],
            narrative_order=["n_test_ch_0"],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_0"],
            metadata=SourceMetadata(snippet_count=1),
            version="1.0.0"
        )
        
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain)
        
        # Single node is trivially connected
        assert report.connectivity == 1.0
        # Single node has entry and terminal (same node)
        assert report.argument_completeness >= 0.66
        # Single node with no edges is an orphan
        assert report.orphan_ratio == 1.0
        # Single node has no cycles
        assert report.cycle_count == 0


# =============================================================================
# Helper Method Tests
# =============================================================================

class TestHelperMethods:
    """
    Tests for helper methods in LogicChainQualityScorer.
    """

    @settings(max_examples=100)
    @given(chain_data=chain_with_orphan_nodes_strategy())
    def test_get_orphan_nodes(
        self, 
        chain_data: Tuple[LogicChain, int, int]
    ):
        """
        Test that get_orphan_nodes returns correct orphan node IDs.
        """
        chain, connected_count, orphan_count = chain_data
        
        scorer = LogicChainQualityScorer()
        orphan_nodes = scorer.get_orphan_nodes(chain)
        
        # Should have exactly orphan_count orphan nodes
        assert len(orphan_nodes) == orphan_count, (
            f"Expected {orphan_count} orphan nodes, got {len(orphan_nodes)}"
        )
        
        # All orphan nodes should have "orphan" in their ID
        for node_id in orphan_nodes:
            assert "orphan" in node_id, (
                f"Orphan node {node_id} should have 'orphan' in ID"
            )

    @settings(max_examples=100)
    @given(chain_data=chain_with_disconnected_components_strategy())
    def test_get_disconnected_components(
        self, 
        chain_data: Tuple[LogicChain, int, int]
    ):
        """
        Test that get_disconnected_components returns correct components.
        """
        chain, group1_size, group2_size = chain_data
        
        scorer = LogicChainQualityScorer()
        components = scorer.get_disconnected_components(chain)
        
        # Should have exactly 2 components
        assert len(components) == 2, (
            f"Expected 2 components, got {len(components)}"
        )
        
        # Component sizes should match
        component_sizes = sorted([len(c) for c in components])
        expected_sizes = sorted([group1_size, group2_size])
        
        assert component_sizes == expected_sizes, (
            f"Component sizes mismatch: expected {expected_sizes}, "
            f"got {component_sizes}"
        )


# =============================================================================
# Overall Score Tests
# =============================================================================

class TestOverallScore:
    """
    Tests for the overall quality score calculation.
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=3, max_nodes=10))
    def test_overall_score_range(self, chain: LogicChain):
        """
        Test that overall score is always between 0 and 1.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain, total_snippet_count=len(chain.nodes))
        
        overall = report.overall_score()
        
        assert 0.0 <= overall <= 1.0, (
            f"Overall score should be between 0 and 1, got {overall}"
        )

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=3, max_nodes=10))
    def test_high_quality_chain_has_high_overall_score(self, chain: LogicChain):
        """
        Test that a high-quality chain has a high overall score.
        """
        scorer = LogicChainQualityScorer()
        report = scorer.score(chain, total_snippet_count=len(chain.nodes))
        
        overall = report.overall_score()
        
        # A valid chain should have a high overall score
        assert overall >= 0.7, (
            f"Valid chain should have overall score >= 0.7, got {overall}"
        )
