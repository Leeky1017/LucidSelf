"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027159
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
    semantic_id="bot_v1.0.0_three_of_cups__abundance__圣杯三__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class ThreeOfCupsAbundance圣杯三(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Binah in Water | Mother in Water | Spiritual fertility |
| Mercury in Cancer | Will + reception | Abundant joy |
| Pomegranate | Persephone's fruit | Binding abundance |
| Demeter/Persephone | Harvest goddesses | Fertility mystery |

**Title**: Lord of Abundance (丰饶之主)
**Qabalistic**: Binah in Water (水中之理解)
**Astrological**: Mercury in Cancer (水星入巨蟹座)

**Source Text**:
> "This card refers to Binah in the suit of Water. This is the card of Demeter or Persephone. The Cups are pomegranates... overflowing from a single lotus... fulfilment of the Will of Love in abounding joy. ... Mercury in Cancer... Mercury is the Will or Word of the All-Father... The pomegranate was the fruit which Persephone ate... enabling him to hold her in the lower world... good things of life, although enjoyed, should be distrusted."

**English Paraphrase**:
**Spiritual Fertility** - Corresponds to Binah (Understanding/Mother) in Water. It is the card of **Demeter/Persephone**. The cups are **pomegranates**, overflowing from a lotus in a dark calm sea. Ruled by **Mercury in Cancer** (Will of All-Father in receptive sign). It represents the fulfillment of Love in **abounding joy**. However, the pomegranate symbolism implies a mystery: the fruit that bound Persephone to the underworld. Thus, while it signifies abundance and fertility, it warns that the good things of life should be enjoyed but **distrusted** (transient/binding).

**Core**: **Overflowing Joy** - Fertility, plenty, celebration, birth, harvest, but with a hint of binding to the material/lower world.

**Chinese Explanation**:
**圣杯三（丰饶）**对应水元素中的Binah（理解/母亲）。这是得墨忒耳或珀耳塞福涅的牌。圣杯呈**石榴**状，从黑色宁静海面的一朵莲花中满溢而出。对应**水星在巨蟹座**（全父的意志进入最接受的星座）。它代表爱之意志在**充盈的喜悦**中实现，是生育的灵性基础。然而，石榴是珀耳塞福涅在冥界吃的果实，暗示着即便享受生命的美好，也应保持**不信任**（警惕其束缚力）。

**In Readings**: Abundance, fertility, celebration, harvest, pleasure, overflowing emotion, conception.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Three of Cups shows Demeter/Persephone mythology. Pomegranate cups symbolize binding pleasure. Mercury in Cancer brings Will into reception. Abundance should be enjoyed but distrusted.
- **中文**: Crowley的圣杯三展示得墨忇耳/珀耳塞福涅神话。石榴杯象征束缚性快乐。水星入巨蟹带来意志进入接受。丰饶应享受但不信任。

**Narrative Snippets**:
- `[ns_thoth_cups_007]` `[trigger: three_cups_abundance]` `[factor_trigger: thoth_cups_three]` `[role: 主干]` Three of Cups = Lord of Abundance—Demeter/Persephone card; Mercury in Cancer brings Will into reception. → Core
- `[ns_thoth_cups_008]` `[trigger: pomegranate_binding]` `[factor_trigger: thoth_cups_three AND symbol_pomegranate]` `[role: 条件分支]` Pomegranate cups—fruit binding Persephone to underworld; enjoyed but distrusted. → Warning
- `[ns_thoth_cups_009]` `[trigger: abounding_joy]` `[factor_trigger: thoth_cups_three AND state_abundance]` `[role: 条件分支]` Fulfilment of Will of Love in abounding joy—spiritual fertility with binding hint. → Paradox"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Cups: Abundance (圣杯三：丰饶)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_three_001', 'tarot_joy', 'rel_cups_three_002', 'tarot_binding_pleasure', 'l1_anchor', 'confidence', 'evi_cups_three_001', 'evi_cups_three_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_three_001', 'tarot_cups_three', 'astro_mercury_cancer']
    
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
        l1_anchor="bot_v1.0.0_three_of_cups__abundance__圣杯三__001_L1",
    )
    version: str = "1.0.0"
