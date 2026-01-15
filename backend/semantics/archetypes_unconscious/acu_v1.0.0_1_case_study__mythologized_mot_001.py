"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568723
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
    semantic_id="acu_v1.0.0_1_case_study__mythologized_mot_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1CaseStudyMythologizedMot(SemanticEntry):
    """
    **Source Text** (¶138-141, Lines 2198-2252):

> [138] I remember a case... The man had made drawings...
    """
    
    original_text: str = """**Source Text** (¶138-141, Lines 2198-2252):

> [138] I remember a case... The man had made drawings which showed the mother first as a superhuman being, and then as a figure of woe, with bloody mutilations... The drawings clearly represented a diminishing climax: first the mother was a divine hermaphrodite, who then, through the son's disappointing experience of reality, was robbed of its androgynous, Platonic perfection and changed into the woeful figure of an ordinary old woman.
>
> [139] The son's disappointment effected a castration of the hermaphroditic mother: this was the patient's so-called castration complex. He had tumbled down from his childhood Olympus and was no longer the son-hero of a divine mother. His so-called fear of castration was fear of real life, which refused to come up to his erstwhile childish expectations...
>
> [140] Because people have always feared that the connection with the instinctive, archetypal stage might get lost in the course of life, the custom has long since been adopted of giving the new-born child two godparents—a "godfather" and "godmother"—who represent the pair of gods who appear at its birth, illustrating the "dual birth" motif.
>
> [141] The anima image sinks back into the unconscious, but without losing its original tension and instinctivity. It is ready to spring out and project itself at the first opportunity... Actually, nobody can stand the total loss of the archetype. When that happens, it gives rise to that frightful "discontent in our culture," where nobody feels at home because a "father" and "mother" are missing.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Divine hermaphrodite | Male-female unity | Idealized mother | Before reality |
| Castration complex | Fear of loss | Fear of real life | Neurotic misunderstanding |
| Dual birth | Physical + spiritual | Godparents tradition | Archetype preservation |
| Discontent in culture | Homelessness | Loss of archetypes | Freud's Unbehagen |

**English Paraphrase (Primary Language)**:

**Mythologized mother case**:
A patient drew the mother first as **superhuman divine hermaphrodite**, then as a figure of woe with bloody mutilations. This represented a **diminishing climax**: mother first = divine androgynous perfection; after reality's disappointment = ordinary old woman. From birth, mother was assimilated to archetypal **syzygy** (male-female conjunction), appearing perfect and superhuman.

**Castration complex reinterpreted**:
Son's disappointment "castrated" the hermaphroditic mother. His **castration complex** = tumbling from childhood Olympus, no longer son-hero of divine mother. "Fear of castration" = **fear of real life** that lacks mythological meaning. Life becomes "godless"—dire loss of hope and energy.

**Godparents as archetype preservation**:
People have always feared losing connection to instinctive, archetypal stage. Hence the tradition of **godparents** ("godfather" and "godmother")—representing the pair of gods at birth, illustrating the **"dual birth" motif**.

**Anima persists**:
Anima image sinks into unconscious but **doesn't lose tension**—ready to spring out and project. Nobody can stand **total loss of the archetype**. When that happens: frightful "discontent in our culture"—nobody feels at home because **"father" and "mother" are missing**.

**Complete Chinese Interpretation (Secondary Language)**:

**神化母亲的案例**：
一位患者画出母亲先是**超人的神性雌雄同体**，然后是带有血腥残缺的悲惨形象。这代表了**递减高潮**：母亲先 = 神圣双性完美；现实失望后 = 普通老妇。从出生起，母亲就被同化为原型**合体**（男女结合），显得完美和超人。

**阉割情结重释**：
儿子的失望"阉割"了雌雄同体母亲。他的**阉割情结** = 从童年奥林匹斯跌落，不再是神圣母亲的英雄儿子。"阉割恐惧" = **对现实生活的恐惧**，现实缺乏神话意义。生活变得"没有神"——希望和能量的可怕丧失。

**教父母作为原型保存**：
人们总是害怕失去与本能、原型阶段的联系。因此有**教父母**（"教父"和"教母"）的传统——代表出生时出现的神对，说明**"双重出生"母题**。

**阿尼玛持续存在**：
阿尼玛意象沉入无意识但**不失张力**——准备跳出并投射。没有人能承受**原型的完全丧失**。当那发生时：可怕的"文化中的不满"——没有人感到在家，因为**"父亲"和"母亲"缺失**。

**Core Points**:
- Mother mythologized as divine hermaphrodite in childhood
- Reality disappoints—"castration" of androgynous perfection
- Castration complex = fear of non-mythological real life
- "Godless" life = loss of hope and energy
- Godparents tradition preserves archetypal pair (dual birth)
- Anima sinks but retains tension—ready to project
- Total archetype loss = cultural discontent ("Unbehagen")
- Missing "father" and "mother" = psychological homelessness

**Narrative Snippets**:
- `[ns_cw9i_II_020]` `[trigger: hermaphrodite_mother]` `[factor_trigger: jung_syzygy]` `[role: 条件分支]` The mother was first a divine hermaphrodite, then through reality's disappointment, changed into an ordinary old woman—this was the patient's "castration." → ¶138
- `[ns_cw9i_II_021]` `[trigger: castration_reframed]` `[factor_trigger: jung_castration_complex]` `[role: 主干]` "Fear of castration" was fear of real life, which refused to come up to childish expectations and lacked mythological meaning—life became "godless." → ¶139
- `[ns_cw9i_II_022]` `[trigger: dual_birth]` `[factor_trigger: jung_godparents]` `[role: 条件分支]` Godparents represent the pair of gods who appear at birth—the "dual birth" motif preserving connection to archetypal stage. → ¶140
- `[ns_cw9i_II_023]` `[trigger: archetype_loss]` `[factor_trigger: jung_archetype]` `[role: 总结]` Nobody can stand total loss of the archetype—when that happens, it gives rise to frightful "discontent in culture" where nobody feels at home. → ¶141"""
    normalized_text_zh: str = """"""
    subject: str = "1 Case Study: Mythologized Mother (¶138-141)"
    factor_refs: list = ['engine_id', 'demythologization', 'psych_semantic', 'castration_reframed', 'psych_semantic', 'dual_birth', 'psych_semantic', 'cultural_discontent', 'psych_semantic', 'source_ref', 'causes', 'demythologization', 'destructive', 'preserves', 'archetype', 'protective', 'causes', 'cultural_discontent', 'destructive', 'concept_dual_parents', 'parent_dream']
    
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
        l1_anchor="acu_v1.0.0_1_case_study__mythologized_mot_001_L1",
    )
    version: str = "1.0.0"
