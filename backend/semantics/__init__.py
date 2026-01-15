"""
LucidSelf 语义层 (Semantic Layer)

这个模块取代了旧的 data/semantics/*.jsonl 存储方式，
采用 Python 代码定义 + PostgreSQL 持久化 + Redis 缓存的三层架构。

架构说明：
- Python 定义：提供类型安全和 IDE 支持
- PostgreSQL 存储：提供高性能索引和复杂查询能力
- Redis 缓存：加速热点数据访问

使用方式：
```python
from backend.semantics.dts.jiamu import 甲木参天
from backend.semantics import SemanticRegistry

# 获取语义条目
entry = SemanticRegistry.get("dts_v2_jia_001")

# 查询
results = await SemanticQueryEngine.query_by_factors(["day_master_jia", "season_spring"])
```
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry
from backend.semantics.core.cache import CacheStats, SemanticCache
from backend.semantics.core.index import SemanticIndexer
from backend.semantics.core.query import QueryMetrics, SemanticQueryEngine

__all__ = [
    "SemanticEntry",
    "SemanticRegistry",
    "SemanticQueryEngine",
    "QueryMetrics",
    "SemanticCache",
    "CacheStats",
    "SemanticIndexer",
]
