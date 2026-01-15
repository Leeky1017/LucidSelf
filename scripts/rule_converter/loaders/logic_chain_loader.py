"""
LogicChain Loader

加载和解析 LogicChain YAML 文件。

Feature: rule-converter
Requirement Refs: Req 1.1-1.8
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

logger = logging.getLogger(__name__)


@dataclass
class LogicChainNode:
    """
    LogicChain 逻辑节点
    
    对应 data/logic_chains/*.yaml 中的 nodes 列表元素
    """
    node_id: str
    snippet_ids: List[str] = field(default_factory=list)
    role: str = "主干"  # 主干/条件分支/例外处理/主干依赖/总结
    condition: Optional[str] = None
    summary: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    factor_refs: List[str] = field(default_factory=list)
    
    @property
    def source_ref(self) -> Optional[str]:
        """获取 source_ref"""
        return self.metadata.get("source_ref")
    
    @property
    def snippet_count(self) -> int:
        """获取 snippet_count"""
        return self.metadata.get("snippet_count", len(self.snippet_ids))
    
    @property
    def is_convertible(self) -> bool:
        """
        判断节点是否可转换为规则
        
        可转换条件：
        1. 有 factor_refs，或
        2. 有显式 condition
        """
        return bool(self.factor_refs) or bool(self.condition)


@dataclass
class LogicChainEdge:
    """
    LogicChain 关系边
    
    对应 data/logic_chains/*.yaml 中的 edges 列表元素
    """
    from_node: str
    to_node: str
    relation: str  # leads_to/supports/depends_on
    condition: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LogicChainData:
    """
    单个 LogicChain 文件的完整数据
    """
    chain_id: str
    book_id: str
    nodes: List[LogicChainNode] = field(default_factory=list)
    edges: List[LogicChainEdge] = field(default_factory=list)
    
    @property
    def convertible_nodes(self) -> List[LogicChainNode]:
        """获取可转换的节点"""
        return [n for n in self.nodes if n.is_convertible]
    
    @property
    def node_count(self) -> int:
        return len(self.nodes)
    
    @property
    def convertible_count(self) -> int:
        return len(self.convertible_nodes)
    
    @property
    def edge_count(self) -> int:
        return len(self.edges)


class LoaderError(Exception):
    """加载错误"""
    def __init__(self, message: str, file_path: Optional[Path] = None, line_number: Optional[int] = None):
        self.file_path = file_path
        self.line_number = line_number
        super().__init__(f"{message} (file: {file_path}, line: {line_number})")


class LogicChainLoader:
    """
    LogicChain 加载器
    
    从 data/logic_chains/ 目录加载所有 LogicChain YAML 文件。
    
    Requirement Refs: Req 1.1-1.8
    """
    
    DEFAULT_DIR = Path("data/logic_chains")
    SKIP_PATTERNS = [".bak", ".failed.yaml"]  # 后缀匹配
    
    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = Path(base_dir) if base_dir else self.DEFAULT_DIR
        self._chains: Dict[str, LogicChainData] = {}
        self._stats: Dict[str, int] = {
            "total_files": 0,
            "loaded_files": 0,
            "skipped_files": 0,
            "failed_files": 0,
            "total_nodes": 0,
            "nodes_with_factor_refs": 0,
            "convertible_nodes": 0,
            "total_edges": 0,
        }
    
    def load_file(self, path: Path) -> LogicChainData:
        """
        加载单个 LogicChain YAML 文件
        
        Args:
            path: YAML 文件路径
            
        Returns:
            LogicChainData
            
        Raises:
            LoaderError: 解析失败时
        """
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            
            if not data:
                raise LoaderError("Empty YAML file", path)
            
            # 解析基本信息
            chain_id = data.get("chain_id", f"chain_{path.stem}")
            book_id = data.get("book_id", path.stem)
            
            # 解析 nodes
            nodes = []
            for node_data in data.get("nodes", []):
                node = self._parse_node(node_data)
                nodes.append(node)
            
            # 解析 edges
            edges = []
            for edge_data in data.get("edges", []):
                edge = self._parse_edge(edge_data)
                edges.append(edge)
            
            return LogicChainData(
                chain_id=chain_id,
                book_id=book_id,
                nodes=nodes,
                edges=edges,
            )
            
        except yaml.YAMLError as e:
            line = getattr(e, "problem_mark", None)
            line_num = line.line + 1 if line else None
            raise LoaderError(f"YAML parse error: {e}", path, line_num)
        except Exception as e:
            if isinstance(e, LoaderError):
                raise
            raise LoaderError(f"Load error: {e}", path)
    
    def _parse_node(self, data: Dict[str, Any]) -> LogicChainNode:
        """解析单个节点"""
        return LogicChainNode(
            node_id=data.get("node_id", ""),
            snippet_ids=data.get("snippet_ids", []),
            role=data.get("role", "主干"),
            condition=data.get("condition"),
            summary=data.get("summary", ""),
            metadata=data.get("metadata", {}),
            factor_refs=data.get("factor_refs", []),
        )
    
    def _parse_edge(self, data: Dict[str, Any]) -> LogicChainEdge:
        """解析单条边"""
        return LogicChainEdge(
            from_node=data.get("from_node", ""),
            to_node=data.get("to_node", ""),
            relation=data.get("relation", "leads_to"),
            condition=data.get("condition"),
            metadata=data.get("metadata", {}),
        )
    
    def _should_skip(self, path: Path) -> bool:
        """判断是否应该跳过该文件"""
        name = path.name
        for suffix in self.SKIP_PATTERNS:
            if name.endswith(suffix):
                return True
        return False
    
    def load_all(self, directory: Optional[Path] = None) -> Dict[str, LogicChainData]:
        """
        批量加载目录下所有 LogicChain 文件
        
        Args:
            directory: 目录路径，默认使用 base_dir
            
        Returns:
            Dict[book_id, LogicChainData]
        """
        dir_path = Path(directory) if directory else self.base_dir
        
        if not dir_path.exists():
            logger.warning(f"Directory not found: {dir_path}")
            return {}
        
        self._chains.clear()
        self._reset_stats()
        
        yaml_files = list(dir_path.glob("*.yaml"))
        self._stats["total_files"] = len(yaml_files)
        
        for yaml_file in yaml_files:
            # 跳过备份和失败文件
            if self._should_skip(yaml_file):
                self._stats["skipped_files"] += 1
                logger.debug(f"Skipping: {yaml_file.name}")
                continue
            
            try:
                chain_data = self.load_file(yaml_file)
                self._chains[chain_data.book_id] = chain_data
                self._stats["loaded_files"] += 1
                
                # 更新统计
                self._stats["total_nodes"] += chain_data.node_count
                self._stats["total_edges"] += chain_data.edge_count
                self._stats["convertible_nodes"] += chain_data.convertible_count
                
                nodes_with_refs = sum(1 for n in chain_data.nodes if n.factor_refs)
                self._stats["nodes_with_factor_refs"] += nodes_with_refs
                
                logger.info(f"Loaded: {yaml_file.name} ({chain_data.node_count} nodes, {chain_data.edge_count} edges)")
                
            except LoaderError as e:
                self._stats["failed_files"] += 1
                logger.warning(f"Failed to load {yaml_file.name}: {e}")
        
        return self._chains
    
    def _reset_stats(self):
        """重置统计信息"""
        for key in self._stats:
            self._stats[key] = 0
    
    def get_chain(self, book_id: str) -> Optional[LogicChainData]:
        """获取指定书籍的 LogicChain"""
        return self._chains.get(book_id)
    
    def get_all_convertible_nodes(self) -> List[Tuple[str, LogicChainNode]]:
        """
        获取所有可转换的节点
        
        Returns:
            List[(book_id, node)]
        """
        result = []
        for book_id, chain in self._chains.items():
            for node in chain.convertible_nodes:
                result.append((book_id, node))
        return result
    
    @property
    def stats(self) -> Dict[str, int]:
        """获取统计信息"""
        return self._stats.copy()
    
    @property
    def chains(self) -> Dict[str, LogicChainData]:
        """获取所有已加载的 LogicChain"""
        return self._chains
    
    def __len__(self) -> int:
        return len(self._chains)
    
    def __iter__(self):
        return iter(self._chains.values())
