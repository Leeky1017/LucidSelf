"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492373
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
    semantic_id="zpzq_v1.0.0_伤官格的多重形态与秀气层次_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 伤官格的多重形态与秀气层次(SemanticEntry):
    """
    - **原文（source_text）**：
  四十一、论伤官。
  伤官虽非吉神，实为秀气，故文人学士，多于伤官格内得之。而夏木见水，冬金见火，则又为秀之尤秀者也。其中格局比他格多，变化尤多，在查...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十一、论伤官。
  伤官虽非吉神，实为秀气，故文人学士，多于伤官格内得之。而夏木见水，冬金见火，则又为秀之尤秀者也。其中格局比他格多，变化尤多，在查其气候，量其强弱，审其喜忌，观其纯杂，微之又微，不可执也。

  故有伤官用财者，盖伤不利于民，所以为凶，伤官生财，则以伤官为生官之具，转凶为吉，故最利。只要身强而有根，便为贵格，如壬午、己酉、戊午、庚申，史春芳命也。

  至于化伤为财，大为秀气，如罗状元命，甲子、乙亥、辛未、戊子，干头之甲，通根于亥，然又会未成局，化水为木，化之生财，尤为有情，所以伤官生财，冬金不贵，以冻水不能生木。若乃化木，不待于生，安得不为殿元乎？

  至于财伤有情，与化伤为财者，其秀气不相上下，如秦龙图命，己卯、丁丑、丙寅、庚寅，已与庚同根月令是也。

  有伤官佩印者，印能制伤，所以为贵，反要伤官旺，身稍弱，始为秀气。如孛罗平章命，壬申、丙午、申午、壬申，伤官旺，印根深，身又弱，又是夏木逢润，其秀百倍，所以一品之贵。然印旺极深，不必多见，偏正叠出，反为不秀，故伤轻身重而印绶多见，贫穷之格也。

  有伤官兼用财印者，财印相克，本不并用，只要干头两清而不相碍；又必生财者，财太旺而带印，佩印者印太重而带财，调停中和，遂为贵格。如丁酉、己酉、戊子、壬子，财太重而带印，而丁与壬隔以戊已，两不碍，且金水多而觉寒，得火融和，都统制命也。又如壬戌、己酉、戊午、丁巳，印太重而隔戊已，而丁与壬不相碍，一丞相命也。反是则财印不并用而不秀矣。

  有伤官用煞印者，伤多身弱，赖煞生印以邦身而制伤，如己未、丙子、庚子、丙子，蔡贵妃也。煞因伤而有制，两得其宜，只要无财，便为贵格，如壬寅、丁未、丙寅，夏阁老命是也。

  有伤官用官者，他格不用，金水独宜，然要财印为辅，不可伤官并透。如戊申、甲子、庚午、丁丑，藏癸露丁，戊甲为辅，官又得禄，所以为丞相之格。若孤官无辅，或官伤并透，则发福不大矣。

  若冬金用官，而又化伤为财，则尤为极秀极贵。如丙申、己亥、辛未、己亥，郑丞相命是也。

  然亦有非金水而见官，何也？化伤为财，伤非其伤，作财旺生官而不作伤官见官，如甲子、壬申、己亥、辛未，章丞相命也。

  至于伤官而官煞并透，只要干头取清，金水得之亦清，不然则空结构而已。

- 原注（原文注解）：
  　本章专论“伤官格”的多种形态与贵贱层次，核心在于：伤官本属“克官之神”，却又是最具“秀气与创造力”的十神之一。
  - 首段总纲：
    - 伤官虽非传统意义上的吉神，却是文人学士、创作型人才常见之格；
    - 夏木见水、冬金见火 → 顺时得气，更显其秀；
    - 格局比他格更多、变化尤多，必须细查气候（节令）、强弱、喜忌、纯杂，不能执一公式。

  针对文中几类典型伤官格，可归纳为：
  1) **伤官用财 / 伤官生财格**：
     - 伤官本“不利于民”，故为凶；
     - 若以伤官生财，使伤官成为“生官之具”，则转凶为吉，为最利格；
     - 前提是身强有根，方能承“伤→财→官”的链条。
  2) **化伤为财格**：
     - 直接把伤官化作财星，而非只看“伤生财”；
     - 尤以冬金见火、夏木见水等“气候配合得宜”者为上；
     - 文中以罗状元、秦龙图等命例说明“化伤为财”之秀气极盛.
  3) **财伤有情格**：
     - 财、伤之间既相生又相依，互不破坏；
     - 与“化伤为财”相较，其秀气不相上下.
  4) **伤官佩印格**：
     - 伤官旺、印根深而身略弱 → 印能制伤，伤反为秀；
     - 反要伤官旺、身稍弱而印有力，方显“以印制伤”的妙处；
     - 若伤轻身重而印多，则印反成负担，主贫.
  5) **伤官兼用财印格**：
     - 财印本相克，不宜并用；
     - 但若干头两清、不相碍，且“财重带印”或“印重带财”而能调和中和，则反为贵格；
  6) **伤官用煞印格**：
     - 伤多身弱，以煞生印、印制伤，一面护身，一面制伤；
     - 条件是“无财”→ 防财破印、党煞；
  7) **伤官用官格**：
     - 他格少用，金水独宜；
     - 必以财印为辅，不可伤官并透，否则成“伤官见官”之凶象；
  8) **伤官而官煞并透者**：
     - 只要干头取清、金水得之，则尚可成格；
     - 若浊乱不清，则只是“空结构”。

- 分字分词释义：
  - 伤官：十神之一，“我生之神”之偏，能生财又能克官，多主才华、表达、突破、批判；
  - 秀气：指才华外露、气质灵动之象；
  - 化伤为财：通过会合、化气等，使伤官之气转为财星之用；
  - 财伤有情：财与伤官之间生克有序、互相成就；
  - 佩印：以印绶制伤护身，如佩带印绶以示名分；
  - 伤官见官：伤官克制正官，未得制化，主对秩序与权威的冲突；
  - 官煞并透：正官、七煞同时透出于天干，争权混杂.

- **规范化释义（primary_lang_explained）**：
  可以把伤官理解为“过度输出与批判之力”：
  - 正面时：是创造力、批判思维、艺术天赋、表达能力；
  - 负面时：是任性、抗命、好胜与破坏秩序.
- **完整对等诠释（secondary_lang_full）**：  
  Hurting Officer is the power of excessive output and critique pushed to the point of challenging established order. At its best it appears as creativity, sharp intellect, artistic originality and the courage to question what is stale or unjust; at its worst it turns into defiance, quarrelsomeness, refusal to cooperate and the urge to tear down what others are trying to uphold. The structure of the chart tells us whether this force will mainly create new value, or mainly attack the Officer and the systems it represents.

  When Hurting Officer is linked to Printing, high output is disciplined and given a recognised place; when it drives Killing rather than attacking Proper Officer directly, it becomes a cutting edge used in dangerous fields; when it feeds Wealth, talent is converted into concrete projects and income instead of pure resistance. Only when Hurting Officer directly batters Officer without any Ink or alternative channels do we see the classic pattern of "talent pressuring position, words pressing authority". The old slogan "Hurting Officer seeing Officer brings a hundred disasters" is too rigid; the author emphasises that as long as there are real救应 mechanisms—Printing to restrain, Killing to substitute, Wealth to divert—Hurting Officer can be integrated into a larger order instead of being pure ruin.


  本章要说明的是：
  - 伤官若能转化为财（伤生财、化伤为财），则是一种“用才生财富、用批判生生产力”的模式；
  - 伤官若能佩印、用煞印，则是借制度与压力来约束“过度输出”，反成高阶格局；
  - 伤官若直接冲官而无印制，则成为“才压位、言压权”的风险结构.

- 详细解说：
  - 伤官格并非简单“好”或“坏”，而是高度依赖：
    - 日主强弱；
    - 财、官、印、煞与伤官之间的路径；
    - 格局是“用伤生财、伤生官、伤佩印、伤用煞印”哪一类.
  - 从现代视角：
    - 伤官强而有制，多见于创意工作者、技术突破者、批判性知识分子；
    - 伤官失控而无制，则多见于与体制冲突、言行过激、难以长期合作之人.

- **核心要点**：
  - 伤官虽非吉神，而有时用之，但要身强
  - 伤官用印，运喜印绶，身旺之地
  - 伤官用财，运喜财乡，食伤亦利
  - 伤官带煞，运喜印绶制伤护煞

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_561]` `[trigger: 伤官格的多重形态与秀]` `[role: 主干]` `[factor_trigger: shangguan_fei_jishen AND youshi_yongzhi AND xu_shenqiang]` 伤官虽非吉神，而有时用之，但要身强 → 《子平真诠》#下卷
  - `[ns_zpzy_562]` `[trigger: 伤官格的多重形态与秀]` `[role: 条件分支]` `[factor_trigger: shangguan_yongyin AND yunxi_yinshou AND shenwang_zhidi]` 伤官用印，运喜印绶，身旺之地 → 《子平真诠》#下卷
  - `[ns_zpzy_563]` `[trigger: 伤官格的多重形态与秀]` `[role: 条件分支]` `[factor_trigger: shangguan_yongcai AND yunxi_caixiang AND shishang_yili]` 伤官用财，运喜财乡，食伤亦利 → 《子平真诠》#下卷
  - `[ns_zpzy_564]` `[trigger: 伤官格的多重形态与秀]` `[role: 条件分支]` `[factor_trigger: shangguan_daisha AND yunxi_yinshou_zhishang_husha]` 伤官带煞，运喜印绶制伤护煞 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 伤官格主用类型     |        | new_candidate | 分型轴     | shang_yong_cai / hua_shang_wei_cai / shang_pei_yin / shang_yong_sha_yin / shang_yong_guan | 概括本章主要结构           |"""
    normalized_text_zh: str = """"""
    subject: str = "伤官格的多重形态与秀气层次"
    factor_refs: list = ['shangguan', 'xiuqi', 'shangguan_shengcai', 'huashang_weicai', 'caishang_youqing', 'shangguan_peiyin', 'shangguan_yongguan', 'shangguan_jianguan', 'engine_id', 'shangguan', 'bazi_rule_engine', 'shangguan_shengcai_ge', 'bazi_rule_engine', 'huashang_weicai_ge', 'bazi_rule_engine', 'shangguan_peiyin_ge', 'bazi_rule_engine', 'shangguan_jianyong_caiyin_ge', 'bazi_rule_engine', 'shangguan_yong_shayin_ge', 'bazi_rule_engine', 'shangguan_yongguan_ge', 'bazi_rule_engine', 'qihou_peihe', 'bazi_rule_engine', 'shangguan_jianguan', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_41_01', 'shangguan', 'rel_zpzq_41_02', 'shangguan', 'rel_zpzq_41_03', 'huashang_weicai', 'rel_zpzq_41_04', 'yinxing', 'rel_zpzq_41_05', 'qihou_peihe', 'rel_zpzq_41_06', 'qisha', 'rel_zpzq_41_07', 'shangguan_yongguan_ge', 'rel_zpzq_41_08', 'caiyin_liangqing', 'evi_zpzq_41_01', 'rule_shangguan_xiuqi', 'evi_zpzq_41_02', 'shangguan_shengcai_ge', 'rule_shangguan_shengcai_zhuanji', 'evi_zpzq_41_03', 'huashang_weicai_ge', 'rule_huashang_weicai_jixiu', 'evi_zpzq_41_04', 'shangguan_peiyin_ge', 'rule_shangguan_peiyin_tiaojian', 'evi_zpzq_41_05', 'shangguan_yongguan_ge', 'rule_jinshui_shangguan_jianguan', 'evi_zpzq_41_06', 'shangguan_yong_shayin_ge', 'rule_shangguan_yong_shayin', 'concept_creative_output', 'concept_talent_monetization', 'concept_discipline_creativity', 'concept_authority_conflict']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_伤官格的多重形态与秀气层次_001_L1",
    )
    version: str = "1.0.0"
