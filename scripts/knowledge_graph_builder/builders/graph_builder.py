"""
GraphBuilder - 图谱构建器基础框架

Feature: cross-book-knowledge-graph
Requirement Refs: Req 2.1, Req 5.1, Req 5.3, Req 5.8, Req 5.9
Design Refs: Design.md#构建器接口
"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from scripts.knowledge_graph_builder.models import (
    AggregationStrategy,
    ConceptAggregationRule,
    ConceptNode,
    DivinationSystem,
    GraphMetadata,
    KnowledgeGraph,
    LabelSelectionStrategy,
    SemanticEdge,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.builders.alignment import ConceptAligner, AlignmentThresholds
from scripts.knowledge_graph_builder.builders.aggregator import ConceptAggregator
from scripts.knowledge_graph_builder.builders.conflict_detector import ConflictDetector
from scripts.knowledge_graph_builder.builders.authority import AuthorityScorer

logger = logging.getLogger(__name__)


class LogicChainData:
    """LogicChain数据的轻量封装"""
    
    def __init__(self, book_id: str, file_path: Path, data: dict, file_hash: str):
        self.book_id = book_id
        self.file_path = file_path
        self.data = data
        self.file_hash = file_hash
        self.nodes: List[dict] = data.get('nodes', [])
        self.edges: List[dict] = data.get('edges', [])
        self.metadata: dict = data.get('metadata', {})
    
    @property
    def node_count(self) -> int:
        return len(self.nodes)
    
    @property
    def edge_count(self) -> int:
        return len(self.edges)
    
    @property
    def divination_system(self) -> str:
        """推断占卜体系"""
        return self.metadata.get('divination_system', 'unknown')
    
    @property
    def quality_metrics(self) -> dict:
        """获取质量指标"""
        return self.metadata.get('quality_metrics', {})


class BuildManifest:
    """构建清单 - 跟踪已处理的文件"""
    
    def __init__(self, manifest_path: Path):
        self.manifest_path = manifest_path
        self.data: dict = self._load()
    
    def _load(self) -> dict:
        if self.manifest_path.exists():
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        return {
            'last_build_time': None,
            'graph_version': '0.0.0',
            'processed_files': {},
            'alignment_stats': {},
            'conflict_stats': {},
            'manual_alignments': [],
        }
    
    def save(self) -> None:
        with open(self.manifest_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.data, f, allow_unicode=True, default_flow_style=False)
    
    def get_file_hash(self, book_id: str) -> Optional[str]:
        return self.data.get('processed_files', {}).get(book_id, {}).get('file_hash')
    
    def update_file(self, book_id: str, file_hash: str, node_count: int) -> None:
        if 'processed_files' not in self.data:
            self.data['processed_files'] = {}
        self.data['processed_files'][book_id] = {
            'file_hash': file_hash,
            'node_count': node_count,
            'last_modified': datetime.now().isoformat(),
        }
    
    def is_file_changed(self, book_id: str, current_hash: str) -> bool:
        stored_hash = self.get_file_hash(book_id)
        return stored_hash is None or stored_hash != current_hash
    
    def update_build_info(self, version: str) -> None:
        self.data['last_build_time'] = datetime.now().isoformat()
        self.data['graph_version'] = version
    
    def update_alignment_stats(self, total: int, same_system: int, cross_system: int) -> None:
        """Update alignment statistics"""
        self.data['alignment_stats'] = {
            'total_alignments': total,
            'same_system_alignments': same_system,
            'cross_system_alignments': cross_system,
            'last_updated': datetime.now().isoformat(),
        }
    
    def update_conflict_stats(self, total: int, by_type: Dict[str, int]) -> None:
        """Update conflict statistics"""
        self.data['conflict_stats'] = {
            'total_conflicts': total,
            'by_type': by_type,
            'last_updated': datetime.now().isoformat(),
        }
    
    def get_manual_alignments(self) -> List[Tuple[str, str]]:
        """Get manually preserved alignments"""
        return [(a['concept_a'], a['concept_b']) for a in self.data.get('manual_alignments', [])]
    
    def add_manual_alignment(self, concept_a_id: str, concept_b_id: str) -> None:
        """Record a manual alignment to preserve across rebuilds"""
        if 'manual_alignments' not in self.data:
            self.data['manual_alignments'] = []
        self.data['manual_alignments'].append({
            'concept_a': concept_a_id,
            'concept_b': concept_b_id,
            'created_at': datetime.now().isoformat(),
        })


class GraphBuilder:
    """
    图谱构建器 - 负责从LogicChain构建KnowledgeGraph
    
    职责：
    1. 扫描data/logic_chains/目录
    2. 解析LogicChain YAML文件
    3. 检测文件变更（增量构建）
    4. 协调对齐器、聚合器、冲突检测器
    5. 构建最终的KnowledgeGraph
    """
    
    # 质量阈值
    QUALITY_THRESHOLDS = {
        'reasoning_coherence': 0.7,
        'node_homogeneity': 0.5,
    }
    
    def __init__(
        self,
        logic_chains_dir: Path = Path('data/logic_chains'),
        knowledge_graph_dir: Path = Path('data/knowledge_graph'),
        authority_config_path: Optional[Path] = None,
    ):
        self.logic_chains_dir = logic_chains_dir
        self.knowledge_graph_dir = knowledge_graph_dir
        self.authority_config_path = authority_config_path or (
            knowledge_graph_dir / 'authority_config.yaml'
        )
        self.manifest = BuildManifest(knowledge_graph_dir / 'build_manifest.yaml')
        self._authority_weights: Optional[dict] = None
    
    @property
    def authority_weights(self) -> dict:
        """懒加载权威性权重配置"""
        if self._authority_weights is None:
            self._authority_weights = self._load_authority_weights()
        return self._authority_weights
    
    def _load_authority_weights(self) -> dict:
        """加载权威性权重配置"""
        if self.authority_config_path.exists():
            with open(self.authority_config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                return config.get('book_authority_weights', {})
        return {}
    
    def _compute_file_hash(self, file_path: Path) -> str:
        """计算文件MD5哈希"""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def _sanitize_id(self, raw_id: str) -> str:
        """
        将原始ID转换为符合regex ^[a-z0-9_]+$ 的格式
        
        - 中文字符转换为拼音首字母或hash
        - 特殊字符转换为下划线
        - 全部转小写
        """
        import re
        import unicodedata
        
        # 简单处理：非ASCII字符用其Unicode码点的hex表示
        result = []
        for char in raw_id.lower():
            if char.isascii() and (char.isalnum() or char == '_'):
                result.append(char)
            elif char in '-. ':
                result.append('_')
            elif not char.isascii():
                # 中文等字符：使用简单hash
                result.append(f"u{ord(char):04x}")
            else:
                result.append('_')
        
        sanitized = ''.join(result)
        # 合并连续下划线
        sanitized = re.sub(r'_+', '_', sanitized)
        # 移除首尾下划线
        sanitized = sanitized.strip('_')
        
        return sanitized if sanitized else 'unknown'
    
    def scan_logic_chains(self) -> List[Path]:
        """
        扫描logic_chains目录，获取所有有效的YAML文件
        排除.bak文件和非YAML文件
        """
        if not self.logic_chains_dir.exists():
            logger.warning(f"Logic chains directory not found: {self.logic_chains_dir}")
            return []
        
        yaml_files = []
        for f in self.logic_chains_dir.glob('*.yaml'):
            # 排除备份文件和失败文件
            if '.bak' in f.name or '.failed' in f.name:
                continue
            # 排除配置文件
            if f.name == 'book_quality_thresholds.yaml':
                continue
            yaml_files.append(f)
        
        logger.info(f"Found {len(yaml_files)} LogicChain files")
        return sorted(yaml_files)
    
    def _parse_logic_chain(self, file_path: Path) -> Optional[LogicChainData]:
        """解析单个LogicChain文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if not data:
                logger.warning(f"Empty LogicChain file: {file_path}")
                return None
            
            book_id = file_path.stem  # 文件名作为book_id
            file_hash = self._compute_file_hash(file_path)
            
            return LogicChainData(book_id, file_path, data, file_hash)
        except Exception as e:
            logger.error(f"Failed to parse LogicChain: {file_path}, error: {e}")
            return None
    
    def _check_quality_metrics(self, chain: LogicChainData) -> Tuple[bool, List[str]]:
        """
        检查质量指标是否满足阈值
        
        Returns:
            (passed, warnings): 是否通过及警告列表
        """
        warnings = []
        metrics = chain.quality_metrics
        
        if not metrics:
            return True, ["No quality metrics found"]
        
        reasoning_coherence = metrics.get('reasoning_coherence', 1.0)
        node_homogeneity = metrics.get('node_homogeneity', 1.0)
        
        if reasoning_coherence < self.QUALITY_THRESHOLDS['reasoning_coherence']:
            warnings.append(
                f"Low reasoning_coherence: {reasoning_coherence:.2f} < "
                f"{self.QUALITY_THRESHOLDS['reasoning_coherence']}"
            )
        
        if node_homogeneity < self.QUALITY_THRESHOLDS['node_homogeneity']:
            warnings.append(
                f"Low node_homogeneity: {node_homogeneity:.2f} < "
                f"{self.QUALITY_THRESHOLDS['node_homogeneity']}"
            )
        
        passed = len(warnings) == 0
        return passed, warnings
    
    def _infer_divination_system(self, book_id: str) -> DivinationSystem:
        """根据book_id推断占卜体系"""
        book_id_lower = book_id.lower()
        
        # 八字典籍
        bazi_books = {'滴天髓', '子平真诠', '穷通宝鉴', '三命通会', '渊海子平'}
        if book_id in bazi_books:
            return DivinationSystem.BAZI
        
        # 紫微典籍
        if '紫微' in book_id:
            return DivinationSystem.ZIWEI
        
        # 占星典籍
        astro_keywords = ['astro', 'planet', 'tetrabiblos', 'inner_sky', 'house']
        if any(kw in book_id_lower for kw in astro_keywords):
            return DivinationSystem.ASTRO
        
        # 塔罗典籍
        tarot_keywords = ['tarot', 'thoth', 'waite', 'degrees_of_wisdom']
        if any(kw in book_id_lower for kw in tarot_keywords):
            return DivinationSystem.TAROT
        
        # 解梦典籍
        dream_keywords = ['dream', '周公解梦', '梦林玄解']
        if any(kw in book_id_lower or kw in book_id for kw in dream_keywords):
            return DivinationSystem.DREAM
        
        # 周易
        if '周易' in book_id or 'yijing' in book_id_lower:
            return DivinationSystem.YIJING
        
        # 心理学
        if 'archetype' in book_id_lower or 'unconscious' in book_id_lower:
            return DivinationSystem.PSYCHOLOGY
        
        return DivinationSystem.CROSS_SYSTEM
    
    def get_changed_files(self) -> List[Path]:
        """获取自上次构建以来发生变更的文件"""
        all_files = self.scan_logic_chains()
        changed = []
        
        for file_path in all_files:
            book_id = file_path.stem
            current_hash = self._compute_file_hash(file_path)
            if self.manifest.is_file_changed(book_id, current_hash):
                changed.append(file_path)
        
        return changed
    
    def build_full(self, dry_run: bool = False) -> KnowledgeGraph:
        """
        全量构建图谱
        
        Args:
            dry_run: 如果为True，只报告变更但不应用
            
        Returns:
            构建的KnowledgeGraph
        """
        logger.info("Starting full build...")
        
        all_files = self.scan_logic_chains()
        chains: List[LogicChainData] = []
        
        for file_path in all_files:
            chain = self._parse_logic_chain(file_path)
            if chain:
                passed, warnings = self._check_quality_metrics(chain)
                if warnings:
                    for w in warnings:
                        logger.warning(f"[{chain.book_id}] {w}")
                chains.append(chain)
        
        if dry_run:
            logger.info(f"[DRY RUN] Would process {len(chains)} LogicChains")
            for chain in chains:
                logger.info(f"  - {chain.book_id}: {chain.node_count} nodes")
            # 返回空图谱
            return self._create_empty_graph()
        
        # 构建图谱
        graph = self._build_graph_from_chains(chains)
        
        # 更新构建清单
        for chain in chains:
            self.manifest.update_file(chain.book_id, chain.file_hash, chain.node_count)
        
        self.manifest.update_build_info(graph.metadata.version)
        self.manifest.save()
        
        logger.info(f"Full build complete: {len(graph.concepts)} concepts, {len(graph.edges)} edges")
        return graph
    
    def build_incremental(self, dry_run: bool = False) -> KnowledgeGraph:
        """
        增量构建图谱 - 只处理变更的文件
        
        Args:
            dry_run: 如果为True，只报告变更但不应用
        """
        logger.info("Starting incremental build...")
        
        changed_files = self.get_changed_files()
        deleted_books = self._detect_deleted_books()
        
        if not changed_files and not deleted_books:
            logger.info("No changes detected, skipping build")
            return self._load_existing_graph()
        
        logger.info(f"Detected {len(changed_files)} changed files, {len(deleted_books)} deleted books")
        
        if dry_run:
            logger.info("[DRY RUN] Changed files:")
            for f in changed_files:
                logger.info(f"  - {f.stem}")
            if deleted_books:
                logger.info("[DRY RUN] Deleted books (will be marked as orphaned):")
                for b in deleted_books:
                    logger.info(f"  - {b}")
            return self._load_existing_graph()
        
        # 加载现有图谱
        existing_graph = self._load_existing_graph()
        
        # 处理删除的书籍 - 标记为orphaned而非删除 (Req 5.7)
        self._mark_orphaned_concepts(existing_graph, deleted_books)
        
        # 处理变更的文件
        for file_path in changed_files:
            chain = self._parse_logic_chain(file_path)
            if chain:
                self._update_graph_with_chain(existing_graph, chain)
                self.manifest.update_file(chain.book_id, chain.file_hash, chain.node_count)
        
        # 更新版本
        self._increment_version(existing_graph)
        self.manifest.update_build_info(existing_graph.metadata.version)
        self.manifest.save()
        
        return existing_graph
    
    def _detect_deleted_books(self) -> List[str]:
        """检测已删除的书籍"""
        current_books = {f.stem for f in self.scan_logic_chains()}
        processed_books = set(self.manifest.data.get('processed_files', {}).keys())
        return list(processed_books - current_books)
    
    def _mark_orphaned_concepts(self, graph: KnowledgeGraph, deleted_books: List[str]) -> None:
        """
        将删除书籍的概念标记为orphaned而非删除 (Req 5.7)
        """
        for concept in graph.concepts:
            for source in concept.source_nodes:
                if source.book_id in deleted_books:
                    # 标记为orphaned（使用alignment_method字段）
                    concept.alignment_method = "orphaned"
                    logger.info(f"Marked concept {concept.concept_id} as orphaned (book {source.book_id} deleted)")
    
    def _create_empty_graph(self) -> KnowledgeGraph:
        """创建空图谱"""
        return KnowledgeGraph(
            metadata=GraphMetadata(
                version="0.1.0",
                build_timestamp=datetime.now(),
            )
        )
    
    def _load_existing_graph(self) -> KnowledgeGraph:
        """加载现有图谱，如不存在则创建空图谱"""
        try:
            from scripts.knowledge_graph_builder.persistence import GraphSerializer
            serializer = GraphSerializer()
            concepts_path = self.knowledge_graph_dir / 'concepts.yaml'
            if concepts_path.exists():
                return serializer.deserialize(self.knowledge_graph_dir)
        except Exception as e:
            logger.warning(f"Failed to load existing graph: {e}")
        return self._create_empty_graph()
    
    def _build_graph_from_chains(self, chains: List[LogicChainData]) -> KnowledgeGraph:
        """
        从LogicChain列表构建图谱
        
        完整构建管线:
        1. 提取原始概念 (per-node ConceptNodes)
        2. 对齐器: 发现跨书概念对齐
        3. 聚合器: 合并对齐的概念
        4. 冲突检测: 检测概念间冲突
        5. 权威性计算: 计算最终authority_score
        """
        raw_concepts: List[ConceptNode] = []
        edges: List[SemanticEdge] = []
        books_included: List[str] = []
        systems_covered: set = set()
        quality_metrics: Dict[str, Dict[str, float]] = {}
        
        # Step 1: Extract raw concepts from LogicChains
        for chain in chains:
            books_included.append(chain.book_id)
            system = self._infer_divination_system(chain.book_id)
            systems_covered.add(system)
            
            # Store quality metrics for authority calculation
            metrics = chain.quality_metrics
            if metrics:
                quality_metrics[chain.book_id] = {
                    'reasoning_coherence': metrics.get('reasoning_coherence', 0.8),
                    'node_homogeneity': metrics.get('node_homogeneity', 0.7),
                }
            
            # 为每个LogicNode创建初始ConceptNode
            for node in chain.nodes:
                node_id = node.get('node_id', '')
                if not node_id:
                    continue
                
                safe_book_id = self._sanitize_id(chain.book_id)
                safe_node_id = self._sanitize_id(node_id)
                
                concept = ConceptNode(
                    concept_id=f"concept_{safe_book_id}_{safe_node_id}",
                    canonical_label_zh=node.get('summary', node_id)[:50],
                    divination_system=system,
                    source_nodes=[
                        SourceNodeRef(
                            book_id=chain.book_id,
                            node_id=node_id,
                            snippet_ids=node.get('snippet_ids', []),
                        )
                    ],
                    factor_refs=node.get('factor_refs', []),
                    authority_score=self._compute_initial_authority(chain.book_id),
                    alignment_method="factor_overlap",
                )
                raw_concepts.append(concept)
        
        logger.info(f"Step 1: Extracted {len(raw_concepts)} raw concepts from {len(chains)} chains")
        
        # Step 2: Run ConceptAligner to find cross-book alignments
        aligner = ConceptAligner(thresholds=AlignmentThresholds())
        alignments = aligner.find_alignments(raw_concepts)
        
        # Update alignment stats in manifest
        same_system = sum(1 for a in alignments if a.is_same_system)
        cross_system = len(alignments) - same_system
        self.manifest.update_alignment_stats(
            total=len(alignments),
            same_system=same_system,
            cross_system=cross_system,
        )
        
        logger.info(f"Step 2: Found {len(alignments)} alignments ({same_system} same-system, {cross_system} cross-system)")
        
        # Step 3: Run ConceptAggregator to merge aligned concepts
        aggregation_rule = ConceptAggregationRule(
            rule_id="rule_default",
            name="默认聚合规则",
            aggregation_strategy=AggregationStrategy.MERGE_ALL,
            label_selection_strategy=LabelSelectionStrategy.HIGHEST_AUTHORITY,
        )
        aggregator = ConceptAggregator(default_rule=aggregation_rule)
        aggregated_concepts = aggregator.aggregate_concepts(raw_concepts, alignments)
        
        logger.info(f"Step 3: Aggregated to {len(aggregated_concepts)} concepts")
        
        # Step 4: Run ConflictDetector to detect conflicts
        conflict_detector = ConflictDetector()
        conflict_edges, conflict_outputs = conflict_detector.detect_conflicts(aggregated_concepts)
        conflict_detector.update_conflict_summaries(aggregated_concepts, conflict_edges)
        
        # Add conflict edges to edge list
        edges.extend(conflict_edges)
        
        # Update conflict stats in manifest
        conflict_types: Dict[str, int] = {}
        for edge in conflict_edges:
            if edge.conflict_type:
                type_name = edge.conflict_type.value
                conflict_types[type_name] = conflict_types.get(type_name, 0) + 1
        self.manifest.update_conflict_stats(total=len(conflict_edges), by_type=conflict_types)
        
        logger.info(f"Step 4: Detected {len(conflict_edges)} conflicts")
        
        # Step 5: Run AuthorityScorer to compute final authority scores
        authority_scorer = AuthorityScorer(
            authority_config_path=self.authority_config_path,
            quality_metrics=quality_metrics,
        )
        authority_scorer.update_concept_authorities(aggregated_concepts)
        
        logger.info(f"Step 5: Updated authority scores for {len(aggregated_concepts)} concepts")
        
        # Build final KnowledgeGraph
        graph = KnowledgeGraph(
            metadata=GraphMetadata(
                version="1.0.0",
                build_timestamp=datetime.now(),
                total_concepts=len(aggregated_concepts),
                total_edges=len(edges),
                books_included=sorted(books_included),
                systems_covered=sorted(list(systems_covered), key=lambda x: x.value),
            ),
            concepts=aggregated_concepts,
            edges=edges,
        )
        
        return graph
    
    def _compute_initial_authority(self, book_id: str) -> float:
        """计算初始权威性分数"""
        default_weight = self.authority_weights.get('_default', 0.7)
        book_weight = self.authority_weights.get(book_id, default_weight)
        
        # 初始分数只基于书籍权威性，后续会根据quality和source_count调整
        return book_weight * 0.5 + 0.5 * 0.5  # 假设初始quality=0.5
    
    def _update_graph_with_chain(self, graph: KnowledgeGraph, chain: LogicChainData) -> None:
        """
        增量更新图谱
        
        保留:
        - 手动对齐的概念 (alignment_method="manual")
        - 不受影响的概念和边
        
        更新:
        - 来自变更书籍的概念
        - 相关的边
        """
        # Get IDs of manual alignments to preserve
        manual_alignment_pairs = set(self.manifest.get_manual_alignments())
        
        # Collect concept IDs from this book that should be removed
        concepts_to_remove = set()
        for c in graph.concepts:
            is_from_book = any(s.book_id == chain.book_id for s in c.source_nodes)
            is_manual = c.alignment_method == "manual"
            
            # Also check if concept is part of a manual alignment pair
            is_in_manual_pair = any(
                c.concept_id in pair for pair in manual_alignment_pairs
            )
            
            if is_from_book and not is_manual and not is_in_manual_pair:
                concepts_to_remove.add(c.concept_id)
        
        # Remove outdated concepts (but preserve manually aligned)
        graph.concepts = [
            c for c in graph.concepts 
            if c.concept_id not in concepts_to_remove
        ]
        
        # Remove edges connected to removed concepts
        graph.edges = [
            e for e in graph.edges
            if e.source_concept_id not in concepts_to_remove 
            and e.target_concept_id not in concepts_to_remove
        ]
        
        # Add new concepts from the updated chain
        new_concepts: List[ConceptNode] = []
        system = self._infer_divination_system(chain.book_id)
        
        for node in chain.nodes:
            node_id = node.get('node_id', '')
            if not node_id:
                continue
            
            safe_book_id = self._sanitize_id(chain.book_id)
            safe_node_id = self._sanitize_id(node_id)
            
            concept = ConceptNode(
                concept_id=f"concept_{safe_book_id}_{safe_node_id}",
                canonical_label_zh=node.get('summary', node_id)[:50],
                divination_system=system,
                source_nodes=[
                    SourceNodeRef(
                        book_id=chain.book_id,
                        node_id=node_id,
                        snippet_ids=node.get('snippet_ids', []),
                    )
                ],
                factor_refs=node.get('factor_refs', []),
                authority_score=self._compute_initial_authority(chain.book_id),
            )
            new_concepts.append(concept)
        
        # Run alignment on new concepts against existing
        all_concepts = graph.concepts + new_concepts
        aligner = ConceptAligner(thresholds=AlignmentThresholds())
        alignments = aligner.find_alignments(all_concepts)
        
        # Filter to only include alignments involving new concepts
        new_concept_ids = {c.concept_id for c in new_concepts}
        relevant_alignments = [
            a for a in alignments
            if a.concept_a_id in new_concept_ids or a.concept_b_id in new_concept_ids
        ]
        
        # Aggregate
        aggregation_rule = ConceptAggregationRule(
            rule_id="rule_default",
            name="默认聚合规则",
            aggregation_strategy=AggregationStrategy.MERGE_ALL,
            label_selection_strategy=LabelSelectionStrategy.HIGHEST_AUTHORITY,
        )
        aggregator = ConceptAggregator(default_rule=aggregation_rule)
        graph.concepts = aggregator.aggregate_concepts(all_concepts, relevant_alignments)
        
        # Detect conflicts
        conflict_detector = ConflictDetector()
        conflict_edges, _ = conflict_detector.detect_conflicts(graph.concepts)
        conflict_detector.update_conflict_summaries(graph.concepts, conflict_edges)
        graph.edges.extend(conflict_edges)
        
        # Update authority scores
        authority_scorer = AuthorityScorer(authority_config_path=self.authority_config_path)
        authority_scorer.update_concept_authorities(graph.concepts)
        
        # Rebuild indices
        graph.build_indices()
        
        # Update metadata
        graph.metadata.total_concepts = len(graph.concepts)
        graph.metadata.total_edges = len(graph.edges)
    
    def _increment_version(self, graph: KnowledgeGraph) -> None:
        """增加版本号"""
        parts = graph.metadata.version.split('.')
        parts[-1] = str(int(parts[-1]) + 1)
        graph.metadata.version = '.'.join(parts)
        graph.metadata.build_timestamp = datetime.now()
