"""
EngineManager Tests

测试引擎管理器的 CRUD、查询、状态管理、依赖验证和持久化功能。
"""

import json
import pytest
import tempfile
from pathlib import Path
from datetime import datetime

from backend.core.contracts.engine_models import EngineDescriptor
from backend.core.engines.manager import EngineManager, VALID_STATUS_TRANSITIONS
from backend.core.engines.exceptions import (
    EngineNotFoundError,
    EngineAlreadyRegisteredError,
    EngineStatusTransitionError,
    EngineDependencyError,
    EngineRegistryIOError,
)


@pytest.fixture
def temp_registry_path():
    """创建临时注册表文件"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump([], f)
        return Path(f.name)


@pytest.fixture
def manager(temp_registry_path):
    """创建使用临时文件的管理器"""
    return EngineManager(registry_path=str(temp_registry_path))


@pytest.fixture
def sample_calculator():
    """示例 Calculator 引擎"""
    return EngineDescriptor(
        engine_id="bazi_calculator",
        kind="calculator",
        supported_dimensions=["事业", "财富", "婚姻", "健康"],
        supported_systems=["bazi"],
        default_weight=1.0,
        status="active",
        owner_team="engine",
        version="1.0.0",
    )


@pytest.fixture
def sample_semantic():
    """示例 Semantic 引擎"""
    return EngineDescriptor(
        engine_id="bazi_semantic",
        kind="semantic",
        supported_dimensions=["事业", "财富"],
        supported_systems=["bazi"],
        default_weight=1.0,
        status="active",
        owner_team="content",
        version="1.0.0",
    )


@pytest.fixture
def sample_fusion():
    """示例 Fusion 引擎（有依赖）"""
    return EngineDescriptor(
        engine_id="bazi_fusion",
        kind="fusion",
        supported_dimensions=["事业", "财富"],
        supported_systems=["bazi"],
        depends_on=["bazi_calculator", "bazi_semantic"],
        default_weight=1.5,
        status="active",
        owner_team="engine",
        version="1.0.0",
    )


class TestEngineManagerCRUD:
    """测试 CRUD 操作"""
    
    def test_register_engine_success(self, manager, sample_calculator):
        """测试注册引擎成功"""
        manager.register_engine(sample_calculator)
        assert manager.validate_engine_id("bazi_calculator")
        assert len(manager) == 1
    
    def test_register_duplicate_raises_error(self, manager, sample_calculator):
        """测试重复注册抛出异常"""
        manager.register_engine(sample_calculator)
        with pytest.raises(EngineAlreadyRegisteredError) as exc_info:
            manager.register_engine(sample_calculator)
        assert exc_info.value.engine_id == "bazi_calculator"
    
    def test_unregister_engine_success(self, manager, sample_calculator):
        """测试注销引擎成功"""
        manager.register_engine(sample_calculator)
        manager.unregister_engine("bazi_calculator")
        assert not manager.validate_engine_id("bazi_calculator")
        assert len(manager) == 0
    
    def test_unregister_nonexistent_raises_error(self, manager):
        """测试注销不存在的引擎抛出异常"""
        with pytest.raises(EngineNotFoundError) as exc_info:
            manager.unregister_engine("nonexistent")
        assert exc_info.value.engine_id == "nonexistent"
    
    def test_get_engine_success(self, manager, sample_calculator):
        """测试获取引擎成功"""
        manager.register_engine(sample_calculator)
        engine = manager.get_engine("bazi_calculator")
        assert engine.engine_id == "bazi_calculator"
        assert engine.kind == "calculator"
    
    def test_get_engine_not_found(self, manager):
        """测试获取不存在的引擎"""
        with pytest.raises(EngineNotFoundError):
            manager.get_engine("nonexistent")
    
    def test_list_engines(self, manager, sample_calculator, sample_semantic):
        """测试列出所有引擎"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_semantic)
        engines = manager.list_engines()
        assert len(engines) == 2
        engine_ids = [e.engine_id for e in engines]
        assert "bazi_calculator" in engine_ids
        assert "bazi_semantic" in engine_ids


