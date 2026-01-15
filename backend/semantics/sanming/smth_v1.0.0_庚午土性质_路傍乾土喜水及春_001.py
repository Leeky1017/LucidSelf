"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228334
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
    semantic_id="smth_v1.0.0_庚午土性质_路傍乾土喜水及春_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚午土性质路傍乾土喜水及春(SemanticEntry):
    """
    - **原文（source_text）**：
  庚午土、路傍乾土，喜水及春。福星官贵截路棒杖悬针。

- **分字分词释义**：
  - **路傍乾土**：道路旁边的干土。
  - **喜水及春**...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚午土、路傍乾土，喜水及春。福星官贵截路棒杖悬针。

- **分字分词释义**：
  - **路傍乾土**：道路旁边的干土。
  - **喜水及春**：喜欢水和春季。
  - **官贵**：官贵星，吉神。

- **规范化释义（primary_lang_explained）**：
  庚午土，是道路旁边的干土，喜欢水和春季，有福星、官贵星则吉，遇截路煞、棒杖煞、悬针煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Gengwu Earth is dry earth beside roads, favoring Water and spring season, auspicious with Fortune Star and Official-Nobility Star, inauspicious with Road-Blocking sha, Club-Staff sha, and Suspended-Needle sha.

- **核心要点**：
  - 庚午为路旁土，如干土
  - 喜水润泽、春季生发
  - 喜福星、官贵
  - 忌截路、棒杖、悬针

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_201]` `[trigger: 庚午土性质]` `[factor_trigger: gengwu_earth_dry AND favor_water_spring AND official_nobility]` `[role: 主干]` 庚午土、路傍乾土，喜水及春。福星官贵截路棒杖悬针。 → 《三命通会》卷一#庚午土性质

- **详细解说**：
  此条解释庚午（路旁土）的性质。庚午纳音为土，在路旁如干土，喜欢水来滋润（土润则生），喜欢春季（万物生发），遇福星、官贵星则吉，但忌截路煞、棒杖煞、悬针煞等凶煞。路旁干土需要水的滋润才能有用。

- **校勘与字词辨析（双语）**：
  - **中文**："路傍乾土"指道路旁的干燥土地。"官贵"为官贵星，主仕途显贵。"截路、棒杖、悬针"都是凶煞。
  - **English**: "Dry earth beside roads" refers to dry soil alongside pathways. "Official-Nobility" is Official-Nobility Star, indicating career advancement. "Road-Blocking, Club-Staff, Suspended-Needle" are all inauspicious sha."""
    normalized_text_zh: str = """"""
    subject: str = "庚午土性质：路傍乾土喜水及春"
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
        l1_anchor="smth_v1.0.0_庚午土性质_路傍乾土喜水及春_001_L1",
    )
    version: str = "1.0.0"
