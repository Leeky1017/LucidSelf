"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288754
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
    semantic_id="smth_v1.0.0_壬癸_水干与火土调剂_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬癸水干与火土调剂(SemanticEntry):
    """
    - **原文（source_text）**：
  壬水属阳，乃甘泽长流之水，能滋生草木，长养万物，独喜春夏生人，秋冬值令，则无生意。若见寅午戌官星，得生助之气，名誉自彰。金局生八月，名利两遂；水局生三...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬水属阳，乃甘泽长流之水，能滋生草木，长养万物，独喜春夏生人，秋冬值令，则无生意。若见寅午戌官星，得生助之气，名誉自彰。金局生八月，名利两遂；水局生三月，为天德主贵。地支亥卯未，行南方运，发财。癸水属阴，乃大海无涯之水，不能生长万物，一云雨露润泽之水，滋助万物。喜春秋间，运行巳午戌地，发福非常，大忌辰戌丑未运，成败。地支亥卯未合，伤旺益财，无寅甲，亦发名利，如见己土丑未月，更带三刑，平常衣禄，初中未济，终末荣发。若五行有救，身旺，运喜财官，亦主贵显。壬癸日生，水为主，根基惟在火与土：春秋来往，发财官；冬夏东行，为得所。壬癸日生，坐下辰戌丑未巳午，为玄武当权，运行宜火木分野，过与不及，偏阴偏阳，则贵而不实。若生四季巳午月，引亥子时；或冬生，引辰戌丑未巳午时，俱贵，非此时，则虚名虚利。运喜金水分野，生助为荣，无金则水绝，忌比肩劫财。冬十一月三合结局，水涨横泛而土崩，故水无土则滥，土无水则干：土得水而受润通气，水得土而成堤为河，二者不可偏倚。若更气运得宜，无不贵显，其刑合、拱合等格，不在此论。六壬日，除壬辰为魁罡，财官喜忌，论于日下。壬寅、壬子、壬申、壬午、壬戌五日，用丙丁为财，巳为正官，戊为偏官。四柱透丙丁巳字，生九夏四季火土局中，财官有用；如不透此三字，生九夏火土局，亦作财官论。见壬癸夺财，乙为伤官，名利艰难。若生春冬及水木局中，财官无气，虽得滋助，亦轻。喜行南方四季火土分野、向官临财之运。柱见戊己，煞官混杂，无制反贱；如无己有戊，不见制伏，作鬼论。要分身鬼强弱，定其吉凶：制伏得中，作偏官论，制过，不福。更详日干于所生月内，有无力助，分节气浅深轻重言之，喜行身旺鬼衰之运，忌行身衰鬼旺之运。六癸日用丙丁为财，戊为正官，己为偏官。若四柱透丙丁戊字，生九夏四季火土局，财官有用；若无此三字，生九夏四季火土局中，亦作财官论。见壬癸夺财，甲为伤官，不利。若生春冬水木局中，财官无气。喜行南方四季财官之运，怕官煞混杂，有煞无制，鬼论；制太过，凶。更详日干于月令内，有无力助，轻重言之，运喜忌同上。

- 分字分词释义：
  - **水为主，根基在火土**：壬癸日主虽以水为体，但真正的根基在于是否有火土为之调剂与承载。
  - **水无土则滥**：水多而无土堵，则横溢成灾；土得水而润通，水得土而成堰。
  - **玄武当权**：壬癸日坐辰戌丑未巳午，如玄武当权，水有承载而不溢。

- 规范化释义（primary_lang_explained）：
  本段总论壬癸水日主在火土调剂下的成败关键。壬水如长流甜泽，能滋生草木、长养万物，独喜春夏生人，秋冬值令则无生意。若见寅午戌官星得生助，名誉自彰。癸水如大海或雨露，喞春秋间、行巳午戌地发福，大忌辰戌丑未运成败。壬癸日生，水为主但根基惟在火与土：春秋来往发财官，冬夏东行为得所。若坐辰戌丑未巳午为玄武当权，运行宜火木分野。冬十一月三合结局水涨横泛而土崩，故水无土则滥，土无水则干：土得水而受润通气，水得土而成堰为河，二者不可偏倚。六壬六癸用神，皆以丙丁为财、巳戊为官，宜九夏四季火土局透出方可为用。


- **完整对等诠释（secondary_lang_full）**：
  Ren and Gui are both water, but they are pictured differently. Ren is a broad, sweet current that irrigates fields and nourishes plants; it likes to be born in spring and summer when there is warmth and wood to receive and transform it. In such charts, especially if the branches contain Yin, Wu and Xu as officials that gain qi, reputation tends to arise naturally. Gui is either the boundless ocean or fine rain and dew. In practice, the text focuses on its role as gentle moisture: it prefers the temperate times of spring and autumn and the fire–earth territories of Si, Wu and Xu, where warmth and form give its fluid nature channels and containers. What both fear is an overdose of the graveyard earths Chen, Xu, Chou and Wei without sufficient fire, which turns fertile mud into mire and drags success into repeated reversals.
  Although Ren and Gui take water as their body, the passage insists that their foundation "lies only in fire and earth". Water without earth becomes a flood, and earth without water becomes dry and dead: the image is emotional and material life that either spills everywhere with no boundaries or is so stiff that nothing can grow. Charts where Ren or Gui day stems sit on Chen, Xu, Chou, Wei, Si or Wu are called "Xuanwu in authority": water has both source and embankment, and later fortunes through fire and wood regions can then bring real wealth and office. Summer and four‑season fire–earth fortunes that reveal Bing, Ding and Wu–Ji with qi are especially helpful; pure water–wood or pure metal–water fortunes without fire and earth are treated as high‑volatility periods, rich in movement but risky for stability. In evaluating Ren and Gui, one therefore looks not just at how strong water is, but at whether metal provides a source, fire gives warmth and purpose, and earth builds banks. Where these three relationships are balanced, the person can use flow and adaptability to carry real responsibility; where they are badly imbalanced, the same water nature shows up as scattered effort, emotional flooding or structures that collapse when pressure rises.

- 核心要点：
  - 壬癸水日根基不在单纯水旺，而在火土的调剂与承载：水火土须配合得宜，方能化生机与权柄，而非仅成泛滥之水。
  - 格局判断上，需同时看「金生水」「火制水」「土为堤」三重关系：缺金则源绝，缺火则无温，缺土则无堤，三者任何一端严重失衡都难成真正贵格。
  - 行运以南方四季火土分野为主要发用区域，金水运为生助之地，需配合原局强弱与比劫多少，谨防比肩劫财过重或官煞混杂。

- 应用推演（操作顺序）：
  1) 判盘时，先评估壬癸水之旺衰，并记录火土配置：将「水强/水弱」「火足/火乏」「土厚/土薄」作为基础特征。
  2) 检查是否形成「水有堤岸」结构：有戌辰丑未等土支承托，且火土不过分受制者，标记为「水土相济」；一见水无土或土无水，则标记为高风险结构。
  3) 结合六壬六癸用神，判断丙丁戊己是否在火土局中得气，编码「财官有用/无用」「伤官夺财」「官煞混杂」等指标，作为后续预测权重的基础。
  4) 在行运模拟中，将南方四季火土运视为壬癸日的主要成就期，将纯水木或纯金水运视为高波动时期：一方面有扩张与流动的机会，另一方面需提高对情绪泛滥、资源流失与结构坍塌的预警。

- 反例与边界：
  - 不宜一见壬癸属水，便断「水越旺越好」，忽略原文中「水无土则滥」的明确提醒。
  - 不可简单把金水多视为财源滚滚，而不看火土是否足以承载，容易导致对高流量、高波动行业的过度乐观。
  - 工程实现中若只将壬癸映射为「情绪/流动」单一标签，会忽视其在资源输送、缓冲与跨边界连接上的复杂作用。
  - 反向误区是过分压制壬癸水，一味追求土之稳定与火之效率，结果使系统失去必要的弹性与适应性。

- 小例（示意）：
  - 某壬日生于午月，日坐戌土，柱中丙丁透而金水有源，行运再入南方火土分野，系统可将其识别为「水土相济、财官皆有」的格局：适合在既有流动性又需承担责任的大型项目或组织中发挥作用。
  - 另一命局癸日生于冬月，水木极旺而土火全乏，行运又频入北方寒水之乡，系统则标记为「水无堤岸、虚名虚利」：虽有跨界与扩张之势，但现实中易出现情绪失衡与资源难以沉淀的问题，需要借后天环境与选择刻意补足火土因子。"""
    normalized_text_zh: str = """"""
    subject: str = "壬癸：水干与火土调剂"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'water_earth_harmony_state', 'bazi_semantic', 'fire_earth_regulate_support', 'bazi_semantic', 'xuanwu_authority', 'bazi_semantic', 'water_no_earth_flood_risk', 'bazi_semantic', 'water_rises_earth_collapse', 'bazi_semantic', 'south_season_fire_earth_luck', 'bazi_semantic', 'official_killing_mixed_risk', 'bazi_semantic', 'source_ref', 'rel_smth_04_013', 'water_earth_harmony_state', 'rel_smth_04_014', 'water_no_earth_flood_risk', 'rel_smth_04_015', 'xuanwu_authority', 'evi_smth_04_013', 'fire_earth_regulate_support', 'rule_water_fire_earth_root', 'evi_smth_04_014', 'water_no_earth_flood_risk', 'rule_water_earth_balance', 'evi_smth_04_015', 'xuanwu_authority', 'rule_xuanwu_luck', 'map_smth_04_009', 'map_smth_04_010']
    
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
        l1_anchor="smth_v1.0.0_壬癸_水干与火土调剂_001_L1",
    )
    version: str = "1.0.0"
