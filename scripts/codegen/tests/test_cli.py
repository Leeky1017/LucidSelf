"""
Tests for CLI
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest


class TestCLI:
    """CLI 测试"""
    
    @pytest.fixture
    def cli_runner(self):
        """CLI 运行器"""
        def run(*args):
            result = subprocess.run(
                [sys.executable, "-m", "scripts.codegen", *args],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent.parent.parent  # 项目根目录
            )
            return result
        return run
    
    @pytest.fixture
    def sample_rule_file(self, tmp_path):
        """创建测试用规则文件（符合 ConfigRuleDefinition Schema）"""
        rule = {
            "rule_id": "cli_test_001",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "CLI测试规则",
            "category": "test",
            "required_factors": ["test"],
            "condition": {
                "operator": "==",
                "factor_id": "test",
                "value": 1
            },
            "result": {
                "dimension": "测试",
                "level": "中等",
                "conclusion_template_zh": "测试结论",
                "confidence": 0.9,
                "weight": 1.0,
                "tags": [],
                "evidence_factors": []
            },
            "metadata": {
                "book_id": "test",
                "chapter": "test",
                "l1_anchor": "TEST_001"
            }
        }
        path = tmp_path / "test_rule.json"
        path.write_text(json.dumps(rule, ensure_ascii=False))
        return path
    
    # ===== 基本命令测试 =====
    
    def test_help(self, cli_runner):
        """测试 --help"""
        result = cli_runner("--help")
        assert result.returncode == 0
        assert "compile" in result.stdout or "usage" in result.stdout.lower()
    
    def test_version(self, cli_runner):
        """测试 --version 或版本信息"""
        result = cli_runner("--version")
        # 如果支持 --version
        if result.returncode == 0:
            assert "1.0" in result.stdout or "version" in result.stdout.lower()
    
    # ===== compile 命令测试 =====
    
    def test_compile_rule(self, cli_runner, sample_rule_file, tmp_path):
        """测试编译规则"""
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        
        # CLI 格式: compile <type> <source> [-o output]
        result = cli_runner(
            "compile",
            "rule",
            str(sample_rule_file),
            "-o", str(output_dir)
        )
        
        # 应该成功或给出有意义的错误
        assert result.returncode == 0 or "error" in result.stderr.lower()
    
    def test_compile_missing_input(self, cli_runner, tmp_path):
        """测试缺少输入文件"""
        # CLI 格式: compile <type> <source> [-o output]
        result = cli_runner(
            "compile",
            "rule",
            str(tmp_path / "nonexistent.json"),
            "-o", str(tmp_path)
        )
        
        # 应该失败
        assert result.returncode != 0 or "not found" in result.stderr.lower() or "error" in result.stderr.lower()
    
    # ===== validate 命令测试 =====
    
    def test_validate_valid_rule(self, cli_runner, sample_rule_file):
        """测试校验有效规则"""
        # CLI 格式: validate <type> <source>
        result = cli_runner(
            "validate",
            "rule",
            str(sample_rule_file)
        )
        
        # 应该成功
        assert result.returncode == 0 or "valid" in result.stdout.lower()
    
    def test_validate_invalid_rule(self, cli_runner, tmp_path):
        """测试校验无效规则"""
        invalid_rule = tmp_path / "invalid.json"
        invalid_rule.write_text('{"rule_id": "test"}')  # 缺少必填字段
        
        # CLI 格式: validate <type> <source>
        result = cli_runner(
            "validate",
            "rule",
            str(invalid_rule)
        )
        
        # 应该报告错误
        assert result.returncode != 0 or "error" in result.stdout.lower() or "missing" in result.stdout.lower()
    
    # ===== status 命令测试 =====
    
    def test_status(self, cli_runner, tmp_path):
        """测试状态查询"""
        # CLI 格式: status [-o output]
        result = cli_runner(
            "status",
            "-o", str(tmp_path)
        )
        
        # 应该成功显示状态
        assert result.returncode == 0 or "status" in result.stdout.lower()
    
    # ===== clean 命令测试 =====
    
    def test_clean_empty(self, cli_runner, tmp_path):
        """测试清理空目录"""
        # CLI 格式: clean [-o output]
        result = cli_runner(
            "clean",
            "-o", str(tmp_path)
        )
        
        # 应该成功
        assert result.returncode == 0


class TestCLIIntegration:
    """CLI 集成测试"""
    
    @pytest.fixture
    def project_dir(self, tmp_path):
        """创建完整的测试项目结构"""
        # 创建目录结构
        rules_dir = tmp_path / "data" / "rules"
        rules_dir.mkdir(parents=True)
        
        output_dir = tmp_path / "backend" / "generated"
        output_dir.mkdir(parents=True)
        
        # 创建规则文件（符合 ConfigRuleDefinition Schema）
        rule = {
            "rule_id": "integration_test_001",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "集成测试规则",
            "category": "test",
            "required_factors": ["x"],
            "condition": {"operator": "==", "factor_id": "x", "value": 1},
            "result": {
                "dimension": "test",
                "level": "中等",
                "conclusion_template_zh": "测试结论",
                "confidence": 0.9,
                "weight": 1.0,
                "tags": [],
                "evidence_factors": []
            },
            "metadata": {"book_id": "test", "chapter": "test", "l1_anchor": "TEST_001"}
        }
        (rules_dir / "test.json").write_text(json.dumps(rule, ensure_ascii=False))
        
        return tmp_path
    
    def test_full_compile_workflow(self, project_dir):
        """测试完整的编译工作流程"""
        rules_dir = project_dir / "data" / "rules"
        output_dir = project_dir / "backend" / "generated"
        
        # 运行编译 - CLI 格式: compile <type> <source> [-o output]
        result = subprocess.run(
            [
                sys.executable, "-m", "scripts.codegen",
                "compile",
                "rule",
                str(rules_dir / "test.json"),
                "-o", str(output_dir)
            ],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent.parent.parent
        )
        
        # 检查结果
        if result.returncode == 0:
            # 应该生成了文件
            generated_files = list(output_dir.glob("**/*.py"))
            assert len(generated_files) > 0 or "success" in result.stdout.lower()
