"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515494
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
    semantic_id="acu_v1.0.0_3_shadow_anima_sequence_and_an_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3ShadowAnimaSequenceAndAn(SemanticEntry):
    """
    **Source Text** (¶61-62, Lines 1133-1169):

> [61] If the encounter with the shadow is the "apprenti...
    """
    
    original_text: str = """**Source Text** (¶61-62, Lines 1133-1169):

> [61] If the encounter with the shadow is the "apprentice-piece" in the individual's development, then that with the anima is the "master-piece." The relation with the anima is again a test of courage, an ordeal by fire for the spiritual and moral forces of man. We should never forget that in dealing with the anima we are dealing with psychic facts which have never been in man's possession before, since they were always found "outside" his psychic territory, so to speak, in the form of projections. For the son, the anima is hidden in the dominating power of the mother, and sometimes she leaves him with a sentimental attachment that lasts throughout life and seriously impairs the fate of the adult...
>
> [62] In dealing with the shadow or anima it is not sufficient just to know about these concepts and to reflect on them. Nor can we ever experience their content by feeling our way into them or by appropriating other people's feelings. It is no use at all to learn a list of archetypes by heart. Archetypes are complexes of experience that come upon us like fate, and their effects are felt in our most personal life.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Apprentice-piece | First work | Shadow encounter | Initial test |
| Master-piece | Masterwork | Anima encounter | Advanced test |
| Ordeal by fire | Trial | Spiritual/moral test | Anima challenge |
| Complexes of experience | Fate-like patterns | Archetypes as lived | Not abstract |

**English Paraphrase (Primary Language)**:

Jung establishes the **developmental sequence** of individuation:

**Shadow vs Anima**:
- Shadow encounter = "apprentice-piece" (beginner's work)
- Anima encounter = "master-piece" (advanced mastery)
- Anima is "ordeal by fire for spiritual and moral forces"

**Why anima is harder**:
- Anima was never in man's possession—always projected outside
- For son: anima hidden in mother's dominating power
- Can leave "sentimental attachment that lasts throughout life"

**Critical warning**:
- Insufficient to just "know about" archetypes conceptually
- Cannot learn "a list of archetypes by heart"
- **Archetypes are complexes of experience that come upon us like fate**
- Effects felt in most personal life—not abstract knowledge

**Complete Chinese Interpretation (Secondary Language)**:

荣格建立个体化的**发展序列**：

**阴影vs阿尼玛**：
- 阴影相遇 = "学徒作品"（初学者作品）
- 阿尼玛相遇 = "杰作"（高级精通）
- 阿尼玛是"精神和道德力量的火之考验"

**为何阿尼玛更难**：
- 阿尼玛从未在男性所有中——总是投射在外
- 对儿子：阿尼玛隐藏在母亲的支配力量中
- 可能留下"持续一生的感伤依恋"

**关键警告**：
- 仅仅"知道"原型概念是不够的
- 不能"背诵原型列表"
- **原型是如命运般降临的经验复合体**
- 效果在最个人生活中感受——非抽象知识

**Core Points**:
- Shadow = apprentice-piece; Anima = master-piece in individuation
- Anima encounter is an "ordeal by fire"
- Anima was always projected (onto mother, beloved)
- Mother-complex can impair adult development
- Archetypes cannot be learned abstractly—they are lived experience
- Archetypes "come upon us like fate"

**Narrative Snippets**:
- `[ns_cw9i_020]` `[trigger: shadow_anima_sequence]` `[factor_trigger: jung_shadow AND jung_anima]` `[role: 主干]` Shadow encounter is the "apprentice-piece"; anima encounter is the "master-piece"—an ordeal by fire for spiritual and moral forces. → ¶61
- `[ns_cw9i_021]` `[trigger: archetypes_as_fate]` `[factor_trigger: jung_archetype]` `[role: 主干依赖]` Archetypes are complexes of experience that come upon us like fate—it is no use at all to learn a list of archetypes by heart. → ¶62
- `[ns_cw9i_022]` `[trigger: anima_in_mother]` `[factor_trigger: jung_anima AND jung_mother_complex]` `[role: 条件分支]` For the son, the anima is hidden in the dominating power of the mother—can leave sentimental attachment impairing adult fate. → ¶61"""
    normalized_text_zh: str = """"""
    subject: str = "3 Shadow-Anima Sequence and Anima as Master-Piece (¶61-62)"
    factor_refs: list = ['engine_id', 'individuation_sequence', 'psych_semantic', 'ordeal_fire', 'psych_semantic', 'anima_mother', 'psych_semantic', 'source_ref', 'rel_cw9i_016', 'jung_shadow', 'progressive', 'rel_cw9i_017', 'anima', 'concealing', 'evi_cw9i_013', 'rule_shadow_anima_seq', 'evi_cw9i_014', 'archetype', 'rule_archetype_experiential', 'concept_individuation_stages', 'progressions_transits', 'individuation']
    
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
        l1_anchor="acu_v1.0.0_3_shadow_anima_sequence_and_an_001_L1",
    )
    version: str = "1.0.0"
