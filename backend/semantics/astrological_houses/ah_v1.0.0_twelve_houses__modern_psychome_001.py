"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333623
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
    semantic_id="ah_v1.0.0_twelve_houses__modern_psychome_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class TwelveHousesModernPsychome(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Twelve Houses | 30° sect...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Twelve Houses | 30° sectors | Modern system |
| Counterclockwise | Earth rotation | Psychomental |
| Four Angles | Asc/MC/Desc/IC | Cardinal cross |
| Life Arenas | Psychological domains | 12 distinctions |

#### Source Text

"Modern astrology employs twelve houses of 30 degrees each, proceeding counterclockwise from the Ascendant—opposite to the Sun's apparent motion. This reversal reflects Earth's rotation perspective and symbolizes the psychomental rhythm opposing the vitalistic. Individual consciousness unfolds from Ascendant through Midheaven to Descendant to IC, creating a person-centered rather than Sun-centered framework."

#### English Paraphrase (Primary Language)

Contemporary astrological practice divides the ecliptic into twelve equal sectors of thirty degrees each, beginning at the Ascendant and proceeding counterclockwise. This directionality opposes the Sun's clockwise apparent motion, instead following Earth's actual rotational direction. The twelve-house system embodies a psychomental paradigm where mental/psychological development takes precedence over biological/vitalistic rhythms. The sequence traces individual consciousness unfolding: self-awareness at the Ascendant, culmination in social achievement at the Midheaven, relationship encounter at the Descendant, and foundational roots at the IC. This creates an individual-centered cosmology where the person's psychological journey, not the Sun's life-giving motion, structures temporal experience.

#### Complete Chinese Interpretation (Secondary Language)

现代十二宫系统逆时针展开——地球自转方向——反映心智发展和个体意识演进，以人类心理成长而非太阳生命力为中心。十二分代表意识更细分化，从简单生命节奏(八更)到复杂心理精微(十二宫)。逆时针运动体现地球自转，强调地球(人类栖息地)而非太阳。每宫30度代表黄道十二星座对应，将天上星座模式投射到地上时间框架。这种**心智中心**系统适合个体化意识，宫位成为心理发展竞技场而非仅生命节奏标记。从第一宫(自我意识黎明)逆时针到第十二宫(意识溶解回归)，追踪完整的个体化旅程。

#### Core Points

- **Twelve houses**: 30° sectors, equal mathematical divisions
- **Counterclockwise sequence**: Follows Earth rotation, opposes Sun's motion
- **Psychomental focus**: Mental/psychological development vs biological rhythms
- **Individual-centered**: Person's consciousness journey vs solar life-force
- **Four-angle structure**: Asc→MC→Desc→IC traces consciousness unfoldment

#### Detailed Explanation

The shift from eight watches to twelve houses represents astrology's most profound paradigm revolution. The twelve-house system's counterclockwise directionality is revolutionary—it moves against the Sun's apparent path, following instead Earth's actual spin on its axis. This reversal symbolizes humanity's evolution from solar-dominated vitalistic consciousness to self-aware psychomental consciousness.

Where eight watches followed the Sun's life-giving motion clockwise, twelve houses follow the Earth-rooted individual's perspective counterclockwise. The person stands at the Ascendant (eastern horizon) and watches consciousness unfold through rising (MC, overhead point), setting (Descendant, western horizon), and nadir (IC, below). This sequence maps the individual's psychological development: self-emergence (Asc), social manifestation (MC), relational encounter (Desc), and foundational depth (IC).

The twelve-fold division creates finer distinctions than eight watches, reflecting increased psychological complexity. Where eight watches marked biological work-rest cycles, twelve houses map psychological life arenas: self-image, resources, communication, home, creativity, work, partnership, transformation, philosophy, career, community, and transcendence. This detailed psychological mapping serves individualized consciousness navigating complex modern existence.

The counterclockwise motion also symbolizes opposition between vitalistic (life-force) and psychomental (mind-spirit) principles. The psychomental rhythm "opposes" but doesn't negate the vitalistic—it transcends and includes it. Modern consciousness still lives in biological bodies subject to solar cycles, but psychological development follows its own internal logic that can override biological imperatives.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Twelve Houses (Modern Psychomental System)"
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
        l1_anchor="ah_v1.0.0_twelve_houses__modern_psychome_001_L1",
    )
    version: str = "1.0.0"
