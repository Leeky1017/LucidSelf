"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994819
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
    semantic_id="pt_v1.0.0_ace_of_cups__love_s_gift_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class AceOfCupsLoveSGift(SemanticEntry):
    """
    **Visual Elements**:
- Hand from cloud holding ornate chalice
- Dove descending with wafer (Holy Gra...
    """
    
    original_text: str = """**Visual Elements**:
- Hand from cloud holding ornate chalice
- Dove descending with wafer (Holy Grail imagery)
- Water overflows, forms five streams
- Lotus flowers below
- Sacred, spiritual composition

**English Paraphrase**:

The **Ace of Cups** represents the **gift of love** - the spiritual foundation underpinning all existence. This is the **Holy Grail**, containing the divine presence in the world. It signifies happiness, emotional awakening, and the capacity to receive love and joy.

**Core Symbolism**:
- **Chalice**: Container for divine love/spirit
- **Dove + wafer**: Holy Grail/Eucharist symbolism (Holy Ghost present in world)
- **Overflowing water**: Abundance of emotion, love freely given
- **Five streams**: Love flowing into five senses, making world perceptible
- **Lotus**: Spiritual awakening, enlightenment from water

**Upright Meaning**:
- **New love**: Beginning of relationship, emotional opening
- **Happiness**: Gift of joy, time of emotional fulfillment
- **Spiritual awakening**: Connection to divine love
- **Emotional availability**: Heart open to receive and give
- **Creative inspiration**: Imagination awakened
- **The Grail**: Finding what gives life meaning and value

**Reversed/Challenged**:
- **Unhappiness**: Joy denied or unrecognized
- **Love refused**: Unable or unwilling to accept love offered
- **Emotional closure**: Heart shut down, protection becomes prison
- **Violence/destruction**: When Grail leaves kingdom (Arthur legend), chaos follows
- **Clouded joy**: Happiness exists but cannot be perceived

**完整中文诠释**:
**圣杯王牌**=**爱之礼物**——支撑所有存在的灵性基础。这是**圣杯**（Holy Grail），包含世界中的神圣临在。象征幸福、情感觉醒、接受爱与喜悦的能力。**图像元素**：**圣杯**=神圣爱/灵性的容器；**鸽子+圣饼**=圣杯/圣餐象征（圣灵临在于世界）；**溢出的水**=情感丰盛，爱被自由给予；**五条水流**=爱流入五种感官，使世界可感知；**莲花**=灵性觉醒，从水中得启蒙。**正位含义**：**新恋情**（关系开始，情感打开），**幸福**（喜悦之礼，情感满足的时刻），**灵性觉醒**（与神圣之爱连接），**情感可得**（心打开以接受和给予），**创意灵感**（想象力被唤醒），**圣杯**（找到赋予生命意义和价值之物）。**逆位/挑战**：**不快乐**（喜悦被拒绝或不被承认），**拒绝爱**（无法或不愿接受被提供的爱），**情感封闭**（心关闭，保护变成牢笼），**暴力/毁灭**（当圣杯离开王国时【亚瑟传说】，混乱随之），**被遮蔽的喜悦**（幸福存在但无法被感知）。

**Philosophical Layer**: **Love as spiritual basis** - world functions not by laws/structures alone but by spiritual presence giving them meaning. The Grail legend teaches: **love cannot be conquered, only received**. Cups = receptivity.

**Narrative Snippets**:
- `[ns_78deg_215]` `[trigger: ace_cups_grail]` `[factor_trigger: tarot_ace_cups AND symbol_holy_grail]` `[role: 主干]` Ace of Cups represents the gift of love—the Holy Grail containing divine presence in the world; spiritual foundation underpinning all existence. → English Paraphrase
- `[ns_78deg_216]` `[trigger: dove_wafer]` `[factor_trigger: tarot_ace_cups AND symbol_dove AND symbol_wafer]` `[role: 主干依赖]` Dove descending with wafer—Holy Ghost present in world; chalice as container for divine love/spirit; Eucharist symbolism of sacred presence. → Core Symbolism
- `[ns_78deg_217]` `[trigger: five_streams]` `[factor_trigger: tarot_ace_cups AND symbol_five_streams]` `[role: 条件分支]` Water overflows forming five streams—love flowing into five senses, making the world perceptible; abundance given freely, not earned. → Core Symbolism
- `[ns_78deg_218]` `[trigger: ace_cups_opening]` `[factor_trigger: tarot_ace_cups AND state_heart_opening]` `[role: 条件分支]` New love beginning, emotional availability, heart open to receive and give—happiness as gift, creative inspiration awakened. → Upright Meaning
- `[ns_78deg_219]` `[trigger: ace_cups_reversed]` `[factor_trigger: tarot_ace_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: love refused, heart shut down, protection becomes prison; when Grail leaves kingdom, chaos follows—joy exists but cannot be perceived. → Reversed Meaning
- `[ns_78deg_220]` `[trigger: grail_lesson]` `[factor_trigger: tarot_ace_cups AND principle_receptivity]` `[role: 总结]` The Grail legend teaches: love cannot be conquered, only received—Cups represent receptivity; world functions by spiritual presence giving meaning, not by laws alone. → Philosophical Layer
- `[ns_78deg_440]` `[trigger: lotus_awakening]` `[factor_trigger: tarot_ace_cups AND symbol_lotus]` `[role: 条件分支]` Lotus flowers below the cup—spiritual awakening rising from water; enlightenment emerging from emotional depths; beauty rooted in the unconscious. → Core Symbolism
- `[ns_78deg_441]` `[trigger: creative_inspiration]` `[factor_trigger: tarot_ace_cups AND state_inspiration]` `[role: 条件分支]` Creative inspiration and emotional availability—heart open to both receive and give; imagination awakened by love's gift; the Grail as what gives life meaning. → Upright Meaning
- `[ns_78deg_494]` `[trigger: overflowing_abundance]` `[factor_trigger: tarot_ace_cups AND principle_overflow]` `[role: 条件分支]` Water overflows the chalice—true love cannot be contained; abundance given freely, not earned or controlled; the gift exceeds any vessel designed to hold it. → Visual Elements
- `[ns_78deg_551]` `[trigger: hand_from_cloud_cups]` `[factor_trigger: tarot_ace_cups AND symbol_divine_hand]` `[role: 条件分支]` Hand from cloud holding ornate chalice—divine gift, spiritual energy made emotionally available; the container as gift, not just its contents. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Cups: Love's Gift"
    factor_refs: list = ['receptive', 'existing', 'receptive', 'existing', 'opening', 'existing', 'state', 'existing', 'principle', 'existing']
    
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
        l1_anchor="pt_v1.0.0_ace_of_cups__love_s_gift_001_L1",
    )
    version: str = "1.0.0"
