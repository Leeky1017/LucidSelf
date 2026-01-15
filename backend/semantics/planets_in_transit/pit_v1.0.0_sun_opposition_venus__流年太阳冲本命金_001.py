"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224364
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
    semantic_id="pit_v1.0.0_sun_opposition_venus__流年太阳冲本命金_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionVenus流年太阳冲本命金(SemanticEntry):
    """
    **Source Text** (Lines 2513-2536):
> Brings all relationships into focus. Usually easy and pleasant,...
    """
    
    original_text: str = """**Source Text** (Lines 2513-2536):
> Brings all relationships into focus. Usually easy and pleasant, but can release hidden tensions in relationships. You encounter yourself through different relationships—good ones remain good, bad ones become unstable. You don't want to be alone; cannot operate without close relationship. Good day to talk to counselor. This transit is about consciousness—awareness of relationship. Makes you aware how much you need loved ones.

**English Paraphrase**: Relationships in focus. Usually pleasant but can release hidden tensions. Encounter self through relationships—good stay good, bad become unstable. Don't want to be alone; need close relationship. Good for counseling. About relationship consciousness. Aware how much you need loved ones.

**Complete Chinese Interpretation**: 关系成为焦点。通常愉快但可能释放隐藏的紧张。通过关系遇见自己——好的保持好，坏的变得不稳定。不想独处；需要亲密关系。适合咨询。关于关系意识。意识到你多么需要所爱之人。

**Narrative Snippets**:
- `[ns_pit_080]` `[trigger: transit_sun_opposition_natal_venus]` `[factor_trigger: astro_transit_sun OPPOSITION natal_venus]` `[role: 主干]` All relationships in focus—usually pleasant but can release hidden tensions. Encounter self through relationships. → PIT Ch4 Sun☍Venus
- `[ns_pit_081]` `[trigger: transit_sun_opposition_natal_venus]` `[factor_trigger: astro_transit_sun OPPOSITION natal_venus]` `[role: 总结]` This transit is about relationship consciousness—awareness of how much you need loved ones. → PIT Ch4 Sun☍Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Venus (流年太阳冲本命金星)"
    factor_refs: list = []
    
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
        l1_anchor="pit_v1.0.0_sun_opposition_venus__流年太阳冲本命金_001_L1",
    )
    version: str = "1.0.0"
