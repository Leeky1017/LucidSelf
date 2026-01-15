"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654341
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
    semantic_id="zw_v1.0.0_金锁铁蛇关_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 金锁铁蛇关(SemanticEntry):
    """
    - 分字分词释义：

  - **金锁铁蛇关**：小儿关煞，四级推算定位危险宫位。
  - **关煞**：小儿命理中的危险关口。
  - **顺行逆数**：按地支顺序或逆序推算。
  - **丑未病有...
    """
    
    original_text: str = """- 分字分词释义：

  - **金锁铁蛇关**：小儿关煞，四级推算定位危险宫位。
  - **关煞**：小儿命理中的危险关口。
  - **顺行逆数**：按地支顺序或逆序推算。
  - **丑未病有救**：落在丑未宫位病可治。
  - **辰戌宫死**：落在辰戌宫位主凶险。

**主题**：小儿关煞推算。

从戌上起子年顺行至生年，年上起月逆数至生月，月上起日顺数至生日，日上起时逆数至生时。遇丑未宫病有救，辰戌宫死。

#### 完整对等诠释（secondary_lang_full·36金锁铁蛇关）：

  The Golden Lock and Iron Snake barrier is a childhood danger calculation. Starting from the Xu palace for Zi year, count forward to the birth year; from that palace count backward to the birth month; from that result count forward to the birth day; then count backward to the birth hour. The final palace indicates the danger zone. If the calculation lands in Chou or Wei, illness can be treated and recovery is possible; if it lands in Chen or Xu, the threat is severe and potentially fatal. This formula is specifically applied to young children's charts to identify periods of heightened vulnerability during early life."""
    normalized_text_zh: str = """"""
    subject: str = "金锁铁蛇关"
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_金锁铁蛇关_001_L1",
    )
    version: str = "1.0.0"
