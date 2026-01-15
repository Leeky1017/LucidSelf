"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288743
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
    semantic_id="smth_v1.0.0_庚辛_金干与火木成器_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚辛金干与火木成器(SemanticEntry):
    """
    - **原文（source_text）**：
  庚金属阳，乃金银铜铁之类，禀太阳而成，要见丁火制之，方能成器。如见丙火，遇而不遇。喜行东南火木之运，明亮，金得制。如值寅卯临于甲乙，及己午未官星印元得...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚金属阳，乃金银铜铁之类，禀太阳而成，要见丁火制之，方能成器。如见丙火，遇而不遇。喜行东南火木之运，明亮，金得制。如值寅卯临于甲乙，及己午未官星印元得气之乡，皆是发越；惟居西北方，为金沉水底，是不能成器。辛金属阴，乃水银朱砂赤碧珍珠之类，秉日精月华秀气结成，最要金清水秀、土气丰厚地方，并西北方运。如行辰戌巳东南运，五行四柱不见丁火为妙，见则不能成其器，如珠坠炉之喻，秀而不实。尤恐寅午戌成局煞旺，要身强乃当其旺；柱有亥卯未，更见丙丁透，行午未运，发福。巳酉丑成金局，为温厚造化，行东方运，大吉，不宜南。庚辛日主号金干，木火相生，福自专：年月时中如会合，东西运步，定居官。庚辛日生，坐下寅午戌巳火，又生寅午戌月，要引金土时，贵。秋三月及季冬或十一月，引木火旺时，大贵。运行木火分野，忌过与不及，偏阳偏阴，则苗而不秀。若通火月气，非巳酉丑申时不贵。运金土则吉，比肩三合成金局，金盛火微，喜行木火之运。故金非火不能成其器，火无金无以显其用，金火相停，方为乘轩衣冕。若火太炎而无土，则金必败；有土则为铸印之象，陶熔革化而成器，大人之命也。火多金少，金盛火微，皆凶暴之辈。六庚日，除庚戌、庚辰为魁罡，其财官喜忌，论于日下。庚申、庚寅、庚午、庚子四日，用甲乙为财，丁为正官，丙为偏官。若年月时透甲乙丁字，生春夏火木局中，财官有用；如不透此三字，生春夏火木局，亦作财官论。见庚辛夺财，壬癸为伤官，名利艰难。如生秋冬金水中，财官无气，虽得滋助，亦轻。喜行东南木火分野、向官临财之运，不喜行西北金水分野、伤官败财之运。若柱有丙丁，官煞混杂，煞无制反贱；如无丁有丙，无制，当作鬼论。要分身鬼强弱，定其吉凶寿夭：制伏得中，作偏官论；制过，反不为福。更详日干于所生月内，有力无力、有助无助，分节气浅深轻重言之，喜行身旺鬼衰之运，忌身衰鬼旺之运。六辛日用甲乙为财，丙为正官，丁为偏官。柱中年月时透甲乙丙字，生春夏及火木局中，财官有用；如不透此三字，生春夏及火木局，亦作财官论。见庚辛为夺财，壬为伤官，名利艰难。若生秋冬及金水局，财官无气，虽得滋助，亦轻。运喜东南火木分野、向官临财，不喜西北金水分野、伤官败财之运。怕官煞混杂，有煞无制，鬼论；制太过，不福。更详日干于所生月内有无力助，分轻重言之，运喜忌同上。

- 分字分词释义：
  - **金干**：指庚辛两金为日主时的总称，偏重刚毅、决断与执行力。
  - **金非火不能成其器**：金要经火炼制方能成器，比喻庚辛命需历经火局锤炼、制度与环境的考验，才显其用。
  - **金沉水底**：庚辛居西北金水之地而无火，喻才能被埋没、难成器用。
  - **金清水秀**：辛金喜环境清澈、土气丰厚而水润，比喻格局清纯、不杂浊煞。
  - **官煞混杂**：丙丁并见而无制时，官煞杂乱，主是非反覆、恩威失衡。

- 规范化释义（primary_lang_explained）：
  本段总论庚辛金日主在不同环境与行运分野中的成败关键。庚金如金银铜铁，重在锻炼成器，最喜丁火来制，既能去其臃重，又能显其锋芒；若只见丙火，则有光而少制，容易虚张而不实。庚金喜行东南火木之运，在寅卯木旺、己午未官印得地之乡,多主发越；若久居西北金水之方，则如金沉水底，虽性刚而难成大器。辛金则偏于精微，如水银、珠玉一类，重在「金清水秀、土气丰厚」：既要根基稳定，又要环境清透，不宜火气粗暴。行辰戌巳东南之运而不见丁火，为最得其宜；若被丁火逼烈，则如珠坠炉，秀而不实，反伤本质。庚辛日主合称「金干」，以木火为福缘：年月时中若能形成木火生助之局，再行东南木火分野，往往易居官位、掌权柄；但木火过与不及，或官煞混杂，又失其中和。六庚、六辛在用神上，皆以甲乙为财、丙丁为官，宜春夏火木旺地；若落秋冬金水、财官无气，纵见名目亦多虚轻。原文反复强调：金与火须相停，既忌金沉水底，也忌火炎而无土，唯有土火得中、木火适度，方成「乘轩衣冕」之贵。


- **完整对等诠释（secondary_lang_full）**：
  For Geng and Xin, the classics focus on how raw metal is turned into something that can really be used. Geng, the yang metal, is coarse ore and heavy tools: gold, silver, copper and iron that still need the furnace. It is said that "metal cannot become a tool without fire"; specifically, Ding fire is praised as the proper refining force that both removes dross and reveals edge. Bing fire, by contrast, is often "met but not truly met": it provides light and reputation but not enough disciplined heat to finish the work, so achievement risks being flashy yet hollow. Geng likes to move through the south‑eastern wood–fire regions, especially where Yin and Mao are strong and Ji‑Wu‑Wei give official and seal support; if it stays too long in the north‑west metal–water areas without fire, it is as if metal has sunk to the bottom of water, hard and bright in itself but buried and unshaped.
  Xin, the yin metal, is compared to mercury, pearls and fine gemstones. It favours conditions that are "metal clear and water beautiful, with earth qi abundant": stable foundations, clean surroundings and gentle moisture, rather than crude, scorching fire. When Xin walks Chen, Xu and Si in the east–south without being lashed by Ding fire, its refinement and grace can shine; if Ding is too fierce, it becomes "a pearl fallen into the furnace", refined to the point of damage. Taken together as "metal stems", Geng and Xin treat wood as wealth and fire as office. Charts where Jia and Yi are present to provide resources, where Bing and Ding appear in the right measure and where earth carries the whole structure are the ones that truly produce "carriage and robe" status. Autumn–winter metal–water charts without sufficient fire or earth leave wealth and office names without qi; charts where both Bing and Ding appear chaotically without control are classified as mixed Official and Killing, leading to disputes and unstable authority. In practice, the key questions are whether metal has enough but not too much fire to be forged, whether earth exists to hold the heat and results, and whether later fortunes through south‑eastern wood–fire regions arrive when the person is ready to shoulder responsibility.

- 核心要点：
  - 庚辛金日成败，重在「金火相济」：须得适度火来炼制成器，又忌火炎太过或全无火气导致沉埋。
  - 用神结构上，庚辛以木为财、火为官，宜在春夏及木火局透出甲乙丙丁，并得土以承之；落秋冬金水则多财官无气。
  - 行运以东南木火分野为主，西北金水分野多为伤官败财之地：须视原局强弱与官煞是否混杂，再决定可承受的火木强度。

- 应用推演（操作顺序）：
  1) 判盘时，先评估庚辛日主之强弱：配合季节、根气与同类金的数量，标记为「金强/金弱」。
  2) 检查局中木火配置：有甲乙生财、丙丁为官且不过度者，标记为「金火成器」；若火过炎又缺土或官煞混杂，则标记为高风险结构。
  3) 结合六庚六辛用神，判断财官是否在春夏木火局中得气，或落秋冬金水而无力，将「财官有气/无气」与「伤官夺财」等要素编码。
  4) 行运模拟时，将东南木火运视为主要发用期，但根据原局金强弱控制其上限；西北金水运则多视为「伤官败财或沉埋期」，需特别监控官煞混杂与才华被埋没两类风险。

- 反例与边界：
  - 不宜一见庚辛属金，便断「必喜金水」，忽略原文中多次强调「金非火不能成其器」「金沉水底不能成器」的条件。
  - 不可简单以「见官即吉」来处理丙丁火，丙丁并见且无制时，反成官煞混杂，易致是非与权力失衡。
  - 工程实现中若只用「金旺=刚强」「火旺=贵显」等粗标签，会忽视金火之间的制化关系与土之承载，导致对庚辛命局的判断失准。
  - 反向误区是过分畏惧火局，一见火多便全盘否定，而不看是否有土承、有木生，可从「火炼金成器」中提炼出真正的成就路径。

- 小例（示意）：
  - 某庚日生于寅月，日坐午火，柱中甲乙透而丁火有制，行运东南木火又兼土，可在系统中标记为「金火相济、财官有气」的成器格局，适合在制度严谨、需承担决策责任的岗位上发展。
  - 另一命局辛日生于秋冬，金水极旺而少火，行运再入西北金水之乡，系统则标记为「金沉水底、财官无气」：虽有才华与敏锐，但在现实中易沦为幕后或边缘角色，需要主动寻求火土场域来锻炼与承载。"""
    normalized_text_zh: str = """"""
    subject: str = "庚辛：金干与火木成器"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'metal_fire_tool_state', 'bazi_semantic', 'fire_refines_metal_tool', 'bazi_semantic', 'metal_sinks_water_risk', 'bazi_semantic', 'metal_clear_water_beautiful', 'bazi_semantic', 'pearl_furnace_damage', 'bazi_semantic', 'southeast_wood_fire_luck', 'bazi_semantic', 'official_killing_mixed_risk', 'bazi_semantic', 'source_ref', 'rel_smth_04_010', 'metal_fire_tool_state', 'rel_smth_04_011', 'metal_sinks_water_risk', 'rel_smth_04_012', 'pearl_furnace_damage', 'evi_smth_04_010', 'fire_refines_metal_tool', 'rule_fire_refines_metal', 'evi_smth_04_011', 'metal_sinks_water_risk', 'rule_metal_sinks_water', 'evi_smth_04_012', 'metal_fire_tool_state', 'rule_metal_fire_balance', 'map_smth_04_007', 'map_smth_04_008']
    
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
        l1_anchor="smth_v1.0.0_庚辛_金干与火木成器_001_L1",
    )
    version: str = "1.0.0"
