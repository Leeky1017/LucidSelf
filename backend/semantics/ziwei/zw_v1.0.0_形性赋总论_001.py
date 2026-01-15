"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725410
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
    semantic_id="zw_v1.0.0_形性赋总论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 形性赋总论(SemanticEntry):
    """
    - 原文（source_text）：

  原夫紫微帝座，生为厚重之容；天府尊星，当主纯和之体。金乌圆满，玉兔清奇，天机为不长不短之姿，情怀好善。武曲乃至刚至毅之操，心性果决；天同肥满，目秀清奇；廉贞...
    """
    
    original_text: str = """- 原文（source_text）：

  原夫紫微帝座，生为厚重之容；天府尊星，当主纯和之体。金乌圆满，玉兔清奇，天机为不长不短之姿，情怀好善。武曲乃至刚至毅之操，心性果决；天同肥满，目秀清奇；廉贞眉宽口阔、面横，为人性暴，好忿，好争。贪狼为善恶之星，入庙必应长耸，出垣必定顽嚚。巨门乃是非之曜，在庙敦厚温良；天相精神，相貌持重；天梁稳重，心事玉洁冰清。七杀如子路，暴虎冯河；火铃似豫让，吞炭装哑——暴虎冯河兮，目大凶狼；吞炭装哑兮，暗狼声沉俊雅。文昌眉清目秀，襟怀磊落；文曲口舌便佞，在庙定生异痣，失陷必有班痕。左辅右弼，温良规模，端庄高士；天魁天钺，具足威仪，重合三台，则十全模范。擎羊、陀罗，形丑貌粗，有矫诈体态；破军不仁，背厚眉宽，行坐腰斜，奸诈，好行惊险。性貌如春和蔼，乃是禄存之情德；情怀似火烽冲，此诚破耗之威权。星论庙旺，最怕空亡；杀落空亡，竟无威力。权禄克九窍之奇，耗劫散平生之福。禄逢梁阴抱私财，益与他人；耗遇贪狼，凄淫情于井底。贪星入于马垣，易善易恶；恶曜扶同善曜，禀性不常。财居空亡，巴三览四；文曲旺宫，闻一知十。暗合廉贞，为贪滥之曹吏；身命司数，寔奸盗之技儿，猪屠之流。善禄，定是奇高之艺，细巧伶俐之人。男居生旺，最要得𫄸；女居死绝，专看福德。命最嫌立于败位，财源却怕逢空亡。机、刑、杀、荫、狐星论嗣续之宫，加恶星忌耗，不为奇特；陀、忌、耗、囚之星，守父母之缠，决然破祖，刑伤兼之。童格宜相，根基要察。紫微肥满，天府精神；禄存禄主，也应厚重。日月、曲相、同梁、机昌，皆为美俊之姿，乃是清奇之格，上长下短，自秀眉清。贪狼同武曲，形小声高而量大；天同加陀忌，肥满而目渺；擎羊身察遭伤，若遇火铃巨暗，必生异病，又值耗杀，定主形丑貌粗。若居死绝之限，童子乳哺，徒劳其力；老者亦然寿终。此数中之纲领，乃为星纬之机关。玩味专精，以恭玄妙。限有高低，星寻喜怒；假如运限驳杂，终有浮沉。如逢杀地，更要推详；倘遇空亡，必须细察。精研于此，不患不神。

- 原注（原文注解，可无则省略小节）：

  （本条概述诸星“形性”之象，属实务相面与命盘形态映射的总论。底本未见单独原注，本稿仅在“详细解说”与 L2 中归纳历代注家与命例之共通要点。）

- 分字分词释义：

  - **形性**：形体与性情的合称，本赋意在说明各星座守命身等宫位时，对人的外貌、气质与行事风格的影响。
  - **紫微帝座，天府尊星**：紫微、天府为帝王与帑藏之星，主厚重、端庄、稳健之形象与气度。
  - **金乌、玉兔**：比喻太阳、太阴两曜；金乌圆满象征日之光明刚健，玉兔清奇象征月之清润秀美。
  - **入庙 / 出垣**：星在本垣、本旺之地称“入庙”，力量纯正；远离本位、失其根气者称“出垣”或“失度”，多有偏差与乖戾。
  - **顽嚚**：顽固而难化，兼有粗野之意，多指贪狼出垣后的顽劣表现。
  - **暴虎冯河 / 吞炭装哑**：前者比喻七杀之勇猛无惧，后者比喻火铃之极端行事与不言之烈。
  - **三台八座**：此处以“三台”指高阶辅佐、台省之星聚会，象征“十全模范”的典型贵格形象。
  - **巴三览四**：形容财居空亡之人，多方打听、东张西望而难以定性定向，是财源漂泊之象。
  - **童格**：指命局偏向幼年、童年格局，或童限早应的结构，需要特别察看根基与承载力。
  - **死绝之限**：命局或限运落在衰、病、死、绝等极弱之地，多主气力不继或生命力衰残。

- 规范化释义（primary_lang_explained）：

  本篇通过描写各颗主星、辅星与杀星对“外貌、体态、气质、性格”的影响，说明紫微斗数如何从星曜组合推知一个人的形象特征与行事风格。紫微、天府主厚重端庄；太阳、太阴主圆满清奇；天机、天同、文昌、文曲等吉星，使人温和、聪慧、清秀；七杀、火铃、擎羊、陀罗、破军等，则多带粗犷、凶猛、伤残或极端之象。

  文中强调：星曜是否入庙、是否落空亡、是否与禄存、耗劫、贪狼等相会，会显著改变形性表达的“纯度”和“方向”。禄星得梁阴抱私财，则主暗中积蓄；耗星遇贪狼，则易沉溺情欲。财星居空亡，则东张西望而难以聚财；文曲在旺宫，则一闻十解。童限、老限处于死绝之地，人力难支，往往徒劳无功或寿终。全篇以“此数中之纲领”“星寻喜怒”“运限驳杂终有浮沉”等句，总结出：形性之象虽可观，但仍需配合星垣、限运与根基综合判断。

- 完整对等诠释（secondary_lang_full）：

  This chapter outlines how the major stars, assistant stars and malefic stars in Ziwei Doushu map onto a person’s visible appearance, bodily build, temperament and style of action. Ziwei and Tianfu give a heavy, dignified bearing that can shoulder responsibility; the Sun, figured as the Golden Crow, and the Moon, figured as the Jade Rabbit, bring fullness, clarity and refined elegance. Stars such as Tianji, Tiantong, Wenchang and Wenqu soften the expression, making people appear gentle, intelligent and literate, whereas Qisha, Huoxing, Lingxing, Qingyang, Tuoluo and Pojun tend to produce coarse, fierce, wounded or extreme traits in face and manner when their power is unchecked.

  The text emphasises that no star acts alone. Whether a configuration manifests as attractive or distorted depends on temple or fall, on void positions, and on combinations with wealth and depletion stars such as Lu Cun, Hao and Jie, or desire‑oriented stars such as Tanlang. Lu‑type stars joined with Yin‑type companions often indicate hidden savings and restrained expression—someone who looks mild yet accumulates quietly. When depletion stars meet Tanlang, indulgence in pleasure and sensuality becomes more visible in posture, gaze and overall atmosphere. If wealth stars fall into void, a person may fidget and run around all day without truly gathering resources, a restlessness that shows in their demeanour.

  Finally, the chapter introduces the dimension of timing. Childhood and old‑age limits that fall into the weakest “death and extinction” regions, even when the chart promises ability or attractive form, often indicate that the body cannot sustain long‑term exertion and that certain talents never fully unfold. Taken together, this essay teaches that “form and nature” are not read from facial features alone but from the interaction between natal structure, the strength or weakness of the stars, and the periods in which these patterns are activated.

- 核心要点：

  - 各星有其 **典型形性模板**：紫微天府主厚重端庄，日月主光明清润，文昌文曲主清秀聪慧，七杀破军等主刚烈、险狠。
  - 形性判断高度依赖 **星曜的庙旺与空亡状态**，以及与禄存、耗劫、贪狼等吉凶星的组合。
  - 财星、禄星与耗星在不同宫位与状态下，决定一个人“财的取得方式与消耗轨迹”，并体现在神情举止之上。
  - 童限、老限及死绝之地，对形体气力与生命力的削弱尤甚，需要结合命身与限运谨慎观照。

- 详细解说：

  1. **主星的形性主调**  
     紫微、天府为帝王与帑藏之星，落命身或三方多主体格厚实、气度端庄，有“可任重载”的感觉；太阳、太阴则分别主阳刚光明与阴柔清润，配合文昌、文曲、天相、天梁等星，可成“清奇俊秀”的形象。此类主星决定的是一个人的“第一印象底色”。

  2. **辅星与杀星的修饰与扭曲**  
     左辅、右弼、天魁、天钺等吉辅，往往使人显得端方、庄重、有礼；三台齐会，则有“十全模范”之象。反之，擎羊、陀罗、火铃、七杀、破军等杀曜，则多带粗犷、凶狠、伤残、极端之象，尤其在庙陷不佳、又逢空亡时，其形性表现更为尖锐。文本中用“暴虎冯河”“吞炭装哑”等比喻，强化了这种“过猛、过烈”的体感。

  3. **禄、耗、贪的形性与财性联动**  
     禄存与各禄星落命身或三方，会带来“性貌如春和蔼”的印象，但若与梁阴抱私财，则暗示财不外露、私蓄于内。耗劫与贪狼相会，则多主沉溺情欲与享乐，形神往往带有疲惫或放纵之色。财星居空亡则“巴三览四”，整日张罗而难以真聚，容易在形貌上显出焦躁与不安。

  4. **限运、死绝与童老之别**  
     文末以“死绝之限”点出时间维度：童子尚在乳哺，老者接近寿终，若此时限运又落在死绝之地，即便命中有某种形性与技艺，也难以长期发挥，往往事倍功半，甚至无功而终。这里提醒读者：形性虽由星定，但能否施展，仍需看限运与年龄阶段。

- 叙事素材（narrative_snippets）：

  - **帝星形象**："紫微帝座，生为厚重之容；天府尊星，当主纯和之体。"此句描绘紫微天府两颗帝星的典型形象——厚重端庄、纯和稳重。
  - **日月清奇**："金乌圆满，玉兔清奇"，以金乌喻太阳之光明刚健，玉兔喻太阴之清润秀美，是日月入命的典型形性描写。
  - **杀曜极端**："七杀如子路，暴虎冯河；火铃似豫让，吞炭装哑"，以历史人物比喻七杀与火铃的极端刚烈之性。
  - **贪狼两面**："贪狼为善恶之星，入庙必应长耸，出垣必定顽嚚"，说明贪狼庙旺与落陷时的形性差异极大。
  - **财星漂泊**："财居空亡，巴三览四"，形容财星落空亡者东张西望、难以聚财的焦躁之象。
  - **现代应用**：本条可作为人物形象评估的参考框架，从星曜组合推知外貌气质与行事风格倾向。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j1_058]` `[trigger: 厚重性格]` `[factor_trigger: trait_houzhong]` `[role: 主干]` 紫微帝座主厚重之容，形貌端庄稳重。 → 《形性赋》"紫微帝座，生为厚重之容"
  - `[ns_zwds_j1_059]` `[trigger: 刚烈性格]` `[factor_trigger: trait_ganglie]` `[role: 主干]` 七杀如子路暴虎冯河，主刚烈勇猛之性。 → 《形性赋》"七杀如子路，暴虎冯河"
  - `[ns_zwds_j1_060]` `[trigger: 左辅吉星]` `[factor_trigger: star_zuofu]` `[role: 主干]` 左辅为吉辅，主端庄高士，温良规模。 → 《形性赋》"左辅右弼，温良规模，端庄高士"
  - `[ns_zwds_j1_061]` `[trigger: 右弼吉星]` `[factor_trigger: star_youbi]` `[role: 主干]` 右弼为吉辅，主温良端正，贵人相助。 → 《形性赋》"左辅右弼，温良规模"
  - `[ns_zwds_j1_062]` `[trigger: 八座贵星]` `[factor_trigger: star_bazuo]` `[role: 主干]` 八座为贵星，与三台同会主十全模范。 → 《形性赋》"重合三台，则十全模范"
  - `[ns_zwds_j1_063]` `[trigger: 天刑刑星]` `[factor_trigger: star_tianxing]` `[role: 主干]` 天刑为刑星，主刑伤孤克，宜从事法律医药。 → 《形性赋》
  - `[ns_zwds_j1_064]` `[trigger: 天姚桃花]` `[factor_trigger: star_tianyao]` `[role: 主干]` 天姚为桃花星，主风流多情，异性缘重。 → 《形性赋》
  - `[ns_zwds_j1_065]` `[trigger: 红鸾桃花]` `[factor_trigger: star_hongluan]` `[role: 主干]` 红鸾为桃花星，主婚姻喜庆，异性缘旺。 → 《形性赋》
  - `[ns_zwds_j1_066]` `[trigger: 天喜喜星]` `[factor_trigger: star_tianxi]` `[role: 主干]` 天喜为喜庆星，主添丁进口，喜事临门。 → 《形性赋》
  - `[ns_zwds_j1_067]` `[trigger: 天空劫星]` `[factor_trigger: star_tiankong]` `[role: 主干]` 天空为劫星，主思想空灵，不切实际。 → 《形性赋》"星论庙旺，最怕空亡"
  - `[ns_zwds_j1_068]` `[trigger: 天哭丧星]` `[factor_trigger: star_tianku]` `[role: 主干]` 天哭为丧星，主悲伤哭泣，孤寂之象。 → 《形性赋》
  - `[ns_zwds_j1_069]` `[trigger: 天虚耗星]` `[factor_trigger: star_tianxu]` `[role: 主干]` 天虚为耗星，主虚耗损失，身心空虚。 → 《形性赋》
  - `[ns_zwds_j1_070]` `[trigger: 龙池文星]` `[factor_trigger: star_longchi]` `[role: 主干]` 龙池为文星，主聪明才艺，利科甲功名。 → 《形性赋》
  - `[ns_zwds_j1_071]` `[trigger: 凤阁文星]` `[factor_trigger: star_fengge]` `[role: 主干]` 凤阁为文星，主文采风华，利文艺创作。 → 《形性赋》
  - `[ns_zwds_j1_072]` `[trigger: 封诰贵星]` `[factor_trigger: star_fenggao]` `[role: 主干]` 封诰为贵星，主受封荣显，得官得禄。 → 《形性赋》
  - `[ns_zwds_j1_073]` `[trigger: 天官贵星]` `[factor_trigger: star_tianguan]` `[role: 主干]` 天官为贵星，主得官贵人，仕途顺遂。 → 《形性赋》
  - `[ns_zwds_j1_074]` `[trigger: 天福福星]` `[factor_trigger: star_tianfu_xing]` `[role: 主干]` 天福为福星，主福禄寿喜，逢凶化吉。 → 《形性赋》
  - `[ns_zwds_j1_075]` `[trigger: 解神化解]` `[factor_trigger: star_jieshen]` `[role: 主干]` 解神为化解星，主逢凶化吉，灾厄可解。 → 《形性赋》
  - `[ns_zwds_j1_076]` `[trigger: 截空空星]` `[factor_trigger: star_jiekong]` `[role: 主干]` 截空为空星，主空亡虚耗，落入截空宫位主事不成。 → 《形性赋》"最怕空亡"
  - `[ns_zwds_j1_077]` `[trigger: 白虎凶星]` `[factor_trigger: star_baihu]` `[role: 主干]` 白虎为凶星，主血光刑伤，官非横祸。 → 《形性赋》
  - `[ns_zwds_j1_078]` `[trigger: 丧门丧星]` `[factor_trigger: star_sangmen]` `[role: 主干]` 丧门为丧星，主丧亡哭泣，不利六亲。 → 《形性赋》
  - `[ns_zwds_j1_079]` `[trigger: 病符病星]` `[factor_trigger: star_bingfu]` `[role: 主干]` 病符为病星，主疾病缠身，体弱多病。 → 《形性赋》
  - `[ns_zwds_j1_080]` `[trigger: 官符讼星]` `[factor_trigger: star_guanfu]` `[role: 主干]` 官符为讼星，主官非诉讼，是非口舌。 → 《形性赋》
  - `[ns_zwds_j1_081]` `[trigger: 斗君流星]` `[factor_trigger: star_doujun]` `[role: 主干]` 斗君为流年之主，主流年吉凶应期。 → 《形性赋》
  - `[ns_zwds_j1_082]` `[trigger: 火铃组合]` `[factor_trigger: star_huoling]` `[role: 条件分支]` 火铃二星同会，主急躁暴烈，性情偏激。 → 《形性赋》"火铃似豫让，吞炭装哑"
  - `[ns_zwds_j1_083]` `[trigger: 魁钺同行]` `[factor_trigger: star_tiankui_tianyue]` `[role: 条件分支]` 魁钺二星同行，主贵人扶持，位居台辅。 → 《形性赋》
  - `[ns_zwds_j1_084]` `[trigger: 丧门白虎]` `[factor_trigger: star_sangmenbaihu]` `[role: 条件分支]` 丧门白虎同会，主丧亡血光，重大灾祸。 → 《形性赋》
  - `[ns_zwds_j1_085]` `[trigger: 丧门病符]` `[factor_trigger: star_sangmenbingfu]` `[role: 条件分支]` 丧门病符同会，主疾病丧亡，不利六亲。 → 《形性赋》
  - `[ns_zwds_j1_086]` `[trigger: 身宫位置]` `[factor_trigger: palace_shen]` `[role: 主干]` 身宫为后天之身，主行为表现与际遇变化。 → 《形性赋》"身命"
  - `[ns_zwds_j1_087]` `[trigger: 命宫定位]` `[factor_trigger: palace_ming]` `[role: 主干]` 命宫为先天之命，主格局高低与性格特质。 → 《形性赋》"身命"
  - `[ns_zwds_j1_111]` `[trigger: 命结果]` `[factor_trigger: result_ming]` `[role: 结果]` 命结果为命格整体吉凶的判断。 → 《形性赋》
  - `[ns_zwds_j1_112]` `[trigger: 官职结果]` `[factor_trigger: result_guanzhi]` `[role: 结果]` 官职结果为官禄地位的判断。 → 《形性赋》
  - `[ns_zwds_j1_113]` `[trigger: 分析结果]` `[factor_trigger: result_analysis]` `[role: 结果]` 分析结果为命盘综合分析的判断。 → 《形性赋》
  - `[ns_zwds_j1_114]` `[trigger: 掌兵权结果]` `[factor_trigger: result_zhangbingquan]` `[role: 结果]` 掌兵权结果为掌握权力的贵格判断。 → 《形性赋》
  - `[ns_zwds_j1_115]` `[trigger: 地劫劫忌煞]` `[factor_trigger: malefic_dijie_jie_ji]` `[role: 条件分支]` 地劫劫忌煞为地劫与化忌的凶险组合。 → 《形性赋》
  - `[ns_zwds_j1_116]` `[trigger: 精神之养]` `[factor_trigger: affliction_jingshen_zhi_yang]` `[role: 条件分支]` 精神之养为精神修养的状态因子。 → 《形性赋》
  - `[ns_zwds_j1_117]` `[trigger: 不得其死结果]` `[factor_trigger: result_bude_qisi]` `[role: 结果]` 不得其死结果为非正常死亡的凶险判断。 → 《形性赋》
  - `[ns_zwds_j1_118]` `[trigger: 文武双全质量]` `[factor_trigger: quality_wenwu_shuangquan]` `[role: 主干]` 文武双全质量为文武兼备的优良特质。 → 《形性赋》
  - `[ns_zwds_j1_119]` `[trigger: 狂邪之忌]` `[factor_trigger: affliction_kuangxie_zhiji]` `[role: 条件分支]` 狂邪之忌为狂妄邪僻的凶险特质。 → 《形性赋》
  - `[ns_zwds_j1_120]` `[trigger: 男阳女阴质量]` `[factor_trigger: quality_nanyang_biyi]` `[role: 主干]` 男阳女阴质量为阴阳配合的评判标准。 → 《形性赋》
  - `[ns_zwds_j1_121]` `[trigger: 宜主隐欲质量]` `[factor_trigger: quality_yi_zhu_yinyu]` `[role: 主干]` 宜主隐欲质量为内敛低调的性格特质。 → 《形性赋》
  - `[ns_zwds_j1_122]` `[trigger: 女命不宜质量]` `[factor_trigger: quality_nvming_buyi]` `[role: 条件分支]` 女命不宜质量为女命忌讳的配置。 → 《形性赋》
  - `[ns_zwds_j1_123]` `[trigger: 七杀临身煞]` `[factor_trigger: malefic_qisha_linshen]` `[role: 条件分支]` 七杀临身煞为七杀入身宫的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_124]` `[trigger: 空亡状态]` `[factor_trigger: state_kongwang]` `[role: 主干]` 空亡状态为星曜落入空亡的虚耗状态。 → 《形性赋》"最怕空亡"
  - `[ns_zwds_j1_125]` `[trigger: 金水相生]` `[factor_trigger: wuxing_jinshui_xiangsheng]` `[role: 条件分支]` 金水相生为金生水的五行相生配置。 → 《形性赋》
  - `[ns_zwds_j1_126]` `[trigger: 金水文贵结果]` `[factor_trigger: result_jinshui_wengui]` `[role: 结果]` 金水文贵结果为金水相生主文贵的判断。 → 《形性赋》
  - `[ns_zwds_j1_127]` `[trigger: 百步穿杨]` `[factor_trigger: symbol_baibu_chuanyang]` `[role: 主干]` 百步穿杨为精准射中的象征，主技艺精湛。 → 《形性赋》
  - `[ns_zwds_j1_128]` `[trigger: 贪狼遇火格]` `[factor_trigger: star_tanlang_yuohuo]` `[role: 条件分支]` 贪狼遇火格为贪狼与火星同宫的格局。 → 《形性赋》
  - `[ns_zwds_j1_129]` `[trigger: 火贪身垣格]` `[factor_trigger: pattern_huotan_shenyuan]` `[role: 条件分支]` 火贪身垣格为火星贪狼在身宫的格局。 → 《形性赋》
  - `[ns_zwds_j1_130]` `[trigger: 天梁贵结果]` `[factor_trigger: result_tianliang_gui]` `[role: 结果]` 天梁贵结果为天梁星主贵的判断。 → 《形性赋》
  - `[ns_zwds_j1_131]` `[trigger: 紫府福命结果]` `[factor_trigger: result_zifu_fuming]` `[role: 结果]` 紫府福命结果为紫微天府守命主福的判断。 → 《形性赋》
  - `[ns_zwds_j1_132]` `[trigger: 天府大富结果]` `[factor_trigger: result_tianfu_dafu]` `[role: 结果]` 天府大富结果为天府主大富的判断。 → 《形性赋》
  - `[ns_zwds_j1_133]` `[trigger: 随限福命结果]` `[factor_trigger: result_suixian_fuming]` `[role: 结果]` 随限福命结果为限运决定福命的判断。 → 《形性赋》
  - `[ns_zwds_j1_134]` `[trigger: 武曲福命结果]` `[factor_trigger: result_wuqu_fuming]` `[role: 结果]` 武曲福命结果为武曲守命主福的判断。 → 《形性赋》
  - `[ns_zwds_j1_135]` `[trigger: 巨门辰戌陷]` `[factor_trigger: star_jumen_chenxu_xian]` `[role: 条件分支]` 巨门辰戌陷为巨门在辰戌落陷的配置。 → 《形性赋》
  - `[ns_zwds_j1_136]` `[trigger: 暴亡结果]` `[factor_trigger: result_baowang]` `[role: 结果]` 暴亡结果为暴病暴死的凶险判断。 → 《形性赋》
  - `[ns_zwds_j1_137]` `[trigger: 天罗流羊陀格]` `[factor_trigger: pattern_tianluoliuyangtuo]` `[role: 条件分支]` 天罗流羊陀格为天罗遇流羊陀的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_138]` `[trigger: 巨日同宫格]` `[factor_trigger: pattern_juritonggong]` `[role: 条件分支]` 巨日同宫格为巨门太阳同宫的格局。 → 《形性赋》
  - `[ns_zwds_j1_139]` `[trigger: 晚成结果]` `[factor_trigger: result_wancheng]` `[role: 结果]` 晚成结果为大器晚成的判断。 → 《形性赋》
  - `[ns_zwds_j1_140]` `[trigger: 擎羊败地格]` `[factor_trigger: pattern_qingyangbaidi]` `[role: 条件分支]` 擎羊败地格为擎羊在败地的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_141]` `[trigger: 禄马倒行格]` `[factor_trigger: pattern_lumadaoxing]` `[role: 条件分支]` 禄马倒行格为禄存天马倒行的配置。 → 《形性赋》
  - `[ns_zwds_j1_142]` `[trigger: 七杀朝斗格]` `[factor_trigger: pattern_qishachaodou]` `[role: 条件分支]` 七杀朝斗格为七杀朝斗的贵格。 → 《形性赋》
  - `[ns_zwds_j1_143]` `[trigger: 天伤天空天使组合]` `[factor_trigger: pattern_tianshangtiankongtianshi]` `[role: 条件分支]` 天伤天空天使组合为凶险的三星组合。 → 《形性赋》
  - `[ns_zwds_j1_144]` `[trigger: 流羊冲命格]` `[factor_trigger: pattern_liuyangchongming]` `[role: 条件分支]` 流羊冲命格为流年擎羊冲命的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_145]` `[trigger: 左右科禄格]` `[factor_trigger: pattern_zuoyoukelu]` `[role: 条件分支]` 左右科禄格为左右与科禄同会的贵格。 → 《形性赋》
  - `[ns_zwds_j1_146]` `[trigger: 命理结果]` `[factor_trigger: result_mingli]` `[role: 结果]` 命理结果为命格整体判断。 → 《形性赋》
  - `[ns_zwds_j1_147]` `[trigger: 子生寅申忌]` `[factor_trigger: taboo_zishengyinshen]` `[role: 条件分支]` 子生寅申忌为子年生人寅申的忌讳。 → 《形性赋》
  - `[ns_zwds_j1_148]` `[trigger: 吉险结果]` `[factor_trigger: result_jixian]` `[role: 结果]` 吉险结果为吉凶参半的判断。 → 《形性赋》
  - `[ns_zwds_j1_149]` `[trigger: 丙申年]` `[factor_trigger: year_bingshen]` `[role: 主干]` 丙申年为特定的年份配置。 → 《形性赋》
  - `[ns_zwds_j1_150]` `[trigger: 左右贵格]` `[factor_trigger: pattern_zuoyouguige]` `[role: 条件分支]` 左右贵格为左右辅佐的贵人格局。 → 《形性赋》
  - `[ns_zwds_j1_151]` `[trigger: 攀天折枝喻]` `[factor_trigger: metaphor_bantianzhezhi]` `[role: 主干]` 攀天折枝喻为攀登高位的比喻。 → 《形性赋》
  - `[ns_zwds_j1_152]` `[trigger: 劫空会脑格]` `[factor_trigger: pattern_jiekonghuinao]` `[role: 条件分支]` 劫空会脑格为地劫地空会合的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_153]` `[trigger: 七杀紫府格]` `[factor_trigger: pattern_qishazifuge]` `[role: 条件分支]` 七杀紫府格为七杀与紫府的组合格局。 → 《形性赋》
  - `[ns_zwds_j1_154]` `[trigger: 乘马格]` `[factor_trigger: pattern_chenma]` `[role: 条件分支]` 乘马格为天马的配置格局。 → 《形性赋》
  - `[ns_zwds_j1_155]` `[trigger: 羊陀叠并格]` `[factor_trigger: pattern_yangtuodiebing]` `[role: 条件分支]` 羊陀叠并格为擎羊陀罗叠加的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_156]` `[trigger: 府相科禄格]` `[factor_trigger: pattern_fuxiangkelu]` `[role: 条件分支]` 府相科禄格为府相与科禄同会的贵格。 → 《形性赋》
  - `[ns_zwds_j1_157]` `[trigger: 劫空在命格]` `[factor_trigger: pattern_jiekongzaiming]` `[role: 条件分支]` 劫空在命格为地劫地空在命宫的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_158]` `[trigger: 七杀羊陀冲格]` `[factor_trigger: pattern_qishayangtuochong]` `[role: 条件分支]` 七杀羊陀冲格为七杀与羊陀冲照的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_159]` `[trigger: 文星昂宫格]` `[factor_trigger: pattern_wenxinganggong]` `[role: 条件分支]` 文星昂宫格为文星在昂宫的格局。 → 《形性赋》
  - `[ns_zwds_j1_160]` `[trigger: 登科结果]` `[factor_trigger: result_dengke]` `[role: 结果]` 登科结果为科举登第的贵显判断。 → 《形性赋》
  - `[ns_zwds_j1_161]` `[trigger: 四墓群]` `[factor_trigger: group_simu]` `[role: 主干]` 四墓群为辰戌丑未四墓宫的统称。 → 《形性赋》
  - `[ns_zwds_j1_162]` `[trigger: 四墓地群]` `[factor_trigger: group_simudi]` `[role: 主干]` 四墓地群为四墓宫位的组合。 → 《形性赋》
  - `[ns_zwds_j1_163]` `[trigger: 四煞空劫群]` `[factor_trigger: group_sishakongjie]` `[role: 主干]` 四煞空劫群为四煞与空劫的组合。 → 《形性赋》
  - `[ns_zwds_j1_164]` `[trigger: 四余群]` `[factor_trigger: group_siyu]` `[role: 主干]` 四余群为四余星的组合。 → 《形性赋》
  - `[ns_zwds_j1_165]` `[trigger: 四正群]` `[factor_trigger: group_sizheng]` `[role: 主干]` 四正群为子午卯酉四正宫的统称。 → 《形性赋》
  - `[ns_zwds_j1_166]` `[trigger: 所值吉星群]` `[factor_trigger: group_suozhijixing]` `[role: 主干]` 所值吉星群为所值之吉星的组合。 → 《形性赋》
  - `[ns_zwds_j1_167]` `[trigger: 小儿身煞群]` `[factor_trigger: group_xiaoershensha]` `[role: 主干]` 小儿身煞群为小儿关煞的组合。 → 《形性赋》
  - `[ns_zwds_j1_168]` `[trigger: 贵格星曜]` `[factor_trigger: guige_xingyao]` `[role: 主干]` 贵格星曜为贵格相关的星曜配置。 → 《形性赋》
  - `[ns_zwds_j1_169]` `[trigger: 贵人配合]` `[factor_trigger: guiren_peihe]` `[role: 主干]` 贵人配合为贵人星曜的配合关系。 → 《形性赋》
  - `[ns_zwds_j1_170]` `[trigger: 古科刑科]` `[factor_trigger: guke_xingke]` `[role: 主干]` 古科刑科为古法科名与刑克的关系。 → 《形性赋》
  - `[ns_zwds_j1_171]` `[trigger: 化曜加持]` `[factor_trigger: huayao_jiachi]` `[role: 主干]` 化曜加持为四化星的加持效果。 → 《形性赋》
  - `[ns_zwds_j1_172]` `[trigger: 甲格层级]` `[factor_trigger: jiage_cengci]` `[role: 主干]` 甲格层级为甲级格局的层级分类。 → 《形性赋》
  - `[ns_zwds_j1_173]` `[trigger: 甲格类型]` `[factor_trigger: jiage_leixing]` `[role: 主干]` 甲格类型为甲级格局的类型。 → 《形性赋》
  - `[ns_zwds_j1_174]` `[trigger: 将相之才]` `[factor_trigger: jiangxiang_zhicai]` `[role: 结果]` 将相之才为武将宰相的才能判断。 → 《形性赋》
  - `[ns_zwds_j1_175]` `[trigger: 夹星组合]` `[factor_trigger: jiaxing_zuhe]` `[role: 主干]` 夹星组合为夹命夹身的配置。 → 《形性赋》
  - `[ns_zwds_j1_176]` `[trigger: 吉星密度检查]` `[factor_trigger: jixing_density_check]` `[role: 主干]` 吉星密度检查为吉星聚会密度的检查。 → 《形性赋》
  - `[ns_zwds_j1_177]` `[trigger: 吉星甲格]` `[factor_trigger: jixing_jiage]` `[role: 主干]` 吉星甲格为吉星甲级格局的配置。 → 《形性赋》
  - `[ns_zwds_j1_178]` `[trigger: 吉星配合]` `[factor_trigger: jixing_peihe]` `[role: 主干]` 吉星配合为吉星之间的配合关系。 → 《形性赋》
  - `[ns_zwds_j1_179]` `[trigger: 忌曜风险]` `[factor_trigger: jiyao_fengxian]` `[role: 主干]` 忌曜风险为化忌星的风险评估。 → 《形性赋》
  - `[ns_zwds_j1_180]` `[trigger: 空亡破耗]` `[factor_trigger: kongwang_pohao]` `[role: 主干]` 空亡破耗为空亡与破耗的组合。 → 《形性赋》
  - `[ns_zwds_j1_181]` `[trigger: 魁钺贵星]` `[factor_trigger: kuiyue_guixing]` `[role: 主干]` 魁钺贵星为天魁天钺的贵星配置。 → 《形性赋》
  - `[ns_zwds_j1_182]` `[trigger: 枯木逢春格]` `[factor_trigger: kumufengchun]` `[role: 条件分支]` 枯木逢春格为晚年转运的格局。 → 《形性赋》
  - `[ns_zwds_j1_183]` `[trigger: 书格层级]` `[factor_trigger: level_shuge]` `[role: 主干]` 书格层级为文书格局的层级。 → 《形性赋》
  - `[ns_zwds_j1_184]` `[trigger: 星格层级]` `[factor_trigger: level_xingge]` `[role: 主干]` 星格层级为星曜格局的层级。 → 《形性赋》
  - `[ns_zwds_j1_185]` `[trigger: 流动吉类]` `[factor_trigger: liudong_jilei]` `[role: 主干]` 流动吉类为流年吉星的分类。 → 《形性赋》
  - `[ns_zwds_j1_186]` `[trigger: 空劫身命格]` `[factor_trigger: pattern_kongjieshenming]` `[role: 条件分支]` 空劫身命格为空劫在身命的凶险配置。 → 《形性赋》
  - `[ns_zwds_j1_187]` `[trigger: 魁钺夹命格]` `[factor_trigger: pattern_kuiyue_jiaming]` `[role: 条件分支]` 魁钺夹命格为魁钺夹命的贵格。 → 《形性赋》
  - `[ns_zwds_j1_188]` `[trigger: 魁钺三合格]` `[factor_trigger: pattern_kuiyue_sanhe]` `[role: 条件分支]` 魁钺三合格为魁钺三合的贵格。 → 《形性赋》
  - `[ns_zwds_j1_189]` `[trigger: 魁钺迎解格]` `[factor_trigger: pattern_kuiyue_yingjie]` `[role: 条件分支]` 魁钺迎解格为魁钺迎解的贵格。 → 《形性赋》
  - `[ns_zwds_j1_190]` `[trigger: 廉破卯酉格]` `[factor_trigger: pattern_lianpomaoyu]` `[role: 条件分支]` 廉破卯酉格为廉贞破军在卯酉的格局。 → 《形性赋》
  - `[ns_zwds_j1_191]` `[trigger: 廉贞七杀格]` `[factor_trigger: pattern_lianzhen_qisha]` `[role: 条件分支]` 廉贞七杀格为廉贞七杀的格局。 → 《形性赋》
  - `[ns_zwds_j1_192]` `[trigger: 禄无位格]` `[factor_trigger: pattern_lu_wuwei]` `[role: 条件分支]` 禄无位格为禄星无位的配置。 → 《形性赋》
  - `[ns_zwds_j1_193]` `[trigger: 禄合加会格]` `[factor_trigger: pattern_luhe_jiahui]` `[role: 条件分支]` 禄合加会格为禄合加会的贵格。 → 《形性赋》
  - `[ns_zwds_j1_194]` `[trigger: 禄科聚会格]` `[factor_trigger: pattern_luke_juhui]` `[role: 条件分支]` 禄科聚会格为禄科聚会的贵格。 → 《形性赋》
  - `[ns_zwds_j1_195]` `[trigger: 禄马扶身格]` `[factor_trigger: pattern_luma_fushen]` `[role: 条件分支]` 禄马扶身格为禄马扶身的贵格。 → 《形性赋》
  - `[ns_zwds_j1_196]` `[trigger: 落陷不逢克战格]` `[factor_trigger: pattern_luoxian_bufeng_kezhan]` `[role: 条件分支]` 落陷不逢克战格为落陷不逢克战的配置。 → 《形性赋》
  - `[ns_zwds_j1_197]` `[trigger: 禄权加会格]` `[factor_trigger: pattern_luquan_jiahui]` `[role: 条件分支]` 禄权加会格为禄权加会的贵格。 → 《形性赋》
  - `[ns_zwds_j1_198]` `[trigger: 禄权左守格]` `[factor_trigger: pattern_luquan_zuoshou]` `[role: 条件分支]` 禄权左守格为禄权与左辅的贵格。 → 《形性赋》
  - `[ns_zwds_j1_199]` `[trigger: 禄权科合格]` `[factor_trigger: pattern_luquanke_he]` `[role: 条件分支]` 禄权科合格为禄权科合的极贵格局。 → 《形性赋》
  - `[ns_zwds_j1_200]` `[trigger: 吕后专权格]` `[factor_trigger: pattern_lvhou_zhuanquan]` `[role: 条件分支]` 吕后专权格为女命专权的凶险格局。 → 《形性赋》
  - `[ns_zwds_j1_201]` `[trigger: 马头带剑格2]` `[factor_trigger: pattern_matou_daijian]` `[role: 条件分支]` 马头带剑格为天马擎羊的格局。 → 《形性赋》
  - `[ns_zwds_j1_202]` `[trigger: 命无正曜格]` `[factor_trigger: pattern_ming_wu_zhengyao]` `[role: 条件分支]` 命无正曜格为命宫无正曜的配置。 → 《形性赋》
  - `[ns_zwds_j1_203]` `[trigger: 明珠两照格]` `[factor_trigger: pattern_mingzhu_liangzhao]` `[role: 条件分支]` 明珠两照格为明珠两照的贵格。 → 《形性赋》
  - `[ns_zwds_j1_204]` `[trigger: 七杀朝斗格2]` `[factor_trigger: pattern_qisha_chaodou]` `[role: 条件分支]` 七杀朝斗格为七杀朝斗的贵格。 → 《形性赋》
  - `[ns_zwds_j1_205]` `[trigger: 七杀单居格]` `[factor_trigger: pattern_qishadanju]` `[role: 条件分支]` 七杀单居格为七杀单居的格局。 → 《形性赋》
  - `[ns_zwds_j1_206]` `[trigger: 权会巨门格]` `[factor_trigger: pattern_quan_hui_jumen]` `[role: 条件分支]` 权会巨门格为化权会巨门的格局。 → 《形性赋》
  - `[ns_zwds_j1_207]` `[trigger: 权禄拱照格]` `[factor_trigger: pattern_quanlu_gongzhao]` `[role: 条件分支]` 权禄拱照格为权禄拱照的贵格。 → 《形性赋》
  - `[ns_zwds_j1_208]` `[trigger: 权禄会合格]` `[factor_trigger: pattern_quanlu_huihe]` `[role: 条件分支]` 权禄会合格为权禄会合的贵格。 → 《形性赋》
  - `[ns_zwds_j1_209]` `[trigger: 权禄加会格]` `[factor_trigger: pattern_quanlu_jiahui]` `[role: 条件分支]` 权禄加会格为权禄加会的贵格。 → 《形性赋》
  - `[ns_zwds_j1_210]` `[trigger: 权禄守财格]` `[factor_trigger: pattern_quanlu_shoucai]` `[role: 条件分支]` 权禄守财格为权禄守财的富格。 → 《形性赋》
  - `[ns_zwds_j1_211]` `[trigger: 不能发达结果]` `[factor_trigger: result_bunengfada]` `[role: 结果]` 不能发达结果为不能发达的判断。 → 《形性赋》
  - `[ns_zwds_j1_212]` `[trigger: 财不误结果]` `[factor_trigger: result_caibuwu]` `[role: 结果]` 财不误结果为财不误的判断。 → 《形性赋》
  - `[ns_zwds_j1_213]` `[trigger: 财官结果]` `[factor_trigger: result_caiguan]` `[role: 结果]` 财官结果为财官的判断。 → 《形性赋》
  - `[ns_zwds_j1_214]` `[trigger: 长寿结果]` `[factor_trigger: result_changshou]` `[role: 结果]` 长寿结果为长寿的判断。 → 《形性赋》
  - `[ns_zwds_j1_215]` `[trigger: 出将出相结果]` `[factor_trigger: result_chujiangchuxiang]` `[role: 结果]` 出将出相结果为出将出相的判断。 → 《形性赋》
  - `[ns_zwds_j1_216]` `[trigger: 出仕结果]` `[factor_trigger: result_chushi]` `[role: 结果]` 出仕结果为出仕的判断。 → 《形性赋》
  - `[ns_zwds_j1_217]` `[trigger: 达结果]` `[factor_trigger: result_da]` `[role: 结果]` 达结果为发达的判断。 → 《形性赋》
  - `[ns_zwds_j1_218]` `[trigger: 短福结果]` `[factor_trigger: result_duanfu]` `[role: 结果]` 短福结果为短福的判断。 → 《形性赋》
  - `[ns_zwds_j1_219]` `[trigger: 多才多能结果]` `[factor_trigger: result_duocai_duoneng]` `[role: 结果]` 多才多能结果为多才多能的判断。 → 《形性赋》
  - `[ns_zwds_j1_220]` `[trigger: 二品结果]` `[factor_trigger: result_erpin]` `[role: 结果]` 二品结果为二品的判断。 → 《形性赋》
  - `[ns_zwds_j1_221]` `[trigger: 奉献结果]` `[factor_trigger: result_fengxian]` `[role: 结果]` 奉献结果为奉献的判断。 → 《形性赋》
  - `[ns_zwds_j1_222]` `[trigger: 富贵必宜结果]` `[factor_trigger: result_fugui_biyi]` `[role: 结果]` 富贵必宜结果为富贵必宜的判断。 → 《形性赋》
  - `[ns_zwds_j1_223]` `[trigger: 富贵全美结果]` `[factor_trigger: result_fugui_quanmei]` `[role: 结果]` 富贵全美结果为富贵全美的判断。 → 《形性赋》
  - `[ns_zwds_j1_224]` `[trigger: 富贵双全结果]` `[factor_trigger: result_fugui_shuangquan]` `[role: 结果]` 富贵双全结果为富贵双全的判断。 → 《形性赋》
  - `[ns_zwds_j1_225]` `[trigger: 福厚结果]` `[factor_trigger: result_fuhou]` `[role: 结果]` 福厚结果为福厚的判断。 → 《形性赋》
  - `[ns_zwds_j1_226]` `[trigger: 福厚二品结果]` `[factor_trigger: result_fuhou_erpin]` `[role: 结果]` 福厚二品结果为福厚二品的判断。 → 《形性赋》
  - `[ns_zwds_j1_227]` `[trigger: 高强结果]` `[factor_trigger: result_gaoqiang]` `[role: 结果]` 高强结果为高强的判断。 → 《形性赋》
  - `[ns_zwds_j1_228]` `[trigger: 公门结果]` `[factor_trigger: result_gongmen]` `[role: 结果]` 公门结果为公门的判断。 → 《形性赋》
  - `[ns_zwds_j1_229]` `[trigger: 孤损寿结果]` `[factor_trigger: result_gu_sunshou]` `[role: 结果]` 孤损寿结果为孤损寿的判断。 → 《形性赋》
  - `[ns_zwds_j1_230]` `[trigger: 鬼体结果]` `[factor_trigger: result_guiti]` `[role: 结果]` 鬼体结果为鬼体的判断。 → 《形性赋》
  - `[ns_zwds_j1_231]` `[trigger: 合格局结果]` `[factor_trigger: result_hegejü]` `[role: 结果]` 合格局结果为合格局的判断。 → 《形性赋》
  - `[ns_zwds_j1_232]` `[trigger: 火贪贵结果]` `[factor_trigger: result_huotan_gui]` `[role: 结果]` 火贪贵结果为火贪贵的判断。 → 《形性赋》
  - `[ns_zwds_j1_233]` `[trigger: 吉结果]` `[factor_trigger: result_ji]` `[role: 结果]` 吉结果为吉的判断。 → 《形性赋》
  - `[ns_zwds_j1_234]` `[trigger: 兼寿结果]` `[factor_trigger: result_jianshou]` `[role: 结果]` 兼寿结果为兼寿的判断。 → 《形性赋》
  - `[ns_zwds_j1_235]` `[trigger: 九五结果]` `[factor_trigger: result_jiuwu]` `[role: 结果]` 九五结果为九五的判断。 → 《形性赋》
  - `[ns_zwds_j1_236]` `[trigger: 凶星数量]` `[factor_trigger: star_xiong_count]` `[role: 主干]` 凶星数量为凶星的数量。 → 《形性赋》
  - `[ns_zwds_j1_237]` `[trigger: 阳刃对宫入庙]` `[factor_trigger: star_yangren_duigong_rumiao]` `[role: 条件分支]` 阳刃对宫入庙为阳刃对宫入庙的配置。 → 《形性赋》
  - `[ns_zwds_j1_238]` `[trigger: 主星]` `[factor_trigger: star_zhu]` `[role: 主干]` 主星为命宫的主星。 → 《形性赋》
  - `[ns_zwds_j1_239]` `[trigger: 辰巳旺地状态]` `[factor_trigger: state_chensi_wangdi]` `[role: 主干]` 辰巳旺地状态为辰巳旺地的状态。 → 《形性赋》
  - `[ns_zwds_j1_240]` `[trigger: 倒限状态]` `[factor_trigger: state_daoxian]` `[role: 主干]` 倒限状态为倒限的状态。 → 《形性赋》
  - `[ns_zwds_j1_241]` `[trigger: 惊幻状态]` `[factor_trigger: state_jinghuan]` `[role: 主干]` 惊幻状态为惊幻的状态。 → 《形性赋》
  - `[ns_zwds_j1_242]` `[trigger: 吉凶会合状态]` `[factor_trigger: state_jixionghuihe]` `[role: 主干]` 吉凶会合状态为吉凶会合的状态。 → 《形性赋》
  - `[ns_zwds_j1_243]` `[trigger: 庙旺平陷状态]` `[factor_trigger: state_miaowangpingxian]` `[role: 主干]` 庙旺平陷状态为庙旺平陷的状态。 → 《形性赋》
  - `[ns_zwds_j1_244]` `[trigger: 庙陷状态]` `[factor_trigger: state_miaoxian]` `[role: 主干]` 庙陷状态为庙陷的状态。 → 《形性赋》
  - `[ns_zwds_j1_245]` `[trigger: 入庙状态]` `[factor_trigger: state_rumiao]` `[role: 主干]` 入庙状态为入庙的状态。 → 《形性赋》
  - `[ns_zwds_j1_246]` `[trigger: 生逢陷地状态]` `[factor_trigger: state_shengfengxiandi]` `[role: 主干]` 生逢陷地状态为生逢陷地的状态。 → 《形性赋》
  - `[ns_zwds_j1_247]` `[trigger: 太岁并小限状态]` `[factor_trigger: state_taisuibingxiaoxian]` `[role: 主干]` 太岁并小限状态为太岁并小限的状态。 → 《形性赋》
  - `[ns_zwds_j1_248]` `[trigger: 太岁刑命宫状态]` `[factor_trigger: state_taisuixingminggong]` `[role: 主干]` 太岁刑命宫状态为太岁刑命宫的状态。 → 《形性赋》
  - `[ns_zwds_j1_249]` `[trigger: 陷不逢凶状态]` `[factor_trigger: state_xianbufengxiong]` `[role: 主干]` 陷不逢凶状态为陷不逢凶的状态。 → 《形性赋》
  - `[ns_zwds_j1_250]` `[trigger: 阴阳反背状态]` `[factor_trigger: state_yinyangfanbei]` `[role: 主干]` 阴阳反背状态为阴阳反背的状态。 → 《形性赋》
  - `[ns_zwds_j1_251]` `[trigger: 百无子象征]` `[factor_trigger: symbol_baiwuzi]` `[role: 主干]` 百无子象征为百无子的象征。 → 《形性赋》
  - `[ns_zwds_j1_252]` `[trigger: 不蟾折桂象征]` `[factor_trigger: symbol_buchan_zhegui]` `[role: 主干]` 不蟾折桂象征为不蟾折桂的象征。 → 《形性赋》
  - `[ns_zwds_j1_253]` `[trigger: 洞宾仙师象征]` `[factor_trigger: symbol_dongbin_xianshi]` `[role: 主干]` 洞宾仙师象征为洞宾仙师的象征。 → 《形性赋》
  - `[ns_zwds_j1_254]` `[trigger: 对皇极拜象征]` `[factor_trigger: symbol_duihuang_jibai]` `[role: 主干]` 对皇极拜象征为对皇极拜的象征。 → 《形性赋》
  - `[ns_zwds_j1_255]` `[trigger: 封诰几贵象征]` `[factor_trigger: symbol_fengao_jigui]` `[role: 主干]` 封诰几贵象征为封诰几贵的象征。 → 《形性赋》
  - `[ns_zwds_j1_256]` `[trigger: 焚舟济绝战象征]` `[factor_trigger: symbol_fenzhouji_juezhan]` `[role: 主干]` 焚舟济绝战象征为焚舟济绝战的象征。 → 《形性赋》
  - `[ns_zwds_j1_257]` `[trigger: 负驮囊象征]` `[factor_trigger: symbol_fu_tuonang]` `[role: 主干]` 负驮囊象征为负驮囊的象征。 → 《形性赋》
  - `[ns_zwds_j1_258]` `[trigger: 合贵华表象征]` `[factor_trigger: symbol_heguihuabiao]` `[role: 主干]` 合贵华表象征为合贵华表的象征。 → 《形性赋》
  - `[ns_zwds_j1_259]` `[trigger: 黄粱梦象征]` `[factor_trigger: symbol_huangliangmeng]` `[role: 主干]` 黄粱梦象征为黄粱梦的象征。 → 《形性赋》
  - `[ns_zwds_j1_260]` `[trigger: 镜破一分象征]` `[factor_trigger: symbol_jingpo_yifen]` `[role: 主干]` 镜破一分象征为镜破一分的象征。 → 《形性赋》
  - `[ns_zwds_j1_261]` `[trigger: 家庭类型]` `[factor_trigger: type_jiating]` `[role: 主干]` 家庭类型为家庭的类型。 → 《形性赋》
  - `[ns_zwds_j1_262]` `[trigger: 男命类型]` `[factor_trigger: type_nanming]` `[role: 主干]` 男命类型为男命的类型。 → 《形性赋》
  - `[ns_zwds_j1_263]` `[trigger: 女命类型]` `[factor_trigger: type_nvming]` `[role: 主干]` 女命类型为女命的类型。 → 《形性赋》
  - `[ns_zwds_j1_264]` `[trigger: 生年支类型]` `[factor_trigger: type_shengnianzhi]` `[role: 主干]` 生年支类型为生年支的类型。 → 《形性赋》
  - `[ns_zwds_j1_265]` `[trigger: 双丁类型]` `[factor_trigger: type_shuangding]` `[role: 主干]` 双丁类型为双丁的类型。 → 《形性赋》
  - `[ns_zwds_j1_266]` `[trigger: 五行命类型]` `[factor_trigger: type_wuxingming]` `[role: 主干]` 五行命类型为五行命的类型。 → 《形性赋》
  - `[ns_zwds_j1_267]` `[trigger: 阳男阴女类型]` `[factor_trigger: type_yangnanyinnv]` `[role: 主干]` 阳男阴女类型为阳男阴女的类型。 → 《形性赋》
  - `[ns_zwds_j1_268]` `[trigger: 阴男阳女类型]` `[factor_trigger: type_yinnanyangnu]` `[role: 主干]` 阴男阳女类型为阴男阳女的类型。 → 《形性赋》
  - `[ns_zwds_j1_269]` `[trigger: 中庸之局类型]` `[factor_trigger: type_zhongyongzhiju]` `[role: 主干]` 中庸之局类型为中庸之局的类型。 → 《形性赋》
  - `[ns_zwds_j1_270]` `[trigger: 文武庙旺]` `[factor_trigger: wenwu_miaowang]` `[role: 主干]` 文武庙旺为文武庙旺的配置。 → 《形性赋》
  - `[ns_zwds_j1_271]` `[trigger: 五行制化]` `[factor_trigger: wuxing_zhihua]` `[role: 主干]` 五行制化为五行制化的关系。 → 《形性赋》
  - `[ns_zwds_j1_272]` `[trigger: 陷地失辉]` `[factor_trigger: xiandi_shihui]` `[role: 主干]` 陷地失辉为陷地失辉的配置。 → 《形性赋》
  - `[ns_zwds_j1_273]` `[trigger: 性格映射]` `[factor_trigger: xingge_yingshe]` `[role: 主干]` 性格映射为性格的映射。 → 《形性赋》
  - `[ns_zwds_j1_274]` `[trigger: 凶星聚集]` `[factor_trigger: xiongxing_juji]` `[role: 主干]` 凶星聚集为凶星聚集的配置。 → 《形性赋》
  - `[ns_zwds_j1_275]` `[trigger: 凶星组合]` `[factor_trigger: xiongxing_zuhe]` `[role: 主干]` 凶星组合为凶星的组合。 → 《形性赋》
  - `[ns_zwds_j1_276]` `[trigger: 制化关系]` `[factor_trigger: zhihua_guanxi]` `[role: 主干]` 制化关系为制化的关系。 → 《形性赋》
  - `[ns_zwds_j1_277]` `[trigger: 紫府照合]` `[factor_trigger: zifuzhaohe]` `[role: 主干]` 紫府照合为紫府照合的配置。 → 《形性赋》
  - `[ns_zwds_j1_278]` `[trigger: 子亥区域]` `[factor_trigger: zone_zihai]` `[role: 主干]` 子亥区域为子亥的区域。 → 《形性赋》"""
    normalized_text_zh: str = """"""
    subject: str = "形性赋总论"
    factor_refs: list = ['new_candidate', 'star_taiyang', 'star_taiyin', 'star_group_sha', 'star_santai', 'state_kongwang']
    
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
        l1_anchor="zw_v1.0.0_形性赋总论_001_L1",
    )
    version: str = "1.0.0"
