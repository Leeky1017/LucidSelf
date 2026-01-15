"""
Semantic Layer Core Module

语义层核心模块。
"""

from backend.semantics.core.base import (
    SemanticEntry,
    SemanticRegistry,
    NarrativeSnippetExtended,
)
from backend.semantics.core.cache import (
    SemanticCache,
    CacheStats,
    CacheEntry,
)
from backend.semantics.core.query import (
    SemanticQueryEngine,
    QueryMetrics,
)
from backend.semantics.core.index import (
    SemanticIndexer,
)

__all__ = [
    # Base
    "SemanticEntry",
    "SemanticRegistry",
    "NarrativeSnippetExtended",
    # Cache
    "SemanticCache",
    "CacheStats",
    "CacheEntry",
    # Query
    "SemanticQueryEngine",
    "QueryMetrics",
    # Index
    "SemanticIndexer",
]
