"""
Logic Chain Builder - 从Schema数据构建逻辑链

将已提取的Schema数据（snippets、relations）转换为结构化逻辑链。
为全部21本典籍各自构建完整的逻辑链，输出到`data/logic_chains/`目录。

使用方式：
    python -m scripts.logic_chain_builder build <book_id>
    python -m scripts.logic_chain_builder batch
    python -m scripts.logic_chain_builder validate <book_id>

对照文档:
- .kiro/specs/logic-chain-builder/requirements.md
- .kiro/specs/logic-chain-builder/design.md

模块结构:
- models: 数据模型定义 (LogicNode, LogicEdge, LogicChain等)
- loader: SchemaLoader - 加载snippets和relations
- clusterer: SnippetClusterer - 将snippets聚类为节点
- edge_inferrer: EdgeInferrer - 推断节点间的边
- builder: LogicChainBuilder - 构建完整逻辑链
- validator: LogicChainValidator - 验证逻辑链
- writer: LogicChainWriter - 输出YAML文件
- report: BuildReport - 生成构建报告
- cli: CLI入口
"""

__version__ = "1.0.0"
__author__ = "LucidSelf Team"

__all__ = [
    # 数据模型
    "LogicNode",
    "LogicEdge",
    "LogicChain",
    "SourceMetadata",
    "BookStats",
    "BuildReport",
    "ValidationResult",
    # 组件
    "SchemaLoader",
    "SnippetClusterer",
    "EdgeInferrer",
    "LogicChainBuilder",
    "LogicChainValidator",
    "LogicChainWriter",
    "BuildReportGenerator",
    # 常量
    "TARGET_BOOKS",
    "BOOK_TYPE_MAP",
]


def __getattr__(name: str):
    """延迟导入模块"""
    # 数据模型
    if name in ("LogicNode", "LogicEdge", "LogicChain", "SourceMetadata", 
                "BookStats", "BuildReport", "ValidationResult"):
        from scripts.logic_chain_builder import models
        return getattr(models, name)
    
    # 组件
    if name == "SchemaLoader":
        from scripts.logic_chain_builder.loader import SchemaLoader
        return SchemaLoader
    if name == "SnippetClusterer":
        from scripts.logic_chain_builder.clusterer import SnippetClusterer
        return SnippetClusterer
    if name == "EdgeInferrer":
        from scripts.logic_chain_builder.edge_inferrer import EdgeInferrer
        return EdgeInferrer
    if name == "LogicChainBuilder":
        from scripts.logic_chain_builder.builder import LogicChainBuilder
        return LogicChainBuilder
    if name == "LogicChainValidator":
        from scripts.logic_chain_builder.validator import LogicChainValidator
        return LogicChainValidator
    if name == "LogicChainWriter":
        from scripts.logic_chain_builder.writer import LogicChainWriter
        return LogicChainWriter
    if name == "BuildReportGenerator":
        from scripts.logic_chain_builder.report import BuildReportGenerator
        return BuildReportGenerator
    
    # 常量
    if name == "TARGET_BOOKS":
        from scripts.logic_chain_builder.constants import TARGET_BOOKS
        return TARGET_BOOKS
    if name == "BOOK_TYPE_MAP":
        from scripts.logic_chain_builder.constants import BOOK_TYPE_MAP
        return BOOK_TYPE_MAP
    
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
