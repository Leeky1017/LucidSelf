"""
Engine Registry Constraints

引擎注册表约束规则验证。
对照文档:
- docs/ls_engine_architecture_v3.md §4.6
- docs/数据契约_Schema定义规范_v1.md §9.5
"""

import re
from typing import Optional

from backend.core.contracts.engine_models import (
    EngineDescriptor,
    ENGINE_KINDS,
    SUPPORTED_SYSTEMS,
    ENGINE_REGISTRY_CONSTRAINTS,
)

# 引擎ID正则模式
ENGINE_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_-]*$")

# 版本号正则模式 (semver)
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")


def validate_engine_id(engine_id: str) -> Optional[str]:
    """验证引擎ID格式
    
    约束C1: engine_id 必须符合 ^[a-z][a-z0-9_-]*$
    
    Args:
        engine_id: 引擎ID
        
    Returns:
        错误信息，如果有效返回 None
    """
    if not engine_id:
        return "engine_id cannot be empty"
    if not ENGINE_ID_PATTERN.match(engine_id):
        return f"engine_id '{engine_id}' must match pattern ^[a-z][a-z0-9_-]*$"
    return None


def validate_version(version: str) -> Optional[str]:
    """验证版本号格式
    
    约束C2: version 必须符合 semver ^\\d+\\.\\d+\\.\\d+$
    
    Args:
        version: 版本号
        
    Returns:
        错误信息，如果有效返回 None
    """
    if not version:
        return "version cannot be empty"
    if not VERSION_PATTERN.match(version):
        return f"version '{version}' must match semver pattern (e.g., 1.0.0)"
    return None


def validate_supported_systems(supported_systems: list[str]) -> Optional[str]:
    """验证支持的体系列表
    
    约束C3: supported_systems 不能为空列表
    
    Args:
        supported_systems: 体系列表
        
    Returns:
        错误信息，如果有效返回 None
    """
    if not supported_systems:
        return "supported_systems cannot be empty"
    
    invalid = [s for s in supported_systems if s not in SUPPORTED_SYSTEMS]
    if invalid:
        return f"Invalid systems: {invalid}. Valid: {SUPPORTED_SYSTEMS}"
    
    return None


def validate_default_weight(weight: float) -> Optional[str]:
    """验证默认权重
    
    约束C4: default_weight 范围 0.0 ~ 10.0
    
    Args:
        weight: 权重值
        
    Returns:
        错误信息，如果有效返回 None
    """
    if weight < 0.0 or weight > 10.0:
        return f"default_weight {weight} must be between 0.0 and 10.0"
    return None


def validate_status(status: str) -> Optional[str]:
    """验证状态
    
    约束C5: status 只能是 active/experimental/deprecated
    
    Args:
        status: 状态值
        
    Returns:
        错误信息，如果有效返回 None
    """
    valid_statuses = {"active", "experimental", "deprecated"}
    if status not in valid_statuses:
        return f"status '{status}' must be one of {valid_statuses}"
    return None


def validate_kind(kind: str) -> Optional[str]:
    """验证引擎类型
    
    Args:
        kind: 引擎类型
        
    Returns:
        错误信息，如果有效返回 None
    """
    if kind not in ENGINE_KINDS:
        return f"kind '{kind}' must be one of {ENGINE_KINDS}"
    return None


def validate_engine_descriptor(descriptor: EngineDescriptor) -> list[str]:
    """验证引擎描述符的所有约束
    
    检查约束 C1-C5:
    - C1: engine_id 必须符合 ^[a-z][a-z0-9_]*$
    - C2: version 必须符合 semver
    - C3: supported_systems 不能为空列表
    - C4: default_weight 范围 0.0 ~ 10.0
    - C5: status 只能是 active/experimental/deprecated
    
    Args:
        descriptor: 引擎描述符
        
    Returns:
        违规列表，空列表表示全部通过
    """
    violations = []
    
    # C1: engine_id
    error = validate_engine_id(descriptor.engine_id)
    if error:
        violations.append(f"C1: {error}")
    
    # C2: version
    error = validate_version(descriptor.version)
    if error:
        violations.append(f"C2: {error}")
    
    # C3: supported_systems
    error = validate_supported_systems(descriptor.supported_systems)
    if error:
        violations.append(f"C3: {error}")
    
    # C4: default_weight
    error = validate_default_weight(descriptor.default_weight)
    if error:
        violations.append(f"C4: {error}")
    
    # C5: status
    status_value = descriptor.status.value if hasattr(descriptor.status, 'value') else descriptor.status
    error = validate_status(status_value)
    if error:
        violations.append(f"C5: {error}")
    
    # 验证 kind
    error = validate_kind(descriptor.kind)
    if error:
        violations.append(f"kind: {error}")
    
    return violations


def validate_engine_id_in_registry(
    engine_id: str,
    registry_validator: callable
) -> Optional[str]:
    """验证引擎ID是否存在于注册表
    
    约束C6/C7: PreferenceManager/FusionEngine/ConfigFactor/ConfigRuleDefinition
    引用的 engine_id 必须存在于注册表
    
    Args:
        engine_id: 要验证的引擎ID
        registry_validator: 验证函数，接收engine_id返回bool
        
    Returns:
        错误信息，如果有效返回 None
    """
    if not registry_validator(engine_id):
        return f"engine_id '{engine_id}' not found in registry"
    return None


# 导出约束规则列表（与 contracts.engine_models 对齐）
CONSTRAINT_DESCRIPTIONS = {
    "C1": "engine_id 必须符合 ^[a-z][a-z0-9_-]*$",
    "C2": "version 必须符合 semver ^\\d+\\.\\d+\\.\\d+$",
    "C3": "supported_systems 不能为空列表",
    "C4": "default_weight 范围 0.0 ~ 10.0",
    "C5": "status 只能是 active/experimental/deprecated",
    "C6": "PreferenceManager 和 FusionEngine 只接受已注册的 engine_id",
    "C7": "ConfigFactor 和 ConfigRuleDefinition 的 engine_id 必须存在于注册表",
    "C8": "depends_on 字段引用的引擎必须存在于注册表",
}
