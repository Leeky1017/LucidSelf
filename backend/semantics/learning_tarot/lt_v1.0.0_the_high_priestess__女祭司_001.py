"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007979
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
    semantic_id="lt_v1.0.0_the_high_priestess__女祭司_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheHighPriestess女祭司(SemanticEntry):
    """
    **Source Text** (Lines 3591-3654):
> **Keywords**: Nonaction • Unconscious Awareness • Potential • M...
    """
    
    original_text: str = """**Source Text** (Lines 3591-3654):
> **Keywords**: Nonaction • Unconscious Awareness • Potential • Mystery
>
> **Actions**:
> - **Staying Nonactive**: withdrawing from involvement, allowing events to proceed without intervention, being receptive to influence, becoming calm, being passive, waiting patiently
> - **Accessing the Unconscious**: using your intuition, seeking guidance from within, trusting your inner voice, opening to dreams and the imagination, being aware of a larger reality
> - **Seeing the Potential**: understanding the possibilities, opening to what could be, seeing your hidden talents, allowing development, letting what is there flower
> - **Sensing the Mystery**: looking beyond the obvious, approaching a closed off area, opening to the unknown, remembering something important, sensing the secret and hidden, seeking what is concealed, acknowledging the Shadow
>
> **Description**: The High Priestess is the guardian of the unconscious. She sits in front of the thin veil of unawareness which is all that separates us from our inner landscape... The High Priestess is the feminine principle that balances the masculine force of the Magician.

**Key Term Analysis**:
- **The High Priestess (2)**: `guardian of the unconscious` / `feminine principle` / `balances Magician`
- **Nonaction**: `withdrawing from involvement` / `allowing events to proceed` / `waiting patiently`
- **Unconscious Awareness**: `using intuition` / `seeking guidance from within` / `trusting inner voice`
- **Potential**: `understanding possibilities` / `seeing hidden talents` / `allowing development`
- **Mystery**: `looking beyond obvious` / `sensing secret and hidden` / `acknowledging Shadow`

**English Paraphrase (Primary Language)**:
**The High Priestess (Card 2)** is "the guardian of the unconscious." She sits before "the thin veil of unawareness which is all that separates us from our inner landscape."

**Key aspects**:
1. **Nonaction**: "Withdrawing from involvement, allowing events to proceed without intervention." Unlike the Magician's active doing, she represents wise waiting.

2. **Unconscious Awareness**: "Using your intuition, seeking guidance from within, trusting your inner voice, opening to dreams and the imagination."

3. **Potential**: "Understanding the possibilities, seeing your hidden talents, allowing development, letting what is there flower."

4. **Mystery**: "Looking beyond the obvious, sensing the secret and hidden, acknowledging the Shadow."

**Balance**: "The High Priestess is the feminine principle that balances the masculine force of the Magician." Together, cards 1 and 2 form the first polarity pair.

**Reading implication**: "The High Priestess poses a challenge to go deeper—to look beyond the obvious, surface situation to what is hidden and obscure."

**Complete Chinese Interpretation (Secondary Language)**:
**女祭司（第2号牌）**是"无意识的守护者"。她坐在"无觉知的薄纱前，这薄纱是将我们与内在景观分开的全部"。

**关键方面**：
1. **不行动**："从参与中退出，允许事件在没有干预的情况下进行。"不同于魔术师的主动作为，她代表智慧的等待。

2. **无意识觉知**："使用你的直觉，从内在寻求指引，信任你的内在声音，向梦境和想象力开放。"

3. **潜能**："理解可能性，看到你隐藏的才能，允许发展，让那里的东西绽放。"

4. **神秘**："看透表面，感知秘密和隐藏的事物，承认阴影。"

**平衡**："女祭司是平衡魔术师阳性力量的阴性原则。"第1和第2张牌共同形成第一对极性配对。

**解读含义**："女祭司提出挑战，要你更深入——看透表面情境，发现隐藏和晦涩的东西。"

**Core Points**:
- Card 2 = guardian of unconscious, feminine principle balancing Magician
- Nonaction: withdrawing, allowing events, patient waiting
- Unconscious Awareness: intuition, inner voice, dreams
- Potential: hidden talents, possibilities, allowing development
- Mystery: beyond obvious, secret and hidden, Shadow

**Narrative Snippets**:
- `[ns_ltt_027]` `[trigger: high_priestess_card]` `[factor_trigger: tarot_high_priestess AND nonaction]` `[role: 主干]` The High Priestess is the guardian of the unconscious—she sits in front of the thin veil of unawareness which is all that separates us from our inner landscape. → L3639-3641
- `[ns_ltt_028]` `[trigger: high_priestess_balance]` `[factor_trigger: tarot_high_priestess AND tarot_tarot_magician]` `[role: 主干依赖]` The High Priestess is the feminine principle that balances the masculine force of the Magician. → L3643-3644
- `[ns_ltt_029]` `[trigger: high_priestess_deeper]` `[factor_trigger: tarot_high_priestess AND tarot_intuition AND unconscious_awareness]` `[role: 总结]` The High Priestess poses a challenge to go deeper—to look beyond the obvious, surface situation to what is hidden and obscure. → L3649-3651"""
    normalized_text_zh: str = """"""
    subject: str = "The High Priestess (女祭司)"
    factor_refs: list = ['tarot_high_priestess', 'nonaction', 'unconscious_awareness', 'mystery']
    
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
        l1_anchor="lt_v1.0.0_the_high_priestess__女祭司_001_L1",
    )
    version: str = "1.0.0"
