"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997649
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
    semantic_id="dts_v1.0.0_坎离气不并行_而有相济者在_001",
    book_id="dts",
    engine_id="bazi"
)
class 坎离气不并行而有相济者在(SemanticEntry):
    """
    - **原文（source_text）**：
  坎离气不并行，而有相济者在。

- 原注（原文注解）：
  　　天干透壬癸，地支属离，为既济，要天气下降；天干透丙丁，地支属坎，为未济，要地气上升。天...
    """
    
    original_text: str = """- **原文（source_text）**：
  坎离气不并行，而有相济者在。

- 原注（原文注解）：
  　　天干透壬癸，地支属离，为既济，要天气下降；天干透丙丁，地支属坎，为未济，要地气上升。天干皆水，地支皆火，为交姤，身强则吉；天干皆火，地支皆水，为交战，身弱则凶。坎外离内，亦谓之未济，所喜在离，要水竭……（并论子午卯酉之专气及调和通关要点）。

- **规范化释义（primary_lang_explained）**：
  水火不并行，贵在一降一升以致“既济”。强弱不同，凶吉相反；以木为通，水火得济。

- 分字分词释义：
  - 坎：水卦象。
  - 离：火卦象。
  - 既济/未济：降升得序/未成调剂。
  - 木为媒：以木通水火。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 坎离 | Water-Fire (Kan-Li) | 水火既济 | Water and Fire interaction | kanli | existing |
| 气不并行 | Qi Not Parallel | 水火不容 | Qi does not run parallel | qibubingxing | new_candidate |
| 相济 | Mutual Aid (Xiang-Ji) | 互相调剂 | Complementary aid | xiangji | new_candidate |
| 既济 | Already Completed (Ji-Ji) | 水火既济 | Perfect balance | jiji | new_candidate |
| 未济 | Not Yet Completed (Wei-Ji) | 水火未济 | Incomplete balance | weiji | new_candidate |
| 交姤 | Intercourse (Jiao-Gou) | 水火交融 | Interaction without conflict | jiaogou | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Kan-Li (Water-Fire) theory: Water (Kan) and Fire (Li) do not run parallel (Qi-Bu-Bing-Xing) but can complement (Xiang-Ji). "Already Completed" (Ji-Ji): Water descends, Fire ascends. "Not Yet Completed" (Wei-Ji): Needs adjustment. Use Wood as Mediator (Mu-Wei-Mei) to connect them. Body Strength determines if "Intercourse" (Jiao-Gou) is safe or "Battle" (Jiao-Zhan) is dangerous."""
    normalized_text_zh: str = """"""
    subject: str = "坎离气不并行，而有相济者在。"
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_坎离气不并行_而有相济者在_001_L1",
    )
    version: str = "1.0.0"
