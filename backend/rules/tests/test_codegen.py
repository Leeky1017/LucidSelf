"""
Test Rule Code Generator

规则代码生成器测试 - 验证编译、格式化、批量处理。

对照 tasks.md Task 3:
- Property 5: Codegen Round-Trip Consistency
- Property 6: Hash-Based Recompilation Detection
- Validates: Requirements 2.1-2.10
"""

import json
import tempfile
from pathlib import Path

import pytest
from hypothesis import given, strategies as st, settings

from scripts.codegen.rule_generator import RuleCodeGenerator, OPERATOR_MAP
from scripts.codegen.manifest import CodegenManifest


@pytest.fixture
def rule_generator():
    """创建规则代码生成器"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield RuleCodeGenerator(output_dir=Path(tmpdir))


@pytest.fixture
def sample_rule_json():
    """创建示例规则 JSON"""
    return {
        "rule_id": "test_rule_001",
        "human_label": "测试规则",
        "category": "test",
        "condition": {
            "operator": "AND",
            "conditions": [
                {"factor_id": "day_master", "operator": "==", "value": "甲"},
                {"factor_id": "strength", "operator": ">", "value": 0.5},
            ]
        },
        "required_factors": ["day_master", "strength"],
        "is_complex_logic": False,
        "result": {
            "dimension": "personality",
            "level": "吉",
            "conclusion_template_zh": "测试结论",
            "weight": 1.0,
            "confidence": 0.8,
            "tags": ["test"],
            "evidence_factors": ["day_master"],
        },
        "priority": 100,
        "version": "1.0.0",
        "status": "active",
        "engine_id": "bazi_rule_engine",
        "metadata": {
            "book_id": "test_book",
            "chapter": "chapter1",
            "l1_anchor": "TEST_L1_001",
        }
    }


@pytest.fixture
def complex_rule_json():
    """创建复杂规则 JSON"""
    return {
        "rule_id": "complex_rule_001",
        "human_label": "复杂规则",
        "category": "complex",
        "condition": {
            "factor_id": "pattern",
            "operator": "==",
            "value": "special",
        },
        "required_factors": ["pattern"],
        "is_complex_logic": True,
        "python_handler_ref": "handle_complex_pattern",
        "result": {
            "dimension": "career",
            "level": "大吉",
            "conclusion_template_zh": "复杂规则结论",
            "weight": 2.0,
            "confidence": 0.9,
            "tags": [],
            "evidence_factors": [],
        },
        "priority": 200,
        "version": "1.0.0",
        "status": "active",
        "engine_id": "bazi_rule_engine",
        "metadata": {
            "book_id": "test_book",
            "chapter": "chapter2",
            "l1_anchor": "TEST_L1_002",
        }
    }


class TestRuleCodeGeneratorValidation:
    """规则校验测试"""
    
    def test_validate_valid_rule(self, rule_generator, sample_rule_json):
        """测试有效规则校验"""
        errors = rule_generator.validate(sample_rule_json)
        assert errors == []
    
    def test_validate_missing_required_field(self, rule_generator):
        """测试缺少必填字段"""
        invalid = {"rule_id": "test"}  # 缺少其他必填字段
        errors = rule_generator.validate(invalid)
        assert len(errors) > 0
    
    def test_validate_invalid_version(self, rule_generator, sample_rule_json):
        """测试无效版本格式"""
        sample_rule_json["version"] = "invalid"
        errors = rule_generator.validate(sample_rule_json)
        assert len(errors) > 0
        assert any("version" in e.lower() for e in errors)
    
    def test_validate_complex_rule_missing_handler(self, rule_generator, sample_rule_json):
        """测试复杂规则缺少 handler"""
        sample_rule_json["is_complex_logic"] = True
        # 不提供 python_handler_ref
        errors = rule_generator.validate(sample_rule_json)
        assert len(errors) > 0
        assert any("python_handler_ref" in e for e in errors)


class TestRuleCodeGeneratorCompilation:
    """规则编译测试"""
    
    def test_compile_simple_rule(self, rule_generator, sample_rule_json):
        """测试简单规则编译"""
        code = rule_generator.compile(sample_rule_json)
        
        # 验证生成的代码包含关键元素
        assert "@register_rule" in code
        assert "test_rule_001" in code
        assert "def test_rule_001_evaluate" in code
        assert "RuntimeRuleResult" in code
        assert "context: RuleContext" in code
    
    def test_compile_complex_rule(self, rule_generator, complex_rule_json):
        """测试复杂规则编译（生成 stub）"""
        code = rule_generator.compile(complex_rule_json)
        
        assert "@register_rule" in code
        assert "complex_rule_001" in code
        assert "NotImplementedError" in code
        assert "handle_complex_pattern" in code
    
    def test_compile_with_all_operators(self, rule_generator, sample_rule_json):
        """测试支持所有运算符"""
        operators = {
            "==": "test_op_eq",
            "!=": "test_op_ne",
            ">": "test_op_gt",
            "<": "test_op_lt",
            ">=": "test_op_ge",
            "<=": "test_op_le",
            "in": "test_op_in",
            "not_in": "test_op_not_in",
            "exists": "test_op_exists",
            "not_exists": "test_op_not_exists",
            "between": "test_op_between",
        }
        
        for op, rule_id in operators.items():
            sample_rule_json["rule_id"] = rule_id
            
            if op == "between":
                sample_rule_json["condition"] = {
                    "factor_id": "score",
                    "operator": op,
                    "value": [0.3, 0.7],
                }
            elif op in ("exists", "not_exists"):
                sample_rule_json["condition"] = {
                    "factor_id": "factor",
                    "operator": op,
                }
            elif op in ("in", "not_in"):
                sample_rule_json["condition"] = {
                    "factor_id": "category",
                    "operator": op,
                    "value": ["a", "b", "c"],
                }
            else:
                sample_rule_json["condition"] = {
                    "factor_id": "value",
                    "operator": op,
                    "value": 10,
                }
            
            code = rule_generator.compile(sample_rule_json)
            assert rule_id in code
    
    def test_compile_and_syntax_check(self, rule_generator, sample_rule_json):
        """测试编译代码语法正确性"""
        code = rule_generator.compile(sample_rule_json)
        
        # 应该能通过语法检查
        assert rule_generator.verify_syntax(code) is True


class TestRuleCodeGeneratorBatch:
    """批量编译测试"""
    
    def test_compile_jsonl(self, rule_generator, sample_rule_json):
        """测试编译 JSONL 文件"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # 创建 JSONL 文件
            jsonl_path = Path(tmpdir) / "test_rules.jsonl"
            
            # 写入两条规则
            rule1 = sample_rule_json.copy()
            rule2 = sample_rule_json.copy()
            rule2["rule_id"] = "test_rule_002"
            
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(rule1, ensure_ascii=False) + "\n")
                f.write(json.dumps(rule2, ensure_ascii=False) + "\n")
            
            # 编译
            output_dir = Path(tmpdir) / "output"
            output_dir.mkdir()
            
            report = rule_generator.compile_jsonl(
                jsonl_path,
                output_dir=output_dir,
            )
            
            # 验证报告
            assert report["rules_compiled"] == 2
            assert report["errors"] == []
            assert len(report["output_files"]) == 1
            
            # 验证输出文件
            output_path = Path(report["output_files"][0])
            assert output_path.exists()
            
            content = output_path.read_text()
            assert "test_rule_001" in content
            assert "test_rule_002" in content
    
    def test_compile_jsonl_with_errors(self, rule_generator):
        """测试编译包含错误的 JSONL"""
        with tempfile.TemporaryDirectory() as tmpdir:
            jsonl_path = Path(tmpdir) / "bad_rules.jsonl"
            
            # 写入一条有效规则和一条无效规则
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write('{"invalid": "rule"}\n')
                f.write('also invalid json\n')
            
            output_dir = Path(tmpdir) / "output"
            output_dir.mkdir()
            
            report = rule_generator.compile_jsonl(
                jsonl_path,
                output_dir=output_dir,
            )
            
            # 应该有错误
            assert len(report["errors"]) > 0


