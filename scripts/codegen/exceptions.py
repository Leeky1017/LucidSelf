"""
Codegen Pipeline Exceptions

代码生成器管线异常定义。
"""

from typing import Any, Dict, List, Optional


class CodegenError(Exception):
    """代码生成器基础异常"""
    
    def __init__(
        self, 
        message: str, 
        source_file: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message)
        self.message = message
        self.source_file = source_file
        self.details = details or {}
    
    def __str__(self) -> str:
        parts = [self.message]
        if self.source_file:
            parts.append(f"[source: {self.source_file}]")
        if self.details:
            parts.append(f"[details: {self.details}]")
        return " ".join(parts)


class ValidationError(CodegenError):
    """
    校验失败异常
    
    当 JSON 不符合 Pydantic Schema 时抛出。
    包含详细的校验错误列表。
    """
    
    def __init__(
        self, 
        message: str, 
        errors: List[str],
        source_file: Optional[str] = None
    ):
        super().__init__(message, source_file, {"errors": errors})
        self.errors = errors
    
    def __str__(self) -> str:
        error_list = "\n  - ".join(self.errors)
        base = f"{self.message}"
        if self.source_file:
            base += f" [source: {self.source_file}]"
        return f"{base}\nValidation errors:\n  - {error_list}"


class CompilationError(CodegenError):
    """
    编译失败异常
    
    当代码生成过程失败时抛出。
    """
    
    def __init__(
        self, 
        message: str, 
        rule_id: Optional[str] = None,
        source_file: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message, source_file, details)
        self.rule_id = rule_id
    
    def __str__(self) -> str:
        base = self.message
        if self.rule_id:
            base = f"[rule_id: {self.rule_id}] {base}"
        if self.source_file:
            base += f" [source: {self.source_file}]"
        return base


class SyntaxVerificationError(CodegenError):
    """
    语法验证失败异常
    
    当生成的代码无法通过 Python AST 解析时抛出。
    """
    
    def __init__(
        self, 
        message: str,
        generated_code: str,
        line_number: Optional[int] = None,
        source_file: Optional[str] = None
    ):
        details = {"line_number": line_number} if line_number else {}
        super().__init__(message, source_file, details)
        self.generated_code = generated_code
        self.line_number = line_number
    
    def __str__(self) -> str:
        base = self.message
        if self.line_number:
            base += f" (line {self.line_number})"
        if self.source_file:
            base += f" [source: {self.source_file}]"
        return base


class ManifestError(CodegenError):
    """
    清单操作异常
    
    当清单读写或校验失败时抛出。
    """
    pass


class FormattingError(CodegenError):
    """
    代码格式化异常
    
    当 black 格式化失败时抛出。
    """
    pass
