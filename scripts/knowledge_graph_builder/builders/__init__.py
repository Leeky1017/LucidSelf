"""
Knowledge Graph Builders - 图谱构建器模块

包含：
- GraphBuilder: 图谱构建器主框架
- ConceptAligner: 概念对齐器
- ConceptAggregator: 概念聚合器
- ConflictDetector: 冲突检测器
- AuthorityScorer: 权威性计算器
"""

from scripts.knowledge_graph_builder.builders.graph_builder import (
    BuildManifest,
    GraphBuilder,
    LogicChainData,
)

from scripts.knowledge_graph_builder.builders.alignment import (
    AlignmentCandidate,
    AlignmentThresholds,
    ConceptAligner,
    prioritize_alignments,
)

from scripts.knowledge_graph_builder.builders.aggregator import (
    ConceptAggregator,
)

from scripts.knowledge_graph_builder.builders.conflict_detector import (
    ConflictCandidate,
    ConflictDetector,
)

from scripts.knowledge_graph_builder.builders.authority import (
    AuthorityScorer,
)

__all__ = [
    # GraphBuilder
    "BuildManifest",
    "GraphBuilder",
    "LogicChainData",
    # Alignment
    "AlignmentCandidate",
    "AlignmentThresholds",
    "ConceptAligner",
    "prioritize_alignments",
    # Aggregation
    "ConceptAggregator",
    # Conflict Detection
    "ConflictCandidate",
    "ConflictDetector",
    # Authority
    "AuthorityScorer",
]
