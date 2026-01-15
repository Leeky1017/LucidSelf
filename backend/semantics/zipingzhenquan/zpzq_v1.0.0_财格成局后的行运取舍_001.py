"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492272
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
    semantic_id="zpzq_v1.0.0_财格成局后的行运取舍_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 财格成局后的行运取舍(SemanticEntry):
    """
    - **原文（source_text）**：
  三十四、论财取运。
  财格取运，即以财格所就之局，分而配之。
  其财旺生官者，运喜身旺印缓，不利七煞伤官；
  若生官而后透印，伤官之地，不甚有害...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十四、论财取运。
  财格取运，即以财格所就之局，分而配之。
  其财旺生官者，运喜身旺印缓，不利七煞伤官；
  若生官而后透印，伤官之地，不甚有害。
  至于生官而带食破局，则运喜印绶，而逢煞反吉矣。

  财用食生，财食重而身轻，则喜助身；
  财食轻而身重，则仍行财食。
  煞运不忌，官印反晦矣。

  财格佩印，运喜官乡，身弱逢之，最喜印旺。

  财用食印，财轻则喜财食，身轻则喜比印，官运有碍，煞反不忌也。

  财带伤官，财运则亨，煞运不利，运行官印，未见其美矣。

  财带七煞，不论合煞制煞，运喜食伤身旺之方。

  财用煞印，印旺最宜，逢财必忌。
  伤食之方，亦任意矣。

- 原注（原文注解）：
  　　本章是三十三章“论财”的行运篇，对已经形成不同“财格”的命局，分别说明行运取舍的大原则：
  - 先分清命局属于哪一类财格（财旺生官、财用食生、财格佩印、财用食印、财带伤官、财带七煞、财用煞印等）；
  - 再按“身强身弱、财重财轻、官煞轻重”的情况，选择相宜之运；
  - 同一类财格，在不同行运组合下，吉凶可以南辕北辙。

  关于“财旺生官”之取运：
  - 原文云“运喜身旺印缓，不利七煞伤官”：
    - 身旺印缓 → 以身、印承财所生之官，使“财→官→身”链条稳定；
    - 忌七煞、伤官 → 以防煞来争权、伤官败官，破坏财生官的主线。
  - “若生官而后透印，伤官之地，不甚有害”：
    - 先有财生官，再以印护身，伤官虽现，因官印有根，尚不至全毁；
    - 说明“次序与量级”会影响同一伤官运的吉凶程度。
  - “生官而带食破局，则运喜印绶，而逢煞反吉”：
    - 若命局中食神过多，削弱财生官的纯度，则需行印运以“抬高官印系统”；
    - 此时反而“煞运略吉”，因为煞可与食伤纠缠，引去其病势。

  关于“财用食生”之取运：
  - “财食重而身轻，则喜助身”：
    - 身弱而财食重 → 需先补身，使其能承受食生财、财生官的链条；
  - “财食轻而身重，则仍行财食”：
    - 身强而财食略轻 → 可多走财运、食伤运，以放大“食生财”的优势；
  - “煞运不忌，官印反晦”：
    - 此类命局本不依靠官印，过多官印反而“压抑食财之用”；
    - 煞运反而不甚可惧，只要不过分破身。

  关于“财格佩印”之取运：
  - “运喜官乡，身弱逢之，最喜印旺”：
    - 财格但佩印护身 → 行官运可以使“财生官、官得印护”，富贵并举；
    - 身弱者尤喜印旺之运，印来援身，使财、官不过分压身。

  关于“财用食印”之取运：
  - “财轻则喜财食”：
    - 若命中财偏轻，则需以财运、食运加强“食生财”链条；
  - “身轻则喜比印”：
    - 若日主偏弱，则以比劫、印绶运补身，使其有力驾驭财印体系；
  - “官运有碍，煞反不忌”：
    - 官运容易压制食神的活力，反令格局失衡；
    - 煞运若有印制，可反成“煞印相生”，未必为凶。

  关于“财带伤官”之取运：
  - “财运则亨，煞运不利”：
    - 伤官本能生财，财运到来，多主财路亨通；
    - 若再遇煞运，则易成“伤官见煞”之险局，凶性大增；
  - “运行官印，未见其美”：
    - 官印虽可约束伤官，但若力度失衡，反造成“官伤对峙”，不利顺达。

  关于“财带七煞”之取运：
  - “不论合煞制煞，运喜食伤身旺之方”：
    - 无论命局是以合煞存财，还是制煞生财；
    - 行运以食伤与帮身为佳，使身能驾驭财煞之力，而不被反噬。

  关于“财用煞印”之取运：
  - “印旺最宜，逢财必忌”：
    - 命局以煞印体系为主，印旺则煞得化，身得护；
    - 财来则伤印、助煞，故“逢财必忌”；
  - “伤食之方，亦任意矣”：
    - 在印足以护身之前提下，伤食运可视为“活泼之气”，可适度任其发挥。

- 分字分词释义：
  - 财格取运：针对以财为主格局的命局，选择合宜行运的原则与方法。
  - 财旺生官：财星有根有力，主要作用是生官，而非党煞或耗身。
  - 食生财：以食神泄身生财，财再生官，形成温和柔顺的生克链条。
  - 佩印：以印绶护身、护官、护财，如佩戴印绶以示名分。
  - 食印：命局中同时有食神与印绶参与财格结构。
  - 财带伤官：命局中财与伤官彼此关联，以伤官生财或伤财并见。
  - 财带七煞：财与七煞同现，或财助煞，或以煞制身而借财为用。
  - 财用煞印：以七煞生印，印护身与财，是“煞印相生”体系中的财格形态。

- **规范化释义（primary_lang_explained）**：
  这一篇可以看作“三十三．论财”的“时间维度版”，在问：
  > 已成的财格，在不同大运、流年里，会朝哪个方向放大？

  若用工程语言描述：
  - 命局是“静态结构”；
  - 行运是“外部输入”；
  - 财格取运就是：
    - 识别系统当前是“财→官→身”、“食→财→官”、“煞→印→身”哪种主链条；
    - 再决定在时间轴上加什么输入，会让系统更稳定，而不是崩溃。

  各类财格行运逻辑，可概括为：
  - 财旺生官格：
    - 先扶身、印，再谈加财与官；
    - 忌再添煞与伤官，避免“权力系统过载”。
  - 财用食生格：
    - 以食神为“柔性驱动”，忌官印夺其气；
    - 身弱则先补身，身强则扩展财与食。
  - 财格佩印：
    - 财是资源，印是合法性，官是位；
    - 运上以“官地＋印旺”为最佳组合。
  - 财用食印：
    - 食与印同在，要么补财，要么补身；
    - 官运过重则压制整体灵活度。
  - 财带伤官、财带七煞：
    - 都是“锋利型财格”，宜以食伤、帮身行运来调和锋芒；
  - 财用煞印：
    - 关键在印足以化煞，行运以印与身为本，避再行重财。

- 详细解说：
  - “财格取运”的本质，不是简单地说“见财必富”，而是：
    - 识别财在系统中的角色：是为官服务、为煞服务，还是为身服务；
    - 再看行运是强化这个角色，还是把它扭曲成负担；
  - 文中多次出现“煞反不忌”“逢煞反吉”之类句子：
    - 提醒我们：任何一神，都有“合适的位置与剂量”；
    - 离开具体结构谈“吉凶”，只会流于空谈。

- **完整对等诠释（secondary_lang_full）**：  
  Luck that touches Wealth must always be judged within the specific Wealth structure. Periods that appear to be "money luck" can in fact deepen debt, intensify competition or expose the native to risky ventures if the underlying chart is already overloaded with Wealth and lacks support. Conversely, in charts where Wealth is meant to feed Officer, collaborate with Killing, or serve the Day Master’s development, the right mix of Food, Printing and moderate Wealth can turn sharp, dangerous combinations into opportunities to harness resources and influence.

  Thus, Wealth periods are not judged by the slogan "seeing Wealth means becoming rich", but by whether they reinforce the role Wealth is supposed to play in this system. If Wealth is to serve Officer, good periods help stabilise the order and protect assets; if Wealth is to temper Killing, good periods bring enough Printing and body strength to control risk; if Wealth is to nourish the self, good periods allow sustained investment in skills and projects without overextension. The same Wealth sign can either strengthen function or twist into a burden depending on context; only by returning to structure can we see which way a given period will bend.

- **核心要点**：
  - 财旺生官：运喜身旺印绶，不利七煞伤官
  - 生官而带食破局，则运喜印绶，逢煞反吉
  - 财用食生：财食重身轻喜助身，身重则行财食运
  - 财格佩印：运喜官乡，身弱最喜印旺
  - 财用食印：财轻喜财食，身轻喜比印，官运有碍
  - 财带伤官：财运则亨，煞运不利
  - 财带七煞：运喜食伤身旺之方
  - 财用煞印：印旺最宜，逢财必忌

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_525]` `[trigger: 印绶喜其生身]` `[role: 主干]` `[factor_trigger: yinshou_shengshen AND zhengpian_yinshou]` 印绶喜其生身，正偏同为美格，故财与印不分偏正，同为一格而论之。 → 《子平真诠》#下卷
  - `[ns_zpzy_526]` `[trigger: 有印而透官者]` `[role: 条件分支]` `[factor_trigger: youyin_touguan AND zhengguan_shengyin]` 有印而透官者，正官不独取其生印，而即可以为用，与用煞者不同。 → 《子平真诠》#下卷
  - `[ns_zpzy_527]` `[trigger: 印带伤食而贵者]` `[role: 条件分支]` `[factor_trigger: yin_dai_shangshi AND shangshi_buji_shengguan]` 然亦有带伤食而贵者，则如朱尚书命，丙戌、戊戌、辛未、壬辰，壬为戊制，不伤官也。 → 《子平真诠》#下卷
  - `[ns_zpzy_528]` `[trigger: 有印而用伤食者]` `[role: 条件分支]` `[factor_trigger: youyin_yongshangshi AND shenqiang_yinwang]` 有印而用伤食者，身强印旺，恐其太过，泄身以为秀气。 → 《子平真诠》#下卷
  - `[ns_zpzy_529]` `[trigger: 借偏官生印者]` `[role: 条件分支]` `[factor_trigger: jiepianguan_shengyin AND shenqing_yinjian]` 借偏官生印者，偏官本非美物，藉其生印，不得已而用之。 → 《子平真诠》#下卷
  - `[ns_zpzy_530]` `[trigger: 用煞而兼带伤食者]` `[role: 条件分支]` `[factor_trigger: yongsha_jian_dai_shangshi AND sha_sheng_yin_shangshi_xie]` 用煞而兼带伤食者，则用煞而有制，生身而有泄，不论身旺印重，皆为贵格。 → 《子平真诠》#下卷
  - `[ns_zpzy_531]` `[trigger: 印多而用财者]` `[role: 条件分支]` `[factor_trigger: yin_duo_yongcai AND yinzhong_shenqiang]` 印多而用财者，印重身强，透财以抑太过，权而用之，只要根深，无防财破。 → 《子平真诠》#下卷
  - `[ns_zpzy_532]` `[trigger: 贪财破印者]` `[role: 条件分支]` `[factor_trigger: tancai_poyin AND yinqing_caizhong]` 贪财破印者，以财克印，致使印绶无力护身，身与官皆失其依。 → 《子平真诠》#下卷
  - `[ns_zpzy_533]` `[trigger: 合财存食者]` `[role: 条件分支]` `[factor_trigger: hecai_cunshi AND shangshi_xiecai]` 合财存食者，通过合化去财而留食，使食神得以发挥成秀之用。 → 《子平真诠》#下卷
  - `[ns_zpzy_534]` `[trigger: 合煞留官者]` `[role: 条件分支]` `[factor_trigger: he_sha_liu_guan AND sha_he_guan_zheng]` 合煞留官者，以合化方式使煞被合去而官星得以独立成用。 → 《子平真诠》#下卷

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 财格类型           | caige_leixing        | new_candidate | 分型轴       | cai_wang_sheng_guan / cai_yong_shi_sheng / cai_ge_pei_yin / cai_yong_shi_yin / cai_dai_shang_guan / cai_dai_qi_sha / cai_yong_sha_yin | bazi_rule_engine | 取运前必须先行分型         |"""
    normalized_text_zh: str = """"""
    subject: str = "财格成局后的行运取舍"
    factor_refs: list = ['caige_quyun', 'shenwang_yinshou', 'caishi_zhong_shenqing', 'guanxiang', 'sha_fan_buji', 'feng_cai_biji', 'engine_id', 'caige_leixing', 'bazi_rule_engine', 'shenwang_chengdu', 'bazi_rule_engine', 'xiyun_fangxiang', 'bazi_rule_engine', 'jiyun_fangxiang', 'bazi_rule_engine', 'caishi_qingzhong', 'bazi_rule_engine', 'yinwang_chengdu', 'bazi_rule_engine', 'shayun_xiaoguo', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_34_01', 'caiwang_shengguan_ge', 'rel_zpzq_34_02', 'caiwang_shengguan_ge', 'rel_zpzq_34_03', 'caishi_qingzhong', 'rel_zpzq_34_04', 'caishi_qingzhong', 'rel_zpzq_34_05', 'caige_peiyin_ge', 'rel_zpzq_34_06', 'caidai_shangguan_ge', 'rel_zpzq_34_07', 'caidai_qisha_ge', 'rel_zpzq_34_08', 'caiyong_shayin_ge', 'rel_zpzq_34_09', 'caiyong_shayin_ge', 'evi_zpzq_34_01', 'caige_leixing', 'rule_caige_quyun_fenxing', 'evi_zpzq_34_02', 'rule_caiwang_shengguan_quyun', 'evi_zpzq_34_03', 'shayun_xiaoguo', 'rule_shidai_poju_shafanji', 'evi_zpzq_34_04', 'rule_caishi_qingzhong_dingyun', 'evi_zpzq_34_05', 'rule_peiyin_quyun', 'evi_zpzq_34_06', 'caidai_shangguan_ge', 'rule_caidai_shangguan_quyun', 'evi_zpzq_34_07', 'rule_shayin_jicai', 'concept_timing_adaptation', 'concept_capacity_balance', 'concept_contextual_reversal']
    
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
        l1_anchor="zpzq_v1.0.0_财格成局后的行运取舍_001_L1",
    )
    version: str = "1.0.0"
