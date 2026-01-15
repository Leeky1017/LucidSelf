"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864303
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
    semantic_id="zgjm_v1.0.0_刀剑旌节钟鼓_001",
    book_id="zhougong",
    engine_id="dream"
)
class 刀剑旌节钟鼓(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  刀剑旌节钟鼓。

  【条文】

  君王对仗，有异吉。
  旌旗有龙，大吉利。
  抱旌节，主贵人扶。

  旌剑引入山，主凶。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  刀剑旌节钟鼓。

  【条文】

  君王对仗，有异吉。
  旌旗有龙，大吉利。
  抱旌节，主贵人扶。

  旌剑引入山，主凶。
  造旌盖，主大吉利。
  羽盖盖身，主富贵。

  旗幡迎接，大富贵。
  旗幡竟出，主疾病。
  手持旌节，有恩赏。

  白盖覆身，大吉利。
  见做新旌，大吉利。
  与人分伞，主分散。

  拔刀出行，主大吉。
  得人刀，主行人至。
  与人三刀，作刺史。

  与人与斫，大吉庆。
  被刀出血，得酒食。
  折刀刺人，主失利。

  刀斧自伤，大吉利。
  得人刀斧，禄位至。
  刀落水中，妻妾亡。

  失落刀剑，主破财。
  带刀剑行，有财利。
  磨刀剑锋快，大吉。

  与人刀剑，皆主凶。
  剑在床头，大吉利。
  女人带刀，大吉庆。

  女人拔刀，主有子。
  剪刀，主分财之事。
  剪刀剪物，主得财。

  剪刀折股，妻妾亡。
  甲胄庇身，主吉利。
  枪槊，主官位吉利。

  见军兵散，主有凶。
  钟磐有声，远人来。
  钟豉大鸣，福禄至。

  打鼓有声，远人来。
  见鼓佳声，欢乐吉。
  见鼓不呜，凶必至。

  看放烟火，百忧散。

- 分字分词释义：

  - **刀剑旌节钟鼓**：本类总纲，涵盖兵器（刀、剑、斧、枪槊、甲胄）、仪仗（旌旗、节、羽盖、伞盖）、声器（钟、鼓、钟磐）与烟火，反映**权威、征伐、庇护与庆典**四大方向。
  - **君王对仗，有异吉**：与君王对列而立或立于阵仗之前，多主被权力核心“看见”，得非常之吉，象征意外机缘与殊礼.
  - **旌旗有龙，大吉利；抱旌节，主贵人扶**：旌旗上有龙纹、手抱旌节（符节）皆为极尊之象，主得显贵之人提携，出入仪仗之列.
  - **旌剑引入山，主凶**：被旌旗、刀剑引入山中，多象征被卷入险地或权力斗争前线，凶象较重.
  - **造旌盖、羽盖盖身，主大吉利、主富贵**：新造旌盖、羽盖覆身，是“为己张盖、蒙受庇荫”的意象，多主名位渐高、富贵可期.
  - **旗幡迎接、旗幡竟出**：旗幡迎接主大富贵；旗幡竟出（出门不返）则有“气散、人心散”之象，多主疾病与耗损.
  - **手持旌节，有恩赏**：亲手执节，多主奉命行事、承领任务，获得上位者恩赏.
  - **白盖覆身、见做新旌，与人分伞**：白盖覆身、见人制作新旌皆为新设仪仗，多主新任、新封与新恩；与人分伞则象征把同一庇护权分给多人，多主伙伴或家人分散.
  - **拔刀出行，主大吉；得人刀，主行人至；与人三刀，作刺史**：拔刀出行主大吉，是“有所准备而行”的象征；得人刀主行人至或外来帮助；与人三刀而作刺史，是“以武得官”的比喻.
  - **与人与斫，大吉庆；被刀出血，得酒食**：与人比武或砍斫而得胜、或小有伤而流血，原书多作“先险后吉”，视为为宴饮、庆功所致的小伤.
  - **折刀刺人，主失利；失落刀剑，主破财**：刀折而刺人，或刀剑遗失，皆指损器伤人、破军破财之象.
  - **刀斧自伤，大吉利；得人刀斧，禄位至**：自伤反吉，强调“伤在己、不伤于人”反可解祸；得人刀斧则象征受托以职，禄位可至.
  - **刀落水中，妻妾亡**：刀为阳刚之物，亦可象征配偶或情感之刃，落水多主情感或婚姻结构溃散，对妻妾不利.
  - **带刀剑行，有财利；磨刀剑锋快，大吉**：行路带刀有财利，主在风险中亦有收益；磨刀锋利，则是“备战充分”的象征，有利于把握机会.
  - **与人刀剑，皆主凶**：主动将刀剑交与他人，象征把控制权与攻防之权交出，多主不利.
  - **剑在床头，大吉利；女人带刀、大吉庆；女人拔刀，主有子**：
    - 剑在床头，多解作“防身有备”，主家宅与婚床有护卫力；
    - 女人佩刀或拔刀，多主性格刚强、能自护，古书由此引出“得子”“有子”的象.
  - **剪刀、剪物、折股**：剪刀主分割、分财：
    - 剪刀剪物主得财，为分配中获利；
    - 剪刀折股则主妻妾有损，多指感情或家内结构的断裂.
  - **甲胄庇身、枪槊主官位吉利**：披甲穿胄、手持枪槊，多主掌兵、从军或在体系中负重责，官位可得而亦有风险.
  - **见军兵散，主有凶**：兵散则阵乱，多主环境中有集体恐慌或秩序崩坏.
  - **钟磐有声、钟豉大鸣、打鼓有声**：钟鼓齐鸣，主远人来、福禄至、喜事集；声响既远且和谐，则多为喜讯.
  - **见鼓佳声欢乐吉、见鼓不呜凶必至**：鼓声佳妙而有节律，主庆典与群体欢乐；若见鼓却不鸣，则为“名存实亡”，主事情中止或凶事将至.
  - **看放烟火，百忧散**：烟火以光声并发之乐象征忧思被冲散，多为解愁之梦.

- **规范化释义（primary_lang_explained）**：

  本类围绕“兵器、仪仗与乐器”，通过刀剑、旌旗、甲胄、钟鼓、烟火等意象，占断一个人在**权力结构、冲突场域与庆典场合**中的位置与吉凶.

  总体来说：

  - **仪仗与盖伞相关的梦，多主贵人庇护与荣耀场合的出入。**
  - **刀剑斧枪相关的梦，多主行动决断、风险承受与名禄得失。**
  - **剪刀与“分割”相关的梦，多关财产划分与婚姻、妻妾结构的变化。**
  - **钟鼓与烟火相关的梦，多主远人来信、宴饮庆典与忧愁释放，也可能提示未鸣之鼓、将至的变局。**

- 核心要点：

  - **看“旌节旗盖”象征的权威与庇护：**
    - 抱旌节、羽盖盖身、白盖覆身、新旌初作，多主身在仪仗之列、受制度或贵人庇护；
    - 旌剑引入山、旗幡竟出、与人分伞，则提醒被卷入险地或人心涣散之忧.
  - **看“刀剑斧枪”的指向：是自护、为公，还是伤人、失器？**
    - 拔刀出行、带刀剑行、磨刀锋快，多主行动有备、可以得财或得势；
    - 自伤、被刀出血而吉，偏向“以小伤解大祸”；
    - 折刀刺人、与人刀剑、刀落水中、失落刀剑，则多与破财、婚姻受损或权力旁落有关.
  - **看“剪刀与分股”的分合：**
    - 剪刀象征分开与分配：剪物获财，可是合理分配之利；
    - 剪刀折股则是结构断裂，易应妻妾或副缘的损害.
  - **看“甲胄、军兵与散聚”的军阵之象：**
    - 披甲持槊，多主身处高压或战斗岗位，既有立功之机，亦有身心代价；
    - 军兵若散，则为阵乱与失序之象，现实中宜警惕组织瓦解或群体恐慌.
  - **看“钟鼓与烟火”的声光：**
    - 钟鼓大鸣、鼓声佳妙，多主远客来、喜事临；
    - 鼓存而不鸣，则预示名义上的职位或项目实际停摆，需警惕空有其表.

- 详细解说：

  **（一）旌旗、羽盖与节伞：权势光环与庇护之网**

  - “君王对仗有异吉”“旌旗有龙大吉利”“抱旌节主贵人扶”“白盖覆身大吉利”“见做新旌大吉利”等条，集中描绘“站在权力前列、身处仪仗之中”的场景：
    - 对仕途而言，是被看见、被点名、被委任的象征；
    - 对普通人而言，则可视为在集体或组织中获得正式认可与保护.
  - 与之相对，“旌剑引入山主凶”提示：若被军旗与兵器所引而入险地，则可能深陷权力斗争或风险一线，需要衡量自身能否承受其后果.
  - “旗幡迎接大富贵”“旗幡竟出主疾病”说明同一物象因方向不同而吉凶互换：
    - 旗幡迎接是“礼迎其人”，为吉；
    - 旗幡出而不返，则是“气散势尽”，主精力耗损与病气滋生.
  - “与人分伞主分散”则点出：共同庇护之物若被分割，多主关系与资源的拆分，现实中可对应伙伴、团队、家庭结构的调整与拆分.

  **（二）刀剑斧枪：行动风险与名禄得失**

  - “拔刀出行主大吉”“带刀剑行有财利”“磨刀剑锋快大吉”共同强调：当下决心明确、准备充分时，行动往往顺利，且有财利可期.
  - “得人刀主行人至”“得人刀斧禄位至”则指出来自他人的兵器象征“授权”与“托付”：可能是职位、任务或资源交接.
  - “与人与斫大吉庆”“被刀出血得酒食”“刀斧自伤大吉利”一组文字较为反常：
    - 古解多视为“小伤换大吉”，即在比试或劳作中略有伤损，反为日后宴饮、喜庆与荣誉的铺垫；
    - 现实解读可理解为：适度的冒险与付出虽有代价，却换来更大的成长与回报.
  - “折刀刺人主失利”“失落刀剑主破财”“刀落水中妻妾亡”“与人刀剑皆主凶”则是动用兵器的反面案例：
    - 折刀刺人象征以失灵的工具去伤人，得不偿失；
    - 刀剑遗失或落水，则象征控制权旁落、婚姻与财务安全受损；
    - 主动将刀剑交给他人，则可能在现实中让渡关键话语权与防卫能力.

  **（三）剪刀与妻妾、分财：分配秩序的考验**

  - “剪刀主分财之事”“剪刀剪物主得财”显示：剪刀象征分割与划界，在合理运用时可以帮助厘清权属、获得属于自己的那一份.
  - “剪刀折股妻妾亡”则提醒：若工具本身损坏，或分割过程中过于粗暴，易导致感情结构的断裂，尤其在古人语境下多指妻妾受损；今人可泛指伴侣关系中的严重伤害或决裂.

  **（四）甲胄、枪槊与军兵散：战阵与秩序的两面**

  - “甲胄庇身主吉利”“枪槊主官位吉利”说明：
    - 甲胄是防护之物，穿在身上表示在风险中仍有护体之力；
    - 枪槊则是进攻与权责的象征，多主掌兵、管理或承担冲锋任务的角色.
  - “见军兵散主有凶”则从反面点出：若战阵之兵四散，则为“令不行、众不一”的象征，现实中需警惕团队瓦解、组织纪律松弛或外部安全局势恶化.

  **（五）钟鼓与烟火：消息、庆典与忧思释放**

  - “钟磐有声远人来”“打鼓有声远人来”“钟豉大鸣福禄至”皆指：钟鼓之声远播，主远客来访、消息传来或福禄将临，是信息与能量汇聚的象意.
  - “见鼓佳声欢乐吉”“见鼓不呜凶必至”则把焦点放在“鼓是否真正发声”：
    - 鼓声佳妙则活动顺利、人心欢悦；
    - 鼓不鸣则象征仪式空转、形同虚设，现实中可能是项目停摆、制度失灵或名誉与实利脱节.



- **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to weapons (swords, blades, axes, spears, armour), ceremonial regalia (banners, staffs of authority, canopies, umbrellas), and ritual percussion (bells, drums, gongs). These images collectively map onto **authority, warfare, protection, and celebration**.

  The core interpretive principle hinges on the condition and use of these symbols: a sharp, intact blade carried purposefully portends decisive action and fortune; a broken or lost sword signals power slipping away or financial loss. Banners emblazoned with dragons or personally held staffs of authority indicate noble patronage and advancement within hierarchy; banners departing and not returning warn of dissipating energy and illness. Bells and drums sounding in unison herald distant visitors, good tidings, and prosperity; drums present yet silent suggest hollow rituals and impending setbacks. Fireworks lighting up the dream sky disperse accumulated worries.

  **Key interpretive axes**:
  - **Blades and swords**: focus on "state and direction of use"—drawing a blade to travel brings great fortune; giving one's weapon away surrenders control; blade falling into water harms spouse or partner; self-inflicted minor wounds paradoxically resolve greater misfortune.
  - **Banners, staffs, and canopies**: focus on "ceremonial shelter and rank"—holding the staff of authority earns rewards; feathered canopy covering one's body promises wealth and status; sharing an umbrella with another foretells parting of ways.
  - **Scissors**: focus on "division and allocation"—cutting cloth brings profit through fair distribution; broken scissors warn of marital or partnership rupture.
  - **Bells and drums**: focus on "whether sound actually issues forth"—resounding tones summon distant guests and blessings; silence despite the instrument's presence indicates failure beneath appearances.

- 校勘与字词辨析：

  - 原文本类多以三句连写，如“君王对仗有异吉　旌旗有龙大吉利　抱旌节主贵人扶”等，本稿在 L1 层将其拆分为独立句式，并加上逗号、句号，仅为阅读与后续处理方便，不改动原字序与用词.
  - “君王对仗有异吉”一语，“对仗”亦可作“对杖”“对仗列阵”解，本稿不作细分，只按“在君王仪仗前列对立而站”之象解说.
  - “旗幡竟出主疾病”中“竟出”各本或作“竞出”“出竟”等，皆有“出门不返”“越界而出”之意，本稿据底本录为“竟出”，在释义中以“旗幡出而不返”说明其气散之象.
  - “钟磐有声远人来　钟豉大鸣福禄至”中“钟豉”疑为“钟鼓”之讹字，L1 层仍据原文直录，在释义中按钟鼓齐鸣解，不强行改字.
  - “与人三刀作刺史”一作“人与三刀作刺史”，本稿采“与人三刀”的结构，在分词中解释为“以刀为信、得刺史之任”，不再追索具体史事.
  - “剪刀折股妻妾亡”所言“妻妾亡”，乃古书关于婚姻与副缘的想象框架，L1 层仅据其文字记录，不直接套用于现代伦理判断，后续高阶语义层可再补充心理学与当代关系视角.

  - **English**：
    - In "君王对仗有异吉," the term "对仗" can also be read as "对杖" or "对仗列阵." This edition does not distinguish between these readings, simply interpreting it as "standing in the king's ceremonial formation."
    - In "旗幡竟出主疾病," the phrase "竟出" varies across editions as "竞出" or "出竟," all carrying the meaning of "going out and not returning" or "crossing boundaries." This edition follows the base text as "竟出," explaining it as "banners going out and dissipating energy."
    - In "钟磐有声远人来" and "钟豉大鸣福禄至," the term "钟豉" is suspected to be an error for "钟鼓." The L1 layer records the original text as-is, interpreting it as bells and drums sounding together without forcibly changing the characters.
    - "与人三刀作刺史" appears in some versions as "人与三刀作刺史." This edition adopts the "与人三刀" structure, explaining it as "giving three blades as a token to obtain the position of Regional Inspector," without tracing specific historical events.
    - The phrase "剪刀折股妻妾亡" involving "妻妾亡" represents the ancient text's imaginative framework about marriage and secondary relationships; the L1 layer only records its literal meaning without applying modern ethical judgments. Psychological and contemporary relationship perspectives can be added in higher semantic layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_108]` `[trigger: 梦见君王对仗]` `[factor_trigger: dream_emperor_guard]` `[role: 主干]` 君王对仗，有异吉。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_109]` `[trigger: 梦见旌旗有龙]` `[factor_trigger: dream_flag_dragon]` `[role: 主干]` 旌旗有龙，大吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_110]` `[trigger: 梦见抱旌节]` `[factor_trigger: dream_hold_banner]` `[role: 主干]` 抱旌节，主贵人扶。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_111]` `[trigger: 梦见旌剑引入山]` `[factor_trigger: dream_banner_sword_mountain]` `[role: 主干]` 旌剑引入山，主凶。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_112]` `[trigger: 梦见造旌盖]` `[factor_trigger: dream_make_canopy]` `[role: 主干]` 造旌盖，主大吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_113]` `[trigger: 梦见羽盖盖身]` `[factor_trigger: dream_feather_canopy]` `[role: 主干]` 羽盖盖身，主富贵。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_114]` `[trigger: 梦见旗幡迎接]` `[factor_trigger: dream_flag_welcome]` `[role: 主干]` 旗幡迎接，大富贵。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_115]` `[trigger: 梦见旗幡竟出]` `[factor_trigger: dream_flag_out]` `[role: 主干]` 旗幡竟出，主疾病。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_116]` `[trigger: 梦见手持旌节]` `[factor_trigger: dream_hold_banner_staff]` `[role: 主干]` 手持旌节，有恩赏。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_117]` `[trigger: 梦见白盖覆身]` `[factor_trigger: dream_white_canopy]` `[role: 主干]` 白盖覆身，大吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_118]` `[trigger: 梦见做新旌]` `[factor_trigger: dream_new_banner]` `[role: 主干]` 见做新旌，大吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_119]` `[trigger: 梦见与人分伞]` `[factor_trigger: dream_share_umbrella]` `[role: 主干]` 与人分伞，主分散。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_120]` `[trigger: 梦见拔刀出行]` `[factor_trigger: dream_draw_sword_travel]` `[role: 主干]` 拔刀出行，主大吉。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_121]` `[trigger: 梦见得人刀]` `[factor_trigger: dream_receive_knife]` `[role: 主干]` 得人刀，主行人至。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_122]` `[trigger: 梦见人与三刀]` `[factor_trigger: dream_three_knives]` `[role: 主干]` 人与三刀，作刺史。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_123]` `[trigger: 梦见与人与斫]` `[factor_trigger: dream_chop_together]` `[role: 主干]` 与人与斫，大吉庆。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_124]` `[trigger: 梦见被刀出血]` `[factor_trigger: dream_cut_bleed]` `[role: 主干]` 被刀出血，得酒食。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_125]` `[trigger: 梦见折刀刺人]` `[factor_trigger: dream_broken_knife_stab]` `[role: 主干]` 折刀刺人，主失利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_126]` `[trigger: 梦见刀斧自伤]` `[factor_trigger: dream_blade_selfharm]` `[role: 主干]` 刀斧自伤，大吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_127]` `[trigger: 梦见得人刀斧]` `[factor_trigger: dream_receive_axe]` `[role: 主干]` 得人刀斧，禄位至。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_128]` `[trigger: 梦见刀落水中]` `[factor_trigger: dream_knife_in_water]` `[role: 主干]` 刀落水中，妻妾亡。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_129]` `[trigger: 梦见失落刀剑]` `[factor_trigger: dream_lose_sword]` `[role: 主干]` 失落刀剑，主破财。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_130]` `[trigger: 梦见带刀剑行]` `[factor_trigger: dream_carry_sword]` `[role: 主干]` 带刀剑行，有财利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_131]` `[trigger: 梦见磨刀剑锋快]` `[factor_trigger: dream_sharpen_sword]` `[role: 主干]` 磨刀剑锋快，大吉。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_132]` `[trigger: 梦见与人刀剑]` `[factor_trigger: dream_give_sword]` `[role: 主干]` 与人刀剑，皆主凶。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_133]` `[trigger: 梦见剑在床头]` `[factor_trigger: dream_sword_bedside]` `[role: 主干]` 剑在床头，大吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_134]` `[trigger: 梦见女人带刀]` `[factor_trigger: dream_woman_knife]` `[role: 主干]` 女人带刀，大吉庆。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_135]` `[trigger: 梦见女人拔刀]` `[factor_trigger: dream_woman_draw_knife]` `[role: 主干]` 女人拔刀，主有子。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_136]` `[trigger: 梦见剪刀]` `[factor_trigger: dream_scissors]` `[role: 主干]` 剪刀，主分财之事。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_137]` `[trigger: 梦见剪刀剪物]` `[factor_trigger: dream_cut_with_scissors]` `[role: 主干]` 剪刀剪物，主得财。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_138]` `[trigger: 梦见剪刀折股]` `[factor_trigger: dream_scissors_break]` `[role: 主干]` 剪刀折股，妻妾亡。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_139]` `[trigger: 梦见甲胄庇身]` `[factor_trigger: dream_armor]` `[role: 主干]` 甲胄庇身，主吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_140]` `[trigger: 梦见枪槊]` `[factor_trigger: dream_spear]` `[role: 主干]` 枪槊，主官位吉利。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_141]` `[trigger: 梦见军兵散]` `[factor_trigger: dream_army_disperse]` `[role: 主干]` 见军兵散，主有凶。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_142]` `[trigger: 梦见钟磐有声]` `[factor_trigger: dream_bell_chime]` `[role: 主干]` 钟磐有声，远人来。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_143]` `[trigger: 梦见钟鼓大鸣]` `[factor_trigger: dream_bell_drum_loud]` `[role: 主干]` 钟鼓大鸣，福禄至。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_144]` `[trigger: 梦见打鼓有声]` `[factor_trigger: dream_drum_beat]` `[role: 主干]` 打鼓有声，远人来。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_145]` `[trigger: 梦见鼓佳声]` `[factor_trigger: dream_drum_good_sound]` `[role: 主干]` 见鼓佳声，欢乐吉。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_146]` `[trigger: 梦见鼓不鸣]` `[factor_trigger: dream_drum_silent]` `[role: 主干]` 见鼓不鸣，凶必至。 → 《周公解梦·刀剑旌节钟鼓》
  - `[ns_zgjm_147]` `[trigger: 梦见看放烟火]` `[factor_trigger: dream_fireworks]` `[role: 主干]` 看放烟火，百忧散。 → 《周公解梦·刀剑旌节钟鼓》"""
    normalized_text_zh: str = """"""
    subject: str = "刀剑旌节钟鼓"
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
        l1_anchor="zgjm_v1.0.0_刀剑旌节钟鼓_001_L1",
    )
    version: str = "1.0.0"