class TestEngineManagerQuery:
    """测试查询与过滤"""
    
    def test_get_active_engines(self, manager, sample_calculator, sample_semantic):
        """测试获取活跃引擎"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_semantic)
        active = manager.get_active_engines()
        assert len(active) == 2
    
    def test_get_active_engines_by_kind(self, manager, sample_calculator, sample_semantic):
        """测试按类型过滤活跃引擎"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_semantic)
        calculators = manager.get_active_engines(kind="calculator")
        assert len(calculators) == 1
        assert calculators[0].engine_id == "bazi_calculator"
    
    def test_get_active_engines_excludes_deprecated(self, manager, sample_calculator):
        """测试活跃引擎排除已废弃的"""
        manager.register_engine(sample_calculator)
        manager.update_engine_status("bazi_calculator", "deprecated")
        active = manager.get_active_engines()
        assert len(active) == 0
    
    def test_get_engines_by_system(self, manager, sample_calculator):
        """测试按体系过滤引擎"""
        manager.register_engine(sample_calculator)
        
        # 添加一个占星引擎
        astro = EngineDescriptor(
            engine_id="astro_calculator",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["astro"],
            owner_team="engine",
            version="1.0.0",
        )
        manager.register_engine(astro)
        
        bazi_engines = manager.get_engines_by_system("bazi")
        assert len(bazi_engines) == 1
        assert bazi_engines[0].engine_id == "bazi_calculator"
    
    def test_validate_engine_id_exists(self, manager, sample_calculator):
        """测试验证存在的引擎ID"""
        manager.register_engine(sample_calculator)
        assert manager.validate_engine_id("bazi_calculator") is True
    
    def test_validate_engine_id_not_exists(self, manager):
        """测试验证不存在的引擎ID"""
        assert manager.validate_engine_id("nonexistent") is False


class TestEngineManagerStatus:
    """测试状态管理"""
    
    def test_update_status_active_to_deprecated(self, manager, sample_calculator):
        """测试 active -> deprecated"""
        manager.register_engine(sample_calculator)
        manager.update_engine_status("bazi_calculator", "deprecated")
        engine = manager.get_engine("bazi_calculator")
        assert engine.status.value == "deprecated"
    
    def test_update_status_experimental_to_active(self, manager):
        """测试 experimental -> active"""
        exp_engine = EngineDescriptor(
            engine_id="test_engine",
            kind="calculator",
            supported_dimensions=["事业"],
            supported_systems=["bazi"],
            status="experimental",
            owner_team="engine",
            version="1.0.0",
        )
        manager.register_engine(exp_engine)
        manager.update_engine_status("test_engine", "active")
        engine = manager.get_engine("test_engine")
        assert engine.status.value == "active"
    
    def test_update_status_deprecated_to_experimental(self, manager, sample_calculator):
        """测试 deprecated -> experimental (reactivation)"""
        manager.register_engine(sample_calculator)
        manager.update_engine_status("bazi_calculator", "deprecated")
        manager.update_engine_status("bazi_calculator", "experimental")
        engine = manager.get_engine("bazi_calculator")
        assert engine.status.value == "experimental"
    
    def test_update_status_deprecated_to_active_raises_error(self, manager, sample_calculator):
        """测试 deprecated -> active 禁止"""
        manager.register_engine(sample_calculator)
        manager.update_engine_status("bazi_calculator", "deprecated")
        with pytest.raises(EngineStatusTransitionError) as exc_info:
            manager.update_engine_status("bazi_calculator", "active")
        assert exc_info.value.current_status == "deprecated"
        assert exc_info.value.target_status == "active"
    
    def test_update_status_active_to_experimental_raises_error(self, manager, sample_calculator):
        """测试 active -> experimental 禁止"""
        manager.register_engine(sample_calculator)
        with pytest.raises(EngineStatusTransitionError):
            manager.update_engine_status("bazi_calculator", "experimental")
    
    def test_update_status_same_status_noop(self, manager, sample_calculator):
        """测试更新为相同状态无操作"""
        manager.register_engine(sample_calculator)
        manager.update_engine_status("bazi_calculator", "active")
        engine = manager.get_engine("bazi_calculator")
        assert engine.status.value == "active"
    
    def test_update_metrics(self, manager, sample_calculator):
        """测试更新执行时间指标"""
        manager.register_engine(sample_calculator)
        manager.update_engine_metrics("bazi_calculator", 10.0)
        engine = manager.get_engine("bazi_calculator")
        assert engine.avg_execution_time_ms == 10.0
        
        # 滑动平均
        manager.update_engine_metrics("bazi_calculator", 20.0)
        engine = manager.get_engine("bazi_calculator")
        # 0.9 * 10.0 + 0.1 * 20.0 = 11.0
        assert abs(engine.avg_execution_time_ms - 11.0) < 0.001


