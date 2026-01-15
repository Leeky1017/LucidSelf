"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182721
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
    semantic_id="tb_v1.0.0_tropical_vs_sidereal_zodiac_de_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TropicalVsSiderealZodiacDe(SemanticEntry):
    """
    **Source Text** (Lines 2825-2837):
> The beginnings of the signs, and likewise those of the terms, a...
    """
    
    original_text: str = """**Source Text** (Lines 2825-2837):
> The beginnings of the signs, and likewise those of the terms, are to be taken from the equinoctial and tropical points. This rule is not only clearly stated by writers on the subject, but is also especially evident by the demonstration constantly afforded, that their natures, influences and familiarities have no other origin than from the tropics and equinoxes... And, if other beginnings were allowed, it would either be necessary to exclude the natures of the signs from the theory of prognostication, or impossible to avoid error.

**English Paraphrase (Primary Language)**:
Ptolemy makes an **explicit defense of the tropical zodiac**: sign beginnings must be measured from the **equinoctial and tropical points** (vernal equinox = 0° Aries), not from fixed star positions. The rationale is that sign natures derive from their relationship to seasons and solstices—Aries is moist because it begins spring, not because of any particular stars.

This passage directly addresses the **precession objection**: even though the constellation Aries has drifted from the vernal equinox, the *sign* of Aries (defined as "30° after vernal equinox") retains its meaning. Using any other starting point would either invalidate sign meanings or produce errors.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密**明确为回归黄道辩护**：星座起点必须从**分至点**（春分点 = 白羊座0°）测量，而不是从恒星位置。理由是星座性质源于它们与季节和至点的关系——白羊座是湿润的因为它开始春天，而非因为任何特定恒星。

这段话直接回应了**岁差反对意见**：即使白羊座星群已经从春分点漂移，白羊座*星座*（定义为"春分后30°"）仍保留其意义。使用任何其他起点要么会使星座意义无效，要么会产生错误。

**Core Points**:
- Signs begin from equinoctial/tropical points, not fixed stars
- This is the definitive statement for tropical zodiac
- Sign natures derive from seasonal relationship
- Precession does not invalidate tropical signs
- Using sidereal starting points would cause errors
- Aries = 30° after vernal equinox, regardless of constellation

**Narrative Snippets**:
- `[ns_tetra_i056]` `[trigger: tropical_zodiac_defense]` `[factor_trigger: astro_tropical_signs]` `[role: 主干]` The beginnings of the signs are to be taken from the equinoctial and tropical points—their natures derive from these origins. → Source Text I.25
- `[ns_tetra_i057]` `[trigger: precession_addressed]` `[factor_trigger: astro_epistemology]` `[role: 总结]` If other beginnings were allowed, sign natures would be excluded from prognostication or error would be unavoidable. → Source Text I.25

**Textual Criticism**: This is the definitive Ptolemaic statement on tropical vs sidereal zodiac; cited throughout astrological history."""
    normalized_text_zh: str = """"""
    subject: str = "Tropical vs Sidereal Zodiac Defense (Chapter XXV)"
    factor_refs: list = ['engine_id', 'tropical_zodiac', 'astrology_classical', 'source_ref', 'rel_i_022', 'tropical_zodiac', 'defining', 'evi_i_018', 'tropical_zodiac', 'rule_tropical_zodiac', 'concept_tropical', 'tropical_zodiac', 'seasonal_rhythm']
    
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
        l1_anchor="tb_v1.0.0_tropical_vs_sidereal_zodiac_de_001_L1",
    )
    version: str = "1.0.0"
