"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027090
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
    semantic_id="bot_v1.0.0_ace_of_cups__圣杯一_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AceOfCups圣杯一(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Kether in Water | Crown in Water | Primordial emotion |
| Holy Grail | Sacred vessel | Divine reception |
| Dove of Holy Ghost | Spirit descending | Consecration |
| Binah's Sea | Great Mother ocean | Life source |

**Title**: The Root of the Powers of Water (水之力量的根源)
**Qabalistic**: Kether in Water (水中之冠)
**Astrological**: Root of Water signs (Cancer, Scorpio, Pisces)

**Source Text**:
> "This card represents the element of Water in its most secret and original form. It is the feminine complement of the Ace of Wands... derived from the Yoni and the Moon... essential form of the Holy Grail. Upon the dark sea of Binah, the Great Mother, are Lotuses, two in one... Above the Cup, descending upon it, is the Dove of the Holy Ghost... At the base... is the Moon."

**English Paraphrase**:
**Primordial Water Essence** - This card embodies the pure, secret origin of the Water element. It is the **Holy Grail**, the feminine complement to the Ace of Wands (Yoni/Moon vs Lingam/Sun). It depicts the dark sea of **Binah** (Great Mother) with Lotuses. The cup is filled with Life-fluid (Water/Blood/Wine) and consecrated by the descending **Dove of the Holy Ghost**. It represents the conception and production of the second form of Nature.

**Core**: **Divine Love** - The Holy Grail, pure emotion, spiritual reception, the Great Mother, intuition, the source of life.

**Chinese Explanation**:
**圣杯一**代表水元素的**最隐秘原始形式**。它是权杖一（阳具/太阳）的阴性互补（阴户/月亮），象征**圣杯**（Holy Grail）的本质形式。在**Binah**（伟大的母亲）的黑暗之海上，莲花盛开。圣杯中充满生命流体（水/血/酒），上方有**圣灵之鸽**降临祝圣。基座是月亮。它代表自然的第二种形式的受孕与生产，是神圣之爱与生命的源头。

**In Readings**: Love, intuition, spiritual beginning, fertility, reception, deep emotion, the Holy Grail.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ace of Cups is the Holy Grail, feminine complement to Ace of Wands. Binah's dark sea supports the lotus. Dove of Holy Ghost consecrates from above. Moon at base shows lunar nature.
- **中文**: Crowley的圣杯一是圣杯，权杖一的阴性互补。Binah的黑暗之海支撑莲花。圣灵之鸿从上方祝圣。底座月亮显示月亮本质。

**Narrative Snippets**:
- `[ns_thoth_cups_001]` `[trigger: ace_cups_thoth]` `[factor_trigger: thoth_cups_ace]` `[role: 主干]` Ace of Cups = Water in its most secret, original form—feminine complement to Ace of Wands (Yoni/Moon vs Lingam/Sun); essential form of the Holy Grail. → Core Meaning
- `[ns_thoth_cups_002]` `[trigger: binah_dark_sea]` `[factor_trigger: thoth_cups_ace AND symbol_binah_sea]` `[role: 条件分支]` Upon the dark sea of Binah (Great Mother), lotuses bloom—cup filled with Life-fluid (Water/Blood/Wine) that transforms into any form. → Visual Elements
- `[ns_thoth_cups_003]` `[trigger: dove_consecration]` `[factor_trigger: thoth_cups_ace AND symbol_dove_holy_ghost]` `[role: 条件分支]` Dove of Holy Ghost descends upon cup—Spirit consecrating Matter; conception and production of Nature's second form. → Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Cups (圣杯一)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_ace_001', 'tarot_divine_love', 'rel_cups_ace_002', 'tarot_life_source', 'l1_anchor', 'confidence', 'evi_cups_ace_001', 'evi_cups_ace_002', 'tarot_holy_grail', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_ace_001', 'tarot_cups_ace', 'astro_water_signs']
    
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
        l1_anchor="bot_v1.0.0_ace_of_cups__圣杯一_001_L1",
    )
    version: str = "1.0.0"
