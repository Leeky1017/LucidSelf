# scripts/logic_chain_builder/tests/test_edge_inferrer_pbt.py
"""
Property-Based Tests for EdgeInferrer

Tests the edge inference functionality using Hypothesis.
"""

from typing import List, Optional

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.edge_inferrer import EdgeInferrer
from scripts.logic_chain_builder.models import LogicNode, LogicEdge, EdgeRelation, SnippetRole
from scripts.logic_chain_builder.constants import RELATION_TYPE_MAPPING
from scripts.schema_extractor.models import ConfigRelation


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for relation types that map to depends_on
depends_on_types_strategy = st.sampled_from(["hierarchy", "dependency"])

# Strategy for relation types that map to supports
supports_types_strategy = st.sampled_from(["cooperation", "supports"])

# Strategy for relation types that map to leads_to
leads_to_types_strategy = st.sampled_from(["conditional", "gateway"])

# Strategy for relation types that map to conflicts_with
conflicts_with_types_strategy = st.just("conflict")

# Strategy for all known relation types
known_relation_type_strategy = st.sampled_from(list(RELATION_TYPE_MAPPING.keys()))

# Strategy for unknown relation types
unknown_relation_type_strategy = st.text(
    min_size=1,
    max_size=20,
    alphabet=st.characters(whitelist_categories=('L', 'N'))
).filter(lambda x: x.lower().strip() not in RELATION_TYPE_MAPPING)

# Strategy for factor IDs
factor_id_strategy = st.from_regex(r"[a-z][a-z0-9_]{2,20}", fullmatch=True)

# Strategy for relation IDs
relation_id_strategy = st.from_regex(r"rel_[a-z]{2,5}_\d{3}", fullmatch=True)

# Strategy for source references
source_ref_strategy = st.one_of(
    st.builds(
        lambda book, chapter: f"《{book}》#{chapter}",
        book=st.text(min_size=2, max_size=10, alphabet=st.characters(
            whitelist_categories=('L',),
        )).filter(lambda x: x.strip()),
        chapter=st.text(min_size=1, max_size=20, alphabet=st.characters(
            whitelist_categories=('L', 'N'),
        )).filter(lambda x: x.strip())
    ),
    st.builds(
        lambda book, chapter: f"{book}#Chapter {chapter}",
        book=st.text(min_size=2, max_size=20, alphabet=st.characters(
            whitelist_categories=('L',),
            whitelist_characters=' _'
        )).filter(lambda x: x.strip()),
        chapter=st.integers(min_value=1, max_value=100)
    )
)

# Strategy for condition constraints (optional)
condition_constraint_strategy = st.one_of(
    st.none(),
    st.just(""),
    st.text(min_size=1, max_size=100, alphabet=st.characters(
        whitelist_categories=('L', 'N', 'P'),
        whitelist_characters=' '
    )).filter(lambda x: x.strip())
)


@st.composite
def config_relation_strategy(draw, relation_type=None, condition_constraint=None):
    """Generate a valid ConfigRelation."""
    return ConfigRelation(
        relation_id=draw(relation_id_strategy),
        relation_type=relation_type if relation_type else draw(known_relation_type_strategy),
        factor_a=draw(factor_id_strategy),
        factor_b=draw(factor_id_strategy),
        relation_nature=draw(st.text(min_size=1, max_size=20)),
        condition_constraint=condition_constraint if condition_constraint is not None else draw(condition_constraint_strategy) or "",
        effect_direction=draw(st.sampled_from(["增益", "损害", "限制", "中性"])),
        source_ref=draw(source_ref_strategy),
    )


# =============================================================================
# Property 5: Edge Type Mapping Correctness
# =============================================================================

