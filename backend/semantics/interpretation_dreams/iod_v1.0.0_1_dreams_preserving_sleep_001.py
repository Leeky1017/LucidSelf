"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.473146
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
    semantic_id="iod_v1.0.0_1_dreams_preserving_sleep_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1DreamsPreservingSleep(SemanticEntry):
    """
    **Source Text**:
"Dreams which can only be understood as wish-fulfilments, and which express their m...
    """
    
    original_text: str = """**Source Text**:
"Dreams which can only be understood as wish-fulfilments, and which express their meaning undisguisedly, are to be found under the most varied conditions. These are the 'convenience' dreams, which constitute the answer of the dreamer to a stimulus which threatens to interrupt sleep."

"If I eat anchovies, olives or other strongly salted foods in the evening, I am thirsty during the night and therefore wake. But the waking is preceded by a dream with the same content: namely, I am drinking—I drink in long draughts, it tastes as delicious as only a cool drink can taste when one is parched—and then I wake, and find that I have a real desire to drink."

"A young colleague, who is a heavy sleeper, and who was called upon each morning to go to the hospital, was in the habit of prolonging his morning sleep. He related: 'My landlady calls me to go to the hospital. I then dream that I am in a bed in the hospital, and that a ticket is fastened on my head which reads: "Need not get up."'"

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Convenience Dreams | 便利梦 | Dreams serving sleep protection | Common type |
| Sleep-Preserving | 保护睡眠 | Dream satisfies need mentally | Avoids waking |
| Thirst Dream | 口渴梦 | Drinking in dream | Postpones waking |
| Hospital Dream | 医院梦 | "Need not get up" | Wish to sleep more |
| Stimulus | 刺激 | Threat to sleep | External or internal |

**English Paraphrase (Primary Language)**:

**Convenience dreams** are dreams that protect sleep by fulfilling wishes mentally rather than requiring physical action. They are **sleep's guardians**.

The thirst dream: Freud eats salty food, becomes thirsty, but instead of waking, dreams of drinking. The dream provides **hallucinatory satisfaction** that postpones waking. When the real need becomes too strong, he wakes—but the dream bought extra sleep.

The hospital dream: A young doctor must wake for work, but dreams he's already AT the hospital with a sign saying "Need not get up." The dream fulfills the wish to sleep more by **hallucinating the obstacle removed**.

These dreams show wish fulfillment serving a **biological function**: sleep preservation. The psyche would rather hallucinate satisfaction than interrupt restorative sleep. This is why:
- Thirst → dream of drinking
- Bladder pressure → dream of urinating
- Alarm clock → dream incorporating sound

**Complete Chinese Interpretation (Secondary Language)**:

**便利梦**是通过在心理上满足愿望而不需要身体行动来保护睡眠的梦。它们是**睡眠的守护者**。

口渴梦：弗洛伊德吃了咸食，变得口渴，但不是醒来，而是梦见喝水。梦提供**幻觉性满足**推迟醒来。当真正的需求变得太强时，他醒来——但梦争取了额外的睡眠。

医院梦：一个年轻医生必须醒来上班，但梦见自己已经在医院，有一个牌子写着"不需要起床"。梦通过**幻觉消除障碍**来满足继续睡眠的愿望。

这些梦展示了愿望满足服务于**生物功能**：睡眠保护。心灵宁愿幻觉满足也不愿中断恢复性睡眠。这就是为什么：
- 口渴 → 梦见喝水
- 膀胱压力 → 梦见排尿
- 闹钟 → 梦境纳入声音

**Narrative Snippets**:

- `[ns_freud_wish_007]` `[trigger: convenience_dreams]` `[factor_trigger: convenience_dreams AND dream_wishfulfillment]` `[role: 主干]` Convenience dreams are sleep's guardians—they fulfill wishes mentally to avoid waking. Thirst produces a dream of drinking; the need to work produces a dream of "need not get up." → Freud Ch.III #Convenience
- `[ns_freud_wish_008]` `[trigger: thirst_dream]` `[factor_trigger: dream_wishfulfillment AND dream_somatic AND hallucinatory_satisfaction]` `[role: 主干依赖]` After eating salty food, Freud dreams of drinking in long draughts—hallucinatory satisfaction postpones waking until real need becomes too strong. → Freud Ch.III #Convenience
- `[ns_freud_wish_009]` `[trigger: hospital_dream]` `[factor_trigger: dream_wishfulfillment AND dream_sleep]` `[role: 主干依赖]` Young doctor must wake for hospital—dreams he's already there with sign "Need not get up." Wish to sleep more fulfilled by hallucinating obstacle removed. → Freud Ch.III #Convenience
- `[ns_freud_wish_010]` `[trigger: sleep_guardian]` `[factor_trigger: dream_function AND dream_biology AND sleep_guardian]` `[role: 总结]` Dreams serve a biological function: sleep preservation. The psyche would rather hallucinate satisfaction than interrupt restorative sleep. → Freud Ch.III #Convenience"""
    normalized_text_zh: str = """"""
    subject: str = "1 Dreams Preserving Sleep"
    factor_refs: list = ['wish_fulfillment', 'children_dreams', 'convenience_dreams', 'sleep_guardian', 'hallucinatory_satisfaction']
    
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
        l1_anchor="iod_v1.0.0_1_dreams_preserving_sleep_001_L1",
    )
    version: str = "1.0.0"
