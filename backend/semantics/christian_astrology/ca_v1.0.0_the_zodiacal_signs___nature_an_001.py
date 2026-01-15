"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156368
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
    semantic_id="ca_v1.0.0_the_zodiacal_signs___nature_an_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class TheZodiacalSignsNatureAn(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 86-99): "The twelve Signs are divided into four Triplicities: Fi...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 86-99): "The twelve Signs are divided into four Triplicities: Fire (Aries, Leo, Sagittarius), Earth (Taurus, Virgo, Capricorn), Air (Gemini, Libra, Aquarius), Water (Cancer, Scorpio, Pisces). Signs are also Cardinal, Fixed, or Mutable."

#### English Paraphrase (Primary Language)

**The Twelve Signs** form the ecliptic backdrop against which planets move:

| Sign | Symbol | Element | Quality | Ruler |
|------|--------|---------|---------|-------|
| Aries | ♈ | Fire | Cardinal | Mars |
| Taurus | ♉ | Earth | Fixed | Venus |
| Gemini | ♊ | Air | Mutable | Mercury |
| Cancer | ♋ | Water | Cardinal | Moon |
| Leo | ♌ | Fire | Fixed | Sun |
| Virgo | ♍ | Earth | Mutable | Mercury |
| Libra | ♎ | Air | Cardinal | Venus |
| Scorpio | ♏ | Water | Fixed | Mars |
| Sagittarius | ♐ | Fire | Mutable | Jupiter |
| Capricorn | ♑ | Earth | Cardinal | Saturn |
| Aquarius | ♒ | Air | Fixed | Saturn |
| Pisces | ♓ | Water | Mutable | Jupiter |

**Triplicities (Elements)**:
- **Fire** (♈♌♐): Hot, dry, active, enthusiastic
- **Earth** (♉♍♑): Cold, dry, practical, material
- **Air** (♊♎♒): Hot, moist, intellectual, social
- **Water** (♋♏♓): Cold, moist, emotional, intuitive

**Quadruplicities (Qualities)**:
- **Cardinal** (♈♋♎♑): Initiating, leading, direct
- **Fixed** (♉♌♏♒): Stabilizing, persistent, stubborn
- **Mutable** (♊♍♐♓): Adapting, flexible, changeable

#### Complete Chinese Interpretation (Secondary Language)

**十二星座**形成行星运行的黄道背景。**三方（元素）**：火象（白羊♈、狮子♌、射手♐）=热燥、主动；土象（金牛♉、处女♍、摩羯♑）=寒燥、实际；风象（双子♊、天秤♎、水瓶♒）=热湿、智识；水象（巨蟹♋、天蝎♏、双鱼♓）=寒湿、情感。**四正（品质）**：启动宫=发起；固定宫=稳定；变动宫=适应。

**Narrative Snippets**:
- `[ns_lilly_sign_001]` `[trigger: element_fire]` `[factor_trigger: astro_sign_fire_triplicity AND astro_hot_dry_active]` `[role: 主干]` Fire signs (Aries, Leo, Sagittarius) are hot, dry, active, enthusiastic. → CA I #Signs
- `[ns_lilly_sign_002]` `[trigger: quality_cardinal]` `[factor_trigger: astro_sign_cardinal AND astro_initiation_leadership]` `[role: 主干依赖]` Cardinal signs (Aries, Cancer, Libra, Capricorn) initiate and lead. → CA I #Signs"""
    normalized_text_zh: str = """"""
    subject: str = "The Zodiacal Signs - Nature and Qualities"
    factor_refs: list = ['triplicity', 'quadruplicity', 'quality_cardinal', 'quality_fixed', 'quality_mutable']
    
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
        l1_anchor="ca_v1.0.0_the_zodiacal_signs___nature_an_001_L1",
    )
    version: str = "1.0.0"