class TestEdgeTypeMappingCorrectness:
    """
    **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
    **Validates: Requirements 4.1, 4.2, 4.3, 4.4**
    
    *For any* ConfigRelation with type in {hierarchy, dependency, cooperation, 
    supports, conditional, gateway, conflict}, the resulting LogicEdge should 
    have the correct mapped relation type.
    """

    @settings(max_examples=100)
    @given(relation_type=depends_on_types_strategy)
    def test_hierarchy_dependency_maps_to_depends_on(self, relation_type: str):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.1**
        
        Property: hierarchy and dependency relation types should map to depends_on.
        """
        inferrer = EdgeInferrer()
        result = inferrer.map_relation_type(relation_type)
        
        assert result == EdgeRelation.DEPENDS_ON, (
            f"Relation type '{relation_type}' should map to depends_on, got {result}"
        )

    @settings(max_examples=100)
    @given(relation_type=supports_types_strategy)
    def test_cooperation_supports_maps_to_supports(self, relation_type: str):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.2**
        
        Property: cooperation and supports relation types should map to supports.
        """
        inferrer = EdgeInferrer()
        result = inferrer.map_relation_type(relation_type)
        
        assert result == EdgeRelation.SUPPORTS, (
            f"Relation type '{relation_type}' should map to supports, got {result}"
        )

    @settings(max_examples=100)
    @given(relation_type=leads_to_types_strategy)
    def test_conditional_gateway_maps_to_leads_to(self, relation_type: str):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.3**
        
        Property: conditional and gateway relation types should map to leads_to.
        """
        inferrer = EdgeInferrer()
        result = inferrer.map_relation_type(relation_type)
        
        assert result == EdgeRelation.LEADS_TO, (
            f"Relation type '{relation_type}' should map to leads_to, got {result}"
        )

    @settings(max_examples=100)
    @given(relation_type=conflicts_with_types_strategy)
    def test_conflict_maps_to_conflicts_with(self, relation_type: str):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.4**
        
        Property: conflict relation type should map to conflicts_with.
        """
        inferrer = EdgeInferrer()
        result = inferrer.map_relation_type(relation_type)
        
        assert result == EdgeRelation.CONFLICTS_WITH, (
            f"Relation type '{relation_type}' should map to conflicts_with, got {result}"
        )

    @settings(max_examples=100)
    @given(relation_type=known_relation_type_strategy)
    def test_all_known_types_map_correctly(self, relation_type: str):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.1, 4.2, 4.3, 4.4**
        
        Property: All known relation types should map to their expected EdgeRelation.
        """
        inferrer = EdgeInferrer()
        result = inferrer.map_relation_type(relation_type)
        
        expected_mapping = {
            "hierarchy": EdgeRelation.DEPENDS_ON,
            "dependency": EdgeRelation.DEPENDS_ON,
            "cooperation": EdgeRelation.SUPPORTS,
            "supports": EdgeRelation.SUPPORTS,
            "conditional": EdgeRelation.LEADS_TO,
            "gateway": EdgeRelation.LEADS_TO,
            "conflict": EdgeRelation.CONFLICTS_WITH,
        }
        
        expected = expected_mapping[relation_type]
        assert result == expected, (
            f"Relation type '{relation_type}' should map to {expected}, got {result}"
        )

    @settings(max_examples=50)
    @given(relation_type=unknown_relation_type_strategy)
    def test_unknown_types_default_to_leads_to(self, relation_type: str):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.1, 4.2, 4.3, 4.4**
        
        Property: Unknown relation types should default to leads_to.
        """
        inferrer = EdgeInferrer()
        result = inferrer.map_relation_type(relation_type)
        
        assert result == EdgeRelation.LEADS_TO, (
            f"Unknown relation type '{relation_type}' should default to leads_to, got {result}"
        )

    def test_case_insensitive_mapping(self):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.1, 4.2, 4.3, 4.4**
        
        Property: Relation type mapping should be case-insensitive.
        """
        inferrer = EdgeInferrer()
        
        # Test various case variations
        test_cases = [
            ("HIERARCHY", EdgeRelation.DEPENDS_ON),
            ("Hierarchy", EdgeRelation.DEPENDS_ON),
            ("DEPENDENCY", EdgeRelation.DEPENDS_ON),
            ("COOPERATION", EdgeRelation.SUPPORTS),
            ("Supports", EdgeRelation.SUPPORTS),
            ("CONDITIONAL", EdgeRelation.LEADS_TO),
            ("Gateway", EdgeRelation.LEADS_TO),
            ("CONFLICT", EdgeRelation.CONFLICTS_WITH),
        ]
        
        for relation_type, expected in test_cases:
            result = inferrer.map_relation_type(relation_type)
            assert result == expected, (
                f"Relation type '{relation_type}' should map to {expected}, got {result}"
            )

    def test_whitespace_handling(self):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.1, 4.2, 4.3, 4.4**
        
        Property: Relation type mapping should handle leading/trailing whitespace.
        """
        inferrer = EdgeInferrer()
        
        test_cases = [
            ("  hierarchy  ", EdgeRelation.DEPENDS_ON),
            ("\tdependency\n", EdgeRelation.DEPENDS_ON),
            (" cooperation ", EdgeRelation.SUPPORTS),
        ]
        
        for relation_type, expected in test_cases:
            result = inferrer.map_relation_type(relation_type)
            assert result == expected, (
                f"Relation type '{relation_type}' should map to {expected}, got {result}"
            )

    def test_empty_and_none_handling(self):
        """
        **Feature: logic-chain-builder, Property 5: Edge Type Mapping Correctness**
        **Validates: Requirements 4.1, 4.2, 4.3, 4.4**
        
        Property: Empty or None relation types should default to leads_to.
        """
        inferrer = EdgeInferrer()
        
        # Empty string
        result = inferrer.map_relation_type("")
        assert result == EdgeRelation.LEADS_TO
        
        # Whitespace only
        result = inferrer.map_relation_type("   ")
        assert result == EdgeRelation.LEADS_TO



