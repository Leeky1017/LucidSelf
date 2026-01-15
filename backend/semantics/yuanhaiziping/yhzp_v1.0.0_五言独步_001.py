"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559560
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
    semantic_id="yhzp_v1.0.0_五言独步_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 五言独步(SemanticEntry):
    """
    - **原文（source_text）**：  
  五言独步。  
  有病方为贵，无伤不是奇；格中如去病，财禄两相随。寅卯多金丑，贫富高低走；南地怕逢申，北方休见酉。建禄生提月，财官喜透天；不宜身...
    """
    
    original_text: str = """- **原文（source_text）**：  
  五言独步。  
  有病方为贵，无伤不是奇；格中如去病，财禄两相随。寅卯多金丑，贫富高低走；南地怕逢申，北方休见酉。建禄生提月，财官喜透天；不宜身再旺，惟喜茂财源。土厚多逢火、归金旺遇秋、冬天水木泛，名利总虚浮。甲乙生居卯，金多反吉祥；不宜重见杀，火地得衣粮。火忌西方酉。（十二长生，丙死于酉）金沉怕水乡。（十二长生，庚死于子）木神休见午。（十二长生，甲死于午）水到卯中伤。（十二长生，壬死于卯）土宿休行亥，临官在巳宫；南方根有旺，西北莫相逢。阴日朝阳格，无根月建辰；西方还有贵，惟怕火来侵。乙木生居酉，莫逢全巳丑；富贵坎离宫，贫穷申酉守。有杀只论杀，无杀方论用；只要去杀星，不怕提纲重。甲乙若逢申，杀印暗相生；木旺金逢旺，冠袍必挂身。离火怕重逢，北方反有功；虽然宜见水，犹恐对提冲。八月官星旺，甲逢秋气深；财官兼有助，名利自然亨。曲直生春月，庚辛干上逢；南离推富贵，坎地却犹凶。甲乙生三月，庚辛戌未存；丑宫壬癸位，何虑见无根。木茂宜金火，身衰鬼作关；时分西与北，轻重辨东西。时上胞胎格，月逢印绶通；杀官行运助，职位至三公。二子不冲午；二寅不冲申；得一分三格，财官印绶同；运中逢克破，一命丧黄泉。进气死不死，退气生不生；终年无发旺，犹忌少年刑。时上偏财格，干头忌比肩；月生逢主旺，贵气福重添。运行十数载，上下五年分；先看流年岁，深知来往旬。时上一位贵，藏在支中是；日主要刚强，名利方有气。


- **分字分词释义**：
  - **有病方为贵无伤不是奇**：格局有病反需去病才贵，无伤不奇。
  - **格中如去病财禄两相随**：格局去病则财禄双全。
  - **建禄生提月财官喜透天**：建禄生于月令，喜财官透干。
  - **火忌西方酉金沉怕水乡**：火忌酉金沉忌水，十二长生死地。
  - **有杀只论杀无杀方论用**：有杀论杀无杀论用。
  - **只要去杀星不怕提纲重**：去杀则不怕月令杀重。
  - **杀印暗相生冠袍必挂身**：杀印相生则冠袍挂身。
  - **进气死不死退气生不生**：进气不死，退气不生。
  - **时上偏财格干头忌比肩**：时上偏财忌比肩劫财。
  - **运行十数载上下五年分**：大运十年分上下各五年。
- **规范化释义（primary_lang_explained）**：  
  《五言独步》以五言口诀形式总结子平命理的核心速断法则，是《四言独步》的姊妹篇与补充。**有病方为贵**：格局有病（冲克破害）反需去病才成贵格，无伤不奇强调平和的重要性。**建禄与财官**：建禄生于提月喜财官透天不宜身再旺，惟喜财源茂盛。**十二长生与死地**：火忌酉（丙死酉）、金沉怕水（庚死子）、木休见午（甲死午）、水到卯伤（壬死卯），土休行亥临官在巳。**有杀论杀无杀论用**：有杀只论杀无杀方论用，只要去杀星不怕提纲重；强调七杀为重中之重。**杀印与去留**：甲乙逢申杀印暗生木旺金旺冠袍挂身，八月官星旺甲逢秋气深财官兼助名利亨。**进退气与时上格**：进气死不死退气生不生；时上偏财格干头忌比肩，时上胞胎格月逢印绶通杀官运助职至三公。**运程与流年**：运行十数载上下五年分，先看流年岁深知来往旬；强调大运流年的精细推算。

- **完整对等诠释（secondary_lang_full）**：  
  **Five-Character Ode**: A sister chapter to the Four-Character Ode, summarizing Zi Ping core quick-judgment rules in five-character verse format. **Having Illness Brings Nobility**: Patterns with "illness" (clashes, harms, breakages) are only noble if the illness is removed; having no injury is not considered extraordinary—this emphasizes the importance of curing imbalances. **Jianlu and Wealth-Officer**: Jianlu born in the Month Command delights in Wealth and Officer penetrating Heaven; it is not suitable for the Body to be vigorous again, only delighting in flourishing Wealth sources. **Twelve Longevity and Death Locations**: Fire detests You (Bing dies at You), Metal sinking fears Water regions (Geng dies at Zi), Wood Spirit ceases upon seeing Noon (Jia dies at Noon), Water arriving at Mao suffers injury (Ren dies at Mao); Earth Star ceases traveling in Hai, while Approaching Office is in Si Palace. **Having Killing Discuss Killing, No Killing Discuss Use**: If there is Killing, only discuss Killing; if no Killing, then discuss Use God; as long as the Killing Star is removed, one need not fear a heavy Month Command; this emphasizes Seven Killings as the utmost priority. **Killing-Seal and Retain-Discard**: Jia and Yi meeting Shen have Killing and Seal secretly generating; if Wood is vigorous and Metal meets vigor, crown and robe will surely hang on the body; in the eighth month Officer Star is vigorous, Jia meets deep autumn Qi; if Wealth and Officer both assist, fame and profit naturally prosper. **Advancing-Retreating Qi and Hour-Position Patterns**: Advancing Qi does not die, Retreating Qi does not live; Hour-position Indirect Wealth pattern taboos Parallel on the Stem head; Hour-position Embryo pattern with Month meeting Seal connecting, if Killing and Officer fortune assists, position reaches Three Dukes. **Fortune Path and Fleeting Years**: Fortune travels for ten-odd years, divided into upper and lower five years; first look at the Fleeting Year (Tai Sui), deeply knowing the passing decades; emphasizes precise calculation of Major Fortune and Fleeting Years.

- **核心要点**：  
  - 以五言口诀补充四言独步，涵盖有病去病、建禄财官、十二长生死地等核心要点  
  - 强调"有杀只论杀无杀方论用"——七杀为命理第一要务  
  - 详述十二长生与死地的应用（火酉金子木午水卯土亥）  
  - 涵盖时上格（时上偏财格、时上胞胎格）与运程流年推算法则

- **详细解说**：  《五言独步》以五言口诀形式补充四言独步。**有病去病**——"有病方为贵，无伤不是奇；格中如去病，财禄两相随"揭示去病成贵之法。**建禄财官**——"建禄生提月，财官喜透天；不宜身再旺，惟喜茂财源"阐述建禄格的配置。**十二长生**——"火忌西方酉，金沉怕水乡；木神休见午，水到卯中伤"揭示十天干死地禁忌。**有杀论杀**——"有杀只论杀，无杀方论用；只要去杀星，不怕提纲重"确立七杀为第一要务。**杀印相生**——"甲乙若逢申，杀印暗相生；木旺金逢旺，冠袍必挂身"揭示杀印相生成贵之法。**进退气**——"进气死不死，退气生不生"阐述进退气的旺衰规律。**时上格与运程**——"时上偏财格，干头忌比肩"；"运行十数载，上下五年分"揭示时格与运程推算法则。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_492]` `[trigger: 有病去病]` `[factor_trigger: youbing_fangwei_gui AND qubing_cailu_xiangsu AND anchong_qugui AND angui]` `[role: 主干]` 有病方为贵无伤不是奇；格中如去病财禄两相随。 → 《渊海子平·五言独步》
  - `[ns_yhzp_493]` `[trigger: 建禄财官]` `[factor_trigger: jianlu_tiyue AND caiguan_toutian AND xi_caiyuan]` `[role: 条件分支]` 建禄生提月财官喜透天；不宜身再旺惟喜茂财源。 → 《渊海子平·五言独步》
  - `[ns_yhzp_494]` `[trigger: 十二长生]` `[factor_trigger: huo_ji_you AND jin_pa_shui AND mu_xiujian_wu AND shui_shang_mao AND jin_chen_shui]` `[role: 条件分支]` 火忌西方酉金沉怕水乡；木神休见午水到卯中伤；死地禁忌。 → 《渊海子平·五言独步》
  - `[ns_yhzp_495]` `[trigger: 有杀论杀]` `[factor_trigger: yousha_lunsha AND wusha_lunyong AND qusha_bupa_tigang]` `[role: 主干]` 有杀只论杀无杀方论用；只要去杀星不怕提纲重。 → 《渊海子平·五言独步》
  - `[ns_yhzp_496]` `[trigger: 杀印相生]` `[factor_trigger: jiayi_feng_shen_shayin AND muwang_jinwang_guanpao AND caiyin AND caiyin_qing_guansha_zu AND changyin AND guanpao]` `[role: 条件分支]` 甲乙若逢申杀印暗相生；木旺金逢旺冠袍必挂身。 → 《渊海子平·五言独步》
  - `[ns_yhzp_497]` `[trigger: 进退气]` `[factor_trigger: jinqi_busi AND tuiqi_busheng AND jintui_wangshuai]` `[role: 条件分支]` 进气死不死退气生不生；进退旺衰规律。 → 《渊海子平·五言独步》
  - `[ns_yhzp_498]` `[trigger: 时上偏财]` `[factor_trigger: shishang_piancai AND ji_bijian AND yunxing_wunian]` `[role: 条件分支]` 时上偏财格干头忌比肩；运行十数载上下五年分。 → 《渊海子平·五言独步》
  - `[ns_yhzp_499]` `[trigger: 五言独步纲领]` `[factor_trigger: wuyan_dubu AND youbing_qubing AND yousha_lunsha AND shier_changsheng]` `[role: 总结]` 五言独步以有病去病、有杀论杀、十二长生、时上格为核心，补充四言独步。 → 《渊海子平·五言独步》"""
    normalized_text_zh: str = """"""
    subject: str = "五言独步"
    factor_refs: list = ['five_character_ode', 'illness_brings_nobility', 'killing_first_principle', 'twelve_longevity_death', 'hour_position_patterns']
    
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
        l1_anchor="yhzp_v1.0.0_五言独步_001_L1",
    )
    version: str = "1.0.0"
