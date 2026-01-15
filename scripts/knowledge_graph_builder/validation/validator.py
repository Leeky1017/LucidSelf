"""
GraphValidator - 图谱完整性验证器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 6.1, Req 6.2, Req 6.3, Req 6.4, Req 6.5, Req 6.6, Req 6.7, Req 6.8, Req 6.9, Req 6.10
Design Refs: Design.md#错误分类

实现:
- 验证source_node引用可解析
- 检测孤立节点（WARNING）
- 检测循环依赖（ERROR）
- 验证factor_refs匹配namespace
- 验证edge引用的concept存在
- 验证divination_system一致性
- 生成validation_report.json
"""

import json
import logging
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import yaml

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
)
from scripts.knowledge_graph_builder.models.edge import RelationType, SemanticEdge
from scripts.knowledge_graph_builder.models.graph import KnowledgeGraph

logger = logging.getLogger(__name__)


class IssueSeverity(str, Enum):
    """问题严重性"""
    ERROR = "error"      # 致命错误，图谱无效
    WARNING = "warning"  # 警告，不影响有效性
    INFO = "info"        # 信息提示


class IssueType(str, Enum):
    """问题类型"""
    # 引用类
    INVALID_SOURCE_NODE_REF = "invalid_source_node_ref"
    INVALID_EDGE_CONCEPT_REF = "invalid_edge_concept_ref"
    INVALID_FACTOR_REF = "invalid_factor_ref"
    # 结构类
    ORPHAN_CONCEPT = "orphan_concept"
    CIRCULAR_DEPENDENCY = "circular_dependency"
    DUPLICATE_CONCEPT_ID = "duplicate_concept_id"
    DUPLICATE_EDGE_ID = "duplicate_edge_id"
    # 一致性类
    SYSTEM_CONSISTENCY = "system_consistency"
    DIMENSION_CONSISTENCY = "dimension_consistency"
    # 其他
    EMPTY_GRAPH = "empty_graph"


@dataclass
class ValidationIssue:
    """验证问题"""
    severity: IssueSeverity
    issue_type: IssueType
    affected_ids: List[str]
    message: str
    suggested_fix: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'severity': self.severity.value,
            'issue_type': self.issue_type.value,
            'affected_ids': self.affected_ids,
            'message': self.message,
            'suggested_fix': self.suggested_fix,
        }


@dataclass
class ValidationReport:
    """验证报告"""
    validation_timestamp: datetime = field(default_factory=datetime.now)
    error_count: int = 0
    warning_count: int = 0
    info_count: int = 0
    issues: List[ValidationIssue] = field(default_factory=list)
    graph_status: str = "valid"
    
    def add_issue(self, issue: ValidationIssue) -> None:
        """添加问题"""
        self.issues.append(issue)
        if issue.severity == IssueSeverity.ERROR:
            self.error_count += 1
            self.graph_status = "invalid"
        elif issue.severity == IssueSeverity.WARNING:
            self.warning_count += 1
        else:
            self.info_count += 1
    
    def to_dict(self) -> Dict:
        return {
            'validation_timestamp': self.validation_timestamp.isoformat(),
            'error_count': self.error_count,
            'warning_count': self.warning_count,
            'info_count': self.info_count,
            'graph_status': self.graph_status,
            'issues': [i.to_dict() for i in self.issues],
        }
    
    def is_valid(self) -> bool:
        return self.error_count == 0


