"""
LogicChainBuilderV2 - V2版本逻辑链构建器

整合所有V2组件的主编排器。
"""

from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml

from scripts.logic_chain_builder.models import (
    LogicChain,
    LogicNode,
    LogicEdge,
    SourceMetadata,
)
from scripts.logic_chain_builder.loader import SchemaLoader
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.constants import OUTPUT_DIR

from scripts.logic_chain_builder.v2.validator import SourceDataValidator
from scripts.logic_chain_builder.v2.stopwords import StopwordsFilter
from scripts.logic_chain_builder.v2.factor_mapper import FactorMapper
from scripts.logic_chain_builder.v2.clusterer import HierarchicalClusterer
from scripts.logic_chain_builder.v2.edge_inferrer import PrioritizedEdgeInferrer
from scripts.logic_chain_builder.v2.quality_scorer import SemanticQualityScorer
from scripts.logic_chain_builder.v2.book_adapter import BookTypeAdapter
from scripts.logic_chain_builder.v2.backup import BackupManager
from scripts.logic_chain_builder.v2.report import BuildReportGeneratorV2
from scripts.logic_chain_builder.v2.models import (
    BookBuildResult,
    QualityReportV2,
    ValidationReport,
)

from scripts.schema_extractor.models import NarrativeSnippet, ConfigRelation

logger = get_logger(__name__)


