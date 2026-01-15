"""
Conversion Orchestrator

端到端转换编排器，协调所有组件完成 LogicChain → Rule 转换。

Feature: rule-converter
Requirement Refs: Req 9.1-9.10
"""

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from scripts.rule_converter.converters.condition_inferer import (
    ConditionInferer,
    InferenceResult,
)
from scripts.rule_converter.converters.metadata_mapper import MetadataMapper
from scripts.rule_converter.converters.result_builder import ResultBuilder
from scripts.rule_converter.converters.rule_id_generator import RuleIdGenerator
from scripts.rule_converter.loaders.factor_ontology import FactorOntology
from scripts.rule_converter.loaders.logic_chain_loader import (
    LogicChainData,
    LogicChainLoader,
    LogicChainNode,
)
from scripts.rule_converter.loaders.snippet_store import SnippetStore
from scripts.rule_converter.validators.quality_classifier import (
    ClassificationResult,
    QualityClassifier,
    RuleQuality,
)
from scripts.rule_converter.validators.schema_validator import SchemaValidator

logger = logging.getLogger(__name__)


@dataclass
class ConversionResult:
    """单个节点的转换结果"""
    node_id: str
    book_id: str
    rule: Optional[Dict[str, Any]]
    classification: Optional[ClassificationResult]
    error: Optional[str] = None
    
    @property
    def is_success(self) -> bool:
        return self.rule is not None and self.error is None
    
    @property
    def quality(self) -> Optional[RuleQuality]:
        return self.classification.quality if self.classification else None


@dataclass
class ConversionReport:
    """转换报告"""
    start_time: str
    end_time: str
    duration_seconds: float
    
    # 输入统计
    total_chains: int = 0
    total_nodes: int = 0
    convertible_nodes: int = 0
    
    # 转换结果统计
    converted: int = 0
    auto_approved: int = 0
    human_review: int = 0
    rejected: int = 0
    failed: int = 0
    
    # 按体系统计
    by_system: Dict[str, int] = field(default_factory=dict)
    
    # 按书籍统计
    by_book: Dict[str, int] = field(default_factory=dict)
    
    # 错误列表
    errors: List[Dict[str, str]] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration_seconds": self.duration_seconds,
            "input": {
                "total_chains": self.total_chains,
                "total_nodes": self.total_nodes,
                "convertible_nodes": self.convertible_nodes,
            },
            "output": {
                "converted": self.converted,
                "auto_approved": self.auto_approved,
                "human_review": self.human_review,
                "rejected": self.rejected,
                "failed": self.failed,
            },
            "by_system": self.by_system,
            "by_book": self.by_book,
            "errors": self.errors[:20],  # 最多显示20个错误
        }


