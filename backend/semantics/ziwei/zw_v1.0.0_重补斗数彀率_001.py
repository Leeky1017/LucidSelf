"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725477
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
    semantic_id="zw_v1.0.0_重补斗数彀率_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 重补斗数彀率(SemanticEntry):
    """
    - 原文（source_text）：

  诸星吉多逢凶也吉，诸恶星多逢吉也凶。星更缠度，数分定局，重在看星得垣受制，方可论人祸福穷通。大槩以身命为祸福之柄，以根源为穷通之机。紫微在命，辅弼同垣，其贵...
    """
    
    original_text: str = """- 原文（source_text）：

  诸星吉多逢凶也吉，诸恶星多逢吉也凶。星更缠度，数分定局，重在看星得垣受制，方可论人祸福穷通。大槩以身命为祸福之柄，以根源为穷通之机。紫微在命，辅弼同垣，其贵必矣。财印夹命，日月夹财，其富何疑。荫福临不怕凶冲；日月会不如合照。贪狼居子，乃为泛水桃花；天刑遇贪，必主风流刑杖。紫微坐命库，则曰金举捧御辇；临官安文曜，号为衣锦惹天杳。太阴合文曲于妻宫，翰林清异；太阳会文昌于官禄，金殿传胪。禄合守田财，为烂谷堆金；财荫居迁移，为高商豪客。耗居败地，沿途丐求；贪会旺宫，终身用窃；杀居绝地，生成三十二之颜回，日在旺宫，可学八百年之彭祖。巨暗同垣于身命，疾厄羸瘦其躯；凶星交会于相貌迁移，伤刑其面。大耗会廉贞于官禄，枷杽囚徒；官符会刑杀于迁移，离卿远配；七杀临于陷地，流羊必见死亡。耗杀忌逢破军，火铃嫌逢太岁。奏书博士，并官禄以长乎吉祥；力士将军与青龙以显其威福。童子限弱，水上浮泡；老人限衰，风中燃烛。遇杀必惊，流年最紧。人生发达，限元最怕浮沉，一世沌澶，命限逢乎驳杂。论而至此，允矣玄微。

- 原注：

  本篇名为"重补彀率"，"彀率"即法则、准则之意。在前面《准绳》《发微》基础上再次"重补"，通过大量格局口诀与吉凶组合，建立更为细化的判断标准，使学者在实际推命时有"彀率"可依。

- 分字分词释义：

  - **彀率**：法则、准则，此处指斗数推命的实务规则与口诀体系。
  - **星更缠度**：星曜在不同宫度上的缠绕配置，"缠度"指星与宫的精确对应关系。
  - **得垣受制**：得其本垣本位为"得垣"，受到他星制化为"受制"，两者结合决定星曜真实力量。
  - **身命为祸福之柄**：命宫、身宫是判断一生祸福的主要抓手与杠杆。
  - **根源为穷通之机**：禄存等根气是决定一生穷通起伏的关键机制。
  - **财印夹命**：财星与印星夹辅命宫，主富贵双全。
  - **日月夹财**：太阳、太阴夹拱财帛宫，主财源广进、不权则富。
  - **泛水桃花**：贪狼居子水之地，桃花星遇旺水，主情欲放纵、风流多情。
  - **金举捧御辇**：紫微坐命库（如辰戌丑未），象征皇帝乘坐华贵车舆，主富贵显赫。
  - **翰林清异**：太阴合文曲于妻宫，主配偶清秀有文才，或本人因妻得文名。
  - **金殿传胪**：太阳会文昌于官禄，主科甲及第、官场显达。
  - **烂谷堆金**：禄存守田宅财帛，主财富丰厚、积谷如山。

- 规范化释义（primary_lang_explained）：

  身命宫是祸福的主要抓手，禄存等根气是穷通的关键机制。紫微在命若有辅弼同垣，其贵无疑；财印夹命、日月夹财，其富何疑。荫星福星临命不怕凶冲；日月会合不如合照更佳。贪狼居子为泛水桃花，主风流多情；天刑遇贪，必主风流而招刑杖。紫微坐命库则贵如"金举捧御辇"；太阴合文曲于妻宫，主"翰林清异"；太阳会文昌于官禄，可"金殿传胪"。禄存守田财为"烂谷堆金"；财荫居迁移为"高商豪客"。

  反面组合同样明确：耗星居败地则沿途丐求；贪狼会旺宫则终身偷窃；七杀居绝地则短寿如颜回；巨门暗曜同垣身命则疾厄羸瘦；凶星交会相貌迁移则伤刑其面。大耗会廉贞于官禄主枷杽囚徒；官符会刑杀于迁移主离乡远配；七杀临陷地遇流羊必见死亡。

  最后强调限运的脆弱性：童限如水上浮泡、老限如风中燃烛，遇杀必惊。人生发达关键在限元不可浮沉，一世沌澶多因命限驳杂。论至此处，斗数玄微已可见矣。

- 核心要点：

  1. **吉凶互转的整体观**：吉星多者逢凶也吉、凶星多者逢吉也凶，强调看整体力量对比而非单一星曜。
  2. **身命与根源的双重抓手**：身命为祸福之柄、根源为穷通之机，两者缺一不可。
  3. **格局口诀的密集呈现**：财印夹命、日月夹财、泛水桃花、金举捧御辇、翰林清异、金殿传胪、烂谷堆金等，提供大量可操作的判断标准。
  4. **极端正负对比**：彭祖八百岁vs颜回三十二岁、金殿传胪vs枷杽囚徒、烂谷堆金vs沿途丐求。通过对比强化记忆与判断。
  5. **限运脆弱期的特别提示**：童限老限遇杀必惊，限元浮沉决定一生发达与否。

- 详细解说：

  1. **"吉多逢凶也吉、凶多逢吉也凶"的辩证法**  
     本条开篇即建立辩证观：不能简单说"某星吉"或"某星凶"，而要看整体配置中吉星与凶星的数量对比、力量对比与位置对比。若吉星占主导，即便遇到部分凶星，也能化凶为吉；反之，若凶星占主导，即便有部分吉星，也难以真正成吉。这是对前文"吉凶互藏"理念的进一步深化。

  2. **格局口诀的实用价值**  
     本条密集呈现了十几个格局口诀，如"财印夹命""日月夹财""泛水桃花""金举捧御辇""翰林清异""金殿传胪""烂谷堆金"等。这些口诀不是单纯的文学修辞，而是对特定星曜组合与宫位配置的精炼概括。在实际推命时，可以快速定位命局特征，提高判断效率。

  3. **极端正负对比的教学策略**  
     文中多处采用极端对比：彭祖八百岁vs颜回三十二岁、金殿传胪vs枷杽囚徒、烂谷堆金vs沿途丐求。通过这种强烈对比，让学者深刻记忆不同组合的吉凶差异，避免混淆。

  4. **童限老限的脆弱性警示**  
     "童子限弱，水上浮泡；老人限衰，风中燃烛"，点出人生两端最脆弱的时段。在这两个阶段，即便本命结构尚可，若限运遇凶，也容易应验为重大灾祸。这是对《发微论》中同类提示的再次强调，提醒命师在这两个阶段需格外谨慎。

  5. **限元浮沉与命限驳杂**  
     最后总结："人生发达，限元最怕浮沉；一世沌澶，命限逢乎驳杂。"点出：一生能否发达，关键在于限运是否稳定（不浮沉）；一生若混沌不清，多因本命与限运配置驳杂（矛盾冲突）。这是对前文"命—限"二元结构的最终归纳。

- 校勘与字词辨析：

  - **"彀率"**：诸本多同，"彀"本义为张弓满弦、射中目标，引申为法则、准则。本条即以"重补法则"为主题。
  - **"金举"**：部分版本作"金舆""金辂"，皆指华贵车舆，本稿从原文"金举"，在释义中以"华贵车舆"解释。
  - **"枷杽"**：古代刑具，"枷"为颈枷，"杽"为手铐脚镣，合称"枷杽"表示囚禁刑罚。

- 完整对等诠释（secondary_lang_full）：

  This supplementary chapter on "Standards and Measures" (Goulü) establishes a dialectical framework for chart interpretation. The opening principle states that when benefic stars predominate, even encountering malefics produces fortunate outcomes; conversely, when malefics predominate, even benefic presences cannot prevent misfortune. The Life and Body palaces serve as the handles of fortune and disaster, while root factors like Lucun govern the mechanisms of prosperity and poverty.

  The text then presents a dense catalog of pattern formulas: Wealth-and-Seal flanking the Life Palace, Sun-and-Moon flanking Wealth, Tanlang in Zi as "Peach Blossom adrift on water," Ziwei seated in a Treasury palace as "Golden Palanquin bearing the imperial carriage," Taiyin meeting Wenqu in the Spouse palace for "Hanlin elegance," Taiyang meeting Wenchang in Career for "announcing success in the Golden Hall," and Lucun guarding Property-Wealth as "grain piled like gold." Each formula condenses specific stellar combinations into memorable images that practitioners can apply when reading charts.

  The negative counterparts are equally stark: Great Consumption in a defeated palace means begging along the road; Tanlang in a prosperous palace signals lifelong theft; Qisha in extinction ground shortens life like Yan Hui's thirty-two years; dark stars converging on the Appearance or Travel palaces scar the face; Great Consumption meeting Lianzhen in Career brings shackles and imprisonment; Official Talisman meeting punishment stars in Travel means distant exile. Qisha in a fallen palace encountering Flowing Ram guarantees death.

  Finally, the chapter warns about vulnerable limit periods: childhood limits are like bubbles on water, elderly limits like candles in the wind—both easily extinguished when killers appear. Whether one achieves success depends on whether the limit element remains stable; a lifetime of confusion often stems from mixed and contradictory natal-limit configurations. With this, the text declares, the subtleties of Ziwei Doushu become visible.

- 叙事素材（narrative_snippets）：

  - **吉凶辩证**："吉多逢凶也吉，凶多逢吉也凶"，此为本条的核心辩证观——整体配置决定单星的吉凶表现。
  - **身命根源**："身命为祸福之柄，根源为穷通之机"，身命宫与禄存根气是判断一生穷通的两大根本。
  - **格局口诀**："财印夹命、日月夹财、金殿传胪、烂谷堆金"等密集格局口诀，供快速定位命局特征。
  - **凶象警示**："大耗居于落陷，沿门持钵"、"枷杽缠身，大耗廉贞同居官禄"，以极端对比强化吉凶判断。
  - **限运脆弱**："童子限如水上泡沫，老人限似风中燃烛"，再次强调幼年老年限运的脆弱性。
  - **现代应用**：本条提供一套"格局口诀库"，可作为命盘快速扫描的参考工具，但需结合整体配置而非机械套用。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j1_121]` `[trigger: 大耗凶星]` `[factor_trigger: star_dahao]` `[role: 主干]` 大耗为耗损星，主破财消耗，落陷则沿门持钵。 → 《重补斗数彀率》
  - `[ns_zwds_j1_122]` `[trigger: 财印夹命格]` `[factor_trigger: geju_caiyinjiaming]` `[role: 条件分支]` 财星印星夹命宫，主富贵双全。 → 《重补斗数彀率》格局
  - `[ns_zwds_j1_123]` `[trigger: 日月夹财格]` `[factor_trigger: geju_riyuejiacai]` `[role: 条件分支]` 日月夹财帛宫，主财源广进。 → 《重补斗数彀率》格局
  - `[ns_zwds_j1_124]` `[trigger: 金殿传胪格]` `[factor_trigger: geju_jindianchuanlu]` `[role: 条件分支]` 太阳文昌在官禄庙旺，主科甲及第。 → 《重补斗数彀率》"金殿传胪"
  - `[ns_zwds_j1_125]` `[trigger: 烂谷堆金格]` `[factor_trigger: geju_languduijin]` `[role: 条件分支]` 禄存守田宅庙旺，主家财万贯。 → 《重补斗数彀率》"烂谷堆金"
  - `[ns_zwds_j1_126]` `[trigger: 泛水桃花格]` `[factor_trigger: geju_fanshuaitaohua]` `[role: 条件分支]` 贪狼在子宫，主风流多情。 → 《重补斗数彀率》"泛水桃花"
  - `[ns_zwds_j1_127]` `[trigger: 翰林清异格]` `[factor_trigger: geju_hanlinqingyi]` `[role: 条件分支]` 太阴文曲在夫妻宫，主配偶才华出众。 → 《重补斗数彀率》"翰林清异"
  - `[ns_zwds_j1_128]` `[trigger: 富贵层次]` `[factor_trigger: fugui_cengci]` `[role: 结果]` 富贵层次由命盘格局配置决定，分上中下三等。 → 《重补斗数彀率》
  - `[ns_zwds_j1_129]` `[trigger: 成就层次]` `[factor_trigger: chengjiu_cengci]` `[role: 结果]` 成就层次由格局与限运共同决定。 → 《重补斗数彀率》
  - `[ns_zwds_j1_130]` `[trigger: 时间限制]` `[factor_trigger: time_limit]` `[role: 主干]` 时间限制为命运应验的时间范围约束。 → 《重补斗数彀率》限运
  - `[ns_zwds_j1_131]` `[trigger: 限运浮沉]` `[factor_trigger: timing_xianbu_weiji]` `[role: 条件分支]` 限运浮沉为限元不稳定，吉凶起伏大。 → 《重补斗数彀率》"限元最怕浮沉"
  - `[ns_zwds_j1_132]` `[trigger: 命限驳杂]` `[factor_trigger: timing_xianbu_busui]` `[role: 条件分支]` 命限驳杂为本命与限运配置矛盾冲突。 → 《重补斗数彀率》"命限逢乎驳杂"
  - `[ns_zwds_j1_133]` `[trigger: 童子限危]` `[factor_trigger: timing_tongzi_laoren]` `[role: 条件分支]` 童子限弱如水上浮泡，遇凶易应灾祸。 → 《重补斗数彀率》"童子限弱"
  - `[ns_zwds_j1_134]` `[trigger: 吉凶汇合]` `[factor_trigger: state_jixionghuihe]` `[role: 主干]` 吉凶汇合为吉星凶星同宫或对冲的状态。 → 《重补斗数彀率》"吉多逢凶也吉"
  - `[ns_zwds_j1_135]` `[trigger: 入格条件]` `[factor_trigger: state_ruge]` `[role: 主干]` 入格为符合特定格局条件的状态。 → 《重补斗数彀率》格局
  - `[ns_zwds_j1_136]` `[trigger: 入庙条件]` `[factor_trigger: state_rumiao]` `[role: 主干]` 入庙为星曜处于庙旺之地的状态。 → 《重补斗数彀率》
  - `[ns_zwds_j1_137]` `[trigger: 庙陷评估]` `[factor_trigger: state_miaoxian]` `[role: 主干]` 庙陷评估为判断星曜力量强弱的基本方法。 → 《重补斗数彀率》
  - `[ns_zwds_j1_138]` `[trigger: 日夜生原理]` `[factor_trigger: principle_rishengyesheng]` `[role: 主干]` 日夜生原理为昼生宜阳星、夜生宜阴星的配置法则。 → 《重补斗数彀率》"""
    normalized_text_zh: str = """"""
    subject: str = "重补斗数彀率"
    factor_refs: list = ['term_goulu', 'combo_caiyin_jiaming', 'combo_riyue_jiacai', 'combo_fanshui_taohua', 'combo_langu_duijin', 'time_tongzi_laoren']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_重补斗数彀率_001_L1",
    )
    version: str = "1.0.0"
