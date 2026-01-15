"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755721
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
    semantic_id="zw_v1.0.0_论人生时要审的确_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论人生时要审的确(SemanticEntry):
    """
    - 分字分词释义：

  - **生时的确**：确保出生时辰准确无误，是一切命理推断的前提，稍有偏差则全盘失准。
  - **子亥二时最难定准**：子时（23:00-01:00）与亥时（21:00-2...
    """
    
    original_text: str = """- 分字分词释义：

  - **生时的确**：确保出生时辰准确无误，是一切命理推断的前提，稍有偏差则全盘失准。
  - **子亥二时最难定准**：子时（23:00-01:00）与亥时（21:00-23:00）交界处最易混淆，须特别仔细推详。
  - **子时有十刻**：古法将子时细分为十刻，强调时辰内部仍有早晚之分。
  - **上五刻属昨夜亥时**：子时前五刻（约23:00-00:00）实际上仍属前一日的亥时气运。
  - **下五刻属今日子时**：子时后五刻（约00:00-01:00）方为真正的今日子时，日干支已换。
  - **阴雨之际**：天气阴暗、日月难辨时，更易记时不准，须格外审慎。
  - **罗经以定真确**：借助罗盘等定向工具，结合天象观察，尽量校正至准确时刻。
  - **差讹则命不准**：生时哪怕差一刻两刻，命宫、星曜分布都可能整宫错位，后续推断全部失效。

- 原文（断句）：

  论人生时要审的确：

  如人生子亥二时，最难定准，要仔细推详。如子时有十刻，上五刻属昨夜亥时，下五刻属今日子时。如天气阴雨之际，必湏罗经以定真确时候，若差讹，则命不准矣。

- 规范化释义（primary_lang_explained）：

  本条专门提醒断命之人必须严谨审定出生时刻，尤其是在子、亥等相邻时支之间，最易发生记时模糊与界线摇摆。古法以「子时分为十刻」为喻：前五刻可视作仍属昨夜亥时，后五刻方真属今日子时；若只凭大致印象而不细加推详，往往会在命宫安立与星曜起布上发生一整宫的偏差，导致后续推断全盘失准。

  在天气阴雨、日月难见或家人记时不清的情境中，原文建议借助罗经等工具，尽量校正至较为准确的时刻，再行安命排盘。其核心意思是：生时误差哪怕只差一刻两刻，所对应的宫位、星曜与神煞组合都有可能完全不同。若前提时刻不确，则后续一切精细的格局分析、限运推断，都只是「在错盘上做对推演」，难以真正可信。

- 核心要点：

  1. 子、亥等交界时段最难精确判定，传统以「子时十刻，上五属亥，下五属子」来提示界线敏感。
  2. 生时稍有误差，就可能导致命宫安错一宫，星曜与神煞分布整体错位。
  3. 阴雨昏暗、记时草率时，应借助罗经或其他工具尽量校正时刻，而非凭印象作数。
  4. 若前提生时不确，则再精细的格局分析与运程推断，可靠性都大打折扣。
  5. 本条实为对整部卷五的「方法论提醒」：先求时刻准确，再谈命理精度。

- 完整对等诠释（secondary_lang_full）：

  This passage is a methodological warning about the accuracy of birth time. It
  notes that boundary periods, especially between the Hai and Zi hours, are the
  hardest to judge. Traditional texts imagine Zi as being divided into ten
  parts: the first five still belonging to the previous Hai hour and the last
  five to Zi itself. If one treats the whole span simply as "Zi" without such
  care, the Life palace may be placed an entire house off, reshaping the whole
  chart.

  In conditions of darkness, bad weather or vague family memory, the author
  recommends using instruments such as the Luo compass and, by extension, any
  reliable method to pin down the time as precisely as possible before casting
  the chart. Even small errors can change which stars and spirit markers occupy
  key palaces, so highly detailed interpretations built on a mis-timed chart
  are little more than elegant guesses. The rule urges practitioners to secure
  accurate input data first and only then indulge in fine-grained destiny
  analysis.

- 叙事素材（narrative_snippets）：

  - **子亥交界**："子时十刻，上五属亥，下五属子"，交界时段最难精确判定。
  - **一宫之差**："生时稍有误差，就可能导致命宫安错一宫"，时刻精度决定全盘准确性。
  - **借助工具**："阴雨昏暗时，应借助罗经尽量校正时刻"，强调准确记时的重要性。
  - **现代应用**：本条是卷五的方法论总结——"先求时刻准确，再谈命理精度"。"""
    normalized_text_zh: str = """"""
    subject: str = "论人生时要审的确"
    factor_refs: list = ['zone_zihai', 'system_shike', 'method_luojing', 'risk_cuogong', 'level_kexin', 'source_ref', 'rel_shenshi_001', 'zone_zihai', 'rel_shenshi_002', 'method_luojing', 'rel_shenshi_003', 'risk_cuogong', 'evi_shenshi_001', 'system_shike', 'rule_shenshi_shike', 'evi_shenshi_002', 'method_luojing', 'rule_shenshi_luojing', 'concept_time_precision', 'concept_chart_validity']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_论人生时要审的确_001_L1",
    )
    version: str = "1.0.0"
