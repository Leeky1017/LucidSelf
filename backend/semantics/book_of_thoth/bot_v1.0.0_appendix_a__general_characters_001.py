"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.052190
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
    semantic_id="bot_v1.0.0_appendix_a__general_characters_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AppendixAGeneralCharacters(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Spiritual matters | Higher/abstract interpretation | Card's essential meaning |
| Material matters | Practical/mundane interpretation | Everyday application |
| Dignified | Well-aspected | Positive expression |
| Ill-dignified | Badly-aspected | Negative/shadow expression |

**Source Text** (Selected Trumps):

**0 - The Fool**:
> "In spiritual matters, the Fool means idea, thought, spirituality, that which endeavours to transcend earth. In material matters, it may, if badly dignified, mean folly, eccentricity, or even mania. But the essential of this card is that it represents an original, subtle, sudden impulse or impact, coming from a completely strange quarter."

**I - The Magus**:
> "Skill, wisdom, adroitness, elasticity, craft, cunning, deceit, theft. Sometimes occult wisdom or power, sometimes a quick impulse, a 'brain-wave'. It may imply messages, business transactions, the interference of learning or intelligence with the matter in hand."

**II - The High Priestess**:
> "Pure, exalted and gracious influence enters the matter. Hence, change, alternation, increase and decrease, fluctuation. There is, however, a liability to be led away by enthusiasm; one may become 'moon-struck' unless careful balance is maintained."

**English Paraphrase**:

Crowley provides **practical divinatory meanings** for each Trump, distinguishing between **spiritual** and **material** contexts:

**Key Patterns**:
- Each card has an **essential character** (its core meaning)
- **Dignified** (well-placed): Positive expression of the card's energy
- **Ill-dignified** (badly-placed): Shadow/negative expression
- Context determines whether the spiritual or material meaning applies

**Selected Trump Meanings**:

| Atu | Dignified | Ill-Dignified | Essential |
|-----|-----------|---------------|-----------|
| 0 Fool | Idea, spirituality, transcendence | Folly, eccentricity, mania | Sudden impulse from strange quarter |
| I Magus | Skill, wisdom, occult power | Cunning, deceit, theft | Intelligence interfering with matter |
| II Priestess | Pure influence, change, grace | Moon-struck, imbalanced | Fluctuation, increase/decrease |
| III Empress | Love, beauty, happiness, pleasure | Dissipation, debauchery | Creative harmony |
| IV Emperor | War, conquest, ambition, energy | Stubbornness, ill-temper | Overweening confidence |
| V Hierophant | Teaching, endurance, goodness | Stubborn orthodoxy | Manifestation of wisdom |

**完整中文诠释**：

Crowley提供每张大牌的**实用占卜含义**，区分**精神**和**物质**语境：

**关键模式**：
- 每张牌都有**本质特性**（核心含义）
- **尊贵**（良好位置）：牌能量的正面表达
- **卑下**（不良位置）：阴影/负面表达
- 语境决定适用精神还是物质含义

**部分大牌含义**：

| Atu | 尊贵 | 卑下 | 本质 |
|-----|------|------|------|
| 0 愚者 | 想法、灵性、超越 | 愚蠢、怪癖、疯狂 | 来自陌生处的突然冲动 |
| I 魔术师 | 技巧、智慧、神秘力量 | 狡猾、欺骗、盗窃 | 智力干预事务 |
| II 女祭司 | 纯净影响、变化、优雅 | 月迷、失衡 | 波动、增减 |
| III 皇后 | 爱、美、快乐、愉悦 | 放纵、堕落 | 创造和谐 |
| IV 皇帝 | 战争、征服、野心、能量 | 固执、坏脾气 | 过度自信 |
| V 教皇 | 教导、忍耐、善良 | 顽固正统 | 智慧显化 |

#### Core Points

- **Dual interpretation**: Each Trump has both spiritual (abstract) and material (practical) meanings.
- **Dignity system**: Well-dignified = positive; Ill-dignified = shadow/negative.
- **Essential character**: The card's irreducible core meaning, independent of dignity.
- **Context sensitivity**: The same card means different things in different positions and combinations.
- **Practical focus**: These meanings are for **actual readings**, not just theoretical study.

**Narrative Snippets**:
- `[ns_thoth_app_005]` `[trigger: trump_use]` `[factor_trigger: tarot_trump AND tarot_dignity]` `[role: 主干]` Each Trump has an essential character plus dignified and ill-dignified expressions depending on context. → English Paraphrase
- `[ns_thoth_app_006]` `[trigger: fool_essential]` `[factor_trigger: tarot_fool AND tarot_essential]` `[role: 主干依赖]` The Fool's essential meaning is an original, subtle, sudden impulse or impact from a completely strange quarter. → Source Text
- `[ns_thoth_app_013]` `[trigger: magus_skill]` `[factor_trigger: tarot_magus AND tarot_practical]` `[role: 条件分支]` The Magus signifies skill, wisdom, adroitness—sometimes occult wisdom or power, sometimes a quick impulse, a 'brain-wave'. → Magus
- `[ns_thoth_app_014]` `[trigger: dignity_system]` `[factor_trigger: tarot_dignity AND tarot_shadow]` `[role: 条件分支]` Dignified = positive expression of card's energy; Ill-dignified = shadow/negative expression. Context determines which applies. → Dignity"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix A: General Characters of the Trumps in Use (大牌实用特性)"
    factor_refs: list = []
    
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
        l1_anchor="bot_v1.0.0_appendix_a__general_characters_001_L1",
    )
    version: str = "1.0.0"