class GraphValidator:
    """
    图谱完整性验证器
    
    验证内容:
    1. 引用完整性：source_node、edge概念、factor_refs
    2. 结构完整性：孤立节点、循环依赖、重复ID
    3. 一致性：divination_system、dimension约束
    """
    
    def __init__(
        self,
        logic_chains_dir: Optional[Union[str, Path]] = None,
        factor_namespace_path: Optional[Union[str, Path]] = None,
        dimension_config_path: Optional[Union[str, Path]] = None,
    ):
        """
        初始化验证器
        
        Args:
            logic_chains_dir: LogicChain目录路径
            factor_namespace_path: 因子命名空间文件路径
            dimension_config_path: 维度配置文件路径
        """
        self.logic_chains_dir = Path(logic_chains_dir) if logic_chains_dir else Path("data/logic_chains")
        self.factor_namespace_path = Path(factor_namespace_path) if factor_namespace_path else Path("data/factor_ontology/namespace.yaml")
        self.dimension_config_path = Path(dimension_config_path) if dimension_config_path else Path("data/knowledge_graph/dimension_config.yaml")
        
        # 缓存
        self._logic_chains_cache: Optional[Dict[str, Dict]] = None
        self._factor_namespaces_cache: Optional[Set[str]] = None
        self._dimension_config_cache: Optional[Dict[str, List[str]]] = None
    
    def validate(self, graph: KnowledgeGraph) -> ValidationReport:
        """
        执行完整验证
        
        Args:
            graph: 要验证的知识图谱
            
        Returns:
            ValidationReport
        """
        report = ValidationReport()
        
        # 空图检查
        if not graph.concepts and not graph.edges:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.INFO,
                issue_type=IssueType.EMPTY_GRAPH,
                affected_ids=[],
                message="Graph is empty",
                suggested_fix="Build the graph using GraphBuilder",
            ))
            return report
        
        # 1. 检测重复ID
        self._check_duplicate_ids(graph, report)
        
        # 2. 验证edge引用的concept存在
        self._check_edge_concept_refs(graph, report)
        
        # 3. 检测孤立节点
        self._check_orphan_concepts(graph, report)
        
        # 4. 检测循环依赖
        self._check_circular_dependencies(graph, report)
        
        # 5. 验证source_node引用
        self._check_source_node_refs(graph, report)
        
        # 6. 验证factor_refs
        self._check_factor_refs(graph, report)
        
        # 7. 验证divination_system一致性
        self._check_system_consistency(graph, report)
        
        # 8. 验证dimension一致性
        self._check_dimension_consistency(graph, report)
        
        # 更新图谱状态
        if report.is_valid():
            graph.metadata.graph_status = "valid"
            graph.metadata.validation_passed = True
            graph.metadata.last_validated_at = datetime.now()
        else:
            graph.metadata.graph_status = "invalid"
            graph.metadata.validation_passed = False
        
        return report
    
    def save_report(
        self,
        report: ValidationReport,
        output_path: Optional[Union[str, Path]] = None,
    ) -> Path:
        """保存验证报告到JSON文件"""
        path = Path(output_path) if output_path else Path("data/knowledge_graph/validation_report.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report.to_dict(), f, ensure_ascii=False, indent=2)
        
        logger.info(f"Saved validation report to {path}")
        return path
    
    def _check_duplicate_ids(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """检测重复ID"""
        # 检测重复concept_id
        concept_ids = [c.concept_id for c in graph.concepts]
        seen = set()
        duplicates = []
        for cid in concept_ids:
            if cid in seen:
                duplicates.append(cid)
            seen.add(cid)
        
        if duplicates:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.ERROR,
                issue_type=IssueType.DUPLICATE_CONCEPT_ID,
                affected_ids=duplicates,
                message=f"Found {len(duplicates)} duplicate concept_ids",
                suggested_fix="Remove or merge duplicate concepts",
            ))
        
        # 检测重复edge_id
        edge_ids = [e.edge_id for e in graph.edges]
        seen = set()
        duplicates = []
        for eid in edge_ids:
            if eid in seen:
                duplicates.append(eid)
            seen.add(eid)
        
        if duplicates:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.ERROR,
                issue_type=IssueType.DUPLICATE_EDGE_ID,
                affected_ids=duplicates,
                message=f"Found {len(duplicates)} duplicate edge_ids",
                suggested_fix="Remove or regenerate duplicate edges",
            ))
    
    def _check_edge_concept_refs(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """验证edge引用的concept存在"""
        concept_ids = {c.concept_id for c in graph.concepts}
        invalid_refs = []
        
        for edge in graph.edges:
            if edge.source_concept_id not in concept_ids:
                invalid_refs.append(f"{edge.edge_id}:source={edge.source_concept_id}")
            if edge.target_concept_id not in concept_ids:
                invalid_refs.append(f"{edge.edge_id}:target={edge.target_concept_id}")
        
        if invalid_refs:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.ERROR,
                issue_type=IssueType.INVALID_EDGE_CONCEPT_REF,
                affected_ids=invalid_refs,
                message=f"Found {len(invalid_refs)} edges referencing non-existent concepts",
                suggested_fix="Remove edges with invalid references or add missing concepts",
            ))
    
    def _check_orphan_concepts(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """检测孤立节点（没有任何边连接的节点）"""
        if not graph.edges:
            return  # 空边列表时不检查
        
        connected_ids = set()
        for edge in graph.edges:
            connected_ids.add(edge.source_concept_id)
            connected_ids.add(edge.target_concept_id)
        
        orphan_ids = [
            c.concept_id for c in graph.concepts
            if c.concept_id not in connected_ids
        ]
        
        if orphan_ids:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.WARNING,
                issue_type=IssueType.ORPHAN_CONCEPT,
                affected_ids=orphan_ids[:20],  # 限制数量
                message=f"Found {len(orphan_ids)} orphan concepts with no edges",
                suggested_fix="Review and connect orphan concepts or remove if unnecessary",
            ))
    
    def _check_circular_dependencies(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """检测循环依赖（在entails/specializes/generalizes关系中）"""
        # 构建有向图
        directed_relations = {
            RelationType.ENTAILS,
            RelationType.SPECIALIZES,
            RelationType.GENERALIZES,
        }
        
        adjacency: Dict[str, List[str]] = defaultdict(list)
        for edge in graph.edges:
            if edge.relation_type in directed_relations:
                adjacency[edge.source_concept_id].append(edge.target_concept_id)
        
        if not adjacency:
            return
        
        # DFS检测环
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        cycles = []
        
        def dfs(node: str, path: List[str]) -> bool:
            color[node] = GRAY
            path.append(node)
            
            for neighbor in adjacency.get(node, []):
                if color[neighbor] == GRAY:
                    # 找到环
                    cycle_start = path.index(neighbor)
                    cycles.append(path[cycle_start:])
                    return True
                elif color[neighbor] == WHITE:
                    if dfs(neighbor, path):
                        return True
            
            path.pop()
            color[node] = BLACK
            return False
        
        for node in adjacency:
            if color[node] == WHITE:
                dfs(node, [])
        
        if cycles:
            cycle_strs = [" -> ".join(c[:5]) + ("..." if len(c) > 5 else "") for c in cycles[:3]]
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.ERROR,
                issue_type=IssueType.CIRCULAR_DEPENDENCY,
                affected_ids=[n for c in cycles for n in c][:20],
                message=f"Found {len(cycles)} circular dependencies: {'; '.join(cycle_strs)}",
                suggested_fix="Remove edges causing cycles in entails/specializes/generalizes relations",
            ))
    
    def _check_source_node_refs(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """验证source_node引用可解析"""
        logic_chains = self._load_logic_chains()
        if not logic_chains:
            return  # 无法验证
        
        invalid_refs = []
        for concept in graph.concepts:
            for source in concept.source_nodes:
                book_id = source.book_id
                node_id = source.node_id
                
                if book_id not in logic_chains:
                    invalid_refs.append(f"{concept.concept_id}:book={book_id}")
                else:
                    node_ids = {n.get('node_id') for n in logic_chains[book_id].get('nodes', [])}
                    if node_id not in node_ids:
                        invalid_refs.append(f"{concept.concept_id}:node={node_id}")
        
        if invalid_refs:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.WARNING,
                issue_type=IssueType.INVALID_SOURCE_NODE_REF,
                affected_ids=invalid_refs[:20],
                message=f"Found {len(invalid_refs)} unresolvable source_node references",
                suggested_fix="Verify LogicChain files exist and contain referenced nodes",
            ))
    
    def _check_factor_refs(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """验证factor_refs匹配namespace"""
        namespaces = self._load_factor_namespaces()
        if not namespaces:
            return  # 无法验证
        
        invalid_refs = []
        for concept in graph.concepts:
            for factor_id in concept.factor_refs:
                # 检查是否匹配任一命名空间前缀
                if not any(factor_id.startswith(ns) for ns in namespaces):
                    # 也接受无前缀的（可能是通用因子）
                    if '_' in factor_id:
                        prefix = factor_id.split('_')[0] + '_'
                        if prefix not in namespaces and factor_id not in {'general', 'unknown'}:
                            invalid_refs.append(f"{concept.concept_id}:factor={factor_id}")
        
        if invalid_refs:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.WARNING,
                issue_type=IssueType.INVALID_FACTOR_REF,
                affected_ids=invalid_refs[:20],
                message=f"Found {len(invalid_refs)} factor_refs not matching namespace patterns",
                suggested_fix="Verify factor_ids conform to namespace.yaml patterns",
            ))
    
    def _check_system_consistency(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """验证divination_system一致性"""
        inconsistent = []
        
        for concept in graph.concepts:
            if concept.divination_system == DivinationSystem.CROSS_SYSTEM:
                continue  # 跨体系概念允许多来源
            
            for source in concept.source_nodes:
                # 从book_id推断体系
                book_system = self._infer_system_from_book(source.book_id)
                if book_system and book_system != concept.divination_system:
                    inconsistent.append(
                        f"{concept.concept_id}:system={concept.divination_system.value},book={source.book_id}"
                    )
        
        if inconsistent:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.WARNING,
                issue_type=IssueType.SYSTEM_CONSISTENCY,
                affected_ids=inconsistent[:20],
                message=f"Found {len(inconsistent)} concepts with divination_system inconsistent with source book",
                suggested_fix="Review concept system assignments or mark as cross_system",
            ))
    
    def _check_dimension_consistency(self, graph: KnowledgeGraph, report: ValidationReport) -> None:
        """验证dimension与divination_system的一致性 - 使用dimension_config.yaml"""
        inconsistent = []
        
        # Load dimension config from YAML
        allowed_dimensions = self._load_dimension_config()
        
        for concept in graph.concepts:
            system_key = concept.divination_system.value
            allowed = allowed_dimensions.get(system_key, [])
            
            # If no config for this system, allow all dimensions
            if not allowed:
                continue
            
            # Map dimension enum value to Chinese label for comparison
            dimension_label = self._dimension_to_label(concept.dimension)
            
            if dimension_label not in allowed:
                inconsistent.append(
                    f"{concept.concept_id}:system={system_key},dim={concept.dimension.value}"
                )
        
        if inconsistent:
            report.add_issue(ValidationIssue(
                severity=IssueSeverity.WARNING,
                issue_type=IssueType.DIMENSION_CONSISTENCY,
                affected_ids=inconsistent[:20],
                message=f"Found {len(inconsistent)} concepts with dimension not allowed for their system",
                suggested_fix="Review dimension assignments according to dimension_config.yaml",
            ))
    
    def _load_dimension_config(self) -> Dict[str, List[str]]:
        """仍imension_config.yaml加载维度配置"""
        if self._dimension_config_cache is not None:
            return self._dimension_config_cache
        
        self._dimension_config_cache = {}
        
        if not self.dimension_config_path.exists():
            logger.warning(f"Dimension config not found: {self.dimension_config_path}")
            return self._dimension_config_cache
        
        try:
            with open(self.dimension_config_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data and 'system_dimensions' in data:
                    for system, config in data['system_dimensions'].items():
                        dimensions = config.get('dimensions', [])
                        self._dimension_config_cache[system] = dimensions
        except Exception as e:
            logger.warning(f"Failed to load dimension config: {e}")
        
        return self._dimension_config_cache
    
    def _dimension_to_label(self, dimension: Dimension) -> str:
        """将Dimension枚举转换为中文标签"""
        # Map dimension enum values to Chinese labels used in config
        mapping = {
            Dimension.CAREER: '事业',
            Dimension.HEALTH: '健康',
            Dimension.MARRIAGE: '婚姻',
            Dimension.WEALTH: '财富',
            Dimension.PERSONALITY: '性格',
            Dimension.FORTUNE: '运势',
            Dimension.OMEN: '预兆',
            Dimension.GUIDANCE: '指引',
            Dimension.UNCONSCIOUS: '潜意识',
            Dimension.GENERAL: '通用',
        }
        return mapping.get(dimension, dimension.value)
    
    def _load_logic_chains(self) -> Dict[str, Dict]:
        """加载LogicChain数据"""
        if self._logic_chains_cache is not None:
            return self._logic_chains_cache
        
        self._logic_chains_cache = {}
        
        if not self.logic_chains_dir.exists():
            logger.warning(f"Logic chains directory not found: {self.logic_chains_dir}")
            return self._logic_chains_cache
        
        for yaml_file in self.logic_chains_dir.glob("*.yaml"):
            if yaml_file.name.endswith('.bak') or 'quality' in yaml_file.name:
                continue
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data and 'book_id' in data:
                        self._logic_chains_cache[data['book_id']] = data
            except Exception as e:
                logger.warning(f"Failed to load {yaml_file}: {e}")
        
        return self._logic_chains_cache
    
    def _load_factor_namespaces(self) -> Set[str]:
        """加载因子命名空间"""
        if self._factor_namespaces_cache is not None:
            return self._factor_namespaces_cache
        
        self._factor_namespaces_cache = set()
        
        if not self.factor_namespace_path.exists():
            logger.warning(f"Factor namespace file not found: {self.factor_namespace_path}")
            return self._factor_namespaces_cache
        
        try:
            with open(self.factor_namespace_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data and 'namespaces' in data:
                    for ns in data['namespaces']:
                        prefix = ns.get('prefix', '')
                        if prefix:
                            self._factor_namespaces_cache.add(prefix)
        except Exception as e:
            logger.warning(f"Failed to load factor namespace: {e}")
        
        return self._factor_namespaces_cache
    
    def _infer_system_from_book(self, book_id: str) -> Optional[DivinationSystem]:
        """从book_id推断divination_system"""
        book_system_map = {
            '滴天髓': DivinationSystem.BAZI,
            '子平真诠': DivinationSystem.BAZI,
            '渊海子平': DivinationSystem.BAZI,
            '穷通宝鉴': DivinationSystem.BAZI,
            '三命通会': DivinationSystem.BAZI,
            '紫微斗数全书': DivinationSystem.ZIWEI,
            '周易': DivinationSystem.YIJING,
            '周公解梦': DivinationSystem.DREAM,
            '梦林玄解': DivinationSystem.DREAM,
        }
        
        # 英文书名
        if 'astro' in book_id.lower() or 'planet' in book_id.lower() or 'house' in book_id.lower():
            return DivinationSystem.ASTRO
        if 'tarot' in book_id.lower() or 'thoth' in book_id.lower():
            return DivinationSystem.TAROT
        if 'dream' in book_id.lower():
            return DivinationSystem.DREAM
        if 'archetype' in book_id.lower() or 'unconscious' in book_id.lower():
            return DivinationSystem.PSYCHOLOGY
        
        return book_system_map.get(book_id)
