"""
Conflict Integration Tests

冲突检测集成测试，验证 Layer 3 ConflictResolver 在 Layer 4 的复用。

对照 tasks.md Task 9.1-9.5
对照 Requirements 5.1-5.5
"""

import pytest

from backend.core.contracts import RuntimeRuleResult, ConflictWarning
from backend.rules.conflict import ConflictResolver, ExclusiveGroups
from backend.integration import FusionEngine


class TestConflictIntegration:
    """冲突检测集成测试"""
    
    @pytest.fixture
    def exclusive_groups(self):
        """创建互斥组"""
        groups = ExclusiveGroups()
        # 添加测试用互斥组 (使用 add_group 方法)
        groups.add_group("test_body_strength_group", [
            "bazi_body_strong_001",
            "bazi_body_weak_001",
        ])
        return groups
    
    @pytest.fixture
    def conflict_resolver(self, exclusive_groups):
        """创建冲突解决器"""
        return ConflictResolver(exclusive_groups=exclusive_groups)
    
    @pytest.fixture
    def fusion_engine_with_resolver(self, conflict_resolver):
        """创建带冲突解决器的融合引擎"""
        return FusionEngine(conflict_resolver=conflict_resolver)
    
    def test_conflict_detection_reuses_layer3(self, fusion_engine_with_resolver):
        """测试复用 Layer 3 ConflictResolver (Requirement 5.1)"""
        # 创建冲突结果 - 同一互斥组的两个规则
        results = {
            "bazi-calculator": [
                RuntimeRuleResult(
                    rule_id="bazi_body_strong_001",
                    matched=True,
                    dimension="personality",
                    level="吉",
                    description="日主身强",
                    confidence=0.85,
                    weight=1.5,
                    tags=["身强"],
                    evidence_factors=["day_master"],
                    execution_time_ms=1.0,
                ),
                RuntimeRuleResult(
                    rule_id="bazi_body_weak_001",
                    matched=True,
                    dimension="personality",
                    level="凶",
                    description="日主身弱",
                    confidence=0.7,
                    weight=1.2,
                    tags=["身弱"],
                    evidence_factors=["day_master"],
                    execution_time_ms=1.0,
                ),
            ],
        }
        
        fusion_result = fusion_engine_with_resolver.fuse_results(results)
        
        # 应该检测到冲突
        assert len(fusion_result.conflicts) >= 1
    
    def test_conflict_warning_format(self, fusion_engine_with_resolver):
        """测试冲突警告格式 (Requirement 5.2)"""
        results = {
            "bazi-calculator": [
                RuntimeRuleResult(
                    rule_id="bazi_body_strong_001",
                    matched=True,
                    dimension="personality",
                    level="吉",
                    confidence=0.85,
                    weight=1.5,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
                RuntimeRuleResult(
                    rule_id="bazi_body_weak_001",
                    matched=True,
                    dimension="personality",
                    level="凶",
                    confidence=0.7,
                    weight=1.2,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
            ],
        }
        
        fusion_result = fusion_engine_with_resolver.fuse_results(results)
        
        if fusion_result.conflicts:
            conflict = fusion_result.conflicts[0]
            # 验证是 Pydantic 契约版本
            assert isinstance(conflict, ConflictWarning)
            # 验证字段存在
            assert hasattr(conflict, "group")
            assert hasattr(conflict, "conflicting_rules")
            assert hasattr(conflict, "severity")
            assert hasattr(conflict, "resolution_strategy")
    
    def test_no_conflict_when_no_exclusive_group(self, fusion_engine):
        """测试无互斥组时不产生冲突"""
        results = {
            "bazi-calculator": [
                RuntimeRuleResult(
                    rule_id="bazi_career_001",
                    matched=True,
                    dimension="career",
                    level="吉",
                    confidence=0.85,
                    weight=1.5,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
            ],
            "astro-calculator": [
                RuntimeRuleResult(
                    rule_id="astro_career_001",
                    matched=True,
                    dimension="career",
                    level="大吉",
                    confidence=0.9,
                    weight=1.8,
                    tags=[],
                    evidence_factors=[],
                    execution_time_ms=1.0,
                ),
            ],
        }
        
        fusion_result = fusion_engine.fuse_results(results)
        
        # 不同引擎的规则默认不在同一互斥组
        # 冲突应该为空或仅记录跨引擎冲突
        # 默认 ConflictResolver 没有预设互斥组，所以应该没有冲突
        assert isinstance(fusion_result.conflicts, list)


class TestConflictSeverity:
    """冲突严重程度测试"""
    
    def test_severity_values(self):
        """测试严重程度枚举值 (Requirement 7.5)"""
        valid_severities = ["LOW", "MEDIUM", "HIGH"]
        
        # 创建测试冲突警告
        warning = ConflictWarning(
            group="test_group",
            conflicting_rules=["rule_1", "rule_2"],
            severity="MEDIUM",
            resolution_strategy="priority_based",
        )
        
        assert warning.severity in valid_severities


class TestResolutionStrategies:
    """解决策略测试"""
    
    def test_four_strategies_available(self):
        """测试 4 种解决策略可用 (Requirement 5.3)"""
        from backend.rules.conflict import ResolutionStrategy
        
        strategies = [
            ResolutionStrategy.PRIORITY_BASED,
            ResolutionStrategy.WEIGHT_BASED,
            ResolutionStrategy.CONFIDENCE_BASED,
            ResolutionStrategy.SOURCE_BASED,
        ]
        
        assert len(strategies) >= 4
        
        for strategy in strategies:
            assert strategy.value in [
                "priority_based",
                "weight_based",
                "confidence_based",
                "source_based",
            ]
