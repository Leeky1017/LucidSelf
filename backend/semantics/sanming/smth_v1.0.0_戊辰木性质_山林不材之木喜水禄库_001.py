"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228319
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
    semantic_id="smth_v1.0.0_戊辰木性质_山林不材之木喜水禄库_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊辰木性质山林不材之木喜水禄库(SemanticEntry):
    """
    - **原文（source_text）**：
  戊辰木、山林山野处不材之木，喜水禄库、华盖、水禄马库、棒杖、伏神、平头。

- **分字分词释义**：
  - **山林山野处**：山林野外的地方。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊辰木、山林山野处不材之木，喜水禄库、华盖、水禄马库、棒杖、伏神、平头。

- **分字分词释义**：
  - **山林山野处**：山林野外的地方。
  - **不材之木**：不成材的树木。
  - **禄库**：禄神入库。
  - **禄马库**：禄马入库。
  - **棒杖**：棒杖煞，凶煞名。
  - **伏神**：伏神煞。

- **规范化释义（primary_lang_explained）**：
  戊辰木，是山林野外不成材的树木，喜欢水以及禄库、华盖、禄马库，忌讳棒杖煞、伏神煞、平头煞。

- **完整对等诠释（secondary_lang_full）**：
  Wuchen Wood is uncultivated wood in mountains and wilds, favoring Water, Salary-Storage, Canopy, Salary-Horse-Storage, avoiding Club-Staff sha, Concealed-Spirit sha, and Level-Head sha.

- **核心要点**：
  - 戊辰为大林木，山林不材木
  - 喜水滋润、禄库等
  - 有华盖则清贵
  - 忌棒杖、伏神、平头

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_199]` `[trigger: 戊辰木性质]` `[factor_trigger: wuchen_wood_uncultivated AND favor_water_salary_storage AND canopy_star]` `[role: 主干]` 戊辰木、山林山野处不材之木，喜水禄库、华盖、水禄马库、棒杖、伏神、平头。 → 《三命通会》卷一#戊辰木性质

- **详细解说**：
  此条解释戊辰（大林木）的性质。戊辰纳音为木，在山林野外，不成材之木（野生未经培育），喜欢水来滋润（水生木），喜禄库、华盖星、禄马库等吉神，但忌棒杖煞、伏神煞、平头煞等凶煞。山林之木需要水土滋养才能生长。

- **校勘与字词辨析（双语）**：
  - **中文**："不材"指不成材，未经培育。"禄库"指禄神入库，主财富储藏。"棒杖"为棒杖煞，主刑伤。"伏神"指隐伏之神。
  - **English**: "Uncultivated" means not properly grown, uncultivated. "Salary-Storage" means Salary Spirit entering storage, indicating wealth accumulation. "Club-Staff" is Club-Staff sha, indicating punishment and injury. "Concealed-Spirit" means hidden spirit."""
    normalized_text_zh: str = """"""
    subject: str = "戊辰木性质：山林不材之木喜水禄库"
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
        l1_anchor="smth_v1.0.0_戊辰木性质_山林不材之木喜水禄库_001_L1",
    )
    version: str = "1.0.0"
