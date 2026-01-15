"""
LogicChainBuilder - 构建完整的逻辑链

协调Loader、Clusterer、EdgeInferrer组装LogicChain。

**Validates: Requirements 2.1, 2.2, 4.1-4.6, 5.1-5.5**
"""

from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

from scripts.logic_chain_builder.models import (
    LogicChain, LogicNode, LogicEdge, SourceMetadata, SnippetRole, EdgeRelation
)
from scripts.logic_chain_builder.loader import SchemaLoader
from scripts.logic_chain_builder.clusterer import SnippetClusterer
from scripts.logic_chain_builder.edge_inferrer import EdgeInferrer
from scripts.logic_chain_builder.factor_cooccurrence import FactorCooccurrenceInferrer
from scripts.logic_chain_builder.book_type_adapter import BookTypeAdapter
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import NarrativeSnippet


logger = get_logger(__name__)


class LogicChainBuilder:
    """
    构建完整的逻辑链
    
    协调各组件完成逻辑链的构建。
    
    **Validates: Requirements 2.1, 2.2, 4.1-4.6, 5.1-5.5**
    """
    
    def __init__(self, book_id: str):
        """
        初始化构建器
        
        Args:
            book_id: 书籍ID
        """
        self.book_id = book_id
        self.loader = SchemaLoader()
        self.clusterer = SnippetClusterer()
        self.edge_inferrer = EdgeInferrer()
        self.factor_cooccurrence_inferrer = FactorCooccurrenceInferrer()
        self.book_type_adapter = BookTypeAdapter()
    
    def build(self) -> LogicChain:
        """
        构建逻辑链的主流程
        
        1. 加载数据
        2. 聚类为节点
        3. 推断边
        4. 确定入口和终端节点
        5. 拓扑排序
        
        Returns:
            LogicChain实例
            
        **Validates: Requirements 2.1, 2.2, 4.1-4.6**
        """
        logger.info(f"Building logic chain for book: {self.book_id}")
        
        # 1. 加载数据
        snippets = self.loader.load_snippets(self.book_id)
        relations = self.loader.load_relations(self.book_id)
        
        logger.info(f"Loaded {len(snippets)} snippets and {len(relations)} relations")
        
        # 2. 聚类为节点
        book_abbr = self._abbreviate(self.book_id)
        groups = self.clusterer.cluster_by_source_ref(snippets)
        
        nodes: List[LogicNode] = []
        for seq, (source_ref, group_snippets) in enumerate(groups.items()):
            # Extract chapter from source_ref
            chapter = self.clusterer._extract_chapter_from_source_ref(source_ref)
            node = self.clusterer.create_node(
                book_abbr=book_abbr,
                chapter=chapter,
                seq=seq,
                snippets=group_snippets
            )
            nodes.append(node)
        
        logger.info(f"Created {len(nodes)} nodes from {len(groups)} groups")
        
        # 3. 推断边
        # 3a. Build node-factor mapping for relation-based edge inference
        node_factor_map = self.factor_cooccurrence_inferrer.build_node_factor_map(
            nodes, snippets
        )
        
        # 3b. Infer edges from explicit relations
        edges = self.edge_inferrer.infer_from_relations(relations, node_factor_map)
        
        # 3c. Infer edges from factor cooccurrence
        cooccurrence_edges = self.factor_cooccurrence_inferrer.infer_from_factor_cooccurrence(
            nodes, node_factor_map, edges
        )
        edges.extend(cooccurrence_edges)
        
        # 3d. Infer sequential edges (only where no explicit edge exists)
        sequential_edges = self.edge_inferrer.infer_sequential_edges(nodes, edges)
        edges.extend(sequential_edges)
        
        logger.info(f"Inferred {len(edges)} total edges")
        
        # 4. 确定入口和终端节点
        entry_nodes = self._find_entry_nodes(nodes, edges)
        terminal_nodes = self._find_terminal_nodes(nodes, edges)
        
        logger.info(
            f"Found {len(entry_nodes)} entry nodes and {len(terminal_nodes)} terminal nodes"
        )
        
        # 5. 拓扑排序
        narrative_order = self._topological_sort(nodes, edges, entry_nodes)
        
        logger.info(f"Generated narrative order with {len(narrative_order)} nodes")
        
        # 6. 组装LogicChain
        chain = LogicChain(
            chain_id=f"chain_{book_abbr}",
            book_id=self.book_id,
            nodes=nodes,
            edges=edges,
            narrative_order=narrative_order,
            entry_nodes=entry_nodes,
            terminal_nodes=terminal_nodes,
            metadata=SourceMetadata(
                version="1.0.0",
                extracted_at=datetime.now(),
                source_files=[
                    f"data/schema_staging/snippets/{self.book_id}_snippets.yaml",
                    f"data/schema_staging/relations/{self.book_id}_relations.yaml",
                ],
                snippet_count=len(snippets),
                relation_count=len(relations),
            ),
            version="1.0.0",
        )
        
        logger.info(f"Successfully built logic chain: {chain.chain_id}")
        return chain
    
    def _find_entry_nodes(
        self, 
        nodes: List[LogicNode],
        edges: List[LogicEdge]
    ) -> List[str]:
        """
        查找入口节点
        
        入口节点优先级：
        1. role=主干 的节点
        2. 无入边的节点（fallback）
        
        Args:
            nodes: LogicNode列表
            edges: LogicEdge列表
        
        Returns:
            入口节点ID列表
            
        **Validates: Requirements 2.5, 3.4**
        """
        # First, find nodes with role=主干
        role_based_entries = [
            node.node_id for node in nodes 
            if node.role == SnippetRole.MAIN
        ]
        
        if role_based_entries:
            logger.debug(f"Found {len(role_based_entries)} entry nodes by role=主干")
            return role_based_entries
        
        # Fallback: find nodes with no incoming edges
        nodes_with_incoming: Set[str] = set()
        for edge in edges:
            nodes_with_incoming.add(edge.to_node)
        
        all_node_ids = {node.node_id for node in nodes}
        no_incoming_entries = [
            node_id for node_id in all_node_ids 
            if node_id not in nodes_with_incoming
        ]
        
        # Sort by node_id for deterministic ordering
        no_incoming_entries.sort()
        
        logger.debug(
            f"Found {len(no_incoming_entries)} entry nodes by no-incoming-edges fallback"
        )
        return no_incoming_entries
    
    def _find_terminal_nodes(
        self, 
        nodes: List[LogicNode],
        edges: List[LogicEdge]
    ) -> List[str]:
        """
        查找终端节点
        
        终端节点优先级：
        1. role=总结 的节点
        2. 无出边的节点（fallback）
        
        Args:
            nodes: LogicNode列表
            edges: LogicEdge列表
        
        Returns:
            终端节点ID列表
            
        **Validates: Requirements 2.5, 3.4**
        """
        # First, find nodes with role=总结
        role_based_terminals = [
            node.node_id for node in nodes 
            if node.role == SnippetRole.SUMMARY
        ]
        
        if role_based_terminals:
            logger.debug(f"Found {len(role_based_terminals)} terminal nodes by role=总结")
            return role_based_terminals
        
        # Fallback: find nodes with no outgoing edges
        nodes_with_outgoing: Set[str] = set()
        for edge in edges:
            nodes_with_outgoing.add(edge.from_node)
        
        all_node_ids = {node.node_id for node in nodes}
        no_outgoing_terminals = [
            node_id for node_id in all_node_ids 
            if node_id not in nodes_with_outgoing
        ]
        
        # Sort by node_id for deterministic ordering
        no_outgoing_terminals.sort()
        
        logger.debug(
            f"Found {len(no_outgoing_terminals)} terminal nodes by no-outgoing-edges fallback"
        )
        return no_outgoing_terminals
    
    def _topological_sort(
        self,
        nodes: List[LogicNode],
        edges: List[LogicEdge],
        entry_nodes: List[str]
    ) -> List[str]:
        """
        拓扑排序生成narrative_order
        
        使用Kahn's algorithm进行拓扑排序：
        1. 从entry_nodes开始
        2. 处理循环：在最低置信度边处打断
        3. 多个有效排序时，优先按source_ref顺序
        
        Args:
            nodes: LogicNode列表
            edges: LogicEdge列表
            entry_nodes: 入口节点ID列表
        
        Returns:
            排序后的node_id列表
            
        **Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5**
        """
        if not nodes:
            return []
        
        # Build adjacency list and in-degree map
        all_node_ids = {node.node_id for node in nodes}
        adjacency: Dict[str, List[str]] = defaultdict(list)
        in_degree: Dict[str, int] = {node_id: 0 for node_id in all_node_ids}
        
        # Build node lookup for source_ref ordering
        node_lookup: Dict[str, LogicNode] = {node.node_id: node for node in nodes}
        
        # Track edges for cycle detection
        edge_set: Set[Tuple[str, str]] = set()
        
        for edge in edges:
            # Only consider edges between existing nodes
            if edge.from_node in all_node_ids and edge.to_node in all_node_ids:
                adjacency[edge.from_node].append(edge.to_node)
                in_degree[edge.to_node] += 1
                edge_set.add((edge.from_node, edge.to_node))
        
        # Detect and break cycles if necessary
        edges_to_remove = self._detect_and_break_cycles(
            all_node_ids, adjacency, in_degree, edges
        )
        
        # Remove cycle-breaking edges from adjacency and update in-degree
        for from_node, to_node in edges_to_remove:
            if to_node in adjacency[from_node]:
                adjacency[from_node].remove(to_node)
                in_degree[to_node] -= 1
        
        # Kahn's algorithm with source_ref ordering preference
        result: List[str] = []
        
        # Initialize queue with entry nodes (or nodes with in_degree 0)
        queue: List[str] = []
        
        # Prioritize entry_nodes
        entry_set = set(entry_nodes)
        for node_id in all_node_ids:
            if in_degree[node_id] == 0:
                queue.append(node_id)
        
        # Sort queue: entry_nodes first, then by source_ref order
        def sort_key(node_id: str) -> Tuple[int, str, int]:
            is_entry = 0 if node_id in entry_set else 1
            node = node_lookup.get(node_id)
            source_ref = ""
            seq = 0
            if node and node.metadata:
                source_ref = node.metadata.get("source_ref", "") or ""
            # Extract seq from node_id
            parts = node_id.split('_')
            if parts:
                try:
                    seq = int(parts[-1])
                except ValueError:
                    pass
            return (is_entry, source_ref, seq)
        
        queue.sort(key=sort_key)
        
        while queue:
            # Pop the first node (highest priority)
            current = queue.pop(0)
            result.append(current)
            
            # Process neighbors
            neighbors = adjacency[current]
            # Sort neighbors by source_ref order
            neighbors_sorted = sorted(neighbors, key=sort_key)
            
            for neighbor in neighbors_sorted:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            
            # Re-sort queue after adding new nodes
            queue.sort(key=sort_key)
        
        # Handle any remaining nodes (disconnected components)
        remaining = [node_id for node_id in all_node_ids if node_id not in result]
        if remaining:
            remaining.sort(key=sort_key)
            result.extend(remaining)
            logger.warning(
                f"Added {len(remaining)} disconnected nodes to narrative_order"
            )
        
        return result
    
    def _detect_and_break_cycles(
        self,
        all_node_ids: Set[str],
        adjacency: Dict[str, List[str]],
        in_degree: Dict[str, int],
        edges: List[LogicEdge]
    ) -> List[Tuple[str, str]]:
        """
        检测并打断循环
        
        使用DFS检测循环，在最低置信度边处打断。
        置信度判断：
        - 显式关系边 > 因子共现边 > 顺序推断边
        
        Args:
            all_node_ids: 所有节点ID集合
            adjacency: 邻接表
            in_degree: 入度映射
            edges: 边列表
        
        Returns:
            需要移除的边列表 [(from_node, to_node), ...]
            
        **Validates: Requirements 5.2**
        """
        edges_to_remove: List[Tuple[str, str]] = []
        
        # Build edge confidence map
        edge_confidence: Dict[Tuple[str, str], int] = {}
        for edge in edges:
            key = (edge.from_node, edge.to_node)
            inferred_from = edge.metadata.get("inferred_from", "") if edge.metadata else ""
            
            # Confidence levels: explicit > factor_cooccurrence > sequential
            if inferred_from == "explicit_relation":
                confidence = 3
            elif inferred_from == "factor_cooccurrence":
                confidence = 2
            elif inferred_from == "sequential_order":
                confidence = 1
            else:
                confidence = 2  # Default
            
            edge_confidence[key] = confidence
        
        # DFS-based cycle detection
        visited: Set[str] = set()
        rec_stack: Set[str] = set()
        parent: Dict[str, Optional[str]] = {}
        
        def dfs(node: str) -> Optional[List[str]]:
            """DFS to find a cycle, returns cycle path if found."""
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in adjacency.get(node, []):
                if neighbor not in visited:
                    parent[neighbor] = node
                    cycle = dfs(neighbor)
                    if cycle:
                        return cycle
                elif neighbor in rec_stack:
                    # Found a cycle - reconstruct it
                    cycle = [neighbor]
                    current = node
                    while current != neighbor:
                        cycle.append(current)
                        current = parent.get(current)
                        if current is None:
                            break
                    cycle.append(neighbor)
                    return cycle[::-1]
            
            rec_stack.remove(node)
            return None
        
        # Find and break cycles iteratively
        max_iterations = len(all_node_ids)  # Safety limit
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            visited.clear()
            rec_stack.clear()
            parent.clear()
            
            cycle_found = None
            for node_id in all_node_ids:
                if node_id not in visited:
                    parent[node_id] = None
                    cycle_found = dfs(node_id)
                    if cycle_found:
                        break
            
            if not cycle_found:
                break
            
            # Find the lowest confidence edge in the cycle
            min_confidence = float('inf')
            edge_to_break = None
            
            for i in range(len(cycle_found) - 1):
                from_node = cycle_found[i]
                to_node = cycle_found[i + 1]
                key = (from_node, to_node)
                confidence = edge_confidence.get(key, 2)
                
                if confidence < min_confidence:
                    min_confidence = confidence
                    edge_to_break = key
            
            if edge_to_break:
                from_node, to_node = edge_to_break
                edges_to_remove.append(edge_to_break)
                
                # Update adjacency for next iteration
                if to_node in adjacency[from_node]:
                    adjacency[from_node].remove(to_node)
                
                logger.warning(
                    f"Breaking cycle by removing edge: {from_node} -> {to_node} "
                    f"(confidence: {min_confidence})"
                )
        
        if edges_to_remove:
            logger.info(f"Broke {len(edges_to_remove)} cycles")
        
        return edges_to_remove
    
    def _abbreviate(self, book_id: str) -> str:
        """
        生成书籍缩写
        
        Args:
            book_id: 书籍ID
        
        Returns:
            缩写字符串
        """
        # 简单实现：取前几个字符或首字母
        if book_id.isascii():
            # 英文书籍：取单词首字母
            words = book_id.replace("_", " ").split()
            return "".join(w[0] for w in words if w).lower()
        else:
            # 中文书籍：取前两个字的拼音首字母或直接使用
            return book_id[:3]
