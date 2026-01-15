"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027299
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
    semantic_id="bot_v1.0.0_eight_of_cups__indolence__圣杯八__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class EightOfCupsIndolence圣杯八(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hod in Water | Glory in Water | Mercury overwhelmed |
| Saturn in Pisces | Heavy + dissolving | Complete deadening |
| Stagnant Pools | Dead water | No living sea |
| Cracked Cups | Broken vessels | Depleted emotion |

**Title**: Lord of Indolence (懈怠之主)
**Qabalistic**: Hod in Water (水中之荣光)
**Astrological**: Saturn in Pisces (土星入双鱼座)

**Source Text**:
> "The Eight, Hod, in the suit of Water, governs this card. It shows the influence of Mercury, but this is overpowered by the reference of the card to Saturn in Pisces. Pisces is calm but stagnant water; and Saturn deadens it completely. Water appears no longer as the Sea but as pools... The Lotuses droop for lack of sun and rain... The cups are shallow, old and broken... The water is dark and muddy."

**English Paraphrase**:
**Stagnant Withdrawal** - Corresponds to Hod (Intellect/Glory) in Water, but the quickness of Mercury is overwhelmed by **Saturn in Pisces**. The Water element becomes **stagnant pools** rather than a living sea; lotuses droop, the soil is poisonous, and the cups are shallow, old, and cracked. Only a little dark water trickles between a few cups, never filling them. This is **Indolence**: emotional energy has collapsed into apathy, weariness, and drained desire. The mind knows it should move, but Saturn-in-Pisces binds it in swamp-like inaction.

**Core**: **Emotional Exhaustion** - Apathy, weariness, emotional burnout, lack of motivation, walking away because the heart is empty.

**Chinese Explanation**:
**圣杯八（懈怠）**对应水元素中的Hod（荣光/智力），但原本属于水星的机敏之光被**土星入双鱼座**完全压制。水不再是流动的大海，而变成**停滞的水洼**；莲花因缺乏日照与雨水而低垂，土壤本身带有毒性，杯子**浅、旧且破裂**，只有极少量污水在少数杯子之间滴流，却从未真正注满。画面呈现一种**懈怠、疲惫、情感枯竭**的状态——理智知道该行动，但土星-双鱼的沼泽能量把人困在无力和拖延之中。

**In Readings**: Apathy, emotional burnout, lack of interest, stagnation, drifting, walking away from an unfulfilling situation, spiritual fatigue.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Eight of Cups shows Saturn completely deadening Pisces water. Mercury's quickness overwhelmed. Stagnant pools replace living sea. Cups shallow, cracked, unable to hold. Emotional exhaustion state.
- **中文**: Crowley的圣杯八展示土星完全麻痹双鱼之水。水星的敏捷被压制。停滞水洼取代活水之海。杯子浅、裂、无法盛载。情感耗竭状态。

**Narrative Snippets**:
- `[ns_thoth_cups_022]` `[trigger: eight_cups_indolence]` `[factor_trigger: thoth_cups_eight]` `[role: 主干]` Eight of Cups = Lord of Indolence—Hod's Mercury overpowered by Saturn in Pisces; stagnant pools. → Core
- `[ns_thoth_cups_023]` `[trigger: broken_cups]` `[factor_trigger: thoth_cups_eight AND symbol_broken_cups]` `[role: 条件分支]` Cups shallow, old, broken—lotuses droop; dark muddy water trickles but never fills. → Visual
- `[ns_thoth_cups_024]` `[trigger: saturn_deadening]` `[factor_trigger: thoth_cups_eight AND planet_saturn_pisces]` `[role: 条件分支]` Saturn deadens Pisces completely—water no longer sea but pools; collapsed into apathy. → Astrological"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Cups: Indolence (圣杯八：懈怠)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_eight_001', 'tarot_emotional_exhaustion', 'rel_cups_eight_002', 'tarot_apathy', 'l1_anchor', 'confidence', 'evi_cups_eight_001', 'evi_cups_eight_002', 'tarot_broken_cups', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_eight_001', 'tarot_cups_eight', 'astro_saturn_pisces']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_eight_of_cups__indolence__圣杯八__001_L1",
    )
    version: str = "1.0.0"
