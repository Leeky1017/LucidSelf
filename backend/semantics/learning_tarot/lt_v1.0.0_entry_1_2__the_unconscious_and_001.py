"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007895
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
    semantic_id="lt_v1.0.0_entry_1_2__the_unconscious_and_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Entry12TheUnconsciousAnd(SemanticEntry):
    """
    **Source Text** (Lines 346-464):
> The answer lies with the unconscious—that deep level of memory an...
    """
    
    original_text: str = """**Source Text** (Lines 346-464):
> The answer lies with the unconscious—that deep level of memory and awareness that resides within each of us, but outside our everyday experience... Sigmund Freud stressed the irrational, primitive aspect of the unconscious. He thought that it was the home of our most unacceptable desires and urges. His contemporary Carl Jung emphasized the positive, creative aspect of the unconscious. He tried to show that it has a collective component that touches universal qualities.
>
> If there is meaning in a reading, where does it come from? I believe it comes from that part of ourselves that is aware of the divine source of meaning. This is an aspect of the unconscious, yet it is much more. It acts as a wise advisor who knows us well... Some people call this advisor the soul, the superconscious, or the higher self. I call it the Inner Guide because that is the role it plays in connection with the tarot.

**Key Term Analysis**:
- **Unconscious**: `deep level of memory and awareness` / `outside everyday experience`
- **Freud view**: `irrational, primitive` / `unacceptable desires and urges`
- **Jung view**: `positive, creative` / `collective component` / `universal qualities`
- **Inner Guide**: `wise advisor` / `knows us well` / `soul, superconscious, higher self`
- **Projection**: `unconscious material onto objects` / `Rorschach inkblot test`
- **Archetypes**: `consistent, directing patterns` / `universal human experiences`

**English Paraphrase (Primary Language)**:
Bunning synthesizes Freud and Jung: the unconscious contains both shadow material (Freud) and creative wisdom (Jung). But her key innovation is the **Inner Guide**—"that part of ourselves that is aware of the divine source of meaning."

The Inner Guide = soul/superconscious/higher self. It "acts as a wise advisor who knows us well"—understanding what we need and guiding us toward authentic paths. Tarot works by **accessing this Inner Guide** through symbolic projection.

**Mechanism**: We project unconscious content onto ambiguous card images (like Rorschach test). What we "see" in cards reveals our inner state. But beyond projection, the cards we draw are not random—they're selected by Inner Guide through synchronicity.

**Practical implication**: "You do not have to have 'psychic powers' to use the tarot successfully. All you need is the willingness to honor and develop your natural intuitive abilities."

**Complete Chinese Interpretation (Secondary Language)**:
Bunning综合了弗洛伊德和荣格：无意识既包含阴影材料（弗洛伊德），也包含创造性智慧（荣格）。但她的关键创新是**内在指引**——"我们自身中意识到意义神圣来源的那部分"。

内在指引 = 灵魂/超意识/高我。它"作为了解我们的智慧顾问"——理解我们需要什么并引导我们走向真实的道路。塔罗通过象征性投射**接入这个内在指引**而起作用。

**机制**：我们将无意识内容投射到模糊的牌面图像上（如罗夏墨迹测试）。我们在牌中"看到"的揭示了我们的内在状态。但除了投射之外，我们抽到的牌并非随机——它们是由内在指引通过共时性选择的。

**实际意义**："你不需要'通灵能力'才能成功使用塔罗。你只需要愿意尊重和发展你天生的直觉能力。"

**Core Points**:
- Unconscious = deep awareness outside everyday experience
- Freud: primitive urges; Jung: creative collective wisdom
- Inner Guide = wise advisor, soul, higher self accessing divine meaning
- Tarot works through projection + synchronicity
- No "psychic powers" needed—only willingness to honor intuition

**Narrative Snippets**:
- `[ns_ltt_004]` `[trigger: unconscious_definition]` `[factor_trigger: tarot_unconscious AND unconscious]` `[role: 主干]` The unconscious is that deep level of memory and awareness that resides within each of us, but outside our everyday experience. → L346-348
- `[ns_ltt_005]` `[trigger: jung_creative]` `[factor_trigger: archetype]` `[role: 主干依赖]` Carl Jung emphasized the positive, creative aspect of the unconscious—a collective component with archetypes as consistent, directing patterns. → L351-353
- `[ns_ltt_006]` `[trigger: inner_guide_def]` `[factor_trigger: inner_guide]` `[role: 主干]` The Inner Guide is that part of ourselves aware of the divine source of meaning—a wise advisor who knows us well. → L434-438
- `[ns_ltt_007]` `[trigger: projection_mechanism]` `[factor_trigger: projection]` `[role: 条件分支]` Projection is why tarot cards are valuable—their intriguing pictures effectively tap the unconscious. → L374-375
- `[ns_ltt_008]` `[trigger: synchronicity_def]` `[factor_trigger: synchronicity AND intuition]` `[role: 条件分支]` Cards drawn are not truly random—they are selected through synchronicity, meaningful coincidence connecting inner and outer. → L462-464

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Bunning's "Inner Guide" concept draws on Jung's Self archetype and transpersonal psychology (Assagioli's Higher Self). Her position that cards aren't truly "random" reflects synchronicity theory (Jung, 1952). This psychological framing distinguishes her from predictive fortune-telling traditions.
- **中文**: Bunning的"内在指引"概念借鉴了荣格的自性原型和超个人心理学（阿萨吉奥利的高我）。她认为牌并非真正"随机"的立场反映了共时性理论（荣格，1952年）。这种心理学框架使她区别于预测性算命传统。"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1.2: The Unconscious and Inner Guide"
    factor_refs: list = ['inner_guide', 'unconscious', 'projection', 'synchronicity', 'archetype']
    
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
        l1_anchor="lt_v1.0.0_entry_1_2__the_unconscious_and_001_L1",
    )
    version: str = "1.0.0"
