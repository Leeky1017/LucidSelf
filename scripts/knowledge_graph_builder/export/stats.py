"""
StatsGenerator - 统计报告生成器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 7.4, Req 7.8
Design Refs: Design.md#模块结构

实现:
- stats.json包含详细统计数据
- summary.md包含人类可读的统计报告
"""

import json
import logging
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from scripts.knowledge_graph_builder.models.concept import ConceptNode, DivinationSystem
from scripts.knowledge_graph_builder.models.edge import RelationType, SemanticEdge
from scripts.knowledge_graph_builder.models.graph import KnowledgeGraph

logger = logging.getLogger(__name__)


@dataclass
class GraphStats:
    """图谱统计数据"""
    total_concepts: int
    total_edges: int
    concepts_per_book: Dict[str, int]
    concepts_per_system: Dict[str, int]
    edges_per_relation_type: Dict[str, int]
    average_authority_score: float
    conflict_count: int
    orphan_count: int
    # 额外统计
    total_books: int
    total_systems: int
    total_factors: int
    avg_sources_per_concept: float
    avg_edges_per_concept: float
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'total_concepts': self.total_concepts,
            'total_edges': self.total_edges,
            'concepts_per_book': self.concepts_per_book,
            'concepts_per_system': self.concepts_per_system,
            'edges_per_relation_type': self.edges_per_relation_type,
            'average_authority_score': round(self.average_authority_score, 4),
            'conflict_count': self.conflict_count,
            'orphan_count': self.orphan_count,
            'total_books': self.total_books,
            'total_systems': self.total_systems,
            'total_factors': self.total_factors,
            'avg_sources_per_concept': round(self.avg_sources_per_concept, 2),
            'avg_edges_per_concept': round(self.avg_edges_per_concept, 2),
        }