# =============================================================================
# Property 6: Condition Propagation
# =============================================================================

class TestConditionPropagation:
    """
    **Feature: logic-chain-builder, Property 6: Condition Propagation**
    **Validates: Requirements 4.5**
    
    *For any* ConfigRelation with non-null `condition_constraint`, the resulting 
    LogicEdge should have the same value in its `condition` field.
    """

    @settings(max_examples=100)
    @given(
        condition=st.text(
            min_size=1,
            max_size=100,
            alphabet=st.characters(
                whitelist_categories=('L', 'N', 'P'),
                whitelist_characters=' '
            )
        ).filter(lambda x: x.strip())
    )
    def test_non_empty_condition_propagated(self, condition: str):
        """
        **Feature: logic-chain-builder, Property 6: Condition Propagation**
        **Validates: Requirements 4.5**
        
        Property: Non-empty condition_constraint should be copied to edge condition.
        """
        inferrer = EdgeInferrer()
        
        # Create a relation with the condition
        relation = ConfigRelation(
            relation_id="rel_test_001",
            relation_type="hierarchy",
            factor_a="factor_a",
            factor_b="factor_b",
            relation_nature="test",
            condition_constraint=condition,
            effect_direction="增益",
            source_ref="《测试》#章节",
        )
        
        # Create node-factor mapping where both factors are in different nodes
        node_factor_map = {
            "n_test_ch_0": ["factor_a"],
            "n_test_ch_1": ["factor_b"],
        }
        
        edges = inferrer.infer_from_relations([relation], node_factor_map)
        
        # Should create at least one edge
        assert len(edges) >= 1, "Should create at least one edge"
        
        # The edge should have the condition propagated
        edge = edges[0]
        assert edge.condition == condition.strip(), (
            f"Edge condition '{edge.condition}' should equal '{condition.strip()}'"
        )

    @settings(max_examples=50)
    @given(
        condition=st.one_of(
            st.none(),
            st.just(""),
            st.sampled_from([" ", "  ", "\t", "\n", "   \t\n  "])
        )
    )
    def test_empty_condition_not_propagated(self, condition: Optional[str]):
        """
        **Feature: logic-chain-builder, Property 6: Condition Propagation**
        **Validates: Requirements 4.5**
        
        Property: Empty or whitespace-only condition_constraint should result in None condition.
        """
        inferrer = EdgeInferrer()
        
        # Create a relation with empty/None condition
        relation = ConfigRelation(
            relation_id="rel_test_001",
            relation_type="hierarchy",
            factor_a="factor_a",
            factor_b="factor_b",
            relation_nature="test",
            condition_constraint=condition if condition is not None else "",
            effect_direction="增益",
            source_ref="《测试》#章节",
        )
        
        # Create node-factor mapping
        node_factor_map = {
            "n_test_ch_0": ["factor_a"],
            "n_test_ch_1": ["factor_b"],
        }
        
        edges = inferrer.infer_from_relations([relation], node_factor_map)
        
        # Should create at least one edge
        assert len(edges) >= 1, "Should create at least one edge"
        
        # The edge should have None condition
        edge = edges[0]
        assert edge.condition is None, (
            f"Edge condition should be None for empty constraint, got '{edge.condition}'"
        )

    @settings(max_examples=100)
    @given(
        conditions=st.lists(
            st.text(
                min_size=1,
                max_size=50,
                alphabet=st.characters(
                    whitelist_categories=('L', 'N', 'P'),
                    whitelist_characters=' '
                )
            ).filter(lambda x: x.strip()),
            min_size=2,
            max_size=5
        )
    )
    def test_multiple_relations_preserve_conditions(self, conditions: List[str]):
        """
        **Feature: logic-chain-builder, Property 6: Condition Propagation**
        **Validates: Requirements 4.5**
        
        Property: Each relation's condition should be preserved in its corresponding edge.
        """
        inferrer = EdgeInferrer()
        
        # Create multiple relations with different conditions
        relations = []
        node_factor_map = {}
        
        for i, condition in enumerate(conditions):
            factor_a = f"factor_a_{i}"
            factor_b = f"factor_b_{i}"
            
            relation = ConfigRelation(
                relation_id=f"rel_test_{i:03d}",
                relation_type="hierarchy",
                factor_a=factor_a,
                factor_b=factor_b,
                relation_nature="test",
                condition_constraint=condition,
                effect_direction="增益",
                source_ref="《测试》#章节",
            )
            relations.append(relation)
            
            # Each factor pair in different nodes
            node_factor_map[f"n_test_ch_{i*2}"] = [factor_a]
            node_factor_map[f"n_test_ch_{i*2+1}"] = [factor_b]
        
        edges = inferrer.infer_from_relations(relations, node_factor_map)
        
        # Should create one edge per relation
        assert len(edges) == len(conditions), (
            f"Expected {len(conditions)} edges, got {len(edges)}"
        )
        
        # Each edge should have its corresponding condition
        edge_conditions = {e.condition for e in edges}
        expected_conditions = {c.strip() for c in conditions}
        
        assert edge_conditions == expected_conditions, (
            f"Edge conditions {edge_conditions} should match expected {expected_conditions}"
        )

    def test_condition_whitespace_trimmed(self):
        """
        **Feature: logic-chain-builder, Property 6: Condition Propagation**
        **Validates: Requirements 4.5**
        
        Property: Condition should have leading/trailing whitespace trimmed.
        """
        inferrer = EdgeInferrer()
        
        relation = ConfigRelation(
            relation_id="rel_test_001",
            relation_type="hierarchy",
            factor_a="factor_a",
            factor_b="factor_b",
            relation_nature="test",
            condition_constraint="  日主旺相  ",  # With whitespace
            effect_direction="增益",
            source_ref="《测试》#章节",
        )
        
        node_factor_map = {
            "n_test_ch_0": ["factor_a"],
            "n_test_ch_1": ["factor_b"],
        }
        
        edges = inferrer.infer_from_relations([relation], node_factor_map)
        
        assert len(edges) >= 1
        assert edges[0].condition == "日主旺相", (
            f"Condition should be trimmed, got '{edges[0].condition}'"
        )


