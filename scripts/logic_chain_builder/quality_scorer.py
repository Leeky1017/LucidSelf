"""
QualityScorer - Multi-dimensional quality scoring for LogicChains

Evaluates logic chain quality across multiple dimensions:
- Connectivity: ratio of nodes in largest connected component
- Argument completeness: presence of entry→middle→terminal pattern
- Orphan ratio: nodes with no edges / total nodes
- Cycle count: number of cycles before breaking

**Feature: logic-chain-builder**
**Validates: Requirements 12.1, 12.2, 12.3, 12.4, 12.5**
"""

from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml
from pydantic import BaseModel, Field

from scripts.logic_chain_builder.models import LogicChain, LogicEdge
from scripts.logic_chain_builder.logging_config import get_logger


logger = get_logger(__name__)


# Quality thresholds for pass/fail determination (defaults)
COVERAGE_THRESHOLD = 0.8
CONNECTIVITY_THRESHOLD = 0.7
ARGUMENT_COMPLETENESS_THRESHOLD = 0.5
ORPHAN_RATIO_THRESHOLD = 0.2

# Book-specific thresholds config file
BOOK_THRESHOLDS_FILE = Path("data/logic_chains/book_quality_thresholds.yaml")


def load_book_thresholds(book_id: str) -> Dict[str, float]:
    """
    Load book-specific quality thresholds from config file.
    
    Args:
        book_id: The book identifier
        
    Returns:
        Dict with threshold values, falls back to defaults if not found
    """
    defaults = {
        "connectivity": CONNECTIVITY_THRESHOLD,
        "orphan_ratio": ORPHAN_RATIO_THRESHOLD,
        "argument_completeness": ARGUMENT_COMPLETENESS_THRESHOLD,
        "coverage": COVERAGE_THRESHOLD,
    }
    
    if not BOOK_THRESHOLDS_FILE.exists():
        return defaults
    
    try:
        with open(BOOK_THRESHOLDS_FILE) as f:
            config = yaml.safe_load(f) or {}
        
        # Check for book-specific config
        if book_id in config:
            book_config = config[book_id]
            return {
                "connectivity": book_config.get("connectivity", defaults["connectivity"]),
                "orphan_ratio": book_config.get("orphan_ratio", defaults["orphan_ratio"]),
                "argument_completeness": book_config.get("argument_completeness", defaults["argument_completeness"]),
                "coverage": book_config.get("coverage", defaults["coverage"]),
            }
        
        # Fall back to default section if exists
        if "default" in config:
            default_config = config["default"]
            return {
                "connectivity": default_config.get("connectivity", defaults["connectivity"]),
                "orphan_ratio": default_config.get("orphan_ratio", defaults["orphan_ratio"]),
                "argument_completeness": default_config.get("argument_completeness", defaults["argument_completeness"]),
                "coverage": default_config.get("coverage", defaults["coverage"]),
            }
    except Exception as e:
        logger.warning(f"Failed to load book thresholds for {book_id}: {e}")
    
    return defaults


class QualityReport(BaseModel):
    """
    Multi-dimensional quality report for a LogicChain.
    
    **Validates: Requirements 12.1, 12.2, 12.3, 12.4, 12.5**
    """
    coverage: float = Field(default=0.0, description="Snippet coverage ratio (0-1)")
    connectivity: float = Field(default=0.0, description="Largest connected component ratio (0-1)")
    argument_completeness: float = Field(default=0.0, description="Argument pattern completeness (0-1)")
    orphan_ratio: float = Field(default=0.0, description="Ratio of nodes with no edges (0-1, lower is better)")
    cycle_count: int = Field(default=0, description="Number of cycles detected before breaking")
    
    # Pass/fail status for each dimension
    coverage_pass: bool = Field(default=False, description="Coverage meets threshold")
    connectivity_pass: bool = Field(default=False, description="Connectivity meets threshold")
    argument_completeness_pass: bool = Field(default=False, description="Argument completeness meets threshold")
    orphan_ratio_pass: bool = Field(default=False, description="Orphan ratio meets threshold")
    
    def passes_threshold(self) -> bool:
        """
        Check if all quality dimensions pass their thresholds.
        
        Returns:
            True if all dimensions pass, False otherwise
        """
        return (
            self.coverage_pass and
            self.connectivity_pass and
            self.argument_completeness_pass and
            self.orphan_ratio_pass
        )
    
    def overall_score(self) -> float:
        """
        Calculate an overall quality score (0-1).
        
        Weighted average of all dimensions.
        """
        # Invert orphan_ratio since lower is better
        orphan_score = 1.0 - self.orphan_ratio
        
        # Weighted average (connectivity and argument completeness are most important)
        return (
            self.coverage * 0.2 +
            self.connectivity * 0.3 +
            self.argument_completeness * 0.3 +
            orphan_score * 0.2
        )


