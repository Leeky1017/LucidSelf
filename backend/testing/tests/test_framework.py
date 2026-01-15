"""
Tests for Testing Framework

测试框架的单元测试。
"""

import asyncio
import pytest
from datetime import datetime, timedelta
from unittest.mock import MagicMock, AsyncMock, patch

from backend.testing.framework.runner import (
    TestRunner,
    TestResult,
    TestStatus,
    BatchResult,
)
from backend.testing.framework.assertions import (
    RuleAssertions,
    FusionAssertions,
    NarrativeAssertions,
    AssertionError,
)
from backend.testing.framework.fixtures import (
    TestFixtures,
    MockRuleResult,
    MockFusionResult,
)
from backend.testing.framework.reporter import (
    TestReporter,
    ReportFormat,
)


# =============================================================================
# TestResult Tests
# =============================================================================

class TestTestResult:
    """TestResult 单元测试"""
    
    def test_success_creation(self):
        """测试成功结果创建"""
        result = TestResult.success(
            test_id="test_001",
            duration_ms=100.0,
            details={"key": "value"},
        )
        
        assert result.test_id == "test_001"
        assert result.status == TestStatus.PASSED
        assert result.passed is True
        assert result.duration_ms == 100.0
        assert result.details == {"key": "value"}
        assert result.error is None
    
    def test_failure_creation(self):
        """测试失败结果创建"""
        result = TestResult.failure(
            test_id="test_002",
            duration_ms=50.0,
            error="Assertion failed",
            details={"expected": 1, "actual": 2},
        )
        
        assert result.test_id == "test_002"
        assert result.status == TestStatus.FAILED
        assert result.passed is False
        assert result.error == "Assertion failed"
    
    def test_error_creation(self):
        """测试错误结果创建"""
        result = TestResult.create_error(
            test_id="test_003",
            duration_ms=10.0,
            error_msg="RuntimeError: something wrong",
            error_type="RuntimeError",
        )
        
        assert result.status == TestStatus.ERROR
        assert result.passed is False
        assert result.error_type == "RuntimeError"
    
    def test_skipped_creation(self):
        """测试跳过结果创建"""
        result = TestResult.skipped(
            test_id="test_004",
            reason="Not implemented",
        )
        
        assert result.status == TestStatus.SKIPPED
        assert result.passed is True  # 跳过不算失败
        assert result.duration_ms == 0.0
        assert result.details["skip_reason"] == "Not implemented"


# =============================================================================
# BatchResult Tests
# =============================================================================

class TestBatchResult:
    """BatchResult 单元测试"""
    
    def test_empty_batch(self):
        """测试空批次"""
        batch = BatchResult()
        
        assert batch.total == 0
        assert batch.passed_count == 0
        assert batch.failed_count == 0
        assert batch.pass_rate == 0.0
        assert batch.all_passed is True
    
    def test_batch_with_results(self):
        """测试有结果的批次"""
        batch = BatchResult()
        batch.add(TestResult.success("t1", 10.0))
        batch.add(TestResult.success("t2", 20.0))
        batch.add(TestResult.failure("t3", 15.0, "Failed"))
        batch.finish()
        
        assert batch.total == 3
        assert batch.passed_count == 2
        assert batch.failed_count == 1
        assert batch.pass_rate == pytest.approx(2/3)
        assert batch.all_passed is False
        assert batch.total_duration_ms == 45.0
    
    def test_all_passed(self):
        """测试全部通过"""
        batch = BatchResult()
        batch.add(TestResult.success("t1", 10.0))
        batch.add(TestResult.success("t2", 20.0))
        
        assert batch.all_passed is True


# =============================================================================
# RuleAssertions Tests
# =============================================================================

