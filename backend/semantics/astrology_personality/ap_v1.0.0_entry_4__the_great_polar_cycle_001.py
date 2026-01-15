"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238002
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
    semantic_id="ap_v1.0.0_entry_4__the_great_polar_cycle_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4TheGreatPolarCycle(SemanticEntry):
    """
    **Source Text** (Lines 6047-6127):
> The Great Polar Cycle: Besides these, there is another basic cy...
    """
    
    original_text: str = """**Source Text** (Lines 6047-6127):
> The Great Polar Cycle: Besides these, there is another basic cycle: the cycle of the precession of the equinoxes. It should rather be called the "Great Polar Cycle." It is created by a peculiar gyrating motion of the Earth's axis...
>
> This gyration does not mean a displacement of the center of the Earth. It belongs thus to our first category of "motion in time" or "subjective motion." But the "subject" here involved is the Individual whose physical center is one with the center of the Earth, that is to say, the great planetary Whole...
>
> These changes of planetary selfhood constitute the reality of what we call "Piscean Age," "Aquarian Age," etc...
>
> The polar motion... represents the essential manifestation of the creative factor in astrology.

**Key Term Analysis**:
- **Great Polar Cycle**: `precession of equinoxes` / `~25,868 years` / `gyrating motion of Earth's axis`
- **Pole Star changes**: `planetary selfhood modifies` / `attunes to different cosmic tones`
- **Astrological Ages**: `Piscean Age, Aquarian Age` / `result of polar axis direction changes`
- **Creative factor**: `polar motion = cosmic creativeness` / `cyclic outpouring of archetypes`

**English Paraphrase (Primary Language)**:
The Great Polar Cycle (~25,868 years) is the third fundamental Earth motion—the gyration of the polar axis causing precession of equinoxes. It represents "subjective motion" but for the planetary Whole. Pole Star changes mean planetary selfhood attunes to different cosmic tones—this is the reality behind "Piscean Age," "Aquarian Age."

The polar motion "represents the essential manifestation of the creative factor in astrology"—the cyclic outpouring of archetypes and primordial ideas.

**Complete Chinese Interpretation (Secondary Language)**:
大极点周期（约25,868年）是第三种基本地球运动——极轴的进动引起岁差。它代表"主观运动"但针对行星整体。极星变化意味着行星自性调谐到不同的宇宙音调——这是"双鱼座时代"、"水瓶座时代"背后的实在。

极点运动"代表占星学中创造性因素的本质显现"——原型和原初观念的周期性涌现。

**Narrative Snippets**:
- `[ns_aop_140]` `[trigger: polar_cycle]` `[factor_trigger: astro_cycle_polar AND astro_polar_cycle]` `[role: 主干]` Great Polar Cycle: ~25,868 years, gyrating axis, planetary selfhood, astrological ages. → L6049-6088
- `[ns_aop_141]` `[trigger: creative_factor]` `[factor_trigger: astro_creative_polar AND astro_polar_cycle]` `[role: 总结]` Polar motion = creative factor in astrology, cyclic outpouring of archetypes. → L6512-6521"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: The Great Polar Cycle—Cosmic Creative"
    factor_refs: list = ['cycle_polar', 'astro_ages']
    
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
        l1_anchor="ap_v1.0.0_entry_4__the_great_polar_cycle_001_L1",
    )
    version: str = "1.0.0"