class TestEngineManagerDependencies:
    """测试依赖验证"""
    
    def test_validate_dependencies_all_satisfied(
        self, manager, sample_calculator, sample_semantic, sample_fusion
    ):
        """测试依赖全部满足"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_semantic)
        manager.register_engine(sample_fusion)
        
        missing = manager.validate_dependencies("bazi_fusion")
        assert missing == []
    
    def test_validate_dependencies_missing(self, manager, sample_fusion):
        """测试检测缺失依赖"""
        manager.register_engine(sample_fusion)
        missing = manager.validate_dependencies("bazi_fusion")
        assert "bazi_calculator" in missing
        assert "bazi_semantic" in missing
    
    def test_validate_dependencies_partial(self, manager, sample_calculator, sample_fusion):
        """测试部分依赖缺失"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_fusion)
        missing = manager.validate_dependencies("bazi_fusion")
        assert "bazi_semantic" in missing
        assert "bazi_calculator" not in missing
    
    def test_ensure_dependencies_success(
        self, manager, sample_calculator, sample_semantic, sample_fusion
    ):
        """测试确保依赖满足成功"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_semantic)
        manager.register_engine(sample_fusion)
        
        # 不应抛出异常
        manager.ensure_dependencies("bazi_fusion")
    
    def test_ensure_dependencies_raises_error(self, manager, sample_fusion):
        """测试确保依赖不满足抛出异常"""
        manager.register_engine(sample_fusion)
        with pytest.raises(EngineDependencyError) as exc_info:
            manager.ensure_dependencies("bazi_fusion")
        assert "bazi_calculator" in exc_info.value.missing_dependencies
    
    def test_validate_all_dependencies(
        self, manager, sample_calculator, sample_fusion
    ):
        """测试验证所有引擎依赖"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_fusion)
        
        result = manager.validate_all_dependencies()
        assert "bazi_fusion" in result
        assert "bazi_semantic" in result["bazi_fusion"]
        assert "bazi_calculator" not in result  # calculator 无依赖


class TestEngineManagerPersistence:
    """测试持久化"""
    
    def test_save_and_load_registry(self, temp_registry_path, sample_calculator):
        """测试保存和加载注册表"""
        # 创建管理器并注册引擎
        manager1 = EngineManager(registry_path=str(temp_registry_path))
        manager1.register_engine(sample_calculator)
        manager1._save_registry()
        
        # 创建新管理器并加载
        manager2 = EngineManager(registry_path=str(temp_registry_path))
        assert manager2.validate_engine_id("bazi_calculator")
        engine = manager2.get_engine("bazi_calculator")
        assert engine.kind == "calculator"
    
    def test_load_empty_registry(self, temp_registry_path):
        """测试加载空注册表"""
        manager = EngineManager(registry_path=str(temp_registry_path))
        assert len(manager) == 0
    
    def test_load_nonexistent_file(self):
        """测试加载不存在的文件"""
        manager = EngineManager(registry_path="/nonexistent/path/registry.json")
        assert len(manager) == 0
    
    def test_reload_registry(self, temp_registry_path, sample_calculator, sample_semantic):
        """测试重新加载注册表"""
        manager = EngineManager(registry_path=str(temp_registry_path))
        manager.register_engine(sample_calculator)
        manager._save_registry()
        
        # 内存中添加更多
        manager.register_engine(sample_semantic)
        assert len(manager) == 2
        
        # 重新加载丢弃内存修改
        manager.reload_registry()
        assert len(manager) == 1
        assert manager.validate_engine_id("bazi_calculator")
        assert not manager.validate_engine_id("bazi_semantic")
    
    def test_save_creates_directory(self):
        """测试保存时自动创建目录"""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "subdir" / "registry.json"
            manager = EngineManager(registry_path=str(path))
            
            engine = EngineDescriptor(
                engine_id="test_engine",
                kind="calculator",
                supported_dimensions=["事业"],
                supported_systems=["bazi"],
                owner_team="engine",
                version="1.0.0",
            )
            manager.register_engine(engine)
            manager._save_registry()
            
            assert path.exists()


class TestEngineManagerUtilities:
    """测试工具方法"""
    
    def test_len(self, manager, sample_calculator, sample_semantic):
        """测试 __len__"""
        assert len(manager) == 0
        manager.register_engine(sample_calculator)
        assert len(manager) == 1
        manager.register_engine(sample_semantic)
        assert len(manager) == 2
    
    def test_contains(self, manager, sample_calculator):
        """测试 __contains__"""
        assert "bazi_calculator" not in manager
        manager.register_engine(sample_calculator)
        assert "bazi_calculator" in manager
    
    def test_iter(self, manager, sample_calculator, sample_semantic):
        """测试 __iter__"""
        manager.register_engine(sample_calculator)
        manager.register_engine(sample_semantic)
        
        engine_ids = [e.engine_id for e in manager]
        assert len(engine_ids) == 2
        assert "bazi_calculator" in engine_ids
        assert "bazi_semantic" in engine_ids
