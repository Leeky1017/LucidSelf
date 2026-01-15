"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251460
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
    semantic_id="pit_v1.0.0_orb__effective_range___容许度_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class OrbEffectiveRange容许度(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "The orb is the degree range before and after an exact as...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "The orb is the degree range before and after an exact aspect within which the transit effect is felt. Typically 1-3 degrees for outer planets, wider for inner planets. The orb determines the duration of the transit's influence and marks the beginning and end of the effective period."

**English Paraphrase (Primary Language)**:
The **orb** is a technical but crucial parameter in transit interpretation: it defines the **effective range** (in degrees of arc) within which a transit aspect begins to be felt and continues to influence. An aspect is "exact" when the planets are at the precise degree; the orb extends before and after this exactitude. For **outer planets** (Saturn, Uranus, Neptune, Pluto), the typical orb is **1–3 degrees**—meaning Saturn's influence begins about 1–3 degrees before exact conjunction and continues 1–3 degrees after. For **inner planets** (Sun, Moon, Mercury, Venus, Mars), the orb is typically **wider**, sometimes 5–8 degrees, because these planets move faster and their effects are more immediate. The orb determines the **duration** of the transit: a Saturn transit with a 2-degree orb lasts roughly 2–3 weeks at exact, plus approach and departure phases, totaling several months of influence. Understanding orb is essential for **timing predictions** and knowing when a transit truly begins and ends.

**Complete Chinese Interpretation (Secondary Language)**:
**容许度**是行运解读中的技术性但关键参数：它定义了**生效范围**（以黄道度数计），在这个范围内行运相位开始被感受，并继续施加影响。相位"精确"是指行星处于精确度数；容许度则延伸到这个精确点之前和之后。对于**外行星**（土星、天王、海王、冥王），典型容许度是**1–3度**——意思是土星的影响在精确合相前约1–3度开始，在精确合相后1–3度继续。对于**内行星**（太阳、月亮、水星、金星、火星），容许度通常**更宽**，有时5–8度，因为这些行星运行更快，其效应更即时。容许度决定了行运的**持续时间**：一个土星行运，容许度2度，在精确点持续约2–3周，加上接近与离开阶段，总共数月的影响。理解容许度对**时间预测**和知道行运何时真正开始和结束至关重要。

**Key Term Analysis**:
- **Orb**: `degree range` / `effective period` / `before and after exact`
- **Outer Planets**: `1-3 degrees` / `slow-moving` / `longer duration`
- **Inner Planets**: `wider orb` / `faster-moving` / `immediate effect`
- **Duration**: `weeks to months` / `approach-exact-departure` / `timing marker`

**Core Points** (decomposed, no upper limit):
- Orb = degree range before/after exact aspect where transit effects felt
- Outer planets typically 1–3 degrees orb
- Inner planets typically wider orb (5–8 degrees)
- Orb determines duration of transit influence
- Marks beginning and end of effective period
- Approach phase: building intensity
- Exact phase: maximum intensity
- Departure phase: fading influence
- Essential for accurate timing predictions

