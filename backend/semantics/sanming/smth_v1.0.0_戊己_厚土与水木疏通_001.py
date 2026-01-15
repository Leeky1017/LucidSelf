"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288730
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
    semantic_id="smth_v1.0.0_戊己_厚土与水木疏通_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊己厚土与水木疏通(SemanticEntry):
    """
    - **原文（source_text）**：
  戊土属阳，乃堤岸城墙之土，止能拒水，不能种养万物。凡城堤不有刑冲破害，人民得安，喜甲乙木，以煞化印之地。忌行西方运，纵发而当破当忧，要火生扶，嫌水克制...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊土属阳，乃堤岸城墙之土，止能拒水，不能种养万物。凡城堤不有刑冲破害，人民得安，喜甲乙木，以煞化印之地。忌行西方运，纵发而当破当忧，要火生扶，嫌水克制。戊己重犯，名利两失；辛庚叠逢，作事进退。己土属阴，为田地山园之土，可以种养万物，要刑冲破害，即耕凿之论。喜生春夏辰巳之乡，乃官印之地，更不值伤官损印，发福主为人好置造田，丰盈。行东北方运尤妙，更兼亥卯未木，决主富贵，人物稳厚，大宽小急。值辰戌丑未，乃背禄逐马及劫财刑伤，破耗讼服不一。戊己日干寻水木，柱中原有，还为福；运临北野及东方，德润身兮富润屋。戊己日生，坐下亥卯寅位，为勾陈得位，运行宜水木分野。生亥子月，要引辰戌丑未巳午时；若生辰戌丑未巳午月，要引亥子时为贵。盖土得木而疏通，木赖土而培养：若木重而土少，则崩；土重而无木，乃顽浊无用之土。巳日丑年月，西方不吉，南方大显。六戊日，除戊戌为魁罡，其财官喜忌，论子日下；其余戊子、戊午、戊申、戊寅、戊辰五日，用壬癸为财，乙为正官，甲为偏官。若年月时中透壬癸乙字，生春冬水木局中，财官有用；不透此三字，生春冬及水木局中，亦作财官论。见戊己夺财，辛为伤官，名利艰难。若生三秋四季及金土局，财官无气，虽得滋助，亦轻。喜行东北方水木分野、向官临财之运，忌行四季西方败财伤官之地。若柱透甲乙，官煞混杂，无制反贱；如无乙有甲，无制，当作鬼论。要分身鬼强弱，定其吉凶寿夭：制伏中和，作偏官用；太过，反不为福。更详日干于所生月内，有力无力、有救无救，分节气浅深轻重言之，喜身旺鬼衰运，忌身衰鬼旺运。六己日用壬癸为财，甲为正官，乙为偏官。若年月时透壬癸甲字，生春冬水木局，财官有气；如不透此三字，生春冬水木局，亦作财官论。见戊己夺财，庚为伤官，名利艰难。若生三秋四季及金土局中，纵有财官，无气，虽得滋助，亦轻。喜行东北水木分野，忌伤官败财之运。怕官煞混杂，有煞无制，鬼论；制太过则贫。更详日干于所生月令内，有无力助，分轻重言之，运喜忌同上。

- 分字分词释义：
  - **堤岸城墙之土**：比喻戊土厚重坚固，主防守与承载，而非直接生养万物。
  - **煞化印**：以七煞之力化为印绶，转凶为用，常借甲乙木来引导戊土的克制关系。
  - **勾陈得位**：戊己日坐亥卯寅等位，如勾陈镇守，象征土有根基、能统摄局中气机。
  - **背禄逐马**：舍弃原有禄位而追逐驿马，多主奔波折腾、破耗不定。
  - **土得木而疏通**：木来疏土，使厚重之土不至板结；反过来木赖土以培植其根基。

- 规范化释义（primary_lang_explained）：
  戊土象堤岸城墙之土，偏重防守与承载，能挡水却不宜直接种植，宜有甲乙木来疏通、化煞为印，方能由刚转柔，既守又能用；若多行西方金地，虽一时可发，却终有堤防被冲、成败难保之忧，需要火来温养而忌水过度侵蚀。己土为田园之土，可培植万物，喜春夏辰巳之乡为官印之地，不宜伤官损印；行东北水木运，又有亥卯未木相助，则多主田产丰厚、性情稳厚宽裕。若值辰戌丑未等库土重重，则易出现背禄逐马、劫财刑伤等情形，破耗讼事接连。戊己日主整体上「寻水木而为福」：若原局中已有水木，行运再临北方与东方，多主「德润身、富润屋」，身心俱得滋养。日主坐亥卯寅者，如勾陈得位，土有根基而可统摄局中气机，宜行水木分野；生于亥子之月者，当以辰戌丑未巳午之时为贵，使土水火木互相贯通；生于辰戌丑未巳午月者，则宜以亥子时为引，形成「土赖水木以通达」之局。六戊、六己日的官财用法，则皆以壬癸为财、甲乙为官：在春冬水木局中若能透出壬癸甲乙，则财官有气可用；若反被戊己比劫夺财、辛庚伤官过重，则名利艰难。行运宜东北水木分野向官临财，忌四季西方之败财伤官地，亦须防官煞混杂而无制，化贵为贱。


- **完整对等诠释（secondary_lang_full）**：
  Wu and Ji represent two faces of earth. Wu, the yang earth, is likened to dykes and city walls: it is meant to block and contain, not to sprout life on its own. Such earth must be firm yet not dead; the text therefore praises charts where Jia and Yi wood appear to channel and carve Wu, turning harsh Killing into protective Seal. If Wu repeatedly meets western metal fortunes, the walls may at first bring advantage, but over time there is a danger that floodwaters break the banks and success proves hard to keep. Ji, the yin earth, is field and garden soil. It should be turned, ploughed and even "injured" by tilling so that it can produce; appropriate punishment and clash here symbolise cultivation rather than destruction. Ji prefers the spring–summer Chen and Si regions where it holds official and seal qi and is not injured by Hurting Officers.
  Taken together, Wu and Ji days are said to "seek water and wood for blessing". When the natal chart already contains both water and wood and later fortunes revisit the northern and eastern water–wood territories, the result is described as "virtue moistening the body and wealth moistening the house": character and resources are both enriched. When Wu or Ji day sits on Hai, Mao or Yin, the configuration is compared to the guardian Gouchen in its proper seat, an image of earth with true roots and command; such charts do best when they then walk water–wood fortunes. Those born in Hai–Zi months are helped by later Chen–Xu–Chou–Wei–Si–Wu times that weave earth, water, fire and wood into a connected cycle, while those born in heavy earth months need Hai–Zi hours to open channels. For both stems, charts where Ren and Gui wealth and Jia and Yi official emerge with qi in water–wood contexts are treated as capable of real achievement; charts where Wu and Ji peers abound, Xin and Geng Hurting Officers are heavy and water–wood are missing are labelled as thick but stagnant earth: there may be effort and responsibility, but little true growth.

- 核心要点：
  - 戊己土之用，不在「愈厚愈好」，而在「厚中有通」：须借甲乙木以疏土、壬癸水以润土，否则非崩即顽浊无用。
  - 戊己日主在春冬水木局中透出壬癸甲乙，财官方有气可用；若局在金土而官财无气，则纵见财官名目亦多虚名。
  - 行运上，戊己宜向东北水木分野以取德润与开财，忌久居西方败财伤官之地，以免背禄逐马、反复破耗。

- 应用推演（操作顺序）：
  1) 判盘时先区分戊土与己土：前者偏重防守承载，后者偏重培植生养，再结合年月日时判断其所处环境是「城堤」还是「田园」。
  2) 检查局中木与水的配置：若有甲乙木疏土、壬癸水润土，则标记为「厚土而通」；若木重土少则恐崩塌，土重无木则为顽浊之土，两者分别标记为不同风险标签。
  3) 结合六戊六己的官财用神，判断局中壬癸（财）与甲乙（官）是否透出且在水木局有气，将「财官有用/无用」「官煞混/不混」等信息编码进模型。
  4) 行运推演时，将东北水木分野标记为戊己日的「德润身、富润屋」优选方位，将四季西方金土分野标记为「败财伤官」高风险区域，并根据原局厚薄与通达程度调整风险权重。
- 反例与边界：
  - 不宜一见戊土厚重就断为「根基稳固、必主安稳」，忽视水木过少而致板结顽浊，或木重土薄而致崩塌的结构风险。
  - 不可将一切刑冲视为坏事：对己土田园之土而言，适度刑冲正是耕凿之象，有利于开垦与翻新，但过度则成破坏。
  - 工程实现中若只用「土旺=稳」「水多=坏」等粗糙标签，会遮蔽「土得水木而通」这一关键中介结构，使模型对基础与资源类问题的解释力不足。
  - 反向误区是过分畏惧官煞混杂，一见壬癸甲乙并见便全盘否定，而不看是否已有合适的制伏与中和条件，可转煞为用。
 
- 小例（示意）：
  - 某戊日命局土厚而有甲乙透出，壬癸在水木局中得气，行运又向东北水木分野，系统可将其识别为「厚土有通、官财俱用」的格局：适合承担基础设施、土地金融等需要稳定承载与审慎扩张的领域。
  - 另一命局己日生于三秋，辰戌丑未重重而木水全无，又行西方金土之运，系统则标记为「顽浊厚土、背禄逐马」：虽有一时之财，却易反复破耗与诉讼纠纷，需在现实中主动引入学习、合作与制度约束来打通与软化。"""
    normalized_text_zh: str = """"""
    subject: str = "戊己：厚土与水木疏通"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'earth_wood_loosening_state', 'bazi_semantic', 'water_wood_moisten_loosen', 'bazi_semantic', 'gouchen_position', 'bazi_semantic', 'killing_transforms_seal', 'bazi_semantic', 'abandon_salary_chase_risk', 'bazi_semantic', 'northeast_water_wood_luck', 'bazi_semantic', 'heavy_earth_little_wood_collapse', 'bazi_semantic', 'source_ref', 'rel_smth_04_007', 'earth_wood_loosening_state', 'rel_smth_04_008', 'killing_transforms_seal', 'rel_smth_04_009', 'abandon_salary_chase_risk', 'evi_smth_04_007', 'earth_wood_loosening_state', 'rule_earth_wood_loosen', 'evi_smth_04_008', 'water_wood_moisten_loosen', 'rule_wuji_seek_water_wood', 'evi_smth_04_009', 'abandon_salary_chase_risk', 'rule_abandon_salary_risk', 'map_smth_04_005', 'map_smth_04_006']
    
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
        l1_anchor="smth_v1.0.0_戊己_厚土与水木疏通_001_L1",
    )
    version: str = "1.0.0"
