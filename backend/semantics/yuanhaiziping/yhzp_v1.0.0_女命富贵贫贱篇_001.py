"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559214
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
    semantic_id="yhzp_v1.0.0_女命富贵贫贱篇_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 女命富贵贫贱篇(SemanticEntry):
    """
    - **原文（source_text）**：  
  欲推女命，先看官星；官带杀而贫贱，官得令以安荣。伤官太重必妨夫，且是为人性重。倒食重逢须减福，那堪更犯孤辰。杀重须奔贵室。合多定损贞名。坐禄乘舆而...
    """
    
    original_text: str = """- **原文（source_text）**：  
  欲推女命，先看官星；官带杀而贫贱，官得令以安荣。伤官太重必妨夫，且是为人性重。倒食重逢须减福，那堪更犯孤辰。杀重须奔贵室。合多定损贞名。坐禄乘舆而稳厚。冲身动步以轻浮。若乃桃花浪滚，淫奔之耻不堪言。日禄归时，贵重为人所敬。天月二德以坐本命，如逢印绶，贵当两国之封。时日阳刃，本是凶神，既不利于夫主之宫，兼损坏乎平生之性。身干主祯祥。时犯食神健旺，要观八字之强；专食子荣，忌偏印窃身之胜。守闺门而正静，必由阴日守中和。待夫婿以经营，此乃阳干时旺甚。大抵，欣逢正禄。怕犯咸池。清贵得长生之辅。杂浊以败气之归。四柱败多，大忌冲身而犯合。一生忙甚，若非是妓即为尼。印坏与公姑相妒。食专得子嗣之宜。官杀重逢，须防淫乱。姊妹透出，便见争夫。魁罡有灵变之机。日贵有安常之福。即以干支分定，官杀胜而无制伏，不为娼妓，定作尼姑。

- **分字分词释义**：
  - **欲推女命，先看官星**：判断女命首先观察官星，官星为夫星是女命核心。
  - **官带杀而贫贱**：官星与七杀同见，夫星混杂，主贫贱。
  - **官得令以安荣**：官星得时令旺气，主女命安稳荣华。
  - **伤官太重必妨夫**：伤官过旺克制官星，必然妨碍丈夫。
  - **倒食重逢须减福**：偏印（倒食）重叠出现，克制食神，减损福分。
  - **孤辰**：神煞之一，主孤独寡合。
  - **杀重须奔贵室**：七杀过重，女命需依附贵人之家（为妾为仆）。
  - **合多定损贞名**：合神过多，情缘纷杂，必损贞节名声。
  - **坐禄乘舆**：日主坐禄逢驿马，主稳厚有福。
  - **冲身动步**：日主被冲或逢驿马太多，主轻浮不稳。
  - **桃花浪滚**：桃花过多过旺，主淫乱不贞。
  - **日禄归时**：日主之禄归于时柱，主晚年尊贵。
  - **天月二德坐本命**：天德月德坐于日柱或年柱，主大贵。
  - **两国之封**：极高的贵妇封号，象征极品贵格。
  - **时日阳刃**：阳刃出现在时柱或日柱，本是凶神。
  - **专食子荣**：食神专旺无克，主子息荣贵。
  - **阴日守中和**：阴日主守中庸和顺，主女命正静守闺。
  - **阳干时旺**：阳日主时柱旺盛，主能干善经营。
  - **正禄**：正官之禄或日主之禄，女命喜逢。
  - **咸池**：桃花神煞之一，女命忌犯。
  - **官杀无制伏**：官杀过旺无印化无食制，主极贱。

- **规范化释义（primary_lang_explained）**：  
  《女命富贵贫贱篇》系统阐述女命富贵贫贱的判断标准与格局吉凶。**官星为主**：推女命先看官星，官带杀主贫贱官得令主安荣。**伤官倒食**：伤官太重必妨夫且为人性重；倒食重逢须减福那堪更犯孤辰。**杀重合多**：杀重须奔贵室，合多定损贞名。**禄马冲合**：坐禄乘舆主稳厚，冲身动步主轻浮；桃花浪滚淫奔之耻，日禄归时贵重为人敬。**天月二德**：天月二德坐本命如逢印绶贵当两国之封。**阳刃食神**：时日阳刃本是凶神不利夫主兼损平生之性；时犯食神健旺要观八字之强专食子荣忌偏印窃身。**阴阳日干**：守闺门正静必由阴日守中和；待夫婿经营乃阳干时旺甚。**正禄咸池**：大抵欣逢正禄怕犯咸池；清贵得长生之辅杂浊以败气之归。**败多与印食官杀**：四柱败多大忌冲身犯合一生忙甚若非妓即尼；印坏与公姑相妒食专得子嗣之宜；官杀重逢须防淫乱姊妹透出便见争夫。**魁罡日贵**：魁罡有灵变之机日贵有安常之福；官杀胜而无制伏不为娼妓定作尼姑。

- **完整对等诠释（secondary_lang_full）**：  
  **Women's Fate Wealth-Nobility-Poverty-Baseness Chapter**: This chapter systematically expounds the judgment standards and patterns for determining wealth, nobility, poverty, and baseness in women's fate. **Officer Star Primary**: To deduce a woman's fate, first examine the Officer Star; if the Officer carries Killing, it indicates poverty and baseness; if the Officer gains the Command (season), it indicates peace and glory. **Injury Officer-Inverted Food**: If Injury Officer is too heavy, it will inevitably obstruct the husband and indicates a heavy nature; if Inverted Food (Indirect Seal) appears repeatedly, blessings must be reduced, and it is unbearable if further violating Solitary Spirit. **Killing Heavy-Combine Many**: If Killing is heavy, one must run to a noble household (as concubine/servant); if Combinations are numerous, it certainly damages chastity and reputation. **Salary-Horse-Clash-Combine**: Sitting on Salary and riding the Carriage (Horse) indicates stability and thickness; Clashing the Body and moving steps indicates frivolity and floating. If Peach Blossom waves roll, the shame of promiscuous running is unspeakable. If Day Salary returns to Hour, one is noble and respected by others. **Heaven-Moon Two Virtues**: If Heaven and Moon Two Virtues sit on the natal life (Day/Year) and encounter Seal, nobility is equivalent to enfeoffment of two states. **Yang Blade-Food God**: Hour and Day Yang Blade are inherently fierce spirits; they are disadvantageous to the Husband Master's palace and simultaneously damage lifelong character. If the Hour violates Food God which is healthy and vigorous, one must observe the Eight Characters' strength; exclusive Food brings children glory, but taboos Indirect Seal stealing the body's victory. **Yin-Yang Day Stems**: Guarding the inner chamber with propriety and quietude must come from Yin Day keeping moderation; waiting upon the husband to manage affairs comes from Yang Stem Hour being extremely vigorous. **Proper Salary-Salty Pond**: Generally, one delights in meeting Proper Salary and fears violating Salty Pond (Hamchi). Pure nobility obtains assistance from Long Life; mixed turbidity returns to Defeated Qi. **Defeat Many and Seal-Food-Officer-Killing**: If Four Pillars have many Defeats (Zi-Wu-Mao-You), greatly taboos clashing the Body and violating Combinations—a life extremely busy; if not a prostitute, then a nun. If Seal is broken, one is jealous of parents-in-law; if Food is exclusive, one obtains suitability of descendants. If Officer and Killing repeatedly meet, one must guard against promiscuity; if sisters (Parallels) appear transparently, one will see competition for the husband. **Kuigang-Day Noble**: Kuigang possesses mechanism of spiritual flexibility; Day Noble possesses fortune of peaceful constancy. If Officer and Killing prevail without control or suppression, if not becoming a prostitute, one is destined to be a nun.

- **核心要点**：  
  - 系统阐述女命富贵贫贱的判断标准，以官星为第一要务  
  - 官得令主安荣，官带杀主贫贱；伤官太重妨夫，倒食重逢减福  
  - 天月二德坐命逢印绶主两国之封大贵；阳刃食神阴阳日干各有宜忌  
  - 官杀重逢防淫乱，姊妹透出见争夫；官杀胜无制伏不为妓即为尼

- **详细解说**：  《女命富贵贫贱篇》是女命判断的系统性总结，将女命分为"富贵"与"贫贱"两大类型，并提供了完整的判断框架。**官星为首要**——"欲推女命，先看官星"开篇定调：官星得令（当时令旺气）主"安荣"，官星带杀（官杀混杂）主"贫贱"，这是女命富贵贫贱的第一分水岭。**凶神禁忌**——伤官太重"必妨夫"且"为人性重"，倒食（偏印）重逢"须减福"，合多"定损贞名"，这些都是女命常见的凶象。**禄马与桃花**——"坐禄乘舆"主稳厚，"冲身动步"主轻浮，"桃花浪滚"则"淫奔之耻不堪言"。**天月二德**——天德月德坐于本命且逢印绶，"贵当两国之封"，这是女命极品贵格。**阴阳日干**——阴日主"守闺门而正静"，阳日主"待夫婿以经营"，二者性格与命运走向不同。**极端判断**——"官杀胜而无制伏，不为娼妓，定作尼姑"是女命最贱配置，官杀过旺无印化无食制，则沦为边缘人物。全篇以官星为纲，以伤官倒食为忌，以天月二德为贵，以桃花咸池为贱，构建了女命判断的完整体系。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_247]` `[trigger: 女命先看官星]` `[factor_trigger: nvming AND guanxing_xiankan AND fugui_pinjian AND anchong_qugui AND angui]` `[role: 主干]` 欲推女命，先看官星；官带杀而贫贱，官得令以安荣。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_248]` `[trigger: 伤官妨夫]` `[factor_trigger: nvming AND shangguan_taizhong AND fang_fu AND harm_officer_harms_husband]` `[role: 条件分支]` 伤官太重必妨夫，且是为人性重；伤官克官星为女命大忌。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_249]` `[trigger: 倒食减福]` `[factor_trigger: nvming AND daoshi_chongfeng AND jianfu AND inverted_food]` `[role: 条件分支]` 倒食重逢须减福，那堪更犯孤辰；偏印克食神减损福分。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_250]` `[trigger: 合多损贞]` `[factor_trigger: nvming AND he_duo AND sun_zhenming]` `[role: 条件分支]` 合多定损贞名；合神过多情缘纷杂必损贞节名声。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_251]` `[trigger: 桃花浪滚]` `[factor_trigger: nvming AND taohua_langgun AND yinluan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 若乃桃花浪滚，淫奔之耻不堪言；桃花过旺主淫乱。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_252]` `[trigger: 天月二德大贵]` `[factor_trigger: nvming AND tianyue_erde AND yinshou AND dagui AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin AND liangguo_feng]` `[role: 条件分支]` 天月二德以坐本命，如逢印绶，贵当两国之封。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_253]` `[trigger: 阴日阳干]` `[factor_trigger: nvming AND yinri_zhenjing AND yanggan_jingying AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 守闺门而正静，必由阴日守中和；待夫婿以经营，此乃阳干时旺甚。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_254]` `[trigger: 正禄咸池]` `[factor_trigger: nvming AND zhenglu_ji AND xianchi_ji AND taohua_xianchi]` `[role: 条件分支]` 大抵，欣逢正禄，怕犯咸池；正禄为吉咸池为忌。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_255]` `[trigger: 官杀重逢淫乱]` `[factor_trigger: nvming AND guansha_chongfeng AND yinluan AND caiyin AND caiyin_qing_guansha_zu AND changyin AND multiple_officer_killing_multiple_husbands]` `[role: 条件分支]` 官杀重逢，须防淫乱；姊妹透出，便见争夫。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_256]` `[trigger: 官杀无制极贱]` `[factor_trigger: nvming AND guansha_wuzhi AND jijian]` `[role: 例外处理]` 官杀胜而无制伏，不为娼妓，定作尼姑；官杀过旺无制为女命最贱。 → 《渊海子平·女命富贵贫贱篇》
  - `[ns_yhzp_257]` `[trigger: 女命富贵贫贱纲领]` `[factor_trigger: nvming AND fugui_pinjian_gangling AND anchong_qugui AND angui]` `[role: 总结]` 女命富贵贫贱篇以官星为纲，以伤官倒食为忌，以天月二德为贵，以桃花咸池为贱。 → 《渊海子平·女命富贵贫贱篇》"""
    normalized_text_zh: str = """"""
    subject: str = "女命富贵贫贱篇"
    factor_refs: list = ['officer_season', 'virtue', 'inverted_food', 'two_states_enfeoffment', 'officer_killing_no_control']
    
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
        l1_anchor="yhzp_v1.0.0_女命富贵贫贱篇_001_L1",
    )
    version: str = "1.0.0"
