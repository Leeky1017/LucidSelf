"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559161
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
    semantic_id="yhzp_v1.0.0_论子息_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论子息(SemanticEntry):
    """
    - **原文（source_text）**：七杀者子也。如甲见庚申是子，辛酉是女。若见丙火午寅、或杀临阳刃杀宫，主克子；不然疾病不肖。阳日阳时男重见；阳日阴时，先男后女。伤官见官，子孙凶顽。女命取伤官...
    """
    
    original_text: str = """- **原文（source_text）**：七杀者子也。如甲见庚申是子，辛酉是女。若见丙火午寅、或杀临阳刃杀宫，主克子；不然疾病不肖。阳日阳时男重见；阳日阴时，先男后女。伤官见官，子孙凶顽。女命取伤官是子，食神是女；若见印绶枭神，难得子也。官杀得地而有扶助，吉曜多者，其子忠孝贤明。八字有一杀一子，二杀二子，无杀无子。

- **分字分词释义**：
  - **七杀者子也**：男命以七杀代表子女。
  - **甲见庚申是子**：甲日以庚（七杀）为子，申中藏庚。
  - **辛酉是女**：甲日以辛（正官）为女，酉中藏辛。
  - **丙火午寅**：食伤制杀，克制子星。
  - **杀临阳刃杀宫**：杀星临凶地，主克子。
  - **疾病不肖**：子女有病或不孝。
  - **阳日阳时**：日时皆阳，主多男。
  - **阳日阴时**：日阳时阴，先男后女。
  - **伤官见官**：子星（官杀）受克，子孙凶顽。
  - **女命伤官是子**：女命以伤官为子（我生且阴阳相异者）。
  - **食神是女**：女命以食神为女（我生且阴阳相同者）。
  - **印绶枭神**：印绶克食伤，女命难得子。
  - **官杀得地**：子星旺相得力，主子贤明。
  - **一杀一子二杀二子**：杀多主多子，无杀无子。

- **规范化释义（primary_lang_explained）**：男命以官杀论子女，女命以食伤论子女。男命七杀为子女，阳见阳为子阴见阴为女；女命伤官为子食神为女。印绶克食伤主难得子。阳日阳时多男，阳日阴时先男后女。杀临阳刃或刑冲主克子；官杀得地吉曜多主子贤；杀多主多子，无杀无子。

- **完整对等诠释（secondary_lang_full）**：Male fate analyzes children via Officer/Killing; female fate via Food/Injury. Male takes Seven Killings as children—yang-yang for sons, yin-yin for daughters; female takes Injuring Officer as sons, Eating God as daughters. Seal controlling Food/Injury brings difficulty conceiving. Yang Day-yang Hour brings many sons; yang Day-yin Hour brings sons first then daughters. Killing in Blade or punishments harms children; prosperous Officer/Killing with auspicious stars brings wise children. Multiple Killings bring multiple children; no Killing brings no children.

- **核心要点**：
  - 男命以七杀为子，正官为女
  - 女命以伤官为子，食神为女
  - 印绶枭神克食伤，难得子
  - 杀临阳刃杀宫，主克子
  - 阳日阳时多男，阳日阴时先男后女
  - 伤官见官，子孙凶顽
  - 官杀得地有吉曜，其子忠孝贤明
  - 一杀一子，二杀二子，无杀无子

- **详细解说**：  
  本条论述子息的判断方法。"七杀者子也"——男命以官杀论子女。以甲日为例："甲见庚申是子，辛酉是女"——七杀（庚）为子，正官（辛）为女。克子的情况是"若见丙火午寅、或杀临阳刃杀宫，主克子"——食伤制杀或杀临凶地主克子；"不然疾病不肖"——否则子女有病或不孝。子女性别的判断是"阳日阳时男重见；阳日阴时，先男后女"——以日时阴阳判断子女性别。"伤官见官，子孙凶顽"——子星受克主子女不贤。女命取子的方法是"伤官是子，食神是女"——女命以食伤为子女；"若见印绶枭神，难得子也"——印绶克食伤主难得子。子贤的情况是"官杀得地而有扶助，吉曜多者，其子忠孝贤明"——子星旺相主子贤。"一杀一子，二杀二子，无杀无子"——以杀数论子数。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_189]` `[trigger: 七杀为子]` `[factor_trigger: seven_killings_children]` `[role: 主干]` 七杀者子也。 → 《渊海子平·论子息》
  - `[ns_yhzp_190]` `[trigger: 官杀子女]` `[factor_trigger: seven_killings_children AND daughter AND eating_god]` `[role: 主干依赖]` 如甲见庚申是子，辛酉是女。 → 《渊海子平·论子息》
  - `[ns_yhzp_191]` `[trigger: 克子之象]` `[factor_trigger: killing_blade_harms_children]` `[role: 条件分支]` 若见丙火午寅、或杀临阳刃杀宫，主克子。 → 《渊海子平·论子息》
  - `[ns_yhzp_192]` `[trigger: 阳日阳时]` `[factor_trigger: seven_killings_children]` `[role: 条件分支]` 阳日阳时男重见；阳日阴时，先男后女。 → 《渊海子平·论子息》
  - `[ns_yhzp_193]` `[trigger: 伤官见官]` `[factor_trigger: food_injury_children AND direct_officer]` `[role: 例外处理]` 伤官见官，子孙凶顽。 → 《渊海子平·论子息》
  - `[ns_yhzp_194]` `[trigger: 女命子女]` `[factor_trigger: food_injury_children AND seal_harms_children AND abundant_seal_harms_children]` `[role: 条件分支]` 女命取伤官是子，食神是女；若见印绶枭神，难得子也。 → 《渊海子平·论子息》
  - `[ns_yhzp_195]` `[trigger: 子贤明]` `[factor_trigger: seven_killings_children]` `[role: 条件分支]` 官杀得地而有扶助，吉曜多者，其子忠孝贤明。 → 《渊海子平·论子息》
  - `[ns_yhzp_196]` `[trigger: 杀数论子]` `[factor_trigger: children_count]` `[role: 总结]` 八字有一杀一子，二杀二子，无杀无子。 → 《渊海子平·论子息》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 七杀为子 | Seven Killings as Children | 男命以七杀正官代表子女 | Male fate takes Seven Killings/Officer as children | seven_killings_children | existing |
| 食伤为子 | Food/Injury as Children | 女命以食神伤官代表子女 | Female fate takes Eating God/Injuring Officer as children | food_injury_children | existing |
| 印绶克子 | Seal Harms Children | 印绶克食伤主难得子 | Seal controlling Food/Injury brings few children | seal_harms_children | existing |
| 杀临阳刃克子 | Killing in Blade Harms Children | 七杀临阳刃主克子 | Seven Killings in Yang Blade harms children | killing_blade_harms_children | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "论子息"
    factor_refs: list = []
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论子息_001_L1",
    )
    version: str = "1.0.0"
