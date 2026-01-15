"""
Test Conflict Resolver

冲突解决器测试 - 验证互斥组、解决策略、严重级别评估。

对照 tasks.md Task 5:
- Property 4: Conflict Resolution Determinism
- Validates: Requirements 3.1-3.10
"""

import pytest
from hypothesis import given, strategies as st, settings

from backend.core.contracts import RuntimeRuleResult
from backend.rules.conflict import (
    ConflictResolver,
    ConflictWarning,
    ConflictSeverity,
    ExclusiveGroups,
    ResolutionStrategy,
)


@pytest.fixture
def exclusive_groups():
    """创建互斥组管理器"""
    return ExclusiveGroups()


@pytest.fixture
def conflict_resolver():
    """创建冲突解决器"""
    return ConflictResolver()


@pytest.fixture
def sample_results():
    """创建示例规则结果（同一互斥组）"""
    return [
        RuntimeRuleResult(
            rule_id="rule_body_strong",
            matched=True,
            dimension="personality",
            level="吉",
            confidence=0.9,
            weight=2.0,
            tags=[],
            evidence_factors=[],
            source_book="滴天髓",
            execution_time_ms=0.1,
        ),
        RuntimeRuleResult(
            rule_id="rule_body_weak",
            matched=True,
            dimension="personality",
            level="凶",
            confidence=0.8,
            weight=1.5,
            tags=[],
            evidence_factors=[],
            source_book="三命通会",
            execution_time_ms=0.1,
        ),
    ]


class TestExclusiveGroups:
    """互斥组管理器测试"""
    
    def test_predefined_groups(self, exclusive_groups):
        """测试预定义互斥组"""
        assert "body_strength_group" in exclusive_groups.get_all_groups()
        assert "wealth_pattern_group" in exclusive_groups.get_all_groups()
        assert "career_direction_group" in exclusive_groups.get_all_groups()
    
    def test_get_group(self, exclusive_groups):
        """测试获取规则所属组"""
        assert exclusive_groups.get_group("rule_body_strong") == "body_strength_group"
        assert exclusive_groups.get_group("rule_body_weak") == "body_strength_group"
        assert exclusive_groups.get_group("nonexistent_rule") is None
    
    def test_add_custom_group(self, exclusive_groups):
        """测试添加自定义互斥组"""
        exclusive_groups.add_group("custom_group", ["rule_a", "rule_b"])
        
        assert "custom_group" in exclusive_groups.get_all_groups()
        assert exclusive_groups.get_group("rule_a") == "custom_group"
        assert exclusive_groups.get_group("rule_b") == "custom_group"
    
    def test_remove_group(self, exclusive_groups):
        """测试移除互斥组"""
        exclusive_groups.add_group("temp_group", ["rule_temp"])
        assert exclusive_groups.get_group("rule_temp") == "temp_group"
        
        result = exclusive_groups.remove_group("temp_group")
        assert result is True
        assert exclusive_groups.get_group("rule_temp") is None
    
    def test_get_group_rules(self, exclusive_groups):
        """测试获取组内规则"""
        rules = exclusive_groups.get_group_rules("body_strength_group")
        
        assert "rule_body_strong" in rules
        assert "rule_body_weak" in rules
        assert "rule_body_neutral" in rules
    
    def test_is_in_group(self, exclusive_groups):
        """测试检查规则是否在组内"""
        assert exclusive_groups.is_in_group("rule_body_strong", "body_strength_group") is True
        assert exclusive_groups.is_in_group("rule_body_strong", "wealth_pattern_group") is False


class TestConflictResolverStrategies:
    """冲突解决策略测试"""
    
    def test_resolve_by_priority(self, conflict_resolver, sample_results):
        """测试按优先级（权重）解决"""
        result = conflict_resolver._resolve_by_priority(sample_results)
        
        # 应该选择权重最高的（2.0）
        assert result.rule_id == "rule_body_strong"
    
    def test_resolve_by_weight(self, conflict_resolver, sample_results):
        """测试按权重解决"""
        result = conflict_resolver._resolve_by_weight(sample_results)
        
        # 应该选择权重最高的（2.0）
        assert result.rule_id == "rule_body_strong"
    
    def test_resolve_by_confidence(self, conflict_resolver, sample_results):
        """测试按置信度解决"""
        result = conflict_resolver._resolve_by_confidence(sample_results)
        
        # 应该选择置信度最高的（0.9）
        assert result.rule_id == "rule_body_strong"
    
    def test_resolve_by_source(self, conflict_resolver, sample_results):
        """测试按来源权威性解决"""
        result = conflict_resolver._resolve_by_source(sample_results)
        
        # 滴天髓排名最高，应该选择 rule_body_strong
        assert result.rule_id == "rule_body_strong"
    
    def test_resolve_by_source_unknown(self, conflict_resolver):
        """测试未知来源的处理"""
        results = [
            RuntimeRuleResult(
                rule_id="rule_a",
                matched=True,
                dimension="test",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                source_book="unknown_book",
                execution_time_ms=0.1,
            ),
            RuntimeRuleResult(
                rule_id="rule_b",
                matched=True,
                dimension="test",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                source_book="滴天髓",
                execution_time_ms=0.1,
            ),
        ]
        
        result = conflict_resolver._resolve_by_source(results)
        # 滴天髓是已知来源，应该选择 rule_b
        assert result.rule_id == "rule_b"


