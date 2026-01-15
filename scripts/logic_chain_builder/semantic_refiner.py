"""
SemanticClusterRefiner - 语义聚类细化

自动识别和拆分异构节点，确保节点内容语义一致。
"""

from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

from scripts.logic_chain_builder.models import (
    LogicNode,
    LogicEdge,
    LogicChain,
    SnippetRole,
)
from scripts.logic_chain_builder.clusterer import SnippetClusterer
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import NarrativeSnippet


logger = get_logger(__name__)


# Thresholds for heterogeneous node detection
MAX_SNIPPETS_PER_NODE = 5
MAX_UNIQUE_TRIGGERS = 3


class SemanticClusterRefiner:
    """
    语义聚类细化 - 自动识别和拆分异构节点
    
    Identifies nodes with heterogeneous content (low semantic similarity)
    and splits them into multiple nodes based on trigger field similarity.
    """
    
    def __init__(self):
        self.clusterer = SnippetClusterer()
    
    def identify_heterogeneous_nodes(
        self,
        nodes: List[LogicNode],
        snippets: List[NarrativeSnippet]
    ) -> List[LogicNode]:
        """
        识别需要拆分的异构节点
        
        Conditions for heterogeneous nodes:
        - Node contains > MAX_SNIPPETS_PER_NODE snippets (default: 5)
        - Node has > MAX_UNIQUE_TRIGGERS unique triggers (default: 3)
        - Node has mixed roles (multiple different roles)
        
        Args:
            nodes: LogicNode列表
            snippets: NarrativeSnippet列表
            
        Returns:
            需要拆分的节点列表
        """
        # Build snippet lookup by ID
        snippet_map = {s.snippet_id: s for s in snippets}
        
        heterogeneous = []
        for node in nodes:
            node_snippets = [
                snippet_map[sid] 
                for sid in node.snippet_ids 
                if sid in snippet_map
            ]
            
            if self._is_heterogeneous(node_snippets):
                heterogeneous.append(node)
                logger.debug(
                    f"Identified heterogeneous node: {node.node_id} "
                    f"(snippets: {len(node_snippets)})"
                )
        
        logger.info(
            f"Identified {len(heterogeneous)} heterogeneous nodes "
            f"out of {len(nodes)} total nodes"
        )
        return heterogeneous
    
    def _is_heterogeneous(self, snippets: List[NarrativeSnippet]) -> bool:
        """
        Check if a set of snippets is heterogeneous.
        
        A node is considered heterogeneous if:
        1. It has more than MAX_SNIPPETS_PER_NODE snippets, OR
        2. It has more than MAX_UNIQUE_TRIGGERS unique triggers, OR
        3. It has mixed roles (more than 2 different roles)
        
        Args:
            snippets: List of snippets in the node
            
        Returns:
            True if the node is heterogeneous
        """
        if not snippets:
            return False
        
        # Check snippet count
        if len(snippets) > MAX_SNIPPETS_PER_NODE:
            return True
        
        # Check unique triggers
        triggers = self._extract_unique_triggers(snippets)
        if len(triggers) > MAX_UNIQUE_TRIGGERS:
            return True
        
        # Check mixed roles
        roles = set(s.role for s in snippets)
        if len(roles) > 2:
            return True
        
        return False
    
    def _extract_unique_triggers(
        self, 
        snippets: List[NarrativeSnippet]
    ) -> Set[str]:
        """
        Extract unique trigger values from snippets.
        
        Normalizes triggers by stripping whitespace and converting to lowercase.
        
        Args:
            snippets: List of snippets
            
        Returns:
            Set of unique normalized triggers
        """
        triggers = set()
        for s in snippets:
            if s.trigger and s.trigger.strip():
                # Normalize: strip and lowercase for comparison
                normalized = s.trigger.strip().lower()
                triggers.add(normalized)
        return triggers
    
    def split_node(
        self,
        node: LogicNode,
        snippets: List[NarrativeSnippet]
    ) -> List[LogicNode]:
        """
        自动拆分节点
        
        Splits a node based on trigger field similarity. Snippets with the same
        or similar triggers are grouped together into new nodes.
        
        Args:
            node: The node to split
            snippets: All snippets (used to look up node's snippets)
            
        Returns:
            List of new nodes (original node is replaced)
        """
        # Build snippet lookup
        snippet_map = {s.snippet_id: s for s in snippets}
        
        # Get snippets belonging to this node
        node_snippets = [
            snippet_map[sid] 
            for sid in node.snippet_ids 
            if sid in snippet_map
        ]
        
        if not node_snippets:
            logger.warning(f"Node {node.node_id} has no valid snippets, skipping split")
            return [node]
        
        # Group snippets by trigger
        trigger_groups = self._group_by_trigger(node_snippets)
        
        # If only one group, no split needed
        if len(trigger_groups) <= 1:
            logger.debug(f"Node {node.node_id} has only one trigger group, no split needed")
            return [node]
        
        # Create new nodes for each group
        new_nodes = []
        for i, (trigger_key, group_snippets) in enumerate(trigger_groups.items()):
            new_node = self._create_split_node(
                original_node=node,
                split_index=i,
                trigger_key=trigger_key,
                group_snippets=group_snippets
            )
            new_nodes.append(new_node)
        
        logger.info(
            f"Split node {node.node_id} into {len(new_nodes)} nodes "
            f"(triggers: {list(trigger_groups.keys())})"
        )
        
        return new_nodes
    
    def _group_by_trigger(
        self, 
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, List[NarrativeSnippet]]:
        """
        Group snippets by their trigger field.
        
        Snippets with empty triggers are grouped under "__no_trigger__".
        
        Args:
            snippets: List of snippets to group
            
        Returns:
            Dictionary mapping trigger keys to snippet lists
        """
        groups: Dict[str, List[NarrativeSnippet]] = defaultdict(list)
        
        for snippet in snippets:
            trigger_key = self._normalize_trigger_key(snippet.trigger)
            groups[trigger_key].append(snippet)
        
        return dict(groups)
    
    def _normalize_trigger_key(self, trigger: Optional[str]) -> str:
        """
        Normalize trigger string for grouping.
        
        Args:
            trigger: Raw trigger string
            
        Returns:
            Normalized trigger key
        """
        if not trigger or not trigger.strip():
            return "__no_trigger__"
        
        # Strip whitespace and use as-is (preserve case for Chinese)
        return trigger.strip()
    
    def _create_split_node(
        self,
        original_node: LogicNode,
        split_index: int,
        trigger_key: str,
        group_snippets: List[NarrativeSnippet]
    ) -> LogicNode:
        """
        Create a new node from a split operation.
        
        Args:
            original_node: The original node being split
            split_index: Index of this split (0, 1, 2, ...)
            trigger_key: The trigger key for this group
            group_snippets: Snippets belonging to this group
            
        Returns:
            New LogicNode
        """
        # Generate new node_id
        new_node_id = f"{original_node.node_id}_split{split_index}"
        
        # Collect snippet_ids
        snippet_ids = [s.snippet_id for s in group_snippets]
        
        # Determine role for the new node
        role = self.clusterer.determine_node_role(group_snippets)
        
        # Generate summary
        summary = self.clusterer.generate_summary(group_snippets)
        
        # Build metadata
        metadata = {
            "split_from": original_node.node_id,
            "split_reason": f"trigger: {trigger_key}",
            "original_snippet_count": len(original_node.snippet_ids),
            "split_snippet_count": len(snippet_ids),
        }
        
        # Preserve original metadata if present
        if original_node.metadata:
            if "source_ref" in original_node.metadata:
                metadata["source_ref"] = original_node.metadata["source_ref"]
        
        return LogicNode(
            node_id=new_node_id,
            snippet_ids=snippet_ids,
            role=role,
            condition=original_node.condition,
            summary=summary,
            metadata=metadata,
        )
    
    def update_edges_after_split(
        self,
        edges: List[LogicEdge],
        original_node_id: str,
        new_nodes: List[LogicNode]
    ) -> List[LogicEdge]:
        """
        Update edges after a node split.
        
        When a node is split:
        - Edges pointing TO the original node are updated to point to ALL new nodes
        - Edges pointing FROM the original node are updated to point from the FIRST new node
        
        Args:
            edges: Original edge list
            original_node_id: ID of the node that was split
            new_nodes: List of new nodes created from the split
            
        Returns:
            Updated edge list
        """
        if not new_nodes:
            return edges
        
        updated_edges: List[LogicEdge] = []
        first_new_node_id = new_nodes[0].node_id
        all_new_node_ids = [n.node_id for n in new_nodes]
        
        for edge in edges:
            if edge.from_node == original_node_id:
                # Edge FROM original node -> update to FROM first new node
                updated_edge = LogicEdge(
                    from_node=first_new_node_id,
                    to_node=edge.to_node,
                    relation=edge.relation,
                    condition=edge.condition,
                    metadata={
                        **edge.metadata,
                        "updated_from_split": original_node_id,
                    }
                )
                updated_edges.append(updated_edge)
                
            elif edge.to_node == original_node_id:
                # Edge TO original node -> create edges to ALL new nodes
                for new_node_id in all_new_node_ids:
                    updated_edge = LogicEdge(
                        from_node=edge.from_node,
                        to_node=new_node_id,
                        relation=edge.relation,
                        condition=edge.condition,
                        metadata={
                            **edge.metadata,
                            "updated_from_split": original_node_id,
                        }
                    )
                    updated_edges.append(updated_edge)
            else:
                # Edge not affected by split
                updated_edges.append(edge)
        
        return updated_edges
    
    def refine_chain(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet]
    ) -> Tuple[LogicChain, List[str]]:
        """
        Refine a logic chain by splitting heterogeneous nodes.
        
        This is the main entry point for semantic refinement.
        
        Args:
            chain: The logic chain to refine
            snippets: All snippets for the book
            
        Returns:
            Tuple of (refined chain, list of changes made)
        """
        changes: List[str] = []
        
        # Identify heterogeneous nodes
        heterogeneous_nodes = self.identify_heterogeneous_nodes(
            chain.nodes, snippets
        )
        
        if not heterogeneous_nodes:
            logger.info("No heterogeneous nodes found, chain unchanged")
            return chain, changes
        
        # Track node replacements
        node_map: Dict[str, List[LogicNode]] = {}  # old_id -> new_nodes
        
        # Split each heterogeneous node
        for node in heterogeneous_nodes:
            new_nodes = self.split_node(node, snippets)
            if len(new_nodes) > 1:
                node_map[node.node_id] = new_nodes
                changes.append(
                    f"Split node {node.node_id} into {len(new_nodes)} nodes: "
                    f"{[n.node_id for n in new_nodes]}"
                )
        
        if not node_map:
            logger.info("No nodes were actually split")
            return chain, changes
        
        # Build new node list
        new_nodes_list: List[LogicNode] = []
        split_node_ids = set(node_map.keys())
        
        for node in chain.nodes:
            if node.node_id in split_node_ids:
                # Replace with split nodes
                new_nodes_list.extend(node_map[node.node_id])
            else:
                # Keep original node
                new_nodes_list.append(node)
        
        # Update edges
        new_edges = list(chain.edges)
        for original_id, new_nodes in node_map.items():
            new_edges = self.update_edges_after_split(
                new_edges, original_id, new_nodes
            )
        
        # Update entry_nodes and terminal_nodes
        new_entry_nodes = self._update_special_nodes(
            chain.entry_nodes, node_map
        )
        new_terminal_nodes = self._update_special_nodes(
            chain.terminal_nodes, node_map
        )
        
        # Update narrative_order
        new_narrative_order = self._update_narrative_order(
            chain.narrative_order, node_map
        )
        
        # Create refined chain
        refined_chain = LogicChain(
            chain_id=chain.chain_id,
            book_id=chain.book_id,
            nodes=new_nodes_list,
            edges=new_edges,
            narrative_order=new_narrative_order,
            entry_nodes=new_entry_nodes,
            terminal_nodes=new_terminal_nodes,
            metadata=chain.metadata,
            version=chain.version,
        )
        
        logger.info(
            f"Refined chain: {len(chain.nodes)} -> {len(new_nodes_list)} nodes, "
            f"{len(chain.edges)} -> {len(new_edges)} edges"
        )
        
        return refined_chain, changes
    
    def _update_special_nodes(
        self,
        node_ids: List[str],
        node_map: Dict[str, List[LogicNode]]
    ) -> List[str]:
        """
        Update entry_nodes or terminal_nodes after splits.
        
        If a special node was split, include all its split nodes.
        
        Args:
            node_ids: Original list of special node IDs
            node_map: Mapping of split node IDs to new nodes
            
        Returns:
            Updated list of special node IDs
        """
        updated_ids: List[str] = []
        
        for node_id in node_ids:
            if node_id in node_map:
                # Add all split nodes
                updated_ids.extend(n.node_id for n in node_map[node_id])
            else:
                updated_ids.append(node_id)
        
        return updated_ids
    
    def _update_narrative_order(
        self,
        narrative_order: List[str],
        node_map: Dict[str, List[LogicNode]]
    ) -> List[str]:
        """
        Update narrative_order after splits.
        
        Split nodes are inserted in place of the original node.
        
        Args:
            narrative_order: Original narrative order
            node_map: Mapping of split node IDs to new nodes
            
        Returns:
            Updated narrative order
        """
        updated_order: List[str] = []
        
        for node_id in narrative_order:
            if node_id in node_map:
                # Insert all split nodes in order
                updated_order.extend(n.node_id for n in node_map[node_id])
            else:
                updated_order.append(node_id)
        
        return updated_order
