"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997529
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
    semantic_id="dts_v1.0.0_月令提纲_譬之宅也_人元用事之神_宅之向也_不可以不卜_001",
    book_id="dts",
    engine_id="bazi"
)
class 月令提纲譬之宅也人元用事之神宅之向也不可以不卜(SemanticEntry):
    """
    - **原文（source_text）**：
  月令提纲，譬之宅也，人元用事之神，宅之向也，不可以不卜。

- 原注（原文注解）：
  　　令星，乃命之至要，宜气象得令者吉，喜神得令者吉，故如人之家...
    """
    
    original_text: str = """- **原文（source_text）**：
  月令提纲，譬之宅也，人元用事之神，宅之向也，不可以不卜。

- 原注（原文注解）：
  　　令星，乃命之至要，宜气象得令者吉，喜神得令者吉，故如人之家宅，支藏之人元，如寅中戊土丙火甲木，辨其孰为用事，则可以取格，可以取用，故如宅之向也。（如寅月生人，立春后七日前，皆值戊土用事，八日后十四日前，丙火用事，十五日后，甲木用事，知此则可以取格，可以取用矣）。

- 分字分词释义：
  - 月令：当月用事之气，为全局“宅基”；
  - 提纲：总纲领之意，一切格局、体用多从此发端；
  - 用事之神：在该月内实际当权之人元；
  - 宅之向：宅基既定，其向所朝，即吉凶之分野。

- **规范化释义（primary_lang_explained）**：
  月令好比一座宅子的地基，人元用事之神好比宅子的坐向。先看哪一位在该月当令用事，再由此决定格局与用神；若连“宅”与“向”都未辨清，就谈格局高下与用神喜忌，便失其本。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 月令提纲 | Month Command (Yue-Ling) | 命之宅基 | Foundation of the chart | yueling_tigang | existing |
| 人元用事 | Hidden Stem Governing | 当令之神 | Ruling hidden stem | renyuan_yongshi | existing |
| 宅之向 | House Direction | 气之所向 | Direction of Qi | zhai_zhixiang | new_candidate |
| 分日用事 | Daily Governing | 月内分段 | Segments within month | fenri_yongshi | new_candidate |
| 取格 | Determine Pattern | 定格局 | Define the structure | quge | existing |
| 气象得令 | Qi Image in Season | 气象合时 | Qi matches season | qixiang_deling | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Yue-Ling (Month Command) is the "House" (Zhai), the Hidden Stem in charge (Ren-Yuan Yong-Shi) is the "Direction" (Xiang). Must divine (卜) these first. Even within the same month, different stems govern different days (e.g. Wu, Bing, Jia in Yin month). Knowing the specific "Yong-Shi" (governing spirit) determines the true Pattern and Yong-Shen."""
    normalized_text_zh: str = """"""
    subject: str = "月令提纲，譬之宅也，人元用事之神，宅之向也，不可以不卜。"
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
        l1_anchor="dts_v1.0.0_月令提纲_譬之宅也_人元用事之神_宅之向也_不可以不卜_001_L1",
    )
    version: str = "1.0.0"
