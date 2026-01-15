"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559410
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
    semantic_id="yhzp_v1.0.0_络绎赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 络绎赋(SemanticEntry):
    """
    - **原文（source_text）**：
  参天地之奥妙，测造化之幽微，别人生之贵贱，取法则于干支；决生死之吉凶，推得失之玄妙。
  甲乙之木，最喜春生。
  壬癸之水，偏宜冬旺。
  丙丁火而...
    """
    
    original_text: str = """- **原文（source_text）**：
  参天地之奥妙，测造化之幽微，别人生之贵贱，取法则于干支；决生死之吉凶，推得失之玄妙。
  甲乙之木，最喜春生。
  壬癸之水，偏宜冬旺。
  丙丁火而夏明。
  庚辛金而秋锐。
  戊己两干之土，要旺四季之期。
  日乃自身，须究强弱。
  年为本主，宜细推详。
  年干父兮支母。日干己兮支妻。月干兄兮支弟。时支女兮干儿。
  后杀克年，父母早丧。
  前杀克后，子息必亏。
  马入妻宫，必得能家之妇。
  杀临子位，必招悖逆之儿。
  禄入妻宫，食妻之禄。
  印临子位，受子之荣。
  枭居子位，破祖之基。
  财官月旺，得父赀财。
  所忌，财伤禄薄。最嫌，鬼旺身衰。
  原其，克彼为财，生我为印。
  食神暗见，人物丰肥。
  枭印重生，祖财漂荡。
  咸池财露，主淫奢。
  凶杀合年，防自刃。
  土克水，而成腹脏之疾。
  火锻金，以患痨瘵之灾。
  桃花会禄，酒色亡身。
  财旺身衰，因财丧命。
  观乎，财生官者，用贿求官；财坏印者，贪财卸职。
  财旺生官，自身荣显。
  财生杀党，夭折童年。
  独杀冲破，废闲人。
  诸杀逢刑，凶狠辈。
  天干多兮，见干年须当夭折。
  地支多兮，见支年必见凶灾。
  财生官，官生印，印生身，富贵双全。
  干党财，财党杀，杀攻身，凶穷两逼。
  酉寅刑害继伤婚。
  丑卯风雷多性急。
  杀官混杂，乃技艺之流。
  财禄生马，为经商之客。
  马落空亡，迁居飘流。
  禄遭冲破，别土离乡。
  阴多利于女人。阳盛宜于男子。
  阴盛于阳，主女兴家。阳胜于阴，男当建府。
  纯阳，则男必孤寒。纯阴，则女当寡困。
  官贵生年，伏凶煞而名垂万古。
  贵宜乎多。禄宜乎少。
  绝虑忘思，无差无误！

- **分字分词释义**：
  - **参天地之奥妙测造化之幽微**：参悟天地奥秘，测度造化玄机。
  - **甲乙之木最喜春生**：甲乙木日主喜春月得令。
  - **年干父兮支母日干己兮支妻**：年干代表父亲，年支代表母亲；日干代表自己，日支代表妻子。
  - **马入妻宫必得能家之妇**：日支坐驿马，主妻子能干。
  - **禄入妻宫食妻之禄**：日支坐禄神，主依靠妻财。
  - **财生官官生印印生身富贵双全**：财官印顺生至身，主富贵。
  - **干党财财党杀杀攻身凶穷两逼**：比劫生财、财生杀、杀克身，主凶穷。
  - **纯阳则男必孤寒纯阴则女当寡困**：八字全阳男孤，全阴女寡。
  - **阴多利于女人阳盛宜于男子**：阴气重利女性，阳气盛利男性。

- **规范化释义（primary_lang_explained）**：
  本篇名为《络绎赋》，意指命理法则如丝缕般络绎不绝、条理分明。主要论述了六亲推断、身体疾病、性情职业等方面：
  - **五行四时**：重申木喜春、火喜夏等得时得地原则。
  - **六亲定位**：
    - **年干/支**：父/母。杀克年主父母早丧。
    - **日干/支**：己/妻。马入妻宫（日支坐驿马）主妻能干。禄入妻宫主食妻财。
    - **月干/支**：兄/弟。
    - **时干/支**：子/女。杀临子位主子悖逆。印临子位主得子荣。
  - **身体与灾祸**：土克水主腹脏疾，火克金主肺痨。桃花会禄主酒色亡身。凶杀合年防自杀（自刃）。
  - **财官印流转**：
    - **良性循环**：财生官、官生印、印生身（富贵双全）。
    - **恶性循环**：干党财、财党杀、杀攻身（凶穷两逼）。
  - **阴阳平衡**：男宜阳盛，女宜阴多。纯阳孤寒，纯阴寡困。

- **完整对等诠释（secondary_lang_full）**：
  **Continuous Ode (Luo Yi Fu)**:
  - **Seasonal Strength**: Wood loves Spring, Water loves Winter, Fire bright in Summer, Metal sharp in Autumn, Earth prosperous in Four Seasons.
  - **Relations (Six Kins)**:
    - **Year Stem/Branch**: Father/Mother. Killing attacking Year = Early loss of parents.
    - **Day Stem/Branch**: Self/Wife. Horse in Wife Palace = Capable wife. Salary in Wife Palace = Living off wife's wealth.
    - **Month**: Siblings. **Hour**: Children. Killing in Hour = Rebellious children. Seal in Hour = Glory from children.
  - **Health & Calamity**: Earth controlling Water = Abdominal/Visceral disease. Fire forging Metal = Tuberculosis/Lung disease. Peach Blossom meeting Salary = Ruin via alcohol/lust.
  - **Cycle of Fortune**:
    - **Auspicious**: Wealth generates Officer -> Officer generates Seal -> Seal generates Self.
    - **Inauspicious**: Stems support Wealth -> Wealth supports Killing -> Killing attacks Self (Poverty & Disaster).
  - **Yin/Yang Balance**: Men favor Yang, Women favor Yin. Pure Yang = Men solitary/poor. Pure Yin = Women widowed/distressed.

- **核心要点**：
  - **六亲宫位法**：年父母、月兄弟、日夫妻、时子女
  - **生克循环**：财官印顺生为吉，财党杀攻身为凶
  - **五行病理**：根据五行相克推断脏腑疾病（水肾/土脾胃/金肺）
  - **阴阳调和**：纯阴纯阳均为偏枯，贵在阴阳得所

- **详细解说**：  《络绎赋》以络绎不绝为喻，阐述命理法则如丝缕般条理分明。开篇"参天地之奥妙，测造化之幽微"定调命学的深邃。**五行四时**——"甲乙之木最喜春生"等重申得时得地之法。**六亲宫位**——"年干父兮支母，日干己兮支妻，月干兄兮支弟，时支女兮干儿"，确立四柱六亲定位法则；"马入妻宫必得能家之妇"主妻能干，"禄入妻宫食妻之禄"主食妻财。**生克循环**——"财生官，官生印，印生身，富贵双全"为良性循环；"干党财，财党杀，杀攻身，凶穷两逼"为恶性循环。**阴阳平衡**——"纯阳则男必孤寒，纯阴则女当寡困"，揭示阴阳偏枯之害；"阴盛于阳主女兴家，阳胜于阴男当建府"为得所之象。末句"绝虑忘思，无差无误"点明论命需专注。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_704]` `[trigger: 五行四时]` `[factor_trigger: wuxing_sishi AND deshi_dedi]` `[role: 主干]` 甲乙之木最喜春生；壬癸之水偏宜冬旺；五行得时法则。 → 《渊海子平·络绎赋》
  - `[ns_yhzp_705]` `[trigger: 六亲宫位]` `[factor_trigger: liuqin_gongwei AND nian_yue_ri_shi_dingwei AND nian_yue_ri_shi]` `[role: 主干]` 年干父兮支母，日干己兮支妻，月干兄兮支弟，时支女兮干儿。 → 《渊海子平·络绎赋》
  - `[ns_yhzp_706]` `[trigger: 马入妻宫]` `[factor_trigger: maru_qigong AND nengjia_fu AND shiqilu]` `[role: 条件分支]` 马入妻宫必得能家之妇；禄入妻宫食妻之禄。 → 《渊海子平·络绎赋》
  - `[ns_yhzp_707]` `[trigger: 财官印顺生]` `[factor_trigger: caisheng_guan_yinsheng_shen AND fugui_shuangquan AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 财生官官生印印生身富贵双全；良性循环主吉。 → 《渊海子平·络绎赋》
  - `[ns_yhzp_708]` `[trigger: 财党杀攻身]` `[factor_trigger: caidangsha_shagongshen AND xiongqiong_liangbi]` `[role: 例外处理]` 干党财财党杀杀攻身凶穷两逼；恶性循环主凶。 → 《渊海子平·络绎赋》
  - `[ns_yhzp_709]` `[trigger: 纯阴纯阳]` `[factor_trigger: chunyang_nan_guhan AND chunyin_nv_guakun AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 纯阳则男必孤寒，纯阴则女当寡困；阴阳偏枯之害。 → 《渊海子平·络绎赋》
  - `[ns_yhzp_710]` `[trigger: 络绎赋纲领]` `[factor_trigger: luoyi_fu AND liuqin_gongwei AND shengke_xunhuan AND yinyang_tiaohe AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 总结]` 络绎赋以六亲宫位、生克循环、阴阳调和为核心，论命如丝缕络绎分明。 → 《渊海子平·络绎赋》"""
    normalized_text_zh: str = """"""
    subject: str = "络绎赋"
    factor_refs: list = ['continuous_ode', 'wealth_partisan_killing', 'yin', 'horse_wife_palace']
    
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
        l1_anchor="yhzp_v1.0.0_络绎赋_001_L1",
    )
    version: str = "1.0.0"
