"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995001
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
    semantic_id="pt_v1.0.0_knight_of_swords__charging_int_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KnightOfSwordsChargingInt(SemanticEntry):
    """
    **Visual Elements**:
- Knight charging forward at full speed
- Sword held high
- Horse galloping rap...
    """
    
    original_text: str = """**Visual Elements**:
- Knight charging forward at full speed
- Sword held high
- Horse galloping rapidly
- Stormy, turbulent sky
- Aggressive, forceful energy

**English Paraphrase**:

The **Knight of Swords** represents **Air at its most extreme** - intellectual force charging ahead without caution. This is **thought as weapon**, ideas pursued with aggressive certainty. Knights are extremists; this one attacks with **mind and words**, sometimes brilliant, sometimes destructive.

**Core Symbolism**:
- **Charging horse**: Unrestrained mental force
- **Raised sword**: Ideas as weapons, words that cut
- **Speed**: Quick thinking, rapid conclusions
- **Stormy sky**: Conflict, turmoil, unstable conditions

**Upright Meaning**:
- **Intellectual aggression**: Attacking problems/people with logic
- **Forceful truth**: Speaking bluntly, sometimes cruelly
- **Quick decisions**: Rushing to conclusions without full information
- **Brilliant but reckless**: Smart but lacks wisdom
- **Verbal combat**: Arguments, debates, using words to wound
- **Courage to act**: Willing to take mental/social risks

**Reversed/Challenged**:
- **Scattered thinking**: Many ideas, no follow-through
- **Cruelty**: Intelligence used to harm
- **Impulsive speech**: Saying things later regretted
- **Mental tyranny**: Using logic to dominate
- **Blocked action**: Energy frustrated, leading to anger

**完整中文诠释**:
**宝剑骑士**=**风之最极端**——智力力量不顾谨慎向前冲锋。这是**思想作武器**，以激进确定性追求想法。骑士是极端分子；此位以**心智与语言**攻击，有时辉煌有时毁灭。**图像元素**：**冲锋的马**=无约束的心智力量；**高举的剑**=想法作武器，切割的话语；**速度**=快速思考，快速结论；**暴风天**=冲突、动荡、不稳条件。**正位含义**：**智力攻击**（用逻辑攻击问题/人），**强力真理**（直言不讳，有时残忍），**快速决定**（在没有完整信息时匆忙下结论），**聪明但鲁莽**（有智慧但缺乏智慧），**言语战斗**（争论、辩论、用话语伤害），**行动勇气**（愿意承担心智/社交风险）。**逆位/挑战**：**分散思考**（许多想法，无后续），**残忍**（智力被用来伤害），**冲动言语**（说出后悔的话），**心智暴政**（用逻辑统治），**阻塞行动**（能量受挫，导致愤怒）。**人格类型**：**辩论家**、**活动家**、**智力战士**。可以是真理的激励倡导者或话语的残忍使用者。代表风之礼物（清晰、勇气）与危险（残忍、鲁莽）。

**Personality Type**: The **debater**, **activist**, **intellectual warrior**. Can be inspiring advocate for truth or cruel wielder of words. Represents Air's gift (clarity, courage) and danger (cruelty, recklessness).

**Narrative Snippets**:
- `[ns_78deg_274]` `[trigger: knight_swords_charge]` `[factor_trigger: tarot_knight_swords AND state_intellectual_aggression]` `[role: 主干]` Knight of Swords represents Air at its most extreme—intellectual force charging ahead without caution; thought as weapon, ideas pursued with aggressive certainty. → English Paraphrase
- `[ns_78deg_275]` `[trigger: charging_horse_sword]` `[factor_trigger: tarot_knight_swords AND symbol_charging_horse]` `[role: 主干依赖]` Charging horse with raised sword beneath stormy sky—unrestrained mental force, rapid conclusions, conflict and turmoil; knight as extremist. → Core Symbolism
- `[ns_78deg_276]` `[trigger: knight_swords_combat]` `[factor_trigger: tarot_knight_swords AND state_verbal_combat]` `[role: 条件分支]` Verbal combat—arguments, debates, using words to wound; forceful truth spoken bluntly, sometimes cruelly; quick decisions without full information. → Upright Meaning
- `[ns_78deg_277]` `[trigger: knight_swords_reversed]` `[factor_trigger: tarot_knight_swords AND polarity_reversed]` `[role: 例外处理]` Reversed: scattered thinking, no follow-through; cruelty using intelligence to harm; impulsive speech later regretted; mental tyranny dominating through logic. → Reversed Meaning
- `[ns_78deg_278]` `[trigger: intellectual_warrior]` `[factor_trigger: tarot_knight_swords AND archetype_warrior]` `[role: 总结]` Personality type: debater, activist, intellectual warrior—inspiring advocate for truth or cruel wielder of words; Air's gift (clarity, courage) and danger (cruelty, recklessness). → Personality Type
- `[ns_78deg_414]` `[trigger: stormy_sky_knight]` `[factor_trigger: tarot_knight_swords AND symbol_stormy_sky]` `[role: 条件分支]` Stormy, turbulent sky—conflict, turmoil, unstable conditions; the environment matches the energy; charging through chaos with certainty. → Visual Elements
- `[ns_78deg_415]` `[trigger: brilliant_reckless]` `[factor_trigger: tarot_knight_swords AND state_brilliant_reckless]` `[role: 条件分支]` Brilliant but reckless—smart but lacks wisdom; courage to act and take mental risks, but may destroy what could have been built with patience. → Upright Meaning
- `[ns_78deg_484]` `[trigger: words_that_cut]` `[factor_trigger: tarot_knight_swords AND principle_verbal_weapon]` `[role: 条件分支]` Sword held high as words that cut—intellect used as blade; speaking truths that wound even when accurate; fire of knights combined with air's sharpness creates dangerous intensity. → Core Symbolism
- `[ns_78deg_528]` `[trigger: quick_conclusions]` `[factor_trigger: tarot_knight_swords AND state_rapid_thinking]` `[role: 条件分支]` Quick thinking, rapid conclusions—speed as virtue when accuracy suffers; rushing to judgment without full information; brilliant insight or reckless error. → Upright Meaning
- `[ns_78deg_529]` `[trigger: unrestrained_force]` `[factor_trigger: tarot_knight_swords AND state_mental_force]` `[role: 条件分支]` Charging horse as unrestrained mental force—thought without brake, ideas as cavalry assault; the debate won by overwhelming rather than persuading. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Swords: Charging Intellect"
    factor_refs: list = ['force', 'existing', 'action', 'existing', 'quality', 'existing', 'expression', 'existing', 'pitfall', 'existing']
    
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
        l1_anchor="pt_v1.0.0_knight_of_swords__charging_int_001_L1",
    )
    version: str = "1.0.0"
