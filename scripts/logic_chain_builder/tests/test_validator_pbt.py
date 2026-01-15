# scripts/logic_chain_builder/tests/test_validator_pbt.py
"""
Property-Based Tests for LogicChainValidator

Tests the structural integrity validation of LogicChain using Hypothesis.

**Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
**Validates: Requirements 6.1, 6.2, 6.3, 6.4**
"""

from typing import List, Set

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.models import (
    LogicChain, LogicNode, LogicEdge, SnippetRole, EdgeRelation, SourceMetadata
)
from scripts.logic_chain_builder.validator import LogicChainValidator


# =============================================================================
# Hypothesis Strategies
# =============================================================================

node_role_strategy = st.sampled_from(list(SnippetRole))
edge_relation_strategy = st.sampled_from(list(EdgeRelation))


@st.composite
def logic_node_strategy(draw, node_id: str):
    """Generate a valid LogicNode with a specific node_id."""
    return LogicNode(
        node_id=node_id,
        snippet_ids=draw(st.lists(
            st.from_regex(r"ns_[a-z]{2,5}_\d{3}", fullmatch=True),
            min_size=1, max_size=3
        )),
        role=draw(node_role_strategy),
        condition=draw(st.one_of(st.none(), st.text(min_size=1, max_size=20))),
        summary=draw(st.text(min_size=1, max_size=50)),
        metadata={}
    )


@st.composite
def valid_logic_chain_strategy(draw, min_nodes=2, max_nodes=8):
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
def chain_with_invalid_edge_refs_strategy(draw):
    """Generate a LogicChain with invalid edge references."""
    base_chain = draw(valid_logic_chain_strategy(min_nodes=3, max_nodes=6))
    
    # Add an edge with invalid from_node or to_node
    invalid_type = draw(st.sampled_from(["from_node", "to_node", "both"]))
    
    invalid_edge = LogicEdge(
        from_node="n_nonexistent_0" if invalid_type in ["from_node", "both"] else base_chain.nodes[0].node_id,
        to_node="n_nonexistent_1" if invalid_type in ["to_node", "both"] else base_chain.nodes[-1].node_id,
        relation=draw(edge_relation_strategy),
        metadata={}
    )
    
    new_edges = list(base_chain.edges) + [invalid_edge]
    
    return LogicChain(
        chain_id=base_chain.chain_id,
        book_id=base_chain.book_id,
        nodes=base_chain.nodes,
        edges=new_edges,
        narrative_order=base_chain.narrative_order,
        entry_nodes=base_chain.entry_nodes,
        terminal_nodes=base_chain.terminal_nodes,
        metadata=base_chain.metadata,
        version=base_chain.version
    )


