"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237860
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
    semantic_id="ap_v1.0.0_entry_14__geocentric_vs_helioc_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry14GeocentricVsHelioc(SemanticEntry):
    """
    **Source Text** (Lines 3082-3245):
> In archaic times men's concrete and significant experience of c...
    """
    
    original_text: str = """**Source Text** (Lines 3082-3245):
> In archaic times men's concrete and significant experience of celestial bodies was solely in terms of the light they gave...
>
> Nevertheless in modern astrology the geocentric and the heliocentric viewpoints are hopelessly mixed, and the basis of symbolism is lost sight of. The result is utter philosophical confusion...
>
> If we wish to use a heliocentric basis for our astrological symbolism, then many of the traditional concepts... must go overboard...
>
> From the heliocentric standpoint, the solar system is obviously to be considered as a whole... This orbit as a constant series of viewpoints is what we, in heliocentric symbolism, call the zodiac. Constellations are quite meaningless in themselves in such a symbolism...
>
> The truly intuitive person will recognize the absoluteness of this logic on internal evidence. But few are the men who... possess such a perfectly developed faculty: the faculty of holistic perception, the power to identify themselves with the wholeness of the wholes, and to release the significance of these wholes in terms of true and compelling symbols.

**Key Term Analysis**:
- **Geocentric basis**: `light experience` / `Sun as life-source` / `Moon cycles` / `constellations as constant patterns`
- **Heliocentric basis**: `solar system as whole` / `zodiac = Earth orbit viewpoints` / `constellations meaningless`
- **No mixing**: `philosophical confusion from mixing` / `each plane separate` / `consistent data use`
- **Holistic perception**: `few possess` / `identify with wholeness` / `release significance in symbols`

**English Paraphrase (Primary Language)**:
Rudhyar distinguishes geocentric (archaic, based on light experience) and heliocentric (modern, based on solar system as whole) symbolism. Modern astrology mixes them, causing "utter philosophical confusion."

In heliocentric symbolism: zodiac = Earth's orbit as series of viewpoints; constellations are "meaningless in themselves"; planets relate to Sun by position, distance, mass. Each viewpoint must be used consistently—never mixed.

The chapter concludes: "few possess the faculty of holistic perception, the power to identify themselves with the wholeness of the wholes, and to release the significance of these wholes in terms of true and compelling symbols." Buddha, Lao-Tze, Jesus exemplified this.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar区分了地心（古代，基于光经验）和日心（现代，基于太阳系作为整体）符号论。现代占星学混淆两者，导致"彻底的哲学混乱"。

在日心符号论中：黄道=地球轨道作为一系列视角；星座"本身没有意义"；行星通过位置、距离、质量与太阳相关。每种视角必须一致使用——绝不混淆。

章节总结："少有人拥有整体性感知的能力，与整体的整体性认同，并以真实而有说服力的符号释放这些整体的意义。"佛陀、老子、耶稣体现了这一点。

**Narrative Snippets**:
- `[ns_aop_107]` `[trigger: geocentric_basis]` `[factor_trigger: astro_geocentric]` `[role: 主干]` Geocentric: based on light experience, Sun as life-source, Moon cycles, constellations. → L3082-3108
- `[ns_aop_108]` `[trigger: heliocentric_basis]` `[factor_trigger: astro_heliocentric]` `[role: 主干依赖]` Heliocentric: solar system as whole, zodiac = orbit viewpoints, constellations meaningless. → L3171-3203
- `[ns_aop_109]` `[trigger: no_mixing]` `[factor_trigger: astro_no_mix AND astro_dual_sym]` `[role: 条件分支]` Mixing viewpoints causes philosophical confusion; each plane must be consistent. → L3136-3141
- `[ns_aop_110]` `[trigger: few_possess]` `[factor_trigger: astro_few_possess]` `[role: 总结]` Few possess holistic perception—power to identify with wholeness and release significance. → L3235-3245"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 14: Geocentric vs Heliocentric Symbolism"
    factor_refs: list = ['astro_geocentric', 'astro_heliocentric', 'astro_no_mixing']
    
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
        l1_anchor="ap_v1.0.0_entry_14__geocentric_vs_helioc_001_L1",
    )
    version: str = "1.0.0"
