"""
Test Rule Context

规则执行上下文测试 - 验证因子访问和语义缓存。

对照 tasks.md Task 1.5, 1.6:
- Property 2: Factor Access Consistency
- Validates: Requirements 1.3, 1.4
"""

import pytest
from hypothesis import given, strategies as st, settings
from unittest.mock import MagicMock, patch

from backend.core.contracts import FactorMatrix, FactorValue
from backend.rules.context import RuleContext


@pytest.fixture
def sample_factors():
    """创建示例因子字典"""
    return {
        "day_master": FactorValue(
            factor_id="day_master",
            value="甲",
            confidence=1.0,
            source="bazi_calculator",
        ),
        "month_branch": FactorValue(
            factor_id="month_branch",
            value="寅",
            confidence=1.0,
            source="bazi_calculator",
        ),
        "strength": FactorValue(
            factor_id="strength",
            value=0.7,
            confidence=0.9,
            source="bazi_calculator",
        ),
        "count": FactorValue(
            factor_id="count",
            value=3,
            confidence=1.0,
            source="bazi_calculator",
        ),
        "zero_value": FactorValue(
            factor_id="zero_value",
            value=0,
            confidence=1.0,
            source="test",
        ),
        "empty_string": FactorValue(
            factor_id="empty_string",
            value="",
            confidence=1.0,
            source="test",
        ),
    }


@pytest.fixture
def sample_factor_matrix(sample_factors):
    """创建示例因子矩阵"""
    return FactorMatrix(
        engine_id="bazi",
        factors=sample_factors,
    )


@pytest.fixture
def rule_context(sample_factor_matrix):
    """创建规则上下文"""
    return RuleContext(factor_matrix=sample_factor_matrix)


class TestRuleContextFactorAccess:
    """因子访问测试"""
    
    def test_get_factor(self, rule_context):
        """测试 get_factor()"""
        fv = rule_context.get_factor("day_master")
        assert fv is not None
        assert fv.factor_id == "day_master"
        assert fv.value == "甲"
    
    def test_get_factor_not_found(self, rule_context):
        """测试 get_factor() 未找到"""
        fv = rule_context.get_factor("nonexistent")
        assert fv is None
    
    def test_get_factor_value(self, rule_context):
        """测试 get_factor_value()"""
        value = rule_context.get_factor_value("day_master")
        assert value == "甲"
        
        value = rule_context.get_factor_value("strength")
        assert value == 0.7
    
    def test_get_factor_value_default(self, rule_context):
        """测试 get_factor_value() 默认值"""
        value = rule_context.get_factor_value("nonexistent", default="default")
        assert value == "default"
    
    def test_get_factors_batch(self, rule_context):
        """测试 get_factors() 批量获取"""
        factors = rule_context.get_factors(["day_master", "month_branch"])
        
        assert "day_master" in factors
        assert "month_branch" in factors
        assert factors["day_master"] == "甲"
        assert factors["month_branch"] == "寅"
    
    def test_get_factors_with_missing(self, rule_context):
        """测试 get_factors() 包含不存在的因子"""
        factors = rule_context.get_factors(["day_master", "nonexistent"])
        
        assert factors["day_master"] == "甲"
        assert factors["nonexistent"] is None
    
    def test_get_factors_caching(self, rule_context):
        """测试 get_factors() 缓存"""
        factors1 = rule_context.get_factors(["day_master", "month_branch"])
        factors2 = rule_context.get_factors(["day_master", "month_branch"])
        
        # 应该返回相同的缓存对象
        assert factors1 is factors2
    
    def test_has_factor(self, rule_context):
        """测试 has_factor()"""
        assert rule_context.has_factor("day_master") is True
        assert rule_context.has_factor("nonexistent") is False
    
    def test_get_shortcut(self, rule_context):
        """测试 get() 快捷方法"""
        value = rule_context.get("day_master")
        assert value == "甲"
        
        value = rule_context.get("nonexistent")
        assert value is None
    
    def test_zero_value_factor(self, rule_context):
        """测试值为 0 的因子"""
        value = rule_context.get_factor_value("zero_value")
        assert value == 0
        assert rule_context.has_factor("zero_value") is True
    
    def test_empty_string_factor(self, rule_context):
        """测试值为空字符串的因子"""
        value = rule_context.get_factor_value("empty_string")
        assert value == ""
        assert rule_context.has_factor("empty_string") is True


