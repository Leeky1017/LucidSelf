"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228342
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
    semantic_id="smth_v1.0.0_辛未土性质_含万宝待秋成喜秋及火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛未土性质含万宝待秋成喜秋及火(SemanticEntry):
    """
    - **原文（source_text）**：
  辛未土、含万宝，待秋成喜秋及火华盖悬针破字。

- **分字分词释义**：
  - **含万宝**：蕴含万物之宝。
  - **待秋成**：等待秋季成...
    """
    
    original_text: str = """- **原文（source_text）**：
  辛未土、含万宝，待秋成喜秋及火华盖悬针破字。

- **分字分词释义**：
  - **含万宝**：蕴含万物之宝。
  - **待秋成**：等待秋季成熟。
  - **喜秋及火**：喜欢秋季和火。

- **规范化释义（primary_lang_explained）**：
  辛未土，蕴含万物之宝，等待秋季成熟，喜欢秋季和火，有华盖星则吉，遇悬针煞、破字煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Xinwei Earth contains myriad treasures, awaiting autumn maturation, favoring autumn and Fire, auspicious with Canopy Star, inauspicious with Suspended-Needle sha and Broken-Character sha.

- **核心要点**：
  - 辛未为路旁土，含万宝
  - 待秋季成熟
  - 喜秋季、火
  - 有华盖、忌悬针破字

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_202]` `[trigger: 辛未土性质]` `[factor_trigger: xinwei_earth_treasures AND favor_autumn_fire AND canopy_star]` `[role: 主干]` 辛未土、含万宝，待秋成喜秋及火华盖悬针破字。 → 《三命通会》卷一#辛未土性质

- **详细解说**：
  此条解释辛未（路旁土）的性质。辛未纳音也是土，蕴含万物之宝，等待秋季收获成熟，喜欢秋季（收获时节）和火（土得火生），有华盖星则清贵，但忌悬针煞、破字煞等凶煞。路旁土承载万物，秋季是其显现价值的时候。

- **校勘与字词辨析（双语）**：
  - **中文**："含万宝"指土中蕴藏万物。"待秋成"指等待秋季收获。"华盖"为孤高清贵之星。
  - **English**: "Contains myriad treasures" means earth contains all things. "Awaiting autumn maturation" means waiting for autumn harvest. "Canopy" is star of lofty nobility."""
    normalized_text_zh: str = """"""
    subject: str = "辛未土性质：含万宝待秋成喜秋及火"
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
        l1_anchor="smth_v1.0.0_辛未土性质_含万宝待秋成喜秋及火_001_L1",
    )
    version: str = "1.0.0"
