"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997762
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
    semantic_id="dts_v1.0.0_清得静时黄榜客_虽杂浊气亦中式_001",
    book_id="dts",
    engine_id="bazi"
)
class 清得静时黄榜客虽杂浊气亦中式(SemanticEntry):
    """
    - **原文（source_text）**：
  清得静时黄榜客，虽杂浊气亦中式。

- 原注（原文注解）：
 　　清而尽、安顿得所，虽略浊亦可发科。

- 分字分词释义：
  - 清得静时：清气能安...
    """
    
    original_text: str = """- **原文（source_text）**：
  清得静时黄榜客，虽杂浊气亦中式。

- 原注（原文注解）：
 　　清而尽、安顿得所，虽略浊亦可发科。

- 分字分词释义：
  - 清得静时：清气能安定下来。
  - 黄榜客：金榜题名之人。
  - 虽杂浊气：虽有些许杂乱浊气。
  - 亦中式：仍可及第。

- 规范化释义（primary_lang_explained）：
  若命局之清气能够收束而不外泄，并在适当宫位“安顿得所”，则即便夹带少许浊气，仍有机会在科第上中式上榜。换言之，关键在“清得其所、静中有承”，而非一味追求绝对无浊。

- **核心要点**：
  - 清气须“得静、得所”，方能承载科名；
  - 略带浊气并非全无科第之望，重在主线是否清稳；
  - 断科第不可拘泥于“全清无浊”的理想模式。

- 详细解说：
  很多命局难免杂气，但只要主干之官印清正、学业与人格所依之宫位安稳，杂气多退居陪衬，不足以坏大局。此句提醒：判断科第，不必苛求“纯阳纯阴、全清无浊”，而要看清的一端是否能静定、是否有稳定的承载点（如提纲、日座、用神所依之支）。一旦“清得静时”，便有可能在关键考试年份展现出来，成为“黄榜客”。

- 校勘与字词辨析：
  - “黄榜客”：指金榜题名之人，科举中式者。
  - “清得静时”：既有清气，又能安静不被杂气搅扰之时机与状态。

- **次语种完整诠释（secondary_lang_full）**:
  Clear-quiet清得静 achieves-yellow-list黄榜客: even-if虽 mixed-turbid-qi杂浊气 also-passes亦中式—key关键 in清静 clear-quiet不在纯粹 not-pure-only but可容杂 tolerates-mixed若能静定 if-can-be-still."""
    normalized_text_zh: str = """"""
    subject: str = "清得静时黄榜客，虽杂浊气亦中式。"
    factor_refs: list = ['clear_quiet_level', 'keju_rank', 'turbid_energy_flag', 'keju_rank', 'mixture_tolerance']
    
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
        l1_anchor="dts_v1.0.0_清得静时黄榜客_虽杂浊气亦中式_001_L1",
    )
    version: str = "1.0.0"
