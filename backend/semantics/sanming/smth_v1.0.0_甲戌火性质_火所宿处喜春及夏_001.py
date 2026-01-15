"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228369
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
    semantic_id="smth_v1.0.0_甲戌火性质_火所宿处喜春及夏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲戌火性质火所宿处喜春及夏(SemanticEntry):
    """
    - **原文（source_text）**：
  甲戌火、火所宿处，喜春及夏。正印华盖平头，悬针破字棒杖。

- **分字分词释义**：
  - **火所宿处**：火停留的地方。
  - **喜春及夏...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲戌火、火所宿处，喜春及夏。正印华盖平头，悬针破字棒杖。

- **分字分词释义**：
  - **火所宿处**：火停留的地方。
  - **喜春及夏**：喜欢春季和夏季。
  - **正印**：正印格。

- **规范化释义（primary_lang_explained）**：
  甲戌火，是火停留的地方，喜欢春季和夏季，有正印格、华盖星则吉，遇平头煞、悬针煞、破字煞、棒杖煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Jiaxu Fire is place where fire dwells, favoring spring and summer seasons, auspicious with Proper Seal pattern and Canopy Star, inauspicious with Level-Head sha, Suspended-Needle sha, Broken-Character sha, and Club-Staff sha.

- **核心要点**：
  - 甲戌为山头火，火之宿处
  - 喜春夏（火旺时节）
  - 喜正印、华盖
  - 忌多种凶煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_205]` `[trigger: 甲戌火性质]` `[factor_trigger: jiaxu_fire_dwelling AND favor_spring_summer AND proper_seal]` `[role: 主干]` 甲戌火、火所宿处，喜春及夏。正印华盖平头，悬针破字棒杖。 → 《三命通会》卷一#甲戌火性质

- **详细解说**：
  此条解释甲戌（山头火）的性质。甲戌纳音为火，是火停留休息的地方，喜欢春夏季节（火旺之时），有正印格、华盖星则吉，但忌平头煞、悬针煞、破字煞、棒杖煞等凶煞。山头火需要旺盛的季节才能显现。

- **校勘与字词辨析（双语）**：
  - **中文**："火所宿处"指火停留之处。"春夏"为火旺季节。"正印"为生我之格，主文贵。
  - **English**: "Place where fire dwells" means where fire resides. "Spring-summer" are fire-flourishing seasons. "Proper Seal" is pattern of what generates me, indicating literary honor."""
    normalized_text_zh: str = """"""
    subject: str = "甲戌火性质：火所宿处喜春及夏"
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
        l1_anchor="smth_v1.0.0_甲戌火性质_火所宿处喜春及夏_001_L1",
    )
    version: str = "1.0.0"
