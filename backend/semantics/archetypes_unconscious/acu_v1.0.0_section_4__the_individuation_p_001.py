"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541801
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
    semantic_id="acu_v1.0.0_section_4__the_individuation_p_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section4TheIndividuationP(SemanticEntry):
    """
    **Source Text** (¶520-524, Lines 7992-8056):

> [520] If we now turn back to the problem of individu...
    """
    
    original_text: str = """**Source Text** (¶520-524, Lines 7992-8056):

> [520] If we now turn back to the problem of individuation, we shall see ourselves faced with a rather extraordinary task: the psyche consists of two incongruous halves which together should form a whole.
>
> [521] For this reason we must look for a different solution. We believe in ego-consciousness and in what we call reality... For us it makes sense to concern ourselves with reality.
>
> [522] Conscious and unconscious do not make a whole when one of them is suppressed and injured by the other. If they must contend, let it at least be a fair fight with equal rights on both sides. Both are aspects of life. Consciousness should defend its reason and protect itself, and the chaotic life of the unconscious should be given the chance of having its way too—as much of it as we can stand. This means open conflict and open collaboration at once. That, evidently, is the way human life should be. It is the old game of hammer and anvil: between them the patient iron is forged into an indestructible whole, an "individual."
>
> [523] This, roughly, is what I mean by the individuation process. As the name shows, it is a process or course of development arising out of the conflict between the two fundamental psychic facts.
>
> [524] How the harmonizing of conscious and unconscious data is to be undertaken cannot be indicated in the form of a recipe. It is an irrational life-process which expresses itself in definite symbols... Out of this union emerge new situations and new conscious attitudes. I have therefore called the union of opposites the "transcendent function." This rounding out of the personality into a whole may well be the goal of any psychotherapy that claims to be more than a mere cure of symptoms.

**English Paraphrase**: Individuation = psyche's two incongruous halves forming whole. Conscious and unconscious need fair fight—equal rights. Both are life; neither should suppress other. Hammer and anvil: patient iron forged into "individual." Individuation = development from conflict of two fundamental psychic facts. Cannot be recipe—irrational life-process expressing in symbols. Union of opposites = "transcendent function." Goal: rounding personality into whole.

**中文诠释**: 个体化=心灵的两个不协调半部形成整体。意识和无意识需要公平斗争——平等权利。两者都是生命；都不应压制对方。锤子和砧：耐心的铁被锻造成"个体"。个体化=两个基本心理事实冲突中的发展。不能是配方——非理性生命过程以象征表达。对立统一="超越功能"。目标：将人格圆满为整体。

**Narrative Snippets**:
- `[ns_cw9i_VIII_006]` `[trigger: fair_fight]` `[factor_trigger: jung_individuation AND jung_conflict]` `[role: 主干]` Individuation = fair fight between conscious and unconscious; hammer and anvil forging "individual." → ¶522
- `[ns_cw9i_VIII_007]` `[trigger: transcendent_function]` `[factor_trigger: jung_opposites AND jung_transcendent]` `[role: 总结]` Union of opposites = "transcendent function"—goal of psychotherapy beyond symptom cure. → ¶524"""
    normalized_text_zh: str = """"""
    subject: str = "Section 4: The Individuation Process (¶520-524)"
    factor_refs: list = ['individuation_definition', 'fair_fight', 'hammer_anvil', 'transcendent_function', 'conscious', 'jung_opposites_union']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_section_4__the_individuation_p_001_L1",
    )
    version: str = "1.0.0"
