"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182527
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
    semantic_id="tb_v1.0.0_the_fixed_stars__chapter_ix_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheFixedStarsChapterIx(SemanticEntry):
    """
    **Source Text** (Lines 1774-1905):
> Next in succession, it is necessary to detail the natures and p...
    """
    
    original_text: str = """**Source Text** (Lines 1774-1905):
> Next in succession, it is necessary to detail the natures and properties of the fixed stars; all of which have their respective influences, analogous to the influences of the planets... [Detailed listing of zodiacal stars by sign, with planetary nature attributions: e.g., "Aries: stars in the head possess influence similar to Mars and Saturn; those in the mouth act like Mercury..."; Aldebaran = Mars; Castor = Mercury; Pollux = Mars; Regulus = Mars and Jupiter; Spica = Venus and Mars; Antares = Mars and Jupiter; etc.]

**English Paraphrase (Primary Language)**:
Ptolemy catalogues the **fixed stars** by their planetary natures—each star or star group is assigned influence analogous to one or two planets. This establishes the basis for **parans** (stars rising/setting with chart points) and fixed star interpretation.

Key examples from the zodiacal constellations:
- **Aldebaran** (α Tauri, "the Follower"): Mars nature
- **Pleiades**: Moon and Mars
- **Castor** (α Geminorum): Mercury
- **Pollux** (β Geminorum): Mars
- **Præsepe** (Beehive cluster): Mars and Moon
- **Regulus** (α Leonis, "Cor Leonis"): Mars and Jupiter
- **Spica** (α Virginis): Venus and partly Mars
- **Antares** (α Scorpii, "Scorpion's Heart"): Mars and moderately Jupiter

The principle is that fixed stars, though they emit no independent "rays" (aspects), transmit influence when configured with planets or chart angles—especially when rising, culminating, or setting.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密按行星性质对**恒星**进行分类——每颗恒星或恒星群都被赋予类似于一颗或两颗行星的影响。这为**共升**（与星盘点位同升/同落的恒星）和恒星解读建立了基础。

来自黄道星座的关键例子：
- **毕宿五**（金牛座α，"追随者"）：火星性质
- **昴宿星团**：月亮和火星
- **北河二**（双子座α）：水星
- **北河三**（双子座β）：火星
- **鬼宿星团**（蜂巢星团）：火星和月亮
- **轩辕十四**（狮子座α，"狮心"）：火星和木星
- **角宿一**（室女座α）：金星，部分火星
- **心宿二**（天蝎座α，"蝎心"）：火星，适度木星

原则是恒星虽然不发出独立的"光线"（相位），但当与行星或星盘角度配置时——尤其是升起、中天或落下时——会传递影响。

**Core Points**:
- Fixed stars have planetary natures (analogous influence)
- Each zodiacal constellation's stars catalogued with planetary attributions
- Major stars: Aldebaran (Mars), Regulus (Mars/Jupiter), Spica (Venus/Mars), Antares (Mars/Jupiter)
- Stars operate through configuration with planets and angles
- Parans (co-rising, co-culminating) are primary mechanism
- Stars do not emit independent rays like planets

**Narrative Snippets**:
- `[ns_tetra_i034]` `[trigger: fixed_star_nature]` `[factor_trigger: fixed_star AND astro_planet_qualities]` `[role: 主干]` Fixed stars have respective influences analogous to the planets—each star assigned planetary nature. → Source Text I.9
- `[ns_tetra_i035]` `[trigger: regulus_nature]` `[factor_trigger: astro_ambient_configuration AND concurrent_causes]` `[role: 条件分支]` Regulus, the bright one in the heart of Leo, agrees with Mars and Jupiter. → Source Text I.9
- `[ns_tetra_i036]` `[trigger: spica_nature]` `[factor_trigger: house_angle AND tropical_zodiac]` `[role: 条件分支]` Spica Virginis is like Venus and partly Mars. → Source Text I.9

**Textual Criticism**: Star names follow Greek/Arabic tradition; footnotes identify modern names (Aldebaran, Castor, Pollux, Regulus, Antares)."""
    normalized_text_zh: str = """"""
    subject: str = "The Fixed Stars (Chapter IX)"
    factor_refs: list = ['fixed_star', 'engine_id', 'fixed_star', 'astrology_classical', 'source_ref', 'rel_i_013', 'fixed_star', 'amplifying', 'evi_i_009', 'fixed_star', 'rule_fixed_star', 'concept_fixed_star', 'fixed_star', 'archetype']
    
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
        l1_anchor="tb_v1.0.0_the_fixed_stars__chapter_ix_001_L1",
    )
    version: str = "1.0.0"
