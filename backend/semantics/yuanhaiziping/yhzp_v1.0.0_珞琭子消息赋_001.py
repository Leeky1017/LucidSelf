"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559578
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
    semantic_id="yhzp_v1.0.0_珞琭子消息赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 珞琭子消息赋(SemanticEntry):
    """
    - **原文（source_text）**：  
  珞琭子消息赋。  
  元一气兮先天，禀清浊兮自然；著三才以为象，播四时以为年。以干为禄，以向背定贫富；以支为命，详顺逆以循环。运行则一辰十载。折...
    """
    
    original_text: str = """- **原文（source_text）**：  
  珞琭子消息赋。  
  元一气兮先天，禀清浊兮自然；著三才以为象，播四时以为年。以干为禄，以向背定贫富；以支为命，详顺逆以循环。运行则一辰十载。折除乃三日为年；折除者乃一年二十四气，七十二候。命有节气浅深，用之而为妙。其为气也，将来者进，成功者退；如蛇在灰，如鳝在尘。气者，四时向背之气也；其为有也，是从无而立有；其为无也，天垂象以为文；此五行临于绝地而建贵也。五行绝处有禄马；其为常也，立仁立义；其为事也，或见或闻。崇为实也，奇为贵也，将星扶德，天乙加临，本主休囚，行藏汩没。至若，勾陈得位，不亏小信以成仁；真武当权，是知大才而分瑞。不仁不义，庚辛与甲乙交争。或是或非，壬癸与丙丁相畏。故，有先贤谦己，处俗求仙；崇释则离宫修定，归道乃水府求玄。见不见之形，无时不有；抽不抽之绪，万古联绵。是以何公惧其七杀；宣父畏以元辰；峨眉阐以三生，无全士庶；鬼谷布其九命，约以星观。今集诸家之要，略其偏见之能，是以未解曲通，妙须神悟。（以下略，原文甚长至4870行，包含大量论命理法则、运程吉凶、神煞应用等内容）


- **分字分词释义**：
  - **元一气兮先天禀清浊兮自然**：元一之气先天而生，禀赋清浊自然形成。
  - **以干为禄以向背定贫富**：天干定禄位，向背定贫富。
  - **以支为命详顺逆以循环**：地支为命基，顺逆循环。
  - **运行则一辰十载**：大运一辰十年。
  - **五行绝处有禄马**：五行临绝地反有禄马。
  - **将星扶德天乙加临**：将星扶德，天乙贵人加临。
  - **勾陈得位不亏小信以成仁**：勾陈得位可成仁。
  - **不仁不义庚辛与甲乙交争**：庚辛甲乙交争主不仁不义。
  - **妙须神悟**：妙法须神悟。
  - **集诸家之要略其偏见之能**：集诸家精要，略去偏见。
- **规范化释义（primary_lang_explained）**：  
  《珞琭子消息赋》为唐代珞琭子所著的命理总论赋文，系统阐述干支阴阳、运程消息、神煞吉凶等命理核心法则，是子平法的重要理论源头之一。**元气先天与三才四时**：元一气兮先天禀清浊自然，著三才为象播四时为年；以干为禄以向背定贫富，以支为命详顺逆循环。**运程与节气**：运行一辰十载，折除三日为年（一年24气72候）；命有节气浅深用之为妙，将来者进成功者退如蛇在灰如鳝在尘。**五行绝处与禄马**：五行临绝地而建贵，五行绝处有禄马；将星扶德天乙加临，本主休囚行藏汩没。**神煞与仁义**：勾陈得位不亏小信成仁，真武当权知大才分瑞；不仁不义庚辛甲乙交争，或是或非壬癸丙丁相畏。**先贤与传承**：何公惧七杀宣父畏元辰，峨眉阐三生鬼谷布九命；集诸家之要略偏见之能，未解曲通妙须神悟。

- **完整对等诠释（secondary_lang_full）**：  
  **Luo-Lu-Zi Message Rhapsody**: A comprehensive destiny principles treatise by Tang dynasty Luo-Lu-Zi, systematically expounding Stem-Branch Yin-Yang, Fortune Path messages, Spirit-Sha fortunes-disasters and other core principles—an important theoretical source for Zi Ping method. **Primal Qi Prior-Heaven and Three Powers Four Seasons**: Primal unified qi of Prior-Heaven receives clear and turbid nature; it manifests as Three Powers taking image, and spreads as Four Seasons forming the year. Using Heavenly Stems as salary, using facing-backing to determine poverty-wealth; using Earthly Branches as fate, detailing harmonious and contrary circulation. **Fortune Path and Solar Terms**: Fortune travels one Chen (Earthly Branch) for ten years; reducing three days makes one year (one year has 24 terms and 72 periods). Fate has solar terms shallow and deep; using this properly is wonderful. What comes advances, what is accomplished retreats—like a snake moving through ashes, like an eel moving through dust. **Five Elements Extinction and Salary-Horse**: When Five Elements arrive at extinction positions, they establish nobility; where Five Elements are extinct, there exists salary-horse. General Star supports virtue, Tianyi adds its presence; root-master declining-imprisoned, conduct-storage submerged. **Spirit-Sha and Benevolence-Righteousness**: Gouchen gaining position does not lose small trust and achieves benevolence; Zhenwu holding authority knows great talent and distinguishes auspiciousness. Not benevolent and not righteous: Geng-Xin and Jia-Yi contest; or this or that: Ren-Gui and Bing-Ding fear each other. **Predecessors and Transmission**: Master He feared Seven Killings, Master Xuan feared Yuan Chen; Emei expounded Three Lives, Guigu arranged Nine Fates. Collecting the essentials from various schools, omitting partial biased abilities—if not comprehending through flexible understanding, wonderfulness requires divine insight.

- **核心要点**：  
  - 唐代珞琭子命理总论赋文，为子平法重要理论源头  
  - 系统阐述干支阴阳、运程消息、节气深浅、五行绝处禄马等核心法则  
  - 强调神煞应用（勾陈真武、将星天乙、七杀元辰等）与仁义吉凶  
  - 集诸家之要，强调"未解曲通妙须神悟"的灵活运用

- **详细解说**：  《珞琭子消息赋》为唐代珞琭子命理总论。**元气先天**——"元一气兮先天，禀清浊兮自然"揭示先天元气之源。**干支定位**——"以干为禄，以向背定贫富；以支为命，详顺逆以循环"确立干支核心地位。**运程节气**——"运行则一辰十载"；"命有节气浅深，用之而为妙"阐述运程与节气的应用。**五行绝处**——"五行临于绝地而建贵也；五行绝处有禄马"揭示绝处逢生之理。**神煞仁义**——"勾陈得位，不亏小信以成仁"；"不仁不义，庚辛与甲乙交争"阐述神煞与仁义的关系。**传承神悟**——"集诸家之要，略其偏见之能；未解曲通，妙须神悟"点明传承与神悟的重要。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_507]` `[trigger: 元气先天]` `[factor_trigger: yuan_yiqi_xiantian AND bin_qingzhuo_ziran]` `[role: 主干]` 元一气兮先天禀清浊兮自然；先天元气之源。 → 《渊海子平·珞琭子消息赋》
  - `[ns_yhzp_508]` `[trigger: 干支定位]` `[factor_trigger: gan_weilu AND xiangbei_ding_pinfu AND zhi_weiming AND shunni_xunhuan]` `[role: 主干依赖]` 以干为禄以向背定贫富；以支为命详顺逆以循环。 → 《渊海子平·珞琭子消息赋》
  - `[ns_yhzp_509]` `[trigger: 运程节气]` `[factor_trigger: yunxing_yichen_shizai AND jieqi_qianshen_weimiao]` `[role: 条件分支]` 运行则一辰十载；命有节气浅深用之而为妙。 → 《渊海子平·珞琭子消息赋》
  - `[ns_yhzp_510]` `[trigger: 五行绝处]` `[factor_trigger: wuxing_lin_juedi_jiangui AND juechu_you_luma AND juechu_fengsheng AND anchong_qugui]` `[role: 条件分支]` 五行临于绝地而建贵；五行绝处有禄马；绝处逢生。 → 《渊海子平·珞琭子消息赋》
  - `[ns_yhzp_511]` `[trigger: 神煞仁义]` `[factor_trigger: gouchen_dewei_chengren AND buren_buyi_gengxin_jiayi_zhengzheng AND chengren AND gouchen_dewei AND gengxin_jiayi]` `[role: 条件分支]` 勾陈得位不亏小信以成仁；不仁不义庚辛与甲乙交争。 → 《渊海子平·珞琭子消息赋》
  - `[ns_yhzp_512]` `[trigger: 妙须神悟]` `[factor_trigger: ji_zhujia_zhiyao AND lue_pianjian AND weijie_qutong_miaoxu_shenwu]` `[role: 总结]` 集诸家之要略其偏见之能；未解曲通妙须神悟。 → 《渊海子平·珞琭子消息赋》"""
    normalized_text_zh: str = """"""
    subject: str = "珞琭子消息赋"
    factor_refs: list = ['luoluzi_rhapsody', 'fold_reduce_calculation', 'extinction_salary_horse', 'general_star_tianyi', 'divine_understanding']
    
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
        l1_anchor="yhzp_v1.0.0_珞琭子消息赋_001_L1",
    )
    version: str = "1.0.0"
