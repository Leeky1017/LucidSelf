"""
版本树服务

管理用户决策轨迹和版本树。

对照文档: docs/ls_roadmap_executable.md §五、Phase 4: 版本树与决策追踪

v2.0 更新: 集成 VersionTreeRepository 实现数据持久化
"""

import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from backend.core.contracts.life_version_models import (
    LifeVersion,
    LifeVersionSet,
)
from backend.core.contracts.version_tree_models import (
    DecisionRecord,
    TREE_CONSTRAINTS,
    TreeNode,
    TreeTraversalPath,
    VersionTree,
)

logger = logging.getLogger(__name__)


class VersionTreeService:
    """
    版本树服务
    
    职责:
    - 创建和管理版本树
    - 记录用户决策
    - 遍历和查询版本路径
    
    支持两种模式:
    - persist=True: 使用数据库持久化 (生产环境)
    - persist=False: 使用内存存储 (测试/开发)
    """
    
    def __init__(self, persist: bool = True):
        """
        初始化服务
        
        Args:
            persist: 是否使用数据库持久化
        """
        self._persist = persist
        self._repository = None
        
        # 内存存储（仅当 persist=False 时使用）
        self._trees: Dict[str, VersionTree] = {}
        self._decisions: List[DecisionRecord] = []
        
        if persist:
            try:
                from backend.repositories.version_tree_repository import (
                    get_version_tree_repository,
                )
                self._repository = get_version_tree_repository()
                logger.info("VersionTreeService initialized with database persistence")
            except Exception as e:
                logger.warning(f"Failed to initialize repository, falling back to memory: {e}")
                self._persist = False
    
    async def create_tree(
        self, 
        user_id: str, 
        version_set: LifeVersionSet,
    ) -> VersionTree:
        """
        从版本集创建版本树
        
        Args:
            user_id: 用户 ID
            version_set: 版本集合
            
        Returns:
            新创建的版本树
        """
        if self._persist and self._repository:
            # 使用 Repository 持久化
            # 使用第一个版本作为默认根版本
            root_version_id = version_set.versions[0].version_id if version_set.versions else ""
            
            tree = await self._repository.create_tree(
                user_id=user_id,
                root_version_id=root_version_id,
                scenario_id=version_set.scenario_id,
                domain=version_set.domain.value,
            )
            
            # 为其他版本添加分支节点
            for version in version_set.versions[1:]:
                await self._repository.add_node(
                    tree_id=tree.tree_id,
                    parent_id=tree.root_node_id,
                    version_id=version.version_id,
                )
            
            # 重新获取完整的树
            tree = await self._repository.get_tree(tree.tree_id)
            
            logger.info(
                f"Created version tree {tree.tree_id} with "
                f"{len(version_set.versions)} version nodes (persisted)"
            )
            
            return tree
        else:
            # 使用内存存储
            return await self._create_tree_in_memory(user_id, version_set)
    
    async def _create_tree_in_memory(
        self,
        user_id: str,
        version_set: LifeVersionSet,
    ) -> VersionTree:
        """内存模式下创建版本树"""
        # 创建版本节点
        version_nodes: List[TreeNode] = []
        for version in version_set.versions:
            node = TreeNode(
                node_id=f"node_{uuid.uuid4().hex[:12]}",
                parent_id="root",
                version_id=version.version_id,
            )
            version_nodes.append(node)
        
        # 创建虚拟根节点
        root_node = TreeNode(
            node_id="node_root00000000",
            parent_id=None,
            version_id="",
            children=[n.node_id for n in version_nodes],
        )
        
        # 构建节点映射
        nodes = {"node_root00000000": root_node}
        for node in version_nodes:
            nodes[node.node_id] = node
        
        # 创建版本树
        tree = VersionTree(
            tree_id=f"tree_{uuid.uuid4().hex[:12]}",
            user_id=user_id,
            root_node_id="node_root00000000",
            current_node_id="node_root00000000",
            nodes=nodes,
            scenario_id=version_set.scenario_id,
            domain=version_set.domain.value,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            total_decisions=0,
            max_depth=1,
        )
        
        self._trees[tree.tree_id] = tree
        
        logger.info(
            f"Created version tree {tree.tree_id} with "
            f"{len(version_nodes)} version nodes (in-memory)"
        )
        
        return tree
    
    async def record_decision(
        self,
        tree_id: str,
        node_id: str,
        option: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> DecisionRecord:
        """
        记录用户决策
        
        Args:
            tree_id: 版本树 ID
            node_id: 当前节点 ID
            option: 用户选择的选项
            context: 决策上下文
            
        Returns:
            决策记录
        """
        if self._persist and self._repository:
            # 获取节点信息
            node = await self._repository.get_node(node_id)
            if not node:
                raise ValueError(f"Node not found: {node_id}")
            
            tree = await self._repository.get_tree(tree_id)
            if not tree:
                raise ValueError(f"Tree not found: {tree_id}")
            
            # 记录决策
            record = await self._repository.record_decision(
                user_id=tree.user_id,
                tree_id=tree_id,
                node_id=node_id,
                decision_point=node.decision_point or "版本选择",
                options_presented=node.children if node.children else [node.version_id],
                option_selected=option,
                context_snapshot=context,
            )
            
            # 更新当前节点位置
            new_current = option if option in tree.nodes else node_id
            await self._repository.update_current_node(tree_id, new_current)
            
            logger.info(
                f"Recorded decision in tree {tree_id}: "
                f"node={node_id}, selected={option} (persisted)"
            )
            
            return record
        else:
            # 内存模式
            return await self._record_decision_in_memory(tree_id, node_id, option, context)
    
    async def _record_decision_in_memory(
        self,
        tree_id: str,
        node_id: str,
        option: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> DecisionRecord:
        """内存模式下记录决策"""
        tree = self._trees.get(tree_id)
        if not tree:
            raise ValueError(f"Tree not found: {tree_id}")
        
        node = tree.nodes.get(node_id)
        if not node:
            raise ValueError(f"Node not found: {node_id}")
        
        # 创建决策记录
        record = DecisionRecord(
            record_id=f"dr_{uuid.uuid4().hex[:12]}",
            user_id=tree.user_id,
            tree_id=tree_id,
            node_id=node_id,
            decision_point=node.decision_point or "版本选择",
            options_presented=node.children if node.children else [node.version_id],
            option_selected=option,
            context_snapshot=context or {},
            created_at=datetime.now(),
        )
        
        self._decisions.append(record)
        
        # 更新树状态
        node.selected_option = option
        node.decision_time = datetime.now()
        tree.current_node_id = option if option in tree.nodes else node_id
        tree.updated_at = datetime.now()
        tree.total_decisions += 1
        
        return record
    
    async def get_tree(self, tree_id: str) -> Optional[VersionTree]:
        """获取版本树"""
        if self._persist and self._repository:
            return await self._repository.get_tree(tree_id)
        return self._trees.get(tree_id)
    
    async def get_user_trees(
        self, 
        user_id: str,
        domain: Optional[str] = None,
    ) -> List[VersionTree]:
        """获取用户的所有版本树"""
        if self._persist and self._repository:
            return await self._repository.get_user_trees(user_id, domain)
        
        trees = [t for t in self._trees.values() if t.user_id == user_id]
        if domain:
            trees = [t for t in trees if t.domain == domain]
        return trees
    
    async def get_current_path(self, tree_id: str) -> TreeTraversalPath:
        """
        获取当前路径
        
        从根节点到当前节点的完整路径。
        """
        if self._persist and self._repository:
            tree = await self._repository.get_tree(tree_id)
            if not tree:
                raise ValueError(f"Tree not found: {tree_id}")
            path = await self._repository.get_path_to_node(tree_id, tree.current_node_id)
            if path:
                return path
            raise ValueError(f"Path not found for tree: {tree_id}")
        
        # 内存模式
        tree = self._trees.get(tree_id)
        if not tree:
            raise ValueError(f"Tree not found: {tree_id}")
        
        path: List[str] = []
        decisions: List[str] = []
        
        # 从当前节点向上遍历
        current_id = tree.current_node_id
        while current_id:
            path.insert(0, current_id)
            node = tree.nodes.get(current_id)
            if node and node.selected_option:
                decisions.insert(0, node.selected_option)
            current_id = node.parent_id if node else None
        
        return TreeTraversalPath(
            tree_id=tree_id,
            path=path,
            decisions=decisions,
            total_depth=len(path) - 1,
        )
    
    async def add_branch(
        self,
        tree_id: str,
        parent_node_id: str,
        version: LifeVersion,
    ) -> TreeNode:
        """
        添加分支节点
        
        Args:
            tree_id: 版本树 ID
            parent_node_id: 父节点 ID
            version: 新版本
            
        Returns:
            新创建的节点
        """
        if self._persist and self._repository:
            node = await self._repository.add_node(
                tree_id=tree_id,
                parent_id=parent_node_id,
                version_id=version.version_id,
            )
            if not node:
                raise ValueError("Failed to add branch - constraints exceeded")
            
            logger.info(
                f"Added branch to tree {tree_id}: "
                f"parent={parent_node_id}, new={node.node_id} (persisted)"
            )
            return node
        
        # 内存模式
        return await self._add_branch_in_memory(tree_id, parent_node_id, version)
    
    async def _add_branch_in_memory(
        self,
        tree_id: str,
        parent_node_id: str,
        version: LifeVersion,
    ) -> TreeNode:
        """内存模式下添加分支"""
        tree = self._trees.get(tree_id)
        if not tree:
            raise ValueError(f"Tree not found: {tree_id}")
        
        parent = tree.nodes.get(parent_node_id)
        if not parent:
            raise ValueError(f"Parent node not found: {parent_node_id}")
        
        # 检查约束
        if len(parent.children) >= TREE_CONSTRAINTS["max_children_per_node"]:
            raise ValueError("Max children per node reached")
        
        if len(tree.nodes) >= TREE_CONSTRAINTS["max_nodes"]:
            raise ValueError("Max nodes per tree reached")
        
        # 创建新节点
        new_node = TreeNode(
            node_id=f"node_{uuid.uuid4().hex[:12]}",
            parent_id=parent_node_id,
            version_id=version.version_id,
        )
        
        # 更新树
        parent.children.append(new_node.node_id)
        tree.nodes[new_node.node_id] = new_node
        tree.updated_at = datetime.now()
        
        # 更新深度
        depth = self._calculate_node_depth(tree, new_node.node_id)
        tree.max_depth = max(tree.max_depth, depth)
        
        return new_node
    
    def _calculate_node_depth(self, tree: VersionTree, node_id: str) -> int:
        """计算节点深度"""
        depth = 0
        current = tree.nodes.get(node_id)
        while current and current.parent_id:
            depth += 1
            current = tree.nodes.get(current.parent_id)
        return depth
    
    async def get_decisions_for_tree(
        self, 
        tree_id: str,
    ) -> List[DecisionRecord]:
        """获取树的所有决策记录"""
        if self._persist and self._repository:
            tree = await self._repository.get_tree(tree_id)
            if tree:
                return await self._repository.get_user_decisions(
                    tree.user_id, tree_id
                )
            return []
        return [d for d in self._decisions if d.tree_id == tree_id]
    
    async def delete_tree(self, tree_id: str) -> bool:
        """删除版本树"""
        if self._persist and self._repository:
            success = await self._repository.delete_tree(tree_id)
            if success:
                logger.info(f"Deleted tree {tree_id} (persisted)")
            return success
        
        if tree_id in self._trees:
            del self._trees[tree_id]
            # 删除相关决策记录
            self._decisions = [d for d in self._decisions if d.tree_id != tree_id]
            logger.info(f"Deleted tree {tree_id} (in-memory)")
            return True
        return False
    
    # 测试辅助方法
    def reset(self) -> None:
        """重置状态（用于测试）"""
        self._trees.clear()
        self._decisions.clear()


# =============================================================================
# 便捷函数
# =============================================================================

_service: Optional[VersionTreeService] = None


def get_version_tree_service(persist: bool = True) -> VersionTreeService:
    """获取版本树服务单例"""
    global _service
    if _service is None:
        _service = VersionTreeService(persist=persist)
    return _service
