"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864209
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
    semantic_id="zgjm_v1.0.0_天地日月星辰_001",
    book_id="zhougong",
    engine_id="dream"
)
class 天地日月星辰(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  天地日月星辰。

  【条文】

  天门开，贵人荐引。
  天光照，主疾病除。
  天晴雨散，百忧去。
  天明，妇人生贵子。

...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  天地日月星辰。

  【条文】

  天门开，贵人荐引。
  天光照，主疾病除。
  天晴雨散，百忧去。
  天明，妇人生贵子。

  天门赤，主有大起。
  仰面向天，大富贵。
  乘龙上天，大主贵。

  上天求妻，儿女贵。
  天上取物，位王侯。
  飞上天，富贵大吉。

  登天上屋，得高官。
  天裂，有分国之忧。
  天星明，主公卿至。

  天愈铙，益寿命吉。
  渡天河，主有所吉。
  天地富，所求皆得。

  天公使，有大吉祥。
  日月初出，家道昌。
  日月照身，得重位。

  日月落，忧没父母。
  日月昏暗，孕妇吉。
  日月欲出，有官职。

  日月合会，妻有子。
  日月衔山，奴欺主。
  负抱日月，贵侯王。

  吞日月，当生贵子。
  礼拜日月，大吉昌。
  日光入屋，官位至。

  日初出无云，大吉。
  日出有光，有好事。
  云开日出，凶事散。

  日入怀，贵子月女。
  拜星月烧香，大吉。
  云忽遮日，有阴私。

  星入怀，主生贵子。
  星落，有病及官事。
  星列行，主添奴婢。

  持执星宿，大富贵。
  流星不落，主移居。
  巡天摩星，位公卿。

  云起四方，交易吉。
  五色云，主大吉昌。
  云赤白吉，青黑凶。

  见浮云，作事不成。
  云雾遮事，大吉利。
  黑云至地，时气病。

  霜雪降，主事不成。
  雪下及时，大吉利。
  雪落身上，万事成。

  雪不沾身，主孝服。
  雪落家庭，主丧事。
  阴雨晦暗，主凶事。

  行路逢雨，有酒食。
  雷霆作事，官位至。
  雷声恐怕，移居吉。

  雷从地震，主志遂。
  身被霹雳，主富贵。
  电光照身，有吉庆。

  赤虹见吉，黑虹凶。
  霞满天，百事欢悦。
  狂风大雨，人死亡。

  风吹人衣，主疾病。
  忽大风，国有号令。
  风如吼，主远信至。

- 分字分词释义：

  - **天地日月星辰**：本类总纲，涵盖天象、日月、星辰与风云雷雨的梦兆。
  - **天门**：天之门户，象征通达之径、机缘入口，以及与上层权力、贵人相通的关口。
  - **贵人荐引**：得有地位之人推荐、引见，比喻获得提携机会。
  - **天光照**：天光照临，象征光明显露、晦气消除。
  - **天晴雨散**：阴雨散尽、天色放晴，比喻忧事解除、困顿渐消。
  - **天门赤**：天门泛赤光，赤为火色，多主剧烈变动中的大起之象。
  - **乘龙上天**：乘龙升天，比喻骤然飞黄腾达、位极人臣。
  - **天裂**：天幕开裂，多寓“分裂”“分国之忧”，象征局势撕裂与大范围不安。
  - **天星明**：星辰光明可辨，象征贤达、公卿来临或辅佐。
  - **日月初出**：日月初升，象征开端、启运，家道初兴之时。
  - **日月落**：日月西沉，比喻光辉既逝，多关父母、长辈之衰谢与忧思。
  - **日月昏暗**：光辉不显，多与孕中之人相关，暗含“藏而未发”的反向吉意。
  - **合会／衔山／入怀／吞日月**：日月相合、被山所衔、入怀或被吞食等意象，分别指婚生、压抑、怀抱与吞纳等不同结构。
  - **星入怀／星落／星列行**：星入怀多主得子；星落多主病讼；星列有序则主添人手、奴婢助力。
  - **五色云**：青、赤、黄、白、黑五色祥云，综合为吉，多主大喜大庆。
  - **浮云／黑云／云雾遮事**：浮云主事难成；黑云下压主时疫与病气；云雾遮掩则多为“事有遮护”，不宜明攻、反宜暗度陈仓之利。
  - **霜雪降／雪下及时**：霜雪普降、事多阻滞；而“及时之雪”则为润物之象，有利于农事与缓解旱情。
  - **雷霆／霹雳／电光照身**：雷、电之象皆为动中带威：作事用雷霆手段则官位可至；霹雳加身则显赫非常；电光照身则主突发的喜庆与启悟。
  - **虹（赤虹／黑虹）**：虹为水火交感之气，赤虹多吉、黑虹多凶，用色彩区分吉凶。
  - **风吹人衣／忽大风／风如吼**：风入衣主身体受风而致病；忽起大风代表国家号令、政令骤变；风声如吼多关远方急信、消息突至。

- **规范化释义（primary_lang_explained）**：

  本类汇总了一切与“天象”相关的梦：从天门开闭、日月升落，到星辰云气、风雨雷电，意在通过天时的变化，折射人间的荣辱得失与祸福吉凶。

  总体而言：

  - **高升、光明、开阔、色彩和悦的天象，多主吉祥**：天门开启、仰面向天、乘龙上天、日月初出、星列有序、五色祥云、霞满长空，往往对应贵人荐引、家道兴隆、功名富贵或心愿达成。
  - **坠落、破裂、晦暗、压抑、色泽晦黑的天象，多含忧凶**：天裂、日月落、星坠、黑云压地、阴雨晦暗、狂风暴雨，则象征局势分裂、长辈病忧、是非官事、时疫流行乃至人命损伤。
  - **部分看似不佳的形象，亦含“先难后易”的转机**：如云雾遮事、“云开日出凶事散”“雪下及时”“雷声恐怕而实主移居吉”等，强调在惊惧或阻滞之后，反有转机与解脱。

- 核心要点：

  - **“天门与上天”的梦，重点在“是否得路”**：门开则贵人荐引，上天而稳则主飞黄腾达；若天裂分国，则是位高而局势不安，需防“位重责巨”。
  - **“日月之象”，重点在“光的状态与位置”**：初出、照身、入屋、入怀，多关家道、官位与子嗣；落、昏暗、被山所衔，则关父母忧患、时运受阻或上下失序。
  - **“星辰之象”，偏向人丁与人手**：星入怀、负抱日月主生贵子或得良缘；星落则警惕疾病与官事；星列成行、持执星宿，则是人手充足、辅佐得力之象。
  - **“云、风、雨、霜雪雷电之象”，综合反映时局与情绪的晴雨表**：
    - 云色与高度决定喜忧（五色云、赤白吉，青黑凶；黑云压地主时疫病气）。
    - 雨雪之时机与沾染与否，区分“润物”与“丧服”。
    - 雷电风暴既主权威、号令与变局，也提示惊惧之中暗藏机缘。

- 详细解说：

  **（一）天门、上天与天裂：通路与版图的象征**

  - “天门开，贵人荐引”“仰面向天，大富贵”“乘龙上天，大主贵”“飞上天，富贵大吉”“登天上屋，得高官”等条，将“上天”与“天门”视作人与更高权力层级之间的通道：门开而路通，则多主有人引荐、升官、跨入更高的平台。
  - “上天求妻，儿女贵”“上天求妻儿女贵”“负抱日月，贵侯王”等，则把“上天”与婚姻、子嗣相连，表示所求婚配与儿女层级较高，多有门第或品格上的优势。
  - 与此相对，“天裂，有分国之忧”提醒：即便身在高位、攀上“天上之屋”，若天幕本身出现裂痕，则国家、组织或家族层面的分裂之忧已经浮现——常对应权力内部不稳、领地被瓜分或制度基础松动。

  **（二）日月升落与光暗：家道与尊亲的晴雨表**

  - “日月初出，家道昌”“日月照身，得重位”“日光入屋，官位至”“日初出无云，大吉”“日出有光，有好事”“云开日出，凶事散”等，均以日月之光照临身、家、屋，象征家道兴隆、仕途光明、晦气散尽。
  - “日入怀，贵子月女”“星入怀，主生贵子”“吞日月，当生贵子”“礼拜日月，大吉昌”等，则将日月星入怀、吞纳或礼拜，与贵子、贤女、信仰与誓愿相连，提示在精神与血脉两层面皆有“承接光明之果”的意味。
  - 反面条文如“日月落，忧没父母”“日月昏暗，孕妇吉”“日月衔山，奴欺主”，则显示：
    - 日月落多与父母、尊长之衰病、离世相关，是对“光源”本身的忧惧。
    - 日月昏暗，却特指“孕妇吉”，可以理解为光辉内敛、胎气安藏，适合孕育而非外放。
    - 日月被山所衔，象征光辉被下层结构“夹持”，奴欺主、下犯上之象，需要警惕制度与关系中的失衡。

  **（三）星辰运行：人丁、属下与机缘配置**

  - 星入怀、负抱日月，多主得子或得贤偶；“星列行，主添奴婢”“持执星宿，大富贵”“巡天摩星，位公卿”则指星辰有序、可以持执操控，比喻下属、人手、资源配置完备，足以支撑更高位次的运作。
  - “星落，有病及官事”提醒：某颗星陨落，往往对应家庭某一位成员或属下遭遇病灾、官非，需提早关照、分担。
  - “流星不落，主移居”则将流星视作移动的光点：不落，表示尚未定于一处，多主迁居、调动、出差或人生重心的转移。

  **（四）云气、风雨霜雪：大环境与情绪场的起伏**

  - 云色与形状：
    - “云起四方，交易吉”“五色云，主大吉昌”强调祥云四起、多色相杂，是市场活络、人际往来频繁、适宜交易的象征。
    - “云赤白吉，青黑凶”用色彩二分：赤白为暖色，偏吉；青黑为阴沉之色，偏凶。
    - “见浮云，作事不成”提醒对那些“来去匆匆”的机会保持警惕，不要轻信“浮云般”的承诺与风头。
    - “云雾遮事，大吉利”则有反向含义：适度遮蔽反而使某些事免遭正面冲击，暗示在特定情境下，“不全部摊开”反而更安全。
    - “黑云至地，时气病”明确指向流行病气与环境压抑，当心时疫流行与整体健康状况。
  - 雨雪与寒霜：
    - “霜雪降，主事不成”点出霜雪为收敛、凝滞之象，万物不长，事多受阻。
    - “雪下及时，大吉利”“雪落身上，万事成”则强调“及时”与“亲身承受”：在需要水分的时节降雪，既解旱又护苗；梦中雪落身上，象征承袭这一润泽之力。
    - “雪不沾身，主孝服”“雪落家庭，主丧事”则把寒雪与丧服联系，指向孝服与家中死亡之忧。
  - 风与雷电：
    - “行路逢雨，有酒食”说明途中遇雨反得食物款待，是“因阻滞而得意外好处”的典型象。
    - “雷霆作事，官位至”“身被霹雳，主富贵”“电光照身，有吉庆”将雷电视作高能量的权威信号：敢于以雷霆手段行事者，若守正，则有望借大势上升，但同时暗含风险与代价。
    - “雷声恐怕，移居吉”提示：对雷声的本能恐惧，反而促使人离开险地，故而迁居得吉。
  190→    - “赤虹见吉，黑虹凶”“霞满天，百事欢悦”“狂风大雨，人死亡”“风吹人衣，主疾病”“忽大风，国有号令”“风如吼，主远信至”，则分别从彩虹、晚霞、大风暴与风吹身的角度，刻画出从喜庆、号令到疾病与死亡的不同范围影响，让梦者可以据天象而推测“此变是偏向庆贺，还是偏向灾祸”。
  191→
  192→

- **完整对等诠释（secondary_lang_full）**：

  This category encompasses dream omens related to celestial phenomena—heaven and earth, sun and moon, stars and constellations, clouds and weather patterns. The fundamental interpretive principle parallels the quality and state of these heavenly images: ascending, radiant, unobstructed, and harmonious celestial symbols (such as heaven's gate opening, facing heaven directly, riding a dragon to the heavens, sun and moon rising initially, stars arrayed in orderly fashion, five-colored auspicious clouds, glowing rainbow spanning the sky) typically signify auspicious events—noble patronage and recommendation, family prosperity flourishing, fame and wealth advancing, or aspirations fulfilled. Conversely, descending, fragmented, dim, oppressive, or darkly-hued celestial phenomena (such as heaven fracturing, sun and moon setting, stars falling, black clouds pressing down to earth, overcast rain and gloom, violent storm winds) symbolize concerning omens—political rupture, elder illness and worry, legal entanglements and disputes, epidemic disease spreading, or even mortality risks.

  Notably, certain seemingly adverse images contain "difficulty preceding ease" transformation opportunities: for instance, "clouds and mist obscuring affairs" may actually protect from direct assault through a covert manoeuvre often described as a "secretly crossing Chen Cang" strategy, "clouds parting and sun emerging disperses calamitous events," "timely snow," or "thunder's frightening sound actually portends auspicious relocation"—emphasizing that after initial alarm or obstruction, reversal and liberation may follow.
  
  **Key interpretive axes**:
  - **Heaven's gate and ascending to heaven**: focus on "whether the path is accessible"—gate open brings noble recommendation; stable ascension signifies meteoric rise; heaven fracturing indicates high position amid unstable circumstances, requiring vigilance against "heavy responsibility accompanying elevated status."
  - **Sun and moon imagery**: centers on "light's condition and position"—initial rising, shining on body, entering house, entering embrace relate to family prosperity, official status, and offspring; setting, dimming, being held by mountains relate to parental worries, blocked fortune, or hierarchical disorder.
  - **Star and constellation imagery**: leans toward family population and personnel—stars entering embrace or carrying the sun and moon portend noble offspring or an auspicious match; falling stars warn of illness and legal matters; stars arrayed in procession, holding the constellations, represent sufficient manpower and capable assistance.
  - **Clouds, wind, rain, frost-snow, thunder-lightning imagery**: comprehensively reflects situational and emotional barometer—cloud color and altitude determine joy or worry; rain-snow timing and whether it touches the body distinguishes "nourishing moisture" from "mourning garments"; combined thunder-lightning-storm imagery signifies authority, decrees, and upheaval, also suggesting opportunities hidden within alarm.

#### L2 语义提取

- **主题**：天象梦兆的吉凶判断与象征系统
- **自然属性**：
  - 象征：
    - **天门与上天**：通达之径、权力入口、与上层的连接通道。
    - **日月**：家道兴衰与父母尊亲的光辉，日月初出主家道昌、日月落主父母忧。
    - **星辰**：人丁配置与辅佐资源，星入怀主生贵子、星落主病讼。
    - **云气**：大环境情绪与市场氛围，五色云主吉庆、黑云压地主时疫。
    - **风雨雷电**：变局、权威与突发事件，雷霆主官位、狂风暴雨主死亡。
  - 特性：
    - 光明、开阔、上升、色彩和悦的天象多主吉祥。
    - 坠落、破裂、晦暗、压抑、色泽晦黑的天象多含忧凶。
    - 部分惊惧之象（如雷声恐怕、云雾遮事）反含转机与解脱。
  - 元素：天门、日月星辰、云气、风雨、霜雪、雷电、虹霞等。
  - 象征：天地日月星辰、风云雨雪雷电等自然现象
  - 特性：宏大、高远、不可控、规律性变化
  - 元素：光明/黑暗、上升/下降、开合/裂隙、色彩、动静
- **功能象义**：
  - 占断功能：通过天象状态判断人事吉凶
  - 梦境功能：反映梦者对权力、前途、家族的潜意识关注
  - 指导功能：提示当前局势的走向与应对策略
- **条件结构**：
  - 必要条件：天象需有明确形态（开/合、明/暗、升/落等）
  - 增强条件：梦者身处关键人生节点（求官、婚嫁、孕育）
  - 失效条件：天象模糊不清、梦者醒后无法回忆细节
- **多层解释**：
  - 字面层：天象本身的物理状态变化
  - 象征层：通过天象比拟人事的高低、明暗、通塞
  - 实践层：指导梦者在权力、婚姻、子嗣方面的决策
  - 心理层：揭示梦者对上升/坠落、光明/黑暗的深层焦虑或期待

**L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天门 | Heaven's Gate | 天之门户，象征通达之径与贵人引荐 | Gateway to heaven, symbolizing accessible path and noble patronage |  | new_candidate |
| 贵人荐引 | Noble Recommendation | 得有地位之人推荐引见 | Receiving introduction and advocacy from person of elevated status |  | new_candidate |
| 日月初出 | Sun-Moon Rising | 日月初升，象征开端启运与家道初兴 | Sun and moon initially rising, symbolizing auspicious beginnings and family prosperity dawning |  | new_candidate |
| 星入怀 | Star Entering Embrace | 星辰入怀，主生贵子或得良缘 | Star entering one's embrace, portending noble offspring or auspicious match |  | new_candidate |
| 五色云 | Five-Colored Cloud | 青赤黄白黑五色祥云，综合为吉 | Auspicious clouds of five colors (blue, red, yellow, white, black), collectively auspicious |  | new_candidate |
| 天裂 | Heaven Fracturing | 天幕开裂，寓分裂与分国之忧 | Sky splitting open, signifying division and national anxiety |  | new_candidate |

#### 语义因子提取（因子层）

| 因子类型 | 因子标签 | 因子ID | 因子来源 | 角色/位置 | 取值/约束 | 备注 |
|----------|---------|--------|----------|----------|----------|------|
| 梦象类 | 天象类型 | | new_candidate | 主要物象 | 天门/日月/星辰/云气/风雨/雷电 | 梦书特有分类 |
| 态势类 | 光明程度 | | new_candidate | 视觉状态 | 明亮/昏暗/裂隙/遮蔽 | 影响吉凶判断 |
| 方位类 | 上升下降 | | new_candidate | 动态方向 | 上天/登高/坠落/沉没 | 关联权位升降 |
| 关系类 | 贵人助力 | | new_candidate | 人际支持 | 荐引/提携/推荐 | 梦兆预示人脉 |
| 结果类 | 梦兆吉凶 | | new_candidate | 预测结果 | 大吉/吉/凶/大凶 | 传统判词 |
| 应期类 | 应验时机 | | new_candidate | 时间维度 | 即应/缓应/远应 | 梦兆实现时间 |


- 校勘与字词辨析：

  193→  - 本类条文明显承袭“短句＋判词”体例，如“天门开贵人荐引”“天光照主疾病除”“日初出无云大吉”等。本稿在 L1 层仅加适度标点，将“主”“大吉”“大凶”等判词与前句分开，以便阅读，并未改动原字次序。
  194→  - “天愈铙益寿命吉”中“愈铙”疑为传写讹字，可能作“愈劳”或他字；L1 层仍据底本直录，仅在解释中以“益寿命吉”理解为“病愈、劳损减轻”之象，待后续版本学工作另行校勘。
  195→  - “天地富所求皆得”一句，原文作连写，本稿以“天地富，所求皆得”断为两意：其一为“天地丰富”；其二为“所求皆得”，以保持语气的递进。
  196→  - “日入怀贵子月女”“云忽遮日有阴私”等条，L1 层不预设具体伦理判断，只对结构与象意加以说明，留待高阶语义层（L2/L3）展开对亲密关系与隐私结构的进一步分析。

  - **English**：
    - This category's entries follow the classic "short phrase + verdict" format, e.g. "Heaven gate opens—noble patron recommends." This edition adds minimal punctuation to separate verdict phrases like "indicates," "great fortune," or "great misfortune" for readability, without altering the original character order.
    - In "天愈铙益寿命吉," the term "愈铙" is suspected to be a scribal error, possibly for "愈劳" or another term. The L1 layer preserves the base text as-is, interpreting the phrase as signifying recovery from illness or fatigue, pending future textual criticism.
    - The phrase "天地富所求皆得" is punctuated as "天地富，所求皆得" to create two parallel meanings: (1) heaven and earth are bountiful; (2) all desires are fulfilled.
    - Entries like "日入怀贵子月女" and "云忽遮日有阴私" are described structurally without imposing ethical judgments at the L1 layer, reserving deeper analysis for L2/L3 semantic layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_278]` `[trigger: 梦见天门开]` `[factor_trigger: dream_tianmen_open]` `[role: 主干]` 天门开，贵人荐引。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_279]` `[trigger: 梦见天光照]` `[factor_trigger: dream_tianlight]` `[role: 主干]` 天光照，主疾病除。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_280]` `[trigger: 梦见天晴雨散]` `[factor_trigger: dream_sky_clear]` `[role: 主干]` 天晴雨散，百忧去。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_281]` `[trigger: 梦见天明]` `[factor_trigger: dream_sky_bright]` `[role: 主干]` 天明，妇人生贵子。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_282]` `[trigger: 梦见天门赤]` `[factor_trigger: dream_tianmen_red]` `[role: 主干]` 天门赤，主有大起。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_283]` `[trigger: 梦见仰面向天]` `[factor_trigger: dream_face_sky]` `[role: 主干]` 仰面向天，大富贵。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_284]` `[trigger: 梦见乘龙上天]` `[factor_trigger: dream_dragon_ascend]` `[role: 主干]` 乘龙上天，大主贵。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_285]` `[trigger: 梦见上天求妻]` `[factor_trigger: dream_sky_wife]` `[role: 主干]` 上天求妻，儿女贵。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_286]` `[trigger: 梦见天上取物]` `[factor_trigger: dream_sky_get]` `[role: 主干]` 天上取物，位王侯。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_287]` `[trigger: 梦见飞上天]` `[factor_trigger: dream_fly_sky]` `[role: 主干]` 飞上天，富贵大吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_288]` `[trigger: 梦见登天上屋]` `[factor_trigger: dream_climb_sky]` `[role: 主干]` 登天上屋，得高官。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_289]` `[trigger: 梦见天裂]` `[factor_trigger: dream_sky_crack]` `[role: 主干]` 天裂，有分国之忧。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_290]` `[trigger: 梦见天星明]` `[factor_trigger: dream_star_bright]` `[role: 主干]` 天星明，主公卿至。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_291]` `[trigger: 梦见天愈铙]` `[factor_trigger: dream_sky_drum]` `[role: 主干]` 天愈铙，益寿命吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_292]` `[trigger: 梦见渡天河]` `[factor_trigger: dream_cross_milkyway]` `[role: 主干]` 渡天河，主有所吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_293]` `[trigger: 梦见天地富]` `[factor_trigger: dream_sky_earth_rich]` `[role: 主干]` 天地富，所求皆得。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_294]` `[trigger: 梦见天公使]` `[factor_trigger: dream_heaven_messenger]` `[role: 主干]` 天公使，有大吉祥。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_295]` `[trigger: 梦见日月初出]` `[factor_trigger: dream_sunmoon_rise]` `[role: 主干]` 日月初出，家道昌。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_296]` `[trigger: 梦见日月照身]` `[factor_trigger: dream_sunmoon_shine]` `[role: 主干]` 日月照身，得重位。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_297]` `[trigger: 梦见日月落]` `[factor_trigger: dream_sunmoon_set]` `[role: 主干]` 日月落，忧没父母。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_298]` `[trigger: 梦见日月昏暗]` `[factor_trigger: dream_sunmoon_dim]` `[role: 主干]` 日月昏暗，孕妇吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_299]` `[trigger: 梦见日月欲出]` `[factor_trigger: dream_sunmoon_about]` `[role: 主干]` 日月欲出，有官职。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_300]` `[trigger: 梦见日月合会]` `[factor_trigger: dream_sunmoon_join]` `[role: 主干]` 日月合会，妻有子。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_301]` `[trigger: 梦见日月衔山]` `[factor_trigger: dream_sunmoon_mountain]` `[role: 主干]` 日月衔山，奴欺主。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_302]` `[trigger: 梦见负抱日月]` `[factor_trigger: dream_hold_sunmoon]` `[role: 主干]` 负抱日月，贵侯王。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_303]` `[trigger: 梦见吞日月]` `[factor_trigger: dream_swallow_sunmoon]` `[role: 主干]` 吞日月，当生贵子。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_304]` `[trigger: 梦见礼拜日月]` `[factor_trigger: dream_worship_sunmoon]` `[role: 主干]` 礼拜日月，大吉昌。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_305]` `[trigger: 梦见日光入屋]` `[factor_trigger: dream_sunlight_house]` `[role: 主干]` 日光入屋，官位至。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_306]` `[trigger: 梦见日初出无云]` `[factor_trigger: dream_sun_clear]` `[role: 主干]` 日初出无云，大吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_307]` `[trigger: 梦见日出有光]` `[factor_trigger: dream_sun_bright]` `[role: 主干]` 日出有光，有好事。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_308]` `[trigger: 梦见云开日出]` `[factor_trigger: dream_cloud_part_sun]` `[role: 主干]` 云开日出，凶事散。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_309]` `[trigger: 梦见日入怀]` `[factor_trigger: dream_sun_embrace]` `[role: 主干]` 日入怀贵子，月女。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_310]` `[trigger: 梦见拜星月烧香]` `[factor_trigger: dream_worship_star]` `[role: 主干]` 拜星月烧香，大吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_311]` `[trigger: 梦见云忽遮日]` `[factor_trigger: dream_cloud_cover_sun]` `[role: 主干]` 云忽遮日，有阴私。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_312]` `[trigger: 梦见星入怀]` `[factor_trigger: dream_star_embrace]` `[role: 主干]` 星入怀，主生贵子。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_313]` `[trigger: 梦见星落]` `[factor_trigger: dream_star_fall]` `[role: 主干]` 星落，有病及官事。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_314]` `[trigger: 梦见星列行]` `[factor_trigger: dream_star_line]` `[role: 主干]` 星列行，主添奴婢。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_315]` `[trigger: 梦见持执星宿]` `[factor_trigger: dream_hold_star]` `[role: 主干]` 持执星宿，大富贵。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_316]` `[trigger: 梦见流星不落]` `[factor_trigger: dream_meteor_stay]` `[role: 主干]` 流星不落，主移居。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_317]` `[trigger: 梦见巡天摩星]` `[factor_trigger: dream_touch_star]` `[role: 主干]` 巡天摩星，位公卿。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_318]` `[trigger: 梦见云起四方]` `[factor_trigger: dream_cloud_rise]` `[role: 主干]` 云起四方，交易吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_319]` `[trigger: 梦见五色云]` `[factor_trigger: dream_colorful_cloud]` `[role: 主干]` 五色云，主大吉昌。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_320]` `[trigger: 梦见云赤白]` `[factor_trigger: dream_cloud_color]` `[role: 主干]` 云赤白吉，青黑凶。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_321]` `[trigger: 梦见见浮云]` `[factor_trigger: dream_floating_cloud]` `[role: 主干]` 见浮云，作事不成。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_322]` `[trigger: 梦见云雾遮事]` `[factor_trigger: dream_fog_cover]` `[role: 主干]` 云雾遮事，大吉利。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_323]` `[trigger: 梦见黑云至地]` `[factor_trigger: dream_black_cloud]` `[role: 主干]` 黑云至地，时气病。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_324]` `[trigger: 梦见霜雪降]` `[factor_trigger: dream_frost_snow]` `[role: 主干]` 霜雪降，主事不成。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_325]` `[trigger: 梦见雪下及时]` `[factor_trigger: dream_snow_timely]` `[role: 主干]` 雪下及时，大吉利。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_326]` `[trigger: 梦见雪落身上]` `[factor_trigger: dream_snow_body]` `[role: 主干]` 雪落身上，万事成。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_327]` `[trigger: 梦见雪不沾身]` `[factor_trigger: dream_snow_avoid]` `[role: 主干]` 雪不沾身，主孝服。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_328]` `[trigger: 梦见雪落家庭]` `[factor_trigger: dream_snow_home]` `[role: 主干]` 雪落家庭，主丧事。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_329]` `[trigger: 梦见阴雨晦暗]` `[factor_trigger: dream_gloomy_rain]` `[role: 主干]` 阴雨晦暗，主凶事。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_330]` `[trigger: 梦见行路逢雨]` `[factor_trigger: dream_rain_road]` `[role: 主干]` 行路逢雨，有酒食。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_331]` `[trigger: 梦见雷霆作事]` `[factor_trigger: dream_thunder_action]` `[role: 主干]` 雷霆作事，官位至。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_332]` `[trigger: 梦见雷声恐怕]` `[factor_trigger: dream_thunder_fear]` `[role: 主干]` 雷声恐怕，移居吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_333]` `[trigger: 梦见雷从地震]` `[factor_trigger: dream_thunder_earth]` `[role: 主干]` 雷从地震，主志遂。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_334]` `[trigger: 梦见身被霹雳]` `[factor_trigger: dream_thunderbolt]` `[role: 主干]` 身被霹雳，主富贵。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_335]` `[trigger: 梦见电光照身]` `[factor_trigger: dream_lightning]` `[role: 主干]` 电光照身，有吉庆。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_336]` `[trigger: 梦见赤虹见]` `[factor_trigger: dream_red_rainbow]` `[role: 主干]` 赤虹见吉，黑虹凶。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_337]` `[trigger: 梦见霞满天]` `[factor_trigger: dream_sunset_glow]` `[role: 主干]` 霞满天，百事欢悦。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_338]` `[trigger: 梦见狂风大雨]` `[factor_trigger: dream_storm]` `[role: 主干]` 狂风大雨，人死亡。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_339]` `[trigger: 梦见风吹人衣]` `[factor_trigger: dream_wind_clothes]` `[role: 主干]` 风吹人衣，主疾病。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_340]` `[trigger: 梦见忽大风]` `[factor_trigger: dream_sudden_wind]` `[role: 主干]` 忽大风，国有号令。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_341]` `[trigger: 梦见风如吼]` `[factor_trigger: dream_roaring_wind]` `[role: 主干]` 风如吼，主远信至。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_342]` `[trigger: 梦见白石凶]` `[factor_trigger: dream_baishi_xiong]` `[role: 主干]` 白石凶，主凶兆。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_343]` `[trigger: 梦见百忧去]` `[factor_trigger: dream_baiyou_qu]` `[role: 主干]` 百忧去，主忧散。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_344]` `[trigger: 梦见沐浴]` `[factor_trigger: dream_bath]` `[role: 主干]` 梦见沐浴，主洁净。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_345]` `[trigger: 梦见洗澡]` `[factor_trigger: dream_bathing]` `[role: 主干]` 梦见洗澡，主洁净更新。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_346]` `[trigger: 梦见洗身]` `[factor_trigger: dream_bathing_body]` `[role: 主干]` 梦见洗身，主洁净。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_347]` `[trigger: 梦见驯兽]` `[factor_trigger: dream_beast_tame]` `[role: 主干]` 梦见驯兽，主顺服。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_348]` `[trigger: 梦见打人]` `[factor_trigger: dream_beating_others]` `[role: 主干]` 梦见打人，主争斗。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_349]` `[trigger: 梦见被打]` `[factor_trigger: dream_being_beaten]` `[role: 主干]` 梦见被打，主灾祸。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_350]` `[trigger: 梦见被擒]` `[factor_trigger: dream_being_captured]` `[role: 主干]` 梦见被擒，主困厄。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_351]` `[trigger: 梦见受辱]` `[factor_trigger: dream_being_humiliated]` `[role: 主干]` 梦见受辱，主屈辱。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_352]` `[trigger: 梦见被杀]` `[factor_trigger: dream_being_killed]` `[role: 主干]` 梦见被杀，主大凶。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_353]` `[trigger: 梦见被骂]` `[factor_trigger: dream_being_scolded]` `[role: 主干]` 梦见被骂，主口舌。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_354]` `[trigger: 梦见病官事]` `[factor_trigger: dream_bing_guanshi]` `[role: 主干]` 梦见病官事，主病及官非。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_355]` `[trigger: 梦见鸟飞]` `[factor_trigger: dream_bird_fly]` `[role: 主干]` 梦见鸟飞，主远信。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_356]` `[trigger: 梦见祝福]` `[factor_trigger: dream_blessing]` `[role: 主干]` 梦见祝福，主吉祥。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_357]` `[trigger: 梦见船破]` `[factor_trigger: dream_boat_broken]` `[role: 主干]` 梦见船破，主灾祸。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_358]` `[trigger: 梦见乘船]` `[factor_trigger: dream_boat_ride]` `[role: 主干]` 梦见乘船，主远行。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_359]` `[trigger: 梦见身脏]` `[factor_trigger: dream_body_dirty]` `[role: 主干]` 梦见身脏，主有疾。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_360]` `[trigger: 梦见身汗]` `[factor_trigger: dream_body_sweat]` `[role: 主干]` 梦见身汗，主劳碌。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_361]` `[trigger: 梦见桥断]` `[factor_trigger: dream_bridge_broken]` `[role: 主干]` 梦见桥断，主阻隔。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_362]` `[trigger: 梦见镜破]` `[factor_trigger: dream_broken_mirror]` `[role: 主干]` 梦见镜破，主夫妻离。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_363]` `[trigger: 梦见佛菩萨]` `[factor_trigger: dream_buddha_bodhisattva]` `[role: 主干]` 梦见佛菩萨，主大吉。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_364]` `[trigger: 梦见财散]` `[factor_trigger: dream_caisan]` `[role: 主干]` 梦见财散，主破财。 → 《周公解梦·天地日月星辰》
  - `[ns_zgjm_365]` `[trigger: 梦见坐毯]` `[factor_trigger: dream_carpet_lie]` `[role: 主干]` 梦见坐毯，主安乐。 → 《周公解梦·天地日月星辰》

---"""
    normalized_text_zh: str = """"""
    subject: str = "天地日月星辰"
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
        l1_anchor="zgjm_v1.0.0_天地日月星辰_001_L1",
    )
    version: str = "1.0.0"