@st.composite
def chain_with_entry_node_incoming_edges_strategy(draw):
    """Generate a LogicChain where entry nodes have incoming edges."""
    num_nodes = draw(st.integers(min_value=3, max_value=6))
    
    nodes = []
    for i in range(num_nodes):
        node_id = f"n_test_ch_{i}"
        role = SnippetRole.MAIN if i == 0 else (
            SnippetRole.SUMMARY if i == num_nodes - 1 else SnippetRole.MAIN_DEPENDENCY
        )
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_{i:03d}"],
            role=role,
            summary=f"Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Create edges including one pointing TO the entry node (invalid)
    edges = [
        LogicEdge(
            from_node=nodes[1].node_id,
            to_node=nodes[0].node_id,  # Points to entry node - invalid!
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        )
    ]
    
    # Add normal forward edges
    for i in range(num_nodes - 1):
        edges.append(LogicEdge(
            from_node=nodes[i].node_id,
            to_node=nodes[i + 1].node_id,
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    return LogicChain(
        chain_id="chain_test",
        book_id="test_book",
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[nodes[0].node_id],  # Entry node has incoming edge
        terminal_nodes=[nodes[-1].node_id],
        metadata=SourceMetadata(),
        version="1.0.0"
    )


@st.composite
def chain_with_terminal_node_outgoing_edges_strategy(draw):
    """Generate a LogicChain where terminal nodes have outgoing edges."""
    num_nodes = draw(st.integers(min_value=3, max_value=6))
    
    nodes = []
    for i in range(num_nodes):
        node_id = f"n_test_ch_{i}"
        role = SnippetRole.MAIN if i == 0 else (
            SnippetRole.SUMMARY if i == num_nodes - 1 else SnippetRole.MAIN_DEPENDENCY
        )
        node = LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_{i:03d}"],
            role=role,
            summary=f"Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Create normal forward edges
    edges = []
    for i in range(num_nodes - 1):
        edges.append(LogicEdge(
            from_node=nodes[i].node_id,
            to_node=nodes[i + 1].node_id,
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    # Add edge FROM terminal node (invalid)
    edges.append(LogicEdge(
        from_node=nodes[-1].node_id,  # From terminal node - invalid!
        to_node=nodes[0].node_id,
        relation=EdgeRelation.LEADS_TO,
        metadata={}
    ))
    
    return LogicChain(
        chain_id="chain_test",
        book_id="test_book",
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[nodes[0].node_id],
        terminal_nodes=[nodes[-1].node_id],  # Terminal node has outgoing edge
        metadata=SourceMetadata(),
        version="1.0.0"
    )


@st.composite
def chain_with_invalid_narrative_order_strategy(draw):
    """Generate a LogicChain with invalid narrative_order."""
    base_chain = draw(valid_logic_chain_strategy(min_nodes=3, max_nodes=6))
    
    invalid_type = draw(st.sampled_from(["duplicate", "missing", "extra"]))
    
    node_ids = [n.node_id for n in base_chain.nodes]
    
    if invalid_type == "duplicate":
        # Add a duplicate
        new_order = node_ids + [node_ids[0]]
    elif invalid_type == "missing":
        # Remove one node
        new_order = node_ids[:-1]
    else:  # extra
        # Add a non-existent node
        new_order = node_ids + ["n_nonexistent_999"]
    
    return LogicChain(
        chain_id=base_chain.chain_id,
        book_id=base_chain.book_id,
        nodes=base_chain.nodes,
        edges=base_chain.edges,
        narrative_order=new_order,
        entry_nodes=base_chain.entry_nodes,
        terminal_nodes=base_chain.terminal_nodes,
        metadata=base_chain.metadata,
        version=base_chain.version
    )


# =============================================================================
# Property 8: Logic Chain Structural Integrity
# =============================================================================

class TestLogicChainStructuralIntegrity:
    """
    **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
    **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
    
    *For any* generated LogicChain:
    - All edge `from_node` and `to_node` references should point to existing nodes
    - Entry nodes should have no incoming edges
    - Terminal nodes should have no outgoing edges
    - `narrative_order` should contain all node_ids exactly once
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_valid_chain_passes_edge_reference_validation(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.1**
        
        Property: For any valid LogicChain, all edge references should point to existing nodes.
        """
        validator = LogicChainValidator()
        errors = validator._validate_edge_references(chain)
        
        assert len(errors) == 0, f"Valid chain should have no edge reference errors: {errors}"

    @settings(max_examples=100)
    @given(chain=chain_with_invalid_edge_refs_strategy())
    def test_invalid_edge_refs_detected(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.1**
        
        Property: Chains with invalid edge references should be detected.
        """
        validator = LogicChainValidator()
        errors = validator._validate_edge_references(chain)
        
        assert len(errors) > 0, "Should detect invalid edge references"
        assert all(e.error_type == "invalid_edge_reference" for e in errors)

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_valid_chain_passes_entry_node_validation(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.2**
        
        Property: For any valid LogicChain, entry nodes should have no incoming edges.
        """
        validator = LogicChainValidator()
        errors = validator._validate_entry_nodes(chain)
        
        assert len(errors) == 0, f"Valid chain should have no entry node errors: {errors}"

    @settings(max_examples=100)
    @given(chain=chain_with_entry_node_incoming_edges_strategy())
    def test_entry_node_with_incoming_edges_detected(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.2**
        
        Property: Entry nodes with incoming edges should be detected as errors.
        """
        validator = LogicChainValidator()
        errors = validator._validate_entry_nodes(chain)
        
        assert len(errors) > 0, "Should detect entry nodes with incoming edges"
        assert all(e.error_type == "entry_node_has_incoming_edges" for e in errors)

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_valid_chain_passes_terminal_node_validation(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.3**
        
        Property: For any valid LogicChain, terminal nodes should have no outgoing edges.
        """
        validator = LogicChainValidator()
        errors = validator._validate_terminal_nodes(chain)
        
        assert len(errors) == 0, f"Valid chain should have no terminal node errors: {errors}"

    @settings(max_examples=100)
    @given(chain=chain_with_terminal_node_outgoing_edges_strategy())
    def test_terminal_node_with_outgoing_edges_detected(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.3**
        
        Property: Terminal nodes with outgoing edges should be detected as errors.
        """
        validator = LogicChainValidator()
        errors = validator._validate_terminal_nodes(chain)
        
        assert len(errors) > 0, "Should detect terminal nodes with outgoing edges"
        assert all(e.error_type == "terminal_node_has_outgoing_edges" for e in errors)

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_valid_chain_passes_narrative_order_validation(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.4**
        
        Property: For any valid LogicChain, narrative_order should contain all node_ids exactly once.
        """
        validator = LogicChainValidator()
        errors = validator._validate_narrative_order(chain)
        
        assert len(errors) == 0, f"Valid chain should have no narrative order errors: {errors}"

    @settings(max_examples=100)
    @given(chain=chain_with_invalid_narrative_order_strategy())
    def test_invalid_narrative_order_detected(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.4**
        
        Property: Invalid narrative_order (duplicates, missing, or extra nodes) should be detected.
        """
        validator = LogicChainValidator()
        errors = validator._validate_narrative_order(chain)
        
        assert len(errors) > 0, "Should detect invalid narrative order"
        valid_error_types = {
            "duplicate_in_narrative_order",
            "missing_from_narrative_order",
            "extra_in_narrative_order"
        }
        assert all(e.error_type in valid_error_types for e in errors)


# =============================================================================
# Combined Structural Integrity Tests
# =============================================================================

class TestCombinedStructuralIntegrity:
    """
    Combined tests for overall structural integrity.
    
    **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
    **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_valid_chain_all_validations_pass(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
        
        Property: A structurally valid LogicChain should pass all validation checks.
        """
        validator = LogicChainValidator()
        
        edge_errors = validator._validate_edge_references(chain)
        entry_errors = validator._validate_entry_nodes(chain)
        terminal_errors = validator._validate_terminal_nodes(chain)
        order_errors = validator._validate_narrative_order(chain)
        
        all_errors = edge_errors + entry_errors + terminal_errors + order_errors
        
        assert len(all_errors) == 0, f"Valid chain should pass all validations: {all_errors}"

    def test_empty_chain_validation(self):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
        
        Property: An empty chain (no nodes, no edges) should pass validation.
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
        
        validator = LogicChainValidator()
        
        edge_errors = validator._validate_edge_references(chain)
        entry_errors = validator._validate_entry_nodes(chain)
        terminal_errors = validator._validate_terminal_nodes(chain)
        order_errors = validator._validate_narrative_order(chain)
        
        all_errors = edge_errors + entry_errors + terminal_errors + order_errors
        
        assert len(all_errors) == 0, f"Empty chain should pass validation: {all_errors}"

    def test_single_node_chain_validation(self):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
        
        Property: A single-node chain should pass validation.
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
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        
        edge_errors = validator._validate_edge_references(chain)
        entry_errors = validator._validate_entry_nodes(chain)
        terminal_errors = validator._validate_terminal_nodes(chain)
        order_errors = validator._validate_narrative_order(chain)
        
        all_errors = edge_errors + entry_errors + terminal_errors + order_errors
        
        assert len(all_errors) == 0, f"Single-node chain should pass validation: {all_errors}"

    def test_self_loop_edge_validation(self):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.1**
        
        Property: Self-loop edges (from_node == to_node) should be valid if node exists.
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN_DEPENDENCY,  # Not entry or terminal
            summary="Self-loop node",
            metadata={}
        )
        
        self_loop_edge = LogicEdge(
            from_node="n_test_ch_0",
            to_node="n_test_ch_0",
            relation=EdgeRelation.SUPPORTS,
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_selfloop",
            book_id="selfloop_book",
            nodes=[node],
            edges=[self_loop_edge],
            narrative_order=["n_test_ch_0"],
            entry_nodes=[],  # No entry nodes
            terminal_nodes=[],  # No terminal nodes
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        edge_errors = validator._validate_edge_references(chain)
        
        # Self-loop should be valid from edge reference perspective
        assert len(edge_errors) == 0, f"Self-loop edge should be valid: {edge_errors}"


# =============================================================================
# Auto-Repair Tests
# =============================================================================

class TestAutoRepair:
    """
    Tests for the auto_repair function.
    
    **Feature: logic-chain-builder, Task 8.5: Implement auto_repair function**
    **Validates: Requirements 6.5**
    """

    def test_repair_invalid_edge_references(self):
        """
        Test that invalid edge references are removed.
        
        **Validates: Requirements 6.5**
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Test node",
            metadata={}
        )
        
        # Edge with invalid to_node
        invalid_edge = LogicEdge(
            from_node="n_test_ch_0",
            to_node="n_nonexistent",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=[node],
            edges=[invalid_edge],
            narrative_order=["n_test_ch_0"],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_0"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        errors = validator._validate_edge_references(chain)
        
        repaired_chain, repairs = validator.auto_repair(chain, errors)
        
        assert len(repaired_chain.edges) == 0, "Invalid edge should be removed"
        assert len(repairs) > 0, "Repairs should be reported"
        assert any("invalid reference" in r.lower() for r in repairs)

    def test_repair_missing_entry_nodes(self):
        """
        Test that missing entry nodes are promoted from nodes with no incoming edges.
        
        **Validates: Requirements 6.5**
        """
        nodes = [
            LogicNode(
                node_id="n_test_ch_0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                summary="Entry node",
                metadata={}
            ),
            LogicNode(
                node_id="n_test_ch_1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.SUMMARY,
                summary="Terminal node",
                metadata={}
            )
        ]
        
        edge = LogicEdge(
            from_node="n_test_ch_0",
            to_node="n_test_ch_1",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=nodes,
            edges=[edge],
            narrative_order=["n_test_ch_0", "n_test_ch_1"],
            entry_nodes=[],  # Missing entry nodes
            terminal_nodes=["n_test_ch_1"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        assert len(repaired_chain.entry_nodes) > 0, "Entry nodes should be promoted"
        assert "n_test_ch_0" in repaired_chain.entry_nodes, "Node with no incoming edges should be entry"
        assert any("entry_nodes" in r.lower() for r in repairs)

    def test_repair_missing_terminal_nodes(self):
        """
        Test that missing terminal nodes are promoted from nodes with no outgoing edges.
        
        **Validates: Requirements 6.5**
        """
        nodes = [
            LogicNode(
                node_id="n_test_ch_0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                summary="Entry node",
                metadata={}
            ),
            LogicNode(
                node_id="n_test_ch_1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.SUMMARY,
                summary="Terminal node",
                metadata={}
            )
        ]
        
        edge = LogicEdge(
            from_node="n_test_ch_0",
            to_node="n_test_ch_1",
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=nodes,
            edges=[edge],
            narrative_order=["n_test_ch_0", "n_test_ch_1"],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=[],  # Missing terminal nodes
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        assert len(repaired_chain.terminal_nodes) > 0, "Terminal nodes should be promoted"
        assert "n_test_ch_1" in repaired_chain.terminal_nodes, "Node with no outgoing edges should be terminal"
        assert any("terminal_nodes" in r.lower() for r in repairs)

    def test_repair_duplicate_edges(self):
        """
        Test that duplicate edges are removed.
        
        **Validates: Requirements 6.5**
        """
        nodes = [
            LogicNode(
                node_id="n_test_ch_0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                summary="Entry node",
                metadata={}
            ),
            LogicNode(
                node_id="n_test_ch_1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.SUMMARY,
                summary="Terminal node",
                metadata={}
            )
        ]
        
        # Duplicate edges
        edges = [
            LogicEdge(
                from_node="n_test_ch_0",
                to_node="n_test_ch_1",
                relation=EdgeRelation.LEADS_TO,
                metadata={}
            ),
            LogicEdge(
                from_node="n_test_ch_0",
                to_node="n_test_ch_1",
                relation=EdgeRelation.LEADS_TO,
                metadata={}
            )
        ]
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=nodes,
            edges=edges,
            narrative_order=["n_test_ch_0", "n_test_ch_1"],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_1"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        assert len(repaired_chain.edges) == 1, "Duplicate edge should be removed"
        assert any("duplicate" in r.lower() for r in repairs)

    def test_repair_narrative_order_missing_nodes(self):
        """
        Test that missing nodes are added to narrative_order.
        
        **Validates: Requirements 6.5**
        """
        nodes = [
            LogicNode(
                node_id="n_test_ch_0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                summary="Entry node",
                metadata={}
            ),
            LogicNode(
                node_id="n_test_ch_1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.SUMMARY,
                summary="Terminal node",
                metadata={}
            )
        ]
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=nodes,
            edges=[],
            narrative_order=["n_test_ch_0"],  # Missing n_test_ch_1
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_1"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        assert len(repaired_chain.narrative_order) == 2, "Missing node should be added"
        assert "n_test_ch_1" in repaired_chain.narrative_order
        assert any("missing" in r.lower() for r in repairs)

    def test_repair_narrative_order_duplicates(self):
        """
        Test that duplicate entries are removed from narrative_order.
        
        **Validates: Requirements 6.5**
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Test node",
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=[node],
            edges=[],
            narrative_order=["n_test_ch_0", "n_test_ch_0"],  # Duplicate
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_0"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        assert len(repaired_chain.narrative_order) == 1, "Duplicate should be removed"
        assert any("duplicate" in r.lower() for r in repairs)

    def test_repair_narrative_order_extra_nodes(self):
        """
        Test that non-existent nodes are removed from narrative_order.
        
        **Validates: Requirements 6.5**
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Test node",
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=[node],
            edges=[],
            narrative_order=["n_test_ch_0", "n_nonexistent"],  # Extra non-existent node
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=["n_test_ch_0"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        assert len(repaired_chain.narrative_order) == 1, "Non-existent node should be removed"
        assert "n_nonexistent" not in repaired_chain.narrative_order
        assert any("non-existent" in r.lower() for r in repairs)

    def test_repair_reports_all_repairs(self):
        """
        Test that all repairs are reported.
        
        **Validates: Requirements 6.5**
        """
        nodes = [
            LogicNode(
                node_id="n_test_ch_0",
                snippet_ids=["ns_test_000"],
                role=SnippetRole.MAIN,
                summary="Entry node",
                metadata={}
            ),
            LogicNode(
                node_id="n_test_ch_1",
                snippet_ids=["ns_test_001"],
                role=SnippetRole.SUMMARY,
                summary="Terminal node",
                metadata={}
            )
        ]
        
        # Multiple issues: invalid edge, missing entry/terminal, duplicate in order
        edges = [
            LogicEdge(
                from_node="n_test_ch_0",
                to_node="n_nonexistent",  # Invalid
                relation=EdgeRelation.LEADS_TO,
                metadata={}
            )
        ]
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=nodes,
            edges=edges,
            narrative_order=["n_test_ch_0"],  # Missing n_test_ch_1
            entry_nodes=[],  # Missing
            terminal_nodes=[],  # Missing
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        repaired_chain, repairs = validator.auto_repair(chain, [])
        
        # Should have multiple repairs reported
        assert len(repairs) >= 3, f"Should report multiple repairs, got: {repairs}"

    @settings(max_examples=100)
    @given(chain=chain_with_invalid_edge_refs_strategy())
    def test_auto_repair_produces_valid_chain_from_invalid_edges(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.5**
        
        Property: After auto_repair, a chain with invalid edge references should pass edge validation.
        """
        validator = LogicChainValidator()
        
        # Verify chain has invalid edges
        initial_errors = validator._validate_edge_references(chain)
        assume(len(initial_errors) > 0)
        
        # Repair
        repaired_chain, repairs = validator.auto_repair(chain, initial_errors)
        
        # Verify repaired chain passes edge validation
        final_errors = validator._validate_edge_references(repaired_chain)
        assert len(final_errors) == 0, f"Repaired chain should pass edge validation: {final_errors}"

    @settings(max_examples=100)
    @given(chain=chain_with_invalid_narrative_order_strategy())
    def test_auto_repair_produces_valid_narrative_order(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 8: Logic Chain Structural Integrity**
        **Validates: Requirements 6.5**
        
        Property: After auto_repair, a chain with invalid narrative_order should pass narrative_order validation.
        """
        validator = LogicChainValidator()
        
        # Verify chain has invalid narrative_order
        initial_errors = validator._validate_narrative_order(chain)
        assume(len(initial_errors) > 0)
        
        # Repair
        repaired_chain, repairs = validator.auto_repair(chain, initial_errors)
        
        # Verify repaired chain passes narrative_order validation
        final_errors = validator._validate_narrative_order(repaired_chain)
        assert len(final_errors) == 0, f"Repaired chain should pass narrative_order validation: {final_errors}"


class TestValidateMethod:
    """
    Tests for the validate method.
    
    **Feature: logic-chain-builder, Task 8.1-8.4**
    **Validates: Requirements 6.1, 6.2, 6.3, 6.4**
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=10))
    def test_validate_returns_valid_for_valid_chain(self, chain: LogicChain):
        """
        Property: A valid chain should return valid=True from validate().
        """
        validator = LogicChainValidator()
        result = validator.validate(chain)
        
        assert result.valid is True, f"Valid chain should pass validation: {result.errors}"
        assert len(result.errors) == 0

    @settings(max_examples=100)
    @given(chain=chain_with_invalid_edge_refs_strategy())
    def test_validate_returns_invalid_for_invalid_chain(self, chain: LogicChain):
        """
        Property: A chain with invalid edge references should return valid=False from validate().
        """
        validator = LogicChainValidator()
        result = validator.validate(chain)
        
        assert result.valid is False, "Invalid chain should fail validation"
        assert len(result.errors) > 0

    def test_validate_adds_warnings_for_empty_entry_nodes(self):
        """
        Test that validate adds warnings for missing entry nodes.
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Test node",
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=[node],
            edges=[],
            narrative_order=["n_test_ch_0"],
            entry_nodes=[],  # Empty
            terminal_nodes=["n_test_ch_0"],
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        result = validator.validate(chain)
        
        assert any("entry" in w.lower() for w in result.warnings)

    def test_validate_adds_warnings_for_empty_terminal_nodes(self):
        """
        Test that validate adds warnings for missing terminal nodes.
        """
        node = LogicNode(
            node_id="n_test_ch_0",
            snippet_ids=["ns_test_000"],
            role=SnippetRole.MAIN,
            summary="Test node",
            metadata={}
        )
        
        chain = LogicChain(
            chain_id="chain_test",
            book_id="test_book",
            nodes=[node],
            edges=[],
            narrative_order=["n_test_ch_0"],
            entry_nodes=["n_test_ch_0"],
            terminal_nodes=[],  # Empty
            metadata=SourceMetadata(),
            version="1.0.0"
        )
        
        validator = LogicChainValidator()
        result = validator.validate(chain)
        
        assert any("terminal" in w.lower() for w in result.warnings)
