"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515410
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
    semantic_id="acu_v1.0.0_6_water_as_symbol_of_the_uncon_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 6WaterAsSymbolOfTheUncon(SemanticEntry):
    """
    **Source Text** (¶40, 45-46, Lines 818-921):

> [40] Water is the commonest symbol for the unconscio...
    """
    
    original_text: str = """**Source Text** (¶40, 45-46, Lines 818-921):

> [40] Water is the commonest symbol for the unconscious. The lake in the valley is the unconscious, which lies, as it were, underneath consciousness, so that it is often referred to as the "subconscious," usually with the pejorative connotation of an inferior consciousness. Water is the "valley spirit," the water dragon of Tao, whose nature resembles water—a yang embraced in the yin. Psychologically, therefore, water means spirit that has become unconscious.
>
> [45] The necessary and needful reaction from the collective unconscious expresses itself in archetypally formed ideas. The meeting with oneself is, at first, the meeting with one's own shadow. The shadow is a tight passage, a narrow door, whose painful constriction no one is spared who goes down to the deep well. But one must learn to know oneself in order to know who one is. For what comes after the door is, surprisingly enough, a boundless expanse full of unprecedented uncertainty, with apparently no inside and no outside, no above and no below, no here and no there, no mine and no thine, no good and no bad. It is the world of water, where all life floats in suspension...
>
> [46] No, the collective unconscious is anything but an incapsulated personal system; it is sheer objectivity, as wide as the world and open to all the world. There I am the object of every subject, in complete reversal of my ordinary consciousness, where I am always the subject that has an object. There I am utterly one with the world, so much a part of it that I forget all too easily who I really am. "Lost in oneself" is a good way of describing this state. But this self is the world, if only a consciousness could see it. That is why we must know who we are.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Water | Physical element | Symbol of unconscious | Universal dream symbol |
| Valley spirit | Taoist concept | Yin receptivity | Water's nature |
| Shadow | Dark side | Personal unconscious content | First encounter |
| Sheer objectivity | Pure objectness | Transpersonal nature of CU | Not personal |

**English Paraphrase (Primary Language)**:

Jung establishes **water as the primary symbol of the unconscious**:

**Water symbolism**:
- Water = unconscious (lying beneath consciousness like valley beneath mountain)
- "Valley spirit" (Tao Te Ching) = water dragon = yang embraced in yin
- Psychologically: water = **spirit that has become unconscious**

**Shadow as gateway**:
- Meeting with self = first meeting with shadow
- Shadow = "tight passage, narrow door"—painful but necessary
- Beyond shadow: boundless expanse, no distinctions (inside/outside, above/below, mine/thine)

**Collective unconscious nature**:
- **NOT** an incapsulated personal system
- "Sheer objectivity, as wide as the world and open to all the world"
- Reversal: ego becomes object of every subject
- Danger: "Lost in oneself"—forgetting individual identity
- **Must know who we are** to safely navigate collective depths

**Complete Chinese Interpretation (Secondary Language)**:

荣格确立**水作为无意识的首要象征**：

**水的象征意义**：
- 水 = 无意识（位于意识之下如山谷位于山下）
- "谷神"（道德经）= 水龙 = 阳被阴包容
- 心理学上：水 = **变成无意识的精神**

**阴影作为门户**：
- 与自我相遇 = 首先与阴影相遇
- 阴影 = "紧窄通道，窄门"——痛苦但必要
- 阴影之外：无边无际，无分别（内/外、上/下、我的/你的）

**集体无意识的性质**：
- **不是**封闭的个人系统
- "纯粹客观性，如世界般广阔，对所有世界开放"
- 逆转：自我成为每个主体的客体
- 危险："迷失在自我中"——遗忘个体身份
- **必须知道我们是谁**才能安全导航集体深处

**Core Points**:
- Water is the commonest symbol for the unconscious
- Water = spirit that has become unconscious (Taoist connection)
- Shadow is the first encounter in descent to unconscious
- Beyond shadow lies boundless expanse without distinctions
- Collective unconscious = sheer objectivity, not personal encapsulation
- In CU, ego becomes object rather than subject
- Danger of losing individual identity in collective depths
- Self-knowledge essential for safe navigation

**Narrative Snippets**:
- `[ns_cw9i_010]` `[trigger: water_symbol]` `[factor_trigger: jung_water_symbolism]` `[role: 主干]` Water is the commonest symbol for the unconscious—psychologically, water means spirit that has become unconscious. → ¶40
- `[ns_cw9i_011]` `[trigger: shadow_encounter]` `[factor_trigger: jung_shadow]` `[role: 条件分支]` The shadow is a tight passage, a narrow door, whose painful constriction no one is spared who goes down to the deep well. → ¶45
- `[ns_cw9i_012]` `[trigger: cu_objectivity]` `[factor_trigger: jung_collective_unconscious]` `[role: 主干依赖]` The collective unconscious is sheer objectivity, as wide as the world—there I am the object of every subject. → ¶46
- `[ns_cw9i_013]` `[trigger: identity_danger]` `[factor_trigger: jung_ego AND jung_collective_unconscious]` `[role: 例外处理]` "Lost in oneself"—I forget who I really am. That is why we must know who we are. → ¶46

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Jung's integration of Taoist concepts ("valley spirit") demonstrates his cross-cultural synthesis. The shadow concept here is briefly introduced; fuller treatment appears in later essays and Aion. The warning about losing oneself anticipates his concept of "inflation."
- **中文**: 荣格对道家概念（"谷神"）的整合展示了他的跨文化综合。阴影概念在此简略介绍；更完整论述出现在后来论文和《永世》中。关于迷失自我的警告预示了他的"膨胀"概念。"""
    normalized_text_zh: str = """"""
    subject: str = "6 Water as Symbol of the Unconscious (¶40-46)"
    factor_refs: list = ['shadow', 'valley_spirit', 'water_symbol', 'engine_id', 'water_symbol', 'psych_semantic', 'shadow', 'psych_semantic', 'cu_objectivity', 'psych_semantic', 'source_ref', 'rel_cw9i_008', 'jung_water_symbolism', 'representing', 'rel_cw9i_009', 'jung_shadow', 'transitional', 'rel_cw9i_010', 'cu_objectivity', 'defining', 'evi_cw9i_007', 'water_symbol', 'rule_water_unc', 'evi_cw9i_008', 'collective_unconscious', 'rule_cu_objective', 'concept_water_unconscious', 'water_dream', 'concept_shadow', 'shadow_figure']
    
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
        l1_anchor="acu_v1.0.0_6_water_as_symbol_of_the_uncon_001_L1",
    )
    version: str = "1.0.0"