class StatsGenerator:
    """
    图谱统计生成器
    
    生成:
    - stats.json: 详细统计数据
    - summary.md: 人类可读的统计报告
    """
    
    def generate_stats(self, graph: KnowledgeGraph) -> GraphStats:
        """
        生成统计数据
        
        Args:
            graph: 知识图谱
            
        Returns:
            GraphStats对象
        """
        # 基础统计
        total_concepts = len(graph.concepts)
        total_edges = len(graph.edges)
        
        # 按book统计
        concepts_per_book: Counter = Counter()
        for concept in graph.concepts:
            for source in concept.source_nodes:
                concepts_per_book[source.book_id] += 1
        
        # 按system统计
        concepts_per_system: Counter = Counter()
        for concept in graph.concepts:
            concepts_per_system[concept.divination_system.value] += 1
        
        # 按关系类型统计
        edges_per_relation: Counter = Counter()
        conflict_count = 0
        for edge in graph.edges:
            edges_per_relation[edge.relation_type.value] += 1
            if edge.relation_type == RelationType.CONFLICTS_WITH:
                conflict_count += 1
        
        # 平均权威性分数
        if total_concepts > 0:
            avg_authority = sum(c.authority_score for c in graph.concepts) / total_concepts
        else:
            avg_authority = 0.0
        
        # 孤立节点统计
        connected_ids = set()
        for edge in graph.edges:
            connected_ids.add(edge.source_concept_id)
            connected_ids.add(edge.target_concept_id)
        orphan_count = sum(1 for c in graph.concepts if c.concept_id not in connected_ids)
        
        # 额外统计
        total_books = len(concepts_per_book)
        total_systems = len(concepts_per_system)
        
        all_factors = set()
        total_sources = 0
        for concept in graph.concepts:
            all_factors.update(concept.factor_refs)
            total_sources += len(concept.source_nodes)
        total_factors = len(all_factors)
        
        avg_sources = total_sources / total_concepts if total_concepts > 0 else 0
        avg_edges = total_edges / total_concepts if total_concepts > 0 else 0
        
        return GraphStats(
            total_concepts=total_concepts,
            total_edges=total_edges,
            concepts_per_book=dict(concepts_per_book),
            concepts_per_system=dict(concepts_per_system),
            edges_per_relation_type=dict(edges_per_relation),
            average_authority_score=avg_authority,
            conflict_count=conflict_count,
            orphan_count=orphan_count,
            total_books=total_books,
            total_systems=total_systems,
            total_factors=total_factors,
            avg_sources_per_concept=avg_sources,
            avg_edges_per_concept=avg_edges,
        )
    
    def save_stats(
        self,
        stats: GraphStats,
        output_path: Optional[Union[str, Path]] = None,
    ) -> Path:
        """保存统计数据到JSON文件"""
        path = Path(output_path) if output_path else Path("data/knowledge_graph/stats.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(stats.to_dict(), f, ensure_ascii=False, indent=2)
        
        logger.info(f"Saved stats to {path}")
        return path
    
    def generate_summary(self, graph: KnowledgeGraph, stats: Optional[GraphStats] = None) -> str:
        """
        生成人类可读的统计报告
        
        Args:
            graph: 知识图谱
            stats: 统计数据（可选，不提供则自动生成）
            
        Returns:
            Markdown格式的统计报告
        """
        if stats is None:
            stats = self.generate_stats(graph)
        
        lines = [
            "# 知识图谱统计报告",
            "",
            f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"图谱版本: {graph.metadata.version}",
            "",
            "## 概览统计",
            "",
            f"- **总概念数**: {stats.total_concepts:,}",
            f"- **总边数**: {stats.total_edges:,}",
            f"- **涉及典籍**: {stats.total_books}本",
            f"- **涉及体系**: {stats.total_systems}个",
            f"- **涉及因子**: {stats.total_factors:,}个",
            f"- **平均权威性分数**: {stats.average_authority_score:.2%}",
            f"- **冲突数**: {stats.conflict_count}",
            f"- **孤立节点数**: {stats.orphan_count}",
            "",
        ]
        
        # Top-10 连接概念
        lines.extend([
            "## Top-10 连接最多的概念",
            "",
        ])
        
        edge_counts = Counter()
        for edge in graph.edges:
            edge_counts[edge.source_concept_id] += 1
            edge_counts[edge.target_concept_id] += 1
        
        concept_map = {c.concept_id: c for c in graph.concepts}
        top_connected = edge_counts.most_common(10)
        
        if top_connected:
            lines.append("| 概念 | 连接数 | 权威性 |")
            lines.append("|------|--------|--------|")
            for cid, count in top_connected:
                concept = concept_map.get(cid)
                if concept:
                    lines.append(f"| {concept.canonical_label_zh} | {count} | {concept.authority_score:.2%} |")
        else:
            lines.append("*暂无数据*")
        lines.append("")
        
        # Top-10 权威概念
        lines.extend([
            "## Top-10 最高权威概念",
            "",
        ])
        
        top_authority = sorted(graph.concepts, key=lambda c: c.authority_score, reverse=True)[:10]
        
        if top_authority:
            lines.append("| 概念 | 体系 | 权威性 |")
            lines.append("|------|------|--------|")
            for concept in top_authority:
                lines.append(f"| {concept.canonical_label_zh} | {concept.divination_system.value} | {concept.authority_score:.2%} |")
        else:
            lines.append("*暂无数据*")
        lines.append("")
        
        # 冲突热点
        lines.extend([
            "## 冲突热点",
            "",
        ])
        
        conflict_concepts = Counter()
        for edge in graph.edges:
            if edge.relation_type == RelationType.CONFLICTS_WITH:
                conflict_concepts[edge.source_concept_id] += 1
                conflict_concepts[edge.target_concept_id] += 1
        
        top_conflicts = conflict_concepts.most_common(5)
        
        if top_conflicts:
            lines.append("| 概念 | 冲突数 |")
            lines.append("|------|--------|")
            for cid, count in top_conflicts:
                concept = concept_map.get(cid)
                if concept:
                    lines.append(f"| {concept.canonical_label_zh} | {count} |")
        else:
            lines.append("*无冲突记录*")
        lines.append("")
        
        # 体系分布
        lines.extend([
            "## 体系分布",
            "",
            "| 体系 | 概念数 | 占比 |",
            "|------|--------|------|",
        ])
        
        for system, count in sorted(stats.concepts_per_system.items(), key=lambda x: x[1], reverse=True):
            pct = count / stats.total_concepts * 100 if stats.total_concepts > 0 else 0
            lines.append(f"| {system} | {count:,} | {pct:.1f}% |")
        lines.append("")
        
        # 关系类型分布
        lines.extend([
            "## 关系类型分布",
            "",
            "| 关系类型 | 数量 | 占比 |",
            "|----------|------|------|",
        ])
        
        for rel_type, count in sorted(stats.edges_per_relation_type.items(), key=lambda x: x[1], reverse=True):
            pct = count / stats.total_edges * 100 if stats.total_edges > 0 else 0
            lines.append(f"| {rel_type} | {count:,} | {pct:.1f}% |")
        lines.append("")
        
        # 覆盖缺口
        lines.extend([
            "## 覆盖缺口分析",
            "",
        ])
        
        # 检查哪些体系概念较少
        system_counts = stats.concepts_per_system
        avg_per_system = stats.total_concepts / stats.total_systems if stats.total_systems > 0 else 0
        
        gaps = []
        for system in DivinationSystem:
            count = system_counts.get(system.value, 0)
            if count < avg_per_system * 0.3:  # 低于平均的30%
                gaps.append(f"- **{system.value}**: {count}个概念（低于平均）")
        
        if gaps:
            lines.extend(gaps)
        else:
            lines.append("*各体系覆盖较为均衡*")
        lines.append("")
        
        return '\n'.join(lines)
    
    def save_summary(
        self,
        summary: str,
        output_path: Optional[Union[str, Path]] = None,
    ) -> Path:
        """保存统计报告到Markdown文件"""
        path = Path(output_path) if output_path else Path("data/knowledge_graph/summary.md")
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        logger.info(f"Saved summary to {path}")
        return path
