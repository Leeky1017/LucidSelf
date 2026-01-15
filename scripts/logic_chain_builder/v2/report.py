"""
BuildReportGeneratorV2 - 升级版构建报告生成器

生成包含所有v2质量指标的报告。
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.v2.models import (
    BookBuildResult,
    BookStatsV2,
    BuildReportV2,
    QualityReportV2,
    ThresholdFailure,
)

logger = get_logger(__name__)


class BuildReportGeneratorV2:
    """
    升级版构建报告生成器
    
    生成包含所有6个质量维度的报告。
    """
    
    OUTPUT_DIR = "data/logic_chains"
    
    def generate(
        self,
        results: List[BookBuildResult],
        quality_reports: Dict[str, QualityReportV2]
    ) -> BuildReportV2:
        """
        生成包含所有v2指标的报告
        
        Args:
            results: BookBuildResult列表
            quality_reports: book_id -> QualityReportV2映射
            
        Returns:
            BuildReportV2
        """
        book_stats = []
        threshold_failures = []
        
        for result in results:
            qr = quality_reports.get(result.book_id)
            stats = self._build_book_stats(result, qr)
            book_stats.append(stats)
            
            # 收集阈值失败
            for failure in stats.threshold_failures:
                threshold_failures.append(ThresholdFailure(
                    book_id=result.book_id,
                    metric=failure.split(":")[0] if ":" in failure else failure,
                    actual_value=0.0,  # 简化处理
                    threshold=0.0,
                    remediation=f"Review {result.book_id} quality metrics"
                ))
        
        # 计算总边推断分布
        edge_breakdown = self._calc_edge_breakdown(results)
        
        # 计算总聚类层级分布
        cluster_breakdown = self._calc_cluster_breakdown(results)
        
        # 计算平均质量
        avg_quality = self._calc_average_quality(quality_reports)
        
        return BuildReportV2(
            generated_at=datetime.now(),
            total_books=len(results),
            successful_books=sum(1 for r in results if r.success),
            failed_books=sum(1 for r in results if not r.success),
            book_stats=book_stats,
            edge_inference_breakdown=edge_breakdown,
            cluster_level_breakdown=cluster_breakdown,
            threshold_failures=threshold_failures,
            average_quality=avg_quality,
        )
    
    def _build_book_stats(
        self,
        result: BookBuildResult,
        quality_report: Optional[QualityReportV2]
    ) -> BookStatsV2:
        """构建单本书籍统计"""
        edge_breakdown = {}
        cluster_breakdown = {}
        threshold_failures = []
        
        if result.chain:
            # 统计边推断方法
            for edge in result.chain.edges:
                method = edge.metadata.get("inferred_from", "unknown")
                edge_breakdown[method] = edge_breakdown.get(method, 0) + 1
            
            # 统计聚类层级
            for node in result.chain.nodes:
                level = node.metadata.get("cluster_level", "L1")
                cluster_breakdown[level] = cluster_breakdown.get(level, 0) + 1
        
        # 检查阈值（使用书籍特定阈值）
        if quality_report:
            from scripts.logic_chain_builder.v2.quality_scorer import SemanticQualityScorer
            scorer = SemanticQualityScorer()
            _, failures = scorer.passes_thresholds(quality_report, book_id=result.book_id)
            threshold_failures = failures
        
        return BookStatsV2(
            book_id=result.book_id,
            snippet_count=len(result.chain.nodes) if result.chain else 0,
            node_count=len(result.chain.nodes) if result.chain else 0,
            edge_count=len(result.chain.edges) if result.chain else 0,
            coverage=1.0 if result.success else 0.0,
            quality_report=quality_report,
            edge_inference_breakdown=edge_breakdown,
            cluster_level_breakdown=cluster_breakdown,
            status="success" if result.success else "failed",
            error_message=result.error_message,
            threshold_failures=threshold_failures,
        )
    
    def _calc_edge_breakdown(
        self,
        results: List[BookBuildResult]
    ) -> Dict[str, int]:
        """计算边推断方法分布"""
        breakdown = {
            "explicit_relation": 0,
            "factor_semantic": 0,
            "condition_dependency": 0,
            "sequential_order": 0,
            "orphan_fix": 0,
        }
        
        for result in results:
            if result.chain:
                for edge in result.chain.edges:
                    method = edge.metadata.get("inferred_from", "unknown")
                    if method in breakdown:
                        breakdown[method] += 1
        
        return breakdown
    
    def _calc_cluster_breakdown(
        self,
        results: List[BookBuildResult]
    ) -> Dict[str, int]:
        """计算聚类层级分布"""
        breakdown = {"L1": 0, "L2": 0, "L3": 0}
        
        for result in results:
            if result.chain:
                for node in result.chain.nodes:
                    level = node.metadata.get("cluster_level", "L1")
                    if level in breakdown:
                        breakdown[level] += 1
        
        return breakdown
    
    def _calc_average_quality(
        self,
        quality_reports: Dict[str, QualityReportV2]
    ) -> Optional[QualityReportV2]:
        """计算平均质量指标"""
        if not quality_reports:
            return None
        
        n = len(quality_reports)
        total = QualityReportV2()
        
        for qr in quality_reports.values():
            total.connectivity += qr.connectivity
            total.orphan_ratio += qr.orphan_ratio
            total.reasoning_coherence += qr.reasoning_coherence
            total.condition_coverage += qr.condition_coverage
            total.argument_completeness += qr.argument_completeness
            total.node_homogeneity += qr.node_homogeneity
        
        return QualityReportV2(
            connectivity=total.connectivity / n,
            orphan_ratio=total.orphan_ratio / n,
            reasoning_coherence=total.reasoning_coherence / n,
            condition_coverage=total.condition_coverage / n,
            argument_completeness=total.argument_completeness / n,
            node_homogeneity=total.node_homogeneity / n,
        )
    
    def write(self, report: BuildReportV2):
        """输出报告到markdown和JSON"""
        output_dir = Path(self.OUTPUT_DIR)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Markdown output
        md_path = output_dir / "build_report_v2.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(self._format_markdown(report))
        
        # JSON output
        json_path = output_dir / "build_report_v2.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(
                report.model_dump(),
                f,
                ensure_ascii=False,
                indent=2,
                default=str
            )
        
        logger.info(f"Reports written to {md_path} and {json_path}")
    
    def _format_markdown(self, report: BuildReportV2) -> str:
        """格式化为Markdown"""
        lines = [
            "# Logic Chain Build Report V2",
            "",
            f"**Generated at**: {report.generated_at}",
            "",
            "## Summary",
            "",
            f"- **Total Books**: {report.total_books}",
            f"- **Successful**: {report.successful_books}",
            f"- **Failed**: {report.failed_books}",
            "",
        ]
        
        # 平均质量
        if report.average_quality:
            lines.extend([
                "## Average Quality Metrics",
                "",
                f"| Metric | Value |",
                f"|--------|-------|",
                f"| Connectivity | {report.average_quality.connectivity:.2f} |",
                f"| Orphan Ratio | {report.average_quality.orphan_ratio:.2f} |",
                f"| Reasoning Coherence | {report.average_quality.reasoning_coherence:.2f} |",
                f"| Condition Coverage | {report.average_quality.condition_coverage:.2f} |",
                f"| Argument Completeness | {report.average_quality.argument_completeness:.2f} |",
                f"| Node Homogeneity | {report.average_quality.node_homogeneity:.2f} |",
                "",
            ])
        
        # 边推断分布
        lines.extend([
            "## Edge Inference Breakdown",
            "",
            "| Method | Count |",
            "|--------|-------|",
        ])
        for method, count in report.edge_inference_breakdown.items():
            lines.append(f"| {method} | {count} |")
        lines.append("")
        
        # 聚类层级分布
        lines.extend([
            "## Cluster Level Breakdown",
            "",
            "| Level | Count |",
            "|-------|-------|",
        ])
        for level, count in report.cluster_level_breakdown.items():
            lines.append(f"| {level} | {count} |")
        lines.append("")
        
        # 阈值失败
        if report.threshold_failures:
            lines.extend([
                "## Threshold Failures",
                "",
                "| Book | Metric | Remediation |",
                "|------|--------|-------------|",
            ])
            for failure in report.threshold_failures:
                lines.append(f"| {failure.book_id} | {failure.metric} | {failure.remediation} |")
            lines.append("")
        
        # 各书籍详情
        lines.extend([
            "## Book Details",
            "",
        ])
        for stats in report.book_stats:
            lines.extend([
                f"### {stats.book_id}",
                "",
                f"- **Status**: {stats.status}",
                f"- **Nodes**: {stats.node_count}",
                f"- **Edges**: {stats.edge_count}",
            ])
            if stats.quality_report:
                qr = stats.quality_report
                lines.extend([
                    f"- **Connectivity**: {qr.connectivity:.2f}",
                    f"- **Reasoning Coherence**: {qr.reasoning_coherence:.2f}",
                    f"- **Node Homogeneity**: {qr.node_homogeneity:.2f}",
                ])
            if stats.error_message:
                lines.append(f"- **Error**: {stats.error_message}")
            lines.append("")
        
        return "\n".join(lines)


# 导出
__all__ = ["BuildReportGeneratorV2", "BuildReportV2", "BookStatsV2"]
