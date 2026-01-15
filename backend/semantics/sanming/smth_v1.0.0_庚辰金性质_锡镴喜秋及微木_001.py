"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228413
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
    semantic_id="smth_v1.0.0_庚辰金性质_锡镴喜秋及微木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚辰金性质锡镴喜秋及微木(SemanticEntry):
    """
    - **原文（source_text）**：
  庚辰金、锡镴喜秋及微木，华盖大败，棒杖平头。

- **分字分词释义**：
  - **锡镴**：锡和铅等软金属。
  - **喜秋及微木**：喜欢秋...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚辰金、锡镴喜秋及微木，华盖大败，棒杖平头。

- **分字分词释义**：
  - **锡镴**：锡和铅等软金属。
  - **喜秋及微木**：喜欢秋季和少量的木。
  - **大败**：大败煞。

- **规范化释义（primary_lang_explained）**：
  庚辰金，是锡铅等软金属，喜欢秋季和少量的木，有华盖星则吉，遇大败煞、棒杖煞、平头煞则凶。

- **完整对等诠释（secondary_lang_full）**：
  Gengchen Metal is tin-lead soft metal, favoring autumn season and slight Wood, auspicious with Canopy Star, inauspicious with Great-Defeat sha, Club-Staff sha, and Level-Head sha.

- **核心要点**：
  - 庚辰为白镴金，如锡镴
  - 喜秋季（金旺）、微木（少量财）
  - 有华盖清贵
  - 忌大败等煞

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_211]` `[trigger: 庚辰金性质]` `[factor_trigger: gengchen_metal_tin_lead AND favor_autumn_slight_wood AND canopy_star]` `[role: 主干]` 庚辰金、锡镴喜秋及微木，华盖大败，棒杖平头。 → 《三命通会》卷一#庚辰金性质

- **详细解说**：
  此条解释庚辰（白镴金）的性质。庚辰纳音为金，如锡铅等软金属，喜欢秋季（金旺之时），喜欢少量的木（木为金之财，但不宜多），有华盖星则清贵，但忌大败煞、棒杖煞、平头煞等凶煞。软金属需要合适的时节和适量的财才能发挥价值。

- **校勘与字词辨析（双语）**：
  - **中文**："锡镴"指锡、铅等软金属。"微木"指少量的木，木多则克金太过。
  - **English**: "Tin-lead" refers to soft metals like tin and lead. "Slight Wood" means small amount of wood; too much wood overcomes metal."""
    normalized_text_zh: str = """"""
    subject: str = "庚辰金性质：锡镴喜秋及微木"
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
        l1_anchor="smth_v1.0.0_庚辰金性质_锡镴喜秋及微木_001_L1",
    )
    version: str = "1.0.0"
