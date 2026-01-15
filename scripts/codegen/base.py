"""
BaseCodeGenerator - 代码生成器抽象基类

提供所有代码生成器的公共功能：
- 代码格式化 (black)
- 语法验证 (AST)
- 文件保存

对照文档: docs/ls_engine_architecture_v3.md §2.2
"""

from __future__ import annotations

import ast
import hashlib
import logging
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from scripts.codegen.exceptions import (
    FormattingError,
    SyntaxVerificationError,
    ValidationError,
)

logger = logging.getLogger(__name__)


class BaseCodeGenerator(ABC):
    """
    代码生成器抽象基类
    
    所有具体生成器（Rule/Factor/Semantic）必须继承此类并实现：
    - validate(source: Dict) -> List[str]: 校验输入 JSON
    - compile(source: Dict) -> str: 编译为 Python 代码
    
    提供的公共方法：
    - format_code(code: str) -> str: 使用 black 格式化
    - verify_syntax(code: str) -> bool: AST 语法检查
    - save(code: str, filename: str) -> Path: 保存到文件
    - compute_hash(content: str) -> str: 计算内容哈希
    """
    
    def __init__(self, output_dir: Path):
        """
        初始化生成器
        
        Args:
            output_dir: 输出目录路径（如 backend/generated/rules）
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._black_available = self._check_black_available()
    
    @staticmethod
    def _check_black_available() -> bool:
        """检查 black 是否可用"""
        try:
            import black  # noqa: F401
            return True
        except ImportError:
            logger.warning("black not installed, code formatting will be skipped")
            return False
    
    # =========================================================================
    # 抽象方法 - 子类必须实现
    # =========================================================================
    
    @abstractmethod
    def validate(self, source: Dict[str, Any]) -> List[str]:
        """
        校验输入 JSON
        
        Args:
            source: 输入的 JSON 字典
        
        Returns:
            校验错误列表，空列表表示通过
        
        Raises:
            ValidationError: 当校验失败时
        """
        pass
    
    @abstractmethod
    def compile(self, source: Dict[str, Any]) -> str:
        """
        将 JSON 编译为 Python 代码
        
        Args:
            source: 经过校验的 JSON 字典
        
        Returns:
            生成的 Python 代码字符串
        
        Raises:
            CompilationError: 当编译失败时
        """
        pass
    
    # =========================================================================
    # 公共方法 - 代码格式化
    # =========================================================================
    
    def format_code(self, code: str) -> str:
        """
        使用 black 格式化 Python 代码
        
        Args:
            code: 原始 Python 代码
        
        Returns:
            格式化后的代码
        
        Raises:
            FormattingError: 当格式化失败时
        """
        if not self._black_available:
            return code
        
        try:
            import black
            
            mode = black.Mode(
                target_versions={black.TargetVersion.PY312},
                line_length=100,
                string_normalization=True,
            )
            formatted = black.format_str(code, mode=mode)
            return formatted
        except Exception as e:
            raise FormattingError(
                f"Failed to format code with black: {e}",
                details={"error_type": type(e).__name__}
            )
    
    # =========================================================================
    # 公共方法 - 语法验证
    # =========================================================================
    
    def verify_syntax(self, code: str) -> bool:
        """
        使用 Python AST 验证代码语法
        
        Args:
            code: Python 代码字符串
        
        Returns:
            True 表示语法正确
        
        Raises:
            SyntaxVerificationError: 当语法错误时
        """
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            raise SyntaxVerificationError(
                message=f"Syntax error: {e.msg}",
                generated_code=code,
                line_number=e.lineno,
            )
    
    # =========================================================================
    # 公共方法 - 文件操作
    # =========================================================================
    
    def save(self, code: str, filename: str) -> Path:
        """
        保存生成的代码到文件
        
        Args:
            code: Python 代码字符串
            filename: 文件名（不含路径）
        
        Returns:
            保存的文件路径
        """
        if not filename.endswith(".py"):
            filename = f"{filename}.py"
        
        filepath = self.output_dir / filename
        
        # 确保目录存在
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # 写入文件
        filepath.write_text(code, encoding="utf-8")
        
        logger.info(f"Saved generated code to {filepath}")
        return filepath
    
    @staticmethod
    def compute_hash(content: str) -> str:
        """
        计算内容的 SHA256 哈希
        
        Args:
            content: 要计算哈希的字符串
        
        Returns:
            十六进制哈希字符串
        """
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
    
    # =========================================================================
    # 工具方法 - 代码生成辅助
    # =========================================================================
    
    def generate_header(
        self,
        module_name: str,
        source_file: Optional[str] = None,
        version: Optional[str] = None,
    ) -> str:
        """
        生成模块头部注释
        
        Args:
            module_name: 模块名称
            source_file: 源文件路径
            version: 版本号
        
        Returns:
            头部注释字符串
        """
        timestamp = datetime.now(timezone.utc).isoformat()
        
        header = f'''"""
{module_name}

自动生成的代码 - 请勿手动编辑！
生成时间: {timestamp}
'''
        
        if source_file:
            header += f"源文件: {source_file}\n"
        
        if version:
            header += f"版本: {version}\n"
        
        header += '''
重新生成: python -m scripts.codegen compile <type> <source>
"""

'''
        return header
    
    def generate_imports(self, imports: List[str]) -> str:
        """
        生成 import 语句块
        
        Args:
            imports: import 语句列表
        
        Returns:
            import 语句块字符串
        """
        if not imports:
            return ""
        
        # 分类 import 语句
        stdlib_imports = []
        third_party_imports = []
        local_imports = []
        
        stdlib_modules = {
            "datetime", "typing", "enum", "abc", "collections",
            "functools", "itertools", "pathlib", "re", "json",
            "logging", "time", "dataclasses"
        }
        
        for imp in imports:
            if imp.startswith("from backend") or imp.startswith("from scripts"):
                local_imports.append(imp)
            elif any(imp.startswith(f"from {m}") or imp.startswith(f"import {m}") 
                     for m in stdlib_modules):
                stdlib_imports.append(imp)
            else:
                third_party_imports.append(imp)
        
        # 组装
        sections = []
        
        if stdlib_imports:
            sections.append("\n".join(sorted(stdlib_imports)))
        
        if third_party_imports:
            sections.append("\n".join(sorted(third_party_imports)))
        
        if local_imports:
            sections.append("\n".join(sorted(local_imports)))
        
        return "\n\n".join(sections) + "\n\n" if sections else ""
    
    # =========================================================================
    # 完整编译流程
    # =========================================================================
    
    def compile_and_save(
        self,
        source: Dict[str, Any],
        filename: str,
        source_file: Optional[str] = None,
    ) -> Path:
        """
        完整编译流程：校验 → 编译 → 格式化 → 语法检查 → 保存
        
        Args:
            source: 输入的 JSON 字典
            filename: 输出文件名
            source_file: 源文件路径（用于错误报告）
        
        Returns:
            保存的文件路径
        
        Raises:
            ValidationError: 校验失败
            CompilationError: 编译失败
            SyntaxVerificationError: 语法错误
            FormattingError: 格式化失败
        """
        # 1. 校验
        errors = self.validate(source)
        if errors:
            raise ValidationError(
                "Validation failed",
                errors=errors,
                source_file=source_file
            )
        
        # 2. 编译
        code = self.compile(source)
        
        # 3. 格式化
        code = self.format_code(code)
        
        # 4. 语法检查
        self.verify_syntax(code)
        
        # 5. 保存
        return self.save(code, filename)
