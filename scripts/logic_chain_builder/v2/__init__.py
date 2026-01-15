"""
Logic Chain Builder V2 - 全面升级版

包含以下核心组件:
- L0: SourceDataValidator - 源数据完整性校验
- L1: FactorMapper + StopwordsFilter - 因子映射与停用词过滤
- L2: HierarchicalClusterer - 三级聚类
- L3: PrioritizedEdgeInferrer - 优先级边推断
- L4: SemanticQualityScorer - 语义质量评估
- L5: BookTypeAdapter - 领域适配器
- BackupManager - 备份与回滚
- BuildReportGeneratorV2 - 升级版报告生成
"""

from scripts.logic_chain_builder.v2.validator import (
    SourceDataValidator,
    ValidationReport,
    DataQualityIssue,
)
from scripts.logic_chain_builder.v2.stopwords import StopwordsFilter
from scripts.logic_chain_builder.v2.factor_mapper import FactorMapper
from scripts.logic_chain_builder.v2.clusterer import HierarchicalClusterer
from scripts.logic_chain_builder.v2.edge_inferrer import PrioritizedEdgeInferrer
from scripts.logic_chain_builder.v2.quality_scorer import (
    SemanticQualityScorer,
    QualityReportV2,
)
from scripts.logic_chain_builder.v2.report import (
    BuildReportGeneratorV2,
    BuildReportV2,
    BookStatsV2,
)
from scripts.logic_chain_builder.v2.book_adapter import (
    BookTypeAdapter,
    BaseAdapter,
    BaziAdapter,
    ZiweiAdapter,
    AstrologyAdapter,
    TarotAdapter,
    DreamAdapter,
    YijingAdapter,
)
from scripts.logic_chain_builder.v2.backup import BackupManager
from scripts.logic_chain_builder.v2.builder import LogicChainBuilderV2

__all__ = [
    # L0
    "SourceDataValidator",
    "ValidationReport",
    "DataQualityIssue",
    # L1
    "StopwordsFilter",
    "FactorMapper",
    # L2
    "HierarchicalClusterer",
    # L3
    "PrioritizedEdgeInferrer",
    # L4
    "SemanticQualityScorer",
    "QualityReportV2",
    # L5
    "BookTypeAdapter",
    "BaseAdapter",
    "BaziAdapter",
    "ZiweiAdapter",
    "AstrologyAdapter",
    "TarotAdapter",
    "DreamAdapter",
    "YijingAdapter",
    # Report
    "BuildReportGeneratorV2",
    "BuildReportV2",
    "BookStatsV2",
    # Backup
    "BackupManager",
    # Builder
    "LogicChainBuilderV2",
]
