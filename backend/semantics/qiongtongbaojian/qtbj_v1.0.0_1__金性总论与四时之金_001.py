"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578207
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
    semantic_id="qtbj_v1.0.0_1__金性总论与四时之金_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1金性总论与四时之金(SemanticEntry):
    """
    - **原文（source_text）**：
  金以至阴为体，中含至阳之精，乃能坚刚，独异众物，若独阴而不坚，冰雪是也，遇火则消矣。故金无火炼，不能成器，金重火轻，执事繁难。金轻火重，煅炼消亡。金极...
    """
    
    original_text: str = """- **原文（source_text）**：
  金以至阴为体，中含至阳之精，乃能坚刚，独异众物，若独阴而不坚，冰雪是也，遇火则消矣。故金无火炼，不能成器，金重火轻，执事繁难。金轻火重，煅炼消亡。金极火盛，为格最精。金火全、名曰铸印。犯丑字、即为损模。金火多名为乘轩，遇死衰、反为不利。
  
  木火炼金，成名锐而退速。纯金遇水，逢富显以赢余。
  
  金能生水，水旺则金沉；土能生金，金多则土贱。金无水干枯；水重、则沉沦无用。金无土则死绝；土重、则埋没不显。两金两火、最上。两金两木、才足。一金生三水，力弱难胜；一金得三木，顽钝自损。金成则火灭，故金未成器，欲得见火；金已成器，不欲见火。金到申酉巳丑，亦可谓之成也，运喜西北，不利东南。
  
  生于春月，余寒未尽，贵乎火气为荣；性柔体弱，欲得厚土为助；水盛增寒，难施锋锐之势；木旺损力，有挫钝之危，金来比助，扶持最妙。比而无火，失类非良。
  
  夏月之金，尤为柔弱，形质未备，尤嫌死绝。火多而却为不厌；水盛而滋润呈祥；见木而助鬼伤身；遇金而扶持精壮；土薄而最为有用；土厚而埋没无光。
  
  秋月之金，当权得令，火来煅炼，遂成钟鼎之材。土多培养，反惹顽浊之气。见水则精神越秀；逢木则琢削施威；金助愈刚，刚过则决。气重愈旺，旺极则衰。
  
  冬月之金，形寒性冷；木多则难施琢削之功；水盛未免沉潜之患。土能制水，金体不寒，火来助土，子母成功，喜比肩聚气相扶，欲官印温养为利。

- **分字分词释义**：
  - **至阴**：极阴之质 / 金为西方少阴 / 五行本体
  - **至阳之精**：阳气之精华 / 肃杀刚硬之性 / 金之特质
  - **坚刚**：坚硬刚强 / 金性 / 与木火土水区别之处
  - **独异**：独自不同 / 金的独特性 / 五行之中
  - **火炼**：火来锻炼 / 成器之道 / 官杀作用
  - **成器**：成为器皿 / 有用之才 / 格局成立
  - **铸印**：铸造印章 / 金火配合成大器 / 格局名
  - **损模**：损坏模型 / 丑土湿泥坏火 / 凶格
  - **乘轩**：乘坐高车 / 高官显贵 / 吉格
  - **金水相涵**：金生水、水润金 / 清秀之象 / 吉格
  - **水多金沉**：水旺则金沉底 / 泄气太过 / 凶象
  - **土多金埋**：土重则金被埋 / 印多身弱 / 凶象
  - **钟鼎之材**：大器之才 / 秋金得火炼 / 成就比喻
  - **琢削**：雕琢削减 / 金克木 / 财星作用

- **规范化释义（primary_lang_explained）**：
  金以至阴（少阴？）作为本体，中间包含至阳的精华（肃杀之气/刚性），所以能坚硬刚强，独自不同于万物。如果是独阴而不坚硬，那就是冰雪，遇到火就消融了。所以金没有火的锻炼，不能成为器皿。金重火轻，做事繁杂艰难（顽金难化）。金轻火重，锻炼消亡（金被熔化）。金极火盛（身旺杀旺），格局最精妙。金火齐全，名字叫“铸印”。如果犯了丑字（金库/湿土晦火），就是损模。金火多名为“乘轩”（高官），遇到死衰运，反而不利。
  
  木火炼金，成名锐利（快）但退得也快。纯金遇到水（金水相涵），富贵显达而且有盈余。
  
  金能生水，水旺则金沉（水多金沉）；土能生金，金多则土贱（土生金泄气）。金无水则干枯（顽金）；水重则沉沦无用。金无土则死绝（无生源）；土重则埋没不显（土多金埋）。两金两火（比劫+官杀），最上格。两金两木（身财两停），财足。一金生三水（伤官泄气），力弱难胜；一金得三木（财多身弱），顽钝自损。金成器则火灭（不再需火），所以金未成器，想要见火；金已成器，不想要见火。金到了申酉巳丑（西方/金局），也可以说是成了，运气喜欢西北（金水），不利东南（木火）。
  
  生于春月（寅卯辰），余寒未尽，贵在有火气为荣（温养/制木）；性柔体弱（绝胎养），想要得到厚土（印）帮助；水盛（伤官）增加寒气，难以施展锋锐的气势；木旺（财）损耗力量，有挫折钝化的危险，金来比助，扶持最妙。有比肩而无火，失去同类也不良（？失类可能指不成格）。
  
  夏月之金（巳午未），尤其柔弱，形质未备，最嫌死绝（长生沐浴冠带，其实气弱）。火多（杀）却不厌恶（？原文“不厌”疑为“不堪”或“不宜”，但夏金喜水济火，若无水则火多销熔。原文可能指长生之金需火炼？待考。通常夏金怕火多）。水盛（食伤）滋润呈祥（润燥制杀）；见木（财）助鬼（生杀）伤身；遇金比助扶持精壮；土薄（印）最为有用；土厚则埋没无光。
  
  秋月之金（申酉戌），当权得令，火来锻炼，就成为钟鼎之材。土多培养，反而招惹顽浊之气（土重埋金）。见水（食伤）则精神越秀（金水伤官）；逢木（财）则琢削施威（金克木）；金助（比劫）愈刚，刚过则折决。气重愈旺，旺极则衰。
  
  冬月之金（亥子丑），形寒性冷；木多则难施琢削之功（冻木坚）；水盛未免沉潜之患（水多金沉）。土能制水，金体不寒，火来助土，子母成功（官印相生），喜欢比肩聚气相扶，想要官印温养为利。

- **完整对等诠释（secondary_lang_full）**：
  Metal takes Ultimate Yin as its body, containing Ultimate Yang essence within; thus it is hard and strong, unique among things. If it were "Lonely Yin" without hardness, it would be ice/snow, melting upon meeting Fire. Therefore, without Fire smelting, Metal cannot become a vessel. Heavy Metal Light Fire means tasks are difficult. Light Metal Heavy Fire means melting away. Extreme Metal Prosperous Fire forms the finest pattern. Metal and Fire complete is called "Casting the Seal". Meeting "Chou" (Ox) breaks the mold. Abundant Metal/Fire is called "Riding the Carriage" (High Official); meeting Death/衰 (Decline) phases is unfavorable.
  
  Wood and Fire smelting Metal brings sharp fame but quick retreat. Pure Metal meeting Water leads to wealth, prominence, and surplus.
  
  Metal generates Water; if Water is prosperous, Metal sinks. Earth generates Metal; if Metal is abundant, Earth is cheap. Metal without Water is dry/withered; Water heavy makes it sink uselessly. Metal without Earth dies (no source); Earth heavy buries it. Two Metals Two Fires is superior. Two Metals Two Woods brings sufficient wealth. One Metal generating Three Waters is weak; One Metal with Three Woods becomes dull and damaged. When Metal is formed, Fire is extinguished; thus Unformed Metal wants Fire, Formed Metal dislikes Fire. Metal in Shen/You/Si/Chou is considered "Formed"; Luck favors NW, dislikes SE.
  
  Spring Metal: Remaining cold; honors Fire Qi. Soft nature weak body; wants thick Earth assistance. Prosperous Water adds cold, blunting sharpness. Prosperous Wood drains strength. Metal assistance is best. Parallels without Fire are not good.
  
  Summer Metal: Especially weak, form unprepared. Fire abundant is not disliked (textual query: usually feared). Water moistening is auspicious. Wood aids Ghost (Fire) harming body. Metal assistance strengthens. Thin Earth is useful; thick Earth buries.
  
  Autumn Metal: Commanding season. Fire smelting makes vessels (Zhong Ding). Abundant Earth makes it stubborn/muddy. Seeing Water makes spirit elegant. Meeting Wood exercises power. Metal assistance makes it too rigid, risking breakage.
  
  Winter Metal: Cold form/nature. Wood hard to carve. Water causes sinking. Earth controls Water, warming Metal. Fire aiding Earth brings success to Mother/Child. Likes Parallels support; wants Officer/Seal for warmth.

- **核心要点**：
  - **喜忌**：
    - **顽金喜火**：未成器之金（秋金），喜火炼。
    - **成器忌火**：已成器之金（申酉金或见水），忌火销。
    - **金水相涵**：金白水清，富贵。
    - **土重埋金**：忌土多。
  - **四时**：
    - 春：体弱，喜土金，火暖。
    - 夏：柔弱，喜水润土生。
    - 秋：当令，喜火炼或水泄。
    - 冬：寒冷，喜火土。

- **详细解说**：
  - “铸印”：金为印章之材，火为铸造之工。金火相停，掌大权。
  - “水多金沉”：金生水，但水多泄气过重，金沉底无用。
  - “土多金埋”：土生金，但土太厚金被掩埋，无光。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_311]` `[trigger: 金五行]` `[factor_trigger: element_metal AND yin_yang_nature]` `[role: 主干]` 金以至阴为体，中含至阳之精，乃能坚刚，独异众物。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_312]` `[trigger: 金无火]` `[factor_trigger: element_metal AND NOT element_fire AND metal_unformed]` `[role: 主干依赖]` 故金无火炼，不能成器；金重火轻，执事繁难。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_313]` `[trigger: 金火配合]` `[factor_trigger: element_metal AND element_fire AND metal_fire_balance AND pattern_casting_seal]` `[role: 条件分支]` 金极火盛，为格最精。金火全、名曰铸印。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_314]` `[trigger: 金遇水]` `[factor_trigger: element_metal AND element_water AND metal_water_containing]` `[role: 条件分支]` 纯金遇水，逢富显以赢余。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_315]` `[trigger: 水多金沉]` `[factor_trigger: element_metal AND water_excessive AND water_sinks_metal]` `[role: 例外处理]` 金能生水，水旺则金沉。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_316]` `[trigger: 土多金埋]` `[factor_trigger: element_metal AND earth_excessive AND earth_buries_metal]` `[role: 例外处理]` 土能生金，金多则土贱。土重则埋没不显。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_317]` `[trigger: 春金]` `[factor_trigger: season_spring AND element_metal AND likes_fire_warmth AND likes_earth_support]` `[role: 条件分支]` 生于春月，余寒未尽，贵乎火气为荣；性柔体弱，欲得厚土为助。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_318]` `[trigger: 夏金]` `[factor_trigger: season_summer AND element_metal AND likes_water_moistening]` `[role: 条件分支]` 夏月之金，尤为柔弱，水盛而滋润呈祥。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_319]` `[trigger: 秋金]` `[factor_trigger: season_autumn AND element_metal AND likes_fire_smelt AND zhongding_material]` `[role: 条件分支]` 秋月之金，当权得令，火来煅炼，遂成钟鼎之材。 → 《穷通宝鉴·论金》#29.1
  - `[ns_qttbj_320]` `[trigger: 冬金]` `[factor_trigger: season_winter AND element_metal AND likes_parallel_support AND likes_officer_seal_warmth]` `[role: 条件分支]` 冬月之金，形寒性冷，喜比肩聚气相扶，欲官印温养为利。 → 《穷通宝鉴·论金》#29.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 金性总论与四时之金"
    factor_refs: list = ['casting_seal', 'damaging_mold', 'metal_water_containing', 'earth_buries_metal']
    
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
        l1_anchor="qtbj_v1.0.0_1__金性总论与四时之金_001_L1",
    )
    version: str = "1.0.0"
