# scripts/logic_chain_builder/tests/test_report_pbt.py
"""
Property-Based Tests for BuildReportGenerator

Tests the report statistics accuracy using Hypothesis.

**Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
**Validates: Requirements 8.2, 8.4, 8.5**
"""

import tempfile
from pathlib import Path
from typing import List, Set, Tuple

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.models import (
    BookStats, BuildReport, LogicChain, LogicNode, LogicEdge,
    SnippetRole, EdgeRelation, SourceMetadata
)
from scripts.logic_chain_builder.report import BuildReportGenerator, LOW_COVERAGE_THRESHOLD


# =============================================================================
# Hypothesis Strategies
# =============================================================================

@st.composite
def valid_snippet_ids_strategy(draw, min_size=1, max_size=20):
    """Generate a set of valid snippet IDs."""
    count = draw(st.integers(min_value=min_size, max_value=max_size))
    return {f"ns_test_{i:03d}" for i in range(count)}


@st.composite
def valid_logic_chain_with_snippets_strategy(draw, min_snippets=1, max_snippets=30):
    """
    Generate a LogicChain along with the total snippets and used snippets.
    
    Returns: (chain, total_snippet_ids, used_snippet_ids)
    """
    # Generate book_id
    book_id = draw(st.from_regex(r"[a-z][a-z0-9_]{2,15}", fullmatch=True))
    
    # Generate total snippets
    total_count = draw(st.integers(min_value=min_snippets, max_value=max_snippets))
    total_snippet_ids = {f"ns_test_{i:03d}" for i in range(total_count)}
    snippet_list = list(total_snippet_ids)
    
    # Generate nodes
    num_nodes = draw(st.integers(min_value=1, max_value=min(10, max(1, len(snippet_list)))))
    
    nodes = []
    used_snippets: Set[str] = set()
    
    for i in range(num_nodes):
        node_id = f"n_test_ch_{i}"
        
        # Decide how many snippets this node gets
        remaining = [s for s in snippet_list if s not in used_snippets]
        if remaining:
            # Use some snippets (may leave some orphaned)
            max_to_use = min(5, len(remaining))
            num_to_use = draw(st.integers(min_value=0, max_value=max_to_use))
            if num_to_use > 0:
                # Deterministically select first N remaining snippets
                node_snippets = remaining[:num_to_use]
            else:
                node_snippets = []
        else:
            node_snippets = []
        
        used_snippets.update(node_snippets)
        
        role = SnippetRole.MAIN if i == 0 else (
            SnippetRole.SUMMARY if i == num_nodes - 1 else SnippetRole.CONDITION_BRANCH
        )
        
        node = LogicNode(
            node_id=node_id,
            snippet_ids=node_snippets,
            role=role,
            summary=f"Node {i}",
            metadata={}
        )
        nodes.append(node)
    
    # Create simple sequential edges
    edges = []
    for i in range(len(nodes) - 1):
        edges.append(LogicEdge(
            from_node=nodes[i].node_id,
            to_node=nodes[i + 1].node_id,
            relation=EdgeRelation.LEADS_TO,
            metadata={}
        ))
    
    chain = LogicChain(
        chain_id=f"chain_{book_id[:10]}",
        book_id=book_id,
        nodes=nodes,
        edges=edges,
        narrative_order=[n.node_id for n in nodes],
        entry_nodes=[nodes[0].node_id] if nodes else [],
        terminal_nodes=[nodes[-1].node_id] if nodes else [],
        metadata=SourceMetadata(
            version="1.0.0",
            source_files=[f"data/schema_staging/snippets/{book_id}_snippets.yaml"],
            snippet_count=len(total_snippet_ids),
            relation_count=len(edges)
        ),
        version="1.0.0"
    )
    
    return chain, total_snippet_ids, used_snippets


