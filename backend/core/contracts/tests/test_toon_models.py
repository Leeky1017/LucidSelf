"""
Tests for TOON Protocol Models

对照文档: docs/数据契约_Schema定义规范_v1.md §11
"""

import pytest
from pydantic import ValidationError

from backend.core.contracts import (
    ABBREVIATIONS,
    ABBREVIATIONS_REVERSE,
    TOON_CONSTRAINTS,
    TOON_SYNTAX,
    ToonPayload,
)


# =============================================================================
# TOON_SYNTAX 常量测试
# =============================================================================


class TestToonSyntax:
    """TOON_SYNTAX 常量测试"""

    def test_rule_syntax(self):
        """测试 rule 语法定义"""
        assert "rule" in TOON_SYNTAX
        rule_syn = TOON_SYNTAX["rule"]
        assert "format" in rule_syn
        assert "example" in rule_syn
        assert "fields" in rule_syn
        assert "rid" in rule_syn["fields"]
        assert "dim" in rule_syn["fields"]
        assert "lvl" in rule_syn["fields"]
        assert "conf" in rule_syn["fields"]

    def test_fusion_syntax(self):
        """测试 fusion 语法定义"""
        assert "fusion" in TOON_SYNTAX
        fusion_syn = TOON_SYNTAX["fusion"]
        assert "format" in fusion_syn
        assert "example" in fusion_syn
        assert "lines" in fusion_syn
        assert "T" in fusion_syn["lines"]
        assert "XV" in fusion_syn["lines"]

    def test_factor_matrix_syntax(self):
        """测试 factor_matrix 语法定义"""
        assert "factor_matrix" in TOON_SYNTAX
        fm_syn = TOON_SYNTAX["factor_matrix"]
        assert "format" in fm_syn
        assert "example" in fm_syn
        assert fm_syn["max_factors"] == 20


# =============================================================================
# ABBREVIATIONS 常量测试
# =============================================================================


class TestAbbreviations:
    """ABBREVIATIONS 常量测试"""

    def test_dimension_abbreviations(self):
        """测试维度缩写"""
        assert ABBREVIATIONS["事业"] == "C"
        assert ABBREVIATIONS["健康"] == "H"
        assert ABBREVIATIONS["婚姻"] == "M"
        assert ABBREVIATIONS["财富"] == "W"
        assert ABBREVIATIONS["人际"] == "R"
        assert ABBREVIATIONS["学业"] == "E"
        assert ABBREVIATIONS["性格"] == "P"

    def test_level_abbreviations(self):
        """测试等级缩写"""
        assert ABBREVIATIONS["大吉"] == "++"
        assert ABBREVIATIONS["吉"] == "+"
        assert ABBREVIATIONS["中等"] == "0"
        assert ABBREVIATIONS["凶"] == "-"
        assert ABBREVIATIONS["大凶"] == "--"

    def test_bazi_factor_abbreviations(self):
        """测试八字因子缩写"""
        assert ABBREVIATIONS["day_master"] == "dm"
        assert ABBREVIATIONS["season"] == "ssn"
        assert ABBREVIATIONS["strength"] == "str"
        assert ABBREVIATIONS["ten_god_zhengguan"] == "zg"

    def test_tarot_factor_abbreviations(self):
        """测试塔罗因子缩写"""
        assert ABBREVIATIONS["major_arcana"] == "ma"
        assert ABBREVIATIONS["minor_arcana"] == "mi"
        assert ABBREVIATIONS["suit_wands"] == "sw"
        assert ABBREVIATIONS["orientation_upright"] == "up"
        assert ABBREVIATIONS["orientation_reversed"] == "rv"

    def test_astro_factor_abbreviations(self):
        """测试占星因子缩写"""
        assert ABBREVIATIONS["sun_sign"] == "sun"
        assert ABBREVIATIONS["moon_sign"] == "moon"
        assert ABBREVIATIONS["ascendant"] == "asc"
        assert ABBREVIATIONS["house"] == "h"

    def test_reverse_mapping(self):
        """测试反向映射"""
        assert ABBREVIATIONS_REVERSE["C"] == "事业"
        assert ABBREVIATIONS_REVERSE["dm"] == "day_master"
        assert ABBREVIATIONS_REVERSE["++"] == "大吉"

    def test_bidirectional_mapping(self):
        """测试双向映射一致性"""
        for key, val in ABBREVIATIONS.items():
            assert ABBREVIATIONS_REVERSE[val] == key


