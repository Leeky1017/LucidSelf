"""
Version Tree Database Models

版本树的 SQLAlchemy 模型，用于持久化用户决策轨迹。

对照契约: backend/core/contracts/version_tree_models.py
"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from backend.db.base import Base


class VersionTree(Base):
    """
    版本树表
    
    记录用户在版本选择中的完整轨迹。
    每个用户可以有多棵版本树（按场景/领域划分）。
    """
    __tablename__ = "version_trees"

    # 主键
    tree_id = Column(
        String(64), 
        primary_key=True,
        comment="树ID，格式 tree_xxxxxxxxxxxx"
    )
    
    # 关联用户
    user_id = Column(
        String(64), 
        nullable=False, 
        index=True,
        comment="用户ID"
    )
    
    # 根节点和当前节点
    root_node_id = Column(
        String(64),
        nullable=False,
        comment="根节点 ID"
    )
    
    current_node_id = Column(
        String(64),
        nullable=False,
        comment="当前所在节点 ID"
    )
    
    # 场景和领域
    scenario_id = Column(
        String(64),
        nullable=True,
        comment="关联的场景 ID"
    )
    
    domain = Column(
        String(32),
        nullable=True,
        comment="生活领域 (career/wealth/relationship/health/...)"
    )
    
    # 统计
    total_decisions = Column(
        Integer,
        default=0,
        nullable=False,
        comment="总决策次数"
    )
    
    max_depth = Column(
        Integer,
        default=0,
        nullable=False,
        comment="当前最大深度"
    )
    
    # 时间戳
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="创建时间"
    )
    
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
        comment="更新时间"
    )

    # 关联节点
    nodes = relationship(
        "TreeNode",
        back_populates="tree",
        cascade="all, delete-orphan",
    )

    # 复合索引
    __table_args__ = (
        Index('ix_tree_user_domain', 'user_id', 'domain'),
        Index('ix_tree_user_scenario', 'user_id', 'scenario_id'),
    )

    def __repr__(self) -> str:
        return f"<VersionTree {self.tree_id} user={self.user_id}>"


class TreeNode(Base):
    """
    版本树节点表
    
    代表用户在版本树中的一个位置。
    """
    __tablename__ = "tree_nodes"

    # 主键
    node_id = Column(
        String(64), 
        primary_key=True,
        comment="节点ID，格式 node_xxxxxxxxxxxx"
    )
    
    # 关联树
    tree_id = Column(
        String(64),
        ForeignKey("version_trees.tree_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="所属树 ID"
    )
    
    # 父节点
    parent_id = Column(
        String(64),
        ForeignKey("tree_nodes.node_id", ondelete="SET NULL"),
        nullable=True,
        comment="父节点 ID，根节点为 None"
    )
    
    # 关联版本
    version_id = Column(
        String(64),
        nullable=False,
        comment="关联的 LifeVersion ID"
    )
    
    # 决策信息
    decision_point = Column(
        String(100),
        nullable=True,
        comment="用户在此做的决策描述"
    )
    
    selected_option = Column(
        String(50),
        nullable=True,
        comment="用户选择的选项"
    )
    
    decision_time = Column(
        DateTime,
        nullable=True,
        comment="决策时间"
    )
    
    # 状态
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="是否为当前活跃路径"
    )
    
    # 深度（便于查询）
    depth = Column(
        Integer,
        default=0,
        nullable=False,
        comment="节点深度（根节点为0）"
    )
    
    # 创建时间
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="创建时间"
    )

    # 关联
    tree = relationship("VersionTree", back_populates="nodes")
    parent = relationship(
        "TreeNode",
        remote_side=[node_id],
        backref="children",
    )

    # 索引
    __table_args__ = (
        Index('ix_node_tree_depth', 'tree_id', 'depth'),
        Index('ix_node_parent', 'parent_id'),
    )

    def __repr__(self) -> str:
        return f"<TreeNode {self.node_id} version={self.version_id}>"


class DecisionRecord(Base):
    """
    决策记录表
    
    记录每次用户决策的详细信息，用于回溯和分析。
    """
    __tablename__ = "decision_records"

    # 主键
    record_id = Column(
        String(64), 
        primary_key=True,
        comment="记录ID，格式 dr_xxxxxxxxxxxx"
    )
    
    # 关联
    user_id = Column(
        String(64),
        nullable=False,
        index=True,
        comment="用户ID"
    )
    
    tree_id = Column(
        String(64),
        ForeignKey("version_trees.tree_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="树 ID"
    )
    
    node_id = Column(
        String(64),
        ForeignKey("tree_nodes.node_id", ondelete="SET NULL"),
        nullable=True,
        comment="节点 ID"
    )
    
    # 决策内容
    decision_point = Column(
        String(100),
        nullable=False,
        comment="决策点描述"
    )
    
    options_presented = Column(
        JSON,
        nullable=False,
        comment="呈现给用户的选项列表"
    )
    
    option_selected = Column(
        String(50),
        nullable=False,
        comment="用户选择的选项"
    )
    
    # 上下文快照
    context_snapshot = Column(
        JSON,
        default=dict,
        nullable=False,
        comment="决策时的关键因子快照"
    )
    
    # 备注
    notes = Column(
        String(200),
        nullable=True,
        comment="用户备注"
    )
    
    # 时间戳
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="决策时间"
    )

    # 索引
    __table_args__ = (
        Index('ix_decision_user_time', 'user_id', 'created_at'),
        Index('ix_decision_tree', 'tree_id', 'created_at'),
    )

    def __repr__(self) -> str:
        return f"<DecisionRecord {self.record_id} user={self.user_id}>"

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "record_id": self.record_id,
            "user_id": self.user_id,
            "tree_id": self.tree_id,
            "node_id": self.node_id,
            "decision_point": self.decision_point,
            "options_presented": self.options_presented,
            "option_selected": self.option_selected,
            "context_snapshot": self.context_snapshot,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
