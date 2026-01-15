"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027207
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
    semantic_id="bot_v1.0.0_five_of_cups__disappointment___001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FiveOfCupsDisappointment(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Geburah in Water | Severity in Water | Fire-water antipathy |
| Mars in Scorpio | Force in decay | Putrefying power |
| Inverted Pentagram | Matter over spirit | Evil omen |
| Torn Lotuses | Damaged flowers | Frustrated pleasure |

**Title**: Lord of Disappointment (失望之主)
**Qabalistic**: Geburah in Water (水中之严厉)
**Astrological**: Mars in Scorpio (火星入天蝎座)

**Source Text**:
> "This card is ruled by Geburah in the suit of Water. Geburah being fiery, there is a natural antipathy. ... Mars in Scorpio... putrefying power of Water. ... anticipated pleasure is frustrated. The Lotuses have their petals torn by fiery winds; the sea is arid and stagnant... No water flows into the cups. Moreover, these cups are arranged in the form of an inverted pentagram, symbolizing the triumph of matter over spirit."

**English Paraphrase**:
**Frustrated Pleasure** - Corresponds to Geburah (Severity) in Water. The fiery nature of Geburah creates **antipathy** with Water. Ruled by **Mars in Scorpio**. While powerful, Scorpio here suggests the **putrefying power** of Water. Anticipated pleasure is frustrated. The lotus petals are torn by fiery winds, the sea is stagnant (like a "chott"), and no water flows. The cups form an **inverted pentagram**, symbolizing the **triumph of matter over spirit**. It is disturbance in a time of ease.

**Core**: **Emotional Loss** - Disappointment, loss, regret, bitterness, stagnant emotion, dried up feelings, betrayal, matter over spirit.

**Chinese Explanation**:
**圣杯五（失望）**对应水元素中的Geburah（严厉）。火性的Geburah与水存在天然**反感**。对应**火星在天蝎座**，暗示水的**腐败力量**。预期的快乐受挫。莲花瓣被火风撕裂，海水干涸停滞（死海）。没有水流入杯中。杯子排列成**倒五芒星**，象征**物质战胜了灵性**。这是安逸时期的突然扰动，代表失望、痛苦和情感的干涸。

**In Readings**: Disappointment, regret, loss, frustration, bitterness, betrayal, emotional dryness, "crying over spilt milk".

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Five of Cups shows Geburah's fire creating antipathy with Water. Mars in Scorpio brings putrefying power. Inverted pentagram symbolizes matter triumphing over spirit. Lotuses torn, sea stagnant.
- **中文**: Crowley的圣杯五展示Geburah的火与水创造反感。火星入天蝎带来腐败力量。倒五芒星象征物质战胜精神。莲花被撕裂，海水停滞。

**Narrative Snippets**:
- `[ns_thoth_cups_013]` `[trigger: five_cups_disappointment]` `[factor_trigger: thoth_cups_five]` `[role: 主干]` Five of Cups = Lord of Disappointment—Geburah fire antipathy with Water; Mars in Scorpio putrefying. → Core
- `[ns_thoth_cups_014]` `[trigger: inverted_pentagram]` `[factor_trigger: thoth_cups_five AND symbol_pentagram]` `[role: 条件分支]` Cups form inverted pentagram—matter triumphs over spirit; anticipated pleasure frustrated. → Symbolism
- `[ns_thoth_cups_015]` `[trigger: torn_lotuses]` `[factor_trigger: thoth_cups_five AND symbol_torn_lotus]` `[role: 条件分支]` Lotuses torn by fiery winds, sea arid stagnant—no water flows; disturbance in ease. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Five of Cups: Disappointment (圣杯五：失望)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_five_001', 'tarot_frustrated_pleasure', 'rel_cups_five_002', 'tarot_spirit_defeat', 'l1_anchor', 'confidence', 'evi_cups_five_001', 'evi_cups_five_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_five_001', 'tarot_cups_five', 'astro_mars_scorpio']
    
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
        l1_anchor="bot_v1.0.0_five_of_cups__disappointment___001_L1",
    )
    version: str = "1.0.0"
