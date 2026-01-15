"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997536
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
    semantic_id="dts_v1.0.0_生时归宿_譬之墓也_人元用事之神_墓之穴也_不可以不辨_001",
    book_id="dts",
    engine_id="bazi"
)
class 生时归宿譬之墓也人元用事之神墓之穴也不可以不辨(SemanticEntry):
    """
    - **原文（source_text）**：
  生时归宿，譬之墓也，人元用事之神，墓之穴也，不可以不辨。

- 原注（原文注解）（节要）：
  　　子时生人前三刻三分，壬水用事，后四刻七分，癸水用事...
    """
    
    original_text: str = """- **原文（source_text）**：
  生时归宿，譬之墓也，人元用事之神，墓之穴也，不可以不辨。

- 原注（原文注解）（节要）：
  　　子时生人前三刻三分，壬水用事，后四刻七分，癸水用事……同年月日时而百人各一应者，固当究其时之先后，又当论其山川之异，世德之殊……学者察此，可以知兴替矣。

- 分字分词释义：
  - 生时：出生日所对应之时辰，为“归宿之处”；
  - 归宿：命局落点、收束之地；
  - 墓之穴：埋藏之点，比喻最终所归之处；
  - 山川之异、世德之殊：外部环境与家族背景之差异。

- **规范化释义（primary_lang_explained）**：
  生时为“归宿”，好比宅之墓穴：气数至此归于一处。须细分时辰内的用事之神，并结合地域山川、家族世德等外部条件，才能解释为什么“同年同月同日而时同”之人，际遇却大不相同。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 生时 | Birth Hour (Sheng-Shi) | 归宿之地 | Place of destination | shengshi | existing |
| 归宿 | Destination | 最终结局 | Final outcome | guisu | new_candidate |
| 墓之穴 | Grave Hole | 气之落点 | Resting point of Qi | mu_zhixue | new_candidate |
| 山川之异 | Geographic Difference | 地理环境 | Environmental factor | shanchuan_zhiyi | new_candidate |
| 世德之殊 | Family Virtue Difference | 祖德家世 | Family background factor | shide_zhishu | new_candidate |
| 兴替 | Rise and Fall | 盛衰结局 | Final success or failure | xingti | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Sheng-Shi (Birth Hour) is the "Grave/Destination" (Mu), the governing stem is the "Hole" (Xue). It is the final resting place of the Qi. Differentiates people born on same day/month/year. Must analyze the specific governing stem of the hour and combine with external factors (Geography, Virtue) to understand the final outcome (兴替)."""
    normalized_text_zh: str = """"""
    subject: str = "生时归宿，譬之墓也，人元用事之神，墓之穴也，不可以不辨。"
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
        l1_anchor="dts_v1.0.0_生时归宿_譬之墓也_人元用事之神_墓之穴也_不可以不辨_001_L1",
    )
    version: str = "1.0.0"
