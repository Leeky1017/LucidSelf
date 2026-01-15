"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182540
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
    semantic_id="tb_v1.0.0_constellations_north_of_the_zo_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ConstellationsNorthOfTheZo(SemanticEntry):
    """
    **Source Text** (Lines 1907-1941):
> The constellations north of the zodiac have their respective in...
    """
    
    original_text: str = """**Source Text** (Lines 1907-1941):
> The constellations north of the zodiac have their respective influences, analogous to those of the planets, existing in the mode described in the following list.
> Ursa Minor: The bright stars are like Saturn, and in some degree like Venus.
> Ursa Major is like Mars, but the nebula under the tail resembles the Moon and Venus.
> Draco: The bright stars operate like Saturn and Mars.
> Cepheus is like Saturn and Jupiter.
> Bootes is like Mercury and Saturn; but Arcturus is like Mars and Jupiter.
> Corona Borealis is like Venus and Mercury.
> Hercules is like Mercury.
> Lyra is like Venus and Mercury.
> Cygnus is like Venus and Mercury.
> Cassiopeia is like Saturn and Venus.
> Perseus is like Jupiter and Saturn; the nebula in the sword is like Mars and Mercury.
> Auriga: The bright stars are like Mars and Mercury.
> Serpentarius is like Saturn, and moderately like Venus.
> Serpens is like Saturn and Mars.
> Sagitta is like Saturn, and moderately like Venus.
> Aquila is like Mars and Jupiter.
> Delphinus is like Saturn and Mars.
> Equus (Pegasus): The bright stars are like Mars and Mercury.
> Andromeda is like Venus.
> Delta (Triangle) is like Mercury.

**English Paraphrase (Primary Language)**:
Ptolemy catalogues the **northern constellations** (those above the zodiac band) by their planetary natures. Each constellation or its bright stars is assigned influence analogous to specific planets, enabling interpretation when these stars are configured with planets or chart points.

Key examples:
- **Ursa Minor/Major**: Saturn-Venus / Mars (with Moon-Venus nebula)
- **Draco**: Saturn-Mars (fierce, cold-dry)
- **Bootes/Arcturus**: Mercury-Saturn / Mars-Jupiter (Arcturus is especially powerful)
- **Lyra, Cygnus**: Venus-Mercury (artistic, communicative)
- **Aquila**: Mars-Jupiter (martial-regal)
- **Andromeda**: Pure Venus nature

**Complete Chinese Interpretation (Secondary Language)**:
托勒密按行星性质对**北黄道星座**（黄道带上方的星座）进行分类。每个星座或其亮星都被赋予类似于特定行星的影响，使这些恒星与行星或星盘点位配置时可以进行解读。

关键例子：
- **小熊座/大熊座**：土星-金星 / 火星（尾部星云类似月亮-金星）
- **天龙座**：土星-火星（凶猛、冷干）
- **牧夫座/大角星**：水星-土星 / 火星-木星（大角星尤其强力）
- **天琴座、天鹅座**：金星-水星（艺术性、沟通性）
- **天鹰座**：火星-木星（武勇-王者）
- **仙女座**：纯金星性质

**Core Points**:
- Northern constellations assigned planetary natures
- Each star/constellation has one or two planetary analogues
- Arcturus especially powerful (Mars-Jupiter)
- Stars influence when configured with planets/angles
- Foundation for paran and fixed star interpretation

**Narrative Snippets**:
- `[ns_tetra_i070]` `[trigger: northern_stars]` `[factor_trigger: fixed_star_north AND sign_triplicity]` `[role: 主干]` Northern constellations have influences analogous to planets—Draco like Saturn-Mars, Arcturus like Mars-Jupiter. → Source Text I.10"""
    normalized_text_zh: str = """"""
    subject: str = "Constellations North of the Zodiac (Chapter X)"
    factor_refs: list = ['fixed_star_north', 'engine_id', 'fixed_star_north', 'astrology_classical', 'source_ref', 'rel_i_026', 'fixed_star_north', 'amplifying', 'evi_i_021', 'fixed_star_north', 'rule_north_star', 'concept_north_star', 'fixed_star_north', 'guiding_archetype']
    
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
        l1_anchor="tb_v1.0.0_constellations_north_of_the_zo_001_L1",
    )
    version: str = "1.0.0"