# =============================================================================
# TOON_CONSTRAINTS 常量测试
# =============================================================================


class TestToonConstraints:
    """TOON_CONSTRAINTS 常量测试"""

    def test_constraints_exist(self):
        """测试约束规则存在"""
        assert len(TOON_CONSTRAINTS) > 0

    def test_pii_constraint(self):
        """测试 PII 约束"""
        pii_constraint = any("PII" in c for c in TOON_CONSTRAINTS)
        assert pii_constraint

    def test_character_limit_constraint(self):
        """测试字符限制约束"""
        char_constraint = any("1000" in c for c in TOON_CONSTRAINTS)
        assert char_constraint

    def test_llm_boundary_constraint(self):
        """测试 LLM 边界约束"""
        boundary_constraint = any("LLM 边界" in c for c in TOON_CONSTRAINTS)
        assert boundary_constraint


# =============================================================================
# ToonPayload 测试
# =============================================================================


class TestToonPayload:
    """ToonPayload 模型测试"""

    def test_valid_rule_payload(self):
        """测试有效的 rule 类型载体"""
        payload = ToonPayload(
            kind="rule",
            body="dts_jia_spring_001:C/+/0.8/dm,sn,st",
        )
        assert payload.version == "1"  # 默认值
        assert payload.kind == "rule"
        assert len(payload.body) < 1000

    def test_valid_fusion_payload(self):
        """测试有效的 fusion 类型载体"""
        body = (
            "T:事业突破|财富积累|团队建设\n"
            "dts_jia_001:C/+/0.85/dm,sn\n"
            "bazi_cai_002:W/++/0.9/cai,shn\n"
            "XV:0.87\nCF:0"
        )
        payload = ToonPayload(
            kind="fusion",
            body=body,
        )
        assert payload.kind == "fusion"
        assert "T:" in payload.body
        assert "XV:" in payload.body

    def test_valid_factor_matrix_payload(self):
        """测试有效的 factor_matrix 类型载体"""
        payload = ToonPayload(
            kind="factor_matrix",
            body="dm:jia,ssn:spring,str:0.75",
        )
        assert payload.kind == "factor_matrix"

    def test_valid_memory_payload(self):
        """测试有效的 memory 类型载体"""
        payload = ToonPayload(
            kind="memory",
            body="u:12345,t:事业突破|领导力,s:0.85",
        )
        assert payload.kind == "memory"

    def test_all_kinds(self):
        """测试所有载体类型"""
        kinds = ["rule", "fusion", "memory", "factor_matrix"]
        for kind in kinds:
            payload = ToonPayload(
                kind=kind,
                body="test content",
            )
            assert payload.kind == kind

    def test_invalid_kind(self):
        """测试无效的载体类型"""
        with pytest.raises(ValidationError):
            ToonPayload(
                kind="invalid",  # 不支持的类型
                body="test",
            )

    def test_body_max_length(self):
        """测试 body 最大长度"""
        # 1000 字符以内有效
        payload = ToonPayload(
            kind="rule",
            body="x" * 1000,
        )
        assert len(payload.body) == 1000

        # 超过 1000 字符失败
        with pytest.raises(ValidationError):
            ToonPayload(
                kind="rule",
                body="x" * 1001,
            )

    def test_empty_body(self):
        """测试空 body"""
        # 空字符串应该有效（虽然实际上不常用）
        payload = ToonPayload(
            kind="rule",
            body="",
        )
        assert payload.body == ""

    def test_version_default(self):
        """测试版本默认值"""
        payload = ToonPayload(
            kind="rule",
            body="test",
        )
        assert payload.version == "1"

    def test_version_explicit(self):
        """测试显式设置版本"""
        payload = ToonPayload(
            version="1",
            kind="rule",
            body="test",
        )
        assert payload.version == "1"

    def test_multiline_body(self):
        """测试多行 body"""
        payload = ToonPayload(
            kind="fusion",
            body="line1\nline2\nline3",
        )
        assert "\n" in payload.body
        assert len(payload.body.split("\n")) == 3

    def test_unicode_body(self):
        """测试 Unicode 内容"""
        payload = ToonPayload(
            kind="fusion",
            body="T:事业突破|财富积累|人际拓展",
        )
        assert "事业突破" in payload.body

    def test_real_rule_format(self):
        """测试真实的 rule 格式"""
        # 根据 TOON_SYNTAX["rule"]["format"]
        body = "dts_jia_spring_001:C/+/0.85/dm,sn,st"
        payload = ToonPayload(kind="rule", body=body)
        
        # 解析验证
        parts = payload.body.split(":")
        assert len(parts) == 2
        rule_id = parts[0]
        assert rule_id == "dts_jia_spring_001"
        
        details = parts[1].split("/")
        assert len(details) == 4
        assert details[0] == "C"   # 维度
        assert details[1] == "+"   # 等级
        assert details[2] == "0.85"  # 置信度

    def test_real_factor_matrix_format(self):
        """测试真实的 factor_matrix 格式"""
        # 根据 TOON_SYNTAX["factor_matrix"]["format"]
        body = "dm:jia,ssn:spring,str:0.75"
        payload = ToonPayload(kind="factor_matrix", body=body)
        
        # 解析验证
        pairs = payload.body.split(",")
        assert len(pairs) == 3
        
        factor_dict = {}
        for pair in pairs:
            k, v = pair.split(":")
            factor_dict[k] = v
        
        assert factor_dict["dm"] == "jia"
        assert factor_dict["ssn"] == "spring"
        assert factor_dict["str"] == "0.75"


