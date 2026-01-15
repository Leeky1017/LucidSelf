"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439604
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
    semantic_id="dvd_v1.0.0_alien_外星人_异类_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Alien外星人异类(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: 
> 1. People that are strange or foreign to you.
> 2. When y...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: 
> 1. People that are strange or foreign to you.
> 2. When you are foreign or on the outside looking in.
> 3. Monsters or creatures that are demonic in nature.

**Dreams - Positive**: If you are the alien in your dreams, or if you feel on the outside looking in, then the Lord has separated you from others. You will not be as them for you are called out, 'separated' and set apart for His work. If you dream that you are overcoming monsters or aliens, it indicates that you are gaining a victory in your life.

**Dreams - Negative**: Speaks of the works of the enemy, of deception; of things appearing different to what they really are. If you keep dreaming of monsters, aliens or other strange creatures, consider what you are feeding into your spirit (movies, media).

**Internal Prophetic Dream**: "I am become a stranger to my brothers, and an alien to my mother's children." (Psalm 69:8) — You are feeling an outcast, alienated from others.

**Visions - Positive**: Anyone who is called to the fivefold ministry is separated just as Apostle Paul was. To see someone set apart is an indication of a ministry calling.

**See also**: Demons

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Alien | Foreign/strange being | Separation, otherness |
| Separated | Set apart by God | Ministry calling |
| Monsters | Demonic creatures | Enemy's work |

### English Paraphrase

"Alien" in dreams has three meanings: (1) foreign/strange people, (2) being an outsider looking in, (3) demonic creatures. Positively: being the alien means God has separated you—you're called out, set apart for His work. Overcoming aliens/monsters indicates gaining victory. Negatively: represents enemy's work, deception, things appearing different than they are. If recurring, examine what you're feeding your spirit (media input). In visions, seeing someone set apart indicates a ministry calling (like Paul's separation).

### Chinese Interpretation（完整对等诠释）

「外星人」在梦中有三层含义：(1) 陌生/外来的人，(2) 作为局外人向内看，(3) 魔鬼性质的生物。正面：自己是外星人意味着神已将你分别出来——你被呼召、为祂的工作分别为圣。战胜外星人/怪物表示在生命中得胜。负面：代表仇敌的工作、欺骗、事物与真相不符。若反复出现，检查你在喂养灵魂什么（媒体输入）。在异象中，看到某人被分别出来表示事工呼召（如保罗的分别）。

### Core Points

- 外星人 = 分别/异类的象征
- 正面：神的分别为圣、事工呼召
- 战胜外星人 = 属灵得胜
- 负面：仇敌工作、欺骗
- 反复梦见 → 检查媒体/灵粮输入
- 诗篇69:8：感觉被排斥、疏离

### Narrative Snippets

- `[ns_dav_a007]` `[trigger: 梦外星人]` `[factor_trigger: dream_symbol_alien AND separation_state]` `[role: 主干]` Alien = separation symbolism—either God's setting apart or demonic deception. → Dreams Dictionary #Alien
- `[ns_dav_a008]` `[trigger: 自己是外星人]` `[factor_trigger: dream_symbol_alien AND dream_self]` `[role: 条件分支]` Being the alien = God has separated you, called out, set apart for His work. → Dreams Dictionary #Alien
- `[ns_dav_a009]` `[trigger: 战胜外星人]` `[factor_trigger: dream_symbol_alien AND dream_victory AND combat_outcome]` `[role: 条件分支]` Overcoming aliens/monsters = gaining victory in your life. → Dreams Dictionary #Alien
- `[ns_dav_a010]` `[trigger: 反复梦怪物]` `[factor_trigger: dream_symbol_alien AND dream_recurring]` `[role: 总结]` Recurring monster dreams = check what you're feeding your spirit (media input). → Dreams Dictionary #Alien"""
    normalized_text_zh: str = """"""
    subject: str = "Alien 外星人/异类"
    factor_refs: list = ['dream_symbol_alien', 'concept_separated', 'dream_symbol_monster']
    
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_alien_外星人_异类_001_L1",
    )
    version: str = "1.0.0"
