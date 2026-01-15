# scripts/logic_chain_builder/tests/test_factor_cooccurrence_pbt.py
"""
Property-Based Tests for FactorCooccurrenceInferrer

Tests the factor cooccurrence edge inference functionality using Hypothesis.

**Feature: logic-chain-builder, Property 11: Factor Cooccurrence Edge Validity**
**Validates: Requirements 10.1, 10.2**
"""

from typing import List, Set

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.factor_cooccurrence import FactorCooccurrenceInferrer
from scripts.logic_chain_builder.models import LogicNode, LogicEdge, EdgeRelation, SnippetRole
from scripts.schema_extractor.models import NarrativeSnippet


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for factor IDs (lowercase alphanumeric with underscores, starting with letter)
factor_id_strategy = st.from_regex(r"[a-z][a-z0-9_]{2,15}", fullmatch=True)

# Strategy for snippet IDs
snippet_id_strategy = st.from_regex(r"ns_[a-z]{2,5}_\d{3}", fullmatch=True)

# Strategy for node IDs
node_id_strategy = st.from_regex(r"n_[a-z]{2,5}_ch\d+_\d+", fullmatch=True)

# Strategy for source references
source_ref_strategy = st.one_of(
    st.builds(
        lambda book, chapter: f"《{book}》#{chapter}",
        book=st.text(min_size=2, max_size=6, alphabet=st.characters(
            whitelist_categories=('L',),
        )).filter(lambda x: x.strip()),
        chapter=st.text(min_size=1, max_size=10, alphabet=st.characters(
            whitelist_categories=('L', 'N'),
        )).filter(lambda x: x.strip())
    ),
    st.builds(
        lambda book, chapter: f"{book}#Chapter {chapter}",
        book=st.text(min_size=2, max_size=15, alphabet=st.characters(
            whitelist_categories=('L',),
            whitelist_characters=' _'
        )).filter(lambda x: x.strip()),
        chapter=st.integers(min_value=1, max_value=100)
    )
)

# Strategy for factor_trigger field (comma-separated factor IDs)
factor_trigger_strategy = st.one_of(
    st.none(),
    st.just(""),
    st.lists(factor_id_strategy, min_size=1, max_size=5).map(lambda x: ", ".join(x))
)


@st.composite
def narrative_snippet_strategy(draw, factor_trigger=None, snippet_id=None):
    """Generate a valid NarrativeSnippet."""
    return NarrativeSnippet(
        snippet_id=snippet_id if snippet_id else draw(snippet_id_strategy),
        trigger=draw(st.text(min_size=1, max_size=30)),
        factor_trigger=factor_trigger if factor_trigger is not None else draw(factor_trigger_strategy),
        role=draw(st.sampled_from(list(SnippetRole))),
        snippet_text=draw(st.text(min_size=5, max_size=100)),
        source_ref=draw(source_ref_strategy),
    )


@st.composite
def logic_node_strategy(draw, node_id=None, snippet_ids=None, source_ref=None):
    """Generate a valid LogicNode."""
    return LogicNode(
        node_id=node_id if node_id else draw(node_id_strategy),
        snippet_ids=snippet_ids if snippet_ids else draw(st.lists(snippet_id_strategy, min_size=1, max_size=5)),
        role=draw(st.sampled_from(list(SnippetRole))),
        summary=draw(st.text(min_size=1, max_size=50)),
        metadata={"source_ref": source_ref if source_ref else draw(source_ref_strategy)},
    )


# =============================================================================
# Property 11: Factor Cooccurrence Edge Validity
# =============================================================================

