"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237991
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
    semantic_id="ap_v1.0.0_entry_3__day_and_year_individu_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3DayAndYearIndividu(SemanticEntry):
    """
    **Source Text** (Lines 6020-6046):
> Day and Year—Individual and Collective: The collective meaning ...
    """
    
    original_text: str = """**Source Text** (Lines 6020-6046):
> Day and Year—Individual and Collective: The collective meaning of the year-cycle will be more evident if we realize that because of the inclination of the Earth's axis... the angle of incidence of the Sun rays varies throughout the year, causing the change of seasons. Seasons and climates affect the collective being and consciousness of human races and groups...
>
> The "day" is always the unit of selfhood. The self of collective Man operates through a basic unit: the orbital cycle. The self of an individual man operates through a basic unit: the axial-rotation cycle.

**Key Term Analysis**:
- **Day cycle (axial rotation)**: `unit of individual selfhood` / `24-hour cycle` / `rotation around Earth axis`
- **Year cycle (orbital revolution)**: `unit of collective selfhood` / `seasons, climates` / `affects physiological growth`
- **Day of the Lord**: `year = day for collective consciousness` / `biblical symbolism`

**English Paraphrase (Primary Language)**:
The year cycle is collective: seasons/climates affect races and groups physiologically, tied to orbital revolution. The day cycle is individual: the unit of personal selfhood, tied to axial rotation.

"The 'day' is always the unit of selfhood. The self of collective Man operates through... the orbital cycle. The self of an individual man operates through... the axial-rotation cycle."

**Complete Chinese Interpretation (Secondary Language)**:
年周期是集体性的：季节/气候通过轨道公转影响种族和群体的生理。日周期是个体性的：个人自性的单位，与轴向旋转相关。

"'日'始终是自性的单位。集体人类的自性通过……轨道周期运作。个体人类的自性通过……轴向旋转周期运作。"

**Narrative Snippets**:
- `[ns_aop_138]` `[trigger: day_individual]` `[factor_trigger: astro_cycle_day AND astro_day_year]` `[role: 主干]` Day cycle: unit of individual selfhood, axial rotation, personal consciousness. → L6043-6045
- `[ns_aop_139]` `[trigger: year_collective]` `[factor_trigger: astro_cycle_year AND astro_day_year AND astro_two_motions]` `[role: 主干依赖]` Year cycle: unit of collective selfhood, orbital revolution, seasonal/climatic influence. → L6022-6028"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Day and Year—Individual and Collective Cycles"
    factor_refs: list = ['cycle_day', 'cycle_year']
    
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
        l1_anchor="ap_v1.0.0_entry_3__day_and_year_individu_001_L1",
    )
    version: str = "1.0.0"
