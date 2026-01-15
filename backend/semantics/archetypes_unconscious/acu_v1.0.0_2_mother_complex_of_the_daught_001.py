"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491576
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
    semantic_id="acu_v1.0.0_2_mother_complex_of_the_daught_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2MotherComplexOfTheDaught(SemanticEntry):
    """
    **Source Text** (¶167-170, Lines 2657-2747):

> [167] (a) Hypertrophy of the Maternal Element.—The e...
    """
    
    original_text: str = """**Source Text** (¶167-170, Lines 2657-2747):

> [167] (a) Hypertrophy of the Maternal Element.—The exaggeration of the feminine side means an intensification of all female instincts, above all the maternal instinct. The negative aspect is seen in the woman whose only goal is childbirth. To her the husband is obviously of secondary importance... Even her own personality is of secondary importance; she often remains entirely unconscious of it... She is content to cling to her mother in selfless devotion...
>
> [168] (b) Overdevelopment of Eros.—Quite the contrary, this instinct may be wiped out altogether. As a substitute, an overdeveloped Eros results, and this almost invariably leads to an unconscious incestuous relationship with the father. The intensified Eros places an abnormal emphasis on the personality of others. Jealousy of the mother and the desire to outdo her become the leitmotifs...
>
> [169] (c) Identity with the Mother.—If a mother-complex in a woman does not produce an overdeveloped Eros, it leads to identification with the mother and to paralysis of the daughter's feminine initiative. A complete projection of her personality on to the mother then takes place... The daughter leads a shadow-existence, often visibly sucked dry by her mother...
>
> [170] (d) Resistance to the Mother.—The motto of this type is: Anything, so long as it is not like Mother! On one hand we have a fascination which never reaches the point of identification; on the other, an intensification of Eros which exhausts itself in jealous resistance. This kind of daughter knows what she does not want, but is usually completely at sea as to what she would choose as her own fate.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Hypertrophy | Overgrowth | Excessive maternal | Type (a) |
| Overdeveloped Eros | Excessive relatedness | Father-bound | Type (b) |
| Identity with mother | Fusion | Paralysis | Type (c) |
| Resistance | Opposition | Counter-identification | Type (d) |

**English Paraphrase (Primary Language)**:

Jung identifies **four types of daughter's mother-complex**:

**(a) Hypertrophy of Maternal Element**:
- Intensification of all female instincts, especially maternal
- Husband is secondary; childbirth is only goal
- Own personality unconscious—lives through others
- Like Demeter: possessive, will to power masked as devotion

**(b) Overdevelopment of Eros**:
- Maternal instinct wiped out; replaced by intense Eros
- Leads to unconscious incestuous relationship with father
- Jealousy of mother; desire to outdo her
- Attracted to married men to wreck marriages
- Remarkable unconsciousness of own actions

**(c) Identity with Mother**:
- Complete projection of personality onto mother
- Paralysis of feminine initiative
- "Shadow-existence, sucked dry by mother"
- Yet attractive to men (empty vessel for projections)
- Like Persephone abducted from Demeter

**(d) Resistance to Mother**:
- Motto: "Anything, so long as it is not like Mother!"
- Fascination but never identification
- Eros exhausted in jealous resistance
- Knows what she doesn't want; no idea of own fate
- Negative mother-complex par excellence

**Complete Chinese Interpretation (Secondary Language)**:

荣格识别**女儿母亲情结的四种类型**：

**(a) 母性元素肥大**：
- 所有女性本能强化，尤其是母性
- 丈夫次要；生育是唯一目标
- 自己人格无意识——通过他人生活
- 如德墨忒尔：占有欲、权力意志伪装为奉献

**(b) 厄洛斯过度发展**：
- 母性本能被消除；被强烈厄洛斯取代
- 导致与父亲的无意识乱伦关系
- 嫉妒母亲；渴望胜过她
- 被已婚男人吸引以破坏婚姻
- 对自己行为显著无意识

**(c) 与母亲认同**：
- 人格完全投射到母亲身上
- 女性主动性瘫痪
- "影子存在，被母亲吸干"
- 却对男人有吸引力（投射的空容器）
- 如珀尔塞福涅被从德墨忒尔那里劫走

**(d) 对母亲的抵抗**：
- 座右铭："只要不像母亲就行！"
- 着迷但从不认同
- 厄洛斯在嫉妒抵抗中耗尽
- 知道不想要什么；不知道自己命运
- 典型的负面母亲情结

**Core Points**:
- Type (a): Maternal hypertrophy—lives through children, possessive
- Type (b): Overdeveloped Eros—father-bound, marriage-wrecking
- Type (c): Mother identification—shadow existence, paralyzed
- Type (d): Mother resistance—knows only what she doesn't want
- All four types represent different distortions of feminine development
- Demeter-Persephone myth underlies daughter psychology

**Narrative Snippets**:
- `[ns_cw9i_III_014]` `[trigger: daughter_type_a]` `[factor_trigger: jung_mother_complex]` `[role: 条件分支]` Type (a) Maternal hypertrophy: intensification of all female instincts, husband secondary, lives through children, unconscious will to power. → ¶167
- `[ns_cw9i_III_015]` `[trigger: daughter_type_b]` `[factor_trigger: jung_mother_complex AND jung_eros]` `[role: 条件分支]` Type (b) Overdeveloped Eros: maternal instinct wiped out, unconscious incestuous relation with father, attracted to married men. → ¶168
- `[ns_cw9i_III_016]` `[trigger: daughter_type_c]` `[factor_trigger: jung_mother_complex AND jung_shadow]` `[role: 条件分支]` Type (c) Identity with mother: shadow-existence, sucked dry by mother, paralysis of feminine initiative, attractive as empty vessel. → ¶169
- `[ns_cw9i_III_017]` `[trigger: daughter_type_d]` `[factor_trigger: jung_mother_complex]` `[role: 条件分支]` Type (d) Resistance: "Anything so long as it is not like Mother!"—knows what she doesn't want but not her own fate. → ¶170"""
    normalized_text_zh: str = """"""
    subject: str = "2 Mother-Complex of the Daughter: Four Types (¶167-170)"
    factor_refs: list = ['engine_id', 'daughter_type_a', 'psych_semantic', 'daughter_type_b', 'psych_semantic', 'daughter_type_c', 'psych_semantic', 'daughter_type_d', 'psych_semantic', 'source_ref', 'variation', 'mother_complex', 'expressing', 'variation', 'mother_complex', 'expressing', 'variation', 'mother_complex', 'expressing', 'variation', 'mother_complex', 'expressing', 'concept_daughter_mothercomplex', 'mother_daughter_dream']
    
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
        l1_anchor="acu_v1.0.0_2_mother_complex_of_the_daught_001_L1",
    )
    version: str = "1.0.0"
