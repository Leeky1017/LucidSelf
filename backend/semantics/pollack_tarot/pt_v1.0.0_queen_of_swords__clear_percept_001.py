"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995047
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
    semantic_id="pt_v1.0.0_queen_of_swords__clear_percept_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class QueenOfSwordsClearPercept(SemanticEntry):
    """
    **Visual Elements**:
- Queen seated on throne
- Sword pointing straight up
- Left hand extended (bec...
    """
    
    original_text: str = """**Visual Elements**:
- Queen seated on throne
- Sword pointing straight up
- Left hand extended (beckoning)
- Clear sky after storm
- Butterflies on throne (transformation through sorrow)
- Bird in flight

**English Paraphrase**:

The **Queen of Swords** represents **clarity achieved through experience of loss**. Where King wields authority, Queen possesses **wisdom born of sorrow**. Her sword points straight up for **pure perception** - she sees truth clearly because she has **faced pain and emerged stronger**.

**Core Symbolism**:
- **Sword pointing up**: Pure wisdom, unclouded perception
- **Extended hand**: Beckoning truth, inviting clarity
- **Clear sky**: After storm passes, clarity remains
- **Butterflies**: Transformation through grief, beauty from pain
- **Bird**: Mind freed from illusion

**Upright Meaning**:
- **Clear perception**: Sees reality without illusion
- **Wisdom through sorrow**: Understanding gained from loss
- **Independent**: Self-sufficient, doesn't need validation
- **Honest communication**: Speaks truth directly, without cruelty
- **Perceptive judge**: Sees through deception
- **Widow archetype**: Often represents loss transforming to strength

**Reversed/Challenged**:
- **Bitter**: Sorrow turns to cynicism
- **Harsh judgment**: Uses insight to wound
- **Isolated**: Independence becomes loneliness
- **Overly critical**: Cannot see positive, only flaws
- **Vindictive**: Uses knowledge to punish

**完整中文诠释**:
**宝剑皇后**=通过失去经验获得的**清晰**。国王掌握权威，皇后拥有**悲伤诞生的智慧**。剑直指向上为**纯净感知**——她清晰见真理因**面对痛苦并浮现更强**。**图像元素**：**剑指向上**=纯智慧，无云感知；**伸出的手**=召唤真理，邀请清晰；**晴空**=风暴过后清晰留存；**蝴蝶**=通过悲伤转化，痛苦中的美；**鸟**=心智从幻觉中解放。**正位含义**：**清晰感知**（无幻觉地看到现实），**通过悲伤的智慧**（从失去中获得理解），**独立**（自给自足，不需验证），**诚实沟通**（直接说真话，无残忍），**敏锐判断**（看穿欺骗），**寡妇原型**（常代表失去转化为力量）。**逆位/挑战**：**苦涩**（悲伤转为愤世嫉俗），**严酷判断**（用洞察伤害），**孤立**（独立变成孤独），**过度批判**（无法看到积极，只见缺点），**报复**（用知识惩罚）。**原型**：常与**寡妇**相联——失去但获得独立与洞察的女人。非由关系定义，独自站在真理中。

**Archetype**: Often associated with **widow** - woman who has lost but gained independence and insight. Not defined by relationship, stands alone in truth.

**Narrative Snippets**:
- `[ns_78deg_279]` `[trigger: queen_swords_clarity]` `[factor_trigger: tarot_queen_swords AND state_clear_perception]` `[role: 主干]` Queen of Swords represents clarity achieved through experience of loss—wisdom born of sorrow; she sees truth clearly because she has faced pain and emerged stronger. → English Paraphrase
- `[ns_78deg_280]` `[trigger: sword_up_queen]` `[factor_trigger: tarot_queen_swords AND symbol_upward_sword]` `[role: 主干依赖]` Sword pointing straight up, extended hand beckoning truth—pure perception, unclouded wisdom; butterflies on throne symbolizing transformation through grief, beauty from pain. → Core Symbolism
- `[ns_78deg_281]` `[trigger: queen_swords_independent]` `[factor_trigger: tarot_queen_swords AND state_independence]` `[role: 条件分支]` Clear perception seeing reality without illusion—independent, self-sufficient, doesn't need validation; speaks truth directly without cruelty. → Upright Meaning
- `[ns_78deg_282]` `[trigger: queen_swords_reversed]` `[factor_trigger: tarot_queen_swords AND polarity_reversed]` `[role: 例外处理]` Reversed: sorrow turns to bitterness and cynicism; harsh judgment using insight to wound; independence becomes loneliness; overly critical, vindictive. → Reversed Meaning
- `[ns_78deg_283]` `[trigger: widow_archetype]` `[factor_trigger: tarot_queen_swords AND archetype_widow]` `[role: 总结]` Widow archetype—woman who has lost but gained independence and insight; not defined by relationship, stands alone in truth; loss transformed to strength. → Archetype
- `[ns_78deg_406]` `[trigger: butterflies_transformation]` `[factor_trigger: tarot_queen_swords AND symbol_butterflies]` `[role: 条件分支]` Butterflies on throne—transformation through grief, beauty emerging from pain; clear sky after storm showing clarity that remains when turmoil passes. → Core Symbolism
- `[ns_78deg_407]` `[trigger: honest_communication]` `[factor_trigger: tarot_queen_swords AND principle_honest_communication]` `[role: 条件分支]` Honest communication—speaks truth directly without cruelty; perceptive judge who sees through deception; wisdom allows clarity without harshness. → Upright Meaning
- `[ns_78deg_481]` `[trigger: bird_flight]` `[factor_trigger: tarot_queen_swords AND symbol_bird_flight]` `[role: 条件分支]` Bird in flight—mind freed from illusion; thought that has risen above earthly attachments; clarity of vision gained when one is no longer bound by hope or fear. → Visual Elements
- `[ns_78deg_512]` `[trigger: sorrow_wisdom]` `[factor_trigger: tarot_queen_swords AND state_wisdom_through_loss]` `[role: 条件分支]` Wisdom born of sorrow—understanding gained from loss; the grief that strips away illusion reveals what truly matters; pain becomes teacher of clarity. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Swords: Clear Perception"
    factor_refs: list = ['faculty', 'existing', 'attainment', 'existing', 'archetype', 'existing', 'expression', 'existing', 'pitfall', 'existing']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_queen_of_swords__clear_percept_001_L1",
    )
    version: str = "1.0.0"
