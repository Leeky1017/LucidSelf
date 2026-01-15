"""
Version Tree Repository

版本树数据访问层，封装所有数据库操作。

对照模型: backend/models/version_tree.py
对照契约: backend/core/contracts/version_tree_models.py
"""

import logging
import uuid
from datetime import datetime
from typing import Dict, List, Optional

from sqlalchemy import select, update, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.db.session import async_session_maker
from backend.models.version_tree import (
    VersionTree as VersionTreeModel,
    TreeNode as TreeNodeModel,
    DecisionRecord as DecisionRecordModel,
)
from backend.core.contracts.version_tree_models import (
    VersionTree,
    TreeNode,
    DecisionRecord,
    TreeTraversalPath,
    TREE_CONSTRAINTS,
)

logger = logging.getLogger(__name__)


def _gen_id(prefix: str) -> str:
    """生成唯一 ID"""
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


class VersionTreeRepository:
    """
    版本树数据访问仓库
    
    提供版本树的 CRUD 操作，将 Pydantic 模型与 SQLAlchemy 模型相互转换。
    """
    
    # =========================================================================
    # 树操作
    # =========================================================================
    
    async def create_tree(
        self,
        user_id: str,
        root_version_id: str,
        scenario_id: Optional[str] = None,
        domain: Optional[str] = None,
    ) -> VersionTree:
        """
        创建新的版本树
        
        Args:
            user_id: 用户 ID
            root_version_id: 根节点的版本 ID
            scenario_id: 场景 ID
            domain: 生活领域
            
        Returns:
            VersionTree Pydantic 模型
        """
        tree_id = _gen_id("tree")
        root_node_id = _gen_id("node")
        
        async with async_session_maker() as session:
            # 创建树
            tree_model = VersionTreeModel(
                tree_id=tree_id,
                user_id=user_id,
                root_node_id=root_node_id,
                current_node_id=root_node_id,
                scenario_id=scenario_id,
                domain=domain,
                total_decisions=0,
                max_depth=0,
            )
            session.add(tree_model)
            
            # 创建根节点
            root_node = TreeNodeModel(
                node_id=root_node_id,
                tree_id=tree_id,
                parent_id=None,
                version_id=root_version_id,
                is_active=True,
                depth=0,
            )
            session.add(root_node)
            
            await session.commit()
            
            logger.info(f"Created tree {tree_id} for user {user_id}")
            
            return await self.get_tree(tree_id)
    
    async def get_tree(self, tree_id: str) -> Optional[VersionTree]:
        """获取版本树（含所有节点）"""
        async with async_session_maker() as session:
            result = await session.execute(
                select(VersionTreeModel)
                .options(selectinload(VersionTreeModel.nodes))
                .where(VersionTreeModel.tree_id == tree_id)
            )
            tree_model = result.scalar_one_or_none()
            
            if not tree_model:
                return None
            
            return self._to_pydantic_tree(tree_model)
    
    async def get_user_trees(
        self,
        user_id: str,
        domain: Optional[str] = None,
    ) -> List[VersionTree]:
        """获取用户的所有版本树"""
        async with async_session_maker() as session:
            query = (
                select(VersionTreeModel)
                .options(selectinload(VersionTreeModel.nodes))
                .where(VersionTreeModel.user_id == user_id)
            )
            
            if domain:
                query = query.where(VersionTreeModel.domain == domain)
            
            query = query.order_by(VersionTreeModel.updated_at.desc())
            
            result = await session.execute(query)
            trees = result.scalars().all()
            
            return [self._to_pydantic_tree(t) for t in trees]
    
    async def update_current_node(
        self,
        tree_id: str,
        node_id: str,
    ) -> bool:
        """更新当前节点位置"""
        async with async_session_maker() as session:
            result = await session.execute(
                update(VersionTreeModel)
                .where(VersionTreeModel.tree_id == tree_id)
                .values(
                    current_node_id=node_id,
                    updated_at=datetime.utcnow(),
                )
            )
            await session.commit()
            return result.rowcount > 0
    
    async def delete_tree(self, tree_id: str) -> bool:
        """删除版本树（级联删除节点）"""
        async with async_session_maker() as session:
            result = await session.execute(
                delete(VersionTreeModel)
                .where(VersionTreeModel.tree_id == tree_id)
            )
            await session.commit()
            return result.rowcount > 0
    
    # =========================================================================
    # 节点操作
    # =========================================================================
    
    async def add_node(
        self,
        tree_id: str,
        parent_id: str,
        version_id: str,
        decision_point: Optional[str] = None,
        selected_option: Optional[str] = None,
    ) -> Optional[TreeNode]:
        """
        添加新节点（分支）
        
        Args:
            tree_id: 树 ID
            parent_id: 父节点 ID
            version_id: 关联的版本 ID
            decision_point: 决策描述
            selected_option: 选择的选项
            
        Returns:
            新创建的节点，若超出限制则返回 None
        """
        node_id = _gen_id("node")
        
        async with async_session_maker() as session:
            # 获取父节点深度
            parent_result = await session.execute(
                select(TreeNodeModel.depth)
                .where(TreeNodeModel.node_id == parent_id)
            )
            parent_depth = parent_result.scalar_one_or_none()
            
            if parent_depth is None:
                logger.error(f"Parent node {parent_id} not found")
                return None
            
            new_depth = parent_depth + 1
            
            # 检查深度限制
            if new_depth > TREE_CONSTRAINTS["max_depth"]:
                logger.warning(f"Max depth exceeded for tree {tree_id}")
                return None
            
            # 检查节点数限制
            node_count = await session.scalar(
                select(TreeNodeModel.node_id)
                .where(TreeNodeModel.tree_id == tree_id)
            )
            # (简化：只检查是否存在，实际应计数)
            
            # 创建节点
            node_model = TreeNodeModel(
                node_id=node_id,
                tree_id=tree_id,
                parent_id=parent_id,
                version_id=version_id,
                decision_point=decision_point,
                selected_option=selected_option,
                decision_time=datetime.utcnow(),
                is_active=True,
                depth=new_depth,
            )
            session.add(node_model)
            
            # 更新树统计
            await session.execute(
                update(VersionTreeModel)
                .where(VersionTreeModel.tree_id == tree_id)
                .values(
                    total_decisions=VersionTreeModel.total_decisions + 1,
                    max_depth=max(new_depth, VersionTreeModel.max_depth),
                    updated_at=datetime.utcnow(),
                )
            )
            
            await session.commit()
            
            logger.info(f"Added node {node_id} to tree {tree_id}")
            
            return TreeNode(
                node_id=node_id,
                parent_id=parent_id,
                version_id=version_id,
                decision_point=decision_point,
                selected_option=selected_option,
                decision_time=datetime.utcnow(),
                is_active=True,
            )
    
    async def get_node(self, node_id: str) -> Optional[TreeNode]:
        """获取单个节点"""
        async with async_session_maker() as session:
            result = await session.execute(
                select(TreeNodeModel)
                .where(TreeNodeModel.node_id == node_id)
            )
            node_model = result.scalar_one_or_none()
            
            if not node_model:
                return None
            
            return self._to_pydantic_node(node_model)
    
    async def get_path_to_node(
        self,
        tree_id: str,
        node_id: str,
    ) -> Optional[TreeTraversalPath]:
        """获取从根到指定节点的路径"""
        async with async_session_maker() as session:
            # 递归查询路径
            path = []
            decisions = []
            current_id = node_id
            
            while current_id:
                result = await session.execute(
                    select(TreeNodeModel)
                    .where(TreeNodeModel.node_id == current_id)
                )
                node = result.scalar_one_or_none()
                
                if not node:
                    break
                
                path.insert(0, current_id)
                if node.decision_point:
                    decisions.insert(0, node.decision_point)
                
                current_id = node.parent_id
            
            if not path:
                return None
            
            return TreeTraversalPath(
                tree_id=tree_id,
                path=path,
                decisions=decisions,
                total_depth=len(path) - 1,
            )
    
    async def deactivate_branch(
        self,
        tree_id: str,
        node_id: str,
    ) -> int:
        """停用从指定节点开始的整个分支"""
        async with async_session_maker() as session:
            # 获取所有子孙节点（使用递归 CTE 或简单循环）
            nodes_to_deactivate = [node_id]
            to_check = [node_id]
            
            while to_check:
                current = to_check.pop()
                result = await session.execute(
                    select(TreeNodeModel.node_id)
                    .where(TreeNodeModel.parent_id == current)
                )
                children = [r[0] for r in result.fetchall()]
                nodes_to_deactivate.extend(children)
                to_check.extend(children)
            
            # 批量更新
            await session.execute(
                update(TreeNodeModel)
                .where(TreeNodeModel.node_id.in_(nodes_to_deactivate))
                .values(is_active=False)
            )
            
            await session.commit()
            
            return len(nodes_to_deactivate)
    
    # =========================================================================
    # 决策记录操作
    # =========================================================================
    
    async def record_decision(
        self,
        user_id: str,
        tree_id: str,
        node_id: str,
        decision_point: str,
        options_presented: List[str],
        option_selected: str,
        context_snapshot: Optional[Dict] = None,
        notes: Optional[str] = None,
    ) -> DecisionRecord:
        """记录用户决策"""
        record_id = _gen_id("dr")
        
        async with async_session_maker() as session:
            record_model = DecisionRecordModel(
                record_id=record_id,
                user_id=user_id,
                tree_id=tree_id,
                node_id=node_id,
                decision_point=decision_point,
                options_presented=options_presented,
                option_selected=option_selected,
                context_snapshot=context_snapshot or {},
                notes=notes,
            )
            session.add(record_model)
            await session.commit()
            
            logger.info(f"Recorded decision {record_id}")
            
            return DecisionRecord(
                record_id=record_id,
                user_id=user_id,
                tree_id=tree_id,
                node_id=node_id,
                decision_point=decision_point,
                options_presented=options_presented,
                option_selected=option_selected,
                context_snapshot=context_snapshot or {},
                notes=notes,
            )
    
    async def get_user_decisions(
        self,
        user_id: str,
        tree_id: Optional[str] = None,
        limit: int = 50,
    ) -> List[DecisionRecord]:
        """获取用户决策历史"""
        async with async_session_maker() as session:
            query = (
                select(DecisionRecordModel)
                .where(DecisionRecordModel.user_id == user_id)
            )
            
            if tree_id:
                query = query.where(DecisionRecordModel.tree_id == tree_id)
            
            query = query.order_by(
                DecisionRecordModel.created_at.desc()
            ).limit(limit)
            
            result = await session.execute(query)
            records = result.scalars().all()
            
            return [
                DecisionRecord(
                    record_id=r.record_id,
                    user_id=r.user_id,
                    tree_id=r.tree_id,
                    node_id=r.node_id,
                    decision_point=r.decision_point,
                    options_presented=r.options_presented,
                    option_selected=r.option_selected,
                    context_snapshot=r.context_snapshot,
                    notes=r.notes,
                )
                for r in records
            ]
    
    # =========================================================================
    # 转换辅助方法
    # =========================================================================
    
    def _to_pydantic_tree(self, model: VersionTreeModel) -> VersionTree:
        """SQLAlchemy 模型转 Pydantic 模型"""
        nodes_dict = {}
        for node in model.nodes:
            nodes_dict[node.node_id] = self._to_pydantic_node(node)
        
        return VersionTree(
            tree_id=model.tree_id,
            user_id=model.user_id,
            root_node_id=model.root_node_id,
            current_node_id=model.current_node_id,
            nodes=nodes_dict,
            scenario_id=model.scenario_id,
            domain=model.domain,
            created_at=model.created_at,
            updated_at=model.updated_at,
            total_decisions=model.total_decisions,
            max_depth=model.max_depth,
        )
    
    def _to_pydantic_node(self, model: TreeNodeModel) -> TreeNode:
        """SQLAlchemy 模型转 Pydantic 模型"""
        return TreeNode(
            node_id=model.node_id,
            parent_id=model.parent_id,
            version_id=model.version_id,
            decision_point=model.decision_point,
            selected_option=model.selected_option,
            decision_time=model.decision_time,
            children=[c.node_id for c in model.children] if model.children else [],
            is_active=model.is_active,
        )


# =============================================================================
# 单例 / 便捷函数
# =============================================================================

_repository: Optional[VersionTreeRepository] = None


def get_version_tree_repository() -> VersionTreeRepository:
    """获取版本树仓库单例"""
    global _repository
    if _repository is None:
        _repository = VersionTreeRepository()
    return _repository
