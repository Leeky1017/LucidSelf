"""
EdgeInferrer - 推断节点间的边

从显式关系和隐式顺序推断LogicEdge。
"""

from typing import Dict, List, Set

from scripts.logic_chain_builder.models import LogicNode, LogicEdge, EdgeRelation
from scripts.logic_chain_builder.constants import RELATION_TYPE_MAPPING
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import ConfigRelation


logger = get_logger(__name__)


class EdgeInferrer:
    """
    推断节点间的边
    
    从显式关系(ConfigRelation)和隐式顺序推断LogicEdge。
    """
    
    def infer_from_relations(
        self,
        relations: List[ConfigRelation],
        node_factor_map: Dict[str, List[str]]
    ) -> List[LogicEdge]:
        """
        从显式关系推断边
        
        Creates edges from explicit ConfigRelation entries by:
        1. Mapping factor_a/factor_b to node_ids via factor-node mapping
        2. Mapping relation_type to EdgeRelation
        3. Copying condition_constraint to edge condition
        
        Args:
            relations: ConfigRelation列表
            node_factor_map: node_id -> factor_ids映射
        
        Returns:
            LogicEdge列表
        """
        edges: List[LogicEdge] = []
        
        # Build reverse mapping: factor_id -> node_ids
        factor_to_nodes: Dict[str, Set[str]] = {}
        for node_id, factor_ids in node_factor_map.items():
            for factor_id in factor_ids:
                if factor_id not in factor_to_nodes:
                    factor_to_nodes[factor_id] = set()
                factor_to_nodes[factor_id].add(node_id)
        
        # Track created edges to avoid duplicates
        created_edges: Set[tuple] = set()
        
        for relation in relations:
            # Find nodes containing factor_a and factor_b
            nodes_with_factor_a = factor_to_nodes.get(relation.factor_a, set())
            nodes_with_factor_b = factor_to_nodes.get(relation.factor_b, set())
            
            if not nodes_with_factor_a or not nodes_with_factor_b:
                logger.debug(
                    f"Skipping relation {relation.relation_id}: "
                    f"factor_a={relation.factor_a} (nodes: {len(nodes_with_factor_a)}), "
                    f"factor_b={relation.factor_b} (nodes: {len(nodes_with_factor_b)})"
                )
                continue
            
            # Map relation type to edge relation
            edge_relation = self.map_relation_type(relation.relation_type)
            
            # Handle condition_constraint - copy to edge condition if non-empty
            condition = None
            if relation.condition_constraint and relation.condition_constraint.strip():
                condition = relation.condition_constraint.strip()
            
            # Create edges between all pairs of nodes
            for from_node in nodes_with_factor_a:
                for to_node in nodes_with_factor_b:
                    # Skip self-loops
                    if from_node == to_node:
                        continue
                    
                    # Skip duplicate edges
                    edge_key = (from_node, to_node, edge_relation.value)
                    if edge_key in created_edges:
                        continue
                    
                    created_edges.add(edge_key)
                    
                    edge = LogicEdge(
                        from_node=from_node,
                        to_node=to_node,
                        relation=edge_relation,
                        condition=condition,
                        metadata={
                            "source_relation_id": relation.relation_id,
                            "source_ref": relation.source_ref,
                            "inferred_from": "explicit_relation",
                        }
                    )
                    edges.append(edge)
                    
                    logger.debug(
                        f"Created edge: {from_node} --[{edge_relation.value}]--> {to_node} "
                        f"(from relation {relation.relation_id})"
                    )
        
        logger.info(f"Inferred {len(edges)} edges from {len(relations)} relations")
        return edges
    
    def infer_sequential_edges(
        self,
        nodes: List[LogicNode],
        existing_edges: List[LogicEdge] = None
    ) -> List[LogicEdge]:
        """
        从source_ref顺序推断隐式边
        
        Infers leads_to edges for sequential nodes in the same chapter.
        Only creates edges when no explicit relation exists between the nodes.
        
        Args:
            nodes: LogicNode列表
            existing_edges: 已存在的边列表（用于避免重复）
        
        Returns:
            LogicEdge列表
        """
        edges: List[LogicEdge] = []
        existing_edges = existing_edges or []
        
        # Build set of existing edge pairs for quick lookup
        existing_pairs: Set[tuple] = set()
        for edge in existing_edges:
            existing_pairs.add((edge.from_node, edge.to_node))
        
        # Group nodes by chapter (extracted from source_ref in metadata)
        chapter_nodes: Dict[str, List[LogicNode]] = {}
        
        for node in nodes:
            # Extract chapter from metadata or node_id
            chapter = self._extract_chapter_from_node(node)
            if chapter not in chapter_nodes:
                chapter_nodes[chapter] = []
            chapter_nodes[chapter].append(node)
        
        # For each chapter, create sequential edges
        for chapter, chapter_node_list in chapter_nodes.items():
            # Sort nodes by their sequence number (extracted from node_id)
            sorted_nodes = sorted(
                chapter_node_list,
                key=lambda n: self._extract_seq_from_node_id(n.node_id)
            )
            
            # Create leads_to edges between consecutive nodes
            for i in range(len(sorted_nodes) - 1):
                from_node = sorted_nodes[i]
                to_node = sorted_nodes[i + 1]
                
                # Skip if edge already exists
                if (from_node.node_id, to_node.node_id) in existing_pairs:
                    logger.debug(
                        f"Skipping sequential edge {from_node.node_id} -> {to_node.node_id}: "
                        "explicit edge exists"
                    )
                    continue
                
                edge = LogicEdge(
                    from_node=from_node.node_id,
                    to_node=to_node.node_id,
                    relation=EdgeRelation.LEADS_TO,
                    condition=None,
                    metadata={
                        "inferred_from": "sequential_order",
                        "chapter": chapter,
                    }
                )
                edges.append(edge)
                existing_pairs.add((from_node.node_id, to_node.node_id))
                
                logger.debug(
                    f"Created sequential edge: {from_node.node_id} --[leads_to]--> {to_node.node_id}"
                )
        
        logger.info(f"Inferred {len(edges)} sequential edges from {len(nodes)} nodes")
        return edges
    
    def _extract_chapter_from_node(self, node: LogicNode) -> str:
        """
        Extract chapter identifier from node metadata or node_id.
        
        Args:
            node: LogicNode
            
        Returns:
            Chapter identifier string
        """
        # Try to get from metadata first
        if node.metadata and "source_ref" in node.metadata:
            source_ref = node.metadata["source_ref"]
            if source_ref and '#' in source_ref:
                parts = source_ref.split('#', 1)
                if len(parts) > 1 and parts[1].strip():
                    return parts[1].strip()
        
        # Fallback: extract from node_id (format: n_{book}_{chapter}_{seq})
        parts = node.node_id.split('_')
        if len(parts) >= 3:
            # Chapter is the second-to-last part (before seq)
            return '_'.join(parts[2:-1])
        
        return "unknown"
    
    def _extract_seq_from_node_id(self, node_id: str) -> int:
        """
        Extract sequence number from node_id.
        
        Node ID format: n_{book}_{chapter}_{seq}
        
        Args:
            node_id: Node identifier string
            
        Returns:
            Sequence number (0 if not found)
        """
        parts = node_id.split('_')
        if parts:
            try:
                return int(parts[-1])
            except ValueError:
                pass
        return 0
    
    def map_relation_type(self, relation_type: str) -> EdgeRelation:
        """
        映射关系类型
        
        Maps ConfigRelation relation_type to EdgeRelation:
        - hierarchy/dependency → depends_on
        - cooperation/supports → supports
        - conditional/gateway → leads_to
        - conflict → conflicts_with
        
        Args:
            relation_type: ConfigRelation的relation_type
        
        Returns:
            EdgeRelation枚举值
        """
        # Normalize the relation type (lowercase, strip whitespace)
        normalized_type = relation_type.lower().strip() if relation_type else ""
        
        # Look up in the mapping
        mapped_type = RELATION_TYPE_MAPPING.get(normalized_type)
        
        if mapped_type:
            return EdgeRelation(mapped_type)
        
        # Default to leads_to for unknown types
        logger.warning(f"Unknown relation type '{relation_type}', defaulting to leads_to")
        return EdgeRelation.LEADS_TO
