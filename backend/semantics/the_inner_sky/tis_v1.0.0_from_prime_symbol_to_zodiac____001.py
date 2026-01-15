"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134394
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
    semantic_id="tis_v1.0.0_from_prime_symbol_to_zodiac____001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class FromPrimeSymbolToZodiac(SemanticEntry):
    """
    **Source Text**:
Two physical motions, both circular, lie at the roots of astrological symbolism. On...
    """
    
    original_text: str = """**Source Text**:
Two physical motions, both circular, lie at the roots of astrological symbolism. One is the rotation of the earth on its axis. The second is the revolution of the earth in its orbit around the sun. The first motion produces the houses. We discuss those in a later chapter. The second circle gives rise to the symbolism of the signs. And it is through the signs that the prime symbol comes down to earth.
...
Astrology really has nothing to do with the stars themselves. It is based solely on these variations in light, or, more simply, on the seasons.
...
Seasonal changes, then, not stars, are at the heart of sign symbolism. Through variations in the length of night, we mark four critical points that help us divide the circle. Infinity is broken down into four finite phases, each with its own distinctive character.
We call these four phases elements.
Fire, Earth, Air, and Water. The elements. Images from antiquity. Four primal states of being. Four faces of the universe. Within us they exist as states of consciousness. Beyond us they function as templates for all physical and metaphysical processes.

**Key Term Analysis**:
- `circle of the year`: the annual revolution of earth around the sun, forming the basis of sign symbolism.
- `seasons not stars`: sign meanings derive from seasonal light cycles rather than fixed constellations.
- `four critical points`: the solstices and equinoxes that divide the annual circle.
- `elements as phases`: Fire, Earth, Air, Water as four seasonal phases and states of consciousness.

**English Paraphrase (Primary Language)**:
Forrest brings the prime symbol down from the abstract sphere of the sky to the practical circle of the year. Two circular motions lie at the root of astrology: earth’s daily rotation, which produces the houses, and earth’s yearly revolution, which produces the signs. It is through this second motion—the changing relationship between sun and earth over the year—that the sky’s vastness becomes a usable symbolic system.

He argues that astrology is not fundamentally about the stars as clusters of points, but about variations in light, which we experience as seasons. Changes in the length of day and night carve the year into four critical turning points: the equinoxes and solstices. These crises break the abstract circle into four phases, each with a distinct energetic quality. Those phases are the elements: Fire, Earth, Air, and Water. They are not just old images from antiquity, but four basic states of being. Inside us they appear as states of consciousness; outside us they serve as templates for processes in the physical and metaphysical worlds.

**Complete Chinese Interpretation (Secondary Language)**:
在说明完「天空」这个原始象征之后，Forrest 把视角收束到一年一度的循环，让象征真正「落地」。一切占星符号的根源，是两个圆周运动：地球自转与地球公转。自转带来昼夜交替，对应宫位体系；绕日公转带来一年四季的更替，对应星座体系。正是通过这一年的循环，抽象的「天空球体」被转换成我们可以直观感受与使用的符号结构。

他明确提出，占星「其实与星星本身关系不大」，真正的基础是光线长短的变化，也就是四季。随着昼夜长短的起伏，一年当中会出现四个关键转折点——春分、夏至、秋分与冬至，它们把原本无限的圆切分成四个「有限阶段」，每一阶段都有鲜明的气质。这四个阶段，就是传统所说的四元素：火、土、风、水。它们不仅是古老的想象，而是四种原初存在状态、宇宙的四个侧面：在我们内在体现为四类意识状态，在我们之外则像模版一样，映射到各种物质与「形而上」过程之中。

**Core Points**:
- The daily rotation produces houses; the yearly revolution produces signs.
- Sign symbolism is rooted in seasonal light cycles, not in the shapes of constellations.
- Four turning points in the year divide the circle into four elemental phases.
- Fire, Earth, Air, and Water function as both seasonal phases and states of consciousness.

**Detailed Explanation**:
This section builds a bridge between the prime symbol and the concrete mechanics of the zodiac. By tying signs to the circle of the year, Forrest reframes them as experiential responses to changing light, temperature, and seasonal mood, rather than as projections onto distant constellations. This removes a common objection from astronomers—"the constellations have shifted"—by clarifying that the real referent is the cycle of seasons.

The four elements emerge as a structured way of summarizing the year’s rhythm. Each element represents a distinct mode of being—initiating, stabilizing, relating, or deepening—that arises from how light and dark interact at that phase. Treating elements as states of consciousness aligns astrological language with psychological phenomenology: we can describe how a person tends to experience and respond to life, not only which season they were born into. For calibration, this makes the element layer a crucial bridge between raw astronomical cycles and lived inner states.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The contrast "seasons, not stars" is made explicit, since it encapsulates Forrest’s corrective to popular misunderstandings. References to "two physical motions" and "four critical points" are preserved, while details of astronomical mechanics are lightly compressed to keep focus on symbolic consequences.
- **中文**：译文有意强化「自转 = 宫位、公转 = 星座」这一对照，方便后续在教学与引擎中调用；同时把 "images from antiquity" 扩展为「不只是古老想象，而是四种原初存在状态」，以贴合中文读者对「元素」一词常见的玄学化印象，并把它重新拉回经验与意识层面。

**Narrative Snippets**:
- `[ns_inner_sky_season_001]` `[trigger: seasonal_zodiac]` `[factor_trigger: seasonal_zodiac AND element_system]` `[role: 主干]` Seasonal changes, not stars, are at the heart of sign symbolism—through variations in light we mark four critical points that divide the circle into Fire, Earth, Air, and Water. → Forrest Ch.4 #Zodiac"""
    normalized_text_zh: str = """"""
    subject: str = "From Prime Symbol to Zodiac – Circle of the Year and Elements"
    factor_refs: list = ['source_ref', 'rel_inner_sky_season_001', 'seasonal_zodiac', 'evi_inner_sky_season_001', 'rule_seasonal_signs', 'concept_seasonal_cycle', 'jieqi_system', 'dream_seasonal']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_from_prime_symbol_to_zodiac____001_L1",
    )
    version: str = "1.0.0"
