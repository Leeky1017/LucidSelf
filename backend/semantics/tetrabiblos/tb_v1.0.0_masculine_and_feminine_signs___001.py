"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182604
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
    semantic_id="tb_v1.0.0_masculine_and_feminine_signs___001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class MasculineAndFeminineSigns(SemanticEntry):
    """
    **Source Text** (Lines 2137-2180):
> Among the twelve signs, six are called masculine and diurnal, a...
    """
    
    original_text: str = """**Source Text** (Lines 2137-2180):
> Among the twelve signs, six are called masculine and diurnal, and six feminine and nocturnal. They are arranged in alternate order, one after the other, as the day is followed by the night, and as the male is coupled with the female. The commencement belongs to Aries; since the moisture of spring forms an introduction for the other seasons. And, as the male sex governs, and the active principle takes precedence of the passive, the signs of Aries and Libra are consequently considered to be masculine and diurnal. The signs immediately following them are feminine and nocturnal; and the rest are consecutively arranged as masculine and feminine, by alternate order.

**English Paraphrase (Primary Language)**:
Ptolemy assigns **gender to signs** in alternating pattern starting from Aries:
- **Masculine/Diurnal signs**: Aries, Gemini, Leo, Libra, Sagittarius, Aquarius (odd signs)
- **Feminine/Nocturnal signs**: Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces (even signs)

The rationale: Aries is masculine because (1) it begins the zodiac at spring, (2) the active/masculine principle precedes the passive/feminine. Signs alternate thereafter.

Alternative methods exist: some astrologers assign gender based on (1) the ascending sign, or (2) quadrant position (oriental quadrants = masculine, occidental = feminine).

**Complete Chinese Interpretation (Secondary Language)**:
托勒密以从白羊座开始的交替模式为**星座分配性别**：
- **阳性/昼间星座**：白羊座、双子座、狮子座、天秤座、射手座、水瓶座（奇数星座）
- **阴性/夜间星座**：金牛座、巨蟹座、室女座、天蝎座、摩羯座、双鱼座（偶数星座）

理由：白羊座是阳性的因为(1)它在春季开始黄道，(2)主动/阳性原则先于被动/阴性。此后星座交替。

存在替代方法：一些占星家根据(1)上升星座，或(2)象限位置（东方象限=阳性，西方=阴性）分配性别。

**Core Points**:
- Signs alternate masculine/feminine starting from Aries
- Masculine = active, diurnal; Feminine = passive, nocturnal
- Aries is masculine as zodiacal beginning and spring initiator
- Alternative systems exist (quadrant-based)

**Narrative Snippets**:
- `[ns_tetra_i073]` `[trigger: sign_gender]` `[factor_trigger: astro_sign_masculine OR astro_sign_feminine]` `[role: 主干]` Signs are alternately masculine and feminine, starting from masculine Aries. → Source Text I.15"""
    normalized_text_zh: str = """"""
    subject: str = "Masculine and Feminine Signs (Chapter XV)"
    factor_refs: list = ['sign_gender', 'engine_id', 'sign_gender', 'astrology_classical', 'source_ref', 'rel_i_028', 'sign_gender', 'characterizing', 'evi_i_023', 'sign_gender', 'rule_sign_gender', 'concept_sign_gender', 'sign_gender', 'anima_animus']
    
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
        l1_anchor="tb_v1.0.0_masculine_and_feminine_signs___001_L1",
    )
    version: str = "1.0.0"
