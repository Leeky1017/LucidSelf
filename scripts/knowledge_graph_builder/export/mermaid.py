"""
MermaidExporter - Mermaid图表格式导出

Feature: cross-book-knowledge-graph
Requirement Refs: Req 7.2, Req 7.6
Design Refs: Design.md#模块结构

实现:
- Mermaid使用subgraph按divination_system分组
- 支持过滤参数
- max_nodes限制
"""

import logging
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Union

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
)
from scripts.knowledge_graph_builder.models.edge import RelationType, SemanticEdge
from scripts.knowledge_graph_builder.models.graph import KnowledgeGraph

logger = logging.getLogger(__name__)


class MermaidExporter:
    """
    Mermaid图表格式导出器
    
    Mermaid是一种基于Markdown的图表工具，可嵌入文档。
    使用subgraph按divination_system分组以提高可读性。
    """
    
    DEFAULT_MAX_NODES = 100
    MAX_NODES_LIMIT = 500
    
    # 关系类型到Mermaid箭头的映射
    RELATION_ARROWS = {
        RelationType.SYNONYM: '---',
        RelationType.ENTAILS: '-->',
        RelationType.CONFLICTS_WITH: 'x--x',
        RelationType.COMPLEMENTS: '<-->',
        RelationType.SPECIALIZES: '-.->',
        RelationType.GENERALIZES: '-..->',
        RelationType.CROSS_SYSTEM_EQUIVALENT: '===',
    }
    
    # 体系中文名
    SYSTEM_NAMES = {
        DivinationSystem.BAZI: '八字',
        DivinationSystem.ZIWEI: '紫微',
        DivinationSystem.ASTRO: '占星',
        DivinationSystem.TAROT: '塔罗',
        DivinationSystem.DREAM: '解梦',
        DivinationSystem.YIJING: '周易',
        DivinationSystem.PSYCHOLOGY: '心理',
        DivinationSystem.CROSS_SYSTEM: '跨体系',
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
        导出为Mermaid格式
        
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
            Mermaid图表字符串
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
        
        # 构建Mermaid
        mermaid_content = self._build_mermaid(concepts, edges)
        
        # 保存文件
        if output_path:
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(mermaid_content)
            logger.info(f"Exported {len(concepts)} nodes, {len(edges)} edges to {path}")
        
        return mermaid_content
    
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
    
    def _build_mermaid(
        self,
        concepts: List[ConceptNode],
        edges: List[SemanticEdge],
    ) -> str:
        """构建Mermaid图表"""
        lines = ['graph TD']
        
        # 按体系分组
        system_concepts: Dict[DivinationSystem, List[ConceptNode]] = defaultdict(list)
        for concept in concepts:
            system_concepts[concept.divination_system].append(concept)
        
        # 创建节点ID映射（简化ID以便显示）
        id_map = {c.concept_id: f"n{i}" for i, c in enumerate(concepts)}
        
        # 生成subgraph
        for system, system_nodes in sorted(system_concepts.items(), key=lambda x: x[0].value):
            system_name = self.SYSTEM_NAMES.get(system, system.value)
            lines.append(f'    subgraph {system_name}')
            
            for concept in system_nodes:
                short_id = id_map[concept.concept_id]
                label = self._escape_label(concept.canonical_label_zh)
                # 使用节点形状表示权威性
                if concept.authority_score >= 0.9:
                    lines.append(f'        {short_id}[("{label}")]')  # 圆角矩形（高权威）
                elif concept.authority_score >= 0.7:
                    lines.append(f'        {short_id}["{label}"]')  # 矩形
                else:
                    lines.append(f'        {short_id}("{label}")')  # 圆角（低权威）
            
            lines.append('    end')
        
        # 生成边
        lines.append('')
        for edge in edges:
            source = id_map.get(edge.source_concept_id)
            target = id_map.get(edge.target_concept_id)
            if source and target:
                arrow = self.RELATION_ARROWS.get(edge.relation_type, '-->')
                lines.append(f'    {source} {arrow} {target}')
        
        return '\n'.join(lines)
    
    def _escape_label(self, label: str) -> str:
        """转义Mermaid标签中的特殊字符"""
        # 限制长度
        if len(label) > 20:
            label = label[:18] + '..'
        # 转义引号
        label = label.replace('"', "'")
        return label
