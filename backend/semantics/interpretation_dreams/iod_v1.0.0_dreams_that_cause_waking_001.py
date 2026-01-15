"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.465566
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
    semantic_id="iod_v1.0.0_dreams_that_cause_waking_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class DreamsThatCauseWaking(SemanticEntry):
    """
    **Source Text**:
"We know that the waking activity leaves day remnants from which the sum of energy ...
    """
    
    original_text: str = """**Source Text**:
"We know that the waking activity leaves day remnants from which the sum of energy cannot be entirely removed; or the waking activity revives during the day one of the unconscious wishes... The unconscious wish has already made its way to the day remnants, either during the day or at any rate with the beginning of sleep, and has effected a transference to it."

"The dream process takes the regressive course, which has just been opened by the peculiarity of the sleeping state... On its way to regression the dream takes on the form of dramatisation."

"The dream invariably awakens us, that is, it puts into activity a part of the dormant force of the Foreconscious. This force imparts to the dream that influence which we have designated as secondary elaboration."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Anxiety Dream | Dream that causes waking through distress | Apparent exception to wish-fulfillment |
| Dream as Awakener | All dreams partially arouse consciousness | Universal property |
| Failed Guardian | When dream fails to preserve sleep | Anxiety dream mechanism |
| Transference to Day Remnants | Unconscious wish attaches to recent material | Dream formation step |
| Dramatisation | Thought takes on scenic form during regression | Dream characteristic |

**English Paraphrase (Primary Language)**:

Section (d) addresses the **anxiety dream problem**—dreams that cause waking rather than preserving sleep. If dreams are wish-fulfillments guarding sleep, why do nightmares exist?

Freud's answer involves the **guardian failure**: All dreams "invariably awaken us" to some degree—they activate a portion of the dormant foreconscious. The difference is quantitative: successful dreams arouse just enough consciousness for secondary elaboration without waking; anxiety dreams arouse **too much**, triggering full awakening.

The mechanism: An unconscious wish transfers to day remnants, undergoes censorship distortion, and regresses to hallucinatory form. If the wish is **too threatening** despite distortion, the anxiety signal overwhelms the dream's protective function. The dreamer wakes in self-defense.

Anxiety dreams thus **confirm** rather than refute wish-fulfillment: the wish is present but so disturbing that even its disguised expression triggers alarm. The censor says "no" not by blocking the dream but by ending sleep.

**Complete Chinese Interpretation (Secondary Language)**:

(d)部分探讨**焦虑梦问题**——导致觉醒而非保护睡眠的梦。如果梦是守护睡眠的愿望满足，为什么噩梦存在？

弗洛伊德的答案涉及**守护失败**：所有梦在某种程度上"必然唤醒我们"——它们激活休眠前意识的一部分。差异是量的问题：成功的梦只唤起足够润饰的意识而不导致觉醒；焦虑梦唤起**太多**，触发完全觉醒。

机制：一个无意识愿望转移到日间残余，经历审查歪曲，退行到幻觉形式。如果愿望尽管经过伪装仍然**过于威胁**，焦虑信号就会压倒梦的保护功能。梦者出于自我防卫而醒来。

焦虑梦因此**确认**而非反驳愿望满足：愿望存在，但如此令人不安，以至于即使其伪装表达也触发警报。审查者不是通过阻止梦而是通过结束睡眠来说"不"。

**Core Points**:

- Anxiety dreams = guardian function failure
- All dreams arouse consciousness partially
- Difference is quantitative: how much arousal
- Anxiety = wish too threatening despite distortion
- Censor ends sleep rather than blocks dream
- Anxiety dreams confirm, not refute, wish-fulfillment
- Waking = last-resort defense against disturbing wish

**Detailed Explanation**:

The anxiety dream presents the **crucial test case** for wish-fulfillment theory. If nightmares exist, isn't the theory falsified?

Freud's solution is elegant: anxiety dreams are **failed** wish-fulfillments. The wish is present; the dream attempts to fulfill it; but the material is so disturbing that even disguised expression triggers the **anxiety signal**. This signal, a function of the ego, overrides the wish-to-sleep and forces waking.

Consider the mechanism: A forbidden wish (say, incestuous or murderous) transfers to innocent day residue, undergoes maximum distortion, regresses to imagery. But the dreamer's internal censor recognizes the danger **despite** disguise. Rather than letting the wish achieve even hallucinatory satisfaction, the censor **aborts** the dream by triggering waking.

This explains why **anxiety often appears at dream's end**: the dream nearly succeeded in fulfilling the wish; anxiety is the last-moment intervention. The dreamer wakes with fear, not because the dream threatened them from outside, but because it threatened to gratify a forbidden wish from inside.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Anxiety dream" (German: Angsttraum) is distinct from mere "bad dream." Anxiety (Angst) has technical meaning in psychoanalysis—signal of internal danger.
- **中文**: "焦虑梦"（德语：Angsttraum）不同于普通"噩梦"。焦虑（Angst）在精神分析中有技术含义——内部危险的信号。弗洛伊德后来发展出更系统的焦虑理论。

**Narrative Snippets**:

- `[ns_freud_psy_010]` `[trigger: anxiety_dream]` `[factor_trigger: dream_anxiety_dream]` `[role: 主干]` Anxiety dreams represent guardian function failure—the wish is too threatening despite distortion, triggering waking as last-resort defense. → Freud Ch.VII #AnxietyDream
- `[ns_freud_psy_011]` `[trigger: dream_awakens]` `[factor_trigger: dream_guardian_of_sleep]` `[role: 主干依赖]` The dream invariably awakens us—it puts into activity part of the dormant foreconscious. The question is how much arousal before waking occurs. → Freud Ch.VII #AnxietyDream
- `[ns_freud_psy_012]` `[trigger: anxiety_confirms_wish]` `[factor_trigger: dream_anxiety_dream AND dream_wish_fulfillment]` `[role: 条件分支]` Anxiety dreams confirm wish-fulfillment: the forbidden wish is present but so disturbing that even disguised expression triggers alarm and ends sleep. → Freud Ch.VII #AnxietyDream"""
    normalized_text_zh: str = """"""
    subject: str = "Dreams That Cause Waking"
    factor_refs: list = ['anxiety_dream', 'failed_guardian', 'anxiety_signal', 'dream_abortion']
    
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
        l1_anchor="iod_v1.0.0_dreams_that_cause_waking_001_L1",
    )
    version: str = "1.0.0"
