"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027397
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
    semantic_id="bot_v1.0.0_ten_of_cups__satiety__圣杯十_饱和_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TenOfCupsSatiety圣杯十饱和(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Malkuth in Water | Kingdom in Water | Completed work |
| Mars in Pisces | Disruption + flow | Agitation after fullness |
| Tilted Cups | Unstable vessels | Spilling perfection |
| Satiety | Over-fullness | Too much of good |

**Title**: Lord of Perfected Success (完满成功之主)
**Qabalistic**: Malkuth in Water (水中之王国)
**Astrological**: Mars in Pisces (火星入双鱼座)

**Source Text**:
> "This card represents a conflicting element. On the one hand, it receives the influence of the Ten, Malkah the Virgin. The arrangement of the cups is that of the Tree of Life. But, on the other hand, they are themselves unstable. They are tilted; they spill the water from the great Lotus which overhangs the whole system from one into the other. The work proper to water is complete: and disturbance is due. This comes from the influence of Mars in Pisces. Mars is the gross, violent and disruptive force which inevitably attacks every supposed perfection."

**English Paraphrase**:
**Too Much of a Good Thing** - Corresponds to Malkuth (Kingdom) in Water. The cups are arranged like the **Tree of Life**, showing perfected success, but they are **tilted and unstable**, spilling water from the overhanging lotus from one to another. Water's work is complete—there is nothing further to add—so disturbance must follow. With **Mars in Pisces**, a gross, disruptive force agitates an already saturated emotional field. This is **Satiety**: fullness tipping into boredom, overindulgence, or emotional overload, where success starts to feel heavy, dull, or unstable.

**Core**: **Over-Saturation** - Emotional fullness turning to restlessness, "too much", success that now feels heavy or unstable.

**Chinese Explanation**:
**圣杯十（饱和）**对应水元素中的Malkuth（王国/显化）。杯子的排列仿照**生命之树**，在形式上象征"完满成功"，但这些杯子**本身不稳定、向外倾斜**，从头顶巨莲中泼出的水不断在杯与杯之间溢出。水的工作已经完成，再继续只会带来扰动。再加上**火星入双鱼座**的影响——粗暴、破坏性的火闯入柔和、灵性的水领域——便形成一种**情感过度、饱和甚至厌倦**的局面：好事太多，反而失去新鲜感，隐含下一阶段的震荡预告。

**In Readings**: Satiety, emotional overload, "too much", domestic success that feels dull, restlessness after success, tipping point before change.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ten of Cups shows Water's work complete - disturbance is due. Mars in Pisces brings disruption to saturated field. Cups arranged as Tree of Life but tilted and spilling. Perfected success tips into boredom.
- **中文**: Crowley的圣杯十展示水的工作完成—扰动将至。火星入双鱼给饱和领域带来扰动。杯子按生命之树排列但倾斜溢出。完美成功转向乏味。

**Narrative Snippets**:
- `[ns_thoth_cups_028]` `[trigger: ten_cups_satiety]` `[factor_trigger: thoth_cups_ten]` `[role: 主干]` Ten of Cups = Lord of Perfected Success—Malkuth completes Water's work; disturbance is due. → Core
- `[ns_thoth_cups_029]` `[trigger: tilted_cups]` `[factor_trigger: thoth_cups_ten AND symbol_tilted_cups]` `[role: 条件分支]` Cups arranged as Tree of Life but tilted, unstable—spilling from overhanging lotus. → Visual
- `[ns_thoth_cups_030]` `[trigger: mars_disruption]` `[factor_trigger: thoth_cups_ten AND planet_mars_pisces]` `[role: 条件分支]` Mars in Pisces—gross disruptive force attacking supposed perfection; satiety invites change. → Astrological"""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Cups: Satiety (圣杯十：饱和)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_ten_001', 'tarot_over_fullness', 'rel_cups_ten_002', 'tarot_disturbance_due', 'l1_anchor', 'confidence', 'evi_cups_ten_001', 'evi_cups_ten_002', 'tarot_tilted_cups', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_ten_001', 'tarot_cups_ten', 'astro_mars_pisces']
    
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
        l1_anchor="bot_v1.0.0_ten_of_cups__satiety__圣杯十_饱和_001_L1",
    )
    version: str = "1.0.0"
