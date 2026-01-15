"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027134
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
    semantic_id="bot_v1.0.0_two_of_cups__love__圣杯二_爱_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TwoOfCupsLove圣杯二爱(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chokmah in Water | Wisdom in Water | Love's Will |
| Venus in Cancer | Harmony + receptivity | Perfect union |
| Twin Dolphins | Alchemical symbol | Mutual joy |
| Love under Will | Thelemic formula | Guided passion |

**Title**: Lord of Love (爱之主)
**Qabalistic**: Chokmah in Water (水中之智慧)
**Astrological**: Venus in Cancer (金星入巨蟹座)

**Source Text**:
> "The Two always represents the Word and the Will. ... in the suit of Water, it must refer to Love, which recovers unity from dividuality by mutual annihilation. The card also refers to Venus in Cancer... The hieroglyph... represents two cups... fed with lucent water from a lotus... twin dolphins... The dolphin is peculiarly sacred to Alchemy. ... Lord of Love under Will... perfect and placid harmony."

**English Paraphrase**:
**Love under Will** - Corresponds to Chokmah (Wisdom/Will) in Water. It represents the first manifestation: **Love**, which recovers unity from division through mutual annihilation. Ruled by **Venus in Cancer** (House of Moon, Jupiter exalted), signifying a perfect, placid harmony. The symbol shows two cups fed by a lotus, with **twin dolphins** (Alchemy's Royal Art) entwined. It is the "Lord of Love under Will", radiating intense joy and ecstasy before any impurity sets in.

**Core**: **Harmonious Union** - Perfect partnership, love under will, alchemical marriage, mutual reflection, emotional unity.

**Chinese Explanation**:
**圣杯二（爱）**对应水元素中的Chokmah（智慧/意志）。在水中，二代表**爱**，即通过相互消融从分裂中恢复统一。对应**金星在巨蟹座**（月亮之家，木星旺相），象征极其友好的行星组合。图像显示两只杯子由莲花注水，伴有**双海豚**（炼金术神圣符号）。这被称为"**意志下的爱之主**"（Lord of Love under Will），展示了男性与女性的完美、平静的和谐，辐射着狂喜。

**In Readings**: Love, partnership, marriage, harmony, attraction, emotional connection, perfect union.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Two of Cups shows Love recovering unity from division. Venus in Cancer creates perfect harmony. Twin dolphins symbolize alchemical Royal Art. "Love under Will" is core Thelemic principle.
- **中文**: Crowley的圣杯二展示爱从分裂中恢复统一。金星入巨蟹创造完美和谐。双海豚象征炼金皇家艺术。"意志下的爱"是泰勒玛核心原则。

**Narrative Snippets**:
- `[ns_thoth_cups_004]` `[trigger: two_cups_love]` `[factor_trigger: thoth_cups_two]` `[role: 主干]` Two of Cups = Lord of Love—recovers unity from dividuality by mutual annihilation; Venus in Cancer creating perfect, placid harmony. → Core Meaning
- `[ns_thoth_cups_005]` `[trigger: twin_dolphins]` `[factor_trigger: thoth_cups_two AND symbol_twin_dolphins]` `[role: 条件分支]` Twin dolphins entwined—Alchemy's sacred Royal Art symbol; joyous reciprocal union; cups fed by lucent water from lotus. → Visual Elements
- `[ns_thoth_cups_006]` `[trigger: love_under_will]` `[factor_trigger: thoth_cups_two AND principle_thelema]` `[role: 主干依赖]` "Lord of Love under Will"—Thelemic formula; passion guided by True Will; intense joy and ecstasy before impurity. → Thelemic Principle"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Cups: Love (圣杯二：爱)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_two_001', 'tarot_unity', 'rel_cups_two_002', 'tarot_thelemic_love', 'l1_anchor', 'confidence', 'evi_cups_two_001', 'evi_cups_two_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_two_001', 'tarot_cups_two', 'astro_venus_cancer']
    
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
        l1_anchor="bot_v1.0.0_two_of_cups__love__圣杯二_爱_001_L1",
    )
    version: str = "1.0.0"
