# scripts/logic_chain_builder/tests/test_writer_pbt.py
"""
Property-Based Tests for LogicChainWriter

Tests the output schema conformance of LogicChain YAML files using Hypothesis.

**Feature: logic-chain-builder, Property 9: Output Schema Conformance**
**Validates: Requirements 7.2, 7.3**
"""

import tempfile
from pathlib import Path

import pytest
import yaml
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.models import (
    LogicChain, LogicNode, LogicEdge, SnippetRole, EdgeRelation, SourceMetadata
)
from scripts.logic_chain_builder.writer import LogicChainWriter


# =============================================================================
# Hypothesis Strategies
# =============================================================================

node_role_strategy = st.sampled_from(list(SnippetRole))
edge_relation_strategy = st.sampled_from(list(EdgeRelation))


@st.composite
def valid_logic_node_strategy(draw, node_id: str):
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
def valid_logic_chain_strategy(draw, min_nodes=1, max_nodes=8):
    """
    Generate a structurally valid LogicChain for round-trip testing.
    
    This strategy ensures:
    - All edge references point to existing nodes
    - Entry nodes have no incoming edges
    - Terminal nodes have no outgoing edges
    - narrative_order contains all node_ids exactly once
    """
    num_nodes = draw(st.integers(min_value=min_nodes, max_value=max_nodes))
    
    # Generate a valid book_id (alphanumeric with underscores)
    book_id = draw(st.from_regex(r"[a-z][a-z0-9_]{2,20}", fullmatch=True))
    
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
    
    # Generate valid edges (DAG structure)
    edges = []
    for i in range(num_nodes - 1):
        from_node = nodes[i].node_id
        to_node = nodes[i + 1].node_id
        edge = LogicEdge(
            from_node=from_node,
            to_node=to_node,
            relation=draw(edge_relation_strategy),
            metadata={}
        )
        edges.append(edge)
    
    # Entry nodes: first node
    entry_nodes = [nodes[0].node_id] if nodes else []
    
    # Terminal nodes: last node
    terminal_nodes = [nodes[-1].node_id] if nodes else []
    
    # narrative_order: all nodes in order
    narrative_order = node_ids.copy()
    
    return LogicChain(
        chain_id=f"chain_{book_id[:10]}",
        book_id=book_id,
        nodes=nodes,
        edges=edges,
        narrative_order=narrative_order,
        entry_nodes=entry_nodes,
        terminal_nodes=terminal_nodes,
        metadata=SourceMetadata(
            version="1.0.0",
            source_files=[f"data/schema_staging/snippets/{book_id}_snippets.yaml"],
            snippet_count=num_nodes,
            relation_count=len(edges)
        ),
        version="1.0.0"
    )


# =============================================================================
# Property 9: Output Schema Conformance
# =============================================================================

