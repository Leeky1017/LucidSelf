"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251379
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
    semantic_id="pit_v1.0.0_transit_concept__行运概念_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class TransitConcept行运概念(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "A transit occurs when a moving planet forms an aspect by...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "A transit occurs when a moving planet forms an aspect by degree to a point in the natal horoscope. The transiting planet activates the natal planet or point, bringing its symbolism into manifestation through external circumstances and internal psychological pressure. Transits are not events themselves but symbols of the intentions that create events."

**English Paraphrase (Primary Language)**:
A **transit** is the fundamental mechanism of predictive astrology: a currently moving (transiting) planet forms an aspect—conjunction, sextile, square, trine, opposition—to a planet or point in the natal birth chart. This aspect creates an **activation**: the transiting planet's energy catalyzes the natal planet's inherent potential, bringing what was latent into manifest expression. Hand emphasizes transits are **symbolic, not causal**. They don't make events happen through external force but represent the natural timing when internal intentions and potentials ripen into external manifestation. The natal chart shows what you are (character, potentials, patterns); transits show **when** those patterns naturally tend to express themselves.

**Complete Chinese Interpretation (Secondary Language)**:
**行运**是预测占星的核心激活机制：一颗正在运行的行星（行运行星）在黄道上走到与本命盘中某个行星或关键点形成精确相位（合相、六合、四分、三分、对分）的位置时，就像按下了那颗本命行星对应的键——原本潜伏在性格与命局中的倾向被强行调到前台，要求被体验、被处理。汉德特别强调：行运本身并不"制造事件"，而是像表盘一样，标记出**内在意图与潜能成熟到需要外显的时间点**，具有强烈的象征性而非物理因果性。本命盘显示你是什么（性格、潜能、模式）；行运显示**何时**那些模式自然倾向于表达自己。

**Key Term Analysis**:
- **Transit**: `moving planet` / `aspect formation` / `activation trigger`
- **Activation**: `triggers latent potential` / `brings into manifestation` / `catalytic function`
- **Symbolic not Causal**: `timing not forcing` / `intention display` / `synchronistic`
- **Transit-to-Natal**: `personal activation` / `individual experience` / `natal potential`

**Core Points** (decomposed, no upper limit):
- Transit = moving planet aspects natal planet/point by degree
- Activation mechanism: external catalyst triggering natal potential into expression
- Symbolic not causal: represents timing of manifestation, not external forcing
- Transit-to-natal: personal activation (individual experience)
- Transit-to-transit: collective atmosphere (generation-wide influence)
- Timing principle: shows when natal potentials naturally express
- Natal chart = static (what); transits = dynamic (when)

**Detailed Explanation**:
The transit concept is foundational to all predictive astrology. While the natal chart is **static** (showing the permanent pattern at birth), transits are **dynamic** (showing how that pattern unfolds through time). This creates a two-layer interpretive system: natal potential (what) + transit timing (when). Imagine the natal chart as a keyboard with certain keys representing different potentials—career ambition (Saturn), relationship needs (Venus), aggressive drive (Mars), etc. Most keys remain silent most of the time. A transit is like a finger pressing a specific key—suddenly that potential sounds, becoming prominent in consciousness and circumstance.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_001]` `[trigger: transit_definition]` `[factor_trigger: astro_transit_mechanism AND astro_activation_function]` `[role: 主干]` A transit occurs when a moving planet forms an aspect to a point in the natal horoscope, activating its symbolism. → Source Text
- `[ns_hand_pit_002]` `[trigger: symbolic_not_causal]` `[factor_trigger: astro_synchronicity]` `[role: 主干依赖]` Transits are not events themselves but symbols of the intentions that create events. → Source Text
- `[ns_hand_pit_003]` `[trigger: activation_mechanism]` `[factor_trigger: astro_aspect_square AND astro_aspect_opposition]` `[role: 条件分支]` The transiting planet activates the natal planet, bringing its symbolism into manifestation through circumstances and psychological pressure. → Source Text
- `[ns_hand_pit_004]` `[trigger: natal_vs_transit]` `[factor_trigger: astro_timing_principle]` `[role: 总结]` The natal chart represents potentials; transits represent the times when those potentials seek actualization. → Source Text
- `[ns_pit_np]` `[trigger: natal_point]` `[factor_trigger: natal_point]` `[role: 主干]` Natal point is any planet, angle, or sensitive point in the birth chart that can be activated by transits. → PIT Foundation
- `[ns_pit_nj]` `[trigger: natal_jupiter]` `[factor_trigger: natal_jupiter]` `[role: 条件分支]` Natal Jupiter represents expansion, optimism, opportunity, growth, and philosophical understanding in the birth chart. → PIT Foundation
- `[ns_pit_nm]` `[trigger: natal_mars]` `[factor_trigger: natal_mars]` `[role: 条件分支]` Natal Mars represents drive, assertion, energy, anger, and physical vitality in the birth chart. → PIT Foundation
- `[ns_pit_ns]` `[trigger: natal_saturn]` `[factor_trigger: natal_saturn]` `[role: 条件分支]` Natal Saturn represents structure, limitation, responsibility, discipline, and maturation in the birth chart. → PIT Foundation
- `[ns_pit_nu]` `[trigger: natal_uranus]` `[factor_trigger: natal_uranus]` `[role: 条件分支]` Natal Uranus represents individuation, awakening, disruption, innovation, and freedom-seeking in the birth chart. → PIT Foundation
- `[ns_pit_nne]` `[trigger: natal_neptune]` `[factor_trigger: natal_neptune]` `[role: 条件分支]` Natal Neptune represents transcendence, dissolution, spirituality, illusion, and compassion in the birth chart. → PIT Foundation
- `[ns_pit_npl]` `[trigger: natal_pluto]` `[factor_trigger: natal_pluto]` `[role: 条件分支]` Natal Pluto represents transformation, power, regeneration, death/rebirth, and depth psychology in the birth chart. → PIT Foundation

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The transit concept is foundational to modern predictive astrology and widely accepted across schools.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。行运概念是现代预测占星的基础，在各流派中广泛接受。"""
    normalized_text_zh: str = """"""
    subject: str = "Transit Concept (行运概念)"
    factor_refs: list = ['astro_transit_mechanism', 'astro_activation_function', 'astro_symbolic_timing', 'astro_transit_to_natal', 'astro_synchronicity']
    
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
        l1_anchor="pit_v1.0.0_transit_concept__行运概念_001_L1",
    )
    version: str = "1.0.0"
