"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237877
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
    semantic_id="ap_v1.0.0_entry_2__three_types_of_psycho_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2ThreeTypesOfPsycho(SemanticEntry):
    """
    **Source Text** (Lines 3529-3649):
> Three Basic Types of Psychology... there is: 1) a spiritual psy...
    """
    
    original_text: str = """**Source Text** (Lines 3529-3649):
> Three Basic Types of Psychology... there is: 1) a spiritual psychology, which is a branch of philosophy or religion, and contemplates all human values, introspectively and intuitionally, in terms of beliefs, or intuitions, or transcendental perceptions. 2) a physiological psychology, which considers all processes usually classified as "psychological" from the standpoint of physiological functions. 3) an analytical psychology, which deals primarily and directly with the facts of consciousness and the structural relationship existing between the various functions of the psyche per se.
>
> ...the analyst—especially Jung—is essentially the physician or healer, who deals with the functional balance of the psychic organism as a whole... What also differentiates analytical psychology from the "physiological" type above mentioned is the fact that it is purposeful. It does not analyze for the sake of mere investigation, but with the definite aim to heal, to cure, to make whole.

**Key Term Analysis**:
- **Spiritual psychology**: `philosophical/religious` / `introspective` / `transcendental perceptions`
- **Physiological psychology**: `from physiological standpoint` / `scientific method` / `Behaviorists`
- **Analytical psychology**: `psyche as autonomous domain` / `structural relationships` / `purposeful healing`

**English Paraphrase (Primary Language)**:
Rudhyar distinguishes three psychology types: (1) Spiritual—contemplates values through intuition/belief; (2) Physiological—considers psychological processes as physiological functions; (3) Analytical—deals with psyche as autonomous domain, emphasizing structural relationships.

Jung's analytical psychology differs fundamentally: it's purposeful—"to heal, to cure, to make whole." The analyst treats the "functional balance of the psychic organism as a whole," not isolated elements. This aligns with astrology's holistic approach.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar区分三种心理学类型：(1)精神的——通过直觉/信仰思考价值；(2)生理的——将心理过程视为生理功能；(3)分析的——处理心灵作为自主领域，强调结构关系。

Jung的分析心理学根本不同：它是有目的的——"治愈、疗愈、使完整"。分析师处理"心灵有机体作为整体的功能平衡"，而非孤立元素。这与占星学的整体方法一致。

**Narrative Snippets**:
- `[ns_aop_113]` `[trigger: three_types]` `[factor_trigger: astro_three_psych AND astro_psych_vital_struct]` `[role: 主干]` Three psychology types: spiritual (intuition), physiological (functions), analytical (psyche structure). → L3536-3548
- `[ns_aop_114]` `[trigger: purposeful_healing]` `[factor_trigger: astro_purposeful AND astro_purpose_whole AND astro_self_real]` `[role: 总结]` Analytical psychology purposeful—to heal, make whole, treat psychic organism as whole. → L3654-3656"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Three Types of Psychology"
    factor_refs: list = ['astro_analytical_psych', 'astro_purposeful_heal']
    
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
        l1_anchor="ap_v1.0.0_entry_2__three_types_of_psycho_001_L1",
    )
    version: str = "1.0.0"
