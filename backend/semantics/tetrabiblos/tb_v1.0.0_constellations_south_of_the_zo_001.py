"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182554
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
    semantic_id="tb_v1.0.0_constellations_south_of_the_zo_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ConstellationsSouthOfTheZo(SemanticEntry):
    """
    **Source Text** (Lines 1943-1991):
> The influences of the constellations south of the zodiac, exist...
    """
    
    original_text: str = """**Source Text** (Lines 1943-1991):
> The influences of the constellations south of the zodiac, existing in a similar mode, are as follows:
> Piscis Australis: The bright star in the mouth (Fomalhaut) is of the same influence as Venus and Mercury.
> Cetus is like Saturn.
> Orion: The stars on the shoulders operate similarly to Mars and Mercury; other bright stars to Jupiter and Saturn.
> Fluvius (Eridanus): The last bright one is like Jupiter; the rest are like Saturn.
> Lepus is like Saturn and Mercury.
> Canis: The bright star in the mouth (Sirius) is like Jupiter, and partly like Mars; the others are like Venus.
> Procyon (Canis Minor): The bright star is like Mercury, and in some degree like Mars.
> Hydrus: The bright stars are like Saturn and Venus.
> Crater is like Venus, and in some degree like Mercury.
> Corvus is like Mars and Saturn.
> Argo is like Saturn and Jupiter.
> Centaurus: The human part is like Venus and Mercury; the horse part like Venus and Jupiter.
> Lupus: The bright stars are like Saturn, and partly like Mars.
> Ara is like Venus, and also Mercury in some degree.
> Corona Australis: The bright stars are like Saturn and Jupiter.

**English Paraphrase (Primary Language)**:
Ptolemy catalogues the **southern constellations** (below the zodiac) by planetary natures:

Key examples:
- **Fomalhaut** (α Piscis Australis): Venus-Mercury—the "Royal Star" of the south
- **Sirius** (α Canis Majoris): Jupiter-Mars—the brightest fixed star, powerful for fame and honor
- **Orion**: Mixed—shoulders Mars-Mercury, body Jupiter-Saturn
- **Centaurus**: Human part Venus-Mercury, horse part Venus-Jupiter

The footnote notes that stars emit no independent rays but gain power through: (1) proximity to ecliptic, (2) northern position, (3) zenith passage, (4) conjunction with planets, or (5) rising/setting/culminating with planets.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密按行星性质对**南黄道星座**（黄道以下）进行分类：

关键例子：
- **北落师门**（南鱼座α）：金星-水星——南方"王者恒星"
- **天狼星**（大犬座α）：木星-火星——最亮的恒星，对名誉和荣誉有强力
- **猎户座**：混合——肩部火星-水星，躯体木星-土星
- **半人马座**：人体部分金星-水星，马体部分金星-木星

脚注指出恒星不发射独立光线，但通过以下方式获得力量：(1) 靠近黄道，(2) 北方位置，(3) 过天顶，(4) 与行星合相，或 (5) 与行星同升/同落/同中天。

**Core Points**:
- Southern constellations assigned planetary natures
- Sirius (Dog Star) = Jupiter-Mars, most powerful fixed star
- Fomalhaut = Venus-Mercury, southern Royal Star
- Stars gain power through configuration with planets and angles
- Stars emit no independent rays—influence through paran

**Narrative Snippets**:
- `[ns_tetra_i071]` `[trigger: southern_stars]` `[factor_trigger: fixed_star_south AND sign_meaning AND star_sirius]` `[role: 主干]` Southern constellations have influences analogous to planets—Sirius like Jupiter-Mars, Fomalhaut like Venus-Mercury. → Source Text I.11
- `[ns_tetra_i072]` `[trigger: star_power]` `[factor_trigger: sign_modality AND sign_antiscia]` `[role: 条件分支]` Fixed stars emit no rays but gain power through ecliptic proximity, paran, and configuration. → Footnote I.11"""
    normalized_text_zh: str = """"""
    subject: str = "Constellations South of the Zodiac (Chapter XI)"
    factor_refs: list = ['fixed_star_south', 'star_sirius', 'engine_id', 'fixed_star_south', 'astrology_classical', 'star_sirius', 'astrology_classical', 'source_ref', 'rel_i_027', 'fixed_star_south', 'amplifying', 'evi_i_022', 'star_sirius', 'rule_south_star', 'concept_south_star', 'fixed_star_south', 'shadow_archetype']
    
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
        l1_anchor="tb_v1.0.0_constellations_south_of_the_zo_001_L1",
    )
    version: str = "1.0.0"
