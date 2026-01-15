"""
Tests for SemanticCodeGenerator

测试新版 SemanticCodeGenerator，支持：
- L1/L2/L2.5 Markdown 解析
- NarrativeSnippetExtended 生成
- @SemanticRegistry.register 装饰器输出
"""

import ast
import json
from pathlib import Path

import pytest

from scripts.codegen.semantic_generator import SemanticCodeGenerator
from scripts.codegen.exceptions import ValidationError


class TestSemanticCodeGenerator:
    """SemanticCodeGenerator 测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return SemanticCodeGenerator(output_dir=tmp_path)
    
    @pytest.fixture
    def valid_parsed_semantic(self):
        """有效的解析后语义结构（新格式）"""
        return {
            "l1": {"original_text": "甲木为阳木，主生发、向上，性格正直。"},
            "l2": {"normalized_text_zh": "甲木如大树栋梁，生发向上。", "factors": ["day_master_jia"]},
            "l25": {"relations": [], "evidence": []},
            "narrative_snippets": [],
            "factor_refs": ["day_master_jia"],
            "subject": "甲木特性",
            "book_id": "ditianshui",
            "engine_id": "bazi",
            "version": "1.0.0",
        }
    
    @pytest.fixture
    def valid_semantics_list(self, valid_parsed_semantic):
        """有效的语义核心列表"""
        return [
            valid_parsed_semantic,
            {
                "l1": {"original_text": "乙木为阴木，柔顺依附。"},
                "l2": {"normalized_text_zh": "乙木柔弱需要依附。", "factors": ["day_master_yi"]},
                "l25": {"relations": [], "evidence": []},
                "narrative_snippets": [],
                "factor_refs": ["day_master_yi"],
                "subject": "乙木特性",
                "book_id": "ditianshui",
                "engine_id": "bazi",
                "version": "1.0.0",
            }
        ]
    
    # ===== 校验测试 =====
    
    def test_validate_valid_semantic(self, generator, valid_parsed_semantic):
        """测试有效语义核心校验通过"""
        errors = generator.validate(valid_parsed_semantic)
        assert errors == []
    
    def test_validate_missing_l1(self, generator, valid_parsed_semantic):
        """测试缺少 l1"""
        del valid_parsed_semantic["l1"]
        errors = generator.validate(valid_parsed_semantic)
        assert len(errors) > 0
        assert any("l1" in e.lower() for e in errors)
    
    def test_validate_missing_l2(self, generator, valid_parsed_semantic):
        """测试缺少 l2"""
        del valid_parsed_semantic["l2"]
        errors = generator.validate(valid_parsed_semantic)
        assert any("l2" in e.lower() for e in errors)
    
    # ===== 编译测试 =====
    
    def test_compile_single_semantic(self, generator, valid_parsed_semantic):
        """测试单个语义核心编译"""
        code = generator.compile(valid_parsed_semantic)
        assert isinstance(code, str)
        assert "SemanticEntry" in code
        assert "@SemanticRegistry.register" in code
    
    def test_compile_generates_valid_python(self, generator, valid_parsed_semantic):
        """测试生成的代码是有效 Python"""
        code = generator.compile(valid_parsed_semantic)
        ast.parse(code)
    
    def test_compile_includes_content(self, generator, valid_parsed_semantic):
        """测试生成的代码包含内容"""
        code = generator.compile(valid_parsed_semantic)
        # 应该包含中文内容
        assert "甲木" in code
    
    def test_compile_includes_factor_refs(self, generator, valid_parsed_semantic):
        """测试生成的代码包含因子引用"""
        code = generator.compile(valid_parsed_semantic)
        assert "day_master_jia" in code or "factor_refs" in code
    
    def test_compile_includes_metadata(self, generator, valid_parsed_semantic):
        """测试生成的代码包含元数据"""
        code = generator.compile(valid_parsed_semantic)
        assert "SourceMetadata" in code
        assert "ditianshui" in code
    
    # ===== 批量编译测试 =====
    
    def test_compile_multiple_semantics(self, generator, valid_semantics_list):
        """测试编译多个语义配置"""
        codes = []
        for sem in valid_semantics_list:
            code = generator.compile(sem)
            codes.append(code)
            ast.parse(code)
        
        # 每个都应该生成有效代码
        assert len(codes) == len(valid_semantics_list)
        for code in codes:
            assert isinstance(code, str)
            assert len(code) > 0
            assert "SemanticEntry" in code


class TestSemanticCodeGeneratorEdgeCases:
    """边界情况测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return SemanticCodeGenerator(output_dir=tmp_path)
    
    def test_compile_simple_entries(self, generator):
        """测试简单条目的语义核心"""
        semantic = {
            "l1": {"original_text": "简单测试内容"},
            "l2": {"normalized_text_zh": "简单释义", "factors": []},
            "l25": {"relations": [], "evidence": []},
            "narrative_snippets": [],
            "factor_refs": [],
            "subject": "简单测试",
            "book_id": "test_book",
            "engine_id": "bazi",
            "version": "1.0.0",
        }
        code = generator.compile(semantic)
        ast.parse(code)
    
    def test_compile_with_unicode(self, generator):
        """测试包含各种 Unicode 字符"""
        semantic = {
            "l1": {"original_text": "测试™©®特殊字符①②③"},
            "l2": {"normalized_text_zh": "特殊字符测试释义", "factors": []},
            "l25": {"relations": [], "evidence": []},
            "narrative_snippets": [],
            "factor_refs": [],
            "subject": "Unicode测试",
            "book_id": "test_book",
            "engine_id": "bazi",
            "version": "1.0.0",
        }
        code = generator.compile(semantic)
        ast.parse(code)
    
    def test_compile_empty_l1(self, generator):
        """测试编译空 L1 内容"""
        semantic = {
            "l1": {"original_text": ""},
            "l2": {"normalized_text_zh": "", "factors": []},
            "l25": {"relations": [], "evidence": []},
            "narrative_snippets": [],
            "factor_refs": [],
            "subject": "空内容测试",
            "book_id": "test_book",
            "engine_id": "bazi",
            "version": "1.0.0",
        }
        code = generator.compile(semantic)
        # 空内容应该生成有效模块
        ast.parse(code)


class TestSemanticCodeGeneratorMarkdownParsing:
    """Markdown 解析测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return SemanticCodeGenerator(output_dir=tmp_path)
    
    def test_parse_l1_block(self, generator):
        """测试 L1 区块解析"""
        content = """# 甲木
## L1 原文
甲木参天，脱胎要火。

## L2 语义
**释义**: 甲木如大树。
"""
        result = generator._parse_markdown(content, "test.md")
        assert "甲木参天" in result["l1"]["original_text"]
    
    def test_parse_l2_block(self, generator):
        """测试 L2 区块解析"""
        # L2 区块内含因子表
        content = """## L2 语义
**释义**: 甲木如大树栋梁。

**因子表**:
| day_master_jia | 日主甲木 |
| element_wood | 木元素 |
"""
        result = generator._parse_markdown(content, "test.md")
        # 验证释义提取
        assert "normalized_text_zh" in result["l2"]
        assert "甲木如大树栋梁" in result["l2"]["normalized_text_zh"]
        # 验证因子提取
        assert "day_master_jia" in result["factor_refs"]
    
    def test_infer_engine_id(self, generator):
        """测试引擎 ID 推断"""
        assert generator._infer_engine_id("ditianshui") == "bazi"
        assert generator._infer_engine_id("zhouyi") == "yijing"
        assert generator._infer_engine_id("the_inner_sky") == "astro"
        assert generator._infer_engine_id("unknown_book") == "bazi"  # 默认
