"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251476
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
    semantic_id="pit_v1.0.0_station__stationary_point___静止_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class StationStationaryPoint静止(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Station is the point where a planet appears motionless b...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Station is the point where a planet appears motionless before and after retrograde motion. It marks the maximum intensity of the transit—energy is concentrated, breakthrough or breakdown most likely. Station is the turning point where the transit's direction reverses."

**English Paraphrase (Primary Language)**:
The **station** (or stationary point) is a critical moment in transit interpretation: it's the point where a **retrograding planet appears to stop moving** before reversing direction. Due to Earth's orbital perspective, outer planets periodically appear to move backward (retrograde) in the zodiac. Just before turning retrograde and just after resuming direct motion, the planet appears **stationary**—motionless for a day or two. This apparent stillness represents **maximum concentration of energy**. Hand emphasizes that station is the **peak intensity point** of a transit: the pressure is greatest, the activation most acute. Psychologically, station often marks a **turning point or crisis moment**—a breakthrough (sudden clarity, decision, action) or breakdown (collapse, confrontation, forced change). Because energy is concentrated rather than flowing, station transits are often the most memorable and impactful moments in a transit cycle. A Saturn station might coincide with a major life decision; a Pluto station with a profound psychological transformation.

**Complete Chinese Interpretation (Secondary Language)**:
**静止点**（或称静止位置）是行运解读中的关键时刻：它是一颗**逆行行星在改变方向前后显现停止运动**的点。由于地球轨道视角，外行星周期性地在黄道上显现向后运动（逆行）。在转入逆行前和恢复顺行后，行星显现**静止**——一两天内不动。这种表观的静止代表**能量的最大集中**。汉德强调，静止点是行运的**最大强度点**：压力最大，激活最急。心理上，静止点常常标记**转折点或危机时刻**——突破（突然清晰、决定、行动）或崩溃（瓦解、对抗、被迫改变）。因为能量是集中而非流动的，静止点行运常常是行运周期中最难忘、最有影响的时刻。一个土星静止点可能与重大人生决定相吻合；一个冥王静止点与深刻的心理转化相吻合。

**Key Term Analysis**:
- **Station**: `apparent motionless` / `retrograde turning point` / `maximum intensity`
- **Retrograde**: `backward motion` / `Earth perspective` / `cyclical pattern`
- **Peak Intensity**: `concentrated energy` / `breakthrough/breakdown` / `turning point`
- **Crisis Moment**: `forced change` / `confrontation` / `transformation`

**Core Points** (decomposed, no upper limit):
- Station = point where planet appears motionless before/after retrograde
- Maximum intensity point of transit
- Energy concentrated rather than flowing
- Turning point or crisis moment often occurs
- Breakthrough (clarity, decision, action) or breakdown (collapse, confrontation)
- Most memorable and impactful moments in transit cycle
- Retrograde motion creates three-pass pattern (forward-retrograde-forward)
- Each pass deepens understanding and integration
- Station marks the reversal points in this cycle

**Detailed Explanation**:
Station is the **crescendo moment** in a transit's unfolding. While the approach phase builds pressure and the exact phase maintains intensity, the station concentrates all that energy into a single point. Psychologically, this often manifests as a **crisis or breakthrough**—a moment when you can no longer avoid the transit's issue, when something must give or transform. Clients often report that station moments coincide with major decisions, confrontations, or sudden insights. The retrograde cycle (forward-retrograde-forward) means the same transit aspect occurs three times over months, each pass deepening integration. Station marks the turning points in this cycle.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_015]` `[trigger: station_definition]` `[factor_trigger: astro_station_point]` `[role: 主干]` Station is where a planet appears motionless before and after retrograde motion. → Source Text
- `[ns_hand_pit_016]` `[trigger: maximum_intensity]` `[factor_trigger: astro_maximum_intensity]` `[role: 主干依赖]` Station marks the maximum intensity of the transit—energy is concentrated. → Source Text
- `[ns_hand_pit_017]` `[trigger: breakthrough_breakdown]` `[factor_trigger: astro_crisis_moment]` `[role: 条件分支]` Station often marks breakthrough or breakdown—a turning point or crisis moment. → Source Text
- `[ns_hand_pit_018]` `[trigger: retrograde_cycle]` `[factor_trigger: astro_retrograde_cycle]` `[role: 总结]` Retrograde creates three-pass pattern; station marks the turning points in this cycle. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Station as peak intensity is widely recognized in modern astrology; Hand emphasizes its psychological significance as turning point or crisis moment.
- **中文**: 静止点作为最大强度在现代占星中广泛认可；Hand强调其作为转折点或危机时刻的心理意义。"""
    normalized_text_zh: str = """"""
    subject: str = "Station (Stationary Point) (静止点)"
    factor_refs: list = ['astro_station_point', 'astro_maximum_intensity', 'astro_crisis_moment', 'astro_retrograde_cycle', 'astro_turning_point']
    
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
        l1_anchor="pit_v1.0.0_station__stationary_point___静止_001_L1",
    )
    version: str = "1.0.0"
