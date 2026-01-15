"""
SnapshotManager - 版本快照管理器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 5.5, Req 5.6
Design Refs: Design.md#模块结构

实现:
- create_snapshot: 生成snapshot_{version}_{timestamp}.yaml
- list_snapshots: 列出所有快照（按时间排序）
- rollback: 恢复指定版本的图谱状态
- 支持retention_period配置（默认7天）
- 自动清理过期快照
"""

import logging
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional, Tuple, Union

import yaml

from scripts.knowledge_graph_builder.models.graph import KnowledgeGraph
from scripts.knowledge_graph_builder.persistence.serializer import (
    GraphSerializer,
    DeserializationError,
)

logger = logging.getLogger(__name__)


class SnapshotInfo:
    """快照信息"""
    
    def __init__(
        self,
        version: str,
        timestamp: datetime,
        snapshot_dir: Path,
        total_concepts: int = 0,
        total_edges: int = 0,
    ):
        self.version = version
        self.timestamp = timestamp
        self.snapshot_dir = snapshot_dir
        self.total_concepts = total_concepts
        self.total_edges = total_edges
    
    @property
    def name(self) -> str:
        """快照目录名"""
        return self.snapshot_dir.name
    
    def __repr__(self) -> str:
        return (
            f"SnapshotInfo(version={self.version}, "
            f"timestamp={self.timestamp.isoformat()}, "
            f"concepts={self.total_concepts}, edges={self.total_edges})"
        )


class SnapshotError(Exception):
    """快照操作错误"""
    pass


