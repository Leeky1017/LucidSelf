"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997362
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
    semantic_id="dts_v1.0.0_格局论_001",
    book_id="dts",
    engine_id="bazi"
)
class 格局论(SemanticEntry):
    """
    - **原文（source_text）**：
  格局层 L2 与因子模块总览。

- 规范化释义（primary_lang_explained）：
  本节不解某一条原文，而是作为全书格局论的总纲导...
    """
    
    original_text: str = """- **原文（source_text）**：
  格局层 L2 与因子模块总览。

- 规范化释义（primary_lang_explained）：
  本节不解某一条原文，而是作为全书格局论的总纲导论：一方面总结本书在格局层使用的 L2 语义模块（如“真格识别”“无格退阶”），另一方面梳理这些语义模块在工程侧对应的因子字段与激活窗口。核心目的是把“月令为纲、透干为标”的传统格局思路，翻译成一套可在多书之间复用的 L2+因子框架，既不僵硬固定某一套规则，又能给后续 L3 提供清晰接口。

- 完整对等诠释（secondary_lang_full）：
  This introductory section does not interpret a single classical line; instead, it outlines how Di Tian Sui uses L2 semantics and factor modules at the pattern level. It explains how concepts like "true pattern", "remote influence", and "no-pattern fallback" are turned into reusable semantic modules, and how these modules map onto factor fields and activation windows. The goal is to translate the traditional idea of "month branch as pivot, stems as manifestation" into a stable L2+factor framework that can be shared across books, while still leaving logical room for different rule designs at the L3 layer."""
    normalized_text_zh: str = """"""
    subject: str = "格局论"
    factor_refs: list = ['geju_type', 'yueling_key_god', 'tougan_status', 'zhen_ge', 'yao_xi', 'yong_shen']
    
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
        l1_anchor="dts_v1.0.0_格局论_001_L1",
    )
    version: str = "1.0.0"
