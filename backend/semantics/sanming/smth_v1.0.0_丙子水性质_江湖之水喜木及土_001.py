"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228383
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
    semantic_id="smth_v1.0.0_丙子水性质_江湖之水喜木及土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙子水性质江湖之水喜木及土(SemanticEntry):
    """
    - **原文（source_text）**：
  丙子水、江湖喜木及土，福星官贵，平头聋哑，交神飞刃。

- **分字分词释义**：
  - **江湖**：江河湖泊。
  - **喜木及土**：喜欢木...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙子水、江湖喜木及土，福星官贵，平头聋哑，交神飞刃。

- **分字分词释义**：
  - **江湖**：江河湖泊。
  - **喜木及土**：喜欢木和土。
  - **交神**：交神煞。
  - **飞刃**：飞刃煞。

- **规范化释义（primary_lang_explained）**：
  丙子水，是江河湖泊之水，喜欢木和土，有福星、官贵星则吉，遇平头煞、聋哑煞、交神煞、飞刃煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Bingzi Water is river-lake water, favoring Wood and Earth, auspicious with Fortune Star and Official-Nobility Star, inauspicious with Level-Head sha, Deaf-Mute sha, Crossing-Spirit sha, and Flying-Blade sha.

- **核心要点**：
  - 丙子为涧下水，如江湖
  - 喜木（水生木）、土（土制水）
  - 喜福星、官贵
  - 忌多种凶煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_207]` `[trigger: 丙子水性质]` `[factor_trigger: bingzi_water_river_lake AND favor_wood_earth AND official_nobility]` `[role: 主干]` 丙子水、江湖喜木及土，福星官贵，平头聋哑，交神飞刃。 → 《三命通会》卷一#丙子水性质

- **详细解说**：
  此条解释丙子（涧下水）的性质。丙子纳音为水，如江河湖泊之水，浩荡流动，喜欢木（水生木有用）和土（土来制水不泛滥），有福星、官贵星则吉，但忌平头煞、聋哑煞、交神煞、飞刃煞等凶煞。江湖之水需要疏导和制约才不泛滥成灾。

- **校勘与字词辨析（双语）**：
  - **中文**："江湖"指大江大河湖泊。"交神"为交神煞。"飞刃"为飞刃煞，主血光之灾。
  - **English**: "River-lake" refers to great rivers and lakes. "Crossing-Spirit" is Crossing-Spirit sha. "Flying-Blade" is Flying-Blade sha, indicating bloodshed disasters."""
    normalized_text_zh: str = """"""
    subject: str = "丙子水性质：江湖之水喜木及土"
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
        l1_anchor="smth_v1.0.0_丙子水性质_江湖之水喜木及土_001_L1",
    )
    version: str = "1.0.0"
