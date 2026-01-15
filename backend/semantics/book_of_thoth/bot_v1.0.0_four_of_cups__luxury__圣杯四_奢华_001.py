"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027181
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
    semantic_id="bot_v1.0.0_four_of_cups__luxury__圣杯四_奢华_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FourOfCupsLuxury圣杯四奢华(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chesed in Water | Mercy in Water | Ordered pleasure |
| Moon in Cancer | Home sign | Strong but passive |
| Curse of Limitation | Four's dead stop | Stagnation |
| Seeds of Decay | Corruption start | Pleasure rotting |

**Title**: Lord of Luxury (奢华之主)
**Qabalistic**: Chesed in Water (水中之仁慈)
**Astrological**: Moon in Cancer (月亮入巨蟹座)

**Source Text**:
> "This card refers to Chesed in the sphere of Water. ... lost the original purity of the conception. The card refers to the Moon in Cancer, which is her own house... implies a certain weakness, an abandonment to desire. ... seeds of decay into the fruit of pleasure. The sea... surface is ruffled... four Cups... no longer so stable. ... Four is the number of the Curse of Limitation... blind and barren Cross... dead stop."

**English Paraphrase**:
**Unstable Pleasure** - Corresponds to Chesed (Mercy) in Water. Ruled by **Moon in Cancer** (her own house). While ordered and stabilized, it has lost the original purity. The placement implies **abandonment to desire**, introducing seeds of decay. The sea is ruffled, and the cups are less stable. Four is a "dead stop," the **Curse of Limitation**. It represents pleasure that has become static or excessive, leading to dissatisfaction. It is the "blind and barren Cross" before the awakening of the Daughter.

**Core**: **Static Pleasure** - Emotional stability turning to stagnation, luxury, dissatisfaction, possessiveness, desire without new influx.

**Chinese Explanation**:
**圣杯四（奢华）**对应水元素中的Chesed（仁慈）。对应**月亮在巨蟹座**（本位宫）。虽然稳定，但失去了原始的纯洁。这暗示了某种软弱，**沉溺于欲望**，将腐败的种子引入快乐的果实中。海面起波澜，杯子不再那么稳定。数字4被视为"限制的诅咒"（Curse of Limitation），是一个死胡同。它代表快乐变得停滞、过度，或者仅仅是物质上的奢华而缺乏灵性流动。

**In Readings**: Luxury, pleasure, stagnation, dissatisfaction, boredom, emotional fixation, needing new input.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Four of Cups shows pleasure losing purity through stabilization. Moon in Cancer is strong but indulgent. "Curse of Limitation" makes Four a dead stop. Seeds of decay enter fruit of pleasure.
- **中文**: Crowley的圣杯四展示快乐通过稳定化失去纯洁。月亮入巨蟹强大但放纵。"限制的诅咒"使四成为死胡同。腐败种子进入快乐果实。

**Narrative Snippets**:
- `[ns_thoth_cups_010]` `[trigger: four_cups_luxury]` `[factor_trigger: thoth_cups_four]` `[role: 主干]` Four of Cups = Lord of Luxury—Moon in Cancer implies abandonment to desire; lost original purity. → Core
- `[ns_thoth_cups_011]` `[trigger: seeds_decay]` `[factor_trigger: thoth_cups_four AND state_decay]` `[role: 条件分支]` Seeds of decay in fruit of pleasure—sea ruffled, cups unstable; pleasure becoming static. → Degradation
- `[ns_thoth_cups_012]` `[trigger: curse_limitation]` `[factor_trigger: thoth_cups_four AND principle_four]` `[role: 条件分支]` Four = Curse of Limitation, blind barren Cross, dead stop—imprisoning stabilization. → Number"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Cups: Luxury (圣杯四：奢华)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_four_001', 'tarot_stagnation', 'rel_cups_four_002', 'tarot_decay_seeds', 'l1_anchor', 'confidence', 'evi_cups_four_001', 'evi_cups_four_002', 'tarot_limitation', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_four_001', 'tarot_cups_four', 'astro_moon_cancer']
    
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
        l1_anchor="bot_v1.0.0_four_of_cups__luxury__圣杯四_奢华_001_L1",
    )
    version: str = "1.0.0"
