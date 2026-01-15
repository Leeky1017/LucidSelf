"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237822
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
    semantic_id="ap_v1.0.0_entry_10__positive_vs_negative_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry10PositiveVsNegative(SemanticEntry):
    """
    **Source Text** (Lines 2545-2676):
> Positive and Negative Time... There are two fundamental concept...
    """
    
    original_text: str = """**Source Text** (Lines 2545-2676):
> Positive and Negative Time... There are two fundamental conceptions of time possible: Negative time is time conceived as the fatality of cessation. Positive time, or holistic time, is the power of whole-making.
>
> The first view is subjective and emotional. It says: "Here I am, whole, alive, conscious; and it is all going to end! Each change is a step toward death, and thus all is suffering and all in vain." Thus speaks the individual, who has seen that individual selfhood is a mirage. "All compound entities decay," said the Buddha...
>
> The positive conception of time sees time as the eternal birthing of wholes which do not necessarily die as such but may keep combining with each other, forming in the process ever greater wholes...
>
> Man should live fully every moment, and first of all his fundamental birth-moment and his entire Destiny. As he ceases resisting time, but on the contrary accepts the creative message of every moment, every moment is seen as a birth. Man, as he lives creatively, lives in a constant process of whole-making.

**Key Term Analysis**:
- **Negative time**: `fatality of cessation` / `death-orientation` / `emotional, subjective` / `"all is suffering"`
- **Positive time**: `power of whole-making` / `eternal birthing` / `creative` / `ever greater wholes`
- **Living fully**: `accept creative message` / `every moment = birth` / `constant whole-making`
- **Destiny fulfillment**: `not resisting time` / `fulfill space/form of moment` / `renew wholeness`

**English Paraphrase (Primary Language)**:
Rudhyar contrasts two conceptions of time. Negative time = "fatality of cessation"—subjective, emotional, death-focused ("all is suffering"). This produces fear, greed, imperialism—trying to preserve space-structure against time's erosion.

Positive time = "power of whole-making"—time eternally births wholes that combine into greater wholes. Man should "live fully every moment," accepting its creative message. Every moment becomes a birth; creative living = constant whole-making.

The practical implication: "Man... ceases resisting time... accepts the creative message of every moment." He fulfills the form determined by each moment's potency, constantly renewing wholeness. Death is not end but transformation—when one space-structure ends, myriads are born elsewhere.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar对比了两种时间观念。负面时间="终止的宿命"——主观、情感、以死亡为焦点（"一切皆苦"）。这产生恐惧、贪婪、帝国主义——试图保护空间结构对抗时间的侵蚀。

正面时间="整体创造的力量"——时间永恒地诞生整体，它们组合成更大的整体。人应该"充分活在每一刻"，接受其创造性信息。每一刻都成为诞生；创造性生活=持续的整体创造。

实践含义："人……停止抵抗时间……接受每一刻的创造性信息。"他实现每一刻潜能所决定的形式，不断更新整体性。死亡不是终结而是转化——当一个空间结构结束时，无数结构在别处诞生。

**Core Points**:
- Negative time = fatality of cessation, death-oriented
- Produces fear, greed, preservation attempts
- Positive time = whole-making power, eternal birthing
- Wholes combine into ever greater wholes
- Live fully every moment—accept creative message
- Every moment = birth; creative life = constant whole-making
- Stop resisting time; fulfill moment's form
- Death = transformation, not end

**Narrative Snippets**:
- `[ns_aop_093]` `[trigger: negative_time]` `[factor_trigger: negative_time AND astro_chronos_state AND astro_time_polarity]` `[role: 主干]` Negative time = fatality of cessation—subjective, emotional, "all is suffering and in vain." → L2633-2643
- `[ns_aop_094]` `[trigger: positive_time]` `[factor_trigger: positive_time AND astro_cyclology_func AND astro_cyclic_struct AND astro_time_qual AND astro_time_rooted AND astro_time_whole_struct AND astro_whole_power]` `[role: 主干依赖]` Positive time = eternal birthing of wholes combining into ever greater wholes. → L2647-2655
- `[ns_aop_095]` `[trigger: live_fully]` `[factor_trigger: moment_acceptance AND whole_making AND astro_moment_accept]` `[role: 条件分支]` Live fully every moment—accept creative message, every moment = birth, constant whole-making. → L2657-2663
- `[ns_aop_096]` `[trigger: death_transform]` `[factor_trigger: astro_death_trans AND astro_rebirth]` `[role: 总结]` When one space-structure ends, myriads born elsewhere—death = transformation, carried to immediate birthing. → L2668-2676"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 10: Positive vs Negative Time"
    factor_refs: list = ['astro_neg_time', 'astro_pos_time', 'astro_live_moment', 'astro_death_transform']
    
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
        l1_anchor="ap_v1.0.0_entry_10__positive_vs_negative_001_L1",
    )
    version: str = "1.0.0"
