"""
Pytest Configuration for Semantic Core Tests

Hypothesis 配置: max_examples=100
"""

import pytest
from hypothesis import settings, Verbosity

# Hypothesis 全局配置
settings.register_profile(
    "ci",
    max_examples=100,
    verbosity=Verbosity.normal,
    deadline=None,  # 禁用超时（某些测试可能较慢）
)
settings.register_profile(
    "dev",
    max_examples=20,
    verbosity=Verbosity.verbose,
    deadline=None,
)
settings.register_profile(
    "debug",
    max_examples=5,
    verbosity=Verbosity.verbose,
    deadline=None,
)

# 默认使用 ci profile
settings.load_profile("ci")


@pytest.fixture(autouse=True)
def reset_registry():
    """每个测试前后重置 SemanticRegistry"""
    from backend.semantics.core.base import SemanticRegistry
    
    # 测试前重置
    SemanticRegistry.reset()
    
    yield
    
    # 测试后重置
    SemanticRegistry.reset()


@pytest.fixture
def sample_source_metadata():
    """提供样例 SourceMetadata"""
    from backend.core.contracts import SourceMetadata
    
    return SourceMetadata(
        book_id="ditianshui",
        chapter="通神论",
        l1_anchor="DTS_L1_001",
    )


@pytest.fixture
def sample_narrative_snippet(sample_source_metadata):
    """提供样例 NarrativeSnippetExtended"""
    from backend.semantics.core.base import NarrativeSnippetExtended
    from backend.core.contracts import SnippetRole
    
    return NarrativeSnippetExtended(
        snippet_id="dts_jia_001",
        trigger_condition="day_master_jia AND season_spring",
        trigger_human="日主甲木且春季",
        role=SnippetRole.MAIN,
        primary_lang="zh-CN",
        snippet_text="甲木生于春，得时得令，如参天大树。",
        source_ref="《滴天髓》#通神论#L23",
        metadata=sample_source_metadata,
        related_factors=["day_master_jia", "season_spring"],
        related_rules=[],
        version="1.0.0",
        engine_id="bazi",
    )


@pytest.fixture
def sample_semantic_entry(sample_source_metadata, sample_narrative_snippet):
    """提供样例 SemanticEntry"""
    from backend.semantics.core.base import SemanticEntry
    
    return SemanticEntry(
        semantic_id="dts_v2_jia_spring_001",
        book_id="ditianshui",
        engine_id="bazi",
        original_text="甲木参天，脱胎要火",
        normalized_text_zh="甲木如参天大树，刚健向上，需要火来泄秀发挥。",
        subject="甲木特性",
        factor_refs=["day_master_jia", "element_fire"],
        narrative_snippets=[sample_narrative_snippet],
        metadata=sample_source_metadata,
        version="1.0.0",
    )
