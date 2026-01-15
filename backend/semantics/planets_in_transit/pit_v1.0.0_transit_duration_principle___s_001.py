"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.200005
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
    semantic_id="pit_v1.0.0_transit_duration_principle___s_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class TransitDurationPrincipleS(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Transit Duration | Speed...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Transit Duration | Speed=depth | Slow=deep |
| Outer Planets | Years per aspect | Life-defining |
| Inner Planets | Days-weeks | Triggering |
| 大运/流年 Parallel | Time hierarchy | East-West bridge |

#### Source Text

"Faster planets produce briefer, lighter transits; slower planets produce longer, heavier transits. The Moon transiting natal Sun lasts hours and feels like a passing mood. Pluto transiting natal Sun lasts years and feels like death and rebirth of identity. Transit duration correlates directly with planetary speed and orb size, determining both the length of influence and depth of impact."

#### English Paraphrase (Primary Language)

**Transit duration principle**: The slower the transiting planet, the longer and deeper the impact. This creates a hierarchy of transit significance from Moon (fastest, lightest) to Pluto (slowest, deepest).

**Duration hierarchy**:

**Moon transits** (~2.5 days per sign, ~2-6 hours per aspect):
- Mood shifts, emotional fluctuations
- Timing daily activities, minor decisions
- "Weather" not "climate"—passing quickly

**Sun transits** (~30 days per sign, ~2-3 days per aspect):
- Weekly themes, temporary focus shifts
- Minor developments, brief emphasis

**Mercury/Venus/Mars** (~3-7 weeks per sign normally):
- Short-term developments (weeks to months)
- Communication/relationship/action themes
- Retrograde extends duration significantly

**Jupiter** (~1 year per sign, ~2-4 weeks per aspect):
- Annual growth themes
- Moderate importance, noticeable but not life-changing
- Multiple Jupiter transits per year

**Saturn** (~2.5 years per sign, months per aspect):
- **Major life developments**
- Reality tests, structure building
- Few Saturn transits simultaneously—each significant

**Uranus** (~7 years per sign, years per aspect):
- **Revolutionary life changes**
- Awakening, liberation themes
- Rare—only a few Uranus transits in a lifetime

**Neptune** (~14 years per sign, years per aspect):
- **Slow dissolution/spiritualization**
- Dream/illusion/transcendence themes  
- Generational—Neptune transits define era of life

**Pluto** (~12-30 years per sign, years per aspect):
- **Deepest transformation possible**
- Death-rebirth, power, collective forces
- Rarest personal transits—life-defining when they occur

**Practical hierarchy**: Inner planet transits set timing for outer planet themes. When Jupiter/Saturn/Uranus/Neptune/Pluto transits are active (slow background), inner planet transits (fast foreground) trigger specific events within that larger context.

**East-West parallel**: Chinese astrology similarly distinguishes **大运/流年/流月/流日** (great fortune 10-year / annual / monthly / daily) with slower cycles more foundational and faster cycles more triggering—same hierarchical time principle.

#### Complete Chinese Interpretation (Secondary Language)

“行运时长原则”把行星的天文学速度直接转译成心理与事件的**影响深度**：越慢的行星，在同一度数附近停留的时间越长，其象征主题在现实与内心中就越像一场“长期气候”；越快的行星，只是短暂掠过，更多像一阵天气。月亮几小时到半天就经过一个敏感点，只会带来心情、身体状态的轻微起伏；冥王星可能在同一度数附近徘徊一两年，其“死亡—重生”主题则会贯穿整段人生阶段。

因此，汉德建立起一个从月亮到冥王的**分层时间结构**：最慢的冥王、海王、天王与土星，定义的是时代性、阶段性的深层课题；中速的木星提供 12 年级别的扩张节律；更快的日、月、水、金、火则负责在这些长周期的背景上“点火”，把原本潜伏的大主题转化为具体事件与短期体验。这与中国命理中的**大运 / 流年 / 流月 / 流日**层级完全同构：大运给出大背景，流年定当年主题，流月流日具体触发。

掌握这一层级关系后，占星师在预测时就不会被短期行运的噪音牵着走，而是先看慢行星在哪些本命区域制造长期压力或机遇，再借助内行星行运来精确定位事件爆发与转折的窗口期。

#### Core Points

- **Speed = Duration + Depth**: Slower planets = longer transits = deeper impact
- **Hierarchy**: Moon (hours) → Sun (days) → Mercury/Venus/Mars (weeks) → Jupiter (weeks) → Saturn (months) → Uranus/Neptune/Pluto (years)
- **Inner planets trigger**: Fast transits activate slow transit themes
- **Outer planets define**: Slow transits provide background life themes
- **Practical timing**: Combine slow (what) + fast (when) for precision
- **East-West parallel**: Matches 大运/流年/流月/流日 time hierarchy"""
    normalized_text_zh: str = """"""
    subject: str = "Transit Duration Principle - Speed and Impact"
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
        l1_anchor="pit_v1.0.0_transit_duration_principle___s_001_L1",
    )
    version: str = "1.0.0"
