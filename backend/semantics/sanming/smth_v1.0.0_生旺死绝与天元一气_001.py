"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264491
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
    semantic_id="smth_v1.0.0_生旺死绝与天元一气_001",
    book_id="sanming",
    engine_id="bazi"
)
class 生旺死绝与天元一气(SemanticEntry):
    """
    - **原文（source_text）**：
  凡命有五行旺相休囚死绝。如甲乙木，寅卯为旺，巳午为相，申酉为死，亥子为相（应为休？印生为相？古注以印为相），辰戌丑未为囚（土为财，耗气？古法旺相休囚与...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡命有五行旺相休囚死绝。如甲乙木，寅卯为旺，巳午为相，申酉为死，亥子为相（应为休？印生为相？古注以印为相），辰戌丑未为囚（土为财，耗气？古法旺相休囚与子平不同）。
  凡看命，要论天元一气。如庚辛见甲乙，是财。
  凡命中五行，如火多则土焦，水多则土流。
  凡看命，要论生旺死绝。如甲生亥月，为长生；生午月，为死地。

- **分字分词释义**：
  - **旺相休囚**：古法（四时）：当令者旺，生我者相（或我生者相？《白虎通》：母旺子相），我克者死，克我者囚，同类者旺（此段原文似有混淆，通常：同我旺，我生相，生我休，克我囚，我克死。或子平法：当令旺，我生相，生我休，克我死，我克囚）。
  - **土焦/土流**：五行太过之害。

- **白话原意**：
  看命要懂五行旺相休囚死绝。甲乙木在寅卯月最旺，巳午月（食伤）为相（次旺），申酉月（官煞）为死，亥子月（印）为休（或相），辰戌丑未月（财）为囚。
  看命要论天元一气（干支纯粹或一气格）。
  五行太过则病：火太多土会被烧焦（土焦），水太多土会被冲流（土流）。
  要看长生十二宫。如甲木生于亥月长生，生于午月死地。

- **核心要点**：
  - **旺衰**：四时旺相与十二宫。
  - **反生反克**：火多土焦，水多土流。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_shengwang_001]` `[trigger: 旺相休囚]` `[factor_trigger: wangxiang_xiuqiu AND sishi_wuxing]` `[role: 主干]` 凡命有五行旺相休囚死绝，如甲乙木，寅卯为旺，巳午为相。 → 《三命通会》卷十#生旺死绝
  - `[ns_smth_10_shengwang_002]` `[trigger: 土焦土流]` `[factor_trigger: tujiao_tuliu AND taiguo_bingji]` `[role: 主干依赖]` 凡命中五行，如火多则土焦，水多则土流。 → 《三命通会》卷十#生旺死绝
  - `[ns_smth_10_shengwang_003]` `[trigger: 天元一气]` `[factor_trigger: tianyuan_yiqi AND siganxiangtong]` `[role: 总结]` 凡看命，要论天元一气，如庚辛见甲乙是财。 → 《三命通会》卷十#生旺死绝
  - `[ns_smth_10_bingling]` `[trigger: 病临] [factor_trigger: bingling]` `[role: 十二运]` 病临者，临病之地。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_chengshu]` `[trigger: 成数] [factor_trigger: chengshu]` `[role: 数理]` 成数者，数之成。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_chong]` `[trigger: 冲] [factor_trigger: chong]` `[role: 地支]` 冲者，六冲之冲。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_dangshen_taisui]` `[trigger: 当神太岁] [factor_trigger: dangshen_taisui]` `[role: 神煞]` 当神太岁者，当年太岁。 → `《三命通会·卷十》#论太岁`
  - `[ns_smth_10_dayan_wushi]` `[trigger: 大衍五十] [factor_trigger: dayan_wushi]` `[role: 数理]` 大衍五十者，大衍之数。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_dayun]` `[trigger: 大运] [factor_trigger: dayun]` `[role: 运程]` 大运者，十年一运。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_dingren_wugui]` `[trigger: 丁壬戊癸] [factor_trigger: dingren_wugui]` `[role: 天干]` 丁壬戊癸者，干支配置。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_duhe]` `[trigger: 独合] [factor_trigger: duhe]` `[role: 地支]` 独合者，单独之合。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_ganhe]` `[trigger: 干合] [factor_trigger: ganhe]` `[role: 天干]` 干合者，天干相合。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_gaoge]` `[trigger: 高阁] [factor_trigger: gaoge]` `[role: 命理]` 高阁者，高阁之位。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_gengshen_jin]` `[trigger: 庚申金] [factor_trigger: gengshen_jin]` `[role: 干支]` 庚申金者，干支配金。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_geren]` `[trigger: 个人] [factor_trigger: geren]` `[role: 命理]` 个人者，个人之命。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_guanyin]` `[trigger: 官印] [factor_trigger: guanyin]` `[role: 十神]` 官印者，官与印绶。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_gudu]` `[trigger: 孤独] [factor_trigger: gudu]` `[role: 神煞]` 孤独者，孤辰寡宿。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_guishu]` `[trigger: 鬼数] [factor_trigger: guishu]` `[role: 数理]` 鬼数者，鬼之数。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_huagai]` `[trigger: 华盖] [factor_trigger: huagai]` `[role: 神煞]` 华盖者，华盖星。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_huaqi]` `[trigger: 化气] [factor_trigger: huaqi]` `[role: 五行]` 化气者，五行化气。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_hunlian]` `[trigger: 婚恋] [factor_trigger: hunlian]` `[role: 命理]` 婚恋者，婚姻恋爱。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_hunpoti]` `[trigger: 魂魄体] [factor_trigger: hunpoti]` `[role: 命理]` 魂魄体者，三命之体。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_huoduo]` `[trigger: 祸夺] [factor_trigger: huoduo]` `[role: 命理]` 祸夺者，祸害剥夺。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_jiaji]` `[trigger: 甲己] [factor_trigger: jiaji]` `[role: 天干]` 甲己者，甲己合土。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_jiangxing]` `[trigger: 将星] [factor_trigger: jiangxing]` `[role: 神煞]` 将星者，将星之贵。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_jiaru_jiaqu]` `[trigger: 嫁入嫁娶] [factor_trigger: jiaru_jiaqu]` `[role: 命理]` 嫁入嫁娶者，婚姻之事。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_jingshen]` `[trigger: 精神] [factor_trigger: jingshen]` `[role: 命理]` 精神者，神气精神。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_jinjiao_tuifu]` `[trigger: 进交退伏] [factor_trigger: jinjiao_tuifu]` `[role: 运程]` 进交退伏者，运之进退。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_liuhai]` `[trigger: 六害] [factor_trigger: liuhai]` `[role: 地支]` 六害者，地支六害。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_liuhe]` `[trigger: 六合] [factor_trigger: liuhe]` `[role: 地支]` 六合者，地支六合。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_liunian]` `[trigger: 流年] [factor_trigger: liunian]` `[role: 运程]` 流年者，每年太岁。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_liuqin]` `[trigger: 六亲] [factor_trigger: liuqin]` `[role: 命理]` 六亲者，父母兄弟妻子。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_liuyang]` `[trigger: 流阳] [factor_trigger: liuyang]` `[role: 阴阳]` 流阳者，阳之流。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_liuyin]` `[trigger: 流阴] [factor_trigger: liuyin]` `[role: 阴阳]` 流阴者，阴之流。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_lvlv]` `[trigger: 律吕] [factor_trigger: lvlv]` `[role: 律吕]` 律吕者，十二律吕。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_meili]` `[trigger: 魅力] [factor_trigger: meili]` `[role: 命理]` 魅力者，个人魅力。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_muyu_wei]` `[trigger: 沐浴位] [factor_trigger: muyu_wei]` `[role: 十二运]` 沐浴位者，沐浴之位。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_nan_shun]` `[trigger: 男顺] [factor_trigger: nan_shun]` `[role: 阴阳]` 男顺者，男命顺行。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_nian_nei]` `[trigger: 年内] [factor_trigger: nian_nei]` `[role: 命理]` 年内者，一年之内。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_nv_ershi]` `[trigger: 女二十] [factor_trigger: nv_ershi]` `[role: 命理]` 女二十者，女命二十岁。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_nv_ni]` `[trigger: 女逆] [factor_trigger: nv_ni]` `[role: 阴阳]` 女逆者，女命逆行。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_pocai_anmei]` `[trigger: 破财暗昧] [factor_trigger: pocai_anmei]` `[role: 命理]` 破财暗昧者，暗中破财。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_renyi]` `[trigger: 仁义] [factor_trigger: renyi]` `[role: 命理]` 仁义者，仁义之德。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_ri_fan_sui]` `[trigger: 日犯岁] [factor_trigger: ri_fan_sui]` `[role: 神煞]` 日犯岁者，日干犯太岁。 → `《三命通会·卷十》#论太岁`
  - `[ns_smth_10_sanhe]` `[trigger: 三合] [factor_trigger: sanhe]` `[role: 地支]` 三合者，地支三合。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_sanhe_ku]` `[trigger: 三合库] [factor_trigger: sanhe_ku]` `[role: 地支]` 三合库者，三合之库。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_sanhe_zhong]` `[trigger: 三合中] [factor_trigger: sanhe_zhong]` `[role: 地支]` 三合中者，三合之中。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_sanshi_ershi]` `[trigger: 三十二十] [factor_trigger: sanshi_ershi]` `[role: 数理]` 三十二十者，岁数之论。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_sanxing]` `[trigger: 三刑] [factor_trigger: sanxing]` `[role: 地支]` 三刑者，地支三刑。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_sexiang]` `[trigger: 色象] [factor_trigger: sexiang]` `[role: 命理]` 色象者，五行之色。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_sheng_wang_ku]` `[trigger: 生旺库] [factor_trigger: sheng_wang_ku]` `[role: 十二运]` 生旺库者，长生帝旺墓库。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_shengcheng]` `[trigger: 生成] [factor_trigger: shengcheng]` `[role: 数理]` 生成者，生成之数。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_shengshu]` `[trigger: 生数] [factor_trigger: shengshu]` `[role: 数理]` 生数者，数之生。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_shengzhu]` `[trigger: 生助] [factor_trigger: shengzhu]` `[role: 五行]` 生助者，生扶之助。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_shijia]` `[trigger: 时家] [factor_trigger: shijia]` `[role: 命理]` 时家者，时柱之家。 → `《三命通会·卷十》#起小运法`
  - `[ns_smth_10_sijuju]` `[trigger: 四局聚] [factor_trigger: sijuju]` `[role: 命理]` 四局聚者，四柱汇聚。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_sui_shang_ri]` `[trigger: 岁上日] [factor_trigger: sui_shang_ri]` `[role: 神煞]` 岁上日者，太岁与日干。 → `《三命通会·卷十》#论太岁`
  - `[ns_smth_10_suiyun]` `[trigger: 岁运] [factor_trigger: suiyun]` `[role: 运程]` 岁运者，流年与大运。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_taisui]` `[trigger: 太岁] [factor_trigger: taisui]` `[role: 神煞]` 太岁者，流年太岁。 → `《三命通会·卷十》#论太岁`
  - `[ns_smth_10_tanhe]` `[trigger: 贪合] [factor_trigger: tanhe]` `[role: 命理]` 贪合者，贪合忘冲。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_tianyuan]` `[trigger: 天元] [factor_trigger: tianyuan]` `[role: 天干]` 天元者，天干之元。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_tonglong]` `[trigger: 通龙] [factor_trigger: tonglong]` `[role: 命理]` 通龙者，通达之龙。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_tongxian]` `[trigger: 通仙] [factor_trigger: tongxian]` `[role: 命理]` 通仙者，通达之仙。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_tujiao]` `[trigger: 土焦] [factor_trigger: tujiao]` `[role: 五行]` 土焦者，火多土焦。 → `《三命通会·卷十》#生旺死绝`
  - `[ns_smth_10_tuju]` `[trigger: 土局] [factor_trigger: tuju]` `[role: 五行]` 土局者，土之局。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_wangxiang]` `[trigger: 旺相] [factor_trigger: wangxiang]` `[role: 十二运]` 旺相者，当令之旺。 → `《三命通会·卷十》#生旺死绝`
  - `[ns_smth_10_wannian]` `[trigger: 万年] [factor_trigger: wannian]` `[role: 命理]` 万年者，万年历。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_wuen_shishi]` `[trigger: 无恩失势] [factor_trigger: wuen_shishi]` `[role: 命理]` 无恩失势者，失势无恩。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_wufang]` `[trigger: 五方] [factor_trigger: wufang]` `[role: 方位]` 五方者，东西南北中。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_wuhe]` `[trigger: 五合] [factor_trigger: wuhe]` `[role: 天干]` 五合者，天干五合。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_wuli_zixing]` `[trigger: 物理自行] [factor_trigger: wuli_zixing]` `[role: 命理]` 物理自行者，物之自行。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_wuxing_ju]` `[trigger: 五行局] [factor_trigger: wuxing_ju]` `[role: 五行]` 五行局者，五行之局。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_xianchi]` `[trigger: 咸池] [factor_trigger: xianchi]` `[role: 神煞]` 咸池者，咸池桃花。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_xiaoyun]` `[trigger: 小运] [factor_trigger: xiaoyun]` `[role: 运程]` 小运者，一年一运。 → `《三命通会·卷十》#起小运法`
  - `[ns_smth_10_xiaoyun_qidian]` `[trigger: 小运起点] [factor_trigger: xiaoyun_qidian]` `[role: 运程]` 小运起点者，小运之起。 → `《三命通会·卷十》#起小运法`
  - `[ns_smth_10_xing]` `[trigger: 刑] [factor_trigger: xing]` `[role: 地支]` 刑者，地支相刑。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_xingnian]` `[trigger: 行年] [factor_trigger: xingnian]` `[role: 运程]` 行年者，行运之年。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_xiong_fan_ji]` `[trigger: 凶犯忌] [factor_trigger: xiong_fan_ji]` `[role: 命理]` 凶犯忌者，凶之犯忌。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_yang_qi]` `[trigger: 阳气] [factor_trigger: yang_qi]` `[role: 阴阳]` 阳气者，阳之气。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_yanggan]` `[trigger: 阳干] [factor_trigger: yanggan]` `[role: 天干]` 阳干者，甲丙戊庚壬。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_yangshu]` `[trigger: 阳数] [factor_trigger: yangshu]` `[role: 数理]` 阳数者，奇数。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_yigeng]` `[trigger: 乙庚] [factor_trigger: yigeng]` `[role: 天干]` 乙庚者，乙庚合金。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_yin_ou]` `[trigger: 阴偶] [factor_trigger: yin_ou]` `[role: 阴阳]` 阴偶者，偶数。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_yin_shen]` `[trigger: 寅申] [factor_trigger: yin_shen]` `[role: 地支]` 寅申者，寅申相冲。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_yingan]` `[trigger: 阴干] [factor_trigger: yingan]` `[role: 天干]` 阴干者，乙丁己辛癸。 → `《三命通会·卷十》#起大运法`
  - `[ns_smth_10_yinyang_deling]` `[trigger: 阴阳得令] [factor_trigger: yinyang_deling]` `[role: 阴阳]` 阴阳得令者，得时令。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_yiqi]` `[trigger: 一气] [factor_trigger: yiqi]` `[role: 五行]` 一气者，一行纯粹。 → `《三命通会·卷十》#论大运`
  - `[ns_smth_10_youxing_taisui]` `[trigger: 有刑太岁] [factor_trigger: youxing_taisui]` `[role: 神煞]` 有刑太岁者，刑犯太岁。 → `《三命通会·卷十》#论太岁`
  - `[ns_smth_10_zhengke]` `[trigger: 正克] [factor_trigger: zhengke]` `[role: 五行]` 正克者，五行正克。 → `《三命通会·卷十》#论流年`
  - `[ns_smth_10_zhongzheng]` `[trigger: 中正] [factor_trigger: zhongzheng]` `[role: 命理]` 中正者，中和之正。 → `《三命通会·卷十》#论行运`
  - `[ns_smth_10_zhouye]` `[trigger: 昼夜] [factor_trigger: zhouye]` `[role: 阴阳]` 昼夜者，阴阳之分。 → `《三命通会·卷十》#起大运法`"""
    normalized_text_zh: str = """"""
    subject: str = "生旺死绝与天元一气"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_生旺死绝与天元一气_001_L1",
    )
    version: str = "1.0.0"
