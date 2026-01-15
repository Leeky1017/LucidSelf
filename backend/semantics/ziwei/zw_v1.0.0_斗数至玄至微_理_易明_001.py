"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725348
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
    semantic_id="zw_v1.0.0_斗数至玄至微_理_易明_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 斗数至玄至微理易明(SemanticEntry):
    """
    - 原文（source_text）：

  斗数至玄至微，理𣥜易明。虽设问于百篇之中，犹有言而未尽。至如星之分野，各有所属，寿夭贤愚、富贵贫贱，不可一概论议。其星分布千十二垣，数定乎三十六位，入庙为奇...
    """
    
    original_text: str = """- 原文（source_text）：

  斗数至玄至微，理𣥜易明。虽设问于百篇之中，犹有言而未尽。至如星之分野，各有所属，寿夭贤愚、富贵贫贱，不可一概论议。其星分布千十二垣，数定乎三十六位，入庙为奇，失度为虚。大抵以身命为福德之本，加以根源为穷通之资。星有同缠，数有分定，须明其生克之要，必详乎得垣失度之分。观乎紫微舍缠，司一天仪之象，卒列宿而成垣。土星苟居其垣，若可动移；金星专司财库，最怕空亡。帝居动，则列宿奔驰；贪守空，而财源不聚。各司其职，不可参差。苟或不察其机，更忘其变，则数之造化远矣。例曰：禄逢冲破，吉处藏凶；马遇空亡，终身奔走。生逢败地，发也虚花；绝处逢生，花而不败。星临庙旺，再观生克之机；命坐强宫，细察制化之理。日月最嫌反背，禄马最喜交驰，倘居空亡，得失最为要紧；若逢败地扶持，大有奇功。紫微天府，全依辅弼之功；七杀破军，专依羊铃之虐。诸星吉，逢凶也吉；诸星凶，逢吉也凶。辅弼夹帝为上品，桃花犯主为至淫。君臣庆会，材擅经邦；魁钺同行，位居台辅。禄文拱命，贵而且贤；日月夹财，不权则富。马头带箭，镇卫边疆；刑囚夹印，刑杖惟司。善荫朝纲，仁慈之长。贵入贵乡，逢者富贵；财居财位，遇者富奢。太阳居午，谓之日丽中天，有专榷之贵，敌国之富。太阴居子，号曰水澄桂萼，得清要之职，忠谏之材。紫微辅弼同宫，一呼百诺，居上品。文耗居寅卯，谓之众水朝东。日月守不如照合，荫福聚，不怕凶危。贪居亥子，名为泛水桃花；刑遇贪狼，号曰风流彩杖。七杀廉贞同位，路上埋尸；破军暗𬺟同乡，水中作冢。禄居奴仆，纵有官也奔驰；帝遇凶徒，虽获吉而无道。帝坐金车，则曰金𬛼捧节；福安文曜，谓之玉袖天香。太阳会文昌于官禄，皇殿朝班，富贵全美；太阴会文曲于妻宫，蟾宫折桂，文章令盛。禄存守于田财，堆金积玉；财荫坐于迁移，巨啇高贾。耗居禄位，沿途乞食；贪会旺宫，终身用窃。杀居绝地，天年夭似颜回；贪坐生乡，寿考永如彭祖。忌暗同居身命，疾厄沉困、弱羸。凶星会于父母、迁移，刑伤产室；刑杀同廉贞于官禄，枷杽难逃；官府加刑杀于迁移，离乡遭配。善福守于空位，天竺生涯；辅弼单守命宫，离宗庶出。七杀临于身命，加恶杀，必定死亡。羊铃合于命宫，遇白虎须当刑戮。官府发于吉曜，流杀怕逢破军；羊铃凭太岁以引行。病符、官符皆作祸；奏书、博士与流禄尽作吉祥。力士、将军同青龙，显其权势。童子限如水上泡沫，老人限似风中燃烛。遇杀与擎羊，流年最忌。人生荣辱，限元必有休咎；处世孤贫，数位定逢驳杂。学者至此，诚玄微矣。

- 原注（原文注解，可无则省略小节）：

  （本节为《太微赋》总纲，自成一体。原书于此未见另列小注，传统注家多在后文诸论中层层发挥，故本条不单独录原注，仅在“详细解说”中吸收要义。）

- 分字分词释义：

  - **斗数**：紫微斗数之略称，以北斗诸星及南北斗体系为骨干，参合诸吉凶星曜、十二宫垣与四化等，以推人之寿夭贤愚、富贵贫贱。
  - **至玄至微**：极其玄妙而入微，既指其理深难尽，又指观察粒度极细，非粗略分类可替代。
  - **理𣥜易明**：道理虽深邃幽远，但若掌握纲领与结构，反而容易理解与运用。“𣥜”与“邃”同义。
  - **星之分野，各有所属**：每一颗星曜都有其司掌领域与应验范围，既有天文上的分野，也有人事、地域、宫位上的分工。
  - **千十二垣、三十六位**：指诸星分布于十二宫垣、三方四正以及细分度数之位，强调“星在何处”与“何等格局”是判断的基础。
  - **入庙为奇，失度为虚**：“入庙”指星在本垣、本气、本旺之地，力量纯正；“失度”指超出本位、失去根气，多虚多耗。
  - **身命为福德之本**：命宫、身宫是全局之根本，决定人之格局、承载力与福德容量。
  - **根源为穷通之资**：禄存、禄地、根气等，为人一生穷通起伏的“资本”，有根则能承受变化，无根则难以长久。
  - **辅弼、魁钺、禄文**：左辅、右弼、天魁、天钺、禄存及化禄、文昌、文曲等吉曜，象征贵人、科名与爵禄。
  - **桃花犯主**：桃花星曜冲犯命主、身主或重要宫位，多为情欲放纵、声名污点之象。
  - **禄逢冲破、马遇空亡**：禄星遭冲破，表面有禄而实多波折；天马落空亡，一生奔波劳碌。
  - **童子限如水上泡沫，老人限似风中燃烛**：以比喻形容幼年与老年限运的脆弱易碎，遇凶则应祸较重。

- 规范化释义（primary_lang_explained）：

  紫微斗数的道理极其深妙细致，但若把握住核心架构，反而并不难懂。诸星各有分工与分野，分布在十二宫垣和三十六位上：落在本垣本位为“入庙”，力量强而有用；超出本位则为“失度”，多虚弱无力。命宫、身宫是一个人福德祸福的根本，禄存等“根气”则是穷通起伏的资本。

  论命时，必须通晓星曜之间的生克制化、得垣失度与同宫夹拱之关系。文中举出许多典型结构：禄星逢冲破，则吉中藏凶；天马落空亡，则多奔波劳禄；绝处逢生，则在险地反得转机。紫微天府要倚靠辅弼方成上品之贵，七杀破军则仗羊铃等杀曜之威；吉星遇凶星，能够化凶为用，凶星遇吉星，却未必就能真正成吉。又以辅弼夹帝、桃花犯主、日月夹财、马头带箭、刑囚夹印等组合，分别象征经邦之才、极端淫奔、权贵富厚、镇守边疆、主刑杖之职等。

  段末提及流年、大限与各类煞曜：童限、老人限如泡沫与残烛，遇恶星则易有灾祸；病符、官符为祸端，奏书、博士、流禄为吉象。总之，人生荣辱、贫富孤盛，皆系于命身之根基与限运之往来，学者若能从此总纲入手，再细玩后文诸论，方能窥见斗数之玄微。

- 完整对等诠释（secondary_lang_full）：

  Ziwei Doushu is presented here as a system that looks extremely arcane and subtle, yet becomes workable once its skeleton is understood. Stars are not judged in isolation but through their allocation across twelve palaces and thirty‑six key positions. When a star occupies its own dignified seat, its power is solid and effective; when it drifts away from its proper degree and loses root‑qi, its influence becomes hollow and easily wasted. The Life Palace and Body Palace act as the core containers of blessing and misfortune, while Lu‑cun‑type salary and root stars provide the underlying capital that supports rise and decline throughout a lifetime.

  The passage insists that chart reading must begin from overall pattern rather than from single stars. One has to understand how stars generate and control one another, whether they are in temple or out of bounds, and how they cluster, flank or oppose within and across palaces. Classic structural motifs such as “salary star broken by assault”, “travelling horse falling into void”, “assistants flanking the emperor”, “peach‑blossom violating the ruler”, “prisoner stars flanking the seal” or “horse‑head carrying arrows” describe recurring combinations that shape specific types of character, vocation and risk. The same birth year, month, day and hour can therefore lead to very different outcomes in wealth, status and longevity, because the underlying configuration, the strength of the root and the timing cycles interact differently.

  At the end, the text brings in major and minor periods, annual influences and a variety of malefic and benefic indicators. Childhood and old‑age periods are likened to foam on water and a candle in the wind, easily disturbed when heavy afflictions strike; symbols such as “illness talisman” or “lawsuit talisman” warn of concrete worldly troubles, while scholarly and salary stars mark opportunities for support. Altogether, this opening chapter establishes a meta‑rule: to judge a life one must take Life and Body palaces as the root, evaluate which stars are in dignity or fallen, and then see how auspicious and inauspicious configurations are activated or suppressed by unfolding time.

- 核心要点：

  - 紫微斗数以 **星垣格局** 为骨干：星曜必须连同宫位、旺陷、组合一起看，不能只念星名。
  - 命宫、身宫与禄存等根气，是判断福德容量与穷通起伏的根本，先定“能承多少”，再谈吉凶。
  - 吉星不必尽吉、凶星不必尽凶：看其所处之地、所会之星，决定“吉中藏凶”或“凶中藏吉”。
  - 大运、流年只是激发本命结构的“时间开关”，须回到本段所述之总纲来统筹判断。

- 详细解说：

  1. **从星分野到宫垣结构**：

     “星之分野，各有所属，寿夭贤愚、富贵贫贱，不可一概论议”，说明斗数并非用少数标签将人生粗暴分类，而是以星曜 + 宫位 + 组合来建立细致的分野系统。十二宫垣与三十六位，为这种精细划分提供空间维度；不同宫垣、不同度位，星性之吉凶、轻重、侧重各异。

  2. **命身与根气的层级**：

     文字中将“身命”与“根源”分列：身命为“福德之本”，是整体格局与人格承载；根源为“穷通之资”，是资源与机会的底盘。这样一来，同样见贵、见财之局，落在不同身命与根源上，其实际所能承受与维持的程度完全不同。

  3. **结构化的典型组合**：

     本段浓缩了大量后来斗数命例中常见的组合模板，如“禄逢冲破”“马遇空亡”“辅弼夹帝”“桃花犯主”“刑囚夹印”“马头带箭”等，既可以作为记忆口诀，也可视作之后规则化时的条件原型：

     - 条件：某星 + 某宫 + 某种夹拱/冲合关系；
     - 结果：对应某种性情、职业、祸福倾向。

     在本卷精校阶段，我们仅在解说中指出其结构含义，后续再在 L2/L3 中细化为可编译的规则。

  4. **时间维度：限运与流年**：

     “童子限如水上泡沫，老人限似风中燃烛”提醒我们：命理的时间维度并不均匀——幼年与老年时期更易受凶星冲击，且同一凶象在不同阶段的后果不同。再加上太岁、流杀、病符、官符等动星，构成“本命结构 + 时间开关”的二元系统。

- 校勘与字词辨析：

  - “理𣥜易明”诸本或作“理邃易明”，“𣥜/邃”古可通用，本稿据当前底本保留“𣥜”。
  - “千十二垣”疑为“千”字之讹，或为“兼”“共”等字之俗写，用意在指“诸星分布于十二宫垣”，本稿暂依原文录入，在详细解说中加以说明，并在后续整理版本时视多种底本再议。
  - “金𬛼捧节”诸本有作“金舆”“金辂”等，皆指华贵车舆与持节之象，本稿据底本录“𬛼”，在白话与解说中以意译说明其为“贵重车舆、持节出入”之意，不另改字。
  - 文中若干冷僻或异体字（如“𬺟”等），本稿统一 **保持底本原字**，并在释义中用现代汉语解释，以兼顾学术严谨与现代可读性。

- 叙事素材（narrative_snippets）：

  - **总纲定位**："斗数至玄至微，理邃易明"是《太微赋》的开篇总纲，为紫微斗数建立了"看似神秘，实则可循"的方法论基调。
  - **传统叙事**："入庙为奇，失度为虚"，形容星曜在庙旺之地力量纯正，失度落陷则多虚多耗，是判断星曜吉凶的首要法则。
  - **吉凶互藏**："禄逢冲破，吉处藏凶；马遇空亡，终身奔走。"此句为吉凶互藏的经典警示，提醒表面吉象未必真吉，需看冲破与空亡情况。
  - **格局模式**："紫微天府，全依辅弼之功；七杀破军，专依羊铃之虐。"说明帝星需吉曜辅助方成上品，孤克之星需煞曜加持方显其威。
  - **限运脆弱期**："童子限如水上泡沫，老人限似风中燃烛"，以生动比喻形容幼年与老年限运的脆弱性，遇凶则应祸较重。
  - **现代应用**：本条总纲可作为紫微斗数解盘的"元规则"——先定命身承载力，再看星曜庙陷，三察吉凶组合，四观限运激发，如此方能避免片面断语。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j1_008]` `[trigger: 天府尊星]` `[factor_trigger: star_tianfu]` `[role: 主干]` 天府令星，南斗主星，司财帛田宅，主富厚稳重。 → 《太微赋》总纲
  - `[ns_zwds_j1_009]` `[trigger: 七杀凶星]` `[factor_trigger: star_qisha]` `[role: 主干]` 七杀为将星，主孤克刚勇，需制化方能成用。 → 《太微赋》"七杀破军，专依羊铃之虐"
  - `[ns_zwds_j1_010]` `[trigger: 破军耗星]` `[factor_trigger: star_pojun]` `[role: 主干]` 破军为耗星，主破旧立新，先破后成。 → 《太微赋》"七杀破军，专依羊铃之虐"
  - `[ns_zwds_j1_011]` `[trigger: 擎羊刑星]` `[factor_trigger: star_qingyang]` `[role: 主干]` 擎羊为刑星，主刑伤是非，性刚暴烈。 → 《太微赋》"羊铃之虐"
  - `[ns_zwds_j1_012]` `[trigger: 火星煞曜]` `[factor_trigger: star_huoxing]` `[role: 主干]` 火星为煞曜，主急躁暴烈，加会命身主性急。 → 《太微赋》"能制火铃为善"
  - `[ns_zwds_j1_013]` `[trigger: 铃星煞曜]` `[factor_trigger: star_lingxing]` `[role: 主干]` 铃星为煞曜，主阴火暗伤，性情偏激。 → 《太微赋》"能制火铃为善"
  - `[ns_zwds_j1_014]` `[trigger: 天马动星]` `[factor_trigger: star_tianma]` `[role: 主干]` 天马为驿马，主奔波驰骋，逢空亡则终身奔走。 → 《太微赋》"马遇空亡，终身奔走"
  - `[ns_zwds_j1_015]` `[trigger: 天魁贵星]` `[factor_trigger: star_tiankui]` `[role: 主干]` 天魁为阳贵，主贵人扶持，昼生得力。 → 《太微赋》"魁钺同行，位居台辅"
  - `[ns_zwds_j1_016]` `[trigger: 天钺贵星]` `[factor_trigger: star_tianyue]` `[role: 主干]` 天钺为阴贵，主贵人暗助，夜生得力。 → 《太微赋》"魁钺同行，位居台辅"
  - `[ns_zwds_j1_017]` `[trigger: 文昌科星]` `[factor_trigger: star_wenchang]` `[role: 主干]` 文昌为科甲星，主聪明好学，利考试功名。 → 《太微赋》"禄文拱命，贵而且贤"
  - `[ns_zwds_j1_018]` `[trigger: 文曲才星]` `[factor_trigger: star_wenqu]` `[role: 主干]` 文曲为才艺星，主口才艺术，性多浮华。 → 《太微赋》"禄文拱命"
  - `[ns_zwds_j1_019]` `[trigger: 太阳日星]` `[factor_trigger: star_taiyang]` `[role: 主干]` 太阳为日星，主光明正大，利男命及父星。 → 《太微赋》"日月最嫌反背"
  - `[ns_zwds_j1_020]` `[trigger: 太阴月星]` `[factor_trigger: star_taiyin]` `[role: 主干]` 太阴为月星，主清秀柔和，利女命及母星。 → 《太微赋》"日月最嫌反背"
  - `[ns_zwds_j1_021]` `[trigger: 廉贞次桃花]` `[factor_trigger: star_lianzhen]` `[role: 主干]` 廉贞为次桃花，主感情复杂，囚星之性。 → 《太微赋》"刑囚夹印"
  - `[ns_zwds_j1_022]` `[trigger: 贪狼桃花]` `[factor_trigger: star_tanlang]` `[role: 主干]` 贪狼为正桃花，主欲望才艺，善恶两极。 → 《太微赋》"贪守空，而财源不聚"
  - `[ns_zwds_j1_023]` `[trigger: 巨门暗星]` `[factor_trigger: star_jumen]` `[role: 主干]` 巨门为暗星，主口舌是非，化气为暗。 → 《太微赋》
  - `[ns_zwds_j1_024]` `[trigger: 天机智星]` `[factor_trigger: star_tianji]` `[role: 主干]` 天机为智星，主机变聪敏，善谋略计划。 → 《太微赋》
  - `[ns_zwds_j1_025]` `[trigger: 天同福星]` `[factor_trigger: star_tiantong]` `[role: 主干]` 天同为福星，主福寿安乐，性情温和。 → 《太微赋》
  - `[ns_zwds_j1_026]` `[trigger: 武曲财星]` `[factor_trigger: star_wuqu]` `[role: 主干]` 武曲为财星，主刚毅果决，利武职财经。 → 《太微赋》
  - `[ns_zwds_j1_027]` `[trigger: 天相印星]` `[factor_trigger: star_tianxiang]` `[role: 主干]` 天相为印星，主端庄稳重，利文书印信。 → 《太微赋》"刑囚夹印"
  - `[ns_zwds_j1_028]` `[trigger: 天梁荫星]` `[factor_trigger: star_tianliang]` `[role: 主干]` 天梁为荫星，主清高孤傲，化气为荫。 → 《太微赋》"善荫朝纲，仁慈之长"
  - `[ns_zwds_j1_029]` `[trigger: 陀罗暗耗]` `[factor_trigger: star_tuoluo]` `[role: 主干]` 陀罗为暗耗，主拖延纠缠，暗中消耗。 → 《太微赋》"羊铃之虐"
  - `[ns_zwds_j1_030]` `[trigger: 地空劫星]` `[factor_trigger: star_dikong]` `[role: 主干]` 地空为劫星，主空亡虚耗，精神层面。 → 《太微赋》"最怕空亡"
  - `[ns_zwds_j1_031]` `[trigger: 地劫劫星]` `[factor_trigger: star_dijie]` `[role: 主干]` 地劫为劫星，主破败损失，物质层面。 → 《太微赋》"最怕空亡"
  - `[ns_zwds_j1_032]` `[trigger: 兄弟宫位]` `[factor_trigger: palace_siblings]` `[role: 主干]` 兄弟宫主兄弟姐妹及平辈关系。 → 《太微赋》十二宫
  - `[ns_zwds_j1_033]` `[trigger: 夫妻宫位]` `[factor_trigger: palace_spouse]` `[role: 主干]` 夫妻宫主配偶及婚姻关系。 → 《太微赋》十二宫
  - `[ns_zwds_j1_034]` `[trigger: 子女宫位]` `[factor_trigger: palace_children]` `[role: 主干]` 子女宫主子女及后代关系。 → 《太微赋》十二宫
  - `[ns_zwds_j1_035]` `[trigger: 财帛宫位]` `[factor_trigger: palace_wealth]` `[role: 主干]` 财帛宫主财运及理财能力。 → 《太微赋》十二宫
  - `[ns_zwds_j1_036]` `[trigger: 疾厄宫位]` `[factor_trigger: palace_health]` `[role: 主干]` 疾厄宫主健康及疾病状况。 → 《太微赋》十二宫
  - `[ns_zwds_j1_037]` `[trigger: 迁移宫位]` `[factor_trigger: palace_travel]` `[role: 主干]` 迁移宫主外出及社会活动。 → 《太微赋》十二宫
  - `[ns_zwds_j1_038]` `[trigger: 奴仆宫位]` `[factor_trigger: palace_servants]` `[role: 主干]` 奴仆宫主下属及朋友关系。 → 《太微赋》十二宫
  - `[ns_zwds_j1_039]` `[trigger: 官禄宫位]` `[factor_trigger: palace_career]` `[role: 主干]` 官禄宫主事业及社会地位。 → 《太微赋》十二宫
  - `[ns_zwds_j1_040]` `[trigger: 田宅宫位]` `[factor_trigger: palace_property]` `[role: 主干]` 田宅宫主不动产及家庭环境。 → 《太微赋》十二宫
  - `[ns_zwds_j1_041]` `[trigger: 福德宫位]` `[factor_trigger: palace_fortune]` `[role: 主干]` 福德宫主精神享受及福气。 → 《太微赋》十二宫
  - `[ns_zwds_j1_042]` `[trigger: 父母宫位]` `[factor_trigger: palace_parents]` `[role: 主干]` 父母宫主父母及长辈关系。 → 《太微赋》十二宫
  - `[ns_zwds_j1_043]` `[trigger: 庙旺状态]` `[factor_trigger: state_miaowang]` `[role: 主干]` 星曜在庙旺之地，力量纯正，吉象易发挥。 → 《太微赋》"入庙为奇"
  - `[ns_zwds_j1_044]` `[trigger: 六煞星群]` `[factor_trigger: group_liusha]` `[role: 主干]` 六煞为擎羊、陀罗、火星、铃星、地空、地劫，主凶险损耗。 → 《太微赋》
  - `[ns_zwds_j1_045]` `[trigger: 吉星群]` `[factor_trigger: group_jixing]` `[role: 主干]` 吉星群包括左辅右弼、天魁天钺、文昌文曲、禄存化禄等。 → 《太微赋》
  - `[ns_zwds_j1_155]` `[trigger: 左辅吉星]` `[factor_trigger: star_zuofu]` `[role: 主干]` 左辅为吉星，主助力扶持，加会命身主得人相助。 → 《安左辅右弼星诀》
  - `[ns_zwds_j1_156]` `[trigger: 天上天空]` `[factor_trigger: star_tianshangtian kong]` `[role: 主干]` 天上天空为空亡之星，主虚耗减损，凶象。 → 《郦生之命》
  - `[ns_zwds_j1_157]` `[trigger: 羊陀叠并]` `[factor_trigger: pattern_yangtuodiebing]` `[role: 主干]` 羊陀叠并为擎羊陀罗交加重叠，主凶象凶亡。 → 《韩通之命》
  - `[ns_zwds_j1_158]` `[trigger: 府相科禄]` `[factor_trigger: pattern_fuxiangkelu]` `[role: 主干]` 府相科禄为天府天相配科禄，主富贵。 → 《宋璟之命》
  - `[ns_zwds_j1_159]` `[trigger: 劫空在命]` `[factor_trigger: pattern_jiekongzaiming]` `[role: 条件分支]` 劫空在命为地劫地空在命宫，主手段孙。 → 《宋璟之命》
  - `[ns_zwds_j1_160]` `[trigger: 七杀羊陀冲]` `[factor_trigger: pattern_qishayangtuochong]` `[role: 条件分支]` 七杀羊陀冲为七杀擎羊陀罗相冲，主伤寿。 → 《宋璟之命》
  - `[ns_zwds_j1_161]` `[trigger: 文星暗拱]` `[factor_trigger: pattern_wenxinganggong]` `[role: 条件分支]` 文星暗拱为文昌文曲暗合拱照，主科名。 → 《贾谊之命》
  - `[ns_zwds_j1_162]` `[trigger: 登科结果]` `[factor_trigger: result_dengke]` `[role: 结果]` 登科结果为考试中第、科名有成。 → 《贾谊之命》
  - `[ns_zwds_j1_163]` `[trigger: 四墓星群]` `[factor_trigger: group_simu]` `[role: 主干]` 四墓星群为辰戌丑未四库之星。 → 《紫微斗数全书》
  - `[ns_zwds_j1_164]` `[trigger: 四墓地]` `[factor_trigger: group_simudi]` `[role: 主干]` 四墓地为辰戌丑未四库之地。 → 《紫微斗数全书》
  - `[ns_zwds_j1_165]` `[trigger: 四煞空劫]` `[factor_trigger: group_sishakongjie]` `[role: 主干]` 四煞空劫为火铃羊陀加地空地劫。 → 《紫微斗数全书》
  - `[ns_zwds_j1_166]` `[trigger: 四余]` `[factor_trigger: group_siyu]` `[role: 主干]` 四余为紫气月孛罗计四余星。 → 《紫微斗数全书》
  - `[ns_zwds_j1_167]` `[trigger: 四正]` `[factor_trigger: group_sizheng]` `[role: 主干]` 四正为子午卯酉四正方位。 → 《紫微斗数全书》
  - `[ns_zwds_j1_168]` `[trigger: 所值吉星]` `[factor_trigger: group_suozhijixing]` `[role: 主干]` 所值吉星为所在宫位的吉星群。 → 《紫微斗数全书》
  - `[ns_zwds_j1_169]` `[trigger: 小儿神煞]` `[factor_trigger: group_xiaoershensha]` `[role: 主干]` 小儿神煞为专用于小儿命局的神煞群。 → 《紫微斗数全书》
  - `[ns_zwds_j1_170]` `[trigger: 贵格星曜]` `[factor_trigger: guige_xingyao]` `[role: 主干]` 贵格星曜为构成贵格的星曜组合。 → 《紫微斗数全书》
  - `[ns_zwds_j1_171]` `[trigger: 贵人配合]` `[factor_trigger: guiren_peihe]` `[role: 条件分支]` 贵人配合为天乙贵人等吉神的配合状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_172]` `[trigger: 孤克刑克]` `[factor_trigger: guke_xingke]` `[role: 条件分支]` 孤克刑克为孤辰寡宿与刑克的组合。 → 《紫微斗数全书》
  - `[ns_zwds_j1_173]` `[trigger: 化曜夹持]` `[factor_trigger: huayao_jiachi]` `[role: 条件分支]` 化曜夹持为四化星夹拱命宫的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_174]` `[trigger: 夹格层次]` `[factor_trigger: jiage_cengci]` `[role: 条件分支]` 夹格层次为夹拱格局的高低层次。 → 《紫微斗数全书》
  - `[ns_zwds_j1_175]` `[trigger: 夹格类型]` `[factor_trigger: jiage_leixing]` `[role: 条件分支]` 夹格类型为夹拱格局的具体类型。 → 《紫微斗数全书》
  - `[ns_zwds_j1_176]` `[trigger: 将相之才]` `[factor_trigger: jiangxiang_zhicai]` `[role: 结果]` 将相之才为具备将帅宰相才能的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_177]` `[trigger: 夹星组合]` `[factor_trigger: jiaxing_zuhe]` `[role: 条件分支]` 夹星组合为夹拱命宫的星曜组合。 → 《紫微斗数全书》
  - `[ns_zwds_j1_178]` `[trigger: 吉星密度检验]` `[factor_trigger: jixing_density_check]` `[role: 条件分支]` 吉星密度检验为吉星在命盘中分布密度的检验。 → 《紫微斗数全书》
  - `[ns_zwds_j1_179]` `[trigger: 吉星夹格]` `[factor_trigger: jixing_jiage]` `[role: 条件分支]` 吉星夹格为吉星夹拱命宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_180]` `[trigger: 吉星配合]` `[factor_trigger: jixing_peihe]` `[role: 条件分支]` 吉星配合为吉星间的组合配置。 → 《紫微斗数全书》
  - `[ns_zwds_j1_181]` `[trigger: 忌曜逢险]` `[factor_trigger: jiyao_fengxian]` `[role: 条件分支]` 忌曜逢险为化忌遇煞星的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_182]` `[trigger: 空亡破耗]` `[factor_trigger: kongwang_pohao]` `[role: 条件分支]` 空亡破耗为空亡与破耗同临的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_183]` `[trigger: 魁钺贵星]` `[factor_trigger: kuiyue_guixing]` `[role: 条件分支]` 魁钺贵星为天魁天钺贵人星的配合。 → 《紫微斗数全书》
  - `[ns_zwds_j1_184]` `[trigger: 枯木逢春]` `[factor_trigger: kumufengchun]` `[role: 结果]` 枯木逢春为困境逢转机、否极泰来之象。 → 《紫微斗数全书》
  - `[ns_zwds_j1_185]` `[trigger: 庶格层次]` `[factor_trigger: level_shuge]` `[role: 条件分支]` 庶格层次为普通格局的层次评定。 → 《紫微斗数全书》
  - `[ns_zwds_j1_186]` `[trigger: 星格层次]` `[factor_trigger: level_xingge]` `[role: 条件分支]` 星格层次为星曜格局的层次评定。 → 《紫微斗数全书》
  - `[ns_zwds_j1_187]` `[trigger: 流动吉累]` `[factor_trigger: liudong_jilei]` `[role: 条件分支]` 流动吉累为流年吉曜累积的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_188]` `[trigger: 空劫守命]` `[factor_trigger: pattern_kongjieshenming]` `[role: 条件分支]` 空劫守命为地空地劫守命宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_189]` `[trigger: 魁钺夹命]` `[factor_trigger: pattern_kuiyue_jiaming]` `[role: 条件分支]` 魁钺夹命为天魁天钺夹拱命宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_190]` `[trigger: 魁钺三合]` `[factor_trigger: pattern_kuiyue_sanhe]` `[role: 条件分支]` 魁钺三合为天魁天钺与命宫三合的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_191]` `[trigger: 魁钺迎解]` `[factor_trigger: pattern_kuiyue_yingjie]` `[role: 条件分支]` 魁钺迎解为天魁天钺化解凶煞的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_192]` `[trigger: 廉破卯酉]` `[factor_trigger: pattern_lianpomaoyu]` `[role: 条件分支]` 廉破卯酉为廉贞破军同在卯酉宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_193]` `[trigger: 廉贞七杀]` `[factor_trigger: pattern_lianzhen_qisha]` `[role: 条件分支]` 廉贞七杀为廉贞与七杀同宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_194]` `[trigger: 禄五位]` `[factor_trigger: pattern_lu_wuwei]` `[role: 条件分支]` 禄五位为禄存或化禄在命盘五个关键宫位的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_195]` `[trigger: 禄合夹会]` `[factor_trigger: pattern_luhe_jiahui]` `[role: 条件分支]` 禄合夹会为禄存与六合夹拱会照的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_196]` `[trigger: 禄科聚会]` `[factor_trigger: pattern_luke_juhui]` `[role: 条件分支]` 禄科聚会为化禄与化科同宫或会照的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_197]` `[trigger: 禄马扶身]` `[factor_trigger: pattern_luma_fushen]` `[role: 条件分支]` 禄马扶身为禄存与天马同宫扶命的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_198]` `[trigger: 落陷不逢科展]` `[factor_trigger: pattern_luoxian_bufeng_kezhan]` `[role: 条件分支]` 落陷不逢科展为星曜落陷且无化科展转的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_199]` `[trigger: 禄权夹会]` `[factor_trigger: pattern_luquan_jiahui]` `[role: 条件分支]` 禄权夹会为化禄与化权夹拱会照的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_200]` `[trigger: 禄权坐守]` `[factor_trigger: pattern_luquan_zuoshou]` `[role: 条件分支]` 禄权坐守为化禄与化权同宫守命的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_201]` `[trigger: 禄权科合]` `[factor_trigger: pattern_luquanke_he]` `[role: 条件分支]` 禄权科合为化禄化权化科三合会照的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_202]` `[trigger: 吕后专权]` `[factor_trigger: pattern_lvhou_zhuanquan]` `[role: 条件分支]` 吕后专权为女命化权过重克夫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_203]` `[trigger: 马头带箭]` `[factor_trigger: pattern_matou_daijian]` `[role: 条件分支]` 马头带箭为擎羊在午宫守命的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_204]` `[trigger: 命无正曜]` `[factor_trigger: pattern_ming_wu_zhengyao]` `[role: 条件分支]` 命无正曜为命宫无甲级主星坐守的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_205]` `[trigger: 明珠两照]` `[factor_trigger: pattern_mingzhu_liangzhao]` `[role: 条件分支]` 明珠两照为太阳太阴分守日月宫位的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_206]` `[trigger: 七杀朝斗]` `[factor_trigger: pattern_qisha_chaodou]` `[role: 条件分支]` 七杀朝斗为七杀入庙得禄朝拱紫微的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_207]` `[trigger: 七杀单居]` `[factor_trigger: pattern_qishadanju]` `[role: 条件分支]` 七杀单居为七杀独守命宫无吉星同宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_208]` `[trigger: 权会巨门]` `[factor_trigger: pattern_quan_hui_jumen]` `[role: 条件分支]` 权会巨门为化权与巨门同宫或会照的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_209]` `[trigger: 权禄拱照]` `[factor_trigger: pattern_quanlu_gongzhao]` `[role: 条件分支]` 权禄拱照为化权与化禄拱照命宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_210]` `[trigger: 权禄会合]` `[factor_trigger: pattern_quanlu_huihe]` `[role: 条件分支]` 权禄会合为化权与化禄会照合局的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_211]` `[trigger: 权禄夹会]` `[factor_trigger: pattern_quanlu_jiahui]` `[role: 条件分支]` 权禄夹会为化权与化禄夹拱会照的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_212]` `[trigger: 权禄守财]` `[factor_trigger: pattern_quanlu_shoucai]` `[role: 条件分支]` 权禄守财为化权与化禄守财帛宫的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_213]` `[trigger: 不能发达]` `[factor_trigger: result_bunengfada]` `[role: 结果]` 不能发达为格局受破难以发迹的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_214]` `[trigger: 财不悟]` `[factor_trigger: result_caibuwu]` `[role: 结果]` 财不悟为求财不得其法的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_215]` `[trigger: 财官]` `[factor_trigger: result_caiguan]` `[role: 结果]` 财官为财禄与官禄兼得的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_216]` `[trigger: 长寿]` `[factor_trigger: result_changshou]` `[role: 结果]` 长寿为寿元悠长的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_217]` `[trigger: 出将出相]` `[factor_trigger: result_chujiangchuxiang]` `[role: 结果]` 出将出相为文武兼备显达的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_218]` `[trigger: 出仕]` `[factor_trigger: result_chushi]` `[role: 结果]` 出仕为入仕为官的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_219]` `[trigger: 达]` `[factor_trigger: result_da]` `[role: 结果]` 达为通达显贵的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_220]` `[trigger: 短夫]` `[factor_trigger: result_duanfu]` `[role: 结果]` 短夫为女命丈夫寿短或缘薄的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_221]` `[trigger: 多才多能]` `[factor_trigger: result_duocai_duoneng]` `[role: 结果]` 多才多能为才艺出众的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_222]` `[trigger: 二品]` `[factor_trigger: result_erpin]` `[role: 结果]` 二品为官至二品的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_223]` `[trigger: 封贤]` `[factor_trigger: result_fengxian]` `[role: 结果]` 封贤为女命受封诰命的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_224]` `[trigger: 富贵比翼]` `[factor_trigger: result_fugui_biyi]` `[role: 结果]` 富贵比翼为夫妻共同显达的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_225]` `[trigger: 富贵全美]` `[factor_trigger: result_fugui_quanmei]` `[role: 结果]` 富贵全美为富贵圆满无缺的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_226]` `[trigger: 富贵双全]` `[factor_trigger: result_fugui_shuangquan]` `[role: 结果]` 富贵双全为财富与地位兼得的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_227]` `[trigger: 福厚]` `[factor_trigger: result_fuhou]` `[role: 结果]` 福厚为福分深厚的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_228]` `[trigger: 福厚二品]` `[factor_trigger: result_fuhou_erpin]` `[role: 结果]` 福厚二品为福泽深厚且官至二品的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_229]` `[trigger: 高强]` `[factor_trigger: result_gaoqiang]` `[role: 结果]` 高强为才能卓越超群的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_230]` `[trigger: 公门]` `[factor_trigger: result_gongmen]` `[role: 结果]` 公门为入仕衙门任职的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_231]` `[trigger: 孤损寿]` `[factor_trigger: result_gu_sunshou]` `[role: 结果]` 孤损寿为孤独且损伤寿元的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_232]` `[trigger: 贵体]` `[factor_trigger: result_guiti]` `[role: 结果]` 贵体为身体尊贵受人敬重的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_233]` `[trigger: 合格局]` `[factor_trigger: result_hegejü]` `[role: 结果]` 合格局为符合格局要求的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_234]` `[trigger: 火贪贵]` `[factor_trigger: result_huotan_gui]` `[role: 结果]` 火贪贵为火星与贪狼同宫主贵的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_235]` `[trigger: 吉]` `[factor_trigger: result_ji]` `[role: 结果]` 吉为吉利顺遂的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_236]` `[trigger: 健寿]` `[factor_trigger: result_jianshou]` `[role: 结果]` 健寿为健康长寿的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_237]` `[trigger: 九五]` `[factor_trigger: result_jiuwu]` `[role: 结果]` 九五为至尊极贵的判断。 → 《紫微斗数全书》
  - `[ns_zwds_j1_238]` `[trigger: 凶星数]` `[factor_trigger: star_xiong_count]` `[role: 条件分支]` 凶星数为命盘中凶星的数量统计。 → 《紫微斗数全书》
  - `[ns_zwds_j1_239]` `[trigger: 擎羊对宫入庙]` `[factor_trigger: star_yangren_duigong_rumiao]` `[role: 条件分支]` 擎羊对宫入庙为擎羊在对宫且庙旺的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_240]` `[trigger: 主星]` `[factor_trigger: star_zhu]` `[role: 条件分支]` 主星为命宫的主导星曜。 → 《紫微斗数全书》
  - `[ns_zwds_j1_241]` `[trigger: 辰巳旺地]` `[factor_trigger: state_chensi_wangdi]` `[role: 条件分支]` 辰巳旺地为星曜在辰宫或巳宫旺盛的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_242]` `[trigger: 到陷]` `[factor_trigger: state_daoxian]` `[role: 条件分支]` 到陷为星曜运行到陷落之地的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_243]` `[trigger: 境遇]` `[factor_trigger: state_jinghuan]` `[role: 条件分支]` 境遇为命主所处环境状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_244]` `[trigger: 吉凶汇合]` `[factor_trigger: state_jixionghuihe]` `[role: 条件分支]` 吉凶汇合为吉星与凶星会照的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_245]` `[trigger: 庙旺平陷]` `[factor_trigger: state_miaowangpingxian]` `[role: 条件分支]` 庙旺平陷为星曜的四种状态等级。 → 《紫微斗数全书》
  - `[ns_zwds_j1_246]` `[trigger: 庙陷]` `[factor_trigger: state_miaoxian]` `[role: 条件分支]` 庙陷为星曜庙旺或陷落的两极状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_247]` `[trigger: 入庙]` `[factor_trigger: state_rumiao]` `[role: 条件分支]` 入庙为星曜处于最佳状态的位置。 → 《紫微斗数全书》
  - `[ns_zwds_j1_248]` `[trigger: 生逢陷地]` `[factor_trigger: state_shengfengxiandi]` `[role: 条件分支]` 生逢陷地为出生时星曜处于陷落之地。 → 《紫微斗数全书》
  - `[ns_zwds_j1_249]` `[trigger: 太岁并小限]` `[factor_trigger: state_taisuibingxiaoxian]` `[role: 条件分支]` 太岁并小限为流年太岁与小限同宫的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_250]` `[trigger: 太岁行命宫]` `[factor_trigger: state_taisuixingminggong]` `[role: 条件分支]` 太岁行命宫为流年太岁经过命宫的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_251]` `[trigger: 陷不逢凶]` `[factor_trigger: state_xianbufengxiong]` `[role: 条件分支]` 陷不逢凶为星曜落陷但不逢凶星的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_252]` `[trigger: 阴阳反背]` `[factor_trigger: state_yinyangfanbei]` `[role: 条件分支]` 阴阳反背为阴阳属性相悖的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_253]` `[trigger: 百无子]` `[factor_trigger: symbol_baiwuzi]` `[role: 条件分支]` 百无子为无子嗣的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_254]` `[trigger: 不禅折贵]` `[factor_trigger: symbol_buchan_zhegui]` `[role: 条件分支]` 不禅折贵为不能传承尊贵地位的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_255]` `[trigger: 洞宾现世]` `[factor_trigger: symbol_dongbin_xianshi]` `[role: 条件分支]` 洞宾现世为吕洞宾仙人现世的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_256]` `[trigger: 对黄鸡拜]` `[factor_trigger: symbol_duihuang_jibai]` `[role: 条件分支]` 对黄鸡拜为祭祀祈福的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_257]` `[trigger: 封诰极贵]` `[factor_trigger: symbol_fengao_jigui]` `[role: 条件分支]` 封诰极贵为受封诰命至极尊贵的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_258]` `[trigger: 焚舟济绝战]` `[factor_trigger: symbol_fenzhouji_juezhan]` `[role: 条件分支]` 焚舟济绝战为破釜沉舟决一死战的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_259]` `[trigger: 负驼囊]` `[factor_trigger: symbol_fu_tuonang]` `[role: 条件分支]` 负驼囊为背负行囊漂泊的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_260]` `[trigger: 和贵华表]` `[factor_trigger: symbol_heguihuabiao]` `[role: 条件分支]` 和贵华表为显赫功业的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_261]` `[trigger: 黄粱梦]` `[factor_trigger: symbol_huangliangmeng]` `[role: 条件分支]` 黄粱梦为人生如梦虚幻的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_262]` `[trigger: 井破一分]` `[factor_trigger: symbol_jingpo_yifen]` `[role: 条件分支]` 井破一分为井宿破损一分的象征。 → 《紫微斗数全书》
  - `[ns_zwds_j1_263]` `[trigger: 家庭]` `[factor_trigger: type_jiating]` `[role: 条件分支]` 家庭为命主家庭状况的分类。 → 《紫微斗数全书》
  - `[ns_zwds_j1_264]` `[trigger: 男命]` `[factor_trigger: type_nanming]` `[role: 条件分支]` 男命为男性命主的命格分类。 → 《紫微斗数全书》
  - `[ns_zwds_j1_265]` `[trigger: 女命]` `[factor_trigger: type_nvming]` `[role: 条件分支]` 女命为女性命主的命格分类。 → 《紫微斗数全书》
  - `[ns_zwds_j1_266]` `[trigger: 生年支]` `[factor_trigger: type_shengnianzhi]` `[role: 条件分支]` 生年支为出生年的地支。 → 《紫微斗数全书》
  - `[ns_zwds_j1_267]` `[trigger: 双丁]` `[factor_trigger: type_shuangding]` `[role: 条件分支]` 双丁为天干中有两个丁的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_268]` `[trigger: 五行命]` `[factor_trigger: type_wuxingming]` `[role: 条件分支]` 五行命为按纳音五行分类的命格。 → 《紫微斗数全书》
  - `[ns_zwds_j1_269]` `[trigger: 阳男阴女]` `[factor_trigger: type_yangnanyinnv]` `[role: 条件分支]` 阳男阴女为阳年生男或阴年生女的分类。 → 《紫微斗数全书》
  - `[ns_zwds_j1_270]` `[trigger: 阴男阳女]` `[factor_trigger: type_yinnanyangnu]` `[role: 条件分支]` 阴男阳女为阴年生男或阳年生女的分类。 → 《紫微斗数全书》
  - `[ns_zwds_j1_271]` `[trigger: 中庸之局]` `[factor_trigger: type_zhongyongzhiju]` `[role: 条件分支]` 中庸之局为不偏不倚的命局分类。 → 《紫微斗数全书》
  - `[ns_zwds_j1_272]` `[trigger: 文武庙旺]` `[factor_trigger: wenwu_miaowang]` `[role: 条件分支]` 文武庙旺为文曲武曲皆庙旺的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_273]` `[trigger: 五行制化]` `[factor_trigger: wuxing_zhihua]` `[role: 条件分支]` 五行制化为五行相克相生的制约转化。 → 《紫微斗数全书》
  - `[ns_zwds_j1_274]` `[trigger: 陷地失辉]` `[factor_trigger: xiandi_shihui]` `[role: 条件分支]` 陷地失辉为星曜落陷失去光辉的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_275]` `[trigger: 性格映射]` `[factor_trigger: xingge_yingshe]` `[role: 条件分支]` 性格映射为星曜对性格特征的映射关系。 → 《紫微斗数全书》
  - `[ns_zwds_j1_276]` `[trigger: 凶星聚集]` `[factor_trigger: xiongxing_juji]` `[role: 条件分支]` 凶星聚集为多颗凶星会聚一宫的状态。 → 《紫微斗数全书》
  - `[ns_zwds_j1_277]` `[trigger: 凶星组合]` `[factor_trigger: xiongxing_zuhe]` `[role: 条件分支]` 凶星组合为凶星之间的特定配合。 → 《紫微斗数全书》
  - `[ns_zwds_j1_278]` `[trigger: 制化关系]` `[factor_trigger: zhihua_guanxi]` `[role: 条件分支]` 制化关系为五行相克相生的制约转化关系。 → 《紫微斗数全书》
  - `[ns_zwds_j1_279]` `[trigger: 紫府朝合]` `[factor_trigger: zifuzhaohe]` `[role: 条件分支]` 紫府朝合为紫微天府朝拱会合的格局。 → 《紫微斗数全书》
  - `[ns_zwds_j1_280]` `[trigger: 子亥宫]` `[factor_trigger: zone_zihai]` `[role: 条件分支]` 子亥宫为子宫或亥宫的宫位区域。 → 《紫微斗数全书》
  - `[ns_zwds_j1_046]` `[trigger: 大限运程]` `[factor_trigger: system_daxian]` `[role: 主干]` 大限为十年一运，主人生阶段之吉凶。 → 《太微赋》"童子限""老人限"
  - `[ns_zwds_j1_047]` `[trigger: 小限运程]` `[factor_trigger: system_xiaoxian]` `[role: 主干]` 小限为一年一运，主流年之吉凶。 → 《太微赋》限运
  - `[ns_zwds_j1_048]` `[trigger: 太岁流年]` `[factor_trigger: system_taisui]` `[role: 主干]` 太岁为流年之主，冲照命宫主动荡变化。 → 《太微赋》限运
  - `[ns_zwds_j1_049]` `[trigger: 三方四正]` `[factor_trigger: structure_sanfangsizheng]` `[role: 主干]` 三方四正为命宫与对宫、三合宫的组合结构。 → 《太微赋》"三合相照"
  - `[ns_zwds_j1_050]` `[trigger: 十二宫结构]` `[factor_trigger: structure_shiergong]` `[role: 主干]` 十二宫为紫微斗数命盘的基本架构。 → 《太微赋》"分布千十二垣"
  - `[ns_zwds_j1_051]` `[trigger: 南北斗体系]` `[factor_trigger: system_nanbeidou]` `[role: 主干]` 南北斗为紫微斗数星曜分类的基本体系。 → 《太微赋》"南北二斗，集而成数"
  - `[ns_zwds_j1_052]` `[trigger: 化禄星]` `[factor_trigger: transform_hualu]` `[role: 主干]` 化禄主财禄增益，逢之主财运亨通。 → 《太微赋》"禄文拱命"
  - `[ns_zwds_j1_053]` `[trigger: 化权星]` `[factor_trigger: transform_huaquan]` `[role: 主干]` 化权主权柄威严，逢之主掌权得势。 → 《太微赋》
  - `[ns_zwds_j1_054]` `[trigger: 化科星]` `[factor_trigger: transform_huake]` `[role: 主干]` 化科主科名声誉，逢之主考试有成。 → 《太微赋》
  - `[ns_zwds_j1_055]` `[trigger: 化忌星]` `[factor_trigger: transform_huaji]` `[role: 主干]` 化忌主阻滞是非，逢之主口舌纠缠。 → 《太微赋》
  - `[ns_zwds_j1_056]` `[trigger: 五行生克]` `[factor_trigger: system_wuxing]` `[role: 主干]` 五行生克为推断星曜相互作用的基础。 → 《太微赋》"生克之要"
  - `[ns_zwds_j1_057]` `[trigger: 长生十二神]` `[factor_trigger: system_changsheng12]` `[role: 主干]` 长生十二神主星曜在各宫之旺衰状态。 → 《太微赋》"得垣失度"
  - `[ns_zwds_j1_058]` `[trigger: 太傅星]` `[factor_trigger: star_taifu]` `[role: 主干]` 太傅为辅佐星，主贵人提携教育。 → 《太微赋》
  - `[ns_zwds_j1_059]` `[trigger: 府相朝垣格]` `[factor_trigger: pattern_fuxiangchaoyuan]` `[role: 条件分支]` 府相朝垣格为天府天相朝拱命宫的贵格。 → 《太微赋》"府相朝垣"
  - `[ns_zwds_j1_060]` `[trigger: 府相朝垣格2]` `[factor_trigger: pattern_fuxiang_chaoyuan]` `[role: 条件分支]` 府相朝垣格为天府天相朝拱命宫的贵格。 → 《太微赋》"府相朝垣"
  - `[ns_zwds_j1_061]` `[trigger: 文武双全结果]` `[factor_trigger: result_wenwu]` `[role: 结果]` 文武双全为命格主文武兼备的判断。 → 《太微赋》
  - `[ns_zwds_j1_062]` `[trigger: 金榜结果]` `[factor_trigger: result_jinji]` `[role: 结果]` 金榜结果为科举登第的贵显结果。 → 《太微赋》
  - `[ns_zwds_j1_063]` `[trigger: 隐患结果]` `[factor_trigger: result_yinhuan]` `[role: 结果]` 隐患结果为命格潜藏凶险的判断。 → 《太微赋》
  - `[ns_zwds_j1_064]` `[trigger: 凶相结果]` `[factor_trigger: result_xiongxiang]` `[role: 结果]` 凶相结果为命格主凶险的判断。 → 《太微赋》
  - `[ns_zwds_j1_065]` `[trigger: 手段孙结果]` `[factor_trigger: result_shouduansun]` `[role: 结果]` 手段孙为手段损人的凶险性格。 → 《太微赋》
  - `[ns_zwds_j1_066]` `[trigger: 权禄生逢格]` `[factor_trigger: pattern_quanlu_shengfeng]` `[role: 条件分支]` 权禄生逢格为化权化禄生旺相逢的贵格。 → 《太微赋》
  - `[ns_zwds_j1_067]` `[trigger: 损寿结果]` `[factor_trigger: result_sunshou]` `[role: 结果]` 损寿结果为寿命受损的凶险判断。 → 《太微赋》
  - `[ns_zwds_j1_068]` `[trigger: 福不轻结果]` `[factor_trigger: result_fubuqing]` `[role: 结果]` 福不轻结果为福气深厚的吉利判断。 → 《太微赋》
  - `[ns_zwds_j1_069]` `[trigger: 昌曲加会格]` `[factor_trigger: pattern_changqu_jiahui]` `[role: 条件分支]` 昌曲加会格为文昌文曲加会命宫的文贵格局。 → 《太微赋》
  - `[ns_zwds_j1_070]` `[trigger: 缘分结果]` `[factor_trigger: result_yuan]` `[role: 结果]` 缘分结果为人际缘分的判断。 → 《太微赋》
  - `[ns_zwds_j1_071]` `[trigger: 僧道结果]` `[factor_trigger: result_seng]` `[role: 结果]` 僧道结果为出家修行的命格判断。 → 《太微赋》
  - `[ns_zwds_j1_072]` `[trigger: 无知结果]` `[factor_trigger: result_wuzhi]` `[role: 结果]` 无知结果为愚钝无知的性格判断。 → 《太微赋》
  - `[ns_zwds_j1_073]` `[trigger: 紫微守命格]` `[factor_trigger: star_ziwei_shouming]` `[role: 条件分支]` 紫微守命格为紫微星坐守命宫的帝星格局。 → 《太微赋》"紫微守命"
  - `[ns_zwds_j1_074]` `[trigger: 君臣庆会格]` `[factor_trigger: pattern_junchen_qinghui]` `[role: 条件分支]` 君臣庆会格为紫微得辅弼环拱的极贵格局。 → 《太微赋》"君臣庆会"
  - `[ns_zwds_j1_075]` `[trigger: 连登结果]` `[factor_trigger: result_liandeng]` `[role: 结果]` 连登结果为连续登科的贵显结果。 → 《太微赋》
  - `[ns_zwds_j1_076]` `[trigger: 大富不贵结果]` `[factor_trigger: result_dafu_bugui]` `[role: 结果]` 大富不贵结果为富而不贵的命格判断。 → 《太微赋》
  - `[ns_zwds_j1_077]` `[trigger: 左右加会格]` `[factor_trigger: pattern_zuoyou_jiahui]` `[role: 条件分支]` 左右加会格为左辅右弼加会命宫的贵人格局。 → 《太微赋》
  - `[ns_zwds_j1_078]` `[trigger: 杀破狼无贵格]` `[factor_trigger: pattern_shapolan_wugui]` `[role: 条件分支]` 杀破狼无贵格为杀破狼无吉星辅佐的凶险格局。 → 《太微赋》
  - `[ns_zwds_j1_079]` `[trigger: 性格结果]` `[factor_trigger: result_xingge]` `[role: 结果]` 性格结果为性情特征的判断。 → 《太微赋》
  - `[ns_zwds_j1_080]` `[trigger: 十年综合结果]` `[factor_trigger: result_shinianzonghe]` `[role: 结果]` 十年综合结果为大限十年运势的综合判断。 → 《太微赋》
  - `[ns_zwds_j1_081]` `[trigger: 富贵贫贱结果]` `[factor_trigger: result_fuguipinjian]` `[role: 结果]` 富贵贫贱结果为命格贵贱的综合判断。 → 《太微赋》
  - `[ns_zwds_j1_082]` `[trigger: 三重配合]` `[factor_trigger: sanchong_peihe]` `[role: 主干]` 三重配合为命身限三重验证的方法。 → 《太微赋》
  - `[ns_zwds_j1_083]` `[trigger: 事务判断]` `[factor_trigger: shiwu_panduan]` `[role: 主干]` 事务判断为具体事项的推断方法。 → 《太微赋》
  - `[ns_zwds_j1_084]` `[trigger: 官贵结构]` `[factor_trigger: guangui_jiegou]` `[role: 主干]` 官贵结构为官禄宫贵格的结构特征。 → 《太微赋》
  - `[ns_zwds_j1_085]` `[trigger: 贫贱格结构]` `[factor_trigger: pinjiange_jiegou]` `[role: 主干]` 贫贱格结构为贫贱命格的结构特征。 → 《太微赋》
  - `[ns_zwds_j1_086]` `[trigger: 天刑星]` `[factor_trigger: star_tianxing]` `[role: 主干]` 天刑为煞曜，主刑伤官非，有孤克之性。 → 《太微赋》
  - `[ns_zwds_j1_087]` `[trigger: 天姚星]` `[factor_trigger: star_tianyao]` `[role: 主干]` 天姚为桃花星，主风流多情，感情纠葛。 → 《太微赋》
  - `[ns_zwds_j1_088]` `[trigger: 丧门星]` `[factor_trigger: star_sangmen]` `[role: 主干]` 丧门为凶星，主孝服丧事，逢之主凶。 → 《太微赋》
  - `[ns_zwds_j1_089]` `[trigger: 红鸾星]` `[factor_trigger: star_hongluan]` `[role: 主干]` 红鸾为喜星，主婚姻喜庆，逢之主吉。 → 《太微赋》
  - `[ns_zwds_j1_090]` `[trigger: 斗君星]` `[factor_trigger: star_doujun]` `[role: 主干]` 斗君为流年星，主当年运势之吉凶。 → 《太微赋》
  - `[ns_zwds_j1_091]` `[trigger: 天空星]` `[factor_trigger: star_tiankong]` `[role: 主干]` 天空为煞曜，主虚空损耗，精神层面。 → 《太微赋》
  - `[ns_zwds_j1_092]` `[trigger: 天使星]` `[factor_trigger: star_tianshi]` `[role: 主干]` 天使为流年星，主病厄意外，逢之需慎。 → 《太微赋》
  - `[ns_zwds_j1_093]` `[trigger: 魁钺组合]` `[factor_trigger: star_kuiyue]` `[role: 主干]` 魁钺组合为天魁天钺的合称，主贵人助力。 → 《太微赋》
  - `[ns_zwds_j1_094]` `[trigger: 天哭星]` `[factor_trigger: star_tianku]` `[role: 主干]` 天哭为凶星，主哭泣悲伤，逢之主凶。 → 《太微赋》
  - `[ns_zwds_j1_095]` `[trigger: 龙池星]` `[factor_trigger: star_longchi]` `[role: 主干]` 龙池为吉星，主才艺显达，逢之主贵。 → 《太微赋》
  - `[ns_zwds_j1_096]` `[trigger: 昌曲组合]` `[factor_trigger: star_changqu]` `[role: 主干]` 昌曲组合为文昌文曲的合称，主科名文采。 → 《太微赋》
  - `[ns_zwds_j1_097]` `[trigger: 封诰星]` `[factor_trigger: star_fenggao]` `[role: 主干]` 封诰为吉星，主诰命封赠，逢之主贵。 → 《太微赋》
  - `[ns_zwds_j1_098]` `[trigger: 吊客星]` `[factor_trigger: star_diaoke]` `[role: 主干]` 吊客为凶星，主丧吊孝服，逢之主凶。 → 《太微赋》
  - `[ns_zwds_j1_099]` `[trigger: 早逝结果]` `[factor_trigger: result_zaoshi]` `[role: 结果]` 早逝结果为早年夭亡的凶险判断。 → 《太微赋》
  - `[ns_zwds_j1_100]` `[trigger: 文明结果]` `[factor_trigger: result_wenming]` `[role: 结果]` 文明结果为文采显达的贵格判断。 → 《太微赋》
  - `[ns_zwds_j1_101]` `[trigger: 紫府朝垣格]` `[factor_trigger: pattern_zifuchaoyuan]` `[role: 条件分支]` 紫府朝垣格为紫微天府朝拱命宫的极贵格局。 → 《太微赋》
  - `[ns_zwds_j1_102]` `[trigger: 乘马星]` `[factor_trigger: star_chenma]` `[role: 主干]` 乘马为动星，主奔波外出，逢之主动。 → 《太微赋》
  - `[ns_zwds_j1_103]` `[trigger: 早亡结果]` `[factor_trigger: result_zaowang]` `[role: 结果]` 早亡结果为早年夭折的凶险判断。 → 《太微赋》
  - `[ns_zwds_j1_104]` `[trigger: 丧门病符组合]` `[factor_trigger: star_sangmenbingfu]` `[role: 主干]` 丧门病符组合为丧门与病符的凶险组合。 → 《太微赋》
  - `[ns_zwds_j1_105]` `[trigger: 酉生忌]` `[factor_trigger: taboo_youshengji]` `[role: 条件分支]` 酉生忌为酉年生人特定的星位忌讳。 → 《太微赋》
  - `[ns_zwds_j1_106]` `[trigger: 入相结果]` `[factor_trigger: result_ruxiang]` `[role: 结果]` 入相结果为入朝拜相的极贵判断。 → 《太微赋》
  - `[ns_zwds_j1_107]` `[trigger: 三公结果]` `[factor_trigger: result_sangong]` `[role: 结果]` 三公结果为位列三公的极贵判断。 → 《太微赋》
  - `[ns_zwds_j1_108]` `[trigger: 极富贵结果]` `[factor_trigger: result_jifugui]` `[role: 结果]` 极富贵结果为极品富贵的命格判断。 → 《太微赋》
  - `[ns_zwds_j1_109]` `[trigger: 空劫轴心]` `[factor_trigger: algo_kongjiezhouxin]` `[role: 主干]` 空劫轴心为地空地劫形成的轴心结构。 → 《太微赋》
  - `[ns_zwds_j1_110]` `[trigger: 五宫七念]` `[factor_trigger: principle_wugongqizinian]` `[role: 主干]` 五宫七念为紫微斗数的核心原则之一。 → 《太微赋》"""
    normalized_text_zh: str = """"""
    subject: str = "斗数至玄至微，理𣥜易明"
    factor_refs: list = ['system_ziwei_doushu', 'star_state_miao', 'star_state_xian', 'palace_life', 'palace_body', 'star_lucun', 'new_candidate']
    
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
        l1_anchor="zw_v1.0.0_斗数至玄至微_理_易明_001_L1",
    )
    version: str = "1.0.0"
