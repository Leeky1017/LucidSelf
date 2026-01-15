"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228471
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
    semantic_id="smth_v1.0.0_戊子火性质_神龙之火遇水方贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊子火性质神龙之火遇水方贵(SemanticEntry):
    """
    - **原文（source_text）**：
  戊子火、己丑火，水中之火，又曰神龙之火，遇水方贵，为六气之君火也。

- **分字分词释义**：
  - **水中之火**：水中的火。
  - **神...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊子火、己丑火，水中之火，又曰神龙之火，遇水方贵，为六气之君火也。

- **分字分词释义**：
  - **水中之火**：水中的火。
  - **神龙之火**：神龙之火。
  - **遇水方贵**：遇到水才尊贵。
  - **六气之君火**：六气中的君主之火。

- **规范化释义（primary_lang_explained）**：
  戊子火、己丑火，是水中的火，又叫神龙之火，遇到水才尊贵，是六气中的君主之火。

- **完整对等诠释（secondary_lang_full）**：
  Wuzi Fire and Jichou Fire are fire within water, also called Divine-Dragon Fire, encountering Water becomes noble, being sovereign fire among Six Energies.

- **核心要点**：
  - 戊子己丑为霹雳火，水中之火
  - 又称神龙之火
  - 遇水方贵（水火既济）
  - 六气君火

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_219]` `[trigger: 戊子火性质]` `[factor_trigger: wuzi_jichou_fire_in_water AND divine_dragon_fire AND water_brings_nobility]` `[role: 主干]` 戊子火、己丑火，水中之火，又曰神龙之火，遇水方贵，为六气之君火也。 → 《三命通会》卷一#戊子火性质

- **详细解说**：
  此条合论戊子己丑（霹雳火）的性质。二者纳音都是火，但如水中的火，又称神龙之火（雷电之火），遇到水才显贵（水火既济，阴阳调和），是六气中的君主之火（火为阳，主生发）。这是特殊的火，与水不相克反而相济。

- **校勘与字词辨析（双语）**：
  - **中文**："水中之火"指雷电之火。"神龙"象征雷电。"遇水方贵"指水火既济。"六气"指阴阳风雨晦明。
  - **English**: "Fire within water" refers to lightning fire. "Divine-Dragon" symbolizes thunder and lightning. "Encountering Water becomes noble" means water-fire harmony. "Six Energies" refers to yin-yang, wind-rain, obscurity-brightness."""
    normalized_text_zh: str = """"""
    subject: str = "戊子火性质：神龙之火遇水方贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_戊子火性质_神龙之火遇水方贵_001_L1",
    )
    version: str = "1.0.0"
