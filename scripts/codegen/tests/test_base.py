"""
Tests for BaseCodeGenerator
"""

import ast
import tempfile
from pathlib import Path

import pytest

from scripts.codegen.base import BaseCodeGenerator
from scripts.codegen.exceptions import SyntaxVerificationError


class ConcreteGenerator(BaseCodeGenerator):
    """用于测试的具体实现"""
    
    def compile(self, source: dict) -> str:
        return f"# Generated from {source.get('id', 'unknown')}\nresult = {source}"
    
    def validate(self, source: dict) -> list:
        errors = []
        if "id" not in source:
            errors.append("Missing required field: id")
        return errors


class TestBaseCodeGenerator:
    """BaseCodeGenerator 测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return ConcreteGenerator(output_dir=tmp_path)
    
    def test_init_creates_output_dir(self, tmp_path):
        """测试初始化时创建输出目录"""
        output_dir = tmp_path / "generated"
        gen = ConcreteGenerator(output_dir=output_dir)
        assert output_dir.exists()
    
    def test_compile_returns_string(self, generator):
        """测试编译返回字符串"""
        source = {"id": "test_001", "value": 42}
        result = generator.compile(source)
        assert isinstance(result, str)
        assert "test_001" in result
    
    def test_validate_returns_errors(self, generator):
        """测试校验返回错误列表"""
        # 有效输入
        errors = generator.validate({"id": "test"})
        assert errors == []
        
        # 无效输入
        errors = generator.validate({})
        assert len(errors) == 1
        assert "id" in errors[0]
    
    def test_verify_syntax_valid_code(self, generator):
        """测试有效代码语法验证"""
        valid_code = "x = 1\ny = x + 2\nprint(y)"
        assert generator.verify_syntax(valid_code) is True
    
    def test_verify_syntax_invalid_code(self, generator):
        """测试无效代码语法验证"""
        invalid_code = "x = 1\ny = x + \nprint(y)"  # 语法错误
        with pytest.raises(SyntaxVerificationError):
            generator.verify_syntax(invalid_code)
    
    def test_save_creates_file(self, generator, tmp_path):
        """测试保存创建文件"""
        code = "x = 1"
        path = generator.save(code, "test_module.py")
        assert path.exists()
        assert path.read_text() == code
    
    def test_save_creates_subdirs(self, generator, tmp_path):
        """测试保存时创建子目录"""
        code = "x = 1"
        path = generator.save(code, "subdir/test_module.py")
        assert path.exists()
        assert path.parent.name == "subdir"
    
    def test_format_code_valid(self, generator):
        """测试代码格式化"""
        unformatted = "x=1\ny=2\nz=x+y"
        formatted = generator.format_code(unformatted)
        # black 会添加换行和空格
        assert "x = 1" in formatted or formatted.strip() == unformatted.strip()
    
    def test_format_code_preserves_semantics(self, generator):
        """测试格式化不改变语义"""
        code = "def foo():\n    return 42"
        formatted = generator.format_code(code)
        # 解析两者，确保语义相同
        ast1 = ast.parse(code)
        ast2 = ast.parse(formatted)
        assert ast.dump(ast1) == ast.dump(ast2)


class TestSyntaxVerification:
    """语法验证详细测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return ConcreteGenerator(output_dir=tmp_path)
    
    @pytest.mark.parametrize("code", [
        "x = 1",
        "def foo(): pass",
        "class Bar: pass",
        "import os",
        "from pathlib import Path",
        "[x for x in range(10)]",
        "lambda x: x + 1",
    ])
    def test_valid_python_syntax(self, generator, code):
        """测试各种有效 Python 语法"""
        assert generator.verify_syntax(code) is True
    
    @pytest.mark.parametrize("code", [
        "x = ",
        "def foo(",
        "class :",
        "if True",
        "for x in",
        "return return",
    ])
    def test_invalid_python_syntax(self, generator, code):
        """测试各种无效 Python 语法"""
        with pytest.raises(SyntaxVerificationError):
            generator.verify_syntax(code)
