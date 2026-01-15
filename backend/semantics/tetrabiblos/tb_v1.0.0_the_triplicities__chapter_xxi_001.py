"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182674
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
    semantic_id="tb_v1.0.0_the_triplicities__chapter_xxi_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheTriplicitiesChapterXxi(SemanticEntry):
    """
    **Source Text** (Lines 2440-2457):
> The triplicity preserves accordance with an equilateral triangl...
    """
    
    original_text: str = """**Source Text** (Lines 2440-2457):
> The triplicity preserves accordance with an equilateral triangle, and the whole zodiacal orbit is defined by three circles... The first triangle, or triplicity, is formed by three masculine signs, Aries, Leo, and Sagittarius, having the Sun, Jupiter, and Mars as lords by house. Mars, however, being contrary in condition to the solar influence, this triplicity receives, as its lords, only Jupiter and the Sun. By day, therefore, the Sun claims the principal co-regency of it, and Jupiter by night.

**English Paraphrase (Primary Language)**:
Ptolemy explains the **triplicity (elemental) system**:

- **Fire triplicity** (Aries, Leo, Sagittarius): Masculine, Sun and Jupiter as lords (Sun by day, Jupiter by night)—Mars excluded due to contrary nature
- **Earth triplicity** (Taurus, Virgo, Capricorn): Feminine, Venus and Moon as lords
- **Air triplicity** (Gemini, Libra, Aquarius): Masculine, Saturn and Mercury as lords
- **Water triplicity** (Cancer, Scorpio, Pisces): Feminine, Mars and Moon as lords

Each triplicity has a **day lord** and **night lord**—the day lord takes precedence in day charts, the night lord in night charts. This is the basis for **triplicity dignities** in traditional astrology.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密解释了**三分性（元素）系统**：

- **火象三分性**（白羊座、狮子座、射手座）：阳性，太阳和木星为主星（白天太阳，夜间木星）——火星因性质相反被排除
- **土象三分性**（金牛座、室女座、摩羯座）：阴性，金星和月亮为主星
- **风象三分性**（双子座、天秤座、水瓶座）：阳性，土星和水星为主星
- **水象三分性**（巨蟹座、天蝎座、双鱼座）：阴性，火星和月亮为主星

每个三分性都有一个**日间主星**和**夜间主星**——日间主星在日盘中优先，夜间主星在夜盘中优先。这是传统占星学中**三分性尊贵**的基础。

**Core Points**:
- Fire (Aries/Leo/Sagittarius): Sun (day), Jupiter (night)
- Earth (Taurus/Virgo/Capricorn): Venus (day), Moon (night)
- Air (Gemini/Libra/Aquarius): Saturn (day), Mercury (night)
- Water (Cancer/Scorpio/Pisces): Mars (day), Moon (night)
- Day/night lords take precedence based on chart sect

**Narrative Snippets**:
- `[ns_tetra_i050]` `[trigger: triplicity_system]` `[factor_trigger: astro_sign_triplicity]` `[role: 主干]` The zodiac is divided into four triplicities based on equilateral triangles, each with day and night lords. → Source Text I.21
- `[ns_tetra_i051]` `[trigger: fire_triplicity]` `[factor_trigger: astro_sign_aries OR astro_sign_leo OR astro_sign_sagittarius]` `[role: 条件分支]` Fire triplicity (Aries, Leo, Sagittarius): Sun rules by day, Jupiter by night. → Source Text I.21

**Textual Criticism**: N/A: Standard triplicity doctrine."""
    normalized_text_zh: str = """"""
    subject: str = "The Triplicities (Chapter XXI)"
    factor_refs: list = ['engine_id', 'sign_triplicity', 'astrology_classical', 'source_ref', 'rel_i_019', 'sign_triplicity', 'supporting', 'evi_i_015', 'sign_triplicity', 'rule_triplicity', 'concept_triplicity', 'sign_triplicity', 'temperament']
    
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
        l1_anchor="tb_v1.0.0_the_triplicities__chapter_xxi_001_L1",
    )
    version: str = "1.0.0"
