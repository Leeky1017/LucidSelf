"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228629
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
    semantic_id="smth_v1.0.0_甲辰覆灯火_偏库之火敏速峻烈_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲辰覆灯火偏库之火敏速峻烈(SemanticEntry):
    """
    - **原文（source_text）**：
  甲辰偏库之火，多火助之吉，所谓同气之求，以资其不足。若见戊辰、戊戌木生之为贵格，忌壬辰、壬戌、丙午、丁未水最毒。五行要论云：甲辰为天将之火，含敏速峻烈...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲辰偏库之火，多火助之吉，所谓同气之求，以资其不足。若见戊辰、戊戌木生之为贵格，忌壬辰、壬戌、丙午、丁未水最毒。五行要论云：甲辰为天将之火，含敏速峻烈之气，入贵格，则为特达，为文魁，利秋冬，不利于夏。

- **分字分词释义**：
  - **偏库之火**：偏于入库的火。
  - **同气之求**：同类五行相求。
  - **资其不足**：补助其不足。
  - **天将之火**：天将星的火。
  - **敏速峻烈**：敏捷迅速峻猛激烈。
  - **特达**：特别通达。
  - **文魁**：文章魁首。

- **规范化释义（primary_lang_explained）**：
  甲辰是偏库的火，多火帮助它才吉利，所谓同类五行相求，来补助其不足。如果见到戊辰、戊戌木来生为贵格，忌讳壬辰、壬戌、丙午、丁未水最为有毒。五行要论说：甲辰是天将之火，包含敏捷迅速峻猛激烈的气质，如果入贵格，就能特别通达，成为文章魁首，利于秋冬，不利于夏天。

- **完整对等诠释（secondary_lang_full）**：
  Jiachen is partial-storage fire, many Fires assisting it auspicious, so-called same-energy mutual-seeking, to supply its insufficiency. If seeing Wuchen, Wuxu Wood generating becomes noble pattern, avoids Renchen, Renxu, Bingwu, Dingwei Water most harmful. Five Elements Essential Discourse says: Jiachen is Heaven-General fire, contains swift-quick steep-fierce energy. Entering noble pattern, then specially-accomplished, becomes literary-chief, favorable autumn-winter, unfavorable in summer.

- **核心要点**：
  - 甲辰为覆灯火，偏库之火
  - 多火助、同气相求吉
  - 见特定木生为贵格
  - 忌特定水最毒
  - 天将之火、敏速峻烈
  - 入贵特达文魁、利秋冬不利夏

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_236]` `[trigger: 甲辰火性质]` `[factor_trigger: jiachen_partial_storage_fire AND swift_quick_steep_fierce AND noble_pattern_specially_accomplished_literary_chief]` `[role: 主干]` 甲辰偏库之火，多火助之吉，所谓同气之求，以资其不足。若见戊辰、戊戌木生之为贵格，忌壬辰、壬戌、丙午、丁未水最毒。五行要论云：甲辰为天将之火，含敏速峻烈之气，入贵格，则为特达，为文魁，利秋冬，不利于夏。 → 《三命通会》卷一#甲辰火性质

- **详细解说**：
  此条详论甲辰（覆灯火）的性质与格局。甲辰是偏库的火（辰为水库但纳音为火），需多火助之（同气相求补不足）。若见戊辰（大林木）、戊戌（平地木）生之为贵格，但忌壬辰（长流水）、壬戌（大海水）、丙午（天河水）、丁未（天河水）等水最毒。五行要论强调甲辰为天将之火，敏速峻烈，入贵则特达文魁，利秋冬（火需收敛）、不利夏（火太旺）。这是论述偏库火的扶助与季节格局。

- **校勘与字词辨析（双语）**：
  - **中文**："偏库"指辰为水库非火库。"同气相求"指同类五行互相扶助。"敏速峻烈"形容火势迅猛。"特达"指特别显达。
  - **English**: "Partial-storage" means Chen is water repository not fire. "Same-energy mutual-seeking" means same-element mutual support. "Swift-quick steep-fierce" describes rapid and fierce fire momentum. "Specially-accomplished" means particularly distinguished."""
    normalized_text_zh: str = """"""
    subject: str = "甲辰覆灯火：偏库之火敏速峻烈"
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
        l1_anchor="smth_v1.0.0_甲辰覆灯火_偏库之火敏速峻烈_001_L1",
    )
    version: str = "1.0.0"
