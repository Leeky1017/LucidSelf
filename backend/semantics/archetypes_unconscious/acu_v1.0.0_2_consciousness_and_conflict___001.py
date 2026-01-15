"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491616
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
    semantic_id="acu_v1.0.0_2_consciousness_and_conflict___001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2ConsciousnessAndConflict(SemanticEntry):
    """
    **Source Text** (¶177-179, Lines 2873-2908):

> [177] A woman of this type directs the burning ray o...
    """
    
    original_text: str = """**Source Text** (¶177-179, Lines 2873-2908):

> [177] A woman of this type directs the burning ray of her Eros upon a man whose life is stifled by maternal solicitude, and by doing so she arouses a moral conflict. Yet without this there can be no consciousness of personality... I believe that, after thousands and millions of years, someone had to realize that this wonderful world of mountains and oceans, suns and moons, galaxies and nebulae, plants and animals, exists... The entire world round me was still in its primeval state; it did not know that it was. And then, in that one moment in which I came to know, the world sprang into being.
>
> [178] There is no consciousness without discrimination of opposites. This is the paternal principle, the Logos, which eternally struggles to extricate itself from the primal warmth and primal darkness of the maternal womb; in a word, from unconsciousness. Divine curiosity yearns to be born and does not shrink from conflict, suffering, or sin. Unconsciousness is the primal sin, evil itself, for the Logos.
>
> [179] Conflict engenders fire, the fire of affects and emotions, and like every other fire it has two aspects, that of combustion and that of creating light... Emotion is the chief source of consciousness. There is no change from darkness to light or from inertia to movement without emotion.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Athi plains vision | African experience | Consciousness creates world | Jung's confession |
| Logos | Word/reason | Paternal principle | Discriminates opposites |
| Matricide | Killing mother | Liberation from unconscious | Spirit's first act |
| Emotion as fire | Affect creates light | Source of consciousness | Change requires it |

**English Paraphrase (Primary Language)**:

**Why consciousness matters**:
Moral conflict is necessary for consciousness of personality. Jung's confession of faith: after millions of years, **someone had to realize** this wonderful world exists. On the Athi plains of East Africa, watching wild herds in primeval stillness, he felt like the first man to know that **all this is**. "The world was still in its primeval state; it did not know that it was. And then, in that one moment in which I came to know, **the world sprang into being**." All Nature seeks this goal—fulfilled in the most conscious man.

**Logos vs Eros**:
There is no consciousness without **discrimination of opposites**. This is the **paternal principle, the Logos**—eternally struggling to extricate itself from the primal darkness of the maternal womb, from unconsciousness. Divine curiosity yearns to be born and **does not shrink from conflict, suffering, or sin**. For the Logos, **unconsciousness is the primal sin**, evil itself. Its first creative act of liberation is **matricide**—yet nothing can exist without its opposite.

**Emotion as source of consciousness**:
Conflict engenders **fire**—the fire of affects and emotions—with two aspects: combustion and creating light. Emotion is the **alchemical fire** that brings everything into existence and burns superfluities to ashes. **Emotion is the chief source of consciousness**. There is no change from darkness to light, from inertia to movement, without emotion.

**Complete Chinese Interpretation (Secondary Language)**:

**为何意识重要**：
道德冲突对于人格意识是必要的。荣格的信仰告白：数百万年后，**必须有人意识到**这个美妙的世界存在。在东非阿提平原上，观看在原初静默中的野生兽群，他感觉自己是第一个知道**这一切是**的人。"世界仍处于原初状态；它不知道它是。然后，在我认识到的那一刻，**世界跃入存在**。"所有自然都追求这个目标——在最有意识的人身上实现。

**逻各斯vs厄洛斯**：
没有**对立面的区分**就没有意识。这是**父性原则，逻各斯**——永恒地挣扎着从母性子宫的原初黑暗中解脱，从无意识中解脱。神圣的好奇心渴望诞生并**不畏惧冲突、苦难或罪**。对逻各斯而言，**无意识是原罪**，是邪恶本身。其第一个创造性解放行为是**弑母**——然而没有对立面就没有存在。

**情感作为意识之源**：
冲突产生**火**——情感和情绪之火——有两面：燃烧和创造光。情感是**炼金之火**，使一切存在并将多余烧成灰烬。**情感是意识的主要来源**。没有情感，就没有从黑暗到光明、从惯性到运动的转变。

**Core Points**:
- Moral conflict necessary for personality consciousness
- Jung's confession: someone had to realize the world exists
- "The world sprang into being" in that moment of knowing
- Consciousness requires discrimination of opposites (Logos)
- Logos struggles to escape maternal unconsciousness
- Unconsciousness = primal sin for Logos
- First creative act = matricide (liberation)
- Emotion = alchemical fire, chief source of consciousness
- No change from darkness to light without emotion

**Narrative Snippets**:
- `[ns_cw9i_III_021]` `[trigger: athi_vision]` `[factor_trigger: jung_consciousness]` `[role: 主干]` "The world was still in its primeval state; it did not know that it was. And then, in that one moment in which I came to know, the world sprang into being." → ¶177
- `[ns_cw9i_III_022]` `[trigger: logos_matricide]` `[factor_trigger: jung_logos]` `[role: 主干依赖]` The Logos eternally struggles to extricate itself from the maternal womb—unconsciousness is the primal sin; its first act of liberation is matricide. → ¶178
- `[ns_cw9i_III_023]` `[trigger: emotion_consciousness]` `[factor_trigger: jung_emotion]` `[role: 总结]` Emotion is the chief source of consciousness—there is no change from darkness to light without emotion. → ¶179"""
    normalized_text_zh: str = """"""
    subject: str = "2 Consciousness and Conflict (¶177-179)"
    factor_refs: list = ['engine_id', 'logos', 'psych_semantic', 'matricide_liberation', 'psych_semantic', 'emotion_fire', 'psych_semantic', 'source_ref', 'creates', 'world', 'creative', 'liberates_from', 'maternal_unconscious', 'separating', 'source_of', 'consciousness', 'generating', 'concept_logos', 'father_dream', 'concept_emotion_fire', 'fire_dream']
    
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
        l1_anchor="acu_v1.0.0_2_consciousness_and_conflict___001_L1",
    )
    version: str = "1.0.0"
