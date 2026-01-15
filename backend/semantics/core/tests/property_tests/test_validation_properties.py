"""
Validation Property Tests

属性测试 - 验证层正确性
对齐 tasks.md 1.6, 3.6

Properties:
- Property 2: ID Format Validation
- Property 3: L2.5 Field Completeness
"""

import re

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from scripts.codegen.validation import (
    CONCEPT_ID_PATTERN,
    EVIDENCE_ID_PATTERN,
    FACTOR_ID_PATTERN,
    RELATION_ID_PATTERN,
    SEMANTIC_ID_PATTERN,
    SNIPPET_ID_PATTERN,
    MigrationValidator,
    ValidationErrorType,
)


# -----------------------------------------------------------------------------
# Hypothesis Strategies
# -----------------------------------------------------------------------------

# 生成有效的 semantic_id
valid_semantic_id = st.from_regex(
    r"^[a-z]+_v\d+_[a-z0-9_]+_\d{3}$",
    fullmatch=True
).filter(lambda s: len(s) <= 50)

# 生成无效的 semantic_id (不符合格式)
invalid_semantic_id = st.one_of(
    st.text(min_size=1, max_size=20).filter(
        lambda s: not re.match(SEMANTIC_ID_PATTERN, s)
    ),
    st.just(""),
    st.just("INVALID_ID"),
    st.just("123_v1_test_001"),  # 以数字开头
    st.just("test_v1_TEST_001"),  # 大写字母
)

# 生成有效的 factor_id
valid_factor_id = st.from_regex(
    r"^[a-z][a-z0-9_]*$",
    fullmatch=True
).filter(lambda s: 1 <= len(s) <= 30)

# 生成无效的 factor_id
invalid_factor_id = st.one_of(
    st.just(""),
    st.just("123abc"),  # 以数字开头
    st.just("ABC"),  # 大写
    st.just("test-factor"),  # 包含连字符
)


# -----------------------------------------------------------------------------
# Property 2: ID Format Validation
# **Feature: semantic-layer-phase2, Property 2: ID Format Validation**
# **Validates: Requirements 1.4, 9.6**
# -----------------------------------------------------------------------------

class TestIDFormatValidation:
    """Property 2: ID 格式验证"""
    
    @given(semantic_id=valid_semantic_id)
    @settings(max_examples=50)
    def test_valid_semantic_id_passes_validation(self, semantic_id: str):
        """
        **Feature: semantic-layer-phase2, Property 2: ID Format Validation**
        
        有效的 semantic_id 应该通过验证
        """
        assert re.match(SEMANTIC_ID_PATTERN, semantic_id) is not None
    
    @given(semantic_id=invalid_semantic_id)
    @settings(max_examples=50)
    def test_invalid_semantic_id_fails_validation(self, semantic_id: str):
        """
        **Feature: semantic-layer-phase2, Property 2: ID Format Validation**
        
        无效的 semantic_id 应该被拒绝
        """
        if semantic_id:  # 空字符串特殊处理
            assert re.match(SEMANTIC_ID_PATTERN, semantic_id) is None
    
    @given(factor_id=valid_factor_id)
    @settings(max_examples=50)
    def test_valid_factor_id_passes_validation(self, factor_id: str):
        """
        **Feature: semantic-layer-phase2, Property 2: ID Format Validation**
        
        有效的 factor_id 应该通过验证
        """
        assert re.match(FACTOR_ID_PATTERN, factor_id) is not None
    
    @given(factor_id=invalid_factor_id)
    @settings(max_examples=50)
    def test_invalid_factor_id_fails_validation(self, factor_id: str):
        """
        **Feature: semantic-layer-phase2, Property 2: ID Format Validation**
        
        无效的 factor_id 应该被拒绝
        """
        if factor_id:  # 空字符串特殊处理
            assert re.match(FACTOR_ID_PATTERN, factor_id) is None
    
    def test_snippet_id_pattern(self):
        """验证 snippet_id 模式"""
        valid_ids = ["ns_test_001", "snippet_example_123", "a_999"]
        invalid_ids = ["", "NS_TEST_001", "123_test", "test-001"]
        
        for sid in valid_ids:
            assert re.match(SNIPPET_ID_PATTERN, sid) is not None, f"{sid} should be valid"
        
        for sid in invalid_ids:
            if sid:
                assert re.match(SNIPPET_ID_PATTERN, sid) is None, f"{sid} should be invalid"
    
    def test_relation_id_pattern(self):
        """验证 relation_id 模式"""
        valid_ids = ["rel_test_001", "rel_dts_shengke_123"]
        invalid_ids = ["", "relation_001", "REL_TEST_001"]
        
        for rid in valid_ids:
            assert re.match(RELATION_ID_PATTERN, rid) is not None, f"{rid} should be valid"
        
        for rid in invalid_ids:
            if rid:
                assert re.match(RELATION_ID_PATTERN, rid) is None, f"{rid} should be invalid"
    
    def test_evidence_id_pattern(self):
        """验证 evidence_id 模式"""
        valid_ids = ["evi_test_001", "evi_dts_proof_123"]
        invalid_ids = ["", "evidence_001", "EVI_TEST_001"]
        
        for eid in valid_ids:
            assert re.match(EVIDENCE_ID_PATTERN, eid) is not None, f"{eid} should be valid"
        
        for eid in invalid_ids:
            if eid:
                assert re.match(EVIDENCE_ID_PATTERN, eid) is None, f"{eid} should be invalid"
    
    def test_concept_id_pattern(self):
        """验证 concept_id 模式"""
        valid_ids = ["concept_authority", "concept_shadow_self"]
        invalid_ids = ["", "concept-test", "CONCEPT_TEST"]
        
        for cid in valid_ids:
            assert re.match(CONCEPT_ID_PATTERN, cid) is not None, f"{cid} should be valid"
        
        for cid in invalid_ids:
            if cid:
                assert re.match(CONCEPT_ID_PATTERN, cid) is None, f"{cid} should be invalid"


