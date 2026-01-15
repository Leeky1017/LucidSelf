"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227710
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
    semantic_id="smth_v1.0.0_石榴木_庚申_辛酉_001",
    book_id="sanming",
    engine_id="bazi"
)
class 石榴木庚申辛酉(SemanticEntry):
    """
    - **原文（source_text）**：
  庚申辛酉，五行为金而纳音属木，以相克取之。盖木性辛者，唯石榴木；申酉气归静肃，物渐成实，木居金地，其味成辛，故曰石榴木；观他木至午而死，惟此木至午而旺...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚申辛酉，五行为金而纳音属木，以相克取之。盖木性辛者，唯石榴木；申酉气归静肃，物渐成实，木居金地，其味成辛，故曰石榴木；观他木至午而死，惟此木至午而旺，取其性之偏也。

- 分字分词释义：
  - **五行为金而纳音属木**：干支本属金位，而纳音却为木，以克中取象。
  - **木性辛**：少见的“味辛之木”，以石榴为代表，果味偏辛。
  - **性之偏**：与常木不同，此木在午位反而旺盛，性情有其特异之处。

- **规范化释义（primary_lang_explained）**：
  庚申、辛酉之木，如石榴木：外在处于金地，却内里为木性，且味带辛烈。它在一般木气衰退的午位反而旺盛，显示性情与运作方式都有偏激、特立的一面。

- **完整对等诠释（secondary_lang_full）**：

  Geng Shen and Xin You are assigned to "Pomegranate Wood". On the surface they belong to the Metal sector, yet their Nayin is Wood, and not the usual mild kind but wood with a pungent, "spicy" taste. At a time and place where ordinary Wood is already weakening, this tree still takes root and ripens fruit, showing a nature that runs against the grain. It suggests growth under restriction, sharpness within softness, and talents that flourish in strict, rule‑bound or harsh environments. Interpreted well, this becomes an unconventional advantage: the capacity to thrive in niches, cross‑border fields or demanding systems where others find it hard to survive. Without guidance and integration, however, the same peculiarity can harden into contrariness, conflict with the mainstream, or a life spent at odds with prevailing norms."""
    normalized_text_zh: str = """"""
    subject: str = "石榴木（庚申、辛酉）"
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
        l1_anchor="smth_v1.0.0_石榴木_庚申_辛酉_001_L1",
    )
    version: str = "1.0.0"