class TestRuleAssertions:
    """RuleAssertions 单元测试"""
    
    def test_assert_hit_success(self):
        """测试命中断言成功"""
        result = MockRuleResult(hit=True, dimension="事业", level="吉", confidence=0.9)
        
        # 不应抛出异常
        RuleAssertions.assert_rule_hit(
            result,
            expected_hit=True,
            expected_dimension="事业",
            expected_level="吉",
            confidence_range=(0.8, 1.0),
        )
    
    def test_assert_hit_failure_wrong_hit(self):
        """测试命中断言失败 - 命中状态错误"""
        result = MockRuleResult(hit=False)
        
        with pytest.raises(AssertionError) as exc:
            RuleAssertions.assert_rule_hit(result, expected_hit=True)
        
        assert len(exc.value.diffs) > 0
    
    def test_assert_hit_failure_wrong_dimension(self):
        """测试命中断言失败 - 维度错误"""
        result = MockRuleResult(hit=True, dimension="财富")
        
        with pytest.raises(AssertionError) as exc:
            RuleAssertions.assert_rule_hit(
                result,
                expected_hit=True,
                expected_dimension="事业",
            )
        
        assert len(exc.value.diffs) > 0
        assert exc.value.diffs[0].field == "dimension"
    
    def test_assert_hit_failure_confidence_out_of_range(self):
        """测试命中断言失败 - 置信度超出范围"""
        result = MockRuleResult(hit=True, confidence=0.5)
        
        with pytest.raises(AssertionError) as exc:
            RuleAssertions.assert_rule_hit(
                result,
                expected_hit=True,
                confidence_range=(0.8, 1.0),
            )
        
        assert len(exc.value.diffs) > 0
        assert exc.value.diffs[0].field == "confidence"
    
    def test_assert_not_hit(self):
        """测试未命中断言"""
        result = MockRuleResult(hit=False)
        
        RuleAssertions.assert_rule_not_hit(result)
    
    def test_assert_hit_count(self):
        """测试命中数量断言"""
        results = [
            MockRuleResult(hit=True),
            MockRuleResult(hit=True),
            MockRuleResult(hit=False),
        ]
        
        RuleAssertions.assert_hit_count(results, expected_count=2)
    
    def test_assert_hit_count_with_tolerance(self):
        """测试命中数量断言 - 带容差"""
        results = [MockRuleResult(hit=True)] * 3
        
        RuleAssertions.assert_hit_count(results, expected_count=2, tolerance=1)


# =============================================================================
# FusionAssertions Tests
# =============================================================================

class TestFusionAssertions:
    """FusionAssertions 单元测试"""
    
    def test_assert_fusion_success(self):
        """测试融合断言成功"""
        result = MockFusionResult(
            themes=["事业发展", "财富积累"],
            cross_validation_score=0.85,
        )
        
        FusionAssertions.assert_fusion_result(
            result,
            expected_themes=["事业发展"],
            min_cross_validation=0.8,
        )
    
    def test_assert_fusion_missing_theme(self):
        """测试融合断言失败 - 缺少主题"""
        result = MockFusionResult(themes=["事业发展"])
        
        with pytest.raises(AssertionError) as exc:
            FusionAssertions.assert_fusion_result(
                result,
                expected_themes=["事业发展", "健康"],
            )
        
        assert len(exc.value.diffs) > 0
        assert "健康" in str(exc.value.diffs[0].message)
    
    def test_assert_fusion_forbidden_theme(self):
        """测试融合断言失败 - 包含禁用主题"""
        result = MockFusionResult(themes=["事业发展", "命中注定"])
        
        with pytest.raises(AssertionError) as exc:
            FusionAssertions.assert_fusion_result(
                result,
                forbidden_themes=["命中注定"],
            )
        
        assert len(exc.value.diffs) > 0
    
    def test_assert_drift_within_threshold(self):
        """测试漂移断言 - 在阈值内"""
        expected = {"a": 1, "b": 2}
        actual = {"a": 1, "b": 2}
        
        drift = FusionAssertions.assert_drift(expected, actual, max_drift=0.1)
        assert drift == 0.0
    
    def test_assert_drift_exceeds_threshold(self):
        """测试漂移断言 - 超出阈值"""
        expected = {"a": 1, "b": 2}
        actual = {"a": 3, "b": 4}
        
        with pytest.raises(AssertionError) as exc:
            FusionAssertions.assert_drift(expected, actual, max_drift=0.1)
        
        assert "exceeds" in str(exc.value)


# =============================================================================
# NarrativeAssertions Tests
# =============================================================================

class TestNarrativeAssertions:
    """NarrativeAssertions 单元测试"""
    
    def test_assert_quality_success(self):
        """测试叙事质量断言成功"""
        narrative = "今年事业发展良好，建议把握机会积极行动。"
        
        NarrativeAssertions.assert_narrative_quality(
            narrative,
            must_include_themes=["事业发展"],
            forbidden_expressions=["命中注定"],
            min_length=10,
        )
    
    def test_assert_quality_missing_theme(self):
        """测试叙事质量断言失败 - 缺少主题"""
        narrative = "这是一段普通的叙事。"
        
        with pytest.raises(AssertionError):
            NarrativeAssertions.assert_narrative_quality(
                narrative,
                must_include_themes=["事业发展"],
            )
    
    def test_assert_quality_forbidden_expression(self):
        """测试叙事质量断言失败 - 包含禁用表述"""
        narrative = "你命中注定会成功。"
        
        with pytest.raises(AssertionError):
            NarrativeAssertions.assert_narrative_quality(
                narrative,
                forbidden_expressions=["命中注定"],
            )
    
    def test_assert_quality_too_short(self):
        """测试叙事质量断言失败 - 太短"""
        narrative = "短"
        
        with pytest.raises(AssertionError):
            NarrativeAssertions.assert_narrative_quality(
                narrative,
                min_length=100,
            )