**Detailed Explanation**:
The orb concept transforms transit prediction from a single moment (exact aspect) into a **temporal window** with three phases. The **approach phase** begins when the transiting planet enters the orb—the person starts feeling the transit's pressure, though often unconsciously. The **exact phase** is the peak intensity—the moment of maximum activation. The **departure phase** continues after exactitude as the influence gradually fades. Understanding this three-phase structure helps clients recognize when a transit is beginning (sometimes weeks before exact) and when it's truly finished (sometimes weeks after). This prevents both premature conclusions ("It's over!") and prolonged anxiety ("Will it ever end?").

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_011]` `[trigger: orb_definition]` `[factor_trigger: astro_orb_range]` `[role: 主干]` The orb is the degree range before and after an exact aspect where transit effects are felt. → Source Text
- `[ns_hand_pit_012]` `[trigger: outer_planet_orb]` `[factor_trigger: astro_outer_planet_orb]` `[role: 主干依赖]` Outer planets typically have 1–3 degree orbs due to slow movement. → Source Text
- `[ns_hand_pit_013]` `[trigger: duration_window]` `[factor_trigger: astro_transit_duration]` `[role: 条件分支]` The orb determines the duration of transit influence across approach, exact, and departure phases. → English Paraphrase
- `[ns_hand_pit_014]` `[trigger: timing_precision]` `[factor_trigger: astro_orb_range]` `[role: 总结]` Understanding orb is essential for accurate timing predictions. → English Paraphrase
- `[ns_pit_cc]` `[trigger: casual_conversation]` `[factor_trigger: casual_conversation]` `[role: 效果]` Casual conversation and daily communication highlighted during Mercury and 3rd house transits. → PIT Foundation
- `[ns_pit_ht]` `[trigger: holding_tight]` `[factor_trigger: holding_tight]` `[role: 条件分支]` Holding tight to possessions or positions may occur during Saturn or 2nd house transits. → PIT Foundation
- `[ns_pit_hc]` `[trigger: hypercriticism]` `[factor_trigger: hypercriticism]` `[role: 效果]` Hypercriticism may emerge during Mercury-Saturn or 6th house transits. → PIT Foundation
- `[ns_pit_los]` `[trigger: losing]` `[factor_trigger: losing]` `[role: 效果]` Losing or letting go may be required during Pluto and 8th house transits. → PIT Foundation
- `[ns_pit_om]` `[trigger: opponent_manipulation]` `[factor_trigger: opponent_manipulation]` `[role: 条件分支]` Opponent manipulation may be encountered during Pluto and 7th house transits. → PIT Foundation
- `[ns_pit_pwp]` `[trigger: powerful_people]` `[factor_trigger: powerful_people]` `[role: 条件分支]` Encounters with powerful people occur during Pluto transits to angles or Sun. → PIT Foundation
- `[ns_pit_6hd]` `[trigger: sixth_house_denial]` `[factor_trigger: sixth_house_denial]` `[role: 条件分支]` Sixth house denial refers to avoiding necessary service or health attention. → PIT Foundation
- `[ns_pit_trb]` `[trigger: trouble]` `[factor_trigger: trouble]` `[role: 效果]` Trouble or difficulties may arise during challenging aspects from malefics. → PIT Foundation
- `[ns_pit_e12n]` `[trigger: eastern_12nian]` `[factor_trigger: eastern_12nian]` `[role: 条件分支]` Eastern 12-year cycle (木星周期) corresponds to Jupiter's orbital period. → Cross-System Mapping
- `[ns_pit_e12nz]` `[trigger: eastern_12nian_zhuanhuan]` `[factor_trigger: eastern_12nian_zhuanhuan]` `[role: 条件分支]` Eastern 12-year transition (流年转换) corresponds to Jupiter sign changes. → Cross-System Mapping
- `[ns_pit_e84n]` `[trigger: eastern_84nian]` `[factor_trigger: eastern_84nian]` `[role: 条件分支]` Eastern 84-year cycle corresponds to Uranus orbital period—generational pattern. → Cross-System Mapping
- `[ns_pit_edy]` `[trigger: eastern_dayun]` `[factor_trigger: eastern_dayun]` `[role: 条件分支]` Eastern great fate period (大运) corresponds to secondary progressions or major transits. → Cross-System Mapping
- `[ns_pit_edyz]` `[trigger: eastern_dayun_zhuanhuan]` `[factor_trigger: eastern_dayun_zhuanhuan]` `[role: 条件分支]` Eastern dayun transition (大运转换) corresponds to major planetary cycle shifts. → Cross-System Mapping
- `[ns_pit_egm]` `[trigger: eastern_geren_ming]` `[factor_trigger: eastern_geren_ming]` `[role: 条件分支]` Eastern personal fate (个人命) corresponds to natal chart potentials. → Cross-System Mapping
- `[ns_pit_emd]` `[trigger: eastern_mingju_dise]` `[factor_trigger: eastern_mingju_dise]` `[role: 条件分支]` Eastern fate structure color (命局底色) corresponds to chart overall tone. → Cross-System Mapping
- `[ns_pit_esy]` `[trigger: eastern_shidai_yun]` `[factor_trigger: eastern_shidai_yun]` `[role: 条件分支]` Eastern era fate (时代运) corresponds to outer planet generational transits. → Cross-System Mapping
- `[ns_pit_exy]` `[trigger: eastern_xiaoyun]` `[factor_trigger: eastern_xiaoyun]` `[role: 条件分支]` Eastern small fate period (小运) corresponds to inner planet transits. → Cross-System Mapping

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Orb conventions vary slightly among astrologers; Hand's 1–3 degrees for outer planets is standard in modern predictive astrology.
- **中文**: 容许度的约定在占星师之间略有不同；Hand的外行星1–3度是现代预测占星的标准。"""
    normalized_text_zh: str = """"""
    subject: str = "Orb (Effective Range) (容许度)"
    factor_refs: list = ['astro_orb_range', 'astro_outer_planet_orb', 'astro_inner_planet_orb', 'astro_transit_duration', 'astro_approach_phase']
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_orb__effective_range___容许度_001_L1",
    )
    version: str = "1.0.0"
