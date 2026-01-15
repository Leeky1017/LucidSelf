"""
版本树数据模型

用户决策轨迹追踪的数据模型。

对照文档: docs/ls_roadmap_executable.md §五、Phase 4: 版本树与决策追踪
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TreeNode(BaseModel):
    """
    版本树节点
    
    代表用户在版本树中的一个位置。
    """
    node_id: str = Field(..., pattern=r"^node_[a-z0-9]{12}$")
    parent_id: Optional[str] = Field(
        None, 
        description="父节点 ID，根节点为 None"
    )
    version_id: str = Field(..., description="关联的 LifeVersion ID")
    
    # 决策信息
    decision_point: Optional[str] = Field(
        None, 
        max_length=100,
        description="用户在此做的决策描述"
    )
    selected_option: Optional[str] = Field(
        None,
        max_length=50,
        description="用户选择的选项"
    )
    
    # 时间
    decision_time: Optional[datetime] = Field(
        None,
        description="决策时间"
    )
    
    # 子节点
    children: List[str] = Field(
        default_factory=list, 
        description="子节点 node_id 列表"
    )
    
    # 状态
    is_active: bool = Field(
        default=True,
        description="是否为当前活跃路径"
    )


class VersionTree(BaseModel):
    """
    版本树
    
    记录用户在版本选择中的完整轨迹。
    """
    tree_id: str = Field(..., pattern=r"^tree_[a-z0-9]{12}$")
    user_id: str
    root_node_id: str = Field(..., description="根节点 ID")
    current_node_id: str = Field(..., description="用户当前所在节点")
    
    # 节点映射
    nodes: Dict[str, TreeNode] = Field(
        default_factory=dict,
        description="node_id → TreeNode"
    )
    
    # 元数据
    scenario_id: Optional[str] = Field(
        None,
        description="关联的场景 ID"
    )
    domain: Optional[str] = Field(
        None,
        description="生活领域"
    )
    
    # 时间戳
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # 统计
    total_decisions: int = Field(default=0, description="总决策次数")
    max_depth: int = Field(default=0, description="当前最大深度")


class DecisionRecord(BaseModel):
    """
    决策记录
    
    记录单次用户决策的详细信息。
    """
    record_id: str = Field(..., pattern=r"^dr_[a-z0-9]{12}$")
    user_id: str
    tree_id: str
    node_id: str
    
    # 决策内容
    decision_point: str = Field(..., max_length=100)
    options_presented: List[str] = Field(
        ..., 
        min_length=2,
        max_length=5,
        description="呈现给用户的选项列表"
    )
    option_selected: str = Field(..., max_length=50)
    
    # 决策时的上下文快照
    context_snapshot: Dict[str, Any] = Field(
        default_factory=dict,
        description="决策时的关键因子快照"
    )
    
    # 时间
    created_at: datetime = Field(default_factory=datetime.now)
    
    # 可选备注
    notes: Optional[str] = Field(None, max_length=200)


class TreeTraversalPath(BaseModel):
    """
    树遍历路径
    
    从根到某节点的完整路径。
    """
    tree_id: str
    path: List[str] = Field(..., description="node_id 序列，从根到目标")
    decisions: List[str] = Field(
        default_factory=list,
        description="路径上的决策序列"
    )
    total_depth: int = Field(default=0)


# =============================================================================
# 树操作约束
# =============================================================================

TREE_CONSTRAINTS = {
    "max_depth": 10,  # 最大深度
    "max_nodes": 100,  # 单棵树最大节点数
    "max_children_per_node": 4,  # 每个节点最多子节点数
    "retention_days": 365,  # 保留天数
}