class SnapshotManager:
    """
    知识图谱快照管理器
    
    快照目录结构:
    data/knowledge_graph/snapshots/
    ├── snapshot_1.0.0_20251204T120000/
    │   ├── concepts.yaml
    │   ├── edges.yaml
    │   └── metadata.yaml
    ├── snapshot_1.0.1_20251205T090000/
    │   └── ...
    """
    
    DEFAULT_SNAPSHOTS_DIR = Path("data/knowledge_graph/snapshots")
    DEFAULT_RETENTION_DAYS = 7
    
    def __init__(
        self,
        snapshots_dir: Optional[Union[str, Path]] = None,
        retention_days: int = DEFAULT_RETENTION_DAYS,
        serializer: Optional[GraphSerializer] = None,
    ):
        """
        初始化快照管理器
        
        Args:
            snapshots_dir: 快照目录，默认为data/knowledge_graph/snapshots/
            retention_days: 快照保留天数，默认7天
            serializer: 图谱序列化器（可选，不提供则自动创建）
        """
        self.snapshots_dir = Path(snapshots_dir) if snapshots_dir else self.DEFAULT_SNAPSHOTS_DIR
        self.retention_days = retention_days
        self.serializer = serializer or GraphSerializer()
        
        # 确保目录存在
        self.snapshots_dir.mkdir(parents=True, exist_ok=True)
    
    def create_snapshot(
        self,
        graph: KnowledgeGraph,
        description: Optional[str] = None,
    ) -> SnapshotInfo:
        """
        创建图谱快照
        
        Args:
            graph: 要快照的知识图谱
            description: 快照描述（可选）
            
        Returns:
            SnapshotInfo对象
            
        Raises:
            SnapshotError: 创建失败时抛出
        """
        try:
            # 生成快照目录名
            version = graph.metadata.version
            timestamp = datetime.now()
            timestamp_str = timestamp.strftime("%Y%m%dT%H%M%S")
            snapshot_name = f"snapshot_{version}_{timestamp_str}"
            snapshot_dir = self.snapshots_dir / snapshot_name
            
            # 创建快照目录
            snapshot_dir.mkdir(parents=True, exist_ok=True)
            
            # 使用serializer保存图谱
            self.serializer.serialize(graph, output_dir=snapshot_dir)
            
            # 保存快照元信息
            snapshot_meta = {
                'version': version,
                'timestamp': timestamp.isoformat(),
                'total_concepts': len(graph.concepts),
                'total_edges': len(graph.edges),
                'description': description,
                'retention_days': self.retention_days,
            }
            meta_path = snapshot_dir / "snapshot_meta.yaml"
            with open(meta_path, 'w', encoding='utf-8') as f:
                yaml.safe_dump(snapshot_meta, f, allow_unicode=True)
            
            logger.info(f"Created snapshot: {snapshot_name}")
            
            # 自动清理过期快照
            self._cleanup_expired_snapshots()
            
            return SnapshotInfo(
                version=version,
                timestamp=timestamp,
                snapshot_dir=snapshot_dir,
                total_concepts=len(graph.concepts),
                total_edges=len(graph.edges),
            )
            
        except Exception as e:
            raise SnapshotError(f"Failed to create snapshot: {e}") from e
    
    def list_snapshots(self) -> List[SnapshotInfo]:
        """
        列出所有快照（按时间倒序排序）
        
        Returns:
            SnapshotInfo列表，最新的在前
        """
        snapshots = []
        
        for entry in self.snapshots_dir.iterdir():
            if not entry.is_dir() or not entry.name.startswith("snapshot_"):
                continue
            
            try:
                info = self._parse_snapshot_info(entry)
                if info:
                    snapshots.append(info)
            except Exception as e:
                logger.warning(f"Failed to parse snapshot {entry.name}: {e}")
        
        # 按时间倒序排序
        snapshots.sort(key=lambda x: x.timestamp, reverse=True)
        
        return snapshots
    
    def get_snapshot(self, version: str) -> Optional[SnapshotInfo]:
        """
        获取指定版本的最新快照
        
        Args:
            version: 版本号
            
        Returns:
            SnapshotInfo，如果不存在则返回None
        """
        snapshots = self.list_snapshots()
        for snapshot in snapshots:
            if snapshot.version == version:
                return snapshot
        return None
    
    def rollback(
        self,
        version: Optional[str] = None,
        snapshot_name: Optional[str] = None,
    ) -> KnowledgeGraph:
        """
        回滚到指定快照
        
        Args:
            version: 版本号（回滚到该版本的最新快照）
            snapshot_name: 快照名称（精确指定）
            
        Returns:
            恢复的KnowledgeGraph
            
        Raises:
            SnapshotError: 回滚失败时抛出
        """
        if not version and not snapshot_name:
            raise SnapshotError("Must specify either version or snapshot_name")
        
        # 查找快照
        snapshot_dir = None
        
        if snapshot_name:
            # 精确查找
            snapshot_dir = self.snapshots_dir / snapshot_name
            if not snapshot_dir.exists():
                raise SnapshotError(f"Snapshot not found: {snapshot_name}")
        else:
            # 按版本查找最新的
            snapshot = self.get_snapshot(version)
            if not snapshot:
                raise SnapshotError(f"No snapshot found for version: {version}")
            snapshot_dir = snapshot.snapshot_dir
        
        try:
            # 使用serializer恢复图谱
            graph = self.serializer.deserialize(input_dir=snapshot_dir)
            logger.info(f"Rolled back to snapshot: {snapshot_dir.name}")
            return graph
            
        except DeserializationError as e:
            raise SnapshotError(f"Failed to restore snapshot: {e}") from e
    
    def delete_snapshot(self, snapshot_name: str) -> bool:
        """
        删除指定快照
        
        Args:
            snapshot_name: 快照名称
            
        Returns:
            是否成功删除
        """
        snapshot_dir = self.snapshots_dir / snapshot_name
        
        if not snapshot_dir.exists():
            logger.warning(f"Snapshot not found: {snapshot_name}")
            return False
        
        try:
            shutil.rmtree(snapshot_dir)
            logger.info(f"Deleted snapshot: {snapshot_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete snapshot {snapshot_name}: {e}")
            return False
    
    def _parse_snapshot_info(self, snapshot_dir: Path) -> Optional[SnapshotInfo]:
        """解析快照目录信息"""
        # 尝试从snapshot_meta.yaml读取
        meta_path = snapshot_dir / "snapshot_meta.yaml"
        if meta_path.exists():
            with open(meta_path, 'r', encoding='utf-8') as f:
                meta = yaml.safe_load(f)
                return SnapshotInfo(
                    version=meta.get('version', 'unknown'),
                    timestamp=datetime.fromisoformat(meta['timestamp']),
                    snapshot_dir=snapshot_dir,
                    total_concepts=meta.get('total_concepts', 0),
                    total_edges=meta.get('total_edges', 0),
                )
        
        # 从目录名解析
        # 格式: snapshot_{version}_{timestamp}
        name = snapshot_dir.name
        parts = name.split('_')
        if len(parts) >= 3:
            version = parts[1]
            timestamp_str = parts[2]
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y%m%dT%H%M%S")
                
                # 尝试从metadata.yaml获取统计
                metadata_path = snapshot_dir / "metadata.yaml"
                total_concepts = 0
                total_edges = 0
                if metadata_path.exists():
                    with open(metadata_path, 'r', encoding='utf-8') as f:
                        metadata = yaml.safe_load(f)
                        total_concepts = metadata.get('total_concepts', 0)
                        total_edges = metadata.get('total_edges', 0)
                
                return SnapshotInfo(
                    version=version,
                    timestamp=timestamp,
                    snapshot_dir=snapshot_dir,
                    total_concepts=total_concepts,
                    total_edges=total_edges,
                )
            except ValueError:
                pass
        
        return None
    
    def _cleanup_expired_snapshots(self) -> int:
        """
        清理过期快照
        
        Returns:
            清理的快照数量
        """
        if self.retention_days <= 0:
            return 0  # 不限制保留期
        
        cutoff_date = datetime.now() - timedelta(days=self.retention_days)
        cleaned_count = 0
        
        for snapshot in self.list_snapshots():
            if snapshot.timestamp < cutoff_date:
                if self.delete_snapshot(snapshot.name):
                    cleaned_count += 1
        
        if cleaned_count > 0:
            logger.info(f"Cleaned up {cleaned_count} expired snapshots")
        
        return cleaned_count
    
    def get_latest_snapshot(self) -> Optional[SnapshotInfo]:
        """获取最新的快照"""
        snapshots = self.list_snapshots()
        return snapshots[0] if snapshots else None
    
    def count_snapshots(self) -> int:
        """统计快照数量"""
        return len(self.list_snapshots())
