"""
Codegen Error Report Module

错误报告生成器，用于：
1. 结构化错误报告 (CodegenErrorReport)
2. 生成 Agent 可解析的修复提示
3. 保存错误报告为 JSON 格式
"""

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from .exceptions import (
    CodegenError,
    ValidationError,
    CompilationError,
    SyntaxVerificationError,
    ManifestError,
    FormattingError,
)


@dataclass
class CodegenErrorReport:
    """
    结构化错误报告
    
    用于记录代码生成过程中的错误信息，供 Agent 分析和修复。
    """
    error_type: str
    message: str
    source_file: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)
    suggestions: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return asdict(self)
    
    def to_json(self, indent: int = 2) -> str:
        """转换为 JSON 字符串"""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
    
    @classmethod
    def from_error(cls, error: CodegenError) -> "CodegenErrorReport":
        """从 CodegenError 创建报告"""
        error_type = type(error).__name__
        suggestions = _generate_suggestions(error)
        
        return cls(
            error_type=error_type,
            message=error.message,
            source_file=error.source_file,
            details=error.details,
            suggestions=suggestions,
        )


def _generate_suggestions(error: CodegenError) -> List[str]:
    """
    根据错误类型生成修复建议
    """
    suggestions = []
    
    if isinstance(error, ValidationError):
        suggestions.append("检查 JSON 文件是否符合 ConfigFactor/ConfigRuleDefinition Schema")
        suggestions.append("确保必填字段存在: version, status, engine_id")
        suggestions.append("验证 version 格式为 ^\\d+\\.\\d+\\.\\d+$")
        suggestions.append("验证 status 为 active/experimental/deprecated 之一")
        if error.errors:
            for err in error.errors[:3]:  # 最多显示3个错误
                suggestions.append(f"修复: {err}")
    
    elif isinstance(error, CompilationError):
        suggestions.append("检查规则定义的 condition 结构是否正确")
        suggestions.append("确保复杂规则 (is_complex_logic=True) 包含 python_handler_ref")
        suggestions.append("验证条件运算符是否在支持列表中: EQ, NE, GT, GE, LT, LE, IN, NOT_IN, CONTAINS, AND, OR, NOT")
        if error.rule_id:
            suggestions.append(f"检查规则 '{error.rule_id}' 的定义")
    
    elif isinstance(error, SyntaxVerificationError):
        suggestions.append("生成的代码存在语法错误，检查模板和输入数据")
        if error.line_number:
            suggestions.append(f"错误位于生成代码的第 {error.line_number} 行")
        suggestions.append("确保条件表达式能正确编译为 Python 语法")
    
    elif isinstance(error, ManifestError):
        suggestions.append("检查 .codegen_manifest.json 文件是否损坏")
        suggestions.append("尝试删除清单文件并重新生成")
        suggestions.append("确保文件系统权限正确")
    
    elif isinstance(error, FormattingError):
        suggestions.append("生成的代码无法被 black 格式化")
        suggestions.append("检查是否存在未闭合的括号或引号")
        suggestions.append("验证字符串内容是否包含非法字符")
    
    else:
        suggestions.append("检查输入文件格式")
        suggestions.append("确认代码生成器配置正确")
        suggestions.append("查看详细错误信息")
    
    return suggestions


def generate_agent_prompt(error: Union[CodegenError, CodegenErrorReport]) -> str:
    """
    生成供 Agent 分析的修复提示
    
    返回一个结构化的 prompt，包含错误信息和修复建议，
    Agent 可以根据此 prompt 生成修复代码或建议。
    
    Args:
        error: CodegenError 异常或 CodegenErrorReport 报告
        
    Returns:
        Agent 可解析的修复提示字符串
    """
    if isinstance(error, CodegenError):
        report = CodegenErrorReport.from_error(error)
    else:
        report = error
    
    lines = [
        "## Codegen Error Report",
        "",
        f"**Error Type**: `{report.error_type}`",
        f"**Message**: {report.message}",
    ]
    
    if report.source_file:
        lines.append(f"**Source File**: `{report.source_file}`")
    
    if report.details:
        lines.append("")
        lines.append("### Details")
        lines.append("```json")
        lines.append(json.dumps(report.details, indent=2, ensure_ascii=False))
        lines.append("```")
    
    if report.suggestions:
        lines.append("")
        lines.append("### Suggested Fixes")
        for i, suggestion in enumerate(report.suggestions, 1):
            lines.append(f"{i}. {suggestion}")
    
    lines.extend([
        "",
        "### Action Required",
        "请根据以上信息分析错误原因，并提供修复方案。",
        "如果是 JSON Schema 校验错误，请修正源文件；",
        "如果是代码生成错误，请检查规则定义的逻辑结构。",
    ])
    
    return "\n".join(lines)


def save_error_report(
    error: Union[CodegenError, CodegenErrorReport],
    path: Path,
    append: bool = False
) -> Path:
    """
    保存错误报告为 JSON 格式
    
    Args:
        error: CodegenError 异常或 CodegenErrorReport 报告
        path: 保存路径（文件或目录）
        append: 如果为 True 且目标为文件，追加到现有报告列表
        
    Returns:
        保存的文件路径
    """
    if isinstance(error, CodegenError):
        report = CodegenErrorReport.from_error(error)
    else:
        report = error
    
    # 确定目标文件
    if path.is_dir():
        filename = f"error_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        target_path = path / filename
    else:
        target_path = path
        target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 读取或创建报告列表
    if append and target_path.exists():
        with open(target_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
            if isinstance(existing, list):
                reports = existing
            else:
                reports = [existing]
        reports.append(report.to_dict())
    else:
        reports = report.to_dict()
    
    # 写入文件
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(reports, f, indent=2, ensure_ascii=False)
    
    return target_path


def load_error_report(path: Path) -> Union[CodegenErrorReport, List[CodegenErrorReport]]:
    """
    从 JSON 文件加载错误报告
    
    Args:
        path: JSON 文件路径
        
    Returns:
        单个报告或报告列表
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if isinstance(data, list):
        return [CodegenErrorReport(**item) for item in data]
    else:
        return CodegenErrorReport(**data)
