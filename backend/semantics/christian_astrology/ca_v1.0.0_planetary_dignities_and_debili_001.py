"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156389
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
    semantic_id="ca_v1.0.0_planetary_dignities_and_debili_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class PlanetaryDignitiesAndDebili(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 101-104): "A Planet is said to be in his Dignity when he is in a...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 101-104): "A Planet is said to be in his Dignity when he is in a Sign of his own nature. In his Domicile (his own house), he hath most strength. In Exaltation, much strength. In Triplicity, Term, or Face, some strength. In Detriment or Fall, he is weakened."

#### English Paraphrase (Primary Language)

**Essential Dignities** measure a planet's inherent strength by sign position:

| Dignity | Points | Description |
|---------|--------|-------------|
| Domicile (Rulership) | +5 | Planet in sign it rules |
| Exaltation | +4 | Planet in sign of highest power |
| Triplicity | +3 | Planet ruling element by sect |
| Term | +2 | Planet in its own term (bound) |
| Face (Decan) | +1 | Planet in its own decan |

**Essential Debilities** weaken planets:

| Debility | Points | Description |
|----------|--------|-------------|
| Detriment | -5 | Opposite to domicile |
| Fall | -4 | Opposite to exaltation |
| Peregrine | 0 | No dignity at all |

**Dignity Table** (major dignities):

| Planet | Domicile | Exaltation | Detriment | Fall |
|--------|----------|------------|-----------|------|
| Sun | Leo | Aries 19° | Aquarius | Libra |
| Moon | Cancer | Taurus 3° | Capricorn | Scorpio |
| Mercury | Gemini/Virgo | Virgo 15° | Sagittarius/Pisces | Pisces |
| Venus | Taurus/Libra | Pisces 27° | Scorpio/Aries | Virgo |
| Mars | Aries/Scorpio | Capricorn 28° | Libra/Taurus | Cancer |
| Jupiter | Sagittarius/Pisces | Cancer 15° | Gemini/Virgo | Capricorn |
| Saturn | Capricorn/Aquarius | Libra 21° | Cancer/Leo | Aries |

#### Complete Chinese Interpretation (Secondary Language)

**本质尊贵**测量行星在星座位置的内在力量：**入庙**（+5）=行星在其守护星座；**入旺**（+4）=行星在最高力量星座；**三合**（+3）=行星守护该元素；**界**（+2）=行星在自己的界内；**面**（+1）=行星在自己的十度区。**本质失势**削弱行星：**入陷**（-5）=与入庙相对；**落陷**（-4）=与入旺相对；**游魂**（0）=无任何尊贵。

**Narrative Snippets**:
- `[ns_lilly_dig_001]` `[trigger: domicile]` `[factor_trigger: astro_dignity_domicile AND astro_planetary_strength]` `[role: 主干]` Planet in domicile has most strength (+5)—like a king in his own kingdom. → CA I #Dignities
- `[ns_lilly_dig_002]` `[trigger: detriment]` `[factor_trigger: astro_debility_detriment AND astro_planetary_weakness]` `[role: 条件分支]` Planet in detriment (-5) is weakened—like a stranger in hostile territory. → CA I #Dignities
- `[ns_lilly_dig_003]` `[trigger: exaltation]` `[factor_trigger: astro_dignity_exaltation]` `[role: 条件分支]` Planet in exaltation (+4) has much strength—elevated to highest expression of its nature. → CA I #Dignities
- `[ns_lilly_dig_004]` `[trigger: peregrine]` `[factor_trigger: astro_peregrine]` `[role: 条件分支]` Planet peregrine (no dignity) is like a wanderer without home or support—significantly weakened. → CA I #Dignities"""
    normalized_text_zh: str = """"""
    subject: str = "Planetary Dignities and Debilities"
    factor_refs: list = ['dignity_domicile', 'dignity_exaltation', 'debility_detriment', 'debility_fall', 'peregrine']
    
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
        l1_anchor="ca_v1.0.0_planetary_dignities_and_debili_001_L1",
    )
    version: str = "1.0.0"