class ConversionOrchestrator:
    """
    转换编排器
    
    协调所有组件完成 LogicChain → ConfigRuleDefinition 的端到端转换。
    
    工作流程:
    1. 加载数据源（LogicChain、SnippetStore、FactorOntology）
    2. 遍历可转换节点
    3. 对每个节点：推断条件、构建结果、映射元数据、生成ID、质量分级
    4. 输出结果（JSONL 文件、审核队列、报告）
    
    Requirement Refs: Req 9.1-9.10
    """
    
    def __init__(
        self,
        logic_chain_dir: Optional[Path] = None,
        snippet_dir: Optional[Path] = None,
        factor_certified_dir: Optional[Path] = None,
        output_dir: Optional[Path] = None,
    ):
        # 数据目录
        self.logic_chain_dir = logic_chain_dir or Path("data/logic_chains")
        self.snippet_dir = snippet_dir  # None 时使用 SnippetStore 的默认多目录
        self.factor_certified_dir = factor_certified_dir or Path("data/factor_ontology/certified")
        self.output_dir = output_dir or Path("data/rules")
        
        # 组件
        self.loader = LogicChainLoader(self.logic_chain_dir)
        self.snippet_store = SnippetStore(self.snippet_dir, lazy_load=False)  # None 使用默认目录
        self.ontology = FactorOntology(certified_dir=self.factor_certified_dir)
        
        self.condition_inferer: Optional[ConditionInferer] = None
        self.result_builder: Optional[ResultBuilder] = None
        self.metadata_mapper = MetadataMapper()
        self.id_generator = RuleIdGenerator()
        self.quality_classifier: Optional[QualityClassifier] = None
        self.schema_validator = SchemaValidator()
        
        # 状态
        self._loaded = False
        self._results: Dict[str, List[ConversionResult]] = {
            "auto_approve": [],
            "human_review": [],
            "reject": [],
            "failed": [],
        }
    
    def load(self) -> None:
        """加载所有数据源"""
        logger.info("Loading data sources...")
        
        # 加载 LogicChain
        self.loader.load_all()
        logger.info(f"Loaded {len(self.loader)} LogicChains, {self.loader.stats['total_nodes']} nodes")
        
        # 加载 Snippets
        self.snippet_store.load_from_dir()
        logger.info(f"Loaded {len(self.snippet_store)} snippets")
        
        # 加载因子本体
        self.ontology.load()
        logger.info(f"Loaded {len(self.ontology)} factors")
        
        # 初始化转换器
        self.condition_inferer = ConditionInferer(self.ontology)
        self.result_builder = ResultBuilder(self.snippet_store)
        self.quality_classifier = QualityClassifier(self.ontology, self.snippet_store)
        
        self._loaded = True
    
    def convert_all(self, dry_run: bool = False) -> ConversionReport:
        """
        转换所有可转换节点
        
        Args:
            dry_run: 如果为 True，只生成报告不写入文件
            
        Returns:
            ConversionReport
        """
        if not self._loaded:
            self.load()
        
        start_time = datetime.now(timezone.utc)
        
        # 重置状态
        self._reset_results()
        self.id_generator.reset()
        self.metadata_mapper.reset_registry()
        
        # 初始化报告
        report = ConversionReport(
            start_time=start_time.isoformat(),
            end_time="",
            duration_seconds=0,
            total_chains=len(self.loader),
            total_nodes=self.loader.stats["total_nodes"],
            convertible_nodes=self.loader.stats["convertible_nodes"],
        )
        
        # 遍历所有可转换节点
        convertible_nodes = self.loader.get_all_convertible_nodes()
        total = len(convertible_nodes)
        
        for i, (book_id, node) in enumerate(convertible_nodes):
            if i % 100 == 0:
                logger.info(f"Processing {i}/{total}...")
            
            try:
                result = self._convert_node(node, book_id)
                self._record_result(result, report)
            except Exception as e:
                logger.warning(f"Failed to convert {node.node_id}: {e}")
                result = ConversionResult(
                    node_id=node.node_id,
                    book_id=book_id,
                    rule=None,
                    classification=None,
                    error=str(e),
                )
                self._results["failed"].append(result)
                report.failed += 1
                report.errors.append({
                    "node_id": node.node_id,
                    "book_id": book_id,
                    "error": str(e),
                })
        
        # 完成报告
        end_time = datetime.now(timezone.utc)
        report.end_time = end_time.isoformat()
        report.duration_seconds = (end_time - start_time).total_seconds()
        
        # 输出结果
        if not dry_run:
            self._write_outputs()
        
        logger.info(f"Conversion complete: {report.converted} converted, "
                   f"{report.auto_approved} auto-approved, "
                   f"{report.human_review} human-review, "
                   f"{report.rejected} rejected, "
                   f"{report.failed} failed")
        
        return report
    
    def _convert_node(self, node: LogicChainNode, book_id: str) -> ConversionResult:
        """转换单个节点"""
        # 1. 推断条件
        inference_result = self.condition_inferer.infer(node)
        
        # 2. 获取 snippets
        snippets = self.snippet_store.get_batch(node.snippet_ids)
        
        # 3. 构建结果
        rule_result = self.result_builder.build(node, snippets)
        
        # 4. 映射元数据
        source_ref = node.metadata.get("source_ref") if node.metadata else None
        metadata = self.metadata_mapper.map(source_ref, node.node_id, book_id)
        
        # 5. 确定体系
        system = self._infer_system(node, book_id)
        
        # 6. 生成 rule_id
        rule_id = self.id_generator.generate(
            book_id=metadata.book_id,
            category=rule_result.dimension,
            system=system,
        )
        
        # 7. 构建完整规则
        rule = self._build_rule(
            node=node,
            rule_id=rule_id,
            inference_result=inference_result,
            rule_result=rule_result,
            metadata=metadata,
            system=system,
        )
        
        # 8. Schema 验证
        validation_result = self.schema_validator.validate(rule)
        if not validation_result.is_valid:
            logger.debug(f"Schema validation failed for {rule_id}: {validation_result.errors}")
        
        # 9. 质量分级
        classification = self.quality_classifier.classify(
            node=node,
            rule=rule,
            condition_confidence=inference_result.confidence,
        )
        
        return ConversionResult(
            node_id=node.node_id,
            book_id=book_id,
            rule=rule,
            classification=classification,
        )
    
    def _build_rule(
        self,
        node: LogicChainNode,
        rule_id: str,
        inference_result: InferenceResult,
        rule_result,
        metadata,
        system: str,
    ) -> Dict[str, Any]:
        """构建完整的规则字典"""
        # 构建 condition
        condition = None
        if inference_result.condition:
            condition = inference_result.condition.to_dict()
        
        return {
            "rule_id": rule_id,
            "human_label": node.summary or f"规则_{rule_id}",
            "category": rule_result.dimension,
            "condition": condition,
            "required_factors": node.factor_refs or [],
            "is_complex_logic": len(node.factor_refs or []) > 3,
            "result": rule_result.to_dict(),
            "priority": 100,
            "version": "1.0.0",
            "status": "active",
            "engine_id": f"{system}_rule_engine",
            "metadata": metadata.to_dict(),
        }
    
    def _infer_system(self, node: LogicChainNode, book_id: str) -> str:
        """
        推断节点所属的体系
        
        优先级：book_id/典籍名称 > 因子的 applicable_systems
        因为典籍名称是最可靠的体系标识
        """
        # 典籍名称到体系的映射（优先使用）
        book_system_map = {
            # 八字
            "滴天髓": "bazi",
            "ditianshui": "bazi",
            "子平真诠": "bazi",
            "zipingzhenquan": "bazi",
            "子平真": "bazi",
            "三命通会": "bazi",
            "三命通": "bazi",
            "sanminghui": "bazi",
            "渊海子平": "bazi",
            "渊海子": "bazi",
            "穷通宝鉴": "bazi",
            "穷通宝": "bazi",
            # 紫微
            "紫微斗数": "ziwei",
            "紫微斗": "ziwei",
            "ziweidoushu": "ziwei",
            "zwds": "ziwei",
            # 易经
            "周易": "yijing",
            "yijing": "yijing",
            # 解梦
            "周公解梦": "dream",
            "周公解": "dream",
            "梦林玄解": "dream",
            "dreams": "dream",
            "dream": "dream",
            # 塔罗
            "tarot": "tarot",
            "ltt": "tarot",
            "78deg": "tarot",
            "7dow": "tarot",
            "waite": "tarot",
            "thoth": "tarot",
            "tbot": "tarot",
            # 占星
            "astro": "astro",
            "planets": "astro",
            "pit": "astro",
            "transit": "astro",
            "inner_sky": "astro",
            "tis": "astro",
            "aop": "astro",
            "tetrabiblos": "astro",
            "christian_astrology": "astro",
            "cav": "astro",
            "houses": "astro",
            "tah": "astro",
            # 心理学
            "archetypes": "psych",
            "taatcu": "psych",
            "collective_unconscious": "psych",
            "interpretation_of_dreams": "psych",
            "tiod": "psych",
            "collected_works": "psych",
            "jung": "psych",
        }
        
        # 1. 先从 book_id 映射（最可靠）
        book_id_lower = book_id.lower()
        for name, sys in book_system_map.items():
            if name.lower() in book_id_lower:
                return sys
        
        # 2. 从 node_id 映射
        node_id_lower = node.node_id.lower()
        for name, sys in book_system_map.items():
            if name.lower() in node_id_lower:
                return sys
        
        # 3. 最后从因子推断
        if node.factor_refs:
            for factor_id in node.factor_refs:
                system = self.ontology.get_system(factor_id)
                if system:
                    return system
        
        return "unknown"
    
    def _record_result(self, result: ConversionResult, report: ConversionReport):
        """记录转换结果"""
        if not result.is_success:
            self._results["failed"].append(result)
            report.failed += 1
            return
        
        report.converted += 1
        
        # 按质量分类
        quality = result.quality
        if quality == RuleQuality.AUTO_APPROVE:
            self._results["auto_approve"].append(result)
            report.auto_approved += 1
        elif quality == RuleQuality.HUMAN_REVIEW:
            self._results["human_review"].append(result)
            report.human_review += 1
        else:
            self._results["reject"].append(result)
            report.rejected += 1
        
        # 统计体系
        system = result.rule.get("engine_id", "unknown").replace("_rule_engine", "")
        report.by_system[system] = report.by_system.get(system, 0) + 1
        
        # 统计书籍
        report.by_book[result.book_id] = report.by_book.get(result.book_id, 0) + 1
    
    def _reset_results(self):
        """重置结果"""
        for key in self._results:
            self._results[key] = []
    
    def _write_outputs(self):
        """写入输出文件"""
        # 这里调用 JSONLWriter（将在下一步实现）
        pass
    
    @property
    def results(self) -> Dict[str, List[ConversionResult]]:
        """获取转换结果"""
        return self._results
    
    def get_rules_by_quality(self, quality: RuleQuality) -> List[Dict]:
        """获取指定质量等级的规则"""
        key = quality.value
        return [r.rule for r in self._results.get(key, []) if r.rule]
    
    def get_all_approved_rules(self) -> List[Dict]:
        """获取所有已批准的规则"""
        return self.get_rules_by_quality(RuleQuality.AUTO_APPROVE)
