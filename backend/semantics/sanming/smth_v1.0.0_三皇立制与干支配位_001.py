"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227514
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
    semantic_id="smth_v1.0.0_三皇立制与干支配位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 三皇立制与干支配位(SemanticEntry):
    """
    - **原文（source_text）**：
  谓之天皇氏者，取其天开于子之义也；谓之地皇氏者，取其地辟于丑之义也；谓之人皇氏者，取其人生于寅之义也。故干支之名在天皇时始制，而地皇氏则定三辰，道分昼...
    """
    
    original_text: str = """- **原文（source_text）**：
  谓之天皇氏者，取其天开于子之义也；谓之地皇氏者，取其地辟于丑之义也；谓之人皇氏者，取其人生于寅之义也。故干支之名在天皇时始制，而地皇氏则定三辰，道分昼夜，以三十日为一月，而干支始各有所配。人皇氏者，主不虚王，臣不虚贵，政教君臣所自起，饮食男女所自始，始得天地之气而有子母之分，于是干支始有所属焉。

- 分字分词释义：
  - **天皇/地皇/人皇**：传说中三皇之名，分别象征天地人三才的开辟与治理。
  - **三辰**：日月星辰的总称，用以标定昼夜与时序。
  - **子母之分**：指干为母、支为子，干支相配以纪年岁日时。
- **规范化释义（primary_lang_explained）**：
  本段以三皇传说说明干支制度的逐步完备：天皇氏时代创制干支名称，以「子开天、丑辟地、寅生人」来对应天地人三才；地皇氏则进一步确定日月星辰的运行，划分昼夜、制定一月三十日之制，使干支开始有了具体配属；到人皇氏时，君臣秩序与人伦生活渐次建立，干支系统也由此真正落实到人世，形成「干为母、支为子」的配属格局。
  - **English**：
    - Foundational terminology explained with examples; classical categorization preserved with modern structural analysis.


- **完整对等诠释（secondary_lang_full）**：

  The legend of the Three Sovereigns is used here to describe how the stem–branch system gradually took shape. Under the Heavenly Sovereign, the basic names of stems and branches were created, with Zi "opening heaven", Chou "clearing earth", and Yin "bringing forth humankind", mapping them onto the three powers of Heaven, Earth and Human. The Earthly Sovereign then fixed the motions of sun, moon and stars, divided day and night, and set up a thirty‑day month, so that stems and branches could be assigned to concrete time segments. Under the Human Sovereign, political order and human relationships emerged; from then on the stem–branch system was fully applied to human affairs, forming the pattern of "stems as mothers, branches as children" that underlies the four pillars of year, month, day and hour. For destiny work this story encodes the idea that each pillar locates a person simultaneously within cosmic time, social order and family lineage."""
    normalized_text_zh: str = """"""
    subject: str = "三皇立制与干支配位"
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
        l1_anchor="smth_v1.0.0_三皇立制与干支配位_001_L1",
    )
    version: str = "1.0.0"
