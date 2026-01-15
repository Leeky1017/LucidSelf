"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.109917
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
    semantic_id="tis_v1.0.0_trine__120_____harmony_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Trine120Harmony(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Trine | 120° aspect, same element | Natural harmony |
| Ease | Effortless flow | Blessing and hazard |
| Complacency | Taking for granted | Trine's shadow |

#### Source Text

"The trick with trines is to see them as representing areas of life with almost unlimited potential for growth. An alliance has been formed in the mind. Two planets are ready to pull together toward a common goal with no energy wasted on friction between them. And yet that lack of friction has allowed them to fall asleep. We must awaken them."

#### English Paraphrase (Primary Language)

The **trine** (120°) represents **natural harmony**: two planetary energies flowing together effortlessly within the same element. This creates **unlimited potential**—but also a hidden danger.

**The paradox**: Trines feel good, so we take them for granted. Without friction to wake us up, trined planets can **fall asleep**. The gift becomes wasted potential.

**Activation requirement**: Forrest emphasizes that trines must be **consciously awakened** through will and self-discipline. When activated, they carry us further than any square with far less effort. When neglected, they lead to "self-satisfied" stagnation.

#### Complete Chinese Interpretation (Secondary Language)

**三分相**（120度）代表**自然和谐**：两种行星能量在同一元素内毫不费力地流动。这创造了**无限潜力**——但也有隐藏的危险。

**悖论**：三分相感觉良好，所以我们视之为理所当然。没有摩擦来唤醒我们，三分相行星可能**沉睡**。天赋变成浪费的潜力。

**激活要求**：Forrest强调三分相必须通过意志和自律**有意识地唤醒**。激活后，它们以远少于四分相的努力带我们走得更远。被忽视时，它们导致"自满的"停滞。

#### Core Points

- **120° aspect**: Same element, natural flow
- **Effortless harmony**: No friction between planets
- **Complacency risk**: Taking the gift for granted
- **Awakening required**: Must consciously activate potential

#### Detailed Explanation

The trine connects planets in the **same element**, creating natural affinity and easy flow. Fire trines Fire; Water trines Water. The planets speak the same language and support each other without effort. This is the "gift" aspect—abilities that come naturally, talents that require no struggle.

Forrest's critical insight is that trines can become **too comfortable**. Because no friction exists, there is no urgency to develop the potential. The "sleeping beauty" metaphor captures the danger: the gift lies dormant, never awakened by the kiss of conscious effort. Many people with strong trines underperform relative to their potential precisely because nothing pushes them.

**Activation through will** is the trine's developmental task. The person must recognize the gift and **consciously choose** to develop it. Once activated, trines provide enormous resources for relatively little effort—this is their true value. But activation requires awareness and intention.

Traditional astrology overvalues trines as "good" aspects. Forrest's nuance shows that trines are **neutral potentials**: tremendous when awakened, utterly wasted when neglected. A single difficult square may produce more actual achievement than multiple dormant trines.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Forrest's trine interpretation balances the traditional "benefic" view with awareness of complacency risk. This nuanced approach prevents over-reliance on "good" aspects.
- **中文**: Forrest的三分相诠释在传统"吉相"观点与对自满风险的觉察间取得平衡。这种细致方法防止过度依赖"好"相位。

**Narrative Snippets**:
- `[ns_forrest_asp_007]` `[trigger: trine]` `[factor_trigger: trine AND aspect_harmony]` `[role: 主干]` The trine represents unlimited potential—an alliance with no friction—but that lack of friction can allow planets to fall asleep. → Source Text
- `[ns_forrest_asp_008]` `[trigger: awakening]` `[factor_trigger: aspect_trine AND aspect_activation]` `[role: 主干依赖]` Trines must be consciously awakened through will and self-discipline to realize their potential. → English Paraphrase
- `[ns_forrest_asp_017]` `[trigger: trine_complacency]` `[factor_trigger: aspect_trine AND aspect_stagnation]` `[role: 条件分支]` Because trines feel good, we take them for granted—the gift becomes wasted potential when neglected. → Shadow
- `[ns_forrest_asp_018]` `[trigger: trine_activation]` `[factor_trigger: aspect_trine AND aspect_effort]` `[role: 条件分支]` Once activated through conscious effort, trines carry us further than any square with far less effort. → Activation"""
    normalized_text_zh: str = """"""
    subject: str = "Trine (120°) - Harmony"
    factor_refs: list = ['aspect_trine', 'new_candidate', 'new_candidate', 'engine_id', 'aspect_trine', 'astro_semantic', 'new_candidate', 'astro_semantic', 'new_candidate', 'astro_semantic', 'source_ref', 'rel_forrest_tri_001', 'aspect_trine', 'supporting', 'rel_forrest_tri_002', 'trine', 'realizing', 'evi_forrest_tri_001', 'rule_aspect_trine', 'concept_trine', 'sanhe_harmony', 'flow_dream']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_trine__120_____harmony_001_L1",
    )
    version: str = "1.0.0"
