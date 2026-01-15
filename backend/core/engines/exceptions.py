"""
Engine Registry Exceptions

引擎注册表相关的异常定义。
对照文档: docs/ls_engine_architecture_v3.md §4.6
"""


class EngineRegistryError(Exception):
    """引擎注册表基类异常"""
    pass


class EngineNotFoundError(EngineRegistryError):
    """引擎未找到异常
    
    当尝试访问不存在的引擎时抛出。
    """
    def __init__(self, engine_id: str):
        self.engine_id = engine_id
        super().__init__(f"Engine not found: {engine_id}")


class EngineAlreadyRegisteredError(EngineRegistryError):
    """引擎已注册异常
    
    当尝试注册已存在的引擎ID时抛出。
    """
    def __init__(self, engine_id: str):
        self.engine_id = engine_id
        super().__init__(f"Engine already registered: {engine_id}")


class EngineStatusTransitionError(EngineRegistryError):
    """引擎状态迁移异常
    
    当尝试进行非法的状态迁移时抛出。
    例如: deprecated -> active 是不允许的。
    """
    def __init__(self, engine_id: str, current_status: str, target_status: str):
        self.engine_id = engine_id
        self.current_status = current_status
        self.target_status = target_status
        super().__init__(
            f"Invalid status transition for engine '{engine_id}': "
            f"{current_status} -> {target_status}"
        )


class InvalidEngineIdError(EngineRegistryError):
    """无效引擎ID异常
    
    当引擎ID不符合命名规范时抛出。
    规范: ^[a-z][a-z0-9_-]*$
    """
    def __init__(self, engine_id: str, reason: str = ""):
        self.engine_id = engine_id
        self.reason = reason
        message = f"Invalid engine ID: {engine_id}"
        if reason:
            message += f" ({reason})"
        super().__init__(message)


class EngineDependencyError(EngineRegistryError):
    """引擎依赖错误异常
    
    当引擎的依赖无法满足时抛出。
    """
    def __init__(self, engine_id: str, missing_dependencies: list[str]):
        self.engine_id = engine_id
        self.missing_dependencies = missing_dependencies
        deps_str = ", ".join(missing_dependencies)
        super().__init__(
            f"Engine '{engine_id}' has unresolved dependencies: {deps_str}"
        )


class EngineRegistryIOError(EngineRegistryError):
    """引擎注册表IO异常
    
    当读取或写入注册表文件失败时抛出。
    """
    def __init__(self, path: str, operation: str, reason: str = ""):
        self.path = path
        self.operation = operation
        self.reason = reason
        message = f"Failed to {operation} engine registry at '{path}'"
        if reason:
            message += f": {reason}"
        super().__init__(message)
