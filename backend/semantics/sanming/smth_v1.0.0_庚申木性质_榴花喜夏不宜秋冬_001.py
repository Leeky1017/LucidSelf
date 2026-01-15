"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228478
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
    semantic_id="smth_v1.0.0_庚申木性质_榴花喜夏不宜秋冬_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚申木性质榴花喜夏不宜秋冬(SemanticEntry):
    """
    - **原文（source_text）**：
  庚申木、榴花喜夏，不宜秋冬，建禄马八专杖刑破字悬针。

- **分字分词释义**：
  - **榴花**：石榴花。
  - **喜夏不宜秋冬**：喜欢...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚申木、榴花喜夏，不宜秋冬，建禄马八专杖刑破字悬针。

- **分字分词释义**：
  - **榴花**：石榴花。
  - **喜夏不宜秋冬**：喜欢夏季不宜秋冬。
  - **建禄马**：建禄、禄马。
  - **八专**：八专日。
  - **杖刑**：杖刑煞。

- **规范化释义（primary_lang_explained）**：
  庚申木，是石榴花，喜欢夏季，不宜秋冬，有建禄、禄马、八专则吉，遇杖刑煞、破字煞、悬针煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Gengshen Wood is pomegranate flower, favors summer, unsuitable for autumn-winter, auspicious with Establishing-Salary, Salary-Horse, Eight-Exclusive, inauspicious with Staff-Punishment sha, Broken-Character sha, Suspended-Needle sha.

- **核心要点**：
  - 庚申为石榴木，如榴花
  - 喜夏季（花开）
  - 不宜秋冬（花谢）
  - 喜建禄马八专、忌杖刑等煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_220]` `[trigger: 庚申木性质]` `[factor_trigger: gengshen_wood_pomegranate AND favor_summer AND establishing_salary_horse]` `[role: 主干]` 庚申木、榴花喜夏，不宜秋冬，建禄马八专杖刑破字悬针。 → 《三命通会》卷一#庚申木性质

- **详细解说**：
  此条解释庚申（石榴木）的性质。庚申纳音为木，如石榴花，喜欢夏季（花开盛时），不宜秋冬（秋冬花谢），有建禄、禄马、八专等吉神则吉，但忌杖刑煞、破字煞、悬针煞等凶煞。花木最需适当季节。

- **校勘与字词辨析（双语）**：
  - **中文**："榴花"指石榴花。"建禄"指禄神建立。"禄马"指禄神与驿马。"杖刑"为杖刑煞，主刑伤。
  - **English**: "Pomegranate flower" refers to flower of pomegranate. "Establishing-Salary" means Salary Spirit establishing. "Salary-Horse" means Salary Spirit and Post-Horse. "Staff-Punishment" is Staff-Punishment sha, indicating punishment."""
    normalized_text_zh: str = """"""
    subject: str = "庚申木性质：榴花喜夏不宜秋冬"
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
        l1_anchor="smth_v1.0.0_庚申木性质_榴花喜夏不宜秋冬_001_L1",
    )
    version: str = "1.0.0"
