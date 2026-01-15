"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251521
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
    semantic_id="pit_v1.0.0_transit_to_natal_vs_transit_to_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class TransitToNatalVsTransitTo(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Transit-to-natal aspects (transiting planet to natal pla...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Transit-to-natal aspects (transiting planet to natal planet) activate personal potential and represent individual experience. Transit-to-transit aspects (two transiting planets) create the collective atmosphere or cosmic weather affecting everyone born in that era similarly."

**English Paraphrase (Primary Language)**:
Hand distinguishes two fundamentally different types of transit aspects, each with different scope and meaning. **Transit-to-natal** (transiting planet aspects natal planet) is **personal activation**—the transiting planet triggers your specific natal potential. This is individual experience: your Saturn transit, your Pluto transit. **Transit-to-transit** (two transiting planets aspect each other) is **collective atmosphere**—the cosmic weather affecting everyone born in that generation. For example, when transiting Saturn squares transiting Uranus, everyone experiences that square's tension; the effect is collective, not personal. Hand emphasizes that **personal transits** (transit-to-natal) are what astrology clients care about—"What does this mean for me?" **Collective transits** (transit-to-transit) provide background context but don't directly activate individual charts unless they also aspect natal planets.

**Complete Chinese Interpretation (Secondary Language)**:
汉德区分两种根本不同的行运相位类型，各有不同的范围和含义。**行运对本命**（行运行星与本命行星形成相位）是**个人激活**——行运行星触发你的特定本命潜能。这是个人体验：你的土星行运、你的冥王行运。**行运对行运**（两颗行运行星相互形成相位）是**集体氛围**——影响该世代所有人的宇宙天气。例如，当行运土星与行运天王星形成四分相，每个人都经历那个四分相的张力；效应是集体的，而非个人的。汉德强调**个人行运**（行运对本命）是占星客户关心的——"这对我意味着什么？"**集体行运**（行运对行运）提供背景语境，但除非它们也与本命行星形成相位，否则不会直接激活个人命盘。

**Key Term Analysis**:
- **Transit-to-Natal**: `personal activation` / `individual experience` / `natal potential trigger`
- **Transit-to-Transit**: `collective atmosphere` / `cosmic weather` / `generation-wide`
- **Personal vs Collective**: `individual scope` / `background context` / `direct activation`

**Core Points** (decomposed, no upper limit):
- Transit-to-natal = transiting planet aspects natal planet
- Personal activation of individual natal potential
- Individual experience: "What does this mean for me?"
- Transit-to-transit = two transiting planets aspect each other
- Collective atmosphere affecting entire generation
- Cosmic weather background context
- Transit-to-transit doesn't directly activate unless also aspects natal
- Personal transits are what clients care about
- Collective transits provide context but not direct impact

**Detailed Explanation**:
This distinction prevents confusion. A client asks, "What does Saturn square Uranus mean?" The astrologer must clarify: "Are you asking about transiting Saturn squaring your natal Uranus (personal), or about the current transiting Saturn-Uranus square (collective)?" The first directly affects you; the second affects everyone but doesn't specifically target your chart unless it also hits your natal planets.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_025]` `[trigger: transit_to_natal]` `[factor_trigger: astro_transit_to_natal AND astro_personal_activation]` `[role: 主干]` Transit-to-natal activates personal potential—individual experience. → Source Text
- `[ns_hand_pit_026]` `[trigger: transit_to_transit]` `[factor_trigger: astro_transit_to_transit AND astro_collective_atmosphere]` `[role: 主干依赖]` Transit-to-transit creates collective atmosphere affecting everyone similarly. → Source Text
- `[ns_hand_pit_027]` `[trigger: personal_vs_collective]` `[factor_trigger: astro_personal_vs_collective]` `[role: 总结]` Personal transits directly activate; collective transits provide background context. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The personal vs collective distinction is fundamental to modern transit interpretation.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。个人vs集体的区分是现代行运解读的基础。"""
    normalized_text_zh: str = """"""
    subject: str = "Transit-to-Natal vs Transit-to-Transit (行运对本命vs行运对行运)"
    factor_refs: list = ['astro_transit_to_natal', 'astro_transit_to_transit', 'astro_personal_activation', 'astro_collective_atmosphere']
    
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
        l1_anchor="pit_v1.0.0_transit_to_natal_vs_transit_to_001_L1",
    )
    version: str = "1.0.0"
