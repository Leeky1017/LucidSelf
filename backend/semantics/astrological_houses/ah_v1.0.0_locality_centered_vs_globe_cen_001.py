"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333571
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
    semantic_id="ah_v1.0.0_locality_centered_vs_globe_cen_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class LocalityCenteredVsGlobeCen(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Locality-Centered | Visi...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Locality-Centered | Visible horizon | Archaic tribal |
| Globe-Centered | Geocentric horizon | Modern individual |
| Topocentric | Observer at surface | Local calculation |
| Consciousness Evolution | Tribal→Individual | Paradigm shift |

#### Source Text

"Archaic astrology was locality-centered, bounded by the horizon of a particular place, reflecting tribal consciousness rooted in the soil. Modern astrology is globe-centered, using a rational horizon through Earth's center, reflecting the mobile consciousness of individualized humanity freed from geographic limitation."

#### English Paraphrase (Primary Language)

Ancient astrological systems operated from a locality-centered perspective, where the house system was defined by the actual visible horizon of a specific geographic location. This approach reflected tribal, place-bound consciousness, where one's identity was inseparable from the local landscape and community. In contrast, modern astrology adopts a globe-centered framework, calculating houses using a theoretical horizon passing through Earth's geometric center. This shift represents the evolution from collective tribal identity to individualized mobile consciousness, where the person's sense of self transcends geographic boundaries and enables global perspective.

#### Complete Chinese Interpretation (Secondary Language)

古代占星系统采用**以地方为中心**的视角，宫位系统由特定地理位置的实际可见地平线定义。这种方法反映部落的、受地方束缚的意识，个人身份与当地景观和社区不可分离。相反，现代占星采用**以地球为中心**的框架，使用穿过地球几何中心的理论地平线计算宫位。这种转变代表从集体部落身份到个体化流动意识的演进，人的自我感超越地理边界并使全球视角成为可能。Rudhyar识别宫位概念化的根本宇宙论转变。古代以地方为中心的方法基于观察者在特定位置的实际地平线计算宫位——环顾时能物理看到的东西。这种方法适合农业、部落社会，身份与地方不可分离。命运与当地土壤、社区、可见天空绑定。现代占星的以地球为中心方法使用穿过地球中心的数学地平线计算宫位，将观察者视为位于地球核心向外看。这种地心方法产生普遍的、可移植的宫位系统，无论观察者纬度或地形特征如何都保持一致。它反映能全球旅行同时保持连贯身份的现代流动个体的意识。

#### Core Points

- **Archaic system**: Locality-centered, actual visible horizon, tribal consciousness
- **Modern system**: Globe-centered, geocentric rational horizon, individual consciousness
- **Philosophical shift**: From soil-bound tribal identity to mobile individualized selfhood
- **Consciousness evolution**: Geographic limitation → global perspective
- **House calculation**: Local topocentric → universal geocentric

#### Detailed Explanation

Rudhyar identifies a fundamental cosmological shift in how astrological houses are conceptualized. The archaic locality-centered approach calculated houses based on the observer's actual horizon at a specific location—what one could physically see when looking around. This method was appropriate for agricultural, tribal societies where identity was inseparable from place. One's destiny was bound to the local soil, community, and visible sky.

Modern astrology's globe-centered approach calculates houses using a mathematical horizon that passes through Earth's center, treating the observer as positioned at Earth's core looking outward. This geocentric method produces a universal, portable house system that remains consistent regardless of the observer's latitude or topographic features. It reflects the consciousness of modern, mobile individuals who can travel globally while maintaining coherent identity.

This shift parallels the broader evolution from collective tribal consciousness to individualized self-awareness. The locality-centered system served communities where identity was collective and place-bound. The globe-centered system serves individuals who navigate multiple cultures and locations while maintaining coherent selfhood. The house system thus encodes fundamental assumptions about consciousness, identity, and humanity's relationship to Earth and cosmos.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Locality-Centered vs Globe-Centered Astrology"
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
        l1_anchor="ah_v1.0.0_locality_centered_vs_globe_cen_001_L1",
    )
    version: str = "1.0.0"
