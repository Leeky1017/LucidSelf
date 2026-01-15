"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182429
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
    semantic_id="tb_v1.0.0_knowledge_may_be_acquired_by_a_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class KnowledgeMayBeAcquiredByA(SemanticEntry):
    """
    **Source Text** (Lines 1014-1166):
> That a certain power, derived from the æthereal nature, is diff...
    """
    
    original_text: str = """**Source Text** (Lines 1014-1166):
> That a certain power, derived from the æthereal nature, is diffused over and pervades the whole atmosphere of the earth, is clearly evident to all men. Fire and air, the first of the sublunary elements, are encompassed and altered by the motions of the æther. These elements in their turn encompass all inferior matter, and vary it as they themselves are varied; acting on earth and water, on plants and animals... The Sun, always acting in connection with the Ambient, contributes to the regulation of all earthly things... The Moon, being of all the heavenly bodies the nearest to the Earth, also dispenses much influence... The stars likewise produce many impressions on the Ambient. They cause heats, winds, and storms, to the influence of which earthly things are conformably subjected... From these premises it follows not only that all bodies, which may be already compounded, are subjected to the motion of the stars, but also that the impregnation and growth of the seeds from which all bodies proceed, are framed and moulded by the quality existing in the Ambient at the time of such impregnation and growth.

**Key Term Analysis**:
- **Æthereal nature**: αἰθήρ - the fifth element, superlunary substance transmitting celestial influence
- **The Ambient**: περιέχον - the total environmental configuration of celestial and elemental forces
- **Sublunary elements**: Fire, Air, Water, Earth - the four terrestrial elements affected by celestial motion
- **Impregnation**: σπορά - the moment of conception/seeding when celestial influence is imprinted

**English Paraphrase (Primary Language)**:
Ptolemy establishes the **physical mechanism** by which celestial bodies influence terrestrial life. The key concept is the **Ambient** (περιέχον)—the total configuration of celestial and elemental influences pervading Earth's atmosphere. The causal chain operates as follows: (1) The **æther** (fifth element) constitutes the celestial spheres and transmits their motions; (2) These motions alter the **sublunary elements** (fire and air first, then earth and water); (3) The altered elements affect all terrestrial matter including plants, animals, and humans.

Each celestial body contributes distinctly: The **Sun** regulates seasons and daily variations in heat/moisture through its position relative to the zenith. The **Moon**, being nearest Earth, strongly affects moisture—governing tides, plant growth, and bodily fluids. The **fixed stars and planets** produce atmospheric phenomena (winds, storms) through their configurations.

Crucially, Ptolemy argues that this influence operates not only on existing bodies but on **seeds and embryos** at the moment of impregnation. This establishes the theoretical basis for natal astrology: the celestial configuration at conception/birth permanently imprints the individual's constitution.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密在此章建立了天体影响地上生命的**物理机制**。核心概念是**环境/周天**（περιέχον）——弥漫在地球大气中的天体与元素影响力的总体配置。因果链条如下运作：（1）**以太**（第五元素）构成天球并传递其运动；（2）这些运动改变**月下元素**（首先是火和气，然后是土和水）；（3）改变后的元素影响所有地上物质，包括植物、动物和人类。

每个天体都有独特贡献：**太阳**通过其相对于天顶的位置调节季节和每日的热/湿变化。**月亮**因最靠近地球，强烈影响湿度——支配潮汐、植物生长和体液。**恒星和行星**通过其配置产生大气现象（风、暴风雨）。

关键的是，托勒密论证这种影响不仅作用于现存物体，还作用于受孕时刻的**种子和胚胎**。这为本命占星学建立了理论基础：受孕/出生时的天体配置永久地印刻在个体的体质中。

**Core Points**:
- Æthereal power diffuses through Earth's atmosphere (the Ambient)
- Causal chain: æther → fire/air → earth/water → plants/animals
- Sun regulates seasons and daily heat/moisture variations
- Moon governs tides, moisture, and bodily fluids (nearest to Earth)
- Stars and planets produce atmospheric phenomena through configurations
- Influence operates on seeds/embryos at conception—basis for natal astrology
- The Ambient = total celestial-elemental configuration at any moment
- Physical causation model, not magical or divine

**Detailed Explanation**:
This chapter provides the cosmological physics underlying Ptolemaic astrology. The model is thoroughly Aristotelian: the universe consists of concentric spheres with Earth at center, surrounded by the elemental spheres (earth, water, air, fire) and then the celestial spheres (Moon, Mercury, Venus, Sun, Mars, Jupiter, Saturn, fixed stars). The æther—the fifth element—fills the celestial realm and transmits motion downward through the elemental chain.

The concept of **imprinting at conception** is philosophically crucial. Ptolemy argues that seeds and embryos are particularly receptive to celestial influence because they are in a formative state. The configuration of the Ambient at the moment of conception/birth becomes permanently encoded in the individual's physical and psychological constitution. This provides the theoretical justification for natal chart interpretation: your birth chart is not arbitrary but reflects real physical forces that shaped your formation.

**Narrative Snippets**:
- `[ns_tetra_i006]` `[trigger: aethereal_power]` `[factor_trigger: astro_astro_regulation AND astro_tidal_effects]` `[role: 主干]` A certain power derived from the æthereal nature is diffused over and pervades the whole atmosphere of the earth. → Source Text I.2
- `[ns_tetra_i007]` `[trigger: causal_chain]` `[factor_trigger: astro_astro_natal_moment AND annual_weather AND natal_moment]` `[role: 主干依赖]` Fire and air are encompassed and altered by the æther's motions; these in turn encompass all inferior matter. → Source Text I.2
- `[ns_tetra_i008]` `[trigger: sun_regulation]` `[factor_trigger: ascendant AND aspect_type]` `[role: 条件分支]` The Sun contributes to the regulation of all earthly things by the revolution of seasons and by daily changes in heat, moisture, dryness and cold. → Source Text I.2
- `[ns_tetra_i009]` `[trigger: moon_moisture]` `[factor_trigger: aspect_formation AND aspect_application]` `[role: 条件分支]` The Moon dispenses much influence; rivers, tides, plants and animals sympathize and vary with her waxing and waning. → Source Text I.2
- `[ns_tetra_i010]` `[trigger: impregnation_imprint]` `[factor_trigger: aspect_inconjunct AND behavior]` `[role: 总结]` The impregnation and growth of seeds are framed and moulded by the quality existing in the Ambient at the time of such impregnation. → Source Text I.2

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The footnote (lines 1022-1058) preserves Peter Apianus's cosmological description (1574), showing how the ten-sphere model was standard until Copernicus. This contextualizes Ptolemy's physics within later reception.
- **中文**: 脚注（1022-1058行）保留了Peter Apianus的宇宙学描述（1574年），展示了十层天球模型在哥白尼之前是标准的。这将托勒密的物理学置于后来接受史的语境中。"""
    normalized_text_zh: str = """"""
    subject: str = "Knowledge May Be Acquired by Astronomy (Chapter II)"
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
        l1_anchor="tb_v1.0.0_knowledge_may_be_acquired_by_a_001_L1",
    )
    version: str = "1.0.0"
