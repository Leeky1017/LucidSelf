"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227733
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
    semantic_id="smth_v1.0.0_大溪水_甲寅_乙卯_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大溪水甲寅乙卯(SemanticEntry):
    """
    - **原文（source_text）**：
  甲寅乙卯，气出阳明，水势恃源，东流滔注，其势浸大，故曰大溪水。

- 分字分词释义：
  - **气出阳明**：水源自高处显露，阳气渐盛。
  - *...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲寅乙卯，气出阳明，水势恃源，东流滔注，其势浸大，故曰大溪水。

- 分字分词释义：
  - **气出阳明**：水源自高处显露，阳气渐盛。
  - **水势恃源，东流滔注**：有稳定水源支撑，水势愈流愈大。

- **规范化释义（primary_lang_explained）**：
  甲寅、乙卯之水，如山间大溪：源头清晰，流向明确，愈行愈广。象征起步虽在山间，但有稳定供给与发展空间，适合顺势扩张。

- **完整对等诠释（secondary_lang_full）**：

  Jia Yin and Yi Mao give the image of a "mountain stream". The source of the water is clear and high, its direction is set, and as it flows eastward it gathers more tributaries and grows broader. The chart may start from a tucked‑away place, but it has a steady supply of Qi and room to develop, favouring paths where one rides existing channels rather than forcing a way upstream. In practice this Nayin often signals people or phases that are well suited to scaling up along a defined development corridor—using platforms, routes and institutions that already exist—rather than relying on solitary struggle with no riverbed to follow."""
    normalized_text_zh: str = """"""
    subject: str = "大溪水（甲寅、乙卯）"
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
        l1_anchor="smth_v1.0.0_大溪水_甲寅_乙卯_001_L1",
    )
    version: str = "1.0.0"
