"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654363
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
    semantic_id="zw_v1.0.0_十二宫星辰落闲宫_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 十二宫星辰落闲宫(SemanticEntry):
    """
    - 分字分词释义：

  - **闲宫**：星曜不得力之地，力量减弱。
  - **紫微子宫辰亥闲**：紫微在子宫时，辰亥为其闲宫。
  - **贪狼寅申闲**：贪狼星在寅申宫为闲地。
  - **七...
    """
    
    original_text: str = """- 分字分词释义：

  - **闲宫**：星曜不得力之地，力量减弱。
  - **紫微子宫辰亥闲**：紫微在子宫时，辰亥为其闲宫。
  - **贪狼寅申闲**：贪狼星在寅申宫为闲地。
  - **七杀辰亥闲**：七杀星在辰亥宫为闲地。
  - **不得力**：星曜在该宫位无法充分发挥作用。

- 紫微子宫：辰亥为闲
- 贪狼：寅申为闲
- 天相：辰戌为闲
- 七杀：辰亥为闲
- 天梁：巳酉为闲
- 天机：巳为闲
- 破军：巳申为闲
- 武曲：申为闲

#### 完整对等诠释（secondary_lang_full·39落闲宫）：

  The "idle palace" table identifies positions where major stars lose effectiveness. Ziwei in Zi has Chen and Hai as idle zones; Tanlang finds Yin and Shen idle; Tianxiang has Chen and Xu; Qisha has Chen and Hai; Tianliang has Si and You; Tianji has Si; Pojun has Si and Shen; Wuqu has Shen. When a star occupies its idle palace, its intrinsic strength cannot fully manifest—wealth stars yield less wealth, authority stars command less respect, and even malefics may cause less direct harm but also less transformative pressure. Recognizing idle placements helps the astrologer calibrate expectations and avoid over-interpreting stars that sit in structurally weak positions."""
    normalized_text_zh: str = """"""
    subject: str = "十二宫星辰落闲宫"
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
        l1_anchor="zw_v1.0.0_十二宫星辰落闲宫_001_L1",
    )
    version: str = "1.0.0"
