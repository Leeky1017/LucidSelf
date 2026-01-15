"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228377
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
    semantic_id="smth_v1.0.0_乙亥火性质_伏明之火其气湮郁喜土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙亥火性质伏明之火其气湮郁喜土(SemanticEntry):
    """
    - **原文（source_text）**：
  乙亥火、火之热气，喜土，及夏天德曲脚。

- **分字分词释义**：
  - **火之热气**：火的热气。
  - **喜土及夏**：喜欢土和夏季。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙亥火、火之热气，喜土，及夏天德曲脚。

- **分字分词释义**：
  - **火之热气**：火的热气。
  - **喜土及夏**：喜欢土和夏季。
  - **天德**：天德贵人，吉神。
  - **曲脚**：曲脚煞。

- **规范化释义（primary_lang_explained）**：
  乙亥火，是火的热气，喜欢土和夏季，有天德贵人则吉，遇曲脚煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Yihai Fire is fire's hot energy, favoring Earth and summer season, auspicious with Heaven-Virtue Noble, inauspicious with Curved-Foot sha.

- **核心要点**：
  - 乙亥为山头火，如热气
  - 喜土（火生土显功）、夏季
  - 喜天德贵人
  - 忌曲脚煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_206]` `[trigger: 乙亥火性质]` `[factor_trigger: yihai_fire_hot_energy AND favor_earth_summer AND heaven_virtue_noble]` `[role: 主干]` 乙亥火、火之热气，喜土，及夏天德曲脚。 → 《三命通会》卷一#乙亥火性质

- **详细解说**：
  此条解释乙亥（山头火）的性质。乙亥纳音也是火，但如火的热气，虚而不实，喜欢土（火生土，有所归宿），喜欢夏季（火旺之时），有天德贵人则吉，但忌曲脚煞。火的热气需要土来承载才能发挥作用。

- **校勘与字词辨析（双语）**：
  - **中文**："火之热气"指火的热量和气息。"天德"为天德贵人，大吉之神。"曲脚"为曲脚煞，主残疾。
  - **English**: "Fire's hot energy" refers to fire's heat and breath. "Heaven-Virtue" is Heaven-Virtue Noble, greatly auspicious spirit. "Curved-Foot" is Curved-Foot sha, indicating disabilities."""
    normalized_text_zh: str = """"""
    subject: str = "乙亥火性质：伏明之火其气湮郁喜土"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_乙亥火性质_伏明之火其气湮郁喜土_001_L1",
    )
    version: str = "1.0.0"
