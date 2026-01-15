"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076493
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
    semantic_id="bot_v1.0.0_seven_of_swords__futility__宝剑七_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SevenOfSwordsFutility宝剑七(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Netzach in Air | Victory in Air | Modifying weakness |
| Moon in Aquarius | Passive lunar | Vacillation |
| Appeasement Policy | Compromise stance | Futile strategy |
| Six vs One | Many weak vs strong | Vain contest |

**Title**: Lord of Unstable Effort (不稳定努力之主)
**Qabalistic**: Netzach in Air (气中之胜利)
**Astrological**: Moon in Aquarius (月亮入宝瓶座)

**Source Text**:
> "Netzach, in the suit of Swords, does not represent such catastrophe as in the other suits, for Netzach, the Sephira of Venus, means victory. There is, therefore, a modifying influence; and this is accentuated by the celestial rule of the Moon in Aquarius. The intellectual wreckage of the card is thus not so vehement as in the Five. There is vacillation, a wish to compromise, a certain toleration. But, in certain circumstances, the results may be more disastrous than ever... This card, like the Four, suggests the policy of appeasement. The symbol shows six Swords with their hilts in crescent formation. Their points meet below the centre of the card, impinging upon a blade of a much larger up-thrusting sword, as if there were a contest between the many feeble and the one strong. He strives in vain."

**English Paraphrase**:
**Vacillating Weakness** – Netzach (Venus/Victory) in Air brings a **modifying influence**, not pure catastrophe. **Moon in Aquarius** adds passivity. The result: **vacillation, compromise, appeasement**. Six swords in crescent formation attack one large upthrusting sword—**many feeble against one strong**, striving in vain. This is **Futility**: well-meaning but weak efforts, policies of appeasement that invite predators.

**Core**: **Futile Effort** – Vacillation, appeasement, compromise that fails, weak against strong.

**Chinese Explanation**:
**宝剑七（徒劳）**对应气元素中的**Netzach（金星/胜利）**，带来调节性影响而非纯粹灾难。**月亮入宝瓶座**增添被动性。结果是：**犹豫、妥协、绥靖**。六把剑呈新月阵形攻击一把大型向上刺出的剑——**众弱对一强**，徒劳奋争。这是**徒劳**：善意但软弱的努力，招来掠夺者的绥靖政策。

**In Readings**: Futile efforts, vacillation, appeasement policies, weakness inviting defeat, compromise that backfires.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Seven of Swords shows Netzach's modifying influence. Moon in Aquarius brings passivity. Six feeble swords vs one strong. Appeasement policy reference. Contest ends in futility.
- **中文**: Crowley的宝剑七展示Netzach的调节性影响。月亮入宝瓶带来被动。六弱剑对一强剑。绥靖政策暗示。争斗以徒劳告终。

**Narrative Snippets**:
- `[ns_thoth_swords_019]` `[trigger: seven_swords_futility]` `[factor_trigger: thoth_swords_seven]` `[role: 主干]` Seven of Swords = Lord of Unstable Effort—Netzach modifies; vacillation, compromise, appeasement. → Core
- `[ns_thoth_swords_020]` `[trigger: moon_aquarius_passive]` `[factor_trigger: thoth_swords_seven AND planet_moon_aquarius]` `[role: 条件分支]` Moon in Aquarius—passive lunar; wish to compromise; results may be worse than direct conflict. → Astrological
- `[ns_thoth_swords_021]` `[trigger: six_vs_one]` `[factor_trigger: thoth_swords_seven AND symbol_swords_contest]` `[role: 条件分支]` Six crescent-formation swords vs one strong upthrusting sword—many feeble striving in vain. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Swords: Futility (宝剑七：徒劳)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_seven_001', 'tarot_wasted_effort', 'rel_swords_seven_002', 'tarot_invited_defeat', 'l1_anchor', 'confidence', 'evi_swords_seven_001', 'evi_swords_seven_002', 'tarot_appeasement', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_seven_001', 'tarot_swords_seven', 'astro_moon_aquarius']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_seven_of_swords__futility__宝剑七_001_L1",
    )
    version: str = "1.0.0"