class TestFactorCooccurrenceEdgeValidity:
    """
    **Feature: logic-chain-builder, Property 11: Factor Cooccurrence Edge Validity**
    **Validates: Requirements 10.1, 10.2**
    
    *For any* inferred factor cooccurrence edge, both nodes should share at least 
    one common factor_id extracted from their snippets' `factor_trigger` fields.
    """

    @settings(max_examples=100)
    @given(
        shared_factor=factor_id_strategy,
        unique_factor_a=factor_id_strategy,
        unique_factor_b=factor_id_strategy,
    )
    def test_edges_only_created_for_shared_factors(
        self,
        shared_factor: str,
        unique_factor_a: str,
        unique_factor_b: str
    ):
        """
        **Feature: logic-chain-builder, Property 11: Factor Cooccurrence Edge Validity**
        **Validates: Requirements 10.1, 10.2**
        
        Property: Edges should only be created when nodes share at least one factor.
        """
        # Ensure factors are distinct
        assume(shared_factor != unique_factor_a)
        assume(shared_factor != unique_factor_b)
        assume(unique_factor_a != unique_factor_b)
        
        inferrer = FactorCooccurrenceInferrer()
        
        # Create snippets with factors
        snippet_a = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger=f"{shared_factor}, {unique_factor_a}",
            role=SnippetRole.MAIN,
            snippet_text="Test snippet A",
            source_ref="《测试》#章节1",
        )
        
        snippet_b = NarrativeSnippet(
            snippet_id="ns_test_002",
            trigger="test",
            factor_trigger=f"{shared_factor}, {unique_factor_b}",
            role=SnippetRole.MAIN,
            snippet_text="Test snippet B",
            source_ref="《测试》#章节2",
        )
        
        # Create nodes
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        snippets = [snippet_a, snippet_b]
        
        # Build node-factor map
        node_factor_map = inferrer.build_node_factor_map(nodes, snippets)
        
        # Infer edges
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        # Should create exactly one edge (nodes share the shared_factor)
        assert len(edges) == 1, f"Expected 1 edge, got {len(edges)}"
        
        edge = edges[0]
        
        # Verify the edge has shared_factors in metadata
        assert "shared_factors" in edge.metadata
        assert shared_factor in edge.metadata["shared_factors"]
        
        # Verify inferred_from metadata
        assert edge.metadata.get("inferred_from") == "factor_cooccurrence"

    @settings(max_examples=100)
    @given(
        factor_a=factor_id_strategy,
        factor_b=factor_id_strategy,
    )
    def test_no_edges_when_no_shared_factors(
        self,
        factor_a: str,
        factor_b: str
    ):
        """
        **Feature: logic-chain-builder, Property 11: Factor Cooccurrence Edge Validity**
        **Validates: Requirements 10.1, 10.2**
        
        Property: No edges should be created when nodes don't share any factors.
        """
        # Ensure factors are distinct
        assume(factor_a != factor_b)
        
        inferrer = FactorCooccurrenceInferrer()
        
        # Create snippets with different factors
        snippet_a = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger=factor_a,
            role=SnippetRole.MAIN,
            snippet_text="Test snippet A",
            source_ref="《测试》#章节1",
        )
        
        snippet_b = NarrativeSnippet(
            snippet_id="ns_test_002",
            trigger="test",
            factor_trigger=factor_b,
            role=SnippetRole.MAIN,
            snippet_text="Test snippet B",
            source_ref="《测试》#章节2",
        )
        
        # Create nodes
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        snippets = [snippet_a, snippet_b]
        
        # Build node-factor map
        node_factor_map = inferrer.build_node_factor_map(nodes, snippets)
        
        # Infer edges
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        # Should create no edges (no shared factors)
        assert len(edges) == 0, f"Expected 0 edges, got {len(edges)}"

    @settings(max_examples=100)
    @given(
        shared_factors=st.lists(factor_id_strategy, min_size=1, max_size=5, unique=True)
    )
    def test_all_shared_factors_in_metadata(self, shared_factors: List[str]):
        """
        **Feature: logic-chain-builder, Property 11: Factor Cooccurrence Edge Validity**
        **Validates: Requirements 10.1, 10.2**
        
        Property: All shared factors should be listed in edge metadata.
        """
        inferrer = FactorCooccurrenceInferrer()
        
        # Create factor_trigger string with all shared factors
        factor_trigger = ", ".join(shared_factors)
        
        # Create snippets with the same factors
        snippet_a = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger=factor_trigger,
            role=SnippetRole.MAIN,
            snippet_text="Test snippet A",
            source_ref="《测试》#章节1",
        )
        
        snippet_b = NarrativeSnippet(
            snippet_id="ns_test_002",
            trigger="test",
            factor_trigger=factor_trigger,
            role=SnippetRole.MAIN,
            snippet_text="Test snippet B",
            source_ref="《测试》#章节2",
        )
        
        # Create nodes
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        snippets = [snippet_a, snippet_b]
        
        # Build node-factor map
        node_factor_map = inferrer.build_node_factor_map(nodes, snippets)
        
        # Infer edges
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        # Should create exactly one edge
        assert len(edges) == 1
        
        edge = edges[0]
        
        # All shared factors should be in metadata
        edge_shared_factors = set(edge.metadata.get("shared_factors", []))
        expected_factors = set(f.lower() for f in shared_factors)
        
        assert edge_shared_factors == expected_factors, (
            f"Edge shared_factors {edge_shared_factors} should equal {expected_factors}"
        )


