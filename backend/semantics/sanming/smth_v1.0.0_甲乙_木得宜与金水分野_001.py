"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288673
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
    semantic_id="smth_v1.0.0_甲乙_木得宜与金水分野_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲乙木得宜与金水分野(SemanticEntry):
    """
    - **原文（source_text）**：
  甲木属阳，乃栋梁之材。喜生秋冬，遇申子月为吉。柱见庚辛，譬斧凿之论，主名利。运行申酉辰戌丑未乡，大能发越，见辛官尤妙。忌寅午戌合局及透丁火伤官，乃辛苦...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲木属阳，乃栋梁之材。喜生秋冬，遇申子月为吉。柱见庚辛，譬斧凿之论，主名利。运行申酉辰戌丑未乡，大能发越，见辛官尤妙。忌寅午戌合局及透丁火伤官，乃辛苦劳力、作事无成之命，运逢亦不顺。若合局丁透，有辰戌丑未，干上露戊己，再行财运，伤官生财，却发大福。乙木属阴，为生气之木，遇春生而花叶茂盛，亦喜生于小春之令。逢亥卯未、甲子辰二局，更行北运，虽透丙丁庚辛，亦不妨。所忌寅午戌火，巳酉丑多，多伤残，再行南运，主夭无疑。甲乙贵乎木得宜，要知金水旺为奇。春从南往秋归北，冬夏西行发福基。甲乙日生人，身坐巳酉丑申戌金乡，运行宜土金分野。若生寅卯辰不结木局，宜时引归土金分野，大贵，行运亦然，则官长远。若生巳酉丑申月，时引归亥卯未寅，取贵，非此时者，乃过与不及，却要运行水木局分野，否则贫儒。柱中原有财星，怕比劫分夺；原无财星，不畏。如木得金而成器，仁者有勇；金得木而成材，勇者必仁，是乃刚柔相济，阴阳相停。运行却喜财官，若有木无金，则庚辛亏而义寡；有金无火，即勇而无礼，则乱。金太盛而无水，则枯；木太多而无金，则繁，是金木各不一也。偏阴偏阳，难名之命，纵遇财官，亦不发达。六甲日用辛为正官，庚为偏官，戊己为财。如年月时中透出戊己辛字，生三秋、四季及金土局，财官有用。如不透此三字，只生三秋、四季及金土局，亦作财官论。见甲乙夺财，丙丁伤官，名利艰难。若生春夏及火木局，财官无气，虽得滋助，名利亦轻。喜行西方、四季金土分野，向官临财之运，不喜东南木火伤官败财之地。若四柱庚辛俱见，谓之官煞混杂，无去留制伏，反主贫贱。如只有庚，不见制伏，当作鬼论。分身鬼强弱，定其吉凶寿夭。若制伏得中，作偏官论；太过，反不为福。更看日干于所生月内，有力无力、有助无助，分节气浅深轻重言之，喜行身旺鬼衰之运，忌行身衰鬼旺之乡。六乙日用戊为正财，己为偏财，庚为正官，辛为偏官。若年月时上透出戊己庚字，生三秋、四季及金土局，财官有用。如不透此三字，生三秋、四季及金土局，亦作财官论。见甲乙夺财，丙伤官，名利艰难。若生春夏及火木局，纵有财官，无气，虽得滋助，亦轻。喜行西方、四季金土分野，向官临财，忌行火木之地，伤官败财。怕官煞混杂，有煞无制，鬼论；制太过不及，皆不为福。更详日干于所生月内，有无力助，分轻重言之，运喜忌同上。

- 分字分词释义：
  - **木得宜**：指甲乙木在时令、方位与格局中得其所宜，而非一味逢木为吉，重在阴阳、寒暖、干湿相称。
  - **金水旺为奇**：甲乙命局若得金来成器、水来滋润，且不过度，多主才德兼备，为上佳组合。
  - **土金分野 / 水木分野**：以行运方位分区：土金分野指西方与四季金土之地，水木分野指东方、北方木水之地。
  - **伤官生财**：伤官透出而有财星承接时，可由耗泄转为生财之机，不再纯属凶象。
  - **官煞混杂**：庚辛并见而无制衡时，官煞不分，主名利反覆、是非难清。

- 规范化释义（primary_lang_explained）：
  本段总论甲乙日主在不同坐支、月令与行运分野下的吉凶消长。甲木属阳，如栋梁之材，宜生于秋冬金水旺地，遇申子月最得其用，柱中见庚辛如斧凿成器，运行申酉辰戌丑未金土分野，多主发越，尤以辛官最妙；若反被寅午戌合局与丁火伤官所困，则多为辛劳而难有成就，唯有在火局中再得戊己财星透出，并行财运，使伤官转而生财，方能反凶为福。乙木属阴，为生气之木，宜春令与小春时节生长，得亥卯未、甲子辰等局配合北运，即便透出丙丁庚辛，也不大妨碍；最怕寅午戌火与巳酉丑金多而成克伐之象，再行南运则有夭折之忧。总之，甲乙之贵在于「木得其宜」，要明白金水旺时方为奇局：木得金则能成器，金得木则成材，刚柔相济、阴阳相停。论日主坐支，若甲乙日身坐巳酉丑申戌等金乡，运又行土金分野，多主根基稳厚；若生于寅卯辰而不成木局，则宜在时柱或行运中引归土金，以求大贵。反之，若生于巳酉丑申月，则需在时上或运中接引亥卯未寅等木水之地，以成贵格，否则易成清贫儒命。又详六甲六乙日的用神：六甲用辛庚为官、戊己为财，在金土局透出方为有用；六乙用戊己为财、庚辛为官，亦须金土得势。若反被甲乙比劫夺财、丙丁伤官，则名利艰难，尤其在春夏火木局中，财官多无气。故行运宜向西方、四季金土「向官临财」之地，忌再向东南木火伤官败财之乡；又须防庚辛官煞混杂而无制，陷于「有官无品」或贫贱反覆之局。


- **完整对等诠释（secondary_lang_full）**：
  This section states that Jia and Yi are not simply "wood that likes to be strong", but timber that must be properly placed and tempered. Jia, the yang stem, is compared to great beams and pillars. It flourishes when born in the cold, dry clarity of autumn and winter, especially in Shen and Zi months where metal and water are strong. There, Geng and Xin on the stems act like axes and chisels that carve rough timber into usable beams, and travel through the western and central earth–metal regions tends to bring rank and advancement. If instead Jia is trapped in fire combinations such as Yin–Wu–Xu with Ding as Hurting Officer, the life is marked by hard work and poor results unless additional Wu–Ji wealth emerges and fortune moves through wealth regions so that Hurting Officer can be turned into a producer of wealth.
  Yi, the yin stem, is a gentler, living wood: buds, branches and vines. It prefers spring and the light warmth of "small spring" when the year first turns; when matched with Hai–Mao–Wei or Jia–Zi–Chen structures and northerly water fortunes, even the appearance of Bing, Ding, Geng and Xin does not necessarily spoil things. What Yi truly fears is an excess of fire (Yin–Wu–Xu) and harsh metal (Si–You–Chou) that cut and scorch without measure; if such combinations are followed again by southern fire fortunes, early harm or exhaustion are likely. For both Jia and Yi, the true nobility lies in "wood appropriately placed": wood should receive just enough metal to become tools and just enough water to be nourished, then be rooted in earth–metal regions. Charts where Jia–Yi day stems sit on metal branches and walk west and four–season earth fortunes tend to have solid foundations and usable wealth and office. Those born on Yin–Mao–Chen without a full wood bureau should look for times or fortunes that lead them back to earth–metal; those born in Si–You–Chou–Shen months need later support from Hai–Mao–Wei–Yin to complete a noble pattern. Throughout, the text emphasises that for the six Jia and six Yi days, usable Geng–Xin and Wu–Ji in metal–earth configurations are the real sources of wealth and office, while excessive peers and Hurting Officers easily hollow out fame and fortune.

- 核心要点：
  - 甲乙木之贵，在于「木得其宜」而非徒求木旺：需配合适度金水成器、润养，并以土金分野为根基，忌火木过盛而失衡。
  - 行运观法重在「分野」：甲乙日身坐金乡，宜行土金之运以固其官财；木局不成者须借运引归金土，火木过盛者则需水金调剂。
  - 六甲、六乙用官财，皆以金土局透出戊己庚辛为佳；比劫夺财、伤官太盛时，纵见官财亦多虚名，需有制伏得中方可成用。

- 应用推演（操作顺序）：
  1) 判盘时先评估甲乙日主之「木得宜」程度：结合节令（秋冬或春令）、局中寒暖与金水多少，判断是「成器之木」还是「孤木失所」。
  2) 其次查看日主所坐之支：若坐巳酉丑申戌等金乡，可标记为「有根于金」，后续行运宜优先考察土金分野的巩固或破坏；若坐寅卯辰而不成木局，则需在大运流年中寻找引归土金或木局成格的关键节点。
  3) 再分析四柱中庚辛、戊己透出情况，以六甲、六乙用神为基准，将「官煞混杂」「伤官生财」「比劫夺财」等结构编码为不同风险/潜能标签。
  4) 在行运模拟中，将西方与四季金土运标记为「官财得地」候选区，将东南木火运标记为「伤官败财」高风险区，并结合日主强弱与格局取用，给出增强或削弱的调节建议。

- 反例与边界：
  - 不宜机械地认为「甲乙属木，必喜春木旺」，忽视原文中甲喜秋冬金水、乙亦喜小春金气裁成等情形。
  - 不可一见「金水旺」便断大吉，而不问日主是否承受得起、是否因此反成「偏阴偏阳」、官煞混杂或水寒木漂。
  - 工程实现中若只以「木多为吉」「见金必凶」作二元标签，会与原文「木得宜」「金来成器」的精细区分相违，导致大量误判样本。
  - 反向误区是过分迷信「伤官生财」，在现实判断中忽略伤官本身对秩序与结构的破坏性，只看到短期财利而不看长期代价。

- 小例（示意）：
  - 某甲日生于申月，日坐酉金，柱中辛透、戊己亦现，行运再入西方金土分野，系统可将其识别为「金水旺而木得宜」的格局：一方面具备成器之才，另一方面官财有根，适合在制度化强、规则清晰的领域中发展；但仍需监控庚辛是否过多而成官煞混杂。
  - 另一命局乙日生于春夏火木旺地，柱中比劫重重而无金，行运又频入东南木火分野，系统则标记为「木盛而不宜」：虽有理想与生发之力，但易陷入竞争过度、财星难聚的状态，需要在现实中主动引入「金水因子」（如规则、约束、冷静评估）以平衡格局。"""
    normalized_text_zh: str = """"""
    subject: str = "甲乙：木得宜与金水分野"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'wood_appropriateness_state', 'bazi_semantic', 'metal_water_tool_nurture', 'bazi_semantic', 'harm_official_wealth_transform', 'bazi_semantic', 'official_killing_mixed_risk', 'bazi_semantic', 'parallel_rob_wealth_loss', 'bazi_semantic', 'earth_metal_territory_luck', 'bazi_semantic', 'water_wood_territory_luck', 'bazi_semantic', 'source_ref', 'rel_smth_04_001', 'wood_appropriateness_state', 'rel_smth_04_002', 'harm_official_wealth_transform', 'rel_smth_04_003', 'official_killing_mixed_risk', 'evi_smth_04_001', 'wood_appropriateness_state', 'rule_wood_appropriate', 'evi_smth_04_002', 'metal_water_tool_nurture', 'rule_wood_metal_tool', 'evi_smth_04_003', 'official_killing_mixed_risk', 'rule_official_killing_mixed', 'map_smth_04_001', 'map_smth_04_002']
    
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
        l1_anchor="smth_v1.0.0_甲乙_木得宜与金水分野_001_L1",
    )
    version: str = "1.0.0"