# =============================================================================
# Additional Tests for infer_from_relations
# =============================================================================

class TestInferFromRelations:
    """
    Additional tests for the infer_from_relations function.
    
    **Validates: Requirements 4.1, 4.2, 4.3, 4.4, 4.5**
    """

    def test_no_edges_when_factors_not_in_nodes(self):
        """Property: No edges should be created when factors are not in any node."""
        inferrer = EdgeInferrer()
        
        relation = ConfigRelation(
            relation_id="rel_test_001",
            relation_type="hierarchy",
            factor_a="unknown_factor_a",
            factor_b="unknown_factor_b",
            relation_nature="test",
            condition_constraint="",
            effect_direction="增益",
            source_ref="《测试》#章节",
        )
        
        # Empty node-factor mapping
        node_factor_map = {}
        
        edges = inferrer.infer_from_relations([relation], node_factor_map)
        
        assert len(edges) == 0, "Should not create edges when factors not in nodes"

    def test_no_self_loops(self):
        """Property: No self-loop edges should be created."""
        inferrer = EdgeInferrer()
        
        relation = ConfigRelation(
            relation_id="rel_test_001",
            relation_type="hierarchy",
            factor_a="factor_a",
            factor_b="factor_b",
            relation_nature="test",
            condition_constraint="",
            effect_direction="增益",
            source_ref="《测试》#章节",
        )
        
        # Both factors in the same node
        node_factor_map = {
            "n_test_ch_0": ["factor_a", "factor_b"],
        }
        
        edges = inferrer.infer_from_relations([relation], node_factor_map)
        
        # Should not create self-loop
        for edge in edges:
            assert edge.from_node != edge.to_node, "Should not create self-loop edges"

    def test_no_duplicate_edges(self):
        """Property: No duplicate edges should be created."""
        inferrer = EdgeInferrer()
        
        # Two relations that would create the same edge
        relations = [
            ConfigRelation(
                relation_id="rel_test_001",
                relation_type="hierarchy",
                factor_a="factor_a",
                factor_b="factor_b",
                relation_nature="test",
                condition_constraint="",
                effect_direction="增益",
                source_ref="《测试》#章节",
            ),
            ConfigRelation(
                relation_id="rel_test_002",
                relation_type="hierarchy",  # Same type
                factor_a="factor_a",
                factor_b="factor_b",
                relation_nature="test",
                condition_constraint="",
                effect_direction="增益",
                source_ref="《测试》#章节",
            ),
        ]
        
        node_factor_map = {
            "n_test_ch_0": ["factor_a"],
            "n_test_ch_1": ["factor_b"],
        }
        
        edges = inferrer.infer_from_relations(relations, node_factor_map)
        
        # Should only create one edge (no duplicates)
        edge_keys = [(e.from_node, e.to_node, e.relation.value) for e in edges]
        assert len(edge_keys) == len(set(edge_keys)), "Should not create duplicate edges"

    def test_metadata_includes_source_info(self):
        """Property: Edge metadata should include source relation info."""
        inferrer = EdgeInferrer()
        
        relation = ConfigRelation(
            relation_id="rel_test_001",
            relation_type="hierarchy",
            factor_a="factor_a",
            factor_b="factor_b",
            relation_nature="test",
            condition_constraint="",
            effect_direction="增益",
            source_ref="《测试》#章节",
        )
        
        node_factor_map = {
            "n_test_ch_0": ["factor_a"],
            "n_test_ch_1": ["factor_b"],
        }
        
        edges = inferrer.infer_from_relations([relation], node_factor_map)
        
        assert len(edges) >= 1
        edge = edges[0]
        
        assert "source_relation_id" in edge.metadata
        assert edge.metadata["source_relation_id"] == "rel_test_001"
        assert "source_ref" in edge.metadata
        assert edge.metadata["inferred_from"] == "explicit_relation"

    @settings(max_examples=50)
    @given(
        num_relations=st.integers(min_value=1, max_value=10)
    )
    def test_multiple_relations_create_multiple_edges(self, num_relations: int):
        """
        Property: Multiple distinct relations should create multiple edges.
        """
        inferrer = EdgeInferrer()
        
        relations = []
        node_factor_map = {}
        
        for i in range(num_relations):
            factor_a = f"factor_a_{i}"
            factor_b = f"factor_b_{i}"
            
            relation = ConfigRelation(
                relation_id=f"rel_test_{i:03d}",
                relation_type="hierarchy",
                factor_a=factor_a,
                factor_b=factor_b,
                relation_nature="test",
                condition_constraint="",
                effect_direction="增益",
                source_ref="《测试》#章节",
            )
            relations.append(relation)
            
            node_factor_map[f"n_test_ch_{i*2}"] = [factor_a]
            node_factor_map[f"n_test_ch_{i*2+1}"] = [factor_b]
        
        edges = inferrer.infer_from_relations(relations, node_factor_map)
        
        assert len(edges) == num_relations, (
            f"Expected {num_relations} edges, got {len(edges)}"
        )



