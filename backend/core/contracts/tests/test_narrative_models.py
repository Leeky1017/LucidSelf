"""
Tests for Narrative and Fusion Models

对照文档: docs/数据契约_Schema定义规范_v1.md §3.1, §3.3
"""

import pytest
from datetime import datetime
from pydantic import ValidationError

from backend.core.contracts import (
    ConflictWarning,
    FusionResult,
    NarrativeConfig,
    RuntimeRuleResult,
)


# =============================================================================
# 辅助函数
# =============================================================================


def make_runtime_result(**kwargs) -> RuntimeRuleResult:
    """创建测试用 RuntimeRuleResult"""
    defaults = {
        "rule_id": "test_rule_001",
        "matched": True,
        "dimension": "事业",
        "level": "吉",
        "confidence": 0.85,
        "weight": 1.5,
        "execution_time_ms": 2.0,
    }
    defaults.update(kwargs)
    return RuntimeRuleResult(**defaults)


# =============================================================================
# NarrativeConfig 测试
# =============================================================================


class TestNarrativeConfig:
    """NarrativeConfig 模型测试"""

    def test_valid_config(self):
        """测试有效的叙事配置"""
        config = NarrativeConfig(
            config_id="bazi_career_friendly",
            target_rule_patterns=["bazi_career_*"],
            tone="friendly",
            audience_level="intermediate",
        )
        assert config.config_id == "bazi_career_friendly"
        assert config.tone == "friendly"
        assert config.locale == "zh-CN"  # 默认值

    def test_all_tones(self):
        """测试所有叙事风格"""
        tones = ["professional", "friendly", "mystical", "scientific"]
        for tone in tones:
            config = NarrativeConfig(
                config_id=f"test_{tone}",
                target_rule_patterns=["*"],
                tone=tone,
                audience_level="beginner",
            )
            assert config.tone == tone

    def test_all_audience_levels(self):
        """测试所有受众水平"""
        levels = ["beginner", "intermediate", "advanced"]
        for level in levels:
            config = NarrativeConfig(
                config_id=f"test_{level}",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level=level,
            )
            assert config.audience_level == level

    def test_all_channels(self):
        """测试所有渠道"""
        channels = ["app", "web", "miniapp", "api"]
        for channel in channels:
            config = NarrativeConfig(
                config_id=f"test_{channel}",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                channel=channel,
            )
            assert config.channel == channel

    def test_all_risk_levels(self):
        """测试所有风险提示级别"""
        levels = ["none", "brief", "detailed"]
        for level in levels:
            config = NarrativeConfig(
                config_id=f"test_{level}",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                risk_disclosure=level,
            )
            assert config.risk_disclosure == level

    def test_all_evidence_levels(self):
        """测试所有证据详细程度"""
        levels = ["simple", "detailed", "full"]
        for level in levels:
            config = NarrativeConfig(
                config_id=f"test_{level}",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                evidence_detail_level=level,
            )
            assert config.evidence_detail_level == level

    def test_invalid_config_id_pattern(self):
        """测试无效的 config_id 格式"""
        with pytest.raises(ValidationError):
            NarrativeConfig(
                config_id="Invalid-Config",  # 不能大写开头或包含连字符
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
            )

    def test_invalid_locale_pattern(self):
        """测试无效的地区代码格式"""
        with pytest.raises(ValidationError):
            NarrativeConfig(
                config_id="test_config",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                locale="invalid",  # 应该是 xx-XX 格式
            )

    def test_valid_locale_formats(self):
        """测试有效的地区代码"""
        locales = ["zh-CN", "en-US", "ja-JP", "ko-KR"]
        for locale in locales:
            config = NarrativeConfig(
                config_id="test_locale",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                locale=locale,
            )
            assert config.locale == locale

    def test_length_bounds(self):
        """测试长度边界"""
        # 有效边界
        config = NarrativeConfig(
            config_id="test_length",
            target_rule_patterns=["*"],
            tone="friendly",
            audience_level="beginner",
            min_length=10,
            max_length=2000,
        )
        assert config.min_length == 10
        assert config.max_length == 2000

        # min_length 下限
        with pytest.raises(ValidationError):
            NarrativeConfig(
                config_id="test_min",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                min_length=5,  # 低于 10
            )

        # max_length 上限
        with pytest.raises(ValidationError):
            NarrativeConfig(
                config_id="test_max",
                target_rule_patterns=["*"],
                tone="friendly",
                audience_level="beginner",
                max_length=3000,  # 高于 2000
            )

    def test_prompt_templates(self):
        """测试 Prompt 模板"""
        config = NarrativeConfig(
            config_id="test_templates",
            target_rule_patterns=["*"],
            tone="friendly",
            audience_level="beginner",
            prompt_templates={
                "opening": "让我们探讨...",
                "evidence": "根据数据...",
                "conclusion": "综合来看...",
            },
        )
        assert "opening" in config.prompt_templates
        assert len(config.prompt_templates) == 3


# =============================================================================
# ConflictWarning 测试
# =============================================================================


class TestConflictWarning:
    """ConflictWarning 模型测试"""

    def test_valid_warning(self):
        """测试有效的冲突警告"""
        warning = ConflictWarning(
            group="body_strength_group",
            conflicting_rules=["rule_strong_001", "rule_weak_001"],
            severity="MEDIUM",
            resolution_strategy="priority_based",
        )
        assert warning.group == "body_strength_group"
        assert len(warning.conflicting_rules) == 2
        assert warning.severity == "MEDIUM"

    def test_all_severities(self):
        """测试所有严重程度"""
        severities = ["LOW", "MEDIUM", "HIGH"]
        for sev in severities:
            warning = ConflictWarning(
                group="test_group",
                conflicting_rules=["rule_a", "rule_b"],
                severity=sev,
                resolution_strategy="test",
            )
            assert warning.severity == sev

    def test_invalid_severity(self):
        """测试无效的严重程度"""
        with pytest.raises(ValidationError):
            ConflictWarning(
                group="test_group",
                conflicting_rules=["rule_a"],
                severity="CRITICAL",  # 不支持
                resolution_strategy="test",
            )


