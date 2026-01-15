"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515457
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
    semantic_id="acu_v1.0.0_1_the_anima_as_soul_image___50_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1TheAnimaAsSoulImage50(SemanticEntry):
    """
    **Source Text** (¶50-53, summary from Lines 960-1100):

> [50] The first thing we meet after the sha...
    """
    
    original_text: str = """**Source Text** (¶50-53, summary from Lines 960-1100):

> [50] The first thing we meet after the shadow is the anima. She is clearly something else—a factor that is not conscious to the man, that is not part of his persona, the mask he shows to the world. She is the other, the complementary side.
>
> [52] Every man carries with him the eternal image of woman, not the image of this or that particular woman, but a definite feminine image. This image is fundamentally unconscious, an hereditary factor of primordial origin engraved in the living organic system of the man...
>
> [53] Since this image is unconscious, it is always unconsciously projected upon the person of the beloved, and is one of the chief reasons for passionate attraction or aversion.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Anima | Soul (Latin) | Feminine in man | Contrasexual archetype |
| Soul-image | Inner feminine figure | Guide to unconscious | Psychopomp function |
| Projection | Casting outward | Seeing inner on outer | Love psychology |
| Contrasexual | Opposite sex within | Inner complement | Gender psychology |

**English Paraphrase (Primary Language)**:

After the shadow comes the **Anima**—the feminine archetype in men:

**Nature of Anima**:
- Not part of persona (social mask)
- "The other, the complementary side"
- Eternal image of woman—not specific woman but **archetypal feminine**
- Fundamentally unconscious, inherited, primordial

**Projection mechanism**:
- Anima is unconsciously projected onto beloved
- Chief reason for "passionate attraction or aversion"
- Man falls in love with his own anima reflected in a woman

**Function**:
- After shadow: anima is next encounter in descent
- Acts as psychopomp (soul-guide) to deeper unconscious
- Mediates between ego and collective unconscious

**Complete Chinese Interpretation (Secondary Language)**:

在阴影之后是**阿尼玛**——男性中的女性原型：

**阿尼玛的性质**：
- 非人格面具的一部分
- "另一个，互补的一面"
- 永恒的女性意象——非具体女性而是**原型女性**
- 根本上是无意识的、遗传的、原始的

**投射机制**：
- 阿尼玛被无意识地投射到所爱之人身上
- "激情吸引或厌恶"的主要原因
- 男性爱上反映在女性中的自己阿尼玛

**功能**：
- 阴影之后：阿尼玛是下降中的下一个相遇
- 作为psychopomp（灵魂向导）通向更深无意识
- 在自我与集体无意识之间中介

**Core Points**:
- Anima is the feminine archetype in man
- It is inherited, primordial, fundamentally unconscious
- Not any specific woman but eternal feminine image
- Unconsciously projected onto beloved—explains passion
- Encountered after shadow in descent to unconscious
- Functions as psychopomp to collective depths

**Narrative Snippets**:
- `[ns_cw9i_014]` `[trigger: anima_definition]` `[factor_trigger: jung_anima]` `[role: 主干]` Every man carries with him the eternal image of woman—a definite feminine image that is fundamentally unconscious, inherited, primordial. → ¶52
- `[ns_cw9i_015]` `[trigger: anima_projection]` `[factor_trigger: jung_anima AND jung_projection]` `[role: 条件分支]` Since this image is unconscious, it is always projected upon the beloved—one of the chief reasons for passionate attraction or aversion. → ¶53
- `[ns_cw9i_016]` `[trigger: anima_after_shadow]` `[factor_trigger: jung_shadow AND jung_anima]` `[role: 主干依赖]` After the shadow comes the anima—she is the other, the complementary side. → ¶50

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The anima concept evolved significantly through Jung's career. This essay provides early formulation; later works (Aion, CW9ii) develop four-stage model (Eve→Helen→Mary→Sophia). Critics note gender essentialism; modern Jungians often reframe as "contrasexual" rather than biologically determined.
- **中文**: 阿尼玛概念在荣格职业生涯中显著演变。本文提供早期表述；后期作品（《永世》）发展四阶段模型（夏娃→海伦→玛利亚→索菲亚）。批评者注意性别本质主义；现代荣格学者常将其重新框架为"对立性别"而非生物决定。"""
    normalized_text_zh: str = """"""
    subject: str = "1 The Anima as Soul-Image (¶50-58)"
    factor_refs: list = ['engine_id', 'anima', 'psych_semantic', 'projection', 'psych_semantic', 'descent_sequence', 'psych_semantic', 'source_ref', 'rel_cw9i_011', 'jung_shadow', 'sequential', 'rel_cw9i_012', 'anima', 'externalizing', 'rel_cw9i_013', 'anima', 'connecting', 'evi_cw9i_009', 'anima', 'rule_anima_nature', 'evi_cw9i_010', 'rule_anima_proj', 'concept_anima', 'feminine_figure_dream', 'concept_projection', 'projection_dream']
    
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
        l1_anchor="acu_v1.0.0_1_the_anima_as_soul_image___50_001_L1",
    )
    version: str = "1.0.0"
