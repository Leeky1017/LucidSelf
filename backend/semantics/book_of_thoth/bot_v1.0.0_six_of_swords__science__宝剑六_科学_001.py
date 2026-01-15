"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076476
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
    semantic_id="bot_v1.0.0_six_of_swords__science__宝剑六_科学_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SixOfSwordsScience宝剑六科学(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tiphareth in Air | Beauty in Air | Harmonized intellect |
| Mercury in Aquarius | Clear detached mind | Humane intelligence |
| Rosy Cross | Rose + golden cross | Scientific truth secret |
| Hexagram Hilts | Six-pointed star | Balanced faculties |

**Title**: Lord of Earned Success (得自努力之成功之主)
**Qabalistic**: Tiphareth in Air (气中之美)
**Astrological**: Mercury in Aquarius (水星入宝瓶座)

**Source Text**:
> "Tiphareth shows the full establishment and balance of the idea of the suit. This is particularly the case with this card, as the intellect itself is also referred to the number Six. Mercury, in Aquarius, represents the celestial Energy influencing the Kerub of the Man, thus showing intelligence and humanity. ... The perfect balance of all mental and moral faculties, hardly won, and almost impossible to hold in an ever-changing world, declares the idea of Science in its fullest interpretation. ... The hilts of the Swords... are in the form of the hexagram. Their points touch the outer petals of a red rose upon a golden cross of six squares, thus showing the Rosy Cross as the central secret of scientific truth."

**English Paraphrase**:
**Balanced Reason** – Corresponds to Tiphareth (Beauty/Harmony) in Air. **Mercury in Aquarius** gives clear, detached, humane intelligence. This card shows the **hard‑won balance of all mental and moral faculties**, expressed as **Science**: disciplined inquiry into truth. Six swords with hexagram hilts touch petals of a red rose on golden cross – the **Rosy Cross** as secret of scientific truth.

**Core**: **Scientific Truth** – Balanced intellect, earned success, disciplined inquiry, but hard to maintain.

**Chinese Explanation**:
**宝剑六（科学）**对应气元素中的**Tiphareth（美/和谐）**，也对应数字六作为智性之球。**水星入宝瓶座**带来清明、超然、人道的智慧。这张牌展示了**所有心智与道德能力的艰难平衡**，表达为最高意义的**科学**：对真理的训练有素之探究。六把装饰精美的剑有六芒星形剑柄；剑尖触及金色十字架上红玫瑰的花瓣——**玫瑰十字**作为科学真理的核心秘密：智性、心灵与灵性意志的结合。

**In Readings**: Earned success through intellectual effort, scientific approach, balanced judgment, but precarious equilibrium requiring constant vigilance.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Six of Swords shows Tiphareth as full intellectual balance. Mercury in Aquarius brings humane detachment. Hexagram hilts form perfect symmetry. Rosy Cross symbolizes union of reason and spirit. Science as disciplined truth-seeking.
- **中文**: Crowley的宝剑六展示Tiphareth作为完整智性平衡。水星入宝瓶带来人道超然。六芒星剑柄形成完美对称。玫瑰十字象征理性与灵性结合。科学作为训练有素的求真。

**Narrative Snippets**:
- `[ns_thoth_swords_016]` `[trigger: six_swords_science]` `[factor_trigger: thoth_swords_six]` `[role: 主干]` Six of Swords = Lord of Earned Success—Tiphareth; perfect balance of mental/moral faculties = Science. → Core
- `[ns_thoth_swords_017]` `[trigger: mercury_aquarius_clarity]` `[factor_trigger: thoth_swords_six AND planet_mercury_aquarius]` `[role: 条件分支]` Mercury in Aquarius—clear detached humane intelligence; Kerub of Man. → Astrological
- `[ns_thoth_swords_018]` `[trigger: rosy_cross_secret]` `[factor_trigger: thoth_swords_six AND symbol_rosy_cross]` `[role: 条件分支]` Hexagram hilts touch red rose on golden cross—Rosy Cross as central secret of scientific truth. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Six of Swords: Science (宝剑六：科学)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_six_001', 'tarot_balanced_intellect', 'rel_swords_six_002', 'tarot_scientific_truth', 'l1_anchor', 'confidence', 'evi_swords_six_001', 'evi_swords_six_002', 'tarot_rosy_cross', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_six_001', 'tarot_swords_six', 'astro_mercury_aquarius']
    
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
        l1_anchor="bot_v1.0.0_six_of_swords__science__宝剑六_科学_001_L1",
    )
    version: str = "1.0.0"
