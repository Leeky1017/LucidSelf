"""
Engine Manager

引擎注册表管理器，提供引擎的CRUD、查询、状态管理、依赖验证和持久化功能。
对照文档: 
- docs/ls_engine_architecture_v3.md §4.6
- docs/数据契约_Schema定义规范_v1.md §9.5
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from backend.core.contracts.engine_models import (
    EngineDescriptor,
    ENGINE_KINDS,
    SUPPORTED_SYSTEMS,
)
from backend.core.engines.exceptions import (
    EngineNotFoundError,
    EngineAlreadyRegisteredError,
    EngineStatusTransitionError,
    EngineDependencyError,
    EngineRegistryIOError,
)

logger = logging.getLogger(__name__)

# 状态迁移规则
# deprecated 不可直接回退到 active，必须先经过 experimental
VALID_STATUS_TRANSITIONS: dict[str, set[str]] = {
    "active": {"deprecated"},  # active 只能迁移到 deprecated
    "experimental": {"active", "deprecated"},  # experimental 可以迁移到 active 或 deprecated
    "deprecated": {"experimental"},  # deprecated 只能迁移到 experimental（reactivation）
}


class EngineManager:
    """
    引擎管理器 - 统一管理所有引擎的注册、查询、状态和持久化
    
    对照架构文档 §4.6 EngineManager
    """
    
    # 默认注册表文件路径
    DEFAULT_REGISTRY_PATH = "data/engines/registry.json"
    
    def __init__(self, registry_path: Optional[str] = None):
        """初始化引擎管理器
        
        Args:
            registry_path: 注册表文件路径，默认为 data/engines/registry.json
        """
        self.registry_path = Path(registry_path or self.DEFAULT_REGISTRY_PATH)
        self._registry: dict[str, EngineDescriptor] = {}
        self._load_registry()
    
    # =========================================================================
    # CRUD 操作
    # =========================================================================
    
    def register_engine(self, descriptor: EngineDescriptor) -> None:
        """注册新引擎
        
        Args:
            descriptor: 引擎描述符
            
        Raises:
            EngineAlreadyRegisteredError: 引擎ID已存在
        """
        if descriptor.engine_id in self._registry:
            raise EngineAlreadyRegisteredError(descriptor.engine_id)
        
        self._registry[descriptor.engine_id] = descriptor
        logger.info(f"Registered engine: {descriptor.engine_id} v{descriptor.version}")
    
    def unregister_engine(self, engine_id: str) -> None:
        """注销引擎
        
        Args:
            engine_id: 引擎ID
            
        Raises:
            EngineNotFoundError: 引擎不存在
        """
        if engine_id not in self._registry:
            raise EngineNotFoundError(engine_id)
        
        del self._registry[engine_id]
        logger.info(f"Unregistered engine: {engine_id}")
    
    def get_engine(self, engine_id: str) -> EngineDescriptor:
        """获取引擎描述符
        
        Args:
            engine_id: 引擎ID
            
        Returns:
            引擎描述符
            
        Raises:
            EngineNotFoundError: 引擎不存在
        """
        if engine_id not in self._registry:
            raise EngineNotFoundError(engine_id)
        return self._registry[engine_id]
    
    def list_engines(self) -> list[EngineDescriptor]:
        """列出所有引擎
        
        Returns:
            所有引擎描述符列表
        """
        return list(self._registry.values())
    
    # =========================================================================
    # 查询与过滤
    # =========================================================================
    
    def get_active_engines(self, kind: Optional[str] = None) -> list[EngineDescriptor]:
        """获取活跃引擎列表
        
        Args:
            kind: 可选，按引擎类型过滤 (calculator/semantic/rule/fusion)
            
        Returns:
            活跃引擎列表
        """
        engines = [
            e for e in self._registry.values()
            if e.status.value == "active"
        ]
        
        if kind:
            engines = [e for e in engines if e.kind == kind]
        
        return engines
    
    def get_engines_by_system(self, system: str) -> list[EngineDescriptor]:
        """按体系获取引擎列表
        
        Args:
            system: 体系名称 (bazi/ziwei/yijing/astro/tarot/dream/psychology)
            
        Returns:
            支持该体系的引擎列表
        """
        return [
            e for e in self._registry.values()
            if system in e.supported_systems
        ]
    
    def get_engines_by_kind(self, kind: str) -> list[EngineDescriptor]:
        """按类型获取引擎列表
        
        Args:
            kind: 引擎类型 (calculator/semantic/rule/fusion)
            
        Returns:
            该类型的引擎列表
        """
        return [
            e for e in self._registry.values()
            if e.kind == kind
        ]
    
    def validate_engine_id(self, engine_id: str) -> bool:
        """验证引擎ID是否存在于注册表
        
        Args:
            engine_id: 引擎ID
            
        Returns:
            True 如果存在，否则 False
        """
        return engine_id in self._registry
    
    # =========================================================================
    # 状态管理
    # =========================================================================
    
    def update_engine_status(self, engine_id: str, new_status: str) -> None:
        """更新引擎状态
        
        状态迁移规则:
        - active -> deprecated: 允许
        - experimental -> active: 允许
        - experimental -> deprecated: 允许
        - deprecated -> experimental: 允许 (reactivation)
        - deprecated -> active: 禁止 (必须先经过 experimental)
        - active -> experimental: 禁止
        
        Args:
            engine_id: 引擎ID
            new_status: 新状态
            
        Raises:
            EngineNotFoundError: 引擎不存在
            EngineStatusTransitionError: 非法状态迁移
        """
        if engine_id not in self._registry:
            raise EngineNotFoundError(engine_id)
        
        engine = self._registry[engine_id]
        current_status = engine.status.value
        
        # 检查是否是相同状态
        if current_status == new_status:
            return
        
        # 检查迁移是否合法
        valid_targets = VALID_STATUS_TRANSITIONS.get(current_status, set())
        if new_status not in valid_targets:
            raise EngineStatusTransitionError(engine_id, current_status, new_status)
        
        # 更新状态 - 创建新的描述符（Pydantic模型是不可变的，需要创建副本）
        updated_data = engine.model_dump()
        updated_data["status"] = new_status
        updated_data["updated_at"] = datetime.now()
        
        self._registry[engine_id] = EngineDescriptor(**updated_data)
        logger.info(f"Updated engine status: {engine_id} {current_status} -> {new_status}")
    
    def update_engine_metrics(self, engine_id: str, execution_time_ms: float) -> None:
        """更新引擎执行时间指标
        
        使用滑动平均更新 avg_execution_time_ms
        
        Args:
            engine_id: 引擎ID
            execution_time_ms: 本次执行时间（毫秒）
            
        Raises:
            EngineNotFoundError: 引擎不存在
        """
        if engine_id not in self._registry:
            raise EngineNotFoundError(engine_id)
        
        engine = self._registry[engine_id]
        updated_data = engine.model_dump()
        
        # 滑动平均计算
        current_avg = engine.avg_execution_time_ms
        if current_avg is None:
            updated_data["avg_execution_time_ms"] = execution_time_ms
        else:
            # 简单滑动平均，权重 0.9
            updated_data["avg_execution_time_ms"] = current_avg * 0.9 + execution_time_ms * 0.1
        
        updated_data["updated_at"] = datetime.now()
        self._registry[engine_id] = EngineDescriptor(**updated_data)
    
    # =========================================================================
    # 依赖验证
    # =========================================================================
    
    def validate_dependencies(self, engine_id: str) -> list[str]:
        """验证引擎依赖是否满足
        
        检查 depends_on 字段中的所有引擎是否都已注册
        
        Args:
            engine_id: 引擎ID
            
        Returns:
            缺失的依赖列表，空列表表示全部满足
            
        Raises:
            EngineNotFoundError: 引擎不存在
        """
        if engine_id not in self._registry:
            raise EngineNotFoundError(engine_id)
        
        engine = self._registry[engine_id]
        missing = []
        
        for dep_id in engine.depends_on:
            if dep_id not in self._registry:
                missing.append(dep_id)
        
        return missing
    
    def validate_all_dependencies(self) -> dict[str, list[str]]:
        """验证所有引擎的依赖
        
        Returns:
            字典，键为引擎ID，值为缺失的依赖列表
            只返回有缺失依赖的引擎
        """
        result = {}
        for engine_id in self._registry:
            missing = self.validate_dependencies(engine_id)
            if missing:
                result[engine_id] = missing
        return result
    
    def ensure_dependencies(self, engine_id: str) -> None:
        """确保引擎依赖满足，否则抛出异常
        
        Args:
            engine_id: 引擎ID
            
        Raises:
            EngineNotFoundError: 引擎不存在
            EngineDependencyError: 存在未满足的依赖
        """
        missing = self.validate_dependencies(engine_id)
        if missing:
            raise EngineDependencyError(engine_id, missing)
    
    # =========================================================================
    # 持久化
    # =========================================================================
    
    def _load_registry(self) -> None:
        """从文件加载注册表
        
        如果文件不存在，初始化为空注册表
        """
        if not self.registry_path.exists():
            logger.info(f"Registry file not found, starting with empty registry: {self.registry_path}")
            self._registry = {}
            return
        
        try:
            with open(self.registry_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self._registry = {}
            for item in data:
                descriptor = EngineDescriptor(**item)
                self._registry[descriptor.engine_id] = descriptor
            
            logger.info(f"Loaded {len(self._registry)} engines from {self.registry_path}")
        except json.JSONDecodeError as e:
            raise EngineRegistryIOError(
                str(self.registry_path), "load", f"Invalid JSON: {e}"
            )
        except Exception as e:
            raise EngineRegistryIOError(
                str(self.registry_path), "load", str(e)
            )
    
    def _save_registry(self) -> None:
        """保存注册表到文件
        
        会自动创建父目录
        """
        try:
            # 确保目录存在
            self.registry_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 序列化所有引擎
            data = [
                engine.model_dump(mode="json")
                for engine in self._registry.values()
            ]
            
            with open(self.registry_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            
            logger.info(f"Saved {len(self._registry)} engines to {self.registry_path}")
        except Exception as e:
            raise EngineRegistryIOError(
                str(self.registry_path), "save", str(e)
            )
    
    def reload_registry(self) -> None:
        """重新加载注册表
        
        丢弃内存中的修改，从文件重新加载
        """
        self._registry.clear()
        self._load_registry()
    
    # =========================================================================
    # 工具方法
    # =========================================================================
    
    def __len__(self) -> int:
        """返回注册的引擎数量"""
        return len(self._registry)
    
    def __contains__(self, engine_id: str) -> bool:
        """检查引擎是否已注册"""
        return engine_id in self._registry
    
    def __iter__(self):
        """迭代所有引擎"""
        return iter(self._registry.values())
