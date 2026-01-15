"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147323
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
    semantic_id="ca_v1.0.0_dignity_and_debility___power_a_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class DignityAndDebilityPowerA(SemanticEntry):
    """
    #### Source Text

"Dignities are certaine Priviledges bestowed upon Planets, whereby they become pow...
    """
    
    original_text: str = """#### Source Text

"Dignities are certaine Priviledges bestowed upon Planets, whereby they become powerful in Operation, and more effectuall. The principall Dignities are Essential and Accidental. Essential Dignities are when a Planet is in his owne House, Exaltation, Triplicity, Terme, or Face. Accidental Dignities are when a Planet is in an Angle, swift in Motion, in Haiz, joyned to Jupiter or Venus. Debilities are the contrary: when a Planet is in his Detriment, Fall, Peregrination, Retrograde, Combust, Cadent, under Sunbeams, or joyned to maleficks."

#### Key Term Analysis

- **Essential Dignity**: Dignity based on zodiacal sign position; inherent to planet's location in zodiac
- **Accidental Dignity**: Dignity from circumstantial factors (house, motion, aspects); context-dependent
- **Haiz**: Planet in sect-appropriate position (diurnal planet in day chart above horizon)
- **Peregrine**: Planet with no essential dignity; "foreign" or "wandering" without resources
- **Combust**: Planet within ~8° of Sun, overwhelmed and invisible; severely weakened

#### English Paraphrase (Primary Language)

**Dignity** measures a planet's **power and effectiveness** in horary judgment. A dignified planet = strong significator capable of acting successfully. A debilitated planet = weak significator struggling or failing. Dignity assessment is **crucial for judgment**—even perfect applying aspects fail if significators too weak.

**Essential Dignities** (本质尊贵) - based on zodiac sign:

**1. Domicile/Rulership** (+5 points):
- Planet in own sign: Sun in Leo, Moon in Cancer, Mercury in Gemini/Virgo, etc.
- **Maximum power**, acts naturally, fully expressive

**2. Exaltation** (+4 points):
- Planet in sign of greatest power: Sun in Aries, Moon in Taurus, Saturn in Libra, etc.
- **Honored guest**, acts with special effectiveness

**3. Triplicity** (+3 points):
- Planet ruling element (Fire/Earth/Air/Water) in day/night/participating ruler
- **Comfortable**, acts with support

**4. Term** (+2 points):
- Planet ruling specific degree range within sign
- **Moderate power**, acts adequately

**5. Face/Decan** (+1 point):
- Planet ruling 10° section of sign
- **Minimal power**, barely capable

**Essential Debilities** (本质衰弱):

**1. Detriment** (-5 points):
- Planet in sign opposite domicile: Sun in Aquarius, Moon in Capricorn, Mars in Libra
- **Exile**, acts against natural grain, uncomfortable

**2. Fall** (-4 points):
- Planet in sign opposite exaltation: Sun in Libra, Moon in Scorpio, Saturn in Aries
- **Dishonored**, weakened, ineffective

**3. Peregrine** (0 points, but weakened):
- Planet has no essential dignity (not in any of 5 above)
- **Stranger**, wandering, no resources or support

**Accidental Dignities** (偶然尊贵) - based on house/motion/aspects:

**Strengthening**:
- **Angular** (in 1st, 4th, 7th, 10th houses): +5, maximum visibility/power
- **Direct motion** at average speed: +2, effective action
- **Swift motion** (faster than average): +2, eager action
- **Oriental** (rising before Sun): +2, independence
- **Free from combustion**: +5, not overwhelmed by Sun
- **Cazimi** (exact conjunction with Sun, within 17'): +5, heart of Sun, empowered
- **Conjunct Jupiter**: +5, fortunate, expanded
- **Conjunct Venus**: +3, pleasant, attractive
- **Trine/sextile Jupiter/Venus**: +3, benefic support

**Weakening**:
- **Cadent** (in 3rd, 6th, 9th, 12th houses): -5, hidden, ineffective
- **Retrograde**: -5, reversed, delayed, inward
- **Slow motion**: -2, sluggish, reluctant
- **Occidental** (setting after Sun): -2, subordinate
- **Combust** (within ~8° of Sun): -5, overwhelmed, invisible
- **Under sunbeams** (within 17° of Sun): -4, weakened by Sun
- **Besieged** (between Mars and Saturn): -5, trapped, attacked
- **Conjunct/oppose Mars/Saturn**: -3/-5, afflicted by malefics

**Practical judgment**: Tally dignity points for each significator:
- **+10 or more**: Very strong, matter succeeds easily
- **+5 to +9**: Strong, matter succeeds with effort
- **0 to +4**: Weak, matter difficult, may fail
- **-5 or below**: Very weak, matter likely fails

**Example**: "Will I win the lawsuit?"
- **Your significator** (Ascendant ruler): Mars in Capricorn (fall -4), retrograde (-5), in 1st house (+5) = **-4 points** (weak)
- **Opponent** (7th ruler): Venus in Pisces (exalted +4), direct, in 7th house (+5), trine Jupiter (+3) = **+12 points** (very strong)
- **Judgment**: Opponent stronger, even if applying aspect exists, you'll likely lose or settle unfavorably

#### Complete Chinese Interpretation (Secondary Language)

**尊贵**(Dignity)与**衰弱**(Debility)度量行星力量，决定征象星是否有力量达成事项。**本质尊贵**：入庙(Domicile，+5分，如火星在白羊)、擢升(Exaltation，+4分，如太阳在白羊)、三分(Triplicity，+3分)、界(Term，+2分)、面(Face，+1分)。**偶然尊贵**：角宫(+5分)、续宫(+4分)、顺行(+4分)、吉相位(+3-5分)、月亮增光(+2分)、速度快(+2分)。**本质衰弱**：失势(Detriment，-5分，如火星在天秤)、落陷(Fall，-4分，如太阳在天秤)、游魂(Peregrine，0分，无尊贵)。**偶然衰弱**：果宫(-5分)、逆行(-5分)、凶相位(-3-5分)、燃烧(-5分)、太阳光束下(-4分)、速度慢(-2分)。**判断原则**：总分+5以上=强有力完成；-5以下=软弱无力失败；0分附近=勉强或部分成功。尊贵强的征象星能克服困难达成愿望；衰弱的征象星即使有入相相位也可能失败。

#### Core Points

- **Dignity = power**: Measures planet's strength and effectiveness
- **Essential dignity**: Based on zodiac sign (domicile +5 to face +1)
- **Essential debility**: Detriment -5, fall -4, peregrine 0
- **Accidental dignity**: Based on house/motion/aspects (angular +5, benefic aspects +3-5)
- **Accidental debility**: Cadent -5, retrograde -5, malefic aspects -3-5, combustion -5
- **Point system**: Tally dignities for judgment strength
- **Judgment impact**: Even perfect aspects fail if significators too weak

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's dignity system synthesizes Ptolemy (essential dignities), Dorotheus (triplicity rulers), and Arabic refinements (terms, faces). The point-scoring system (domicile +5, face +1, etc.) is Lilly's practical adaptation for judgment. "Haiz" (Arabic) and "sect" (Greek hairesis) add day/night considerations. Modern astrologers debate outer planet dignities (Uranus in Aquarius?).
- **中文**: Lilly的尊贵系统综合了托勒密（本质尊贵）、多罗修斯（三分主）和阿拉伯细化（界、面）。分数系统（入庙+5、面+1等）是Lilly的实用判断改编。"Haiz"（阿拉伯语）和"sect"（希腊语haeresis）添加了日/夜考量。现代占星师争论外行星尊贵（天王在水瓶？）。

**Narrative Snippets**:
- `[ns_lilly_019]` `[trigger: dignities_definition]` `[factor_trigger: astro_dignity AND astro_privilege AND astro_planetary_power]` `[role: 主干]` Dignities are certaine Priviledges bestowed upon Planets, whereby they become powerful in Operation, and more effectuall. → Source Text
- `[ns_lilly_020]` `[trigger: domicile_exaltation]` `[factor_trigger: astro_essential_dignity AND astro_score AND astro_power_level]` `[role: 主干依赖]` Essential Dignities: when a Planet is in his owne House (+5), Exaltation (+4), Triplicity (+3), Terme (+2), or Face (+1). → Source Text
- `[ns_lilly_021]` `[trigger: debility_peregrine]` `[factor_trigger: astro_debility AND astro_weakness AND astro_planetary_failure]` `[role: 条件分支]` Debilities: Detriment (-5), Fall (-4), Peregrination (no dignity, wandering), Retrograde, Combust, Cadent—weak significators struggle or fail. → English Paraphrase
- `[ns_lilly_022]` `[trigger: dignity_judgment]` `[factor_trigger: astro_dignity AND astro_judgment AND astro_outcome_modifier]` `[role: 总结]` Even perfect applying aspects fail if significators too weak—dignity assessment is crucial for judgment. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Dignity and Debility - Power Assessment"
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_dignity_and_debility___power_a_001_L1",
    )
    version: str = "1.0.0"
