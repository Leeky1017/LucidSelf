"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063623
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
    semantic_id="bot_v1.0.0_eight_of_disks__prudence__钱币八__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class EightOfDisksPrudence钱币八(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hod in Earth | Intellect in Earth | Mercurial help |
| Sun in Virgo | Meticulous vitality | Intelligence to matter |
| Populus Pattern | Tree figure | Deep roots |
| Turn of Tide | Nadir renewal | After failure |

**Title**: Lord of Prudence (审慎之主)
**Qabalistic**: Hod in Earth (土中之荣光)
**Astrological**: Sun in Virgo (太阳入处女座)

**Source Text**:
> "The number Eight, Hod, is very helpful in this card, because it represents Mercury in his most spiritual aspect, and he both rules and is exalted in the sign of Virgo... It signifies intelligence lovingly applied to material matters, especially those of the agriculturalist, the artificer and the engineer... this card marks the turn of the tide... These last three cards seem to prepare the explosion which will renew the whole Cycle... The disks are arranged in the form of the geomantic figure Populus. These disks may be represented as the flowers or fruits of a great tree, its solid roots in fertile land."

**English Paraphrase**:
**Intelligent Cultivation** – Corresponds to Hod (Intellect) in Earth. Mercury rules and is exalted in Virgo, Sun governs decan: **intelligence lovingly applied to material matters**. After Seven's Failure, this marks **the turn of the tide**: the nadir becomes seed of renewal. Disks form **Populus**, shown as tree with deep roots. This is **Prudence**: careful cultivation, skilled work, patient growth.

**Core**: **Skillful Work** – Prudence, craftsmanship, patience, learning, planting for future.

**Chinese Explanation**:
**钱币八（审慎）**对应**Hod（智力）**。水星在处女座入庙入旺，太阳统治：**智慧以爱应用于物质**。七之后**潮水转向**：最低点孕育更新。圆盘排成**Populus**，大树深根。这是**审慎**：谨慎耕耘、精湛技艺、耐心成长。

**In Readings**: Prudent work, learning craft, patient cultivation, skill development, planting seeds.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Eight of Disks shows Hod with Mercury's help. Sun in Virgo - intelligence to matter. Populus pattern as tree with deep roots. Turn of tide after Seven's failure.
- **中文**: Crowley的钱币八展示Hod得水星帮助。太阳入处女—智慧应用于物质。Populus图案作为深根大树。七号牌失败后潮水转向。

**Narrative Snippets**:
- `[ns_thoth_disks_022]` `[trigger: eight_disks_prudence]` `[factor_trigger: thoth_disks_eight]` `[role: 主干]` Eight of Disks = Lord of Prudence—Hod with Mercury's help; intelligence applied to matter. → Core
- `[ns_thoth_disks_023]` `[trigger: sun_virgo_craft]` `[factor_trigger: thoth_disks_eight AND planet_sun_virgo]` `[role: 条件分支]` Sun in Virgo—meticulous vitality; skilled work; turn of tide after Seven's failure. → Astrological
- `[ns_thoth_disks_024]` `[trigger: populus_tree]` `[factor_trigger: thoth_disks_eight AND symbol_populus]` `[role: 条件分支]` Populus pattern as great tree with deep roots—patient cultivation bears fruit. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Disks: Prudence (钱币八：审慎)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_eight_001', 'tarot_intelligent_cultivation', 'rel_disks_eight_002', 'tarot_renewal_seed', 'l1_anchor', 'confidence', 'evi_disks_eight_001', 'evi_disks_eight_002', 'tarot_turn_of_tide', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_eight_001', 'tarot_disks_eight', 'astro_sun_virgo']
    
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
        l1_anchor="bot_v1.0.0_eight_of_disks__prudence__钱币八__001_L1",
    )
    version: str = "1.0.0"
