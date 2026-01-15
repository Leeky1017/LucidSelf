"""
Migration Models

迁移结果数据模型，对齐 design.md Data Models §1

模型:
- MigrationStatus: 迁移状态枚举
- ValidationError: 验证错误 (Pydantic)
- MigrationResult: 单本书籍迁移结果
- MigrationReport: 完整迁移报告
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# -----------------------------------------------------------------------------
# 迁移状态枚举
# -----------------------------------------------------------------------------

class MigrationStatus(str, Enum):
    """迁移状态 (对齐 design.md Data Models §1)"""
    SUCCESS = "success"   # 全部成功
    PARTIAL = "partial"   # 部分成功
    FAILED = "failed"     # 全部失败
    SKIPPED = "skipped"   # 跳过（无变更）


# -----------------------------------------------------------------------------
# 验证错误模型
# -----------------------------------------------------------------------------

class ValidationErrorModel(BaseModel):
    """
    验证错误 Pydantic 模型 (对齐 design.md Data Models §1, tasks.md 1.3)
    
    字段:
    - file: 源文件路径
    - line: 行号
    - column: 列号
    - error_type: 错误类型
    - message: 错误消息
    - suggestion: 修复建议
    - severity: 严重级别 (ERROR, WARNING)
    """
    file: str = Field(..., description="源文件路径")
    line: int = Field(..., description="行号")
    column: int = Field(..., description="列号")
    error_type: str = Field(..., description="错误类型")
    message: str = Field(..., description="错误消息")
    suggestion: Optional[str] = Field(None, description="修复建议")
    severity: str = Field("ERROR", description="严重级别 (ERROR, WARNING)")
    
    def __str__(self) -> str:
        """格式: {file}:{line}:{column}: {error_type}: {message}"""
        return f"{self.file}:{self.line}:{self.column}: {self.error_type}: {self.message}"
    
    class Config:
        """Pydantic 配置"""
        extra = "forbid"


# -----------------------------------------------------------------------------
# 迁移结果模型
# -----------------------------------------------------------------------------

class MigrationResult(BaseModel):
    """
    单本书籍迁移结果 (对齐 design.md Data Models §1, tasks.md 1.3)
    
    字段:
    - book_id: 书籍 ID
    - engine_id: 引擎 ID
    - status: 迁移状态
    - entries_total: 总条目数
    - entries_success: 成功条目数
    - entries_failed: 失败条目数
    - errors: 错误列表
    - warnings: 警告列表
    - output_files: 输出文件列表
    - duration_ms: 耗时(毫秒)
    - timestamp: 时间戳
    """
    book_id: str = Field(..., description="书籍 ID")
    engine_id: str = Field(..., description="引擎 ID")
    status: MigrationStatus = Field(..., description="迁移状态")
    entries_total: int = Field(0, description="总条目数")
    entries_success: int = Field(0, description="成功条目数")
    entries_failed: int = Field(0, description="失败条目数")
    errors: List[ValidationErrorModel] = Field(default_factory=list, description="错误列表")
    warnings: List[str] = Field(default_factory=list, description="警告列表")
    output_files: List[str] = Field(default_factory=list, description="输出文件列表")
    duration_ms: float = Field(0.0, description="耗时(毫秒)")
    timestamp: datetime = Field(default_factory=datetime.now, description="时间戳")
    
    @property
    def success_rate(self) -> float:
        """成功率: entries_success / entries_total"""
        if self.entries_total == 0:
            return 0.0
        return self.entries_success / self.entries_total
    
    @property
    def has_errors(self) -> bool:
        """是否有错误"""
        return len(self.errors) > 0
    
    @property
    def has_warnings(self) -> bool:
        """是否有警告"""
        return len(self.warnings) > 0
    
    class Config:
        """Pydantic 配置"""
        extra = "forbid"


# -----------------------------------------------------------------------------
# 引擎统计模型
# -----------------------------------------------------------------------------

class EngineStats(BaseModel):
    """引擎统计信息"""
    total_entries: int = Field(0, description="总条目数")
    books: List[str] = Field(default_factory=list, description="书籍列表")
    success_count: int = Field(0, description="成功书籍数")
    failed_count: int = Field(0, description="失败书籍数")
    
    class Config:
        """Pydantic 配置"""
        extra = "forbid"


# -----------------------------------------------------------------------------
# 迁移报告模型
# -----------------------------------------------------------------------------

class MigrationReport(BaseModel):
    """
    完整迁移报告 (对齐 design.md Data Models §1, tasks.md 1.3)
    
    字段:
    - total_books: 总书籍数 (24)
    - migrated_books: 已迁移书籍数
    - by_engine: 按引擎统计
    - coverage_percentage: 覆盖率百分比
    - overall_success_rate: 总体成功率
    - results: 各书籍迁移结果
    - timestamp: 时间戳
    """
    total_books: int = Field(24, description="总书籍数 (不含已归档的记纂渊海)")
    migrated_books: int = Field(0, description="已迁移书籍数")
    by_engine: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="按引擎统计: {engine_id: {'total_entries': int, 'books': List[str]}}"
    )
    coverage_percentage: float = Field(0.0, description="覆盖率百分比")
    overall_success_rate: float = Field(0.0, description="总体成功率")
    results: Dict[str, MigrationResult] = Field(default_factory=dict, description="各书籍迁移结果")
    total_errors: int = Field(0, description="总错误数")
    total_warnings: int = Field(0, description="总警告数")
    timestamp: datetime = Field(default_factory=datetime.now, description="时间戳")
    
    def compute_stats(self) -> None:
        """计算统计信息"""
        if not self.results:
            return
        
        # 统计迁移书籍数
        self.migrated_books = len([r for r in self.results.values() if r.status != MigrationStatus.SKIPPED])
        
        # 计算覆盖率
        self.coverage_percentage = (self.migrated_books / self.total_books) * 100 if self.total_books > 0 else 0.0
        
        # 统计按引擎
        engine_stats: Dict[str, Dict[str, Any]] = {}
        for result in self.results.values():
            engine_id = result.engine_id
            if engine_id not in engine_stats:
                engine_stats[engine_id] = {"total_entries": 0, "books": []}
            engine_stats[engine_id]["total_entries"] += result.entries_total
            engine_stats[engine_id]["books"].append(result.book_id)
        self.by_engine = engine_stats
        
        # 计算总体成功率
        total_entries = sum(r.entries_total for r in self.results.values())
        success_entries = sum(r.entries_success for r in self.results.values())
        self.overall_success_rate = success_entries / total_entries if total_entries > 0 else 0.0
        
        # 统计错误和警告
        self.total_errors = sum(len(r.errors) for r in self.results.values())
        self.total_warnings = sum(len(r.warnings) for r in self.results.values())
    
    class Config:
        """Pydantic 配置"""
        extra = "forbid"


# -----------------------------------------------------------------------------
# 工具函数
# -----------------------------------------------------------------------------

def create_migration_result(
    book_id: str,
    engine_id: str,
    entries_total: int = 0,
    entries_success: int = 0,
    entries_failed: int = 0,
    errors: Optional[List[ValidationErrorModel]] = None,
    warnings: Optional[List[str]] = None,
    output_files: Optional[List[str]] = None,
    duration_ms: float = 0.0,
) -> MigrationResult:
    """创建迁移结果的便捷函数"""
    # 判断状态
    if entries_total == 0:
        status = MigrationStatus.SKIPPED
    elif entries_failed == 0:
        status = MigrationStatus.SUCCESS
    elif entries_success == 0:
        status = MigrationStatus.FAILED
    else:
        status = MigrationStatus.PARTIAL
    
    return MigrationResult(
        book_id=book_id,
        engine_id=engine_id,
        status=status,
        entries_total=entries_total,
        entries_success=entries_success,
        entries_failed=entries_failed,
        errors=errors or [],
        warnings=warnings or [],
        output_files=output_files or [],
        duration_ms=duration_ms,
    )


def merge_results(results: Dict[str, MigrationResult]) -> MigrationReport:
    """合并多个迁移结果为报告"""
    report = MigrationReport(results=results)
    report.compute_stats()
    return report
