"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228427
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
    semantic_id="smth_v1.0.0_壬午木性质_柔和之木枝干微弱_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬午木性质柔和之木枝干微弱(SemanticEntry):
    """
    - **原文（source_text）**：
  壬午木、柔和之木，枝干微弱，木能生火，却忌见火多，多则烬矣，虽生旺之金亦不能伤。

- **分字分词释义**：
  - **柔和之木**：柔软温和的木...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬午木、柔和之木，枝干微弱，木能生火，却忌见火多，多则烬矣，虽生旺之金亦不能伤。

- **分字分词释义**：
  - **柔和之木**：柔软温和的木。
  - **枝干微弱**：枝干细弱。
  - **多则烬矣**：火多则烧成灰烬。
  - **生旺之金亦不能伤**：即使旺盛的金也不能伤害。

- **规范化释义（primary_lang_explained）**：
  壬午木，是柔软温和的木，枝干细弱，木能生火，但忌讳见火太多，火多就会烧成灰烬，即使旺盛的金也不能伤害它。

- **完整对等诠释（secondary_lang_full）**：
  Renwu Wood is gentle-soft wood, branches and trunk slender-weak, wood can generate fire, yet fears seeing too much fire—excess turns it to ashes, even flourishing metal cannot harm it.

- **核心要点**：
  - 壬午为杨柳木，柔和微弱
  - 能生火但忌火多
  - 金不能伤（午为金死地）
  - 需要保护培养

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_213]` `[trigger: 壬午木性质]` `[factor_trigger: renwu_wood_gentle AND branches_slender_weak AND avoid_excess_fire]` `[role: 主干]` 壬午木、柔和之木，枝干微弱，木能生火，却忌见火多，多则烬矣，虽生旺之金亦不能伤。 → 《三命通会》卷一#壬午木性质

- **详细解说**：
  此条解释壬午（杨柳木）的性质。壬午纳音为木，如柔软的杨柳，枝干细弱，能生火但忌火太多（火多则焚），旺盛的金也不能伤害（因为午是金的死地，金无力克木）。柔弱之木需要精心培养，不能过度耗泄。

- **校勘与字词辨析（双语）**：
  - **中文**："柔和"指柔软温和。"枝干微弱"指树枝树干细弱。"烬"指灰烬。"生旺之金"指强盛的金。
  - **English**: "Gentle-soft" means supple and mild. "Branches trunk slender-weak" means thin branches and trunk. "Ashes" means burnt remains. "Flourishing metal" means strong metal."""
    normalized_text_zh: str = """"""
    subject: str = "壬午木性质：柔和之木枝干微弱"
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
        l1_anchor="smth_v1.0.0_壬午木性质_柔和之木枝干微弱_001_L1",
    )
    version: str = "1.0.0"
