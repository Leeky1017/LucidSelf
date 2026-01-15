"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559510
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
    semantic_id="yhzp_v1.0.0_挈要捷驰玄妙诀_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 挈要捷驰玄妙诀(SemanticEntry):
    """
    - **原文（source_text）**：  
  挈要捷驰玄妙诀。  
  以日为主，专论财官。  
  盖，官乃为扶身之本，财为养命之源。  
  故推天时，察地利，约太过而不及，以中和而为用；...
    """
    
    original_text: str = """- **原文（source_text）**：  
  挈要捷驰玄妙诀。  
  以日为主，专论财官。  
  盖，官乃为扶身之本，财为养命之源。  
  故推天时，察地利，约太过而不及，以中和而为用；去留舒配而中理，轻重强弱而表正。  
  先观节气之深浅，后论财官之向背。  
  人之命内，皆不离乎财官；诸格局中，总要虚邀禄马。先贤已成矜式，后学须自变通。  
  宜向之而运背，决之贫贱。  
  宜背之而运向，断之困弱。  
  喜生以逢生，贵而可取。  
  受克而值克，吉而堪言。  
  逢官而看财，见财富贵。  
  逢杀而看印，遇印荣华。  
  逢印看官而遇官，八而七贵。  
  逢财看杀原有杀，十有九贫。  
  甲乙运入西方，身旺功名可许。  
  壬癸路经南域，主健为贵。  
  印财不宜身旺地。  
  食神最喜劫财乡。  
  官杀混杂，身弱则贫。  
  官杀两停，合杀为贵。  
  年月官星，早年出仕。  
  日时正贵，晚岁得名。  
  胞胎逢印绶，禄享千钟。  
  财气遇长生，田肥万顷。  
  秋冬官星逢刃伤，存金去火贵无疑。  
  腊月伤官喜见官。  
  破印重伤而祸死。  
  财旺生官者，何贵少而富多？  
  伤官见官者，何官高而财足？  
  无伤不贵，有病为奇，宜当弃之，理妙于斯，何必外取。  
  如，火炎水少遇庚辛，休作身旺官轻而取。  
  或，土重木绝逢壬癸，难作身旺官轻而决。  
  财轻莫逢劫地。  
  印多最妙财乡。  
  财旺生官，用赂取贵。  
  杀星制刃，劫宝图名。  
  身旺偏财何取，必取横财。  
  主捷正财偏劫，频见妻灾。  
  劫财阳刃入官杀，台阁之臣。  
  归禄倒冲逢刃伤，廊庙之贵。  
  身旺有杀逢印绶，权断之官。  
  主弱逢印见财星，寻常之客。  
  阳刃伤官有制，膺职掌于兵刑。  
  正官正印无伤，出仕牧其士庶。  
  财旺稼穑，给饷之官。  
  飞禄朝阳，侍廷之相。  
  乾坤本清气，畿国之荣。  
  子午为极尊，黄门之贵。  
  癸日癸时兼亥丑，魁名及第入翰林。  
  壬日壬时叠寅辰，高爵承恩登御阁。  
  日德见魁罡，纵吉运，贫寒之士。  
  魁罡见财官，任得地，衣禄之人。  
  伤官见官，妙入财印之地。  
  财星破印，贵行比劫之中。  
  命逢财，运逢杀，吉而堪言。  
  命逢杀，运逢财，凶而可决。  
  女多伤官，归禄得之极吉。  
  男逢阳刃，身弱遇之为奇。  
  金神、归禄、栏叉，女命逢之最忌。  
  阳刃、伤官、七杀，男子值之得权。  
  金神入火逢杀刃，贵而无疑。  
  杀重有印逢食伤，荣而自有。  
  正官无印，居官不显。  
  阳刃七杀，出牧驰名。  
  身旺无依，僧道之例。  
  桃花滚浪，娼妓之流。  
  金弱火强，土木消溶之匠。  
  土多水浅，行商针线之工。  
  五湖云绕，始荣终辱己身贫。  
  遍野桃花，一世风流多酒色。  
  亡神拱杀，盗贼之徒。  
  秀气失时，清名之士。  
  印旺身强多嗜酒。  
  丁壬妒合犯淫讹。  
  身印俱强，平生少病。  
  天月德助，处世无殃。  
  食神生旺，胜似财官。  
  贵全官杀，有弃命就财、就杀、就官者；有馀富贵，无依专旺。  
  绝食、绝财、绝官者，无限贫穷。  
  身弱弃命要无根，官居宰辅。  
  主衰身化得其时，位近天廷。  
  男命，类属从化、照返鬼伏；女命，纯和清贵、浊滥淫娼。宜细详之！  

- **分字分词释义**：
  - **以日为主专论财官**：以日干为主，专门论述财官。
  - **官乃为扶身之本财为养命之源**：官是扶身根本，财是养命之源。
  - **先观节气之深浅后论财官之向背**：先看节气深浅，再论财官向背。
  - **逢官而看财见财富贵**：逢官看财，财旺则富贵。
  - **逢杀而看印遇印荣华**：逢杀看印，印旺则荣华。
  - **官杀混杂身弱则贫**：官杀并见，身弱主贫。
  - **官杀两停合杀为贵**：官杀均停，合杀为贵。
  - **身弱弃命要无根官居宰辅**：身弱无根弃命从格，可官至宰辅。
  - **食神生旺胜似财官**：食神旺相胜似财官。
  - **桃花滚浪娼妓之流**：桃花极旺，主娼妓之流。

- **规范化释义（primary_lang_explained）**：  
  《挈要捷驰玄妙诀》是一篇“财官速断总诀”，核心是：围绕日主，快速判断**财官格局、从格/弃命、官杀两停、阳刃金神等特殊结构**在不同身强身弱情形下的取舍：  
  - **总纲**：以日干为主，专论财官，官为扶身之本，财为养命之源；先看节气深浅与大局中和，再论财官向背与禄马虚实。  
  - **财官与印杀组合**：  
    - 逢官看财、逢杀看印：官配财主富，杀配印主荣；食神有气胜财官，印旺身强多嗜酒。  
    - 官杀混杂，身弱则贫；官杀两停、杀重有印逢食伤，则可成大贵。  
  - **身强身弱与从格/弃命**：  
    - 身旺偏财宜取横财，归禄倒冲逢刃伤，可作廊庙之贵。  
    - 身弱弃命无根，反可官居宰辅；主衰身化得其时，位近天廷，体现**从格/弃命就财、就官、就杀**的用法。  
  - **性别与格局差异**：  
    - 女多伤官，若归禄反极吉；金神、归禄、栏叉为女命大忌。  
    - 男逢阳刃、伤官、七杀，身弱遇之反有掌权之机。  
  - **职业与气质指向**：  
    - 桃花滚浪为娼妓之流；金弱火强、土多水浅分别指向匠人、行商针线。  
    - 五湖云绕、遍野桃花、亡神拱杀、秀气失时等，分别指向流离、风流酒色、盗贼、清名不遇等人生轨迹。  

- **完整对等诠释（secondary_lang_full）**：  
  **Essential Rapid Secrets (Qie Yao Jie Chi Xuan Miao Jue)**:  
  - This ode is a **quick-evaluation manual for Wealth–Officer patterns**. Taking the Day Master as the core, it shows how to weigh Officer, Wealth, Seal, Food God, Rob Wealth, Blades, and Killing in different strength conditions.  
  - When meeting Officer, look at Wealth: if Wealth is sound and supports Officer, rank and resources follow. When meeting Killing, look at Seal: Seal controlling and nourishing Killing can turn danger into honor.  
  - Mixed Officer–Killing with a weak body brings poverty; balanced Killing with strong Seal and suitable luck yields high office. Excess Wealth on a weak body or repeated Rob Wealth/Blade leads to financial loss and marital problems.  
  - For some charts, the Day Master is too weak and must "abandon the self" and follow Wealth, Officer, or Killing—these **Follower/Conversion patterns** can produce ministers and high officials when timed correctly.  
  - The text distinguishes male and female charts, indicating when Yang Blade, Killing, and Peach Blossom bring power vs. scandal, and links specific star combinations to professions, social roles, and moral tone.  

- **核心要点**：  
  - 以日主为核心，快速判定财官、印杀、食神、劫刃的组合优劣。  
  - 通过身强/身弱区分“正格用身”与“弃命从格”的不同路径。  
  - 明确男命、女命在阳刃、金神、桃花等格局下的差异表现。  
  - 将职业倾向与品行风格（清名/盗贼/娼妓等）纳入命理判断框架。  

- **详细解说**：  《挈要捷驰玄妙诀》以"以日为主，专论财官"开篇，阐述财官速断的核心法则。**总纲**——"官乃为扶身之本，财为养命之源"；"先观节气之深浅，后论财官之向背"确立速断框架。**财官印杀**——"逢官而看财，见财富贵"；"逢杀而看印，遇印荣华"揭示财官印杀的配合之法。**官杀取舍**——"官杀混杂，身弱则贫"；"官杀两停，合杀为贵"阐述官杀混杂的处理。**从格弃命**——"身弱弃命要无根，官居宰辅"；"主衰身化得其时，位近天廷"揭示从格弃命之法。**食神福厚**——"食神生旺，胜似财官"为食神有气之吉象。**职业品行**——"桃花滚浪，娼妓之流"；"亡神拱杀，盗贼之徒"揭示格局与职业品行的对应。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_454]` `[trigger: 财官速断]` `[factor_trigger: ri_weizhu AND zhuanlun_caiguan AND guan_fushen AND cai_yangming]` `[role: 主干]` 以日为主专论财官；官乃为扶身之本财为养命之源。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_455]` `[trigger: 逢官看财]` `[factor_trigger: fengguan_kancai AND fugui AND fengsha_kanyin AND ronghua AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 逢官而看财见财富贵；逢杀而看印遇印荣华。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_456]` `[trigger: 官杀混杂]` `[factor_trigger: guansha_hunza AND shenruo_pin AND guansha_liangting_hesha]` `[role: 条件分支]` 官杀混杂身弱则贫；官杀两停合杀为贵。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_457]` `[trigger: 弃命从格]` `[factor_trigger: shenruo_qiming_wugen AND guan_zaifu AND zhushuai_shenhua]` `[role: 条件分支]` 身弱弃命要无根官居宰辅；主衰身化得其时位近天廷。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_458]` `[trigger: 食神胜财官]` `[factor_trigger: shishen_shengwang AND shengsi_caiguan]` `[role: 条件分支]` 食神生旺胜似财官；食神有气之吉象。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_459]` `[trigger: 桃花娼妓]` `[factor_trigger: taohua_gunlang_changji AND wangshen_gongsha_daozei AND changji]` `[role: 例外处理]` 桃花滚浪娼妓之流；亡神拱杀盗贼之徒；格局与品行。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_460]` `[trigger: 男女差异]` `[factor_trigger: nv_shangguan_guilu_ji AND nan_yangren_shenruo_qi AND anchong_qugui AND angui]` `[role: 条件分支]` 女多伤官归禄得之极吉；男逢阳刃身弱遇之为奇。 → 《渊海子平·挈要捷驰玄妙诀》
  - `[ns_yhzp_461]` `[trigger: 挈要捷驰纲领]` `[factor_trigger: qieyao_jiechi_xuanmiaojue AND caiguan_suduan AND congge_qiming AND zhiye_pinxing]` `[role: 总结]` 挈要捷驰玄妙诀以财官速断、官杀取舍、从格弃命、职业品行为核心，阐述速断秘诀。 → 《渊海子平·挈要捷驰玄妙诀》"""
    normalized_text_zh: str = """"""
    subject: str = "挈要捷驰玄妙诀"
    factor_refs: list = ['rapid_secrets_ode', 'balanced_officer_killing', 'abandon_follow_pattern', 'yang_blade_metal_god', 'raging_peach_blossom']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_挈要捷驰玄妙诀_001_L1",
    )
    version: str = "1.0.0"
