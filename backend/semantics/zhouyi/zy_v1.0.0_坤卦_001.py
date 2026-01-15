"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899697
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
    semantic_id="zy_v1.0.0_坤卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 坤卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  坤：元亨，利牝马之贞。君子有攸往，先迷后得，主利。西南得朋，东北丧朋，安贞吉。

  【爻辞】
  初六，履霜，坚冰至。
  六二，直...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  坤：元亨，利牝马之贞。君子有攸往，先迷后得，主利。西南得朋，东北丧朋，安贞吉。

  【爻辞】
  初六，履霜，坚冰至。
  六二，直方大，不习无不利。
  六三，含章可贞；或从王事，无成有终。
  六四，括囊，无咎无誉。
  六五，黄裳，元吉。
  上六，龙战于野，其血玄黄。
  用六，利永贞。

  【彖传】
  《彖》曰：至哉坤元！万物资生，乃顺承天。坤厚载物，德合无疆；含弘光大，品物咸亨。
  牝马地类，行地无疆，柔顺利贞。
  君子攸行，先迷失道，后顺得常。
  西南得朋，乃与类行；东北丧朋，乃终有庆。
  安贞之吉，应地无疆。

  【象传】
  《象》曰：地势坤，君子以厚德载物。

  【文言】
  《文言》曰：坤至柔而动也刚，至静而德方。后得主而有常，含万物而化光。
  坤道其顺乎！
  承天而时行。
  积善之家，必有余庆；积不善之家，必有余殃。
  臣弑其君，子弑其父，非一朝一夕之故，其所由来者渐矣！
  由辩之不早辩也。
  《易》曰：“履霜，坚冰至”，盖言顺也。
  “直”其正也，“方”其义也。君子敬以直内，义以方外，敬义立而德不孤。“直方大，不习无不利”，则不疑其所行也。
  阴虽有美，含之以从王事，弗敢成也。地道也，妻道也，臣道也。地道无成而代有终也。
  天地变化，草木蕃；天地闭，贤人隐。《易》曰：“括囊，无咎无誉。”盖言谨也。
  君子黄中通理，正位居体，美在其中，而畅于四支，发于事业，美之至也。
  阴疑于阳必战。为其嫌于无阳也，故称“龙”焉；犹未离其类也，故称“血”焉。夫玄黄者，天地之杂也，天玄而地黄。

- 分字分词释义：

  - 坤：卦名，象地，性柔顺、承载、包容，为纯阴之卦。
  - 元亨：坤道亦有始与通，偏重“资生”与“咸亨”。
  - 牝马：母马，比喻顺从、坚实、耐久之德，为地类。
  - 利牝马之贞：有利于如牝马般柔顺坚贞的持守。
  - 有攸往：有所往行，有要去之处。
  - 先迷后得：先有迷惑失措，后得所当得、得其常。
  - 西南得朋：西南为坤方，得与类行，得朋党助。
  - 东北丧朋：东北为艮、艮中有止，远离同类之处。
  - 安贞吉：安于守贞而不躁动，自然吉祥。
  - 地势坤：地之形势厚重而广阔。
  - 厚德载物：以深厚之德承载万物。
  - 至柔而动也刚：静态极柔，发动时却能坚刚。
  - 后得主而有常：坤道在乾之后得其主位，而能守恒常。
  - 履霜坚冰：由霜而至冰，比喻渐进之征兆与结果。
  - 直方大：正直、端方、广大。
  - 含章可贞：内含文采、美德，足以守贞。
  - 括囊：收束言行，如系口袋之口。
  - 黄裳：黄色下裳，中和之色，处下而守中。
  - 龙战于野：阴与阳战于野外，象阴极而与阳争。
  - 玄黄：天玄地黄，阴阳杂揉之色。
  - 利永贞：利于长久坚守正道。

