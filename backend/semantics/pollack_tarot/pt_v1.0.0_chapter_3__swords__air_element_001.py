"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994933
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
    semantic_id="pt_v1.0.0_chapter_3__swords__air_element_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Chapter3SwordsAirElement(SemanticEntry):
    """
    **Source Framework**:

Swords represent the **Air element** - thought, intellect, truth, and the min...
    """
    
    original_text: str = """**Source Framework**:

Swords represent the **Air element** - thought, intellect, truth, and the mind's constant motion. Where Wands are action and Cups are feeling, Swords are **thinking and knowing**. The sword can **cut through illusion** (Alexander cutting Gordian knot) or **inflict pain** (weapon of destruction).

**Core Air Symbolism**:
- **Constant motion**: Mind never rests, always moving like wind
- **Clarity**: Cutting through fog to reveal truth
- **Double-edged**: Truth brings both liberation and pain
- **Breath/Spirit**: Word for "spirit" relates to "wind" (Hebrew: ruach)
- **Closest to Ether**: Air approaches fifth element (Spirit) most directly

**Swords as Life Domain**:
- **Intellect**: Rational mind, analysis, planning
- **Truth**: Cutting to reality beneath illusions
- **Communication**: Words as swords (can heal or wound)
- **Conflict**: Internal (anxiety, overthinking) and external (arguments, battles)
- **Sorrow**: The stormy side of Air - pain, anger, grief
- **Justice**: Sword as tool of judgment and discrimination

**The Swords Problem - "Hamlet Complex"**:
- **Ungrounded thought**: Mind sees too many sides, becomes paralyzed
- **Overthinking**: Analysis without action leads to confusion
- **Solution**: Not banishing thought, but **combining Air with other elements**
  - Air + Water (Cups) = Emotion balances intellect
  - Air + Earth (Pentacles) = Grounding in practical reality
  - Air + Ether (Major Arcana) = Spiritual values guide reasoning
  - **Result**: Problem transforms to Way/Wisdom

**Swords Dual Nature**:
- **Positive**: Clarity, truth, wisdom, justice, courage to face reality
- **Negative**: Pain, cruelty, anxiety, despair, mental torture
- **Key**: Like Galahad needing magic sword to begin Grail quest, we need truth (however painful) to begin meaningful life

**Shadow Side of Swords**:
- Overthinking leading to paralysis
- Cruelty and infliction of pain
- Mental anguish and anxiety
- Cynicism and bitter acceptance
- Using intellect to manipulate or harm

**完整中文诠释**:
**宝剑**代表**风元素**——思想、智慧、真理、心智的恒动。权杖=行动，圣杯=感受，宝剑=**思考与知道**。剑可以**穿透幻觉**（亚历山大斩戈尔迪之结）或**施加痛苦**（破坏之武器）。**风之核心象征**：**恒动**（心智永不休息，如风持续移动）；**清晰**（穿透迷雾显示真理）；**双刃**（真理带来解放与痛苦）；**呼吸/灵**（"灵"与"风"同字，希伯来文ruach）；**最近以太**（风最接近第五元素"灵性"）。**宝剑生活领域**：**智慧**（理性心智、分析、计划），**真理**（切到幻觉下的现实），**沟通**（话语如剑，可疗愈或伤害），**冲突**（内在如焦虑/过度思考，外在如争论/战斗），**悲伤**（风之暴风面——痛苦、愤怒、悲伤），**正义**（剑作为审判与辨别工具）。**宝剑问题="哈姆雷特综合症"**：**未接地思想**见太多面陷入麻痹，**过度思考**无行动导致困惑。**解决**：非驱逐思想而是**结合风与其他元素**——风+水（圣杯）=情感平衡智力，风+土（星币）=扎根实际现实，风+以太（大阿尔卡纳）=灵性价值引导理性。**结果**：问题转化为道路/智慧。**双重本质**：正面（清晰、真理、智慧、正义、勇气面对现实），负面（痛苦、残忍、焦虑、绝望、心智折磨）。**关键**：如Galahad需魔法剑开始圣杯探索，我们需真理（无论多痛苦）开始有意义生活。

**Cultural Context**: Modern culture emphasizes rationality, many blame thinking for life's problems. Tarot says: **More confused = more need mind**, but mind must combine with other elements.

**Narrative Snippets**:
- `[ns_78deg_322]` `[trigger: swords_intro]` `[factor_trigger: tarot_swords AND element_air]` `[role: 主干]` Swords represent Air element—thought, intellect, truth, mind's constant motion; where Wands are action and Cups feeling, Swords are thinking and knowing. → Source Framework
- `[ns_78deg_323]` `[trigger: sword_double_edge]` `[factor_trigger: tarot_swords AND principle_duality]` `[role: 主干依赖]` Sword can cut through illusion (Alexander cutting Gordian knot) or inflict pain (weapon of destruction)—double-edged truth brings liberation and pain. → Core Air Symbolism
- `[ns_78deg_324]` `[trigger: air_spirit]` `[factor_trigger: element_air AND element_ether]` `[role: 条件分支]` Air closest to Ether—word for "spirit" relates to "wind" (Hebrew ruach); breath/spirit connection makes Swords the most spiritual Minor suit. → Core Air Symbolism
- `[ns_78deg_325]` `[trigger: hamlet_complex]` `[factor_trigger: tarot_swords AND state_overthinking]` `[role: 条件分支]` Hamlet Complex—ungrounded thought sees too many sides, becomes paralyzed; analysis without action leads to confusion. → The Swords Problem
- `[ns_78deg_326]` `[trigger: air_integration]` `[factor_trigger: tarot_swords AND principle_elemental_balance]` `[role: 条件分支]` Solution: combine Air with other elements—Air+Water balances emotion/intellect, Air+Earth grounds in practical reality, Air+Ether guides reasoning with spiritual values. → The Swords Problem
- `[ns_78deg_327]` `[trigger: galahad_sword]` `[factor_trigger: tarot_swords AND principle_truth]` `[role: 总结]` Like Galahad needing magic sword to begin Grail quest, we need truth (however painful) to begin meaningful life; more confused = more need mind combined with elements. → Swords Dual Nature"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter 3: Swords (Air Element) - Introduction"
    factor_refs: list = ['faculty', 'existing', 'principle', 'existing', 'process', 'existing', 'experience', 'existing', 'shadow', 'existing', 'faculty', 'existing']
    
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
        l1_anchor="pt_v1.0.0_chapter_3__swords__air_element_001_L1",
    )
    version: str = "1.0.0"
