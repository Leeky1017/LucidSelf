"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227702
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
    semantic_id="smth_v1.0.0_杨柳木_壬午_癸未_001",
    book_id="sanming",
    engine_id="bazi"
)
class 杨柳木壬午癸未(SemanticEntry):
    """
    - **原文（source_text）**：
  壬午癸未，木至午而死，至未而墓，故杨柳盛夏叶凋，枝干微弱，取其性之柔也，故曰杨柳木。

- 分字分词释义：
  - **木至午而死，至未而墓**：在地...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬午癸未，木至午而死，至未而墓，故杨柳盛夏叶凋，枝干微弱，取其性之柔也，故曰杨柳木。

- 分字分词释义：
  - **木至午而死，至未而墓**：在地支运行中，木气至午而衰、至未而入墓。
  - **性之柔**：杨柳之性柔软，枝干细弱，随风而动。

- **规范化释义（primary_lang_explained）**：
  壬午、癸未之木，如盛夏时节的杨柳：表面枝叶繁茂，其实木气已近衰退之地，枝干柔弱、多受环境风向所摇。象征温柔、感性、易受外界影响的一类木气。

- **完整对等诠释（secondary_lang_full）**：

  Ren Wu and Gui Wei are imaged as "Willow Wood". By the calendar of the branches, Wood has reached the height of summer and is already moving toward decline; outwardly the foliage is still lush, but inwardly vitality is softening. Willow branches are fine, supple and easily stirred by the wind, capturing a type of Wood that is gentle, receptive and emotionally sensitive, more inclined to bend and accommodate than to push straight through. In destiny reading this Nayin describes people or phases that excel at smoothing tensions, responding to others’ needs and adapting to shifting environments, but who are vulnerable if they lack inner boundaries and grounding in Earth and Metal. When paired with sufficient stability and direction, Willow Wood becomes graceful flexibility; without it, it can slip into over‑pleasing, exhaustion or being carried entirely by the prevailing wind."""
    normalized_text_zh: str = """"""
    subject: str = "杨柳木（壬午、癸未）"
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
        l1_anchor="smth_v1.0.0_杨柳木_壬午_癸未_001_L1",
    )
    version: str = "1.0.0"
