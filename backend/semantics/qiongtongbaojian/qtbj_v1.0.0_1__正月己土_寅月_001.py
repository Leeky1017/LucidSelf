"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597066
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
    semantic_id="qtbj_v1.0.0_1__正月己土_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1正月己土寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月己土，田园犹冻，盖因腊气未除，余寒未退，故丙为尊。得丙照暖，万物自生，忌见壬水，反为己病，何也？壬乃江湖之水，湖水一发，则田园洗荡，变为沙土，而根...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月己土，田园犹冻，盖因腊气未除，余寒未退，故丙为尊。得丙照暖，万物自生，忌见壬水，反为己病，何也？壬乃江湖之水，湖水一发，则田园洗荡，变为沙土，而根苗尽没矣。须戊作堤，以保园圃。壬多要见戊制。有戊出干者，定主玉堂金马。若乏戊制，必属平常。
  或一派甲木，有庚出干，加以癸丙齐透，配得中和，亦名利双全。即丙生寅月，庚透天干，亦有俊秀。若甲多无庚，残疾废人，宜用丁泄。
  或一派火，即不见水无克，何也？正月己土寒滋，必丙暖，反主厚禄。加一癸透，科甲自然。戊透、反作常人。或一派戊土，有甲出制，又主荣显。如见乙出，虽多不能疏土，且乙多者，奸诈小人。

- **分字分词释义**：
  - **田园犹冻**：田园仍然冰冻 / 寅月己土 / 需暖
  - **腊气未除**：腊月寒气未消 / 余寒 / 需丙
  - **丙为尊**：丙火最为尊贵 / 调候 / 用神
  - **江湖之水**：江河湖泊之水 / 壬水 / 忌神
  - **田园洗荡**：田地被冲洗荡平 / 壬水冲奔 / 凶象
  - **戊作堤**：戊土作堤坝 / 制壬 / 救应
  - **玉堂金马**：翰林院 / 大贵 / 吉象
  - **残疾废人**：残废之人 / 甲多无庚 / 凶象
  - **奸诈小人**：奸诈卑鄙之人 / 乙多 / 凶象

- **规范化释义（primary_lang_explained）**：
  正月（寅月）的己土，田园还冻结着，因为腊月（十二月）的寒气未除，余寒未退，所以丙火（太阳）最为尊贵。得到丙火照暖，万物自然生长。忌讳见到壬水（江河水），反成为己土的病，为什么？因为壬是江湖之水，湖水一发，就会洗荡田园，使沃土变为沙土，根苗全都淹没。必须用戊土（防洪堤）作堤坝，来保护园圃。壬水多要见戊土制约。有戊土出干的人，定主玉堂金马（高官翰林）。如果缺乏戊土制约，必属平常人。
  如果一派甲木（正官），有庚金（伤官）出干，加上癸水丙火齐透，配合得中和（财官印食全），也名利双全。即使丙火生于寅月（长生），庚金透出天干，也有俊秀之气。如果甲木多而无庚金，是残疾废人（官多变杀攻身），适宜用丁火泄木气（官印相生）。
  如果一派火（印），即使不见水（财）克火，为什么也好？因为正月己土寒冷湿滋，必须丙火暖局，反而主厚禄。加上一个癸水透出（调候/财），科甲自然。戊土透出（比劫），反而作常人（分夺财/暖气）。或者一派戊土（比劫），有甲木出干制约（官制劫），又主荣显。如果见到乙木（七杀）出干，虽然多也不能疏土（乙木力小），而且乙木多的人，是奸诈小人。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth in the 1st Month (Tiger Month): The fields are still frozen; the Cold Qi of the 12th Month remains. Thus Bing Fire is supreme. With Bing to warm, everything grows naturally. It dreads Ren Water, which becomes a disease. Why? Ren is River/Lake water; if it floods, it washes away the fields, turning them into sand, drowning all roots and seedlings. Wu Earth must serve as a dike to protect the garden. If Ren is abundant, Wu must control it. If Wu reveals, it promises "Jade Hall and Golden Horse" (High Office). Without Wu, one is ordinary.
  If there is a mass of Jia Wood, having Geng revealed, plus Gui and Bing both revealing, balanced and harmonized, implies both fame and profit. Even with Bing born in Yin Month and Geng revealing, one is handsome/talented. If Jia is abundant without Geng, one is disabled/useless; suitable to use Ding to leak (Wood).
  If there is a mass of Fire, even without Water to control it, why is it good? Because 1st Month Ji Earth is cold and wet; it must be warmed by Bing, conversely implying substantial salary. Adding one Gui revealed makes Civil Service natural. If Wu reveals, one is ordinary. Or if a mass of Wu Earth appears with Jia to control, it implies glory. Seeing Yi reveal, even if abundant, cannot dredge Earth; abundant Yi implies a treacherous/petty person.

