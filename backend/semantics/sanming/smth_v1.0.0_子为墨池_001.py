"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042641
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
    semantic_id="smth_v1.0.0_子为墨池_001",
    book_id="sanming",
    engine_id="bazi"
)
class 子为墨池(SemanticEntry):
    """
    - **原文（source_text）**：
  子为墨池。子在正北方，属水，色象墨，故有墨池之象。凡命逢子年生者，时喜见癸亥，谓之水归大海，又谓之双鱼游墨，必为文章士矣。

- **分字分词释义**...
    """
    
    original_text: str = """- **原文（source_text）**：
  子为墨池。子在正北方，属水，色象墨，故有墨池之象。凡命逢子年生者，时喜见癸亥，谓之水归大海，又谓之双鱼游墨，必为文章士矣。

- **分字分词释义**：
  - **墨池**：以墨色喻北方子水之深沉与静黑，如砚池之水。
  - **正北方属水**：对应先天八卦坎位，主寒水之地。
  - **水归大海、双鱼游墨**：形容子水遇亥水，会成大水之势，多主文章才气。

- **规范化释义（primary_lang_explained）**：
  子位在正北，属水，色象如墨，故名「墨池」。子年生人若时支再见癸亥，好比小水归大海、双鱼游于墨池之中，水势深广而不竭，多主文思敏捷、读书写作有根柢。此处强调的是子水与亥水相会时，水势由一隅扩展为江海的变化。

- **完整对等诠释（secondary_lang_full）**：
  Zi, at true north, is pictured as an inkstone pool. It belongs to Water and takes on a dark, inky colour: calm on the surface yet deep and saturated within, like a well of ink that can feed the brush again and again. A person born in a Zi year who meets Gui and Hai at the hour is likened to “small water returning to the great sea” or “twin fish swimming in ink”: the narrow stream of personal experience is joined to a broad reservoir of collective memory and learning. In such charts, thought and language draw from a deep, quiet source; there is room for long reading, careful writing, and sustained reflection rather than only quick impressions. This passage therefore uses Zi not only as cold winter water, but as a dedicated reservoir for study, books, and inner images—a space where material is stored, darkened, and made ready for future use."""
    normalized_text_zh: str = """"""
    subject: str = "子为墨池"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_子为墨池_001_L1",
    )
    version: str = "1.0.0"
