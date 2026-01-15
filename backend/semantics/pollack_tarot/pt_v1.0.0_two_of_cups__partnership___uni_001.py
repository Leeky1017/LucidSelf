"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994868
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
    semantic_id="pt_v1.0.0_two_of_cups__partnership___uni_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class TwoOfCupsPartnershipUni(SemanticEntry):
    """
    **Visual Elements**:
- Man and woman facing each other, raising cups
- Winged lion's head above cadu...
    """
    
    original_text: str = """**Visual Elements**:
- Man and woman facing each other, raising cups
- Winged lion's head above caduceus (Hermes staff)
- Pledging, ceremonial gesture
- Equal standing, mutual regard

**English Paraphrase**:

The **Two of Cups** represents **partnership, union, and mutual commitment** - often the beginning of love or deep friendship. This is a "lesser Lovers" - where the Major Arcana trump shows mature sexual union blessed by divine, this Minor card emphasizes **pledging and beginning**.

**Core Symbolism**:
- **Two figures**: Equality, mutual choice, balanced partnership
- **Winged lion over caduceus**: Sexuality (lion) elevated by Spirit (wings), healing through love (Hermes symbol)
- **Raising cups**: Toast, pledge, commitment ceremony
- **Man/woman**: Can represent inner masculine (action) + feminine (emotion) united

**Upright Meaning**:
- **New relationship**: Beginning of love affair or deep friendship
- **Partnership**: Mutual commitment, equal standing
- **Unity of opposites**: Action + emotion, technical + spiritual
- **Healing connection**: Relationship that makes both whole
- **Creative collaboration**: Two creating more together than alone
- **Inner integration**: Masculine and feminine aspects of self united

**Reversed/Challenged**:
- **Relationship breakdown**: Trust violated, jealousy emerges
- **End of partnership**: Separation, divorce, friendship lost
- **Infatuation**: Pretending relationship means more than it does
- **Going through motions**: One or both not truly engaged
- **Inner split**: What we do vs what we feel disconnected

**完整中文诠释**:
**圣杯二**=**伙伴关系、结合、相互承诺**——常为爱或深厚友谊之开始。"**小恋人**"——大阿卡纳显示神祝福的成熟性结合，小阿卡纳强调**誓约与开始**。**图像元素**：**两人**=平等，相互选择，均衡伙伴；**翅膀狮子于蛇杖**=性欲（狮子）被灵性（翅膀）提升，通过爱治愈（赫尔墨斯象征）；**举杯**=敬酒，誓约，承诺仪式。**正位含义**：**新关系**（爱情或友谊开始），**伙伴**（平等合作），**对立统一**（阴阳结合），**治愈连接**（通过关系疗愈），**创意合作**（共同创造），**内在整合**（内在阴阳整合）。**逆位/挑战**：**关系破裂**（伙伴结束），**终结伙伴**（分离），**迷恋**（非真爱），**走过场**（表面承诺无深度），**内在分裂**（内在对立未整合）。

**Psychological Layer**: **Union creates something beyond individual** - together producing what neither could alone. As inner diagram: action (man/Fool energy) + emotion/sensitivity (woman) = whole person.

**Narrative Snippets**:
- `[ns_78deg_239]` `[trigger: two_cups_union]` `[factor_trigger: tarot_two_cups AND state_partnership]` `[role: 主干]` Two of Cups represents partnership, union, mutual commitment—the beginning of love or deep friendship; a "lesser Lovers" emphasizing pledging and beginning. → English Paraphrase
- `[ns_78deg_240]` `[trigger: winged_lion_caduceus]` `[factor_trigger: tarot_two_cups AND symbol_winged_lion AND symbol_caduceus]` `[role: 主干依赖]` Winged lion over caduceus—sexuality (lion) elevated by Spirit (wings), healing through love (Hermes symbol); sacred union. → Core Symbolism
- `[ns_78deg_241]` `[trigger: two_cups_equality]` `[factor_trigger: tarot_two_cups AND state_equality]` `[role: 条件分支]` Two figures raising cups in toast—equality, mutual choice, balanced partnership; commitment ceremony where both stand as equals. → Core Symbolism
- `[ns_78deg_242]` `[trigger: two_cups_integration]` `[factor_trigger: tarot_two_cups AND state_inner_integration]` `[role: 条件分支]` Unity of opposites—action and emotion, masculine and feminine united; relationship creating more together than either could alone. → Upright Meaning
- `[ns_78deg_243]` `[trigger: two_cups_reversed]` `[factor_trigger: tarot_two_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: relationship breakdown, trust violated; infatuation pretending depth; inner split—what we do disconnected from what we feel. → Reversed Meaning
- `[ns_78deg_244]` `[trigger: union_beyond_individual]` `[factor_trigger: tarot_two_cups AND principle_synergy]` `[role: 总结]` Union creates something beyond individual—together producing what neither could alone; action + emotion/sensitivity = whole person. → Psychological Layer
- `[ns_78deg_438]` `[trigger: lesser_lovers]` `[factor_trigger: tarot_two_cups AND tarot_major_lovers]` `[role: 条件分支]` A "lesser Lovers"—Major Arcana shows mature sexual union blessed by divine; Minor card emphasizes pledging and beginning, the first steps of union. → Core Symbolism
- `[ns_78deg_439]` `[trigger: healing_connection]` `[factor_trigger: tarot_two_cups AND function_healing]` `[role: 条件分支]` Healing connection—relationship that makes both whole; creative collaboration producing what neither could alone; caduceus healing through love. → Upright Meaning
- `[ns_78deg_497]` `[trigger: ceremonial_pledge]` `[factor_trigger: tarot_two_cups AND symbol_pledge]` `[role: 条件分支]` Raising cups in ceremonial gesture—the moment of choice made visible; commitment spoken aloud transforms intention into covenant; the pledge as creative act. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Cups: Partnership & Union"
    factor_refs: list = ['relationship', 'existing', 'quality', 'existing', 'function', 'existing', 'process', 'existing', 'bond', 'existing']
    
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
        l1_anchor="pt_v1.0.0_two_of_cups__partnership___uni_001_L1",
    )
    version: str = "1.0.0"
