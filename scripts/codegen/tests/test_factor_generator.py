"""
Tests for FactorCodeGenerator
"""

import ast
import json
import tempfile
from pathlib import Path

import pytest

from scripts.codegen.factor_generator import FactorCodeGenerator
from scripts.codegen.exceptions import ValidationError


class TestFactorCodeGenerator:
    """FactorCodeGenerator 测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return FactorCodeGenerator(output_dir=tmp_path)
    
    @pytest.fixture
    def valid_factor(self):
        """有效的因子定义（符合 ConfigFactor Schema）"""
        return {
            "factor_id": "day_stem",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "bazi",
            "label_zh": "日干",
            "label_en": "Day Stem",
            "category": "structure",
            "value_type": "enum",
            "enum_values": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
            "description_zh": "八字中的日干",
            "knowledge_ref": ["sanmingtonghui:卷一:论日主"],
            "metadata": {
                "book_id": "sanmingtonghui",
                "chapter": "卷一",
                "l1_anchor": "SMTH_L1_001"
            }
        }
    
    @pytest.fixture
    def valid_factors_list(self, valid_factor):
        """有效的因子列表"""
        return [
            valid_factor,
            {
                "factor_id": "month_branch",
                "version": "1.0.0",
                "status": "active",
                "engine_id": "bazi",
                "label_zh": "月支",
                "label_en": "Month Branch",
                "category": "structure",
                "value_type": "enum",
                "enum_values": ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"],
                "description_zh": "八字中的月支",
                "knowledge_ref": ["sanmingtonghui:卷一:论月令"],
                "metadata": {
                    "book_id": "sanmingtonghui",
                    "chapter": "卷一",
                    "l1_anchor": "SMTH_L1_002"
                }
            }
        ]
    
    # ===== 校验测试 =====
    
    def test_validate_valid_factor(self, generator, valid_factor):
        """测试有效因子校验通过"""
        errors = generator.validate(valid_factor)
        assert errors == []
    
    def test_validate_missing_version(self, generator, valid_factor):
        """测试缺少 version 字段"""
        del valid_factor["version"]
        errors = generator.validate(valid_factor)
        assert any("version" in e.lower() for e in errors)
    
    def test_validate_invalid_version_format(self, generator, valid_factor):
        """测试无效 version 格式"""
        valid_factor["version"] = "1.0"
        errors = generator.validate(valid_factor)
        assert any("version" in e.lower() for e in errors)
    
    def test_validate_missing_status(self, generator, valid_factor):
        """测试缺少 status 字段"""
        del valid_factor["status"]
        errors = generator.validate(valid_factor)
        assert any("status" in e.lower() for e in errors)
    
    def test_validate_invalid_status(self, generator, valid_factor):
        """测试无效 status 值"""
        valid_factor["status"] = "invalid"
        errors = generator.validate(valid_factor)
        assert any("status" in e.lower() for e in errors)
    
    def test_validate_missing_engine_id(self, generator, valid_factor):
        """测试缺少 engine_id 字段"""
        del valid_factor["engine_id"]
        errors = generator.validate(valid_factor)
        assert any("engine_id" in e.lower() for e in errors)
    
    def test_validate_experimental_status(self, generator, valid_factor):
        """测试 experimental 状态"""
        valid_factor["status"] = "experimental"
        errors = generator.validate(valid_factor)
        assert errors == []
    
    def test_validate_deprecated_status(self, generator, valid_factor):
        """测试 deprecated 状态"""
        valid_factor["status"] = "deprecated"
        errors = generator.validate(valid_factor)
        assert errors == []
    
    # ===== 编译测试 =====
    
    def test_compile_single_factor(self, generator, valid_factor):
        """测试单因子编译（返回元数据字典条目）"""
        code = generator.compile(valid_factor)
        assert isinstance(code, str)
        assert "day_stem" in code
        assert "factor_id" in code  # 应包含因子 ID 字段
    
    def test_compile_batch_generates_valid_python(self, generator, valid_factors_list):
        """测试批量编译生成有效 Python（完整模块）"""
        code = generator.compile_batch(
            factors=valid_factors_list,
            engine_id="bazi",
            version="1.0.0"
        )
        ast.parse(code)
    
    def test_compile_batch_generates_enum(self, generator, valid_factors_list):
        """测试批量编译生成 Enum 类"""
        code = generator.compile_batch(
            factors=valid_factors_list,
            engine_id="bazi",
            version="1.0.0"
        )
        # 应该包含 Enum 或类似的类型定义
        assert "class" in code or "Enum" in code
    
    def test_compile_includes_metadata(self, generator, valid_factor):
        """测试生成的代码包含元数据"""
        code = generator.compile(valid_factor)
        assert "日干" in code or "day_stem" in code
        assert "bazi" in code
    
    # ===== 批量编译测试 =====
    
    def test_compile_batch(self, generator, valid_factors_list):
        """测试批量编译（使用 factors 列表）"""
        code = generator.compile_batch(
            factors=valid_factors_list,
            engine_id="bazi",
            version="1.0.0"
        )
        assert isinstance(code, str)
        assert "day_stem" in code
        assert "month_branch" in code
    
    def test_compile_batch_generates_valid_python(self, generator, valid_factors_list):
        """测试批量编译生成有效 Python"""
        code = generator.compile_batch(
            factors=valid_factors_list,
            engine_id="bazi",
            version="1.0.0"
        )
        ast.parse(code)
    
    def test_compile_jsonl_file(self, generator, valid_factors_list, tmp_path):
        """测试从 JSONL 文件编译"""
        # 创建临时 JSONL 文件
        jsonl_path = tmp_path / "factors.jsonl"
        with open(jsonl_path, "w", encoding="utf-8") as f:
            for factor in valid_factors_list:
                f.write(json.dumps(factor, ensure_ascii=False) + "\n")
        
        code = generator.compile_jsonl_file(
            jsonl_path=jsonl_path,
            engine_id="bazi",
            version="1.0.0"
        )
        assert isinstance(code, str)
        assert "day_stem" in code
        assert "month_branch" in code
        ast.parse(code)


class TestFactorCodeGeneratorEdgeCases:
    """边界情况测试"""
    
    @pytest.fixture
    def generator(self, tmp_path):
        return FactorCodeGenerator(output_dir=tmp_path)
    
    def test_compile_numeric_factor(self, generator):
        """测试数值类型因子"""
        factor = {
            "factor_id": "birth_year",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "bazi",
            "label_zh": "出生年份",
            "label_en": "Birth Year",
            "category": "time",  # 有效的 FactorCategory
            "value_type": "float",
            "description_zh": "用户出生年份",
            "knowledge_ref": [],
            "metadata": {
                "book_id": "sanmingtonghui",
                "chapter": "卷一",
                "l1_anchor": "SMTH_L1_001"
            }
        }
        code = generator.compile(factor)
        # compile 返回单个条目片段，检查内容
        assert "birth_year" in code
    
    def test_compile_boolean_factor(self, generator):
        """测试布尔类型因子"""
        factor = {
            "factor_id": "is_yang_day",
            "version": "1.0.0",
            "status": "active",
            "engine_id": "bazi",
            "label_zh": "阳日干",
            "label_en": "Yang Day Stem",
            "category": "state",  # 有效的 FactorCategory
            "value_type": "boolean",
            "description_zh": "日干是否为阳干",
            "knowledge_ref": [],
            "metadata": {
                "book_id": "sanmingtonghui",
                "chapter": "卷一",
                "l1_anchor": "SMTH_L1_002"
            }
        }
        code = generator.compile(factor)
        # compile 返回单个条目片段，检查内容
        assert "is_yang_day" in code
    
    def test_compile_empty_batch(self, generator):
        """测试空批量编译"""
        code = generator.compile_batch(
            factors=[],
            engine_id="test",
            version="1.0.0"
        )
        # 应该生成有效的空模块或最小模块
        ast.parse(code)
