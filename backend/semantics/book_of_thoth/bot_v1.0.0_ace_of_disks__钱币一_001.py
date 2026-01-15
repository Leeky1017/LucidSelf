"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063307
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
    semantic_id="bot_v1.0.0_ace_of_disks__钱币一_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AceOfDisks钱币一(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Kether in Earth | Crown in Earth | Primordial matter |
| Whirling Disk | Rotating sphere | Living Earth |
| Emerald Green | Isis color | Reborn sacredness |
| Sol-Terra Identity | Sun-Earth unity | Divine matter |

**Title**: The Root of the Powers of Earth (土之力量的根源)
**Qabalistic**: Kether in Earth (土中之冠)
**Astrological**: Root of Earth signs (Taurus, Virgo, Capricorn)

**Source Text**:
> "The Ace of Disks pictures the entry of that type of Energy which is called Earth... the old conception of the Earth as a passive, immobile, even dead, even 'evil' element, had to go... to restore the King-Scale colour attribution to that of the Aeon of Isis, Emerald Green... the Disk is a whirling emblem... every Star, every true Planet, is a whirling sphere. The Atom, again, is no more the hard, intractable, dead Particle of Dalton, but a system of whirling forces... About this whirling Disk are its six Wings... This card is thus an affirmation of the identity of Sol and Terra."

**English Paraphrase**:
**Living Earth** – This card embodies the original **energy of Earth**, but transformed for the New Aeon: Earth is no longer passive, dead or evil, but a **whirling, dynamic force**, shown in Emerald Green (the color of Isis reborn). The Disk itself is a rotating sphere with six wings, representing both **Planet Earth** as a living being and the **Atom** as a system of forces. At its center is the hieroglyph of the Beast (666), the Phallus showing Sol and Luna, affirming the **identity of Sun and Earth**: both are alive, both whirl, both are divine. This is the primordial substance in motion, the material foundation of the Universe animated by Spirit.

**Core**: **Manifestation & Matter** – Material foundation, wealth, body, earth as living and sacred, the beginning of physical form.

**Chinese Explanation**:
**钱币一**代表**土元素的原初能量**，但在 Crowley 的"新纪元"重新诠释下，土不再是"被动、僵死、甚至邪恶"的物质，而是一种**旋转、动态、充满生命的力量**。牌面的圆盘以**翡翠绿**（Isis 的重生之绿）为主色调，带有六只翅膀，象征**地球是活的星球、原子是旋转的力量系统**。中心是 666 的象征（野兽的印记），太阳与月亮的结合，宣告**太阳与大地的同一性**——两者都是活生生的存在。它提醒人：物质不是死的、低级的，而是被圣灵贯穿的显化载体，所有形式的根基。

**In Readings**: New material opportunities, wealth, physical manifestation, grounding, embodiment, tangible beginnings, the sacredness of matter.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ace of Disks shows Earth as living, not dead. Whirling disk with six wings represents planet and atom. Emerald Green is Isis reborn. Beast 666 hieroglyph affirms Sol-Terra identity.
- **中文**: Crowley的钱币一展示大地是活的，而非死的。六翼旋转圆盘代表行星和原子。翡翠绿是Isis重生。野兽666象形确认日地同一性。

**Narrative Snippets**:
- `[ns_thoth_disks_001]` `[trigger: ace_disks_thoth]` `[factor_trigger: thoth_disks_ace]` `[role: 主干]` Ace of Disks = Living Earth energy—no longer passive/dead; whirling dynamic force in Emerald Green. → Core
- `[ns_thoth_disks_002]` `[trigger: whirling_disk]` `[factor_trigger: thoth_disks_ace AND symbol_whirling_disk]` `[role: 条件分支]` Whirling disk with six wings—planet Earth and atom as rotating systems of force. → Visual
- `[ns_thoth_disks_003]` `[trigger: sol_terra_identity]` `[factor_trigger: thoth_disks_ace AND doctrine_sol_terra]` `[role: 条件分支]` Beast 666 hieroglyph affirms identity of Sol and Terra—both alive, both whirl, both divine. → Doctrine"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Disks (钱币一)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_ace_001', 'tarot_material_manifestation', 'rel_disks_ace_002', 'tarot_sacred_matter', 'l1_anchor', 'confidence', 'evi_disks_ace_001', 'evi_disks_ace_002', 'tarot_sol_terra', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_ace_001', 'tarot_disks_ace', 'astro_earth_signs']
    
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
        l1_anchor="bot_v1.0.0_ace_of_disks__钱币一_001_L1",
    )
    version: str = "1.0.0"
