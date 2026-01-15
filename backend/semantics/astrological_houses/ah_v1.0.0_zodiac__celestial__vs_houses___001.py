"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333647
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
    semantic_id="ah_v1.0.0_zodiac__celestial__vs_houses___001",
    book_id="astrological_houses",
    engine_id="astro"
)
class ZodiacCelestialVsHouses(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Zodiac Celestial | Orbit...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Zodiac Celestial | Orbital/yearly | Cosmic qualities |
| Houses Terrestrial | Rotational/daily | Life arenas |
| Sky-Earth Polarity | Potential vs manifest | Dual system |
| Macrocosm-Microcosm | Universal→individual | Correspondence |

#### Source Text

"The zodiac represents the celestial/orbital frame of reference—Earth's yearly journey around the Sun, defining space and cosmic qualities. The houses represent the terrestrial/rotational frame—Earth's daily spin, defining time and local experience. These are two distinct frameworks: the zodiac is spatial-cosmic, the houses are durational-local. Together they create the sky-earth polarity essential to astrological interpretation."

#### English Paraphrase (Primary Language)

Astrology employs two independent coordinate systems that must be distinguished. The zodiac is a celestial, orbital framework based on Earth's annual revolution around the Sun, creating twelve spatial sectors (signs) that define cosmic archetypal qualities. The houses constitute a terrestrial, rotational framework based on Earth's daily spin, creating twelve temporal sectors that define how cosmic energies manifest in specific life arenas. The zodiac is space-oriented and universal; the houses are time-oriented and location-specific. This dual system creates a sky-earth polarity: the zodiac represents cosmic potential (what is), while houses represent terrestrial actualization (how and where it manifests).

#### Complete Chinese Interpretation (Secondary Language)

星座代表**天上空间框架**(celestial)，由地球年行围绕太阳产生，反映宇宙生命能量的十二种质性。宫位代表**地上时间框架**(terrestrial)，由地球日旋产生，反映个体经验的十二个领域。这构成**天地两仪极性**：星座=潜能/质性/先天，宫位=显化/领域/后天。星座是生命能量如何(how)，宫位是它在哪里(where)显化。行星在星座获得质性，在宫位找到表达竞技场。天(zodiac)提供宇宙模式，地(houses)提供个人语境。这是宏观宇宙-微观宇宙对应的核心：天上十二星座秩序映射到地上十二宫位经验。

#### Core Points

- **Zodiac = celestial/orbital**: Earth's yearly path, spatial-cosmic, universal qualities
- **Houses = terrestrial/rotational**: Earth's daily spin, durational-local, life arenas
- **Two reference frames**: Space (zodiac) vs Time (houses)
- **Sky-earth polarity**: Cosmic potential vs terrestrial manifestation"""
    normalized_text_zh: str = """"""
    subject: str = "Zodiac (Celestial) vs Houses (Terrestrial)"
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
        l1_anchor="ah_v1.0.0_zodiac__celestial__vs_houses___001_L1",
    )
    version: str = "1.0.0"
