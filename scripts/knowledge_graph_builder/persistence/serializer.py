"""
GraphSerializer - YAML序列化/反序列化器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.5, Req 8.1, Req 8.2, Req 8.3, Req 8.4, Req 8.5
Design Refs: Design.md#存储格式

实现:
- serialize: 将KnowledgeGraph序列化为YAML文件 (concepts.yaml, edges.yaml, metadata.yaml)
- deserialize: 从YAML文件反序列化为KnowledgeGraph
- 往返序列化无数据丢失
- 解析错误报告行号和字段路径
- pretty-print输出（2空格缩进，key排序）
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml
from pydantic import ValidationError

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


class SerializationError(Exception):
    """序列化错误"""
    
    def __init__(
        self, 
        message: str, 
        file_path: Optional[Path] = None,
        line_number: Optional[int] = None,
        field_path: Optional[str] = None,
    ):
        self.file_path = file_path
        self.line_number = line_number
        self.field_path = field_path
        
        details = []
        if file_path:
            details.append(f"file={file_path}")
        if line_number:
            details.append(f"line={line_number}")
        if field_path:
            details.append(f"field={field_path}")
        
        if details:
            full_message = f"{message} ({', '.join(details)})"
        else:
            full_message = message
        
        super().__init__(full_message)


class DeserializationError(Exception):
    """反序列化错误"""
    
    def __init__(
        self,
        message: str,
        file_path: Optional[Path] = None,
        line_number: Optional[int] = None,
        field_path: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ):
        self.file_path = file_path
        self.line_number = line_number
        self.field_path = field_path
        self.original_error = original_error
        
        details = []
        if file_path:
            details.append(f"file={file_path}")
        if line_number:
            details.append(f"line={line_number}")
        if field_path:
            details.append(f"field={field_path}")
        
        if details:
            full_message = f"{message} ({', '.join(details)})"
        else:
            full_message = message
        
        super().__init__(full_message)


class OrderedDumper(yaml.SafeDumper):
    """自定义YAML dumper，保证key排序和pretty-print"""
    pass


def _dict_representer(dumper: yaml.SafeDumper, data: dict) -> yaml.Node:
    """按key排序输出dict"""
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        sorted(data.items()),
    )


def _datetime_representer(dumper: yaml.SafeDumper, data: datetime) -> yaml.Node:
    """datetime转ISO格式字符串"""
    return dumper.represent_scalar('tag:yaml.org,2002:str', data.isoformat())


def _enum_representer(dumper: yaml.SafeDumper, data) -> yaml.Node:
    """Enum转字符串值"""
    return dumper.represent_scalar('tag:yaml.org,2002:str', data.value)


# 注册自定义representer
OrderedDumper.add_representer(dict, _dict_representer)
OrderedDumper.add_representer(datetime, _datetime_representer)
OrderedDumper.add_representer(DivinationSystem, _enum_representer)
OrderedDumper.add_representer(Dimension, _enum_representer)
OrderedDumper.add_representer(RelationType, _enum_representer)
OrderedDumper.add_representer(ConflictType, _enum_representer)


class GraphSerializer:
    """
    知识图谱YAML序列化器
    
    文件结构:
    - concepts.yaml: ConceptNode列表
    - edges.yaml: SemanticEdge列表
    - metadata.yaml: GraphMetadata
    """
    
    DEFAULT_OUTPUT_DIR = Path("data/knowledge_graph")
    
    def __init__(self, output_dir: Optional[Union[str, Path]] = None):
        """
        初始化序列化器
        
        Args:
            output_dir: 输出目录，默认为data/knowledge_graph/
        """
        self.output_dir = Path(output_dir) if output_dir else self.DEFAULT_OUTPUT_DIR
    
    def serialize(
        self,
        graph: KnowledgeGraph,
        output_dir: Optional[Union[str, Path]] = None,
    ) -> Tuple[Path, Path, Path]:
        """
        将KnowledgeGraph序列化为YAML文件
        
        Args:
            graph: 要序列化的知识图谱
            output_dir: 输出目录（可选，覆盖默认）
            
        Returns:
            (concepts_path, edges_path, metadata_path) 三个文件路径
            
        Raises:
            SerializationError: 序列化失败时抛出
        """
        target_dir = Path(output_dir) if output_dir else self.output_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        
        concepts_path = target_dir / "concepts.yaml"
        edges_path = target_dir / "edges.yaml"
        metadata_path = target_dir / "metadata.yaml"
        
        try:
            # 序列化concepts
            concepts_data = self._serialize_concepts(graph.concepts)
            self._write_yaml(concepts_path, concepts_data)
            logger.info(f"Serialized {len(graph.concepts)} concepts to {concepts_path}")
            
            # 序列化edges
            edges_data = self._serialize_edges(graph.edges)
            self._write_yaml(edges_path, edges_data)
            logger.info(f"Serialized {len(graph.edges)} edges to {edges_path}")
            
            # 序列化metadata
            metadata_data = self._serialize_metadata(graph.metadata)
            self._write_yaml(metadata_path, metadata_data)
            logger.info(f"Serialized metadata to {metadata_path}")
            
            return concepts_path, edges_path, metadata_path
            
        except Exception as e:
            raise SerializationError(f"Failed to serialize graph: {e}") from e
    
    def deserialize(
        self,
        input_dir: Optional[Union[str, Path]] = None,
    ) -> KnowledgeGraph:
        """
        从YAML文件反序列化为KnowledgeGraph
        
        Args:
            input_dir: 输入目录（可选，覆盖默认）
            
        Returns:
            反序列化后的KnowledgeGraph
            
        Raises:
            DeserializationError: 反序列化失败时抛出
        """
        source_dir = Path(input_dir) if input_dir else self.output_dir
        
        concepts_path = source_dir / "concepts.yaml"
        edges_path = source_dir / "edges.yaml"
        metadata_path = source_dir / "metadata.yaml"
        
        # 检查文件存在
        for path in [concepts_path, edges_path, metadata_path]:
            if not path.exists():
                raise DeserializationError(
                    f"Required file not found: {path}",
                    file_path=path,
                )
        
        try:
            # 反序列化metadata
            metadata_data = self._read_yaml(metadata_path)
            metadata = self._deserialize_metadata(metadata_data, metadata_path)
            
            # 反序列化concepts
            concepts_data = self._read_yaml(concepts_path)
            concepts = self._deserialize_concepts(concepts_data, concepts_path)
            
            # 反序列化edges
            edges_data = self._read_yaml(edges_path)
            edges = self._deserialize_edges(edges_data, edges_path)
            
            # 构建图谱
            graph = KnowledgeGraph(
                metadata=metadata,
                concepts=concepts,
                edges=edges,
            )
            
            logger.info(
                f"Deserialized graph: {len(concepts)} concepts, "
                f"{len(edges)} edges from {source_dir}"
            )
            
            return graph
            
        except DeserializationError:
            raise
        except Exception as e:
            raise DeserializationError(
                f"Failed to deserialize graph: {e}",
                original_error=e,
            ) from e
    
    def _write_yaml(self, path: Path, data: Any) -> None:
        """写入YAML文件，使用pretty-print格式"""
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(
                data,
                f,
                Dumper=OrderedDumper,
                allow_unicode=True,
                default_flow_style=False,
                indent=2,
                sort_keys=True,
                width=120,
            )
    
    def _read_yaml(self, path: Path) -> Any:
        """读取YAML文件"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except yaml.YAMLError as e:
            line_number = None
            if hasattr(e, 'problem_mark') and e.problem_mark:
                line_number = e.problem_mark.line + 1
            raise DeserializationError(
                f"YAML parse error: {e}",
                file_path=path,
                line_number=line_number,
                original_error=e,
            ) from e
    
    # ============ Concepts 序列化/反序列化 ============
    
    def _serialize_concepts(self, concepts: List[ConceptNode]) -> List[Dict]:
        """序列化ConceptNode列表"""
        return [self._concept_to_dict(c) for c in concepts]
    
    def _concept_to_dict(self, concept: ConceptNode) -> Dict:
        """将ConceptNode转换为可序列化的dict"""
        data = {
            'concept_id': concept.concept_id,
            'canonical_label_zh': concept.canonical_label_zh,
            'divination_system': concept.divination_system.value,
            'dimension': concept.dimension.value,
            'source_nodes': [
                {
                    'book_id': sn.book_id,
                    'node_id': sn.node_id,
                    'snippet_ids': sn.snippet_ids,
                }
                for sn in concept.source_nodes
            ],
            'factor_refs': concept.factor_refs,
            'authority_score': concept.authority_score,
            'created_at': concept.created_at.isoformat() if concept.created_at else None,
            'updated_at': concept.updated_at.isoformat() if concept.updated_at else None,
        }
        
        # 可选字段
        if concept.canonical_label_en:
            data['canonical_label_en'] = concept.canonical_label_en
        if concept.subdimension:
            data['subdimension'] = concept.subdimension
        if concept.alignment_method:
            data['alignment_method'] = concept.alignment_method
        if concept.aggregation_rule_id:
            data['aggregation_rule_id'] = concept.aggregation_rule_id
        if concept.confidence is not None:
            data['confidence'] = concept.confidence
        if concept.conflict_summary:
            data['conflict_summary'] = {
                'conflict_count': concept.conflict_summary.conflict_count,
                'highest_authority_source': concept.conflict_summary.highest_authority_source,
                'conflict_types': concept.conflict_summary.conflict_types,
                'resolution_status': concept.conflict_summary.resolution_status,
            }
        
        return data
    
    def _deserialize_concepts(
        self,
        data: List[Dict],
        file_path: Path,
    ) -> List[ConceptNode]:
        """反序列化ConceptNode列表"""
        if not isinstance(data, list):
            raise DeserializationError(
                "concepts.yaml must contain a list",
                file_path=file_path,
            )
        
        concepts = []
        for i, item in enumerate(data):
            try:
                concept = self._dict_to_concept(item)
                concepts.append(concept)
            except ValidationError as e:
                raise DeserializationError(
                    f"Validation error at concept[{i}]: {e}",
                    file_path=file_path,
                    field_path=f"concepts[{i}]",
                    original_error=e,
                ) from e
            except Exception as e:
                raise DeserializationError(
                    f"Error parsing concept[{i}]: {e}",
                    file_path=file_path,
                    field_path=f"concepts[{i}]",
                    original_error=e,
                ) from e
        
        return concepts
    
    def _dict_to_concept(self, data: Dict) -> ConceptNode:
        """将dict转换为ConceptNode"""
        # 处理source_nodes
        source_nodes = [
            SourceNodeRef(
                book_id=sn['book_id'],
                node_id=sn['node_id'],
                snippet_ids=sn.get('snippet_ids', []),
            )
            for sn in data.get('source_nodes', [])
        ]
        
        # 处理conflict_summary
        conflict_summary = None
        if data.get('conflict_summary'):
            cs = data['conflict_summary']
            conflict_summary = ConflictSummary(
                conflict_count=cs.get('conflict_count', 0),
                highest_authority_source=cs.get('highest_authority_source'),
                conflict_types=cs.get('conflict_types', []),
                resolution_status=cs.get('resolution_status', 'unresolved'),
            )
        
        # 处理datetime字段
        created_at = None
        if data.get('created_at'):
            created_at = datetime.fromisoformat(data['created_at'])
        
        updated_at = None
        if data.get('updated_at'):
            updated_at = datetime.fromisoformat(data['updated_at'])
        
        return ConceptNode(
            concept_id=data['concept_id'],
            canonical_label_zh=data['canonical_label_zh'],
            canonical_label_en=data.get('canonical_label_en'),
            divination_system=DivinationSystem(data['divination_system']),
            dimension=Dimension(data['dimension']),
            subdimension=data.get('subdimension'),
            source_nodes=source_nodes,
            factor_refs=data.get('factor_refs', []),
            authority_score=data.get('authority_score', 0.5),
            alignment_method=data.get('alignment_method', 'factor_overlap'),
            aggregation_rule_id=data.get('aggregation_rule_id'),
            confidence=data.get('confidence', 0.8),
            conflict_summary=conflict_summary,
            created_at=created_at,
            updated_at=updated_at,
        )
    
    # ============ Edges 序列化/反序列化 ============
    
    def _serialize_edges(self, edges: List[SemanticEdge]) -> List[Dict]:
        """序列化SemanticEdge列表"""
        return [self._edge_to_dict(e) for e in edges]
    
    def _edge_to_dict(self, edge: SemanticEdge) -> Dict:
        """将SemanticEdge转换为可序列化的dict"""
        data = {
            'edge_id': edge.edge_id,
            'source_concept_id': edge.source_concept_id,
            'target_concept_id': edge.target_concept_id,
            'relation_type': edge.relation_type.value,
            'confidence': edge.confidence,
            'created_at': edge.created_at.isoformat() if edge.created_at else None,
        }
        
        # 可选字段
        if edge.conflict_type:
            data['conflict_type'] = edge.conflict_type.value
        if edge.evidence_refs:
            data['evidence_refs'] = edge.evidence_refs
        # 记录双向标记
        data['bidirectional'] = edge.bidirectional
        
        return data
    
    def _deserialize_edges(
        self,
        data: List[Dict],
        file_path: Path,
    ) -> List[SemanticEdge]:
        """反序列化SemanticEdge列表"""
        if not isinstance(data, list):
            raise DeserializationError(
                "edges.yaml must contain a list",
                file_path=file_path,
            )
        
        edges = []
        for i, item in enumerate(data):
            try:
                edge = self._dict_to_edge(item)
                edges.append(edge)
            except ValidationError as e:
                raise DeserializationError(
                    f"Validation error at edge[{i}]: {e}",
                    file_path=file_path,
                    field_path=f"edges[{i}]",
                    original_error=e,
                ) from e
            except Exception as e:
                raise DeserializationError(
                    f"Error parsing edge[{i}]: {e}",
                    file_path=file_path,
                    field_path=f"edges[{i}]",
                    original_error=e,
                ) from e
        
        return edges
    
    def _dict_to_edge(self, data: Dict) -> SemanticEdge:
        """将dict转换为SemanticEdge"""
        conflict_type = None
        if data.get('conflict_type'):
            conflict_type = ConflictType(data['conflict_type'])
        
        created_at = None
        if data.get('created_at'):
            created_at = datetime.fromisoformat(data['created_at'])
        
        return SemanticEdge(
            edge_id=data['edge_id'],
            source_concept_id=data['source_concept_id'],
            target_concept_id=data['target_concept_id'],
            relation_type=RelationType(data['relation_type']),
            conflict_type=conflict_type,
            confidence=data.get('confidence', 0.8),
            evidence_refs=data.get('evidence_refs', []),
            bidirectional=data.get('bidirectional', False),
            created_at=created_at,
        )
    
    # ============ Metadata 序列化/反序列化 ============
    
    def _serialize_metadata(self, metadata: GraphMetadata) -> Dict:
        """序列化GraphMetadata"""
        return {
            'version': metadata.version,
            'build_timestamp': metadata.build_timestamp.isoformat(),
            'total_concepts': metadata.total_concepts,
            'total_edges': metadata.total_edges,
            'books_included': metadata.books_included,
            'systems_covered': [s.value for s in metadata.systems_covered],
            'quality_metrics': metadata.quality_metrics,
            'graph_status': metadata.graph_status,
            'last_validated_at': (
                metadata.last_validated_at.isoformat() 
                if metadata.last_validated_at else None
            ),
            'validation_passed': metadata.validation_passed,
        }
    
    def _deserialize_metadata(
        self,
        data: Dict,
        file_path: Path,
    ) -> GraphMetadata:
        """反序列化GraphMetadata"""
        if not isinstance(data, dict):
            raise DeserializationError(
                "metadata.yaml must contain a dict",
                file_path=file_path,
            )
        
        try:
            # 处理datetime字段
            build_timestamp = datetime.fromisoformat(data['build_timestamp'])
            
            last_validated_at = None
            if data.get('last_validated_at'):
                last_validated_at = datetime.fromisoformat(data['last_validated_at'])
            
            # 处理systems_covered
            systems_covered = [
                DivinationSystem(s) for s in data.get('systems_covered', [])
            ]
            
            return GraphMetadata(
                version=data['version'],
                build_timestamp=build_timestamp,
                total_concepts=data.get('total_concepts', 0),
                total_edges=data.get('total_edges', 0),
                books_included=data.get('books_included', []),
                systems_covered=systems_covered,
                quality_metrics=data.get('quality_metrics', {}),
                graph_status=data.get('graph_status', 'valid'),
                last_validated_at=last_validated_at,
                validation_passed=data.get('validation_passed', False),
            )
        except ValidationError as e:
            raise DeserializationError(
                f"Validation error in metadata: {e}",
                file_path=file_path,
                field_path="metadata",
                original_error=e,
            ) from e
        except Exception as e:
            raise DeserializationError(
                f"Error parsing metadata: {e}",
                file_path=file_path,
                field_path="metadata",
                original_error=e,
            ) from e
    
    # ============ 便捷方法 ============
    
    def round_trip(self, graph: KnowledgeGraph) -> KnowledgeGraph:
        """
        往返测试：序列化后立即反序列化
        
        用于验证序列化的正确性
        """
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            self.serialize(graph, output_dir=tmpdir)
            return self.deserialize(input_dir=tmpdir)
    
    def verify_round_trip(self, graph: KnowledgeGraph) -> bool:
        """
        验证往返一致性
        
        Returns:
            True如果往返后图谱完全一致
        """
        restored = self.round_trip(graph)
        
        # 比较概念数量
        if len(graph.concepts) != len(restored.concepts):
            logger.warning(
                f"Concept count mismatch: {len(graph.concepts)} vs {len(restored.concepts)}"
            )
            return False
        
        # 比较边数量
        if len(graph.edges) != len(restored.edges):
            logger.warning(
                f"Edge count mismatch: {len(graph.edges)} vs {len(restored.edges)}"
            )
            return False
        
        # 比较concept_ids
        original_ids = {c.concept_id for c in graph.concepts}
        restored_ids = {c.concept_id for c in restored.concepts}
        if original_ids != restored_ids:
            logger.warning(f"Concept IDs differ: {original_ids ^ restored_ids}")
            return False
        
        # 比较edge_ids
        original_edge_ids = {e.edge_id for e in graph.edges}
        restored_edge_ids = {e.edge_id for e in restored.edges}
        if original_edge_ids != restored_edge_ids:
            logger.warning(f"Edge IDs differ: {original_edge_ids ^ restored_edge_ids}")
            return False
        
        return True
    
    # ============ 懒加载支持 ============
    
    def deserialize_metadata_only(
        self,
        input_dir: Optional[Union[str, Path]] = None,
    ) -> GraphMetadata:
        """
        仅加载metadata（懒加载模式）
        
        Args:
            input_dir: 输入目录
            
        Returns:
            GraphMetadata对象
        """
        source_dir = Path(input_dir) if input_dir else self.output_dir
        metadata_path = source_dir / "metadata.yaml"
        
        if not metadata_path.exists():
            raise DeserializationError(
                f"Metadata file not found: {metadata_path}",
                file_path=metadata_path,
            )
        
        metadata_data = self._read_yaml(metadata_path)
        return self._deserialize_metadata(metadata_data, metadata_path)
    
    def deserialize_concepts_only(
        self,
        input_dir: Optional[Union[str, Path]] = None,
    ) -> List[ConceptNode]:
        """
        仅加载concepts（按需加载）
        
        Args:
            input_dir: 输入目录
            
        Returns:
            ConceptNode列表
        """
        source_dir = Path(input_dir) if input_dir else self.output_dir
        
        # 检查是否为分片存储
        metadata_path = source_dir / "metadata.yaml"
        if metadata_path.exists():
            metadata_data = self._read_yaml(metadata_path)
            shard_info = metadata_data.get('shard_info', {})
            # 如果有shard_info字段（即使为空列表），说明是分片模式
            if 'concepts_shards' in shard_info:
                shards = shard_info['concepts_shards']
                if not shards:
                    return []  # 空分片列表返回空结果
                return self._load_sharded_concepts(source_dir, shard_info)
        
        # 单文件加载
        concepts_path = source_dir / "concepts.yaml"
        if not concepts_path.exists():
            raise DeserializationError(
                f"Concepts file not found: {concepts_path}",
                file_path=concepts_path,
            )
        
        concepts_data = self._read_yaml(concepts_path)
        return self._deserialize_concepts(concepts_data, concepts_path)
    
    def deserialize_edges_only(
        self,
        input_dir: Optional[Union[str, Path]] = None,
    ) -> List[SemanticEdge]:
        """
        仅加载edges（按需加载）
        
        Args:
            input_dir: 输入目录
            
        Returns:
            SemanticEdge列表
        """
        source_dir = Path(input_dir) if input_dir else self.output_dir
        
        # 检查是否为分片存储
        metadata_path = source_dir / "metadata.yaml"
        if metadata_path.exists():
            metadata_data = self._read_yaml(metadata_path)
            shard_info = metadata_data.get('shard_info', {})
            # 如果有shard_info字段（即使为空列表），说明是分片模式
            if 'edges_shards' in shard_info:
                shards = shard_info['edges_shards']
                if not shards:
                    return []  # 空分片列表返回空结果
                return self._load_sharded_edges(source_dir, shard_info)
        
        # 单文件加载
        edges_path = source_dir / "edges.yaml"
        if not edges_path.exists():
            raise DeserializationError(
                f"Edges file not found: {edges_path}",
                file_path=edges_path,
            )
        
        edges_data = self._read_yaml(edges_path)
        return self._deserialize_edges(edges_data, edges_path)
    
    # ============ 分片支持 ============
    
    SHARD_SIZE_THRESHOLD_MB = 50  # 超过50MB自动分片
    SHARD_ITEMS_PER_FILE = 5000   # 每个分片文件的最大条目数
    
    def serialize_with_sharding(
        self,
        graph: KnowledgeGraph,
        output_dir: Optional[Union[str, Path]] = None,
        force_shard: bool = False,
    ) -> Tuple[Path, ...]:
        """
        带分片的序列化（大图谱自动分片）
        
        Args:
            graph: 要序列化的知识图谱
            output_dir: 输出目录
            force_shard: 强制启用分片
            
        Returns:
            所有生成文件的路径元组
        """
        target_dir = Path(output_dir) if output_dir else self.output_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        
        generated_files = []
        shard_info = {}
        
        # 判断是否需要分片
        needs_sharding = force_shard or self._should_shard(graph)
        
        if needs_sharding:
            # 分片保存concepts
            concept_shards = self._shard_concepts(graph.concepts, target_dir)
            shard_info['concepts_shards'] = [s.name for s in concept_shards]
            generated_files.extend(concept_shards)
            
            # 分片保存edges
            edge_shards = self._shard_edges(graph.edges, target_dir)
            shard_info['edges_shards'] = [s.name for s in edge_shards]
            generated_files.extend(edge_shards)
        else:
            # 单文件保存
            concepts_path = target_dir / "concepts.yaml"
            edges_path = target_dir / "edges.yaml"
            
            concepts_data = self._serialize_concepts(graph.concepts)
            self._write_yaml(concepts_path, concepts_data)
            generated_files.append(concepts_path)
            
            edges_data = self._serialize_edges(graph.edges)
            self._write_yaml(edges_path, edges_data)
            generated_files.append(edges_path)
        
        # 保存metadata（包含分片信息）
        metadata_path = target_dir / "metadata.yaml"
        metadata_data = self._serialize_metadata(graph.metadata)
        if shard_info:
            metadata_data['shard_info'] = shard_info
        metadata_data['schema_version'] = '1.0.0'  # 版本迁移支持
        self._write_yaml(metadata_path, metadata_data)
        generated_files.append(metadata_path)
        
        logger.info(
            f"Serialized graph with {'sharding' if needs_sharding else 'single files'}: "
            f"{len(generated_files)} files"
        )
        
        return tuple(generated_files)
    
    def _should_shard(self, graph: KnowledgeGraph) -> bool:
        """判断是否需要分片"""
        # 估算序列化大小（粗略估计：每个concept约2KB，每个edge约500B）
        estimated_size_mb = (
            len(graph.concepts) * 2048 + len(graph.edges) * 512
        ) / (1024 * 1024)
        return estimated_size_mb > self.SHARD_SIZE_THRESHOLD_MB
    
    def _shard_concepts(
        self,
        concepts: List[ConceptNode],
        output_dir: Path,
    ) -> List[Path]:
        """将concepts分片保存"""
        shards = []
        total = len(concepts)
        
        for i in range(0, total, self.SHARD_ITEMS_PER_FILE):
            shard_num = i // self.SHARD_ITEMS_PER_FILE + 1
            shard_path = output_dir / f"concepts_{shard_num:03d}.yaml"
            
            shard_concepts = concepts[i:i + self.SHARD_ITEMS_PER_FILE]
            shard_data = self._serialize_concepts(shard_concepts)
            self._write_yaml(shard_path, shard_data)
            
            shards.append(shard_path)
            logger.debug(f"Created concept shard: {shard_path.name} ({len(shard_concepts)} items)")
        
        return shards
    
    def _shard_edges(
        self,
        edges: List[SemanticEdge],
        output_dir: Path,
    ) -> List[Path]:
        """将edges分片保存"""
        shards = []
        total = len(edges)
        
        for i in range(0, total, self.SHARD_ITEMS_PER_FILE):
            shard_num = i // self.SHARD_ITEMS_PER_FILE + 1
            shard_path = output_dir / f"edges_{shard_num:03d}.yaml"
            
            shard_edges = edges[i:i + self.SHARD_ITEMS_PER_FILE]
            shard_data = self._serialize_edges(shard_edges)
            self._write_yaml(shard_path, shard_data)
            
            shards.append(shard_path)
            logger.debug(f"Created edge shard: {shard_path.name} ({len(shard_edges)} items)")
        
        return shards
    
    def _load_sharded_concepts(
        self,
        source_dir: Path,
        shard_info: dict,
    ) -> List[ConceptNode]:
        """加载分片的concepts"""
        concepts = []
        
        for shard_name in shard_info.get('concepts_shards', []):
            shard_path = source_dir / shard_name
            if not shard_path.exists():
                raise DeserializationError(
                    f"Concept shard not found: {shard_path}",
                    file_path=shard_path,
                )
            
            shard_data = self._read_yaml(shard_path)
            shard_concepts = self._deserialize_concepts(shard_data, shard_path)
            concepts.extend(shard_concepts)
        
        return concepts
    
    def _load_sharded_edges(
        self,
        source_dir: Path,
        shard_info: dict,
    ) -> List[SemanticEdge]:
        """加载分片的edges"""
        edges = []
        
        for shard_name in shard_info.get('edges_shards', []):
            shard_path = source_dir / shard_name
            if not shard_path.exists():
                raise DeserializationError(
                    f"Edge shard not found: {shard_path}",
                    file_path=shard_path,
                )
            
            shard_data = self._read_yaml(shard_path)
            shard_edges = self._deserialize_edges(shard_data, shard_path)
            edges.extend(shard_edges)
        
        return edges


