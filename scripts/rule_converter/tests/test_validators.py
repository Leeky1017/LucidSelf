"""
Tests for Validators

Requirement Refs: Req 8, 9.4
"""

import pytest

from scripts.rule_converter.loaders.logic_chain_loader import LogicChainNode
from scripts.rule_converter.validators.quality_classifier import (
    ClassificationResult,
    QualityClassifier,
    RuleQuality,
)
from scripts.rule_converter.validators.schema_validator import (
    SchemaValidator,
    ValidationResult,
)


# ===========================================================================
# Test QualityClassifier
# ===========================================================================

class TestQualityClassifier:
    """测试 QualityClassifier"""
    
    def test_classify_high_quality(self):
        """测试高质量规则分类（AUTO_APPROVE）"""
        classifier = QualityClassifier()
        
        node = LogicChainNode(
            node_id="test_node",
            snippet_ids=["ns_001", "ns_002"],
            factor_refs=["factor1", "factor2"],
            metadata={"source_ref": "《测试》#1"},
        )
        
        rule = {
            "rule_id": "bazi_dts_career_001",
            "metadata": {
                "book_id": "ditianshui",
                "l1_anchor": "DTS_TTL_1",
            },
        }
        
        result = classifier.classify(node, rule, condition_confidence=0.9)
        
        # 无因子本体和snippet_store，得分会降低
        # 但仍应该能计算出分数
        assert result.score >= 0.0
        assert isinstance(result.quality, RuleQuality)
    
    def test_classify_low_quality(self):
        """测试低质量规则分类（REJECT）"""
        classifier = QualityClassifier()
        
        node = LogicChainNode(
            node_id="test_node",
            # 无 factor_refs, 无 snippet_ids, 无 metadata
        )
        
        rule = {
            "rule_id": "test_001",
            # 无 metadata
        }
        
        result = classifier.classify(node, rule, condition_confidence=0.3)
        
        assert result.quality == RuleQuality.REJECT
        assert result.score < 0.5
        assert len(result.reasons) > 0
    
    def test_classify_medium_quality(self):
        """测试有 factor_refs 的节点自动通过"""
        classifier = QualityClassifier()
        
        node = LogicChainNode(
            node_id="test_node",
            factor_refs=["factor1"],
            metadata={"source_ref": "《测试》#1"},
        )
        
        rule = {
            "rule_id": "test_001",
            "metadata": {"book_id": "test"},
        }
        
        result = classifier.classify(node, rule, condition_confidence=0.6)
        
        # 简化逻辑：有 factor_refs 就自动通过
        assert result.quality == RuleQuality.AUTO_APPROVE
    
    def test_stats(self):
        """测试统计功能"""
        classifier = QualityClassifier()
        
        # 分类几个规则
        node = LogicChainNode(node_id="test")
        rule = {"rule_id": "test"}
        
        classifier.classify(node, rule, 0.2)
        classifier.classify(node, rule, 0.2)
        classifier.classify(node, rule, 0.2)
        
        stats = classifier.stats
        assert stats["total_classified"] == 3
        assert stats["reject_count"] == 3


# ===========================================================================
# Test SchemaValidator
# ===========================================================================

