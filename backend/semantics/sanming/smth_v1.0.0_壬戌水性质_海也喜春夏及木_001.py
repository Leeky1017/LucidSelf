"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228495
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
    semantic_id="smth_v1.0.0_壬戌水性质_海也喜春夏及木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬戌水性质海也喜春夏及木(SemanticEntry):
    """
    - **原文（source_text）**：
  壬戌水、海也喜春夏及木，华盖退神平头，聋哑杖刑。

- **分字分词释义**：
  - **海也**：大海。
  - **喜春夏及木**：喜欢春季夏季...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬戌水、海也喜春夏及木，华盖退神平头，聋哑杖刑。

- **分字分词释义**：
  - **海也**：大海。
  - **喜春夏及木**：喜欢春季夏季和木。
  - **退神**：退神煞。
  - **杖刑**：杖刑煞。

- **规范化释义（primary_lang_explained）**：
  壬戌水，是大海，喜欢春季、夏季和木，有华盖星则吉，遇退神煞、平头煞、聋哑煞、杖刑煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Renxu Water is ocean, favors spring, summer and Wood, auspicious with Canopy Star, inauspicious with Retreat-Spirit sha, Level-Head sha, Deaf-Mute sha, Staff-Punishment sha.

- **核心要点**：
  - 壬戌为大海水，如海
  - 喜春夏（水旺）、木（水生木）
  - 有华盖清贵
  - 忌退神等煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_222]` `[trigger: 壬戌水性质]` `[factor_trigger: renxu_water_ocean AND favor_spring_summer_wood AND canopy_star]` `[role: 主干]` 壬戌水、海也喜春夏及木，华盖退神平头，聋哑杖刑。 → 《三命通会》卷一#壬戌水性质

- **详细解说**：
  此条解释壬戌（大海水）的性质。壬戌纳音为水，如大海，喜欢春夏季节（水旺时节）和木（水生木有用），有华盖星则清贵，但忌退神煞、平头煞、聋哑煞、杖刑煞等凶煞。大海之水浩瀚需要适当的疏导和运用。

- **校勘与字词辨析（双语）**：
  - **中文**："海也"即大海。"春夏"为水旺季节。"杖刑"为杖刑煞，主刑伤。
  - **English**: "Ocean" means great sea. "Spring-summer" are water-flourishing seasons. "Staff-Punishment" is Staff-Punishment sha, indicating punishment."""
    normalized_text_zh: str = """"""
    subject: str = "壬戌水性质：海也喜春夏及木"
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
        l1_anchor="smth_v1.0.0_壬戌水性质_海也喜春夏及木_001_L1",
    )
    version: str = "1.0.0"
