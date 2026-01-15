"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558832
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
    semantic_id="yhzp_v1.0.0_论偏财_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论偏财(SemanticEntry):
    """
    - **原文（source_text）**：何谓之偏财？盖阳见阳财，阴见阴财也。然而偏财者，乃众人之财也，只恐兄弟姊妹有夺之，则福不全；若有官星，祸患百出。故曰：偏财好出、亦不惧藏，惟怕有以分夺，反空...
    """
    
    original_text: str = """- **原文（source_text）**：何谓之偏财？盖阳见阳财，阴见阴财也。然而偏财者，乃众人之财也，只恐兄弟姊妹有夺之，则福不全；若有官星，祸患百出。故曰：偏财好出、亦不惧藏，惟怕有以分夺，反空亡耳。偏财主人慷慨、不甚吝财，惟是得地不止。财丰亦能官旺，何以言之？盖，财盛自生官矣，但为人有情而多诈。

- **分字分词释义**：
  - **偏财**：我克且阴阳相同者，如甲木克戊土，戊土为甲木之偏财。
  - **众人之财**：偏财为公共之财、意外之财，非独占专属。
  - **兄弟姊妹夺**：比劫分夺财星，偏财格大忌。
  - **好出不惧藏**：偏财喜露干，不怕明显，因本就是众人共见之财。
  - **分夺**：比劫克财，使财不能为己用。
  - **空亡**：财星落空亡，财不实在。
  - **慷慨不吝财**：偏财之人性格大方，不计较钱财。
  - **有情而多诈**：偏财之人表面有情但心机较多。

- **规范化释义（primary_lang_explained）**：偏财是我克且阴阳相同者，为众人之财。偏财主人慷慨不吝财，但怕兄弟姊妹劫夺。偏财能生官，但需身强方吉。财盛身弱，行官运则祸患百出。

- **完整对等诠释（secondary_lang_full）**：Indirect Wealth is what-I-control with same polarity, public wealth. Indirect Wealth individuals generous not stingy, but fears siblings robbing. Indirect Wealth generates Officer, but requires strong Self for auspiciousness. Abundant Wealth with weak Self, meeting Officer cycles brings endless calamities.

- **核心要点**：
  - 偏财是我克且阴阳相同者，为众人之财
  - 偏财主人慷慨不吝财，但有情而多诈
  - 偏财怕兄弟姊妹劫夺，比劫分财为大忌
  - 偏财好出不惧藏，喜露干明见
  - 财盛身弱行官运则祸患百出

- **详细解说**：  
  本条论述偏财的性质与特点。偏财是我克且阴阳相同者（如甲木克戊土），与正财的最大区别在于"众人之财"——偏财是公共的、流动的、意外的财富，不像正财那样专属独占。因此偏财最怕"兄弟姊妹有夺之"——比劫是偏财的天敌，若命中比劫旺而分夺偏财，则"福不全"。但偏财"好出、亦不惧藏"，因其本就是众人共见之财，不怕明显露干。偏财之人的性格是"慷慨、不甚吝财"，大方不计较；但也"有情而多诈"，表面热情内心精明。财与官的关系是"财盛自生官"——财多能生官，但需身强方吉；若财盛身弱再行官运，则"祸患百出"，因为财生官、官克身，身弱难以承受。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_061]` `[trigger: 偏财定义]` `[factor_trigger: indirect_wealth AND ke_rizhu_shen]` `[role: 主干]` 何谓之偏财？盖阳见阳财，阴见阴财也。 → 《渊海子平·论偏财》
  - `[ns_yhzp_062]` `[trigger: 偏财性质]` `[factor_trigger: indirect_wealth]` `[role: 主干依赖]` 偏财者，乃众人之财也。 → 《渊海子平·论偏财》
  - `[ns_yhzp_063]` `[trigger: 偏财怕劫]` `[factor_trigger: indirect_wealth AND rob_wealth]` `[role: 条件分支]` 只恐兄弟姊妹有夺之，则福不全。 → 《渊海子平·论偏财》
  - `[ns_yhzp_064]` `[trigger: 偏财喜露]` `[factor_trigger: indirect_wealth AND haochubucan]` `[role: 条件分支]` 偏财好出、亦不惧藏。 → 《渊海子平·论偏财》
  - `[ns_yhzp_065]` `[trigger: 偏财分夺]` `[factor_trigger: indirect_wealth AND rob_wealth]` `[role: 例外处理]` 惟怕有以分夺，反空亡耳。 → 《渊海子平·论偏财》
  - `[ns_yhzp_066]` `[trigger: 偏财性格]` `[factor_trigger: indirect_wealth AND kangkai_xingge]` `[role: 条件分支]` 偏财主人慷慨、不甚吝财，但为人有情而多诈。 → 《渊海子平·论偏财》
  - `[ns_yhzp_067]` `[trigger: 财生官]` `[factor_trigger: indirect_wealth AND direct_officer]` `[role: 总结]` 财丰亦能官旺，财盛自生官矣。 → 《渊海子平·论偏财》"""
    normalized_text_zh: str = """"""
    subject: str = "论偏财"
    factor_refs: list = ['indirect_wealth', 'relation_rob_wealth_seizing_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论偏财_001_L1",
    )
    version: str = "1.0.0"
