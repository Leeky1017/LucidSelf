"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515183
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
    semantic_id="acu_v1.0.0_1_introduction_and_definition__001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1IntroductionAndDefinition(SemanticEntry):
    """
    **Source Text** (¶1-3, Lines 366-387):

> [1] The hypothesis of a collective unconscious belongs to ...
    """
    
    original_text: str = """**Source Text** (¶1-3, Lines 366-387):

> [1] The hypothesis of a collective unconscious belongs to the class of ideas that people at first find strange but soon come to possess and use as familiar conceptions. This has been the case with the concept of the unconscious in general. After the philosophical idea of the unconscious, in the form presented chiefly by Carus and von Hartmann, had gone down under the overwhelming wave of materialism and empiricism, leaving hardly a ripple behind it, it gradually reappeared in the scientific domain of medical psychology.
>
> [2] At first the concept of the unconscious was limited to denoting the state of repressed or forgotten contents. Even with Freud, who makes the unconscious—at least metaphorically—take the stage as the acting subject, it is really nothing but the gathering place of forgotten and repressed contents, and has a functional significance thanks only to these. For Freud, accordingly, the unconscious is of an exclusively personal nature, although he was aware of its archaic and mythological thought-forms.
>
> [3] A more or less superficial layer of the unconscious is undoubtedly personal. I call it the personal unconscious. But this personal unconscious rests upon a deeper layer, which does not derive from personal experience and is not a personal acquisition but is inborn. This deeper layer I call the collective unconscious. I have chosen the term "collective" because this part of the unconscious is not individual but universal; in contrast to the personal psyche, it has contents and modes of behaviour that are more or less the same everywhere and in all individuals. It is, in other words, identical in all men and thus constitutes a common psychic substrate of a suprapersonal nature which is present in every one of us.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Collective Unconscious | Shared unconscious layer | Universal psychic substrate | Jung's core innovation distinguishing from Freud |
| Personal Unconscious | Individual repressed content | Freud's domain | Superficial layer resting on collective |
| Inborn | Present from birth | Inherited, not acquired | Distinguishes collective from personal |
| Suprapersonal | Beyond individual | Transcending personal biography | Universal human substrate |

**English Paraphrase (Primary Language)**:

Jung introduces the **collective unconscious hypothesis** by tracing the history of unconscious concepts:

**Historical context**: The philosophical unconscious (Carus, von Hartmann) was submerged by 19th-century materialism, only to resurface in medical psychology.

**Freud's limitation**: For Freud, the unconscious = repressed/forgotten personal contents. It is exclusively personal—a "gathering place" of individual biography.

**Jung's innovation**: Beneath the personal unconscious lies a **deeper, inborn layer**—the collective unconscious:
- **Not personal**: Does not derive from individual experience
- **Not acquired**: Present at birth, inherited
- **Universal**: Identical in all humans regardless of culture
- **Suprapersonal**: Constitutes common psychic substrate

**Key distinction**:
- Personal unconscious = individual, acquired, biographical
- Collective unconscious = universal, inherited, transpersonal

**Complete Chinese Interpretation (Secondary Language)**:

荣格通过追溯无意识概念的历史引入**集体无意识假说**：

**历史背景**：哲学无意识（卡鲁斯、冯·哈特曼）被19世纪唯物主义淹没，之后在医学心理学中重新浮现。

**弗洛伊德的局限**：对弗洛伊德而言，无意识 = 压抑/遗忘的个人内容。它完全是个人性的——个人传记的"聚集地"。

**荣格的创新**：在个人无意识之下存在**更深的、先天的层次**——集体无意识：
- **非个人**：不源于个人经验
- **非后天获得**：出生即存在，遗传
- **普遍性**：无论文化，所有人类都相同
- **超个人**：构成共同的心理基质

**关键区分**：
- 个人无意识 = 个体的、后天的、传记性的
- 集体无意识 = 普遍的、遗传的、超个人的

**Core Points**:
- Collective unconscious is Jung's foundational concept distinguishing his psychology from Freud's
- It is inborn, not acquired through personal experience
- It is universal, identical across all humans regardless of culture
- It constitutes a "suprapersonal" psychic substrate
- Personal unconscious rests upon this deeper collective layer
- Freud's unconscious is exclusively personal; Jung adds transpersonal dimension

**Narrative Snippets**:
- `[ns_cw9i_001]` `[trigger: collective_unconscious_definition]` `[factor_trigger: collective_unconscious AND consciousness AND personal_unconscious AND psych_layer_relation AND jung_personal_unconscious AND jung_jung_inherited AND jung_universal_patterns AND jung_personal_reductionism]` `[role: 主干]` The collective unconscious is a deeper layer that does not derive from personal experience but is inborn—universal in all humans. → ¶3
- `[ns_cw9i_002]` `[trigger: freud_limitation]` `[factor_trigger: conscious AND archetype]` `[role: 条件分支]` For Freud, the unconscious is exclusively personal—nothing but the gathering place of forgotten and repressed contents. → ¶2
- `[ns_cw9i_003]` `[trigger: suprapersonal_nature]` `[factor_trigger: complex AND archetypal_image]` `[role: 主干依赖]` The collective unconscious constitutes a common psychic substrate of suprapersonal nature present in every one of us. → ¶3

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: This definition appears in the 1954 revised version. Earlier formulations (1916-1936) used different terminology. The term "collective" was chosen specifically to contrast with "individual"—Jung considered alternatives like "universal" or "transpersonal."
- **中文**: 此定义出现在1954年修订版中。早期表述（1916-1936）使用不同术语。"集体"一词是特意选择以与"个人"对比——荣格曾考虑"普遍"或"超个人"等替代词。"""
    normalized_text_zh: str = """"""
    subject: str = "1 Introduction and Definition (¶1-3)"
    factor_refs: list = ['collective_unconscious', 'personal_unconscious', 'suprapersonal', 'engine_id', 'collective_unconscious', 'psych_semantic', 'personal_unconscious', 'psych_semantic', 'psych_layer_relation', 'psych_semantic', 'source_ref', 'rel_cw9i_001', 'jung_personal_unconscious', 'rel_cw9i_002', 'jung_universal_patterns', 'rel_cw9i_003', 'jung_personal_reductionism', 'l1_anchor', 'confidence', 'evi_cw9i_001', 'jung_collective_unconscious', 'evi_cw9i_002', 'evi_cw9i_003', 'jung_personal_unconscious', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cw9i_001', 'jung_collective_unconscious', 'astro_collective_planetary', 'map_cw9i_002', 'jung_archetype', 'tarot_major_arcana', 'map_cw9i_003', 'jung_collective_unconscious', 'dream_universal_symbols']
    
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
        l1_anchor="acu_v1.0.0_1_introduction_and_definition__001_L1",
    )
    version: str = "1.0.0"
