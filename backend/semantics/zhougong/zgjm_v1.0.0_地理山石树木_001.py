"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864253
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
    semantic_id="zgjm_v1.0.0_地理山石树木_001",
    book_id="zhougong",
    engine_id="dream"
)
class 地理山石树木(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  地理山石树木。

  【条文】

  地动，主迁官位吉。
  地裂，主疾病，大凶。
  修平田地，大吉昌。

  地高下不平，主病。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  地理山石树木。

  【条文】

  地动，主迁官位吉。
  地裂，主疾病，大凶。
  修平田地，大吉昌。

  地高下不平，主病。
  卧于石上，主大吉。
  地中黑气上，主凶。

  运石入家，主富贵。
  石上得利禄，大吉。
  盘石安稳，无忧疑。

  登岩抱石，官职迁。
  手弄小石，生贵子。
  身入土中，百事吉。

  自身取土，被耻辱。
  升山落地，主失位。
  上山恐怕，禄位至。

  上山毁坏，主凶恶。
  游看高山，春夏吉。
  行走上坡，病思除。

  居住高山，有喜事。
  山行得财，有福缘。
  抱物上山，孕贵子。

  山中农稼，衣食丰。
  枯木再发，子孙兴。
  堂上地陷，主母忧。

  园林茂盛，大吉利。
  树木枯死，宅不安。
  林中坐卧，病欲痊。

  树木凋零，主人凶。
  林中树生，添贵子。
  种植树木，大吉昌。

  登大树，名利显扬。
  上树忽折，有死伤。
  与人分花，主分散。

  枯木开花，子孙兴。
  大树落人屋上，吉。
  立树下，贵人庇荫。

  树生堂上，父母忧。
  大树忽折，主凶恶。
  担木来家，得财喜。

  砍伐大树，多得财。
  草木茂盛，家道兴。
  门中生果树，有子。

  松生腹上，位三公。
  家中生松，事转丰。
  家中生柏，多吉利。

  庭前竹木，喜重重。
  枫生屋上，百事遂。
  兰生庭前，主添孙。

  果林中行，主得财。
  入菜园中，大发财。
  桑生井上，主有忧。

  果树多熟，子孙安。
  折笋到家，女有子。
  见笋者，主添子孙。

  扫地除粪，家欲破。
  粪土堆者，钱财聚。

- 分字分词释义：

  - **地理山石树木**：本类总纲，涵盖大地高下、山岭岩石、园林树木、田亩草木等一切“所立之地”与“所依之物”。
  - **地动／地裂**：脚下之地轻摇为“动”，裂开成缝为“裂”；前者重在“迁变、移位”，后者则象征根基断裂、多主疾病与大祸。
  - **修平田地**：整修田亩、填平坑洼，比喻整顿基础、平治环境，多为长远发展之吉象。
  - **地高下不平**：行走其上颠簸不稳，为“履险”之象，易应病苦、诉讼与事务不顺。
  - **卧于石上／石上得利禄／盘石安稳**：石为坚重之物，卧其上或立其上，多主根基稳固、所得牢靠，不易摇动。
  - **地中黑气上**：暗浊之气自地而起，多主病疫、阴事或暗中不利之势渐显。
  - **运石入家／担木来家／砍伐大树多得财**：将石木等重物运入家中或砍伐而归，是“有形资产入库”的象征，多主财物积聚、资源到位。
  - **登岩抱石／山行得财／抱物上山**：向高处行、多与“负重登高、凭借山势”有关，既象征出力，也主凭借资源与贵人之势而进。
  - **身入土中／居住高山**：与前一类“天地日月”中“入地见天日”等相表里，前者偏向“扎根”“入本源”，壮年多主安居吉象；后者则寓“立身高处”，有喜事、名望之机。
  - **枯木再发／枯木开花**：枯槁之木忽然重新生芽、开花，多主子孙振兴、旧局再生，是明显的“起死回生”之象。
  - **堂上地陷／树生堂上**：堂上为家中中枢要地；地陷、树生皆为“异常之象”，多牵连父母与家宅安危，须谨慎对待。
  - **园林茂盛／草木茂盛／果树多熟**：主环境丰美、家道兴隆、子孙安泰，是典型的“有地可依、有粮可食”之象。
  - **大树落人屋上／立树下贵人庇荫**：大树比喻高大之人或势力，落在屋上或立树之下，多为得其庇护、逢其护持之意。
  - **松生腹上位三公**：松为长寿、坚贞之象，“腹上”指贴身之处，古人以此比喻“可以承载大任、位极人臣”。
  - **家中生松／家中生柏／庭前竹木、枫、兰**：屋内或庭前长出松柏竹兰枫等，多主家运转丰、喜事重重、子孙增添，但亦需视与他象搭配而定。
  - **桑生井上**：井为水源、根基，桑多与“丧”谐音，桑树覆于井上，多主忧患、病丧之事临近根基处。
  - **扫地除粪／粪土堆者**：粪土本为肥料，扫除过甚则“家欲破”，堆聚得法则“钱财聚”，提示对“废物／资源”的取舍之道。

- **规范化释义（primary_lang_explained）**：

  本类围绕“地形与草木”，把梦中所见的大地高低、山石稳危、园林枯荣、树木开落，视作对现实中**基础环境、家宅根基与家族兴衰**的映照。

  大体可分为几组意象：

  - **地势与山形**：
    - 地动、地裂、地高下不平，分别象征“迁移更新”“根基断裂”“履险不稳”；
    - 登山、行坡、居高山，则偏向“向上而行”的过程：顺利者得禄位与喜事，失脚者则有失位之忧。
  - **石土与入土**：
    - 卧石、石上得利、盘石安稳，主所得坚固、事业稳妥；
    - 身入土中，多为“归根入本”的吉兆，壮年人更主凡事可稳扎稳打；
    - 自身取土则偏向“自污自辱”，若方式不正，反主被耻笑与失面子。
  - **树木与枯荣**：
    - 草木茂盛、园林成行、果树多熟，主家业兴隆、子孙安康；
    - 树木枯死、凋零，则多指宅运不安、主人有凶，需早察家中隐患；
    - 枯木再发、枯木开花，则代表从低谷中再起，是子孙、事业重新振作的强吉之象。
  - **堂上与家门之象**：
    - 堂上地陷、树生堂上，皆为“家中中枢失常”，多牵连父母长辈的健康与地位；
    - 门中生果树，则主家门中有子嗣、后继有人。
  - **松柏竹兰等“君子之木”**：
    - 松柏常与高寿、坚贞、尊贵相连；
    - 竹兰则主清雅、喜庆与子孙添丁；
    - 若在腹上、家中、庭前显现，多主德位、子孙与名望同时增长。
  - **粪土与资源调度**：
    - 粪土若堆聚得所，为田地之肥；
    - 若一味扫除、视为污秽，则反主家业空虚、基础被掏空。

- 核心要点：

  - **看“地形与高度”判断处境：**
    - 平地、修平田地，多主基础整顿好、长远可为；
    - 高山、上坡，象征向上之路，有劳有得；
    - 地裂、坑陷、不平，则提醒基础不稳，凡事易生暗坑。
  - **看“枯荣与再生”判断家运：**
    - 草木茂盛、果树多熟，是家道昌盛的象征；
    - 枯死、凋零需警惕宅运与健康；
    - 枯木再发、枯木开花，则是困境中再获新生的典型吉象。
  - **看“树所在之处”判断应在何人：**
    - 堂上、腹上、门中、庭前，各有对应：堂上关父母，腹上关自己之位，门中关家族后嗣，庭前关门面与对外形象。
  - **看“石土与粪土”的用法判断财富：**
    - 运石、担木、砍树而归，是“搬运资源入库”；
    - 扫地除粪过度，则暗指把本可利用的资产一并清空；
    - 粪土堆者钱财聚，提示善用“边角料”也能积累财富。

- 详细解说：

  **（一）地动、地裂与田地修平：变与稳的开端**

  - “地动，主迁官位吉”承接上一类“地动吉”的思路：大地轻摇，不一定是灾，反而多主职位、住处或事业方向的调整。若现实中正有调动、迁居之意，此梦常为“顺势而迁”的鼓励。
  - “地裂，主疾病，大凶”则另当别论：地面开裂，多象征身体与家庭结构的“裂痕”，尤其关乎慢性病、重病及关系破裂。需结合其他梦象与现实状况，及早检查与修补。
  - “修平田地，大吉昌”提示，通过主动整治田地——比喻重整生活结构、业务基础、家庭秩序，能够获得长久之利。相比寄望突发财喜，更重视“基础工程”。

  **（二）石土与入土：稳固与羞辱的两面**

  - “卧于石上，主大吉”“石上得利禄，大吉”“盘石安稳，无忧疑”共同强调：若能找到坚如磐石的立足点，无论是职业、城市、合作关系还是精神信念，人生多半不至大起大落。
  - “身入土中，百事吉”在本书语境中，不作“入棺”解，而偏向“扎根于土地”：对壮年人是安居乐业、事业有根之象；对重病垂危者，则仍需谨慎结合其他梦象来看。
  - “自身取土，被耻辱”则提醒：若以不正手段从基础处“挖土”、占便宜，如侵占他人基础资源，则易招致耻笑与名誉受损。

  **（三）上山、居高与落地失位：位置的升降**

  - “升山落地，主失位”“上山恐怕，禄位至”“上山毁坏，主凶恶”“居住高山，有喜事”“山行得财，有福缘”“抱物上山，孕贵子”，共构成一组“上山之象”：
    - 安稳登山、居于高山，多主职位、名望或居住环境提升；
    - 中途跌落、山体毁坏，则主失位、环境恶化，甚至名誉受损；
    - 带物上山、抱物而行，则强调“负重有责”——所得贵子与大任皆非无本之福。
  - “游看高山，春夏吉”“行走上坡，病思除”则偏日常：在暖季观山、轻行上坡，多主心情舒畅、旧病渐消，带有“散心疗愈”的意味。

  **（四）园林、林木与家宅兴衰**

  - “园林茂盛，大吉利”“草木茂盛，家道兴”“果树多熟，子孙安”“果林中行，主得财”“入菜园中，大发财”共同描绘出一幅“家有园林、田菜丰实”的景象，主家中有田产、收入稳定、衣食无忧。
  - “树木枯死，宅不安”“树木凋零，主人凶”则偏向宅运衰落、主人身体或运势走下坡，需反思居住环境与生活习惯。
  - “林中坐卧，病欲痊”在本书中却给出反向吉意：身处树林中静坐或卧息，空气清新、远离尘嚣，多主病情好转、精神恢复。

  **（五）枯木再发、枯木开花：困境中再兴的象征**

  - “枯木再发，子孙兴”“枯木开花，子孙兴”是本类中最具诗意的两句：
    - 枯木象征曾经断绝希望或资源的局面；
    - “再发”“开花”则意味着某个以为已无指望的方面突然复苏，多应在子孙、事业或名声上再度兴起。
  - 现实解梦时，可对应长期停滞的项目突然有新机会、家族某一支脉重新振作、晚年得子或晚成之功等。

  **（六）堂上、腹上与门中：位置决定应验对象**

  - “堂上地陷，主母忧”“树生堂上，父母忧”皆指家中大堂出现异常，多应在母亲及家中长辈的健康、情绪或地位上。梦后宜多关怀长辈。
  - “松生腹上，位三公”则从身体位置入手：腹为中宫，承载五脏六腑之要地，梦见此处生松，象征内在承载力增强，有能力担任高位。
  - “门中生果树，有子”以门中之树果对应后嗣之生，暗示家门中将有子女出生或下一代渐渐成长成才。

  **（七）松柏竹兰与桑井、粪土：气质与资源的双重面向**
 
  - “家中生松，事转丰”“家中生柏，多吉利”“庭前竹木，喜重重”“枫生屋上，百事遂”“兰生庭前，主添孙”皆属吉象，强调家风日渐高雅、子孙增多、事事顺遂。
  - “桑生井上，主有忧”则为反例：桑与“丧”谐音，又遮蔽井口，多主与水源、根基相关的忧患，如家族传承、生活来源或情绪深层问题。
  - “扫地除粪，家欲破；粪土堆者，钱财聚”则一语双关：
    - 粪土若全扫尽，肥力不存，田地贫瘠，比喻过度清理、断舍离，把可用资源一并抛弃；
    - 粪土堆聚得所，则成为养地之本，象征善用边缘资源、废物利用，反能聚财。
 
 
 
- **完整对等诠释（secondary_lang_full）**：

  This category focuses on dreams that feature ground, mountains, rocks, fields, gardens, and trees. The stability or disturbance of the land, and the flourishing or withering of vegetation, are read as mirrors of a person's basic environment, family foundation, and the long‑term rise or decline of the household.

  When the land is levelled and tended, mountains are climbed smoothly, and gardens and forests are lush, the dream points to a solid base, stable residence, and resources that can grow over time. Sleeping or standing on firm rocks, carrying stones or timber home, or seeing abundant crops and fruit trees all suggest reliable income, dependable backing, and a home that can support descendants for generations.

  By contrast, shaking or cracked ground, pits beneath the hall, crooked slopes, or dead and withered trees warn of structural problems in health, home, or family lineage. A collapsed floor in the main hall, or strange trees suddenly growing in the central hall, often corresponds to worries around parents and elders, or instability at the very core of the household. A mulberry tree growing over the family well hints at anxiety and trouble around roots and sources of support, because the well is blocked and the name of the tree echoes mourning.

  The most powerful images of renewal are "dead wood sprouting again" and "dead wood blossoming". These point to projects, family branches, or personal fortunes that seemed exhausted suddenly finding new life—children and grandchildren thriving again, or a career reviving after a low period. Manure and refuse gathered in the right place become fertilizer and wealth; swept away too thoroughly, they leave the field barren. The dream therefore reminds the dreamer that even humble or dirty resources, if used wisely, can nourish long‑term prosperity, whereas blind rejection of everything old may hollow out the foundation.

- 校勘与字词辨析：

  - 原文多以三句并列的方式呈现各条，例如“地动主迁官位吉　地裂主疾病大凶　修平田地大吉昌”等。本稿在 L1 层将其拆分为独立句式，加逗号与句号，以利现代阅读，同时严格保留字序与判词，不作意译改写。
  - “山行得财有福缘”中“福缘”本作“福缘”，本稿据义保留，并在白话中解释为“在山行、动中得财与善缘”的象征，不作佛教义理延伸。
  - “松生腹上位三公”一句，历来有象征与字面之争：L1 层仅据字面记录与传统象意（位极人臣），不在本处讨论具体命例的可信度。
  - “桑生井上”“扫地除粪家欲破”“粪土堆者钱财聚”等句，本稿在释义中采用音义结合的传统方式解释（如桑＝丧、粪＝肥料），并提示其现代情境下的可用比喻，而不过度神秘化其占验效力。

  - **English**：
    - The original text presents entries in groups of three parallel phrases, e.g. "地动主迁官位吉　地裂主疾病大凶　修平田地大吉昌." This edition splits them into separate sentences with commas and periods for modern readability, while strictly preserving character order and verdict phrases without paraphrasing.
    - In "山行得财有福缘," the term "福缘" is retained as-is, interpreted in vernacular as symbolizing "gaining wealth and good fortune through mountain travel or movement," without extending into Buddhist doctrinal meanings.
    - The phrase "松生腹上位三公" has long been debated between symbolic and literal readings; the L1 layer records only the literal text and traditional symbolism (reaching the highest ministerial rank) without discussing the credibility of specific case studies.
    - Phrases like "桑生井上," "扫地除粪家欲破," and "粪土堆者钱财聚" are explained using traditional phonetic-semantic association (e.g., 桑=丧, 粪=fertilizer), with modern applicable metaphors suggested, without over-mystifying their divinatory efficacy.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_342]` `[trigger: 梦见地动]` `[factor_trigger: dream_earth_move]` `[role: 主干]` 地动，主迁官位吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_343]` `[trigger: 梦见地裂]` `[factor_trigger: dream_earth_crack]` `[role: 主干]` 地裂，主疾病大凶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_344]` `[trigger: 梦见修平田地]` `[factor_trigger: dream_level_field]` `[role: 主干]` 修平田地，大吉昌。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_345]` `[trigger: 梦见地高下不平]` `[factor_trigger: dream_uneven_ground]` `[role: 主干]` 地高下不平，主病。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_346]` `[trigger: 梦见卧于石上]` `[factor_trigger: dream_lie_stone]` `[role: 主干]` 卧于石上，主大吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_347]` `[trigger: 梦见地中黑气上]` `[factor_trigger: dream_black_air]` `[role: 主干]` 地中黑气上，主凶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_348]` `[trigger: 梦见运石入家]` `[factor_trigger: dream_stone_home]` `[role: 主干]` 运石入家，主富贵。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_349]` `[trigger: 梦见石上得利禄]` `[factor_trigger: dream_stone_profit]` `[role: 主干]` 石上得利禄，大吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_350]` `[trigger: 梦见盘石安稳]` `[factor_trigger: dream_rock_stable]` `[role: 主干]` 盘石安稳，无忧疑。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_351]` `[trigger: 梦见登岩抱石]` `[factor_trigger: dream_climb_rock]` `[role: 主干]` 登岩抱石，官职迁。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_352]` `[trigger: 梦见手弄小石]` `[factor_trigger: dream_play_stone]` `[role: 主干]` 手弄小石，生贵子。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_353]` `[trigger: 梦见身入土中]` `[factor_trigger: dream_enter_earth]` `[role: 主干]` 身入土中，百事吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_354]` `[trigger: 梦见自身取土]` `[factor_trigger: dream_take_soil]` `[role: 主干]` 自身取土，被耻辱。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_355]` `[trigger: 梦见升山落地]` `[factor_trigger: dream_mountain_fall]` `[role: 主干]` 升山落地，主失位。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_356]` `[trigger: 梦见上山恐怕]` `[factor_trigger: dream_mountain_fear]` `[role: 主干]` 上山恐怕，禄位至。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_357]` `[trigger: 梦见上山毁坏]` `[factor_trigger: dream_mountain_damage]` `[role: 主干]` 上山毁坏，主凶恶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_358]` `[trigger: 梦见游看高山]` `[factor_trigger: dream_view_mountain]` `[role: 主干]` 游看高山，春夏吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_359]` `[trigger: 梦见行走上坡]` `[factor_trigger: dream_climb_slope]` `[role: 主干]` 行走上坡，病思除。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_360]` `[trigger: 梦见居住高山]` `[factor_trigger: dream_live_mountain]` `[role: 主干]` 居住高山，有喜事。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_361]` `[trigger: 梦见山行得财]` `[factor_trigger: dream_mountain_wealth]` `[role: 主干]` 山行得财，有福缘。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_362]` `[trigger: 梦见抱物上山]` `[factor_trigger: dream_carry_mountain]` `[role: 主干]` 抱物上山，孕贵子。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_363]` `[trigger: 梦见山中农稼]` `[factor_trigger: dream_mountain_farm]` `[role: 主干]` 山中农稼，衣食丰。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_364]` `[trigger: 梦见枯木再发]` `[factor_trigger: dream_deadwood_bloom]` `[role: 主干]` 枯木再发，子孙兴。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_365]` `[trigger: 梦见堂上地陷]` `[factor_trigger: dream_hall_sink]` `[role: 主干]` 堂上地陷，主母忧。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_366]` `[trigger: 梦见园林茂盛]` `[factor_trigger: dream_garden_flourish]` `[role: 主干]` 园林茂盛，大吉利。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_367]` `[trigger: 梦见树木枯死]` `[factor_trigger: dream_tree_dead]` `[role: 主干]` 树木枯死，宅不安。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_368]` `[trigger: 梦见林中坐卧]` `[factor_trigger: dream_forest_rest]` `[role: 主干]` 林中坐卧，病欲痊。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_369]` `[trigger: 梦见树木凋零]` `[factor_trigger: dream_tree_wither]` `[role: 主干]` 树木凋零，主人凶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_370]` `[trigger: 梦见林中树生]` `[factor_trigger: dream_forest_grow]` `[role: 主干]` 林中树生，添贵子。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_371]` `[trigger: 梦见种植树木]` `[factor_trigger: dream_plant_tree]` `[role: 主干]` 种植树木，大吉昌。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_372]` `[trigger: 梦见登大树]` `[factor_trigger: dream_climb_tree]` `[role: 主干]` 登大树，名利显扬。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_373]` `[trigger: 梦见上树忽折]` `[factor_trigger: dream_tree_break]` `[role: 主干]` 上树忽折，有死伤。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_374]` `[trigger: 梦见与人分花]` `[factor_trigger: dream_share_flower]` `[role: 主干]` 与人分花，主分散。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_375]` `[trigger: 梦见枯木开花]` `[factor_trigger: dream_deadwood_flower]` `[role: 主干]` 枯木开花，子孙兴。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_376]` `[trigger: 梦见大树落人屋上]` `[factor_trigger: dream_tree_roof]` `[role: 主干]` 大树落人屋上，吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_377]` `[trigger: 梦见立树下]` `[factor_trigger: dream_stand_tree]` `[role: 主干]` 立树下，贵人庇荫。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_378]` `[trigger: 梦见树生堂上]` `[factor_trigger: dream_tree_hall]` `[role: 主干]` 树生堂上，父母忧。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_379]` `[trigger: 梦见大树忽折]` `[factor_trigger: dream_tree_sudden_break]` `[role: 主干]` 大树忽折，主凶恶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_380]` `[trigger: 梦见担木来家]` `[factor_trigger: dream_carry_wood]` `[role: 主干]` 担木来家，得财喜。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_381]` `[trigger: 梦见砍伐大树]` `[factor_trigger: dream_cut_tree]` `[role: 主干]` 砍伐大树，多得财。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_382]` `[trigger: 梦见草木茂盛]` `[factor_trigger: dream_vegetation_flourish]` `[role: 主干]` 草木茂盛，家道兴。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_383]` `[trigger: 梦见门中生果树]` `[factor_trigger: dream_fruit_tree_door]` `[role: 主干]` 门中生果树，有子。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_384]` `[trigger: 梦见松生腹上]` `[factor_trigger: dream_pine_belly]` `[role: 主干]` 松生腹上，位三公。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_385]` `[trigger: 梦见家中生松]` `[factor_trigger: dream_home_pine]` `[role: 主干]` 家中生松，事转丰。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_386]` `[trigger: 梦见家中生柏]` `[factor_trigger: dream_home_cypress]` `[role: 主干]` 家中生柏，多吉利。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_387]` `[trigger: 梦见庭前竹木]` `[factor_trigger: dream_bamboo_court]` `[role: 主干]` 庭前竹木，喜重重。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_388]` `[trigger: 梦见枫生屋上]` `[factor_trigger: dream_maple_roof]` `[role: 主干]` 枫生屋上，百事遂。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_389]` `[trigger: 梦见兰生庭前]` `[factor_trigger: dream_orchid_court]` `[role: 主干]` 兰生庭前，主添孙。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_390]` `[trigger: 梦见果林中行]` `[factor_trigger: dream_orchard_walk]` `[role: 主干]` 果林中行，主得财。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_391]` `[trigger: 梦见入菜园中]` `[factor_trigger: dream_vegetable_garden]` `[role: 主干]` 入菜园中，大发财。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_392]` `[trigger: 梦见桑生井上]` `[factor_trigger: dream_mulberry_well]` `[role: 主干]` 桑生井上，主有忧。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_393]` `[trigger: 梦见果树多熟]` `[factor_trigger: dream_fruit_ripe]` `[role: 主干]` 果树多熟，子孙安。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_394]` `[trigger: 梦见折笋到家]` `[factor_trigger: dream_bamboo_shoot]` `[role: 主干]` 折笋到家，女有子。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_395]` `[trigger: 梦见见笋者]` `[factor_trigger: dream_see_shoot]` `[role: 主干]` 见笋者，主添子孙。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_396]` `[trigger: 梦见扫地除粪]` `[factor_trigger: dream_sweep_dung]` `[role: 主干]` 扫地除粪，家欲破。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_397]` `[trigger: 梦见粪土堆者]` `[factor_trigger: dream_dung_pile]` `[role: 主干]` 粪土堆者，钱财聚。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_398]` `[trigger: 梦见乘车]` `[factor_trigger: dream_cart_ride]` `[role: 主干]` 梦见乘车，主出行。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_399]` `[trigger: 梦见捉龟]` `[factor_trigger: dream_catch_tortoise]` `[role: 主干]` 梦见捉龟，主吉祥。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_400]` `[trigger: 梦见喜庆]` `[factor_trigger: dream_celebration]` `[role: 主干]` 梦见喜庆，主吉祥。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_401]` `[trigger: 梦见蜈蚣咬]` `[factor_trigger: dream_centipede_bite]` `[role: 主干]` 梦见蜈蚣咬，主凶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_402]` `[trigger: 梦见长命]` `[factor_trigger: dream_changming]` `[role: 主干]` 梦见长命，主寿延。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_403]` `[trigger: 梦见子死]` `[factor_trigger: dream_child_death]` `[role: 主干]` 梦见子死，主大凶。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_404]` `[trigger: 梦见衣破]` `[factor_trigger: dream_clothes_torn]` `[role: 主干]` 梦见衣破，主贫穷。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_405]` `[trigger: 梦见入棺]` `[factor_trigger: dream_coffin_in]` `[role: 主干]` 梦见入棺，主官禄。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_406]` `[trigger: 梦见梳头]` `[factor_trigger: dream_comb_hair]` `[role: 主干]` 梦见梳头，主忧愁。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_407]` `[trigger: 梦见熟肉]` `[factor_trigger: dream_cooked_meat]` `[role: 主干]` 梦见熟肉，主吉祥。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_408]` `[trigger: 梦见夫妻争]` `[factor_trigger: dream_couple_conflict]` `[role: 主干]` 梦见夫妻争，主不和。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_409]` `[trigger: 梦见夫妻宴]` `[factor_trigger: dream_couple_feast]` `[role: 主干]` 梦见夫妻宴，主和合。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_410]` `[trigger: 梦见见蟹]` `[factor_trigger: dream_crab_seen]` `[role: 主干]` 梦见见蟹，主多子。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_411]` `[trigger: 梦见众人哭]` `[factor_trigger: dream_crying_together]` `[role: 主干]` 梦见众人哭，主有喜。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_412]` `[trigger: 梦见与人哭]` `[factor_trigger: dream_crying_with_others]` `[role: 主干]` 梦见与人哭，主得财。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_413]` `[trigger: 梦见疗愈]` `[factor_trigger: dream_cure]` `[role: 主干]` 梦见疗愈，主病除。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_414]` `[trigger: 梦见挂帘]` `[factor_trigger: dream_curtain_hang]` `[role: 主干]` 梦见挂帘，主安居。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_415]` `[trigger: 梦见坐帘下]` `[factor_trigger: dream_curtain_sit]` `[role: 主干]` 梦见坐帘下，主安逸。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_416]` `[trigger: 梦见大吉]` `[factor_trigger: dream_daji]` `[role: 主干]` 梦见大吉，主大吉祥。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_417]` `[trigger: 梦见危险]` `[factor_trigger: dream_danger]` `[role: 主干]` 梦见危险，主凶险。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_418]` `[trigger: 梦见大喜]` `[factor_trigger: dream_daxi]` `[role: 主干]` 梦见大喜，主大吉。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_419]` `[trigger: 梦见大凶]` `[factor_trigger: dream_daxiong]` `[role: 主干]` 梦见大凶，主大凶险。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_420]` `[trigger: 梦见死者哭]` `[factor_trigger: dream_dead_crying]` `[role: 主干]` 梦见死者哭，主口舌。 → 《周公解梦·地理山石树木》
  - `[ns_zgjm_421]` `[trigger: 梦见死者复活]` `[factor_trigger: dream_dead_revival]` `[role: 主干]` 梦见死者复活，主有信。 → 《周公解梦·地理山石树木》"""
    normalized_text_zh: str = """"""
    subject: str = "地理山石树木"
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
        l1_anchor="zgjm_v1.0.0_地理山石树木_001_L1",
    )
    version: str = "1.0.0"
