"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237802
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
    semantic_id="ap_v1.0.0_entry_8__holistic_logic_vs_int_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry8HolisticLogicVsInt(SemanticEntry):
    """
    **Source Text** (Lines 2316-2398):
> Astrology and Holistic Logic... true astrology is the mathemati...
    """
    
    original_text: str = """**Source Text** (Lines 2316-2398):
> Astrology and Holistic Logic... true astrology is the mathematics of wholeness. It is "holistic logic" in opposition to the "intellectual logic" of this present Western civilization. It deals with wholes. It studies the structural harmony, the growth, development and the disintegration or transfiguration of wholes...
>
> Intellectual logic deals with "parts;" holistic logic with "wholes." All intellectually logical propositions... are essentially tautologies. They equate judgments concerning the realm of "parts." They see that parts fit well causally, one with the others. They are strictly analytical propositions...
>
> The scaffold represents the outside view of the world, a view which deals with parts as if they were not integral components... But the moment the whole becomes an operating unit, parts cease to be merely parts; they become functional organs of the organic whole...
>
> True astrology deals, exclusively and integrally, with operative wholes. It deals with them just at the precise moment when they emerge into the condition of wholes; when they become able to maintain independent operation as wholes at their own level of being...
>
> Astrology is rooted in the mystery of time.

**Key Term Analysis**:
- **Holistic logic**: `deals with wholes` / `opposed to intellectual logic` / `mathematics of wholeness`
- **Intellectual logic**: `deals with parts` / `tautologies` / `causal fitting` / `analytical`
- **Operative wholes**: `moment of emergence` / `independent operation` / `precise moment of integration`
- **Parts → organs**: `when whole operates` / `functional organs` / `not mere parts`
- **Time mystery**: `astrology rooted in time` / `quality of moment` / `unknown in science`

**English Paraphrase (Primary Language)**:
Rudhyar declares astrology "the mathematics of wholeness"—"holistic logic" opposed to Western "intellectual logic." Intellectual logic deals with parts, producing tautologies that show causal fitting. Holistic logic deals with wholes.

Crucially, when a whole operates, parts become functional organs—no longer mere parts. True astrology deals exclusively with "operative wholes" at "the precise moment when they emerge into the condition of wholes"—i.e., the birth moment.

The space factor (structure) must be known independently (from physiology, psychology). The time factor is astrology's domain. "Astrology is rooted in the mystery of time"—a mystery science cannot touch.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar宣称占星学是"整体性的数学"——"整体论逻辑"与西方"知性逻辑"相对。知性逻辑处理部分，产生显示因果配合的同义反复。整体论逻辑处理整体。

关键是，当整体运作时，部分成为功能器官——不再是单纯的部分。真正的占星学专门处理"运作的整体"，在它们"涌现为整体状态的确切时刻"——即出生时刻。

空间因素（结构）必须独立知晓（从生理学、心理学）。时间因素是占星学的领域。"占星学植根于时间的奥秘"——科学无法触及的奥秘。

**Core Points**:
- True astrology = mathematics of wholeness
- Holistic logic vs intellectual logic
- Intellectual logic = parts, tautologies, causal
- Holistic logic = wholes, emergence
- Parts become organs when whole operates
- Astrology deals with operative wholes
- Precise moment of emergence = birth
- Space factor known independently
- Time factor = astrology's domain
- Astrology rooted in mystery of time

**Narrative Snippets**:
- `[ns_aop_085]` `[trigger: holistic_logic]` `[factor_trigger: holistic_logic AND intellectual_logic AND astro_hol_logic_struct]` `[role: 主干]` True astrology = mathematics of wholeness, holistic logic vs intellectual logic of Western civilization. → L2318-2322
- `[ns_aop_086]` `[trigger: parts_organs]` `[factor_trigger: parts AND organs]` `[role: 主干依赖]` When whole operates, parts cease to be mere parts—become functional organs. → L2351-2360
- `[ns_aop_087]` `[trigger: operative_wholes]` `[factor_trigger: astro_operative AND astro_oper_wholes]` `[role: 条件分支]` Astrology deals with operative wholes at precise moment of emergence into independent operation. → L2368-2373
- `[ns_aop_088]` `[trigger: time_mystery]` `[factor_trigger: astro_time_mystery]` `[role: 总结]` Astrology rooted in mystery of time—almost entirely unknown in science. → L2396-2398"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 8: Holistic Logic vs Intellectual Logic"
    factor_refs: list = ['astro_holistic_logic', 'astro_operative_wholes', 'astro_parts_organs', 'astro_time_mystery']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_8__holistic_logic_vs_int_001_L1",
    )
    version: str = "1.0.0"
