"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994685
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
    semantic_id="pt_v1.0.0_introduction__the_minor_arcana_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class IntroductionTheMinorArcana(SemanticEntry):
    """
    **Source Text** (Pollack's framework):

"Because the Minor Arcana deals primarily with the outer ran...
    """
    
    original_text: str = """**Source Text** (Pollack's framework):

"Because the Minor Arcana deals primarily with the outer range of experience... a study of the Minor Arcana shows how mundane experience derives from a spiritual base... The Major cards depict archetypal forces rather than real people... But the Minor cards show aspects of life as people actually live it."

**English Paraphrase**:

The **Minor Arcana** represents the **practical, everyday experiences** of human life, contrasting with the Major Arcana's archetypal spiritual journey.

**Key Distinctions**:
- **Major Arcana** = Archetypal forces, universal spiritual patterns, destiny
- **Minor Arcana** = Daily experiences, personal choices, free will within fate

**Four Suits = Four Elements & Life Domains**:

1. **Wands** (权杖) = **Fire** 🔥
   - Energy, action, movement, will
   - Business, competition, romance (pursuit, not emotion)
   - Optimism, confidence, vitality
   - Shadow: Burnout, aggression, restlessness

2. **Cups** (圣杯) = **Water** 💧
   - Emotion, love, relationships, intuition
   - Feeling, depth, imagination, dreams
   - Receptivity, connection, empathy
   - Shadow: Overwhelm, illusion, emotional instability

3. **Swords** (宝剑) = **Air** 💨
   - Thought, intellect, communication, conflict
   - Planning, analysis, justice, truth
   - Clarity, decision, courage
   - Shadow: Cruelty, overthinking, anxiety, pain

4. **Pentacles** (星币) = **Earth** 🌍
   - Material world, body, practical matters, security
   - Work, money, health, stability
   - Groundedness, enjoyment, manifestation
   - Shadow: Materialism, stagnation, greed

**Card Structure (14 per suit)**:
- **Ace**: Pure elemental energy, gift, potential
- **2-10**: Progressive development of that element
- **Court Cards**: Human embodiments
  - **Page**: Youthful energy, learning, messenger
  - **Knight**: Active energy, quest, extremes
  - **Queen**: Mature receptive energy, mastery
  - **King**: Mature active energy, authority, responsibility

**完整中文诠释**:
**小阿尔卡纳**=**日常生活之镜**——56张牌映射实际经验，对比22张大阿尔卡纳的普遍原型力量。**四花色体系**：**权杖（火🔥）**=行动、意志、创造、灵感、企业心，生命力量；**圣杯（水💧）**=情感、爱情、关系、直觉、接纳、想象力；**宝剑（风💨）**=思想、智力、沟通、冲突、真理、决定；**星币（土🌍）**=物质世界、身体、实际事务、工作、金钱、安全。**结构（每花色14张）**：**Ace**=纯元素能量，神圣礼物，潜能；**2-10**=该元素的渐进发展，从初始到完成；**宫廷牌**（4张）=人类具身化：Page（少年能量，学习，信使）、Knight（主动能量，极端，追求）、Queen（成熟接纳能量，掌握）、King（成熟主动能量，权威，责任）。**核心哲学**：大阿尔卡纳回答"我们为何存在"（灵性本质），小阿尔卡纳回答"我们如何生活"（实际显化），共同构成人类经验的完整地图（内在+外在）。Pollack的"人本塔罗"强调：非固定公式，而是个人洞察的灵活图像；Rider-Waite的插图小牌（vs几何图案）使深度心理解读成为可能。

**Core Philosophy**:
- **Major Arcana** = "Why we exist" (spiritual essence)
- **Minor Arcana** = "How we live" (practical manifestation)
- Together: Complete map of human experience (inner + outer)

**Pollack's "Humanistic Tarot"**: Not fixed formulas, but flexible images for personal insight. Rider-Waite's illustrated pip cards (vs geometric patterns) enable deeper psychological interpretation.

**Narrative Snippets**:
- `[ns_78deg_316]` `[trigger: minor_arcana_intro]` `[factor_trigger: tarot_minor_arcana AND principle_practical_manifestation]` `[role: 主干]` Minor Arcana deals with outer range of experience—showing how mundane experience derives from spiritual base; 56 cards mapping daily life through four elemental domains. → Source Text
- `[ns_78deg_317]` `[trigger: major_vs_minor]` `[factor_trigger: tarot_minor_arcana AND tarot_major_arcana]` `[role: 主干依赖]` Major Arcana depicts archetypal forces rather than real people; Minor cards show aspects of life as people actually live it—destiny vs daily choice. → Source Text
- `[ns_78deg_318]` `[trigger: four_suits_elements]` `[factor_trigger: tarot_four_suits AND element_four_elements]` `[role: 条件分支]` Four Suits = Four Elements: Wands/Fire (action, will), Cups/Water (emotion, love), Swords/Air (thought, conflict), Pentacles/Earth (material, body). → English Paraphrase
- `[ns_78deg_319]` `[trigger: card_structure_14]` `[factor_trigger: tarot_suit_structure AND element_progression]` `[role: 条件分支]` Fourteen cards per suit: Ace (pure elemental gift), 2-10 (progressive development), Court (human embodiments—Page/Knight/Queen/King). → English Paraphrase
- `[ns_78deg_320]` `[trigger: why_vs_how]` `[factor_trigger: tarot_core_philosophy AND principle_integration]` `[role: 条件分支]` Core philosophy: Major Arcana answers "why we exist" (spiritual essence), Minor answers "how we live" (practical manifestation)—complete map of experience. → Core Philosophy
- `[ns_78deg_321]` `[trigger: humanistic_tarot]` `[factor_trigger: tarot_interpretation AND principle_flexibility]` `[role: 总结]` Pollack's "Humanistic Tarot"—not fixed formulas but flexible images for personal insight; Rider-Waite illustrated pips enable deeper psychological interpretation. → Pollack's Framework"""
    normalized_text_zh: str = """"""
    subject: str = "Introduction: The Minor Arcana Framework"
    factor_refs: list = ['domain', 'existing', 'force', 'existing', 'principle', 'existing', 'process', 'existing', 'archetype', 'existing', 'pattern', 'existing']
    
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
        l1_anchor="pt_v1.0.0_introduction__the_minor_arcana_001_L1",
    )
    version: str = "1.0.0"
