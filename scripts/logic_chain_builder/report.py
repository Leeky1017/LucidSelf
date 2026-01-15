"""
BuildReportGenerator - 生成构建报告

生成逻辑链构建的统计报告。

**Feature: logic-chain-builder**
**Validates: Requirements 8.1, 8.2, 8.3, 8.4, 8.5**
"""

from datetime import datetime
from pathlib import Path
from typing import List, Optional, Set

from scripts.logic_chain_builder.models import BuildReport, BookStats, BookQualityScores, LogicChain
from scripts.logic_chain_builder.constants import OUTPUT_DIR
from scripts.logic_chain_builder.logging_config import get_logger


logger = get_logger(__name__)

# Coverage threshold for low coverage warning
LOW_COVERAGE_THRESHOLD = 0.8


class BuildReportGenerator:
    """
    生成构建报告
    
    生成data/logic_chains/build_report.md。
    
    **Validates: Requirements 8.1, 8.2, 8.3, 8.4, 8.5**
    """
    
    def __init__(self, output_dir: str = OUTPUT_DIR):
        """
        初始化报告生成器
        
        Args:
            output_dir: 输出目录路径
        """
        self.output_dir = Path(output_dir)
        self._warnings: List[str] = []
        self._errors: List[str] = []
    
    def add_warning(self, warning: str) -> None:
        """添加警告消息"""
        self._warnings.append(warning)
        logger.warning(warning)
    
    def add_error(self, error: str) -> None:
        """添加错误消息"""
        self._errors.append(error)
        logger.error(error)
    
    def generate(self, book_stats: List[BookStats]) -> BuildReport:
        """
        生成构建报告
        
        Args:
            book_stats: 各书籍统计列表
        
        Returns:
            BuildReport实例
            
        **Validates: Requirements 8.1, 8.2, 8.3, 8.4, 8.5**
        """
        # Calculate totals
        total_books = len(book_stats)
        successful_books = sum(1 for s in book_stats if s.status == "success")
        failed_books = sum(1 for s in book_stats if s.status == "failed")
        skipped_books = sum(1 for s in book_stats if s.status == "skipped")
        
        # Identify low coverage books (< 80%) - Requirement 8.4
        for stats in book_stats:
            if stats.status == "success" and stats.coverage < LOW_COVERAGE_THRESHOLD:
                self.add_warning(
                    f"Low coverage for {stats.book_id}: {stats.coverage:.1%} "
                    f"(threshold: {LOW_COVERAGE_THRESHOLD:.0%})"
                )
        
        # Identify orphan snippets - Requirement 8.5
        for stats in book_stats:
            if stats.orphan_snippets:
                self.add_warning(
                    f"Orphan snippets in {stats.book_id}: {len(stats.orphan_snippets)} "
                    f"snippets not included in any node"
                )
        
        # Collect errors from failed books - Requirement 8.3
        for stats in book_stats:
            if stats.status == "failed" and stats.error_message:
                self.add_error(f"Failed to process {stats.book_id}: {stats.error_message}")
        
        report = BuildReport(
            generated_at=datetime.now(),
            total_books=total_books,
            successful_books=successful_books,
            failed_books=failed_books,
            skipped_books=skipped_books,
            book_stats=book_stats,
            warnings=self._warnings.copy(),
            errors=self._errors.copy(),
        )
        
        logger.info(
            f"Generated build report: {successful_books}/{total_books} successful, "
            f"{failed_books} failed, {skipped_books} skipped"
        )
        
        return report
    
    def create_book_stats(
        self,
        book_id: str,
        chain: Optional[LogicChain],
        total_snippet_ids: Set[str],
        status: str = "success",
        error_message: Optional[str] = None,
        quality_scores: Optional[BookQualityScores] = None,
    ) -> BookStats:
        """
        从LogicChain创建BookStats
        
        Args:
            book_id: 书籍ID
            chain: LogicChain实例（如果成功构建）
            total_snippet_ids: 该书籍的所有snippet_id集合
            status: 处理状态 ("success", "failed", "skipped")
            error_message: 错误消息（如果失败）
            quality_scores: 质量评分（可选）
        
        Returns:
            BookStats实例
            
        **Validates: Requirements 12.5**
        """
        if chain is None or status != "success":
            return BookStats(
                book_id=book_id,
                snippet_count=len(total_snippet_ids),
                node_count=0,
                edge_count=0,
                coverage=0.0,
                orphan_snippets=list(total_snippet_ids),
                status=status,
                error_message=error_message,
                quality_scores=None,
            )
        
        # Calculate snippets included in nodes
        snippets_in_nodes: Set[str] = set()
        for node in chain.nodes:
            snippets_in_nodes.update(node.snippet_ids)
        
        # Calculate coverage
        total_snippets = len(total_snippet_ids)
        coverage = len(snippets_in_nodes) / total_snippets if total_snippets > 0 else 1.0
        
        # Find orphan snippets
        orphan_snippets = list(total_snippet_ids - snippets_in_nodes)
        
        return BookStats(
            book_id=book_id,
            snippet_count=total_snippets,
            node_count=len(chain.nodes),
            edge_count=len(chain.edges),
            coverage=coverage,
            orphan_snippets=orphan_snippets,
            status=status,
            error_message=error_message,
            quality_scores=quality_scores,
        )
    
    def write(self, report: BuildReport) -> Path:
        """
        写入报告到Markdown文件
        
        Args:
            report: BuildReport实例
        
        Returns:
            写入的文件路径
            
        **Validates: Requirements 8.1**
        """
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Format and write
        content = self._format_markdown(report)
        output_path = self._get_report_path()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Build report written to {output_path}")
        return output_path

    def _format_markdown(self, report: BuildReport) -> str:
        """
        格式化报告为Markdown
        
        Args:
            report: BuildReport实例
        
        Returns:
            Markdown字符串
            
        **Validates: Requirements 8.1, 8.2, 9.6**
        """
        lines = []
        
        # Header
        lines.append("# Logic Chain Build Report")
        lines.append("")
        lines.append(f"**Generated at:** {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # Summary section
        lines.append("## Summary")
        lines.append("")
        lines.append(f"- **Total Books:** {report.total_books}")
        lines.append(f"- **Successful:** {report.successful_books}")
        lines.append(f"- **Failed:** {report.failed_books}")
        lines.append(f"- **Skipped:** {report.skipped_books}")
        lines.append("")
        
        # Calculate aggregate statistics
        total_nodes = sum(s.node_count for s in report.book_stats)
        total_edges = sum(s.edge_count for s in report.book_stats)
        total_snippets = sum(s.snippet_count for s in report.book_stats)
        total_orphans = sum(len(s.orphan_snippets) for s in report.book_stats)
        avg_coverage = (
            sum(s.coverage for s in report.book_stats if s.status == "success") 
            / report.successful_books
            if report.successful_books > 0 else 0.0
        )
        
        lines.append("### Aggregate Statistics")
        lines.append("")
        lines.append(f"- **Total Nodes:** {total_nodes}")
        lines.append(f"- **Total Edges:** {total_edges}")
        lines.append(f"- **Total Snippets:** {total_snippets}")
        lines.append(f"- **Total Orphan Snippets:** {total_orphans}")
        lines.append(f"- **Average Coverage:** {avg_coverage:.1%}")
        lines.append("")
        
        # Per-book success/failure summary (Requirement 9.6)
        lines.append("## Per-Book Success/Failure Summary")
        lines.append("")
        lines.append("Quick reference showing the processing result for each of the 21 target books:")
        lines.append("")
        
        # Group by status
        successful_books = [s for s in report.book_stats if s.status == "success"]
        failed_books = [s for s in report.book_stats if s.status == "failed"]
        skipped_books = [s for s in report.book_stats if s.status == "skipped"]
        
        if successful_books:
            lines.append("### ✅ Successful Books")
            lines.append("")
            for stats in successful_books:
                lines.append(f"- {stats.book_id} ({stats.node_count} nodes, {stats.edge_count} edges, {stats.coverage:.1%} coverage)")
            lines.append("")
        
        if failed_books:
            lines.append("### ❌ Failed Books")
            lines.append("")
            for stats in failed_books:
                error_msg = stats.error_message or "Unknown error"
                # Truncate long error messages
                if len(error_msg) > 100:
                    error_msg = error_msg[:100] + "..."
                lines.append(f"- {stats.book_id}: {error_msg}")
            lines.append("")
        
        if skipped_books:
            lines.append("### ⏭️ Skipped Books")
            lines.append("")
            for stats in skipped_books:
                reason = stats.error_message or "Missing required files"
                lines.append(f"- {stats.book_id}: {reason}")
            lines.append("")
        
        # Book statistics table
        lines.append("## Book Statistics")
        lines.append("")
        lines.append("| Book ID | Status | Snippets | Nodes | Edges | Coverage | Orphans |")
        lines.append("|---------|--------|----------|-------|-------|----------|---------|")
        
        for stats in report.book_stats:
            status_emoji = {"success": "✅", "failed": "❌", "skipped": "⏭️"}.get(stats.status, "❓")
            coverage_str = f"{stats.coverage:.1%}" if stats.status == "success" else "N/A"
            lines.append(
                f"| {stats.book_id} | {status_emoji} {stats.status} | "
                f"{stats.snippet_count} | {stats.node_count} | {stats.edge_count} | "
                f"{coverage_str} | {len(stats.orphan_snippets)} |"
            )
        
        lines.append("")
        
        # Quality scores section (Requirement 12.5)
        books_with_quality = [s for s in report.book_stats if s.quality_scores is not None]
        if books_with_quality:
            lines.append("## Quality Scores")
            lines.append("")
            lines.append("Quality dimensions per book with pass/fail thresholds:")
            lines.append("")
            lines.append("| Book ID | Connectivity | Arg. Completeness | Orphan Ratio | Cycles | Overall |")
            lines.append("|---------|--------------|-------------------|--------------|--------|---------|")
            
            for stats in books_with_quality:
                q = stats.quality_scores
                conn_status = "✅" if q.connectivity_pass else "❌"
                arg_status = "✅" if q.argument_completeness_pass else "❌"
                orphan_status = "✅" if q.orphan_ratio_pass else "❌"
                overall_status = "✅" if q.overall_pass else "❌"
                
                lines.append(
                    f"| {stats.book_id} | "
                    f"{conn_status} {q.connectivity:.2f} | "
                    f"{arg_status} {q.argument_completeness:.2f} | "
                    f"{orphan_status} {q.orphan_ratio:.2f} | "
                    f"{q.cycle_count} | "
                    f"{overall_status} |"
                )
            
            lines.append("")
            
            # Quality thresholds legend
            lines.append("### Quality Thresholds")
            lines.append("")
            lines.append("- **Connectivity:** ≥ 0.70 (70% of nodes in largest connected component)")
            lines.append("- **Argument Completeness:** ≥ 0.50 (entry→middle→terminal pattern)")
            lines.append("- **Orphan Ratio:** ≤ 0.20 (max 20% nodes without edges)")
            lines.append("")
            
            # Books failing quality thresholds
            failing_books = [s for s in books_with_quality if not s.quality_scores.overall_pass]
            if failing_books:
                lines.append("### Books Failing Quality Thresholds")
                lines.append("")
                for stats in failing_books:
                    q = stats.quality_scores
                    issues = []
                    if not q.connectivity_pass:
                        issues.append(f"connectivity={q.connectivity:.2f}")
                    if not q.argument_completeness_pass:
                        issues.append(f"arg_completeness={q.argument_completeness:.2f}")
                    if not q.orphan_ratio_pass:
                        issues.append(f"orphan_ratio={q.orphan_ratio:.2f}")
                    lines.append(f"- **{stats.book_id}**: {', '.join(issues)}")
                lines.append("")
        
        # Low coverage books section
        low_coverage_books = [
            s for s in report.book_stats 
            if s.status == "success" and s.coverage < LOW_COVERAGE_THRESHOLD
        ]
        if low_coverage_books:
            lines.append("## Low Coverage Books")
            lines.append("")
            lines.append(f"Books with coverage below {LOW_COVERAGE_THRESHOLD:.0%}:")
            lines.append("")
            for stats in low_coverage_books:
                lines.append(f"- **{stats.book_id}**: {stats.coverage:.1%}")
            lines.append("")
        
        # Warnings section
        if report.warnings:
            lines.append("## Warnings")
            lines.append("")
            for warning in report.warnings:
                lines.append(f"- ⚠️ {warning}")
            lines.append("")
        
        # Errors section
        if report.errors:
            lines.append("## Errors")
            lines.append("")
            for error in report.errors:
                lines.append(f"- ❌ {error}")
            lines.append("")
        
        # Orphan snippets details (if any)
        books_with_orphans = [s for s in report.book_stats if s.orphan_snippets]
        if books_with_orphans:
            lines.append("## Orphan Snippets Details")
            lines.append("")
            for stats in books_with_orphans:
                if len(stats.orphan_snippets) <= 10:
                    orphan_list = ", ".join(stats.orphan_snippets)
                else:
                    orphan_list = ", ".join(stats.orphan_snippets[:10]) + f" ... (+{len(stats.orphan_snippets) - 10} more)"
                lines.append(f"### {stats.book_id}")
                lines.append("")
                lines.append(f"**Count:** {len(stats.orphan_snippets)}")
                lines.append("")
                lines.append(f"**IDs:** {orphan_list}")
                lines.append("")
        
        return "\n".join(lines)
    
    def _get_report_path(self) -> Path:
        """获取报告文件路径"""
        return self.output_dir / "build_report.md"
