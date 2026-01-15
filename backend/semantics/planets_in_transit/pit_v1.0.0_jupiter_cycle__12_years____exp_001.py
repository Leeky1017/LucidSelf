"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.199889
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
    semantic_id="pit_v1.0.0_jupiter_cycle__12_years____exp_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterCycle12YearsExp(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Jupiter Cycle | 12-year ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Jupiter Cycle | 12-year orbit | Expansion timeline |
| Jupiter Return | Every 12 years | New growth cycle |
| Opportunity Windows | Natural growth periods | Optimism function |
| 太岁 Parallel | 12-year Chinese cycle | East-West correlation |

#### Source Text

"Jupiter's 12-year orbital cycle governs expansion, growth, opportunity, abundance, and optimism. Where Saturn contracts and limits, Jupiter expands and opens. The Jupiter cycle provides windows of opportunity, periods when growth comes naturally and new possibilities emerge. Jupiter returns every 12 years to its natal position, initiating fresh cycles of expansion into new areas of life."

#### English Paraphrase (Primary Language)

The **Jupiter cycle** (12 years) is astrology's primary **expansion and growth cycle**, complementing Saturn's contraction. Jupiter symbolizes **abundance principle**: opportunity, optimism, expansion, philosophy, meaning, generosity, good fortune. Its relatively fast cycle (compared to Saturn's 29.5 years) creates frequent opportunities for growth and renewal.

**12-year pattern**: Each Jupiter cycle follows an expansion-consolidation rhythm. The first half emphasizes growth, exploration, and opportunity-seeking. The second half consolidates gains and prepares for the next cycle. Unlike Saturn's hard reality-testing, Jupiter provides optimistic energy and faith in possibilities.

**Jupiter returns** (ages 12, 24, 36, 48, 60, 72, etc.) mark **new growth cycles**: fresh opportunities, philosophical renewal, expansion into new areas. These are generally positive periods (unlike often-difficult Saturn returns), though excessive expansion without consolidation can create problems (overextension, lack of boundaries).

**East-West parallel**: Jupiter's 12-year cycle **exactly matches** the Chinese **太岁/木星年** (Tai Sui/Jupiter year) cycle and zodiac animal 12-year cycle. Both traditions recognized Jupiter's 12-year period as governing fortune cycles, expansion/contraction rhythms, and opportunity windows. This is another precise East-West astronomical correlation.

#### Complete Chinese Interpretation (Secondary Language)

与土星的“现实与责任课”相反，木星 12 年一周的轨道象征的是**扩张、机遇与意义感**的节奏。每一轮木星周期都像一段“成长与拓展”的宏观章节：前半段偏向向外探索、新领域的打开、新关系/新学习机会的出现；后半段则倾向于整理、消化与整合，决定哪些扩张要固化为长期结构，哪些只是一闪而过的尝试。汉德提醒，木星行运虽多被视作“吉”，但如果没有土星式的结构配合，也很容易演变成过度乐观、盲目扩张与后期的负担。

当木星行运行到本命木星位置时，就发生一次**木星回归**：大约在 12、24、36、48、60 岁……这些节点往往伴随新的成长主题——第一次木星回归对应从童年步入青少年、世界观迅速扩展；第二次回归在 20 多岁中后期，常常引发教育、事业或地理上的新拓展；之后的每一次，则在各自的人生阶段带来新一轮的视野更新与机会窗口。总体上，木星回归比土星回归柔和得多，更像“上天给的一波顺风”，但前提是你愿意抓住并善用。

这一 12 年节律与中国传统中的**太岁 / 岁星 / 生肖 12 年循环**完全同频：两边都把木星的 12 年周期视为运势起伏、扩张收缩与机会窗口的自然刻度。把木星周期叠加在土星 30 年骨架之上，就构成了一个类似“大运 + 太岁”的西方时间网格。

#### Core Points

- **12-year cycle**: One Jupiter orbit = expansion/growth cycle
- **Opportunity windows**: Natural periods for growth and new possibilities
- **Jupiter return**: Every 12 years, fresh expansion cycle begins
- **Abundance principle**: Optimism, meaning, generosity, good fortune
- **Expansion-consolidation**: First half grows, second half integrates
- **Generally positive**: Unlike Saturn's tests, Jupiter opens doors
- **East-West parallel**: Exactly matches 太岁 12-year cycle"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Cycle (12 Years) - Expansion Opportunity"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_jupiter_cycle__12_years____exp_001_L1",
    )
    version: str = "1.0.0"
