"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228449
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
    semantic_id="smth_v1.0.0_乙酉水性质_自败之水假众金相之_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙酉水性质自败之水假众金相之(SemanticEntry):
    """
    - **原文（source_text）**：
  乙酉水、自败之水，假众金以相之，盖我气既弱，藉母以育，忌己酉、己卯、戊申、庚子、辛丑之土，则夭折穷贱。

- **分字分词释义**：
  - **自败...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙酉水、自败之水，假众金以相之，盖我气既弱，藉母以育，忌己酉、己卯、戊申、庚子、辛丑之土，则夭折穷贱。

- **分字分词释义**：
  - **自败之水**：自己衰败的水。
  - **假众金以相之**：依靠众多金来帮助。
  - **我气既弱**：自己的气已经衰弱。
  - **藉母以育**：依靠母来养育。
  - **夭折穷贱**：短命贫贱。

- **规范化释义（primary_lang_explained）**：
  乙酉水，是自己衰败的水，依靠众多金来帮助，因为自己的气已经衰弱，依靠母（金生水）来养育，忌讳己酉、己卯、戊申、庚子、辛丑的土，遇之则短命贫贱。

- **完整对等诠释（secondary_lang_full）**：
  Yiyou Water is self-defeated water, relies on many Metals to assist, since own energy already weak, depends on mother (Metal) to nurture, avoids Jiyou, Jimao, Wushen, Gengzi, Xinchou Earth—encountering leads to premature death and poverty.

- **核心要点**：
  - 乙酉为泉中水，自败之水
  - 气弱需金生
  - 藉母育养
  - 忌多种土克

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_216]` `[trigger: 乙酉水性质]` `[factor_trigger: yiyou_water_self_defeated AND relies_many_metals AND avoid_many_earths]` `[role: 主干]` 乙酉水、自败之水，假众金以相之，盖我气既弱，藉母以育，忌己酉、己卯、戊申、庚子、辛丑之土，则夭折穷贱。 → 《三命通会》卷一#乙酉水性质

- **详细解说**：
  此条解释乙酉（泉中水）的性质。乙酉纳音也是水，但是自败之水（酉为水败地），气已衰弱，需要依靠众多的金来生养（金为水之母），忌讳己酉、己卯、戊申、庚子、辛丑等土的克制，遇之则短命贫贱。衰弱之水特别需要生扶，不能再受克制。

- **校勘与字词辨析（双语）**：
  - **中文**："自败"指酉为水的败地。"假"通"借"，依靠。"藉母以育"，金为水母，依靠金生养。"夭折"指短命。
  - **English**: "Self-defeated" means You is water's defeat position. "Relies on" means depends on. "Depends on mother to nurture"—Metal is water's mother, depends on Metal to nourish. "Premature death" means dying young."""
    normalized_text_zh: str = """"""
    subject: str = "乙酉水性质：自败之水假众金相之"
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
        l1_anchor="smth_v1.0.0_乙酉水性质_自败之水假众金相之_001_L1",
    )
    version: str = "1.0.0"