- **规范化释义（primary_lang_explained）**：

  坤卦象征大地，纯阴之气，特性在于厚重、柔顺、承载与包容。卦辞说：坤也有起始、有通达，但它所利的是像牝马那样的柔顺坚贞。君子有所往行时，若走在前面容易先迷失方向，顺从而行则终能获得常道之所归。向西南（坤方）则能得同类之朋，向东北则会失去同伴，但最终反而有喜庆；只要安处守贞，就能吉祥。

  彖传进一步说明坤道：大地之元德在于使万物得以生长，以顺承天道为职。坤厚载万物，其德与天地无疆，包容宏广而又光明广大，因此使万物都能通达。“牝马地类”一语，以母马比喻大地：行走于地而无疆，性情柔顺而利于守贞。君子在世间行事，若轻率在前，必先迷而后得；若顺应天道与地道，则终能得其常。西南得朋，是说趋向坤方而与同类同行；东北丧朋，是说远离同类但可终得其庆。安于守贞之吉，与大地无疆之德相应。

  象传以“地势坤，君子以厚德载物”一句，为坤卦定下君子之道：君子应以大地为法，以厚重广大的德行包容承载万物，而不急于自我彰显。文言则从性情上剖析坤：它在静态中极致柔顺，但一旦承担起现实事务，其行动必须刚健而有方。这里的“刚”不同于乾的“刚健主动”，而是“在担当时不退缩”“在执行时有准绳”的刚。故又曰“地道也，妻道也，臣道也”：坤道代表的是在支持与承载位置上的责任伦理。

  文言中还通过“履霜坚冰至”“积善之家必有余庆”等语，强调事物的发展有渐进之理：霜积而成冰，善积而有余庆，恶积而有余殃；臣弑君、子弑父等极端之恶，并非一朝一夕之故，而是没有及早辨别、渐渐发展而成的结果。坤卦借此示人：顺承天道与人伦，需要从细微处谨慎防范。

  各爻则表现坤道在不同位置的德行：初六“履霜，坚冰至”，提醒从细微征兆预见将来的严重后果；六二“直方大，不习无不利”，强调以正直、方正、广大为德，即使不刻意学习也不会有不利；六三“含章可贞；或从王事，无成有终”，阴虽有美，宜内含以辅君，不敢自成其功；六四“括囊，无咎无誉”，在闭塞之世收束言行，以谨慎避免祸患；六五“黄裳，元吉”，居中守下，内美而不外耀，故元吉；上六“龙战于野，其血玄黄”，阴极疑阳而战，终致天地玄黄混杂，象征阴道穷极之危。用六“利永贞”，总结坤道在于长久守贞，以柔顺之德承担终结与转化。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Kun, "The Receptive" or "Earth", represents pure yin energy and embodies the qualities of flexibility, receptivity, and supportive capacity. Kun is not the opposite of Qian but rather its complement and bearer. While Qian initiates and commands, Kun receives and nourishes, emphasizing the responsibilities of "generating life", "following in accordance", and "carrying with thickness". Thus the key terms for Kun are "yielding, thick, containing, and completing": yielding to Heaven's timing, carrying all with thick virtue, containing all things, and acting on behalf of Heaven to bring completion.

The Judgment's phrase "favorable through the steadfastness of a mare" clarifies a common misconception: Kun is not merely weak, but like a mare has strength, endurance, and capacity for long journeys, yet its strength lies in yielding, in patience, in lasting duration, not in争先 competing to be first. If a noble person acts according to the Way of Kun, they should not rush ahead of Qian's timing; thus "the noble person has somewhere to go: first confused, later obtains" reminds them not to rush ahead but to follow in accordance, only then obtaining the constant Way.

The Tuan explains that "Kun's thickness carries things, virtue harmonizes without boundary; containing grandly and radiating broadly, all beings flourish accordingly", describing Kun's "thickness" and "breadth" to the utmost: the Earth does not select what it carries but embraces all with boundless virtue.

