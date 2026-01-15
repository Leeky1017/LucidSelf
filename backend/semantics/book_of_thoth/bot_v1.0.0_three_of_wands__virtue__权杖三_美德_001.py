"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088800
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
    semantic_id="bot_v1.0.0_three_of_wands__virtue__权杖三_美德_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class ThreeOfWandsVirtue权杖三美德(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Binah in Fire | Understanding in Fire | Mother receives Will |
| Sun in Aries | Exalted Sun position | Spring vitality |
| Virtue | Power/efficacy (Latin vir) | Masculine force |
| Lotus Wands | Blossoming symbols | Harmonious growth |

**Title**: Lord of Virtue (美德之主)
**Qabalistic**: Binah in Fire (火中之理解)
**Astrological**: Sun in Aries (太阳入白羊座)

**Source Text**:
> "This card refers to Binah in the suit of Fire, and so represents the establishment of primeval Energy. The Will has been transmitted to the Mother, who conceives, prepares, and gives birth to, its manifestation. It refers to the Sun in Aries... The meaning is harmonious, for this is the beginning of Spring. ... The Sun has enkindled the Great Mother."

**English Paraphrase**:
**Established Energy** - Corresponds to Binah (Understanding/Mother) in Fire. The primeval energy/Will (from the Two) is now **transmitted to the Mother**, who gives it form and birth. Ruled by the **Sun in Aries** (exalted), it represents harmony and the **beginning of Spring**. The wands take the form of blossoming Lotuses. It is the "Virtue" (manhood/power) of the Sun enkindling the Great Mother, representing successful establishment and initial fruition.

**Core**: **Harmonious Success** - Energy finding form, integrity, beginning of manifestation, self-assertion with dignity.

**Chinese Explanation**:
**权杖三（美德）**对应火元素中的Binah（理解/母亲），代表原始能量的**确立**。意志已被传达给母亲，由她孕育、准备并赋予其显化。对应**太阳在白羊座**（旺相），象征和谐与**春天的开始**。权杖呈现为盛开的莲花形状。这是太阳点燃了伟大的母亲，代表能量成功转化为形式，具有"美德"（Virtue，源自拉丁语Vir，意为男性的力量/效能）。

**In Readings**: Established strength, success, integrity, new beginnings (Spring), harmony, fruition of will, confidence.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Three of Wands represents Will transmitted to Mother (Binah) for manifestation. Sun in Aries (exalted) marks spring's beginning. "Virtue" derives from Latin vir (man/power), meaning efficacy not morality. Harris depicts blossoming lotus wands.
- **中文**: Crowley的权杖三代表意志传递给母亲（Binah）以实现显化。太阳入白羊（旺相）标志春天开始。"美德"源自拉丁语vir（男性/力量），意为效能而非道德。Harris描绘盛开的莲花权杖。

**Narrative Snippets**:
- `[ns_thoth_wands_007]` `[trigger: three_wands_virtue]` `[factor_trigger: thoth_wands_three]` `[role: 主干]` Three of Wands = Lord of Virtue—Will transmitted to Mother (Binah) who conceives and gives birth. → Core
- `[ns_thoth_wands_008]` `[trigger: sun_aries_exalted]` `[factor_trigger: thoth_wands_three AND planet_sun_aries]` `[role: 条件分支]` Sun in Aries (exalted)—beginning of Spring; Sun enkindling Great Mother; harmony. → Astrological
- `[ns_thoth_wands_009]` `[trigger: lotus_wands]` `[factor_trigger: thoth_wands_three AND symbol_lotus_wand]` `[role: 条件分支]` Blossoming lotus wands—established primeval energy finding harmonious form; Virtue as power/efficacy. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Wands: Virtue (权杖三：美德)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_three_001', 'tarot_established_energy', 'rel_wands_three_002', 'tarot_manifestation', 'l1_anchor', 'confidence', 'evi_wands_three_001', 'evi_wands_three_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_three_001', 'tarot_wands_three', 'astro_sun_aries']
    
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
        l1_anchor="bot_v1.0.0_three_of_wands__virtue__权杖三_美德_001_L1",
    )
    version: str = "1.0.0"
