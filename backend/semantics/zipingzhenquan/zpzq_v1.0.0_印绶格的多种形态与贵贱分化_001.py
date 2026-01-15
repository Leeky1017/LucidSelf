"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492290
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
    semantic_id="zpzq_v1.0.0_印绶格的多种形态与贵贱分化_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 印绶格的多种形态与贵贱分化(SemanticEntry):
    """
    - **原文（source_text）**：
  三十五、论印绶。
  印绶喜其生身，正偏同为美格，故财与印不分偏正，同为一格而论之。印绶之格局亦不一，有印而透官者，正官不独取其生印，而即可以为用，与...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十五、论印绶。
  印绶喜其生身，正偏同为美格，故财与印不分偏正，同为一格而论之。印绶之格局亦不一，有印而透官者，正官不独取其生印，而即可以为用，与用煞者不同。故身旺印强，不愁太过，只要官星清纯，如丙寅、戊戌、辛酉、戊子，张参政之命是也。

  然亦有带伤食而贵者，则如朱尚书命，丙戌、戊戌、辛未、壬辰，壬为戊制，不伤官也。又如临淮侯命，乙亥、己卯、丁酉、壬寅，己为乙制，己不碍官也。

  有印而用伤食者，身强印旺，恐其太过，泄身以为秀气。如戊戌、乙卯、丙午、乙亥，李状元命也，若印浅身轻，而用层层伤食，则寒贫之局矣。

  有用偏官者，偏官本非美物，藉其生印，不得已而用之。故必身重印轻，或身轻印重，有所不足，始为有性。如茅状元命，己巳、癸酉、癸未、庚申，此身轻印重也。马参政命，壬寅、戊申、壬辰、壬寅，此身重印轻也。若身印并重而用七煞，非孤则贫矣。

  有用煞而兼带伤食者，则用煞而有制，生身而有泄，不论身旺印重，皆为贵格。

  有印多而用财者，印重身强，透财以抑太过，权而用之，只要根深，无防财破。如辛酉、丙申、壬申、辛亥，汪侍郎命是也。

  若印轻财重，又无劫财以救，则为贪财破印，贫贱之局也。

  即或印重财轻而兼露伤食，财与食相生，轻而不轻，即可就富，亦不贵矣。然亦有带食而贵者，何也？如庚寅、乙酉、癸亥、丙辰，此牛监薄命，乙合庚而不生癸，所以为贵，若合财存食，又可类推矣。如己未、甲戌、辛未、癸已，此合财存食之贵也。

  又有印而兼透官煞者，或合煞，或有制，皆为贵格。如辛亥、庚子、甲辰、乙亥，此合煞留官也；壬子、癸卯、丙子、己亥，此官煞有制也。

  至于化印为劫，弃之以就财官，如赵知府命，丙午、庚寅、丙午、癸已，则变之又变者矣。

  更有印透七煞，而劫财以存煞印，亦有贵格，如庚戌、戊子、甲戌、乙亥是也。然此格毕竟难看，宜细详之。

- 原注（原文注解）：
  　　本章专论“印绶格”的多种形态及其富贵高下，延续前文对财格、官格的分析方式，把印格拆成若干典型组合：
  - 先提出总纲：正印、偏印（枭印）在“生身”这一功能上同属一类，因此“财与印不分偏正，同为一格而论”；
  - 再分述诸多变型：
    - 有印透官者；
    - 印带伤食者；
    - 借偏官生印者；
    - 煞印并用且兼带伤食者；
    - 印多而用财者；
    - 贪财破印者；
    - 合财存食、兼透官煞、化印为劫等变格。

  首段强调印绶的本义与大原则：
  - 印绶以“生身”为职，凡能增益日主根气者均属喜用；
  - 正印、偏印在本章中不做严格区分，而是以“是否生身、有无情”为核心判断；
  - “有印而透官”：
    - 正官既生印又可直接为用，与“用煞生印”的险格不同；
    - 身旺印强时，不怕印过，只要官星清纯不杂煞，即可成贵。

  接着论“印带伤食而反成贵”的情况：
  - 朱尚书、临淮侯两造：
    - 表面看印旁带伤食，似有损官之虞；
    - 实则壬水为戊土所制、己土为乙木所制，使伤食不致伤官；
    - 体现“有制之伤食，可以成秀而不成害”。

  再论“印而用伤食”的格局：
  - 身强印旺，恐其太过，则以伤食泄秀，转厚重为灵动；
  - 若印浅身轻而仍用层层伤食，则“泄过其身”，易成寒贫之局。

  关于“借偏官生印”：
  - 偏官本属凶物，但若用其生印，则转成“不得已而用之”；
  - 必须是在“身重印轻”或“身轻印重”的不平衡状态下，以偏官弥补不足；
  - 若身印两重而又用七煞，则失去平衡，易成孤贫。

  关于“用煞而兼带伤食”：
  - 七煞生印以护身，伤食又泄身以成秀；
  - 在“有制、有泄”的前提下，身旺印重亦可贵，体现高阶格局的复合性。

  关于“印多而用财”与“贪财破印”：
  - 印重身强，透财以抑太过，是“以财节印”的用法，前提是财有根、不致破印；
  - 若印轻财重、且无劫财救印，则为“贪财破印”，主贫贱。

  关于“印重财轻而兼露伤食”：
  - 财虽轻，但有伤食相生，整体“轻而不轻”，可就富而未必大贵；
  - 然而若通过“合财存食”使食神得以保留，则又可在富中见贵。

  关于“印兼透官煞”：
  - 若能“合煞留官”或“官煞有制”，则印、官、煞三者之间形成有序结构，反成佳局；
  - 否则便成官煞混杂、印无所依之病。

  关于“化印为劫、弃印就财官”与“印透七煞而劫财存印”：
  - “化印为劫”是从印格转向劫比、财官体系的极端变化，成败在乎全局；
  - “印透七煞而劫财存煞印”则以劫财去财留印留煞，格局颇险，虽有可贵之处，却“毕竟难看，宜细详之”。

- 分字分词释义：
  - 印绶：十神之一，主生身、护身、护官，亦主学识、名分、资历。
  - 正印 / 偏印：正印偏重护身、护官；偏印（枭印）偏重思维、机变，过重则多疑偏执。
  - 用印：以印为格局核心，用其生身、护官、护财。
  - 偏官：即七煞，本非美物，然可用来生印或成煞印格局。
  - 化印为劫：印星转为比劫之用，不再以印为主，而从比劫、财官体系取用。
  - 贪财破印：以财克印，致使印绶无力护身，身与官皆失其依。
  - 合财存食：通过合化去财而留食，使食神得以发挥成秀之用。
  - 合煞留官：以合化方式使煞被合去而官星得以独立成用。

- **规范化释义（primary_lang_explained）**：
  若从结构上看，本章在回答两个问题：
  1) 印绶做主格时，什么组合是“锦上添花”，什么组合是“添乱”？
  2) 当财、官、煞、伤食同时出现时，印格还能否保持“生身护身”的主线？

  可以把印绶理解为一个人“被支持、被认证”的系统：
  - 正印偏向“正规体系的认证”（学历、任命、师承等）；
  - 偏印偏向“非正规渠道的资源”（偏才、机缘、灵感等）。

  在此基础上：
  - **印 + 官**：
    - 官清而生印 → 有位有名，且有制度性支持，是正统权威型；
    - 印多而官弱 → 易变成资格很多而权力有限。
  - **印 + 伤食**：
    - 身旺印重时，适度伤食为“泄秀”，让人有表达、有作品；
    - 身轻印浅而再加伤食，则变成“透支自己”，难以承受。
  - **印 + 偏官（七煞）**：
    - 若以煞生印、印护身，且煞印有制有序，是“险而有功”的格局；
    - 若官煞杂乱无制，则印亦无从发挥。
  - **印 + 财**：
    - 印多而用财 → 用财削印之过，令格局不致过于封闭；
    - 印轻财重 → 财来破印，成为“有财无靠”的贫贱象。

- **完整对等诠释（secondary_lang_full）**：  
  Printing represents everything that gives the Day Master backing: learning, qualifications, institutions, elders and texts. The value of an Ink pattern does not lie simply in "more Ink" or "less Ink", but in whether this backing truly serves the self and the Officer, or is hollowed out by Wealth, disturbed by Killing, or constantly leaked away by Food and Hurting spirits. Strong, well‑placed Ink can turn a fragile body or a harsh Killing into an honourable path; broken Ink often shows as credentials that are not recognised, support systems that repeatedly fail, or knowledge that never quite protects the native.

  Seen from a social perspective, those with sound Ink patterns tend to have stable affiliations: regular schools, organisations, professional licences, elders who can be relied on. When Ink is withered or repeatedly attacked, we more often see people whose background looks respectable on paper yet does not convert into real protection, or whose support networks collapse at key moments. In every case, the question is whether Ink successfully nourishes body and Officer, or whether it is being eroded by Wealth, confused by Killing and exhausted by constant泄气.

- **核心要点**：
  - 印绶喜其生身，正偏同为美格
  - 有印透官：身旺印强不愁太过，只要官星清纯
  - 印带伤食而贵：伤食有制则不伤官
  - 印而用伤食：身强印旺恐其太过，泄身以为秀气
  - 用偏官生印：必身重印轻或身轻印重，始为有情
  - 印多而用财：印重身强，透财以抑太过
  - 印轻财重无劫财救：贪财破印，贫贱之局
  - 印兼透官煞：合煞或有制，皆为贵格

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_535]` `[trigger: 印绶格]` `[role: 主干]` `[factor_trigger: yinshou_xiqi_shengshen AND zhengpian_tongwei_meige]` 印绶喜其生身，正偏同为美格。 → 《子平真诠》#下卷
  - `[ns_zpzy_536]` `[trigger: 印透官]` `[role: 条件分支]` `[factor_trigger: yin_touguan AND shenwang_yinqiang AND guanxing_qingchun]` 有印而透官者，身旺印强，不愁太过，只要官星清纯。 → 《子平真诠》#下卷
  - `[ns_zpzy_537]` `[trigger: 印用伤食]` `[role: 条件分支]` `[factor_trigger: yin_yong_shangshi AND shenqiang_yinwang AND xieshen_weishou]` 有印而用伤食者，身强印旺，恐其太过，泄身以为秀气。 → 《子平真诠》#下卷
  - `[ns_zpzy_538]` `[trigger: 印用偏官]` `[role: 条件分支]` `[factor_trigger: pianguan_fei_meiwu AND jie_qi_shengyin AND budeyi_er_yong]` 偏官本非美物，藉其生印，不得已而用之。 → 《子平真诠》#下卷
  - `[ns_zpzy_539]` `[trigger: 印多用财]` `[role: 条件分支]` `[factor_trigger: yin_duo_yongcai AND yinzhong_shenqiang AND toucai_yi_taiguo]` 有印多而用财者，印重身强，透财以抑太过。 → 《子平真诠》#下卷
  - `[ns_zpzy_540]` `[trigger: 贪财破印]` `[role: 条件分支]` `[factor_trigger: yinqing_caizhong AND wu_jiecai_jiu AND tancai_poyin_pinjian]` 若印轻财重，又无劫财以救，则为贪财破印，贫贱之局也。 → 《子平真诠》#下卷
  - `[ns_zpzy_541]` `[trigger: 印兼官煞]` `[role: 条件分支]` `[factor_trigger: yin_jian_tou_guansha AND (hesha OR youzhi) AND guige]` 有印而兼透官煞者，或合煞，或有制，皆为贵格。 → 《子平真诠》#下卷
  - `[ns_zpzy_542]` `[trigger: 印格边界]` `[role: 总结]` `[factor_trigger: yinge_bijing_nankan AND yi_xi_xiangzhi]` 然此格毕竟难看，宜细详之。 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签       | 因子ID | 因子来源     | 角色/位置  | 取值/约束                                                                 | 备注                     |
|----------|----------------|--------|--------------|------------|----------------------------------------------------------------------------|--------------------------|
| 结构类   | 印格类型       |        | new_candidate | 分型轴     | qing_chun_zheng_yin / yin_tou_guan / yin_dai_shang_shi / yin_yong_qi_sha / yin_duo_yong_cai / hua_yin_wei_jie | 概括本章主要印格形态   |
| 关系类   | 身印轻重关系   |        | new_candidate | 平衡条件  | shen_qiang_yin_qiang / shen_qing_yin_zhong / shen_yin_da致平衡              | 影响是否需泄身或抑印   |"""
    normalized_text_zh: str = """"""
    subject: str = "印绶格的多种形态与贵贱分化"
    factor_refs: list = ['yinshou', 'zhengpian_tongge', 'yin_touguan', 'xieshenweixiu', 'jiesha_shengyin', 'tancai_poyin', 'hesha_liuguan', 'huayin_weijie', 'engine_id', 'yinshou', 'bazi_rule_engine', 'yin_touguan_ge', 'bazi_rule_engine', 'yin_yong_shangshi_ge', 'bazi_rule_engine', 'yin_yong_pianguan_ge', 'bazi_rule_engine', 'yinduo_yongcai_ge', 'bazi_rule_engine', 'tancai_poyin', 'bazi_rule_engine', 'shenyin_qingzhong', 'bazi_rule_engine', 'shangshi_youzhi', 'bazi_rule_engine', 'yin_jian_guansha_ge', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_35_01', 'yinshou', 'rel_zpzq_35_02', 'guanxing', 'rel_zpzq_35_03', 'shangshi', 'rel_zpzq_35_04', 'qisha', 'rel_zpzq_35_05', 'caixing', 'rel_zpzq_35_06', 'caixin', 'rel_zpzq_35_07', 'shangshi_youzhi', 'rel_zpzq_35_08', 'hesha_liuguan', 'evi_zpzq_35_01', 'rule_yinshou_zhengpian_tongge', 'evi_zpzq_35_02', 'yin_touguan_ge', 'rule_yin_touguan_ge', 'evi_zpzq_35_03', 'rule_yin_shangshi_xiexiu', 'evi_zpzq_35_04', 'yin_yong_shangshi_ge', 'rule_yinqian_shangshi_ji', 'evi_zpzq_35_05', 'rule_sha_shengyin_tiaojian', 'evi_zpzq_35_06', 'tancai_poyin', 'rule_tancai_poyin_xiong', 'evi_zpzq_35_07', 'yin_jian_guansha_ge', 'rule_yin_guansha_hezhi', 'concept_support_system', 'concept_credential_authority', 'concept_expression_channel', 'concept_support_erosion']
    
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
        l1_anchor="zpzq_v1.0.0_印绶格的多种形态与贵贱分化_001_L1",
    )
    version: str = "1.0.0"
