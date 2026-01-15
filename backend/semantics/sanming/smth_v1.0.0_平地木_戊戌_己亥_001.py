"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227718
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
    semantic_id="smth_v1.0.0_平地木_戊戌_己亥_001",
    book_id="sanming",
    engine_id="bazi"
)
class 平地木戊戌己亥(SemanticEntry):
    """
    - **原文（source_text）**：
  戊戌己亥，气归藏伏，阴阳闭塞，木气归根，伏乎土中，故曰平地木也。

- 分字分词释义：
  - **气归藏伏，阴阳闭塞**：气机收敛，外在动象减少，趋...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊戌己亥，气归藏伏，阴阳闭塞，木气归根，伏乎土中，故曰平地木也。

- 分字分词释义：
  - **气归藏伏，阴阳闭塞**：气机收敛，外在动象减少，趋向内藏。
  - **木气归根，伏乎土中**：木之气归于根部，潜伏土中，未见枝叶外张。

- **规范化释义（primary_lang_explained）**：
  戊戌、己亥之木，如潜伏平地之根木：木气多归于根部，外在枝叶不显，重在基础与内层结构，而不在表面之繁华。

- **完整对等诠释（secondary_lang_full）**：

  Wuxu and Jihai are called "Flatland Wood". Here the movement of Qi has closed in; Yin and Yang are relatively sealed, and Wood withdraws its force down into the roots, lying hidden in the level earth. Little shows above ground, yet below the surface structure is being laid and the foundation thickened. This Nayin therefore emphasises groundwork rather than display—building soil, stabilising systems, preparing fields for later planting. In a chart it often marks people or periods suited to base‑layer work: infrastructure, institutions, long‑term training, anything that carries others but does not seek the spotlight. It is not a sign of being doomed to obscurity, but of needing Water and Fire at the right time to draw shoots upward so that what has been patiently rooted can eventually be seen."""
    normalized_text_zh: str = """"""
    subject: str = "平地木（戊戌、己亥）"
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
        l1_anchor="smth_v1.0.0_平地木_戊戌_己亥_001_L1",
    )
    version: str = "1.0.0"
