"""
LucidSelf Codegen Pipeline

代码生成器管线 - 将配置态 JSON/JSONL 编译为可执行的 Python 模块。

对照文档:
- docs/ls_engine_architecture_v3.md §2.2
- docs/数据契约_Schema定义规范_v1.md §2.2

模块结构:
- base: BaseCodeGenerator 抽象基类
- rule_generator: RuleCodeGenerator - 规则编译器
- factor_generator: FactorCodeGenerator - 因子编译器
- semantic_generator: SemanticCodeGenerator - 语义编译器
- manifest: CodegenManifest - 清单管理
- cli: CLI 入口
- exceptions: 异常定义
- error_report: 错误报告与Agent修复提示
- rollback: 回退管理器
- hot_reload: 热重载接口预留

核心原则:
1. ConfigRuleDefinition → Codegen → Python函数 → 返回 RuntimeRuleResult
2. ConfigFactor → Codegen → Python模块 → 运行时产出 FactorValue
3. 禁止跨用 Config/Runtime 类型
"""

__version__ = "1.0.0"
__author__ = "LucidSelf Team"

# 延迟导入，避免循环依赖
# 使用时: from scripts.codegen import RuleCodeGenerator

__all__ = [
    # 基类
    "BaseCodeGenerator",
    # 生成器
    "RuleCodeGenerator",
    "FactorCodeGenerator",
    "SemanticCodeGenerator",
    # 清单
    "CodegenManifest",
    "ManifestEntry",
    # 异常
    "CodegenError",
    "ValidationError",
    "CompilationError",
    "SyntaxVerificationError",
    # 错误报告
    "CodegenErrorReport",
    "generate_agent_prompt",
    "save_error_report",
    # 回退管理
    "RollbackManager",
    "RollbackError",
    # 热重载接口
    "HotReloadable",
    "HotReloadWatcher",
    "notify_reload",
    "register_reload_listener",
]


def __getattr__(name: str):
    """延迟导入模块"""
    if name == "BaseCodeGenerator":
        from scripts.codegen.base import BaseCodeGenerator
        return BaseCodeGenerator
    elif name == "RuleCodeGenerator":
        from scripts.codegen.rule_generator import RuleCodeGenerator
        return RuleCodeGenerator
    elif name == "FactorCodeGenerator":
        from scripts.codegen.factor_generator import FactorCodeGenerator
        return FactorCodeGenerator
    elif name == "SemanticCodeGenerator":
        from scripts.codegen.semantic_generator import SemanticCodeGenerator
        return SemanticCodeGenerator
    elif name == "CodegenManifest":
        from scripts.codegen.manifest import CodegenManifest
        return CodegenManifest
    elif name == "ManifestEntry":
        from scripts.codegen.manifest import ManifestEntry
        return ManifestEntry
    elif name in ("CodegenError", "ValidationError", "CompilationError", "SyntaxVerificationError"):
        from scripts.codegen import exceptions
        return getattr(exceptions, name)
    # 错误报告
    elif name == "CodegenErrorReport":
        from scripts.codegen.error_report import CodegenErrorReport
        return CodegenErrorReport
    elif name == "generate_agent_prompt":
        from scripts.codegen.error_report import generate_agent_prompt
        return generate_agent_prompt
    elif name == "save_error_report":
        from scripts.codegen.error_report import save_error_report
        return save_error_report
    # 回退管理
    elif name == "RollbackManager":
        from scripts.codegen.rollback import RollbackManager
        return RollbackManager
    elif name == "RollbackError":
        from scripts.codegen.rollback import RollbackError
        return RollbackError
    # 热重载接口
    elif name == "HotReloadable":
        from scripts.codegen.hot_reload import HotReloadable
        return HotReloadable
    elif name == "HotReloadWatcher":
        from scripts.codegen.hot_reload import HotReloadWatcher
        return HotReloadWatcher
    elif name == "notify_reload":
        from scripts.codegen.hot_reload import notify_reload
        return notify_reload
    elif name == "register_reload_listener":
        from scripts.codegen.hot_reload import register_reload_listener
        return register_reload_listener
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
