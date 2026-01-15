"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997840
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
    semantic_id="dts_v1.0.0_何知其人寿_性定元气厚_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人寿性定元气厚(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人寿：此人长寿、寿命绵长。
  - 性定：性情安定、不妄动极端。
  - 元气厚：先天精气充沛、根基深厚。

- 规范化释义（pri...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人寿：此人长寿、寿命绵长。
  - 性定：性情安定、不妄动极端。
  - 元气厚：先天精气充沛、根基深厚。

- 规范化释义（primary_lang_explained）：
  论寿夭，长寿之人多半"性情安定、元气充厚"：命局中用神稳定、根气坚实，岁运虽有风波，整体气机仍能自我恢复，不致频繁被折损到根本层面。

- **核心要点**：
  - "性定"对应气机平和、不妄动极端；
  - "元气厚"对应根基深、关键部位少受重伤；
  - 长寿要看整体结构的耐久度，而非只看一时强旺。

- 校勘与字词辨析：
  - "元气"：不仅指身体精气，也象征命局整体的基础能量与恢复能力。

- **次语种完整诠释（secondary_lang_full）**：  
  Long life shows when temperament is steady and original qi is thick: the chart has solid roots, few direct blows to vital structures, and enough Resource and support to recover after shocks."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人寿，性定元气厚。"
    factor_refs: list = ['longevity_grade', 'temperament_stable', 'vitality_level', 'vitality_level']
    
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
        l1_anchor="dts_v1.0.0_何知其人寿_性定元气厚_001_L1",
    )
    version: str = "1.0.0"
