"""
Pytest configuration and shared fixtures for codegen tests

对照数据契约 Schema v1：
- ConfigRuleDefinition: §2.1
- ConfigFactor: §1.1
- SourceMetadata: §0.2
"""

import pytest
from pathlib import Path


@pytest.fixture
def tmp_output(tmp_path):
    """临时输出目录"""
    output_dir = tmp_path / "generated"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def minimal_rule():
    """
    最小有效规则（符合 ConfigRuleDefinition Schema）
    
    注意：运算符可以使用 EQ/NE/GT 等简写，RuleCodeGenerator 会自动规范化为 ==, !=, > 等
    """
    return {
        "rule_id": "test_001",
        "version": "1.0.0",
        "status": "active",
        "engine_id": "test",
        "category": "test_category",
        "priority": 500,
        "required_factors": ["factor_a"],
        "human_label": "测试规则",
        "condition": {
            "operator": "==",  # Schema 要求的格式
            "factor_id": "factor_a",
            "value": 1
        },
        "result": {
            "dimension": "性格",
            "level": "中等",  # 必须是: 大吉/吉/中等/凶/大凶
            "conclusion_template_zh": "测试结论",
            "confidence": 0.9,
            "weight": 1.0,
            "tags": ["test"],
            "evidence_factors": ["factor_a"]
        },
        "metadata": {
            "book_id": "test_book",
            "chapter": "chapter_1",
            "l1_anchor": "TEST_L1_001"
        }
    }


@pytest.fixture
def minimal_factor():
    """
    最小有效因子（符合 ConfigFactor Schema）
    
    必填字段：factor_id, label_zh, category, value_type, description_zh, version, engine_id, metadata
    """
    return {
        "factor_id": "test_factor",
        "version": "1.0.0",
        "status": "active",
        "engine_id": "test",
        "label_zh": "测试因子",
        "label_en": "Test Factor",
        "category": "structure",  # FactorCategory 枚举
        "value_type": "enum",  # boolean/float/enum/string
        "enum_values": ["a", "b", "c"],  # value_type=enum 时必填
        "description_zh": "用于测试的因子定义",
        "knowledge_ref": ["test_book:chapter_1"],
        "metadata": {
            "book_id": "test_book",
            "chapter": "chapter_1",
            "l1_anchor": "TEST_L1_001"
        }
    }


@pytest.fixture
def minimal_semantic():
    """最小有效语义核心"""
    return {
        "semantic_id": "test_semantic",
        "version": "1.0.0",
        "status": "active",
        "engine_id": "test",
        "term_zh": "测试术语",
        "term_en": "Test Term",
        "domain": "test",
        "l2_core": {
            "nature": "test",
            "attributes": []
        },
        "metadata": {
            "book_id": "test_book",
            "chapter": "chapter_1",
            "l1_anchor": "TEST_L1_001"
        }
    }
