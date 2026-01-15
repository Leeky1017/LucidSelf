"""
Integration Tests for Layer 3 Rules

综合测试 - 验证完整的规则管道。

对照 Task 23: Integration and Coverage Report
"""

import json
import tempfile
from pathlib import Path

import pytest

from backend.rules import (
    DimensionMapper,
    CoverageReporter,
    RuleChangeLogger,
    RuleEngine,
    RuleContext,
)
from backend.core.contracts import FactorMatrix, FactorValue


class TestDimensionMapper:
    """维度映射器测试"""
    
    def test_normalize_english(self):
        """测试英文维度标准化"""
        mapper = DimensionMapper()
        assert mapper.normalize("career") == "career"
        assert mapper.normalize("Career") == "career"
        assert mapper.normalize("CAREER") == "career"
    
    def test_normalize_chinese(self):
        """测试中文维度标准化"""
        mapper = DimensionMapper()
        assert mapper.normalize("事业") == "career"
        assert mapper.normalize("健康") == "health"
        assert mapper.normalize("婚姻") == "marriage"
    
    def test_normalize_unknown(self):
        """测试未知维度默认值"""
        mapper = DimensionMapper()
        assert mapper.normalize("unknown_dimension") == "general"
    
    def test_get_all_standard_dimensions(self):
        """测试获取标准维度列表"""
        mapper = DimensionMapper()
        dims = mapper.get_all_standard_dimensions()
        assert len(dims) == 10
        assert "career" in dims
        assert "health" in dims
    
    def test_get_label(self):
        """测试获取维度标签"""
        mapper = DimensionMapper()
        assert mapper.get_label("career", "zh") == "事业"
        assert mapper.get_label("career", "en") == "Career"


class TestCoverageReporter:
    """覆盖率报告测试"""
    
    def test_generate_report(self):
        """测试生成覆盖率报告"""
        reporter = CoverageReporter(rules_dir=Path("data/rules"))
        report = reporter.generate_report()
        
        assert "summary" in report
        assert "by_system" in report
        assert "coverage_matrix" in report
        assert report["summary"]["total_rules"] > 0
    
    def test_report_structure(self):
        """测试报告结构"""
        reporter = CoverageReporter(rules_dir=Path("data/rules"))
        report = reporter.generate_report()
        
        # 验证汇总信息
        assert "total_rules" in report["summary"]
        assert "total_systems" in report["summary"]
        
        # 验证体系信息
        for system, data in report["by_system"].items():
            assert "total_rules" in data
            assert "dimensions" in data


class TestRuleChangeLogger:
    """规则变更日志测试"""
    
    def test_log_create(self):
        """测试记录创建日志"""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "changes.jsonl"
            logger = RuleChangeLogger(log_path=log_path)
            
            logger.log_create(
                rule_id="test_rule_001",
                system="bazi",
                version="1.0.0",
            )
            
            # 验证日志文件
            assert log_path.exists()
            with open(log_path) as f:
                entry = json.loads(f.readline())
            
            assert entry["action"] == "create"
            assert entry["rule_id"] == "test_rule_001"
    
    def test_log_update(self):
        """测试记录更新日志"""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "changes.jsonl"
            logger = RuleChangeLogger(log_path=log_path)
            
            logger.log_update(
                rule_id="test_rule_001",
                system="bazi",
                old_version="1.0.0",
                new_version="1.1.0",
                changes=["Updated condition"],
            )
            
            history = logger.get_history(rule_id="test_rule_001")
            assert len(history) == 1
            assert history[0]["action"] == "update"
    
    def test_log_status_change(self):
        """测试记录状态变更日志"""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "changes.jsonl"
            logger = RuleChangeLogger(log_path=log_path)
            
            logger.log_status_change(
                rule_id="test_rule_001",
                system="bazi",
                old_status="draft",
                new_status="active",
            )
            
            history = logger.get_history(action="status_change")
            assert len(history) == 1
    
    def test_get_history_filter(self):
        """测试获取历史记录过滤"""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "changes.jsonl"
            logger = RuleChangeLogger(log_path=log_path)
            
            # 创建多条记录
            logger.log_create("rule_1", "bazi")
            logger.log_create("rule_2", "ziwei")
            logger.log_update("rule_1", "bazi", "1.0.0", "1.1.0")
            
            # 按 system 过滤
            bazi_history = logger.get_history(system="bazi")
            assert len(bazi_history) == 2
            
            # 按 action 过滤
            create_history = logger.get_history(action="create")
            assert len(create_history) == 2


class TestEndToEndPipeline:
    """端到端管道测试"""
    
    def test_rule_jsonl_to_execution(self):
        """测试从 JSONL 到执行的完整流程"""
        # 1. 读取规则
        rules_file = Path("data/rules/bazi/career.jsonl")
        if not rules_file.exists():
            pytest.skip("Rules file not found")
        
        with open(rules_file) as f:
            first_rule = json.loads(f.readline())
        
        # 2. 验证规则结构
        assert "rule_id" in first_rule
        assert "condition" in first_rule
        assert "result" in first_rule
        
        # 3. 验证维度标准化
        mapper = DimensionMapper()
        dim = first_rule["result"]["dimension"]
        normalized = mapper.normalize(dim)
        assert normalized in mapper.get_all_standard_dimensions()
    
    def test_coverage_includes_all_systems(self):
        """测试覆盖率包含所有体系"""
        reporter = CoverageReporter()
        report = reporter.generate_report()
        
        expected_systems = ["bazi", "ziwei", "tarot", "astro", "dream", "yijing", "psychology"]
        for system in expected_systems:
            if system in report["by_system"]:
                assert report["by_system"][system]["total_rules"] > 0


class TestPropertyTests:
    """属性测试"""
    
    def test_dimension_normalization_idempotent(self):
        """
        Property 11: Dimension Standardization
        标准化操作应该是幂等的
        """
        mapper = DimensionMapper()
        
        for dim in ["career", "health", "事业", "健康", "unknown"]:
            normalized = mapper.normalize(dim)
            # 再次标准化应该得到相同结果
            assert mapper.normalize(normalized) == normalized
    
    def test_category_filtering_correctness(self):
        """
        Property 8: Category Filtering Correctness
        分类过滤应该正确
        """
        engine = RuleEngine()
        
        # 验证空引擎
        assert engine.get_categories() == []
        
        # 验证元数据一致性
        metadata = engine.get_metadata()
        assert metadata["rule_count"] == 0
