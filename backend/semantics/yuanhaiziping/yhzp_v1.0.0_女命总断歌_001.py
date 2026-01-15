"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559203
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
    semantic_id="yhzp_v1.0.0_女命总断歌_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 女命总断歌(SemanticEntry):
    """
    - **原文（source_text）**：  
  择妇须沉静，细说与君听。夫主要强宫，身主要强甚。官星若不合，夫主无所依。合绝莫合贵，此法少人推。专以日为年，此法少人传。带禄入生旺，产死教人谤。驿...
    """
    
    original_text: str = """- **原文（source_text）**：  
  择妇须沉静，细说与君听。夫主要强宫，身主要强甚。官星若不合，夫主无所依。合绝莫合贵，此法少人推。专以日为年，此法少人传。带禄入生旺，产死教人谤。驿马带贵人，终久落风尘。有辰休见戌，有戌休见辰；辰戌若相见，多是淫贱人。有杀不怕合，无杀却怕合；合神若是多，非妓亦讴歌。贵人一座正，两三作宠定。阳刃带伤官，驳杂事多端。满盘多是印，损子必须定。二德坐正财，富贵自然来。四柱俱休囚，封赠福禄寿。金水若相逢，必招美丽容。寅申巳亥全，孤淫口便便。子午逢卯酉，定是随人走。辰戌逢丑未，妇道之大忌。两贵一位杀，权家富贵说。财官若藏库，冲破岂不富。天干一字连，孤破祸绵绵。地字连一字，两度成婚事。

- **分字分词释义**：
  - **择妇须沉静**：选择妻子须看其是否沉稳安静，性情为首要考量。
  - **夫主要强宫**：夫星（官杀）所在宫位须旺盛有力。
  - **身主要强甚**：日主也须相当强健，方能承载夫星之福。
  - **官星若不合**：官星若无合神护卫，夫星孤立无依。
  - **合绝莫合贵**：宁可合入绝地，不可合入贵人；此为女命特殊法则。
  - **带禄入生旺**：禄神入于生旺之地，虽吉却有难产风险。
  - **驿马带贵人**：驿马与贵人同柱，女命反主终落风尘。
  - **辰戌若相见**：辰戌二支同时出现，形成冲克，主淫贱。
  - **有杀不怕合**：命中有七杀，合神可制杀反吉。
  - **无杀却怕合**：命中无杀，合神过多则情缘纷杂主淫。
  - **非妓亦讴歌**：合多即使不为妓女，也是歌姬之类风月职业。
  - **阳刃带伤官**：阳刃与伤官同见，事情驳杂多端。
  - **满盘多是印**：印绶过多，克制子星，必定损子。
  - **二德坐正财**：天德月德坐于正财，富贵自然而来。
  - **金水若相逢**：金水二行相生相逢，主貌美容颜。
  - **寅申巳亥全**：四马齐全，主孤独淫乱口舌。
  - **子午逢卯酉**：四败齐见，主随人而走失节。
  - **辰戌逢丑未**：四库齐全，为妇道之大忌。
  - **天干一字连**：天干同一字贯穿，主孤破灾祸连绵。
  - **地字连一字**：地支同一字贯穿，主两度成婚。

- **规范化释义（primary_lang_explained）**：  
  《女命总断歌》以歌诀形式总结女命判断的诸多要点与速断口诀。**性情与夫身**：择妇须沉静，夫主要强宫身主要强甚；官星若不合夫主无所依。**合化与禄马**：合绝莫合贵此法少人推，专以日为年此法少人传；带禄入生旺产死教人谤，驿马带贵人终久落风尘。**辰戌与杀合**：有辰休见戌有戌休见辰辰戌若相见多是淫贱人；有杀不怕合无杀却怕合合神若是多非妓亦讴歌。**贵人与刃印**：贵人一座正两三作宠定；阳刃带伤官驳杂事多端；满盘多是印损子必须定。**二德与四柱**：二德坐正财富贵自然来；四柱俱休囚封赠福禄寿。**金水与四马四败**：金水若相逢必招美丽容；寅申巳亥全孤淫口便便；子午逢卯酉定是随人走；辰戌逢丑未妇道之大忌。**贵杀与财库**：两贵一位杀权家富贵说；财官若藏库冲破岂不富。**天干地支连**：天干一字连孤破祸绵绵；地字连一字两度成婚事。

- **完整对等诠释（secondary_lang_full）**：  
  **Women's Fate General Judgment Song**: Summarizes numerous key points and quick-judgment formulas for women's fate in verse format. **Temperament and Husband-Body**: In selecting a wife, calmness and quietude are essential. Husband Master palace must be strong, and Body Master must be especially strong. If Officer Star lacks combination, Husband Master has no foundation to rely upon. **Combination-Transformation and Salary-Horse**: Avoid combining with extinction but not nobility—few understand this method. Using Day exclusively as Year—few transmit this technique. Bringing Salary into growth-vigor positions, yet dying in childbirth invites slander. Post Horse combined with Noble Person eventually leads to fallen status. **Chen-Xu and Killing-Combination**: If having Chen, avoid seeing Xu; if having Xu, avoid seeing Chen. When Chen-Xu meet, mostly indicates promiscuous base people. Having Killing, don't fear combination; lacking Killing, fear combination instead. If Combine Spirits are numerous, either prostitute or singing-girl. **Noble Person and Blade-Seal**: One Noble Person positioned correctly; two or three certainly become concubines. Yang Blade combined with Injury Officer brings mixed chaotic affairs. Full chart abundant in Seal certainly harms children. **Two Virtues and Four Pillars**: Two Virtues sitting on Proper Wealth, wealth-nobility naturally arrive. Four Pillars all declining-imprisoned receives imperial honors, blessings, and longevity. **Metal-Water and Four Horses-Four Defeats**: Metal-Water meeting brings beautiful appearance. Yin-Shen-Si-Hai complete indicates solitary promiscuity with glib tongue. Zi-Wu meeting Mao-You certainly follows others. Chen-Xu meeting Chou-Wei is women's way greatest taboo. **Noble-Killing and Wealth-Storehouse**: Two Nobles with one position Killing—powerful family discusses wealth-nobility. If Wealth-Officer hidden in storage, clashing open brings wealth. **Heavenly Stems-Earthly Branches Connection**: Heavenly Stems connected in single character indicate solitary breaking and endless disasters. Earthly characters connected in single character indicate twice marrying and marriage affairs.

- **核心要点**：  
  - 以歌诀形式总结女命判断的数十条速断口诀  
  - 涵盖性情夫身、合化禄马、辰戌杀合、贵人刃印、二德四柱、金水美貌、四马四败等全方位要点  
  - 强调合多主淫、印多损子、辰戌相见淫贱、驿马贵人风尘等女命特殊禁忌  
  - 天干一字连主孤破，地支一字连主两度成婚

- **详细解说**：  《女命总断歌》以歌诀形式汇集女命判断的数十条速断口诀，便于命师快速记忆与应用。全篇可分为几大主题：**性情与夫身**——"择妇须沉静"开篇定调，女命首重性情沉稳；"夫主要强宫，身主要强甚"则强调夫星与日主都需有力。**合化禁忌**——"合绝莫合贵"是女命特殊法则，合入绝地反而无碍，合入贵人反主淫贱；"有杀不怕合，无杀却怕合"区分了有杀制合与无杀多合的不同结果。**地支禁忌**——"辰戌若相见，多是淫贱人"指出辰戌冲克对女命的特殊凶象；"寅申巳亥全"（四马）、"子午逢卯酉"（四败）、"辰戌逢丑未"（四库）齐全皆为女命大忌，主孤淫失节。**神煞与十神**——"驿马带贵人，终久落风尘"是女命特殊凶象；"阳刃带伤官，驳杂事多端"警示刃伤同见；"满盘多是印，损子必须定"点明印多克食伤。**吉格**——"二德坐正财，富贵自然来"为女命大吉配置；"金水若相逢，必招美丽容"主貌美。**干支重叠**——"天干一字连，孤破祸绵绵"主灾厄；"地字连一字，两度成婚事"主再婚。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_236]` `[trigger: 择妇沉静]` `[factor_trigger: nvming AND zefu_chenjing AND fuxing_qiang]` `[role: 主干]` 择妇须沉静，细说与君听；夫主要强宫，身主要强甚。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_237]` `[trigger: 合绝莫合贵]` `[factor_trigger: nvming AND hejue_mohegui AND yinjian AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 合绝莫合贵，此法少人推；女命合入贵人反主淫贱。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_238]` `[trigger: 驿马贵人风尘]` `[factor_trigger: nvming AND yima_guiren AND fengchen AND anchong_qugui AND angui]` `[role: 条件分支]` 驿马带贵人，终久落风尘；女命驿马贵人同柱主风月职业。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_239]` `[trigger: 辰戌相见淫贱]` `[factor_trigger: nvming AND chenxu_xiangjian AND yinjian AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 有辰休见戌，有戌休见辰；辰戌若相见，多是淫贱人。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_240]` `[trigger: 有杀不怕合]` `[factor_trigger: nvming AND yousha_bupa_he AND wusha_pa_he]` `[role: 条件分支]` 有杀不怕合，无杀却怕合；合神若是多，非妓亦讴歌。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_241]` `[trigger: 印多损子]` `[factor_trigger: nvming AND yinshou_duo AND sunzi AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 满盘多是印，损子必须定；印绶过多克制食伤子星。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_242]` `[trigger: 二德坐财富贵]` `[factor_trigger: nvming AND erde_zuocai AND fugui AND anchong_qugui AND angui]` `[role: 条件分支]` 二德坐正财，富贵自然来；天德月德坐财为女命大吉。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_243]` `[trigger: 金水美容]` `[factor_trigger: nvming AND jinshui_xiangfeng AND meirong]` `[role: 条件分支]` 金水若相逢，必招美丽容；金水相生主貌美。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_244]` `[trigger: 四马四败四库禁忌]` `[factor_trigger: nvming AND sima_sibai_siku AND jinji AND guyin]` `[role: 条件分支]` 寅申巳亥全孤淫；子午逢卯酉随人走；辰戌逢丑未妇道大忌。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_245]` `[trigger: 天干地支连]` `[factor_trigger: nvming AND tiangan_yizi AND dizhi_yizi AND hunyin AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 天干一字连，孤破祸绵绵；地字连一字，两度成婚事。 → 《渊海子平·女命总断歌》
  - `[ns_yhzp_246]` `[trigger: 女命总断歌纲领]` `[factor_trigger: nvming AND zongduan_ge AND quanmian_yaodian]` `[role: 总结]` 女命总断歌以歌诀形式汇集女命速断口诀，涵盖夫身合化禁忌地支禁忌神煞十神等全方位要点。 → 《渊海子平·女命总断歌》"""
    normalized_text_zh: str = """"""
    subject: str = "女命总断歌"
    factor_refs: list = ['women_judgment_song', 'multiple_combines_promiscuity', 'abundant_seal_harms_children', 'chen_xu_clash_promiscuity', 'horse']
    
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
        l1_anchor="yhzp_v1.0.0_女命总断歌_001_L1",
    )
    version: str = "1.0.0"