- **核心要点**：
  - **首要用神**：丙火（暖）。田园解冻。
  - **忌讳**：壬水（冲奔）。田园怕冲，喜戊作堤。
  - **官杀**：甲多喜庚（剪裁/制官留杀？不，伤官见官在正月亦可用？应是制木护土），无庚用丁（化杀）。
  - **乙木**：乙为杂草，不能疏土，多则奸诈。

- **详细解说**：
  - 己土为田园卑湿之土，寅月寒湿。
  - “玉堂金马”：翰林院，指清贵之官。
  - 己土怕壬水冲荡，所谓“水泛土溃”，必须用戊土堤防。癸水（雨露）则不忌，反喜滋润。
  - “乙多奸诈”：因乙木在寅月旺，克伐己土，且乙为七杀/偏官，性情阴柔多计谋。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_560]` `[trigger: 寅月己土丙为尊]` `[factor_trigger: month_yin AND tiangan_ji AND tiangan_bing AND likes_bing_warm]` `[role: 主干]` 正月己土，田园犹冻，腊气未除，余寒未退，故丙为尊。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_561]` `[trigger: 丙照暖万物自生]` `[factor_trigger: month_yin AND tiangan_ji AND tiangan_bing AND fields_thaw AND sprouts_grow]` `[role: 主干依赖]` 得丙照暖，万物自生。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_562]` `[trigger: 壬多须戊作堤玉堂金马]` `[factor_trigger: month_yin AND tiangan_ji AND ren_multiple AND tiangan_wu AND jade_hall]` `[role: 条件分支]` 壬多要见戊制，有戊出干者，定主玉堂金马。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_563]` `[trigger: 壬无戊制田园洗荡平常]` `[factor_trigger: month_yin AND tiangan_ji AND ren_multiple AND NOT tiangan_wu AND fields_washed]` `[role: 例外处理]` 若乏戊制，壬水洗荡田园，变为沙土，根苗尽没，必属平常。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_564]` `[trigger: 甲庚癸丙名利双全]` `[factor_trigger: month_yin AND tiangan_ji AND jia_multiple AND tiangan_geng AND tiangan_gui AND tiangan_bing AND fame_wealth_both]` `[role: 条件分支]` 或一派甲木，有庚出干，加以癸丙齐透，配得中和，亦名利双全。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_565]` `[trigger: 丙生寅月庚透俊秀]` `[factor_trigger: month_yin AND tiangan_bing AND tiangan_geng AND clear_elegant]` `[role: 条件分支]` 即丙生寅月，庚透天干，亦有俊秀。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_566]` `[trigger: 甲多无庚残疾废人宜丁泄]` `[factor_trigger: month_yin AND tiangan_ji AND jia_multiple AND NOT tiangan_geng AND tiangan_ding AND disabled_pattern]` `[role: 例外处理]` 若甲多无庚，残疾废人，宜用丁泄。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_567]` `[trigger: 一派火加癸厚禄科甲]` `[factor_trigger: month_yin AND tiangan_ji AND fire_excessive AND tiangan_bing AND tiangan_ding AND tiangan_gui AND peach_waves]` `[role: 条件分支]` 或一派火，即不见水无克，正月己土寒滋必丙暖，反主厚禄；加一癸透，科甲自然。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_568]` `[trigger: 一派火戊透反作常人]` `[factor_trigger: month_yin AND tiangan_ji AND fire_excessive AND tiangan_wu AND NOT tiangan_gui AND ordinary_status]` `[role: 例外处理]` 戊透，反作常人。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_569]` `[trigger: 一派戊土甲出荣显]` `[factor_trigger: month_yin AND tiangan_ji AND wu_multiple AND tiangan_jia AND noble_promotion]` `[role: 条件分支]` 或一派戊土，有甲出制，又主荣显。 → 《穷通宝鉴·三春己土》#25.1
  - `[ns_qttbj_570]` `[trigger: 乙多奸诈小人]` `[factor_trigger: month_yin AND tiangan_ji AND yi_multiple AND treacherous_petty]` `[role: 例外处理]` 如见乙出，乙多者，奸诈小人。 → 《穷通宝鉴·三春己土》#25.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 正月己土（寅月）"
    factor_refs: list = ['jade_hall', 'fields_washed', 'treacherous_petty']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__正月己土_寅月_001_L1",
    )
    version: str = "1.0.0"