# =============================================================================
# Tests for infer_sequential_edges
# =============================================================================

class TestInferSequentialEdges:
    """
    Tests for the infer_sequential_edges function.
    
    **Validates: Requirements 4.6**
    
    Infer leads_to edges for sequential snippets in same chapter.
    Only create edge when no explicit relation exists.
    """

    def _create_node(
        self,
        node_id: str,
        role: SnippetRole = SnippetRole.MAIN,
        source_ref: str = "《测试》#章节1"
    ) -> LogicNode:
        """Helper to create a LogicNode for testing."""
        return LogicNode(
            node_id=node_id,
            snippet_ids=[f"ns_test_{node_id}"],
            role=role,
            summary="测试节点",
            metadata={"source_ref": source_ref},
        )

    def test_sequential_edges_created_for_same_chapter(self):
        """
        Property: Sequential nodes in the same chapter should have leads_to edges.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        # Create nodes in the same chapter
        nodes = [
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_1", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_2", source_ref="《测试》#章节1"),
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        # Should create 2 edges: 0->1 and 1->2
        assert len(edges) == 2
        
        # Check edge types
        for edge in edges:
            assert edge.relation == EdgeRelation.LEADS_TO
            assert edge.metadata.get("inferred_from") == "sequential_order"

    def test_no_edges_between_different_chapters(self):
        """
        Property: Nodes in different chapters should not have sequential edges.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        # Create nodes in different chapters
        nodes = [
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch2_0", source_ref="《测试》#章节2"),
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        # Should create no edges (different chapters)
        assert len(edges) == 0

    def test_skip_existing_edges(self):
        """
        Property: Should not create edge when explicit relation already exists.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        nodes = [
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_1", source_ref="《测试》#章节1"),
        ]
        
        # Existing edge between the nodes
        existing_edges = [
            LogicEdge(
                from_node="n_test_ch1_0",
                to_node="n_test_ch1_1",
                relation=EdgeRelation.DEPENDS_ON,
                condition=None,
            )
        ]
        
        edges = inferrer.infer_sequential_edges(nodes, existing_edges)
        
        # Should create no new edges (explicit edge exists)
        assert len(edges) == 0

    def test_nodes_sorted_by_sequence(self):
        """
        Property: Edges should follow node sequence order, not input order.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        # Create nodes out of order
        nodes = [
            self._create_node("n_test_ch1_2", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_1", source_ref="《测试》#章节1"),
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        # Should create edges in sequence order: 0->1, 1->2
        assert len(edges) == 2
        
        edge_pairs = [(e.from_node, e.to_node) for e in edges]
        assert ("n_test_ch1_0", "n_test_ch1_1") in edge_pairs
        assert ("n_test_ch1_1", "n_test_ch1_2") in edge_pairs

    def test_single_node_no_edges(self):
        """
        Property: Single node should produce no edges.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        nodes = [
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        assert len(edges) == 0

    def test_empty_nodes_no_edges(self):
        """
        Property: Empty node list should produce no edges.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        edges = inferrer.infer_sequential_edges([])
        
        assert len(edges) == 0

    def test_multiple_chapters_independent_sequences(self):
        """
        Property: Multiple chapters should have independent sequential edges.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        # Create nodes in two chapters
        nodes = [
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_1", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch2_0", source_ref="《测试》#章节2"),
            self._create_node("n_test_ch2_1", source_ref="《测试》#章节2"),
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        # Should create 2 edges: one per chapter
        assert len(edges) == 2
        
        edge_pairs = [(e.from_node, e.to_node) for e in edges]
        assert ("n_test_ch1_0", "n_test_ch1_1") in edge_pairs
        assert ("n_test_ch2_0", "n_test_ch2_1") in edge_pairs

    @settings(max_examples=50)
    @given(
        num_nodes=st.integers(min_value=2, max_value=10)
    )
    def test_n_nodes_create_n_minus_1_edges(self, num_nodes: int):
        """
        Property: N sequential nodes should create N-1 edges.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        nodes = [
            LogicNode(
                node_id=f"n_test_ch1_{i}",
                snippet_ids=[f"ns_test_{i}"],
                role=SnippetRole.MAIN,
                summary="测试",
                metadata={"source_ref": "《测试》#章节1"},
            )
            for i in range(num_nodes)
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        assert len(edges) == num_nodes - 1, (
            f"Expected {num_nodes - 1} edges for {num_nodes} nodes, got {len(edges)}"
        )

    def test_edge_metadata_includes_chapter(self):
        """
        Property: Edge metadata should include chapter information.
        
        **Validates: Requirements 4.6**
        """
        inferrer = EdgeInferrer()
        
        nodes = [
            self._create_node("n_test_ch1_0", source_ref="《测试》#章节1"),
            self._create_node("n_test_ch1_1", source_ref="《测试》#章节1"),
        ]
        
        edges = inferrer.infer_sequential_edges(nodes)
        
        assert len(edges) == 1
        assert "chapter" in edges[0].metadata
        assert edges[0].metadata["inferred_from"] == "sequential_order"