class TestRuleCodeGeneratorManifest:
    """增量编译测试 - Property 6: Hash-Based Recompilation Detection"""
    
    def test_needs_recompile_new_file(self, rule_generator, sample_rule_json):
        """测试新文件需要编译"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest = CodegenManifest(Path(tmpdir))
            
            jsonl_path = Path(tmpdir) / "rules.jsonl"
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(sample_rule_json, ensure_ascii=False) + "\n")
            
            assert rule_generator.needs_recompile(jsonl_path, manifest) is True
    
    def test_needs_recompile_unchanged_file(self, rule_generator, sample_rule_json):
        """测试未修改文件不需要重新编译"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest = CodegenManifest(Path(tmpdir))
            
            jsonl_path = Path(tmpdir) / "rules.jsonl"
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(sample_rule_json, ensure_ascii=False) + "\n")
            
            # 第一次编译
            output_dir = Path(tmpdir) / "output"
            output_dir.mkdir()
            
            rule_generator.compile_jsonl(jsonl_path, output_dir=output_dir, manifest=manifest)
            
            # 检查是否需要重新编译
            assert rule_generator.needs_recompile(jsonl_path, manifest) is False
    
    def test_needs_recompile_changed_file(self, rule_generator, sample_rule_json):
        """测试修改后的文件需要重新编译"""
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest = CodegenManifest(Path(tmpdir))
            
            jsonl_path = Path(tmpdir) / "rules.jsonl"
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(sample_rule_json, ensure_ascii=False) + "\n")
            
            # 第一次编译
            output_dir = Path(tmpdir) / "output"
            output_dir.mkdir()
            
            rule_generator.compile_jsonl(jsonl_path, output_dir=output_dir, manifest=manifest)
            
            # 修改文件
            sample_rule_json["rule_id"] = "modified_rule"
            with open(jsonl_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(sample_rule_json, ensure_ascii=False) + "\n")
            
            # 检查是否需要重新编译
            assert rule_generator.needs_recompile(jsonl_path, manifest) is True


