"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088860
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
    semantic_id="bot_v1.0.0_seven_of_wands__valour__权杖七_勇气_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SevenOfWandsValour权杖七勇气(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Netzach in Fire | Victory in Fire | Departing balance |
| Mars in Leo | Aggression + pride | Brutal support |
| Soldiers' Battle | Individual combat | No central command |
| Crude Club | Improvised weapon | Last resort |

**Title**: Lord of Valour (勇气之主)
**Qabalistic**: Netzach in Fire (火中之胜利/情感)
**Astrological**: Mars in Leo (火星入狮子座)

**Source Text**:
> "This card derives from Netzach (Victory) in the suit of Fire. But the Seven is a weak, earthy, feminine number... departure from the balance... loss of confidence. Fortunately, the card is also attributed to Mars in Leo. ... The wavering fire summoned the brutal energy of Mars to its support. ... The army has been thrown into disorder; if victory is to be won, it will be by dint of individual valour-a 'soldiers' battle'."

**English Paraphrase**:
**Desperate Courage** - Corresponds to Netzach (Victory) in Fire, but the number Seven (earthy/feminine) implies a **departure from balance** and loss of confidence. Ruled by **Mars in Leo**: The wavering fire summons the **brutal energy of Mars** to survive. It depicts an army in disorder; victory is no longer strategic but depends on **individual valour** (a "soldiers' battle"). The main wand is a crude club, representing the last resort. It is the fight against overwhelming odds.

**Core**: **Individual Struggle** - Fighting against the odds, courage in desperation, last stand, chaotic energy requiring personal bravery.

**Chinese Explanation**:
**权杖七（勇气）**对应火元素中的Netzach（胜利/情感）。但数字7（土相/阴性）在生命之树上较低，暗示**偏离平衡**和失去信心。对应**火星在狮子座**：摇摆不定的火焰召唤火星的**残暴能量**来支撑自己。这像是一支陷入混乱的军队；如果要获胜，只能靠**个人的勇气**（"士兵的战役"）。前方是一根粗糙的大棒（权杖），是手头的最后武器。象征在绝境中的挣扎和背水一战。

**In Readings**: Courage against odds, struggle, fighting back, precarious position, individual effort needed, disorder.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Seven of Wands shows departure from Six's balance. Mars in Leo provides brutal energy to wavering fire. "Soldiers' battle" requires individual valour when command fails. Crude club is last-resort weapon.
- **中文**: Crowley的权杖七展示偏离六的平衡。火星入狮子为摇摆的火提供残暴能量。"士兵战役"在指挥失败时需要个人勇气。粗糙棍棒是最后武器。

**Narrative Snippets**:
- `[ns_thoth_wands_019]` `[trigger: seven_wands_valour]` `[factor_trigger: thoth_wands_seven]` `[role: 主干]` Seven of Wands = Lord of Valour—Netzach in Fire; departure from balance; loss of confidence. → Core
- `[ns_thoth_wands_020]` `[trigger: mars_leo_brutal]` `[factor_trigger: thoth_wands_seven AND planet_mars_leo]` `[role: 条件分支]` Mars in Leo—wavering fire summons brutal energy; "soldiers' battle" without command. → Astrological
- `[ns_thoth_wands_021]` `[trigger: crude_club]` `[factor_trigger: thoth_wands_seven AND symbol_club]` `[role: 条件分支]` Crude club as main weapon—last resort; army in disorder; individual valour required. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Wands: Valour (权杖七：勇气)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_7_courage', 'valour', 'rel_wands_7_mars', 'planet_mars_leo', 'wands_7_valour']
    
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
        l1_anchor="bot_v1.0.0_seven_of_wands__valour__权杖七_勇气_001_L1",
    )
    version: str = "1.0.0"
