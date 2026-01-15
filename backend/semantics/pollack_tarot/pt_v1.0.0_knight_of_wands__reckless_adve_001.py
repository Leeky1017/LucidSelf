"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994787
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
    semantic_id="pt_v1.0.0_knight_of_wands__reckless_adve_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KnightOfWandsRecklessAdve(SemanticEntry):
    """
    **Visual Elements**:
- Knight on rearing horse
- Rapid motion, dynamic energy
- Wand held high
- Sal...
    """
    
    original_text: str = """**Visual Elements**:
- Knight on rearing horse
- Rapid motion, dynamic energy
- Wand held high
- Salamanders on armor
- Desert landscape

**English Paraphrase**:

The **Knight of Wands** represents **fire energy in extreme motion** - impulsive, passionate, seeking adventure and challenge. Knights are **questers and extremists**, taking the element to its furthest expression. This Knight **charges ahead without looking**.

**Core Symbolism**:
- **Rearing horse**: Barely controlled energy, ready to bolt
- **Rapid motion**: Action without reflection
- **Wand held high**: Banner of enthusiasm, declaration of intent
- **Armor with salamanders**: Protected by fire element itself

**Upright Meaning**:
- **Impulsive action**: Leaping before looking, acting on inspiration
- **Passionate pursuit**: Single-minded focus on goal or desire
- **Adventure seeking**: Craves excitement, novelty, challenge
- **Sexual passion**: Direct, enthusiastic physical attraction
- **Recklessness**: Ignores consequences in pursuit of thrill
- **Inspiring energy**: Others swept up in his momentum

**Reversed/Challenged**:
- **Scattered energy**: Starting many things, finishing none
- **Destructive impulsiveness**: Recklessness causes real damage
- **Frustrated action**: Energy blocked, leading to anger
- **Burnout**: Constant motion exhausts reserves
- **False confidence**: Bravado masking fear or uncertainty

**完整中文诠释**:
**权杖骑士**=**极端运动中的火能量**——冲动、热情、寻求冒险与挑战。骑士是**追寻者与极端分子**，将元素发挥至极致。向前冲不看路。**图像元素**：**跃起的马**=勉强控制的能量准备狂奔；**快速移动**=无反思行动；**高举权杖**=热情旗帜，意图宣言；**火蜥蜴装饰盔甲**=火元素本身作为保护。**正位含义**：**冲动行动**（不考虑后果立即行动），**激情追求**（全情投入目标），**寻求冒险**（渴望刺激、新奇、挑战），**性激情**（直接、热情的肉体吸引），**鲁莽**（追求刺激时忽略后果），**激励能量**（他人被其动力卷入）。**逆位/挑战**：**分散能量**（开始许多事，完成无一），**破坏性冲动**（鲁莽造成真实伤害），**受挫行动**（能量被阻，导致愤怒），**倦怠**（持续运动耗尽储备），**虚假自信**（虚张声势掩盖恐惧或不确定）。**人格类型**：**冒险家**、**企业家**、**寻求刺激者**。生活在持续运动中，需要新经验和挑战。可以激励人但也令人疲惫。代表火之礼物（活力）与危险（倦怠）。

**Personality Type**: The **adventurer**, **entrepreneur**, **thrill-seeker**. Lives in constant motion, needs new experiences and challenges. Can be inspiring but exhausting. Represents fire's gift (vitality) and danger (burnout).

**Narrative Snippets**:
- `[ns_78deg_203]` `[trigger: knight_wands_motion]` `[factor_trigger: tarot_knight_wands AND state_extreme_motion]` `[role: 主干]` Knight of Wands represents fire energy in extreme motion—impulsive, passionate, charging ahead without looking; the quester who takes fire to its furthest expression. → English Paraphrase
- `[ns_78deg_204]` `[trigger: rearing_horse]` `[factor_trigger: tarot_knight_wands AND symbol_rearing_horse]` `[role: 主干依赖]` Rearing horse barely controlled, ready to bolt—energy scarcely contained, action faster than thought; the banner of enthusiasm held high. → Core Symbolism
- `[ns_78deg_205]` `[trigger: knight_wands_adventure]` `[factor_trigger: tarot_knight_wands AND state_adventure_seeking]` `[role: 条件分支]` Adventure seeking, craving excitement, novelty, challenge—single-minded passionate pursuit; others swept up in his contagious momentum. → Upright Meaning
- `[ns_78deg_206]` `[trigger: knight_wands_sexual]` `[factor_trigger: tarot_knight_wands AND state_sexual_passion]` `[role: 条件分支]` Sexual passion direct and enthusiastic—physical attraction acted upon immediately; fire expressed through the body without hesitation. → Upright Meaning
- `[ns_78deg_207]` `[trigger: knight_wands_reversed]` `[factor_trigger: tarot_knight_wands AND polarity_reversed]` `[role: 例外处理]` Reversed: scattered energy starting many things finishing none; destructive impulsiveness causing real damage; burnout from constant motion. → Reversed Meaning
- `[ns_78deg_208]` `[trigger: fire_gift_danger]` `[factor_trigger: tarot_knight_wands AND polarity_dual]` `[role: 总结]` Represents fire's gift (vitality, inspiration) and danger (burnout, recklessness)—the adventurer, entrepreneur, thrill-seeker living in constant motion. → Personality Type
- `[ns_78deg_518]` `[trigger: salamander_armor]` `[factor_trigger: tarot_knight_wands AND symbol_salamander_armor]` `[role: 条件分支]` Salamanders on armor—protected by fire element itself; the one who lives in flames cannot be burned; recklessness as its own shield. → Visual Elements
- `[ns_78deg_519]` `[trigger: wand_banner]` `[factor_trigger: tarot_knight_wands AND symbol_wand_banner]` `[role: 条件分支]` Wand held high like banner—declaration of intent, enthusiasm as flag; announcing arrival before strategically wise; the herald of action. → Core Symbolism
- `[ns_78deg_520]` `[trigger: leap_before_look]` `[factor_trigger: tarot_knight_wands AND principle_impulsiveness]` `[role: 条件分支]` Leaping before looking—acting on inspiration without reflection; the wisdom of foolishness when overthinking kills momentum; sometimes only way forward is through. → Upright Meaning
- `[ns_78deg_521]` `[trigger: contagious_momentum]` `[factor_trigger: tarot_knight_wands AND state_inspiring]` `[role: 条件分支]` Others swept up in his momentum—contagious enthusiasm that moves groups; fire spreads by nature; one spark ignites many; the leader who creates followers through sheer energy. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Wands: Reckless Adventure"
    factor_refs: list = ['state', 'existing', 'behavior', 'existing', 'drive', 'existing', 'quality', 'existing', 'shadow', 'existing']
    
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
        l1_anchor="pt_v1.0.0_knight_of_wands__reckless_adve_001_L1",
    )
    version: str = "1.0.0"