@st.composite
def valid_book_stats_strategy(draw):
    """Generate valid BookStats."""
    book_id = draw(st.from_regex(r"[a-z][a-z0-9_]{2,15}", fullmatch=True))
    status = draw(st.sampled_from(["success", "failed", "skipped"]))
    
    if status == "success":
        snippet_count = draw(st.integers(min_value=1, max_value=100))
        node_count = draw(st.integers(min_value=1, max_value=50))
        edge_count = draw(st.integers(min_value=0, max_value=100))
        # Coverage between 0 and 1
        coverage = draw(st.floats(min_value=0.0, max_value=1.0))
        orphan_count = int((1 - coverage) * snippet_count)
        orphan_snippets = [f"ns_{book_id}_{i:03d}" for i in range(orphan_count)]
        error_message = None
    else:
        snippet_count = draw(st.integers(min_value=0, max_value=100))
        node_count = 0
        edge_count = 0
        coverage = 0.0
        orphan_snippets = [f"ns_{book_id}_{i:03d}" for i in range(snippet_count)]
        error_message = draw(st.text(min_size=5, max_size=50)) if status == "failed" else None
    
    return BookStats(
        book_id=book_id,
        snippet_count=snippet_count,
        node_count=node_count,
        edge_count=edge_count,
        coverage=coverage,
        orphan_snippets=orphan_snippets,
        status=status,
        error_message=error_message
    )


# =============================================================================
# Property 10: Report Statistics Accuracy
# =============================================================================

class TestReportStatisticsAccuracy:
    """
    **Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
    **Validates: Requirements 8.2, 8.4, 8.5**
    
    *For any* generated BuildReport, the `coverage` for each book should equal 
    `len(snippets_in_nodes) / len(total_snippets)`.
    """

    @settings(max_examples=100)
    @given(chain_data=valid_logic_chain_with_snippets_strategy(min_snippets=1, max_snippets=30))
    def test_coverage_calculation_accuracy(
        self, 
        chain_data: Tuple[LogicChain, Set[str], Set[str]]
    ):
        """
        **Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
        **Validates: Requirements 8.2**
        
        Property: For any LogicChain and total snippets, the calculated coverage
        should equal len(snippets_in_nodes) / len(total_snippets).
        """
        chain, total_snippet_ids, used_snippets = chain_data
        assume(len(total_snippet_ids) > 0)
        
        generator = BuildReportGenerator()
        
        # Create book stats
        stats = generator.create_book_stats(
            book_id=chain.book_id,
            chain=chain,
            total_snippet_ids=total_snippet_ids,
            status="success"
        )
        
        # Calculate expected coverage
        expected_coverage = len(used_snippets) / len(total_snippet_ids)
        
        # Verify coverage matches
        assert abs(stats.coverage - expected_coverage) < 0.001, (
            f"Coverage mismatch: expected {expected_coverage}, got {stats.coverage}"
        )

    @settings(max_examples=100)
    @given(book_stats_list=st.lists(valid_book_stats_strategy(), min_size=1, max_size=10))
    def test_report_totals_accuracy(self, book_stats_list: List[BookStats]):
        """
        **Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
        **Validates: Requirements 8.2**
        
        Property: For any list of BookStats, the BuildReport totals should
        accurately reflect the sum of individual stats.
        """
        generator = BuildReportGenerator()
        report = generator.generate(book_stats_list)
        
        # Verify totals
        expected_total = len(book_stats_list)
        expected_successful = sum(1 for s in book_stats_list if s.status == "success")
        expected_failed = sum(1 for s in book_stats_list if s.status == "failed")
        expected_skipped = sum(1 for s in book_stats_list if s.status == "skipped")
        
        assert report.total_books == expected_total
        assert report.successful_books == expected_successful
        assert report.failed_books == expected_failed
        assert report.skipped_books == expected_skipped
        
        # Verify totals add up
        assert report.successful_books + report.failed_books + report.skipped_books == report.total_books

    @settings(max_examples=100)
    @given(book_stats_list=st.lists(valid_book_stats_strategy(), min_size=1, max_size=10))
    def test_low_coverage_detection(self, book_stats_list: List[BookStats]):
        """
        **Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
        **Validates: Requirements 8.4**
        
        Property: For any successful book with coverage < 80%, a warning should
        be generated in the report.
        """
        generator = BuildReportGenerator()
        report = generator.generate(book_stats_list)
        
        # Find books that should trigger low coverage warning
        low_coverage_books = [
            s.book_id for s in book_stats_list
            if s.status == "success" and s.coverage < LOW_COVERAGE_THRESHOLD
        ]
        
        # Verify warnings are generated for low coverage books
        for book_id in low_coverage_books:
            has_warning = any(
                book_id in warning and "coverage" in warning.lower()
                for warning in report.warnings
            )
            assert has_warning, f"Missing low coverage warning for {book_id}"

    @settings(max_examples=100)
    @given(book_stats_list=st.lists(valid_book_stats_strategy(), min_size=1, max_size=10))
    def test_orphan_snippet_detection(self, book_stats_list: List[BookStats]):
        """
        **Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
        **Validates: Requirements 8.5**
        
        Property: For any book with orphan snippets, a warning should be
        generated in the report.
        """
        generator = BuildReportGenerator()
        report = generator.generate(book_stats_list)
        
        # Find books with orphan snippets
        books_with_orphans = [
            s.book_id for s in book_stats_list
            if s.orphan_snippets
        ]
        
        # Verify warnings are generated for books with orphans
        for book_id in books_with_orphans:
            has_warning = any(
                book_id in warning and "orphan" in warning.lower()
                for warning in report.warnings
            )
            assert has_warning, f"Missing orphan snippet warning for {book_id}"


