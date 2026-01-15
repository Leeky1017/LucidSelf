"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301108
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="pit_v1.0.0_moon_in_the_twelfth_house__月亮过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheTwelfthHouse月亮过(SemanticEntry):
    """
    **Source Text** (Lines 3785-3803):
> May be tempted to withdraw and keep feelings secret, especially...
    """
    
    original_text: str = """**Source Text** (Lines 3785-3803):
> May be tempted to withdraw and keep feelings secret, especially if insecure about inner self. If you feel others wouldn't like the "real" you, you keep emotional life secret. This causes problems—whatever you hide from others, you hide from yourself. What you hide from yourself can control you. Unconscious attitudes and fears can be very difficult now. You need to communicate deep inner feelings to someone you trust. Probably won't feel like socializing—good time to be alone and face aspects of yourself you're reluctant to face. Excellent time for mystical or spiritual discipline.

**English Paraphrase**: May withdraw, keep feelings secret if insecure. If you hide from others, you hide from yourself—what's hidden controls you. Unconscious attitudes and fears difficult now. Need to communicate to someone trusted. Won't feel like socializing—good for facing self alone. Excellent for spiritual discipline.

**Complete Chinese Interpretation**: 如果不安全感可能退缩、保守感受秘密。如果对他人隐藏，你对自己也隐藏——隐藏的东西控制你。无意识态度和恐惧现在困难。需要向信任的人沟通。不会想社交——适合独自面对自己。对精神修行极好。

**Narrative Snippets**:
- `[ns_pit_m023]` `[trigger: moon_transit_house_12]` `[factor_trigger: astro_transit_moon AND astro_house_12]` `[role: 主干]` May withdraw and keep feelings secret—but what you hide from others, you hide from yourself. → PIT Ch5 Moon-12H
- `[ns_pit_m024]` `[trigger: moon_transit_house_12]` `[factor_trigger: astro_transit_moon AND astro_house_12]` `[role: 总结]` Good time to face aspects of self you're reluctant to face. Excellent for spiritual discipline. → PIT Ch5 Moon-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Twelfth House (月亮过境第十二宫)"
    factor_refs: list = ['state_emotional_withdrawal', 'pattern_hidden_control', 'practice_spiritual_discipline']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_moon_in_the_twelfth_house__月亮过_001_L1",
    )
    version: str = "1.0.0"
