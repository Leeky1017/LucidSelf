"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206568
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
    semantic_id="pit_v1.0.0_uranus_in_the_second_house__天王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheSecondHouse天王(SemanticEntry):
    """
    **Source Text** (Lines 14443-14483):
> Great changes in economic and material situation. Finances mu...
    """
    
    original_text: str = """**Source Text** (Lines 14443-14483):
> Great changes in economic and material situation. Finances must withstand sudden changes. Be extremely flexible with money and possessions. Inner level: values are changing, reflected in possessions. Inner needs for growth make current relationship to possessions inappropriate. Conscious awareness avoids upset; unconscious creates upsetting events. If feel encumbered by possessions, transit will take them away until free. Can signal sudden windfalls or sudden losses. May radically change means of earning, or make living through Uranian profession (science, technology, astrology, occult). Ultimate effects positive though initially upsetting.

**English Paraphrase**: Sudden financial/material changes. Be flexible. Values changing. If encumbered, possessions may be removed. Sudden gains or losses. May change livelihood. Uranian professions favored. Ultimately positive.

**Complete Chinese Interpretation**: 突然的财务/物质变化。要灵活。价值观在改变。如果感到负担，财产可能被移除。突然的得失。可能改变生计。天王星职业受青睐。最终是积极的。

**Narrative Snippets**:
- `[ns_pit_ur002]` `[trigger: uranus_transit_house_2]` `[factor_trigger: astro_transit_uranus AND astro_house_2]` `[role: 主干]` Sudden financial changes. Values changing. Sudden gains or losses. Uranian professions. → PIT Ch11 Uranus-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Second House (天王星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_second_house__天王_001_L1",
    )
    version: str = "1.0.0"
