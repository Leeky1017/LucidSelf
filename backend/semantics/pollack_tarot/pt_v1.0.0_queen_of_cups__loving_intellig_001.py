"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994855
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
    semantic_id="pt_v1.0.0_queen_of_cups__loving_intellig_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class QueenOfCupsLovingIntellig(SemanticEntry):
    """
    **Visual Elements**:
- Queen on throne at water's edge
- Gazing intently at ornate cup
- Cup more el...
    """
    
    original_text: str = """**Visual Elements**:
- Queen on throne at water's edge
- Gazing intently at ornate cup
- Cup more elaborate than others (unique design)
- Feet not visible (grounded in water)
- Focused, purposeful presence

**English Paraphrase**:

The **Queen of Cups** represents **loving intelligence** - the union of emotion and consciousness. She knows what she wants and takes steps to achieve it, but always **with awareness of love**. Her gaze is fierce, not dreamy - she uses imagination as tool for creation.

**Core Symbolism**:
- **Ornate cup**: Imagination made into something concrete, shaped by will
- **Intense gaze**: Consciousness joined to feeling
- **Feet in water**: Grounded in emotional truth
- **Throne at shore**: Bridge between water (emotion) and land (action)

**Upright Meaning**:
- **Emotional maturity**: Deep feeling combined with wisdom
- **Psychic clarity**: Intuition directed with purpose
- **Creative realization**: Making vision real through love and will
- **Family/emotional goals**: Queen of the heart and home
- **Vision through love**: Seeing life's joy as gift, returning gift through creation
- **Empathy + action**: Caring combined with practical help

**Reversed/Challenged**:
- **Ambition without love**: Powerful but untrustworthy
- **Lost values**: Success pursued at cost of integrity
- **Emotional manipulation**: Uses feeling as weapon
- **Depravity**: Creative force out of control
- **Broken unity**: Vision separated from action

**完整中文诠释**:
**圣杯皇后**=**爱之智慧**——情感与意识结合。她知道所欲且采取步骤实现，但总是**带着爱之觉知**。凝视凶猛非梦幻——她用想象力作创造工具。**图像元素**：**精致的杯**=想象力化为具体物被意志塑形；**强烈凝视**=意识结合感受；**脚在水中**=扎根情感真理；**岸边王座**=水（情感）与陆地（行动）之桥。**正位含义**：**情感成熟**（理解并整合感受），**灵媒清晰**（直觉结合意识），**创造实现**（愿景成为现实），**家庭/情感目标**（通过爱达成），**通过爱之愿景**（想象力服务于爱），**同理+行动**（感受带来有效行动）。**逆位/挑战**：**野心无爱**（成就无心），**失去价值**（忘记什么重要），**情感操纵**（用感受控制他人），**堕落**（爱的能力被滥用），**破碎统一**（情感与意识分离）。

**In Readings**:
- Person: Emotionally mature, psychically gifted presence
- Quality: Unite feeling with conscious purpose
- Advice: Let love guide your creative action
- Situation: Time to manifest emotional vision into reality

**Narrative Snippets**:
- `[ns_78deg_233]` `[trigger: queen_cups_intelligence]` `[factor_trigger: tarot_queen_cups AND state_loving_intelligence]` `[role: 主干]` Queen of Cups represents loving intelligence—the union of emotion and consciousness; she knows what she wants and acts with awareness of love. → English Paraphrase
- `[ns_78deg_234]` `[trigger: ornate_cup]` `[factor_trigger: tarot_queen_cups AND symbol_ornate_cup]` `[role: 主干依赖]` Ornate cup unlike any other—imagination made concrete, shaped by will; her gaze is fierce not dreamy, using vision as tool for creation. → Core Symbolism
- `[ns_78deg_235]` `[trigger: feet_in_water]` `[factor_trigger: tarot_queen_cups AND symbol_feet_water]` `[role: 条件分支]` Feet hidden in water, throne at shore's edge—grounded in emotional truth while bridging water (feeling) to land (action). → Core Symbolism
- `[ns_78deg_236]` `[trigger: queen_cups_psychic]` `[factor_trigger: tarot_queen_cups AND state_psychic_clarity]` `[role: 条件分支]` Emotional maturity combined with psychic clarity—intuition directed with purpose; creative realization making vision real through love and will. → Upright Meaning
- `[ns_78deg_237]` `[trigger: queen_cups_reversed]` `[factor_trigger: tarot_queen_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: ambition without love—powerful but untrustworthy; emotional manipulation using feeling as weapon; vision separated from action. → Reversed Meaning
- `[ns_78deg_238]` `[trigger: vision_through_love]` `[factor_trigger: tarot_queen_cups AND principle_vision_through_love]` `[role: 总结]` Vision through love—seeing life's joy as gift, returning gift through creation; empathy combined with practical help; Queen of heart and home. → Upright Meaning
- `[ns_78deg_446]` `[trigger: shore_bridge]` `[factor_trigger: tarot_queen_cups AND symbol_shore]` `[role: 条件分支]` Throne at shore's edge—bridging water (emotion) and land (action); the Queen can feel deeply yet also manifest practically; integration of inner and outer. → Core Symbolism
- `[ns_78deg_447]` `[trigger: fierce_gaze]` `[factor_trigger: tarot_queen_cups AND symbol_fierce_gaze]` `[role: 条件分支]` Gaze is fierce, not dreamy—consciousness joined to feeling; imagination as tool for creation, not escape; emotional maturity combined with willful direction. → Core Symbolism
- `[ns_78deg_511]` `[trigger: empathy_action]` `[factor_trigger: tarot_queen_cups AND state_empathy_action]` `[role: 条件分支]` Empathy combined with practical help—not just feeling another's pain but acting to ease it; love that manifests as service; the caring that builds and heals. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Cups: Loving Intelligence"
    factor_refs: list = ['integration', 'existing', 'development', 'existing', 'faculty', 'existing', 'manifestation', 'existing', 'function', 'existing']
    
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
        l1_anchor="pt_v1.0.0_queen_of_cups__loving_intellig_001_L1",
    )
    version: str = "1.0.0"
