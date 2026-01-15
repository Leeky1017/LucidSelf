"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227673
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
    semantic_id="smth_v1.0.0_白蜡金_庚辰_辛巳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 白蜡金庚辰辛巳(SemanticEntry):
    """
    - **原文（source_text）**：
  庚辰辛巳以金居火土之地，气已发生，金尚在矿，寄形生养之乡，受西方之正色，乃曰白蜡金。

- 分字分词释义：
  - **金居火土之地**：金处于火土旺...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚辰辛巳以金居火土之地，气已发生，金尚在矿，寄形生养之乡，受西方之正色，乃曰白蜡金。

- 分字分词释义：
  - **金居火土之地**：金处于火土旺地，正当发生、炼化之位。
  - **金尚在矿**：金仍在矿脉之中，尚未显露成器。
  - **白蜡金**：比喻色泽未纯、质地尚待提炼之金，如白蜡般可雕可塑。

- **规范化释义（primary_lang_explained）**：
  庚辰、辛巳之金，如列于火土之中的矿金：气机已起，受火土熬炼，却仍未完全成器，有很强的可塑性。既有被锻炼、雕琢的过程，也有「成败在后」的意味。

- **完整对等诠释（secondary_lang_full）**：

  Geng Chen and Xin Si are grouped under "White Wax Metal". Metal here dwells in the territory of Fire and Earth: its Qi has already been stirred and is undergoing baking and smelting, but it is still locked in the ore, like soft white wax placed in a mould. This suggests a state of being in the furnace rather than already forged—a metal quality that is highly malleable and full of possibility, yet also vulnerable if heat and pressure are mishandled. In practice it points to lives or phases marked by intensive training, discipline and restructuring, where trials serve to shape character and skill. When Fire and Earth work together in balanced fashion, White Wax Metal can emerge as strong, serviceable implements; when either is excessive or deficient, the same process may crack, warp or waste material that might otherwise have become fine iron or steel."""
    normalized_text_zh: str = """"""
    subject: str = "白蜡金（庚辰、辛巳）"
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
        l1_anchor="smth_v1.0.0_白蜡金_庚辰_辛巳_001_L1",
    )
    version: str = "1.0.0"
