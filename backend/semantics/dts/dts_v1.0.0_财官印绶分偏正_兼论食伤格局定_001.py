"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997371
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
    semantic_id="dts_v1.0.0_财官印绶分偏正_兼论食伤格局定_001",
    book_id="dts",
    engine_id="bazi"
)
class 财官印绶分偏正兼论食伤格局定(SemanticEntry):
    """
    - **原文（source_text）**：
  财官印绶分偏正，兼论食伤格局定。

- 原注（原文注解）：
  　　自形象方局之外而格为最，格之真者，月支之神，透于天干也，(格局看月支要紧)以散乱之...
    """
    
    original_text: str = """- **原文（source_text）**：
  财官印绶分偏正，兼论食伤格局定。

- 原注（原文注解）：
  　　自形象方局之外而格为最，格之真者，月支之神，透于天干也，(格局看月支要紧)以散乱之天干，而寻其得所附于提纲者，非格也，自偏正官财食伤印八格之外，若曲直等格皆为格，而以刑冲破害论者，亦不可言格也。

- 分字分词释义：
  - 财官印绶：指正偏财、正偏官（七煞）、正偏印（枭）等纲要之神。
  - 分偏正：分辨正格与偏格（正官/七杀、正财/偏财、正印/偏印）。
  - 食伤：食神、伤官，为泄秀之神，亦能独立成格。
  - 格局：以月令为提纲、以透干为标志而立之“格”；非凡有名目者皆可称格。

 - **规范化释义（primary_lang_explained）**：
  在形象、方局之上，格局是更高一层的总纲。所谓“真格”，是指月支所藏之神透出于天干，以月令为纲、透干为领；若只是天干散乱，再事后硬去附会到提纲之神，那都不算格。除常见的官、财、食伤、印八格之外，曲直、炎上、稼穑等专气之格也都是“格”，但只拿刑、冲、破、害来谈，就已经离开“格”的本义，而只是讨论对格的作用了。

- **次语种完整诠释（secondary_lang_full）**:  
  Pattern格局 established via月令pivot透干manifestation: 真格 true-pattern requires提纲之神 month-branch-god有力透干 stem-expression不可散乱附会 scattered-attribution—官财印食伤八格 eight-primary plus曲直炎上 specialized-patterns constitute格谱 pattern-taxonomy; 刑冲破害 punishment-clash affects格 existing-pattern not立格条件 pattern-establishment; 月令为纲透干为标 month-pivot-stem-标志 as structural-anchor avoiding伪格 pseudo-patterns."""
    normalized_text_zh: str = """"""
    subject: str = "财官印绶分偏正，兼论食伤格局定。"
    factor_refs: list = ['caiguanyinxiu', 'pianzheng', 'shishang', 'gejuding', 'yueling_weigang', 'tougan_weibiao']
    
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
        l1_anchor="dts_v1.0.0_财官印绶分偏正_兼论食伤格局定_001_L1",
    )
    version: str = "1.0.0"
