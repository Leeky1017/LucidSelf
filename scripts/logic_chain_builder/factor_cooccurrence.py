"""
FactorCooccurrenceInferrer - 基于因子共现推断隐式边

从snippets的factor_trigger字段提取因子，推断节点间的supports关系。
"""

import re
from itertools import combinations
from typing import Dict, List, Optional, Set, Tuple

from scripts.logic_chain_builder.models import LogicNode, LogicEdge, EdgeRelation
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import NarrativeSnippet


logger = get_logger(__name__)


class FactorCooccurrenceInferrer:
    """
    基于因子共现推断隐式边
    
    从snippets的factor_trigger字段提取factor_ids，
    当两个节点涉及相同因子时，推断supports关系。
    """
    
    # Pattern to extract factor_ids from factor_trigger field
    # Matches patterns like: factor_id, factor_id:value, factor_id=value
    FACTOR_ID_PATTERN = re.compile(r'([a-z][a-z0-9_]*)', re.IGNORECASE)
    
    def extract_factors_from_snippet(
        self,
        snippet: NarrativeSnippet
    ) -> Set[str]:
        """
        从单个snippet的factor_trigger字段提取factor_ids
        
        Args:
            snippet: NarrativeSnippet对象
            
        Returns:
            提取的factor_id集合
        """
        factor_ids: Set[str] = set()
        
        factor_trigger = snippet.factor_trigger
        if not factor_trigger or not factor_trigger.strip():
            return factor_ids
        
        # Extract all potential factor_ids using regex
        matches = self.FACTOR_ID_PATTERN.findall(factor_trigger)
        
        for match in matches:
            # Normalize to lowercase
            factor_id = match.lower().strip()
            if factor_id:
                factor_ids.add(factor_id)
        
        return factor_ids
    
    def extract_factors_from_snippets(
        self,
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, Set[str]]:
        """
        从snippets列表提取factor_ids，按snippet_id分组
        
        Args:
            snippets: NarrativeSnippet列表
            
        Returns:
            snippet_id -> factor_ids集合的映射
        """
        snippet_factors: Dict[str, Set[str]] = {}
        
        for snippet in snippets:
            factors = self.extract_factors_from_snippet(snippet)
            if factors:
                snippet_factors[snippet.snippet_id] = factors
        
        logger.debug(
            f"Extracted factors from {len(snippet_factors)} snippets "
            f"(out of {len(snippets)} total)"
        )
        
        return snippet_factors
    
    def build_node_factor_map(
        self,
        nodes: List[LogicNode],
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, Set[str]]:
        """
        构建 node_id -> factor_ids 映射
        
        通过节点的snippet_ids关联到snippets，
        再从snippets的factor_trigger提取factor_ids。
        
        Args:
            nodes: LogicNode列表
            snippets: NarrativeSnippet列表
            
        Returns:
            node_id -> factor_ids集合的映射
        """
        # First, extract factors from all snippets
        snippet_factors = self.extract_factors_from_snippets(snippets)
        
        # Build node -> factors mapping
        node_factor_map: Dict[str, Set[str]] = {}
        
        for node in nodes:
            node_factors: Set[str] = set()
            
            for snippet_id in node.snippet_ids:
                if snippet_id in snippet_factors:
                    node_factors.update(snippet_factors[snippet_id])
            
            if node_factors:
                node_factor_map[node.node_id] = node_factors
        
        logger.info(
            f"Built node-factor map: {len(node_factor_map)} nodes have factors "
            f"(out of {len(nodes)} total)"
        )
        
        return node_factor_map


    def _get_source_ref_order(self, node: LogicNode) -> Tuple[str, int]:
        """
        获取节点的source_ref排序键
        
        用于按source_ref proximity排序节点对。
        
        Args:
            node: LogicNode对象
            
        Returns:
            (source_ref, seq) 元组用于排序
        """
        source_ref = ""
        if node.metadata and "source_ref" in node.metadata:
            source_ref = node.metadata["source_ref"] or ""
        
        # Extract sequence number from node_id
        seq = 0
        parts = node.node_id.split('_')
        if parts:
            try:
                seq = int(parts[-1])
            except ValueError:
                pass
        
        return (source_ref, seq)
    
    def _edge_exists(
        self,
        from_node_id: str,
        to_node_id: str,
        existing_edges: List[LogicEdge]
    ) -> bool:
        """
        检查两个节点间是否已存在边
        
        Args:
            from_node_id: 起始节点ID
            to_node_id: 目标节点ID
            existing_edges: 已存在的边列表
            
        Returns:
            True如果边已存在（任意方向）
        """
        for edge in existing_edges:
            # Check both directions
            if (edge.from_node == from_node_id and edge.to_node == to_node_id) or \
               (edge.from_node == to_node_id and edge.to_node == from_node_id):
                return True
        return False
    
    def infer_from_factor_cooccurrence(
        self,
        nodes: List[LogicNode],
        node_factor_map: Dict[str, Set[str]],
        existing_edges: Optional[List[LogicEdge]] = None
    ) -> List[LogicEdge]:
        """
        基于因子共现推断supports边
        
        当两个节点涉及相同因子时，创建supports边。
        
        规则：
        1. 两节点必须共享至少一个factor_id
        2. 跳过已存在显式关系边的节点对
        3. 按source_ref proximity决定边的方向（较早的节点为from_node）
        4. 边的metadata标记为 inferred_from: factor_cooccurrence
        
        Args:
            nodes: LogicNode列表
            node_factor_map: node_id -> factor_ids映射
            existing_edges: 已存在的边列表（用于避免重复）
            
        Returns:
            推断的LogicEdge列表
        """
        existing_edges = existing_edges or []
        edges: List[LogicEdge] = []
        
        # Build node lookup for source_ref ordering
        node_lookup: Dict[str, LogicNode] = {n.node_id: n for n in nodes}
        
        # Track created edges to avoid duplicates
        created_pairs: Set[Tuple[str, str]] = set()
        
        # Get all node_ids that have factors
        nodes_with_factors = [
            n for n in nodes 
            if n.node_id in node_factor_map and node_factor_map[n.node_id]
        ]
        
        # Check all pairs of nodes
        for node_a, node_b in combinations(nodes_with_factors, 2):
            factors_a = node_factor_map.get(node_a.node_id, set())
            factors_b = node_factor_map.get(node_b.node_id, set())
            
            # Find shared factors
            shared_factors = factors_a & factors_b
            
            if not shared_factors:
                continue
            
            # Skip if explicit edge already exists
            if self._edge_exists(node_a.node_id, node_b.node_id, existing_edges):
                logger.debug(
                    f"Skipping factor cooccurrence edge {node_a.node_id} <-> {node_b.node_id}: "
                    "explicit edge exists"
                )
                continue
            
            # Determine direction based on source_ref proximity
            order_a = self._get_source_ref_order(node_a)
            order_b = self._get_source_ref_order(node_b)
            
            if order_a <= order_b:
                from_node, to_node = node_a, node_b
            else:
                from_node, to_node = node_b, node_a
            
            # Skip if we already created this edge
            edge_pair = (from_node.node_id, to_node.node_id)
            if edge_pair in created_pairs:
                continue
            
            created_pairs.add(edge_pair)
            
            # Create the edge
            edge = LogicEdge(
                from_node=from_node.node_id,
                to_node=to_node.node_id,
                relation=EdgeRelation.SUPPORTS,
                condition=None,
                metadata={
                    "inferred_from": "factor_cooccurrence",
                    "shared_factors": sorted(list(shared_factors)),
                }
            )
            edges.append(edge)
            
            logger.debug(
                f"Created factor cooccurrence edge: {from_node.node_id} --[supports]--> "
                f"{to_node.node_id} (shared factors: {shared_factors})"
            )
        
        logger.info(
            f"Inferred {len(edges)} edges from factor cooccurrence "
            f"(checked {len(nodes_with_factors)} nodes with factors)"
        )
        
        return edges
