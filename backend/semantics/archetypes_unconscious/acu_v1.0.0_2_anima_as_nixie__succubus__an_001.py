"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515476
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
    semantic_id="acu_v1.0.0_2_anima_as_nixie__succubus__an_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2AnimaAsNixieSuccubusAn(SemanticEntry):
    """
    **Source Text** (¶53, 55-57, Lines 1014-1089):

> [53] The nixie is an even more instinctive version...
    """
    
    original_text: str = """**Source Text** (¶53, 55-57, Lines 1014-1089):

> [53] The nixie is an even more instinctive version of a magical feminine being whom I call the anima. She can also be a siren, melusina (mermaid), wood-nymph, Grace, or Erlking's daughter, or a lamia or succubus, who infatuates young men and sucks the life out of them...
>
> [55] But how do we dare to call this elfin being the "anima"? Anima means soul and should designate something very wonderful and immortal. Yet this was not always so. We should not forget that this kind of soul is a dogmatic conception whose purpose it is to pin down and capture something uncannily alive and active...
>
> [56] Being that has soul is living being. Soul is the living thing in man, that which lives of itself and causes life. Therefore God breathed into Adam a living breath, that he might live. With her cunning play of illusions the soul lures into life the inertness of matter that does not want to live...
>
> [57] The anima is not the soul in the dogmatic sense, not an anima rationalis, which is a philosophical conception, but a natural archetype that satisfactorily sums up all the statements of the unconscious, of the primitive mind, of the history of language and religion. It is a "factor" in the proper sense of the word. Man cannot make it; on the contrary, it is always the a priori element in his moods, reactions, impulses, and whatever else is spontaneous in psychic life.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Nixie/Melusina | Water spirit | Instinctive anima form | Dangerous feminine |
| Succubus | Night demon | Life-draining anima | Negative possession |
| Soul/Anima | Living breath | Life-giving principle | Etymology exploration |
| Natural archetype | Inborn pattern | Not dogmatic soul | Jung's definition |

**English Paraphrase (Primary Language)**:

Jung explores the **dark and light aspects of anima**:

**Anima's mythic forms**:
- Nixie, siren, melusina (mermaid), wood-nymph, Grace
- Lamia, succubus—"infatuates young men and sucks the life out of them"
- Witch who "mixes vile potions of love and death"
- These are not mere fantasies but ancient psychological realities

**Etymology of "anima"**:
- Latin anima = soul, but soul was not always "wonderful and immortal"
- Greek ψυχή (psyche) = butterfly, "quick-moving, changeful"
- Primitive: soul = magic breath, flame, living principle
- Soul is "living thing in man, that which lives of itself and causes life"

**Anima as natural archetype**:
- **NOT** anima rationalis (philosophical soul)
- A "natural archetype" summing up unconscious, primitive mind, language, religion
- A "factor"—man cannot make it; it is a priori
- The element in moods, reactions, impulses, spontaneous psychic life

**Complete Chinese Interpretation (Secondary Language)**:

荣格探索**阿尼玛的阴暗与光明面**：

**阿尼玛的神话形式**：
- 水精、海妖、美露辛（美人鱼）、树精、美惠女神
- 女妖、梦魔——"迷惑年轻男子并吸取他们的生命"
- 调制"爱情与死亡的恶毒药水"的女巫
- 这些不是纯粹幻想而是古老心理实相

**"阿尼玛"词源**：
- 拉丁语 anima = 灵魂，但灵魂并非总是"美妙不朽"
- 希腊语 ψυχή（psyche）= 蝴蝶，"快速移动、变幻多彩"
- 原始观：灵魂 = 魔力呼吸、火焰、生命原则
- 灵魂是"人内活物，自生自活并引发生命"

**阿尼玛作为自然原型**：
- **不是** anima rationalis（哲学灵魂）
- 一个"自然原型"总结无意识、原始心灵、语言、宗教
- 一个"因素"——人无法制造它；它是先验的
- 情绪、反应、冲动、自发心理生活中的元素

**Core Points**:
- Anima manifests as dangerous mythic figures (nixie, succubus, witch)
- Soul etymologically = breath, butterfly, living fire—not theological concept
- Anima as natural archetype, not philosophical soul (anima rationalis)
- It is an a priori "factor" that man cannot make
- Anima is the spontaneous element in all psychic life
- Life-giving but also potentially destructive (dual nature)

**Narrative Snippets**:
- `[ns_cw9i_017]` `[trigger: anima_dark_forms]` `[factor_trigger: jung_anima]` `[role: 条件分支]` The anima can be a siren, melusina, succubus, who infatuates young men and sucks the life out of them—or a witch mixing vile potions. → ¶53-54
- `[ns_cw9i_018]` `[trigger: soul_etymology]` `[factor_trigger: jung_soul]` `[role: 主干依赖]` Soul is the living thing in man, that which lives of itself and causes life—Greek psyche means butterfly, quick-moving, twinkling. → ¶55-56
- `[ns_cw9i_019]` `[trigger: anima_as_factor]` `[factor_trigger: jung_anima]` `[role: 主干]` The anima is a natural archetype, a "factor" that man cannot make—it is the a priori element in moods, reactions, and spontaneous psychic life. → ¶57"""
    normalized_text_zh: str = """"""
    subject: str = "2 Anima as Nixie, Succubus, and Soul (¶53-57)"
    factor_refs: list = ['engine_id', 'anima_dark', 'psych_semantic', 'anima_light', 'psych_semantic', 'apriori_factor', 'psych_semantic', 'source_ref', 'rel_cw9i_014', 'anima_dark', 'complementary', 'rel_cw9i_015', 'anima', 'defining', 'evi_cw9i_011', 'anima', 'rule_anima_factor', 'evi_cw9i_012', 'anima_dark', 'rule_anima_dark', 'concept_anima_dual', 'venus_benefic_vs_afflicted', 'anima_integration']
    
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
        l1_anchor="acu_v1.0.0_2_anima_as_nixie__succubus__an_001_L1",
    )
    version: str = "1.0.0"