# =============================================================================
# Additional Tests for Factor Extraction
# =============================================================================

class TestFactorExtraction:
    """
    Tests for factor extraction from snippets.
    
    **Validates: Requirements 10.2**
    """

    def test_extract_single_factor(self):
        """Property: Single factor should be extracted correctly."""
        inferrer = FactorCooccurrenceInferrer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger="day_master",
            role=SnippetRole.MAIN,
            snippet_text="Test",
            source_ref="《测试》#章节",
        )
        
        factors = inferrer.extract_factors_from_snippet(snippet)
        
        assert "day_master" in factors

    def test_extract_multiple_factors(self):
        """Property: Multiple comma-separated factors should be extracted."""
        inferrer = FactorCooccurrenceInferrer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger="day_master, month_branch, year_stem",
            role=SnippetRole.MAIN,
            snippet_text="Test",
            source_ref="《测试》#章节",
        )
        
        factors = inferrer.extract_factors_from_snippet(snippet)
        
        assert "day_master" in factors
        assert "month_branch" in factors
        assert "year_stem" in factors

    def test_extract_empty_factor_trigger(self):
        """Property: Empty factor_trigger should return empty set."""
        inferrer = FactorCooccurrenceInferrer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger="",
            role=SnippetRole.MAIN,
            snippet_text="Test",
            source_ref="《测试》#章节",
        )
        
        factors = inferrer.extract_factors_from_snippet(snippet)
        
        assert len(factors) == 0

    def test_extract_none_factor_trigger(self):
        """Property: None factor_trigger should return empty set."""
        inferrer = FactorCooccurrenceInferrer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger=None,
            role=SnippetRole.MAIN,
            snippet_text="Test",
            source_ref="《测试》#章节",
        )
        
        factors = inferrer.extract_factors_from_snippet(snippet)
        
        assert len(factors) == 0

    def test_factors_normalized_to_lowercase(self):
        """Property: Factors should be normalized to lowercase."""
        inferrer = FactorCooccurrenceInferrer()
        
        snippet = NarrativeSnippet(
            snippet_id="ns_test_001",
            trigger="test",
            factor_trigger="Day_Master, MONTH_BRANCH",
            role=SnippetRole.MAIN,
            snippet_text="Test",
            source_ref="《测试》#章节",
        )
        
        factors = inferrer.extract_factors_from_snippet(snippet)
        
        assert "day_master" in factors
        assert "month_branch" in factors


# =============================================================================
# Tests for Edge Inference Behavior
# =============================================================================