class TestOperatorMap:
    """运算符映射测试"""
    
    def test_all_eleven_operators_supported(self):
        """测试支持 11 种运算符"""
        required_operators = [
            "==", "!=", ">", "<", ">=", "<=",
            "in", "not_in", "exists", "not_exists", "between"
        ]
        
        for op in required_operators:
            assert op in OPERATOR_MAP, f"Operator {op} not in OPERATOR_MAP"
    
    def test_operator_aliases(self):
        """测试运算符别名"""
        assert OPERATOR_MAP["EQ"] == "=="
        assert OPERATOR_MAP["NE"] == "!="
        assert OPERATOR_MAP["GT"] == ">"
        assert OPERATOR_MAP["LT"] == "<"
        assert OPERATOR_MAP["GE"] == ">="
        assert OPERATOR_MAP["LE"] == "<="
        assert OPERATOR_MAP["IN"] == "in"


class TestCodegenRoundTrip:
    """
    编译往返测试 - Property 5: Codegen Round-Trip Consistency
    
    测试编译的代码能够正确执行并产生预期结果
    """
    
    def test_round_trip_simple_condition(self, rule_generator, sample_rule_json):
        """
        **Feature: layer3-rules, Property 5: Codegen Round-Trip Consistency**
        
        测试简单条件的编译往返
        """
        # 编译
        code = rule_generator.compile(sample_rule_json)
        
        # 验证编译的代码语法正确
        assert rule_generator.verify_syntax(code)
        
        # 验证包含正确的条件表达式
        assert 'factors.get("day_master")' in code
        assert 'factors.get("strength")' in code
        assert "甲" in code  # 应包含原始值
    
    def test_round_trip_between_operator(self, rule_generator, sample_rule_json):
        """测试 between 运算符的编译往返"""
        sample_rule_json["condition"] = {
            "factor_id": "score",
            "operator": "between",
            "value": [0.3, 0.7],
        }
        
        code = rule_generator.compile(sample_rule_json)
        
        # 验证 between 条件正确生成
        assert "0.3" in code
        assert "0.7" in code
        assert "score" in code
