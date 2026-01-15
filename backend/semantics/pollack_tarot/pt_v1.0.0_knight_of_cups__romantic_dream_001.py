"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994845
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
    semantic_id="pt_v1.0.0_knight_of_cups__romantic_dream_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KnightOfCupsRomanticDream(SemanticEntry):
    """
    **Visual Elements**:
- Knight on slow horse
- Gazing at cup, lost in contemplation
- Winged helmet a...
    """
    
    original_text: str = """**Visual Elements**:
- Knight on slow horse
- Gazing at cup, lost in contemplation
- Winged helmet and feet
- Parched landscape with narrow river
- Resembles Death card (transformation symbol)

**English Paraphrase**:

The **Knight of Cups** represents **imagination ungrounded in action** - the romantic dreamer, lost in fantasy. This is **Fire of Water** (action of emotion) unreconciled. The Knight has not learned that **true imagination feeds on action**, not just daydreams.

**Core Symbolism**:
- **Slow horse**: Passivity, reluctance to engage world
- **Lost in cup**: Absorbed by inner fantasy, not outer reality
- **Winged helmet/feet**: Potential for spiritual flight, if directed
- **Parched land**: Imagination not nourished by real engagement
- **Resembles Death**: Potential for transformation through deep inner work

**Upright Meaning**:
- **Romantic idealism**: Love of ideal more than reality
- **Proposal/invitation**: Offering of romance or creative vision
- **Passive dreaminess**: Fantasy over action
- **Artistic temperament**: Vision-focused but struggle with manifestation
- **Narcissistic withdrawal**: Self-absorbed, avoiding commitment
- **Inner exploration**: Deep dive into imagination (positive interpretation)

**Reversed/Challenged**:
- **Forced action**: Pushed to engage, resents demands
- **Hypocrisy**: Outward compliance, inner resistance
- **Manipulation/lies**: Uses passivity as weapon
- **Escapism intensified**: Retreats further from reality
- **False romance**: Seduction without true feeling

**完整中文诠释**:
**圣杯骑士**=**未接地想象力**——浪漫梦想家，迷失于幻想。这是**火之水**（情感之行动）未和解。骑士未学会**真想象力靠行动而非白日梦滋养**。**图像元素**：**缓慢的马**=被动，不愿参与世界；**迷失于杯中**=被内在幻想吸收，非外在现实；**翅膀盔甲/脚**=灵性飞行潜力，若被引导；**干涸土地**=想象力未被真实参与滋养；**类似死神**=通过深度内在工作转化潜力。**正位含义**：**浪漫理想主义**（对理想的爱胜过现实），**提议/邀请**（浪漫或创意愿景的提供），**被动梦幻**（幻想胜过行动），**艺术气质**（专注愿景但难以显化），**自恋退缩**（自我吸收，逃避承诺），**内在探索**（深潜入想象力，积极解读）。**逆位/挑战**：**被迫行动**（被推动参与，憎恨要求），**伪善**（声称情感不真实拥有），**操纵/谎言**（用魅力操纵），**逃避主义强化**（更深退入幻想），**虚假浪漫**（表面迷人下的空虚）。

**Personality Type**: The **poet**, **romantic**, **idealist**. More comfortable in imagination than action. Can be deeply spiritual or merely escapist. Key question: Does fantasy derive from ego (escapism) or unconscious (genuine vision)?

**Narrative Snippets**:
- `[ns_78deg_227]` `[trigger: knight_cups_dreamer]` `[factor_trigger: tarot_knight_cups AND state_ungrounded_imagination]` `[role: 主干]` Knight of Cups represents imagination ungrounded in action—the romantic dreamer lost in fantasy; Fire of Water (action of emotion) unreconciled. → English Paraphrase
- `[ns_78deg_228]` `[trigger: slow_horse]` `[factor_trigger: tarot_knight_cups AND symbol_slow_horse]` `[role: 主干依赖]` Slow horse moving through parched landscape—passivity, reluctance to engage world; imagination not nourished by real engagement with life. → Core Symbolism
- `[ns_78deg_229]` `[trigger: knight_cups_vision]` `[factor_trigger: tarot_knight_cups AND state_artistic_vision]` `[role: 条件分支]` Artistic temperament—vision-focused but struggles with manifestation; proposal or invitation to romance, creative vision offered. → Upright Meaning
- `[ns_78deg_230]` `[trigger: knight_cups_withdrawal]` `[factor_trigger: tarot_knight_cups AND state_narcissistic_withdrawal]` `[role: 条件分支]` Narcissistic withdrawal—self-absorbed, avoiding commitment; absorbed by inner fantasy rather than outer reality. → Upright Meaning
- `[ns_78deg_231]` `[trigger: knight_cups_reversed]` `[factor_trigger: tarot_knight_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: forced action resented; hypocrisy and manipulation; escapism intensified; false romance—seduction without true feeling. → Reversed Meaning
- `[ns_78deg_232]` `[trigger: fantasy_source_question]` `[factor_trigger: tarot_knight_cups AND polarity_dual]` `[role: 总结]` Key question: Does fantasy derive from ego (escapism) or unconscious (genuine vision)? True imagination feeds on action, not just daydreams. → Personality Type
- `[ns_78deg_442]` `[trigger: death_resemblance]` `[factor_trigger: tarot_knight_cups AND tarot_major_death]` `[role: 条件分支]` Resembles Death card—potential for transformation through deep inner work; the journey inward that can lead to profound change or mere escapism. → Core Symbolism
- `[ns_78deg_443]` `[trigger: winged_potential]` `[factor_trigger: tarot_knight_cups AND symbol_winged_feet]` `[role: 条件分支]` Winged helmet and feet—potential for spiritual flight if directed; Mercury's wings representing imagination that could soar, but remains earthbound without action. → Core Symbolism
- `[ns_78deg_503]` `[trigger: parched_landscape]` `[factor_trigger: tarot_knight_cups AND symbol_parched_land]` `[role: 条件分支]` Parched landscape with narrow river—imagination starving for want of real engagement; the dreamer's inner world rich while outer world withers from neglect. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Cups: Romantic Dreamer"
    factor_refs: list = ['quality', 'existing', 'temperament', 'existing', 'defense', 'existing', 'possibility', 'existing', 'conflict', 'existing']
    
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
        l1_anchor="pt_v1.0.0_knight_of_cups__romantic_dream_001_L1",
    )
    version: str = "1.0.0"
