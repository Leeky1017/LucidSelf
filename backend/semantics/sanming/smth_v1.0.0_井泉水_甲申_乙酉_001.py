"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227758
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
    semantic_id="smth_v1.0.0_井泉水_甲申_乙酉_001",
    book_id="sanming",
    engine_id="bazi"
)
class 井泉水甲申乙酉(SemanticEntry):
    """
    - **原文（source_text）**：
  甲申乙酉，气息安静，子母同位，出而不穷，汲而不竭，乃曰井泉水。

- 分字分词释义：
  - **气息安静**：气机平稳，不急不躁。
  - **出而...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲申乙酉，气息安静，子母同位，出而不穷，汲而不竭，乃曰井泉水。

- 分字分词释义：
  - **气息安静**：气机平稳，不急不躁。
  - **出而不穷，汲而不竭**：水源稳定持久，如井泉长流。

- **规范化释义（primary_lang_explained）**：
  甲申、乙酉之水，如深井泉眼：外观平静，却有稳定水源，汲之不竭。象征稳健、持续的资源与内在生机。

- **完整对等诠释（secondary_lang_full）**：

  Jia Shen and Yi You correspond to "Well‑Spring Water". On the surface the scene is quiet and uneventful, yet beneath lies a deep, steady source that can be drawn on without quickly running dry. The emphasis is on stability and sustainability rather than spectacle: this Nayin speaks of underlying resources, stamina or backing that support life and work over the long haul. In charts it often marks people or situations with reliable but unshowy supply—long‑term clients, enduring relationships, physical resilience, a solid base of skills. Protection and sensible use of the surrounding "earth" are crucial: good structures act like well‑walls that safeguard and channel the water, while negligence or over‑pumping can leave the well blocked or exhausted."""
    normalized_text_zh: str = """"""
    subject: str = "井泉水（甲申、乙酉）"
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
        l1_anchor="smth_v1.0.0_井泉水_甲申_乙酉_001_L1",
    )
    version: str = "1.0.0"
