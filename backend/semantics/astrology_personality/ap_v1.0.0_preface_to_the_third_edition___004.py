"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237550
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
    semantic_id="ap_v1.0.0_preface_to_the_third_edition___004",
    book_id="astrology_personality",
    engine_id="astro"
)
class PrefaceToTheThirdEdition(SemanticEntry):
    """
    **Source Text** (Lines 222-267):
> Because I do not believe that this type of astrology is what we n...
    """
    
    original_text: str = """**Source Text** (Lines 222-267):
> Because I do not believe that this type of astrology is what we need today, I have recently formed an International Committee of Humanistic Astrology (I.C.H.A.) which intends to link people who are interested in a different approach to astrology, a person-oriented approach. It is a "humanistic" approach, not in the sense of a traditional humanism often associated with atheism, but rather in accordance with the meaning given to the word by Abraham Maslow, founder of what is known as Humanistic psychology. This type of psychology is neither Freudian, nor Behavioristic or Clinical. For this reason it is also called Third Force psychology. It seeks to help and guide individuals regarded as developing, aspiring, self-actualizing persons who at times may reach moments of exalted spiritual consciousness in "peak-experiences."
>
> In a similar sense what I conceive as Humanistic astrology is an astrology which assists individuals in the solution of their personal and interpersonal problems, and especially in actualizing more fully their birth-potential. In this type of astrology, no planet and no aspect is in itself "good" or "bad." Every birth-chart is as "good" as any other, in the sense that it symbolizes what the person potentially is and what he is meant to achieve, if he follows the "instructions" which, as it were, are "coded" in the pattern of the sky, as seen from the place and at the exact moment of birth.
>
> Such an astrology is not an empirical science. It is a "language" which can reveal the archetype of what the total person (body, mind, feelings, etc.) essentially is—the "Form" of his or her individuality. What we vaguely and confusingly call "destiny" is simply the process of actualization of the potentialities abstractly formulated in the birth-chart.

**Key Term Analysis**:
- **I.C.H.A.**: `International Committee of Humanistic Astrology` / `1969 founding` / `Rudhyar's organization`
- **Humanistic psychology**: `Maslow's Third Force` / `self-actualization focus` / `neither Freudian nor Behaviorist`
- **Peak-experiences**: `Maslow concept` / `moments of spiritual consciousness` / `transcendent states`
- **Birth-potential**: `chart as seed-pattern` / `what person is meant to become` / `actualization goal`
- **No good or bad planets**: `beyond moral judgment` / `all factors serve wholeness` / `humanistic principle`
- **Coded instructions**: `chart as blueprint` / `sky-pattern at birth` / `guidance for actualization`

**English Paraphrase (Primary Language)**:
Rudhyar announces his founding of the International Committee of Humanistic Astrology (I.C.H.A.) in 1969, establishing humanistic astrology as a distinct movement. He explicitly aligns his approach with Abraham Maslow's Humanistic psychology—the "Third Force" that transcends both Freudian psychoanalysis and Behaviorism. Maslow's psychology focuses on self-actualization, growth, and peak-experiences rather than pathology or conditioning.

Applied to astrology, this means: (1) No planet or aspect is inherently good or bad—all serve the person's wholeness; (2) Every birth chart is equally valuable as a unique pattern of potential; (3) The chart contains "coded instructions" for self-actualization; (4) Astrology is not empirical science but a symbolic language revealing the "Form" of individuality; (5) Destiny is not fixed fate but the process of actualizing birth-potentials.

This represents Rudhyar's definitive break from fortune-telling astrology. The chart doesn't predict what will happen but reveals what the person can become through conscious effort.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar宣布他在1969年创立国际人本占星学委员会(I.C.H.A.)，将人本占星学确立为一个独特的运动。他明确将其方法与Abraham Maslow的人本心理学——超越弗洛伊德精神分析和行为主义的"第三势力"——相结合。Maslow的心理学关注自我实现、成长和高峰体验，而非病理或条件反射。

应用于占星学，这意味着：(1)没有行星或相位本身是好或坏的——所有因素服务于人的完整性；(2)每个出生星盘作为独特的潜能模式都同等有价值；(3)星盘包含自我实现的"编码指令"；(4)占星学不是经验科学而是揭示个体性"形式"的符号语言；(5)命运不是固定的宿命而是实现出生潜能的过程。

这代表了Rudhyar与算命占星术的彻底决裂。星盘不预测将发生什么，而是揭示人通过有意识努力可以成为什么。

**Core Points**:
- I.C.H.A. founded 1969 to promote humanistic astrology
- Alignment with Maslow's Third Force psychology
- Self-actualization and peak-experiences as goals
- No planet or aspect inherently good or bad
- Every chart equally valuable as unique potential-pattern
- Chart contains "coded instructions" for self-actualization
- Astrology as symbolic language, not empirical science
- Destiny = actualization process, not fixed fate
- Total person (body, mind, feelings) represented in chart

**Detailed Explanation**:
This passage establishes the philosophical foundation of humanistic astrology. By linking to Maslow, Rudhyar positions his approach within a respected psychological movement, distancing it from both occultism and fortune-telling. The key innovation is the removal of moral judgment from astrological symbolism: Saturn is not "bad," Venus is not "good"—all planets represent necessary functions within the personality's organic whole.

The concept of "coded instructions" transforms the astrologer's role: not a predictor of fate but a translator of potential, helping the client understand how to work with their unique pattern toward self-fulfillment. This is truly revolutionary—it makes the client the agent of their own destiny while the chart serves as a map of possibilities.

**Narrative Snippets**:
- `[ns_aop_011]` `[trigger: icha_founding]` `[factor_trigger: psych_third_force AND astro_humanistic_movement]` `[role: 主干]` Rudhyar founded I.C.H.A. in 1969 to promote a person-oriented approach aligned with Maslow's Humanistic psychology. → Source Text L222-232
- `[ns_aop_012]` `[trigger: no_good_bad]` `[factor_trigger: astro_non_judgmental AND astro_good_bad_judgment AND astro_chart_indiv AND astro_non_judgmental_interp]` `[role: 主干依赖]` In humanistic astrology, no planet and no aspect is in itself "good" or "bad"—every chart symbolizes unique potential. → Source Text L236-238
- `[ns_aop_013]` `[trigger: coded_instructions]` `[factor_trigger: astro_chart AND astro_coded_instructions AND astro_chart_code AND psych_self_actual_goal]` `[role: 条件分支]` The birth chart contains "coded instructions" for what the person is meant to achieve—a blueprint for self-actualization. → Source Text L238-242
- `[ns_aop_014]` `[trigger: symbolic_language]` `[factor_trigger: astro_symbolic_not_empirical]` `[role: 总结]` Astrology is not empirical science but a symbolic language revealing the "Form" of individuality. → Source Text L244-246

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's humanistic framework became foundational for late 20th-century psychological astrology. Liz Greene, Howard Sasportas, and others built on this foundation while adding Jungian depth.
- **中文**: Rudhyar的人本框架成为20世纪后期心理占星学的基础。Liz Greene、Howard Sasportas等人在此基础上增加了荣格深度心理学的内容。"""
    normalized_text_zh: str = """"""
    subject: str = "Preface to the Third Edition: Person-Centered Approach and Humanistic Astrology"
    factor_refs: list = ['astro_icha', 'psych_third_force', 'psych_peak_experience', 'astro_coded_instructions', 'astro_non_judgmental']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_preface_to_the_third_edition___004_L1",
    )
    version: str = "1.0.0"
