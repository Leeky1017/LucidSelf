"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997616
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
    semantic_id="dts_v1.0.0_一出门来要见儿_见儿成气转相楣_从儿不论身强弱_只要吾儿又遇_001",
    book_id="dts",
    engine_id="bazi"
)
class 一出门来要见儿见儿成气转相楣从儿不论身强弱只要吾儿又遇(SemanticEntry):
    """
    - **原文（source_text）**：
  一出门来要见儿，见儿成气转相楣。从儿不论身强弱，只要吾儿又遇儿。

- 原注（原文注解）（节要）：
  　　此与成象从象伤官不同，只取我生者为儿……是...
    """
    
    original_text: str = """- **原文（source_text）**：
  一出门来要见儿，见儿成气转相楣。从儿不论身强弱，只要吾儿又遇儿。

- 原注（原文注解）（节要）：
  　　此与成象从象伤官不同，只取我生者为儿……是为顺用，必然富贵。

- **规范化释义（primary_lang_explained）**：
  “顺用儿（我所生）”以成生育之势，重在“我子再生”之连锁；不拘身强身弱，但须一路相生成环。

- 分字分词释义：
  - 儿：我所生者（食神/伤官）。
  - 见儿成气：顺生链条成立而气脉转旺。"""
    normalized_text_zh: str = """"""
    subject: str = "一出门来要见儿，见儿成气转相楣，从儿不论身强弱，只要吾儿又遇儿。"
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
        l1_anchor="dts_v1.0.0_一出门来要见儿_见儿成气转相楣_从儿不论身强弱_只要吾儿又遇_001_L1",
    )
    version: str = "1.0.0"
