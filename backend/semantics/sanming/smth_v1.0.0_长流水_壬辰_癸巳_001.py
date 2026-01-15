"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227741
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
    semantic_id="smth_v1.0.0_长流水_壬辰_癸巳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 长流水壬辰癸巳(SemanticEntry):
    """
    - **原文（source_text）**：
  壬辰癸巳，势极东南，气傍离宫，火明势盛，水得归库，盈科后进，乃曰长流水也。

- 分字分词释义：
  - **长流水**：指长久不绝的大河之水，奔流不...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬辰癸巳，势极东南，气傍离宫，火明势盛，水得归库，盈科后进，乃曰长流水也。

- 分字分词释义：
  - **长流水**：指长久不绝的大河之水，奔流不息。
  - **盈科后进**：水满一处再进一处，比喻循序渐进、不断前行。

- **规范化释义（primary_lang_explained）**：
  壬辰、癸巳之水，如大河长流：一路奔向东南，沿途受火土之照拂而归于库地，象征持续不断的推进力与累积力。

- **完整对等诠释（secondary_lang_full）**：

  Ren Chen and Gui Si belong to "Long‑Flowing Water". Their water is like a great river running on toward the southeast: it travels a long path, passes near the Fire palace, and is gathered up in reservoirs along the way. The phrase "filling a hollow before moving on" captures its rhythm of pooling, then advancing again. This Nayin symbolises steady, sustained forward motion and the power of accumulation over distance, rather than short, sharp surges. In readings it points toward life routes and projects that are built through long‑term effort and staged milestones, where pacing, endurance and direction matter more than quick wins or speculative leaps."""
    normalized_text_zh: str = """"""
    subject: str = "长流水（壬辰、癸巳）"
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
        l1_anchor="smth_v1.0.0_长流水_壬辰_癸巳_001_L1",
    )
    version: str = "1.0.0"
