"""
Test Reporter

测试报告生成器，支持多种输出格式。

对照 design.md §2.1 目录结构
对照 Requirements R-6-1-12 ~ R-6-1-14
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, TextIO

from backend.testing.framework.runner import BatchResult, TestResult, TestStatus


class ReportFormat(str, Enum):
    """报告格式"""
    JSON = "json"
    JUNIT_XML = "junit"
    HTML = "html"
    TEXT = "text"


class TestReporter:
    """
    测试报告生成器
    
    对照 Requirements R-6-1-12 ~ R-6-1-14
    """
    
    def __init__(
        self,
        title: str = "LucidSelf Test Report",
        suite_name: str = "TestSuite",
    ):
        self.title = title
        self.suite_name = suite_name
    
    def generate(
        self,
        batch: BatchResult,
        format: ReportFormat = ReportFormat.JSON,
        output_path: Optional[Path] = None,
    ) -> str:
        """
        生成测试报告
        
        Args:
            batch: 批量测试结果
            format: 输出格式
            output_path: 输出文件路径 (可选)
            
        Returns:
            str: 报告内容
        """
        if format == ReportFormat.JSON:
            content = self._generate_json(batch)
        elif format == ReportFormat.JUNIT_XML:
            content = self._generate_junit_xml(batch)
        elif format == ReportFormat.HTML:
            content = self._generate_html(batch)
        elif format == ReportFormat.TEXT:
            content = self._generate_text(batch)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding="utf-8")
        
        return content
    
    def _generate_json(self, batch: BatchResult) -> str:
        """生成 JSON 格式报告"""
        data = {
            "title": self.title,
            "suite_name": self.suite_name,
            "summary": {
                "total": batch.total,
                "passed": batch.passed_count,
                "failed": batch.failed_count,
                "errors": batch.error_count,
                "skipped": batch.skipped_count,
                "pass_rate": batch.pass_rate,
                "duration_ms": batch.total_duration_ms,
            },
            "started_at": batch.started_at.isoformat() if batch.started_at else None,
            "finished_at": batch.finished_at.isoformat() if batch.finished_at else None,
            "results": [
                {
                    "test_id": r.test_id,
                    "status": r.status.value,
                    "passed": r.passed,
                    "duration_ms": r.duration_ms,
                    "error": r.error,
                    "error_type": r.error_type,
                    "details": r.details,
                    "runner_name": r.runner_name,
                    "executed_at": r.executed_at.isoformat(),
                }
                for r in batch.results
            ],
        }
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    def _generate_junit_xml(self, batch: BatchResult) -> str:
        """
        生成 JUnit XML 格式报告
        
        对照 R-6-1-13: 可集成 CI/CD (GitHub Actions)
        """
        # 创建根元素
        testsuite = ET.Element("testsuite")
        testsuite.set("name", self.suite_name)
        testsuite.set("tests", str(batch.total))
        testsuite.set("failures", str(batch.failed_count))
        testsuite.set("errors", str(batch.error_count))
        testsuite.set("skipped", str(batch.skipped_count))
        testsuite.set("time", str(batch.total_duration_ms / 1000))
        
        if batch.started_at:
            testsuite.set("timestamp", batch.started_at.isoformat())
        
        # 添加测试用例
        for result in batch.results:
            testcase = ET.SubElement(testsuite, "testcase")
            testcase.set("name", result.test_id)
            testcase.set("classname", result.runner_name or self.suite_name)
            testcase.set("time", str(result.duration_ms / 1000))
            
            if result.status == TestStatus.FAILED:
                failure = ET.SubElement(testcase, "failure")
                failure.set("message", result.error or "Assertion failed")
                failure.set("type", "AssertionError")
                if result.details:
                    failure.text = json.dumps(result.details, indent=2)
            
            elif result.status == TestStatus.ERROR:
                error = ET.SubElement(testcase, "error")
                error.set("message", result.error or "Test error")
                error.set("type", result.error_type or "Exception")
            
            elif result.status == TestStatus.SKIPPED:
                skipped = ET.SubElement(testcase, "skipped")
                if result.details.get("skip_reason"):
                    skipped.set("message", result.details["skip_reason"])
        
        # 转换为字符串
        return ET.tostring(testsuite, encoding="unicode", xml_declaration=True)
    
    def _generate_html(self, batch: BatchResult) -> str:
        """
        生成 HTML 格式报告
        
        对照 R-6-1-12
        """
        # 简化的 HTML 模板
        status_colors = {
            TestStatus.PASSED: "#4caf50",
            TestStatus.FAILED: "#f44336",
            TestStatus.ERROR: "#ff9800",
            TestStatus.SKIPPED: "#9e9e9e",
        }
        
        rows = []
        for r in batch.results:
            color = status_colors.get(r.status, "#000")
            error_cell = f'<td style="color: red;">{r.error or ""}</td>' if r.error else '<td>-</td>'
            rows.append(f'''
            <tr>
                <td>{r.test_id}</td>
                <td style="color: {color}; font-weight: bold;">{r.status.value.upper()}</td>
                <td>{r.duration_ms:.2f}ms</td>
                {error_cell}
                <td>{r.runner_name}</td>
            </tr>
            ''')
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        .summary {{ background: #f5f5f5; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .summary-item {{ display: inline-block; margin-right: 30px; }}
        .summary-value {{ font-size: 24px; font-weight: bold; }}
        .passed {{ color: #4caf50; }}
        .failed {{ color: #f44336; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background: #f0f0f0; }}
        tr:hover {{ background: #f9f9f9; }}
    </style>
</head>
<body>
    <h1>{self.title}</h1>
    
    <div class="summary">
        <div class="summary-item">
            <div class="summary-value">{batch.total}</div>
            <div>Total</div>
        </div>
        <div class="summary-item">
            <div class="summary-value passed">{batch.passed_count}</div>
            <div>Passed</div>
        </div>
        <div class="summary-item">
            <div class="summary-value failed">{batch.failed_count}</div>
            <div>Failed</div>
        </div>
        <div class="summary-item">
            <div class="summary-value">{batch.error_count}</div>
            <div>Errors</div>
        </div>
        <div class="summary-item">
            <div class="summary-value">{batch.pass_rate:.1%}</div>
            <div>Pass Rate</div>
        </div>
        <div class="summary-item">
            <div class="summary-value">{batch.total_duration_ms:.0f}ms</div>
            <div>Duration</div>
        </div>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Test ID</th>
                <th>Status</th>
                <th>Duration</th>
                <th>Error</th>
                <th>Runner</th>
            </tr>
        </thead>
        <tbody>
            {"".join(rows)}
        </tbody>
    </table>
    
    <footer style="margin-top: 20px; color: #666;">
        Generated at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </footer>
</body>
</html>'''
        
        return html
    
    def _generate_text(self, batch: BatchResult) -> str:
        """生成纯文本格式报告"""
        lines = [
            f"{'=' * 60}",
            f" {self.title}",
            f"{'=' * 60}",
            "",
            f"Total: {batch.total}",
            f"Passed: {batch.passed_count}",
            f"Failed: {batch.failed_count}",
            f"Errors: {batch.error_count}",
            f"Skipped: {batch.skipped_count}",
            f"Pass Rate: {batch.pass_rate:.1%}",
            f"Duration: {batch.total_duration_ms:.0f}ms",
            "",
            f"{'-' * 60}",
            " Results",
            f"{'-' * 60}",
        ]
        
        for r in batch.results:
            status = r.status.value.upper()
            status_icon = "✓" if r.passed else "✗"
            lines.append(f"[{status_icon}] {r.test_id}: {status} ({r.duration_ms:.2f}ms)")
            if r.error:
                lines.append(f"    Error: {r.error}")
        
        lines.append("")
        lines.append(f"{'=' * 60}")
        
        return "\n".join(lines)
    
    def print_summary(self, batch: BatchResult) -> None:
        """打印测试摘要到控制台"""
        print(self._generate_text(batch))
