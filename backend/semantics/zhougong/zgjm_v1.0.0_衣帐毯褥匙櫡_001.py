"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864383
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
    semantic_id="zgjm_v1.0.0_衣帐毯褥匙櫡_001",
    book_id="zhougong",
    engine_id="dream"
)
class 衣帐毯褥匙櫡(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  衣帐毯褥匙櫡。

  【条文】

  床帐改，主官迁移。
  舒展床帐，大富贵。
  新安床帐，远人来。

  床帐出门者，妻亡。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  衣帐毯褥匙櫡。

  【条文】

  床帐改，主官迁移。
  舒展床帐，大富贵。
  新安床帐，远人来。

  床帐出门者，妻亡。
  床帐收换，移居吉。
  床上有蚁，至不祥。

  床帐破损，妻欲亡。
  开帐幔，主有酒食。
  帐幔坏者，妻子病。

  床脚新换，奴仆凶。
  上床卧者，大凶恶。
  血在床，妻妾有奸。

  洗床帐，则主大吉。
  荐席入，吉；出，则凶。
  破席者，主失官位。

  换席入，吉；出，则凶。
  席箪者，主有力助。
  毯褥铺陈，万事稳。

  毁席幔者，妻有奸。
  新帘者，主得好妻。
  铺席合坐，得官位。

  好被自盖，主大吉。
  见好枕，有贵人扶。
  见手帕，主有口舌。

  手中缚布，病患至。
  毛肩忽持，官事至。
  鼎鼐者，主得大财。

  釜溢者，主得大财。
  玉石器，主有人助。
  铜铛者，主口舌至。

  锅铁破，主丧事来。
  铛盏破，主有恶事。
  磁碗者，主酒食至。

  磁碟者，主口舌至。
  匙，主益妻妾子孙。
  櫡，主益田宅奴仆。

  盆，主益仓库大吉。
  棳盆脱底，主财散。
  入盆瓮器，大富贵。

  洗面盆者，美妾至。
  大小盆者，主团圆。
  得盆子者，所求得。

  桶盛水者，主大吉。
  桶无水者，主大凶。
  人送大桶，主得利。

  桌架于宅，事不成。
  锯，主有断决之事。
  碾衣食，移居大吉。

  锤钻者，主侵害事。
  锤欲举动，有人持。
  凿，主被人驱使吉。

  熨斗盛火，好事成。
  熏笼者，益增田产。
  人与秤者，主权位。

  绳索，主长命大吉。
  绳索断者，主凶恶。
  人与凿者，得失金。

  人送带者，主得位。

- 分字分词释义：

  - **衣帐毯褥匙櫡**：本类总纲，涵盖床帐、被枕、席毯、帘幔，以及鼎鼐釜锅、碗碟盆桶、匙与櫡等家用器皿，多与**居家起居、卧榻安危与日常用度**有关。
  - **床帐改主官迁移；舒展床帐大富贵；新安床帐远人来**：床帐为卧息与婚床之所，改易、舒展与新安，多主职位变动、家业扩张与远方亲友或宾客来到。
  - **床帐出门者妻亡；床帐破损妻欲亡；床上有蚁至不祥**：床帐象征婚姻与家庭核心，出门或破损，则有妻亡或妻子疾病之忧；床上有蚁则暗示细碎烦扰与不祥之兆。
  - **洗床帐则主大吉；荐席、换席“入吉出凶”；毯褥铺陈万事稳**：洗净床帐属除旧布新，席入而不出象征资源与根基内聚，毯褥铺稳则起居安定，皆为吉象；相反，破席与席出，则主失官位与基础动摇。
  - **毁席幔者妻有奸；新帘者主得好妻；铺席合坐得官位**：席幔与帘幕既遮蔽亦代表礼数，毁则主婚姻不洁，新帘则象新缘与良配；铺席合坐则主人际和合与官位可得。
  - **好被自盖主大吉；见好枕有贵人扶；见手帕主有口舌**：被枕关乎休息与庇护，好被好枕主得保护与贵人扶助；手帕则与拭泪拭汗有关，多主口舌是非与情绪波动。
  - **鼎鼐釜锅玉石器铜铛**：大器完好与内容溢出，多主大财与有人助；锅铁、铛盏破则主丧事与恶事；铜铛易鸣，故主口舌纷争。
  - **匙主益妻妾子孙；櫡主益田宅奴仆；盆主益仓库大吉；棳盆脱底主财散；入盆瓮器大富贵**：匙、櫡、盆瓮皆为承载与分配之器，象征对家人、田宅与仓库的滋益或损耗：器稳则财聚，脱底则财散。
  - **桶盛水大吉；桶无水大凶；人送大桶主得利**：桶中有水则资源充足，无水则空有其器，为大凶；人送大桶则主未来有承载资源与职责之机会。
  - **桌架于宅事不成；锯、锤、钻、凿、熨斗、熏笼、秤与绳索带等器物**：皆象征裁断、修整、温养、权衡与约束，梦中出现时，多指现实中须作取舍、修补与承担权责，绳索不断则主长命，断则主凶恶。

- **规范化释义（primary_lang_explained）**：

  本类以床帐、被枕、席毯、帘幔以及各式家用器皿为纲，描绘的是一个家庭在**起居、饮食与器用**层面的安危与充盈：

  - 床帐与被枕所指向的是睡眠与婚床：改易、洗净与新安，多主官位迁转、远客来访与居家焕然一新；床帐出门、破损或床上有蚁，则多主妻妾有病、有忧甚至生死之虞。
  - 席帷与帘幔既是遮蔽之具也是礼数之物：荐席、换席“入吉出凶”，提示保持根基与资源在“家中”与“正位”即可吉；毁席幔与坏帘则暗示礼数失守与感情破裂。
  - 鼎鼐釜锅、碗碟盆桶与匙櫡等器皿，集中反映饮食与仓储状态：器物完好、有水有食则主酒食与财利；破损、脱底或空无一物则主财散、恶事与丧事。
  - 绳索、秤与带以及诸多工具，则关乎裁断、权衡与约束：工具在手，说明有能力处理事务；绳索不断则主长命，断则主凶恶；人送带与秤则主得位与获权。

- 核心要点：

  - **看卧具之新旧与改易**：床帐、新安、洗净与毯褥铺稳，多主居家与官位有利的调整；床帐出门、破损或床上有蚁，则提醒婚床与家中核心关系不宁。
  - **看席帷与帘幔之毁立**：荐席、换席入而不出，象征资源与根基内聚为吉；毁席幔与坏帘则预示感情与体面的破损。
  - **看器皿之盈虚与破损**：鼎鼐釜锅溢而不破、盆桶有水，是丰足与大财之象；锅铁、铛盏破裂、棳盆脱底或桶无水，则主财散、恶事与大凶。
  - **看盛器所益之对象**：匙主益妻妾子孙；櫡主益田宅奴仆；盆主益仓库——通过“承载之器”可以判断家庭中哪些方面受益或受损。
  - **看工具与权衡象征**：桌架未成、锯锤钻凿、熨斗熏笼与秤绳带等，提示现实中需要裁断、修整、温养与权衡，既有机会也有压力。

- 详细解说：

  **（一）床帐、席毯与婚床结构**

  - “床帐改，主官迁移；舒展床帐，大富贵；新安床帐，远人来”将床帐与官位、家业、来客三者相连：
    - 改床帐如同更换栖身之所，多主职位调动或居住环境改善；
    - 舒展床帐象征空间舒展、生活宽裕，多主富贵；
    - 新安床帐则预示即将迎来远客、亲友或新的亲密关系。
  - “床帐出门者，妻亡；床帐收换，移居吉；床上有蚁，至不祥；床帐破损，妻欲亡；床脚新换，奴仆凶；上床卧者，大凶恶；血在床，妻妾有奸”：
    - 床帐出门或破损，是婚床离位与失护之象，多主妻子有病或生死之忧；
    - 床脚新换则表示支撑结构变更，多应在奴仆或下属身上；
    - 床上有蚁与血在床，则分别暗示细碎的烦扰与情感不洁，需要警惕。

  **（二）席帷帘幔：遮蔽、礼数与界限**

  - “洗床帐，则主大吉；荐席入吉出则凶；换席入吉出则凶；席箪者，主有力助；毯褥铺陈，万事稳”：
    - 清洗与更新床帐，多主除旧布新；
    - 席入而不出，象征基础与资源被妥善保留在内部，故吉；
    - 毯褥铺陈则指起居有安稳基础，万事有所凭依。
  - “毁席幔者，妻有奸；新帘者，主得好妻；铺席合坐，得官位”：
    - 席幔毁坏，暗示婚姻礼数被破坏，容易应在感情变质或外遇上；
    - 新帘则为重立界限与体面，有得贤妻之象；
    - 铺席合坐，则象征在公开场合共坐之礼，有利于官位与人际提升。

  **（三）被枕与布帕：休息、庇护与口舌**

  - “好被自盖，主大吉；见好枕，有贵人扶；见手帕，主有口舌；手中缚布，病患至”：
    - 被褥与枕头直接关系睡眠质量与安全感，梦中见好被好枕，多主得到保护与贵人支持；
    - 手帕与缚布则与包裹、遮掩与束缚有关，前者多主口舌与情绪，后者主疾病缠身与行动不便。

  **（四）鼎釜碗盆与匙櫡：衣食与仓储的容器**

  - “鼎鼐者，主得大财；釜溢者，主得大财；玉石器，主有人助；铜铛者，主口舌至；锅铁破，主丧事来；铛盏破，主有恶事；磁碗者，主酒食至；磁碟者，主口舌至”一组，将大器、贵器与破器分别对应财、助与祸：
    - 鼎鼐与釜溢象征炊煮有余与资源丰厚，主大财；
    - 玉石器多为贵重器物，主得高人扶助；
    - 铜铛与磁碟与声音与言谈相连，主口舌是非；
    - 锅铁与铛盏破则预示生计中断、丧事与恶事。
  - “匙，主益妻妾子孙；櫡，主益田宅奴仆；盆，主益仓库大吉；棳盆脱底，主财散；入盆瓮器，大富贵；洗面盆者，美妾至；大小盆者，主团圆；得盆子者，所求得”：
    - 匙与櫡、盆与瓮器，分别指向家庭成员、田宅与仓库等不同领域；
    - 盆器完好且有水，象征储备丰足与团圆；
    - 棳盆脱底则提醒基础漏洞导致财物流失。

  **（五）桶、桌与工具：取舍、裁断与权衡**

  - “桶盛水者，主大吉；桶无水者，主大凶；人送大桶，主得利”：桶的关键在于“是否盛水”，即是否真正承载资源；
  - “桌架于宅，事不成”：桌子为摆放物品之所，架而未成，多主支撑不稳、规划未定，故事不成。
  - “锯，主有断决之事；碾衣食，移居大吉；锤钻者，主侵害事；锤欲举动，有人持；凿，主被人驱使吉；熨斗盛火，好事成；熏笼者，益增田产；人与秤者，主权位；绳索主长命大吉；绳索断者，主凶恶；人与凿者，得失金；人送带者，主得位”一系列工具象征：
    - 锯与凿代表裁断与开辟，需要作出决定与取舍；
    - 碾衣食象征通过劳作换取衣食与迁居之机；
    - 熨斗与熏笼分别象征理顺与温养，利于好事成与田产增；
    - 秤与带、绳索象征衡量、约束与联系：秤在手者有权衡之权，带与绳索完好者主得位与长命，断裂者则主凶恶与失控。



 - **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to clothing, bed curtains, carpets, quilts, keys, and cabinets. These images map onto **personal covering and protection, domestic comfort, access and secrets, and household management**.

  The core interpretive principle centers on the state and function of these domestic items: fine clothing indicates honor and proper social position; tattered garments warn of poverty or disgrace. Bed furnishings relate to rest, intimacy, and health—clean bedding suggests peaceful domestic life; dirty or torn bedding warns of marital troubles or illness. Keys symbolize access and control—having keys indicates authority over one's domain; losing keys suggests loss of control or secrets being exposed.

  **Key interpretive axes**:
  - **Clothing**: new or fine garments indicate improved status; torn or dirty clothes warn of disgrace or poverty; the color and type of garment carry specific meanings.
  - **Bed furnishings**: clean and comfortable bedding suggests peaceful rest and harmonious marriage; torn curtains or dirty quilts warn of domestic troubles or illness.
  - **Keys**: possessing keys indicates control and authority; losing keys warns of lost access or exposed secrets; receiving keys suggests being entrusted with responsibility.
  - **Storage and cabinets**: full cabinets indicate prosperity; empty or broken storage warns of depleted resources; locked containers relate to hidden matters.
  - **Latrines**: waste accumulation paradoxically suggests wealth gathering; cleanliness relates to proper management of resources; falling in often carries unexpected fortune.- 校勘与字词辨析：

  - “衣帐毯褥匙櫡”一题，各本或见“衣帐毯褥匙杓”等异文，本稿据底本录作“櫡”，并在释义中按“盛物承器”理解，不再分辨具体器形。
  - “鼎鼐者主得大财”中“鼐”字为大鼎名，部分通俗本或简化为“鼎釜”，本稿仍据底本保留“鼎鼐”写法，并在释义中以“大型炊具”统摄之。
  - “棳盆脱底主财散”之“棳”，或为盆架或特定盆名，L1 层不改字，仅按“承盆之物脱落导致盆器失用”理解为财散之象。
  - “席箪者主有力助”句，“箪”本指盛物之竹器，此处多指带结构的席具，本稿从“有层次、有支撑”之意理解为“有力助”。
  - 诸如“妻有奸”“妻妾有奸佞”等语，本稿保留原判语，在白话与详细解说中统一转化为“情感结构不稳、外缘介入或信任受损”等较中性的描述，为后续高阶语义层做准备。

  - **English**：
    - The category title "衣帐毯褥匙櫡" appears in some editions as "衣帐毯褥匙杓" with variant readings. This edition follows the base text as "櫡," interpreting it as "vessels for holding and receiving" without distinguishing specific vessel forms.
    - In "鼎鼐者主得大财," the character "鼐" refers to a large ceremonial tripod; some popular editions simplify it to "鼎釜." This edition preserves "鼎鼐" per the base text, summarizing it in the interpretation as "large cooking vessels."
    - In "棳盆脱底主财散," the character "棳" may refer to a basin stand or specific basin type. The L1 layer does not alter the character, interpreting it as "the basin support falling away, causing the basin to become useless," symbolizing wealth dispersing.
    - In "席箪者主有力助," the term "箪" originally refers to bamboo containers, here likely meaning structured seating. This edition interprets it based on "having layers, having support" as "having powerful assistance."
    - Phrases such as "妻有奸" and "妻妾有奸佞" are preserved in original verdict form, but uniformly transformed in vernacular and detailed commentary to more neutral descriptions like "unstable emotional structure, external interference or trust damage," preparing for higher semantic layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_422]` `[trigger: 梦见床帐改]` `[factor_trigger: dream_tent_change]` `[role: 主干]` 床帐改，主官迁移。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_423]` `[trigger: 梦见舒展床帐]` `[factor_trigger: dream_spread_tent]` `[role: 主干]` 舒展床帐，大富贵。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_424]` `[trigger: 梦见新安床帐]` `[factor_trigger: dream_new_tent]` `[role: 主干]` 新安床帐，远人来。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_425]` `[trigger: 梦见床帐出门者]` `[factor_trigger: dream_tent_out]` `[role: 主干]` 床帐出门者，妻亡。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_426]` `[trigger: 梦见床帐收换]` `[factor_trigger: dream_tent_swap]` `[role: 主干]` 床帐收换，移居吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_427]` `[trigger: 梦见床上有蚁]` `[factor_trigger: dream_bed_ants]` `[role: 主干]` 床上有蚁，至不祥。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_428]` `[trigger: 梦见床帐破损]` `[factor_trigger: dream_tent_torn]` `[role: 主干]` 床帐破损，妻欲亡。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_429]` `[trigger: 梦见开帐幔]` `[factor_trigger: dream_open_tent]` `[role: 主干]` 开帐幔，主有酒食。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_430]` `[trigger: 梦见帐幔坏者]` `[factor_trigger: dream_tent_damage]` `[role: 主干]` 帐幔坏者，妻子病。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_431]` `[trigger: 梦见床脚新换]` `[factor_trigger: dream_bed_leg]` `[role: 主干]` 床脚新换，奴仆凶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_432]` `[trigger: 梦见上床卧者]` `[factor_trigger: dream_lie_bed]` `[role: 主干]` 上床卧者，大凶恶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_433]` `[trigger: 梦见血在床]` `[factor_trigger: dream_blood_bed]` `[role: 主干]` 血在床，妻妾有奸。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_434]` `[trigger: 梦见洗床帐]` `[factor_trigger: dream_wash_tent]` `[role: 主干]` 洗床帐，则主大吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_435]` `[trigger: 梦见荐席入]` `[factor_trigger: dream_mat_in]` `[role: 主干]` 荐席入吉，出则凶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_436]` `[trigger: 梦见破席者]` `[factor_trigger: dream_mat_torn]` `[role: 主干]` 破席者，主失官位。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_437]` `[trigger: 梦见换席入]` `[factor_trigger: dream_mat_swap]` `[role: 主干]` 换席入吉，出则凶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_438]` `[trigger: 梦见席箪者]` `[factor_trigger: dream_mat_bamboo]` `[role: 主干]` 席箪者，主有力助。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_439]` `[trigger: 梦见毯褥铺陈]` `[factor_trigger: dream_blanket_spread]` `[role: 主干]` 毯褥铺陈，万事稳。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_440]` `[trigger: 梦见毁席幔者]` `[factor_trigger: dream_destroy_mat]` `[role: 主干]` 毁席幔者，妻有奸。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_441]` `[trigger: 梦见新帘者]` `[factor_trigger: dream_new_curtain]` `[role: 主干]` 新帘者，主得好妻。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_442]` `[trigger: 梦见铺席合坐]` `[factor_trigger: dream_sit_mat]` `[role: 主干]` 铺席合坐，得官位。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_443]` `[trigger: 梦见好被自盖]` `[factor_trigger: dream_quilt_cover]` `[role: 主干]` 好被自盖，主大吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_444]` `[trigger: 梦见见好枕]` `[factor_trigger: dream_good_pillow]` `[role: 主干]` 见好枕，有贵人扶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_445]` `[trigger: 梦见见手帕]` `[factor_trigger: dream_handkerchief]` `[role: 主干]` 见手帕，主有口舌。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_446]` `[trigger: 梦见手中缚布]` `[factor_trigger: dream_cloth_bind]` `[role: 主干]` 手中缚布，病患至。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_447]` `[trigger: 梦见毛肩忽持]` `[factor_trigger: dream_fur_shoulder]` `[role: 主干]` 毛肩忽持，官事至。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_448]` `[trigger: 梦见鼎鼐者]` `[factor_trigger: dream_tripod]` `[role: 主干]` 鼎鼐者，主得大财。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_449]` `[trigger: 梦见釜溢者]` `[factor_trigger: dream_pot_overflow]` `[role: 主干]` 釜溢者，主得大财。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_450]` `[trigger: 梦见玉石器]` `[factor_trigger: dream_jade_vessel]` `[role: 主干]` 玉石器，主有人助。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_451]` `[trigger: 梦见铜铛者]` `[factor_trigger: dream_copper_pot]` `[role: 主干]` 铜铛者，主口舌至。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_452]` `[trigger: 梦见锅铁破]` `[factor_trigger: dream_pot_break]` `[role: 主干]` 锅铁破，主丧事来。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_453]` `[trigger: 梦见铛盏破]` `[factor_trigger: dream_cup_break]` `[role: 主干]` 铛盏破，主有恶事。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_454]` `[trigger: 梦见磁碗者]` `[factor_trigger: dream_porcelain_bowl]` `[role: 主干]` 磁碗者，主酒食至。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_455]` `[trigger: 梦见磁碟者]` `[factor_trigger: dream_porcelain_plate]` `[role: 主干]` 磁碟者，主口舌至。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_456]` `[trigger: 梦见匙]` `[factor_trigger: dream_spoon]` `[role: 主干]` 匙，主益妻妾子孙。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_457]` `[trigger: 梦见櫡]` `[factor_trigger: dream_chopsticks]` `[role: 主干]` 櫡，主益田宅奴仆。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_458]` `[trigger: 梦见盆主益]` `[factor_trigger: dream_basin]` `[role: 主干]` 盆，主益仓库大吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_459]` `[trigger: 梦见棳盆脱底]` `[factor_trigger: dream_basin_bottom]` `[role: 主干]` 棳盆脱底，主财散。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_460]` `[trigger: 梦见入盆瓮器]` `[factor_trigger: dream_enter_vessel]` `[role: 主干]` 入盆瓮器，大富贵。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_461]` `[trigger: 梦见洗面盆者]` `[factor_trigger: dream_washbasin]` `[role: 主干]` 洗面盆者，美妾至。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_462]` `[trigger: 梦见大小盆者]` `[factor_trigger: dream_basin_size]` `[role: 主干]` 大小盆者，主团圆。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_463]` `[trigger: 梦见得盆子者]` `[factor_trigger: dream_get_basin]` `[role: 主干]` 得盆子者，所求得。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_464]` `[trigger: 梦见桶盛水者]` `[factor_trigger: dream_bucket_water]` `[role: 主干]` 桶盛水者，主大吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_465]` `[trigger: 梦见桶无水者]` `[factor_trigger: dream_bucket_empty]` `[role: 主干]` 桶无水者，主大凶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_466]` `[trigger: 梦见人送大桶]` `[factor_trigger: dream_send_bucket]` `[role: 主干]` 人送大桶，主得利。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_467]` `[trigger: 梦见桌架于宅]` `[factor_trigger: dream_table_house]` `[role: 主干]` 桌架于宅，事不成。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_468]` `[trigger: 梦见锯主有断决]` `[factor_trigger: dream_saw]` `[role: 主干]` 锯，主有断决之事。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_469]` `[trigger: 梦见碾衣食]` `[factor_trigger: dream_roll_clothes]` `[role: 主干]` 碾衣食，移居大吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_470]` `[trigger: 梦见锤钻者]` `[factor_trigger: dream_hammer_drill]` `[role: 主干]` 锤钻者，主侵害事。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_471]` `[trigger: 梦见锤欲举动]` `[factor_trigger: dream_hammer_move]` `[role: 主干]` 锤欲举动，有人持。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_472]` `[trigger: 梦见凿主被人]` `[factor_trigger: dream_chisel]` `[role: 主干]` 凿，主被人驱使吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_473]` `[trigger: 梦见熨斗盛火]` `[factor_trigger: dream_iron_fire]` `[role: 主干]` 熨斗盛火，好事成。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_474]` `[trigger: 梦见熏笼者]` `[factor_trigger: dream_fumigator]` `[role: 主干]` 熏笼者，益增田产。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_475]` `[trigger: 梦见人与秤者]` `[factor_trigger: dream_scale]` `[role: 主干]` 人与秤者，主权位。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_476]` `[trigger: 梦见绳索主]` `[factor_trigger: dream_rope]` `[role: 主干]` 绳索，主长命大吉。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_477]` `[trigger: 梦见绳索断者]` `[factor_trigger: dream_rope_break]` `[role: 主干]` 绳索断者，主凶恶。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_478]` `[trigger: 梦见人与凿者]` `[factor_trigger: dream_give_chisel]` `[role: 主干]` 人与凿者，得失金。 → 《周公解梦·衣帐毯褥匙櫡》
  - `[ns_zgjm_479]` `[trigger: 梦见人送带者]` `[factor_trigger: dream_send_belt]` `[role: 主干]` 人送带者，主得位。 → 《周公解梦·衣帐毯褥匙櫡》

---"""
    normalized_text_zh: str = """"""
    subject: str = "衣帐毯褥匙櫡"
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
        l1_anchor="zgjm_v1.0.0_衣帐毯褥匙櫡_001_L1",
    )
    version: str = "1.0.0"
