"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755633
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
    semantic_id="zw_v1.0.0_论人命入格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论人命入格(SemanticEntry):
    """
    - 分字分词释义：

  - **入格**：命局符合经典格局的基本形态。
  - **庙旺聚吉**：星曜入庙旺地且吉星聚集。
  - **科权禄守**：化科、化权、化禄三化星守护命宫。
  - **上...
    """
    
    original_text: str = """- 分字分词释义：

  - **入格**：命局符合经典格局的基本形态。
  - **庙旺聚吉**：星曜入庙旺地且吉星聚集。
  - **科权禄守**：化科、化权、化禄三化星守护命宫。
  - **上上之命**：最高等级的命格。
  - **加吉化吉**：有吉星相助并产生吉利转化。
  - **陷地加杀**：星曜落陷又加凶杀星。
  - **化忌**：四化中的凶星转化。
  - **下格之命**：低等级的命格。
  - **不以入格论**：虽有格局名称但实际不作入格看待。

- 原文（断句）：

  如命入格，庙旺聚吉，科权禄守上上之。命不入庙，加吉化吉科权禄上次之。命不入庙，不加吉，平常命入庙不加吉，中等。若居陷地，又加杀化忌，为下格之命，不以入格而论也。又入格不化吉而化凶，只以本命吉凶多寡而断之。

- 规范化释义（primary_lang_explained）：

  若一命局已经「入格」，又在庙旺之地且吉星聚会，并有科、权、禄三化曜守护，则为上上之格局，是格中之贵者。若命局虽然不在庙旺之地，但后天又有吉星相助、化吉明显，并得科权禄之力，则可列为次一等的好格局。

  若命局不在庙旺之地，且后天不见吉星相助，只是平常的「命入庙」而不加吉者，则只是中等之命；若反而居于陷地，又加诸多杀星并化忌，则为下格之命，此时即使形式上「入格」，也不再以入格而论，而应视作劣等格局来判断。又有一种情形：命局虽名义上入格，但所见化曜不向吉而向凶，则不再执着于「入格」二字，只能根据本命中吉星与凶星多寡、整体吉凶轻重来断其高低。

- 完整对等诠释（secondary_lang_full）：

  This section explains what it truly means for a chart to "enter a pattern".
  When the structure meets the classical conditions, the main stars stand in
  temple dignity, and benefics with Examination, Authority and Salary gather
  around them, the pattern is judged top tier. If the stars are not in full
  dignity but later receive strong support—added benefics, clear auspicious
  transformations and the presence of the three transformations—the fate is
  still lifted well above the ordinary. Charts that merely sit in acceptable
  places without such support are only middle rank, while those that fall into
  debility and are surrounded by killing stars and inauspicious
  transformations must be placed in the lower tier, whatever name they claim.

  The text especially warns against relying on titles alone. A chart may
  technically "enter a pattern" yet direct its key transformations toward harm
  rather than blessing, or contain far more malefics than benefics. In such
  cases one should set aside the honourable label and judge instead by the
  real balance of strength and affliction: how dignified the stars are, how
  many helping or hurting forces they receive, and how much load the structure
  can actually bear. Used in this way, pattern entry becomes a starting gate,
  not a guarantee of nobility.

- 核心要点：

  1. 入格只是起点，必须配合庙旺与吉星聚会，方成上上格局。
  2. 不在庙旺但有加吉、化吉与科权禄者，为次一等好格。
  3. 仅有「入庙」而无加吉者，多只是中等；陷地又加杀化忌，则为下格。
  4. 形式上入格但化凶者，不再以入格论贵贱，只看整体吉凶轻重。
  5. 本条强调：判断格局高低时，优先看庙旺/陷地与吉凶星多寡，而不是被「入格」二字迷惑。

- 叙事素材（narrative_snippets）：

  - **入格分层**："入格加庙旺吉会为上上格，无加吉者中等，陷地加杀为下格"，入格后仍需分层。
  - **庙旺优先**："优先看庙旺陷地与吉凶星多寡"，庙旺状态重于格局名称。
  - **化曜方向**："形式上入格但化凶者，不再以入格论"，化曜方向决定实际吉凶。
  - **现代应用**：本条警示"入格只是门槛"——判断格局需看实质（庙旺+吉星+化曜），而非被名称迷惑。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j5_011]` `[trigger: 入格条件]` `[factor_trigger: state_ruge]` `[role: 主干]` 入格条件为符合经典格局基本形态的状态。 → 《卷五》"入格分层"
  - `[ns_zwds_j5_012]` `[trigger: 上上格局]` `[factor_trigger: level_shangshangge]` `[role: 结果]` 上上格局为入格加庙旺吉会的最高等级。 → 《卷五》"上上格"
  - `[ns_zwds_j5_013]` `[trigger: 中等格局]` `[factor_trigger: level_zhongdengge]` `[role: 结果]` 中等格局为入格无加吉的中间等级。 → 《卷五》"中等"
  - `[ns_zwds_j5_014]` `[trigger: 下格格局]` `[factor_trigger: level_xiage]` `[role: 结果]` 下格格局为陷地加杀的最低等级。 → 《卷五》"下格"
  - `[ns_zwds_j5_015]` `[trigger: 羊陀空劫夹]` `[factor_trigger: malefic_yangtuo_kongjie_jia]` `[role: 条件分支]` 羊陀空劫夹为擎羊陀罗空劫夹命的凶险配置。 → 《卷五》
  - `[ns_zwds_j5_016]` `[trigger: 科权禄拱]` `[factor_trigger: pattern_kequanlu_gong]` `[role: 条件分支]` 科权禄拱为三化星拱照的贵格配置。 → 《卷五》"科权禄"
  - `[ns_zwds_j5_017]` `[trigger: 天罗地网格]` `[factor_trigger: pattern_tianluodiwang]` `[role: 条件分支]` 天罗地网格为辰戌二宫困锁的凶险格局。 → 《卷五》
  - `[ns_zwds_j5_018]` `[trigger: 三台星]` `[factor_trigger: star_santai]` `[role: 主干]` 三台星为辅佐星之一，主贵人提携。 → 《卷五》
  - `[ns_zwds_j5_019]` `[trigger: 生年定位]` `[factor_trigger: principle_shengniandinwei]` `[role: 主干]` 生年定位为根据生年确定星曜的算法原理。 → 《卷五》
  - `[ns_zwds_j5_020]` `[trigger: 生月卯点]` `[factor_trigger: principle_shengyuemaodian]` `[role: 主干]` 生月卯点为根据生月确定星曜的算法原理。 → 《卷五》
  - `[ns_zwds_j5_039]` `[trigger: 申生忌]` `[factor_trigger: taboo_shenshengji]` `[role: 条件分支]` 申生忌为申年生人特定的忌讳。 → 《卷五》
  - `[ns_zwds_j5_040]` `[trigger: 文昌武曲组合]` `[factor_trigger: star_wenchangwuqu]` `[role: 条件分支]` 文昌武曲组合为文昌与武曲同会的配置。 → 《卷五》
  - `[ns_zwds_j5_041]` `[trigger: 天罗格]` `[factor_trigger: pattern_tianluo]` `[role: 条件分支]` 天罗格为辰宫困锁的格局。 → 《卷五》
  - `[ns_zwds_j5_042]` `[trigger: 紫府科权禄格]` `[factor_trigger: pattern_zifukequanlu]` `[role: 条件分支]` 紫府科权禄格为紫微天府遇科权禄的极贵格局。 → 《卷五》
  - `[ns_zwds_j5_043]` `[trigger: 陀罗命格]` `[factor_trigger: star_tuoluoming]` `[role: 条件分支]` 陀罗命格为陀罗入命的配置。 → 《卷五》
  - `[ns_zwds_j5_044]` `[trigger: 权禄格]` `[factor_trigger: pattern_quanlu]` `[role: 条件分支]` 权禄格为化权化禄同会的贵格。 → 《卷五》
  - `[ns_zwds_j5_045]` `[trigger: 正荣结果]` `[factor_trigger: result_zhenggrong]` `[role: 结果]` 正荣结果为正统荣显的判断。 → 《卷五》
  - `[ns_zwds_j5_046]` `[trigger: 小限重逢格]` `[factor_trigger: pattern_xiaoxianchongfeng]` `[role: 条件分支]` 小限重逢格为小限重逢凶星的配置。 → 《卷五》
  - `[ns_zwds_j5_047]` `[trigger: 流羊冲格]` `[factor_trigger: pattern_liuyangchong]` `[role: 条件分支]` 流羊冲格为流年擎羊冲照的配置。 → 《卷五》
  - `[ns_zwds_j5_048]` `[trigger: 权禄天府格]` `[factor_trigger: pattern_quanlutianfu]` `[role: 条件分支]` 权禄天府格为权禄与天府同会的贵格。 → 《卷五》
  - `[ns_zwds_j5_049]` `[trigger: 身临绝地位]` `[factor_trigger: pos_shenlingjuedi]` `[role: 条件分支]` 身临绝地位为身宫落入绝地的配置。 → 《卷五》
  - `[ns_zwds_j5_050]` `[trigger: 气衰结果]` `[factor_trigger: result_qishuai]` `[role: 结果]` 气衰结果为气力衰弱的判断。 → 《卷五》
  - `[ns_zwds_j5_051]` `[trigger: 戌生陀罗忌]` `[factor_trigger: taboo_xushengtuoluo]` `[role: 条件分支]` 戌生陀罗忌为戌年生人遇陀罗的忌讳。 → 《卷五》
  - `[ns_zwds_j5_052]` `[trigger: 破军子午格]` `[factor_trigger: pattern_pojunziwu]` `[role: 条件分支]` 破军子午格为破军在子午宫的格局。 → 《卷五》
  - `[ns_zwds_j5_053]` `[trigger: 小限冲太岁格]` `[factor_trigger: pattern_xiaoxianchongtaisui]` `[role: 条件分支]` 小限冲太岁格为小限冲太岁的凶险配置。 → 《卷五》
  - `[ns_zwds_j5_054]` `[trigger: 富格星曜]` `[factor_trigger: fuge_xingyao]` `[role: 主干]` 富格星曜为富格相关的星曜配置。 → 《卷五》
  - `[ns_zwds_j5_055]` `[trigger: 富贵格局类型]` `[factor_trigger: fugui_geju_type]` `[role: 主干]` 富贵格局类型为富贵格局的分类。 → 《卷五》
  - `[ns_zwds_j5_056]` `[trigger: 富贵来源]` `[factor_trigger: fugui_laiyuan]` `[role: 主干]` 富贵来源为富贵的来源分析。 → 《卷五》
  - `[ns_zwds_j5_057]` `[trigger: 富贵时序]` `[factor_trigger: fugui_shixu]` `[role: 主干]` 富贵时序为富贵的时间顺序。 → 《卷五》
  - `[ns_zwds_j5_058]` `[trigger: 富贵自类型]` `[factor_trigger: fugui_zileixing]` `[role: 主干]` 富贵自类型为自然富贵的类型。 → 《卷五》
  - `[ns_zwds_j5_059]` `[trigger: 夫妻子女]` `[factor_trigger: fuqi_zinu]` `[role: 主干]` 夫妻子女为夫妻子女宫的统称。 → 《卷五》
  - `[ns_zwds_j5_060]` `[trigger: 格局等级]` `[factor_trigger: geju_dengji]` `[role: 主干]` 格局等级为格局的等级分类。 → 《卷五》
  - `[ns_zwds_j5_061]` `[trigger: 格局破格]` `[factor_trigger: geju_poge]` `[role: 条件分支]` 格局破格为格局被破坏的配置。 → 《卷五》
  - `[ns_zwds_j5_062]` `[trigger: 宫刑适配]` `[factor_trigger: gongxing_shipei]` `[role: 主干]` 宫刑适配为宫位与刑克的适配关系。 → 《卷五》
  - `[ns_zwds_j5_063]` `[trigger: 北斗群]` `[factor_trigger: group_beidou]` `[role: 主干]` 北斗群为北斗星群的统称。 → 《卷五》
  - `[ns_zwds_j5_064]` `[trigger: 科权禄群]` `[factor_trigger: group_kequanlu]` `[role: 主干]` 科权禄群为化科化权化禄的组合。 → 《卷五》
  - `[ns_zwds_j5_065]` `[trigger: 流羊群]` `[factor_trigger: group_liuyang]` `[role: 主干]` 流羊群为流年擎羊的配置。 → 《卷五》
  - `[ns_zwds_j5_066]` `[trigger: 流阴群]` `[factor_trigger: group_liuyin]` `[role: 主干]` 流阴群为流年太阴的配置。 → 《卷五》
  - `[ns_zwds_j5_067]` `[trigger: 南斗群]` `[factor_trigger: group_nandou]` `[role: 主干]` 南斗群为南斗星群的统称。 → 《卷五》
  - `[ns_zwds_j5_068]` `[trigger: 寿星群]` `[factor_trigger: group_shouxing]` `[role: 主干]` 寿星群为寿元相关星曜的组合。 → 《卷五》
  - `[ns_zwds_j5_069]` `[trigger: 桃花群]` `[factor_trigger: group_taohua]` `[role: 主干]` 桃花群为桃花相关星曜的组合。 → 《卷五》
  - `[ns_zwds_j5_070]` `[trigger: 文星群]` `[factor_trigger: group_wenxing]` `[role: 主干]` 文星群为文曲文昌等文星的组合。 → 《卷五》
  - `[ns_zwds_j5_071]` `[trigger: 武星群]` `[factor_trigger: group_wuxing]` `[role: 主干]` 武星群为武曲七杀等武星的组合。 → 《卷五》
  - `[ns_zwds_j5_072]` `[trigger: 刑星群]` `[factor_trigger: group_xingxing]` `[role: 主干]` 刑星群为刑克相关星曜的组合。 → 《卷五》
  - `[ns_zwds_j5_073]` `[trigger: 阳星群]` `[factor_trigger: group_yangxing]` `[role: 主干]` 阳星群为阳性星曜的组合。 → 《卷五》
  - `[ns_zwds_j5_074]` `[trigger: 阴星群]` `[factor_trigger: group_yinxing]` `[role: 主干]` 阴星群为阴性星曜的组合。 → 《卷五》
  - `[ns_zwds_j5_075]` `[trigger: 早发晚发]` `[factor_trigger: zaofawanfa]` `[role: 主干]` 早发晚发为发迹时间的判断。 → 《卷五》
  - `[ns_zwds_j5_076]` `[trigger: 贵人体系]` `[factor_trigger: guiren_tixi]` `[role: 主干]` 贵人体系为贵人星曜的体系。 → 《卷五》
  - `[ns_zwds_j5_077]` `[trigger: 官禄体系]` `[factor_trigger: guanlu_tixi]` `[role: 主干]` 官禄体系为官禄相关的体系。 → 《卷五》
  - `[ns_zwds_j5_078]` `[trigger: 阳宫]` `[factor_trigger: palace_yang]` `[role: 主干]` 阳宫为阳性宫位的统称。 → 《卷五》
  - `[ns_zwds_j5_079]` `[trigger: 昌曲辅持格]` `[factor_trigger: pattern_changqu_fuchi]` `[role: 条件分支]` 昌曲辅持格为昌曲辅持的贵格。 → 《卷五》
  - `[ns_zwds_j5_080]` `[trigger: 昌曲加贵格]` `[factor_trigger: pattern_changqu_jiagui]` `[role: 条件分支]` 昌曲加贵格为昌曲加贵的贵格。 → 《卷五》
  - `[ns_zwds_j5_081]` `[trigger: 昌曲魁钺格]` `[factor_trigger: pattern_changqu_kuiyue]` `[role: 条件分支]` 昌曲魁钺格为昌曲与魁钺的贵格。 → 《卷五》
  - `[ns_zwds_j5_082]` `[trigger: 朝斗格]` `[factor_trigger: pattern_chaodou]` `[role: 条件分支]` 朝斗格为朝斗的贵格。 → 《卷五》
  - `[ns_zwds_j5_083]` `[trigger: 朝堂科权禄格]` `[factor_trigger: pattern_chaotang_kequanlu]` `[role: 条件分支]` 朝堂科权禄格为朝堂遇科权禄的贵格。 → 《卷五》
  - `[ns_zwds_j5_084]` `[trigger: 倒限格]` `[factor_trigger: pattern_daoxian]` `[role: 条件分支]` 倒限格为限运倒行的配置。 → 《卷五》
  - `[ns_zwds_j5_085]` `[trigger: 辅弼缠榜格]` `[factor_trigger: pattern_fubi_chanbang]` `[role: 条件分支]` 辅弼缠榜格为辅弼缠榜的贵格。 → 《卷五》
  - `[ns_zwds_j5_086]` `[trigger: 辅弼加会格]` `[factor_trigger: pattern_fubi_jiahui]` `[role: 条件分支]` 辅弼加会格为辅弼加会的贵格。 → 《卷五》
  - `[ns_zwds_j5_087]` `[trigger: 辅弼陶朱格]` `[factor_trigger: pattern_fubitaozhu]` `[role: 条件分支]` 辅弼陶朱格为辅弼陶朱的富格。 → 《卷五》
  - `[ns_zwds_j5_088]` `[trigger: 机巨卯格]` `[factor_trigger: pattern_ji_ju_mao]` `[role: 条件分支]` 机巨卯格为天机巨门在卯的格局。 → 《卷五》
  - `[ns_zwds_j5_089]` `[trigger: 机巨酉格]` `[factor_trigger: pattern_ji_ju_you]` `[role: 条件分支]` 机巨酉格为天机巨门在酉的格局。 → 《卷五》
  - `[ns_zwds_j5_090]` `[trigger: 加限格]` `[factor_trigger: pattern_jiaxian]` `[role: 条件分支]` 加限格为加限的配置。 → 《卷五》
  - `[ns_zwds_j5_091]` `[trigger: 金星四财库格]` `[factor_trigger: pattern_jinxing_sicaiku]` `[role: 条件分支]` 金星四财库格为金星与四财库的格局。 → 《卷五》
  - `[ns_zwds_j5_092]` `[trigger: 金星旺地格]` `[factor_trigger: pattern_jinxing_wangdi]` `[role: 条件分支]` 金星旺地格为金星在旺地的格局。 → 《卷五》
  - `[ns_zwds_j5_093]` `[trigger: 巨机酉化忌格]` `[factor_trigger: pattern_juji_you_huaji]` `[role: 条件分支]` 巨机酉化忌格为巨机在酉化忌的格局。 → 《卷五》
  - `[ns_zwds_j5_094]` `[trigger: 巨日共明格]` `[factor_trigger: pattern_juri_gongming]` `[role: 条件分支]` 巨日共明格为巨门太阳共明的贵格。 → 《卷五》
  - `[ns_zwds_j5_095]` `[trigger: 巨日同宫格2]` `[factor_trigger: pattern_juri_tonggong]` `[role: 条件分支]` 巨日同宫格为巨门太阳同宫的格局。 → 《卷五》
  - `[ns_zwds_j5_096]` `[trigger: 科禄拱照格]` `[factor_trigger: pattern_kelu_gongzhao]` `[role: 条件分支]` 科禄拱照格为科禄拱照的贵格。 → 《卷五》
  - `[ns_zwds_j5_097]` `[trigger: 科禄天阳天梁格]` `[factor_trigger: pattern_kelutianyangtianliang]` `[role: 条件分支]` 科禄天阳天梁格为科禄与日梁的贵格。 → 《卷五》
  - `[ns_zwds_j5_098]` `[trigger: 科权加宫格]` `[factor_trigger: pattern_keqian_jiagong]` `[role: 条件分支]` 科权加宫格为科权加宫的贵格。 → 《卷五》
  - `[ns_zwds_j5_099]` `[trigger: 科权共明格]` `[factor_trigger: pattern_kequan_gongming]` `[role: 条件分支]` 科权共明格为科权共明的贵格。 → 《卷五》
  - `[ns_zwds_j5_100]` `[trigger: 科权守照格]` `[factor_trigger: pattern_kequan_shouzhao]` `[role: 条件分支]` 科权守照格为科权守照的贵格。 → 《卷五》
  - `[ns_zwds_j5_101]` `[trigger: 科权左右格]` `[factor_trigger: pattern_kequan_zuoyou]` `[role: 条件分支]` 科权左右格为科权与左右的贵格。 → 《卷五》
  - `[ns_zwds_j5_102]` `[trigger: 科权禄会合格]` `[factor_trigger: pattern_kequanlu_huihe]` `[role: 条件分支]` 科权禄会合格为科权禄三化会合的极贵格局。 → 《卷五》
  - `[ns_zwds_j5_103]` `[trigger: 科甲知事品质]` `[factor_trigger: quality_kejia_zhishi]` `[role: 结果]` 科甲知事品质为科举知事的品质判断。 → 《卷五》
  - `[ns_zwds_j5_104]` `[trigger: 命不助财品质]` `[factor_trigger: quality_ming_buzhucai]` `[role: 结果]` 命不助财品质为命格不助财的品质判断。 → 《卷五》
  - `[ns_zwds_j5_105]` `[trigger: 配三夫品质]` `[factor_trigger: quality_pei_sanfu]` `[role: 结果]` 配三夫品质为女命配三夫的品质判断。 → 《卷五》
  - `[ns_zwds_j5_106]` `[trigger: 若非大贵品质]` `[factor_trigger: quality_ruofei_dagui]` `[role: 结果]` 若非大贵品质为若非大贵的品质判断。 → 《卷五》
  - `[ns_zwds_j5_107]` `[trigger: 三方合一品质]` `[factor_trigger: quality_sanfang_heyi]` `[role: 结果]` 三方合一品质为三方合一的品质判断。 → 《卷五》
  - `[ns_zwds_j5_108]` `[trigger: 收入不如人品质]` `[factor_trigger: quality_shouru_buru_ren]` `[role: 结果]` 收入不如人品质为收入不如人的品质判断。 → 《卷五》
  - `[ns_zwds_j5_109]` `[trigger: 数目品质]` `[factor_trigger: quality_shumu]` `[role: 结果]` 数目品质为数目的品质判断。 → 《卷五》
  - `[ns_zwds_j5_110]` `[trigger: 天魁无用品质]` `[factor_trigger: quality_tiankui_wuyong]` `[role: 结果]` 天魁无用品质为天魁无用的品质判断。 → 《卷五》
  - `[ns_zwds_j5_111]` `[trigger: 威武志志品质]` `[factor_trigger: quality_weiwu_zhizhi]` `[role: 结果]` 威武志志品质为威武志志的品质判断。 → 《卷五》
  - `[ns_zwds_j5_112]` `[trigger: 为阳奸臣品质]` `[factor_trigger: quality_weiyang_jianchen]` `[role: 结果]` 为阳奸臣品质为奸臣的品质判断。 → 《卷五》
  - `[ns_zwds_j5_113]` `[trigger: 无正曜品质]` `[factor_trigger: quality_wu_zhengyao]` `[role: 结果]` 无正曜品质为无正曜的品质判断。 → 《卷五》
  - `[ns_zwds_j5_114]` `[trigger: 无正曜品质2]` `[factor_trigger: quality_wuzheng_yao]` `[role: 结果]` 无正曜品质为命宫无正曜的品质判断。 → 《卷五》
  - `[ns_zwds_j5_115]` `[trigger: 刑暴品质]` `[factor_trigger: quality_xingbao]` `[role: 结果]` 刑暴品质为刑暴的品质判断。 → 《卷五》
  - `[ns_zwds_j5_116]` `[trigger: 眼权制命品质]` `[factor_trigger: quality_yanquan_zhiming]` `[role: 结果]` 眼权制命品质为眼权制命的品质判断。 → 《卷五》
  - `[ns_zwds_j5_117]` `[trigger: 援贤品质]` `[factor_trigger: quality_yuanxian]` `[role: 结果]` 援贤品质为援贤的品质判断。 → 《卷五》
  - `[ns_zwds_j5_118]` `[trigger: 终不美品质]` `[factor_trigger: quality_zhong_bumei]` `[role: 结果]` 终不美品质为终不美的品质判断。 → 《卷五》
  - `[ns_zwds_j5_119]` `[trigger: 主持弱权品质]` `[factor_trigger: quality_zhuchi_ruoquan]` `[role: 结果]` 主持弱权品质为主持弱权的品质判断。 → 《卷五》
  - `[ns_zwds_j5_120]` `[trigger: 会合冲关系]` `[factor_trigger: relation_huihechong]` `[role: 主干]` 会合冲关系为会合与冲的关系。 → 《卷五》
  - `[ns_zwds_j5_121]` `[trigger: 三方对照关系]` `[factor_trigger: relation_sanfangduizhao]` `[role: 主干]` 三方对照关系为三方对照的关系。 → 《卷五》
  - `[ns_zwds_j5_122]` `[trigger: 人生路径]` `[factor_trigger: rensheng_lujing]` `[role: 主干]` 人生路径为人生的路径分析。 → 《卷五》
  - `[ns_zwds_j5_123]` `[trigger: 安定结果]` `[factor_trigger: result_anding]` `[role: 结果]` 安定结果为安定的判断。 → 《卷五》
  - `[ns_zwds_j5_124]` `[trigger: 不得联登结果]` `[factor_trigger: result_bude_liandeng]` `[role: 结果]` 不得联登结果为不得联登的判断。 → 《卷五》
  - `[ns_zwds_j5_125]` `[trigger: 不防结果]` `[factor_trigger: result_bufang]` `[role: 结果]` 不防结果为不防的判断。 → 《卷五》
  - `[ns_zwds_j5_126]` `[trigger: 不美结果]` `[factor_trigger: result_bumei]` `[role: 结果]` 不美结果为不美的判断。 → 《卷五》
  - `[ns_zwds_j5_127]` `[trigger: 不免远结果]` `[factor_trigger: result_bumianyuan]` `[role: 结果]` 不免远结果为不免远的判断。 → 《卷五》
  - `[ns_zwds_j5_128]` `[trigger: 十六岁时机]` `[factor_trigger: timing_shiliusui]` `[role: 主干]` 十六岁时机为十六岁的时机。 → 《卷五》
  - `[ns_zwds_j5_129]` `[trigger: 太岁辰马时机]` `[factor_trigger: timing_taisui_chenma]` `[role: 主干]` 太岁辰马时机为太岁辰马的时机。 → 《卷五》
  - `[ns_zwds_j5_130]` `[trigger: 太岁大限戌时机]` `[factor_trigger: timing_taisui_daxian_xu]` `[role: 主干]` 太岁大限戌时机为太岁大限戌的时机。 → 《卷五》
  - `[ns_zwds_j5_131]` `[trigger: 太岁地劫时机]` `[factor_trigger: timing_taisui_dijie]` `[role: 主干]` 太岁地劫时机为太岁地劫的时机。 → 《卷五》
  - `[ns_zwds_j5_132]` `[trigger: 太岁犯人相时机]` `[factor_trigger: timing_taisui_fanrenxiang]` `[role: 主干]` 太岁犯人相时机为太岁犯人相的时机。 → 《卷五》
  - `[ns_zwds_j5_133]` `[trigger: 太岁逢忌时机]` `[factor_trigger: timing_taisui_fengji]` `[role: 主干]` 太岁逢忌时机为太岁逢忌的时机。 → 《卷五》
  - `[ns_zwds_j5_134]` `[trigger: 太岁逢劫时机]` `[factor_trigger: timing_taisui_fengjie]` `[role: 主干]` 太岁逢劫时机为太岁逢劫的时机。 → 《卷五》
  - `[ns_zwds_j5_135]` `[trigger: 太岁逢铃时机]` `[factor_trigger: timing_taisui_fengling]` `[role: 主干]` 太岁逢铃时机为太岁逢铃的时机。 → 《卷五》
  - `[ns_zwds_j5_136]` `[trigger: 太岁买涉时机]` `[factor_trigger: timing_taisui_maishe]` `[role: 主干]` 太岁买涉时机为太岁买涉的时机。 → 《卷五》
  - `[ns_zwds_j5_137]` `[trigger: 太岁命垣时机]` `[factor_trigger: timing_taisui_mingyuan]` `[role: 主干]` 太岁命垣时机为太岁命垣的时机。 → 《卷五》
  - `[ns_zwds_j5_138]` `[trigger: 太岁天罗时机]` `[factor_trigger: timing_taisui_tianluo]` `[role: 主干]` 太岁天罗时机为太岁天罗的时机。 → 《卷五》
  - `[ns_zwds_j5_139]` `[trigger: 太岁陀害时机]` `[factor_trigger: timing_taisui_tuohai]` `[role: 主干]` 太岁陀害时机为太岁陀害的时机。 → 《卷五》
  - `[ns_zwds_j5_140]` `[trigger: 太岁刑忌时机]` `[factor_trigger: timing_taisui_xingji]` `[role: 主干]` 太岁刑忌时机为太岁刑忌的时机。 → 《卷五》
  - `[ns_zwds_j5_141]` `[trigger: 太岁寅时机]` `[factor_trigger: timing_taisui_yin]` `[role: 主干]` 太岁寅时机为太岁寅的时机。 → 《卷五》
  - `[ns_zwds_j5_142]` `[trigger: 太岁酉时机]` `[factor_trigger: timing_taisui_you]` `[role: 主干]` 太岁酉时机为太岁酉的时机。 → 《卷五》
  - `[ns_zwds_j5_143]` `[trigger: 太岁有忌时机]` `[factor_trigger: timing_taisui_youji]` `[role: 主干]` 太岁有忌时机为太岁有忌的时机。 → 《卷五》
  - `[ns_zwds_j5_144]` `[trigger: 天使地时机]` `[factor_trigger: timing_tianshi_di]` `[role: 主干]` 天使地时机为天使地的时机。 → 《卷五》
  - `[ns_zwds_j5_145]` `[trigger: 同廉害时机]` `[factor_trigger: timing_tonglian_hai]` `[role: 主干]` 同廉害时机为同廉害的时机。 → 《卷五》
  - `[ns_zwds_j5_146]` `[trigger: 五十四立达时机]` `[factor_trigger: timing_wushisi_lida]` `[role: 主干]` 五十四立达时机为五十四立达的时机。 → 《卷五》
  - `[ns_zwds_j5_147]` `[trigger: 限绝地时机]` `[factor_trigger: timing_xian_juedi]` `[role: 主干]` 限绝地时机为限绝地的时机。 → 《卷五》
  - `[ns_zwds_j5_148]` `[trigger: 限不补岁时机]` `[factor_trigger: timing_xianbu_busui]` `[role: 主干]` 限不补岁时机为限不补岁的时机。 → 《卷五》
  - `[ns_zwds_j5_149]` `[trigger: 限不为忌时机]` `[factor_trigger: timing_xianbu_weiji]` `[role: 主干]` 限不为忌时机为限不为忌的时机。 → 《卷五》
  - `[ns_zwds_j5_150]` `[trigger: 限年岁陷地时机]` `[factor_trigger: timing_xiannsui_xiandi]` `[role: 主干]` 限年岁陷地时机为限年岁陷地的时机。 → 《卷五》
  - `[ns_zwds_j5_151]` `[trigger: 小限43时机]` `[factor_trigger: timing_xiaoxian_43]` `[role: 主干]` 小限43时机为小限43的时机。 → 《卷五》
  - `[ns_zwds_j5_152]` `[trigger: 小限败地时机]` `[factor_trigger: timing_xiaoxian_baidi]` `[role: 主干]` 小限败地时机为小限败地的时机。 → 《卷五》"""
    normalized_text_zh: str = """"""
    subject: str = "论人命入格"
    factor_refs: list = ['state_ruge', 'state_miaowang', 'group_kequanlu', 'transform_jixiong', 'level_geju', 'source_ref', 'rel_ruge_001', 'state_ruge', 'rel_ruge_002', 'state_miaowang', 'rel_ruge_003', 'group_kequanlu', 'evi_ruge_001', 'state_ruge', 'rule_ruge_shangshang', 'evi_ruge_002', 'level_geju', 'rule_ruge_xiage', 'concept_pattern', 'concept_tier']
    
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
        l1_anchor="zw_v1.0.0_论人命入格_001_L1",
    )
    version: str = "1.0.0"
