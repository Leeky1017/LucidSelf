"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007913
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
    semantic_id="lt_v1.0.0_entry_2_1__22_major_arcana___t_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Entry2122MajorArcanaT(SemanticEntry):
    """
    **Source Text** (Lines 473-529):
> The standard tarot deck consists of 78 cards divided into two sec...
    """
    
    original_text: str = """**Source Text** (Lines 473-529):
> The standard tarot deck consists of 78 cards divided into two sections, the major and minor arcanas. The word arcana is the plural of arcanum, which means "profound secret." To the alchemists of the Middle Ages, the arcanum was the secret of nature. The tarot cards are therefore a collection of the "secrets" that underlie and explain our universe.
>
> The 22 cards of the major arcana are the heart of the deck. Each of these cards symbolizes some universal aspect of human experience. They represent the archetypes—consistent, directing patterns of influence that are an inherent part of human nature...
>
> Many interpreters view the major arcana as showing the different stages on an individual's journey of inner growth—what some call the Fool's Journey. In these systems, each card stands for some quality or experience that we must incorporate before we can realize our wholeness.

**Key Term Analysis**:
- **Arcana**: `plural of arcanum` / `profound secret` / `alchemists' secret of nature`
- **Major Arcana (22)**: `heart of the deck` / `universal aspects` / `archetypes`
- **Archetype**: `consistent, directing patterns of influence` / `inherent part of human nature`
- **Fool's Journey**: `stages of inner growth` / `quality or experience to incorporate` / `realize wholeness`
- **Card 0 to Card 21**: `earliest awareness → integration and fulfillment`

**English Paraphrase (Primary Language)**:
The 22 Major Arcana cards are the "heart of the deck"—each symbolizing a universal aspect of human experience. "Arcana" means "profound secrets" (alchemical term), so tarot = "collection of secrets underlying our universe."

**The Fool's Journey** framework: Major Arcana as developmental stages from Card 0 (Fool = beginning, potential, innocence) through various initiations to Card 21 (World = integration, completion, fulfillment). Each card = "quality or experience we must incorporate before we can realize our wholeness."

Journey isn't linear—we "make mistakes, skip lessons, fail to realize potential." Some never feel Hermit's call to look inward or experience Tower's liberating crisis. Often we learn lessons out of order or need to repeat them (Hanged Man's surrender particularly difficult).

**Weight in readings**: "A major arcana card is always given extra weight in a reading. When one of these cards appears, you know the issues at stake are not mundane or temporary."

**Complete Chinese Interpretation (Secondary Language)**:
22张大阿卡纳牌是整副牌的"核心"——每张都象征人类经验的一个普遍面向。"阿卡纳"意为"深奥秘密"（炼金术语），因此塔罗 = "支撑我们宇宙的秘密集合"。

**愚者之旅**框架：大阿卡纳作为从第0号牌（愚者 = 开始、潜能、纯真）经过各种启蒙到第21号牌（世界 = 整合、完成、圆满）的发展阶段。每张牌 = "我们必须整合才能实现完整性的品质或经验"。

旅程不是线性的——我们"犯错、跳课、无法实现潜能"。有些人从未感受到隐士向内看的召唤，或经历高塔的解放危机。我们经常不按顺序学习课程或需要重复（倒吊人的臣服特别困难）。

**解读中的权重**："大阿卡纳牌在解读中总是被赋予额外权重。当这些牌出现时，你知道所涉及的问题不是平凡或暂时的。"

**Core Points**:
- Arcana = profound secrets (alchemical term)
- 22 Major Arcana = heart of deck, universal archetypes
- Fool's Journey = developmental stages toward wholeness
- Journey non-linear: mistakes, repetitions, out-of-order lessons
- Major Arcana = extra weight in readings, non-mundane issues

**Narrative Snippets**:
- `[ns_ltt_009]` `[trigger: arcana_meaning]` `[factor_trigger: tarot_arcana_definition AND arcana]` `[role: 主干]` Arcana means "profound secret"—tarot cards are a collection of the secrets that underlie and explain our universe. → L474-476
- `[ns_ltt_010]` `[trigger: major_arcana_heart]` `[factor_trigger: major_arcana]` `[role: 主干]` The 22 cards of the major arcana are the heart of the deck—each symbolizes a universal aspect of human experience. → L477-478
- `[ns_ltt_011]` `[trigger: fools_journey]` `[factor_trigger: fools_journey]` `[role: 主干依赖]` The Fool's Journey shows stages of inner growth—each card stands for some quality we must incorporate before we can realize wholeness. → L495-498
- `[ns_ltt_012]` `[trigger: wholeness_goal]` `[factor_trigger: wholeness]` `[role: 总结]` Each card represents a quality or experience we must incorporate before we can realize our wholeness—the goal of the Fool's Journey. → L497-498
- `[ns_ltt_013]` `[trigger: new_beginning]` `[factor_trigger: new_beginning]` `[role: 条件分支]` The Fool (Card 0) represents new beginning—the earliest awareness of potential before the journey of inner growth. → L500-502
- `[ns_ltt_023]` `[trigger: fool_card]` `[factor_trigger: tarot_fool]` `[role: 条件分支]` The Fool (Card 0) is the protagonist of the Fool's Journey—representing innocence, potential, and the beginning of all experience. → L499-502

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The "Fool's Journey" as continuous narrative originates with Eden Gray (1970s) and was popularized by Rachel Pollack. Bunning's version emphasizes non-linear development. The 22-card structure corresponds to Hebrew alphabet (22 letters) per Eliphas Levi (1856), though this connection is contested.
- **中文**: "愚者之旅"作为连续叙事起源于Eden Gray（1970年代），由Rachel Pollack普及。Bunning的版本强调非线性发展。22张牌结构对应希伯来字母表（22个字母），这是Eliphas Levi（1856年）的说法，但这种联系有争议。"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2.1: 22 Major Arcana - The Fool's Journey"
    factor_refs: list = ['major_arcana', 'fools_journey', 'archetype', 'wholeness']
    
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_entry_2_1__22_major_arcana___t_001_L1",
    )
    version: str = "1.0.0"