class LogicChainQualityScorer:
    """
    Multi-dimensional quality scorer for LogicChains.
    
    Evaluates:
    - Connectivity: ratio of nodes in largest connected component
    - Argument completeness: presence of entry→middle→terminal pattern
    - Orphan ratio: nodes with no edges / total nodes
    - Cycle count: number of cycles before breaking
    
    **Feature: logic-chain-builder**
    **Validates: Requirements 12.1, 12.2, 12.3, 12.4, 12.5**
    """
    
    def __init__(
        self,
        coverage_threshold: float = COVERAGE_THRESHOLD,
        connectivity_threshold: float = CONNECTIVITY_THRESHOLD,
        argument_completeness_threshold: float = ARGUMENT_COMPLETENESS_THRESHOLD,
        orphan_ratio_threshold: float = ORPHAN_RATIO_THRESHOLD,
    ):
        """
        Initialize the quality scorer with configurable thresholds.
        
        Args:
            coverage_threshold: Minimum coverage ratio (default 0.8)
            connectivity_threshold: Minimum connectivity ratio (default 0.7)
            argument_completeness_threshold: Minimum argument completeness (default 0.5)
            orphan_ratio_threshold: Maximum orphan ratio (default 0.2)
        """
        self.coverage_threshold = coverage_threshold
        self.connectivity_threshold = connectivity_threshold
        self.argument_completeness_threshold = argument_completeness_threshold
        self.orphan_ratio_threshold = orphan_ratio_threshold

    def score(
        self,
        chain: LogicChain,
        total_snippet_count: Optional[int] = None,
    ) -> QualityReport:
        """
        Calculate quality scores for a LogicChain.
        
        Args:
            chain: The LogicChain to evaluate
            total_snippet_count: Total snippets for coverage calculation (optional)
        
        Returns:
            QualityReport with all quality dimensions
            
        **Validates: Requirements 12.1, 12.2, 12.3, 12.4, 12.5**
        """
        # Calculate each dimension
        coverage = self._calc_coverage(chain, total_snippet_count)
        connectivity = self._calc_connectivity(chain)
        argument_completeness = self._check_argument_pattern(chain)
        orphan_ratio = self._calc_orphan_ratio(chain)
        cycle_count = self._count_cycles(chain)
        
        # Determine pass/fail for each dimension
        coverage_pass = coverage >= self.coverage_threshold
        connectivity_pass = connectivity >= self.connectivity_threshold
        argument_completeness_pass = argument_completeness >= self.argument_completeness_threshold
        orphan_ratio_pass = orphan_ratio <= self.orphan_ratio_threshold
        
        report = QualityReport(
            coverage=coverage,
            connectivity=connectivity,
            argument_completeness=argument_completeness,
            orphan_ratio=orphan_ratio,
            cycle_count=cycle_count,
            coverage_pass=coverage_pass,
            connectivity_pass=connectivity_pass,
            argument_completeness_pass=argument_completeness_pass,
            orphan_ratio_pass=orphan_ratio_pass,
        )
        
        logger.debug(
            f"Quality scores for {chain.book_id}: "
            f"coverage={coverage:.2f}, connectivity={connectivity:.2f}, "
            f"argument_completeness={argument_completeness:.2f}, "
            f"orphan_ratio={orphan_ratio:.2f}, cycles={cycle_count}"
        )
        
        return report
    
    def _calc_coverage(
        self,
        chain: LogicChain,
        total_snippet_count: Optional[int] = None,
    ) -> float:
        """
        Calculate snippet coverage ratio.
        
        Coverage = snippets in nodes / total snippets
        
        Args:
            chain: The LogicChain to evaluate
            total_snippet_count: Total snippets (if None, uses metadata)
        
        Returns:
            Coverage ratio (0-1)
        """
        if not chain.nodes:
            return 0.0 if total_snippet_count and total_snippet_count > 0 else 1.0
        
        # Count unique snippets in nodes
        snippets_in_nodes: Set[str] = set()
        for node in chain.nodes:
            snippets_in_nodes.update(node.snippet_ids)
        
        # Get total snippet count
        if total_snippet_count is not None:
            total = total_snippet_count
        elif chain.metadata and chain.metadata.snippet_count > 0:
            total = chain.metadata.snippet_count
        else:
            # Fallback: assume all snippets are in nodes
            total = len(snippets_in_nodes)
        
        if total == 0:
            return 1.0
        
        return len(snippets_in_nodes) / total
    
    def _calc_connectivity(self, chain: LogicChain) -> float:
        """
        Calculate connectivity score.
        
        Connectivity = nodes in largest connected component / total nodes
        
        Uses undirected graph representation to find connected components.
        
        Args:
            chain: The LogicChain to evaluate
        
        Returns:
            Connectivity ratio (0-1)
            
        **Validates: Requirements 12.1**
        """
        if not chain.nodes:
            return 1.0  # Empty chain is trivially connected
        
        if len(chain.nodes) == 1:
            return 1.0  # Single node is trivially connected
        
        # Build undirected adjacency list
        adjacency: Dict[str, Set[str]] = defaultdict(set)
        all_node_ids: Set[str] = {node.node_id for node in chain.nodes}
        
        for edge in chain.edges:
            if edge.from_node in all_node_ids and edge.to_node in all_node_ids:
                # Add both directions for undirected graph
                adjacency[edge.from_node].add(edge.to_node)
                adjacency[edge.to_node].add(edge.from_node)
        
        # Find connected components using BFS
        visited: Set[str] = set()
        largest_component_size = 0
        
        for node_id in all_node_ids:
            if node_id not in visited:
                # BFS to find component size
                component_size = 0
                queue = [node_id]
                
                while queue:
                    current = queue.pop(0)
                    if current in visited:
                        continue
                    
                    visited.add(current)
                    component_size += 1
                    
                    # Add unvisited neighbors
                    for neighbor in adjacency[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                
                largest_component_size = max(largest_component_size, component_size)
        
        return largest_component_size / len(chain.nodes)

    def _check_argument_pattern(self, chain: LogicChain) -> float:
        """
        Check argument completeness.
        
        Evaluates presence of entry→middle→terminal pattern:
        - Has entry nodes (score +0.33)
        - Has terminal nodes (score +0.33)
        - Has middle nodes (nodes that are neither entry nor terminal) (score +0.34)
        
        Args:
            chain: The LogicChain to evaluate
        
        Returns:
            Argument completeness score (0-1)
            
        **Validates: Requirements 12.2**
        """
        if not chain.nodes:
            return 0.0
        
        score = 0.0
        
        # Check for entry nodes
        has_entry = len(chain.entry_nodes) > 0
        if has_entry:
            score += 0.33
        
        # Check for terminal nodes
        has_terminal = len(chain.terminal_nodes) > 0
        if has_terminal:
            score += 0.33
        
        # Check for middle nodes (nodes that are neither entry nor terminal)
        entry_set = set(chain.entry_nodes)
        terminal_set = set(chain.terminal_nodes)
        all_node_ids = {node.node_id for node in chain.nodes}
        
        middle_nodes = all_node_ids - entry_set - terminal_set
        has_middle = len(middle_nodes) > 0
        
        if has_middle:
            score += 0.34
        elif len(chain.nodes) <= 2:
            # For very small chains (1-2 nodes), having entry and terminal is sufficient
            if has_entry and has_terminal:
                score += 0.34
        
        return score

    def _calc_orphan_ratio(self, chain: LogicChain) -> float:
        """
        Calculate orphan ratio.
        
        Orphan ratio = nodes with no edges / total nodes
        
        A node is an orphan if it has no incoming AND no outgoing edges.
        
        Args:
            chain: The LogicChain to evaluate
        
        Returns:
            Orphan ratio (0-1, lower is better)
            
        **Validates: Requirements 12.3**
        """
        if not chain.nodes:
            return 0.0  # No nodes means no orphans
        
        # Find all nodes that participate in at least one edge
        nodes_with_edges: Set[str] = set()
        
        for edge in chain.edges:
            nodes_with_edges.add(edge.from_node)
            nodes_with_edges.add(edge.to_node)
        
        # Count orphan nodes (nodes not in any edge)
        all_node_ids = {node.node_id for node in chain.nodes}
        orphan_count = len(all_node_ids - nodes_with_edges)
        
        return orphan_count / len(chain.nodes)

    def _count_cycles(self, chain: LogicChain) -> int:
        """
        Count cycles in the graph before breaking them.
        
        Uses DFS-based cycle detection to count the number of back edges,
        which corresponds to the number of cycles in the graph.
        
        Args:
            chain: The LogicChain to evaluate
        
        Returns:
            Number of cycles detected
            
        **Validates: Requirements 12.4**
        """
        if not chain.nodes or not chain.edges:
            return 0
        
        # Build directed adjacency list
        adjacency: Dict[str, List[str]] = defaultdict(list)
        all_node_ids: Set[str] = {node.node_id for node in chain.nodes}
        
        for edge in chain.edges:
            if edge.from_node in all_node_ids and edge.to_node in all_node_ids:
                adjacency[edge.from_node].append(edge.to_node)
        
        # DFS-based cycle detection
        # Count back edges (edges pointing to ancestors in DFS tree)
        visited: Set[str] = set()
        rec_stack: Set[str] = set()  # Nodes in current recursion stack
        cycle_count = 0
        
        def dfs(node: str) -> int:
            """DFS to count back edges (cycles)."""
            nonlocal cycle_count
            
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in rec_stack:
                    # Found a back edge (cycle)
                    cycle_count += 1
            
            rec_stack.remove(node)
        
        # Run DFS from all unvisited nodes
        for node_id in all_node_ids:
            if node_id not in visited:
                dfs(node_id)
        
        return cycle_count
    
    def get_orphan_nodes(self, chain: LogicChain) -> List[str]:
        """
        Get list of orphan node IDs.
        
        Args:
            chain: The LogicChain to evaluate
        
        Returns:
            List of node IDs that have no edges
        """
        if not chain.nodes:
            return []
        
        nodes_with_edges: Set[str] = set()
        for edge in chain.edges:
            nodes_with_edges.add(edge.from_node)
            nodes_with_edges.add(edge.to_node)
        
        all_node_ids = {node.node_id for node in chain.nodes}
        return list(all_node_ids - nodes_with_edges)
    
    def get_disconnected_components(self, chain: LogicChain) -> List[Set[str]]:
        """
        Get all connected components in the graph.
        
        Args:
            chain: The LogicChain to evaluate
        
        Returns:
            List of sets, each containing node IDs in a connected component
        """
        if not chain.nodes:
            return []
        
        # Build undirected adjacency list
        adjacency: Dict[str, Set[str]] = defaultdict(set)
        all_node_ids: Set[str] = {node.node_id for node in chain.nodes}
        
        for edge in chain.edges:
            if edge.from_node in all_node_ids and edge.to_node in all_node_ids:
                adjacency[edge.from_node].add(edge.to_node)
                adjacency[edge.to_node].add(edge.from_node)
        
        # Find all connected components using BFS
        visited: Set[str] = set()
        components: List[Set[str]] = []
        
        for node_id in all_node_ids:
            if node_id not in visited:
                component: Set[str] = set()
                queue = [node_id]
                
                while queue:
                    current = queue.pop(0)
                    if current in visited:
                        continue
                    
                    visited.add(current)
                    component.add(current)
                    
                    for neighbor in adjacency[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                
                components.append(component)
        
        return components
