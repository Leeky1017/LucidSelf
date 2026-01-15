"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778371
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
    semantic_id="zw_v1.0.0_1_总论_格局与命限_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 1总论格局与命限(SemanticEntry):
    """
    - 原文（断句）：

  太极星缠，乃群宿众星之主，天门运限，即扶身助命之原。在天则运用无常，在人则命有格局。先明格局，次看恶星。或有同年同月、同日同时而生，则有贫贱富贵寿夭之异。或在恶限，积百万之金...
    """
    
    original_text: str = """- 原文（断句）：

  太极星缠，乃群宿众星之主，天门运限，即扶身助命之原。在天则运用无常，在人则命有格局。先明格局，次看恶星。或有同年同月、同日同时而生，则有贫贱富贵寿夭之异。或在恶限，积百万之金银；或在旺乡，抛连年之困苦。祸福不一途而推，吉凶不可一例而断。要知一世之荣枯，定看五行之宫位。立命便知贵贱，安身即晓根基。第一先看福德，再三细考迁移。分对宫之体用，定三合之源流。命无正曜，夭折孤贫；士有凶星，美玉瑕玷。既得根基坚固，须知合局相生。坚固则富贵延寿，相生则财官昭著。

- 分字分词释义：

  - **太极星缠**：以北极紫微为中心，众星环绕的格局结构，象征命盘的核心架构。
  - **天门运限**：大限小限与流年的运行轨迹，是扶持身命的时间因素。
  - **先明格局**：推命首要步骤是确定格局层次，格局定框架。
  - **次看恶星**：在格局确定后，再看凶星配合情况。
  - **恶限积财**：在凶煞主运的限期内，反而积累财富的反常现象。
  - **旺乡困苦**：在本应吉旺的宫位或时期，却遭受困苦。
  - **五行之宫位**：十二宫与五行的配属关系，是判断吉凶的基础。
  - **立命知贵贱**：通过命宫的配置判断贵贱高低。
  - **安身晓根基**：通过身宫的配置了解命主的根本基础。
  - **福德先看**：推命首先看福德宫，主一生福禄根基。
  - **细考迁移**：仔细考察迁移宫，主外出运势与变化。
  - **对宫体用**：命宫与迁移、财帛与福德等对宫的主次关系。
  - **三合源流**：命宫与三方（财帛、官禄）形成的三合局。
  - **命无正曜**：命宫没有紫微、天府等正曜主星。
  - **合局相生**：三方四正的星曜形成相生配合的吉格。

- 规范化释义（primary_lang_explained）：

  太极星缠是众星之主，天门运限是扶身助命的根源。在天道则运转无常，在人命则各有格局。推命要先明确格局层次，再看恶星配合；即使同年同月同日同时生人，也会因格局不同而贫富寿夭各异。有人在凶限中却能积累百万财富，有人在旺地却连年困苦，祸福路径不同，吉凶不可一概而论。要知一生荣枯，必看五行宫位；立命便知贵贱高低，安身即晓根基深浅。推命首先看福德宫，再三细考迁移宫，分辨对宫的体用关系，确定三方的源流配合。命宫无正曜则夭折孤贫，命中有凶星则如美玉有瑕。既要根基坚固，也须合局相生：根基坚固则富贵延寿，合局相生则财官昭著。

- 完整对等诠释（secondary_lang_full）：

  The Celestial Pole and stellar configurations serve as the lords of all stars, while the cycles of transiting limits provide the foundational source for sustaining life and destiny. In Heaven's operation, cycles shift unpredictably; in human fate, each life carries its unique pattern-structure. When analyzing a chart, first discern the pattern hierarchy, then examine malefic influences. Even individuals born at identical year-month-day-hour may experience vastly different outcomes in wealth, nobility, longevity, or early death due to divergent pattern configurations. One person may amass a fortune during adverse limits; another may endure prolonged hardship in prosperous periods—fortune and misfortune follow distinct pathways, and auspiciousness or inauspiciousness cannot be judged by a single standard. To understand a lifetime's rise and decline, one must examine the Five-Element positions of palaces. Establishing the Life Palace reveals nobility or baseness; locating the Body Palace discloses the root foundation. Begin by scrutinizing the Fortune Palace, then carefully investigate the Travel Palace. Distinguish the substance-function relationship of opposing palaces and determine the source-flow dynamics of the three-directional harmony. A Life Palace lacking principal stars indicates early death and destitution; a chart riddled with malefic stars is like flawed jade. One requires both a solid foundation and harmonious pattern-interaction: a solid foundation brings wealth, nobility, and longevity, while harmonious pattern-interaction illuminates wealth and official rank.

- 核心要点：

  1. **格局为先**：先明格局，次看恶星，格局决定命运框架。
  2. **同时不同命**：同年月日时生人，因格局不同而贫富寿夭有异。
  3. **限运关键**：恶限积财、旺乡困苦，祸福由限运决定。
  4. **看命顺序**：立命知贵贱、安身晓根基、先看福德、细考迁移。
  5. **合局相生**：根基坚固+合局相生，则富贵延寿财官昭著。

- 叙事素材（narrative_snippets）：

  - **太极核心**："太极星缠，天门运限"，以太极为核心、限运为时机的判断框架。
  - **格局先行**："先明格局，次看恶星"，判断命运必须先定格局，再看具体吉凶星配合。
  - **同时异命**："同年月日时，生人不同，贫富寿夭有异"，解释同时生人命运各异的原因。
  - **限运关键**："恶限积财，旺乡困苦"，强调限运对实际祸福的决定作用。
  - **看命顺序**："立命知贵贱，安身晓根基，先看福德，细考迁移"，建立标准看命流程。
  - **现代应用**：本条可作为命盘判断的"元规则"——先格局、次限运、三合局相生。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j2_001]` `[trigger: 格局层次]` `[factor_trigger: geju_cengci]` `[role: 主干]` 格局层次由命盘整体配置决定，分富贵/中局/贫贱三等。 → 《骨髓赋》
  - `[ns_zwds_j2_002]` `[trigger: 根基状态]` `[factor_trigger: genji_zhuangtai]` `[role: 主干]` 根基状态为身命宫的强弱程度，分坚固/平常/浮弱。 → 《骨髓赋》"安身晓根基"
  - `[ns_zwds_j2_003]` `[trigger: 合局状态]` `[factor_trigger: heju_zhuangtai]` `[role: 主干]` 合局状态为三方四正的配合程度，分相生/相克/混杂。 → 《骨髓赋》"合局相生"
  - `[ns_zwds_j2_004]` `[trigger: 限运配合]` `[factor_trigger: xianyun_peihe]` `[role: 主干]` 限运配合度为限运与格局的吻合程度。 → 《骨髓赋》"恶限积财"
  - `[ns_zwds_j2_005]` `[trigger: 荣枯评估]` `[factor_trigger: rongku_pinggu]` `[role: 结果]` 荣枯评估为命运最终结果的综合判断。 → 《骨髓赋》
  - `[ns_zwds_j2_006]` `[trigger: 三位评估]` `[factor_trigger: sanwei_pinggu]` `[role: 主干]` 三位评估为身命福德迁移三位的综合考量。 → 《骨髓赋》"先看福德，细考迁移"
  - `[ns_zwds_j2_007]` `[trigger: 德行评估]` `[factor_trigger: dexing_pinggu]` `[role: 主干]` 德行评估为福德宫状态的判断。 → 《骨髓赋》"先看福德"
  - `[ns_zwds_j2_008]` `[trigger: 格局结构]` `[factor_trigger: zuhe_geju]` `[role: 主干]` 格局结构为命盘星曜组合形成的整体配置。 → 《骨髓赋》
  - `[ns_zwds_j2_009]` `[trigger: 组合庙旺]` `[factor_trigger: zuhe_miaowang]` `[role: 条件分支]` 组合庙旺为星曜组合处于庙旺之地的状态。 → 《骨髓赋》
  - `[ns_zwds_j2_010]` `[trigger: 杂居结构]` `[factor_trigger: zaju_jiegou]` `[role: 条件分支]` 杂居结构为吉凶星混杂同宫的配置。 → 《骨髓赋》"恶星杂凑"
  - `[ns_zwds_j2_011]` `[trigger: 仙云配合]` `[factor_trigger: xianyun_peihe]` `[role: 主干]` 仙云配合为限运与格局的配合程度判断。 → 《骨髓赋》
  - `[ns_zwds_j2_012]` `[trigger: 仙云吉凶]` `[factor_trigger: xianyun_jixi]` `[role: 条件分支]` 仙云吉凶为限运所遇星曜的吉凶状态。 → 《骨髓赋》
  - `[ns_zwds_j2_013]` `[trigger: 仙云转折]` `[factor_trigger: xianyun_zhuanzhe]` `[role: 条件分支]` 仙云转折为限运交接时的吉凶变化。 → 《骨髓赋》
  - `[ns_zwds_j2_014]` `[trigger: 案例格局]` `[factor_trigger: anli_geju]` `[role: 主干]` 案例格局为命例中的实际格局配置。 → 《骨髓赋》
  - `[ns_zwds_j2_015]` `[trigger: 案例验证]` `[factor_trigger: anli_yanzheng]` `[role: 主干]` 案例验证为命例与理论的对照验证。 → 《骨髓赋》
  - `[ns_zwds_j2_086]` `[trigger: 十四主星结构]` `[factor_trigger: structure_shisizhuxing]` `[role: 主干]` 十四主星结构为紫微斗数十四颗主星的整体配置。 → 《骨髓赋》
  - `[ns_zwds_j2_087]` `[trigger: 流年太岁系统]` `[factor_trigger: system_liuniantaisui]` `[role: 主干]` 流年太岁系统为年份运势判断的核心系统。 → 《骨髓赋》
  - `[ns_zwds_j2_088]` `[trigger: 太岁十二神煞]` `[factor_trigger: system_taishui12shensha]` `[role: 主干]` 太岁十二神煞为流年太岁所带的十二神煞系统。 → 《骨髓赋》
  - `[ns_zwds_j2_089]` `[trigger: 不中结果]` `[factor_trigger: result_buzhong]` `[role: 结果]` 不中结果为考试不中的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_090]` `[trigger: 福禄损结果]` `[factor_trigger: result_fulusun]` `[role: 结果]` 福禄损结果为福禄受损的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_091]` `[trigger: 凶险结果]` `[factor_trigger: result_xiongxian]` `[role: 结果]` 凶险结果为凶险灾厄的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_092]` `[trigger: 上寿结果]` `[factor_trigger: result_shangshou]` `[role: 结果]` 上寿结果为高寿长寿的吉利判断。 → 《骨髓赋》
  - `[ns_zwds_j2_093]` `[trigger: 贪武同行格]` `[factor_trigger: pattern_tanwu_tongxing]` `[role: 条件分支]` 贪武同行格为贪狼武曲同宫或对照的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_094]` `[trigger: 机月同梁格]` `[factor_trigger: pattern_jiyuetongliang]` `[role: 条件分支]` 机月同梁格为天机太阴天同天梁的组合格局。 → 《骨髓赋》
  - `[ns_zwds_j2_095]` `[trigger: 科禄加会格]` `[factor_trigger: pattern_kelu_jiahui]` `[role: 条件分支]` 科禄加会格为化科化禄加会命宫的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_096]` `[trigger: 到寿结果]` `[factor_trigger: result_daoshou]` `[role: 结果]` 到寿结果为寿终正寝的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_097]` `[trigger: 大限天伤时]` `[factor_trigger: timing_daxian_tianshang]` `[role: 条件分支]` 大限天伤时为大限遇天伤的凶险时机。 → 《骨髓赋》
  - `[ns_zwds_j2_098]` `[trigger: 紫破辰戌格]` `[factor_trigger: pattern_zipo_chenxu]` `[role: 条件分支]` 紫破辰戌格为紫微破军在辰戌的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_099]` `[trigger: 左右同宫格]` `[factor_trigger: pattern_zuoyou_tonggong]` `[role: 条件分支]` 左右同宫格为左辅右弼同宫的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_100]` `[trigger: 紫府同宫格]` `[factor_trigger: pattern_zifu_tonggong]` `[role: 条件分支]` 紫府同宫格为紫微天府同宫的极贵格局。 → 《骨髓赋》
  - `[ns_zwds_j2_101]` `[trigger: 天空天伤煞]` `[factor_trigger: malefic_tiankong_tianshang]` `[role: 条件分支]` 天空天伤煞为天空与天伤的凶险组合。 → 《骨髓赋》
  - `[ns_zwds_j2_102]` `[trigger: 权禄夹命格]` `[factor_trigger: pattern_quanlu_jiaming]` `[role: 条件分支]` 权禄夹命格为化权化禄夹命宫的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_103]` `[trigger: 中寿结果]` `[factor_trigger: result_zhongshou]` `[role: 结果]` 中寿结果为中等寿命的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_104]` `[trigger: 太刚结果]` `[factor_trigger: result_taigang]` `[role: 结果]` 太刚结果为性格太刚的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_105]` `[trigger: 巨日拱照格]` `[factor_trigger: pattern_juri_gongzhao]` `[role: 条件分支]` 巨日拱照格为巨门太阳拱照的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_106]` `[trigger: 大限绝地时]` `[factor_trigger: timing_daxian_jiadi]` `[role: 条件分支]` 大限绝地时为大限行绝地的凶险时机。 → 《骨髓赋》
  - `[ns_zwds_j2_107]` `[trigger: 紫府朝垣格2]` `[factor_trigger: pattern_zifu_chaoyuan]` `[role: 条件分支]` 紫府朝垣格为紫微天府朝拱命宫的极贵格局。 → 《骨髓赋》
  - `[ns_zwds_j2_108]` `[trigger: 左右扶持格]` `[factor_trigger: pattern_zuoyou_fuchi]` `[role: 条件分支]` 左右扶持格为左辅右弼扶持命宫的贵人格局。 → 《骨髓赋》
  - `[ns_zwds_j2_109]` `[trigger: 火索天伤煞]` `[factor_trigger: malefic_huosuo_tianshang]` `[role: 条件分支]` 火索天伤煞为火星与天伤的凶险组合。 → 《骨髓赋》
  - `[ns_zwds_j2_110]` `[trigger: 小限重逢时]` `[factor_trigger: timing_xiaoxian_chongfeng]` `[role: 条件分支]` 小限重逢时为小限重逢凶星的凶险时机。 → 《骨髓赋》
  - `[ns_zwds_j2_111]` `[trigger: 苦堪结果]` `[factor_trigger: result_kukan]` `[role: 结果]` 苦堪结果为艰苦困难的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_112]` `[trigger: 贤结果]` `[factor_trigger: result_xian]` `[role: 结果]` 贤结果为贤德贤良的吉利判断。 → 《骨髓赋》
  - `[ns_zwds_j2_113]` `[trigger: 不修结果]` `[factor_trigger: result_buxiu]` `[role: 结果]` 不修结果为不修德行的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_114]` `[trigger: 不达结果]` `[factor_trigger: result_buda]` `[role: 结果]` 不达结果为不能通达的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_115]` `[trigger: 贫结果]` `[factor_trigger: result_pin]` `[role: 结果]` 贫结果为贫穷困苦的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_116]` `[trigger: 富贵层次]` `[factor_trigger: fugui_cengci]` `[role: 主干]` 富贵层次为命格富贵程度的分级评估。 → 《骨髓赋》
  - `[ns_zwds_j2_117]` `[trigger: 煞星类型]` `[factor_trigger: star_sha]` `[role: 主干]` 煞星类型为凶煞星的分类。 → 《骨髓赋》
  - `[ns_zwds_j2_118]` `[trigger: 巨门福命结果]` `[factor_trigger: result_jumen_fuming]` `[role: 结果]` 巨门福命结果为巨门守命主福的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_119]` `[trigger: 落陷福命结果]` `[factor_trigger: result_luoxian_fuming]` `[role: 结果]` 落陷福命结果为星曜落陷时的福命判断。 → 《骨髓赋》
  - `[ns_zwds_j2_120]` `[trigger: 贵妇命结果]` `[factor_trigger: result_guifu_ming]` `[role: 结果]` 贵妇命结果为女命贵妇的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_121]` `[trigger: 内助持家特质]` `[factor_trigger: trait_neizhu_chijia]` `[role: 主干]` 内助持家特质为女命贤良持家的特质。 → 《骨髓赋》
  - `[ns_zwds_j2_122]` `[trigger: 幽兰出谷象征]` `[factor_trigger: symbol_youlan_chugu]` `[role: 主干]` 幽兰出谷象征为高洁不群的美好象征。 → 《骨髓赋》
  - `[ns_zwds_j2_123]` `[trigger: 女命贵结果]` `[factor_trigger: result_numing_gui]` `[role: 结果]` 女命贵结果为女命显贵的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_124]` `[trigger: 社会结果]` `[factor_trigger: result_shehui]` `[role: 结果]` 社会结果为社会地位的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_125]` `[trigger: 颐养结果]` `[factor_trigger: result_yiyang]` `[role: 结果]` 颐养结果为养生颐养的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_126]` `[trigger: 父母结果]` `[factor_trigger: result_fumu]` `[role: 结果]` 父母结果为父母宫吉凶的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_127]` `[trigger: 单丁门类型]` `[factor_trigger: type_dandingmen]` `[role: 主干]` 单丁门类型为子嗣稀少的命格类型。 → 《骨髓赋》
  - `[ns_zwds_j2_128]` `[trigger: 可信层次]` `[factor_trigger: level_kexin]` `[role: 主干]` 可信层次为判断可信度的分级。 → 《骨髓赋》
  - `[ns_zwds_j2_129]` `[trigger: 孝而可钦格]` `[factor_trigger: pattern_xiaoerkeqin]` `[role: 条件分支]` 孝而可钦格为孝顺可敬的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_130]` `[trigger: 当年压力结果]` `[factor_trigger: result_dangnianyali]` `[role: 结果]` 当年压力结果为流年压力的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_131]` `[trigger: 阴质概念]` `[factor_trigger: concept_yinzhi]` `[role: 主干]` 阴质概念为阴性特质的核心概念。 → 《骨髓赋》
  - `[ns_zwds_j2_132]` `[trigger: 灾祸结果]` `[factor_trigger: result_zaihuo]` `[role: 结果]` 灾祸结果为灾难祸患的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_133]` `[trigger: 驳折结果]` `[factor_trigger: result_bozhe]` `[role: 结果]` 驳折结果为挫折坎坷的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_134]` `[trigger: 年度吉凶结果]` `[factor_trigger: result_niandujixiong]` `[role: 结果]` 年度吉凶结果为流年吉凶的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_135]` `[trigger: 嘉格破格]` `[factor_trigger: jiage_poge]` `[role: 主干]` 嘉格破格为好格局被破坏的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_136]` `[trigger: 富贵层级]` `[factor_trigger: fugui_cenji]` `[role: 主干]` 富贵层级为富贵等级的分类。 → 《骨髓赋》
  - `[ns_zwds_j2_137]` `[trigger: 盛极必衰]` `[factor_trigger: shengjibishuai]` `[role: 主干]` 盛极必衰为物极必反的原则。 → 《骨髓赋》
  - `[ns_zwds_j2_138]` `[trigger: 女命体系]` `[factor_trigger: nvming_tixi]` `[role: 主干]` 女命体系为女命论断的专属体系。 → 《骨髓赋》
  - `[ns_zwds_j2_139]` `[trigger: 人生状态]` `[factor_trigger: rensheng_zhuangtai]` `[role: 主干]` 人生状态为人生阶段的状态评估。 → 《骨髓赋》
  - `[ns_zwds_j2_140]` `[trigger: 星曜庙旺]` `[factor_trigger: xingyao_miaowang]` `[role: 主干]` 星曜庙旺为星曜庙旺状态的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_141]` `[trigger: 因妻得贵效果]` `[factor_trigger: effect_yinqidegui]` `[role: 结果]` 因妻得贵效果为因配偶而显贵的效果。 → 《骨髓赋》
  - `[ns_zwds_j2_142]` `[trigger: 主星类型]` `[factor_trigger: star_zhuxing]` `[role: 主干]` 主星类型为十四主星的分类。 → 《骨髓赋》
  - `[ns_zwds_j2_143]` `[trigger: 横发横破格]` `[factor_trigger: pattern_hengfahengpo]` `[role: 条件分支]` 横发横破格为暴发暴落的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_144]` `[trigger: 血气纪类型]` `[factor_trigger: type_xueqiji]` `[role: 主干]` 血气纪类型为血气体质的类型。 → 《骨髓赋》
  - `[ns_zwds_j2_145]` `[trigger: 流荡格]` `[factor_trigger: pattern_liudang]` `[role: 条件分支]` 流荡格为漂泊不定的凶格。 → 《骨髓赋》
  - `[ns_zwds_j2_146]` `[trigger: 命犯擎羊格]` `[factor_trigger: pattern_mingfanqingyang]` `[role: 条件分支]` 命犯擎羊格为命宫犯擎羊的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_147]` `[trigger: 夭亡结果]` `[factor_trigger: result_yaowang]` `[role: 结果]` 夭亡结果为早年夭折的凶险判断。 → 《骨髓赋》
  - `[ns_zwds_j2_148]` `[trigger: 巨机巨卯格]` `[factor_trigger: pattern_jujijumao]` `[role: 条件分支]` 巨机巨卯格为巨门天机在卯的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_149]` `[trigger: 公卿结果]` `[factor_trigger: result_gongqing]` `[role: 结果]` 公卿结果为位列公卿的贵显判断。 → 《骨髓赋》
  - `[ns_zwds_j2_150]` `[trigger: 未宫擎羊格]` `[factor_trigger: pattern_weigongqingyang]` `[role: 条件分支]` 未宫擎羊格为未宫遇擎羊的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_151]` `[trigger: 流陀夹格]` `[factor_trigger: pattern_liutuojia]` `[role: 条件分支]` 流陀夹格为流年陀罗夹命的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_152]` `[trigger: 空劫流年格]` `[factor_trigger: pattern_kongjieliunian]` `[role: 条件分支]` 空劫流年格为流年遇空劫的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_153]` `[trigger: 权禄科格]` `[factor_trigger: pattern_quanluke]` `[role: 条件分支]` 权禄科格为化权化禄化科同会的极贵格局。 → 《骨髓赋》
  - `[ns_zwds_j2_154]` `[trigger: 三奇加会格]` `[factor_trigger: pattern_sanqijiahui]` `[role: 条件分支]` 三奇加会格为化科权禄加会的极贵格局。 → 《骨髓赋》
  - `[ns_zwds_j2_155]` `[trigger: 吉凶混杂格]` `[factor_trigger: pattern_jixionghunza]` `[role: 条件分支]` 吉凶混杂格为吉凶星混杂的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_156]` `[trigger: 寿元结果]` `[factor_trigger: result_shouyuan]` `[role: 结果]` 寿元结果为寿命长短的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_157]` `[trigger: 官禄结果]` `[factor_trigger: result_guanlu]` `[role: 结果]` 官禄结果为官职禄位的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_158]` `[trigger: 事业结果]` `[factor_trigger: result_shiye]` `[role: 结果]` 事业结果为事业成就的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_159]` `[trigger: 田宅结果]` `[factor_trigger: result_tianzhai]` `[role: 结果]` 田宅结果为田产房宅的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_160]` `[trigger: 子嗣结果]` `[factor_trigger: result_zisi]` `[role: 结果]` 子嗣结果为子女后代的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_161]` `[trigger: 婚姻结果]` `[factor_trigger: result_hunyin]` `[role: 结果]` 婚姻结果为婚姻配偶的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_162]` `[trigger: 疾厄结果]` `[factor_trigger: result_jie]` `[role: 结果]` 疾厄结果为疾病灾厄的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_163]` `[trigger: 迁移结果]` `[factor_trigger: result_qianyi]` `[role: 结果]` 迁移结果为迁移外出的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_164]` `[trigger: 仆役结果]` `[factor_trigger: result_puyi]` `[role: 结果]` 仆役结果为仆役下属的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_165]` `[trigger: 紫破加吉格]` `[factor_trigger: pattern_zipojiaqi]` `[role: 条件分支]` 紫破加吉格为紫微破军加吉星的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_166]` `[trigger: 廉贞化忌格]` `[factor_trigger: pattern_lianzhenhuaji]` `[role: 条件分支]` 廉贞化忌格为廉贞化忌的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_167]` `[trigger: 武曲化忌格]` `[factor_trigger: pattern_wuquhuaji]` `[role: 条件分支]` 武曲化忌格为武曲化忌的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_168]` `[trigger: 太阳化忌格]` `[factor_trigger: pattern_taiyanghuaji]` `[role: 条件分支]` 太阳化忌格为太阳化忌的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_169]` `[trigger: 巨门化忌格]` `[factor_trigger: pattern_jumenhuaji]` `[role: 条件分支]` 巨门化忌格为巨门化忌的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_170]` `[trigger: 禄马交驰格]` `[factor_trigger: lumajiaochi]` `[role: 条件分支]` 禄马交驰格为禄存天马交会的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_171]` `[trigger: 白虎三方凶]` `[factor_trigger: malefic_baihu_sanfang]` `[role: 条件分支]` 白虎三方凶为白虎在三方的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_172]` `[trigger: 病符流羊凶]` `[factor_trigger: malefic_bingfu_liuyang]` `[role: 条件分支]` 病符流羊凶为病符与流羊的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_173]` `[trigger: 乘马指向凶]` `[factor_trigger: malefic_chenma_zhixiang]` `[role: 条件分支]` 乘马指向凶为天马方向的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_174]` `[trigger: 凶星簇聚]` `[factor_trigger: malefic_cluster]` `[role: 条件分支]` 凶星簇聚为凶星聚集的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_175]` `[trigger: 大龄地网凶]` `[factor_trigger: malefic_daling_diwang]` `[role: 条件分支]` 大龄地网凶为老年入地网的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_176]` `[trigger: 大限天空凶]` `[factor_trigger: malefic_daxian_tiankong]` `[role: 条件分支]` 大限天空凶为大限遇天空的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_177]` `[trigger: 地劫宫位凶]` `[factor_trigger: malefic_dijie_gong]` `[role: 条件分支]` 地劫宫位凶为地劫所在宫位的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_178]` `[trigger: 地劫火星凶]` `[factor_trigger: malefic_dijie_huoxing]` `[role: 条件分支]` 地劫火星凶为地劫与火星的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_179]` `[trigger: 地劫天哭凶]` `[factor_trigger: malefic_dijie_tianku]` `[role: 条件分支]` 地劫天哭凶为地劫与天哭的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_180]` `[trigger: 地劫相凑凶]` `[factor_trigger: malefic_dijie_xiangcou]` `[role: 条件分支]` 地劫相凑凶为地劫相凑的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_181]` `[trigger: 地劫在垣凶]` `[factor_trigger: malefic_dijie_zaiyuan]` `[role: 条件分支]` 地劫在垣凶为地劫在垣的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_182]` `[trigger: 地网凶格]` `[factor_trigger: malefic_diwang]` `[role: 条件分支]` 地网凶格为地网的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_183]` `[trigger: 地网陀忌凶]` `[factor_trigger: malefic_diwang_tuoji]` `[role: 条件分支]` 地网陀忌凶为地网遇陀忌的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_184]` `[trigger: 恶煞交并凶]` `[factor_trigger: malefic_esha_jiaobing]` `[role: 条件分支]` 恶煞交并凶为恶煞交会的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_185]` `[trigger: 飞廉流羊凶]` `[factor_trigger: malefic_feilian_liuyang]` `[role: 条件分支]` 飞廉流羊凶为飞廉与流羊的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_186]` `[trigger: 福星陷背凶]` `[factor_trigger: malefic_fuxing_xianbei]` `[role: 条件分支]` 福星陷背凶为福星陷落背向的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_187]` `[trigger: 福子混杂凶]` `[factor_trigger: malefic_fuzi_hunza]` `[role: 条件分支]` 福子混杂凶为福德子女混杂的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_188]` `[trigger: 干支化忌凶]` `[factor_trigger: malefic_gan_huaji]` `[role: 条件分支]` 干支化忌凶为干支化忌的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_189]` `[trigger: 火铃冲照凶]` `[factor_trigger: malefic_huoling_chongzhao]` `[role: 条件分支]` 火铃冲照凶为火铃冲照的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_190]` `[trigger: 火铃羊陀夹命凶]` `[factor_trigger: malefic_huoling_yangtuo_jiaming]` `[role: 条件分支]` 火铃羊陀夹命凶为火铃羊陀夹命的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_191]` `[trigger: 火星冲照凶]` `[factor_trigger: malefic_huoxing_chongzhao]` `[role: 条件分支]` 火星冲照凶为火星冲照的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_192]` `[trigger: 火星劫空凶]` `[factor_trigger: malefic_huoxing_jiekong]` `[role: 条件分支]` 火星劫空凶为火星与劫空的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_193]` `[trigger: 火星同垣凶]` `[factor_trigger: malefic_huoxing_tongyuan]` `[role: 条件分支]` 火星同垣凶为火星同垣的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_194]` `[trigger: 火星未凶]` `[factor_trigger: malefic_huoxing_wei]` `[role: 条件分支]` 火星未凶为火星在未的凶险配置。 → 《骨髓赋》
  - `[ns_zwds_j2_195]` `[trigger: 权禄格2]` `[factor_trigger: pattern_quanluge]` `[role: 条件分支]` 权禄格为化权化禄的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_196]` `[trigger: 日月反背格2]` `[factor_trigger: pattern_riyue_fanbei]` `[role: 条件分支]` 日月反背格为日月反背的凶格。 → 《骨髓赋》
  - `[ns_zwds_j2_197]` `[trigger: 日月照明格]` `[factor_trigger: pattern_riyue_zhaoming]` `[role: 条件分支]` 日月照明格为日月照明的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_198]` `[trigger: 日月正曜格]` `[factor_trigger: pattern_riyue_zhengyao]` `[role: 条件分支]` 日月正曜格为日月正曜的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_199]` `[trigger: 煞破贪廉格]` `[factor_trigger: pattern_sha_po_tan_lian]` `[role: 条件分支]` 煞破贪廉格为煞破与贪廉的凶险格局。 → 《骨髓赋》
  - `[ns_zwds_j2_200]` `[trigger: 善星守命格]` `[factor_trigger: pattern_shanxingshouming]` `[role: 条件分支]` 善星守命格为善星守命的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_201]` `[trigger: 煞破廉贞格]` `[factor_trigger: pattern_shapo_lianzhen]` `[role: 条件分支]` 煞破廉贞格为煞破与廉贞的凶险格局。 → 《骨髓赋》
  - `[ns_zwds_j2_202]` `[trigger: 石中隐玉格2]` `[factor_trigger: pattern_shijin_yinyu]` `[role: 条件分支]` 石中隐玉格为巨门午宫的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_203]` `[trigger: 双禄朝垣格2]` `[factor_trigger: pattern_shuanglu_chaoyuan]` `[role: 条件分支]` 双禄朝垣格为双禄朝垣的极贵格局。 → 《骨髓赋》
  - `[ns_zwds_j2_204]` `[trigger: 双禄守垣格]` `[factor_trigger: pattern_shuanglu_shouyuan]` `[role: 条件分支]` 双禄守垣格为双禄守垣的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_205]` `[trigger: 双禄左右格]` `[factor_trigger: pattern_shuangluzuoyou]` `[role: 条件分支]` 双禄左右格为双禄与左右的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_206]` `[trigger: 四酉金水白格]` `[factor_trigger: pattern_siyou_jinshuibai]` `[role: 条件分支]` 四酉金水白格为四酉金水白的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_207]` `[trigger: 四正无煞格]` `[factor_trigger: pattern_sizheng_wusha]` `[role: 条件分支]` 四正无煞格为四正宫无煞的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_208]` `[trigger: 随限注吉格]` `[factor_trigger: pattern_suixian_zhuji]` `[role: 条件分支]` 随限注吉格为随限注吉的配置。 → 《骨髓赋》
  - `[ns_zwds_j2_209]` `[trigger: 太辅导命格]` `[factor_trigger: pattern_taifu_daoming]` `[role: 条件分支]` 太辅导命格为太辅导命的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_210]` `[trigger: 太阳曲官禄格]` `[factor_trigger: pattern_taiyang_qu_guanlu]` `[role: 条件分支]` 太阳曲官禄格为太阳文曲在官禄的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_211]` `[trigger: 太阴昌气宫格]` `[factor_trigger: pattern_taiyin_chang_qigong]` `[role: 条件分支]` 太阴昌气宫格为太阴文昌的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_212]` `[trigger: 太阴天同子格]` `[factor_trigger: pattern_taiyintiantongzi]` `[role: 条件分支]` 太阴天同子格为太阴天同在子的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_213]` `[trigger: 贪狼遇权格]` `[factor_trigger: pattern_tanlang_yuquan]` `[role: 条件分支]` 贪狼遇权格为贪狼遇化权的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_214]` `[trigger: 天府武曲财帛格]` `[factor_trigger: pattern_tianfu_wuqu_caibo]` `[role: 条件分支]` 天府武曲财帛格为天府武曲在财帛的富格。 → 《骨髓赋》
  - `[ns_zwds_j2_215]` `[trigger: 天梁文曲台港格]` `[factor_trigger: pattern_tianliang_wenqu_taigang]` `[role: 条件分支]` 天梁文曲台港格为天梁文曲台港的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_216]` `[trigger: 天伤天刑格]` `[factor_trigger: pattern_tianshangtianxing]` `[role: 条件分支]` 天伤天刑格为天伤天刑的凶险格局。 → 《骨髓赋》
  - `[ns_zwds_j2_217]` `[trigger: 天使夹地格]` `[factor_trigger: pattern_tianshijiadi]` `[role: 条件分支]` 天使夹地格为天使夹地的凶险格局。 → 《骨髓赋》
  - `[ns_zwds_j2_218]` `[trigger: 天同机梁格]` `[factor_trigger: pattern_tiantongjiliang]` `[role: 条件分支]` 天同机梁格为天同机梁的格局。 → 《骨髓赋》
  - `[ns_zwds_j2_219]` `[trigger: 天相紫微格]` `[factor_trigger: pattern_tianxiang_ziwei]` `[role: 条件分支]` 天相紫微格为天相紫微的贵格。 → 《骨髓赋》
  - `[ns_zwds_j2_220]` `[trigger: 老守结果]` `[factor_trigger: result_laoshou]` `[role: 结果]` 老守结果为老守的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_221]` `[trigger: 老寿结果]` `[factor_trigger: result_laoshou2]` `[role: 结果]` 老寿结果为老寿的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_222]` `[trigger: 离祖结果]` `[factor_trigger: result_lizu]` `[role: 结果]` 离祖结果为离祖的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_223]` `[trigger: 良成结果]` `[factor_trigger: result_liangcheng]` `[role: 结果]` 良成结果为良成的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_224]` `[trigger: 六亲缘薄结果]` `[factor_trigger: result_liuqin_yuanbo]` `[role: 结果]` 六亲缘薄结果为六亲缘薄的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_225]` `[trigger: 龙池凤阁结果]` `[factor_trigger: result_longchi_fengge]` `[role: 结果]` 龙池凤阁结果为龙池凤阁的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_226]` `[trigger: 禄位结果]` `[factor_trigger: result_luwei]` `[role: 结果]` 禄位结果为禄位的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_227]` `[trigger: 妻财结果]` `[factor_trigger: result_qicai]` `[role: 结果]` 妻财结果为妻财的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_228]` `[trigger: 妻宜结果]` `[factor_trigger: result_qiyi]` `[role: 结果]` 妻宜结果为妻宜的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_229]` `[trigger: 权贵结果]` `[factor_trigger: result_quangui]` `[role: 结果]` 权贵结果为权贵的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_230]` `[trigger: 权威结果]` `[factor_trigger: result_quanwei]` `[role: 结果]` 权威结果为权威的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_231]` `[trigger: 仁德结果]` `[factor_trigger: result_rende]` `[role: 结果]` 仁德结果为仁德的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_232]` `[trigger: 荣显结果]` `[factor_trigger: result_rongxian]` `[role: 结果]` 荣显结果为荣显的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_233]` `[trigger: 三品结果]` `[factor_trigger: result_sanpin]` `[role: 结果]` 三品结果为三品的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_234]` `[trigger: 善终结果]` `[factor_trigger: result_shanzhong]` `[role: 结果]` 善终结果为善终的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_235]` `[trigger: 少年结果]` `[factor_trigger: result_shaonian]` `[role: 结果]` 少年结果为少年的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_236]` `[trigger: 身体健结果]` `[factor_trigger: result_shentijian]` `[role: 结果]` 身体健结果为身体健康的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_237]` `[trigger: 世禄结果]` `[factor_trigger: result_shilu]` `[role: 结果]` 世禄结果为世禄的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_238]` `[trigger: 仕途结果]` `[factor_trigger: result_shitu]` `[role: 结果]` 仕途结果为仕途的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_239]` `[trigger: 寿高结果]` `[factor_trigger: result_shougao]` `[role: 结果]` 寿高结果为寿高的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_240]` `[trigger: 寿终结果]` `[factor_trigger: result_shouzhong]` `[role: 结果]` 寿终结果为寿终的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_241]` `[trigger: 特达结果]` `[factor_trigger: result_teda]` `[role: 结果]` 特达结果为特达的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_242]` `[trigger: 天年结果]` `[factor_trigger: result_tiannian]` `[role: 结果]` 天年结果为天年的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_243]` `[trigger: 庭生结果]` `[factor_trigger: result_tingsheng]` `[role: 结果]` 庭生结果为庭生的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_244]` `[trigger: 卫禄结果]` `[factor_trigger: result_weilu]` `[role: 结果]` 卫禄结果为卫禄的判断。 → 《骨髓赋》
  - `[ns_zwds_j2_245]` `[trigger: 金石之梦象征]` `[factor_trigger: symbol_jinshi_zhimeng]` `[role: 主干]` 金石之梦象征为金石之梦的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_246]` `[trigger: 枯梅心怕象征]` `[factor_trigger: symbol_kumei_xinpa]` `[role: 主干]` 枯梅心怕象征为枯梅心怕的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_247]` `[trigger: 雷剑吐光芒象征]` `[factor_trigger: symbol_leijian_tuguangmang]` `[role: 主干]` 雷剑吐光芒象征为雷剑吐光芒的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_248]` `[trigger: 桃夭象征]` `[factor_trigger: symbol_taoyao]` `[role: 主干]` 桃夭象征为桃夭的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_249]` `[trigger: 天盘天添象征]` `[factor_trigger: symbol_tianpan_tiantian]` `[role: 主干]` 天盘天添象征为天盘天添的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_250]` `[trigger: 无福涉象征]` `[factor_trigger: symbol_wufu_she]` `[role: 主干]` 无福涉象征为无福涉的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_251]` `[trigger: 印带换金带象征]` `[factor_trigger: symbol_yindai_huanjindai]` `[role: 主干]` 印带换金带象征为印带换金带的象征。 → 《骨髓赋》
  - `[ns_zwds_j2_252]` `[trigger: 卦象系统]` `[factor_trigger: system_guaxiang]` `[role: 主干]` 卦象系统为卦象的系统。 → 《骨髓赋》
  - `[ns_zwds_j2_253]` `[trigger: 十二时所忌系统]` `[factor_trigger: system_shiershisuoji]` `[role: 主干]` 十二时所忌系统为十二时所忌的系统。 → 《骨髓赋》
  - `[ns_zwds_j2_254]` `[trigger: 申人铃星禁忌]` `[factor_trigger: taboo_shenrenlingxing]` `[role: 主干]` 申人铃星禁忌为申人铃星的禁忌。 → 《骨髓赋》
  - `[ns_zwds_j2_255]` `[trigger: 四生本申林禁忌]` `[factor_trigger: taboo_sisheng_benshenlin]` `[role: 主干]` 四生本申林禁忌为四生本申林的禁忌。 → 《骨髓赋》
  - `[ns_zwds_j2_256]` `[trigger: 酉人忌之禁忌]` `[factor_trigger: taboo_youren_jizhi]` `[role: 主干]` 酉人忌之禁忌为酉人忌之的禁忌。 → 《骨髓赋》
  - `[ns_zwds_j2_257]` `[trigger: 子生寅陷禁忌]` `[factor_trigger: taboo_zishengyinxian]` `[role: 主干]` 子生寅陷禁忌为子生寅陷的禁忌。 → 《骨髓赋》
  - `[ns_zwds_j2_258]` `[trigger: 天伤天使凶组合]` `[factor_trigger: tianshang_tianshi_malefic_combo]` `[role: 主干]` 天伤天使凶组合为天伤天使的凶险组合。 → 《骨髓赋》
  - `[ns_zwds_j2_259]` `[trigger: 天刑尊严状态]` `[factor_trigger: tianxing_dignity_state]` `[role: 主干]` 天刑尊严状态为天刑的尊严状态。 → 《骨髓赋》
  - `[ns_zwds_j2_260]` `[trigger: 天刑重组合]` `[factor_trigger: tianxing_heavy_combo]` `[role: 主干]` 天刑重组合为天刑的重组合。 → 《骨髓赋》
  - `[ns_zwds_j2_261]` `[trigger: 天姚吉组合]` `[factor_trigger: tianyao_benefic_combo]` `[role: 主干]` 天姚吉组合为天姚的吉组合。 → 《骨髓赋》
  - `[ns_zwds_j2_262]` `[trigger: 天姚凶组合]` `[factor_trigger: tianyao_malefic_combo]` `[role: 主干]` 天姚凶组合为天姚的凶组合。 → 《骨髓赋》
  - `[ns_zwds_j2_263]` `[trigger: 倒限时间]` `[factor_trigger: time_daoxian]` `[role: 主干]` 倒限时间为倒限的时间。 → 《骨髓赋》
  - `[ns_zwds_j2_264]` `[trigger: 二限时间]` `[factor_trigger: time_erxian]` `[role: 主干]` 二限时间为二限的时间。 → 《骨髓赋》
  - `[ns_zwds_j2_265]` `[trigger: 限运时间]` `[factor_trigger: time_limit]` `[role: 主干]` 限运时间为限运的时间。 → 《骨髓赋》
  - `[ns_zwds_j2_266]` `[trigger: 禄主甲酉时时间]` `[factor_trigger: time_luzhu_jia_youshi]` `[role: 主干]` 禄主甲酉时时间为禄主甲酉时的时间。 → 《骨髓赋》
  - `[ns_zwds_j2_267]` `[trigger: 童子老人时间]` `[factor_trigger: time_tongzi_laoren]` `[role: 主干]` 童子老人时间为童子老人的时间。 → 《骨髓赋》
  - `[ns_zwds_j2_268]` `[trigger: 戌巳生人时间]` `[factor_trigger: time_xusi_shengren]` `[role: 主干]` 戌巳生人时间为戌巳生人的时间。 → 《骨髓赋》
  - `[ns_zwds_j2_269]` `[trigger: 二十四极地时机]` `[factor_trigger: timing_24_jidi]` `[role: 主干]` 二十四极地时机为二十四极地的时机。 → 《骨髓赋》"""
    normalized_text_zh: str = """"""
    subject: str = "1 总论：格局与命限"
    factor_refs: list = ['engine_id', 'geju_cengci', 'ziwei_rule_engine', 'genji_zhuangtai', 'ziwei_calculator', 'heju_zhuangtai', 'ziwei_rule_engine', 'xianyun_peihe', 'ziwei_rule_engine', 'rongku_pinggu', 'ziwei_rule_engine', 'term_taiji', 'term_tianmen', 'geju_cengci', 'heju_zhuangtai', 'star_zhengyao', 'relation_duigong', 'relation_sanhe', 'source_ref', 'rel_gusui_001', 'geju_cengci', 'rel_gusui_002', 'heju_zhuangtai', 'rel_gusui_003', 'xianyun_peihe', 'evi_gusui_001', 'geju_cengci', 'rule_geju_xian', 'evi_gusui_002', 'rule_jiangu_xiangsheng', 'evi_gusui_003', 'xianyun_peihe', 'rule_xianyun_jueding', 'concept_pattern_frame', 'concept_foundation', 'concept_timing_fate']
    
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
        l1_anchor="zw_v1.0.0_1_总论_格局与命限_001_L1",
    )
    version: str = "1.0.0"
