"""
IterativeRefinementEngine - 迭代优化引擎

自动改进逻辑链直到达到质量阈值或最大迭代次数。

**Feature: logic-chain-builder**
**Validates: Requirements 16.1, 16.2, 16.3, 16.4, 16.5**
"""

from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

from pydantic import BaseModel, Field

from scripts.logic_chain_builder.models import (
    LogicChain, LogicNode, LogicEdge, SnippetRole, EdgeRelation
)
from scripts.logic_chain_builder.quality_scorer import (
    LogicChainQualityScorer, QualityReport,
    CONNECTIVITY_THRESHOLD, ORPHAN_RATIO_THRESHOLD,
    ARGUMENT_COMPLETENESS_THRESHOLD, COVERAGE_THRESHOLD
)
from scripts.logic_chain_builder.semantic_refiner import SemanticClusterRefiner
from scripts.logic_chain_builder.summary_generator import IntelligentSummaryGenerator
from scripts.logic_chain_builder.book_type_adapter import BookTypeAdapter
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import NarrativeSnippet


logger = get_logger(__name__)


# Default configuration
MAX_ITERATIONS = 5
QUALITY_THRESHOLD_OVERALL = 0.6  # Minimum overall quality score


class RefinementRecord(BaseModel):
    """
    Record of a single refinement iteration.
    
    Tracks quality scores, changes made, and rationale for each iteration.
    
    **Validates: Requirements 16.5**
    """
    version: int = Field(..., description="Iteration version number (1-based)")
    timestamp: datetime = Field(default_factory=datetime.now, description="When this iteration occurred")
    quality_scores: QualityReport = Field(..., description="Quality scores at this iteration")
    changes: List[str] = Field(default_factory=list, description="List of changes made")
    rationale: str = Field(default="", description="Rationale for changes")
    overall_score: float = Field(default=0.0, description="Overall quality score")


class RefinementResult(BaseModel):
    """
    Result of the refinement process.
    
    Contains the refined chain, history of iterations, and summary statistics.
    """
    chain: LogicChain = Field(..., description="The refined LogicChain")
    history: List[RefinementRecord] = Field(default_factory=list, description="History of refinement iterations")
    initial_score: float = Field(default=0.0, description="Initial overall quality score")
    final_score: float = Field(default=0.0, description="Final overall quality score")
    iterations_performed: int = Field(default=0, description="Number of iterations performed")
    threshold_met: bool = Field(default=False, description="Whether quality threshold was met")
    improvements_made: List[str] = Field(default_factory=list, description="Summary of all improvements")


