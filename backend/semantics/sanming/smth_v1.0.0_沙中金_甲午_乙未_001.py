"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227680
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
    semantic_id="smth_v1.0.0_沙中金_甲午_乙未_001",
    book_id="sanming",
    engine_id="bazi"
)
class 沙中金甲午乙未(SemanticEntry):
    """
    - **原文（source_text）**：
  甲午乙未则气已成，物质自坚实，混于沙而别于沙，居于火而炼于火，乃曰沙中金也。

- 分字分词释义：
  - **混于沙而别于沙**：金与沙混杂却可被识...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲午乙未则气已成，物质自坚实，混于沙而别于沙，居于火而炼于火，乃曰沙中金也。

- 分字分词释义：
  - **混于沙而别于沙**：金与沙混杂却可被识别出来，喻藏于常物之中而自有贵气.
  - **居于火而炼于火**：在火地之中接受熬炼，使其坚实成材.

- **规范化释义（primary_lang_explained）**：
  甲午、乙未之金，已经有坚实之质，只是掺杂在沙砾之间，需要经过火炼才能显露其价值.象征在平凡环境或纷杂局势中自有真材实料，但往往需要机缘与筛选.

- **完整对等诠释（secondary_lang_full）**：

  Jiawu and Yiwei make up "Metal in the Sand". Here the Metal is already firm in nature, but mixed in with grains of sand: real quality buried in a mass of ordinary matter. Dwelling in the region of Fire, it must be repeatedly heated and refined for that value to stand out. This points to people or phases where solid ability is present in commonplace or chaotic environments—on the shop floor, among crowds, or in rough conditions—and only through processes of sifting, testing and tempering do they become recognisably "true gold". In fate reading this Nayin often signals a path of rising from the grassroots: not a life fated to hardship for its own sake, but one in which selection mechanisms, competition and hard work are the necessary means by which genuine strength is separated from the surrounding sand."""
    normalized_text_zh: str = """"""
    subject: str = "沙中金（甲午、乙未）"
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
        l1_anchor="smth_v1.0.0_沙中金_甲午_乙未_001_L1",
    )
    version: str = "1.0.0"
