"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182567
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
    semantic_id="tb_v1.0.0_the_annual_seasons__chapter_xi_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheAnnualSeasonsChapterXi(SemanticEntry):
    """
    **Source Text** (Lines 1999-2035):
> The year comprises four seasons; spring, summer, autumn, and wi...
    """
    
    original_text: str = """**Source Text** (Lines 1999-2035):
> The year comprises four seasons; spring, summer, autumn, and winter; of these, the spring partakes chiefly of moisture, for on the dissipation of cold and recommencement of warmth, an expansion of the fluids takes place: the summer is principally hot, owing to the Sun's nearest approach to the zenith: the autumn is principally dry, because the recent heat has absorbed the moisture: and the winter is chiefly cold, the Sun being then at his farthest distance from the zenith. The beginning of the whole zodiacal circle is therefore assumed to be the sign of Aries, which commences at the vernal equinox: since the moisture of spring forms a primary beginning in the zodiac, analogous to the beginning of all animal life, which, in its first age of existence, abounds principally in moisture...

**English Paraphrase (Primary Language)**:
Ptolemy establishes the **seasonal-zodiacal correspondence**:
- **Spring** (Aries) = Moist—fluids expand as cold dissipates
- **Summer** (Cancer) = Hot—Sun nearest zenith
- **Autumn** (Libra) = Dry—heat has absorbed moisture
- **Winter** (Capricorn) = Cold—Sun farthest from zenith

This explains why **Aries is the zodiacal beginning**: spring's moisture parallels the moisture of new life. The seasons also correspond to **ages of life**: Spring = infancy (moist), Summer = prime (hot), Autumn = decline (dry), Winter = old age (cold).

Crucially, the footnote (lines 2023-2035) addresses the "precession objection"—Ptolemy explicitly defines signs by the **tropical points** (equinoxes/solstices), not fixed stars. The "sign of Aries" means "the 30° after the vernal equinox," regardless of which constellation occupies that space.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密建立了**季节-黄道对应**：
- **春季**（白羊座）= 湿润——随着寒冷消散，液体扩张
- **夏季**（巨蟹座）= 炎热——太阳最接近天顶
- **秋季**（天秤座）= 干燥——热量已吸收水分
- **冬季**（摩羯座）= 寒冷——太阳离天顶最远

这解释了为什么**白羊座是黄道的起点**：春天的湿润与新生命的湿润平行。季节也对应**人生阶段**：春季=婴儿期（湿润），夏季=壮年（炎热），秋季=衰退（干燥），冬季=老年（寒冷）。

关键地，脚注（2023-2035行）解答了"岁差反对意见"——托勒密明确按**回归点**（春分/秋分）定义星座，而非恒星。"白羊座"意为"春分后的30°"，无论哪个星座占据该空间。

**Core Points**:
- Spring = moist, Summer = hot, Autumn = dry, Winter = cold
- Aries begins zodiac because spring's moisture = beginning of life
- Seasons correspond to ages: infancy-prime-decline-old age
- Signs defined by tropical points, not fixed stars
- Precession does not invalidate astrological signs

**Narrative Snippets**:
- `[ns_tetra_i037]` `[trigger: seasonal_quality]` `[factor_trigger: astro_season_quality]` `[role: 主干]` Spring is moist, summer hot, autumn dry, winter cold—corresponding to the four zodiacal quadrants. → Source Text I.12
- `[ns_tetra_i038]` `[trigger: aries_beginning]` `[factor_trigger: astro_sign_aries]` `[role: 主干依赖]` Aries commences at the vernal equinox because spring's moisture forms the primary beginning, analogous to animal life. → Source Text I.12
- `[ns_tetra_i039]` `[trigger: tropical_zodiac]` `[factor_trigger: astro_tropical_signs]` `[role: 总结]` Signs are defined by tropical points (equinoxes/solstices), not by fixed star positions. → Footnote I.12

**Textual Criticism**: Footnote explicitly defends tropical zodiac against precession objection."""
    normalized_text_zh: str = """"""
    subject: str = "The Annual Seasons (Chapter XII)"
    factor_refs: list = ['tropical_zodiac', 'engine_id', 'tropical_zodiac', 'astrology_classical', 'source_ref', 'rel_i_014', 'tropical_zodiac', 'defining', 'evi_i_010', 'tropical_zodiac', 'rule_tropical', 'concept_season', 'tropical_zodiac', 'seasonal_affect']
    
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
        l1_anchor="tb_v1.0.0_the_annual_seasons__chapter_xi_001_L1",
    )
    version: str = "1.0.0"
