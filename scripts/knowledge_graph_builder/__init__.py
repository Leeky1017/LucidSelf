"""
Knowledge Graph Builder - 跨书知识图谱构建器

该模块负责将23本典籍的单书逻辑链(LogicChain)整合为统一的跨书知识网络,
并向Layer 4 FusionEngine提供只读查询接口。

Layer位置: Layer 2.5 (桥接层)
Phase: Phase 0.5

模块结构:
- models/: 核心数据模型 (ConceptNode, SemanticEdge, KnowledgeGraph等)
- builders/: 图谱构建器 (GraphBuilder, ConceptAligner, ConflictDetector等)
- query/: 查询服务 (SemanticQueryService, ConceptSelector等)
- persistence/: 持久化 (GraphSerializer, SnapshotManager等)
- validation/: 验证器 (GraphValidator等)
- export/: 导出器 (GraphML, Mermaid, JSON-LD等)
- cli.py: CLI命令入口
"""

__version__ = "0.1.0"