- 核心要点：

  - 坤卦象地，以柔顺、承载、包容为德，其道在“顺承天”与“厚德载物”。
  - “利牝马之贞”点明坤道适宜柔顺坚贞、坚韧耐久的行事方式，而不在创制与领首。
  - 卦辞与彖传通过“西南得朋，东北丧朋”“先迷后得”等语，强调君子应知趋向与时位，顺势而行而不过度逞强。
  - 各爻呈现坤道的渐进与守分：从履霜识冰，到含章辅君、括囊谨慎、黄裳居中，再到阴极与阳战，警示阴柔若失其度亦会走向极端。

- 详细解说：

  与乾卦相比，坤卦并非乾之对立，而是乾之配与承。乾为天，主始与主统；坤为地，主生与主承。乾以“元亨利贞”开出积极进取的结构，而坤在承接乾道后，强调自身的职责是“资生”“顺承”与“厚载”。因此，坤卦的关键词是“顺、厚、含、终”：顺天之时、厚德载物、含容万物、代天而为终。

  卦辞“利牝马之贞”，澄清了一种常见误解：坤并非一味柔弱，而是如牝马般有力量、有耐力、能远行，但其强在顺、在忍、在持久，不在争先。君子若以坤道行事，就不能抢在乾道之前去领首；所以“君子有攸往，先迷后得”提醒君子不要抢先于时，而应该顺承之后，才能获得常道。

  彖传中“坤厚载物，德合无疆；含弘光大，品物咸亨”，将坤的“厚”与“广”写至极致：大地并不挑拣所承载的事物，而是以无疆之德包容一切；这一点对于命理与解梦而言，提示我们：坤象往往与“承受”“包容”“载负”“环境与土壤”有关，而不是简单的“消极顺从”。

  文言中“坤至柔而动也刚，至静而德方”则揭示坤道的另一面：在静态中，坤保持柔顺与承受；一旦承担起现实事务，其行动必须刚健而有方。这里的“刚”不同于乾的“刚健主动”，而是“在担当时不退缩”“在执行时有准绳”的刚。故又曰“地道也，妻道也，臣道也”：坤道代表的是在支持与承载位置上的责任伦理。

  爻辞则从微兆与渐变着笔：初六“履霜，坚冰至”告诉我们任何极端结果，皆始于细微征兆，这与文言中“臣弑其君，子弑其父，非一朝一夕之故”互为表里。六二“直方大，不习无不利”，是坤卦中最典型的“正位中”之象：以正直、方正、广大为德，即使不多言、不多学，也不至于有害。六三“含章可贞；或从王事，无成有终”，强调阴柔应辅君而不自成其功，是坤道“以成全他者”为高境界的一种表达。六四“括囊，无咎无誉”，则提醒在时势险恶而言语易招祸时，收束自己反而是最合宜的谦退。六五“黄裳，元吉”，通过“黄中之色 + 在下之裳”结合，说明中和而居下的美德。上六“龙战于野，其血玄黄”，是坤道走向极端时的警示：当阴疑阳而争战，就会出现天地玄黄混杂的失衡状态，此时已非坤之正德。

  最后，“用六，利永贞”总结坤道的成就方式：坤并不在于一时之功，而在于长久守贞的恒常之德。与乾之“用九，见群龙无首，吉”相比，乾强调群贤共治、无一人独尊；坤则强调持守岗位、以柔顺恒常作为成全乾道的方式。二者相配，才构成《周易》宇宙与人格结构的根基。"""
    normalized_text_zh: str = """"""
    subject: str = "坤卦（䷁）"
    factor_refs: list = ['zhouyi_trigram_kun', 'zhouyi_li_pinma_zhen', 'zhouyi_houde_zaiwu', 'zhouyi_xinan_dongbei_peng', 'zhouyi_lvshuang_jianbing', 'zhouyi_huangchang', 'zhouyi_longzhan_yuye']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_坤卦_001_L1",
    )
    version: str = "1.0.0"
