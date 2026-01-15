"""
Persistence Package - 知识图谱持久化模块

Feature: cross-book-knowledge-graph
Requirement Refs: Req 8.1
Design Refs: Design.md#模块结构

模块包含:
- GraphSerializer: YAML序列化/反序列化器
- SnapshotManager: 版本快照管理器
- LazyKnowledgeGraph: 懒加载图谱包装器
"""

from scripts.knowledge_graph_builder.persistence.serializer import (
    GraphSerializer,
    LazyKnowledgeGraph,
    SerializationError,
    DeserializationError,
)
from scripts.knowledge_graph_builder.persistence.snapshot import (
    SnapshotManager,
    SnapshotInfo,
    SnapshotError,
)

__all__ = [
    # Serializer
    "GraphSerializer",
    "LazyKnowledgeGraph",
    "SerializationError",
    "DeserializationError",
    # Snapshot
    "SnapshotManager",
    "SnapshotInfo",
    "SnapshotError",
]
