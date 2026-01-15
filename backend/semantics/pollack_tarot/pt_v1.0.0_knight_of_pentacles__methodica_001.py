"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995131
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
    semantic_id="pt_v1.0.0_knight_of_pentacles__methodica_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KnightOfPentaclesMethodica(SemanticEntry):
    """
    **Visual Elements**:
- Knight on stationary horse
- Holding pentacle, examining it
- Plowed field
- ...
    """
    
    original_text: str = """**Visual Elements**:
- Knight on stationary horse
- Holding pentacle, examining it
- Plowed field
- Slow, deliberate energy
- Solid, unmov演ing stance

**English Paraphrase**:

The **Knight of Pentacles** represents **Earth at extreme** - slow, methodical, utterly reliable but potentially **stuck**. Unlike other Knights (charging ahead), this Knight **barely moves** - dedicated to task but may lack vision or flexibility.

**Core Symbolism**:
- **Stationary horse**: Slowness, patience taken to extreme
- **Examining pentacle**: Focused on immediate task, not bigger picture
- **Plowed field**: Hard work accomplished, but repetitive
- **Solid stance**: Dependability, but also stubbornness

**Upright Meaning**:
- **Reliability**: Utterly dependable, will complete task
- **Hard work**: Dedicated, persistent effort
- **Methodical**: Step-by-step approach, careful planning
- **Patience**: Willingness to take time needed
- **Practical focus**: Concerned with tangible results
- **Lack of vision**: May miss forest for trees

**Reversed/Challenged**:
- **Stagnation**: Stuck in routine, refusing change
- **Laziness**: Slowness becomes inaction
- **Dullness**: Lost joy in work, mechanical
- **Obstinacy**: Stubbornly resists new approaches
- **Irresponsibility**: Fails to complete tasks

**完整中文诠释**:
**星币骑士**=**土之极端**——缓慢、有条不紊、极度可靠但可能**停滞**。不同于其他骑士（向前冲锋），此骑士**几乎不动**——专注任务但可能缺乏愿景或灵活性。**图像元素**：**静止的马**=缓慢耐心至极端；**审视星币**=专注眼前任务非更大图景；**犁过的田**=完成艰苦工作但重复；**稳固姿态**=可靠但也固执。**正位含义**：**可靠性**（绝对可靠，将完成任务），**艰苦工作**（专注、持续努力），**有条不紊**（逐步方法，仔细计划），**耐心**（愿意花所需时间），**实际专注**（关注有形结果），**缺乏愿景**（可能见树不见林）。**逆位/挑战**：**停滞**（困在例行中，拒绝改变），**懒惰**（缓慢变成不行动），**乏味**（失去工作中的喜悦，机械化），**固执**（顽固抵抗新方法），**不负责任**（未能完成任务）。**人格类型**：**可靠工人**、**专注工匠**、**有条不紊的计划者**。代表土之礼物（坚持、可靠）与危险（停滞、狭隘焦点）。

**Personality Type**: The **reliable worker**, **dedicated craftsperson**, **methodical planner**. Represents Earth's gift (persistence, dependability) and danger (stagnation, narrow focus).

**Narrative Snippets**:
- `[ns_78deg_306]` `[trigger: knight_pentacles_methodical]` `[factor_trigger: tarot_knight_pentacles AND state_methodical_progress]` `[role: 主干]` Knight of Pentacles represents Earth at its extreme—slow, methodical, utterly reliable but potentially stuck; unlike other Knights charging ahead, this one barely moves. → English Paraphrase
- `[ns_78deg_307]` `[trigger: stationary_horse]` `[factor_trigger: tarot_knight_pentacles AND symbol_stationary_horse]` `[role: 主干依赖]` Knight on stationary horse examining pentacle—slowness and patience taken to extreme; focused on immediate task not bigger picture; solid stance showing dependability but also stubbornness. → Core Symbolism
- `[ns_78deg_308]` `[trigger: knight_pentacles_reliable]` `[factor_trigger: tarot_knight_pentacles AND state_reliability]` `[role: 条件分支]` Utter reliability—will complete task; methodical step-by-step approach; patience willing to take time needed; practical focus on tangible results; but may lack vision and miss forest for trees. → Upright Meaning
- `[ns_78deg_309]` `[trigger: knight_pentacles_reversed]` `[factor_trigger: tarot_knight_pentacles AND polarity_reversed]` `[role: 例外处理]` Reversed: stagnation stuck in routine; laziness where slowness becomes inaction; dullness losing joy in work; obstinate resistance to new approaches; irresponsibility. → Reversed Meaning
- `[ns_78deg_310]` `[trigger: earth_extreme]` `[factor_trigger: tarot_knight_pentacles AND principle_earth_extreme]` `[role: 总结]` Reliable worker, dedicated craftsperson, methodical planner—represents Earth's gift (persistence, dependability) and danger (stagnation, narrow focus). → Personality Type
- `[ns_78deg_408]` `[trigger: plowed_field_knight]` `[factor_trigger: tarot_knight_pentacles AND symbol_plowed_field]` `[role: 条件分支]` Plowed field behind Knight—hard work accomplished but repetitive; dedication to task may miss larger vision; seeing trees not forest. → Visual Elements
- `[ns_78deg_409]` `[trigger: patience_extreme]` `[factor_trigger: tarot_knight_pentacles AND state_extreme_patience]` `[role: 条件分支]` Patience taken to extreme—willingness to take all time needed, but may become stubbornness; solid stance as virtue when flexibility needed is vice. → Upright Meaning
- `[ns_78deg_483]` `[trigger: examining_pentacle]` `[factor_trigger: tarot_knight_pentacles AND state_focused_examination]` `[role: 条件分支]` Examining pentacle closely—mastery through detailed attention; the craftsman who perfects through repetition; fire (knight energy) slowed by earth until barely flickering. → Core Symbolism
- `[ns_78deg_530]` `[trigger: step_by_step]` `[factor_trigger: tarot_knight_pentacles AND principle_methodical]` `[role: 条件分支]` Step-by-step approach, careful planning—patience willing to take time needed; practical focus on tangible results without rushing. → Upright Meaning
- `[ns_78deg_531]` `[trigger: solid_stance]` `[factor_trigger: tarot_knight_pentacles AND symbol_solid_stance]` `[role: 条件分支]` Solid, unmoving stance—dependability as virtue but also potential vice; the one who cannot be moved even when movement is needed. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Pentacles: Methodical Progress"
    factor_refs: list = ['quality', 'existing', 'action', 'existing', 'pitfall', 'existing', 'limitation', 'existing', 'virtue', 'existing']
    
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
        l1_anchor="pt_v1.0.0_knight_of_pentacles__methodica_001_L1",
    )
    version: str = "1.0.0"
