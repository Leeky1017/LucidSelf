"""
Pytest Configuration for Integration Tests

共享 fixtures 和测试配置。
"""

import pytest
from datetime import datetime
from typing import List

from backend.core.contracts import RuntimeRuleResult
from backend.integration import (
    WeightManager,
    CrossValidator,
    ThemeMapper,
    EvidenceChainBuilder,
    FusionEngine,
)


@pytest.fixture
def sample_rule_result() -> RuntimeRuleResult:
    """创建示例规则结果"""
    return RuntimeRuleResult(
        rule_id="bazi_career_001",
        matched=True,
        dimension="career",
        level="吉",
        description="事业运势良好",
        confidence=0.85,
        weight=1.5,
        tags=["事业", "官印"],
        evidence_factors=["day_master", "official_star"],
        semantic_refs=["bazi_v2_zhengguan_001"],
        source_book="子平真诠",
        l1_anchor="官印相生章",
        execution_time_ms=1.2,
    )


@pytest.fixture
def sample_results_multi_engine(sample_rule_result) -> dict:
    """创建多引擎示例结果"""
    return {
        "bazi-calculator": [
            sample_rule_result,
            RuntimeRuleResult(
                rule_id="bazi_wealth_001",
                matched=True,
                dimension="wealth",
                level="大吉",
                description="财运亨通",
                confidence=0.9,
                weight=1.8,
                tags=["财富"],
                evidence_factors=["wealth_star"],
                execution_time_ms=0.8,
            ),
        ],
        "astro-calculator": [
            RuntimeRuleResult(
                rule_id="astro_career_001",
                matched=True,
                dimension="career",
                level="吉",
                description="事业有贵人相助",
                confidence=0.75,
                weight=1.2,
                tags=["事业", "贵人"],
                evidence_factors=["sun_position"],
                source_book="Tetrabiblos",
                execution_time_ms=1.5,
            ),
        ],
        "tarot-interpreter": [
            RuntimeRuleResult(
                rule_id="tarot_fortune_001",
                matched=True,
                dimension="fortune",
                level="中等",
                description="整体运势平稳",
                confidence=0.7,
                weight=1.0,
                tags=["运势"],
                evidence_factors=["major_arcana"],
                execution_time_ms=0.5,
            ),
        ],
    }


@pytest.fixture
def weight_manager() -> WeightManager:
    """创建权重管理器"""
    return WeightManager()


@pytest.fixture
def cross_validator() -> CrossValidator:
    """创建交叉验证器"""
    return CrossValidator()


@pytest.fixture
def theme_mapper() -> ThemeMapper:
    """创建主题映射器"""
    return ThemeMapper()


@pytest.fixture
def evidence_builder() -> EvidenceChainBuilder:
    """创建证据链构建器"""
    return EvidenceChainBuilder()


@pytest.fixture
def fusion_engine() -> FusionEngine:
    """创建融合引擎"""
    return FusionEngine()
