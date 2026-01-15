"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492308
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
    semantic_id="zpzq_v1.0.0_印格成局后的行运配法_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 印格成局后的行运配法(SemanticEntry):
    """
    - **原文（source_text）**：
  三十六、论印绶取运。
  印格取运，即以印格所成之局，分而配之。其印绶用官者，官露印重，财运反吉，伤食之方，亦为最利。
  
  若用官而带伤食，运喜...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十六、论印绶取运。
  印格取运，即以印格所成之局，分而配之。其印绶用官者，官露印重，财运反吉，伤食之方，亦为最利。
  
  若用官而带伤食，运喜官旺印绶之乡，伤食为害，逢煞不忌矣。
  
  印绶而用伤食，财运反吉，伤食亦利，若行官运，反见其灾，煞运则反能为福矣。
  
  印用七煞，运喜伤食，身旺之方，亦为美地，一见财乡，其凶立至。
  
  若用煞而兼带伤食，运喜身旺印绶之方，伤食亦美，逢官遇财，皆不吉也。
  
  印绶遇财，运喜劫地，官印亦亨，财乡则忌。
  
  印格而官煞竞透，运喜食神伤官，印旺身旺，行之亦利。若再透官煞，行财运，立见其灾矣。
  
  印用食伤，印轻者亦不利见财也。

- 原注（原文注解）：
  　　本章承接“三十五．论印绶”，从“静态印格”过渡到“行运中的印格表现”，说明：
  - 一旦印绶已在命局中成格，不同的用神结构（印用官、印用伤食、印用煞、印遇财、官煞竞透等），在行运上有完全不同的吉凶取舍；
  - 特别强调：
    - 有时财运反吉、有时财运立凶；
    - 有时煞运不忌，甚至反为福地；
    - 关键全在“原局如何用印”，以及“行运强化哪条链条”。
  
  关于“印绶用官”的取运：
  - “官露印重，财运反吉，伤食之方，亦为最利”：
    - 官透而印重，说明官印体系清楚而有力；
    - 一般印格忌财破印，但此类格局中，财运反而有利：
      - 财来可资官、助印，而不至于全破印根；
    - 伤食之运亦佳：
      - 适度伤食可泄身成秀，使印格不至于过于郁闭。
  
  关于“用官而带伤食”的取运：
  - “运喜官旺印绶之乡，伤食为害，逢煞不忌”：
    - 此时伤食的本性偏向“伤官”一面，易损官名；
    - 故行运宜加强官印之乡，使官印合力压制伤食；
    - 反而七煞之运不必过虑：
      - 煞与伤相缠，有时反能减轻伤食直伤官之力。
  
  关于“印绶而用伤食”的取运：
  - “财运反吉，伤食亦利，若行官运，反见其灾，煞运则反能为福”：
    - 原局以伤食泄印、泄身为主要用法，使印格转厚重为灵动；
    - 在此结构下：
      - 财运可受伤食所生，形成“食生财”的链条，故反而为吉；
      - 官运则容易来夺伤食之气，变成“伤官见官”，反主灾；
      - 煞运若有印护，则煞印相生，甚至可成为助力。
  
  关于“印用七煞”的取运：
  - “运喜伤食，身旺之方，亦为美地，一见财乡，其凶立至”：
    - 印格以煞生印为用，需日主身旺方可承受煞力；
    - 行伤食之运，可泄身成秀，又不至破印；
    - 一旦遇重财运，财来克印、党煞，则煞性外泄，凶祸立至。
  
  关于“用煞而兼带伤食”的取运：
  - “运喜身旺印绶之方，伤食亦美，逢官遇财，皆不吉”：
    - 煞生印、印护身，而伤食在旁泄身成秀；
    - 行运以身旺、印旺之地为佳，可固主干而不被煞压；
    - 官、财运皆不宜：
      - 官来与煞争权，破坏煞印关系；
      - 财来破印、党煞，使体系失衡。
  
  关于“印绶遇财”的取运：
  - “运喜劫地，官印亦亨，财乡则忌”：
    - 印绶本忌重财破印，此时宜比劫之运来分财护印；
    - 官印之运亦可，形成官印相生；
    - 再行重财之地，则印被削弱，反主不吉。
  
  关于“官煞竞透之印格”的取运：
  - “运喜食神伤官，印旺身旺，行之亦利。若再透官煞，行财运，立见其灾”：
    - 官煞并见而竞透时，易成纷争不清之象；
    - 行食神、伤官之运，可转部分官煞之气为“才华、产出”；
    - 若再行财运，则财来党煞、破印，引爆潜伏矛盾，故灾来迅速。
  
  关于“印用食伤”的取运：
  - “印用食伤，印轻者亦不利见财”：
    - 此类格局本以食伤泄印；
    - 若印本就偏轻，再遇财运克印，则印力全失，身失所依；
    - 故对“印轻而用食伤”者，尤忌重财之运。

- 分字分词释义：
  - 印格取运：以印绶为主格局时，就其结构分门别类，选择相应行运的方法。
  - 印绶用官：命局中以正官生印、印护身为主线之印格形态。
  - 印绶用伤食：以伤官、食神泄身成秀，同时兼顾印格之平衡的结构。
  - 印用七煞：以七煞生印、印护身的“煞印格”结构。
  - 劫地：比肩、劫财所在之地支与大运方位，主分财、助身。
  - 官煞竞透：正官与七煞同时在干上透出，彼此争权的状态。
  - 印用食伤：命局以食神、伤官调节印格强弱、转化为才华与成果之结构。

- **规范化释义（primary_lang_explained）**：
  若把“三十五．论印绶”看作“印格静态设计”，本章就是“印格在时间轴上的运行手册”：
  - 同样是印绶格：
    - 有的以官生印为主；
    - 有的以煞生印；
    - 有的以伤食泄印；
    - 有的则官煞并透、印遇财、印用食伤。
  - 行运好比给系统加“外部输入”：
    - 官运、煞运、财运、食伤运、比劫运，分别强化不同模块；
    - 若强化对的模块，就成“画龙点睛”；
    - 若强化错的模块，就成“放大缺陷”。

  例如：
  - 印绶用官格：
    - 官、印本已配合良好，再行财、伤运反能锦上添花；
  - 印绶用伤食格：
    - 结构本就以“食泄印、印护身”为主，行财运可顺势放大“食生财”；
    - 反而官运会压制伤食、冲突印格，变成“伤官见官”；
  - 煞印格：
    - 需要身旺、印旺才能驾驭煞力；
    - 一遇重财，则财破印、党煞，体系迅速失衡。

- 详细解说：
  - 本章再强调一个“系统论”视角：
    - 行运不是简单的“添一个五行”，而是改变系统内部各模块的相对强弱；
    - 同一个“财运”，在不同印格结构中，可以是救应，也可以是祸根。
  - 对现代工程化而言：
    - 不宜把“财运好、官运好、印运好”当成固定标签；
    - 在建模时，应将“原局结构 + 运势输入”视作组合特征，而非简单相加。

- **完整对等诠释（secondary_lang_full）**：  
  Luck that touches Printing must be read as a shift in the support system, not as the simple arrival of one extra god. In some structures, periods that bring Wealth and Food merely decorate an already solid Officer–Ink–body triangle, adding opportunities without shaking foundations. In others, the same Wealth will cut away at Ink, strip the native of backing, and leave the body exposed to pressure from Officer or Killing. A so‑called "good Wealth year" can therefore either fund studies and credentials, or undermine them, depending entirely on the existing Ink pattern.

  From a systems point of view, each luck period adjusts the relative strength of the modules: body, Printing, Officer/Killing, Wealth and output. We should describe periods in terms of how they rebalance this network—whether they reinforce the lines by which Ink protects and legitimises, or break those lines by over‑exciting Wealth and neglecting Printing. Treating "good Officer luck" or "good Ink luck" as fixed labels misses this dynamic; in modelling terms, the feature is always "natal structure + luck input" as a combination, not two independent scores simply added together.

- **核心要点**：
  - 印绶用官者，官露印重，财运反吉
  - 用官而带伤食，运喜官旺印绶之乡
  - 印绶而用伤食，财运反吉，伤食亦利
  - 印用七煞，运喜伤食，身旺之方
  - 印绶遇财，运喜劫地，官印亦亨

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_543]` `[trigger: 印格成局后的行运配法]` `[role: 主干]` `[factor_trigger: yinshou_yongguan AND guanlu_yinzhong AND caiyun_fanji]` 印绶用官者，官露印重，财运反吉 → 《子平真诠》#下卷
  - `[ns_zpzy_544]` `[trigger: 印格成局后的行运配法]` `[role: 条件分支]` `[factor_trigger: yongguan_daishangshi AND yunxi_guanwang_yinshou]` 用官而带伤食，运喜官旺印绶之乡 → 《子平真诠》#下卷
  - `[ns_zpzy_545]` `[trigger: 印格成局后的行运配法]` `[role: 条件分支]` `[factor_trigger: yinshou_yongshangshi AND caiyun_fanji AND shangshi_yili]` 印绶而用伤食，财运反吉，伤食亦利 → 《子平真诠》#下卷
  - `[ns_zpzy_546]` `[trigger: 印格成局后的行运配法]` `[role: 条件分支]` `[factor_trigger: yin_yong_qisha AND yunxi_shangshi AND shenwang_zhifang]` 印用七煞，运喜伤食，身旺之方 → 《子平真诠》#下卷
  - `[ns_zpzy_547]` `[trigger: 印格成局后的行运配法]` `[role: 条件分支]` `[factor_trigger: yinshou_yucai AND yunxi_jiedi AND guanyin_yiheng]` 印绶遇财，运喜劫地，官印亦亨 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 印格取运类型       | yinge_quyun_leixing        | new_candidate | 分型轴     | yin_yong_guan / yin_yong_shang_shi / yin_yong_qi_sha / yin_yong_sha_jian_shang / yin_yu_cai / guan_sha_jing_tou | bazi_rule_engine | 概括本章各类印格用运形态 |
| 关系类   | 身印强弱与行运     | shenyin_qiangruo_yunxiang        | new_candidate | 取运前提  | shen_qiang_yin_zhong / shen_qing_yin_qiang / shen_yin_daj致平衡              | bazi_rule_engine | 决定宜行帮身或泄印之运   |"""
    normalized_text_zh: str = """"""
    subject: str = "印格成局后的行运配法"
    factor_refs: list = ['yinge_quyun', 'yinshou_yongguan', 'yin_yong_qisha', 'guansha_jingtou', 'jiedi', 'caiyun_fanji', 'engine_id', 'yinge_leixing', 'bazi_rule_engine', 'yinge_xiyun', 'bazi_rule_engine', 'yinge_jiyun', 'bazi_rule_engine', 'guan_lu_yin_zhong', 'bazi_rule_engine', 'yinge_shayun_xiaoguo', 'bazi_rule_engine', 'cai_xiong_lizhi', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_36_01', 'yinshou_yongguan', 'rel_zpzq_36_02', 'yinshou_yongguan', 'rel_zpzq_36_03', 'yin_yong_shangshi', 'rel_zpzq_36_04', 'yin_yong_shangshi', 'rel_zpzq_36_05', 'yin_yong_qisha', 'rel_zpzq_36_06', 'yin_yong_qisha', 'rel_zpzq_36_07', 'yin_yu_cai', 'rel_zpzq_36_08', 'guansha_jingtou', 'evi_zpzq_36_01', 'rule_yin_yongguan_quyun', 'evi_zpzq_36_02', 'rule_yongguan_daishangshi_quyun', 'evi_zpzq_36_03', 'rule_yin_shangshi_quyun', 'evi_zpzq_36_04', 'rule_shayin_jicai_lizhi', 'evi_zpzq_36_05', 'rule_yin_yucai_quyun', 'evi_zpzq_36_06', 'guansha_jingtou', 'rule_guansha_jingtou_quyun', 'concept_system_input', 'concept_contextual_benefit', 'concept_sudden_crisis']
    
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
        l1_anchor="zpzq_v1.0.0_印格成局后的行运配法_001_L1",
    )
    version: str = "1.0.0"
