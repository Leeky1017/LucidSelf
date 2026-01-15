"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558590
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
    semantic_id="yhzp_v1.0.0_论天干地支暗藏总诀_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论天干地支暗藏总诀(SemanticEntry):
    """
    - **原文（source_text）**：  
  立春念三丙火用,馀日甲木旺提纲。  
  惊蛰乙木未用事,春分乙未正相当。  
  清明乙木十日管,后来八日癸水洋;谷雨前三戊土盛,其中土旺要消详...
    """
    
    original_text: str = """- **原文（source_text）**：  
  立春念三丙火用,馀日甲木旺提纲。  
  惊蛰乙木未用事,春分乙未正相当。  
  清明乙木十日管,后来八日癸水洋;谷雨前三戊土盛,其中土旺要消详。  
  立夏又伏戊土取,小满过午丙火光。  
  芒种己土相当好,中停七日土高张;夏至阴生阳极利,丙丁火旺有土张。  
  小暑十日丁火旺,后来三日乙木芳,己土三日威风盛;大暑己土十日黄。  
  立秋十日壬水涨,处暑十五庚金良。  
  白露七日庚金旺,八日辛兮祇独行。  
  寒露七日辛金管,八日丁火又水降;霜降己土十五日,其中杂气取无妨。  
  立冬七日癸水旺,壬水八日更流忙;小雪七日壬水急,八日甲木又芬芳。  
  大雪七日壬水管,冬至癸水更潺汪。  
  小寒七日癸水养,八日辛金丑库藏;大寒十日己土胜,术者精研仔细详。

- **分字分词释义**：
  - **暗藏**：天干地支在节气流转中暗中主事之气，不显于表层干支，而在节令、人元中司令。
  - **总诀**：总纲性歌诀，统摄用神、旺衰判断的基本时间框架。
  - **念三**：底本作"念三"，解为"廿三"或"二十三"日，指立春后若干日由丙火主事。部分传本作异文，因版本差异较大，本次保留"念三"字形，仅在校勘中备述。
  - **馀日甲木旺提纲**：除前若干日丙火司令外，余日由甲木得令，为春季提纲之气。"提纲"即主宰一季格局之纲领。
  - **十日/七日/八日/十五日**：某节气后若干日内，由某一五行司令主气。非精确天文分割，而是命理经验划分，用以判断旺衰用神。
  - **癸水洋/壬水忙/潺汪**：以水势之盛衰形容癸、壬两水当令时的充盈、奔流状态，暗示水气旺盛、流行无阻。
  - **丑库藏**：辛金在丑为库地，丑中辛金得根有藏，冬末小寒节后辛金伏藏于丑土之中。
  - **杂气**：支中兼含多种天干之气，非一气独专，如辰、戌、丑、未等墓库之支，多为杂气之象。

- **规范化释义（primary_lang_explained）**：  
  这条总诀按二十四节气顺序，说明一年中各节气前后，哪一位天干、哪一类五行在暗中主持气机、成为旺气的"提纲"。立春之初有一段时间由丙火当令，之后轮到甲木成为春令主气；惊蛰时乙木力量尚未真正发挥，要到春分才算正当其位。清明前后十日仍是乙木主事，继而有一段癸水当令，又在谷雨前若干日里戊土力量大盛。立夏、小满、芒种、夏至诸节，则在戊土、丙火、己土与火土相杂的司令中轮替；小暑、大暑之间，丁火、乙木与己土相继为令。秋季由壬水开局，处暑庚金担当主事；白露后先是庚金旺盛，再轮到辛金独掌纲领。寒露之后辛金当令一段时间，随后丁火、水气相继显现，霜降时己土主事而杂气并存。至冬季，立冬、小雪、大雪、小寒、大寒诸节，则大体在癸水、壬水、甲木与己土、辛金之间轮替主令，构成冬令之水土、藏金之势。总体而言，此诀是为了告诉命者：判断命局mìngjú的旺衰，不仅要看四柱干支，还要看节令中暗藏的司令之气，分辨每一节气之前后由哪一气最为得令。

- **完整对等诠释（secondary_lang_full）**：  
  This master formula follows the sequence of the 24 solar terms throughout the year, clarifying which Heavenly Stem and which of the Five Elements secretly governs the vital energy (qi) during each period, becoming the "guiding principle" of that season's dominant force. At the beginning of spring, Fire element through Bing reigns for a certain period, then Wood through Jia becomes the primary spring force. During Awakening of Insects, Yi Wood's power has not yet fully manifested; only at Spring Equinox does it assume its proper position. Around Qingming, Yi Wood governs for ten days, followed by a period when Gui Water flows abundantly, and before Grain Rain Wu Earth's power intensifies. From Start of Summer through Summer Solstice, Wu Earth, Bing Fire, Ji Earth, and their combinations rotate in dominance. Between Minor Heat and Major Heat, Ding Fire, Yi Wood, and Ji Earth successively take command. Autumn begins with Ren Water's surge, then Geng Metal takes charge at End of Heat; after White Dew, Geng Metal first flourishes, then Xin Metal assumes sole governance. After Cold Dew, Xin Metal commands for a period, followed by manifestations of Ding Fire and Water qi; at Frost Descent, Ji Earth governs while mixed qi coexists. In winter, from Start of Winter through Major Cold, Gui Water, Ren Water, Jia Wood, Ji Earth, and Xin Metal rotate in dominance, forming the winter configuration of Water-Earth and hidden Metal. In essence, this formula teaches practitioners that judging the strength and weakness of a fate structure requires examining not only the visible Four Pillars' stems and branches, but also the hidden governing qi within each solar term, distinguishing which element holds sway at which moment. power before and after each node.

- **核心要点**：
  - 以二十四节气为纲，分配一年中各阶段的"司令天干"与五行旺衰，是全书判断旺衰和用神的时间基准
  - 同一节令内部，往往分为前若干日、后若干日，分别由不同天干主事，提示命理判断时要细分节内气机
  - 春夏多见木火土轮替主令，秋冬多见金水与藏金、杂气当权，反映四时五行生克流转的大势
  - 判断命局mìngjú的旺衰，不仅要看四柱干支，还要看节令中暗藏的司令之气，分辨每一节气之前后由哪一气最为得令
  - 歌中多用"养、旺、急、涨、潺汪、库藏"等词形容气机状态，提示该五行处于养、生、旺、衰、藏等不同阶段

- **详细解说**：  
  从结构上看，此条歌诀并非孤立存在，而是作为《渊海子平》全书的"时间坐标系"，为后文十神、格局、六亲等判断提供季节与气机的背景。命理上常言"得令为先"，但"何谓得令"在不同门派中有细微差别：有的以月令为主，有的重视节气，更有以司令天干、人元司令来分配旺衰者。本条即属于以节气司令为主的系统。歌诀从立春起首，顺次行至大寒，几乎囊括全年节令。每一节气内部，以"若干日"为单位划分主令：例如立春前段以丙火主事，表示阳气初动，火气先萌；之后转由甲木为提纲，象征万物发生、木气渐长。惊蛰、春分、清明、谷雨等节气，则描写乙木、癸水、戊土依次得令的过程：木气生而未用、渐至正当，水气起而流行，土气盛而需防过旺。夏季部分则强调火土相杂：立夏、芒种、夏至、小暑、大暑之间，丙火、丁火、戊土、己土交替主令，既象征阳气极盛，也提示火土过旺之时，命局中同类过多就易成燥烈之象。入秋之后，歌诀将重点转向金水：立秋壬水、处暑庚金、白露庚辛、寒露辛金与丁火、水气的交替，表现出秋令肃杀与金气收敛，同时水气渐起，为冬令作准备。霜降一节特别提到"己土十五日，其中杂气取无妨"，是提醒术者：墓库之支所含的杂气，在某些时候也可以成为取用之神，不能只看表面"土旺"而忽略其内含金水木之气。冬季诸节，则以癸水、壬水为主，间以甲木、辛金、己土等，构成"冬水主令、土金藏气"的图景。实务应用上，此歌诀常被用来细化"日主得令"与"用神得令"的判断：例如同样是寅月甲木日，若节气仍在立春前段，则丙火司令，对火用神有利；若已过春分，则乙木得令，木气比旺而火气稍次。以此为基础，可以更精细地区分同一月份中不同日子的旺衰，避免只以月令一刀切地判断命局。

- **校勘与字词辨析**：
  - **立春念三丙火用**：底本作"念三"。部分流行本作"廿三"，亦有资料记载民间抄本作"戊三丙火九"等异文，大体皆指立春后前若干日由丙火司令。鉴于各本差异较大且缺乏统一权威底本，本次精校阶段遵从现用底本，保留"念三"之写法，并在此注明异文，供后续版本学考证参考。
  - **春分乙未正相当**：文义上可读作"至春分时，乙气正当其位"，其中"未"既可视作语气副词"未尝不"之类的讹变，亦可能与部分版本所列十二支对应系统有关。因目前手头材料有限，暂不强行改作"乙木"，仍据底本录"乙未"，并在解释中按"乙木当令"处理。
  - **癸水洋/壬水忙/潺汪**：底本文字通顺，语义通过水势的形容体现旺盛与流行之象，未见确凿他本可据以订正，故不作改动。
  - 其他如各节气后"十日、七日、八日、十五日"等数字，在各家命理书与不同版本的《渊海子平》中多有细微差别，本次仅据现用底本统一呈现，不对数字作臆测性修订，留待后续有影印古本或专题研究时再行系统比勘。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_001]` `[trigger: 二十四节气]` `[factor_trigger: solar_term]` `[role: 主干]` 二十四节气各有主令天干，节内再分若干日轮流主事。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_002]` `[trigger: 立春前段]` `[factor_trigger: solar_term AND tiangan_bing]` `[role: 条件分支]` 立春之初由丙火当令，之后轮到甲木成为春令主气。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_003]` `[trigger: 春季节气]` `[factor_trigger: season_spring AND tiangan_yi]` `[role: 条件分支]` 春分时乙木正当其位，为春季提纲之气。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_004]` `[trigger: 夏季节气]` `[factor_trigger: season_summer AND element_fire AND element_earth AND bing_ding_fire]` `[role: 条件分支]` 夏季火土相杂，丙火、丁火、戊土、己土交替主令。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_005]` `[trigger: 秋季节气]` `[factor_trigger: season_autumn AND element_metal AND element_water]` `[role: 条件分支]` 秋季由壬水开局，处暑庚金担当主事，白露后先是庚金旺盛。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_006]` `[trigger: 冬季节气]` `[factor_trigger: season_winter AND element_water AND element_metal]` `[role: 条件分支]` 冬季诸节以癸水、壬水为主，间以甲木、辛金、己土等。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_007]` `[trigger: 杂气月令]` `[factor_trigger: dizhi_chen OR dizhi_xu OR dizhi_chou OR dizhi_wei]` `[role: 例外处理]` 霜降时己土主事而杂气并存，杂气可以成为取用之神。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_008]` `[trigger: 判断旺衰]` `[factor_trigger: solar_term AND day_master_strength]` `[role: 总结]` 判断命局旺衰，不仅要看四柱干支，还要看节令中暗藏的司令之气。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_300]` `[trigger: 财多]` `[factor_trigger: abundant_wealth]` `[role: 条件分支]` 财多身弱则不胜财，需身旺方可担财。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_301]` `[trigger: 四吉神]` `[factor_trigger: auspicious_four]` `[role: 条件分支]` 正官、正印、食神、正财为四吉神。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_302]` `[trigger: 权力]` `[factor_trigger: authority AND borrowed_killing_authority]` `[role: 结果]` 官杀得用主权力，食伤制杀亦主权。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_303]` `[trigger: 厄尽]` `[factor_trigger: bad_luck_end]` `[role: 结果]` 大运转顺则厄尽吉来。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_304]` `[trigger: 卑贱]` `[factor_trigger: baseness]` `[role: 结果]` 格局破败主贫贱。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_305]` `[trigger: 吉神]` `[factor_trigger: benefic]` `[role: 条件分支]` 吉神宜生旺有情。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_306]` `[trigger: 仁慈]` `[factor_trigger: benevolent]` `[role: 结果]` 印绶有情主仁慈。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_307]` `[trigger: 身体]` `[factor_trigger: body AND body_vigorous_no_reliance AND body_vigorous_weak_adjustment]` `[role: 主干]` 日主代表身体，旺则健，弱则病。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_308]` `[trigger: 灾厄]` `[factor_trigger: calamity]` `[role: 结果]` 冲刑破害主灾厄。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_309]` `[trigger: 辰戌冲]` `[factor_trigger: chen_xu_clash]` `[role: 条件分支]` 辰戌冲动库房，主出入财物。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_310]` `[trigger: 辰戌全]` `[factor_trigger: chen_xu_complete]` `[role: 条件分支]` 辰戌丑未四库全，主杂气多变。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_311]` `[trigger: 子女]` `[factor_trigger: children AND hour_pillar]` `[role: 主干]` 时柱为子女宫，食伤为子女星。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_312]` `[trigger: 子孙兴旺]` `[factor_trigger: children_prosperity]` `[role: 结果]` 食伤有情主子孙兴旺。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_313]` `[trigger: 清格]` `[factor_trigger: clear_pattern]` `[role: 条件分支]` 清格无杂主贵，杂格多破主贱。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_314]` `[trigger: 争妒]` `[factor_trigger: contention_jealousy]` `[role: 结果]` 比劫争财主争妒。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_315]` `[trigger: 克制]` `[factor_trigger: control]` `[role: 主干]` 五行相克为制，克者制被克者。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_316]` `[trigger: 羊刃]` `[factor_trigger: day_blade]` `[role: 条件分支]` 羊刃为日主之刃，旺极则有刚毅之象。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_317]` `[trigger: 日主]` `[factor_trigger: day_master]` `[role: 主干]` 日主为命之根本，代表自身。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_318]` `[trigger: 日主强]` `[factor_trigger: day_master_strong]` `[role: 条件分支]` 日主得令得地则强，可担财官。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_319]` `[trigger: 日主弱]` `[factor_trigger: day_master_weak]` `[role: 条件分支]` 日主失令失地则弱，需印比扶助。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_320]` `[trigger: 生死]` `[factor_trigger: dead_alive]` `[role: 结果]` 五行有生死之别，长生为生，死绝为死。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_321]` `[trigger: 土]` `[factor_trigger: earth]` `[role: 主干]` 土为中央之气，主信主脾。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_322]` `[trigger: 地支]` `[factor_trigger: earthly_branch]` `[role: 主干]` 地支为十二，主空间与藏干。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_323]` `[trigger: 易养]` `[factor_trigger: easy_raising]` `[role: 结果]` 印绶护佑主易养成人。 → 《渊海子平·论天干地支暗藏总诀》
  - `[ns_yhzp_324]` `[trigger: 五行]` `[factor_trigger: element]` `[role: 主干]` 五行金木水火土，为命理根本。 → 《渊海子平·论天干地支暗藏总诀》"""
    normalized_text_zh: str = """"""
    subject: str = "论天干地支暗藏总诀"
    factor_refs: list = ['solar_term', 'new_candidate', 'month_command', 'new_candidate', 'new_candidate', 'new_candidate', 'earthly_branch_hidden_stems']
    
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
        l1_anchor="yhzp_v1.0.0_论天干地支暗藏总诀_001_L1",
    )
    version: str = "1.0.0"
