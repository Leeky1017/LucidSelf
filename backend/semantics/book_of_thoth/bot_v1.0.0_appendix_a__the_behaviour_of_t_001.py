"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.052141
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
    semantic_id="bot_v1.0.0_appendix_a__the_behaviour_of_t_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AppendixATheBehaviourOfT(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Behaviour | Card interaction patterns | Experiential knowledge |
| Divination | Practical card use | Primary learning method |
| Significator | Card representing Querent | Reading anchor |
| Operations | Divination stages | Five-step process |

**Source Text**:
> "The position of the student of the Tarot is very similar. In this essay, and in these designs, is given an analysis of the general character of each card; but he cannot reach any true appreciation of them without observing their behaviour over a long period; he can only come to an understanding of the Tarot through experience. It will not be sufficient for him to intensify his studies of the cards as objective things; he must use them; he must live with them. They, too, must live with him. A card is not isolated from its fellows. The reactions of the cards, their interplay with each other, must be built into the very life of the student."

**English Paraphrase**:

Crowley emphasizes that **intellectual study alone is insufficient**—the Tarot must be **experienced through use**:

**Core Principle**:
- Cards are **living entities** with distinct "behaviours"
- Understanding comes from **observing interactions** over time
- The student must **live with the cards**—they become part of daily consciousness
- **Divination is the practical method** for most students (vs. contemplation for advanced initiates)

**Why Divination?**
The ideal way to know the cards is through high-level contemplation, but this requires advanced initiation. For most people, **practical divination** is the accessible path. Through repeated readings, the cards reveal their characters through their **interactions and relationships**.

**完整中文诠释**：

Crowley强调**单纯的智力学习是不够的**——塔罗必须**通过使用来体验**：

**核心原则**：
- 牌是具有独特"行为"的**活体存在**
- 理解来自于长期**观察互动**
- 学生必须**与牌共同生活**——它们成为日常意识的一部分
- **占卜是实践方法**，适合大多数学生（而非高级启蒙者的冥想）

**为何占卜？**
认识牌的理想方式是通过高层次冥想，但这需要高级启蒙。对大多数人来说，**实践占卜**是可及的路径。通过反复的解读，牌通过它们的**互动和关系**展现其特性。

#### Core Points

- **Experiential learning**: Tarot cannot be mastered through intellectual study alone—practical use is essential.
- **Living entities**: Cards have distinct "behaviours" that reveal themselves through interaction.
- **Divination as method**: For most students, divination is the accessible path to understanding (vs. advanced contemplation).
- **Interplay**: A card's meaning emerges from its **relationships with other cards**, not in isolation.
- **Time requirement**: True appreciation requires observing card behaviour over a **long period**.

**Narrative Snippets**:
- `[ns_thoth_app_001]` `[trigger: card_behaviour]` `[factor_trigger: tarot_behaviour AND tarot_experience]` `[role: 主干]` The student cannot reach true appreciation of the cards without observing their behaviour over a long period through experience. → Source Text
- `[ns_thoth_app_002]` `[trigger: divination_method]` `[factor_trigger: tarot_divination AND tarot_learning]` `[role: 主干依赖]` The practical every-day commonplace way to learn the Tarot is divination. → Source Text
- `[ns_thoth_app_009]` `[trigger: living_cards]` `[factor_trigger: tarot_cards AND tarot_interaction]` `[role: 条件分支]` A card is not isolated from its fellows—the reactions and interplay of the cards must be built into the very life of the student. → Living Entities
- `[ns_thoth_app_010]` `[trigger: experiential_path]` `[factor_trigger: tarot_experience AND tarot_contemplation]` `[role: 条件分支]` Divination is the accessible path for most students; advanced contemplation requires higher initiation. → Levels"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix A: The Behaviour of the Tarot (塔罗牌的行为)"
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
        l1_anchor="bot_v1.0.0_appendix_a__the_behaviour_of_t_001_L1",
    )
    version: str = "1.0.0"