class TestEdgeInferenceBehavior:
    """
    Tests for edge inference behavior.
    
    **Validates: Requirements 10.1, 10.3, 10.4, 10.5**
    """

    def test_skip_existing_explicit_edges(self):
        """
        Property: Should skip creating edge when explicit relation already exists.
        
        **Validates: Requirements 10.4**
        """
        inferrer = FactorCooccurrenceInferrer()
        
        # Create nodes with shared factor
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        
        # Node-factor map with shared factor
        node_factor_map = {
            "n_test_ch1_0": {"shared_factor"},
            "n_test_ch2_0": {"shared_factor"},
        }
        
        # Existing explicit edge
        existing_edges = [
            LogicEdge(
                from_node="n_test_ch1_0",
                to_node="n_test_ch2_0",
                relation=EdgeRelation.DEPENDS_ON,
                condition=None,
            )
        ]
        
        edges = inferrer.infer_from_factor_cooccurrence(
            nodes, node_factor_map, existing_edges
        )
        
        # Should not create edge (explicit edge exists)
        assert len(edges) == 0

    def test_skip_existing_reverse_edges(self):
        """
        Property: Should skip creating edge when reverse explicit edge exists.
        
        **Validates: Requirements 10.4**
        """
        inferrer = FactorCooccurrenceInferrer()
        
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        
        node_factor_map = {
            "n_test_ch1_0": {"shared_factor"},
            "n_test_ch2_0": {"shared_factor"},
        }
        
        # Existing edge in reverse direction
        existing_edges = [
            LogicEdge(
                from_node="n_test_ch2_0",
                to_node="n_test_ch1_0",
                relation=EdgeRelation.DEPENDS_ON,
                condition=None,
            )
        ]
        
        edges = inferrer.infer_from_factor_cooccurrence(
            nodes, node_factor_map, existing_edges
        )
        
        # Should not create edge (reverse edge exists)
        assert len(edges) == 0

    def test_edge_direction_by_source_ref_order(self):
        """
        Property: Edge direction should be determined by source_ref proximity.
        
        **Validates: Requirements 10.3**
        """
        inferrer = FactorCooccurrenceInferrer()
        
        # Node A has earlier source_ref
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        # Node B has later source_ref
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_b, node_a]  # Intentionally reversed order
        
        node_factor_map = {
            "n_test_ch1_0": {"shared_factor"},
            "n_test_ch2_0": {"shared_factor"},
        }
        
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        assert len(edges) == 1
        
        # Edge should go from earlier to later node
        edge = edges[0]
        assert edge.from_node == "n_test_ch1_0"
        assert edge.to_node == "n_test_ch2_0"

    def test_edge_relation_is_supports(self):
        """
        Property: Factor cooccurrence edges should have relation type 'supports'.
        
        **Validates: Requirements 10.1**
        """
        inferrer = FactorCooccurrenceInferrer()
        
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        
        node_factor_map = {
            "n_test_ch1_0": {"shared_factor"},
            "n_test_ch2_0": {"shared_factor"},
        }
        
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        assert len(edges) == 1
        assert edges[0].relation == EdgeRelation.SUPPORTS

    def test_metadata_includes_inferred_from(self):
        """
        Property: Edge metadata should include inferred_from: factor_cooccurrence.
        
        **Validates: Requirements 10.5**
        """
        inferrer = FactorCooccurrenceInferrer()
        
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        
        node_factor_map = {
            "n_test_ch1_0": {"shared_factor"},
            "n_test_ch2_0": {"shared_factor"},
        }
        
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        assert len(edges) == 1
        assert edges[0].metadata.get("inferred_from") == "factor_cooccurrence"

    def test_empty_nodes_no_edges(self):
        """Property: Empty node list should produce no edges."""
        inferrer = FactorCooccurrenceInferrer()
        
        edges = inferrer.infer_from_factor_cooccurrence([], {})
        
        assert len(edges) == 0

    def test_single_node_no_edges(self):
        """Property: Single node should produce no edges."""
        inferrer = FactorCooccurrenceInferrer()
        
        node = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_factor_map = {"n_test_ch1_0": {"factor_a"}}
        
        edges = inferrer.infer_from_factor_cooccurrence([node], node_factor_map)
        
        assert len(edges) == 0

    def test_nodes_without_factors_no_edges(self):
        """Property: Nodes without factors should not produce edges."""
        inferrer = FactorCooccurrenceInferrer()
        
        node_a = LogicNode(
            node_id="n_test_ch1_0",
            snippet_ids=["ns_test_001"],
            role=SnippetRole.MAIN,
            summary="Node A",
            metadata={"source_ref": "《测试》#章节1"},
        )
        
        node_b = LogicNode(
            node_id="n_test_ch2_0",
            snippet_ids=["ns_test_002"],
            role=SnippetRole.MAIN,
            summary="Node B",
            metadata={"source_ref": "《测试》#章节2"},
        )
        
        nodes = [node_a, node_b]
        
        # Empty node-factor map
        node_factor_map = {}
        
        edges = inferrer.infer_from_factor_cooccurrence(nodes, node_factor_map)
        
        assert len(edges) == 0
