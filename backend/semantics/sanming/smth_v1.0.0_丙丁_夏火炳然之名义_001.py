"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227554
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
    semantic_id="smth_v1.0.0_丙丁_夏火炳然之名义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙丁夏火炳然之名义(SemanticEntry):
    """
    - **原文（source_text）**：
  丙丁其位火，行夏之令。丙，炳也，万物皆炳然著见而强大。丁，其强适能与阴气相丁。

- 分字分词释义：
  - **丙，炳也**：炳然显著之意，光明外露...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙丁其位火，行夏之令。丙，炳也，万物皆炳然著见而强大。丁，其强适能与阴气相丁。

- 分字分词释义：
  - **丙，炳也**：炳然显著之意，光明外露，万物尽见。
  - **丁，其强适能与阴气相丁**：丁火之强恰好能与阴气对接、相当，较丙更收敛细致。

- **规范化释义（primary_lang_explained）**：
  丙丁属夏火。丙火如烈日当空，光明炳然、一览无遗，象征显露、张扬、力量大开；丁火则像灯火、炉火，强度适中，可以与阴柔之物配合，不至于过烈。二火同属火性，却在明暗、粗细上有分工。

- **完整对等诠释（secondary_lang_full）**：

  Bing and Ding belong to Fire and command the summer season. Bing Fire is like the blazing midday sun: brilliant and overwhelming, driving away shadow so that everything is exposed and made strong and obvious. Ding Fire is like lamplight or hearth‑fire: its intensity is moderate, able to meet and work with Yin things without burning them up. Both are Fire, yet they divide Fire’s work between spectacular display and gentle, sustained warmth. In destiny reading, Bing Fire often appears as charisma, high visibility and forceful expression, whereas Ding Fire shows up as craftsmanship, care and the steady glow that keeps relationships and projects alive over time."""
    normalized_text_zh: str = """"""
    subject: str = "丙丁：夏火炳然之名义"
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
        l1_anchor="smth_v1.0.0_丙丁_夏火炳然之名义_001_L1",
    )
    version: str = "1.0.0"
