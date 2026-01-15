"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066681
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
    semantic_id="smth_v1.0.0_1_官煞财印的变通之道_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1官煞财印的变通之道(SemanticEntry):
    """
    - 原文（source_text）：
  五行妙用，难逃一理之中；进退存亡，要识变通之道。
  正官佩印，不如乘马。
  七煞用财，岂宜得禄。
  印逢财而罢职，财逢印以迁官。
  命当夭折，食神孑立...
    """
    
    original_text: str = """- 原文（source_text）：
  五行妙用，难逃一理之中；进退存亡，要识变通之道。
  正官佩印，不如乘马。
  七煞用财，岂宜得禄。
  印逢财而罢职，财逢印以迁官。
  命当夭折，食神孑立逢枭。
  运至凶危，羊刃重逢破局。
  争正官不可无伤，归七煞最嫌有制。
  官居煞地，难守其官；煞在官乡，岂能变煞。
  贪财坏印，擢高科印分轻重。
  遇比用财，缠万贯比得资扶。

- 分字分词释义：
  - **乘马**：财星（马）。正官佩印（官印相生），不如财星生官（乘马）更有实利（前提是身旺）。
  - **得禄**：日主得禄（身旺）或煞得禄（煞旺）。此处指煞旺用财生煞，若日主又得禄（身强），身煞交战，凶。
  - **食神孑立**：食神孤单无援，又见枭神。
  - **争正官**：比劫争官。
  - **无伤**：无伤官。原文注云“运至伤官伤尽官星，则比肩无争夺始可安矣”，意即官星被争，不如弃之。
  - **归七煞**：时上七煞。
  - **印分轻重**：印重喜财（财坏印发科甲），印轻忌财。

- **规范化释义（primary_lang_explained）**：
  五行的运用虽万变不离其宗，但要懂得进退存亡的变通。
  正官格佩印（清高），不如有财生官（富贵）来得实惠。
  七煞格本忌财星党煞，若日主又得禄旺（身强），身煞对峙，岂宜再用财生煞？（或指煞用财生，忌日主得禄，因身强则不从煞，必有一战）。
  印绶格见财星破印，主罢职；财格（身弱）见印绶扶身，主迁官。
  食神一位孤立，又逢枭神夺食，主夭折。
  用财格（忌刃），若行运重逢羊刃劫财，主破局凶危。
  比劫争夺正官，若无伤官制官（去官留劫）或制劫（护官），则争夺不休。
  时上七煞格（归七煞）本来喜制，但若局中比劫多，七煞能制比劫护财；此时若再见食神制煞太过，煞不能制劫，比劫夺财，反为祸。
  官星处于煞旺之地（官煞混杂且煞重），官星难保；七煞处于官旺之地（混杂且官重），七煞也不能变成官（仍需去留）。
  贪财坏印，若印重身强，反主高中科举（财制太过之印）；若印轻身弱，则为大害。
  财格遇比劫争夺，若得官煞制比劫（比得资扶？原文注"比得资扶"指比劫得势，需官煞制之，或指日主得比劫资扶，能任财），可缠万贯。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Flexibility of Official-Killing-Wealth-Seal" from the Six Spirits Chapter:

  - Five Elements marvelous usage, hard to escape one principle; advance-retreat survival-extinction, must understand flexibility way.
  - Proper Official wearing Seal, not as good as riding Horse (Wealth generating Official).
  - Seal meets Wealth loses position; Wealth meets Seal promotes rank.
  - Eating God solitary meets Owl, life shortened folding; Yang Blade doubles meets broken pattern, disaster arrives.
  - Greedy-Wealth breaks Seal, selecting high rank Seal divides weight—Seal heavy welcomes Wealth, Seal light fears Wealth.
  - Key: Ten Gods preferences not absolute; flexibility according to body strength; balance between control and generation.

- 核心要点：
  - **变通**：官煞财印喜忌非绝对。
  - **身煞平衡**：煞旺宜制，身弱宜扶。
  - **制化有情**：贪财坏印有时吉（印重）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_013]` `[trigger: 变通之道]` `[factor_trigger: biantong_zhidao AND jintui_cunwang]` `[role: 主干]` 五行妙用，难逃一理之中；进退存亡，要识变通之道。 → 《三命通会》卷十一#官煞财印的变通之道
  - `[ns_smth_11_014]` `[trigger: 印逢财]` `[factor_trigger: yinfeng_cai AND baizhi_qianguan]` `[role: 主干依赖]` 印逢财而罢职，财逢印以迁官。 → 《三命通会》卷十一#官煞财印的变通之道
  - `[ns_smth_11_015]` `[trigger: 枭夺食]` `[factor_trigger: xiaoduo_shi AND mingyao_zheshou]` `[role: 条件分支]` 命当夭折，食神孑立逢枭。 → 《三命通会》卷十一#官煞财印的变通之道
  - `[ns_smth_11_016]` `[trigger: 贪财坏印]` `[factor_trigger: tancai_huaiyin AND yinfen_qingzhong]` `[role: 总结]` 贪财坏印，擢高科印分轻重。 → 《三命通会》卷十一#官煞财印的变通之道"""
    normalized_text_zh: str = """"""
    subject: str = "1 官煞财印的变通之道"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_9', 'bazi_semantic', 'bazi_relation_zhenguan', 'bazi_semantic', 'bazi_state_factor_166', 'bazi_semantic', 'bazi_state_factor_50', 'bazi_semantic', 'bazi_state_factor_51', 'bazi_semantic', 'bazi_condition_factor_7', 'bazi_semantic', 'source_ref', 'rel_smth_11_010', 'shishen_biantong', 'rel_smth_11_011', 'xiaohen_duoshi', 'rel_smth_11_012', 'yinzhong_xicai', 'evi_smth_11_010', 'shishen_biantong', 'rule_shishen_biantong1', 'evi_smth_11_011', 'xiaohen_duoshi', 'rule_xiaohen_duoshi1', 'evi_smth_11_012', 'yinzhong_xicai', 'rule_yinzhong_xicai1', 'map_smth_11_007', 'map_smth_11_008']
    
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
        l1_anchor="smth_v1.0.0_1_官煞财印的变通之道_001_L1",
    )
    version: str = "1.0.0"