class TestRuleContextFactorAccessConsistency:
    """
    因子访问一致性测试
    
    **Feature: layer3-rules, Property 2: Factor Access Consistency**
    **Validates: Requirements 1.3**
    """
    
    def test_consistency_existing_factor(self, rule_context):
        """测试存在因子的访问一致性"""
        factor_id = "day_master"
        
        # has_factor 返回 True
        assert rule_context.has_factor(factor_id) is True
        
        # get_factor 返回非 None
        fv = rule_context.get_factor(factor_id)
        assert fv is not None
        
        # get_factor_value 返回实际值
        value = rule_context.get_factor_value(factor_id)
        assert value == fv.value
        
        # get 返回实际值
        assert rule_context.get(factor_id) == value
    
    def test_consistency_missing_factor(self, rule_context):
        """测试不存在因子的访问一致性"""
        factor_id = "nonexistent"
        
        # has_factor 返回 False
        assert rule_context.has_factor(factor_id) is False
        
        # get_factor 返回 None
        assert rule_context.get_factor(factor_id) is None
        
        # get_factor_value 返回 None
        assert rule_context.get_factor_value(factor_id) is None
        
        # get 返回 None
        assert rule_context.get(factor_id) is None
    
    @given(
        factor_values=st.dictionaries(
            keys=st.text(min_size=1, max_size=20, alphabet="abcdefghijklmnopqrstuvwxyz_"),
            values=st.one_of(
                st.integers(),
                st.floats(allow_nan=False, allow_infinity=False),
                st.booleans(),
                st.text(max_size=10),
            ),
            min_size=1,
            max_size=10,
        )
    )
    @settings(max_examples=50)
    def test_property_factor_access_consistency(self, factor_values):
        """
        **Feature: layer3-rules, Property 2: Factor Access Consistency**
        
        对任意因子矩阵，has_factor/get_factor/get_factor_value 应一致
        """
        # 构建因子矩阵
        factors = {
            k: FactorValue(factor_id=k, value=v, confidence=1.0, source="test")
            for k, v in factor_values.items()
        }
        matrix = FactorMatrix(engine_id="test", factors=factors)
        context = RuleContext(factor_matrix=matrix)
        
        # 验证所有存在的因子
        for factor_id, expected_value in factor_values.items():
            # has_factor 应返回 True
            assert context.has_factor(factor_id) is True
            
            # get_factor 应返回非 None
            fv = context.get_factor(factor_id)
            assert fv is not None
            
            # 值应一致
            assert context.get_factor_value(factor_id) == expected_value
            assert context.get(factor_id) == expected_value
        
        # 验证不存在的因子
        nonexistent = "definitely_nonexistent_factor_12345"
        assert context.has_factor(nonexistent) is False
        assert context.get_factor(nonexistent) is None
        assert context.get_factor_value(nonexistent) is None


class TestRuleContextSemanticAccess:
    """语义条目访问测试"""
    
    def test_get_semantic_entry_not_found(self, rule_context):
        """测试获取不存在的语义条目"""
        # 由于没有配置 semantic_cache 和 registry，应返回 None
        entry = rule_context.get_semantic_entry("nonexistent_semantic")
        assert entry is None
    
    def test_semantic_access_log(self, rule_context):
        """测试语义访问日志"""
        # 尝试获取语义条目（会失败）
        rule_context.get_semantic_entry("test_semantic_1")
        rule_context.get_semantic_entry("test_semantic_2")
        
        log = rule_context.get_semantic_access_log()
        assert len(log) == 2
        assert log[0]["semantic_id"] == "test_semantic_1"
        assert log[1]["semantic_id"] == "test_semantic_2"
        assert log[0]["source"] == "not_found"
    
    def test_semantic_cache_integration(self, sample_factor_matrix):
        """测试语义缓存集成"""
        # 创建 mock 缓存
        mock_cache = MagicMock()
        mock_entry = MagicMock()
        mock_cache.get_sync.return_value = mock_entry
        
        context = RuleContext(
            factor_matrix=sample_factor_matrix,
            semantic_cache=mock_cache,
        )
        
        # 获取语义条目
        entry = context.get_semantic_entry("test_semantic")
        
        # 应该从缓存获取
        assert entry is mock_entry
        mock_cache.get_sync.assert_called_once_with("test_semantic")
        
        # 再次获取应该从本地缓存获取
        entry2 = context.get_semantic_entry("test_semantic")
        assert entry2 is mock_entry
        # get_sync 仍只调用一次（本地缓存命中）
        assert mock_cache.get_sync.call_count == 1
    
    def test_resolve_semantic_refs(self, sample_factor_matrix):
        """测试批量解析语义引用"""
        # 创建 mock 缓存
        mock_cache = MagicMock()
        mock_entry1 = MagicMock()
        mock_entry2 = MagicMock()
        
        def mock_get_sync(semantic_id):
            if semantic_id == "ref_1":
                return mock_entry1
            elif semantic_id == "ref_2":
                return mock_entry2
            return None
        
        mock_cache.get_sync.side_effect = mock_get_sync
        
        context = RuleContext(
            factor_matrix=sample_factor_matrix,
            semantic_cache=mock_cache,
        )
        
        entries = context.resolve_semantic_refs(["ref_1", "ref_2", "ref_nonexistent"])
        
        assert len(entries) == 2
        assert mock_entry1 in entries
        assert mock_entry2 in entries


class TestRuleContextCacheManagement:
    """缓存管理测试"""
    
    def test_clear_caches(self, rule_context):
        """测试清空缓存"""
        # 填充缓存
        rule_context.get_factors(["day_master", "month_branch"])
        rule_context.get_semantic_entry("test")
        
        # 验证有数据
        assert len(rule_context._factors_cache) > 0
        assert len(rule_context._semantic_access_log) > 0
        
        # 清空
        rule_context.clear_caches()
        
        # 验证已清空
        assert len(rule_context._factors_cache) == 0
        assert len(rule_context._semantic_entries_cache) == 0
        assert len(rule_context._semantic_access_log) == 0