class LogicChainBuilderV2:
    """
    V2版本逻辑链构建器
    
    整合所有V2组件:
    - L0: SourceDataValidator
    - L1: FactorMapper + StopwordsFilter
    - L2: HierarchicalClusterer
    - L3: PrioritizedEdgeInferrer
    - L4: SemanticQualityScorer
    - L5: BookTypeAdapter
    - BackupManager
    - BuildReportGeneratorV2
    """
    
    def __init__(
        self,
        loader: SchemaLoader = None,
        output_dir: str = None,
        auto_backup: bool = True,
        auto_rollback: bool = True,
    ):
        """
        初始化构建器
        
        Args:
            loader: SchemaLoader实例
            output_dir: 输出目录
            auto_backup: 是否自动备份
            auto_rollback: 失败时是否自动回滚
        """
        self.loader = loader or SchemaLoader()
        self.output_dir = Path(output_dir or OUTPUT_DIR)
        self.auto_backup = auto_backup
        self.auto_rollback = auto_rollback
        
        # 初始化组件
        self.validator = SourceDataValidator(self.loader)
        self.factor_mapper = FactorMapper()
        self.clusterer = HierarchicalClusterer(self.factor_mapper)
        self.edge_inferrer = PrioritizedEdgeInferrer(self.factor_mapper)
        self.quality_scorer = SemanticQualityScorer()
        self.book_adapter = BookTypeAdapter()
        self.backup_manager = BackupManager()
        self.report_generator = BuildReportGeneratorV2()
    
    def build(self, book_id: str) -> BookBuildResult:
        """
        构建单本书籍的逻辑链
        
        Args:
            book_id: 书籍ID
            
        Returns:
            BookBuildResult
        """
        logger.info(f"Building logic chain for {book_id} (V2)")
        
        # 创建备份
        if self.auto_backup:
            self.backup_manager.create_backup(book_id)
        
        try:
            # L0: 验证数据
            validation_report = self.validator.validate_book(book_id)
            
            if not validation_report.is_complete:
                logger.warning(
                    f"{book_id} has incomplete data: "
                    f"{len(validation_report.issues)} issues found"
                )
            
            # 加载数据
            try:
                snippets = self.loader.load_snippets(book_id)
                relations = self.loader.load_relations(book_id)
            except FileNotFoundError as e:
                return BookBuildResult(
                    book_id=book_id,
                    success=False,
                    error_message=str(e),
                    validation_report=validation_report,
                )
            
            if not snippets:
                return BookBuildResult(
                    book_id=book_id,
                    success=False,
                    error_message="No snippets found",
                    validation_report=validation_report,
                )
            
            # L2: 聚类
            nodes = self.clusterer.cluster(snippets, book_id)
            
            if not nodes:
                return BookBuildResult(
                    book_id=book_id,
                    success=False,
                    error_message="No nodes created from clustering",
                    validation_report=validation_report,
                )
            
            # L1: 构建节点-因子映射
            node_factor_map = self.factor_mapper.build_node_factor_map(
                nodes, snippets
            )
            
            # L3: 推断边
            edges = self.edge_inferrer.infer_edges(
                nodes, relations, snippets, node_factor_map
            )
            
            # 确定入口和终端节点
            entry_nodes = self._find_entry_nodes(nodes, book_id)
            terminal_nodes = self._find_terminal_nodes(nodes, edges)
            
            # 创建逻辑链
            chain = LogicChain(
                chain_id=f"chain_{book_id}",
                book_id=book_id,
                nodes=nodes,
                edges=edges,
                narrative_order=[n.node_id for n in nodes],
                entry_nodes=entry_nodes,
                terminal_nodes=terminal_nodes,
                metadata=SourceMetadata(
                    version="2.0.0",
                    snippet_count=len(snippets),
                    relation_count=len(relations),
                ),
            )
            
            # L4: 质量评估
            quality_report = self.quality_scorer.score(chain, snippets)
            passes, failures = self.quality_scorer.passes_thresholds(quality_report, book_id=book_id)
            
            if not passes:
                logger.warning(
                    f"{book_id} failed quality thresholds: {failures}"
                )
                if self.auto_rollback:
                    self.backup_manager.rollback(
                        book_id,
                        f"Quality thresholds not met: {failures}"
                    )
            
            # 写入输出
            self._write_chain(chain)
            
            return BookBuildResult(
                book_id=book_id,
                success=True,
                chain=chain,
                quality_report=quality_report,
                validation_report=validation_report,
            )
            
        except Exception as e:
            logger.error(f"Failed to build {book_id}: {e}")
            if self.auto_rollback:
                self.backup_manager.rollback(book_id, str(e))
            return BookBuildResult(
                book_id=book_id,
                success=False,
                error_message=str(e),
            )
    
    def build_batch(self, book_ids: List[str] = None) -> Dict[str, BookBuildResult]:
        """
        批量构建逻辑链
        
        Args:
            book_ids: 书籍ID列表，如果为None则处理所有可用书籍
            
        Returns:
            book_id -> BookBuildResult映射
        """
        if book_ids is None:
            book_ids = self.loader.list_available_books()
        
        results = {}
        for book_id in book_ids:
            results[book_id] = self.build(book_id)
        
        # 生成报告
        quality_reports = {
            book_id: result.quality_report
            for book_id, result in results.items()
            if result.quality_report
        }
        
        report = self.report_generator.generate(
            list(results.values()),
            quality_reports
        )
        self.report_generator.write(report)
        
        return results
    
    def validate(self, book_id: str) -> ValidationReport:
        """
        验证单本书籍数据
        
        Args:
            book_id: 书籍ID
            
        Returns:
            ValidationReport
        """
        return self.validator.validate_book(book_id)
    
    def validate_batch(self, book_ids: List[str] = None) -> Dict[str, ValidationReport]:
        """
        批量验证
        
        Args:
            book_ids: 书籍ID列表
            
        Returns:
            book_id -> ValidationReport映射
        """
        if book_ids is None:
            book_ids = self.loader.list_available_books()
        
        return {book_id: self.validate(book_id) for book_id in book_ids}
    
    def _find_entry_nodes(
        self,
        nodes: List[LogicNode],
        book_id: str
    ) -> List[str]:
        """查找入口节点"""
        adapter = self.book_adapter.get_adapter(book_id)
        heuristic = adapter.get_entry_node_heuristics()
        
        # 按启发式评分排序
        scored_nodes = [(n, heuristic(n)) for n in nodes]
        scored_nodes.sort(key=lambda x: x[1], reverse=True)
        
        # 返回得分>0的节点
        entry_nodes = [n.node_id for n, score in scored_nodes if score > 0]
        
        # 如果没有找到，使用第一个主干节点
        if not entry_nodes:
            for node in nodes:
                role_value = node.role.value if hasattr(node.role, 'value') else str(node.role)
                if role_value == "主干":
                    entry_nodes.append(node.node_id)
                    break
        
        # 如果还是没有，使用第一个节点
        if not entry_nodes and nodes:
            entry_nodes = [nodes[0].node_id]
        
        return entry_nodes
    
    def _find_terminal_nodes(
        self,
        nodes: List[LogicNode],
        edges: List[LogicEdge]
    ) -> List[str]:
        """查找终端节点（无出边的节点）"""
        # 找出所有有出边的节点
        nodes_with_outgoing = {edge.from_node for edge in edges}
        
        # 终端节点 = 所有节点 - 有出边的节点
        all_node_ids = {n.node_id for n in nodes}
        terminal_nodes = list(all_node_ids - nodes_with_outgoing)
        
        # 如果没有终端节点，使用最后一个节点
        if not terminal_nodes and nodes:
            terminal_nodes = [nodes[-1].node_id]
        
        return terminal_nodes
    
    def _write_chain(self, chain: LogicChain):
        """写入逻辑链到文件"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = self.output_dir / f"{chain.book_id}.yaml"
        
        # 转换为字典
        chain_dict = chain.model_dump()
        
        # 处理枚举值
        for node in chain_dict.get("nodes", []):
            if hasattr(node.get("role"), "value"):
                node["role"] = node["role"].value
        
        for edge in chain_dict.get("edges", []):
            if hasattr(edge.get("relation"), "value"):
                edge["relation"] = edge["relation"].value
        
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(
                chain_dict,
                f,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
            )
        
        logger.info(f"Wrote logic chain to {output_path}")


# 导出
__all__ = ["LogicChainBuilderV2"]