# =============================================================================
# TOON 压缩效果测试
# =============================================================================


class TestToonCompressionDemo:
    """TOON 压缩效果演示测试"""

    def test_rule_compression_ratio(self):
        """测试规则压缩率"""
        # 原始 JSON 格式（约 200+ 字符）
        original = """{
            "rule_id": "dts_jia_spring_001",
            "dimension": "事业",
            "level": "吉",
            "confidence": 0.85,
            "evidence_factors": ["day_master", "season", "strength"]
        }"""
        
        # TOON 格式（约 40 字符）
        toon = "dts_jia_spring_001:C/+/0.85/dm,sn,st"
        
        # 压缩率 > 70%
        compression_ratio = 1 - (len(toon) / len(original))
        assert compression_ratio > 0.7

    def test_fusion_compression_ratio(self):
        """测试融合结果压缩率"""
        # 原始 JSON 格式（约 500+ 字符）
        original = """{
            "primary_themes": ["事业突破", "财富积累", "团队建设"],
            "evidence_chain": [
                {"rule_id": "dts_jia_001", "dimension": "事业", "level": "吉", "confidence": 0.85},
                {"rule_id": "bazi_cai_002", "dimension": "财富", "level": "大吉", "confidence": 0.9}
            ],
            "cross_validation_score": 0.87,
            "conflict_count": 0
        }"""
        
        # TOON 格式（约 100 字符）
        toon = "T:事业突破|财富积累|团队建设\ndts_jia_001:C/+/0.85/dm\nbazi_cai_002:W/++/0.9/cai\nXV:0.87\nCF:0"
        
        # 压缩率 > 70%
        compression_ratio = 1 - (len(toon) / len(original))
        assert compression_ratio > 0.7
