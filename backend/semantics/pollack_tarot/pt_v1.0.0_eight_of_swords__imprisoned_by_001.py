"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994975
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
    semantic_id="pt_v1.0.0_eight_of_swords__imprisoned_by_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class EightOfSwordsImprisonedBy(SemanticEntry):
    """
    **Visual Elements**:
- Blindfolded woman surrounded by eight swords
- Ropes binding arms but not leg...
    """
    
    original_text: str = """**Visual Elements**:
- Blindfolded woman surrounded by eight swords
- Ropes binding arms but not legs
- Standing in mud
- Castle in background (authority)
- Swords don't actually fence her in
- No captors visible

**English Paraphrase**:

The **Eight of Swords** represents **oppression through confusion and false beliefs** - being imprisoned not by force but by **training to believe in own helplessness**. The blindfold symbolizes **mystification**: keeping people down by making them think they cannot leave, when nothing actually prevents escape.

**Core Symbolism**:
- **Blindfold**: Confusion, oppressive ideas, inability to see options
- **Loose ropes**: Not actually bound, could walk away
- **Swords not fencing**: No real barrier, only perceived ones
- **No captors**: Self-imprisonment, internalized oppression
- **Mud**: Humiliation, shame, feeling degraded
- **Castle**: Authority that intimidates but may be distant

**Upright Meaning**:
- **Self-imposed limitation**: Believing you're more trapped than you are
- **Victim mentality**: Trained helplessness, political oppression
- **Confusion**: Cannot see way out, overwhelmed by options
- **Shame**: Deep hidden feelings preventing action
- **Isolation**: Cut off from others in similar situations
- **Gate to Ignorance**: Recognition of not knowing (spiritual paradox)

**Reversed/Challenged**:
- **Liberation begins**: Removing blindfold, seeing clearly
- **Understanding situation**: What you did, others did, what's possible now
- **First step of freedom**: Clarity precedes action
- **Throwing off conditioning**: Breaking free from imposed beliefs

**完整中文诠释**:
**宝剑八**=通过困惑与虚假信念的**压迫**——非通过武力而是通过**训练相信自身无助**而被囚禁。眼罩象征**神秘化**：通过让人认为无法离开而压制，而实际无物阻止逃脱。**图像元素**：**眼罩**=困惑，压迫性想法，无法看到选择；**松散绳索**=实际未被绑住，可以走开；**剑未围栏**=无真实障碍，仅有感知的；**无看守者**=自我囚禁，内化的压迫；**泥泞**=羞辱、羞耻、感觉被贬低；**远处城堡**=威吓的权威但可能遥远。**正位含义**：**自我施加限制**（相信你比实际更被困），**受害者心态**（训练的无助，政治压迫），**困惑**（看不到出路，被选择淹没），**羞耻**（深藏的感受阻止行动），**孤立**（与类似处境的他人隔绝），**通向无知之门**（承认不知是第一步，灵性悖论）。**逆位/挑战**：**解放开始**（移除眼罩，清晰看见），**理解情况**（你做了什么，他人做了什么，现在可能什么），**自由第一步**（清晰先于行动），**甩掉调制**（打破强加的信念）。**政治/灵性层面**：**政治**：被压迫状态的图解——神秘化使人屈服。**灵性**：门户牌——承认无知是通向真知的第一步（最难的）。悖论：智力上知道但不接受我们在开悟前无法真正知晓。

**Political/Spiritual Layers**: **Political**: Diagram of oppressed condition - mystification keeps people down. **Spiritual**: Gate card - recognizing ignorance is first (hardest) step to true knowledge. Paradox: intellectually know but don't accept we cannot truly know without enlightenment.

**Narrative Snippets**:
- `[ns_78deg_328]` `[trigger: eight_swords_prison]` `[factor_trigger: tarot_eight_swords AND state_imprisoned]` `[role: 主干]` Eight of Swords represents oppression through confusion and false beliefs—imprisoned not by force but by training to believe in own helplessness; nothing actually prevents escape. → English Paraphrase
- `[ns_78deg_329]` `[trigger: blindfold_mystification]` `[factor_trigger: tarot_eight_swords AND symbol_blindfold]` `[role: 主干依赖]` Blindfold symbolizes mystification—keeping people down by making them think they cannot leave; loose ropes not actually bound, swords don't actually fence her in, no captors visible. → Core Symbolism
- `[ns_78deg_330]` `[trigger: self_imprisonment]` `[factor_trigger: tarot_eight_swords AND state_self_limitation]` `[role: 条件分支]` Self-imposed limitation—believing you're more trapped than you are; victim mentality, trained helplessness; confusion preventing sight of way out. → Upright Meaning
- `[ns_78deg_331]` `[trigger: eight_swords_reversed]` `[factor_trigger: tarot_eight_swords AND polarity_reversed]` `[role: 例外处理]` Reversed: liberation begins by removing blindfold, seeing clearly; understanding situation—what you did, what others did, what's possible now; clarity precedes action. → Reversed Meaning
- `[ns_78deg_332]` `[trigger: gate_ignorance]` `[factor_trigger: tarot_eight_swords AND principle_gate_card]` `[role: 条件分支]` Gate card—recognizing ignorance is first (hardest) step to true knowledge; paradox: intellectually know but don't accept we cannot truly know without enlightenment. → Political/Spiritual Layers
- `[ns_78deg_333]` `[trigger: political_oppression]` `[factor_trigger: tarot_eight_swords AND principle_mystification]` `[role: 总结]` Political diagram of oppressed condition—mystification keeps people down; internalized oppression becomes self-imprisonment; breaking free requires seeing through trained beliefs. → Political/Spiritual Layers
- `[ns_78deg_456]` `[trigger: mud_shame]` `[factor_trigger: tarot_eight_swords AND symbol_mud]` `[role: 条件分支]` Standing in mud—humiliation, shame, feeling degraded; deep hidden feelings preventing action; the weight of unworthiness keeping one stuck in place. → Core Symbolism
- `[ns_78deg_457]` `[trigger: distant_castle]` `[factor_trigger: tarot_eight_swords AND symbol_castle]` `[role: 条件分支]` Castle in background—authority that intimidates but may be distant; the oppressive power may be less present than imagined; isolation from support systems. → Core Symbolism
- `[ns_78deg_500]` `[trigger: invisible_captors]` `[factor_trigger: tarot_eight_swords AND principle_invisible_oppression]` `[role: 条件分支]` No captors visible—the oppressor has been internalized; the prison guard is now inside the mind; liberation requires confronting one's own trained beliefs. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Swords: Imprisoned by Beliefs"
    factor_refs: list = ['limitation', 'existing', 'oppression', 'existing', 'condition', 'existing', 'breakthrough', 'existing', 'paradox', 'existing']
    
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
        l1_anchor="pt_v1.0.0_eight_of_swords__imprisoned_by_001_L1",
    )
    version: str = "1.0.0"
