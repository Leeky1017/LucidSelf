"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063436
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
    semantic_id="bot_v1.0.0_five_of_disks__worry__钱币五_忧虑_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FiveOfDisksWorry钱币五忧虑(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Geburah in Earth | Severity in Earth | Disruption |
| Mercury in Taurus | Mind vs matter | Strain and anxiety |
| Inverted Pentagram | Unstable base | Earthquake effect |
| Five Tattvas | Hindu elements | Barely holding |

**Title**: Lord of Material Trouble (物质困扰之主)
**Qabalistic**: Geburah in Earth (土中之严厉)
**Astrological**: Mercury in Taurus (水星入金牛座)

**Source Text**:
> "The Number Five, Geburah, in the suit of Earth, shows the disruption of the Elements, just as in the other suits. This is emphasized by the rule of Mercury in Taurus, types of energy which are opposed. It needs a very powerful Mercury to upset Taurus; so the natural meaning is Intelligence applied to Labour. The symbol represents five disks in the form of the inverted Pentagram, instability in the very foundations of Matter. The effect is that of an earthquake. They are, however, representative of the five Tatvas; these hold together, on a very low plane, an organism which would otherwise disrupt completely..."

**English Paraphrase**:
**Unstable Foundation** – Corresponds to Geburah (Severity/Disruption) in Earth. As in other suits, Five brings disruption; here **Mercury in Taurus** pits restless intellect against immovable stability. It takes a very strong Mercury to upset Taurus, so the card represents **intelligence applied to labor** – but often with strain, anxiety, and insecurity. The five disks form an **inverted pentagram**, showing **instability in the very foundations of matter** – like an earthquake. However, they also represent the **five Tattvas** (Hindu elements), which barely hold together the organism that would otherwise fall apart. This is **Worry**: financial strain, job insecurity, material anxiety, and the effort to prevent collapse.

**Core**: **Material Anxiety** – Worry, financial strain, job insecurity, poverty consciousness, unstable foundations.

**Chinese Explanation**:
**钱币五（忧虑）**对应土元素中的**Geburah（严厉/破坏）**，一如其它花色的五号牌，带来扰动与瓦解。统治星为**水星入金牛座**——两者本质对立：水星灵活多变，金牛固定稳定。牌义指向"**智力应用于劳动**"，但往往伴随巨大的**压力、焦虑与不安全感**。五个圆盘排列成**倒五芒星**，象征**物质基础的不稳定**，效果如同地震。然而，它们也代表印度的**五大元素（Tattvas）**，勉强把一个本该崩溃的有机体维系在一起。这张牌常指向：财务困难、失业风险、入不敷出、对物质匮乏的恐惧，以及为防止彻底崩溃而持续的紧张努力。

**In Readings**: Worry, financial problems, job loss, material insecurity, strain, hardship, fear of poverty, barely holding together.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Five of Disks shows Geburah disrupting Earth. Mercury in Taurus creates strain. Inverted pentagram shows unstable foundations like earthquake. Five Tattvas barely hold organism together.
- **中文**: Crowley的钱币五展示Geburah扰乱大地。水星入金牛创造紧张。倒五芒星显示不稳定基础如地震。五大元素勉强维系有机体。

**Narrative Snippets**:
- `[ns_thoth_disks_013]` `[trigger: five_disks_worry]` `[factor_trigger: thoth_disks_five]` `[role: 主干]` Five of Disks = Lord of Material Trouble—Geburah disrupts Earth; instability in foundations. → Core
- `[ns_thoth_disks_014]` `[trigger: mercury_taurus_strain]` `[factor_trigger: thoth_disks_five AND planet_mercury_taurus]` `[role: 条件分支]` Mercury in Taurus—opposed energies; intelligence applied to labor with strain and anxiety. → Astrological
- `[ns_thoth_disks_015]` `[trigger: inverted_pentagram_earthquake]` `[factor_trigger: thoth_disks_five AND symbol_inverted_pentagram]` `[role: 条件分支]` Inverted pentagram of disks—earthquake effect; five Tattvas barely hold organism together. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Five of Disks: Worry (钱币五：忧虑)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_five_001', 'tarot_material_anxiety', 'rel_disks_five_002', 'tarot_barely_holding', 'l1_anchor', 'confidence', 'evi_disks_five_001', 'evi_disks_five_002', 'tarot_five_tattvas', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_five_001', 'tarot_disks_five', 'astro_mercury_taurus']
    
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
        l1_anchor="bot_v1.0.0_five_of_disks__worry__钱币五_忧虑_001_L1",
    )
    version: str = "1.0.0"
