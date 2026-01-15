"""
GraphMLExporter - GraphML格式导出

Feature: cross-book-knowledge-graph
Requirement Refs: Req 7.1, Req 7.3, Req 7.5
Design Refs: Design.md#模块结构

实现:
- 生成有效GraphML格式
- 支持过滤参数
- max_nodes限制（默认100，max=500）
- 节点按authority_score排序选择
"""

import logging
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional, Set, Union

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
)
from scripts.knowledge_graph_builder.models.edge import SemanticEdge
from scripts.knowledge_graph_builder.models.graph import KnowledgeGraph

logger = logging.getLogger(__name__)


class GraphMLExporter:
    """
    GraphML格式导出器
    
    GraphML是一种基于XML的图形文件格式，可被Gephi、yEd等工具读取。
    """
    
    DEFAULT_MAX_NODES = 100
    MAX_NODES_LIMIT = 500
    
    def __init__(self, max_nodes: int = DEFAULT_MAX_NODES):
        """
        初始化导出器
        
        Args:
            max_nodes: 最大节点数，默认100，最大500
        """
        self.max_nodes = min(max_nodes, self.MAX_NODES_LIMIT)
    
    def export(
        self,
        graph: KnowledgeGraph,
        output_path: Optional[Union[str, Path]] = None,
        book_ids: Optional[List[str]] = None,
        divination_systems: Optional[List[DivinationSystem]] = None,
        dimensions: Optional[List[Dimension]] = None,
        authority_threshold: float = 0.0,
        relation_types: Optional[List['RelationType']] = None,
        concept_id_prefix: Optional[str] = None,
    ) -> str:
        """
        导出为GraphML格式
        
        Args:
            graph: 知识图谱
            output_path: 输出文件路径（可选）
            book_ids: 过滤的book_id列表
            divination_systems: 过滤的体系列表
            dimensions: 过滤的维度列表
            authority_threshold: 权威性阈值
            relation_types: 过滤的边类型列表
            concept_id_prefix: 概念ID前缀过滤
            
        Returns:
            GraphML XML字符串
        """
        from scripts.knowledge_graph_builder.models.edge import RelationType
        
        # 过滤并选择概念
        concepts = self._filter_and_select_concepts(
            graph.concepts,
            book_ids=book_ids,
            divination_systems=divination_systems,
            dimensions=dimensions,
            authority_threshold=authority_threshold,
            concept_id_prefix=concept_id_prefix,
        )
        
        concept_ids = {c.concept_id for c in concepts}
        
        # 过滤边 - include relation_type filter
        edges = []
        for e in graph.edges:
            if e.source_concept_id not in concept_ids or e.target_concept_id not in concept_ids:
                continue
            if relation_types and e.relation_type not in relation_types:
                continue
            edges.append(e)
        
        # 构建GraphML
        xml_content = self._build_graphml(concepts, edges)
        
        # 保存文件
        if output_path:
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(xml_content)
            logger.info(f"Exported {len(concepts)} nodes, {len(edges)} edges to {path}")
        
        return xml_content
    
    def _filter_and_select_concepts(
        self,
        concepts: List[ConceptNode],
        book_ids: Optional[List[str]] = None,
        divination_systems: Optional[List[DivinationSystem]] = None,
        dimensions: Optional[List[Dimension]] = None,
        authority_threshold: float = 0.0,
        concept_id_prefix: Optional[str] = None,
    ) -> List[ConceptNode]:
        """过滤并选择概念"""
        filtered = []
        
        book_id_set = set(book_ids) if book_ids else None
        system_set = set(divination_systems) if divination_systems else None
        dimension_set = set(dimensions) if dimensions else None
        
        for concept in concepts:
            # 权威性过滤
            if concept.authority_score < authority_threshold:
                continue
            
            # concept_id前缀过滤
            if concept_id_prefix and not concept.concept_id.startswith(concept_id_prefix):
                continue
            
            # book_id过滤
            if book_id_set:
                concept_books = {s.book_id for s in concept.source_nodes}
                if not concept_books & book_id_set:
                    continue
            
            # 体系过滤
            if system_set and concept.divination_system not in system_set:
                continue
            
            # 维度过滤
            if dimension_set and concept.dimension not in dimension_set:
                continue
            
            filtered.append(concept)
        
        # 按authority_score排序，选择top N
        filtered.sort(key=lambda c: c.authority_score, reverse=True)
        return filtered[:self.max_nodes]
    
    def _build_graphml(
        self,
        concepts: List[ConceptNode],
        edges: List[SemanticEdge],
    ) -> str:
        """构建GraphML XML"""
        # 创建根元素
        root = ET.Element('graphml')
        root.set('xmlns', 'http://graphml.graphdrawing.org/xmlns')
        root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        root.set('xsi:schemaLocation', 
                 'http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd')
        
        # 定义节点属性
        self._add_key(root, 'd0', 'node', 'label_zh', 'string')
        self._add_key(root, 'd1', 'node', 'label_en', 'string')
        self._add_key(root, 'd2', 'node', 'system', 'string')
        self._add_key(root, 'd3', 'node', 'dimension', 'string')
        self._add_key(root, 'd4', 'node', 'authority', 'double')
        self._add_key(root, 'd5', 'node', 'factor_count', 'int')
        
        # 定义边属性
        self._add_key(root, 'd6', 'edge', 'relation', 'string')
        self._add_key(root, 'd7', 'edge', 'confidence', 'double')
        self._add_key(root, 'd8', 'edge', 'conflict_type', 'string')
        
        # 创建图
        graph_elem = ET.SubElement(root, 'graph')
        graph_elem.set('id', 'knowledge_graph')
        graph_elem.set('edgedefault', 'directed')
        
        # 添加节点
        for concept in concepts:
            node = ET.SubElement(graph_elem, 'node')
            node.set('id', concept.concept_id)
            
            self._add_data(node, 'd0', concept.canonical_label_zh)
            self._add_data(node, 'd1', concept.canonical_label_en or '')
            self._add_data(node, 'd2', concept.divination_system.value)
            self._add_data(node, 'd3', concept.dimension.value)
            self._add_data(node, 'd4', str(concept.authority_score))
            self._add_data(node, 'd5', str(len(concept.factor_refs)))
        
        # 添加边
        for edge in edges:
            edge_elem = ET.SubElement(graph_elem, 'edge')
            edge_elem.set('id', edge.edge_id)
            edge_elem.set('source', edge.source_concept_id)
            edge_elem.set('target', edge.target_concept_id)
            
            self._add_data(edge_elem, 'd6', edge.relation_type.value)
            self._add_data(edge_elem, 'd7', str(edge.confidence))
            if edge.conflict_type:
                self._add_data(edge_elem, 'd8', edge.conflict_type.value)
        
        # 生成XML字符串
        ET.indent(root, space='  ')
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding='unicode')
    
    def _add_key(
        self,
        parent: ET.Element,
        key_id: str,
        for_type: str,
        attr_name: str,
        attr_type: str,
    ) -> None:
        """添加key定义"""
        key = ET.SubElement(parent, 'key')
        key.set('id', key_id)
        key.set('for', for_type)
        key.set('attr.name', attr_name)
        key.set('attr.type', attr_type)
    
    def _add_data(self, parent: ET.Element, key: str, value: str) -> None:
        """添加data元素"""
        data = ET.SubElement(parent, 'data')
        data.set('key', key)
        data.text = value
