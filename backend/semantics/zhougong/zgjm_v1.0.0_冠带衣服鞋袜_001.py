"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864287
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
    semantic_id="zgjm_v1.0.0_冠带衣服鞋袜_001",
    book_id="zhougong",
    engine_id="dream"
)
class 冠带衣服鞋袜(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  冠带衣服鞋袜。

  【条文】

  戴官登车，官欲迁。
  自戴幞头巾帽，吉。
  簪冠登台，职位迁。

  贵人与之衣冠，吉。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  冠带衣服鞋袜。

  【条文】

  戴官登车，官欲迁。
  自戴幞头巾帽，吉。
  簪冠登台，职位迁。

  贵人与之衣冠，吉。
  新换衣冠，禄位至。
  烧毁冠帽，欲更官。

  失去冠帽，去退职。
  拾得官带，禄位至。
  与人公服，主得职。

  人与公服，加官职。
  女著冠带，主生子。
  洗笏染服，新官来。

  执笏见贵人，大吉。
  笏硫忧凶，三不祥。
  与人笏绶，主官迁。

  腰带者，主官至吉。
  文书用印，有名声。
  带印主妻，生贵子。

  著新袍，主添妻妾。
  著锦绣衣，子孙荣。
  洗染衣服，皆大吉。

  披蓑衣，主大恩至。
  被油污衣，大恩泽。
  衣服忽破，妻外心。

  新衣攒米，百事凶。
  与人衣服，主患至。
  裁衣着孛衣，皆吉。

  衣带自解，百事吉。
  著黄衣皂衣，皆吉。
  著白衣，主有人请。

  著青衣，神人助力。
  著蓝绣衣，妻大利。
  众人著紫，主情毙。

  与人著青，家人散。
  众人著白，主官事。
  众人著绯，大吉利。

  妻著夫衣，生贵子。
  女子着衣，平无事。
  与人共衣，妻私情。

  失却衣服，妻难产。
  好被自盖，得富贵。
  人著己履，妻有私。

  得靴鞋，主奴婢吉。
  失履，主奴婢逃走。
  脱靴束带，主有凶。

  鞋破，子孙妻妾病。
  著麻鞋，百事和合。
  新授官爵，主贵子。

  乞得鞋履，人助力。
  木履脱时，己出厄。

- 分字分词释义：

  - **冠带衣服鞋袜**：本类总纲，涵盖从头冠、腰带到衣袍、鞋履的一切“外在装束”，主要映照人的身份、地位、婚姻与日常人际。
  - **戴官登车，官欲迁**：头戴官帽登车，多主仕途调动，有升有迁，需结合后文条目判断吉凶方向。
  - **幞头巾帽**：古代平民、士人所戴之头巾、帽饰，自戴而整，多主自立其位、得适当之职分。
  - **簪冠登台，职位迁**：加冠登台，比喻登上更高台阶，职位升迁之象。
  - **贵人与之衣冠／人与公服**：贵人赐衣冠、公服，象征被纳入某一体系或机构之中，得其认可与庇护。
  - **新换衣冠，禄位至；洗笏染服，新官来**：更换衣冠、洗刷笏板与衣服，皆是“更新形象、准备新任”的象征，多主调任新职或获得新权责。
  - **烧毁冠帽，欲更官；失去冠帽，去退职**：冠帽被烧毁或失落，多与旧官职的终结、退职或改任相关。
  - **拾得官带，禄位至；腰带者主官至吉**：拾得或佩戴官带，主得禄位与权责，多关“实在的职权”而非虚名。
  - **笏、笏绶、文书用印、带印**：皆为官方凭证或权力象征：
    - 执笏见贵人，主见高位者、获赏识；
    - 文书用印，有名声；
    - 带印主妻生贵子，则将权印与家庭福分相连。
  - **新袍、锦绣衣、洗染衣服**：新衣与锦绣象征荣华与外在光彩；洗染则指更新旧衣，多主家运与面子工程双双提升。
  - **披蓑衣／被油污衣**：蓑衣多与风雨、田野相关，被视为“艰难中受护”的象征；油污衣则暗示虽有劳作，却获上位者的大恩与优待。
  - **衣服忽破，妻外心；妻著夫衣，生贵子；与人共衣，妻私情**：衣服与“配偶角色”强相关：衣破、共衣常被解为婚姻关系中的裂痕或私情。
  - **新衣攒米，百事凶；与人衣服，主患至**：新衣攒米，本为攒聚之象，却被视为虚胖与空耗；赠与衣服则暗示把自身防护与运气交出，易招烦患。
  - **衣带自解，百事吉**：衣带自解，古解多作“束缚解开”，百事顺解。
  - **黄衣、皂衣、白衣、青衣、蓝绣衣、紫衣、绯衣**：衣色各有所主：
    - 黄、皂多与尊严、中正、持重相关；
    - 白衣在此主有人邀请，较前类“自身白衣人所谋”略有差别；
    - 青衣得神人助力，偏向精神或隐形庇护；
    - 蓝绣衣利妻家；
    - 紫衣象贵，但“众人著紫主情毙”，说的是群体情感压抑或情势僵化。
  - **与人著青／众人著白／众人著绯**：多人同色衣服，多主集体事件：
    - 与人著青，家人散；
    - 众人著白，多关官事、诉讼与哀丧；
    - 众人著绯，则主喜庆与集体吉利。
  - **鞋履、靴、木履**：脚下之物，多关根基、人际与奴仆：
    - 得靴鞋主奴婢吉、有人辅助；
    - 失履、鞋破多主奴婢离散及妻妾、子孙之病；
    - 脱靴束带主有凶，提示在卸下防护或松懈之时易出事；
    - 木履脱时己出厄，则象征摆脱旧束缚、出险境。

- **规范化释义（primary_lang_explained）**：

  本类通过“头冠、衣袍、腰带、鞋履”等外在装束，来反映一个人在**仕途、婚姻与日常人际**中的位置变化。

  大致而言：

  - **冠带、公服、笏印类的梦象，重在官职与权责的升降。**
  - **衣袍、颜色、共衣、破衣之梦，则多映照婚姻与家庭气氛。**
  - **鞋履与靴履的梦，则关联脚下根基、部属与生活支持系统的稳与不稳。**

- 核心要点：

  - **看“冠带、公服、笏印”——官与职的进退：**
    - 受赐衣冠、公服、官带，多主得职得禄；
    - 烧毁、失去冠帽，主旧职告终或退居次位；
    - 洗笏染服、新换衣冠，则偏向“换岗”“转任”，不专指升或降。
  - **看“衣的状态与归属”——婚姻与家庭结构：**
    - 新袍、锦绣衣多主荣华与妻妾添增；
    - 衣破、共衣、妻著夫衣、人著己履等象，常涉及配偶忠诚与边界模糊；
    - 与人互换或共用衣物，提示角色与界限正在被打乱。
  - **看“衣色与群体”——事件性质与情绪氛围：**
    - 黄、皂、绯多偏吉；青与神灵、隐助相连；白与哀丧、官事相关；
    - 众人同色时，常指集体事件（如官事、喜宴或某类风潮）。
  - **看“鞋履与木履”——根基与支持系统：**
    - 鞋履完好、得靴鞋，主部属听命、生活便利；
    - 鞋破、失履，则多主支撑系统有洞，奴婢或下属离心。

- 详细解说：

  **（一）冠、带、公服与笏印：仕途与权责之象**

  - “戴官登车，官欲迁”“簪冠登台，职位迁”“贵人与之衣冠吉”“人与公服加官职”几条合看，可见：
    - 冠与公服，象征正式的官职身份；
    - 登车、登台，则是“登高”的动态；
    - 若同时有贵人赐与或与之同服，则升迁之象更明显。
  - “新换衣冠，禄位至”“洗笏染服，新官来”强调“换装”的重要性：旧衣换新衣、旧笏洗净，表示卸下旧职、迎接新任，是改革与调整的好时机。
  - “烧毁冠帽，欲更官”“失去冠帽，去退职”则提示原有职位、光环之破落：
    - 若梦者本就厌倦旧职，此梦或示“脱壳换生”；
    - 若对旧职依恋，则应警惕主动与被动的失位之险。
  - “执笏见贵人大吉”“笏硫忧凶三不祥”“与人笏绶主官迁”说明：
    - 执笏见贵人，多主得到高位者肯定；
    - 若笏上污浊、有裂等，则为“忧凶三不祥”，暗示权柄受损；
    - 与人互换笏绶，则可能是职位轮替、职责转移的象征.

  **（二）袍服、新衣与洗染：外在形象与内在资源**

  - “著新袍主添妻妾”“著锦绣衣子孙荣”“洗染衣服皆大吉”将新袍、锦绣与“添妻妾、子孙荣”连根，使外在装束成为家庭资源与荣光的载体.
  - “披蓑衣主大恩至”“被油污衣大恩泽”则偏向“劳中得恩”：
    - 披蓑衣是风雨中劳作之象，多主在艰难环境中得到照应或恩典；
    - 衣被油污，显示与工事、饮食或机械有关，虽显辛苦，却有上位者嘉奖.

  **（三）衣色与群体服饰：事件性质与情绪场**

  - “著黄衣皂衣皆吉”“著白衣主有人请”“著青衣神人助力”“著蓝绣衣妻大利”“众人著紫主情毙”“众人著白主官事”“众人著绯大吉利”等，围绕衣色与群体服饰，提示梦中要分辨：
    - 穿黄、皂一类庄重之色，多主端正持重、位分稳当；
    - 单身白衣主有人来请，多与应邀、被请托有关；
    - 青衣与神人、隐形助力相关，蓝绣衣则偏向妻家与配偶方面的大利；
    - 众人同著紫、白、绯等，则对应“情感被压抑的场合”“官事、丧事场合”与“喜庆宴集之场合”.
  - “与人著青，家人散”单列强调：当衣色象征“阵营”时，与人同著青色，反而意味着家人各自为阵、难以同心.

  **（四）夫妻互衣、共衣与破衣：亲密关系的边界**

  - “妻著夫衣，生贵子”“女子着衣，平无事”描绘的是正常角色分配下的和谐画面：
    - 妻穿夫衣，象征夫妻一体、气场相合，多主生贵子；
    - 女子穿着得体之衣，则主平稳无事.
  - “衣服忽破，妻外心”“与人共衣，妻私情”“人著己履，妻有私”等几条，则集中提示：
    - 衣服忽然破损，意味着原本完整的遮蔽与安全层被撕裂，多联想到情感上的裂痕；
    - 与他人共穿一衣，象征把只应在夫妻之间的亲密空间分享给外人；
    - 他人穿着自己的鞋履，则有“代入自己位置”的意味，古人因而以此占妻有私情.
  - “与人衣服，主患至”“失却衣服，妻难产”“好被自盖，得富贵”等句，共同强调：
    - 将衣服借与他人，容易让本属于自己的防护与运气外泄，反引来烦恼；
    - 失却衣服，则在本书中多与妻子生产不顺、家庭支持系统薄弱相连；
    - 若被褥完好且自盖其上，则主自身在家庭温床中得富贵之象.

  **（五）鞋履、奴仆与出厄：脚下根基的象征**

  - “得靴鞋，主奴婢吉”“乞得鞋履，人助力”“新授官爵，主贵子”一组，指向脚下根基与辅助系统：
    - 得靴鞋，象征有下属、子弟、奴仆之助，或现实中的团队、后勤支持到位；
    - 乞得鞋履，则是在他人相助下获得行路之具，主有人扶携；
    - 新授官爵而兼见鞋履得当，则“脚下有路可行”，有利于官位落实与子嗣承接.
  - “失履，主奴婢逃走”“鞋破，子孙妻妾病”“木履脱时，己出厄”则从反面刻画：
    - 鞋履丢失，象征帮手、部属离散，凡事需亲力亲为；
    - 鞋破，则脚下受伤，古人多以此比喻子孙、妻妾受损或多病；
    - 木履粗重难行，一旦脱落，反主“旧有拘束解除”，人得以走出困厄之地.



- **完整对等诠释（secondary_lang_full）**：

  This category interprets dreams about hats, robes, belts, bedding, and shoes as symbols of social identity, marital dynamics, and the practical support a person receives in daily life. What rests on the head and shoulders points to rank and public recognition; what wraps the body reflects how one inhabits family roles; what lies under the feet reveals whether the road ahead is firmly supported or fragile.

  When official caps, court robes, belts, and tablets are bestowed, renewed, or worn in proper form, the dream suggests that positions and responsibilities are being adjusted into place. Being given formal garments by a noble or superior, putting on new official attire, or washing and dyeing court clothing and the tablet in one's hand all indicate preparing for new duties—transfer of office, promotion, or a fresh assignment within the same structure. Losing or burning hats and crowns hints that existing titles and prestige are being stripped away or voluntarily abandoned; whether this is a release or a loss depends on the dreamer's real attitude toward their current role.

  Ordinary clothing and shared garments mirror intimacy and boundaries within close relationships. New robes and embroidered clothes point to honor, comfort, and in many readings the increase of spouses and descendants. Torn garments, lending clothes to others, wearing the same outfit together with someone, or suddenly finding one's clothes gone all suggest that protective boundaries are damaged or given away, easily echoing marital strain, hidden affairs, or confusion about who occupies which place in the household. A wife wearing her husband's clothing in a dignified way can signal deep alignment and the birth of a noble child; someone else casually wearing the dreamer's shoes, however, implies another person stepping into the dreamer's position.

  Shoes, boots, and wooden clogs speak directly about footing and support. Receiving footwear or being helped to obtain shoes indicates helpers, servants, teams, or in‑laws who provide real backing so that the dreamer can "walk their path" and make official titles effective. Losing shoes or wearing broken ones, by contrast, reveals that the support network is scattering and that spouses, concubines, or children may be under strain or in poor health. Heavy wooden clogs that suddenly slip off show old restraints falling away and the chance to step out of a constricting situation. Overall, this category teaches the dreamer to read clothing and footwear not as mere decoration, but as a dynamic map of status, relationships, and the strength or weakness of real‑world support.

- 校勘与字词辨析：

  - 原文本类多以三句连写，如“戴官登车官欲迁　自戴幞头巾帽吉　簪冠登台职位迁”，本稿在 L1 层将其拆分为多句并加标点，仅为阅读与后续处理方便，不改动原有字序与用词.
  - “幞头”与“巾帽”等名物，本稿不一一考据服制，仅在分词中点明其为头饰总称.
  - “笏硫忧凶三不祥”中“硫”字疑作“流”或他字，传统多解为“笏上污迹、裂痕”之类，本稿仍依底本，按“笏有污损则多忧凶”释之.
  - “裁衣着孛衣皆吉”中“孛衣”字形少见，或为“襃衣”等他本异写，本稿不强行改作通行词，仅在白话中概括为“合身而吉”的衣饰，不作装束细考.
  - “衣色”部分（黄、皂、白、青、紫、绯等），古今关联众多，本稿仅据原书略述其象，不展开色彩符号学.
  - 关于“妻著夫衣生贵子”“与人共衣妻私情”“人著己履妻有私”等句，本稿在 L1 层忠实记录古书关于婚姻、性别和忠诚的想象框架，不将之直接等同于现代伦理判断，后续 L2/L3 层可再补充心理学与当代关系视角.

  - **English**：
    - The original text presents entries in groups of three consecutive phrases, e.g. "戴官登车官欲迁　自戴幞头巾帽吉　簪冠登台职位迁." This edition splits them into multiple sentences with punctuation for reading convenience, without altering the original word order or terms.
    - Terms like "幞头" (a type of headwear) and "巾帽" are not given detailed costume-history research here; they are simply noted as general terms for headwear in the word analysis.
    - In "笏硫忧凶三不祥," the character "硫" is suspected to be a scribal variant for "流" or another character; traditionally interpreted as "stains or cracks on the tablet." This edition follows the base text, interpreting it as "a damaged tablet indicates worry and misfortune."
    - In "裁衣着孛衣皆吉," the term "孛衣" is rare and may be a variant of "襃衣" from other editions; this edition does not force conversion to common terms, simply summarizing it as "well-fitting and auspicious attire" without detailed costume analysis.
    - The color section (yellow, black, white, blue, purple, vermilion, etc.) has many ancient and modern associations; this edition briefly describes their symbolism per the original text without expanding into color semiotics.
    - Regarding phrases like "妻著夫衣生贵子," "与人共衣妻私情," and "人著己履妻有私," the L1 layer faithfully records the ancient text's imaginative framework about marriage, gender, and fidelity, without directly equating it to modern ethical judgments; psychological and contemporary relationship perspectives can be added in subsequent L2/L3 layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_058]` `[trigger: 梦见戴官登车]` `[factor_trigger: dream_hat_carriage]` `[role: 主干]` 戴官登车，官欲迁。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_059]` `[trigger: 梦见自戴幞头巾帽]` `[factor_trigger: dream_headwrap]` `[role: 主干]` 自戴幞头巾帽，吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_060]` `[trigger: 梦见簪冠登台]` `[factor_trigger: dream_crown_platform]` `[role: 主干]` 簪冠登台，职位迁。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_061]` `[trigger: 梦见贵人与衣冠]` `[factor_trigger: dream_noble_gift_robe]` `[role: 主干]` 贵人与之衣冠，吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_062]` `[trigger: 梦见新换衣冠]` `[factor_trigger: dream_new_robe]` `[role: 主干]` 新换衣冠，禄位至。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_063]` `[trigger: 梦见烧毁冠帽]` `[factor_trigger: dream_burn_hat]` `[role: 主干]` 烧毁冠帽，欲更官。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_064]` `[trigger: 梦见失去冠帽]` `[factor_trigger: dream_lose_hat]` `[role: 主干]` 失去冠帽，去退职。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_065]` `[trigger: 梦见拾得官带]` `[factor_trigger: dream_find_belt]` `[role: 主干]` 拾得官带，禄位至。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_066]` `[trigger: 梦见与人公服]` `[factor_trigger: dream_give_uniform]` `[role: 主干]` 与人公服，主得职。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_067]` `[trigger: 梦见人与公服]` `[factor_trigger: dream_receive_uniform]` `[role: 主干]` 人与公服，加官职。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_068]` `[trigger: 梦见女著冠带]` `[factor_trigger: dream_woman_hat]` `[role: 主干]` 女著冠带，主生子。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_069]` `[trigger: 梦见洗笏染服]` `[factor_trigger: dream_wash_tablet]` `[role: 主干]` 洗笏染服，新官来。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_070]` `[trigger: 梦见执笏见贵人]` `[factor_trigger: dream_hold_tablet]` `[role: 主干]` 执笏见贵人，大吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_071]` `[trigger: 梦见笏污]` `[factor_trigger: dream_tablet_dirty]` `[role: 主干]` 笏污，忧凶三不祥。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_072]` `[trigger: 梦见与人笏绶]` `[factor_trigger: dream_give_tablet]` `[role: 主干]` 与人笏绶，主官迁。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_073]` `[trigger: 梦见腰带]` `[factor_trigger: dream_waist_belt]` `[role: 主干]` 腰带者，主官至吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_074]` `[trigger: 梦见文书用印]` `[factor_trigger: dream_official_seal]` `[role: 主干]` 文书用印，有名声。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_075]` `[trigger: 梦见带印]` `[factor_trigger: dream_carry_seal]` `[role: 主干]` 带印，主妻生贵子。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_076]` `[trigger: 梦见著新袍]` `[factor_trigger: dream_new_robe]` `[role: 主干]` 著新袍，主添妻妾。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_077]` `[trigger: 梦见著锦绣衣]` `[factor_trigger: dream_embroidered]` `[role: 主干]` 著锦绣衣，子孙荣。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_078]` `[trigger: 梦见洗染衣服]` `[factor_trigger: dream_wash_dye]` `[role: 主干]` 洗染衣服，皆大吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_079]` `[trigger: 梦见披蓑衣]` `[factor_trigger: dream_straw_coat]` `[role: 主干]` 披蓑衣，主大恩至。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_080]` `[trigger: 梦见被油污衣]` `[factor_trigger: dream_oil_stain]` `[role: 主干]` 被油污衣，大恩泽。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_081]` `[trigger: 梦见衣服忽破]` `[factor_trigger: dream_clothes_tear]` `[role: 主干]` 衣服忽破，妻外心。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_082]` `[trigger: 梦见新衣攒米]` `[factor_trigger: dream_clothes_rice]` `[role: 主干]` 新衣攒米，百事凶。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_083]` `[trigger: 梦见与人衣服]` `[factor_trigger: dream_give_clothes]` `[role: 主干]` 与人衣服，主患至。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_084]` `[trigger: 梦见裁衣]` `[factor_trigger: dream_tailor]` `[role: 主干]` 裁衣着孛衣，皆吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_085]` `[trigger: 梦见衣带自解]` `[factor_trigger: dream_belt_loosen]` `[role: 主干]` 衣带自解，百事吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_086]` `[trigger: 梦见著黄衣皂衣]` `[factor_trigger: dream_yellow_black]` `[role: 主干]` 著黄衣皂衣，皆吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_087]` `[trigger: 梦见著白衣]` `[factor_trigger: dream_white_clothes]` `[role: 主干]` 著白衣，主有人请。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_088]` `[trigger: 梦见著青衣]` `[factor_trigger: dream_blue_clothes]` `[role: 主干]` 著青衣，神人助力。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_089]` `[trigger: 梦见著蓝绣衣]` `[factor_trigger: dream_blue_embroidered]` `[role: 主干]` 著蓝绣衣，妻大利。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_090]` `[trigger: 梦见众人著紫]` `[factor_trigger: dream_crowd_purple]` `[role: 主干]` 众人著紫，主情毙。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_091]` `[trigger: 梦见与人著青]` `[factor_trigger: dream_give_blue]` `[role: 主干]` 与人著青，家人散。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_092]` `[trigger: 梦见众人著白]` `[factor_trigger: dream_crowd_white]` `[role: 主干]` 众人著白，主官事。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_093]` `[trigger: 梦见众人著绯]` `[factor_trigger: dream_crowd_red]` `[role: 主干]` 众人著绯，大吉利。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_094]` `[trigger: 梦见妻著夫衣]` `[factor_trigger: dream_wife_husband_clothes]` `[role: 主干]` 妻著夫衣，生贵子。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_095]` `[trigger: 梦见女子着衣]` `[factor_trigger: dream_woman_dress]` `[role: 主干]` 女子着衣，平无事。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_096]` `[trigger: 梦见与人共衣]` `[factor_trigger: dream_share_clothes]` `[role: 主干]` 与人共衣，妻私情。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_097]` `[trigger: 梦见失却衣服]` `[factor_trigger: dream_lose_clothes]` `[role: 主干]` 失却衣服，妻难产。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_098]` `[trigger: 梦见好被自盖]` `[factor_trigger: dream_cover_blanket]` `[role: 主干]` 好被自盖，得富贵。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_099]` `[trigger: 梦见人著己履]` `[factor_trigger: dream_other_wear_shoes]` `[role: 主干]` 人著己履，妻有私。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_100]` `[trigger: 梦见得靴鞋]` `[factor_trigger: dream_get_boots]` `[role: 主干]` 得靴鞋，主奴婢吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_101]` `[trigger: 梦见失履]` `[factor_trigger: dream_lose_shoes]` `[role: 主干]` 失履，主奴婢逃走。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_102]` `[trigger: 梦见脱靴束带]` `[factor_trigger: dream_remove_boots]` `[role: 主干]` 脱靴束带，主有凶。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_103]` `[trigger: 梦见鞋破]` `[factor_trigger: dream_shoes_broken]` `[role: 主干]` 鞋破，子孙妻妾病。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_104]` `[trigger: 梦见著麻鞋]` `[factor_trigger: dream_hemp_shoes]` `[role: 主干]` 著麻鞋，百事和合。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_105]` `[trigger: 梦见新授官爵]` `[factor_trigger: dream_new_rank]` `[role: 主干]` 新授官爵，主贵子。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_106]` `[trigger: 梦见乞得鞋履]` `[factor_trigger: dream_beg_shoes]` `[role: 主干]` 乞得鞋履，人助力。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_107]` `[trigger: 梦见木履脱]` `[factor_trigger: dream_wooden_shoe_off]` `[role: 主干]` 木履脱时，己出厄。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_447]` `[trigger: 梦见遗失]` `[factor_trigger: dream_lose_thing]` `[role: 主干]` 梦见遗失，主有忧。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_448]` `[trigger: 梦见幸运]` `[factor_trigger: dream_luck]` `[role: 主干]` 梦见幸运，主大吉。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_449]` `[trigger: 梦见婚姻]` `[factor_trigger: dream_marriage]` `[role: 主干]` 梦见婚姻，主喜庆。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_450]` `[trigger: 梦见肉]` `[factor_trigger: dream_meat]` `[role: 主干]` 梦见肉，主得财。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_451]` `[trigger: 梦见医生]` `[factor_trigger: dream_medicine]` `[role: 主干]` 梦见医生，主病除。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_452]` `[trigger: 梦见钱]` `[factor_trigger: dream_money]` `[role: 主干]` 梦见钱，主得财。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_453]` `[trigger: 梦见月]` `[factor_trigger: dream_moon]` `[role: 主干]` 梦见月，主有喜。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_454]` `[trigger: 梦见母死]` `[factor_trigger: dream_mother_death]` `[role: 主干]` 梦见母死，主大凶。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_455]` `[trigger: 梦见母病]` `[factor_trigger: dream_mother_sick]` `[role: 主干]` 梦见母病，主有忧。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_456]` `[trigger: 梦见音乐]` `[factor_trigger: dream_music]` `[role: 主干]` 梦见音乐，主有喜。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_457]` `[trigger: 梦见裸体]` `[factor_trigger: dream_naked_body]` `[role: 主干]` 梦见裸体，主受辱。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_458]` `[trigger: 梦见噩梦]` `[factor_trigger: dream_nightmare]` `[role: 主干]` 梦见噩梦，主凶险。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_459]` `[trigger: 梦见官员]` `[factor_trigger: dream_official]` `[role: 主干]` 梦见官员，主升迁。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_460]` `[trigger: 梦见官讼]` `[factor_trigger: dream_official_lawsuit]` `[role: 主干]` 梦见官讼，主有争。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_461]` `[trigger: 梦见猪]` `[factor_trigger: dream_pig]` `[role: 主干]` 梦见猪，主有财。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_462]` `[trigger: 梦见贫穷]` `[factor_trigger: dream_poverty]` `[role: 主干]` 梦见贫穷，主破财。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_463]` `[trigger: 梦见祈祷]` `[factor_trigger: dream_pray]` `[role: 主干]` 梦见祈祷，主吉祥。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_464]` `[trigger: 梦见孕]` `[factor_trigger: dream_pregnant]` `[role: 主干]` 梦见孕，主有喜。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_465]` `[trigger: 梦见牢狱]` `[factor_trigger: dream_prison]` `[role: 主干]` 梦见牢狱，主有难。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_466]` `[trigger: 梦见雨]` `[factor_trigger: dream_rain]` `[role: 主干]` 梦见雨，主有财。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_467]` `[trigger: 梦见河]` `[factor_trigger: dream_river]` `[role: 主干]` 梦见河，主远行。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_468]` `[trigger: 梦见抢劫]` `[factor_trigger: dream_robbery]` `[role: 主干]` 梦见抢劫，主破财。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_469]` `[trigger: 梦见绳索]` `[factor_trigger: dream_rope]` `[role: 主干]` 梦见绳索，主长命。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_470]` `[trigger: 梦见跑]` `[factor_trigger: dream_running]` `[role: 主干]` 梦见跑，主有急事。 → 《周公解梦·冠带衣服鞋袜》
  - `[ns_zgjm_471]` `[trigger: 梦见海]` `[factor_trigger: dream_sea]` `[role: 主干]` 梦见海，主远行。 → 《周公解梦·冠带衣服鞋袜》"""
    normalized_text_zh: str = """"""
    subject: str = "冠带衣服鞋袜"
    factor_refs: list = []
    
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
        book_id="zhougong",
        chapter="",
        l1_anchor="zgjm_v1.0.0_冠带衣服鞋袜_001_L1",
    )
    version: str = "1.0.0"
