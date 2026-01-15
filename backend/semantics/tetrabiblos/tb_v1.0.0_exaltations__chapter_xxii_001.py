"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182684
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
    semantic_id="tb_v1.0.0_exaltations__chapter_xxii_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ExaltationsChapterXxii(SemanticEntry):
    """
    **Source Text** (Lines 2512-2553):
> The Sun on his entrance into Aries is then passing into the hig...
    """
    
    original_text: str = """**Source Text** (Lines 2512-2553):
> The Sun on his entrance into Aries is then passing into the higher and more northern semicircle; his exaltation, therefore, is determined to be in Aries, his fall in Libra. Saturn on the contrary, in order to preserve his station opposite to the Sun, obtains his exaltation in Libra, and his fall in Aries. The Moon, after conjunction with the Sun in Aries, makes her first appearance and begins to augment her light in Taurus, which is consequently her exaltation; Scorpio is her fall. Jupiter becomes most northerly and augments his peculiar influence when in Cancer—his exaltation; Capricorn is his fall. Mars possesses a fiery nature receiving greatest intensity in Capricorn—his exaltation; Cancer is his fall. Venus is chiefly moist when in Pisces—her exaltation; Virgo is her fall. Mercury, of a nature opposite to Venus, takes his exaltation in Virgo; Pisces is his fall.

**English Paraphrase (Primary Language)**:
Ptolemy explains the **exaltation (ὕψωμα)** system—each planet has a sign where its influence is maximally intensified, and an opposite sign of "fall" where it is weakened:

| Planet | Exaltation | Fall | Rationale |
|--------|-----------|------|-----------|
| Sun | Aries | Libra | Enters northern hemisphere, days lengthen |
| Saturn | Libra | Aries | Opposite Sun (cold opposes heat) |
| Moon | Taurus | Scorpio | First visible after Sun's exaltation |
| Jupiter | Cancer | Capricorn | Most northerly, fertilizing influence max |
| Mars | Capricorn | Cancer | Fiery nature intensified in south |
| Venus | Pisces | Virgo | Moisture peaks in watery sign |
| Mercury | Virgo | Pisces | Autumnal dryness (opposite Venus) |

The exaltation degrees (not specified here but traditional: Sun 19° Aries, Moon 3° Taurus, etc.) mark the exact point of maximum dignity.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密解释了**擢升/耀升（ὕψωμα）**系统——每颗行星都有一个星座其影响力最大化，以及一个相对的"落陷"星座其影响力减弱：

| 行星 | 擢升 | 落陷 | 理由 |
|------|------|------|------|
| 太阳 | 白羊座 | 天秤座 | 进入北半球，白昼延长 |
| 土星 | 天秤座 | 白羊座 | 与太阳相对（寒冷对抗热量） |
| 月亮 | 金牛座 | 天蝎座 | 太阳擢升后首次可见 |
| 木星 | 巨蟹座 | 摩羯座 | 最北，滋养影响最大 |
| 火星 | 摩羯座 | 巨蟹座 | 火性在南方强化 |
| 金星 | 双鱼座 | 室女座 | 湿润在水象星座达到顶峰 |
| 水星 | 室女座 | 双鱼座 | 秋季干燥（与金星相对） |

**Core Points**:
- Exaltation = sign of maximum planetary influence
- Fall = opposite sign, minimum influence
- Sun exalted Aries (spring, days lengthen)
- Saturn exalted Libra (opposite Sun)
- Moon exalted Taurus (first light after Sun's exaltation)
- Jupiter exalted Cancer (northernmost, fertile)
- Mars exalted Capricorn (fire intensified south)
- Venus exalted Pisces (moisture maximum)
- Mercury exalted Virgo (dryness, opposite Venus)

**Narrative Snippets**:
- `[ns_tetra_i052]` `[trigger: exaltation_system]` `[factor_trigger: astro_planet_exaltation]` `[role: 主干]` Each planet has an exaltation where its influence is maximized, and a fall where it is weakened. → Source Text I.22
- `[ns_tetra_i053]` `[trigger: sun_exaltation]` `[factor_trigger: astro_planet_sun AND astro_sign_aries]` `[role: 条件分支]` Sun's exaltation in Aries: entering the northern semicircle, days lengthen, heating nature increases. → Source Text I.22

**Textual Criticism**: N/A: Standard exaltation doctrine."""
    normalized_text_zh: str = """"""
    subject: str = "Exaltations (Chapter XXII)"
    factor_refs: list = ['engine_id', 'planet_exaltation', 'astrology_classical', 'source_ref', 'rel_i_020', 'planet_exaltation', 'maximizing', 'evi_i_016', 'planet_exaltation', 'rule_exaltation', 'concept_exaltation', 'planet_exaltation', 'self_actualization']
    
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
        l1_anchor="tb_v1.0.0_exaltations__chapter_xxii_001_L1",
    )
    version: str = "1.0.0"