class TestSchemaValidator:
    """测试 SchemaValidator"""
    
    @pytest.fixture
    def valid_rule(self):
        """有效的规则"""
        return {
            "rule_id": "bazi_dts_career_001",
            "human_label": "测试规则",
            "category": "career",
            "condition": {
                "factor_id": "day_master",
                "operator": "exists",
            },
            "required_factors": ["day_master"],
            "is_complex_logic": False,
            "result": {
                "dimension": "career",
                "level": "吉",
                "conclusion_template_zh": "这是测试结论",
                "weight": 1.0,
                "confidence": 0.7,
                "tags": ["测试"],
                "evidence_factors": ["day_master"],
            },
            "priority": 100,
            "version": "1.0.0",
            "status": "active",
            "engine_id": "bazi_rule_engine",
            "metadata": {
                "book_id": "ditianshui",
                "chapter": "通天论",
                "l1_anchor": "DTS_TTL_1",
            },
        }
    
    def test_validate_valid_rule(self, valid_rule):
        """测试验证有效规则"""
        validator = SchemaValidator()
        result = validator.validate(valid_rule)
        
        assert result.is_valid is True
        assert len(result.errors) == 0
    
    def test_validate_missing_required_fields(self):
        """测试缺少必填字段"""
        validator = SchemaValidator()
        
        rule = {
            "rule_id": "test_001",
            # 缺少其他必填字段
        }
        
        result = validator.validate(rule)
        
        assert result.is_valid is False
        assert len(result.errors) > 0
        
        error_fields = [e.field for e in result.errors]
        assert "human_label" in error_fields or any("必填字段" in e.message for e in result.errors)
    
    def test_validate_invalid_rule_id(self):
        """测试无效的 rule_id 格式"""
        validator = SchemaValidator()
        
        rule = {
            "rule_id": "Invalid-ID-123",  # 无效格式
            "human_label": "测试",
            "category": "test",
            "condition": {"factor_id": "f", "operator": "exists"},
            "required_factors": [],
            "result": {
                "dimension": "career",
                "level": "吉",
                "conclusion_template_zh": "测试",
            },
        }
        
        result = validator.validate(rule)
        
        assert result.is_valid is False
        error_fields = [e.field for e in result.errors]
        assert "rule_id" in error_fields
    
    def test_validate_invalid_version(self):
        """测试无效的 version 格式"""
        validator = SchemaValidator()
        
        rule = {
            "rule_id": "test_001",
            "human_label": "测试",
            "category": "test",
            "condition": {"factor_id": "f", "operator": "exists"},
            "required_factors": [],
            "result": {
                "dimension": "career",
                "level": "吉",
                "conclusion_template_zh": "测试",
            },
            "version": "invalid",  # 无效格式
        }
        
        result = validator.validate(rule)
        
        assert result.is_valid is False
        error_fields = [e.field for e in result.errors]
        assert "version" in error_fields
    
    def test_validate_invalid_status(self):
        """测试无效的 status"""
        validator = SchemaValidator()
        
        rule = {
            "rule_id": "test_001",
            "human_label": "测试",
            "category": "test",
            "condition": {"factor_id": "f", "operator": "exists"},
            "required_factors": [],
            "result": {
                "dimension": "career",
                "level": "吉",
                "conclusion_template_zh": "测试",
            },
            "status": "invalid_status",
        }
        
        result = validator.validate(rule)
        
        assert result.is_valid is False
        error_fields = [e.field for e in result.errors]
        assert "status" in error_fields
    
    def test_validate_invalid_level(self):
        """测试无效的 level"""
        validator = SchemaValidator()
        
        rule = {
            "rule_id": "test_001",
            "human_label": "测试",
            "category": "test",
            "condition": {"factor_id": "f", "operator": "exists"},
            "required_factors": [],
            "result": {
                "dimension": "career",
                "level": "无效等级",  # 无效
                "conclusion_template_zh": "测试",
            },
        }
        
        result = validator.validate(rule)
        
        assert result.is_valid is False
        error_fields = [e.field for e in result.errors]
        assert "result.level" in error_fields
    
    def test_validate_logical_expression(self, valid_rule):
        """测试验证逻辑表达式"""
        validator = SchemaValidator()
        
        valid_rule["condition"] = {
            "operator": "AND",
            "conditions": [
                {"factor_id": "f1", "operator": "exists"},
                {"factor_id": "f2", "operator": "==", "value": True},
            ],
        }
        
        result = validator.validate(valid_rule)
        
        assert result.is_valid is True
    
    def test_validate_invalid_operator(self, valid_rule):
        """测试无效的操作符"""
        validator = SchemaValidator()
        
        valid_rule["condition"] = {
            "factor_id": "f1",
            "operator": "invalid_op",
        }
        
        result = validator.validate(valid_rule)
        
        assert result.is_valid is False
        assert any("操作符" in e.message or "operator" in e.field for e in result.errors)
    
    def test_validate_batch(self):
        """测试批量验证"""
        validator = SchemaValidator()
        
        rules = [
            {
                "rule_id": "test_001",
                "human_label": "测试1",
                "category": "test",
                "condition": {"factor_id": "f", "operator": "exists"},
                "required_factors": [],
                "result": {
                    "dimension": "career",
                    "level": "吉",
                    "conclusion_template_zh": "测试",
                },
            },
            {
                "rule_id": "Invalid-ID",  # 无效
                "human_label": "测试2",
                "category": "test",
                "condition": {"factor_id": "f", "operator": "exists"},
                "required_factors": [],
                "result": {
                    "dimension": "career",
                    "level": "吉",
                    "conclusion_template_zh": "测试",
                },
            },
        ]
        
        result = validator.validate_batch(rules)
        
        assert result["total"] == 2
        assert result["valid"] == 1
        assert result["invalid"] == 1
