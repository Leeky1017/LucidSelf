"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182462
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
    semantic_id="tb_v1.0.0_the_influences_of_the_planetar_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheInfluencesOfThePlanetar(SemanticEntry):
    """
    **Source Text** (Lines 1590-1638):
> The Sun is found to produce heat and moderate dryness. His magn...
    """
    
    original_text: str = """**Source Text** (Lines 1590-1638):
> The Sun is found to produce heat and moderate dryness. His magnitude, and the changes which he so evidently makes in the seasons, render his power more plainly perceptible than that of the other heavenly bodies; since his approach to the zenith of any part of the earth creates a greater degree of heat in that part and proportionately disposes its inhabitants after his own nature. The Moon principally generates moisture; her proximity to the earth renders her highly capable of exciting damp vapours, and of thus operating sensibly upon animal bodies by relaxation and putrefaction. She has, however, also a moderate share in the production of heat, in consequence of the illumination she receives from the Sun. Saturn produces cold and dryness, for he is most remote both from the Sun's heat and from the earth's vapours. But he is more effective in the production of cold than of dryness. Mars chiefly causes dryness, and is also strongly heating, by means of his own fiery nature, which is indicated by his colour, and in consequence of his vicinity to the Sun; the sphere of which is immediately below him. Jupiter revolves in an intermediate sphere between the extreme cold of Saturn and the burning heat of Mars, and has consequently a temperate influence: he therefore at once promotes both warmth and moisture. But, owing to the spheres of Mars and the Sun, which lie beneath him, his warmth is predominant: and hence he produces fertilizing breezes. To Venus also the same temperate quality belongs, although it exists conversely; since the heat she produces by her vicinity to the Sun is not so great as the moisture which she generates by the magnitude of her light, and by appropriating to herself the moist vapours of the earth, in the same manner that the Moon does. Mercury sometimes produces dryness, and at other times moisture, and each with equal vigour... he consequently operates rapid changes tending to produce alternately either quality.

**Key Term Analysis**:
- **Heat/Cold**: θερμόν/ψυχρόν - primary active qualities in Aristotelian physics
- **Moist/Dry**: ὑγρόν/ξηρόν - primary passive qualities in Aristotelian physics
- **Temperate**: εὔκρατος - balanced mixture of qualities (Jupiter, Venus)
- **Fertilizing breezes**: γόνιμοι πνοαί - life-promoting atmospheric effects

**English Paraphrase (Primary Language)**:
Ptolemy assigns each planet specific **elemental qualities** based on Aristotelian physics (hot/cold, moist/dry). The assignments derive from observable effects (Sun's heat, Moon's effect on tides) and from celestial position (Saturn is cold because most remote from Sun).

**Planetary qualities**:
- **Sun**: Hot and moderately dry—observable through seasonal heating
- **Moon**: Primarily moist, moderately hot—affects tides, plant growth, bodily fluids
- **Saturn**: Cold and dry—most remote from Sun's heat and Earth's vapors; cold predominates
- **Mars**: Dry and very hot—fiery nature indicated by red color; near Sun's sphere
- **Jupiter**: Temperate (warm and moist)—between Saturn's cold and Mars's heat; warmth predominates, produces "fertilizing breezes"
- **Venus**: Temperate (moist and warm)—moisture predominates; absorbs Earth's vapors like Moon
- **Mercury**: Variable (moist or dry)—rapid motion produces alternating qualities

This establishes the **physiological basis** for planetary meanings: benefics (Jupiter, Venus) promote life through warmth and moisture; malefics (Saturn, Mars) harm through cold/dryness or excessive heat.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密根据亚里士多德物理学（热/冷、湿/干）为每颗行星分配特定的**元素属性**。这些分配源于可观察的效果（太阳的热、月亮对潮汐的影响）和天体位置（土星因离太阳最远而寒冷）。

**行星属性**：
- **太阳**：热且适度干燥——通过季节性加热可观察到
- **月亮**：主要是湿润，适度温热——影响潮汐、植物生长、体液
- **土星**：冷且干——离太阳热量和地球蒸汽最远；寒冷占主导
- **火星**：干且非常热——火性由红色表示；接近太阳天球
- **木星**：温和（温暖且湿润）——介于土星的寒冷和火星的炎热之间；温暖占主导，产生"滋养之风"
- **金星**：温和（湿润且温暖）——湿润占主导；像月亮一样吸收地球蒸汽
- **水星**：可变（湿润或干燥）——快速运动产生交替的属性

这建立了行星意义的**生理学基础**：吉星（木星、金星）通过温暖和湿润促进生命；凶星（土星、火星）通过寒冷/干燥或过热造成伤害。

**Core Points**:
- Sun: Hot and moderately dry—regulates seasons
- Moon: Primarily moist, moderately hot—governs fluids and growth
- Saturn: Cold and dry (cold predominates)—most remote from Sun
- Mars: Dry and very hot—fiery nature, red color
- Jupiter: Temperate (warm/moist, warmth predominates)—fertilizing
- Venus: Temperate (moist/warm, moisture predominates)—like Moon
- Mercury: Variable—alternates between moist and dry
- Qualities derive from position relative to Sun and Earth
- Aristotelian physics: hot/cold (active), moist/dry (passive)
- Basis for benefic/malefic distinction

**Narrative Snippets**:
- `[ns_tetra_i017]` `[trigger: sun_quality]` `[factor_trigger: planet_sun AND quality_hot]` `[role: 主干]` The Sun produces heat and moderate dryness; his approach to the zenith creates greater heat. → Source Text I.4
- `[ns_tetra_i018]` `[trigger: moon_quality]` `[factor_trigger: planet_quality AND planet_nature AND planet_moon]` `[role: 主干]` The Moon principally generates moisture; her proximity to earth renders her capable of exciting damp vapours. → Source Text I.4
- `[ns_tetra_i019]` `[trigger: saturn_quality]` `[factor_trigger: planet_saturn AND quality_cold]` `[role: 主干]` Saturn produces cold and dryness, for he is most remote from the Sun's heat and earth's vapours. → Source Text I.4
- `[ns_tetra_i020]` `[trigger: mars_quality]` `[factor_trigger: planet_mars AND quality_dry]` `[role: 主干]` Mars chiefly causes dryness and is strongly heating by his fiery nature, indicated by his colour. → Source Text I.4
- `[ns_tetra_i021]` `[trigger: jupiter_quality]` `[factor_trigger: planet_power AND planet_strength AND planet_jupiter]` `[role: 主干]` Jupiter has a temperate influence, promoting both warmth and moisture; he produces fertilizing breezes. → Source Text I.4
- `[ns_tetra_i022]` `[trigger: venus_quality]` `[factor_trigger: planet_gender AND planet_feminine AND planet_venus]` `[role: 主干]` Venus produces moisture by the magnitude of her light and by appropriating moist vapours of the earth. → Source Text I.4
- `[ns_tetra_i023]` `[trigger: mercury_quality]` `[factor_trigger: planet_diurnal AND planet_nocturnal AND planet_mercury]` `[role: 主干]` Mercury produces dryness and moisture alternately with equal vigour, operating rapid changes. → Source Text I.4

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: These planetary quality assignments are consistent across all Greek manuscripts and Arabic translations. They form the foundation of medieval and Renaissance astrology.
- **中文**: 无版本差异：这些行星属性分配在所有希腊手稿和阿拉伯译本中一致。它们构成了中世纪和文艺复兴时期占星学的基础。"""
    normalized_text_zh: str = """"""
    subject: str = "The Influences of the Planetary Orbs (Chapter IV)"
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_the_influences_of_the_planetar_001_L1",
    )
    version: str = "1.0.0"
