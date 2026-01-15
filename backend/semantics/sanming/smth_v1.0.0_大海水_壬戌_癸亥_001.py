"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227766
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
    semantic_id="smth_v1.0.0_大海水_壬戌_癸亥_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大海水壬戌癸亥(SemanticEntry):
    """
    - **原文（source_text）**：
  壬戌癸亥，天门之地，气归闭塞，水历遍而不趋，势归乎宁谧之位，来之不穷，纳之不溢，乃曰大海水也。

- 分字分词释义：
  - **大海水**：指无涯之...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬戌癸亥，天门之地，气归闭塞，水历遍而不趋，势归乎宁谧之位，来之不穷，纳之不溢，乃曰大海水也。

- 分字分词释义：
  - **大海水**：指无涯之海水，容量极大。
  - **来之不穷，纳之不溢**：来多少受多少，难以盈满，喻包容量极强。

- **规范化释义（primary_lang_explained）**：
  壬戌、癸亥之水，如无垠大海：气机遍行而终归平静，来水不尽、纳水不溢。象征胸襟宽广、承载力大，亦可表环境宏大、变数复杂。

- **完整对等诠释（secondary_lang_full）**：

  Ren Xu and Gui Hai are gathered under "Great Sea Water". Their water is like a boundless ocean: currents roam widely yet settle into a broad, quiet surface; whatever flows in is received without easily overflowing. This symbolises vast capacity and tolerance—the ability to hold many people, stories and influences—as well as environments that are large‑scale and complex. In a chart, Dahai Water often points to dealings with distant places, big systems or cross‑boundary fields, and to a temperament inclined toward wide horizons. Its gifts are breadth and endurance; its risks are loss of focus and being swamped. Only when Wood (direction, values) and Earth (structure, institutions) are strong enough to steer and contain it can an ocean of Qi be turned into navigable routes instead of aimless, exhausting drift."""
    normalized_text_zh: str = """"""
    subject: str = "大海水（壬戌、癸亥）"
    factor_refs: list = ['source_ref']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_大海水_壬戌_癸亥_001_L1",
    )
    version: str = "1.0.0"
