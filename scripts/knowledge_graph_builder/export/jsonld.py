"""
JSONLDExporter - JSON-LD格式导出

Feature: cross-book-knowledge-graph
Requirement Refs: Req 7.7
Design Refs: Design.md#模块结构

实现:
- JSON-LD符合语义Web标准
- 支持过滤参数
- max_nodes限制
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
)
from scripts.knowledge_graph_builder.models.edge import RelationType, SemanticEdge
from scripts.knowledge_graph_builder.models.graph import KnowledgeGraph

logger = logging.getLogger(__name__)


class JSONLDExporter:
    """
    JSON-LD格式导出器
    
    JSON-LD是一种基于JSON的链接数据格式，符合语义Web标准。
    """
    
    DEFAULT_MAX_NODES = 100
    MAX_NODES_LIMIT = 500
    
    # Schema.org和自定义命名空间
    CONTEXT = {
        "@vocab": "http://schema.org/",
        "ls": "http://lucidself.ai/ontology/",
        "concept_id": "ls:conceptId",
        "canonical_label_zh": "ls:labelZh",
        "canonical_label_en": "ls:labelEn",
        "divination_system": "ls:divinationSystem",
        "dimension": "ls:dimension",
        "authority_score": "ls:authorityScore",
        "factor_refs": "ls:factorRefs",
        "source_nodes": "ls:sourceNodes",
        "relation_type": "ls:relationType",
        "confidence": "ls:confidence",
        "conflict_type": "ls:conflictType",
    }
    
    def __init__(self, max_nodes: int = DEFAULT_MAX_NODES):
        self.max_nodes = min(max_nodes, self.MAX_NODES_LIMIT)
    
    def export(
        self,
        graph: KnowledgeGraph,
        output_path: Optional[Union[str, Path]] = None,
        book_ids: Optional[List[str]] = None,
        divination_systems: Optional[List[DivinationSystem]] = None,
        dimensions: Optional[List[Dimension]] = None,
        authority_threshold: float = 0.0,
        relation_types: Optional[List[RelationType]] = None,
        concept_id_prefix: Optional[str] = None,
    ) -> str:
        """
        导出为JSON-LD格式
        
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
            JSON-LD字符串
        """
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
        
        # 构建JSON-LD
        jsonld_data = self._build_jsonld(graph, concepts, edges)
        jsonld_str = json.dumps(jsonld_data, ensure_ascii=False, indent=2)
        
        # 保存文件
        if output_path:
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(jsonld_str)
            logger.info(f"Exported {len(concepts)} nodes, {len(edges)} edges to {path}")
        
        return jsonld_str
    
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
            if concept.authority_score < authority_threshold:
                continue
            
            if concept_id_prefix and not concept.concept_id.startswith(concept_id_prefix):
                continue
            
            if book_id_set:
                concept_books = {s.book_id for s in concept.source_nodes}
                if not concept_books & book_id_set:
                    continue
            
            if system_set and concept.divination_system not in system_set:
                continue
            
            if dimension_set and concept.dimension not in dimension_set:
                continue
            
            filtered.append(concept)
        
        filtered.sort(key=lambda c: c.authority_score, reverse=True)
        return filtered[:self.max_nodes]
    
    def _build_jsonld(
        self,
        graph: KnowledgeGraph,
        concepts: List[ConceptNode],
        edges: List[SemanticEdge],
    ) -> Dict[str, Any]:
        """构建JSON-LD结构"""
        return {
            "@context": self.CONTEXT,
            "@type": "ls:KnowledgeGraph",
            "@id": f"urn:ls:graph:{graph.metadata.version}",
            "name": "LucidSelf Knowledge Graph",
            "version": graph.metadata.version,
            "dateCreated": graph.metadata.build_timestamp.isoformat(),
            "description": "Cross-book divination knowledge graph",
            "@graph": [
                *[self._concept_to_jsonld(c) for c in concepts],
                *[self._edge_to_jsonld(e) for e in edges],
            ],
        }
    
    def _concept_to_jsonld(self, concept: ConceptNode) -> Dict[str, Any]:
        """将ConceptNode转换为JSON-LD节点"""
        node = {
            "@type": "ls:Concept",
            "@id": f"urn:ls:concept:{concept.concept_id}",
            "concept_id": concept.concept_id,
            "canonical_label_zh": concept.canonical_label_zh,
            "divination_system": concept.divination_system.value,
            "dimension": concept.dimension.value,
            "authority_score": concept.authority_score,
            "factor_refs": concept.factor_refs,
        }
        
        if concept.canonical_label_en:
            node["canonical_label_en"] = concept.canonical_label_en
        
        if concept.source_nodes:
            node["source_nodes"] = [
                {
                    "@type": "ls:SourceRef",
                    "book_id": s.book_id,
                    "node_id": s.node_id,
                }
                for s in concept.source_nodes
            ]
        
        return node
    
    def _edge_to_jsonld(self, edge: SemanticEdge) -> Dict[str, Any]:
        """将SemanticEdge转换为JSON-LD边"""
        edge_node = {
            "@type": "ls:SemanticEdge",
            "@id": f"urn:ls:edge:{edge.edge_id}",
            "ls:source": {"@id": f"urn:ls:concept:{edge.source_concept_id}"},
            "ls:target": {"@id": f"urn:ls:concept:{edge.target_concept_id}"},
            "relation_type": edge.relation_type.value,
            "confidence": edge.confidence,
        }
        
        if edge.conflict_type:
            edge_node["conflict_type"] = edge.conflict_type.value
        
        return edge_node
