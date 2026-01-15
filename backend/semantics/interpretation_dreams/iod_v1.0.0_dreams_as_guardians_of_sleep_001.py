"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.465500
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
    semantic_id="iod_v1.0.0_dreams_as_guardians_of_sleep_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class DreamsAsGuardiansOfSleep(SemanticEntry):
    """
    **Source Text**:
"For days and nights a father had watched at the sick-bed of his child. After the c...
    """
    
    original_text: str = """**Source Text**:
"For days and nights a father had watched at the sick-bed of his child. After the child died, he retired to rest in an adjoining room, leaving the door ajar... After sleeping a few hours the father dreamed that the child stood near his bed clasping his arms and calling out reproachfully, 'Father, don't you see that I am burning?' The father woke and noticed a bright light coming from the adjoining room. Rushing in, he found the old man asleep, and the covers and one arm of the beloved body burned by the fallen candle."

"The dream triumphed over the conscious reflection because it could show the child once more alive. If the father had awakened first, and had then drawn the conclusion which led him into the adjoining room, he would have shortened the child's life by this one moment."

"It was for the sake of this wish-fulfilment that the father slept a moment longer."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Guardian of Sleep | Dream's function to preserve sleep | Core theoretical claim |
| Wish-Fulfilment | Dream fulfills wish (child alive again) | Even in tragedy |
| External Stimulus | Light/fire incorporated into dream | Dream absorbs disturbance |
| Moment Longer | Dream extends sleep duration | Protective function |
| Overdetermination | Multiple sources for dream content | "I am burning" = fever + fire |

**English Paraphrase (Primary Language)**:

The **Burning Child Dream** opens Chapter VII as the paradigmatic example of dreams' **guardian function**. A father, exhausted from watching his dying child, sleeps while a candle falls and begins burning the corpse. Rather than waking immediately, he **dreams** the child alive, saying "Father, don't you see that I am burning?"

This dream **incorporates** the external stimulus (the light of the fire) into its narrative while **fulfilling a wish** (the child alive, speaking). The father sleeps "a moment longer" because the dream provides what reality cannot—his child's continued life. Freud argues this demonstrates the dream's fundamental purpose: **preserving sleep** against disturbing stimuli.

The phrase "I am burning" is **overdetermined**: it incorporates the actual fire AND dream_recalls the child's fever during illness. The dream weaves multiple sources into a unified narrative that serves the wish.

Even this tragic dream follows the wish-fulfillment principle: the deepest wish (child alive) momentarily triumphs over reality's demands.

**Complete Chinese Interpretation (Secondary Language)**:

**燃烧的孩子之梦**作为第七章开篇，是梦的**守护功能**的典范例证。一位父亲因照看濒死的孩子而精疲力竭，在蜡烛倒下开始燃烧尸体时入睡。他没有立即醒来，而是**做梦**看到孩子活着，说"父亲，你没看到我在燃烧吗？"

这个梦**纳入**外部刺激（火光）到其叙事中，同时**满足愿望**（孩子活着，说话）。父亲"多睡了片刻"，因为梦提供了现实无法给予的——孩子的继续生存。弗洛伊德论证这展示了梦的根本目的：**保护睡眠**免受干扰刺激。

"我在燃烧"这个短语是**多重决定的**：它纳入了实际的火焰，也回响着孩子患病时的发烧。梦将多重来源编织成统一叙事，服务于愿望。

即使这个悲剧性的梦也遵循愿望满足原则：最深的愿望（孩子活着）暂时战胜了现实的要求。

**Core Points**:

- Dream as "guardian of sleep" against disturbance
- External stimulus (fire) incorporated into dream narrative
- Wish-fulfillment: child appears alive and speaking
- "Moment longer" = dream extends sleep duration
- Overdetermination: "burning" = fire + fever
- Even tragic dreams serve wish-fulfillment

**Detailed Explanation**:

This dream introduces the **guardian hypothesis**: dreams exist to **protect sleep**. When an external stimulus threatens to wake the sleeper, the dream incorporates it into a narrative that allows continued sleep. The bright light becomes the child's words about burning; the need to wake becomes part of the dream scenario.

The **wish-fulfillment** here is profound: not a trivial wish but the deepest—for the dead child to live. The dream grants this momentarily, and the father accepts it, sleeping on. Reality intrudes only when the dream narrative itself (the child's warning) leads to waking.

**Overdetermination** is elegantly demonstrated: "I am burning" carries multiple meanings simultaneously:
1. The actual fire visible through the door
2. The child's fever during final illness
3. Perhaps symbolic burning (intense emotion, love)

This opening example sets up Chapter VII's project: not just interpreting dreams, but understanding the **psychological apparatus** that makes dreaming possible. How can the mind produce such complex wish-fulfilling narratives while asleep?

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Guardian of sleep" (German: Hüter des Schlafes) emphasizes protective function. Later psychoanalysts debated whether all dreams serve this function.
- **中文**: "睡眠的守护者"（德语：Hüter des Schlafes）强调保护功能。后来的精神分析学者争论是否所有梦都服务于这一功能。这个案例也成为拉康关于"实在界"讨论的核心素材。

**Narrative Snippets**:

- `[ns_freud_psy_001]` `[trigger: guardian_of_sleep]` `[factor_trigger: guardian_of_sleep AND sleep]` `[role: 主干]` The dream triumphed over conscious reflection because it could show the child alive. For the sake of this wish-fulfilment the father slept a moment longer—dreams guard sleep. → Freud Ch.VII #Psychology
- `[ns_freud_psy_002]` `[trigger: stimulus_incorporation]` `[factor_trigger: stimulus_incorporation AND burning_child]` `[role: 主干依赖]` External stimulus (the fire's light) was incorporated into dream narrative—the child's words "I am burning" absorbed the disturbance while fulfilling a wish. → Freud Ch.VII #Psychology
- `[ns_freud_psy_003]` `[trigger: overdetermination_burning]` `[factor_trigger: sleep_extension AND wish_fulfillment]` `[role: 条件分支]` "I am burning" is overdetermined: it incorporates actual fire AND recalls child's fever—multiple sources woven into unified dream narrative. → Freud Ch.VII #Psychology
- `[ns_freud_psy_004]` `[trigger: hallucinatory_quality]` `[factor_trigger: hallucinatory_satisfaction AND visual_quality]` `[role: 总结]` Dreams produce hallucinatory revival of perceptual images—the child appears visually alive, satisfying the deepest wish. → Freud Ch.VII #Psychology"""
    normalized_text_zh: str = """"""
    subject: str = "Dreams as Guardians of Sleep"
    factor_refs: list = ['guardian_of_sleep', 'stimulus_incorporation', 'new_candidate', 'burning_child']
    
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_dreams_as_guardians_of_sleep_001_L1",
    )
    version: str = "1.0.0"
