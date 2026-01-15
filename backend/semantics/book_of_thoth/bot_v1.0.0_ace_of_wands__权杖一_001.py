"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088735
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
    semantic_id="bot_v1.0.0_ace_of_wands__权杖一_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AceOfWands权杖一(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Kether in Fire | Crown in Fire element | Primordial spark |
| Solar-phallic | Sun/masculine eruption | Creative force origin |
| Yod | Hebrew letter "Hand/Seed" | Divine fire seeds |
| Root of Fire | Fire signs foundation | Aries/Leo/Sagittarius |

**Title**: The Root of the Powers of Fire (火之力量的根源)
**Qabalistic**: Kether in Fire (火中之冠)
**Astrological**: Root of Fire signs (Aries, Leo, Sagittarius)

**Source Text**:
> "This card represents the essence of the element of Fire in its inception. It is a solar-phallic outburst of flame from which spring lightnings in every direction. These flames are Yods, arranged in the form of the Tree of Life. ... It is the primordial Energy of the Divine manifesting in Matter, at so early a stage that it is not yet definitely formulated as Will."

**English Paraphrase**:
**Primordial Fire Essence** - This card embodies the pure, initial spark of the Fire element. It is a potent **solar-phallic eruption**, sending lightning bolts (Yods/Seeds) outward in the pattern of the Tree of Life. It represents **Divine Energy** just beginning to manifest in the material world—raw, unshaped, and prior to the formation of specific Will. It is the blind force of creation.

**Core**: **Primordial Energy** - The initial spark, the raw urge to create, the essence of fire before it takes form.

**Chinese Explanation**:
**权杖一**代表火元素的**原始本质**。它是**太阳-阳具式**（solar-phallic）的火焰爆发，向四面八方射出闪电。这些火焰是**Yod**（希伯来字母"手"/种子），按生命之树的形状排列。它象征着**神圣能量**在物质中的初次显化，处于非常早期的阶段，尚未明确形成具体的"意志"。它是纯粹的动力和创造的盲目力量。

**In Readings**: Raw energy, new beginnings, creative impulse, initial spark, force without direction, masculine potential.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ace of Wands emphasizes Fire's primordial essence before Will forms. Solar-phallic imagery represents masculine creative principle. Yods arranged as Tree of Life show divine structure. Harris depicts explosive flame eruption.
- **中文**: Crowley的权杖一强调意志形成前火的原始本质。太阳-阳具意象代表男性创造原则。Yod按生命之树排列显示神圣结构。Harris描绘爆发性火焰喷发。

**Narrative Snippets**:
- `[ns_thoth_wands_001]` `[trigger: ace_wands_thoth]` `[factor_trigger: thoth_wands_ace]` `[role: 主干]` Ace of Wands = Fire in its inception—solar-phallic eruption; divine energy manifesting before Will forms. → Core
- `[ns_thoth_wands_002]` `[trigger: yods_tree_life]` `[factor_trigger: thoth_wands_ace AND symbol_yod]` `[role: 条件分支]` Flames are Yods arranged as Tree of Life—divine fire seeds springing outward in every direction. → Visual
- `[ns_thoth_wands_003]` `[trigger: primordial_force]` `[factor_trigger: thoth_wands_ace AND state_inception]` `[role: 条件分支]` Primordial Energy of Divine manifesting in Matter—so early not yet formulated as Will; blind force. → State"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Wands (权杖一)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_ace_001', 'tarot_primordial_force', 'rel_wands_ace_002', 'tarot_creative_seed', 'l1_anchor', 'confidence', 'evi_wands_ace_001', 'evi_wands_ace_002', 'tarot_solar_phallic', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_ace_001', 'tarot_wands_ace', 'astro_fire_signs']
    
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
        l1_anchor="bot_v1.0.0_ace_of_wands__权杖一_001_L1",
    )
    version: str = "1.0.0"