# =============================================================================
# FusionResult 测试
# =============================================================================


class TestFusionResult:
    """FusionResult 模型测试"""

    def test_valid_fusion(self):
        """测试有效的融合结果"""
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["事业突破", "财富积累"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85, "健康": 0.72},
            cross_validation_score=0.87,
            contributing_engines=["bazi_rule_engine"],
            fusion_time_ms=45.2,
        )
        assert result.fusion_id == "fus_abc123456789"
        assert len(result.primary_themes) == 2
        assert len(result.evidence_chain) == 1

    def test_invalid_fusion_id_pattern(self):
        """测试无效的 fusion_id 格式"""
        with pytest.raises(ValidationError):
            FusionResult(
                fusion_id="invalid_id",  # 应该是 fus_xxxxxxxxxxxx 格式
                primary_themes=["主题"],
                evidence_chain=[make_runtime_result()],
                confidence_matrix={"事业": 0.85},
                cross_validation_score=0.87,
                fusion_time_ms=1.0,
            )

    def test_valid_fusion_id_formats(self):
        """测试有效的 fusion_id 格式"""
        valid_ids = ["fus_abc123456789", "fus_000000000000", "fus_abcdefghij12"]
        for fid in valid_ids:
            result = FusionResult(
                fusion_id=fid,
                primary_themes=["主题"],
                evidence_chain=[make_runtime_result()],
                confidence_matrix={"事业": 0.85},
                cross_validation_score=0.87,
                fusion_time_ms=1.0,
            )
            assert result.fusion_id == fid

    def test_primary_themes_bounds(self):
        """测试 primary_themes 数量边界"""
        # 最少 1 个
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["单一主题"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=0.87,
            fusion_time_ms=1.0,
        )
        assert len(result.primary_themes) == 1

        # 最多 5 个
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["主题1", "主题2", "主题3", "主题4", "主题5"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=0.87,
            fusion_time_ms=1.0,
        )
        assert len(result.primary_themes) == 5

        # 超过 5 个应该失败
        with pytest.raises(ValidationError):
            FusionResult(
                fusion_id="fus_abc123456789",
                primary_themes=["1", "2", "3", "4", "5", "6"],  # 6 个
                evidence_chain=[make_runtime_result()],
                confidence_matrix={"事业": 0.85},
                cross_validation_score=0.87,
                fusion_time_ms=1.0,
            )

        # 0 个应该失败
        with pytest.raises(ValidationError):
            FusionResult(
                fusion_id="fus_abc123456789",
                primary_themes=[],  # 空列表
                evidence_chain=[make_runtime_result()],
                confidence_matrix={"事业": 0.85},
                cross_validation_score=0.87,
                fusion_time_ms=1.0,
            )

    def test_evidence_chain_bounds(self):
        """测试 evidence_chain 数量边界"""
        # 最少 1 个
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["主题"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=0.87,
            fusion_time_ms=1.0,
        )
        assert len(result.evidence_chain) == 1

        # 0 个应该失败
        with pytest.raises(ValidationError):
            FusionResult(
                fusion_id="fus_abc123456789",
                primary_themes=["主题"],
                evidence_chain=[],  # 空列表
                confidence_matrix={"事业": 0.85},
                cross_validation_score=0.87,
                fusion_time_ms=1.0,
            )

        # 超过 20 个应该失败
        with pytest.raises(ValidationError):
            FusionResult(
                fusion_id="fus_abc123456789",
                primary_themes=["主题"],
                evidence_chain=[make_runtime_result(rule_id=f"rule_{i}") for i in range(21)],
                confidence_matrix={"事业": 0.85},
                cross_validation_score=0.87,
                fusion_time_ms=1.0,
            )

    def test_cross_validation_score_bounds(self):
        """测试交叉验证分数边界"""
        # 有效边界
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["主题"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=0.0,
            fusion_time_ms=1.0,
        )
        assert result.cross_validation_score == 0.0

        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["主题"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=1.0,
            fusion_time_ms=1.0,
        )
        assert result.cross_validation_score == 1.0

        # 超出边界
        with pytest.raises(ValidationError):
            FusionResult(
                fusion_id="fus_abc123456789",
                primary_themes=["主题"],
                evidence_chain=[make_runtime_result()],
                confidence_matrix={"事业": 0.85},
                cross_validation_score=1.5,
                fusion_time_ms=1.0,
            )

    def test_with_conflicts(self):
        """测试包含冲突的融合结果"""
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["主题"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=0.6,
            conflicts=[
                ConflictWarning(
                    group="strength_group",
                    conflicting_rules=["rule_a", "rule_b"],
                    severity="MEDIUM",
                    resolution_strategy="priority_based",
                )
            ],
            fusion_time_ms=1.0,
        )
        assert len(result.conflicts) == 1
        assert result.conflicts[0].severity == "MEDIUM"

    def test_timestamp_default(self):
        """测试时间戳默认值"""
        before = datetime.now()
        result = FusionResult(
            fusion_id="fus_abc123456789",
            primary_themes=["主题"],
            evidence_chain=[make_runtime_result()],
            confidence_matrix={"事业": 0.85},
            cross_validation_score=0.87,
            fusion_time_ms=1.0,
        )
        after = datetime.now()
        
        assert before <= result.created_at <= after