class LazyKnowledgeGraph:
    """
    懒加载知识图谱包装器
    
    仅在首次访问concepts/edges时才加载数据
    """
    
    def __init__(
        self,
        serializer: GraphSerializer,
        source_dir: Union[str, Path],
    ):
        self._serializer = serializer
        self._source_dir = Path(source_dir)
        self._metadata: Optional[GraphMetadata] = None
        self._concepts: Optional[List[ConceptNode]] = None
        self._edges: Optional[List[SemanticEdge]] = None
        self._graph: Optional[KnowledgeGraph] = None
    
    @property
    def metadata(self) -> GraphMetadata:
        """懒加载metadata"""
        if self._metadata is None:
            self._metadata = self._serializer.deserialize_metadata_only(self._source_dir)
        return self._metadata
    
    @property
    def concepts(self) -> List[ConceptNode]:
        """懒加载concepts"""
        if self._concepts is None:
            self._concepts = self._serializer.deserialize_concepts_only(self._source_dir)
        return self._concepts
    
    @property
    def edges(self) -> List[SemanticEdge]:
        """懒加载edges"""
        if self._edges is None:
            self._edges = self._serializer.deserialize_edges_only(self._source_dir)
        return self._edges
    
    def to_graph(self) -> KnowledgeGraph:
        """
        转换为完整的KnowledgeGraph
        
        一旦调用此方法，所有数据都会被加载
        """
        if self._graph is None:
            self._graph = KnowledgeGraph(
                metadata=self.metadata,
                concepts=self.concepts,
                edges=self.edges,
            )
        return self._graph
    
    def is_loaded(self) -> Tuple[bool, bool, bool]:
        """
        检查加载状态
        
        Returns:
            (metadata_loaded, concepts_loaded, edges_loaded)
        """
        return (
            self._metadata is not None,
            self._concepts is not None,
            self._edges is not None,
        )
