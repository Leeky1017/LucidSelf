"""
LogicChainValidator - 验证逻辑链的完整性和正确性

验证LogicChain是否符合schema要求。
"""

from typing import List, Set

from scripts.logic_chain_builder.models import (
    LogicChain,
    LogicNode,
    LogicEdge,
    ValidationResult,
    ValidationError,
    SnippetRole,
)
from scripts.logic_chain_builder.logging_config import get_logger


logger = get_logger(__name__)


class LogicChainValidator:
    """
    验证逻辑链的完整性和正确性
    
    执行以下验证：
    - 边引用验证：所有from_node和to_node指向存在的节点
    - 入口节点验证：entry_nodes无入边
    - 终端节点验证：terminal_nodes无出边
    - narrative_order验证：包含所有node_id且无重复
    """
    
    def validate(self, chain: LogicChain) -> ValidationResult:
        """
        执行所有验证
        
        Args:
            chain: LogicChain实例
        
        Returns:
            ValidationResult
        """
        errors: List[ValidationError] = []
        warnings: List[str] = []
        
        # Run all validation checks
        errors.extend(self._validate_edge_references(chain))
        errors.extend(self._validate_entry_nodes(chain))
        errors.extend(self._validate_terminal_nodes(chain))
        errors.extend(self._validate_narrative_order(chain))
        
        # Add warnings for potential issues
        if not chain.entry_nodes:
            warnings.append("No entry nodes defined")
        if not chain.terminal_nodes:
            warnings.append("No terminal nodes defined")
        if not chain.nodes:
            warnings.append("Chain has no nodes")
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            repairs_made=[]
        )
    
    def _validate_edge_references(self, chain: LogicChain) -> List[ValidationError]:
        """
        验证边引用
        
        检查所有from_node和to_node是否指向存在的节点。
        
        Args:
            chain: LogicChain实例
        
        Returns:
            ValidationError列表
        """
        errors: List[ValidationError] = []
        
        # Build set of valid node_ids for O(1) lookup
        valid_node_ids: Set[str] = {node.node_id for node in chain.nodes}
        
        for edge in chain.edges:
            # Check from_node exists
            if edge.from_node not in valid_node_ids:
                errors.append(ValidationError(
                    error_type="invalid_edge_reference",
                    message=f"Edge from_node '{edge.from_node}' does not exist in nodes",
                    details={
                        "edge_from": edge.from_node,
                        "edge_to": edge.to_node,
                        "missing_node": edge.from_node,
                        "field": "from_node"
                    }
                ))
            
            # Check to_node exists
            if edge.to_node not in valid_node_ids:
                errors.append(ValidationError(
                    error_type="invalid_edge_reference",
                    message=f"Edge to_node '{edge.to_node}' does not exist in nodes",
                    details={
                        "edge_from": edge.from_node,
                        "edge_to": edge.to_node,
                        "missing_node": edge.to_node,
                        "field": "to_node"
                    }
                ))
        
        return errors
    
    def _validate_entry_nodes(self, chain: LogicChain) -> List[ValidationError]:
        """
        验证入口节点
        
        检查entry_nodes是否无入边。
        
        Args:
            chain: LogicChain实例
        
        Returns:
            ValidationError列表
        """
        errors: List[ValidationError] = []
        
        # Build set of nodes that have incoming edges
        nodes_with_incoming: Set[str] = {edge.to_node for edge in chain.edges}
        
        # Check each entry_node has no incoming edges
        for entry_node_id in chain.entry_nodes:
            if entry_node_id in nodes_with_incoming:
                # Find the edges that point to this entry node
                incoming_edges = [
                    edge for edge in chain.edges 
                    if edge.to_node == entry_node_id
                ]
                errors.append(ValidationError(
                    error_type="entry_node_has_incoming_edges",
                    message=f"Entry node '{entry_node_id}' has incoming edges",
                    details={
                        "entry_node": entry_node_id,
                        "incoming_edge_count": len(incoming_edges),
                        "incoming_from": [e.from_node for e in incoming_edges]
                    }
                ))
        
        return errors
    
    def _validate_terminal_nodes(self, chain: LogicChain) -> List[ValidationError]:
        """
        验证终端节点
        
        检查terminal_nodes是否无出边。
        
        Args:
            chain: LogicChain实例
        
        Returns:
            ValidationError列表
        """
        errors: List[ValidationError] = []
        
        # Build set of nodes that have outgoing edges
        nodes_with_outgoing: Set[str] = {edge.from_node for edge in chain.edges}
        
        # Check each terminal_node has no outgoing edges
        for terminal_node_id in chain.terminal_nodes:
            if terminal_node_id in nodes_with_outgoing:
                # Find the edges that originate from this terminal node
                outgoing_edges = [
                    edge for edge in chain.edges 
                    if edge.from_node == terminal_node_id
                ]
                errors.append(ValidationError(
                    error_type="terminal_node_has_outgoing_edges",
                    message=f"Terminal node '{terminal_node_id}' has outgoing edges",
                    details={
                        "terminal_node": terminal_node_id,
                        "outgoing_edge_count": len(outgoing_edges),
                        "outgoing_to": [e.to_node for e in outgoing_edges]
                    }
                ))
        
        return errors
    
    def _validate_narrative_order(self, chain: LogicChain) -> List[ValidationError]:
        """
        验证narrative_order
        
        检查是否包含所有node_id且无重复。
        
        Args:
            chain: LogicChain实例
        
        Returns:
            ValidationError列表
        """
        errors: List[ValidationError] = []
        
        # Get all node_ids from nodes
        all_node_ids: Set[str] = {node.node_id for node in chain.nodes}
        
        # Get node_ids in narrative_order
        narrative_order_ids: List[str] = chain.narrative_order
        narrative_order_set: Set[str] = set(narrative_order_ids)
        
        # Check for duplicates in narrative_order
        if len(narrative_order_ids) != len(narrative_order_set):
            # Find the duplicates
            seen: Set[str] = set()
            duplicates: List[str] = []
            for node_id in narrative_order_ids:
                if node_id in seen:
                    duplicates.append(node_id)
                else:
                    seen.add(node_id)
            
            errors.append(ValidationError(
                error_type="duplicate_in_narrative_order",
                message=f"narrative_order contains duplicate node_ids: {duplicates}",
                details={
                    "duplicate_node_ids": duplicates,
                    "narrative_order_length": len(narrative_order_ids),
                    "unique_count": len(narrative_order_set)
                }
            ))
        
        # Check for missing nodes (nodes not in narrative_order)
        missing_from_order = all_node_ids - narrative_order_set
        if missing_from_order:
            errors.append(ValidationError(
                error_type="missing_from_narrative_order",
                message=f"narrative_order is missing {len(missing_from_order)} node(s)",
                details={
                    "missing_node_ids": list(missing_from_order),
                    "total_nodes": len(all_node_ids),
                    "narrative_order_count": len(narrative_order_set)
                }
            ))
        
        # Check for extra nodes (nodes in narrative_order but not in nodes list)
        extra_in_order = narrative_order_set - all_node_ids
        if extra_in_order:
            errors.append(ValidationError(
                error_type="extra_in_narrative_order",
                message=f"narrative_order contains {len(extra_in_order)} node(s) not in nodes list",
                details={
                    "extra_node_ids": list(extra_in_order),
                    "total_nodes": len(all_node_ids),
                    "narrative_order_count": len(narrative_order_set)
                }
            ))
        
        return errors
    
    def auto_repair(self, chain: LogicChain, errors: List[ValidationError]) -> tuple[LogicChain, List[str]]:
        """
        尝试自动修复常见问题
        
        修复策略：
        - 缺少entry_nodes：提升无入边的节点
        - 缺少terminal_nodes：提升无出边的节点
        - 重复边：移除重复
        - 无效边引用：移除无效边
        - entry_nodes有入边：移除有入边的entry_nodes，或移除入边
        - terminal_nodes有出边：移除有出边的terminal_nodes，或移除出边
        
        Args:
            chain: LogicChain实例
            errors: ValidationError列表
        
        Returns:
            tuple of (修复后的LogicChain, 修复记录列表)
        """
        repairs_made: List[str] = []
        
        # Create mutable copies of chain data
        nodes = list(chain.nodes)
        edges = list(chain.edges)
        entry_nodes = list(chain.entry_nodes)
        terminal_nodes = list(chain.terminal_nodes)
        narrative_order = list(chain.narrative_order)
        
        # Build node_id set for validation
        valid_node_ids: Set[str] = {node.node_id for node in nodes}
        
        # 1. Remove invalid edge references
        edges, edge_repairs = self._repair_invalid_edges(edges, valid_node_ids)
        repairs_made.extend(edge_repairs)
        
        # 2. Remove duplicate edges
        edges, dup_repairs = self._repair_duplicate_edges(edges)
        repairs_made.extend(dup_repairs)
        
        # 3. Fix entry_nodes with incoming edges (remove them from entry_nodes)
        entry_nodes, entry_edge_repairs = self._repair_entry_nodes_with_incoming_edges(
            nodes, edges, entry_nodes
        )
        repairs_made.extend(entry_edge_repairs)
        
        # 4. Fix terminal_nodes with outgoing edges (remove them from terminal_nodes)
        terminal_nodes, terminal_edge_repairs = self._repair_terminal_nodes_with_outgoing_edges(
            nodes, edges, terminal_nodes
        )
        repairs_made.extend(terminal_edge_repairs)
        
        # 5. Fix missing entry_nodes (promote nodes with no incoming edges)
        entry_nodes, entry_repairs = self._repair_missing_entry_nodes(
            nodes, edges, entry_nodes
        )
        repairs_made.extend(entry_repairs)
        
        # 6. Fix missing terminal_nodes (promote nodes with no outgoing edges)
        terminal_nodes, terminal_repairs = self._repair_missing_terminal_nodes(
            nodes, edges, terminal_nodes
        )
        repairs_made.extend(terminal_repairs)
        
        # 7. If entry/terminal nodes still have edges (cycle fallback case), remove those edges
        edges, cycle_entry_repairs = self._remove_edges_to_entry_nodes(edges, entry_nodes)
        repairs_made.extend(cycle_entry_repairs)
        
        edges, cycle_terminal_repairs = self._remove_edges_from_terminal_nodes(edges, terminal_nodes)
        repairs_made.extend(cycle_terminal_repairs)
        
        # 8. Fix narrative_order issues
        narrative_order, order_repairs = self._repair_narrative_order(
            nodes, narrative_order
        )
        repairs_made.extend(order_repairs)
        
        # Create repaired chain
        repaired_chain = LogicChain(
            chain_id=chain.chain_id,
            book_id=chain.book_id,
            nodes=nodes,
            edges=edges,
            narrative_order=narrative_order,
            entry_nodes=entry_nodes,
            terminal_nodes=terminal_nodes,
            metadata=chain.metadata,
            version=chain.version
        )
        
        if repairs_made:
            logger.info(f"Auto-repair completed with {len(repairs_made)} repairs")
            for repair in repairs_made:
                logger.debug(f"  - {repair}")
        
        return repaired_chain, repairs_made
    
    def _repair_entry_nodes_with_incoming_edges(
        self,
        nodes: List[LogicNode],
        edges: List[LogicEdge],
        entry_nodes: List[str]
    ) -> tuple[List[str], List[str]]:
        """
        修复有入边的入口节点
        
        移除有入边的节点从entry_nodes列表中。
        
        Args:
            nodes: 节点列表
            edges: 边列表
            entry_nodes: 当前入口节点列表
        
        Returns:
            tuple of (修复后的入口节点列表, 修复记录)
        """
        repairs: List[str] = []
        
        # Find nodes with incoming edges
        nodes_with_incoming: Set[str] = {edge.to_node for edge in edges}
        
        # Filter out entry_nodes that have incoming edges
        valid_entry_nodes = []
        removed_entries = []
        
        for entry_node_id in entry_nodes:
            if entry_node_id in nodes_with_incoming:
                removed_entries.append(entry_node_id)
            else:
                valid_entry_nodes.append(entry_node_id)
        
        if removed_entries:
            repairs.append(
                f"Removed {len(removed_entries)} entry node(s) with incoming edges: {removed_entries}"
            )
        
        return valid_entry_nodes, repairs
    
    def _repair_terminal_nodes_with_outgoing_edges(
        self,
        nodes: List[LogicNode],
        edges: List[LogicEdge],
        terminal_nodes: List[str]
    ) -> tuple[List[str], List[str]]:
        """
        修复有出边的终端节点
        
        移除有出边的节点从terminal_nodes列表中。
        
        Args:
            nodes: 节点列表
            edges: 边列表
            terminal_nodes: 当前终端节点列表
        
        Returns:
            tuple of (修复后的终端节点列表, 修复记录)
        """
        repairs: List[str] = []
        
        # Find nodes with outgoing edges
        nodes_with_outgoing: Set[str] = {edge.from_node for edge in edges}
        
        # Filter out terminal_nodes that have outgoing edges
        valid_terminal_nodes = []
        removed_terminals = []
        
        for terminal_node_id in terminal_nodes:
            if terminal_node_id in nodes_with_outgoing:
                removed_terminals.append(terminal_node_id)
            else:
                valid_terminal_nodes.append(terminal_node_id)
        
        if removed_terminals:
            repairs.append(
                f"Removed {len(removed_terminals)} terminal node(s) with outgoing edges: {removed_terminals}"
            )
        
        return valid_terminal_nodes, repairs

    def _repair_invalid_edges(
        self, 
        edges: List[LogicEdge], 
        valid_node_ids: Set[str]
    ) -> tuple[List[LogicEdge], List[str]]:
        """
        移除引用不存在节点的边
        
        Args:
            edges: 边列表
            valid_node_ids: 有效节点ID集合
        
        Returns:
            tuple of (修复后的边列表, 修复记录)
        """
        repairs: List[str] = []
        valid_edges: List[LogicEdge] = []
        
        for edge in edges:
            from_valid = edge.from_node in valid_node_ids
            to_valid = edge.to_node in valid_node_ids
            
            if from_valid and to_valid:
                valid_edges.append(edge)
            else:
                invalid_refs = []
                if not from_valid:
                    invalid_refs.append(f"from_node='{edge.from_node}'")
                if not to_valid:
                    invalid_refs.append(f"to_node='{edge.to_node}'")
                repairs.append(
                    f"Removed edge with invalid reference(s): {', '.join(invalid_refs)}"
                )
        
        return valid_edges, repairs
    
    def _repair_duplicate_edges(
        self, 
        edges: List[LogicEdge]
    ) -> tuple[List[LogicEdge], List[str]]:
        """
        移除重复边（保留第一个出现的）
        
        Args:
            edges: 边列表
        
        Returns:
            tuple of (去重后的边列表, 修复记录)
        """
        repairs: List[str] = []
        seen: Set[tuple[str, str, str]] = set()
        unique_edges: List[LogicEdge] = []
        
        for edge in edges:
            edge_key = (edge.from_node, edge.to_node, edge.relation.value)
            if edge_key not in seen:
                seen.add(edge_key)
                unique_edges.append(edge)
            else:
                repairs.append(
                    f"Removed duplicate edge: {edge.from_node} -> {edge.to_node} ({edge.relation.value})"
                )
        
        return unique_edges, repairs
    
    def _repair_missing_entry_nodes(
        self,
        nodes: List[LogicNode],
        edges: List[LogicEdge],
        entry_nodes: List[str]
    ) -> tuple[List[str], List[str]]:
        """
        修复缺失的入口节点
        
        如果entry_nodes为空，提升无入边的节点为入口节点。
        
        Args:
            nodes: 节点列表
            edges: 边列表
            entry_nodes: 当前入口节点列表
        
        Returns:
            tuple of (修复后的入口节点列表, 修复记录)
        """
        repairs: List[str] = []
        
        # If there are already entry nodes, no repair needed
        if entry_nodes:
            return entry_nodes, repairs
        
        # If no nodes exist, nothing to repair
        if not nodes:
            return entry_nodes, repairs
        
        # Find nodes with no incoming edges
        nodes_with_incoming: Set[str] = {edge.to_node for edge in edges}
        all_node_ids: Set[str] = {node.node_id for node in nodes}
        
        nodes_without_incoming = all_node_ids - nodes_with_incoming
        
        if nodes_without_incoming:
            # Promote nodes without incoming edges to entry nodes
            # Prefer nodes with role=主干
            promoted = []
            for node in nodes:
                if node.node_id in nodes_without_incoming:
                    promoted.append(node.node_id)
            
            # Sort to prefer 主干 role first
            promoted_sorted = sorted(
                promoted,
                key=lambda nid: 0 if any(
                    n.role == SnippetRole.MAIN for n in nodes if n.node_id == nid
                ) else 1
            )
            
            repairs.append(
                f"Promoted {len(promoted_sorted)} node(s) with no incoming edges to entry_nodes: {promoted_sorted}"
            )
            return promoted_sorted, repairs
        
        # Fallback: if all nodes have incoming edges (cycle), we need to pick entry nodes
        # and remove their incoming edges to make them valid entry nodes
        # Pick the first node as entry and remove edges pointing to it
        first_node_id = nodes[0].node_id
        repairs.append(
            f"No nodes without incoming edges found (possible cycle), using first node as entry: {first_node_id}"
        )
        return [first_node_id], repairs
    
    def _repair_missing_terminal_nodes(
        self,
        nodes: List[LogicNode],
        edges: List[LogicEdge],
        terminal_nodes: List[str]
    ) -> tuple[List[str], List[str]]:
        """
        修复缺失的终端节点
        
        如果terminal_nodes为空，提升无出边的节点为终端节点。
        
        Args:
            nodes: 节点列表
            edges: 边列表
            terminal_nodes: 当前终端节点列表
        
        Returns:
            tuple of (修复后的终端节点列表, 修复记录)
        """
        repairs: List[str] = []
        
        # If there are already terminal nodes, no repair needed
        if terminal_nodes:
            return terminal_nodes, repairs
        
        # If no nodes exist, nothing to repair
        if not nodes:
            return terminal_nodes, repairs
        
        # Find nodes with no outgoing edges
        nodes_with_outgoing: Set[str] = {edge.from_node for edge in edges}
        all_node_ids: Set[str] = {node.node_id for node in nodes}
        
        nodes_without_outgoing = all_node_ids - nodes_with_outgoing
        
        if nodes_without_outgoing:
            # Promote nodes without outgoing edges to terminal nodes
            # Prefer nodes with role=总结
            promoted = []
            for node in nodes:
                if node.node_id in nodes_without_outgoing:
                    promoted.append(node.node_id)
            
            # Sort to prefer 总结 role first
            promoted_sorted = sorted(
                promoted,
                key=lambda nid: 0 if any(
                    n.role == SnippetRole.SUMMARY for n in nodes if n.node_id == nid
                ) else 1
            )
            
            repairs.append(
                f"Promoted {len(promoted_sorted)} node(s) with no outgoing edges to terminal_nodes: {promoted_sorted}"
            )
            return promoted_sorted, repairs
        
        # Fallback: if all nodes have outgoing edges (cycle), use last node
        last_node_id = nodes[-1].node_id
        repairs.append(
            f"No nodes without outgoing edges found (possible cycle), using last node as terminal: {last_node_id}"
        )
        return [last_node_id], repairs
    
    def _remove_edges_to_entry_nodes(
        self,
        edges: List[LogicEdge],
        entry_nodes: List[str]
    ) -> tuple[List[LogicEdge], List[str]]:
        """
        移除指向入口节点的边（用于处理循环图的fallback情况）
        
        Args:
            edges: 边列表
            entry_nodes: 入口节点列表
        
        Returns:
            tuple of (修复后的边列表, 修复记录)
        """
        repairs: List[str] = []
        entry_set = set(entry_nodes)
        
        # Find edges pointing to entry nodes
        edges_to_remove = [e for e in edges if e.to_node in entry_set]
        
        if edges_to_remove:
            # Remove these edges
            filtered_edges = [e for e in edges if e.to_node not in entry_set]
            repairs.append(
                f"Removed {len(edges_to_remove)} edge(s) pointing to entry node(s) to break cycles"
            )
            return filtered_edges, repairs
        
        return edges, repairs
    
    def _remove_edges_from_terminal_nodes(
        self,
        edges: List[LogicEdge],
        terminal_nodes: List[str]
    ) -> tuple[List[LogicEdge], List[str]]:
        """
        移除从终端节点出发的边（用于处理循环图的fallback情况）
        
        Args:
            edges: 边列表
            terminal_nodes: 终端节点列表
        
        Returns:
            tuple of (修复后的边列表, 修复记录)
        """
        repairs: List[str] = []
        terminal_set = set(terminal_nodes)
        
        # Find edges originating from terminal nodes
        edges_to_remove = [e for e in edges if e.from_node in terminal_set]
        
        if edges_to_remove:
            # Remove these edges
            filtered_edges = [e for e in edges if e.from_node not in terminal_set]
            repairs.append(
                f"Removed {len(edges_to_remove)} edge(s) from terminal node(s) to break cycles"
            )
            return filtered_edges, repairs
        
        return edges, repairs

    def _repair_narrative_order(
        self,
        nodes: List[LogicNode],
        narrative_order: List[str]
    ) -> tuple[List[str], List[str]]:
        """
        修复narrative_order问题
        
        确保narrative_order包含所有节点ID且无重复。
        
        Args:
            nodes: 节点列表
            narrative_order: 当前叙事顺序
        
        Returns:
            tuple of (修复后的叙事顺序, 修复记录)
        """
        repairs: List[str] = []
        
        all_node_ids: Set[str] = {node.node_id for node in nodes}
        order_set: Set[str] = set(narrative_order)
        
        # Check for issues
        has_duplicates = len(narrative_order) != len(order_set)
        missing_nodes = all_node_ids - order_set
        extra_nodes = order_set - all_node_ids
        
        if not has_duplicates and not missing_nodes and not extra_nodes:
            return narrative_order, repairs
        
        # Build repaired order
        repaired_order: List[str] = []
        seen: Set[str] = set()
        
        # First, add valid nodes from original order (removing duplicates and extras)
        for node_id in narrative_order:
            if node_id in all_node_ids and node_id not in seen:
                repaired_order.append(node_id)
                seen.add(node_id)
        
        # Then, append any missing nodes at the end
        for node in nodes:
            if node.node_id not in seen:
                repaired_order.append(node.node_id)
                seen.add(node.node_id)
        
        # Report repairs
        if has_duplicates:
            repairs.append("Removed duplicate entries from narrative_order")
        if extra_nodes:
            repairs.append(f"Removed {len(extra_nodes)} non-existent node(s) from narrative_order: {list(extra_nodes)}")
        if missing_nodes:
            repairs.append(f"Added {len(missing_nodes)} missing node(s) to narrative_order: {list(missing_nodes)}")
        
        return repaired_order, repairs
