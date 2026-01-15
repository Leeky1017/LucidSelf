"""
PrioritizedEdgeInferrer - L3 优先级边推断器

实现多优先级边推断策略:
- explicit_relation (1.0): 显式关系
- factor_semantic (0.8): 因子语义匹配
- condition_dependency (0.7): 条件依赖
- sequential_order (0.5): 顺序推断
"""

from collections import defaultdict
from typing import Dict, List, Set, Tuple

from scripts.logic_chain_builder.models import LogicNode, LogicEdge, EdgeRelation
from scripts.logic_chain_builder.constants import RELATION_TYPE_MAPPING
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.v2.factor_mapper import FactorMapper
from scripts.logic_chain_builder.v2.stopwords import StopwordsFilter
from scripts.schema_extractor.models import ConfigRelation, NarrativeSnippet

logger = get_logger(__name__)


class PrioritizedEdgeInferrer:
    """
    优先级边推断器 (L3)
    
    按优先级顺序推断边，确保高置信度边优先。
    """
    
    INFERENCE_METHODS = [
        ("explicit_relation", 1.0),      # 显式关系（最高置信度）
        ("factor_semantic", 0.8),        # 因子语义匹配
        ("condition_dependency", 0.7),   # 条件依赖推断
        ("sequential_order", 0.5),       # 顺序推断（最低）
    ]
    
    def __init__(self, factor_mapper: FactorMapper = None):
        """
        初始化边推断器
        
        Args:
            factor_mapper: FactorMapper实例
        """
        self.factor_mapper = factor_mapper or FactorMapper()
        self.stopwords_filter = StopwordsFilter()
    
    def infer_edges(
        self,
        nodes: List[LogicNode],
        relations: List[ConfigRelation],
        snippets: List[NarrativeSnippet],
        node_factor_map: Dict[str, Set[str]]
    ) -> List[LogicEdge]:
        """
        按优先级推断边
        
        Args:
            nodes: LogicNode列表
            relations: ConfigRelation列表
            snippets: NarrativeSnippet列表
            node_factor_map: node_id -> factors映射
            
        Returns:
            LogicEdge列表
        """
        edges = []
        visited_pairs: Set[Tuple[str, str]] = set()
        
        for method_name, confidence in self.INFERENCE_METHODS:
            method = getattr(self, f"_infer_{method_name}")
            new_edges = method(
                nodes, relations, snippets, node_factor_map, visited_pairs
            )
            
            for edge in new_edges:
                edge.metadata["confidence"] = confidence
                edge.metadata["inferred_from"] = method_name
                edges.append(edge)
                visited_pairs.add((edge.from_node, edge.to_node))
            
            logger.debug(f"{method_name}: inferred {len(new_edges)} edges")
        
        logger.info(f"Total edges inferred: {len(edges)}")
        return edges
    
    # 空条件约束的模式，需要过滤
    EMPTY_CONDITION_PATTERNS = {'-', '', '无', 'N/A', 'null', '暂无', '/', '—', 'None'}
    
    def _infer_explicit_relation(
        self,
        nodes: List[LogicNode],
        relations: List[ConfigRelation],
        snippets: List[NarrativeSnippet],
        node_factor_map: Dict[str, Set[str]],
        visited_pairs: Set[Tuple[str, str]]
    ) -> List[LogicEdge]:
        """从显式关系推断边 (confidence=1.0)"""
        edges = []
        
        for rel in relations:
            node_pairs = self.factor_mapper.map_relation_to_nodes(
                rel, node_factor_map
            )
            
            for from_node, to_node in node_pairs:
                if (from_node, to_node) not in visited_pairs:
                    edge_relation = self._map_relation_type(rel.relation_type)
                    
                    # 严格过滤空条件约束
                    condition = self._clean_condition(rel.condition_constraint)
                    
                    edges.append(LogicEdge(
                        from_node=from_node,
                        to_node=to_node,
                        relation=edge_relation,
                        condition=condition,
                        metadata={
                            "source_relation_id": rel.relation_id,
                            "source_ref": rel.source_ref,
                        }
                    ))
        
        return edges
    
    def _clean_condition(self, condition: str) -> str:
        """清理条件约束，过滤空值模式"""
        if not condition:
            return None
        
        cleaned = str(condition).strip()
        if cleaned in self.EMPTY_CONDITION_PATTERNS:
            return None
        
        return cleaned
    
    def _infer_factor_semantic(
        self,
        nodes: List[LogicNode],
        relations: List[ConfigRelation],
        snippets: List[NarrativeSnippet],
        node_factor_map: Dict[str, Set[str]],
        visited_pairs: Set[Tuple[str, str]]
    ) -> List[LogicEdge]:
        """从因子语义匹配推断边 (confidence=0.8)"""
        edges = []
        node_ids = list(node_factor_map.keys())
        
        for i, node_a in enumerate(node_ids):
            for node_b in node_ids[i + 1:]:
                if (node_a, node_b) in visited_pairs or (node_b, node_a) in visited_pairs:
                    continue
                
                shared_factors = node_factor_map[node_a] & node_factor_map[node_b]
                
                # 验证shared_factors包含有意义的因子
                if self.stopwords_filter.has_meaningful_factors(shared_factors):
                    # 按source_ref proximity决定方向
                    from_node, to_node = self._order_by_source_ref(
                        node_a, node_b, nodes
                    )
                    
                    edges.append(LogicEdge(
                        from_node=from_node,
                        to_node=to_node,
                        relation=EdgeRelation.SUPPORTS,
                        condition=None,
                        metadata={
                            "shared_factors": list(shared_factors),
                        }
                    ))
        
        return edges
    
    def _infer_condition_dependency(
        self,
        nodes: List[LogicNode],
        relations: List[ConfigRelation],
        snippets: List[NarrativeSnippet],
        node_factor_map: Dict[str, Set[str]],
        visited_pairs: Set[Tuple[str, str]]
    ) -> List[LogicEdge]:
        """从条件依赖推断边 (confidence=0.7)
        
        基于 role="条件分支" 的节点与其他节点的因子关联推断依赖关系。
        """
        edges = []
        
        # 构建 snippet_id -> node_id 映射
        snippet_to_node: Dict[str, str] = {}
        for node in nodes:
            for snippet_id in node.snippet_ids:
                snippet_to_node[snippet_id] = node.node_id
        
        # 找出条件分支节点
        condition_nodes = [
            n for n in nodes
            if (n.role.value if hasattr(n.role, 'value') else str(n.role)) == "条件分支"
        ]
        
        # 为每个条件分支节点查找可能的依赖节点
        for cond_node in condition_nodes:
            cond_factors = node_factor_map.get(cond_node.node_id, set())
            
            # 查找包含相同因子的主干节点
            for node in nodes:
                if node.node_id == cond_node.node_id:
                    continue
                
                role_value = node.role.value if hasattr(node.role, 'value') else str(node.role)
                if role_value != "主干":
                    continue
                
                node_factors = node_factor_map.get(node.node_id, set())
                shared = cond_factors & node_factors
                
                if self.stopwords_filter.has_meaningful_factors(shared):
                    pair = (cond_node.node_id, node.node_id)
                    if pair not in visited_pairs:
                        edges.append(LogicEdge(
                            from_node=cond_node.node_id,
                            to_node=node.node_id,
                            relation=EdgeRelation.DEPENDS_ON,
                            condition=None,
                            metadata={
                                "shared_factors": list(shared),
                            }
                        ))
        
        return edges
    
    def _infer_sequential_order(
        self,
        nodes: List[LogicNode],
        relations: List[ConfigRelation],
        snippets: List[NarrativeSnippet],
        node_factor_map: Dict[str, Set[str]],
        visited_pairs: Set[Tuple[str, str]]
    ) -> List[LogicEdge]:
        """从顺序推断边 (confidence=0.5)"""
        edges = []
        
        # 按source_ref排序节点
        sorted_nodes = sorted(
            nodes,
            key=lambda n: self._get_node_sort_key(n, snippets)
        )
        
        for i in range(len(sorted_nodes) - 1):
            from_node = sorted_nodes[i].node_id
            to_node = sorted_nodes[i + 1].node_id
            
            if (from_node, to_node) not in visited_pairs:
                edges.append(LogicEdge(
                    from_node=from_node,
                    to_node=to_node,
                    relation=EdgeRelation.LEADS_TO,
                    condition=None,
                    metadata={}
                ))
        
        return edges
    
    def _order_by_source_ref(
        self,
        node_a: str,
        node_b: str,
        nodes: List[LogicNode]
    ) -> Tuple[str, str]:
        """根据source_ref顺序决定边的方向"""
        seq_a = self._extract_seq_from_node_id(node_a)
        seq_b = self._extract_seq_from_node_id(node_b)
        return (node_a, node_b) if seq_a <= seq_b else (node_b, node_a)
    
    def _extract_seq_from_node_id(self, node_id: str) -> int:
        """从node_id提取序号"""
        parts = node_id.split("_")
        try:
            return int(parts[-1]) if parts else 0
        except ValueError:
            return 0
    
    def _get_node_sort_key(
        self,
        node: LogicNode,
        snippets: List[NarrativeSnippet]
    ) -> Tuple[str, int]:
        """获取节点排序键"""
        source_ref = node.metadata.get("source_ref", "") or ""
        seq = self._extract_seq_from_node_id(node.node_id)
        return (source_ref, seq)
    
    def _map_relation_type(self, relation_type: str) -> EdgeRelation:
        """映射关系类型"""
        if not relation_type:
            return EdgeRelation.LEADS_TO
        
        normalized = relation_type.lower().strip()
        mapped = RELATION_TYPE_MAPPING.get(normalized)
        
        if mapped:
            return EdgeRelation(mapped)
        
        return EdgeRelation.LEADS_TO


# 导出
__all__ = ["PrioritizedEdgeInferrer"]
