"""
Migration Reporter

迁移报告生成器，对齐 design.md Components and Interfaces §4

功能:
- 汇总迁移结果生成报告
- 格式化错误信息
- 生成文本和 JSON 格式报告
- 提供迁移状态查询
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from scripts.codegen.engine_mapping import ENGINE_BOOK_MAPPING, TOTAL_BOOKS, VALID_ENGINE_IDS
from scripts.codegen.models import (
    MigrationReport,
    MigrationResult,
    MigrationStatus,
    ValidationErrorModel,
    merge_results,
)

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# 迁移报告生成器
# -----------------------------------------------------------------------------

class MigrationReporter:
    """
    迁移报告生成器 (对齐 design.md Error Handling §2, tasks.md 1.4)
    """
    
    def __init__(self):
        self._results: Dict[str, MigrationResult] = {}
    
    def add_result(self, result: MigrationResult) -> None:
        """添加迁移结果"""
        self._results[result.book_id] = result
    
    def generate_report(self, results: Optional[Dict[str, MigrationResult]] = None) -> MigrationReport:
        """
        汇总所有迁移结果，计算 coverage_percentage 和 overall_success_rate
        
        Args:
            results: 迁移结果字典（可选，默认使用内部收集的结果）
        
        Returns:
            MigrationReport
        """
        if results is None:
            results = self._results
        
        return merge_results(results)
    
    def format_error(self, error: ValidationErrorModel) -> str:
        """格式化单个错误为可读字符串"""
        result = f"  {error.file}:{error.line}:{error.column}: {error.error_type}: {error.message}"
        if error.suggestion:
            result += f"\n    Suggestion: {error.suggestion}"
        return result
    
    def format_report(self, report: MigrationReport) -> str:
        """
        生成完整的文本报告 (对齐 design.md Error Handling §2 格式)
        
        格式:
        === Migration Report ===
        Book: {book_id} ({book_name})
        Engine: {engine_id}
        Status: {status}
        ...
        """
        lines = [
            "=" * 60,
            "SEMANTIC LAYER PHASE 2 MIGRATION REPORT",
            "=" * 60,
            "",
            f"Timestamp: {report.timestamp.isoformat()}",
            f"Total Books: {report.total_books}",
            f"Migrated Books: {report.migrated_books}",
            f"Coverage: {report.coverage_percentage:.1f}%",
            f"Overall Success Rate: {report.overall_success_rate:.1%}",
            "",
        ]
        
        # 按引擎统计
        lines.append("-" * 40)
        lines.append("BY ENGINE")
        lines.append("-" * 40)
        for engine_id in VALID_ENGINE_IDS:
            stats = report.by_engine.get(engine_id, {"total_entries": 0, "books": []})
            expected_books = len(ENGINE_BOOK_MAPPING.get(engine_id, []))
            actual_books = len(stats.get("books", []))
            lines.append(
                f"  {engine_id}: {stats.get('total_entries', 0)} entries, "
                f"{actual_books}/{expected_books} books"
            )
        lines.append("")
        
        # 各书籍详情
        lines.append("-" * 40)
        lines.append("BOOK DETAILS")
        lines.append("-" * 40)
        
        for book_id, result in sorted(report.results.items()):
            status_icon = {
                MigrationStatus.SUCCESS: "✅",
                MigrationStatus.PARTIAL: "⚠️",
                MigrationStatus.FAILED: "❌",
                MigrationStatus.SKIPPED: "⏭️",
            }.get(result.status, "?")
            
            lines.append("")
            lines.append(f"--- {status_icon} {book_id} ({result.engine_id}) ---")
            lines.append(f"Status: {result.status.value}")
            lines.append(f"Entries: {result.entries_total} total, {result.entries_success} success, {result.entries_failed} failed")
            lines.append(f"Success Rate: {result.success_rate:.1%}")
            lines.append(f"Duration: {result.duration_ms:.0f}ms")
            
            if result.errors:
                lines.append("")
                lines.append("Errors:")
                for error in result.errors[:10]:  # 最多显示 10 个错误
                    lines.append(self.format_error(error))
                if len(result.errors) > 10:
                    lines.append(f"  ... and {len(result.errors) - 10} more errors")
            
            if result.warnings:
                lines.append("")
                lines.append("Warnings:")
                for warning in result.warnings[:5]:  # 最多显示 5 个警告
                    lines.append(f"  - {warning}")
                if len(result.warnings) > 5:
                    lines.append(f"  ... and {len(result.warnings) - 5} more warnings")
            
            if result.output_files:
                lines.append("")
                lines.append("Output Files:")
                for output_file in result.output_files[:5]:  # 最多显示 5 个文件
                    lines.append(f"  - {output_file}")
                if len(result.output_files) > 5:
                    lines.append(f"  ... and {len(result.output_files) - 5} more files")
        
        lines.append("")
        lines.append("=" * 60)
        lines.append("END OF REPORT")
        lines.append("=" * 60)
        
        return "\n".join(lines)
    
    def format_report_json(self, report: MigrationReport) -> str:
        """生成 JSON 格式报告"""
        return report.model_dump_json(indent=2)
    
    def format_summary(self, report: MigrationReport) -> str:
        """生成简短摘要"""
        return (
            f"Migration: {report.migrated_books}/{report.total_books} books, "
            f"{report.coverage_percentage:.1f}% coverage, "
            f"{report.overall_success_rate:.1%} success rate"
        )


# -----------------------------------------------------------------------------
# 迁移状态查询函数
# -----------------------------------------------------------------------------

def get_migration_status() -> Dict[str, Any]:
    """
    获取迁移状态 (对齐 tasks.md 1.4)
    
    返回格式:
    {
        "total_books": 24,
        "migrated_books": len(SemanticRegistry._by_book),
        "by_engine": {engine_id: {"total_entries": ..., "books": [...]}},
        "coverage_percentage": migrated_books / 24 * 100
    }
    """
    try:
        from backend.semantics.core import SemanticRegistry
        
        # 统计已注册的书籍和条目
        by_book = getattr(SemanticRegistry, "_by_book", {})
        by_engine = getattr(SemanticRegistry, "_by_engine", {})
        
        migrated_books = len(by_book)
        
        # 按引擎统计
        engine_stats: Dict[str, Dict[str, Any]] = {}
        for engine_id in VALID_ENGINE_IDS:
            engine_entries = by_engine.get(engine_id, set())
            engine_books = [
                book_id for book_id in ENGINE_BOOK_MAPPING.get(engine_id, [])
                if book_id in by_book
            ]
            engine_stats[engine_id] = {
                "total_entries": len(engine_entries),
                "books": engine_books,
            }
        
        return {
            "total_books": TOTAL_BOOKS,
            "migrated_books": migrated_books,
            "by_engine": engine_stats,
            "coverage_percentage": (migrated_books / TOTAL_BOOKS * 100) if TOTAL_BOOKS > 0 else 0.0,
        }
    except ImportError:
        logger.warning("SemanticRegistry not available, returning empty status")
        return {
            "total_books": TOTAL_BOOKS,
            "migrated_books": 0,
            "by_engine": {engine_id: {"total_entries": 0, "books": []} for engine_id in VALID_ENGINE_IDS},
            "coverage_percentage": 0.0,
        }


def get_migration_progress() -> str:
    """获取迁移进度的简短描述"""
    status = get_migration_status()
    return (
        f"Progress: {status['migrated_books']}/{status['total_books']} books "
        f"({status['coverage_percentage']:.1f}%)"
    )


# -----------------------------------------------------------------------------
# 报告持久化
# -----------------------------------------------------------------------------

def save_report(report: MigrationReport, output_path: str) -> None:
    """保存报告到文件"""
    from pathlib import Path
    
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if output_path.endswith(".json"):
        path.write_text(report.model_dump_json(indent=2), encoding="utf-8")
    else:
        reporter = MigrationReporter()
        path.write_text(reporter.format_report(report), encoding="utf-8")
    
    logger.info(f"Report saved to {output_path}")


def load_report(input_path: str) -> Optional[MigrationReport]:
    """从文件加载报告"""
    from pathlib import Path
    
    path = Path(input_path)
    if not path.exists():
        return None
    
    if input_path.endswith(".json"):
        return MigrationReport.model_validate_json(path.read_text(encoding="utf-8"))
    
    return None
