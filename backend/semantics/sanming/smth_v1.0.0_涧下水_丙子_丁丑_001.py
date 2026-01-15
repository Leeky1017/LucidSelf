"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227726
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
    semantic_id="smth_v1.0.0_涧下水_丙子_丁丑_001",
    book_id="sanming",
    engine_id="bazi"
)
class 涧下水丙子丁丑(SemanticEntry):
    """
    - **原文（source_text）**：
  丙子丁丑何以取象涧下水？盖气未通济，高段非水流之所，卑湿乃水就之乡，由地中行，故曰涧下水。

- 分字分词释义：
  - **涧下水**：指溪谷下方或...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙子丁丑何以取象涧下水？盖气未通济，高段非水流之所，卑湿乃水就之乡，由地中行，故曰涧下水。

- 分字分词释义：
  - **涧下水**：指溪谷下方或地中潜行之水，流量不大而重在润下。
  - **气未通济，高段非水流之所**：水势尚未通达开阔处，只在低洼之地运行。

- **规范化释义（primary_lang_explained）**：
  丙子、丁丑之水，如山涧下或地中潜行的小水：不见浩荡之势，而在低处暗暗流淌。象征资源有限、渠道狭窄，但能在局部滋润、默默支持。

- **完整对等诠释（secondary_lang_full）**：

  Bing Zi and Ding Chou correspond to "Stream‑Below Water". This is water that has not yet reached broad, open channels: it seeps and runs beneath the ground or at the bottom of ravines, gathering in low, damp places rather than surging across the landscape. Its volume is modest, but it quietly moistens what lies nearby. In destiny terms this Nayin speaks of small‑scale, localised resources and support—a talent or supply suited to serving a close circle, a team or a niche, rather than driving great public waves. When the surrounding Earth and Wood provide sound channels and containers, such water can be used with high efficiency for deep cultivation; when there is a mismatch between ambition and actual flow, frustration arises from asking a hidden stream to perform like a mighty river."""
    normalized_text_zh: str = """"""
    subject: str = "涧下水（丙子、丁丑）"
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
        l1_anchor="smth_v1.0.0_涧下水_丙子_丁丑_001_L1",
    )
    version: str = "1.0.0"
