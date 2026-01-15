"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182593
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
    semantic_id="tb_v1.0.0_tropical__equinoctial__fixed___001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TropicalEquinoctialFixed(SemanticEntry):
    """
    **Source Text** (Lines 2102-2134):
> Among the twelve signs, some are termed tropical, others equino...
    """
    
    original_text: str = """**Source Text** (Lines 2102-2134):
> Among the twelve signs, some are termed tropical, others equinoctial, others fixed, and others bicorporeal. The tropical signs are two: Cancer and Capricorn... called tropical because the Sun seems to turn... The equinoctial signs are Aries and Libra... The remaining eight signs: four are fixed (Taurus, Leo, Scorpio, Aquarius) and four bicorporeal (Gemini, Virgo, Sagittarius, Pisces).

**English Paraphrase (Primary Language)**:
Ptolemy classifies signs by their **relationship to seasonal turning points**:

- **Tropical signs** (Cancer, Capricorn): At solstices where Sun "turns" (τρέπω)
- **Equinoctial signs** (Aries, Libra): At equinoxes where day/night equal
- **Fixed signs** (Taurus, Leo, Scorpio, Aquarius): Follow tropical/equinoctial; season is "fixed" and established
- **Bicorporeal/Mutable signs** (Gemini, Virgo, Sagittarius, Pisces): Between fixed and tropical; participate in both preceding and following season

This creates the **quadruplicity** system (Cardinal/Fixed/Mutable) still used in modern astrology.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密按其**与季节转折点的关系**对星座进行分类：

- **回归星座**（巨蟹座、摩羯座）：在太阳"转向"（τρέπω）的至点
- **分点星座**（白羊座、天秤座）：在昼夜等长的分点
- **固定星座**（金牛座、狮子座、天蝎座、水瓶座）：跟随回归/分点；季节"固定"并确立
- **双体/变动星座**（双子座、室女座、射手座、双鱼座）：介于固定和回归之间；参与前后两个季节

这创造了现代占星学仍在使用的**四分性**系统（本位/固定/变动）。

**Core Points**:
- Tropical (Cardinal): Cancer, Capricorn—at solstices, initiate change
- Equinoctial (Cardinal): Aries, Libra—at equinoxes, initiate change
- Fixed: Taurus, Leo, Scorpio, Aquarius—establish and stabilize season
- Bicorporeal (Mutable): Gemini, Virgo, Sagittarius, Pisces—transition between seasons

**Narrative Snippets**:
- `[ns_tetra_i042]` `[trigger: sign_modality]` `[factor_trigger: astro_sign_modality]` `[role: 主干]` Signs are tropical, equinoctial, fixed, or bicorporeal based on relationship to seasonal turning points. → Source Text I.14
- `[ns_tetra_i043]` `[trigger: fixed_signs]` `[factor_trigger: astro_sign_fixed]` `[role: 条件分支]` Fixed signs follow tropical/equinoctial; the season is then firmly established. → Source Text I.14

**Textual Criticism**: N/A: Foundational sign classification."""
    normalized_text_zh: str = """"""
    subject: str = "Tropical, Equinoctial, Fixed, and Bicorporeal Signs (Chapter XIV)"
    factor_refs: list = ['sign_modality', 'engine_id', 'sign_modality', 'astrology_classical', 'source_ref', 'rel_i_016', 'sign_modality', 'characterizing', 'evi_i_012', 'sign_modality', 'rule_modality', 'concept_modality', 'sign_modality', 'behavioral_style']
    
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
        l1_anchor="tb_v1.0.0_tropical__equinoctial__fixed___001_L1",
    )
    version: str = "1.0.0"
