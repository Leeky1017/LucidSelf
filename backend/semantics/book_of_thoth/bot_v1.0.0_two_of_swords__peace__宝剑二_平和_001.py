"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076399
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
    semantic_id="bot_v1.0.0_two_of_swords__peace__宝剑二_平和_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TwoOfSwordsPeace宝剑二平和(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chokmah in Air | Wisdom in Air | Best of Swords |
| Moon in Libra | Emotion + balance | Reflective peace |
| Blue Rose | Uniting flower | Harmonious center |
| Crossed Swords | Held tension | Dynamic equilibrium |

**Title**: Lord of Peace Restored (平和重建之主)
**Qabalistic**: Chokmah in Air (气中之智慧)
**Astrological**: Moon in Libra (月亮入天秤座)

**Source Text**:
> "This card is ruled by Chokmah in the Element of Air. ... It represents a general shaking-up, resulting from the conflict of Fire and Water in their marriage... But the purity and exaltation of Chokmah are such that this card manifests the very best idea possible to the suit. The energy abides above the onslaught of disruption. This comparative calm is emphasized by the celestial attribution: the Moon in Libra. ... In the card appear two swords crossed; they are united by a blue rose with five petals... The Rose emits white rays, producing a geometrical pattern that emphasizes the equilibrium of the symbol."

**English Paraphrase**:
**Balanced Mind** – Corresponds to Chokmah (Wisdom/Force) in Air. Although Swords as a suit are unstable and prone to disruption, here the pure exaltation of Chokmah gives the **best possible expression of Air**. The energy remains above conflict. **Moon in Libra** brings natural peace and emotional balance to the intellect. Two swords are crossed and joined by a five‑petaled blue rose, whose white rays form a pattern of equilibrium. This is **Peace Restored**: a calm, reflective mind after turmoil, holding tension in graceful balance.

**Core**: **Mental Truce** – Inner calm, balanced thinking, reflection, quiet dialogue, temporary peace.

**Chinese Explanation**:
**宝剑二（平和）**对应空气元素中的**Chokmah（智慧/原初力量）**，在本来多变、易受干扰的宝剑牌组中呈现出**最理想的心智状态**。牌义由**月亮入天秤座**强化：月亮象征变动与情绪，天秤象征平衡与公正，两者在一起为心智带来**温和而流动的平衡**。画面中的两把剑交叉，被一朵**五瓣蓝玫瑰**连接，其放射出的白光构成几何图案，强调**对立中的和谐**。这不是完全没有冲突，而是**冲突之后建立的理性停战**：能够在矛盾之间保持冷静、理性与内在平和。

**In Readings**: Mental peace, negotiated truce, calm discussion, fair judgment, balanced choices, a pause in conflict, meditation.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Two of Swords shows Chokmah giving best expression of Air. Moon in Libra brings emotional balance. Blue rose unites crossed swords. Peace restored after conflict.
- **中文**: Crowley的宝剑二展示Chokmah给予空气最佳表达。月亮入天秤带来情感平衡。蓝玫瑰连接交叉剑。冲突后平和恢复。

**Narrative Snippets**:
- `[ns_thoth_swords_004]` `[trigger: two_swords_peace]` `[factor_trigger: thoth_swords_two]` `[role: 主干]` Two of Swords = Lord of Peace Restored—Chokmah's purity gives best expression of Air. → Core
- `[ns_thoth_swords_005]` `[trigger: moon_libra_balance]` `[factor_trigger: thoth_swords_two AND planet_moon_libra]` `[role: 条件分支]` Moon in Libra—emotional balance and reflective peace; calm after disturbance. → Astrological
- `[ns_thoth_swords_006]` `[trigger: blue_rose_unite]` `[factor_trigger: thoth_swords_two AND symbol_blue_rose]` `[role: 条件分支]` Blue five-petaled rose unites crossed swords—white rays form geometric equilibrium. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Swords: Peace (宝剑二：平和)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_two_001', 'tarot_mental_balance', 'rel_swords_two_002', 'tarot_harmonious_truce', 'l1_anchor', 'confidence', 'evi_swords_two_001', 'evi_swords_two_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_two_001', 'tarot_swords_two', 'astro_moon_libra']
    
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
        l1_anchor="bot_v1.0.0_two_of_swords__peace__宝剑二_平和_001_L1",
    )
    version: str = "1.0.0"
