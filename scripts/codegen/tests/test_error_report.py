"""
Tests for error_report module
"""

import json
from pathlib import Path

import pytest

from scripts.codegen.error_report import (
    CodegenErrorReport,
    generate_agent_prompt,
    save_error_report,
    load_error_report,
)
from scripts.codegen.exceptions import (
    ValidationError,
    CompilationError,
    SyntaxVerificationError,
    ManifestError,
    FormattingError,
)


class TestCodegenErrorReport:
    """CodegenErrorReport 测试"""
    
    def test_create_report(self):
        """测试创建报告"""
        report = CodegenErrorReport(
            error_type="ValidationError",
            message="Test error",
            source_file="test.json",
            details={"field": "value"},
            suggestions=["Fix this", "Try that"]
        )
        assert report.error_type == "ValidationError"
        assert report.message == "Test error"
        assert len(report.suggestions) == 2
    
    def test_to_dict(self):
        """测试转换为字典"""
        report = CodegenErrorReport(
            error_type="TestError",
            message="Test",
            suggestions=["suggestion"]
        )
        data = report.to_dict()
        assert isinstance(data, dict)
        assert data["error_type"] == "TestError"
        assert "timestamp" in data
    
    def test_to_json(self):
        """测试转换为 JSON"""
        report = CodegenErrorReport(
            error_type="TestError",
            message="Test"
        )
        json_str = report.to_json()
        parsed = json.loads(json_str)
        assert parsed["error_type"] == "TestError"
    
    def test_from_validation_error(self):
        """测试从 ValidationError 创建"""
        error = ValidationError(
            "Validation failed",
            errors=["field1 missing", "field2 invalid"],
            source_file="test.json"
        )
        report = CodegenErrorReport.from_error(error)
        
        assert report.error_type == "ValidationError"
        assert report.source_file == "test.json"
        assert len(report.suggestions) > 0
    
    def test_from_compilation_error(self):
        """测试从 CompilationError 创建"""
        error = CompilationError(
            "Compilation failed",
            rule_id="test_rule",
            source_file="rules.json"
        )
        report = CodegenErrorReport.from_error(error)
        
        assert report.error_type == "CompilationError"
        assert len(report.suggestions) > 0
    
    def test_from_syntax_verification_error(self):
        """测试从 SyntaxVerificationError 创建"""
        error = SyntaxVerificationError(
            "Syntax error",
            generated_code="x = ",
            line_number=1
        )
        report = CodegenErrorReport.from_error(error)
        
        assert report.error_type == "SyntaxVerificationError"
        # 确保有修复建议
        assert len(report.suggestions) > 0


class TestGenerateAgentPrompt:
    """generate_agent_prompt 测试"""
    
    def test_generate_from_error(self):
        """测试从错误生成提示"""
        error = ValidationError(
            "Missing required fields",
            errors=["version is required"],
            source_file="test.json"
        )
        prompt = generate_agent_prompt(error)
        
        assert isinstance(prompt, str)
        assert "ValidationError" in prompt
        assert "Missing required fields" in prompt
        assert "test.json" in prompt
    
    def test_generate_from_report(self):
        """测试从报告生成提示"""
        report = CodegenErrorReport(
            error_type="TestError",
            message="Test message",
            suggestions=["Fix A", "Try B"]
        )
        prompt = generate_agent_prompt(report)
        
        assert "TestError" in prompt
        assert "Test message" in prompt
        assert "Fix A" in prompt
        assert "Try B" in prompt
    
    def test_prompt_includes_action_section(self):
        """测试提示包含 Action 部分"""
        error = ValidationError("Error", errors=["test"])
        prompt = generate_agent_prompt(error)
        
        assert "Action" in prompt


class TestSaveAndLoadErrorReport:
    """save_error_report 和 load_error_report 测试"""
    
    def test_save_to_file(self, tmp_path):
        """测试保存到文件"""
        report = CodegenErrorReport(
            error_type="TestError",
            message="Test"
        )
        path = tmp_path / "error.json"
        result = save_error_report(report, path)
        
        assert result.exists()
        content = json.loads(path.read_text())
        assert content["error_type"] == "TestError"
    
    def test_save_to_directory(self, tmp_path):
        """测试保存到目录（自动生成文件名）"""
        report = CodegenErrorReport(
            error_type="TestError",
            message="Test"
        )
        result = save_error_report(report, tmp_path)
        
        assert result.exists()
        assert result.parent == tmp_path
        assert result.suffix == ".json"
    
    def test_save_from_error(self, tmp_path):
        """测试从错误直接保存"""
        error = ValidationError("Error", errors=["test"])
        path = tmp_path / "error.json"
        
        save_error_report(error, path)
        
        content = json.loads(path.read_text())
        assert content["error_type"] == "ValidationError"
    
    def test_load_single_report(self, tmp_path):
        """测试加载单个报告"""
        report = CodegenErrorReport(
            error_type="TestError",
            message="Test"
        )
        path = tmp_path / "error.json"
        save_error_report(report, path)
        
        loaded = load_error_report(path)
        
        assert isinstance(loaded, CodegenErrorReport)
        assert loaded.error_type == "TestError"
    
    def test_save_append_mode(self, tmp_path):
        """测试追加模式"""
        path = tmp_path / "errors.json"
        
        # 保存第一个
        report1 = CodegenErrorReport(error_type="Error1", message="First")
        save_error_report(report1, path)
        
        # 追加第二个
        report2 = CodegenErrorReport(error_type="Error2", message="Second")
        save_error_report(report2, path, append=True)
        
        # 加载应该是列表
        loaded = load_error_report(path)
        assert isinstance(loaded, list)
        assert len(loaded) == 2
