"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182640
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
    semantic_id="tb_v1.0.0_signs_beholding_each_other__ch_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class SignsBeholdingEachOtherCh(SemanticEntry):
    """
    **Source Text** (Lines 2271-2292):
> Any two signs, equally distant from either tropical sign, are e...
    """
    
    original_text: str = """**Source Text** (Lines 2271-2292):
> Any two signs, equally distant from either tropical sign, are equal to each other in power; because the Sun, when present in one, makes day and night, and the divisions of time, respectively equal in duration to those which he produces when present in the other. Such signs are also said to behold each other, as well for the foregoing reasons, as because each of them rises from one and the same part of the horizon, and sets in one and the same part.

**English Paraphrase (Primary Language)**:
Ptolemy defines **signs beholding each other (antiscia)**—pairs equidistant from a solstice point:
- Signs at equal distance from Cancer/Capricorn have **equal power**
- They rise and set at the same horizon points
- Examples: Gemini-Leo, Taurus-Virgo, Aries-Libra (but these also have other relationships)

This is distinct from commanding/obeying (which uses equinoxes as reference).

**Complete Chinese Interpretation (Secondary Language)**:
托勒密定义了**互视星座（反映点）**——与至点等距的星座对：
- 与巨蟹座/摩羯座等距的星座具有**相等的力量**
- 它们从同一地平线位置升起和落下
- 例子：双子座-狮子座，金牛座-室女座

这与命令/服从不同（后者以分点为参考）。

**Core Points**:
- Signs equidistant from solstices behold each other
- Equal power (same day/night duration)
- Rise and set at same horizon points
- Antiscia relationship

**Narrative Snippets**:
- `[ns_tetra_i075]` `[trigger: signs_beholding]` `[factor_trigger: astro_sign_antiscia]` `[role: 主干]` Signs equidistant from tropical points behold each other and have equal power. → Source Text I.18"""
    normalized_text_zh: str = """"""
    subject: str = "Signs Beholding Each Other (Chapter XVIII)"
    factor_refs: list = ['engine_id', 'sign_antiscia', 'astrology_classical', 'source_ref', 'rel_i_030', 'sign_antiscia', 'mirroring', 'evi_i_025', 'sign_antiscia', 'rule_antiscia', 'concept_antiscia', 'sign_antiscia', 'shadow_self']
    
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
        l1_anchor="tb_v1.0.0_signs_beholding_each_other__ch_001_L1",
    )
    version: str = "1.0.0"
