"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237782
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
    semantic_id="ap_v1.0.0_entry_6__celestial_bodies_as_m_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry6CelestialBodiesAsM(SemanticEntry):
    """
    **Source Text** (Lines 2060-2130):
> The function of astrology was to bring into the chaos of the na...
    """
    
    original_text: str = """**Source Text** (Lines 2060-2130):
> The function of astrology was to bring into the chaos of the natural world on Earth the supreme order of which celestial revolutions are so conspicuous and psychologically exalting a manifestation. Chaos and imprevisibility and blind chance on Earth; but above in the heavens, perfect order, previsibility, law. Astrology took its significance from such a contrast. The skies were regarded as a cosmic measuring device, an archetypal paragon of order, which could be juxtaposed with any system of natural phenomena.
>
> The complete set of planetary, solar, lunar and stellar revolutions, as seen from the Earth, has ever served in astrology as a complex many-dimensional yard-stick and as a clock, in order to determine the periodical behavior of natural organisms...
>
> Does the cosmic measuring rod and timepiece combined—the birth-chart—mean in itself anything substantial? Not in the least—no more than any yard-stick or clock. It is merely a symbol of measurement. Unless we know first of all what it is we want to measure, we shall know nothing practical after having measured—only a set of algebraic symbols on a wheel.
>
> Jupiter and Mars do not mean anything concrete whatsoever. They mean no more, no less, than 3 and 4, or a spiral and a straight line, or m and p.

**Key Term Analysis**:
- **Skies as measuring device**: `cosmic yard-stick` / `archetypal paragon of order` / `clock`
- **Order vs chaos contrast**: `Earth = chaos` / `Heavens = order` / `juxtaposition brings order`
- **Chart as symbol of measurement**: `no substantial meaning` / `like yard-stick or clock` / `needs content to apply`
- **Planets as pure symbols**: `Jupiter, Mars = 3, 4` / `no concrete meaning` / `conventional signs`

**English Paraphrase (Primary Language)**:
Rudhyar radically reframes astrology's mechanism. The heavens function as a "cosmic measuring device, an archetypal paragon of order"—not as sources of influence. The contrast: Earth = chaos, unpredictability; Heavens = perfect order, law. Astrology's function was to juxtapose this celestial order onto earthly phenomena, thereby bringing coherence.

The birth-chart is "merely a symbol of measurement"—no more substantial than a yard-stick or clock. Without knowing what we're measuring, we have only "algebraic symbols on a wheel." Jupiter and Mars "do not mean anything concrete whatsoever"—they're like numbers (3, 4) or letters (m, p), pure conventional signs.

This demolishes the "planetary influence" model entirely. Planets don't cause anything; they mark positions in a measuring system that humans apply to bring order to experience.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar根本性地重构了占星学的机制。天空作为"宇宙测量工具，秩序的原型典范"——而非影响的来源。对比是：地球=混沌、不可预测；天空=完美秩序、法则。占星学的功能是将这种天体秩序并置于地球现象，从而带来连贯性。

出生图"仅仅是测量的符号"——不比尺子或时钟更有实质。不知道我们在测量什么，我们只有"轮盘上的代数符号"。木星和火星"根本没有任何具体含义"——它们像数字（3、4）或字母（m、p），纯粹的常规符号。

这完全摧毁了"行星影响"模型。行星不导致任何事；它们标记人类用来给经验带来秩序的测量系统中的位置。

**Core Points**:
- Heavens = cosmic measuring device, paragon of order
- Earth = chaos; Heavens = order—contrast is key
- Astrology juxtaposes celestial order onto phenomena
- Birth-chart = symbol of measurement, like yard-stick/clock
- No substantial meaning without content to measure
- Jupiter, Mars = pure symbols like numbers or letters
- Demolishes planetary influence model
- Planets mark positions, don't cause

**Narrative Snippets**:
- `[ns_aop_077]` `[trigger: measuring_device]` `[factor_trigger: measuring_rod AND heavens_order AND astro_measure_sys AND astro_order_jux]` `[role: 主干]` Skies = cosmic measuring device, archetypal paragon of order—not influence source. → L2067-2072
- `[ns_aop_078]` `[trigger: yardstick_clock]` `[factor_trigger: astro_yardstick]` `[role: 主干依赖]` Birth-chart = symbol of measurement, no more substantial than yard-stick or clock. → L2098-2102
- `[ns_aop_079]` `[trigger: pure_symbols]` `[factor_trigger: astro_pure_sym AND astro_pure_sym_state]` `[role: 条件分支]` Jupiter, Mars mean nothing concrete—like 3, 4, m, p—pure conventional signs. → L2105-2107
- `[ns_aop_080]` `[trigger: needs_content]` `[factor_trigger: astro_needs_content]` `[role: 总结]` Without knowing what to measure, only algebraic symbols on wheel. → L2100-2103"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 6: Celestial Bodies as Measuring Device—Not Influence"
    factor_refs: list = ['astro_cosmic_measure', 'astro_order_chaos', 'astro_pure_planets', 'astro_content_req']
    
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
        l1_anchor="ap_v1.0.0_entry_6__celestial_bodies_as_m_001_L1",
    )
    version: str = "1.0.0"