class TestOutputSchemaConformance:
    """
    **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
    **Validates: Requirements 7.2, 7.3**
    
    *For any* written LogicChain YAML file, parsing it back should produce 
    a valid LogicChain object that passes Pydantic validation.
    """

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=1, max_nodes=10))
    def test_round_trip_preserves_structure(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 7.2, 7.3**
        
        Property: For any valid LogicChain, writing to YAML and parsing back
        should produce a valid LogicChain that passes Pydantic validation.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            writer = LogicChainWriter(output_dir=tmpdir)
            
            # Write the chain
            output_path = writer.write(chain)
            
            # Verify file exists
            assert output_path.exists(), "Output file should exist"
            
            # Parse back the YAML
            with open(output_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Validate by creating a new LogicChain from the data
            # This will raise ValidationError if schema is invalid
            parsed_chain = LogicChain.model_validate(data)
            
            # Verify key fields are preserved
            assert parsed_chain.chain_id == chain.chain_id
            assert parsed_chain.book_id == chain.book_id
            assert len(parsed_chain.nodes) == len(chain.nodes)
            assert len(parsed_chain.edges) == len(chain.edges)
            assert parsed_chain.narrative_order == chain.narrative_order
            assert parsed_chain.entry_nodes == chain.entry_nodes
            assert parsed_chain.terminal_nodes == chain.terminal_nodes

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=1, max_nodes=10))
    def test_metadata_is_complete(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 7.2**
        
        Property: For any written LogicChain, the output should include
        complete metadata (version, extracted_at, source_files).
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            writer = LogicChainWriter(output_dir=tmpdir)
            output_path = writer.write(chain)
            
            with open(output_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Verify metadata exists and is complete
            assert 'metadata' in data, "Output should contain metadata"
            metadata = data['metadata']
            
            assert 'version' in metadata, "Metadata should contain version"
            assert metadata['version'], "Version should not be empty"
            
            assert 'extracted_at' in metadata, "Metadata should contain extracted_at"
            assert metadata['extracted_at'], "extracted_at should not be empty"
            
            assert 'source_files' in metadata, "Metadata should contain source_files"
            assert isinstance(metadata['source_files'], list), "source_files should be a list"

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=8))
    def test_nodes_preserve_all_fields(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 7.3**
        
        Property: For any written LogicChain, all node fields should be preserved.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            writer = LogicChainWriter(output_dir=tmpdir)
            output_path = writer.write(chain)
            
            with open(output_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            parsed_chain = LogicChain.model_validate(data)
            
            # Verify each node's fields are preserved
            for original, parsed in zip(chain.nodes, parsed_chain.nodes):
                assert parsed.node_id == original.node_id
                assert parsed.snippet_ids == original.snippet_ids
                assert parsed.role == original.role
                assert parsed.summary == original.summary
                # condition may be None
                assert parsed.condition == original.condition

    @settings(max_examples=100)
    @given(chain=valid_logic_chain_strategy(min_nodes=2, max_nodes=8))
    def test_edges_preserve_all_fields(self, chain: LogicChain):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 7.3**
        
        Property: For any written LogicChain, all edge fields should be preserved.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            writer = LogicChainWriter(output_dir=tmpdir)
            output_path = writer.write(chain)
            
            with open(output_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            parsed_chain = LogicChain.model_validate(data)
            
            # Verify each edge's fields are preserved
            for original, parsed in zip(chain.edges, parsed_chain.edges):
                assert parsed.from_node == original.from_node
                assert parsed.to_node == original.to_node
                assert parsed.relation == original.relation
                assert parsed.condition == original.condition


# =============================================================================
# Additional Writer Tests
# =============================================================================

class TestWriterFunctionality:
    """
    Additional tests for LogicChainWriter functionality.
    
    **Validates: Requirements 7.1, 7.4, 7.5**
    """

    def test_creates_output_directory(self):
        """
        Test that the writer creates the output directory if it doesn't exist.
        
        **Validates: Requirements 7.4**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Use a nested directory that doesn't exist
            nested_dir = Path(tmpdir) / "nested" / "output" / "dir"
            
            chain = LogicChain(
                chain_id="chain_test",
                book_id="test_book",
                nodes=[],
                edges=[],
                narrative_order=[],
                entry_nodes=[],
                terminal_nodes=[],
                metadata=SourceMetadata(),
                version="1.0.0"
            )
            
            writer = LogicChainWriter(output_dir=str(nested_dir))
            output_path = writer.write(chain)
            
            assert nested_dir.exists(), "Output directory should be created"
            assert output_path.exists(), "Output file should exist"

    def test_backup_existing_file(self):
        """
        Test that existing files are backed up before overwriting.
        
        **Validates: Requirements 7.5**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            chain = LogicChain(
                chain_id="chain_test",
                book_id="test_book",
                nodes=[],
                edges=[],
                narrative_order=[],
                entry_nodes=[],
                terminal_nodes=[],
                metadata=SourceMetadata(),
                version="1.0.0"
            )
            
            writer = LogicChainWriter(output_dir=tmpdir)
            
            # Write first time
            writer.write(chain)
            
            # Write second time (should create backup)
            writer.write(chain)
            
            # Check for backup file
            backup_files = list(Path(tmpdir).glob("*.bak"))
            assert len(backup_files) == 1, "Should have exactly one backup file"

    def test_output_path_format(self):
        """
        Test that output path follows the expected format.
        
        **Validates: Requirements 7.1**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            chain = LogicChain(
                chain_id="chain_test",
                book_id="my_test_book",
                nodes=[],
                edges=[],
                narrative_order=[],
                entry_nodes=[],
                terminal_nodes=[],
                metadata=SourceMetadata(),
                version="1.0.0"
            )
            
            writer = LogicChainWriter(output_dir=tmpdir)
            output_path = writer.write(chain)
            
            assert output_path.name == "my_test_book.yaml"
            assert output_path.parent == Path(tmpdir)

    def test_yaml_is_valid_and_readable(self):
        """
        Test that the output YAML is valid and human-readable.
        
        **Validates: Requirements 7.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            chain = LogicChain(
                chain_id="chain_test",
                book_id="test_book",
                nodes=[
                    LogicNode(
                        node_id="n_test_ch_0",
                        snippet_ids=["ns_test_000"],
                        role=SnippetRole.MAIN,
                        summary="测试节点"  # Chinese characters
                    )
                ],
                edges=[],
                narrative_order=["n_test_ch_0"],
                entry_nodes=["n_test_ch_0"],
                terminal_nodes=["n_test_ch_0"],
                metadata=SourceMetadata(),
                version="1.0.0"
            )
            
            writer = LogicChainWriter(output_dir=tmpdir)
            output_path = writer.write(chain)
            
            # Read raw content
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verify Chinese characters are preserved (not escaped)
            assert "测试节点" in content, "Chinese characters should be preserved"
            
            # Verify it's valid YAML
            data = yaml.safe_load(content)
            assert data is not None

    def test_empty_chain_writes_successfully(self):
        """
        Test that an empty chain can be written successfully.
        
        **Validates: Requirements 7.1, 7.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
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
            
            writer = LogicChainWriter(output_dir=tmpdir)
            output_path = writer.write(chain)
            
            assert output_path.exists()
            
            # Verify it can be parsed back
            with open(output_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            parsed = LogicChain.model_validate(data)
            assert parsed.chain_id == "chain_empty"
            assert len(parsed.nodes) == 0
            assert len(parsed.edges) == 0