class IterativeRefinementEngine:
    """
    迭代优化引擎 - 自动改进逻辑链直到达到质量阈值
    
    Applies multiple improvement strategies iteratively:
    1. Semantic cluster refinement (split heterogeneous nodes)
    2. Summary improvement (generate better summaries)
    3. Connectivity improvement (add edges to connect orphan nodes)
    4. Entry/terminal node repair (ensure proper structure)
    
    **Feature: logic-chain-builder**
    **Validates: Requirements 16.1, 16.2, 16.3, 16.4, 16.5**
    """
    
    def __init__(
        self,
        max_iterations: int = MAX_ITERATIONS,
        quality_threshold: float = QUALITY_THRESHOLD_OVERALL,
        connectivity_threshold: float = CONNECTIVITY_THRESHOLD,
        orphan_ratio_threshold: float = ORPHAN_RATIO_THRESHOLD,
        argument_completeness_threshold: float = ARGUMENT_COMPLETENESS_THRESHOLD,
    ):
        """
        Initialize the refinement engine.
        
        Args:
            max_iterations: Maximum number of refinement iterations
            quality_threshold: Minimum overall quality score to achieve
            connectivity_threshold: Minimum connectivity score
            orphan_ratio_threshold: Maximum orphan ratio
            argument_completeness_threshold: Minimum argument completeness
        """
        self.max_iterations = max_iterations
        self.quality_threshold = quality_threshold
        self.connectivity_threshold = connectivity_threshold
        self.orphan_ratio_threshold = orphan_ratio_threshold
        self.argument_completeness_threshold = argument_completeness_threshold
        
        # Initialize components
        self.quality_scorer = LogicChainQualityScorer(
            connectivity_threshold=connectivity_threshold,
            orphan_ratio_threshold=orphan_ratio_threshold,
            argument_completeness_threshold=argument_completeness_threshold,
        )
        self.cluster_refiner = SemanticClusterRefiner()
        self.summary_generator = IntelligentSummaryGenerator()
        self.book_type_adapter = BookTypeAdapter()
        
        # Track refinement history
        self.history: List[RefinementRecord] = []
    
    def refine_until_threshold(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet],
        book_type: Optional[str] = None,
        total_snippet_count: Optional[int] = None,
    ) -> RefinementResult:
        """
        Iteratively refine a logic chain until quality threshold is met.
        
        Main entry point for the refinement engine. Applies improvement
        strategies in sequence until either:
        - Quality threshold is met
        - Maximum iterations reached
        - No further improvements possible
        
        Args:
            chain: The LogicChain to refine
            snippets: All snippets for the book
            book_type: Book type string (auto-detected if None)
            total_snippet_count: Total snippets for coverage calculation
            
        Returns:
            RefinementResult with refined chain and history
            
        **Validates: Requirements 16.1, 16.2, 16.3, 16.4, 16.5**
        """
        # Reset history for this refinement run
        self.history = []
        
        # Auto-detect book type if not provided
        if book_type is None:
            book_type = self.book_type_adapter.get_book_type_str(chain.book_id)
        
        # Calculate total snippet count if not provided
        if total_snippet_count is None:
            total_snippet_count = len(snippets) if snippets else chain.metadata.snippet_count
        
        # Get initial quality score
        initial_quality = self.quality_scorer.score(chain, total_snippet_count)
        initial_score = initial_quality.overall_score()
        
        logger.info(
            f"Starting refinement for {chain.book_id}: "
            f"initial_score={initial_score:.3f}, threshold={self.quality_threshold}"
        )
        
        # Record initial state
        self.history.append(RefinementRecord(
            version=0,
            timestamp=datetime.now(),
            quality_scores=initial_quality,
            changes=["Initial state"],
            rationale="Starting point before refinement",
            overall_score=initial_score,
        ))
        
        current_chain = chain
        current_score = initial_score
        all_improvements: List[str] = []
        
        for iteration in range(1, self.max_iterations + 1):
            # Check if threshold already met
            if current_score >= self.quality_threshold:
                logger.info(
                    f"Quality threshold met at iteration {iteration - 1}: "
                    f"score={current_score:.3f} >= threshold={self.quality_threshold}"
                )
                break
            
            logger.debug(f"Starting refinement iteration {iteration}")
            
            # Apply improvement strategies
            current_chain, changes = self._apply_improvements(
                chain=current_chain,
                snippets=snippets,
                book_type=book_type,
                quality=self.quality_scorer.score(current_chain, total_snippet_count),
            )
            
            # Re-evaluate quality
            new_quality = self.quality_scorer.score(current_chain, total_snippet_count)
            new_score = new_quality.overall_score()
            
            # Record this iteration
            record = RefinementRecord(
                version=iteration,
                timestamp=datetime.now(),
                quality_scores=new_quality,
                changes=changes,
                rationale=f"Auto-refinement iteration {iteration}",
                overall_score=new_score,
            )
            self.history.append(record)
            all_improvements.extend(changes)
            
            logger.info(
                f"Iteration {iteration}: score {current_score:.3f} -> {new_score:.3f}, "
                f"changes: {len(changes)}"
            )
            
            # Check for improvement
            if new_score <= current_score and not changes:
                logger.info(
                    f"No improvement possible at iteration {iteration}, stopping"
                )
                break
            
            current_score = new_score
        
        # Build result
        final_quality = self.quality_scorer.score(current_chain, total_snippet_count)
        final_score = final_quality.overall_score()
        
        result = RefinementResult(
            chain=current_chain,
            history=self.history,
            initial_score=initial_score,
            final_score=final_score,
            iterations_performed=len(self.history) - 1,  # Exclude initial state
            threshold_met=final_score >= self.quality_threshold,
            improvements_made=all_improvements,
        )
        
        logger.info(
            f"Refinement complete for {chain.book_id}: "
            f"score {initial_score:.3f} -> {final_score:.3f}, "
            f"iterations={result.iterations_performed}, "
            f"threshold_met={result.threshold_met}"
        )
        
        return result
    
    def _apply_improvements(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet],
        book_type: str,
        quality: QualityReport,
    ) -> Tuple[LogicChain, List[str]]:
        """
        Apply improvement strategies based on quality issues.
        
        Strategies are applied in order of priority:
        1. Fix orphan nodes (if orphan_ratio > threshold)
        2. Improve connectivity (if connectivity < threshold)
        3. Split heterogeneous nodes (semantic refinement)
        4. Improve summaries
        5. Fix entry/terminal nodes (if argument_completeness < threshold)
        
        Args:
            chain: Current chain state
            snippets: All snippets
            book_type: Book type string
            quality: Current quality report
            
        Returns:
            Tuple of (improved_chain, list_of_changes)
            
        **Validates: Requirements 16.2, 16.3**
        """
        changes: List[str] = []
        current_chain = chain
        
        # Strategy 1: Fix orphan nodes by connecting them
        if quality.orphan_ratio > self.orphan_ratio_threshold:
            current_chain, orphan_changes = self._fix_orphan_nodes(current_chain)
            changes.extend(orphan_changes)
        
        # Strategy 2: Improve connectivity
        if quality.connectivity < self.connectivity_threshold:
            current_chain, conn_changes = self._improve_connectivity(current_chain)
            changes.extend(conn_changes)
        
        # Strategy 3: Semantic cluster refinement
        current_chain, split_changes = self._apply_cluster_refinement(
            current_chain, snippets
        )
        changes.extend(split_changes)
        
        # Strategy 4: Improve summaries
        current_chain, summary_changes = self._apply_summary_improvement(
            current_chain, snippets, book_type
        )
        changes.extend(summary_changes)
        
        # Strategy 5: Fix entry/terminal nodes
        if quality.argument_completeness < self.argument_completeness_threshold:
            current_chain, structure_changes = self._fix_entry_terminal_nodes(current_chain)
            changes.extend(structure_changes)
        
        return current_chain, changes
    
    def _fix_orphan_nodes(
        self,
        chain: LogicChain,
    ) -> Tuple[LogicChain, List[str]]:
        """
        Fix orphan nodes by connecting them to the graph.
        
        Strategy:
        - Find orphan nodes (no incoming or outgoing edges)
        - Connect each orphan to the nearest node by node_id sequence
        - Use "supports" relation for inferred edges
        
        Args:
            chain: Current chain
            
        Returns:
            Tuple of (updated_chain, changes)
            
        **Validates: Requirements 16.2**
        """
        changes: List[str] = []
        
        # Find orphan nodes
        orphan_ids = self.quality_scorer.get_orphan_nodes(chain)
        
        if not orphan_ids:
            return chain, changes
        
        # Build node lookup
        node_lookup = {n.node_id: n for n in chain.nodes}
        all_node_ids = sorted(node_lookup.keys())
        
        # Find non-orphan nodes
        nodes_with_edges: Set[str] = set()
        for edge in chain.edges:
            nodes_with_edges.add(edge.from_node)
            nodes_with_edges.add(edge.to_node)
        
        non_orphan_ids = sorted(nodes_with_edges)
        
        if not non_orphan_ids:
            # All nodes are orphans - connect them sequentially
            non_orphan_ids = all_node_ids[:1] if all_node_ids else []
        
        # Create edges to connect orphans
        new_edges = list(chain.edges)
        
        for orphan_id in orphan_ids:
            # Find the nearest non-orphan node
            target_id = self._find_nearest_node(orphan_id, non_orphan_ids, all_node_ids)
            
            if target_id and target_id != orphan_id:
                # Determine edge direction based on node_id order
                if orphan_id < target_id:
                    from_node, to_node = orphan_id, target_id
                else:
                    from_node, to_node = target_id, orphan_id
                
                # Check if edge already exists
                edge_exists = any(
                    e.from_node == from_node and e.to_node == to_node
                    for e in new_edges
                )
                
                if not edge_exists:
                    new_edge = LogicEdge(
                        from_node=from_node,
                        to_node=to_node,
                        relation=EdgeRelation.SUPPORTS,
                        metadata={"inferred_from": "orphan_fix"}
                    )
                    new_edges.append(new_edge)
                    changes.append(f"Connected orphan {orphan_id} to {target_id}")
                    
                    # Add to non-orphan set for subsequent orphans
                    non_orphan_ids = sorted(set(non_orphan_ids) | {orphan_id})
        
        if changes:
            # Create updated chain
            updated_chain = LogicChain(
                chain_id=chain.chain_id,
                book_id=chain.book_id,
                nodes=chain.nodes,
                edges=new_edges,
                narrative_order=chain.narrative_order,
                entry_nodes=chain.entry_nodes,
                terminal_nodes=chain.terminal_nodes,
                metadata=chain.metadata,
                version=chain.version,
            )
            return updated_chain, changes
        
        return chain, changes
    
    def _find_nearest_node(
        self,
        node_id: str,
        candidates: List[str],
        all_nodes: List[str],
    ) -> Optional[str]:
        """
        Find the nearest candidate node by position in all_nodes list.
        
        Args:
            node_id: The node to find a neighbor for
            candidates: List of candidate node IDs
            all_nodes: Sorted list of all node IDs
            
        Returns:
            Nearest candidate node ID, or None
        """
        if not candidates:
            return None
        
        try:
            node_idx = all_nodes.index(node_id)
        except ValueError:
            return candidates[0] if candidates else None
        
        # Find nearest candidate by index distance
        min_distance = float('inf')
        nearest = None
        
        for candidate in candidates:
            try:
                cand_idx = all_nodes.index(candidate)
                distance = abs(cand_idx - node_idx)
                if distance < min_distance:
                    min_distance = distance
                    nearest = candidate
            except ValueError:
                continue
        
        return nearest or (candidates[0] if candidates else None)
    
    def _improve_connectivity(
        self,
        chain: LogicChain,
    ) -> Tuple[LogicChain, List[str]]:
        """
        Improve connectivity by connecting disconnected components.
        
        Strategy:
        - Find all connected components
        - Connect smaller components to the largest component
        - Use "leads_to" relation for connecting edges
        
        Args:
            chain: Current chain
            
        Returns:
            Tuple of (updated_chain, changes)
            
        **Validates: Requirements 16.2**
        """
        changes: List[str] = []
        
        # Get disconnected components
        components = self.quality_scorer.get_disconnected_components(chain)
        
        if len(components) <= 1:
            return chain, changes
        
        # Sort components by size (largest first)
        components_sorted = sorted(components, key=len, reverse=True)
        largest_component = components_sorted[0]
        
        # Connect smaller components to the largest
        new_edges = list(chain.edges)
        
        for component in components_sorted[1:]:
            # Find a node from each component to connect
            # Use the first node (by sorted order) from each
            from_node = sorted(component)[0]
            to_node = sorted(largest_component)[0]
            
            # Check if edge already exists
            edge_exists = any(
                (e.from_node == from_node and e.to_node == to_node) or
                (e.from_node == to_node and e.to_node == from_node)
                for e in new_edges
            )
            
            if not edge_exists:
                new_edge = LogicEdge(
                    from_node=from_node,
                    to_node=to_node,
                    relation=EdgeRelation.LEADS_TO,
                    metadata={"inferred_from": "connectivity_fix"}
                )
                new_edges.append(new_edge)
                changes.append(
                    f"Connected component ({len(component)} nodes) to main component"
                )
                
                # Merge into largest component for subsequent connections
                largest_component = largest_component | component
        
        if changes:
            updated_chain = LogicChain(
                chain_id=chain.chain_id,
                book_id=chain.book_id,
                nodes=chain.nodes,
                edges=new_edges,
                narrative_order=chain.narrative_order,
                entry_nodes=chain.entry_nodes,
                terminal_nodes=chain.terminal_nodes,
                metadata=chain.metadata,
                version=chain.version,
            )
            return updated_chain, changes
        
        return chain, changes
    
    def _apply_cluster_refinement(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet],
    ) -> Tuple[LogicChain, List[str]]:
        """
        Apply semantic cluster refinement to split heterogeneous nodes.
        
        Args:
            chain: Current chain
            snippets: All snippets
            
        Returns:
            Tuple of (refined_chain, changes)
            
        **Validates: Requirements 16.2**
        """
        return self.cluster_refiner.refine_chain(chain, snippets)
    
    def _apply_summary_improvement(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet],
        book_type: str,
    ) -> Tuple[LogicChain, List[str]]:
        """
        Improve node summaries using intelligent summary generation.
        
        Args:
            chain: Current chain
            snippets: All snippets
            book_type: Book type string
            
        Returns:
            Tuple of (updated_chain, changes)
            
        **Validates: Requirements 16.2**
        """
        changes: List[str] = []
        updated_nodes: List[LogicNode] = []
        
        for node in chain.nodes:
            improved_summary, was_changed = self.summary_generator.improve_existing_summary(
                node=node,
                snippets=snippets,
                book_type=book_type,
            )
            
            if was_changed:
                # Create updated node with new summary
                updated_node = LogicNode(
                    node_id=node.node_id,
                    snippet_ids=node.snippet_ids,
                    role=node.role,
                    condition=node.condition,
                    summary=improved_summary,
                    metadata=node.metadata,
                )
                updated_nodes.append(updated_node)
                changes.append(f"Improved summary for {node.node_id}")
            else:
                updated_nodes.append(node)
        
        if changes:
            updated_chain = LogicChain(
                chain_id=chain.chain_id,
                book_id=chain.book_id,
                nodes=updated_nodes,
                edges=chain.edges,
                narrative_order=chain.narrative_order,
                entry_nodes=chain.entry_nodes,
                terminal_nodes=chain.terminal_nodes,
                metadata=chain.metadata,
                version=chain.version,
            )
            return updated_chain, changes
        
        return chain, changes
    
    def _fix_entry_terminal_nodes(
        self,
        chain: LogicChain,
    ) -> Tuple[LogicChain, List[str]]:
        """
        Fix missing entry and terminal nodes.
        
        Strategy:
        - If no entry nodes: promote nodes with no incoming edges
        - If no terminal nodes: promote nodes with no outgoing edges
        
        Args:
            chain: Current chain
            
        Returns:
            Tuple of (updated_chain, changes)
            
        **Validates: Requirements 16.2**
        """
        changes: List[str] = []
        new_entry_nodes = list(chain.entry_nodes)
        new_terminal_nodes = list(chain.terminal_nodes)
        
        # Build edge maps
        nodes_with_incoming: Set[str] = set()
        nodes_with_outgoing: Set[str] = set()
        
        for edge in chain.edges:
            nodes_with_incoming.add(edge.to_node)
            nodes_with_outgoing.add(edge.from_node)
        
        all_node_ids = {n.node_id for n in chain.nodes}
        
        # Fix missing entry nodes
        if not new_entry_nodes:
            # Find nodes with no incoming edges
            candidates = all_node_ids - nodes_with_incoming
            if candidates:
                new_entry_nodes = sorted(candidates)
                changes.append(f"Added {len(new_entry_nodes)} entry nodes")
        
        # Fix missing terminal nodes
        if not new_terminal_nodes:
            # Find nodes with no outgoing edges
            candidates = all_node_ids - nodes_with_outgoing
            if candidates:
                new_terminal_nodes = sorted(candidates)
                changes.append(f"Added {len(new_terminal_nodes)} terminal nodes")
        
        if changes:
            updated_chain = LogicChain(
                chain_id=chain.chain_id,
                book_id=chain.book_id,
                nodes=chain.nodes,
                edges=chain.edges,
                narrative_order=chain.narrative_order,
                entry_nodes=new_entry_nodes,
                terminal_nodes=new_terminal_nodes,
                metadata=chain.metadata,
                version=chain.version,
            )
            return updated_chain, changes
        
        return chain, changes
    
    def identify_low_quality_chains(
        self,
        chains: List[LogicChain],
        snippets_map: Dict[str, List[NarrativeSnippet]],
    ) -> List[Tuple[LogicChain, QualityReport]]:
        """
        Identify chains with quality score below threshold.
        
        Args:
            chains: List of LogicChains to evaluate
            snippets_map: Mapping of book_id to snippets
            
        Returns:
            List of (chain, quality_report) tuples for low-quality chains
            
        **Validates: Requirements 16.1**
        """
        low_quality: List[Tuple[LogicChain, QualityReport]] = []
        
        for chain in chains:
            snippets = snippets_map.get(chain.book_id, [])
            total_count = len(snippets) if snippets else chain.metadata.snippet_count
            
            quality = self.quality_scorer.score(chain, total_count)
            
            if quality.overall_score() < self.quality_threshold:
                low_quality.append((chain, quality))
                logger.debug(
                    f"Low quality chain: {chain.book_id}, "
                    f"score={quality.overall_score():.3f}"
                )
        
        logger.info(f"Identified {len(low_quality)} low-quality chains out of {len(chains)}")
        return low_quality
    
    def get_history(self) -> List[RefinementRecord]:
        """
        Get the refinement history from the last run.
        
        Returns:
            List of RefinementRecord objects
        """
        return self.history.copy()


def get_refinement_engine(
    max_iterations: int = MAX_ITERATIONS,
    quality_threshold: float = QUALITY_THRESHOLD_OVERALL,
) -> IterativeRefinementEngine:
    """
    Get an IterativeRefinementEngine instance.
    
    Args:
        max_iterations: Maximum refinement iterations
        quality_threshold: Minimum quality score threshold
        
    Returns:
        IterativeRefinementEngine instance
    """
    return IterativeRefinementEngine(
        max_iterations=max_iterations,
        quality_threshold=quality_threshold,
    )
