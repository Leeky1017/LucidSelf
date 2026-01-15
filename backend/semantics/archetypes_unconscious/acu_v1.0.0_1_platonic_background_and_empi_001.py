"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491432
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
    semantic_id="acu_v1.0.0_1_platonic_background_and_empi_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1PlatonicBackgroundAndEmpi(SemanticEntry):
    """
    **Source Text** (¶148-150, Lines 2330-2374):

> [148] The concept of the Great Mother belongs to the...
    """
    
    original_text: str = """**Source Text** (¶148-150, Lines 2330-2374):

> [148] The concept of the Great Mother belongs to the field of comparative religion and embraces widely varying types of mother-goddess. The concept itself is of no immediate concern to psychology, because the image of a Great Mother in this form is rarely encountered in practice... The symbol is obviously a derivative of the mother archetype...
>
> [149] In former times... it was not too difficult to understand Plato's conception of the Idea as supraordinate and pre-existent to all phenomena. "Archetype," far from being a modern term, was already in use before the time of St. Augustine, and was synonymous with "Idea" in the Platonic usage... Were I a philosopher, I should continue in this Platonic strain and say: Somewhere, in "a place beyond the skies," there is a prototype or primordial image of the mother that is pre-existent and supraordinate to all phenomena in which the "maternal," in the broadest sense of the term, is manifest. But I am an empiricist, not a philosopher...
>
> [150] Yet every victory contains the germ of future defeat... Kant's doctrine of categories... paves the way for a rebirth of the Platonic spirit. If it be true that there can be no metaphysics transcending human reason, it is no less true that there can be no empirical knowledge that is not already caught and limited by the a priori structure of cognition.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Great Mother | Religious goddess | Comparative religion concept | Not direct psychology |
| Mother archetype | Psychological pattern | Underlying the Great Mother | Jung's focus |
| Platonic Idea | Supraordinate form | Pre-existent prototype | Philosophical background |
| A priori structure | Pre-experiential forms | Kant's categories | Modern parallel |

**English Paraphrase (Primary Language)**:

Jung establishes his **empirical position** on archetypes:

**Great Mother vs Mother Archetype**:
- Great Mother = comparative religion concept (mother-goddesses)
- Mother archetype = psychological foundation (Jung's focus)
- Great Mother is "derivative" of the archetype

**Platonic parallel**:
- "Archetype" used before St. Augustine = synonymous with Platonic "Idea"
- Plato: Ideas are supraordinate and pre-existent to phenomena
- A philosopher would say: primordial mother-image exists "beyond the skies"

**Jung's empiricist stance**:
- "I am an empiricist, not a philosopher"
- Cannot presuppose his own temperament is universal
- But: Kant's categories bridge empiricism and Platonism
- A priori structure of cognition shapes all empirical knowledge

**Complete Chinese Interpretation (Secondary Language)**:

荣格确立其对原型的**经验主义立场**：

**大母神vs母亲原型**：
- 大母神 = 比较宗教概念（母神）
- 母亲原型 = 心理学基础（荣格焦点）
- 大母神是原型的"衍生物"

**柏拉图平行**：
- "原型"在圣奥古斯丁之前使用 = 等同于柏拉图"理念"
- 柏拉图：理念是超越和先于现象的
- 哲学家会说：原初母亲意象存在于"天外"

**荣格的经验主义立场**：
- "我是经验主义者，非哲学家"
- 不能预设自己的气质是普遍的
- 但：康德的范畴桥接经验主义与柏拉图主义
- 认知的先验结构塑造所有经验知识

**Core Points**:
- Great Mother (religion) derives from mother archetype (psychology)
- "Archetype" = ancient term, synonymous with Platonic Idea
- Jung positions himself as empiricist, not metaphysician
- But acknowledges a priori structures shape cognition (Kantian)
- Archetypes are psychological equivalents of Platonic Ideas

**Narrative Snippets**:
- `[ns_cw9i_III_001]` `[trigger: archetype_platonic]` `[factor_trigger: jung_archetype AND jung_jung_platonic_idea AND jung_a_priori_form]` `[role: 主干]` "Archetype" was synonymous with "Idea" in Platonic usage—pre-existent and supraordinate to phenomena. → ¶149
- `[ns_cw9i_III_002]` `[trigger: jung_empiricist]` `[factor_trigger: jung_methodology AND empiricist_stance]` `[role: 条件分支]` I am an empiricist, not a philosopher—I cannot presuppose my own disposition is universal. → ¶149
- `[ns_cw9i_III_003]` `[trigger: apriori_cognition]` `[factor_trigger: jung_archetype]` `[role: 主干依赖]` There can be no empirical knowledge that is not already caught and limited by the a priori structure of cognition. → ¶150"""
    normalized_text_zh: str = """"""
    subject: str = "1 Platonic Background and Empirical Position (¶148-150)"
    factor_refs: list = ['engine_id', 'great_mother', 'psych_semantic', 'mother_archetype', 'psych_semantic', 'empiricist_stance', 'psych_semantic', 'source_ref', 'causal', 'jung_religious_image', 'complementary', 'jung_a_priori_form', 'l1_anchor', 'confidence', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'jung', 'astro', 'equivalent', 'jung', 'tarot', 'analogous']
    
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
        l1_anchor="acu_v1.0.0_1_platonic_background_and_empi_001_L1",
    )
    version: str = "1.0.0"
