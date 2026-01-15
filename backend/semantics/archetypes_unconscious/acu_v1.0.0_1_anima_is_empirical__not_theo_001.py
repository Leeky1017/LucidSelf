"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568630
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
    semantic_id="acu_v1.0.0_1_anima_is_empirical__not_theo_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1AnimaIsEmpiricalNotTheo(SemanticEntry):
    """
    **Source Text** (¶114-118, Lines 1886-1965):

> [115] Anyone who does not know the universal distrib...
    """
    
    original_text: str = """**Source Text** (¶114-118, Lines 1886-1965):

> [115] Anyone who does not know the universal distribution and significance of the syzygy motif in the psychology of primitives, in mythology, in comparative religion, and in the history of literature, can hardly claim to say anything about the concept of the anima.
>
> [116] Although common prejudice still believes that the sole essential basis of our knowledge is given exclusively from outside ("nihil est in intellectu quod non antea fuerit in sensu"), the atomic theory of Leucippus and Democritus was not based on observations but on a "mythological" conception of smallest particles—soul-atoms known even to palaeolithic Australians.

> [114] These reflections are essential when discussing an empirical concept like that of the anima. As against the constantly reiterated prejudice that this is a theoretical invention or—worse still—sheer mythology, I must emphasize that the concept of the anima is a purely empirical concept, whose sole purpose is to give a name to a group of related or analogous psychic phenomena. The concept does no more and means no more than, shall we say, the concept "arthropods," which includes all animals with articulated body and limbs and so gives a name to this phenomenological group...
>
> [117] These forms are generally supposed to be transmitted by tradition... But where did Democritus, or whoever first spoke of minimal constitutive elements, hear of atoms? This notion had its origin in archetypal ideas, that is, in primordial images which were never reflections of physical events but are spontaneous products of the psychic factor...
>
> [118] The psychic factor must, ex hypothesi, be regarded for the present as an autonomous reality of enigmatic character... From the unconscious there emanate determining influences which, independently of tradition, guarantee in every single individual a similarity and even a sameness of experience, and also of the way it is represented imaginatively. One of the main proofs of this is the almost universal parallelism between mythological motifs, which, on account of their quality as primordial images, I have called archetypes.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Empirical concept | Experience-based | Not theoretical invention | Defense of anima |
| Psychic factor | Autonomous reality | Not epiphenomenon | Sui generis nature |
| Primordial images | Original psychic forms | Spontaneous, not reflected | Source of archetypes |
| Determining influences | Shaping forces | From unconscious | Independent of tradition |

**English Paraphrase (Primary Language)**:

Jung defends the **empirical status** of the anima concept:

**Against critics**:
- Anima is NOT "theoretical invention" or "sheer mythology"
- It is a **purely empirical concept**—naming observed phenomena
- Like "arthropods" in biology—a phenomenological classification

**Psyche as autonomous**:
- Psyche is a "factor sui generis"—cannot be reduced to physics
- It is an "autonomous reality of enigmatic character"
- Psychic processes cannot be "fabricated in a retort"

**Source of archetypes**:
- Archetypes are NOT transmitted only by tradition
- They originate as "primordial images"—spontaneous psychic products
- From unconscious come "determining influences" independent of tradition
- These guarantee "similarity and sameness of experience" across individuals
- Proof: universal parallelism of mythological motifs

**Complete Chinese Interpretation (Secondary Language)**:

荣格为阿尼玛概念的**经验地位**辩护：

**反驳批评**：
- 阿尼玛不是"理论发明"或"纯粹神话"
- 它是**纯粹经验概念**——命名观察到的现象
- 如生物学中的"节肢动物"——现象学分类

**心灵作为自主**：
- 心灵是"自成一类因素"——不能还原为物理
- 它是"神秘性质的自主实在"
- 心理过程不能"在蒸馏器中制造"

**原型的来源**：
- 原型不仅通过传统传递
- 它们起源于"原始意象"——自发的心理产物
- 从无意识来"决定性影响"独立于传统
- 这些保证跨个体的"经验相似性和同一性"
- 证据：神话母题的普遍平行

**Core Points**:
- Anima is empirical concept, not theoretical invention
- It names observed psychic phenomena (like scientific classification)
- Psyche is autonomous reality, not reducible to physiology
- Archetypes originate as spontaneous primordial images
- Universal mythological parallels prove archetype's existence
- Archetypes guarantee cross-cultural similarity of experience

**Narrative Snippets**:
- `[ns_cw9i_II_001]` `[trigger: anima_empirical]` `[factor_trigger: jung_anima]` `[role: 主干]` The concept of the anima is a purely empirical concept, whose sole purpose is to give a name to a group of related psychic phenomena—not theoretical invention. → ¶114
- `[ns_cw9i_II_002]` `[trigger: psyche_autonomous]` `[factor_trigger: jung_psyche]` `[role: 主干依赖]` The psychic factor must be regarded as an autonomous reality of enigmatic character—psychic processes cannot be fabricated in a retort. → ¶118
- `[ns_cw9i_II_003]` `[trigger: archetype_independent]` `[factor_trigger: jung_archetype]` `[role: 条件分支]` From the unconscious emanate determining influences which, independently of tradition, guarantee similarity of experience—proven by universal mythological parallels. → ¶118

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: This methodological defense responds to critics who dismissed Jung's concepts as "unscientific." Jung positions himself as empiricist against both materialists (who reduce psyche to physiology) and dogmatists (who reject unconscious phenomena). The arthropod analogy is particularly effective.
- **中文**: 这一方法论辩护回应了将荣格概念斥为"不科学"的批评者。荣格将自己定位为经验主义者，反对唯物主义者（将心灵还原为生理）和教条主义者（拒绝无意识现象）。节肢动物类比特别有效。"""
    normalized_text_zh: str = """"""
    subject: str = "1 Anima is Empirical, Not Theoretical (¶114-118)"
    factor_refs: list = ['engine_id', 'empirical_concept', 'psych_semantic', 'psychic_autonomy', 'psych_semantic', 'universal_parallels', 'psych_semantic', 'source_ref', 'validates', 'archetype', 'confirming', 'quality_of', 'jung_psyche', 'defining', 'anima', 'rule_anima_empirical', 'archetype', 'rule_archetype_proof', 'concept_empirical_psyche', 'chart_observation', 'empirical_psychology']
    
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
        l1_anchor="acu_v1.0.0_1_anima_is_empirical__not_theo_001_L1",
    )
    version: str = "1.0.0"
