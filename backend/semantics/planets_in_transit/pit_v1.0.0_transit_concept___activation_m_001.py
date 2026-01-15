"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.199812
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
    semantic_id="pit_v1.0.0_transit_concept___activation_m_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class TransitConceptActivationM(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Transit | Moving planet ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Transit | Moving planet aspects natal | Activation mechanism |
| Activation | Triggers latent potential | Core predictive function |
| Symbolic not Causal | Timing not forcing | Hand's philosophy |
| Transit-to-Natal | Personal experience | Individual activation |

#### Source Text

"A transit occurs when a moving planet forms an aspect by degree to a point in the natal horoscope. The transiting planet activates the natal planet or point, bringing its symbolism into manifestation through external circumstances and internal psychological pressure. Transits are not events themselves but symbols of the intentions that create events. The natal chart represents potentials; transits represent the times when those potentials seek actualization."

#### English Paraphrase (Primary Language)

A **transit** is the fundamental mechanism of predictive astrology: a currently moving (transiting) planet forms an aspect—conjunction, sextile, square, trine, opposition—to a planet or point in the natal birth chart. This aspect creates an **activation**: the transiting planet's energy catalyzes the natal planet's inherent potential, bringing what was latent into manifest expression.

Hand emphasizes transits are **symbolic, not causal**. They don't make events happen through external force but represent the natural timing when internal intentions and potentials ripen into external manifestation. The natal chart shows what you are (character, potentials, patterns); transits show **when** those patterns naturally tend to express themselves.

**Key distinction**: Transit-to-natal (transiting planet aspects natal planet) activates **personal** potential. Transit-to-transit (two transiting planets aspect each other) creates **collective** atmospheric conditions affecting everyone born in any era.

The activation works both psychologically (internal pressure to express natal potential) and circumstantially (external events providing opportunities/challenges matching natal themes).

#### Complete Chinese Interpretation (Secondary Language)

在罗伯特·汉德的体系里，“行运”不是一个松散的时间标签，而是**预测占星的核心激活机制**：一颗正在运行的行星（行运行星）在黄道上走到与本命盘中某个行星或关键点形成精确相位（合相、六合、四分、三分、对分）的位置时，就好像有人按下了那颗本命行星对应的键——原本潜伏在性格与命局中的倾向，被强行调到前台，要求被体验、被处理。

这种激活一方面体现在**心理层面**：你会突然更强烈地感受到某类需要、冲动、恐惧或渴望（例如土星行运到太阳，本命“责任与自我价值”的主题被推到聚光灯下）；另一方面，也体现在**外在情境**：与该主题相关的人事物密集出现，形成“逼你面对”的局面。汉德特别强调：行运本身并不“制造事件”，而是像表盘一样，标记出**内在意图与潜能成熟到需要外显的时间点**，具有强烈的象征性而非物理因果性。

因此需要区分两类行运：其一是**行运对本命（transit-to-natal）**，即行运行星与本命星形成相位，这是直接激活个人潜能的触发器；其二是**行运对行运（transit-to-transit）**，是两颗行运行星之间的相位，更多构成“时代氛围”或集体气候，所有人都会在各自本命过滤下感受到同一大背景。整体结构与中国术数中的**大运 / 流年**高度相似：本命盘是“命”，行运是“运”，行运只是在不同时间段把命局中早已写下的模式依次点亮。

#### Core Points

- **Transit**: Moving planet aspects natal planet/point by degree
- **Activation mechanism**: External catalyst triggering natal potential into expression
- **Symbolic not causal**: Represents timing of manifestation, not external forcing
- **Transit-to-natal**: Personal activation (individual experience)
- **Transit-to-transit**: Collective atmosphere (generation-wide influence)
- **Timing principle**: Shows when natal potentials naturally express

#### Detailed Explanation

The transit concept is foundational to all predictive astrology. While the natal chart is **static** (showing the permanent pattern at birth), transits are **dynamic** (showing how that pattern unfolds through time). This creates a two-layer interpretive system: natal potential (what) + transit timing (when).

**How activation works**: Imagine the natal chart as a keyboard with certain keys representing different potentials—career ambition (Saturn), relationship needs (Venus), aggressive drive (Mars), etc. Most keys remain silent most of the time. A transit is like a finger pressing a specific key—suddenly that potential sounds, becoming prominent in consciousness and circumstance.

**Example**: Natal Sun square Saturn suggests lifelong themes of authority conflict, self-discipline challenges, ambition blocked by reality. But this remains background potential until a transit activates it. When transiting Uranus squares natal Sun, the Sun "lights up"—suddenly career conflicts intensify, authority issues demand resolution, the person feels urgent pressure to break free from limitations. The Uranus transit didn't create the Sun-Saturn pattern (that's natal) but activated it into current prominence.

**Why symbolic, not causal**: Hand rejects the old notion that planets physically cause events through rays or emanations. Instead, transits are **synchronistic**—meaningful coincidences between planetary positions and human experience. The cosmos is a unified whole; planetary movements and human life follow the same patterns. Transits reveal when patterns naturally mature into expression.

**The intention framework**: Hand's deeper philosophy sees transits as showing when original intentions (formed before birth or in childhood) naturally manifest. If you unconsciously intended to learn discipline through struggle, Saturn transits provide those learning experiences. This raises consciousness—recognizing the transit as your own intention returns power and responsibility.

**East-West parallel**: This closely parallels Chinese **流年** (flowing year) and **大运** (great fortune) concepts—time periods when natal potentials (命局) activate into manifest circumstances (运程). Both systems see time as cyclic, with certain periods naturally suited to certain experiences.

**Narrative Snippets**:
- `[ns_transit_001]` `[trigger: transit_definition]` `[factor_trigger: astro_transit AND astro_aspect]` `[role: 主干]` A transit occurs when a moving planet forms an aspect to a point in the natal horoscope, activating its symbolism. → Source Text
- `[ns_transit_002]` `[trigger: symbolic_not_causal]` `[factor_trigger: astro_transit AND astro_symbolism]` `[role: 主干依赖]` Transits are not events themselves but symbols of the intentions that create events. → Source Text
- `[ns_transit_003]` `[trigger: activation_mechanism]` `[factor_trigger: astro_transit AND astro_natal]` `[role: 条件分支]` The transiting planet activates the natal planet, bringing its symbolism into manifestation through circumstances and psychological pressure. → Source Text
- `[ns_transit_004]` `[trigger: natal_vs_transit]` `[factor_trigger: astro_natal AND astro_transit]` `[role: 总结]` The natal chart represents potentials; transits represent the times when those potentials seek actualization. → Source Text
- `[ns_transit_005]` `[trigger: transit_keyboard]` `[factor_trigger: astro_transit AND astro_activation]` `[role: 总结]` A transit is like a finger pressing a specific key on the natal keyboard—suddenly that potential sounds, becoming prominent. → English Paraphrase
- `[ns_transit_006]` `[trigger: timing_function]` `[factor_trigger: astro_transit AND astro_timing]` `[role: 总结]` Transits reveal when patterns naturally mature into expression—timing, not forcing. → English Paraphrase

---"""
    normalized_text_zh: str = """"""
    subject: str = "Transit Concept - Activation Mechanism"
    factor_refs: list = []
    
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
        l1_anchor="pit_v1.0.0_transit_concept___activation_m_001_L1",
    )
    version: str = "1.0.0"
