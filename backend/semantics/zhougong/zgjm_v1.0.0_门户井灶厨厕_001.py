"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864348
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
    semantic_id="zgjm_v1.0.0_门户井灶厨厕_001",
    book_id="zhougong",
    engine_id="dream"
)
class 门户井灶厨厕(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  门户井灶厨厕。

  【条文】

  门户高大，主富贵。
  新开门户，大富贵。
  门户忽开，主大吉。

  门户大开，大吉利。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  门户井灶厨厕。

  【条文】

  门户高大，主富贵。
  新开门户，大富贵。
  门户忽开，主大吉。

  门户大开，大吉利。
  门更新，主生贵子。
  门自开，妻有私情。

  门户裂开，主大吉。
  门户破坏，有凶事。
  城门大开，主口舌。

  宫城塞者，口舌至。
  门户闭塞，事不通。
  门户破坏，主大凶。

  门扇自折，奴仆走。
  门户内无人，大凶。
  修移门户，大吉利。

  石为门户，主寿命。
  门前生草，作刺史。
  门前坑沟，事不成。

  天火烧门，主凶事。
  屋开小门，主私情。
  穿井见水，远信至。

  井自损坏，家大败。
  井中沸溢，主得财。
  井枯涸者，家财散。

  井中照身，禄位至。
  身坠井中，疾病凶。
  房在井中，主见病。

  取井水清，吉；混，凶。
  井水负泥，出财主。
  井中欲干，家欲破。

  井中有鱼，身主贵。
  窥井有声，口舌生。
  伏藏井中，刑狱事。

  醉落井中，官事至。
  家住井中，长子凶。
  人云出井，喜气至。

  淘井造井，主大贵。
  器皿落井，有吉事。
  灶下水流，得横财。

  灶下燃火，有声名。
  灶釜破败，有死亡。
  灶下吹者，家破败。

  灶下鸣器，主口舌。
  屋有二灶，事不成。
  修造厨灶，大吉利。

  在官厨中，得财禄。
  自吹臼中，妻妾亡。
  淘厕者，主得横财。

  上厕在屎尿中，吉。
  厕中屎溢，大吉利。
  粪中坐者，主大凶。

  粪土堆积，主得财。

- 分字分词释义：

  - **门户井灶厨厕**：本类总纲，涵盖住宅的“出入口、井水、炉灶与厕所”等基础设施，象征**家门气口、资源泉源、饮食之道与秽浊之地**的运转情况。
  - **门户高大主富贵；新开门户大富贵；门更新主生贵子**：门象征出入与对外连接，高大端正、新开与更新，多主身份提升、财路拓展与子嗣兴旺。
  - **门户忽开主大吉；门户裂开主大吉**：门忽然开启或裂开，传统多解作“堵塞之处被打开”，主原本受阻之事突然通达。
  - **门自开妻有私情；屋开小门主私情**：门自启、小门暗开，都与隐秘往来与私情相关，多主感情或家庭隐忧。
  - **门户破坏有凶事；门户破坏主大凶；城门大开主口舌；宫城塞者口舌至；门户闭塞事不通**：门坏、城门乱开或闭塞不通，皆主是非、诉讼与阻滞，需防对外交往与信息沟通中的问题。
  - **门扇自折奴仆走；门户内无人大凶**：门扇折断、门内无人，多主下属离散、家中空虚，是家道衰败的象。
  - **石为门户主寿命；门前生草作刺史；门前坑沟事不成**：门户以石为框，象征坚固长久，主寿命；门前青草与坑沟，则分别对应仕进机会与行事阻碍。
  - **穿井见水远信至；井中沸溢主得财；井枯涸者家财散**：井为水源与财源，见清水、沸溢多主财利与消息通达；井枯则财散、资源枯竭。
  - **井中照身禄位至；身坠井中疾病凶；房在井中主见病**：井如镜能照见自身，主禄位显露；坠井或房屋陷入井中，则与疾病与危局相关。
  - **取井水清吉混凶；井水负泥出财主；井中欲干家欲破**：取水清明则吉，混浊则凶；井水负泥象征历经劳作仍能出财；井将干则家运将衰。
  - **井中有鱼身主贵；窥井有声口舌生；伏藏井中刑狱事；醉落井中官事至；家住井中长子凶**：鱼、声、伏藏与醉落等象，共同构成交际、是非、官非与子嗣损耗诸象。
  - **淘井造井主大贵；器皿落井有吉事**：整修、开新井多主更新资源、得贵人；器皿落井则有意外之喜。
  - **灶下水流得横财；灶下燃火有声名；灶釜破败有死亡；灶下吹者家破败；灶下鸣器主口舌**：灶象征饮食与家中柴米，水流、火旺与敲击声各有吉凶，对应横财、名声与口舌争端。
  - **屋有二灶事不成；修造厨灶大吉利；在官厨中得财禄**：灶宜一而不宜二，二灶多主意见分歧与资源分散；修造厨灶与在官厨中，多主饮食稳定与财禄。
  - **自吹臼中妻妾亡；淘厕者主得横财；上厕在屎尿中吉；厕中屎溢大吉利；粪中坐者主大凶；粪土堆积主得财**：厕与粪土为秽浊之处，然而适当接触与清理反有“去旧纳新、以污换财”的象。

- **规范化释义（primary_lang_explained）**：

  本类围绕“门、井、灶、厨、厕”五个核心要素，描绘的是一个家庭的**气口（门）、水源（井）、饮食（灶厨）与排出（厕所）**状况。

  - 门户端正高大、更新得时，多主家运扩展、福气临门；门坏、门闭与城门混乱，则多主是非口舌与道路受阻。
  - 井水清澈、沸溢、内有鱼与照身，多主财源充足、消息顺畅与身价提升；井枯、井坏、坠井则代表资源与健康的严重警讯。
  - 灶火顺畅、水火相济，则饮食有节、名利可得；灶破、灶下吹与二灶并立，则预示家中不宁与生计问题。
  - 厕与粪土虽属不净之地，却承载“去旧纳新、排毒弃秽”的功能：适度涉入与清理，多与横财、病愈有关；反之若长期滞留或坐于其上，则为重凶。

- 核心要点：

  - **看门：气口与出入**
    - 高大、更新、新开之门，多主富贵与贵子；
    - 门坏、门闭、城门混乱，则多主是非、阻滞与官讼。
  - **看井：水源与深层资源**
    - 井水清满、沸溢、鱼跃，多主财源与机会；
    - 井枯、坠井、伏藏井中，则需警惕资源枯竭与隐秘纠纷。
  - **看灶：饮食与名声**
    - 灶火旺、灶下水流得横财、灶下燃火有声名，是饮食充足与名声渐扬之象；
    - 灶釜破败、灶下吹与二灶并立，则预示生计摇摆、家庭不睦。
  - **看厕与粪土：去旧纳新之道**
    - 上厕、淘厕与粪土堆积，多主清理旧秽、得财去病；
    - 粪中久坐不出，则象征被困于污浊之境，难以自拔。

- 详细解说：

  **（一）门户：对外连结与口舌是非**

  - “门户高大主富贵”“新开门户大富贵”“门更新主生贵子”体现了门作为“气口”的积极意义：
    - 高大象征格局打开与身份抬升；
    - 新开与更新，则指新的通道开启，代表新的事业、关系与子嗣机会。
  - 与此相对，“门户破坏有凶事”“门户破坏主大凶”“城门大开主口舌”“宫城塞者口舌至”“门户闭塞事不通”：
    - 门坏与闭塞，预示对外联系受阻，信息不通；
    - 城门忽开或防线紊乱，则易引发官司、舆论与集体事件。
  - “门自开妻有私情”“屋开小门主私情”则更直接与隐秘往来相关：
    - 自开与偏门象征“未经允许的出入”，古解多主感情与婚姻的隐患；
    - 现代解读中，也可理解为“界限松动、边界不清”。

  **（二）井水：资源与潜意识的深井**

  - 井不仅是饮水之源，也是储备资源与潜在信息之象：“穿井见水远信至”“井中沸溢主得财”“井水负泥出财主”：
    - 清水、沸溢与负泥均提示资源动起来、信息流动，虽有劳碌，却有收获。
  - “井枯涸者家财散”“井中欲干家欲破”“井自损坏家大败”则是资源枯竭的强烈警讯：
    - 预示长期透支、不再进水之危机；
    - 现实中多对应经济、健康或情绪资源的耗损。
  - “井中照身禄位至”“井中有鱼身主贵”：
    - 井如镜能照见自身，象征发现自我价值、职位与名誉得以确认；
    - 鱼则代表生机与机缘，井中有鱼，恰似深处藏贵。
  - “身坠井中疾病凶”“醉落井中官事至”“伏藏井中刑狱事”“家住井中长子凶”：
    - 坠井象征陷入情绪或事件的深渊；
    - 醉而坠井，更带有因放纵失守招来官非或事故之意；
    - 长住井中，则是长期困囿于狭隘环境，容易应在长子或家中主要继承人身上。

  **（三）灶厨：生计与名声的火候**

  - 灶系饮食之本，亦象征家庭生计：“灶下水流得横财”“灶下燃火有声名”说明：
    - 水流而不泛滥，象征额外财源流入；
    - 火燃而不焚毁，象征名声与影响力上升。
  - “灶釜破败有死亡”“灶下吹者家破败”：
    - 釜破则无以炊煮，对应生计中断与家庭支柱崩坏；
    - 灶下乱吹，象征风火失调，言行与资源调度皆易失控。
  - “屋有二灶事不成”“修造厨灶大吉利”“在官厨中得财禄”：
    - 二灶并存，容易出现“各自为政”的情况，预示合作与计划难以统一；
    - 修整灶厨与在官厨掌勺，则象征重新调整资源、受托管理公共资源，故吉。

  **（四）厕与粪土：排毒与财气的矛盾象**

  - “淘厕者主得横财”“上厕在屎尿中吉”“厕中屎溢大吉利”“粪土堆积主得财”：
    - 虽属污秽，但代表“废物集中、能量待转化”的场域；
    - 主人愿意处理、清理这些污秽，反能在他人避之不及处获取利益。
  - 与之相对，“粪中坐者主大凶”：
    - 久坐粪中，象征沉溺于污浊、负面情境而不走出，故凶象极重。
  - 古人由此提醒：对秽浊之事，宜“过而不留”“治而不恋”，方能化污为利。



 - **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to gates, doors, wells, stoves, kitchens, and latrines. These images map onto **boundaries and access, domestic resources, nourishment systems, and waste disposal**.

  The core interpretive principle focuses on the state and function of these household fixtures: gates and doors opening smoothly indicate favorable transitions and opportunities; blocked or broken doors suggest obstacles or family discord. Wells with clear water promise abundant resources and good fortune; dry or polluted wells warn of depleted livelihood. Bright stove fires indicate thriving household economy; extinguished fires suggest family difficulties. Latrines, paradoxically, often carry positive meaning—overflowing with waste can symbolize incoming wealth, while falling into latrines may indicate profit despite initial disgust.

  **Key interpretive axes**:
  - **Gates and doors**: opening indicates opportunity and smooth passage; closing or breaking indicates obstruction and family troubles; the direction of opening matters for determining fortune flow.
  - **Wells**: clear and full wells bring prosperity; murky or dry wells warn of resource depletion; objects falling into wells often relate to loss of family members or valuables.
  - **Stoves and kitchens**: bright flames indicate prosperous household; cold or dark stoves suggest poverty or mourning; food cooking well promises nourishment and abundance.
  - **Latrines**: waste accumulation paradoxically suggests wealth gathering; cleanliness relates to proper management of resources; falling in often carries unexpected fortune.
  - **Fullness or emptiness**: storerooms filled with goods promise prosperity; empty rooms suggest poverty or loss.- 校勘与字词辨析：

  - 本类原文多以门、井、灶、厕为组，以三句或多句连写，本稿在 L1 层将其拆分为独立句并加标点，方便阅读与后续分层，不改动原字次序。
  - “井水负泥出财主”一语，“负泥”或作“附泥”，皆指水中带泥而出，本稿从“劳作而有获利”的意象理解，不就字形多做考据。
  - “家住井中长子凶”句，“井中”不作真实居住之解，而视为比喻“环境狭隘、上下难通”，L1 层忠实记述，在白话中略作说明，不引申过多灾异。
  - 关于厕与粪土的诸语，原书多以财、凶相杂，本稿遵其吉凶判断，同时在释义中强调“处理污秽”的心理与象征意涵，为后续高阶语义层预留空间。

  - **English**：
    - The original text in this category groups entries by doors, wells, stoves, and toilets, presented in three or more consecutive phrases. This edition splits them into independent sentences with punctuation at the L1 layer for reading convenience and subsequent layering, without changing the original character order.
    - In "井水负泥出财主," the term "负泥" may also be written as "附泥," both referring to water carrying mud when drawn. This edition interprets it as "labor yielding profit" without extensive philological research on character forms.
    - In "家住井中长子凶," the phrase "井中" is not interpreted as literal dwelling, but as a metaphor for "a narrow environment with blocked vertical movement." The L1 layer records faithfully with brief explanation in vernacular, without overextending into disaster omens.
    - Regarding the various phrases about toilets and excrement, the original text mixes fortune and misfortune. This edition follows its fortune-misfortune judgments while emphasizing in the interpretation the psychological and symbolic implications of "dealing with filth," leaving space for higher semantic layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_221]` `[trigger: 梦见门户高大]` `[factor_trigger: dream_door_grand]` `[role: 主干]` 门户高大，主富贵。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_222]` `[trigger: 梦见新开门户]` `[factor_trigger: dream_new_door]` `[role: 主干]` 新开门户，大富贵。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_223]` `[trigger: 梦见门户忽开]` `[factor_trigger: dream_door_sudden_open]` `[role: 主干]` 门户忽开，主大吉。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_224]` `[trigger: 梦见门户大开]` `[factor_trigger: dream_door_wide_open]` `[role: 主干]` 门户大开，大吉利。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_225]` `[trigger: 梦见门更新]` `[factor_trigger: dream_door_renew]` `[role: 主干]` 门更新，主生贵子。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_226]` `[trigger: 梦见门自开]` `[factor_trigger: dream_door_self_open]` `[role: 主干]` 门自开，妻有私情。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_227]` `[trigger: 梦见门户裂开]` `[factor_trigger: dream_door_crack]` `[role: 主干]` 门户裂开，主大吉。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_228]` `[trigger: 梦见门户破坏]` `[factor_trigger: dream_door_damage]` `[role: 主干]` 门户破坏，有凶事。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_229]` `[trigger: 梦见城门大开]` `[factor_trigger: dream_city_gate_open]` `[role: 主干]` 城门大开，主口舌。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_230]` `[trigger: 梦见宫城塞者]` `[factor_trigger: dream_palace_blocked]` `[role: 主干]` 宫城塞者，口舌至。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_231]` `[trigger: 梦见门户闭塞]` `[factor_trigger: dream_door_closed]` `[role: 主干]` 门户闭塞，事不通。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_232]` `[trigger: 梦见门扇自折]` `[factor_trigger: dream_door_break]` `[role: 主干]` 门扇自折，奴仆走。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_233]` `[trigger: 梦见门户内无人]` `[factor_trigger: dream_empty_door]` `[role: 主干]` 门户内无人，大凶。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_234]` `[trigger: 梦见修移门户]` `[factor_trigger: dream_fix_door]` `[role: 主干]` 修移门户，大吉利。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_235]` `[trigger: 梦见石为门户]` `[factor_trigger: dream_stone_door]` `[role: 主干]` 石为门户，主寿命。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_236]` `[trigger: 梦见门前生草]` `[factor_trigger: dream_grass_door]` `[role: 主干]` 门前生草，作刺史。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_237]` `[trigger: 梦见门前坑沟]` `[factor_trigger: dream_pit_door]` `[role: 主干]` 门前坑沟，事不成。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_238]` `[trigger: 梦见天火烧门]` `[factor_trigger: dream_fire_door]` `[role: 主干]` 天火烧门，主凶事。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_239]` `[trigger: 梦见屋开小门]` `[factor_trigger: dream_small_door]` `[role: 主干]` 屋开小门，主私情。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_240]` `[trigger: 梦见穿井见水]` `[factor_trigger: dream_dig_well]` `[role: 主干]` 穿井见水，远信至。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_241]` `[trigger: 梦见井自损坏]` `[factor_trigger: dream_well_damage]` `[role: 主干]` 井自损坏，家大败。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_242]` `[trigger: 梦见井中沸溢]` `[factor_trigger: dream_well_overflow]` `[role: 主干]` 井中沸溢，主得财。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_243]` `[trigger: 梦见井枯涸者]` `[factor_trigger: dream_well_dry]` `[role: 主干]` 井枯涸者，家财散。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_244]` `[trigger: 梦见井中照身]` `[factor_trigger: dream_well_reflect]` `[role: 主干]` 井中照身，禄位至。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_245]` `[trigger: 梦见身坠井中]` `[factor_trigger: dream_fall_well]` `[role: 主干]` 身坠井中，疾病凶。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_246]` `[trigger: 梦见房在井中]` `[factor_trigger: dream_room_well]` `[role: 主干]` 房在井中，主见病。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_247]` `[trigger: 梦见取井水清]` `[factor_trigger: dream_clear_well]` `[role: 主干]` 取井水清吉，混凶。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_248]` `[trigger: 梦见井水负泥出]` `[factor_trigger: dream_mud_well]` `[role: 主干]` 井水负泥出，财主。 → 《周公解梦·门户井灶厨厕》
  - `[ns_zgjm_249]` `[trigger: 梦见井中欲干]` `[factor_trigger: dream_well_drying]` `[role: 主干]` 井中欲干，家欲破。 → 《周公解梦·门户井灶厨厕》"""
    normalized_text_zh: str = """"""
    subject: str = "门户井灶厨厕"
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
        l1_anchor="zgjm_v1.0.0_门户井灶厨厕_001_L1",
    )
    version: str = "1.0.0"
