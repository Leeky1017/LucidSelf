"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228391
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
    semantic_id="smth_v1.0.0_丁丑水性质_水之不流清彻喜金及夏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁丑水性质水之不流清彻喜金及夏(SemanticEntry):
    """
    - **原文（source_text）**：
  丁丑水、水之不流，清彻处，喜金及夏。华盖退神，平头飞刃阙字。

- **分字分词释义**：
  - **水之不流**：不流动的水。
  - **清彻处...
    """
    
    original_text: str = """- **原文（source_text）**：
  丁丑水、水之不流，清彻处，喜金及夏。华盖退神，平头飞刃阙字。

- **分字分词释义**：
  - **水之不流**：不流动的水。
  - **清彻处**：清澈的地方。
  - **喜金及夏**：喜欢金和夏季。
  - **退神**：退神煞。
  - **阙字**：阙字煞。

- **规范化释义（primary_lang_explained）**：
  丁丑水，是不流动的清澈之水，喜欢金和夏季，有华盖星则吉，遇退神煞、平头煞、飞刃煞、阙字煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Dingchou Water is non-flowing clear water, favoring Metal and summer season, auspicious with Canopy Star, inauspicious with Retreat-Spirit sha, Level-Head sha, Flying-Blade sha, and Gap-Character sha.

- **核心要点**：
  - 丁丑为涧下水，不流而清
  - 喜金（金生水）、夏季（显其清）
  - 有华盖清贵
  - 忌退神等煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_208]` `[trigger: 丁丑水性质]` `[factor_trigger: dingchou_water_clear AND favor_metal_summer AND canopy_star]` `[role: 主干]` 丁丑水、水之不流，清彻处，喜金及夏。华盖退神，平头飞刃阙字。 → 《三命通会》卷一#丁丑水性质

- **详细解说**：
  此条解释丁丑（涧下水）的性质。丁丑纳音也是水，但如不流动的清澈之水（如井泉、池塘），喜欢金来生水，喜欢夏季（夏天更显其清凉），有华盖星则清贵，但忌退神煞、平头煞、飞刃煞、阙字煞等凶煞。静水清澈需要金源和适当季节才能发挥价值。

- **校勘与字词辨析（双语）**：
  - **中文**："水之不流"指静止的水。"清彻"指清澈透明。"退神"为退神煞，主退败。"阙字"为阙字煞，主残缺。
  - **English**: "Non-flowing water" refers to still water. "Clear" means transparent and pure. "Retreat-Spirit" is Retreat-Spirit sha, indicating decline. "Gap-Character" is Gap-Character sha, indicating deficiency."""
    normalized_text_zh: str = """"""
    subject: str = "丁丑水性质：水之不流清彻喜金及夏"
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
        l1_anchor="smth_v1.0.0_丁丑水性质_水之不流清彻喜金及夏_001_L1",
    )
    version: str = "1.0.0"
