"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238041
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
    semantic_id="ap_v1.0.0_entry_3__astrology_of_the_coll_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3AstrologyOfTheColl(SemanticEntry):
    """
    **Source Text** (Lines 6689-6796):
> 2. ASTROLOGY OF THE COLLECTIVE: This is, generally speaking, "n...
    """
    
    original_text: str = """**Source Text** (Lines 6689-6796):
> 2. ASTROLOGY OF THE COLLECTIVE: This is, generally speaking, "natural" or "mundane astrology," the type which was associated with the birth of human cultivation and culture... It deals with actual influences, with rays and magnetic currents which are said to emanate from Sun, stars and planets...
>
> Its approach is thus essentially objective, which makes it amenable to "scientific" treatment. That is to say, it is largely experimental. It develops by means of statistical judgments...
>
> In such a type of astrology the Sun occupies normally a most strikingly conspicuous position as the source of the life-force of the whole system. The approach is logically, in most cases, heliocentric.

**Key Term Analysis**:
- **Mundane astrology**: `natural astrology` / `seasons, climates, weather` / `rise and fall of nations`
- **Scientific approach**: `objective, experimental` / `statistical judgments` / `cosmic electro-dynamics`
- **Sun emphasis**: `source of life-force` / `heliocentric approach` / `equatorial forces`
- **Collective moods**: `human collectivities` / `physiological influences on psyche`

**English Paraphrase (Primary Language)**:
**Astrology of the Collective** = mundane/natural astrology. It deals with "actual influences, rays and magnetic currents" from celestial bodies—an objective, scientific, statistical approach. Sun is central as "source of the life-force." The approach is often heliocentric, dealing with equatorial forces.

This type affects "collective moods of men and nations" through physiological changes that react on the psyche—mainly emotions.

**Complete Chinese Interpretation (Secondary Language)**:
**集体占星学** = 世俗/自然占星。它处理来自天体的"实际影响、射线和磁流"——客观、科学、统计的方法。太阳居于中心作为"生命力的源泉"。这种方法通常是日心的，处理赤道力量。

这种类型通过反应于心理（主要是情绪）的生理变化影响"人类和国家的集体情绪"。

**Narrative Snippets**:
- `[ns_aop_149]` `[trigger: mundane_astrology]` `[factor_trigger: astro_mundane AND astro_mundane_func]` `[role: 主干]` Mundane astrology: objective, statistical, actual cosmic influences on collectivities. → L6700-6713
- `[ns_aop_150]` `[trigger: sun_emphasis]` `[factor_trigger: astro_sun_collective]` `[role: 主干依赖]` Sun as source of life-force, heliocentric approach, equatorial forces. → L6749-6760"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Astrology of the Collective—Mundane and Natural"
    factor_refs: list = ['astro_mundane', 'astro_natural']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_3__astrology_of_the_coll_001_L1",
    )
    version: str = "1.0.0"
