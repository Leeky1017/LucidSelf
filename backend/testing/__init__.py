"""
LucidSelf Testing Framework

三层测试金字塔框架：
- Unit (RuleTestCase): 规则级测试，覆盖率100%，每次提交运行
- Integration (GoldenCase): 引擎级测试，核心场景100%，每日CI/CD
- Product (NarrativeGolden): 叙事级测试，关键旅程100%，发布前必过

对照文档:
- docs/数据契约_Schema定义规范_v1.md §8 测试Schema
- .kiro/specs/testing-ops/design.md §2 测试框架设计
"""

# 延迟导入避免循环依赖
def __getattr__(name: str):
    """延迟导入"""
    if name in ("TestRunner", "TestResult", "TestStatus", "BatchResult"):
        from backend.testing.framework.runner import (
            TestRunner, TestResult, TestStatus, BatchResult
        )
        return locals()[name]
    
    if name in ("RuleAssertions", "FusionAssertions", "NarrativeAssertions"):
        from backend.testing.framework.assertions import (
            RuleAssertions, FusionAssertions, NarrativeAssertions
        )
        return locals()[name]
    
    if name == "TestFixtures":
        from backend.testing.framework.fixtures import TestFixtures
        return TestFixtures
    
    if name in ("TestReporter", "ReportFormat"):
        from backend.testing.framework.reporter import TestReporter, ReportFormat
        return locals()[name]
    
    if name == "RuleTestRunner":
        from backend.testing.unit.rule_runner import RuleTestRunner
        return RuleTestRunner
    
    if name == "GoldenCaseRunner":
        from backend.testing.integration.golden_runner import GoldenCaseRunner
        return GoldenCaseRunner
    
    if name == "NarrativeGoldenRunner":
        from backend.testing.product.narrative_runner import NarrativeGoldenRunner
        return NarrativeGoldenRunner
    
    if name == "EvalAgent":
        from backend.testing.product.eval_agent import EvalAgent
        return EvalAgent
    
    if name == "DriftDetector":
        from backend.testing.integration.drift_detector import DriftDetector
        return DriftDetector
    
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    # Base
    "TestRunner",
    "TestResult",
    "TestStatus",
    "BatchResult",
    # Assertions
    "RuleAssertions",
    "FusionAssertions",
    "NarrativeAssertions",
    # Fixtures
    "TestFixtures",
    # Reporter
    "TestReporter",
    "ReportFormat",
    # Runners
    "RuleTestRunner",
    "GoldenCaseRunner",
    "NarrativeGoldenRunner",
    # Helpers
    "EvalAgent",
    "DriftDetector",
]
