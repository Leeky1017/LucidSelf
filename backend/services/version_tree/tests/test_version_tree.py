"""
Tests for Version Tree Service

对照文档: docs/ls_roadmap_executable.md §五、Phase 4: 版本树与决策追踪
"""

import pytest

from backend.core.contracts.life_version_models import (
    LifeVersion,
    LifeVersionSet,
)
from backend.core.contracts.unified_dimensions import LifeDomain
from backend.core.contracts.version_tree_models import (
    DecisionRecord,
    TreeNode,
    VersionTree,
)
from backend.services.version_tree.service import VersionTreeService


@pytest.fixture
def tree_service():
    service = VersionTreeService()
    yield service
    service.reset()


@pytest.fixture
def sample_version_set():
    """模拟版本集合"""
    versions = [
        LifeVersion(
            version_id="ver_t1234567890a",
            title="稳健版",
            subtitle="稳定发展策略",
            strategy=["保持现有优势"],
            expected_outcomes={"income_ceiling": 0.5, "stability": 0.8},
            confidence=0.7,
        ),
        LifeVersion(
            version_id="ver_t2345678901b",
            title="进取版",
            subtitle="积极发展策略",
            strategy=["积极拓展"],
            expected_outcomes={"income_ceiling": 0.8, "stability": 0.4},
            confidence=0.7,
        ),
    ]
    
    return LifeVersionSet(
        set_id="vset_t123456789ab",
        user_id="user_001",
        scenario_id="scn_career",
        domain=LifeDomain.CAREER,
        versions=versions,
        comparison_axes=["income_ceiling", "stability"],
    )


class TestVersionTreeService:
    """VersionTreeService 测试"""
    
    @pytest.mark.asyncio
    async def test_create_tree(self, tree_service, sample_version_set):
        """测试创建版本树"""
        tree = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        assert isinstance(tree, VersionTree)
        assert tree.user_id == "user_001"
        assert tree.scenario_id == "scn_career"
    
    @pytest.mark.asyncio
    async def test_tree_has_version_nodes(self, tree_service, sample_version_set):
        """测试树包含版本节点"""
        tree = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        # 应有根节点 + 2个版本节点
        assert len(tree.nodes) == 3
        
        # 根节点应有2个子节点
        root = tree.nodes.get(tree.root_node_id)
        assert len(root.children) == 2
    
    @pytest.mark.asyncio
    async def test_record_decision(self, tree_service, sample_version_set):
        """测试记录决策"""
        tree = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        # 获取一个版本节点
        root = tree.nodes[tree.root_node_id]
        version_node_id = root.children[0]
        
        record = await tree_service.record_decision(
            tree_id=tree.tree_id,
            node_id=tree.root_node_id,
            option=version_node_id,
            context={"key": "value"},
        )
        
        assert isinstance(record, DecisionRecord)
        assert record.option_selected == version_node_id
        assert tree.total_decisions == 1
    
    @pytest.mark.asyncio
    async def test_get_tree(self, tree_service, sample_version_set):
        """测试获取版本树"""
        created = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        retrieved = await tree_service.get_tree(created.tree_id)
        
        assert retrieved is not None
        assert retrieved.tree_id == created.tree_id
    
    @pytest.mark.asyncio
    async def test_get_user_trees(self, tree_service, sample_version_set):
        """测试获取用户的版本树"""
        await tree_service.create_tree("user_001", sample_version_set)
        await tree_service.create_tree("user_001", sample_version_set)
        await tree_service.create_tree("user_002", sample_version_set)
        
        user1_trees = await tree_service.get_user_trees("user_001")
        user2_trees = await tree_service.get_user_trees("user_002")
        
        assert len(user1_trees) == 2
        assert len(user2_trees) == 1
    
    @pytest.mark.asyncio
    async def test_get_current_path(self, tree_service, sample_version_set):
        """测试获取当前路径"""
        tree = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        path = await tree_service.get_current_path(tree.tree_id)
        
        assert path.tree_id == tree.tree_id
        assert len(path.path) >= 1
    
    @pytest.mark.asyncio
    async def test_add_branch(self, tree_service, sample_version_set):
        """测试添加分支"""
        tree = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        root = tree.nodes[tree.root_node_id]
        first_child_id = root.children[0]
        
        new_version = LifeVersion(
            version_id="ver_newversion01",
            title="新版本",
            subtitle="新策略",
            strategy=["新策略"],
            expected_outcomes={"income_ceiling": 0.7},
            confidence=0.6,
        )
        
        new_node = await tree_service.add_branch(
            tree_id=tree.tree_id,
            parent_node_id=first_child_id,
            version=new_version,
        )
        
        assert isinstance(new_node, TreeNode)
        assert new_node.parent_id == first_child_id
        
        # 刷新树
        tree = await tree_service.get_tree(tree.tree_id)
        assert len(tree.nodes) == 4  # 根 + 2版本 + 1新节点
    
    @pytest.mark.asyncio
    async def test_delete_tree(self, tree_service, sample_version_set):
        """测试删除版本树"""
        tree = await tree_service.create_tree(
            user_id="user_001",
            version_set=sample_version_set,
        )
        
        result = await tree_service.delete_tree(tree.tree_id)
        assert result is True
        
        retrieved = await tree_service.get_tree(tree.tree_id)
        assert retrieved is None
