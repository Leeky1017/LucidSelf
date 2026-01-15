"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027352
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
    semantic_id="bot_v1.0.0_nine_of_cups__happiness__圣杯九_喜_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class NineOfCupsHappiness圣杯九喜(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Yesod in Water | Foundation in Water | Stability restored |
| Jupiter in Pisces | Blessing + flow | Maximum benefic |
| Laetitia | Geomantic Joy | Jupiter/Pisces figure |
| Nine Cups | Ordered fullness | Perfect banquet |

**Title**: Lord of Material Happiness (物质喜悦之主)
**Qabalistic**: Yesod in Water (水中之基础)
**Astrological**: Jupiter in Pisces (木星入双鱼座)

**Source Text**:
> "The Number Nine, Yesod, in the suit of Water, restores the stability lost by the excursions of Netzach and Hod from the Middle Pillar. It is also the number of the Moon... In this card is the pageant of the culmination and perfection of the original force of Water. The Ruler is Jupiter in Pisces... a definite benediction... nine cups perfectly arranged in a square; all are filled and overflowing with Water. It is the most complete and most beneficent aspect of the force of Water. The Geomantic Figure Laetitia... is ruled by Jupiter in Pisces... Laetitia, Joy, gladness... the wine is poured by Ganymede himself... an ordered banquet of delight, True Wisdom self-fulfilled in Perfect Happiness."

**English Paraphrase**:
**Culminated Joy** - Corresponds to Yesod (Foundation/Moon) in Water, restoring stability after the swings of Netzach and Hod. Ruled by **Jupiter in Pisces**, it is pure blessing: nine cups neatly arranged in a square, all **filled and overflowing**. This card shows the **culmination and perfection** of Water's original force—happiness, contentment, emotional success. Associated with the geomantic figure **Laetitia (Joy)**, it is the banquet where the "wine of the gods" is poured freely, symbolizing True Wisdom fulfilled in **Perfect Happiness**.

**Core**: **Deep Contentment** - Emotional fulfillment, joy, satisfaction, success in relationships, wishes fulfilled.

**Chinese Explanation**:
**圣杯九（喜悦）**对应水元素中的Yesod（基础/月亮），在经历Netzach与Hod的摆动之后重新带回**稳定**。统治行星为**木星入双鱼座**，代表彻底的祝福和扩展。画面中九只圣杯整齐排列成方形，全都**盛满并溢出清水/美酒**，展示水元素原初力量的**圆满与成就**。它与几何占卜中的**Laetitia（喜乐）**对应，像众神之杯由伽倪墨得（Ganymede）亲手斟满，是一种"真智慧在完满喜悦中自我实现"的状态，象征心愿达成与由内而外的幸福感。

**In Readings**: Happiness, satisfaction, emotional fulfillment, celebration, wish-fulfillment, enjoying blessings, gratitude.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Nine of Cups shows Yesod restoring stability after Netzach/Hod swings. Jupiter in Pisces is pure benediction. Nine cups arranged in square, all full and overflowing. Laetitia geomantic figure = Joy.
- **中文**: Crowley的圣杯九展示Yesod在Netzach/Hod摆动后恢复稳定。木星入双鱼是纯粹祝福。九杯方形排列，全部满溢。Laetitia几何符号=喜乐。

**Narrative Snippets**:
- `[ns_thoth_cups_025]` `[trigger: nine_cups_happiness]` `[factor_trigger: thoth_cups_nine]` `[role: 主干]` Nine of Cups = Lord of Material Happiness—Yesod restores stability; Jupiter in Pisces pure benediction. → Core
- `[ns_thoth_cups_026]` `[trigger: nine_cups_overflow]` `[factor_trigger: thoth_cups_nine AND state_perfection]` `[role: 条件分支]` Nine cups perfectly arranged in square, all filled and overflowing—most beneficent Water aspect. → Visual
- `[ns_thoth_cups_027]` `[trigger: laetitia_joy]` `[factor_trigger: thoth_cups_nine AND geomancy_laetitia]` `[role: 条件分支]` Geomantic figure Laetitia (Joy)—wine poured by Ganymede; True Wisdom in Perfect Happiness. → Geomantic"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Cups: Happiness (圣杯九：喜悦)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_nine_001', 'tarot_emotional_fulfillment', 'rel_cups_nine_002', 'tarot_perfected_joy', 'l1_anchor', 'confidence', 'evi_cups_nine_001', 'evi_cups_nine_002', 'tarot_perfected_joy', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_nine_001', 'tarot_cups_nine', 'astro_jupiter_pisces']
    
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
        l1_anchor="bot_v1.0.0_nine_of_cups__happiness__圣杯九_喜_001_L1",
    )
    version: str = "1.0.0"
