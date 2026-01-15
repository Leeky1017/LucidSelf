"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.052174
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
    semantic_id="bot_v1.0.0_appendix_a__the_five_operation_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AppendixATheFiveOperation(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Significator | Querent's representative card | Reading anchor |
| YHVH Stacks | Four piles for IHVH | Question domain |
| Twelve Houses | Astrological divisions | Development context |
| Tree of Life | Ten Sephirotic piles | Final outcome |
| Counting | Card-to-card progression | Narrative building |

**Source Text**:
> "Choose a card to represent the Querent, using your knowledge or judgment of his character rather than dwelling on his physical characteristics. ... Hand the cards to Querent, and bid him think of the question attentively, and cut."

**English Paraphrase**:

The **Golden Dawn divination method** as taught by Crowley involves **Five Operations**:

**Preparation**:
1. **Choose a Significator**: Select a Court Card representing the Querent based on **character/personality**, not physical appearance
2. **Invocation**: "I invoke thee, I A O, that thou wilt send H R U, the great Angel..."
3. **Querent cuts**: While focusing on the question

**The Five Operations**:

**Operation I: The Situation**
- Cut into 4 stacks representing **YHVH** (from right to left)
- Find Significator—its stack reveals the **question's domain**:
  - **Yod (י)**: Work, business
  - **Heh (ה)**: Love, marriage, pleasure
  - **Vav (ו)**: Trouble, loss, quarrel
  - **Heh-final (ה)**: Money, material matters
- **Count and pair** cards around Significator to build the story

**Operation II: Development**
- Deal into **12 stacks** for the **12 astrological houses**
- Find Significator in expected house (7th for marriage, etc.)
- Read the stack's narrative

**Operation III: Further Development**
- Deal into **12 stacks** for the **12 zodiac signs**
- Continue the narrative

**Operation IV: Penultimate Aspects**
- Place Significator in center
- Form a **ring of 36 cards** (36 decans) around it
- Count and pair

**Operation V: Final Result**
- Deal into **10 piles** in the form of the **Tree of Life**
- Find Significator and read final outcome

**完整中文诠释**：

Crowley教授的**金色黎明占卜法**包含**五步操作**：

**准备**：
1. **选择Significator**：基于**性格/个性**而非外貌选择代表求问者的宫廷牌
2. **祈祷**："我召唤你，I A O，请派遣H R U，伟大的天使..."
3. **求问者切牌**：同时专注于问题

**五步操作**：

**操作一：情境**
- 切成4堆代表**YHVH**（从右到左）
- 找到Significator——其所在堆显示**问题的领域**：
  - **Yod（י）**：工作、事业
  - **Heh（ה）**：爱情、婚姻、愉悦
  - **Vav（ו）**：麻烦、损失、争吵
  - **Heh-final（ה）**：金钱、物质事务
- **计数并配对**Significator周围的牌以构建故事

**操作二：发展**
- 发成**12堆**对应**12占星宫位**
- 在预期宫位找Significator（婚姻找第7宫等）
- 阅读该堆的叙事

**操作三：进一步发展**
- 发成**12堆**对应**12星座**
- 继续叙事

**操作四：倒数第二面向**
- 将Significator放在中心
- 围绕它形成**36张牌的环**（36旬）
- 计数并配对

**操作五：最终结果**
- 发成**10堆**按**生命之树**形状
- 找到Significator并阅读最终结果

#### Core Points

- **Significator selection**: Based on **personality**, not physical appearance.
- **YHVH stacks** reveal the **domain** of the question (work/love/trouble/money).
- **Counting rules**: Knights/Queens/Princes=4, Princesses=7, Aces=11, Pips=number, Trumps=3/9/12 (elemental/planetary/zodiacal).
- **Five Operations** progressively deepen: Situation → Development → Further Development → Penultimate → Final.
- **Tree of Life spread** (Operation V) gives the **ultimate outcome**.

**Narrative Snippets**:
- `[ns_thoth_app_003]` `[trigger: significator]` `[factor_trigger: tarot_significator AND tarot_querent]` `[role: 主干]` Choose a Significator based on knowledge of the Querent's character rather than physical characteristics. → Source Text
- `[ns_thoth_app_004]` `[trigger: yhvh_stacks]` `[factor_trigger: tarot_yhvh AND tarot_domain]` `[role: 主干依赖]` The four stacks represent YHVH—Yod for work, Heh for love, Vav for trouble, Heh-final for money. → Source Text
- `[ns_thoth_app_011]` `[trigger: five_operations]` `[factor_trigger: tarot_divination AND tarot_progressive]` `[role: 条件分支]` Five Operations progressively deepen: Situation → Development → Further Development → Penultimate → Final Result. → Method
- `[ns_thoth_app_012]` `[trigger: tree_final]` `[factor_trigger: tarot_tree AND tarot_outcome]` `[role: 条件分支]` Operation V deals into 10 piles in the form of the Tree of Life—this gives the ultimate outcome. → Final"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix A: The Five Operations (五步操作法)"
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
        l1_anchor="bot_v1.0.0_appendix_a__the_five_operation_001_L1",
    )
    version: str = "1.0.0"
