"""
Tests for RuleCodeGenerator
"""

import ast
import json
import pytest

from scripts.codegen.rule_generator import RuleCodeGenerator
from scripts.codegen.exceptions import ValidationError, CompilationError


class TestRuleCodeGenerator:
    """RuleCodeGenerator 测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return RuleCodeGenerator(output_dir=tmp_path)
    
    @pytest.fixture
    def valid_simple_rule(self):
        """有效的简单规则（符合 ConfigRuleDefinition Schema）"""
        return {
            "rule_id": "bazi_jia_spring_001",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "bazi",
            "human_label": "甲木生于春月",
            "category": "身强身弱",
            "required_factors": ["day_stem", "month_branch"],
            "condition": {
                "operator": "AND",
                "conditions": [
                    {"operator": "EQ", "factor_id": "day_stem", "value": "甲"},
                    {"operator": "in", "factor_id": "month_branch", "value": ["寅", "卯"]}
                ]
            },
            "result": {
                "dimension": "性格",
                "level": "吉",
                "conclusion_template_zh": "甲木生于春月，得时得令",
                "confidence": 0.9,
                "weight": 1.5,
                "tags": ["seasonal", "strength"],
                "evidence_factors": ["day_stem", "month_branch"]
            },
            "metadata": {
                "book_id": "ditianshui",
                "chapter": "论日主",
                "l1_anchor": "DTS_L1_001"
            }
        }
    
    @pytest.fixture
    def valid_complex_rule(self):
        """有效的复杂规则（符合 ConfigRuleDefinition Schema）"""
        return {
            "rule_id": "bazi_complex_001",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "bazi",
            "human_label": "复杂逻辑规则",
            "category": "复杂规则",
            "required_factors": ["day_stem", "month_branch"],
            "condition": {
                "operator": "==",
                "factor_id": "day_stem",
                "value": "甲"
            },
            "is_complex_logic": True,
            "python_handler_ref": "backend.rules.bazi.complex_handlers.evaluate_complex_001",
            "result": {
                "dimension": "事业",
                "level": "中等",
                "conclusion_template_zh": "复杂规则结论",
                "confidence": 0.8,
                "weight": 1.0,
                "tags": ["complex"],
                "evidence_factors": []
            },
            "metadata": {
                "book_id": "ditianshui",
                "chapter": "论复杂",
                "l1_anchor": "DTS_L1_002"
            }
        }
    
    # ===== 校验测试 =====
    
    def test_validate_valid_rule(self, generator, valid_simple_rule):
        """测试有效规则校验通过"""
        errors = generator.validate(valid_simple_rule)
        assert errors == []
    
    def test_validate_missing_version(self, generator, valid_simple_rule):
        """测试缺少 version 字段"""
        del valid_simple_rule["version"]
        errors = generator.validate(valid_simple_rule)
        assert any("version" in e.lower() for e in errors)
    
    def test_validate_invalid_version_format(self, generator, valid_simple_rule):
        """测试无效 version 格式"""
        valid_simple_rule["version"] = "v1.0"  # 错误格式
        errors = generator.validate(valid_simple_rule)
        assert any("version" in e.lower() for e in errors)
    
    def test_validate_missing_status(self, generator, valid_simple_rule):
        """测试缺少 status 字段"""
        del valid_simple_rule["status"]
        errors = generator.validate(valid_simple_rule)
        assert any("status" in e.lower() for e in errors)
    
    def test_validate_invalid_status(self, generator, valid_simple_rule):
        """测试无效 status 值"""
        valid_simple_rule["status"] = "unknown"
        errors = generator.validate(valid_simple_rule)
        assert any("status" in e.lower() for e in errors)
    
    def test_validate_missing_engine_id(self, generator, valid_simple_rule):
        """测试缺少 engine_id 字段"""
        del valid_simple_rule["engine_id"]
        errors = generator.validate(valid_simple_rule)
        assert any("engine_id" in e.lower() for e in errors)
    
    def test_validate_complex_rule_missing_handler(self, generator, valid_complex_rule):
        """测试复杂规则缺少 python_handler_ref"""
        del valid_complex_rule["python_handler_ref"]
        errors = generator.validate(valid_complex_rule)
        assert any("python_handler_ref" in e.lower() for e in errors)
    
    def test_validate_complex_rule_with_handler(self, generator, valid_complex_rule):
        """测试复杂规则有 python_handler_ref"""
        errors = generator.validate(valid_complex_rule)
        assert errors == []
    
    # ===== 编译测试 =====
    
    def test_compile_simple_rule(self, generator, valid_simple_rule):
        """测试简单规则编译"""
        code = generator.compile(valid_simple_rule)
        assert isinstance(code, str)
        # 函数名格式: {rule_id}_evaluate
        assert "def bazi_jia_spring_001_evaluate" in code
        assert "RuntimeRuleResult" in code
    
    def test_compile_generates_valid_python(self, generator, valid_simple_rule):
        """测试生成的代码是有效 Python"""
        code = generator.compile(valid_simple_rule)
        # 应该能通过 AST 解析
        ast.parse(code)
    
    def test_compile_complex_rule_stub(self, generator, valid_complex_rule):
        """测试复杂规则生成 stub"""
        code = generator.compile(valid_complex_rule)
        assert "python_handler_ref" in code or "stub" in code.lower() or "complex" in code.lower()
    
    def test_compile_includes_all_result_fields(self, generator, valid_simple_rule):
        """测试生成的代码包含所有 RuntimeRuleResult 字段"""
        code = generator.compile(valid_simple_rule)
        required_fields = [
            "rule_id",
            "matched",
            "dimension",
            "level",
            "confidence",
            "weight",
            "tags",
            "evidence_factors",
        ]
        for field in required_fields:
            assert field in code, f"Missing field: {field}"
    
    # ===== 条件编译测试 =====
    
    @pytest.mark.parametrize("operator,expected", [
        ("EQ", "=="),
        ("NE", "!="),
        ("GT", ">"),
        ("GE", ">="),
        ("LT", "<"),
        ("LE", "<="),
    ])
    def test_compile_comparison_operators(self, generator, operator, expected):
        """测试比较运算符编译（验证 OPERATOR_MAP 映射）"""
        rule = {
            "rule_id": f"test_{operator.lower()}",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": f"测试 {operator} 运算符",
            "category": "test",
            "required_factors": ["x"],
            "condition": {
                "operator": operator,
                "factor_id": "x",
                "value": 1
            },
            "result": {
                "dimension": "test",
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
        code = generator.compile(rule)
        assert expected in code
    
    def test_compile_in_operator(self, generator):
        """测试 IN 运算符编译"""
        rule = {
            "rule_id": "test_in",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试 IN 运算符",
            "category": "test",
            "required_factors": ["x"],
            "condition": {
                "operator": "in",
                "factor_id": "x",
                "value": [1, 2, 3]
            },
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
        code = generator.compile(rule)
        assert " in " in code
        assert "[1, 2, 3]" in code or "(1, 2, 3)" in code
    
    def test_compile_not_condition_via_logical(self, generator):
        """测试通过 NOT 逻辑表达式实现非包含关系"""
        # NOT_IN 不在 Schema 中，使用 NOT + in 组合实现
        rule = {
            "rule_id": "test_not_contains",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试非包含条件",
            "category": "test",
            "required_factors": ["x"],
            "condition": {
                "operator": "NOT",
                "conditions": [
                    {"operator": "in", "factor_id": "x", "value": ["a", "b"]}
                ]
            },
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
        code = generator.compile(rule)
        assert "not " in code or "not(" in code
    
    def test_compile_and_operator(self, generator):
        """测试 AND 运算符编译"""
        rule = {
            "rule_id": "test_and",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试 AND 运算符",
            "category": "test",
            "required_factors": ["a", "b"],
            "condition": {
                "operator": "AND",
                "conditions": [
                    {"operator": "EQ", "factor_id": "a", "value": 1},
                    {"operator": "EQ", "factor_id": "b", "value": 2}
                ]
            },
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
        code = generator.compile(rule)
        assert " and " in code
    
    def test_compile_or_operator(self, generator):
        """测试 OR 运算符编译"""
        rule = {
            "rule_id": "test_or",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试 OR 运算符",
            "category": "test",
            "required_factors": ["a", "b"],
            "condition": {
                "operator": "OR",
                "conditions": [
                    {"operator": "EQ", "factor_id": "a", "value": 1},
                    {"operator": "EQ", "factor_id": "b", "value": 2}
                ]
            },
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
        code = generator.compile(rule)
        assert " or " in code
    
    def test_compile_not_operator(self, generator):
        """测试 NOT 运算符编译"""
        rule = {
            "rule_id": "test_not",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试 NOT 运算符",
            "category": "test",
            "required_factors": ["x"],
            "condition": {
                "operator": "NOT",
                "conditions": [{"operator": "==", "factor_id": "x", "value": 1}]  # 使用 == 而不是 EQ
            },
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
        code = generator.compile(rule)
        assert "not " in code or "not(" in code


class TestRuleCodeGeneratorEdgeCases:
    """边界情况测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return RuleCodeGenerator(output_dir=tmp_path)
    
    def test_compile_nested_conditions(self, generator):
        """测试嵌套条件编译"""
        rule = {
            "rule_id": "test_nested",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试嵌套条件",
            "category": "test",
            "required_factors": ["a", "b", "c"],
            "condition": {
                "operator": "AND",
                "conditions": [
                    {
                        "operator": "OR",
                        "conditions": [
                            {"operator": "EQ", "factor_id": "a", "value": 1},
                            {"operator": "EQ", "factor_id": "b", "value": 2}
                        ]
                    },
                    {"operator": "GT", "factor_id": "c", "value": 0}
                ]
            },
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
        code = generator.compile(rule)
        # 应该能生成有效代码
        ast.parse(code)
        assert " and " in code
        assert " or " in code
    
    def test_compile_with_special_characters_in_values(self, generator):
        """测试值中包含特殊字符"""
        rule = {
            "rule_id": "test_special",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "test",
            "human_label": "测试特殊字符",
            "category": "test",
            "required_factors": ["desc"],
            "condition": {
                "operator": "==",
                "factor_id": "desc",
                "value": "测试'引号\"和换行\n"
            },
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
        code = generator.compile(rule)
        # 应该能生成有效代码（特殊字符被正确转义）
        ast.parse(code)
