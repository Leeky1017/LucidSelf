"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238131
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
    semantic_id="ap_v1.0.0_entry_2__the_zodiac_as_earth_s_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2TheZodiacAsEarthS(SemanticEntry):
    """
    **Source Text** (Lines 8003-8110):
> If the zodiac is a picture of the motions and relations of thes...
    """
    
    original_text: str = """**Source Text** (Lines 8003-8110):
> If the zodiac is a picture of the motions and relations of these men-cells within the Earth-body, then it follows logically that the signs of the zodiac represent anatomical divisions of the Earth-body... the zodiac is what astrologers-scientists call the "magnetic field" of the Earth, what occultists call the "aura of the Earth"...
>
> Alan Leo's Casting the Horoscope: "The zodiac that we use is really the Earth's Aura. It is a sphere or ovoid, the poles of which coincide with the poles of the Ecliptic..."
>
> The zodiac is the collective environment of the Earth... the placenta of the embryonic Earth-body. All the building energies which produce the growth of the embryo must pass through the placenta.

**Key Term Analysis**:
- **Zodiac as magnetic field**: `Earth's aura` / `collective environment` / `not rotating with Earth`
- **Placenta metaphor**: `building energies pass through` / `macrocosm vitalizes microcosm`
- **Ring-Pass-Not**: `theosophical term` / `boundary of Earth knowledge`
- **12 Gates**: `channels of universal energies` / `Holy City symbolism`

**English Paraphrase (Primary Language)**:
The zodiac = Earth's magnetic field/aura—a sphere polarized toward the ecliptic pole, NOT rotating with Earth. It's "the collective environment of the Earth," the "placenta of the embryonic Earth-body" through which all building energies pass.

"The zodiac is the Wall that separates all inhabitants of the Earth-surface from the universe... This Wall has twelve gates, twelve signs, twelve channels through which universal energies flow."

**Complete Chinese Interpretation (Secondary Language)**:
黄道 = 地球的磁场/灵光——一个朝向黄道极点极化的球体，不随地球旋转。它是"地球的集体环境"，"胚胎地球体的胎盘"，所有建造能量都通过它传递。

"黄道是将地球表面所有居民与宇宙隔开的墙……这堵墙有十二扇门，十二个星座，十二条宇宙能量流动的通道。"

**Narrative Snippets**:
- `[ns_aop_167]` `[trigger: zodiac_aura]` `[factor_trigger: astro_zodiac_as_aura AND astro_zodiac_aura]` `[role: 主干]` Zodiac as Earth's magnetic field/aura: collective environment, placenta of Earth-body. → L8013-8028
- `[ns_aop_168]` `[trigger: twelve_gates]` `[factor_trigger: astro_zodiac_gates AND astro_zodiac_aura]` `[role: 总结]` Zodiac as Wall with 12 gates, 12 channels of universal energy flow. → L8160-8166"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: The Zodiac as Earth's Aura"
    factor_refs: list = ['zodiac_aura', 'zodiac_gates']
    
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
        l1_anchor="ap_v1.0.0_entry_2__the_zodiac_as_earth_s_001_L1",
    )
    version: str = "1.0.0"
