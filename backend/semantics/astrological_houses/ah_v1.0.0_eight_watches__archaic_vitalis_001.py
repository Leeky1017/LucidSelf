"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333608
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
    semantic_id="ah_v1.0.0_eight_watches__archaic_vitalis_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class EightWatchesArchaicVitalis(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Eight Watches | 3-hour p...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Eight Watches | 3-hour periods | Archaic division |
| Clockwise Sequence | Sun's apparent motion | Vitalistic |
| Solar Life-Force | Time defined by Sun | Cosmology |
| Agricultural Rhythm | Bio-solar cycles | Practical |

#### Source Text

"The archaic house system divided the day into eight three-hour periods or 'watches,' following the Sun's path clockwise from sunrise through culmination to sunset and midnight. This vitalistic system reflected agricultural rhythms and solar life-force, representing a simple division of the solar day into practical time segments."

#### English Paraphrase (Primary Language)

Ancient astrological traditions employed an eight-fold house division, with each "watch" spanning approximately three hours of the solar day. The sequence proceeded clockwise—the direction of the Sun's apparent motion—from dawn (sunrise) through noon (solar culmination) to dusk (sunset) and finally midnight (solar nadir). This eight-watch system embodied a vitalistic worldview centered on the Sun as life-giving force, with house divisions aligned to agricultural society's natural rhythms. The system represented an organic, life-centered approach where time divisions followed the solar cycle's biological and agricultural significance.

#### Complete Chinese Interpretation (Secondary Language)

古代占星传统采用八分宫位划分，每个"更"跨越太阳日约三小时。序列顺时针进行——太阳表观运动方向——从黎明(日出)经正午(太阳中天)到黄昏(日落)最后午夜(太阳下中天)。这种八更系统体现以太阳为生命赋予力量的活力世界观，宫位划分与农业社会自然节奏对齐。系统代表有机的、以生命为中心的方法，时间划分遵循太阳周期的生物和农业意义。八更系统反映**太阳中心**宇宙论，时间本身由太阳创造。顺时针运动(随太阳)是自然的、生命的方向。这与现代十二宫逆时针系统(随地球自转)形成对比。八更适合简单农业社会，日常节奏由太阳决定——黎明起床、正午休息、黄昏回家、午夜睡眠。

#### Core Points

- **Eight watches**: 3-hour periods dividing solar day
- **Clockwise sequence**: Follows Sun's apparent motion (sunrise→noon→sunset→midnight)
- **Vitalistic philosophy**: Sun as life-force, agricultural rhythms
- **Solar-dominant**: Time defined by Sun's position and biological cycles
- **Organic division**: Natural life rhythms vs mathematical abstractions

#### Detailed Explanation

Rudhyar describes the eight-watch system as humanity's earliest house division method, predating the twelve-house system by millennia. This octameral division created eight roughly equal time periods marking key moments in the solar day's agricultural and biological significance. Each three-hour watch corresponded to practical life activities: waking at dawn, working through morning, resting at noon, afternoon labor, evening gathering, early sleep, midnight rest, and pre-dawn preparation.

The clockwise direction is crucial—it follows the Sun's apparent path as seen from Earth, moving from east (sunrise) overhead (noon) to west (sunset) and beneath (midnight). This solar-centered directionality reflects a vitalistic cosmology where the Sun is supreme life-giver, and time itself is defined by solar position rather than abstract mathematical divisions.

This system served agricultural societies perfectly. Farmers rose with sunrise (first watch), worked through morning (second-third watches), rested at high noon (fourth watch), resumed labor (fifth-sixth watches), concluded work at sunset (seventh watch), and slept through night (eighth watch). The house system encoded practical daily rhythms essential to survival in agricultural communities, making astrology a living map of bio-solar life patterns.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Eight Watches (Archaic Vitalistic System)"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_eight_watches__archaic_vitalis_001_L1",
    )
    version: str = "1.0.0"
