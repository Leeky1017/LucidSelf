"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076512
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
    semantic_id="bot_v1.0.0_eight_of_swords__interference__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class EightOfSwordsInterference(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hod in Air | Intellect in Air | Lack of persistence |
| Jupiter in Gemini | Scattered benefic | Accidental help |
| Two Long Swords | Main intentions | Blocked |
| Six Exotic Blades | Foreign forces | Crossing interference |

**Title**: Lord of Shortened Force (缩短之力之主)
**Qabalistic**: Hod in Air (气中之荣光)
**Astrological**: Jupiter in Gemini (木星入双子座)

**Source Text**:
> "The number Eight, Hod, here signifies lack of persistence in matters of the intellect and of contest. Good fortune, however, attends even these weakened efforts, thanks to the influence of Jupiter in Gemini, ruling the Decan. Yet the Will is constantly thwarted by accidental interference. The centre of the card is occupied by two long Swords pointed downward. These are crossed by six small swords, three on each side. They remind one of weapons peculiar to their countries or their cults; we see here the Kriss, the Kukri, the Scramasax, the Dagger, the Machete and the Yataghan."

**English Paraphrase**:
**Interrupted Will** – Hod (Mercury/Intellect) in Air shows **lack of persistence**. **Jupiter in Gemini** brings some good fortune despite weakness, but **Will is constantly thwarted by accidental interference**. Two long swords point downward, crossed by six exotic blades (Kriss, Kukri, etc.)—**main intention cut across by foreign forces**. This is **Interference**: partial success continually interrupted.

**Core**: **Shortened Force** – Interference, lack of persistence, will thwarted by accidents.

**Chinese Explanation**:
**宝剑八（干扰）**对应气元素中的**Hod（水星/智性）**，显示**缺乏持久性**。**木星入双子座**带来一些好运，但**意志不断被意外干扰挫败**。两把长剑向下指，被六把异国短剑（马来短剑、廓尔喀弯刀等）交叉——**主要意图被外来力量切断**。这是**干扰**：部分成功不断被打断。

**In Readings**: Interference, shortened efforts, will thwarted by accidents, partial success interrupted, external obstacles.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Eight of Swords shows Hod's lack of persistence. Jupiter in Gemini offers some luck. Two long swords crossed by six exotic blades. Will thwarted by accidental interference.
- **中文**: Crowley的宝剑八展示Hod的缺乏持久性。木星入双子提供一些运气。两长剑被六异形短剑交叉。意志被意外干扰挫败。

**Narrative Snippets**:
- `[ns_thoth_swords_022]` `[trigger: eight_swords_interference]` `[factor_trigger: thoth_swords_eight]` `[role: 主干]` Eight of Swords = Lord of Shortened Force—Hod; lack of persistence; will constantly thwarted. → Core
- `[ns_thoth_swords_023]` `[trigger: jupiter_gemini_scattered]` `[factor_trigger: thoth_swords_eight AND planet_jupiter_gemini]` `[role: 条件分支]` Jupiter in Gemini—good fortune despite weakness; scattered benefic; some accidental help. → Astrological
- `[ns_thoth_swords_024]` `[trigger: exotic_blades_cross]` `[factor_trigger: thoth_swords_eight AND symbol_exotic_blades]` `[role: 条件分支]` Two long swords crossed by six exotic blades (Kriss, Kukri, etc.)—foreign forces interfere. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Swords: Interference (宝剑八：干扰)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_eight_001', 'tarot_shortened_force', 'rel_swords_eight_002', 'tarot_will_thwarted', 'l1_anchor', 'confidence', 'evi_swords_eight_001', 'evi_swords_eight_002', 'tarot_six_exotic_blades', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_eight_001', 'tarot_swords_eight', 'astro_jupiter_gemini']
    
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
        l1_anchor="bot_v1.0.0_eight_of_swords__interference__001_L1",
    )
    version: str = "1.0.0"
