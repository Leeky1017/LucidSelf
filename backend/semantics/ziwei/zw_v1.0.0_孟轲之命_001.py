"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699000
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
    semantic_id="zw_v1.0.0_孟轲之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 孟轲之命(SemanticEntry):
    """
    - 分字分词释义：

  - **双禄拱照**：禄存与化禄同时拱照命宫，为极贵财禄格局。
  - **昌曲重逢**：文昌文曲同时会合命宫，主文才文名。
  - **戌有机梁**：戌宫有天机天梁同宫，主...
    """
    
    original_text: str = """- 分字分词释义：

  - **双禄拱照**：禄存与化禄同时拱照命宫，为极贵财禄格局。
  - **昌曲重逢**：文昌文曲同时会合命宫，主文才文名。
  - **戌有机梁**：戌宫有天机天梁同宫，主文章冠世。
  - **文曲单坐身命**：文曲独坐身命两宫，主口才便给、善于辩论。
  - **地网逢铃**：大限入地网宫又遇铃星，为凶险之限。
  - **天罗地网**：小限入天罗、太岁行绝地，诸凶齐聚。
  - **阳男金四局**：紫微斗数命盘的五行局数，金四局主刚断决绝。

- **原文（source_text）**：  
  孟轲之命。阳男金四局。双禄拱照，昌曲重逢，戌有机梁，文章冠世。文曲单坐身命，主人口能舌辨。大限地网逢铃，小限天罗，太岁又在绝地，故凶。

- **规范化释义（primary_lang_explained）**：  
  孟子命属阳男金四局，命宫受双禄拱照，昌曲重逢于命，戌宫有天机、天梁同宫，主文章冠世。文曲单坐身命，主口才便给、善于辩论。晚年大限入地网逢铃星，小限入天罗，太岁又行绝地，诸凶齐聚，遂于此限殁。此例说明：文名极盛之命，亦难逃晚年凶限。

- **完整对等诠释（secondary_lang_full）**：  
  Mencius's chart is that of a Yang male of Metal Fourth Configuration. Double Salary stars flank the Life palace; Chang and Qu meet repeatedly; the Xu palace hosts Tianji and Tianliang together, indicating literary fame that crowns the era. Wenqu alone occupies the Body and Life palaces, granting superb eloquence and debating skill. In later years, the major period enters the Net of Earth and encounters the Bell star; the minor period falls into the Net of Heaven; Tai Sui also travels through the Extinction position. With all malefics converging, the Sage passed away during this period. This case demonstrates that even the most illustrious literary destiny cannot escape a perilous late‑life configuration.

- **核心要点**：  
  1. 双禄拱照、昌曲重逢，主文名极盛。  
  2. 文曲单坐身命，主口才辩论之能。  
  3. 地网逢铃、天罗、绝地叠加，为晚年寿终之应期。

- **叙事素材（narrative_snippets）**：
  - **文名极盛**："双禄拱照，昌曲重逢，戌有机梁，文章冠世"，孟子命主文名冠世。
  - **口才辩论**："文曲单坐身命，主人口能舌辨"，文曲坐命主善辩。
  - **晚年凶限**："大限地网逢铃，小限天罗，太岁绝地"，诸凶叠加致晚年殁。
  - **现代应用**：文才极盛之命仍需关注晚年限运——地网天罗绝地为高危组合。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j6_020]` `[trigger: 双禄拱照]` `[factor_trigger: star_lucun AND hua_lu AND gongzhao]` `[role: 条件分支]` 双禄拱照为禄存与化禄同时拱照命宫的极贵配置。 → 《卷六》孟轲命
  - `[ns_zwds_j6_021]` `[trigger: 昌曲重逢]` `[factor_trigger: star_wenchang AND star_wenqu AND chongfeng]` `[role: 条件分支]` 昌曲重逢为文昌文曲同时会合命宫的配置。 → 《卷六》"昌曲重逢"
  - `[ns_zwds_j6_022]` `[trigger: 机梁同宫]` `[factor_trigger: star_tianji AND star_tianliang AND tonggong]` `[role: 条件分支]` 机梁同宫为天机天梁同守一宫的配置。 → 《卷六》"戌有机梁"
  - `[ns_zwds_j6_023]` `[trigger: 文章冠世]` `[factor_trigger: result_wenzhang_guanshi]` `[role: 结果]` 文章冠世为文才文名极盛的贵格结果。 → 《卷六》"文章冠世"
  - `[ns_zwds_j6_024]` `[trigger: 口才辩论]` `[factor_trigger: trait_koucai_bianlun]` `[role: 结果]` 口才辩论为文曲坐命主善辩的特质。 → 《卷六》"口能舌辨"
  - `[ns_zwds_j6_025]` `[trigger: 地网逢铃]` `[factor_trigger: pattern_diwang AND star_lingxing]` `[role: 条件分支]` 地网逢铃为大限入地网又遇铃星的凶险配置。 → 《卷六》"地网逢铃"
  - `[ns_zwds_j6_026]` `[trigger: 太岁绝地]` `[factor_trigger: taisui AND position_juedi]` `[role: 条件分支]` 太岁绝地为流年太岁行绝地的凶险配置。 → 《卷六》"太岁又在绝地"
  - `[ns_zwds_j6_027]` `[trigger: 双禄朝垣格]` `[factor_trigger: pattern_shuangluchaoyuan]` `[role: 条件分支]` 双禄朝垣格为禄存化禄朝拱命宫的极贵格局。 → 《卷六》
  - `[ns_zwds_j6_028]` `[trigger: 善谈兵结果]` `[factor_trigger: result_shantanbing]` `[role: 结果]` 善谈兵结果为善于谋略用兵的判断。 → 《卷六》
  - `[ns_zwds_j6_029]` `[trigger: 大岁埋社格]` `[factor_trigger: pattern_dasuimaishe]` `[role: 条件分支]` 大岁埋社格为太岁埋没的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_030]` `[trigger: 太阴化忌四化]` `[factor_trigger: sihua_taiyinji]` `[role: 条件分支]` 太阴化忌四化为太阴化忌的配置。 → 《卷六》
  - `[ns_zwds_j6_031]` `[trigger: 权禄禄存格]` `[factor_trigger: pattern_quanlu_lucun]` `[role: 条件分支]` 权禄禄存格为权禄与禄存同会的贵格。 → 《卷六》
  - `[ns_zwds_j6_032]` `[trigger: 机储藏凶格]` `[factor_trigger: pattern_jichucangxiong]` `[role: 条件分支]` 机储藏凶格为天机隐藏凶险的配置。 → 《卷六》
  - `[ns_zwds_j6_033]` `[trigger: 大小限冲格]` `[factor_trigger: pattern_daxiaoxianchong]` `[role: 条件分支]` 大小限冲格为大限小限互冲的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_034]` `[trigger: 武将结果]` `[factor_trigger: result_wujiang]` `[role: 结果]` 武将结果为武职将领的贵格判断。 → 《卷六》
  - `[ns_zwds_j6_035]` `[trigger: 双禄紫府格]` `[factor_trigger: pattern_shuangluzifu]` `[role: 条件分支]` 双禄紫府格为双禄与紫府同会的极贵格局。 → 《卷六》
  - `[ns_zwds_j6_036]` `[trigger: 限老绝地格]` `[factor_trigger: pattern_xianlaojiadi]` `[role: 条件分支]` 限老绝地格为老年限入绝地的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_037]` `[trigger: 衰死位]` `[factor_trigger: pos_shuaisi]` `[role: 主干]` 衰死位为十二长生衰死之地。 → 《卷六》
  - `[ns_zwds_j6_038]` `[trigger: 紫府科权格]` `[factor_trigger: pattern_zifukequan]` `[role: 条件分支]` 紫府科权格为紫府遇科权的贵格。 → 《卷六》
  - `[ns_zwds_j6_039]` `[trigger: 出将入相结果]` `[factor_trigger: result_chujiangruxiang]` `[role: 结果]` 出将入相结果为文武极贵的判断。 → 《卷六》
  - `[ns_zwds_j6_040]` `[trigger: 空劫伤忌格]` `[factor_trigger: pattern_kongjieshangi]` `[role: 条件分支]` 空劫伤忌格为空劫与伤忌同会的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_041]` `[trigger: 羊陀冲照格]` `[factor_trigger: pattern_yangtuochongzhao]` `[role: 条件分支]` 羊陀冲照格为擎羊陀罗冲照的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_042]` `[trigger: 毒死结果]` `[factor_trigger: result_dusi]` `[role: 结果]` 毒死结果为中毒身亡的凶险判断。 → 《卷六》
  - `[ns_zwds_j6_043]` `[trigger: 禄合左右格]` `[factor_trigger: pattern_luhezuoyou]` `[role: 条件分支]` 禄合左右格为禄星与左右同会的贵格。 → 《卷六》
  - `[ns_zwds_j6_044]` `[trigger: 紫破辰戌格2]` `[factor_trigger: pattern_zipochenxu]` `[role: 条件分支]` 紫破辰戌格为紫微破军在辰戌的格局。 → 《卷六》
  - `[ns_zwds_j6_045]` `[trigger: 左右权禄格]` `[factor_trigger: pattern_zuoyouquanlu]` `[role: 条件分支]` 左右权禄格为左右与权禄同会的贵格。 → 《卷六》
  - `[ns_zwds_j6_046]` `[trigger: 丧门白虎组合]` `[factor_trigger: star_sangmenbaihu]` `[role: 条件分支]` 丧门白虎组合为丧门白虎的凶险组合。 → 《卷六》
  - `[ns_zwds_j6_047]` `[trigger: 紫微午格]` `[factor_trigger: pattern_ziweiwu]` `[role: 条件分支]` 紫微午格为紫微在午宫的格局。 → 《卷六》
  - `[ns_zwds_j6_048]` `[trigger: 天伤夹格]` `[factor_trigger: pattern_tianshangjia]` `[role: 条件分支]` 天伤夹格为天伤夹命的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_049]` `[trigger: 血光结果]` `[factor_trigger: result_xueguang]` `[role: 结果]` 血光结果为血光之灾的凶险判断。 → 《卷六》
  - `[ns_zwds_j6_050]` `[trigger: 科权加贵格]` `[factor_trigger: pattern_kequanjiagui]` `[role: 条件分支]` 科权加贵格为科权与贵星同会的贵格。 → 《卷六》
  - `[ns_zwds_j6_051]` `[trigger: 美命结果]` `[factor_trigger: result_meiming]` `[role: 结果]` 美命结果为命格美好的吉利判断。 → 《卷六》
  - `[ns_zwds_j6_052]` `[trigger: 丧门白虎冲凶]` `[factor_trigger: malefic_sangmen_baihu_chong]` `[role: 条件分支]` 丧门白虎冲凶为丧门白虎冲照的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_053]` `[trigger: 丧门吊客凶]` `[factor_trigger: malefic_sangmen_diaoke]` `[role: 条件分支]` 丧门吊客凶为丧门吊客的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_054]` `[trigger: 三煞照命凶]` `[factor_trigger: malefic_sansha_zhaoming]` `[role: 条件分支]` 三煞照命凶为三煞照命的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_055]` `[trigger: 四煞凶格]` `[factor_trigger: malefic_sisha]` `[role: 条件分支]` 四煞凶格为四煞的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_056]` `[trigger: 太岁冲凶]` `[factor_trigger: malefic_taisui_chong]` `[role: 条件分支]` 太岁冲凶为太岁冲照的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_057]` `[trigger: 太岁地劫凶]` `[factor_trigger: malefic_taisui_dijie]` `[role: 条件分支]` 太岁地劫凶为太岁与地劫的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_058]` `[trigger: 贪狼化忌凶]` `[factor_trigger: malefic_tanlang_huaji]` `[role: 条件分支]` 贪狼化忌凶为贪狼化忌的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_059]` `[trigger: 贪狼阳刃凶]` `[factor_trigger: malefic_tanlang_yangren]` `[role: 条件分支]` 贪狼阳刃凶为贪狼与阳刃的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_060]` `[trigger: 贪廉凶格]` `[factor_trigger: malefic_tanlian]` `[role: 条件分支]` 贪廉凶格为贪狼廉贞的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_061]` `[trigger: 贪廉俱陷凶]` `[factor_trigger: malefic_tanlian_juxian]` `[role: 条件分支]` 贪廉俱陷凶为贪廉俱陷的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_062]` `[trigger: 天空败绝凶]` `[factor_trigger: malefic_tiankong_baijue]` `[role: 条件分支]` 天空败绝凶为天空败绝的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_063]` `[trigger: 天空地劫凶]` `[factor_trigger: malefic_tiankong_dijie]` `[role: 条件分支]` 天空地劫凶为天空地劫的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_064]` `[trigger: 天空擎羊凶]` `[factor_trigger: malefic_tiankong_qingyang]` `[role: 条件分支]` 天空擎羊凶为天空与擎羊的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_065]` `[trigger: 天哭地劫凶]` `[factor_trigger: malefic_tianku_dijie]` `[role: 条件分支]` 天哭地劫凶为天哭与地劫的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_066]` `[trigger: 天哭煞临凶]` `[factor_trigger: malefic_tianku_shalin]` `[role: 条件分支]` 天哭煞临凶为天哭与煞星临的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_067]` `[trigger: 天罗擎羊凶]` `[factor_trigger: malefic_tianluo_qingyang]` `[role: 条件分支]` 天罗擎羊凶为天罗与擎羊的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_068]` `[trigger: 天罗地网凶]` `[factor_trigger: malefic_tianluodiwang]` `[role: 条件分支]` 天罗地网凶为天罗地网的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_069]` `[trigger: 天伤凶格]` `[factor_trigger: malefic_tianshang]` `[role: 条件分支]` 天伤凶格为天伤的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_070]` `[trigger: 天伤劫凶凶]` `[factor_trigger: malefic_tianshang_jiexiong]` `[role: 条件分支]` 天伤劫凶凶为天伤与劫凶的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_071]` `[trigger: 天伤天刑凶]` `[factor_trigger: malefic_tianshang_tianxing]` `[role: 条件分支]` 天伤天刑凶为天伤与天刑的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_072]` `[trigger: 天使加耗凶]` `[factor_trigger: malefic_tianshi_jiahao]` `[role: 条件分支]` 天使加耗凶为天使加耗的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_073]` `[trigger: 天刑地劫凶]` `[factor_trigger: malefic_tianxing_dijie]` `[role: 条件分支]` 天刑地劫凶为天刑与地劫的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_074]` `[trigger: 陀罗凶格]` `[factor_trigger: malefic_tuoluo]` `[role: 条件分支]` 陀罗凶格为陀罗的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_075]` `[trigger: 陀罗大限凶]` `[factor_trigger: malefic_tuoluo_daxian]` `[role: 条件分支]` 陀罗大限凶为陀罗在大限的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_076]` `[trigger: 陀罗夹地凶]` `[factor_trigger: malefic_tuoluo_jiadi]` `[role: 条件分支]` 陀罗夹地凶为陀罗夹地的凶险配置。 → 《卷六》
  - `[ns_zwds_j6_077]` `[trigger: 左右朝垣格]` `[factor_trigger: pattern_zuoyou_chaoyuan]` `[role: 条件分支]` 左右朝垣格为左右朝垣的贵格。 → 《卷六》
  - `[ns_zwds_j6_078]` `[trigger: 左右加贵格]` `[factor_trigger: pattern_zuoyou_jiagui]` `[role: 条件分支]` 左右加贵格为左右加贵的贵格。 → 《卷六》
  - `[ns_zwds_j6_079]` `[trigger: 左右加聚格]` `[factor_trigger: pattern_zuoyou_jiaju]` `[role: 条件分支]` 左右加聚格为左右加聚的贵格。 → 《卷六》
  - `[ns_zwds_j6_080]` `[trigger: 左右魁钺守照格]` `[factor_trigger: pattern_zuoyou_kuiyue_shouzhao]` `[role: 条件分支]` 左右魁钺守照格为左右魁钺守照的贵格。 → 《卷六》
  - `[ns_zwds_j6_081]` `[trigger: 心限卦象位]` `[factor_trigger: pos_xinxianguaxiang]` `[role: 主干]` 心限卦象位为心限的卦象位置。 → 《卷六》
  - `[ns_zwds_j6_082]` `[trigger: 酉丑位]` `[factor_trigger: pos_youchou]` `[role: 主干]` 酉丑位为酉丑的宫位。 → 《卷六》
  - `[ns_zwds_j6_083]` `[trigger: 不必合格原则]` `[factor_trigger: principle_bubi_hege]` `[role: 主干]` 不必合格原则为不必拘泥于合格的原则。 → 《卷六》
  - `[ns_zwds_j6_084]` `[trigger: 日生夜生原则]` `[factor_trigger: principle_rishengyesheng]` `[role: 主干]` 日生夜生原则为日生夜生的判断原则。 → 《卷六》
  - `[ns_zwds_j6_085]` `[trigger: 同格异人原则]` `[factor_trigger: principle_tongge_yiren]` `[role: 主干]` 同格异人原则为同格不同人的原则。 → 《卷六》
  - `[ns_zwds_j6_086]` `[trigger: 阴人二论原则]` `[factor_trigger: principle_yinren_erlun]` `[role: 主干]` 阴人二论原则为阴人二论的原则。 → 《卷六》
  - `[ns_zwds_j6_087]` `[trigger: 亲缘损害]` `[factor_trigger: qinyuan_sunhai]` `[role: 结果]` 亲缘损害为亲缘关系损害的结果。 → 《卷六》
  - `[ns_zwds_j6_088]` `[trigger: 本宫异阳品质]` `[factor_trigger: quality_bengong_yiyang]` `[role: 结果]` 本宫异阳品质为本宫异阳的品质判断。 → 《卷六》
  - `[ns_zwds_j6_089]` `[trigger: 薄命品质]` `[factor_trigger: quality_boming]` `[role: 结果]` 薄命品质为薄命的品质判断。 → 《卷六》
  - `[ns_zwds_j6_090]` `[trigger: 不免劳力品质]` `[factor_trigger: quality_bumian_laoli]` `[role: 结果]` 不免劳力品质为不免劳力的品质判断。 → 《卷六》
  - `[ns_zwds_j6_091]` `[trigger: 不中俗人品质]` `[factor_trigger: quality_buzhong_suren]` `[role: 结果]` 不中俗人品质为不中俗人的品质判断。 → 《卷六》
  - `[ns_zwds_j6_092]` `[trigger: 才华众显品质]` `[factor_trigger: quality_caihua_zhongxian]` `[role: 结果]` 才华众显品质为才华众显的品质判断。 → 《卷六》
  - `[ns_zwds_j6_093]` `[trigger: 蟾宫折桂品质]` `[factor_trigger: quality_changong_zhegui]` `[role: 结果]` 蟾宫折桂品质为科举及第的品质判断。 → 《卷六》
  - `[ns_zwds_j6_094]` `[trigger: 得贵人宠爱品质]` `[factor_trigger: quality_de_guiren_chongai]` `[role: 结果]` 得贵人宠爱品质为得贵人宠爱的品质判断。 → 《卷六》
  - `[ns_zwds_j6_095]` `[trigger: 帝胄之命品质]` `[factor_trigger: quality_dizhou_zhi_ming]` `[role: 结果]` 帝胄之命品质为帝王后裔的品质判断。 → 《卷六》
  - `[ns_zwds_j6_096]` `[trigger: 富贵福寿品质]` `[factor_trigger: quality_fugui_fushou]` `[role: 结果]` 富贵福寿品质为富贵福寿的品质判断。 → 《卷六》
  - `[ns_zwds_j6_097]` `[trigger: 富贵双全品质]` `[factor_trigger: quality_fugui_shuangquan]` `[role: 结果]` 富贵双全品质为富贵双全的品质判断。 → 《卷六》
  - `[ns_zwds_j6_098]` `[trigger: 高爵厚禄品质]` `[factor_trigger: quality_gaojue_houlu]` `[role: 结果]` 高爵厚禄品质为高爵厚禄的品质判断。 → 《卷六》
  - `[ns_zwds_j6_099]` `[trigger: 公侯承印品质]` `[factor_trigger: quality_gonghou_chengyin]` `[role: 结果]` 公侯承印品质为公侯承印的品质判断。 → 《卷六》
  - `[ns_zwds_j6_100]` `[trigger: 黄殿朝班品质]` `[factor_trigger: quality_huangdian_chaoban]` `[role: 结果]` 黄殿朝班品质为朝廷显贵的品质判断。 → 《卷六》
  - `[ns_zwds_j6_101]` `[trigger: 克夫品质]` `[factor_trigger: quality_kefu]` `[role: 结果]` 克夫品质为克夫的品质判断。 → 《卷六》
  - `[ns_zwds_j6_102]` `[trigger: 四化化忌正荣]` `[factor_trigger: sihua_huaji_zhengrong]` `[role: 条件分支]` 四化化忌正荣为化忌正荣的配置。 → 《卷六》
  - `[ns_zwds_j6_103]` `[trigger: 宾星]` `[factor_trigger: star_bin]` `[role: 主干]` 宾星为宾星的配置。 → 《卷六》
  - `[ns_zwds_j6_104]` `[trigger: 星曜组合]` `[factor_trigger: star_combo]` `[role: 主干]` 星曜组合为星曜的组合配置。 → 《卷六》
  - `[ns_zwds_j6_105]` `[trigger: 煞星群]` `[factor_trigger: star_group_sha]` `[role: 主干]` 煞星群为煞星的组合。 → 《卷六》
  - `[ns_zwds_j6_106]` `[trigger: 火铃星]` `[factor_trigger: star_huoling]` `[role: 主干]` 火铃星为火星铃星的组合。 → 《卷六》
  - `[ns_zwds_j6_107]` `[trigger: 忌星数量]` `[factor_trigger: star_ji_count]` `[role: 主干]` 忌星数量为化忌星的数量。 → 《卷六》
  - `[ns_zwds_j6_108]` `[trigger: 金星守命]` `[factor_trigger: star_jinxing_shouming]` `[role: 条件分支]` 金星守命为金星守命的配置。 → 《卷六》
  - `[ns_zwds_j6_109]` `[trigger: 廉贪二星]` `[factor_trigger: star_liantan_erxing]` `[role: 主干]` 廉贪二星为廉贞贪狼的组合。 → 《卷六》
  - `[ns_zwds_j6_110]` `[trigger: 廉贞出生]` `[factor_trigger: star_lianzhen_chusheng]` `[role: 条件分支]` 廉贞出生为廉贞出生的配置。 → 《卷六》
  - `[ns_zwds_j6_111]` `[trigger: 命星落陷]` `[factor_trigger: star_mingxing_luoxian]` `[role: 条件分支]` 命星落陷为命星落陷的配置。 → 《卷六》
  - `[ns_zwds_j6_112]` `[trigger: 破军得地]` `[factor_trigger: star_pojun_dedi]` `[role: 条件分支]` 破军得地为破军得地的配置。 → 《卷六》
  - `[ns_zwds_j6_113]` `[trigger: 破军迁移]` `[factor_trigger: star_pojun_qianyi]` `[role: 条件分支]` 破军迁移为破军在迁移的配置。 → 《卷六》
  - `[ns_zwds_j6_114]` `[trigger: 破军入庙]` `[factor_trigger: star_pojun_rumiao]` `[role: 条件分支]` 破军入庙为破军入庙的配置。 → 《卷六》
  - `[ns_zwds_j6_115]` `[trigger: 破军身宫]` `[factor_trigger: star_pojun_shengong]` `[role: 条件分支]` 破军身宫为破军在身宫的配置。 → 《卷六》
  - `[ns_zwds_j6_116]` `[trigger: 星曜位置]` `[factor_trigger: star_position]` `[role: 主干]` 星曜位置为星曜的位置配置。 → 《卷六》
  - `[ns_zwds_j6_117]` `[trigger: 庙旺状态]` `[factor_trigger: star_state_miao]` `[role: 主干]` 庙旺状态为星曜的庙旺状态。 → 《卷六》
  - `[ns_zwds_j6_118]` `[trigger: 陷落状态]` `[factor_trigger: star_state_xian]` `[role: 主干]` 陷落状态为星曜的陷落状态。 → 《卷六》
  - `[ns_zwds_j6_119]` `[trigger: 太阳居午]` `[factor_trigger: star_taiyang_juwu]` `[role: 条件分支]` 太阳居午为太阳在午的配置。 → 《卷六》
  - `[ns_zwds_j6_120]` `[trigger: 天府化铃]` `[factor_trigger: star_tianfu_hualing]` `[role: 条件分支]` 天府化铃为天府化铃的配置。 → 《卷六》
  - `[ns_zwds_j6_121]` `[trigger: 天魁天钺]` `[factor_trigger: star_tiankui_tianyue]` `[role: 主干]` 天魁天钺为天魁天钺的组合。 → 《卷六》
  - `[ns_zwds_j6_122]` `[trigger: 天梁庙午]` `[factor_trigger: star_tianliang_miaowu]` `[role: 条件分支]` 天梁庙午为天梁庙于午的配置。 → 《卷六》
  - `[ns_zwds_j6_123]` `[trigger: 天相围垣]` `[factor_trigger: star_tianxiang_weiyuan]` `[role: 条件分支]` 天相围垣为天相围垣的配置。 → 《卷六》
  - `[ns_zwds_j6_124]` `[trigger: 文星居午]` `[factor_trigger: star_wenxing_juwu]` `[role: 条件分支]` 文星居午为文星在午的配置。 → 《卷六》
  - `[ns_zwds_j6_125]` `[trigger: 武曲财宫旺]` `[factor_trigger: star_wuqu_caigong_wang]` `[role: 条件分支]` 武曲财宫旺为武曲在财宫旺的配置。 → 《卷六》
  - `[ns_zwds_j6_126]` `[trigger: 武曲守垣]` `[factor_trigger: star_wuqu_shouyuan]` `[role: 条件分支]` 武曲守垣为武曲守垣的配置。 → 《卷六》"""
    normalized_text_zh: str = """"""
    subject: str = "孟轲之命"
    factor_refs: list = ['pattern_shuanglu', 'pattern_changquchongfeng', 'pattern_jiliang', 'pattern_diwangling', 'pos_juedi', 'source_ref', 'rel_mengke_001', 'pattern_shuanglu', 'rel_mengke_002', 'pattern_diwangling', 'rel_mengke_003', 'pattern_jiliang', 'evi_mengke_001', 'pattern_shuanglu', 'rule_shuanglu_wenming', 'evi_mengke_002', 'pattern_diwangling', 'rule_diwang_wannian', 'concept_literary_fame', 'concept_late_crisis']
    
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
        l1_anchor="zw_v1.0.0_孟轲之命_001_L1",
    )
    version: str = "1.0.0"
