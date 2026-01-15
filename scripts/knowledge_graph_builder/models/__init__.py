"""
Knowledge Graph Builder Models - 核心数据模型

该模块包含跨书知识图谱的所有核心数据模型。
"""

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    ConflictSummary,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
    SYSTEM_ALLOWED_DIMENSIONS,
    validate_dimension_for_system,
)

from scripts.knowledge_graph_builder.models.edge import (
    ConflictType,
    RelationType,
    SemanticEdge,
    BIDIRECTIONAL_RELATIONS,
    create_edge_id,
)

from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)

from scripts.knowledge_graph_builder.models.query import (
    BatchQueryRequest,
    BatchQueryResult,
    ConflictSeverity,
    ConflictWarning,
    QueryResult,
    QueryResultItem,
    SemanticQuery,
)

from scripts.knowledge_graph_builder.models.conflict import (
    ConceptSummary,
    ConflictOutput,
    ConflictTemplate,
    ResolutionStrategy,
)

from scripts.knowledge_graph_builder.models.selector import (
    ConceptSelectionResult,
    DEFAULT_SYSTEM_QUOTAS,
    FunnelStats,
    SelectorConfig,
    SystemQuota,
)

from scripts.knowledge_graph_builder.models.aggregation import (
    AggregationRulesConfig,
    AggregationStrategy,
    ConceptAggregationRule,
    LabelSelectionStrategy,
)

__all__ = [
    # Enums - concept
    "DivinationSystem",
    "Dimension",
    # Enums - edge
    "RelationType",
    "ConflictType",
    # Enums - query
    "ConflictSeverity",
    # Enums - conflict
    "ResolutionStrategy",
    # Enums - aggregation
    "AggregationStrategy",
    "LabelSelectionStrategy",
    # Models - concept
    "SourceNodeRef",
    "ConflictSummary",
    "ConceptNode",
    # Models - edge
    "SemanticEdge",
    # Models - graph
    "GraphMetadata",
    "KnowledgeGraph",
    # Models - query
    "ConflictWarning",
    "SemanticQuery",
    "QueryResultItem",
    "QueryResult",
    "BatchQueryRequest",
    "BatchQueryResult",
    # Models - conflict
    "ConceptSummary",
    "ConflictOutput",
    "ConflictTemplate",
    # Models - selector
    "SystemQuota",
    "FunnelStats",
    "ConceptSelectionResult",
    "SelectorConfig",
    # Models - aggregation
    "ConceptAggregationRule",
    "AggregationRulesConfig",
    # Utils
    "SYSTEM_ALLOWED_DIMENSIONS",
    "validate_dimension_for_system",
    "BIDIRECTIONAL_RELATIONS",
    "create_edge_id",
    "DEFAULT_SYSTEM_QUOTAS",
]
