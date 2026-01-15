"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739754
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
    semantic_id="zw_v1.0.0_批贵命_巨门午垣石中隐玉格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批贵命巨门午垣石中隐玉格(SemanticEntry):
    """
    - 分字分词释义：

  - **石中隐玉格**：巨门星守命于午宫，外表平实而内蕴才华的贵命格局，如美玉藏于顽石之中。
  - **巨门午垣**：巨门星守命于午宫，午为巨门的庙旺之地，主才华终将彰显。...
    """
    
    original_text: str = """- 分字分词释义：

  - **石中隐玉格**：巨门星守命于午宫，外表平实而内蕴才华的贵命格局，如美玉藏于顽石之中。
  - **巨门午垣**：巨门星守命于午宫，午为巨门的庙旺之地，主才华终将彰显。
  - **右彼归垣化权**：右彼星归回本宫且化权，增强权柄与在朝地位。
  - **魁钺拱照**：天魁天钺二贵人星拱照身宫，主贵人扶持不断。
  - **金水会蛇卿**：金水两星在巳宫（属蛇）会合，主文才清秀。
  - **洞房花烛**：婚姻的象征意象，本套语中指中年成婚之喜。
  - **鹿鸣佳宴**：科举考中后的庆贺宴会，出自《诗经·小雅·鹿鸣》，本套语中指举业成功。
  - **桑榆暮景**：晚年归隐的意象，桑榆指夕阳，本套语中指年迈后的退休生活。

- **原文（source_text）**：  
  命坐午垣，巨门石中隐玉明彰，逢生无克，理参详三方四正，吉，福寿等陵岗。右弼归垣互守，化权掌幄铿锵。身宫魁钺拱，贵格岂寻常。注人丰神卓伟，表表景星凤凰，胸怀今右富琳琅。功名应有待，何必恁惶。次究星命：某星逢得地，高强，奇哉。金水会蛇卿，文昌文曲画光芒。加会得照合，定拟发科。伤官福二宫星美，生平作事端庄，身居奴仆静中忙。妻宫逢七杀，正副免刑伤。儿宫擎羊作践，先虚后实飞黄。现今限步正辉光。早夺焚舟计，雷剑吐光芒。小限恩光台辅，文宗取试名扬。观场补廪喜洋洋，流昌曲星集，谁识一穿扬。某限行来题达，中年贪武为良，门庭生色喜非常。财源春水涨，志气吐眉扬。某年忌某星，宜慎内外忧伤。亦宜惩忿恣，亲善远奸狂。某限交来七杀紫微制伏祯祥，巍然超拔声名香。拜官居百里，德政嫓龚黄。某年有所畏忌，须知到此惊慌。尚喜某星为福，依然福履无疆。行交某限，十年康。部院驰彩撽，黔庶植甘棠。某限桑榆暮景，东篱陶菊金黄。蒪鲈美味径三荒，二疏从斛组，看子绍书香。某年某星为忤，某星相党相戕，俄然一梦熟黄粱。哲人其萎矣，空为裂肝肠。

- **规范化释义（primary_lang_explained）**：  
  此为批断「巨门午宫·石中隐玉格」贵命的标准套语。命坐午垣，巨门守命形成「石中隐玉」之象——外表平凡而内蕴才华。三方四正吉星聚会，右弼归垣化权，身宫魁钺拱照，构成非凡贵格。套语详论六亲宫位、限运流年，从青年科举、中年仕途到晚年归隐逐一铺陈。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the noble fate pattern "Ju Men in Wu Palace—Jade Hidden in Stone". Life Palace sits in Wu with Ju Men forming the image of hidden talent beneath plain exterior. With auspicious stars in triad, You Bi transforming into Power, and Kui‑Yue aspecting—an extraordinary noble configuration. The template covers Six Relations, period readings from youth examinations to late‑life retirement.

- **核心要点**：  
  1. 适用格局：巨门午宫守命，「石中隐玉」之象。  
  2. 关键配置：右弼归垣化权，身宫魁钺拱照。  
  3. 人生周期：青年科举、中年仕途、晚年归隐。

- **叙事素材（narrative_snippets）**：
  - **石中隐玉**："巨门石中隐玉明彰"，外表平凡而内蕴才华的贵命之象。
  - **化权得势**："右弼归垣互守，化权掌幄"，右弼化权增强权柄。
  - **人生周期**：青年科举、中年仕途、晚年归隐的完整人生批语框架。
  - **现代应用**：本套语可作为巨门午宫贵命的批命模板，展现"大器晚成"的人生轨迹。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j7_008]` `[trigger: 石中隐玉格]` `[factor_trigger: pattern_jumen_wu_shizhongyinyu]` `[role: 条件分支]` 石中隐玉格为巨门午宫守命的贵格，外朴内秀。 → 《卷七》"巨门石中隐玉"
  - `[ns_zwds_j7_009]` `[trigger: 巨门午宫]` `[factor_trigger: star_jumen AND palace_wu]` `[role: 条件分支]` 巨门午宫为巨门星在午宫守命的配置。 → 《卷七》"命坐午垣"
  - `[ns_zwds_j7_010]` `[trigger: 右弼化权]` `[factor_trigger: star_youbi AND hua_quan]` `[role: 条件分支]` 右弼化权为右弼星化权的增强配置。 → 《卷七》"右弼归垣...化权"
  - `[ns_zwds_j7_011]` `[trigger: 魁钺拱照]` `[factor_trigger: pattern_kuiyue_gongzhao]` `[role: 条件分支]` 魁钺拱照为天魁天钺三方拱照的配置。 → 《卷七》"身宫魁钺拱"
  - `[ns_zwds_j7_012]` `[trigger: 大器晚成]` `[factor_trigger: pattern_daqiwancheng]` `[role: 结果]` 大器晚成为外朴内秀终得彰显的人生轨迹。 → 《卷七》
  - `[ns_zwds_j7_013]` `[trigger: 科举仕途]` `[factor_trigger: result_keju_shitu]` `[role: 结果]` 科举仕途为青年科举中年仕途的人生成就。 → 《卷七》"功名应有待"
  - `[ns_zwds_j7_014]` `[trigger: 空劫夹垣格]` `[factor_trigger: pattern_kongjiejiayuan]` `[role: 条件分支]` 空劫夹垣格为地空地劫夹命宫的凶险配置。 → 《卷七》
  - `[ns_zwds_j7_015]` `[trigger: 天伤天使组合]` `[factor_trigger: star_tianshangtian]` `[role: 主干]` 天伤天使组合为凶险的组合配置。 → 《卷七》
  - `[ns_zwds_j7_016]` `[trigger: 空星]` `[factor_trigger: kong]` `[role: 主干]` 空星为空亡之星的统称。 → 《卷七》
  - `[ns_zwds_j7_017]` `[trigger: 马头带剑格]` `[factor_trigger: pattern_matoudaijian]` `[role: 条件分支]` 马头带剑格为天马与擎羊同宫的格局。 → 《卷七》
  - `[ns_zwds_j7_018]` `[trigger: 空劫叠并格]` `[factor_trigger: pattern_kongjiediebing]` `[role: 条件分支]` 空劫叠并格为地空地劫叠加的凶险配置。 → 《卷七》
  - `[ns_zwds_j7_019]` `[trigger: 陷地煞格]` `[factor_trigger: pattern_xiandisha]` `[role: 条件分支]` 陷地煞格为星曜陷地遇煞的凶险配置。 → 《卷七》
  - `[ns_zwds_j7_020]` `[trigger: 限运凶年格]` `[factor_trigger: pattern_xianyunxiongnian]` `[role: 条件分支]` 限运凶年格为限运遇凶年的配置。 → 《卷七》
  - `[ns_zwds_j7_021]` `[trigger: 绝地死地格]` `[factor_trigger: pattern_juedisidi]` `[role: 条件分支]` 绝地死地格为星曜入绝地死地的凶险配置。 → 《卷七》
  - `[ns_zwds_j7_022]` `[trigger: 吉星聚会格]` `[factor_trigger: pattern_jixingjuhui]` `[role: 条件分支]` 吉星聚会格为吉星聚于一宫的贵格。 → 《卷七》
  - `[ns_zwds_j7_023]` `[trigger: 贵星加会格]` `[factor_trigger: pattern_guixingjiahui]` `[role: 条件分支]` 贵星加会格为贵人星加会命宫的贵格。 → 《卷七》
  - `[ns_zwds_j7_024]` `[trigger: 晚运亨通结果]` `[factor_trigger: result_wanyunhengtong]` `[role: 结果]` 晚运亨通结果为晚年运势通顺的判断。 → 《卷七》
  - `[ns_zwds_j7_025]` `[trigger: 早年困顿结果]` `[factor_trigger: result_zaoniankuntun]` `[role: 结果]` 早年困顿结果为早年艰难困苦的判断。 → 《卷七》
  - `[ns_zwds_j7_026]` `[trigger: 中年发达结果]` `[factor_trigger: result_zhongnianfada]` `[role: 结果]` 中年发达结果为中年发迹显达的判断。 → 《卷七》
  - `[ns_zwds_j7_027]` `[trigger: 套语模板]` `[factor_trigger: structure_taoyumoban]` `[role: 主干]` 套语模板为批命时可套用的标准模板。 → 《卷七》
  - `[ns_zwds_j7_028]` `[trigger: 人生周期]` `[factor_trigger: structure_renshengzhouqi]` `[role: 主干]` 人生周期为青年中年晚年的完整周期。 → 《卷七》
  - `[ns_zwds_j7_029]` `[trigger: 六亲结构]` `[factor_trigger: structure_liuqin]` `[role: 主干]` 六亲结构为六亲宫位的整体配置。 → 《卷七》
  - `[ns_zwds_j7_030]` `[trigger: 限运结构]` `[factor_trigger: structure_xianyun]` `[role: 主干]` 限运结构为大限小限流年的整体配置。 → 《卷七》
  - `[ns_zwds_j7_031]` `[trigger: 风险结果]` `[factor_trigger: result_risk]` `[role: 结果]` 风险结果为风险的判断。 → 《卷七》
  - `[ns_zwds_j7_032]` `[trigger: 荣结果]` `[factor_trigger: result_rong]` `[role: 结果]` 荣结果为荣的判断。 → 《卷七》
  - `[ns_zwds_j7_033]` `[trigger: 儒雅结果]` `[factor_trigger: result_ruya]` `[role: 结果]` 儒雅结果为儒雅的判断。 → 《卷七》
  - `[ns_zwds_j7_034]` `[trigger: 上格结果]` `[factor_trigger: result_shangge]` `[role: 结果]` 上格结果为上格的判断。 → 《卷七》
  - `[ns_zwds_j7_035]` `[trigger: 商贾结果]` `[factor_trigger: result_shangjia]` `[role: 结果]` 商贾结果为商贾的判断。 → 《卷七》
  - `[ns_zwds_j7_036]` `[trigger: 煞破贪贵结果]` `[factor_trigger: result_shapolan_gui]` `[role: 结果]` 煞破贪贵结果为煞破贪贵的判断。 → 《卷七》
  - `[ns_zwds_j7_037]` `[trigger: 身旺结果]` `[factor_trigger: result_shenwang]` `[role: 结果]` 身旺结果为身旺的判断。 → 《卷七》
  - `[ns_zwds_j7_038]` `[trigger: 施义不贵结果]` `[factor_trigger: result_shiyi_bugui]` `[role: 结果]` 施义不贵结果为施义不贵的判断。 → 《卷七》
  - `[ns_zwds_j7_039]` `[trigger: 石中隐玉贵结果]` `[factor_trigger: result_shizhongyinyu_gui]` `[role: 结果]` 石中隐玉贵结果为石中隐玉贵的判断。 → 《卷七》
  - `[ns_zwds_j7_040]` `[trigger: 寿结果]` `[factor_trigger: result_shou]` `[role: 结果]` 寿结果为寿的判断。 → 《卷七》
  - `[ns_zwds_j7_041]` `[trigger: 寿不得长结果]` `[factor_trigger: result_shou_budechang]` `[role: 结果]` 寿不得长结果为寿不得长的判断。 → 《卷七》
  - `[ns_zwds_j7_042]` `[trigger: 寿不长结果]` `[factor_trigger: result_shoubuchang]` `[role: 结果]` 寿不长结果为寿不长的判断。 → 《卷七》
  - `[ns_zwds_j7_043]` `[trigger: 寿命结果]` `[factor_trigger: result_shouming]` `[role: 结果]` 寿命结果为寿命的判断。 → 《卷七》
  - `[ns_zwds_j7_044]` `[trigger: 寿难结果]` `[factor_trigger: result_shounan]` `[role: 结果]` 寿难结果为寿难的判断。 → 《卷七》
  - `[ns_zwds_j7_045]` `[trigger: 寿星结果]` `[factor_trigger: result_shouxing]` `[role: 结果]` 寿星结果为寿星的判断。 → 《卷七》
  - `[ns_zwds_j7_046]` `[trigger: 寿阳结果]` `[factor_trigger: result_shouyang]` `[role: 结果]` 寿阳结果为寿阳的判断。 → 《卷七》
  - `[ns_zwds_j7_047]` `[trigger: 寿夭荣枯结果]` `[factor_trigger: result_shouyaorongku]` `[role: 结果]` 寿夭荣枯结果为寿夭荣枯的判断。 → 《卷七》
  - `[ns_zwds_j7_048]` `[trigger: 寿终延结果]` `[factor_trigger: result_shouzhong_yan]` `[role: 结果]` 寿终延结果为寿终延的判断。 → 《卷七》
  - `[ns_zwds_j7_049]` `[trigger: 双美结果]` `[factor_trigger: result_shuangmei]` `[role: 结果]` 双美结果为双美的判断。 → 《卷七》
  - `[ns_zwds_j7_050]` `[trigger: 死于三岁结果]` `[factor_trigger: result_si_yu_sansui]` `[role: 结果]` 死于三岁结果为死于三岁的判断。 → 《卷七》
  - `[ns_zwds_j7_051]` `[trigger: 四品上结果]` `[factor_trigger: result_sipin_shang]` `[role: 结果]` 四品上结果为四品上的判断。 → 《卷七》
  - `[ns_zwds_j7_052]` `[trigger: 死亡结果]` `[factor_trigger: result_siwang]` `[role: 结果]` 死亡结果为死亡的判断。 → 《卷七》
  - `[ns_zwds_j7_053]` `[trigger: 天相贵结果]` `[factor_trigger: result_tianxiang_gui]` `[role: 结果]` 天相贵结果为天相贵的判断。 → 《卷七》
  - `[ns_zwds_j7_054]` `[trigger: 未常夭折结果]` `[factor_trigger: result_weichang_yaozhe]` `[role: 结果]` 未常夭折结果为未常夭折的判断。 → 《卷七》
  - `[ns_zwds_j7_055]` `[trigger: 为臣不忠结果]` `[factor_trigger: result_weichen_buzhong]` `[role: 结果]` 为臣不忠结果为为臣不忠的判断。 → 《卷七》
  - `[ns_zwds_j7_056]` `[trigger: 小限冲时机]` `[factor_trigger: timing_xiaoxian_chong]` `[role: 主干]` 小限冲时机为小限冲的时机。 → 《卷七》
  - `[ns_zwds_j7_057]` `[trigger: 小限冲命时机]` `[factor_trigger: timing_xiaoxian_chongming]` `[role: 主干]` 小限冲命时机为小限冲命的时机。 → 《卷七》
  - `[ns_zwds_j7_058]` `[trigger: 小限地网时机]` `[factor_trigger: timing_xiaoxian_diwang]` `[role: 主干]` 小限地网时机为小限地网的时机。 → 《卷七》
  - `[ns_zwds_j7_059]` `[trigger: 小限夹地时机]` `[factor_trigger: timing_xiaoxian_jiadi]` `[role: 主干]` 小限夹地时机为小限夹地的时机。 → 《卷七》
  - `[ns_zwds_j7_060]` `[trigger: 小限绝地时机]` `[factor_trigger: timing_xiaoxian_juedi]` `[role: 主干]` 小限绝地时机为小限绝地的时机。 → 《卷七》
  - `[ns_zwds_j7_061]` `[trigger: 小限命垣时机]` `[factor_trigger: timing_xiaoxian_mingyuan]` `[role: 主干]` 小限命垣时机为小限命垣的时机。 → 《卷七》
  - `[ns_zwds_j7_062]` `[trigger: 小限太岁丑时机]` `[factor_trigger: timing_xiaoxian_taisui_chou]` `[role: 主干]` 小限太岁丑时机为小限太岁丑的时机。 → 《卷七》
  - `[ns_zwds_j7_063]` `[trigger: 小限天罗时机]` `[factor_trigger: timing_xiaoxian_tianluo]` `[role: 主干]` 小限天罗时机为小限天罗的时机。 → 《卷七》
  - `[ns_zwds_j7_064]` `[trigger: 小限刑忌时机]` `[factor_trigger: timing_xiaoxian_xingji]` `[role: 主干]` 小限刑忌时机为小限刑忌的时机。 → 《卷七》
  - `[ns_zwds_j7_065]` `[trigger: 小限寅卯时机]` `[factor_trigger: timing_xiaoxian_yinmao]` `[role: 主干]` 小限寅卯时机为小限寅卯的时机。 → 《卷七》
  - `[ns_zwds_j7_066]` `[trigger: 阳星有地时机]` `[factor_trigger: timing_yangxing_youdi]` `[role: 主干]` 阳星有地时机为阳星有地的时机。 → 《卷七》
  - `[ns_zwds_j7_067]` `[trigger: 寅申冲时机]` `[factor_trigger: timing_yinshen_chong]` `[role: 主干]` 寅申冲时机为寅申冲的时机。 → 《卷七》
  - `[ns_zwds_j7_068]` `[trigger: 中年美景时机]` `[factor_trigger: timing_zhongnian_meijing]` `[role: 主干]` 中年美景时机为中年美景的时机。 → 《卷七》
  - `[ns_zwds_j7_069]` `[trigger: 富而不贵特质]` `[factor_trigger: trait_fu_er_bugui]` `[role: 主干]` 富而不贵特质为富而不贵的特质。 → 《卷七》
  - `[ns_zwds_j7_070]` `[trigger: 刚烈特质]` `[factor_trigger: trait_ganglie]` `[role: 主干]` 刚烈特质为刚烈的特质。 → 《卷七》
  - `[ns_zwds_j7_071]` `[trigger: 刚柔并济特质]` `[factor_trigger: trait_gangrou_bingji]` `[role: 主干]` 刚柔并济特质为刚柔并济的特质。 → 《卷七》
  - `[ns_zwds_j7_072]` `[trigger: 厚重特质]` `[factor_trigger: trait_houzhong]` `[role: 主干]` 厚重特质为厚重的特质。 → 《卷七》
  - `[ns_zwds_j7_073]` `[trigger: 克己存仁特质]` `[factor_trigger: trait_keji_cunren]` `[role: 主干]` 克己存仁特质为克己存仁的特质。 → 《卷七》
  - `[ns_zwds_j7_074]` `[trigger: 善政牧民特质]` `[factor_trigger: trait_shanzheng_mumin]` `[role: 主干]` 善政牧民特质为善政牧民的特质。 → 《卷七》
  - `[ns_zwds_j7_075]` `[trigger: 十九安乐特质]` `[factor_trigger: trait_shijiu_anle]` `[role: 主干]` 十九安乐特质为十九安乐的特质。 → 《卷七》
  - `[ns_zwds_j7_076]` `[trigger: 有义无偏党特质]` `[factor_trigger: trait_youyi_wupiandang]` `[role: 主干]` 有义无偏党特质为有义无偏党的特质。 → 《卷七》
  - `[ns_zwds_j7_077]` `[trigger: 州穷徐馈特质]` `[factor_trigger: trait_zhouqiong_xukui]` `[role: 主干]` 州穷徐馈特质为州穷徐馈的特质。 → 《卷七》
  - `[ns_zwds_j7_078]` `[trigger: 主夫益子特质]` `[factor_trigger: trait_zhufu_yizi]` `[role: 主干]` 主夫益子特质为主夫益子的特质。 → 《卷七》
  - `[ns_zwds_j7_079]` `[trigger: 廉贞化忌转化]` `[factor_trigger: trans_lianzhenhuaji]` `[role: 主干]` 廉贞化忌转化为廉贞化忌的转化。 → 《卷七》
  - `[ns_zwds_j7_080]` `[trigger: 文曲化忌转化]` `[factor_trigger: transform_wenqu_huaji]` `[role: 主干]` 文曲化忌转化为文曲化忌的转化。 → 《卷七》"""
    normalized_text_zh: str = """"""
    subject: str = "批贵命·巨门午垣石中隐玉格"
    factor_refs: list = ['pattern_jumen_wu_shizhongyinyu', 'pattern_youbi_guiyuan_huaquan', 'pattern_kuiyue_gongzhao', 'symbol_fenzhouji_juezhan', 'symbol_leijian_tuguangmang', 'source_ref', 'rel_vol7_02_001', 'pattern_jumen_wu_shizhongyinyu', 'rel_vol7_02_002', 'pattern_youbi_guiyuan_huaquan', 'rel_vol7_02_003', 'symbol_fenzhouji_juezhan', 'evi_vol7_02_001', 'rule_shizhongyinyu_gui', 'evi_vol7_02_002', 'pattern_youbi_guiyuan_huaquan', 'rule_youbi_huaquan_quanbing', 'evi_vol7_02_003', 'rule_fenzhou_leijian_breakthrough', 'concept_hidden_talent', 'concept_all_in_decision']
    
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
        l1_anchor="zw_v1.0.0_批贵命_巨门午垣石中隐玉格_001_L1",
    )
    version: str = "1.0.0"