# =============================================================================
# Additional Report Tests
# =============================================================================

class TestReportOutput:
    """
    Additional tests for BuildReportGenerator output functionality.
    
    **Validates: Requirements 8.1**
    """

    def test_write_creates_file(self):
        """
        Test that write() creates the report file.
        
        **Validates: Requirements 8.1**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = BuildReportGenerator(output_dir=tmpdir)
            
            book_stats = [
                BookStats(
                    book_id="test_book",
                    snippet_count=10,
                    node_count=5,
                    edge_count=4,
                    coverage=0.9,
                    orphan_snippets=["ns_test_009"],
                    status="success"
                )
            ]
            
            report = generator.generate(book_stats)
            output_path = generator.write(report)
            
            assert output_path.exists()
            assert output_path.name == "build_report.md"

    def test_markdown_format_contains_required_sections(self):
        """
        Test that the markdown output contains all required sections.
        
        **Validates: Requirements 8.1, 8.2**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = BuildReportGenerator(output_dir=tmpdir)
            
            book_stats = [
                BookStats(
                    book_id="test_book_1",
                    snippet_count=10,
                    node_count=5,
                    edge_count=4,
                    coverage=0.9,
                    orphan_snippets=["ns_test_009"],
                    status="success"
                ),
                BookStats(
                    book_id="test_book_2",
                    snippet_count=20,
                    node_count=0,
                    edge_count=0,
                    coverage=0.0,
                    orphan_snippets=[],
                    status="failed",
                    error_message="Test error"
                )
            ]
            
            report = generator.generate(book_stats)
            output_path = generator.write(report)
            
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verify required sections
            assert "# Logic Chain Build Report" in content
            assert "## Summary" in content
            assert "## Book Statistics" in content
            assert "Total Books" in content
            assert "Successful" in content
            assert "Failed" in content

    def test_markdown_table_format(self):
        """
        Test that the book statistics are formatted as a markdown table.
        
        **Validates: Requirements 8.1**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = BuildReportGenerator(output_dir=tmpdir)
            
            book_stats = [
                BookStats(
                    book_id="test_book",
                    snippet_count=10,
                    node_count=5,
                    edge_count=4,
                    coverage=0.9,
                    orphan_snippets=[],
                    status="success"
                )
            ]
            
            report = generator.generate(book_stats)
            content = generator._format_markdown(report)
            
            # Verify table headers
            assert "| Book ID |" in content
            assert "| Status |" in content
            assert "| Snippets |" in content
            assert "| Nodes |" in content
            assert "| Edges |" in content
            assert "| Coverage |" in content

    @settings(max_examples=100)
    @given(chain_data=valid_logic_chain_with_snippets_strategy(min_snippets=1, max_snippets=20))
    def test_orphan_snippets_correctly_identified(
        self, 
        chain_data: Tuple[LogicChain, Set[str], Set[str]]
    ):
        """
        **Feature: logic-chain-builder, Property 10: Report Statistics Accuracy**
        **Validates: Requirements 8.5**
        
        Property: For any LogicChain, orphan snippets should be exactly
        total_snippets - snippets_in_nodes.
        """
        chain, total_snippet_ids, used_snippets = chain_data
        assume(len(total_snippet_ids) > 0)
        
        generator = BuildReportGenerator()
        
        # Create book stats
        stats = generator.create_book_stats(
            book_id=chain.book_id,
            chain=chain,
            total_snippet_ids=total_snippet_ids,
            status="success"
        )
        
        # Calculate expected orphans
        expected_orphans = total_snippet_ids - used_snippets
        
        # Verify orphan snippets match
        assert set(stats.orphan_snippets) == expected_orphans, (
            f"Orphan mismatch: expected {expected_orphans}, got {set(stats.orphan_snippets)}"
        )