# -----------------------------------------------------------------------------
# Property 3: L2.5 Field Completeness
# **Feature: semantic-layer-phase2, Property 3: L2.5 Field Completeness**
# **Validates: Requirements 1.3**
# -----------------------------------------------------------------------------

class TestL25FieldCompleteness:
    """Property 3: L2.5 字段完整性"""
    
    def setup_method(self):
        self.validator = MigrationValidator()
    
    def test_valid_entry_passes_validation(self):
        """
        **Feature: semantic-layer-phase2, Property 3: L2.5 Field Completeness**
        
        完整的条目应该通过验证
        """
        entry = {
            "semantic_id": "dts_v1_test_001",
            "book_id": "dts",
            "engine_id": "bazi",
            "l1": {"original_text": "测试原文"},
            "l2": {"normalized_text_zh": "测试释义"},
            "subject": "测试主题",
            "factor_refs": ["day_master_jia"],
            "related_semantics": [{"relation_id": "rel_test_001"}],
            "evidence_refs": [{"evidence_id": "evi_test_001"}],
        }
        
        errors = self.validator.validate_entry(entry)
        # 只检查非 WARNING 错误
        critical_errors = [e for e in errors if e.severity == "ERROR"]
        assert len(critical_errors) == 0, f"Unexpected errors: {critical_errors}"
    
    def test_missing_original_text_fails(self):
        """
        **Feature: semantic-layer-phase2, Property 3: L2.5 Field Completeness**
        
        缺少 original_text 应该失败
        """
        entry = {
            "semantic_id": "dts_v1_test_001",
            "book_id": "dts",
            "engine_id": "bazi",
            "l1": {"original_text": ""},  # 空
            "subject": "测试",
            "factor_refs": ["day_master_jia"],
        }
        
        errors = self.validator.validate_entry(entry)
        error_types = [e.error_type for e in errors if e.severity == "ERROR"]
        assert ValidationErrorType.MISSING_L1_FIELD in error_types
    
    def test_empty_factor_refs_warning(self):
        """
        **Feature: semantic-layer-phase2, Property 3: L2.5 Field Completeness**
        
        空的 factor_refs 应该生成警告
        """
        entry = {
            "semantic_id": "dts_v1_test_001",
            "book_id": "dts",
            "engine_id": "bazi",
            "l1": {"original_text": "测试原文"},
            "subject": "测试",
            "factor_refs": [],  # 空列表
        }
        
        errors = self.validator.validate_entry(entry)
        warning_types = [e.error_type for e in errors if e.severity == "WARNING"]
        assert ValidationErrorType.EMPTY_FACTOR_REFS in warning_types
    
    @given(original_text=st.text(min_size=10, max_size=100))
    @settings(max_examples=20)
    def test_non_empty_original_text_passes_l1_validation(self, original_text: str):
        """
        **Feature: semantic-layer-phase2, Property 3: L2.5 Field Completeness**
        
        非空的 original_text 应该通过 L1 验证
        """
        entry = {
            "l1": {"original_text": original_text},
            "subject": "test",
            "factor_refs": ["test_factor"],
        }
        
        errors = self.validator._validate_l1_completeness(entry, "test.md")
        assert len(errors) == 0