class TestConflictResolverResolveAll:
    """冲突解决 resolve_all 测试"""
    
    def test_resolve_all_with_conflict(self, conflict_resolver, sample_results):
        """测试解决冲突"""
        resolved = conflict_resolver.resolve_all(sample_results)
        
        # 应该只保留一个结果
        matched_results = [r for r in resolved if r.matched]
        assert len(matched_results) == 1
        
        # 应该有警告
        warnings = conflict_resolver.get_warnings()
        assert len(warnings) == 1
        assert warnings[0].group == "body_strength_group"
    
    def test_resolve_all_no_conflict(self, conflict_resolver):
        """测试无冲突情况"""
        results = [
            RuntimeRuleResult(
                rule_id="independent_rule_1",
                matched=True,
                dimension="test",
                confidence=0.8,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
            RuntimeRuleResult(
                rule_id="independent_rule_2",
                matched=True,
                dimension="test",
                confidence=0.7,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
        ]
        
        resolved = conflict_resolver.resolve_all(results)
        
        # 两个都应该保留
        matched_results = [r for r in resolved if r.matched]
        assert len(matched_results) == 2
        
        # 无警告
        assert len(conflict_resolver.get_warnings()) == 0
    
    def test_resolve_all_with_strategy(self, sample_results):
        """测试使用不同策略"""
        # 修改 sample_results 使得不同策略选择不同结果
        sample_results[0].confidence = 0.7  # 降低 rule_body_strong 的置信度
        sample_results[1].confidence = 0.9  # 提高 rule_body_weak 的置信度
        
        # 权重策略选择 rule_body_strong (weight=2.0)
        resolver_weight = ConflictResolver(default_strategy=ResolutionStrategy.WEIGHT_BASED)
        resolved_weight = resolver_weight.resolve_all(sample_results)
        selected_weight = [r for r in resolved_weight if r.matched][0]
        assert selected_weight.rule_id == "rule_body_strong"
        
        # 置信度策略选择 rule_body_weak (confidence=0.9)
        resolver_conf = ConflictResolver(default_strategy=ResolutionStrategy.CONFIDENCE_BASED)
        resolved_conf = resolver_conf.resolve_all(sample_results)
        selected_conf = [r for r in resolved_conf if r.matched][0]
        assert selected_conf.rule_id == "rule_body_weak"
    
    def test_resolve_all_preserves_unmatched(self, conflict_resolver, sample_results):
        """测试保留未匹配的结果"""
        unmatched = RuntimeRuleResult(
            rule_id="unmatched_rule",
            matched=False,
            dimension="test",
            confidence=0.5,
            weight=1.0,
            tags=[],
            evidence_factors=[],
            execution_time_ms=0.1,
        )
        sample_results.append(unmatched)
        
        resolved = conflict_resolver.resolve_all(sample_results)
        
        # 未匹配的应该保留
        unmatched_results = [r for r in resolved if not r.matched]
        assert len(unmatched_results) == 1
        assert unmatched_results[0].rule_id == "unmatched_rule"


class TestConflictSeverity:
    """冲突严重级别测试"""
    
    def test_severity_high_multiple_conflicts(self, conflict_resolver):
        """测试 3 个以上冲突为高严重"""
        results = [
            RuntimeRuleResult(
                rule_id=f"rule_{i}",
                matched=True,
                dimension="test",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            )
            for i in range(3)
        ]
        
        severity = conflict_resolver._assess_severity(results)
        assert severity == ConflictSeverity.HIGH
    
    def test_severity_high_opposing_levels(self, conflict_resolver):
        """测试大吉 vs 大凶为高严重"""
        results = [
            RuntimeRuleResult(
                rule_id="rule_a",
                matched=True,
                dimension="test",
                level="大吉",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
            RuntimeRuleResult(
                rule_id="rule_b",
                matched=True,
                dimension="test",
                level="大凶",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
        ]
        
        severity = conflict_resolver._assess_severity(results)
        assert severity == ConflictSeverity.HIGH
    
    def test_severity_medium_different_levels(self, conflict_resolver):
        """测试不同级别为中等严重"""
        results = [
            RuntimeRuleResult(
                rule_id="rule_a",
                matched=True,
                dimension="test",
                level="吉",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
            RuntimeRuleResult(
                rule_id="rule_b",
                matched=True,
                dimension="test",
                level="凶",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
        ]
        
        severity = conflict_resolver._assess_severity(results)
        assert severity == ConflictSeverity.MEDIUM
    
    def test_severity_low_same_level(self, conflict_resolver):
        """测试相同级别为低严重"""
        results = [
            RuntimeRuleResult(
                rule_id="rule_a",
                matched=True,
                dimension="test",
                level="吉",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
            RuntimeRuleResult(
                rule_id="rule_b",
                matched=True,
                dimension="test",
                level="吉",
                confidence=0.5,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            ),
        ]
        
        severity = conflict_resolver._assess_severity(results)
        assert severity == ConflictSeverity.LOW


class TestConflictWarning:
    """冲突警告测试"""
    
    def test_warning_fields(self, conflict_resolver, sample_results):
        """测试警告字段"""
        conflict_resolver.resolve_all(sample_results)
        
        warnings = conflict_resolver.get_warnings()
        assert len(warnings) == 1
        
        warning = warnings[0]
        assert warning.group == "body_strength_group"
        assert "rule_body_strong" in warning.conflicting_rules
        assert "rule_body_weak" in warning.conflicting_rules
        assert warning.resolution_strategy == "priority_based"
        assert warning.selected_rule in ["rule_body_strong", "rule_body_weak"]
    
    def test_warning_to_dict(self):
        """测试警告转字典"""
        warning = ConflictWarning(
            group="test_group",
            conflicting_rules=["rule_a", "rule_b"],
            severity=ConflictSeverity.MEDIUM,
            resolution_strategy="weight_based",
            selected_rule="rule_a",
        )
        
        d = warning.to_dict()
        assert d["group"] == "test_group"
        assert d["severity"] == "MEDIUM"
        assert d["selected_rule"] == "rule_a"
    
    def test_clear_warnings(self, conflict_resolver, sample_results):
        """测试清空警告"""
        conflict_resolver.resolve_all(sample_results)
        assert len(conflict_resolver.get_warnings()) > 0
        
        conflict_resolver.clear_warnings()
        assert len(conflict_resolver.get_warnings()) == 0


class TestConflictResolverPropertyBased:
    """
    属性测试 - Property 4: Conflict Resolution Determinism
    
    对于任意同一互斥组的 RuntimeRuleResults，ConflictResolver 应该：
    1. 精确选择一个结果
    2. 相同策略和输入应该产生确定性的选择
    """
    
    @given(
        weights=st.lists(
            st.floats(min_value=0.1, max_value=10.0, allow_nan=False, allow_infinity=False),
            min_size=2,
            max_size=5,
        )
    )
    @settings(max_examples=50)
    def test_determinism_weight_strategy(self, weights):
        """
        **Feature: layer3-rules, Property 4: Conflict Resolution Determinism**
        
        测试权重策略的确定性
        """
        # 创建结果
        results = [
            RuntimeRuleResult(
                rule_id=f"rule_{i}",
                matched=True,
                dimension="test",
                confidence=0.5,
                weight=w,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            )
            for i, w in enumerate(weights)
        ]
        
        resolver = ConflictResolver(default_strategy=ResolutionStrategy.WEIGHT_BASED)
        
        # 多次执行应该产生相同结果
        selected_1 = resolver._resolve_by_weight(results)
        selected_2 = resolver._resolve_by_weight(results)
        
        assert selected_1.rule_id == selected_2.rule_id
        
        # 应该选择最高权重
        max_weight = max(weights)
        assert selected_1.weight == max_weight
    
    @given(
        confidences=st.lists(
            st.floats(min_value=0.1, max_value=1.0, allow_nan=False, allow_infinity=False),
            min_size=2,
            max_size=5,
        )
    )
    @settings(max_examples=50)
    def test_determinism_confidence_strategy(self, confidences):
        """
        **Feature: layer3-rules, Property 4: Conflict Resolution Determinism**
        
        测试置信度策略的确定性
        """
        results = [
            RuntimeRuleResult(
                rule_id=f"rule_{i}",
                matched=True,
                dimension="test",
                confidence=c,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=0.1,
            )
            for i, c in enumerate(confidences)
        ]
        
        resolver = ConflictResolver(default_strategy=ResolutionStrategy.CONFIDENCE_BASED)
        
        selected_1 = resolver._resolve_by_confidence(results)
        selected_2 = resolver._resolve_by_confidence(results)
        
        assert selected_1.rule_id == selected_2.rule_id
        
        max_confidence = max(confidences)
        assert selected_1.confidence == max_confidence
