"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237906
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
    semantic_id="ap_v1.0.0_entry_5__ethics_vs_esthetics_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5EthicsVsEsthetics(SemanticEntry):
    """
    **Source Text** (Lines 3949-4111):
> The main point, however, which we have to make is that all ethi...
    """
    
    original_text: str = """**Source Text** (Lines 3949-4111):
> The main point, however, which we have to make is that all ethical judgments divide the sum total of experiences into two categories; one which is acceptable, the other which must be rejected...
>
> Ethical judgments create evil. Esthetical judgments produce stresses, emphases, relief, contrasts, light and shade, actual and implied representation, climaxes and suggestions. They balance opposites, and never condemn absolutely. They harmonize; never discard. They deal with whole relations...
>
> So to educate man is the task of the new Psychology and of the new Astrology outlined in this book.

**Key Term Analysis**:
- **Ethical judgments**: `divide accept/reject` / `feeling-based` / `create evil` / `fear-based`
- **Esthetical judgments**: `balance opposites` / `thinking-based` / `no evil/good` / `only form`
- **New psychology/astrology**: `esthetical education` / `perceive significance` / `creative living`

**English Paraphrase (Primary Language)**:
Rudhyar contrasts ethics (divides accept/reject, creates evil, fear-based) with esthetics (balances opposites, never condemns absolutely, deals with whole relations). "Ethical judgments create evil. Esthetical judgments... balance opposites, and never condemn absolutely."

In esthetics, "the only evil is—lack of significance," which is due to inability to perceive, not inherent in things. The esthetical attitude transforms all living into "creative activity"—destroying valuations based on past judgments.

"So to educate man is the task of the new Psychology and of the new Astrology outlined in this book"—no "bad" aspects or "evil" planets.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar对比伦理（划分接受/拒绝，创造恶，基于恐惧）与美学（平衡对立，从不绝对谴责，处理整体关系）。"伦理判断创造恶。美学判断……平衡对立，从不绝对谴责。"

在美学中，"唯一的恶是——缺乏意义"，这是由于无法感知，而非事物固有。美学态度将所有生活转化为"创造性活动"——破坏基于过去判断的价值评估。

"如此教育人是这本书所概述的新心理学和新占星学的任务"——没有"坏"相位或"恶"行星。

**Narrative Snippets**:
- `[ns_aop_119]` `[trigger: ethics_esthetics]` `[factor_trigger: astro_eth_esth AND astro_eth_esth_struct]` `[role: 主干]` Ethics divides/creates evil; Esthetics balances opposites, never condemns, no evil—only lack of significance. → L3949-4095
- `[ns_aop_120]` `[trigger: new_astrology]` `[factor_trigger: astro_new_astro AND astro_esth_astro]` `[role: 总结]` New astrology task: esthetical education, no "bad" aspects or "evil" planets. → L4109-4111"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: Ethics vs Esthetics"
    factor_refs: list = ['astro_esthetical', 'astro_no_evil']
    
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
        l1_anchor="ap_v1.0.0_entry_5__ethics_vs_esthetics_001_L1",
    )
    version: str = "1.0.0"
