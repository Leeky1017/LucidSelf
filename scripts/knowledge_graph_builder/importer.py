"""
L2.5数据导入器 - 从LogicChain导入数据到知识图谱

Feature: cross-book-knowledge-graph
Requirement Refs: Req 9.1, Req 9.2, Req 9.3
Design Refs: Design.md#模块结构

实现:
- 导入至少100个L2.5 LogicChain节点
- 提取概念和关系
- 支持增量导入
"""

import hashlib
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple, Union

import yaml

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    ConflictSummary,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.edge import (
    ConflictType,
    RelationType,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)

logger = logging.getLogger(__name__)


class L25Importer:
    """
    L2.5数据导入器
    
    从LogicChain YAML文件导入数据，创建ConceptNode和SemanticEdge。
    """
    
    # 体系映射
    BOOK_SYSTEM_MAP = {
        # 中文书
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
    
    # 维度映射（从节点标签推断）
    DIMENSION_KEYWORDS = {
        Dimension.CAREER: ['事业', '功名', '官', '职', 'career', 'work', 'profession'],
        Dimension.WEALTH: ['财', '富', '钱', 'wealth', 'money', 'finance'],
        Dimension.MARRIAGE: ['婚', '姻', '夫', '妻', '情', 'relationship', 'marriage', 'love'],
        Dimension.HEALTH: ['病', '疾', '寿', '健康', 'health', 'illness', 'disease'],
        Dimension.PERSONALITY: ['性格', '心性', '品', 'personality', 'character'],
        Dimension.FORTUNE: ['运', '吉凶', '祸福', 'fortune', 'luck'],
    }
    
    def __init__(
        self,
        logic_chains_dir: Optional[Union[str, Path]] = None,
        min_nodes: int = 100,
        factor_namespace_path: Optional[Union[str, Path]] = None,
    ):
        """
        初始化导入器
        
        Args:
            logic_chains_dir: LogicChain目录
            min_nodes: 最小导入节点数
            factor_namespace_path: 因子命名空间文件路径
        """
        self.logic_chains_dir = Path(logic_chains_dir) if logic_chains_dir else Path("data/logic_chains")
        self.min_nodes = min_nodes
        self.factor_namespace_path = Path(factor_namespace_path) if factor_namespace_path else Path("data/factor_ontology/namespace.yaml")
        
        # 状态
        self._imported_books: Set[str] = set()
        self._concept_cache: Dict[str, ConceptNode] = {}
        self._edge_cache: Dict[str, SemanticEdge] = {}
        self._valid_namespaces: Optional[Set[str]] = None
    
    def import_all(self, existing_graph: Optional[KnowledgeGraph] = None) -> KnowledgeGraph:
        """
        导入所有LogicChain数据
        
        Args:
            existing_graph: 现有图谱（用于增量导入）
            
        Returns:
            KnowledgeGraph
        """
        # 初始化或使用现有图谱
        if existing_graph:
            self._concept_cache = {c.concept_id: c for c in existing_graph.concepts}
            self._edge_cache = {e.edge_id: e for e in existing_graph.edges}
            self._imported_books = set(existing_graph.metadata.source_books)
        
        # 扫描并导入
        imported_count = 0
        for yaml_file in self._iter_logic_chain_files():
            try:
                book_data = self._load_yaml(yaml_file)
                if not book_data:
                    continue
                
                book_id = book_data.get('book_id', yaml_file.stem)
                
                # 跳过已导入的书
                if book_id in self._imported_books:
                    continue
                
                # 导入节点
                nodes = book_data.get('nodes', [])
                for node in nodes:
                    concept = self._node_to_concept(node, book_id)
                    if concept:
                        self._merge_concept(concept)
                        imported_count += 1
                
                # 导入关系（从edges字段或节点间推断）
                edges = book_data.get('edges', [])
                for edge_data in edges:
                    edge = self._edge_data_to_edge(edge_data, book_id)
                    if edge:
                        self._add_edge(edge)
                
                self._imported_books.add(book_id)
                logger.info(f"Imported {len(nodes)} nodes from {book_id}")
                
            except Exception as e:
                logger.warning(f"Failed to import {yaml_file}: {e}")
        
        # 检查最小节点数
        if imported_count < self.min_nodes:
            logger.warning(f"Only imported {imported_count} nodes, less than minimum {self.min_nodes}")
        
        # 构建图谱
        return self._build_graph()
    
    def import_book(self, book_id: str) -> Tuple[List[ConceptNode], List[SemanticEdge]]:
        """
        导入单本书
        
        Args:
            book_id: 书籍ID
            
        Returns:
            (concepts, edges)
        """
        concepts = []
        edges = []
        
        for yaml_file in self._iter_logic_chain_files():
            book_data = self._load_yaml(yaml_file)
            if not book_data:
                continue
            
            if book_data.get('book_id') != book_id:
                continue
            
            nodes = book_data.get('nodes', [])
            for node in nodes:
                concept = self._node_to_concept(node, book_id)
                if concept:
                    concepts.append(concept)
            
            edge_data_list = book_data.get('edges', [])
            for edge_data in edge_data_list:
                edge = self._edge_data_to_edge(edge_data, book_id)
                if edge:
                    edges.append(edge)
            
            break
        
        return concepts, edges
    
    def _iter_logic_chain_files(self) -> Iterator[Path]:
        """遍历LogicChain文件"""
        if not self.logic_chains_dir.exists():
            logger.warning(f"LogicChain directory not found: {self.logic_chains_dir}")
            return
        
        for yaml_file in sorted(self.logic_chains_dir.glob("**/*.yaml")):
            if yaml_file.name.endswith('.bak'):
                continue
            if 'quality' in yaml_file.name.lower():
                continue
            yield yaml_file
    
    def _load_yaml(self, path: Path) -> Optional[Dict]:
        """加载YAML文件"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.debug(f"Failed to load {path}: {e}")
            return None
    
    def _node_to_concept(self, node: Dict[str, Any], book_id: str) -> Optional[ConceptNode]:
        """将LogicChain节点转换为ConceptNode"""
        try:
            node_id = node.get('node_id', '')
            if not node_id:
                return None
            
            # 提取标签
            label_zh = node.get('label_zh') or node.get('label') or node.get('name', '')
            if not label_zh:
                return None
            
            # 生成concept_id
            system = self._infer_system(book_id)
            system_prefix = system.value if system else 'general'
            concept_id = self._generate_concept_id(system_prefix, label_zh)
            
            # 推断维度
            dimension = self._infer_dimension(label_zh, node)
            
            # 提取因子引用
            factor_refs = node.get('factor_refs', [])
            if isinstance(factor_refs, str):
                factor_refs = [factor_refs]
            
            return ConceptNode(
                concept_id=concept_id,
                canonical_label_zh=label_zh,
                canonical_label_en=node.get('label_en'),
                divination_system=system or DivinationSystem.CROSS_SYSTEM,
                dimension=dimension,
                source_nodes=[
                    SourceNodeRef(
                        book_id=book_id,
                        node_id=node_id,
                        snippet_ids=node.get('snippet_ids', []),
                    )
                ],
                factor_refs=factor_refs,
                authority_score=node.get('authority_score', 0.5),
            )
        except Exception as e:
            logger.debug(f"Failed to convert node: {e}")
            return None
    
    def _edge_data_to_edge(self, edge_data: Dict[str, Any], book_id: str) -> Optional[SemanticEdge]:
        """将边数据转换为SemanticEdge"""
        try:
            source_id = edge_data.get('source_id') or edge_data.get('source')
            target_id = edge_data.get('target_id') or edge_data.get('target')
            
            if not source_id or not target_id:
                return None
            
            # 查找对应的concept_id
            source_concept_id = self._find_concept_id_by_node(source_id, book_id)
            target_concept_id = self._find_concept_id_by_node(target_id, book_id)
            
            if not source_concept_id or not target_concept_id:
                return None
            
            # 解析关系类型
            rel_str = edge_data.get('relation_type', 'entails')
            try:
                relation_type = RelationType(rel_str)
            except ValueError:
                relation_type = RelationType.ENTAILS
            
            edge_id = self._generate_edge_id(source_concept_id, target_concept_id, relation_type)
            
            return SemanticEdge(
                edge_id=edge_id,
                source_concept_id=source_concept_id,
                target_concept_id=target_concept_id,
                relation_type=relation_type,
                confidence=edge_data.get('confidence', 0.7),
            )
        except Exception as e:
            logger.debug(f"Failed to convert edge: {e}")
            return None
    
    def _infer_system(self, book_id: str) -> Optional[DivinationSystem]:
        """从book_id推断体系"""
        # 直接映射
        if book_id in self.BOOK_SYSTEM_MAP:
            return self.BOOK_SYSTEM_MAP[book_id]
        
        # 关键词匹配
        book_lower = book_id.lower()
        if any(k in book_lower for k in ['bazi', '八字', '命理']):
            return DivinationSystem.BAZI
        if any(k in book_lower for k in ['ziwei', '紫微']):
            return DivinationSystem.ZIWEI
        if any(k in book_lower for k in ['astro', 'planet', 'house', 'zodiac']):
            return DivinationSystem.ASTRO
        if any(k in book_lower for k in ['tarot', '塔罗']):
            return DivinationSystem.TAROT
        if any(k in book_lower for k in ['dream', '梦', '解梦']):
            return DivinationSystem.DREAM
        if any(k in book_lower for k in ['yijing', '周易', '易经']):
            return DivinationSystem.YIJING
        
        return None
    
    def _infer_dimension(self, label: str, node: Dict) -> Dimension:
        """推断维度"""
        # 从节点显式字段
        if 'dimension' in node:
            try:
                return Dimension(node['dimension'])
            except ValueError:
                pass
        
        # 从标签关键词推断
        label_lower = label.lower()
        for dim, keywords in self.DIMENSION_KEYWORDS.items():
            if any(k in label_lower for k in keywords):
                return dim
        
        return Dimension.GENERAL
    
    def _generate_concept_id(self, system_prefix: str, label: str) -> str:
        """生成concept_id"""
        # 使用标签的哈希
        label_hash = hashlib.md5(label.encode()).hexdigest()[:8]
        return f"concept_{system_prefix}_{label_hash}"
    
    def _generate_edge_id(
        self,
        source_id: str,
        target_id: str,
        relation_type: RelationType,
    ) -> str:
        """生成edge_id"""
        combined = f"{source_id}_{target_id}_{relation_type.value}"
        edge_hash = hashlib.md5(combined.encode()).hexdigest()[:8]
        return f"edge_{relation_type.value}_{edge_hash}"
    
    def _find_concept_id_by_node(self, node_id: str, book_id: str) -> Optional[str]:
        """通过node_id查找concept_id"""
        for concept in self._concept_cache.values():
            for source in concept.source_nodes:
                if source.book_id == book_id and source.node_id == node_id:
                    return concept.concept_id
        return None
    
    def _merge_concept(self, concept: ConceptNode) -> None:
        """合并概念（相同ID的合并来源）"""
        if concept.concept_id in self._concept_cache:
            existing = self._concept_cache[concept.concept_id]
            # 合并source_nodes
            existing_sources = {(s.book_id, s.node_id) for s in existing.source_nodes}
            for source in concept.source_nodes:
                if (source.book_id, source.node_id) not in existing_sources:
                    existing.source_nodes.append(source)
            # 更新权威性（取最大值）
            existing.authority_score = max(existing.authority_score, concept.authority_score)
        else:
            self._concept_cache[concept.concept_id] = concept
    
    def _add_edge(self, edge: SemanticEdge) -> None:
        """添加边"""
        if edge.edge_id not in self._edge_cache:
            self._edge_cache[edge.edge_id] = edge
    
    def _build_graph(self) -> KnowledgeGraph:
        """构建最终图谱"""
        # Generate cross-system edges before building final graph
        cross_system_edges = self._generate_cross_system_edges()
        for edge in cross_system_edges:
            self._add_edge(edge)
        
        metadata = GraphMetadata(
            version="1.0.0",
            build_timestamp=datetime.now(),
            source_books=list(self._imported_books),
            total_concepts=len(self._concept_cache),
            total_edges=len(self._edge_cache),
        )
        
        return KnowledgeGraph(
            metadata=metadata,
            concepts=list(self._concept_cache.values()),
            edges=list(self._edge_cache.values()),
        )
    
    def _generate_cross_system_edges(self) -> List[SemanticEdge]:
        """
        Generate cross-system edges from L2.5 contracts:
        - cross_system_equivalent: concepts from different systems with shared factors
        - entails: logical entailment relationships
        - conflicts_with: contradictory concepts
        
        Requirement Refs: Req 9.x
        """
        edges = []
        concepts = list(self._concept_cache.values())
        
        # Build factor index for finding related concepts
        factor_to_concepts: Dict[str, List[ConceptNode]] = defaultdict(list)
        for concept in concepts:
            for factor in concept.factor_refs:
                factor_to_concepts[factor].append(concept)
        
        # Find cross-system equivalents (concepts with significant factor overlap)
        processed_pairs: Set[Tuple[str, str]] = set()
        
        for concept in concepts:
            # Find other concepts with shared factors
            related_concepts: Dict[str, int] = defaultdict(int)
            for factor in concept.factor_refs:
                for other in factor_to_concepts[factor]:
                    if other.concept_id != concept.concept_id:
                        related_concepts[other.concept_id] += 1
            
            for other_id, shared_count in related_concepts.items():
                pair_key = tuple(sorted([concept.concept_id, other_id]))
                if pair_key in processed_pairs:
                    continue
                processed_pairs.add(pair_key)
                
                other = self._concept_cache.get(other_id)
                if not other:
                    continue
                
                # Calculate overlap ratio
                if not concept.factor_refs or not other.factor_refs:
                    continue
                    
                min_factors = min(len(concept.factor_refs), len(other.factor_refs))
                overlap_ratio = shared_count / min_factors if min_factors > 0 else 0
                
                # Cross-system equivalent: different systems, high overlap
                if (concept.divination_system != other.divination_system 
                    and overlap_ratio >= 0.5):
                    edges.append(SemanticEdge(
                        edge_id=self._generate_edge_id(
                            concept.concept_id, other_id, RelationType.CROSS_SYSTEM_EQUIVALENT
                        ),
                        source_concept_id=concept.concept_id,
                        target_concept_id=other_id,
                        relation_type=RelationType.CROSS_SYSTEM_EQUIVALENT,
                        confidence=min(0.9, overlap_ratio),
                        bidirectional=True,
                    ))
                
                # Same-system entails: same system, one is more specific
                elif (concept.divination_system == other.divination_system
                      and overlap_ratio >= 0.7
                      and len(concept.factor_refs) > len(other.factor_refs) * 1.5):
                    edges.append(SemanticEdge(
                        edge_id=self._generate_edge_id(
                            other_id, concept.concept_id, RelationType.ENTAILS
                        ),
                        source_concept_id=other_id,
                        target_concept_id=concept.concept_id,
                        relation_type=RelationType.ENTAILS,
                        confidence=overlap_ratio * 0.8,
                    ))
        
        logger.info(f"Generated {len(edges)} cross-system edges")
        return edges
    
    def _load_valid_namespaces(self) -> Set[str]:
        """Load valid factor namespace prefixes"""
        if self._valid_namespaces is not None:
            return self._valid_namespaces
        
        self._valid_namespaces = set()
        
        if not self.factor_namespace_path.exists():
            logger.warning(f"Factor namespace file not found: {self.factor_namespace_path}")
            return self._valid_namespaces
        
        try:
            with open(self.factor_namespace_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data and 'namespaces' in data:
                    for ns in data['namespaces']:
                        prefix = ns.get('prefix', '')
                        if prefix:
                            self._valid_namespaces.add(prefix)
        except Exception as e:
            logger.warning(f"Failed to load factor namespace: {e}")
        
        return self._valid_namespaces
    
    def validate_factor_refs(
        self,
        factor_refs: List[str],
    ) -> Tuple[List[str], List[str]]:
        """
        Validate factor references against namespace.yaml
        
        Returns:
            (valid_refs, invalid_refs): Tuple of valid and invalid factor IDs
        """
        namespaces = self._load_valid_namespaces()
        if not namespaces:
            return factor_refs, []  # Can't validate without namespaces
        
        valid = []
        invalid = []
        
        for factor_id in factor_refs:
            # Check if matches any namespace prefix
            is_valid = any(factor_id.startswith(ns) for ns in namespaces)
            
            # Also accept common patterns
            if not is_valid and '_' in factor_id:
                prefix = factor_id.split('_')[0] + '_'
                is_valid = prefix in namespaces
            
            if is_valid:
                valid.append(factor_id)
            else:
                invalid.append(factor_id)
        
        return valid, invalid
