"""
Engine Registry Module

引擎注册表模块，提供统一的引擎管理功能。

对照文档:
- docs/ls_engine_architecture_v3.md §4.6
- docs/数据契约_Schema定义规范_v1.md §9.5

使用示例:
    from backend.core.engines import EngineManager, EngineDescriptor
    
    # 创建管理器（自动加载注册表）
    manager = EngineManager()
    
    # 注册新引擎
    descriptor = EngineDescriptor(
        engine_id="bazi_calculator",
        kind="calculator",
        supported_dimensions=["事业", "财富", "婚姻", "健康"],
        supported_systems=["bazi"],
        default_weight=1.0,
        status="active",
        owner_team="engine",
        version="1.0.0"
    )
    manager.register_engine(descriptor)
    
    # 查询引擎
    active = manager.get_active_engines(kind="calculator")
    
    # 保存注册表
    manager._save_registry()
"""

# 从 contracts 导入核心模型（避免重复定义）
from backend.core.contracts.engine_models import (
    EngineDescriptor,
    ENGINE_KINDS,
    SUPPORTED_SYSTEMS,
    ENGINE_REGISTRY_CONSTRAINTS,
)

# 导入管理器
from backend.core.engines.manager import EngineManager

# 导入异常
from backend.core.engines.exceptions import (
    EngineRegistryError,
    EngineNotFoundError,
    EngineAlreadyRegisteredError,
    EngineStatusTransitionError,
    InvalidEngineIdError,
    EngineDependencyError,
    EngineRegistryIOError,
)

# 导入约束验证
from backend.core.engines.constraints import (
    validate_engine_descriptor,
    validate_engine_id,
    validate_version,
    validate_supported_systems,
    validate_default_weight,
    validate_status,
    validate_kind,
    validate_engine_id_in_registry,
    CONSTRAINT_DESCRIPTIONS,
)

__all__ = [
    # 核心模型（来自 contracts）
    "EngineDescriptor",
    "ENGINE_KINDS",
    "SUPPORTED_SYSTEMS",
    "ENGINE_REGISTRY_CONSTRAINTS",
    
    # 管理器
    "EngineManager",
    
    # 异常
    "EngineRegistryError",
    "EngineNotFoundError",
    "EngineAlreadyRegisteredError",
    "EngineStatusTransitionError",
    "InvalidEngineIdError",
    "EngineDependencyError",
    "EngineRegistryIOError",
    
    # 约束验证
    "validate_engine_descriptor",
    "validate_engine_id",
    "validate_version",
    "validate_supported_systems",
    "validate_default_weight",
    "validate_status",
    "validate_kind",
    "validate_engine_id_in_registry",
    "CONSTRAINT_DESCRIPTIONS",
]
