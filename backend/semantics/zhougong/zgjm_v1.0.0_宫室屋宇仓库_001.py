"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864335
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
    semantic_id="zgjm_v1.0.0_宫室屋宇仓库_001",
    book_id="zhougong",
    engine_id="dream"
)
class 宫室屋宇仓库(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  宫室屋宇仓库。

  【条文】

  入帝王宫，行大吉。
  拜朝廷者，主富贵。
  入王侯府库，大吉。

  行道宫，见仙主吉。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  宫室屋宇仓库。

  【条文】

  入帝王宫，行大吉。
  拜朝廷者，主富贵。
  入王侯府库，大吉。

  行道宫，见仙主吉。
  坐官府中，主大吉。
  神庙广大，事事吉。

  上楼阁坛，主大吉。
  上高堂，大富贵至。
  高楼饮酒，富贵至。

  家起高楼，安稳事。
  上城为人所拽，吉。
  上城被执，官职显。

  城郭广大，财喜多。
  城中行凶，出门吉。
  连城青色，有喜吉。

  登赤城郭，主大吉。
  盖城上屋，大吉利。
  上屋，主富出园吉。

  上屋破坏，家道凶。
  堂上有棺，身安乐。
  正堂倒陷，家主凶。

  覆盖屋宇，长命吉。
  屋宅更新，主大吉。
  风吹屋动，主迁移。

  迁入他人新宅，吉。
  居出宅，主妻喜事。
  搬移破屋，主美妻。

  人或典房，主官位。
  家道贫穷，大吉利。
  洒扫宅舍，远人来。

  典卖典舍，主失位。
  屋宅无人，主死亡。
  屋上穿舟，有暗昧。

  逾墙渡宅，百事去。
  与人争屋，主大凶。
  与妇人争屋，主吉。

  房梁忽折，主大凶。
  院宅坑下，主死亡。
  妻男墙下，官位至。

  墙上掘土，主更政。
  军人入宅，主大吉。
  死央瓦落，妇争斗。

  屋中生马，男信至。
  屋中生草，家欲空。
  屋上生松柏，益寿。

  修理田舍，有大喜。
  入寺院中，生男子。
  寺舍有经，病人痊。

  迁移尼寺，主病至。
  起盖仓库，福禄至。
  入仓库中，大吉昂。

  仓库崩坏，百事凶。

- 分字分词释义：

  - **宫室屋宇仓库**：本类总纲，囊括宫殿、官府、城郭、楼阁、民居、寺院与仓库等建筑空间，主要反映**居处安危、家道兴衰与官禄财谷**之象。
  - **入帝王宫行大吉；拜朝廷者主富贵；入王侯府库大吉**：进入帝王、朝廷、王侯府库之梦，多主接近权力核心与财源重地，为仕途与名誉上的大吉。
  - **行道宫见仙主吉；坐官府中主大吉；神庙广大事事吉**：在道宫、官府或宏大庙宇中行走、坐堂，多主有贵人、制度与神明庇护，凡事易成。
  - **上楼阁坛、上高堂、高楼饮酒**：登楼上阁、在高堂高楼宴饮，多主地位提升、视野开阔、富贵临身。
  - **家起高楼安稳事；城郭广大财喜多**：自家新起高楼、城郭广阔，多主家业扩展、根基稳固、财喜连绵。
  - **上城为人所拽吉；上城被执官职显**：被人拉上城头或在城上被拘执，多解作被“带上台面”或“被点名”，象征职责加重、官职显露。
  - **城中行凶出门吉；连城青色有喜吉；登赤城郭主大吉**：城内凶险而出门得吉，青城、赤城等色象多主有惊无险、终归喜庆。
  - **盖城上屋、大吉利；上屋主富出园吉**：在城上覆屋、登屋而出园，多主家业再上一层楼，或由旧境迁入更开阔之地。
  - **上屋破坏家道凶；正堂倒陷家主凶**：屋顶破坏、正堂倒陷，皆为家道受损、宗主不安之象。
  - **覆盖屋宇长命吉；屋宅更新主大吉；风吹屋动主迁移**：加盖屋宇、更新宅舍多主延年益寿与家运更新；屋被风吹动则主有迁居之变。
  - **迁入他人新宅吉；居出宅主妻喜事；搬移破屋主美妻**：迁入他人新宅，暗含借贵地之气；住出宅、搬移破屋，多与婚姻与妻子变动相关。
  - **人或典房主官位；家道贫穷大吉利**：典押房屋反而主官位，家道一时贫穷反主大吉，皆属“以损求益”的象法。
  - **洒扫宅舍远人来**：打扫宅舍，多主整顿内政、迎接远客。
  - **典卖典舍主失位；屋宅无人主死亡；屋上穿舟有暗昧**：卖出宅舍易致位分失守；屋宅空寂主有死亡之忧；屋上穿舟多指暗昧隐情。
  - **逾墙渡宅百事去；与人争屋主大凶；与妇人争屋主吉**：翻墙渡宅有“离旧入新”与避祸之象；与人争屋主大凶，与妇争屋反主吉，暗示内部家事可调和，外争则多祸。
  - **房梁忽折主大凶；院宅坑下主死亡；妻男墙下官位至**：梁折、坑陷多为结构性大祸；“妻男墙下官位至”则主因家人或子嗣之力而得官。
  - **墙上掘土主更政；军人入宅主大吉；死央瓦落妇争斗**：墙上掘土象征改制、更政；军人入宅多主武职或防护之利；“死央瓦落”则主妇女间争斗。
  - **屋中生马男信至；屋中生草家欲空；屋上生松柏益寿**：屋中生马主有男子或男性消息；屋中生草则家道空虚；屋上松柏则主长寿与家运长久。
  - **修理田舍有大喜；入寺院中生男子；寺舍有经病人痊**：修整田舍、寺院多主丰年与病愈；“入寺院中生男子”常被视作得子或得贤徒之象。
  - **迁移尼寺主病至；起盖仓库福禄至；入仓库中大吉昂；仓库崩坏百事凶**：尼寺偏清冷、孤寂，迁居于此易主病；仓库完好则福禄充盈，仓库崩坏则诸事不顺。

- **规范化释义（primary_lang_explained）**：

  本类以“宫室屋宇仓库”为纲，综合讨论宫廷、城郭、官府庙宇，以及普通人家的房屋、庭院、寺院与仓库等建筑空间在梦中的吉凶。

  大体上：

  - **向上攀登、入宫入郡、楼阁高堂，多主地位提升、家业兴隆。**
  - **屋宇完固、加盖更新，主长命与家运更新；屋毁堂陷，则主根基受损。**
  - **迁宅、典卖与争屋，关乎居所与婚姻结构的变动，外争多凶、内调尚可。**
  - **城郭、城门与军人入宅，多与官职、守御与权势场域的变化相关。**
  - **寺院与仓库，前者主福德与疾病，后者主福禄与财谷盈虚。**

- 核心要点：

  - **看“居所高低与坚固”：**
    - 登楼上堂、家起高楼，主居处安全、人生位置上升；
    - 堂倒梁折、屋上破坏，主家道受损、宗主不安。
  - **看“城郭宫室”：**
    - 入帝王宫、王侯府库、官府庙宇，多主接近权力与资源中心；
    - 城中行凶而能出门，主有惊无险，能离开是非之地。
  - **看“迁宅典卖”：**
    - 迁入新宅、屋宅更新多为吉象；
    - 典卖住房、争屋斗宅则多与位分、婚姻与家业之争有关，凶多吉少。
  - **看“屋内异象”：**
    - 屋中生马主男信与行动机会；
    - 屋中生草则象征家道荒废；
    - 屋上松柏则主延寿与福荫绵长。
  - **看“寺院与仓库”：**
    - 入寺得子、寺舍有经主病愈与福德；
    - 仓库坚固主福禄充盈，仓库崩坏则百事受损。

- 详细解说：

  **（一）宫城楼阁：权势与视野的结构**

  - “入帝王宫行大吉”“拜朝廷者主富贵”“入王侯府库大吉”等条，共同构成“接近权力中心”的意象：
    - 对仕途者，多主得上级赏识、接触机要之事；
    - 对平民而言，则可理解为进入大机构、大企业或权力机构内部。
  - “上楼阁坛主大吉”“上高堂大富贵至”“高楼饮酒富贵至”，则强调“登高而望远”：
    - 登高象征社会层级提升与格局放大；
    - 在高楼饮酒，更带有庆功宴、功成后的享受之意。
  - “城郭广大财喜多”“连城青色有喜吉”“登赤城郭主大吉”中，城郭的规模与颜色皆被赋予吉凶：
    - 城广而固，多主外部环境宽阔、安全；
    - 青城、赤城多与文武之气相应，寓有官禄与喜庆。

  **（二）屋宇、正堂与家道根基**

  - 屋宇代表日常生活的容器：“家起高楼安稳事”“覆盖屋宇长命吉”“屋宅更新主大吉”，都指向居所稳固与升级，对应现实中的住房改善、安家立业。
  - 与此相对，“上屋破坏家道凶”“正堂倒陷家主凶”“房梁忽折主大凶”“院宅坑下主死亡”则是对房屋结构性损坏的敏感反应：
    - 正堂、梁柱象征家庭核心与支柱人物，损坏往往喻示家中长辈、主事者有病患或权威受损。
  - “堂上有棺身安乐”一语较为反常：
    - 古解多作“凶已至而得以安置”，故反主身安乐；
    - 亦可解为对死亡议题适度正视，反能减轻恐惧与灾祸。

  **（三）迁宅、典卖与婚姻结构的变动**

  - “风吹屋动主迁移”“迁入他人新宅吉”“居出宅主妻喜事”“搬移破屋主美妻”一组，都涉及居所变更：
    - 风动屋摇，预示搬迁、调动或居住环境改变；
    - 迁入他人新宅，多主借贵人或新系统之势；
    - 居出宅、搬移破屋，则往往连带婚姻或伴侣更替。
  - “人或典房主官位”“典卖典舍主失位”体现了“以房比位”的象法：
    - 典押房屋，短痛换长久，多被视作为官位或身份调整作准备；
    - 全然卖舍则意味地基尽失，易对应职位丧失或关系断绝。
  - “与人争屋主大凶；与妇人争屋主吉”则精细地区分了争执对象：
    - 与外人争屋，多主诉讼、纠纷与财产损失；
    - 与内妇争屋，虽然仍有矛盾，但多在家庭体系内可调和，反主事情得以梳理。

  **（四）墙垣、院宅与制度更替**

  - “逾墙渡宅百事去”象征跨越界限、抛弃旧局：
    - 对被困境中者，是一种突破与脱身；
    - 但若带有偷越之感，则需防范越矩行为引发后患。
  - “墙上掘土主更政”把墙视为制度的边界：
    - 掘土改墙，多与规章制度调整、体制重组相应；
    - 若梦境中伴随不安，则提醒改革中不可轻忽根基。
  - “军人入宅主大吉”则从正面表现守护之象：
    - 军人象征纪律与防御，入宅为守护而非侵扰，多主获得外部力量的保护与秩序引入。

  **（五）寺院、仓库与福禄疾病**

  - 寺院相关：“入寺院中生男子”“寺舍有经病人痊”“迁移尼寺主病至”：
    - 正常寺院、经卷与僧众多主福德与病愈；
    - 尼寺因清冷孤寂，易被视为病弱、离群之象。
  - 仓库相关：“起盖仓库福禄至”“入仓库中大吉昂”“仓库崩坏百事凶”：
    - 仓库是粮食与财物储藏之所，其完好象征资源充盈与后路无忧；
    - 仓库崩坏，则预示储备耗尽、计划失守，事业与家庭皆受牵连。



- **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to palaces, halls, houses, rooms, granaries, and warehouses. These images map onto **status and position, family fortune, resource storage, and domestic structure**.

  The core interpretive principle hinges on the building's condition, location, and changes: ascending to a high hall signifies rising status and fortune; a collapsing or burning house warns of declining family fortune or unexpected disaster; granaries and warehouses full of grain promise wealth accumulation; empty or damaged storage signals resource depletion. Building new structures typically portends new opportunities or family expansion; entering underground chambers may indicate hidden matters or approaching illness.

  **Key interpretive axes**:
  - **Building type**: palaces and great halls relate to official status and power; ordinary houses relate to family situation; granaries and warehouses relate to material wealth and reserves.
  - **Structural condition**: intact and bright buildings are auspicious; damaged, leaning, or collapsing structures warn of setbacks; new construction signals fresh starts.
  - **Directional movement**: ascending to upper floors or rooftops indicates rising fortune; descending to basements or underground suggests hidden troubles or declining health.
  - **Fullness or emptiness**: storerooms filled with goods promise prosperity; empty rooms suggest poverty or loss.- 校勘与字词辨析：

  - 本类原文多以三句并列连写，如“入帝王宫行大吉　拜朝廷者主富贵　入王侯府库大吉”等，本稿于 L1 层拆为数句并加标点，仅为阅读与后续处理方便，不改动原字序。
  - “家道贫穷大吉利”一语表面自相矛盾，古籍中常见“以贫守分而得吉”的观念，本稿在释义与详细解说中按“清苦自守、远离祸端”之意理解。
  - “屋上穿舟有暗昧”中“穿舟”一语颇为少见，多解为屋顶有舟形穿插或架物，本稿从“上悬异物、暗中往来”之象释为暗昧不明之事。
  - “死央瓦落妇争斗”一语，“死央”或作“死殃”“死殃瓦落”，多指不祥之物坠落，本稿据底本录作“死央瓦落”，在白话中仅以“不祥之兆”释义。
  - “大吉昂”“昂”字各本或作“昌”“亨”等，本稿从其“高举、兴盛”之意，保留“昂”字而不改。

  - **English**：
    - The original text presents entries in groups of three parallel phrases, e.g. "入帝王宫行大吉　拜朝廷者主富贵　入王侯府库大吉." This edition splits them into separate sentences with punctuation for reading convenience, without altering the original character order.
    - "家道贫穷大吉利" appears contradictory on the surface. Ancient texts often contain the concept of "finding fortune through maintaining one's station in poverty." This edition interprets it as "living simply and staying away from calamity."
    - In "屋上穿舟有暗昧," the term "穿舟" is quite rare, generally interpreted as a boat-shaped object piercing or suspended from the roof. This edition interprets it as "something unusual overhead, secret comings and goings," symbolizing obscure and unclear matters.
    - In "死央瓦落妇争斗," the term "死央" appears in variants as "死殃" or "死殃瓦落," generally referring to inauspicious objects falling. This edition follows the base text as "死央瓦落," interpreting it simply as "an ominous sign."
    - The character "昂" in "大吉昂" appears in other editions as "昌" or "亨." This edition preserves "昂" based on its meaning of "rising high, flourishing" without changing it.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_176]` `[trigger: 梦见入帝王宫]` `[factor_trigger: dream_palace]` `[role: 主干]` 入帝王宫，行大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_177]` `[trigger: 梦见拜朝廷者]` `[factor_trigger: dream_bow_court]` `[role: 主干]` 拜朝廷者，主富贵。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_178]` `[trigger: 梦见入王侯府库]` `[factor_trigger: dream_noble_treasury]` `[role: 主干]` 入王侯府库，大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_179]` `[trigger: 梦见行道宫见仙]` `[factor_trigger: dream_taoist_temple]` `[role: 主干]` 行道宫见仙，主吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_180]` `[trigger: 梦见坐官府中]` `[factor_trigger: dream_sit_office]` `[role: 主干]` 坐官府中，主大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_181]` `[trigger: 梦见神庙广大]` `[factor_trigger: dream_temple_large]` `[role: 主干]` 神庙广大，事事吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_182]` `[trigger: 梦见上楼阁坛]` `[factor_trigger: dream_climb_pavilion]` `[role: 主干]` 上楼阁坛，主大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_183]` `[trigger: 梦见上高堂]` `[factor_trigger: dream_high_hall]` `[role: 主干]` 上高堂，大富贵至。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_184]` `[trigger: 梦见高楼饮酒]` `[factor_trigger: dream_tower_wine]` `[role: 主干]` 高楼饮酒，富贵至。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_185]` `[trigger: 梦见家起高楼]` `[factor_trigger: dream_build_tower]` `[role: 主干]` 家起高楼，安稳事。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_186]` `[trigger: 梦见上城为人所拽]` `[factor_trigger: dream_pulled_wall]` `[role: 主干]` 上城为人所拽，吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_187]` `[trigger: 梦见上城被执]` `[factor_trigger: dream_arrested_wall]` `[role: 主干]` 上城被执，官职显。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_188]` `[trigger: 梦见城郭广大]` `[factor_trigger: dream_city_large]` `[role: 主干]` 城郭广大，财喜多。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_189]` `[trigger: 梦见城中行凶]` `[factor_trigger: dream_violence_city]` `[role: 主干]` 城中行凶，出门吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_190]` `[trigger: 梦见连城青色]` `[factor_trigger: dream_blue_wall]` `[role: 主干]` 连城青色，有喜吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_191]` `[trigger: 梦见登赤城郭]` `[factor_trigger: dream_red_city]` `[role: 主干]` 登赤城郭，主大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_192]` `[trigger: 梦见盖城上屋]` `[factor_trigger: dream_roof_wall]` `[role: 主干]` 盖城上屋，大吉利。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_193]` `[trigger: 梦见上屋主富]` `[factor_trigger: dream_roof_wealth]` `[role: 主干]` 上屋主富，出园吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_194]` `[trigger: 梦见上屋破坏]` `[factor_trigger: dream_roof_damage]` `[role: 主干]` 上屋破坏，家道凶。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_195]` `[trigger: 梦见堂上有棺]` `[factor_trigger: dream_coffin_hall]` `[role: 主干]` 堂上有棺，身安乐。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_196]` `[trigger: 梦见正堂倒陷]` `[factor_trigger: dream_hall_collapse]` `[role: 主干]` 正堂倒陷，家主凶。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_197]` `[trigger: 梦见覆盖屋宇]` `[factor_trigger: dream_cover_house]` `[role: 主干]` 覆盖屋宇，长命吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_198]` `[trigger: 梦见屋宅更新]` `[factor_trigger: dream_house_renew]` `[role: 主干]` 屋宅更新，主大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_199]` `[trigger: 梦见风吹屋动]` `[factor_trigger: dream_wind_house]` `[role: 主干]` 风吹屋动，主迁移。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_200]` `[trigger: 梦见迁入他人新宅]` `[factor_trigger: dream_move_newhouse]` `[role: 主干]` 迁入他人新宅，吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_201]` `[trigger: 梦见居出宅]` `[factor_trigger: dream_leave_house]` `[role: 主干]` 居出宅，主妻喜事。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_202]` `[trigger: 梦见搬移破屋]` `[factor_trigger: dream_move_old_house]` `[role: 主干]` 搬移破屋，主美妻。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_203]` `[trigger: 梦见人或典房]` `[factor_trigger: dream_pawn_house]` `[role: 主干]` 人或典房，主官位。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_204]` `[trigger: 梦见家道贫穷]` `[factor_trigger: dream_poor_home]` `[role: 主干]` 家道贫穷，大吉利。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_205]` `[trigger: 梦见洒扫宅舍]` `[factor_trigger: dream_clean_house]` `[role: 主干]` 洒扫宅舍，远人来。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_206]` `[trigger: 梦见典卖典舍]` `[factor_trigger: dream_sell_house]` `[role: 主干]` 典卖典舍，主失位。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_207]` `[trigger: 梦见屋宅无人]` `[factor_trigger: dream_empty_house]` `[role: 主干]` 屋宅无人，主死亡。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_208]` `[trigger: 梦见屋上穿舟]` `[factor_trigger: dream_boat_roof]` `[role: 主干]` 屋上穿舟，有暗昧。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_209]` `[trigger: 梦见逾墙渡宅]` `[factor_trigger: dream_climb_wall]` `[role: 主干]` 逾墙渡宅，百事去。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_210]` `[trigger: 梦见与人争屋]` `[factor_trigger: dream_house_dispute]` `[role: 主干]` 与人争屋，主大凶。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_211]` `[trigger: 梦见与妇人争屋]` `[factor_trigger: dream_woman_dispute]` `[role: 主干]` 与妇人争屋，主吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_212]` `[trigger: 梦见房梁忽折]` `[factor_trigger: dream_beam_break]` `[role: 主干]` 房梁忽折，主大凶。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_213]` `[trigger: 梦见院宅坑下]` `[factor_trigger: dream_pit_house]` `[role: 主干]` 院宅坑下，主死亡。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_214]` `[trigger: 梦见妻男墙下]` `[factor_trigger: dream_family_wall]` `[role: 主干]` 妻男墙下，官位至。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_215]` `[trigger: 梦见墙上掘土]` `[factor_trigger: dream_dig_wall]` `[role: 主干]` 墙上掘土，主更政。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_216]` `[trigger: 梦见军人入宅]` `[factor_trigger: dream_soldier_house]` `[role: 主干]` 军人入宅，主大吉。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_217]` `[trigger: 梦见死央瓦落]` `[factor_trigger: dream_tile_fall]` `[role: 主干]` 死央瓦落，妇争斗。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_218]` `[trigger: 梦见屋中生马]` `[factor_trigger: dream_horse_house]` `[role: 主干]` 屋中生马，男信至。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_219]` `[trigger: 梦见屋中生草]` `[factor_trigger: dream_grass_house]` `[role: 主干]` 屋中生草，家欲空。 → 《周公解梦·宫室屋宇仓库》
  - `[ns_zgjm_220]` `[trigger: 梦见屋上生松柏]` `[factor_trigger: dream_pine_roof]` `[role: 主干]` 屋上生松柏，益寿。 → 《周公解梦·宫室屋宇仓库》"""
    normalized_text_zh: str = """"""
    subject: str = "宫室屋宇仓库"
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
        l1_anchor="zgjm_v1.0.0_宫室屋宇仓库_001_L1",
    )
    version: str = "1.0.0"
