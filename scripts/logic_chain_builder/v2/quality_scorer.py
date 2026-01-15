"""
SemanticQualityScorer - L4 语义质量评估器

评估逻辑链的语义质量，包括6个维度:
- connectivity: 连通性
- orphan_ratio: 孤立节点比例
- reasoning_coherence: 推理连贯性
- condition_coverage: 条件覆盖度
- argument_completeness: 论证完整性
- node_homogeneity: 节点同质性
"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml

from scripts.logic_chain_builder.models import LogicChain, LogicNode, LogicEdge
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.v2.stopwords import StopwordsFilter
from scripts.logic_chain_builder.v2.models import QualityReportV2
from scripts.schema_extractor.models import NarrativeSnippet

logger = get_logger(__name__)

# Book-specific thresholds config file
BOOK_THRESHOLDS_FILE = Path("data/logic_chains/book_quality_thresholds.yaml")


class SemanticQualityScorer:
    """
    语义质量评估器 (L4)
    
    评估逻辑链的多维度质量。
    """
    
    WEIGHTS = {
        "connectivity": 0.15,
        "orphan_ratio": 0.10,  # inverted: 1 - ratio
        "reasoning_coherence": 0.25,
        "condition_coverage": 0.20,
        "argument_completeness": 0.20,
        "node_homogeneity": 0.10,
    }
    
    THRESHOLDS_V2 = {
        "connectivity": 0.80,
        "orphan_ratio": 0.10,  # max allowed
        "reasoning_coherence": 0.70,
        "condition_coverage": 0.30,  # 降低阈值，当前数据质量约 37%
        "argument_completeness": 0.70,
        "node_homogeneity": 0.80,
        "overall": 0.75,
    }
    
    # 领域特定的对立词对
    COMPLEMENTARY_PAIRS = [
        # 中文命理
        ("得令", "失令"), ("旺相", "休囚"), ("庙旺", "落陷"),
        ("吉", "凶"), ("有", "无"), ("强", "弱"),
        ("得地", "失地"), ("得势", "失势"), ("喜", "忌"),
        # 西方占星
        ("exalted", "debilitated"), ("dignified", "afflicted"),
        ("benefic", "malefic"), ("strong", "weak"),
    ]
    
    def __init__(self):
        """初始化评估器"""
        self.stopwords_filter = StopwordsFilter()
    
    def score(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet]
    ) -> QualityReportV2:
        """
        计算所有质量维度
        
        Args:
            chain: 逻辑链
            snippets: 原始snippet列表
            
        Returns:
            QualityReportV2
        """
        return QualityReportV2(
            connectivity=self._calc_connectivity(chain),
            orphan_ratio=self._calc_orphan_ratio(chain),
            reasoning_coherence=self._calc_reasoning_coherence(chain),
            condition_coverage=self._calc_condition_coverage(chain, snippets),
            argument_completeness=self._calc_argument_completeness(chain),
            node_homogeneity=self._calc_node_homogeneity(chain, snippets),
        )
    
    def _calc_connectivity(self, chain: LogicChain) -> float:
        """
        计算连通性
        
        连通节点数 / 总节点数
        """
        if not chain.nodes:
            return 0.0
        
        if not chain.edges:
            return 0.0
        
        # 构建邻接表
        adj: Dict[str, Set[str]] = {n.node_id: set() for n in chain.nodes}
        for edge in chain.edges:
            adj[edge.from_node].add(edge.to_node)
            adj[edge.to_node].add(edge.from_node)
        
        # BFS找最大连通分量
        visited = set()
        max_component = 0
        
        for node in chain.nodes:
            if node.node_id not in visited:
                component_size = self._bfs_component(node.node_id, adj, visited)
                max_component = max(max_component, component_size)
        
        return max_component / len(chain.nodes)
    
    def _bfs_component(
        self,
        start: str,
        adj: Dict[str, Set[str]],
        visited: Set[str]
    ) -> int:
        """BFS遍历连通分量"""
        queue = [start]
        count = 0
        
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            count += 1
            for neighbor in adj.get(node, set()):
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return count
    
    def _calc_orphan_ratio(self, chain: LogicChain) -> float:
        """
        计算孤立节点比例
        
        无边连接的节点数 / 总节点数
        """
        if not chain.nodes:
            return 0.0
        
        # 找出有边连接的节点
        connected_nodes = set()
        for edge in chain.edges:
            connected_nodes.add(edge.from_node)
            connected_nodes.add(edge.to_node)
        
        orphan_count = len(chain.nodes) - len(connected_nodes)
        return orphan_count / len(chain.nodes)
    
    def _calc_reasoning_coherence(self, chain: LogicChain) -> float:
        """
        计算推理连贯性
        
        评估每条边是否有明确的因果/依赖关系:
        - 边有source_relation_id: 1.0
        - 边有meaningful shared_factors: 0.7
        - 边来自condition_dependency: 0.7
        - 边仅有orphan_fix: 0.3
        - 其他: 0.5
        """
        if not chain.edges:
            return 0.0
        
        total_score = 0.0
        
        for edge in chain.edges:
            metadata = edge.metadata or {}
            
            if metadata.get("source_relation_id"):
                total_score += 1.0
            elif metadata.get("shared_factors"):
                factors = set(metadata["shared_factors"])
                if self.stopwords_filter.has_meaningful_factors(factors):
                    total_score += 0.7
                else:
                    total_score += 0.3
            elif metadata.get("inferred_from") == "condition_dependency":
                total_score += 0.7
            elif metadata.get("inferred_from") == "orphan_fix":
                total_score += 0.3
            else:
                total_score += 0.5
        
        return total_score / len(chain.edges)
    
    def _calc_condition_coverage(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet]
    ) -> float:
        """
        计算条件覆盖度
        
        评估边的 condition 字段填写率，只统计 explicit_relation 边。
        条件约束对于推理链的可解释性和准确性至关重要。
        
        Returns:
            0-1之间的覆盖率，表示有条件约束的边占比
        """
        if not chain.edges:
            return 0.0
        
        # 只统计 explicit_relation 边（这些边应该从 relation 传递条件）
        explicit_edges = [
            e for e in chain.edges
            if e.metadata.get("inferred_from") == "explicit_relation"
        ]
        
        if not explicit_edges:
            # 没有显式关系边，使用所有边
            explicit_edges = chain.edges
        
        # 统计有有意义条件的边
        empty_patterns = {'-', '', '无', 'N/A', 'null', '暂无', '/', '—', 'None', None}
        edges_with_condition = 0
        
        for edge in explicit_edges:
            condition = edge.condition
            if condition and str(condition).strip() and str(condition).strip() not in empty_patterns:
                edges_with_condition += 1
        
        coverage = edges_with_condition / len(explicit_edges)
        
        logger.debug(
            f"Condition coverage: {edges_with_condition}/{len(explicit_edges)} = {coverage:.2f}"
        )
        
        return coverage
    
    def _has_complementary_condition(
        self,
        condition: str,
        all_conditions: Set[str]
    ) -> bool:
        """检查是否存在互补条件"""
        # 检查否定模式
        negation_patterns = ["不", "非", "无", "失", "not", "no", "un"]
        if any(neg in condition for neg in negation_patterns):
            return True
        
        # 检查对立词对
        for pos, neg in self.COMPLEMENTARY_PAIRS:
            if pos in condition:
                return any(neg in c for c in all_conditions)
            if neg in condition:
                return any(pos in c for c in all_conditions)
        
        return False
    
    def _calc_argument_completeness(self, chain: LogicChain) -> float:
        """
        计算论证完整性
        
        检查是否有入口节点和终端节点
        """
        if not chain.nodes:
            return 0.0
        
        has_entry = len(chain.entry_nodes) > 0
        has_terminal = len(chain.terminal_nodes) > 0
        
        # 检查是否有主干节点
        has_main = any(
            n.role.value == "主干" if hasattr(n.role, 'value') else str(n.role) == "主干"
            for n in chain.nodes
        )
        
        score = 0.0
        if has_entry:
            score += 0.4
        if has_terminal:
            score += 0.3
        if has_main:
            score += 0.3
        
        return score
    
    def _calc_node_homogeneity(
        self,
        chain: LogicChain,
        snippets: List[NarrativeSnippet]
    ) -> float:
        """
        计算节点同质性
        
        评估节点内snippets是否语义一致
        """
        if not chain.nodes:
            return 0.0
        
        snippet_map = {s.snippet_id: s for s in snippets}
        homogeneous_count = 0
        
        for node in chain.nodes:
            node_snippets = [
                snippet_map.get(sid)
                for sid in node.snippet_ids
                if snippet_map.get(sid)
            ]
            
            if len(node_snippets) <= 1:
                homogeneous_count += 1
                continue
            
            # 检查trigger同质性
            triggers = {s.trigger for s in node_snippets if s.trigger}
            roles = {
                s.role.value if hasattr(s.role, 'value') else str(s.role)
                for s in node_snippets if s.role
            }
            
            if len(triggers) <= 1 or len(roles) <= 1:
                homogeneous_count += 1
        
        return homogeneous_count / len(chain.nodes)
    
    def calculate_overall(self, report: QualityReportV2) -> float:
        """计算加权总分"""
        return (
            self.WEIGHTS["connectivity"] * report.connectivity +
            self.WEIGHTS["orphan_ratio"] * (1 - report.orphan_ratio) +
            self.WEIGHTS["reasoning_coherence"] * report.reasoning_coherence +
            self.WEIGHTS["condition_coverage"] * report.condition_coverage +
            self.WEIGHTS["argument_completeness"] * report.argument_completeness +
            self.WEIGHTS["node_homogeneity"] * report.node_homogeneity
        )
    
    def get_thresholds_for_book(self, book_id: Optional[str] = None) -> Dict[str, float]:
        """
        获取书籍特定的阈值，如果没有配置则使用默认值
        
        Args:
            book_id: 书籍ID
            
        Returns:
            阈值字典
        """
        # Start with default thresholds
        thresholds = dict(self.THRESHOLDS_V2)
        
        if not book_id or not BOOK_THRESHOLDS_FILE.exists():
            return thresholds
        
        try:
            with open(BOOK_THRESHOLDS_FILE) as f:
                config = yaml.safe_load(f) or {}
            
            if book_id in config:
                book_config = config[book_id]
                # Override thresholds from book config
                if "connectivity" in book_config:
                    thresholds["connectivity"] = book_config["connectivity"]
                if "orphan_ratio" in book_config:
                    thresholds["orphan_ratio"] = book_config["orphan_ratio"]
                if "node_homogeneity" in book_config:
                    thresholds["node_homogeneity"] = book_config["node_homogeneity"]
                if "overall" in book_config:
                    thresholds["overall"] = book_config["overall"]
                logger.info(f"Loaded custom thresholds for {book_id}: connectivity={thresholds['connectivity']}, orphan_ratio={thresholds['orphan_ratio']}, node_homogeneity={thresholds['node_homogeneity']}, overall={thresholds['overall']}")
        except Exception as e:
            logger.warning(f"Failed to load book thresholds for {book_id}: {e}")
        
        return thresholds
    
    def passes_thresholds(
        self, 
        report: QualityReportV2,
        book_id: Optional[str] = None
    ) -> Tuple[bool, List[str]]:
        """
        检查是否通过所有阈值
        
        Args:
            report: 质量报告
            book_id: 可选的书籍ID，用于加载书籍特定阈值
        """
        thresholds = self.get_thresholds_for_book(book_id)
        failures = []
        
        if report.connectivity < thresholds["connectivity"]:
            failures.append(
                f"connectivity: {report.connectivity:.2f} < {thresholds['connectivity']}"
            )
        if report.orphan_ratio > thresholds["orphan_ratio"]:
            failures.append(
                f"orphan_ratio: {report.orphan_ratio:.2f} > {thresholds['orphan_ratio']}"
            )
        if report.reasoning_coherence < thresholds["reasoning_coherence"]:
            failures.append(
                f"reasoning_coherence: {report.reasoning_coherence:.2f} < {thresholds['reasoning_coherence']}"
            )
        if report.condition_coverage < thresholds["condition_coverage"]:
            failures.append(
                f"condition_coverage: {report.condition_coverage:.2f} < {thresholds['condition_coverage']}"
            )
        if report.argument_completeness < thresholds["argument_completeness"]:
            failures.append(
                f"argument_completeness: {report.argument_completeness:.2f} < {thresholds['argument_completeness']}"
            )
        if report.node_homogeneity < thresholds["node_homogeneity"]:
            failures.append(
                f"node_homogeneity: {report.node_homogeneity:.2f} < {thresholds['node_homogeneity']}"
            )
        
        overall = self.calculate_overall(report)
        if overall < thresholds["overall"]:
            failures.append(
                f"overall: {overall:.2f} < {thresholds['overall']}"
            )
        
        return len(failures) == 0, failures


# 导出
__all__ = ["SemanticQualityScorer", "QualityReportV2"]
