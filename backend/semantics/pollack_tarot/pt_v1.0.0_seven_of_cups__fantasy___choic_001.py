"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994901
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
    semantic_id="pt_v1.0.0_seven_of_cups__fantasy___choic_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class SevenOfCupsFantasyChoic(SemanticEntry):
    """
    **Visual Elements**:
- Silhouette figure facing seven cups in clouds
- Each cup contains different i...
    """
    
    original_text: str = """**Visual Elements**:
- Silhouette figure facing seven cups in clouds
- Each cup contains different image: jewels, victory wreath, dragon, castle, glowing figure, snake, veiled face
- Dreamlike, ungrounded composition

**English Paraphrase**:

The **Seven of Cups** shows **the Cups problem in most direct form** - emotion and imagination produce wonderful visions, but **without grounding remain mere daydreams**. This represents **fancies vs genuine imagination** (Coleridge's distinction: fancy = ego fantasy; imagination = spiritual truth).

**Core Symbolism**:
- **Seven cups in clouds**: Ungrounded, disconnected from reality
- **Diverse visions**: Wealth (jewels), victory (wreath), fear (dragon), adventure (castle), archetypes (godlike face, radiant figure, snake)
- **Silhouette figure**: Lost in fantasy, not engaged with real world
- **Full spectrum**: From material to spiritual fantasies, all equally unmanifested

**Upright Meaning**:
- **Too many choices**: Paralyzed by options, cannot commit
- **Daydreams**: Fantasies disconnected from action
- **Illusion**: Mistaking imagination for reality
- **Escapism**: Using fantasy to avoid current life
- **Archetypal content**: Even meaningful symbols lack value if not grounded
- **Wishful thinking**: Desire without will to manifest

**Reversed/Challenged**:
- **Determination to act**: Making something real from dreams
- **Choosing wisely**: Selecting one path, committing
- **Grounding fantasy**: Connecting vision to reality
- **Disillusionment**: (negative) Fantasy shattered painfully

**完整中文诠释**:
**圣杯七**显示**圣杯问题最直接形式**——情感与想象产生美妙愿景，但**无接地仍为白日梦**。代表**幻想vs真想象力**（柯尔律治区分：幻想=自我幻觉；想象力=灵性真理）。**图像元素**：**云中七杯**=未接地，与现实脱节；**多样愿景**=财富（珠宝）、胜利（花环）、恐惧（龙）、冒险（城堡）、原型（神脸、光辉人形、蛇）；**剪影人物**=迷失幻想，未与真实世界参与。**正位含义**：**选择太多**（被可能性淹没），**白日梦**（幻想取代行动），**幻觉**（看到不真实），**逃避主义**（用幻想逃避现实），**原型内容**（深层心理图像），**一厢情愿**（希望变成信念）。**逆位/挑战**：**决心行动**（选择一条路并行动），**明智选择**（区分真实与幻觉），**接地幻想**（将愿景付诸实践），**幻灭破灭**（面对现实，痛苦但必要）。

**Key Distinction**: Content doesn't determine if fantasy is meaningful - **archetypes** (snake, radiant figure) can be as ungrounded as material desires (jewels). **Connection to action** is what matters.

**Narrative Snippets**:
- `[ns_78deg_245]` `[trigger: seven_cups_fantasy]` `[factor_trigger: tarot_seven_cups AND state_fantasy]` `[role: 主干]` Seven of Cups shows the Cups problem most directly—emotion and imagination produce wonderful visions, but without grounding remain mere daydreams. → English Paraphrase
- `[ns_78deg_246]` `[trigger: cups_in_clouds]` `[factor_trigger: tarot_seven_cups AND symbol_clouds]` `[role: 主干依赖]` Seven cups floating in clouds—ungrounded, disconnected from reality; silhouette figure lost in fantasy, not engaged with real world. → Core Symbolism
- `[ns_78deg_247]` `[trigger: seven_cups_choices]` `[factor_trigger: tarot_seven_cups AND state_choice_paralysis]` `[role: 条件分支]` Too many choices—paralyzed by options, cannot commit; wishful thinking mistaking imagination for reality, desire without will to manifest. → Upright Meaning
- `[ns_78deg_248]` `[trigger: fancy_vs_imagination]` `[factor_trigger: tarot_seven_cups AND principle_coleridge_distinction]` `[role: 条件分支]` Coleridge's distinction: fancy = ego fantasy; imagination = spiritual truth—even archetypal symbols (snake, radiant figure) lack value if not grounded. → Key Distinction
- `[ns_78deg_249]` `[trigger: seven_cups_reversed]` `[factor_trigger: tarot_seven_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: determination to act—making something real from dreams; choosing wisely, committing to one path; or painful disillusionment. → Reversed Meaning
- `[ns_78deg_250]` `[trigger: grounding_fantasy]` `[factor_trigger: tarot_seven_cups AND principle_grounding]` `[role: 总结]` Content doesn't determine meaningfulness—archetypes can be as ungrounded as material desires; connection to action is what matters. → Key Distinction
- `[ns_78deg_450]` `[trigger: diverse_visions]` `[factor_trigger: tarot_seven_cups AND symbol_diverse_visions]` `[role: 条件分支]` Diverse visions in cups—jewels (wealth), wreath (victory), dragon (fear), castle (adventure), godlike face, radiant figure, snake; full spectrum from material to spiritual, all equally unmanifested. → Core Symbolism
- `[ns_78deg_451]` `[trigger: silhouette_lost]` `[factor_trigger: tarot_seven_cups AND symbol_silhouette]` `[role: 条件分支]` Silhouette figure facing cups in clouds—lost in fantasy, not engaged with real world; wishful thinking mistaking imagination for reality; desire without will to manifest. → Visual Elements
- `[ns_78deg_499]` `[trigger: escapism_trap]` `[factor_trigger: tarot_seven_cups AND state_escapism]` `[role: 条件分支]` Escapism using fantasy to avoid current life—the dreamer who never wakes; all visions equally valueless until one is chosen and grounded through action. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Cups: Fantasy & Choices"
    factor_refs: list = ['problem', 'existing', 'state', 'existing', 'defense', 'existing', 'distinction', 'existing', 'pitfall', 'existing']
    
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
        l1_anchor="pt_v1.0.0_seven_of_cups__fantasy___choic_001_L1",
    )
    version: str = "1.0.0"
