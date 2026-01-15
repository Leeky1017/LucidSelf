"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228420
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
    semantic_id="smth_v1.0.0_辛巳金性质_金之生处精神具足_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛巳金性质金之生处精神具足(SemanticEntry):
    """
    - **原文（source_text）**：
  辛巳金、金之生处精神具足，体气完备，炎烈炙化而不亡。忌丙辰、乙巳、戊午之火。

- **分字分词释义**：
  - **金之生处**：金生长的地方。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  辛巳金、金之生处精神具足，体气完备，炎烈炙化而不亡。忌丙辰、乙巳、戊午之火。

- **分字分词释义**：
  - **金之生处**：金生长的地方。
  - **精神具足**：精神充足完备。
  - **体气完备**：形体气质完备。
  - **炎烈炙化而不亡**：即使遇到炽热的火也不会灭亡。

- **规范化释义（primary_lang_explained）**：
  辛巳金，是金生长的地方，精神充足完备，形体气质完备，即使遇到炽热的火也不会灭亡。但忌讳丙辰、乙巳、戊午等火。

- **完整对等诠释（secondary_lang_full）**：
  Xinsi Metal is where metal is born, spirit fully sufficient, bodily energy complete, even blazing intense fire cannot destroy it. However, avoids Bingchen, Yisi, Wuwu fires.

- **核心要点**：
  - 辛巳为白镴金，金生之地
  - 精神体气完备
  - 不畏一般火
  - 忌丙辰、乙巳、戊午火

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_212]` `[trigger: 辛巳金性质]` `[factor_trigger: xinsi_metal_birth_place AND spirit_fully_sufficient AND avoid_intense_fire]` `[role: 主干]` 辛巳金、金之生处精神具足，体气完备，炎烈炙化而不亡。忌丙辰、乙巳、戊午之火。 → 《三命通会》卷一#辛巳金性质

- **详细解说**：
  此条解释辛巳（白镴金）的性质。辛巳纳音也是金，是金生长的地方（巳为金长生位），精神充足，形体气质完备，一般的火不能克制（因为金气强盛），但忌讳丙辰（佛灯火）、乙巳（覆灯火）、戊午（天上火）等特别强烈的火。金生之地有自我保护的能力。

- **校勘与字词辨析（双语）**：
  - **中文**："金之生处"指巳为金的长生位。"精神具足"指精神饱满。"炎烈炙化"指猛烈的火焰。
  - **English**: "Where metal is born" means Si is metal's longevity position. "Spirit fully sufficient" means vigorous spirit. "Blazing intense fire" means fierce flames."""
    normalized_text_zh: str = """"""
    subject: str = "辛巳金性质：金之生处精神具足"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_辛巳金性质_金之生处精神具足_001_L1",
    )
    version: str = "1.0.0"
