"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568751
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
    semantic_id="acu_v1.0.0_3_anima_s_effects_and_life_sta_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3AnimaSEffectsAndLifeSta(SemanticEntry):
    """
    **Source Text** (¶144-147, Lines 2278-2315):

> [144] The anima is a factor of the utmost importance...
    """
    
    original_text: str = """**Source Text** (¶144-147, Lines 2278-2315):

> [144] The anima is a factor of the utmost importance in the psychology of a man wherever emotions and affects are at work. She intensifies, exaggerates, falsifies, and mythologizes all emotional relations with his work and with other people of both sexes. When the anima is strongly constellated, she softens the man's character and makes him touchy, irritable, moody, jealous, vain, and unadjusted.
>
> [146] Younger people, who have not yet reached the middle of life (around the age of 35), can bear even the total loss of the anima without injury. The important thing at this stage is for a man to be a man. The growing youth must be able to free himself from the anima fascination of his mother.
>
> [147] After the middle of life, however, permanent loss of the anima means a diminution of vitality, of flexibility, and of human kindness. The result, as a rule, is premature rigidity, crustiness, stereotypy, fanatical one-sidedness, obstinacy, pedantry, or else resignation, weariness, sloppiness... After middle life, therefore, the connection with the archetypal sphere of experience should if possible be re-established.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Anima constellated | Anima activated | Emotional takeover | Mood disturbance |
| Middle of life | ~35 years | Psychological turning point | Before/after differ |
| Vitality diminution | Loss of life force | Anima loss consequence | Post-midlife |
| Archetypal reconnection | Restoring access | Therapeutic goal | Midlife task |

**English Paraphrase (Primary Language)**:

**Anima's effects on men**:
Anima is of **utmost importance** wherever emotions are at work. She **intensifies, exaggerates, falsifies, and mythologizes** all emotional relations—with work and with people of both sexes. When strongly constellated, she makes a man **touchy, irritable, moody, jealous, vain, and unadjusted**—he spreads discontent all around.

**Before midlife (~35)**:
Young people can bear even **total loss of anima** without injury. At this stage, it's important for a man to **be a man**. Youth must free himself from **anima fascination of mother**. (Exceptions: artists; homosexuality = identity with anima, not pathology but incomplete detachment from hermaphroditic archetype.)

**After midlife**:
Permanent anima loss = **diminution of vitality, flexibility, human kindness**. Results: premature rigidity, crustiness, stereotypy, fanatical one-sidedness, obstinacy, pedantry—OR resignation, weariness, sloppiness, irresponsibility, childish ramollissement with tendency to alcohol. **Connection with archetypal sphere should be re-established**.

**Complete Chinese Interpretation (Secondary Language)**:

**阿尼玛对男性的影响**：
阿尼玛在情感起作用的地方**极为重要**。她**强化、夸大、歪曲和神话化**所有情感关系——与工作和两性的人。当强烈星座化时，她使男人**敏感、易怒、情绪化、嫉妒、虚荣、不适应**——他四处散布不满。

**中年之前（~35岁）**：
年轻人甚至能承受**阿尼玛的完全丧失**而不受伤害。这个阶段，重要的是男人**成为男人**。青年必须从**母亲的阿尼玛魅惑**中解放自己。（例外：艺术家；同性恋 = 与阿尼玛认同，不是病态而是从雌雄同体原型的不完全分离。）

**中年之后**：
永久的阿尼玛丧失 = **活力、灵活性、人情味的减少**。结果：过早僵化、刻薄、刻板、狂热片面、固执、学究气——或者辞职、疲倦、邋遢、不负责任、有酗酒倾向的幼稚软化。**应该重新建立与原型领域的联系**。

**Core Points**:
- Anima intensifies, exaggerates, mythologizes emotional relations
- Strongly constellated: touchy, moody, jealous, maladjusted
- Before 35: can bear anima loss; "be a man"
- Youth must free from mother's anima fascination
- Homosexuality = incomplete detachment from hermaphroditic archetype (not pathology)
- After midlife: anima loss = rigidity OR jung_sloppiness
- Must re-establish archetypal connection after midlife

**Narrative Snippets**:
- `[ns_cw9i_II_024]` `[trigger: anima_effects]` `[factor_trigger: jung_anima]` `[role: 主干]` The anima intensifies, exaggerates, falsifies, and mythologizes all emotional relations—when constellated, she makes a man touchy, moody, jealous, maladjusted. → ¶144
- `[ns_cw9i_II_025]` `[trigger: before_midlife]` `[factor_trigger: jung_development]` `[role: 条件分支]` Before midlife, a man can bear total anima loss—the important thing is for a man to be a man, freeing from mother's fascination. → ¶146
- `[ns_cw9i_II_026]` `[trigger: after_midlife]` `[factor_trigger: jung_development]` `[role: 条件分支]` After midlife, permanent anima loss means diminution of vitality, flexibility, human kindness—premature rigidity or resignation. → ¶147
- `[ns_cw9i_II_027]` `[trigger: reconnect_archetype]` `[factor_trigger: jung_therapy]` `[role: 总结]` After middle life, connection with the archetypal sphere of experience should if possible be re-established. → ¶147"""
    normalized_text_zh: str = """"""
    subject: str = "3 Anima's Effects and Life Stages (¶144-147)"
    factor_refs: list = ['engine_id', 'midlife', 'psych_semantic', 'anima_constellated', 'psych_semantic', 'archetype_reconnection', 'psych_semantic', 'source_ref', 'changes_at', 'midlife', 'transitioning', 'causes', 'rigidity', 'destructive', 'requires', 'archetype_reconnection', 'restorative', 'concept_midlife_turn', 'midlife_dream', 'concept_vitality_loss', 'saturn_affliction', 'anima_loss']
    
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
        l1_anchor="acu_v1.0.0_3_anima_s_effects_and_life_sta_001_L1",
    )
    version: str = "1.0.0"
