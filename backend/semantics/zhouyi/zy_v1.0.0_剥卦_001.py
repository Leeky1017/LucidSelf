"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899906
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
    semantic_id="zy_v1.0.0_剥卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 剥卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  剥：不利有攸往。

  【彖传】
  《彖》曰：“剥，剥也，柔变刚也。不利有攸往，小人长也。顺而止之，观象也。君子尚消息盈虚，天行也。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  剥：不利有攸往。

  【彖传】
  《彖》曰：“剥，剥也，柔变刚也。不利有攸往，小人长也。顺而止之，观象也。君子尚消息盈虚，天行也。”

  【象传】
  《象》曰：山附于地，剥；上以厚下安宅。

  【爻辞】
  初六，剥床以足，蔑；贞凶。
  六二，剥床以辨，蔑；贞凶。
  六三，剥之，无咎。
  六四，剥床以肤，凶。
  六五，贯鱼，以宫人宠，无不利。
  上九，硕果不食，君子得舆，小人剥庐。

- 分字分词释义：

  - **剥**：剥落、剥蚀、逐层削去之意，象征阳刚被阴柔层层削夺，或根基被侵蚀。
  - **柔变刚**：阴柔渐渐改变刚健，使刚者失位，小人得势。
  - **不利有攸往**：剥势既成，不利再行大事大动，宜守不宜进。
  - **消息盈虚**：消长与盈虚，指阴阳、兴衰的周期变化。
  - **剥床以足 / 以辨 / 以肤**：从削去床脚、床头到削去床板，使人接地而卧，比喻基础、支撑与防护被一层层剥去。
  - **贯鱼**：鱼贯而行，比喻宫人依次排列，象征在剥势之中仍然有序的宫闱秩序与宠爱。
  - **硕果不食**：硕大的果实尚未被吃掉，比喻在衰败之中仍存留的君子或好因子。

- **规范化释义（primary_lang_explained）**：

  剥卦讲“势在剥落”的局面：阳刚被阴柔层层剥蚀，小人渐长，正道根基不断被削弱。卦辞“剥：不利有攸往”直接指出，在这种形势下，不宜贸然前行，只宜顺势而止、保全所能保全之物。

  彖传说明，“柔变刚也”“小人长也”，问题不在个别人物，而在结构：当阴柔逐步占据阳刚的位次时，局势自然走向剥落；“顺而止之，观象也”则强调：君子应从卦象中看到山附于地、层次被抹平的形势，知道须厚下安宅、加固基础，而非硬冲；同时“尚消息盈虚，天行也”提醒人们：任何剥落都在循环之内，不必绝望，但也不可以侥幸。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Bo, "Splitting Apart" or "Peeling", portrays a time of decay and erosion when negative forces grow and positive forces retreat. The Judgment, "Bo: it is not favorable to go anywhere", warns that in such times, one should not act rashly but should wait, preserve what remains, and prepare for eventual renewal.

- 核心要点：

  - 剥卦聚焦于**衰败与剥蚀的结构性时刻**，提示“宜止不宜进”。
  - 从“剥床以足、以辨、以肤”的递进，可据以观察基础是否正被层层削弱。
  - 卦中仍保留“硕果不食”的君子之象，为后续“复卦”的回升埋下伏笔。

- 详细解说：

  卦象“山附于地”：山体似乎要与大地合而为一，山与地之间的高下差异被抹平，象征界限与高度被剥蚀。与前一卦贲相比，贲是在有根基时增添文彩，剥则是根基本身被削弱，两者形成鲜明对照。

  在实际应用上，剥卦适合作为识别“系统性风险与衰败”的提示：当制度中正直之人被边缘化、规则被一点点折损、底线逐渐被抹去时，就是“剥床以足 / 以辨 / 以肤”的过程；此时若仍执意扩张或大动干戈，往往招致更大凶险。反之，若能像六三那样主动“剥之”，舍弃部分利益与外饰，保全核心根基，反而可能“无咎”。

  “硕果不食”则是对剥势中残存良善的珍视：当整体体系走向剥落时，仍有少数“硕果”未被吞噬——这些人或资源，便是后续“复”的起点。因而剥卦与复卦在卦序上相连，构成“剥极而复”的结构：剥蚀至极处，新阳亦于内萌生。"""
    normalized_text_zh: str = """"""
    subject: str = "剥卦（䷖）"
    factor_refs: list = ['zhouyi_gua_bo']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_剥卦_001_L1",
    )
    version: str = "1.0.0"