# =============================================================================
# TestFixtures Tests
# =============================================================================

class TestTestFixtures:
    """TestFixtures 单元测试"""
    
    def test_mock_factors_bazi(self):
        """测试八字因子生成"""
        factors = TestFixtures.mock_factors("bazi")
        
        assert "day_master" in factors
        assert "month_branch" in factors
        assert "season" in factors
    
    def test_mock_factors_astro(self):
        """测试占星因子生成"""
        factors = TestFixtures.mock_factors("astro")
        
        assert "sun_sign" in factors
        assert "moon_sign" in factors
    
    def test_mock_birth_data(self):
        """测试出生数据生成"""
        data = TestFixtures.mock_birth_data(year=1990, month=5)
        
        assert data["year"] == 1990
        assert data["month"] == 5
        assert "timezone" in data
        assert "longitude" in data
    
    def test_mock_rule_test_case(self):
        """测试规则测试用例生成"""
        case = TestFixtures.mock_rule_test_case(
            test_id="custom_test",
            expect_hit=False,
        )
        
        assert case["test_id"] == "custom_test"
        assert case["expect_hit"] is False
        assert "mock_factors" in case
    
    def test_mock_golden_case(self):
        """测试黄金用例生成"""
        case = TestFixtures.mock_golden_case(case_id="golden_001")
        
        assert case["case_id"] == "golden_001"
        assert "birth_data" in case
        assert "expected_results" in case
    
    def test_mock_narrative_golden(self):
        """测试叙事黄金标准生成"""
        golden = TestFixtures.mock_narrative_golden(
            golden_id="narr_001",
            min_quality_score=0.9,
        )
        
        assert golden["golden_id"] == "narr_001"
        assert golden["min_quality_score"] == 0.9
        assert "must_include_themes" in golden


# =============================================================================
# TestReporter Tests
# =============================================================================

class TestTestReporter:
    """TestReporter 单元测试"""
    
    def test_generate_json(self):
        """测试 JSON 报告生成"""
        batch = BatchResult()
        batch.add(TestResult.success("t1", 10.0))
        batch.add(TestResult.failure("t2", 20.0, "Failed"))
        batch.finish()
        
        reporter = TestReporter(title="Test Report")
        json_report = reporter.generate(batch, ReportFormat.JSON)
        
        import json
        data = json.loads(json_report)
        
        assert data["title"] == "Test Report"
        assert data["summary"]["total"] == 2
        assert data["summary"]["passed"] == 1
        assert data["summary"]["failed"] == 1
        assert len(data["results"]) == 2
    
    def test_generate_junit_xml(self):
        """测试 JUnit XML 报告生成"""
        batch = BatchResult()
        batch.add(TestResult.success("t1", 10.0))
        batch.add(TestResult.failure("t2", 20.0, "Assertion failed"))
        batch.finish()
        
        reporter = TestReporter(suite_name="MySuite")
        xml_report = reporter.generate(batch, ReportFormat.JUNIT_XML)
        
        assert '<?xml version' in xml_report
        assert 'testsuite' in xml_report
        assert 'MySuite' in xml_report
        assert 'testcase' in xml_report
        assert 'failure' in xml_report
    
    def test_generate_html(self):
        """测试 HTML 报告生成"""
        batch = BatchResult()
        batch.add(TestResult.success("t1", 10.0))
        batch.finish()
        
        reporter = TestReporter(title="HTML Report")
        html_report = reporter.generate(batch, ReportFormat.HTML)
        
        assert '<!DOCTYPE html>' in html_report
        assert 'HTML Report' in html_report
        assert 't1' in html_report
    
    def test_generate_text(self):
        """测试文本报告生成"""
        batch = BatchResult()
        batch.add(TestResult.success("t1", 10.0))
        batch.add(TestResult.failure("t2", 20.0, "Failed"))
        batch.finish()
        
        reporter = TestReporter()
        text_report = reporter.generate(batch, ReportFormat.TEXT)
        
        assert "Total: 2" in text_report
        assert "Passed: 1" in text_report
        assert "Failed: 1" in text_report
        assert "[✓] t1" in text_report
        assert "[✗] t2" in text_report
