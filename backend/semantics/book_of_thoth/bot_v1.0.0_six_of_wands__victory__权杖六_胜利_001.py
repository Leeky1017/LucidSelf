"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088845
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
    semantic_id="bot_v1.0.0_six_of_wands__victory__权杖六_胜利_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SixOfWandsVictory权杖六胜利(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tiphareth in Fire | Beauty in Fire | Balanced success |
| Jupiter in Leo | Expansion + pride | Royal triumph |
| Phoenix Wands | Rebirth symbols | Transformation |
| Balanced Energy | Harmony achieved | Stable victory |

**Title**: Lord of Victory (胜利之主)
**Qabalistic**: Tiphareth in Fire (火中之美)
**Astrological**: Jupiter in Leo (木星入狮子座)

**Source Text**:
> "This card represents Tiphareth of the suit of Fire. This shows Energy in completely balanced manifestation. The Five has broken up the closed forces of the Four... and the result is the Son, and the Sun. The reference is also to Jupiter and Leo... benediction on the harmony and beauty of this arrangement. ... The flames themselves... burn steadily as in lamps."

**English Paraphrase**:
**Balanced Manifestation** - Corresponds to Tiphareth (Beauty/Balance) in Fire. Energy is **completely balanced**. The revolutionary strife of the Five has broken the stagnation of the Four, resulting in a marriage and the birth of the **Son/Sun**. Ruled by **Jupiter in Leo**, signifying a benediction of harmony and expansion. The wands are orderly, and the flames burn steadily like lamps (not explosive). It is the **stabilization of energy**, self-supporting like the Sun.

**Core**: **Triumph and Harmony** - Success after struggle, recognition, balanced leadership, self-confidence, steady burning energy.

**Chinese Explanation**:
**权杖六（胜利）**对应火元素中的Tiphareth（美/平衡）。这是能量的**完全平衡显化**。五号牌打破了四号牌的封闭力量，通过"革命热情"，两者结合诞生了**圣子/太阳**。对应**木星在狮子座**，象征对这种和谐与美丽的祝福。权杖排列有序，火焰像灯一样**稳定燃烧**（而非四散）。这代表能量的稳定化，像太阳一样自我支撑。

**In Readings**: Victory, success, pride, leadership, stability, achievement, confident energy, public recognition.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Six of Wands shows energy achieving complete balance after Five's strife. Jupiter in Leo brings royal benediction. Flames burn steadily like lamps, not explosive. Son/Sun born from Father-Mother union.
- **中文**: Crowley的权杖六展示能量在五的冲突后达到完全平衡。木星入狮子带来王者祝福。火焰像灯一样稳定燃烧而非爆发。子/太阳从父母结合中诞生。

**Narrative Snippets**:
- `[ns_thoth_wands_016]` `[trigger: six_wands_victory]` `[factor_trigger: thoth_wands_six]` `[role: 主干]` Six of Wands = Lord of Victory—Tiphareth in Fire; energy completely balanced after Five's strife. → Core
- `[ns_thoth_wands_017]` `[trigger: jupiter_leo_royal]` `[factor_trigger: thoth_wands_six AND planet_jupiter_leo]` `[role: 条件分支]` Jupiter in Leo—royal benediction on harmony; flames burn steadily like lamps. → Astrological
- `[ns_thoth_wands_018]` `[trigger: son_sun_synthesis]` `[factor_trigger: thoth_wands_six AND symbol_sun]` `[role: 条件分支]` Son and Sun born from Father-Mother union—self-supporting energy; stable triumph. → Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Six of Wands: Victory (权杖六：胜利)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_six_001', 'tarot_balanced_energy', 'rel_wands_six_002', 'tarot_self_supporting', 'l1_anchor', 'confidence', 'evi_wands_six_001', 'evi_wands_six_002', 'tarot_balanced_energy', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_six_001', 'tarot_wands_six', 'astro_jupiter_leo']
    
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
        l1_anchor="bot_v1.0.0_six_of_wands__victory__权杖六_胜利_001_L1",
    )
    version: str = "1.0.0"
