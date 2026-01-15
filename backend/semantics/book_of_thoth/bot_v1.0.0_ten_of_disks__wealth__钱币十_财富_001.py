"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063715
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
    semantic_id="bot_v1.0.0_ten_of_disks__wealth__钱币十_财富_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TenOfDisksWealth钱币十财富(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Malkuth in Earth | Kingdom in Earth | Final solidification |
| Mercury in Virgo | Analytical wealth | Warning inertia |
| Tree of Life | Sephirothic layout | Culmination |
| Sun at Hod | Logos in matter | Regeneration key |

**Title**: Lord of Wealth (财富之主)
**Qabalistic**: Malkuth in Earth (土中之王国)
**Astrological**: Mercury in Virgo (水星入处女座)

**Source Text**:
> "The number Ten, Malkuth, as always, represents the final issue of the Energy. Here is great and final solidification... force is completely expended and results in death. Mercury rules this card in Virgo; and this may imply that the acquired wealth, being inert, will be dissipated unless put to further use... The disks... are arranged on the Tree of Life, but the Tenth coin is much larger than the rest; the image indicates the futility of material gain... except that the coin in the place of Hod (Mercury) on the Tree is marked with the cipher of the Sun. This indicates the only possibility of issue from the impasse... This card is in fact a hieroglyph of the cycle of regeneration."

**English Paraphrase**:
**The End and the Seed** – Malkuth in Earth: **final issue**, complete solidification, force expended to "death." **Mercury in Virgo** warns: inert wealth dissipates unless used beyond hoarding. Ten coins on Tree; tenth (Malkuth) largest, showing **futility**. But coin at Hod bears Sun's cipher: the **way out** – Father's Will (Logos) inherent in matter, Virgin pregnant with future. **Wealth** as culmination and potential rebirth – regeneration cycle hidden in densest matter.

**Core**: **Culmination & Rebirth** – Wealth, inheritance, completion, but stagnation unless renewed; seed in stone.

**Chinese Explanation**:
**钱币十（财富）**对应**Malkuth（王国）**：**最终发放**，完全固化，力量耗尽至"死亡"。**水星入处女**警告：惰性财富会消散。十币在生命树上；第十枚最大，显示**徒劳**。但 Hod 处的币标有**太阳符号**：**唯一出路**——物质中蕴含父神意志，处女怀着未来。**财富**既是终结也是潜在重生——最稠密物质中的再生循环。

**In Readings**: Wealth, inheritance, completion, family legacy, but also stagnation, need to use wealth wisely; hidden seed of renewal.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ten of Disks shows Malkuth as final solidification. Mercury in Virgo warns inert wealth dissipates. Tree of Life layout with largest tenth coin. Sun at Hod is the way out - regeneration cycle.
- **中文**: Crowley的钱币十展示Malkuth作为最终固化。水星入处女警告惰性财富会消散。生命树布局，第十枚币最大。Hod处太阳是出路—再生循环。

**Narrative Snippets**:
- `[ns_thoth_disks_028]` `[trigger: ten_disks_wealth]` `[factor_trigger: thoth_disks_ten]` `[role: 主干]` Ten of Disks = Lord of Wealth—Malkuth; final solidification; force expended to "death". → Core
- `[ns_thoth_disks_029]` `[trigger: mercury_virgo_inert]` `[factor_trigger: thoth_disks_ten AND planet_mercury_virgo]` `[role: 条件分支]` Mercury in Virgo—acquired wealth being inert will dissipate unless put to further use. → Astrological
- `[ns_thoth_disks_030]` `[trigger: sun_at_hod]` `[factor_trigger: thoth_disks_ten AND symbol_sun_hod]` `[role: 条件分支]` Tree of Life layout; Sun cipher at Hod—only way out of impasse; regeneration cycle. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Disks: Wealth (钱币十：财富)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_ten_001', 'tarot_final_solidification', 'rel_disks_ten_002', 'tarot_regeneration_seed', 'l1_anchor', 'confidence', 'evi_disks_ten_001', 'evi_disks_ten_002', 'tarot_sun_at_hod', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_ten_001', 'tarot_disks_ten', 'astro_mercury_virgo']
    
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
        l1_anchor="bot_v1.0.0_ten_of_disks__wealth__钱币十_财富_001_L1",
    )
    version: str = "1.0.0"
