"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063459
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
    semantic_id="bot_v1.0.0_six_of_disks__success__钱币六_成功_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SixOfDisksSuccess钱币六成功(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tiphareth in Earth | Beauty in Earth | Full harmony |
| Moon in Taurus | Exalted Moon | Transient perfection |
| Hexagram Layout | Six-pointed star | Planetary balance |
| Rose & Cross | 49 petals | Spiritual-material union |

**Title**: Lord of Material Success (物质成功之主)
**Qabalistic**: Tiphareth in Earth (土中之美)
**Astrological**: Moon in Taurus (月亮入金牛座)

**Source Text**:
> "The Number Six, Tiphareth, as before, represents the full harmonious establishment of the Energy of the Element. The Moon in Taurus rules the card; and this, while increasing the approach to perfection (for the Moon is exalted in Taurus and therefore in her highest form) marks that the condition is transient. The disks are arranged in the form of the Hexagram... In the centre blushes and glows the light rose-madder of dawn... These colours show Tiphareth fully realized on Earth... The planets are arranged in accordance with their usual attribution; but they are only shown as disks irradiated by the Sun in their centre. This Sun is idolized as the Rose and Cross; the Rose has forty-nine petals, the interplay of the Seven with the Seven."

**English Paraphrase**:
**Harmonious Prosperity** – Corresponds to Tiphareth (Beauty/Harmony) in Earth: the **full harmonious establishment** of material energy. Ruled by **Moon in Taurus**, where the Moon is exalted and in her highest form, bringing perfection – yet also marking this as **transient**. Six disks form a hexagram, with a glowing rose-madder center (dawn), showing **Tiphareth fully realized on Earth**. The planets radiate from a central Sun depicted as the **Rose and Cross** with 49 petals (7×7). This is **Success**: material prosperity, harmonious work, beauty in tangible form, and the union of spiritual and material – but always temporary.

**Core**: **Material Harmony** – Success, prosperity, generosity, fair exchange, beauty in work, but transient.

**Chinese Explanation**:
**钱币六（成功）**对应土元素中的**Tiphareth（美/和谐/中心）**，代表物质能量的**完满和谐建立**。统治星为**月亮入金牛座**，这是月亮**入旺**（exalted）的位置，处于最高形式，带来趋向完美的状态——但同时也标志着这种状态是**短暂的**（transient）。六个圆盘排列成**六芒星**，中心泛出玫瑰红色（黎明之光），象征**Tiphareth 在大地上的完全实现**。行星们按通常对应排列，从中央的太阳放射出光芒；太阳以**玫瑰十字**的形式被理想化，玫瑰有 49 瓣（7×7 的交互）。这是**成功**：物质繁荣、和谐劳动、有形之美、灵性与物质的结合——但终归是暂时的幸福时刻。

**In Readings**: Success, prosperity, fair exchange, generosity, material harmony, beauty realized, reward for work, but also awareness of impermanence.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Six of Disks shows Tiphareth fully realized in Earth. Moon in Taurus exalted - perfection but transient. Hexagram layout with Rose & Cross (49 petals). Planets radiate from central Sun.
- **中文**: Crowley的钱币六展示Tiphareth在大地完全实现。月亮入金牛入旺—完美但短暂。六芒星布局与玫瑰十字（49瓣）。行星从中央太阳放射。

**Narrative Snippets**:
- `[ns_thoth_disks_016]` `[trigger: six_disks_success]` `[factor_trigger: thoth_disks_six]` `[role: 主干]` Six of Disks = Lord of Material Success—Tiphareth fully realized in Earth; harmonious prosperity. → Core
- `[ns_thoth_disks_017]` `[trigger: moon_taurus_exalted]` `[factor_trigger: thoth_disks_six AND planet_moon_taurus]` `[role: 条件分支]` Moon in Taurus exalted—perfection but transient; highest form of material nurture. → Astrological
- `[ns_thoth_disks_018]` `[trigger: hexagram_rose_cross]` `[factor_trigger: thoth_disks_six AND symbol_hexagram]` `[role: 条件分支]` Hexagram layout; Rose & Cross (49 petals) at center; planets radiate from central Sun. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Six of Disks: Success (钱币六：成功)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_six_001', 'tarot_material_harmony', 'rel_disks_six_002', 'tarot_transient_perfection', 'l1_anchor', 'confidence', 'evi_disks_six_001', 'evi_disks_six_002', 'tarot_transient_perfection', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_six_001', 'tarot_disks_six', 'astro_moon_taurus']
    
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
        l1_anchor="bot_v1.0.0_six_of_disks__success__钱币六_成功_001_L1",
    )
    version: str = "1.0.0"
