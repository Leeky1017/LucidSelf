"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156242
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
    semantic_id="ca_v1.0.0_the_celestial_bodies_and_their_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class TheCelestialBodiesAndTheir(SemanticEntry):
    """
    #### Source Text

(Synthesized from Lilly Book I, pp. 25-27):
> "There are seven Planets, viz. Satur...
    """
    
    original_text: str = """#### Source Text

(Synthesized from Lilly Book I, pp. 25-27):
> "There are seven Planets, viz. Saturn ♄, Jupiter ♃, Mars ♂, Sol ☉, Venus ♀, Mercury ☿, Luna ☽. There are also the two Nodes of the Moon, viz. the North Node ☊ called Caput Draconis, or the Dragon's Head, and the South Node ☋ called Cauda Draconis, or the Dragon's Tail."

#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| Planet | Planeta | Wandering star | Seven classical bodies |
| Node | Nodus | Intersection point | Lunar orbit crossing ecliptic |
| Caput Draconis | Dragon's Head | North Node | Increase, benefit |
| Cauda Draconis | Dragon's Tail | South Node | Decrease, malefic |

#### English Paraphrase (Primary Language)

The **seven classical planets** form Lilly's astrological core:

| Planet | Symbol | Nature | Category |
|--------|--------|--------|----------|
| Saturn | ♄ | Cold, dry | Greater Malefic |
| Jupiter | ♃ | Hot, moist | Greater Benefic |
| Mars | ♂ | Hot, dry | Lesser Malefic |
| Sun | ☉ | Hot, dry | Luminary |
| Venus | ♀ | Cold, moist | Lesser Benefic |
| Mercury | ☿ | Variable | Neutral |
| Moon | ☽ | Cold, moist | Luminary |

**Lunar Nodes**: North Node (☊) = increase/gain; South Node (☋) = decrease/loss.

**Five Ptolemaic Aspects**: Conjunction (0°), Sextile (60°), Square (90°), Trine (120°), Opposition (180°).

#### Complete Chinese Interpretation (Secondary Language)

**七大经典行星**构成Lilly占星核心：土星♄（寒燥，大凶）、木星♃（热湿，大吉）、火星♂（热燥，小凶）、太阳☉（热燥，发光体）、金星♀（寒湿，小吉）、水星☿（可变，中性）、月亮☽（寒湿，发光体）。

**月亮交点**：北交点☊=增长/获得；南交点☋=减损/失去。

**五种托勒密相位**：合相（0°）、六分相（60°）、四分相（90°）、三分相（120°）、对分相（180°）。

#### Core Points

- Seven classical planets include Sun and Moon as luminaries
- Planets categorized as benefic (Jupiter, Venus), malefic (Saturn, Mars), or neutral (Mercury)
- Lunar Nodes mark increase (North) and decrease (South)
- Five Ptolemaic aspects define planetary relationships

**Narrative Snippets**:
- `[ns_lilly_found_001]` `[trigger: jupiter_benefic]` `[factor_trigger: astro_planet_jupiter AND astro_benefic]` `[role: 主干]` Jupiter is hot, moist, sanguine—Greater Benefic of expansion and fortune. → CA I #Jupiter
- `[ns_lilly_found_002]` `[trigger: saturn_malefic]` `[factor_trigger: astro_planet_saturn AND astro_malefic]` `[role: 主干依赖]` Saturn is cold, dry, melancholy—Greater Malefic of limitation and time. → CA I #Saturn
- `[ns_lilly_found_003]` `[trigger: nodal_axis]` `[factor_trigger: astro_north_node AND astro_south_node AND astro_nodal_axis]` `[role: 主干依赖]` North Node = increase; South Node = decrease—polar axis of gain/loss. → CA I #Nodes
- `[ns_lilly_found_004]` `[trigger: sun_luminary]` `[factor_trigger: astro_planet_sun AND astro_luminary]` `[role: 主干依赖]` The Sun is Heart of Heaven, Eye of World—vitality and authority. → CA I #Sun

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's symbol system follows standard 17th-century notation. The lunar nodes are sometimes rendered as stylized dragon images.
- **中文**: Lilly的符号系统遵循17世纪标准记法。月亮交点有时以风格化龙图像呈现。"""
    normalized_text_zh: str = """"""
    subject: str = "The Celestial Bodies and Their Characters"
    factor_refs: list = ['planet', 'benefic_planet', 'malefic_planet', 'aspect']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_the_celestial_bodies_and_their_001_L1",
    )
    version: str = "1.0.0"
