"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899662
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
    semantic_id="zy_v1.0.0_乾卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 乾卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  乾：元，亨，利，贞。

  【爻辞】
  初九，潜龙勿用。
  九二，见龙在田，利见大人。
  九三，君子终日乾乾，夕惕若厉，无咎。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  乾：元，亨，利，贞。

  【爻辞】
  初九，潜龙勿用。
  九二，见龙在田，利见大人。
  九三，君子终日乾乾，夕惕若厉，无咎。
  九四，或跃在渊，无咎。
  九五，飞龙在天，利见大人。
  上九，亢龙有悔。
  用九，见群龙无首，吉。

  【彖传】
  《彖》曰：大哉乾元！万物资始，乃统天。云行雨施，品物流形。
  大明终始，六位时成，时乘六龙以御天。
  乾道变化，各正性命，保合大和，乃利贞。
  首出庶物，万国咸宁。

  【象传】
  《象》曰：天行健，君子以自强不息。
  “潜龙勿用”，阳在下也；
  “见龙在田”，德施普也；
  “终日乾乾”，反复道也；
  “或跃在渊”，进无咎也；
  “飞龙在天”，大人造也；
  “亢龙有悔”，盈不可久也；
  “用九”，天德不可为首也。

  【文言】
  《文言》曰：元者，善之长也；亨者，嘉之会也；利者，义之和也；贞者，事之干也。
  君子体仁足以长人，嘉会足以合礼，利物足以和义，贞固足以干事。
  君子行此四德者，故曰：“乾：元，亨，利，贞。”

  初九曰“潜龙勿用”，何谓也？子曰：“龙德而隐者也。
  不易乎世，不成乎名；遁世无闷，不见是而无闷；乐则行之，忧则违之，确乎其不可拔，‘潜龙’也。”

  九二曰“见龙在田，利见大人”，何谓也？子曰：“龙德而正中者也。
  庸言之信，庸行之谨；闲邪存其诚，善世而不伐，德博而化。
  《易》曰：‘见龙在田，利见大人’，君德也。”

  九三曰“君子终日乾乾，夕惕若厉，无咎”，何谓也？
  子曰：“君子进德修业。
  忠信，所以进德也；修辞立其诚，所以居业也。
  知至至之，可与几也；知终终之，可与存义也。
  是故居上位而不骄，在下位而不忧。
  故乾乾因其时而惕，虽危无咎矣。”

  九四曰“或跃在渊，无咎”，何谓也？子曰：“上下无常，非为邪也；进退无恒，非离群也。君子进德修业，欲及时也，故‘无咎’。”

  九五曰“飞龙在天，利见大人”，何谓也？子曰：“同声相应，同气相求；水流湿，火就燥；云从龙，风从虎；圣人作而万物睹；本乎天者亲上，本乎地者亲下，则各从其类也。”

  上九曰“亢龙有悔”，何谓也？子曰：“贵而无位，高而无民，贤人在下位而无辅，是以动而‘有悔’也。”

  “潜龙勿用”，下也；
  “见龙在田”，时舍也；
  “终日乾乾”，行事也；
  “或跃在渊”，自试也；
  “飞龙在天”，上治也；
  “亢龙有悔”，穷之灾也；
  乾元“用九”，天下治也。

  “潜龙勿用”，阳在下也；
  “见龙在田”，天下文明；
  “终日乾乾”，与时偕行；
  “或跃在渊”，乾道乃革；
  “飞龙在天”，乃位乎天德；
  “亢龙有悔”，与时偕极；
  乾元“用九”，乃见天则。

  “乾，元”者，始而亨者也；“利，贞”者，性情也。
  乾始能以美利利天下，不言所利，大矣哉！
  大哉乾乎，刚健中正，纯粹精也；六爻发挥，旁通情也；时乘六龙，以御天也；云行雨施，天下平也。

  君子以成德为行，日可见之行也。“潜”之为言也，隐而未见，行而未成，是以君子弗用也。
  君子学以聚之，问以辩之，宽以居之，仁以行之。《易》曰“见龙在田，利见大人”，君德也。

  九三重刚而不中，上不在天，下不在田，故乾乾因其时而惕，虽危无咎矣。
  九四重刚而不中，上不在天，下不在田，中不在人，故“或”之。“或”之者，疑之也，故无咎。

  夫“大人”者，与天地合其德，与日月合其明，与四时合其序，与鬼神合其吉凶。
  先天而天弗违，后天而奉天时。
  天且弗违，而况于人乎？
  况于鬼神乎？

  “亢”之为言也，知进而不知退，知存而不知亡，知得而不知丧。其唯圣人乎，知进退存亡，而不失其正者，其唯圣人乎！

- 分字分词释义：
  - 乾：卦名，象天，性刚健、主动、上行，为纯阳之卦。
  - 元：开始、根本之德，发端之意，为四德之首。
  - 亨：通达、顺遂、发展之意。
  - 利：有利、适宜，强调合乎义理的利益。
  - 贞：正固不变、专一守正，也指正当的占问与立场。
  - 潜龙：具备大德而暂时隐伏不出之人或之时。
  - 见龙在田：德行显露于世间而能施泽于民。
  - 终日乾乾：整日自我砥砺、勤勉不懈。
  - 夕惕若厉：在夜间仍保持警惕，如临危境。
  - 或跃在渊：或上或下，试跃未定，处进退之间。
  - 飞龙在天：大德已显、居高位而行其道。
  - 亢龙：亢极之龙，指过高、过满而将有损之势。
  - 见群龙无首：众龙并列而无一居首，比喻群贤共治、无专断之君。
  - 资始：资助万物之初始，提供发生之根源。
  - 各正性命：使万物各得其性，各安其命。
  - 保合大和：保任而调和天地间的大和之气。
  - 天行健：天道运行刚健不息。
  - 自强不息：君子法天之健，自我砥砺而不懈怠。
  - 善之长：善德之首、百善之先。
  - 嘉之会：美好事物的聚会与成就。
  - 义之和：合乎义理而能调和众事。
  - 事之干：事情的主干、纲领。
  - 进德修业：内在增进德行，外在修治事业。
  - 本乎天者亲上、本乎地者亲下：各随其类而向其根源靠拢。
  - 知进退存亡：能知什么时候前进、后退、生、亡，而不失其中正。

- **规范化释义（primary_lang_explained）**：
  乾卦象征天，纯阳之气，具有刚健、主动、上行的特性。卦辞“元、亨、利、贞”四字，概括了乾道的四种德性：元是开始与根本，亨是通达与发展，利是合乎义理的利益，贞是守正不移的坚定。君子若能体仁立义、和物利事、坚守正道，就能体现乾卦之四德。

  六爻以“龙”的不同状态来比喻君子随时位而进退变化的过程：初九为潜龙，指德行已具但时机未至，应当隐伏不出，不为名利所动；九二为见龙在田，德行显露于世间，利于与大人相会、施德于民；九三为终日乾乾，处势不中、上下未定，必须整日自勉、夜间警惕，以免陷于危机；九四为或跃在渊，在上升与停留之间试探进退，非邪非离群，只是欲及时而不失其道；九五为飞龙在天，居尊位而与天地日月四时相应，是大人用事之时；上九为亢龙有悔，处于极高之位而过满，易致失衡与悔恨。

  彖传从宇宙论层面描写乾元之大：乾为万物资始，统御于天，道气运行如云行雨施，使万物生成变化。六爻循时而成位，犹如乘六龙以御天，说明乾道随时位而变化，使万物性命各正，并保合宇宙间的大和，故利于守贞。象传以“天行健，君子以自强不息”一句，确立了乾卦对君子的根本要求：效法天道刚健不息，自我砥砺而不懈怠。文言则细致阐发元亨利贞四德，说明君子如何在具体德行与事业上实现乾道。

  整体而言，乾卦展示的是“以天道为法”的人格与秩序：圣人与大人能与天地合德、与日月合明、与四时合序、与鬼神合同其吉凶，因此能知进退存亡而不失其正。凡执于一端、只知进而不知退、只知存而不知亡者，则为“亢”，终有悔恨之道。这也是乾卦以六龙之象反复提醒的核心。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Qian, "The Creative" or "Heaven", represents pure yang energy and embodies the qualities of strength, initiative, and upward movement. The Judgment's four phrases—"yuan, heng, li, zhen" (originating, success, advantage, steadfastness)—encapsulate the four virtues of the Creative Way: yuan is beginning and foundation, heng is development and flow, li is benefit aligned with righteousness, and zhen is steadfast correctness. When a noble person embodies benevolence, harmonizes with ritual propriety, benefits all things appropriately, and remains firmly upright, they manifest these four virtues.

The six lines use the dragon in different states to illustrate how the noble person progresses and retreats according to time and position: the first line shows the hidden dragon—virtue is complete but timing is not yet right, so one should remain concealed; the second line shows the dragon appearing in the field—virtue becomes visible in the world, favorable for meeting great persons and extending benefit to the people; the third line emphasizes constant diligence throughout the day and vigilance at night to avoid danger; the fourth line represents hesitation between leaping upward or remaining in the abyss, testing advancement while staying true to the Way; the fifth line shows the flying dragon in the heavens—occupying the honored position and harmonizing with Heaven, Earth, sun, moon, and the four seasons; the top line warns of the dragon at its height having regret—being at the extreme height and overflowing leads to imbalance and remorse.

- 核心要点：
  - 乾卦为纯阳之天，道性在于刚健不息，要求君子“自强不息”。
  - “元、亨、利、贞”四德构成乾道的完整结构：由始而通，由通而利，由利而守正。
  - 六龙各爻描写君子随时位而变化的进退之道：从潜伏、初显、勤勉、试跃、飞腾到亢极，提醒防止过与不及。
  - 圣人之所以能无悔，在于能知进退存亡而不失其中正，与天地日月四时同其秩序。

- 详细解说：
  卦辞“乾：元，亨，利，贞”看似四个并列的判断，文言中却将其解释为一个结构化的过程：元为始、为善之长，是一切德性的根基；亨为通，为嘉会之时，是元德在具体事物中的展开；利为义之和，是在诸多关系与利益中保持合乎义理的调和；贞为事之干，是最后在具体实践中坚守不变的主干。君子若能体仁、合礼、和义、干事，即是在人格与实践层面落实乾之四德。

  六爻的龙象，将“德业充实”与“时位合宜”两条线交织在一起：初九潜龙，强调在德已具而名未成之时，应当不易于世、不成乎名，宁可遁世无闷，也不为时尚所摇动；九二见龙在田，是德行开始施于人世之时，要求“庸言之信、庸行之谨”，在日常言行中体现诚信与谨慎；九三处位不中，上不在天、下不在田，更需“终日乾乾、夕惕若厉”，用高度自律来避免身处险位时的危机；九四进退未定，“或跃在渊”，非邪非离群，而是因时试跃、以便及时行道；九五飞龙在天，是乾道最光明的时刻，人与天地日月四时、鬼神吉凶相应；上九亢龙，则是对“过满”的告诫——若只知进不知退，只知存不知亡，只知得不知丧，则必致“有悔”。

  彖传与后文言段落，将这种人格修养与宇宙秩序打通：乾元为万物资始，云行雨施使品物流形，六爻因时而成位，如乘六龙御天。君子若能以成德为行、日可见之行，并通过学习、发问、宽厚、仁行使德业充实，则其行动可以“先天而天弗违，后天而奉天时”。天且不违之，人何以违之？这正是“大人”之所以能与天地合德者。

- **校勘与字词辨析（双语）**：
  - **中文**：本稿据项目内王弼注本为底本，行文中仅调整标点与少量引号形式，以便现代阅读；经文用字不做随意改动。"乾：元，亨，利，贞"一语，在通行本中写法基本一致，本稿保留原字序与四字结构。"天行健，君子以自强不息"保留"健"字而不改作"健行"等现代误写。"乾乾"作连绵字表示持续勤勉。"亢龙有悔"中"亢"释为"高亢、过极"，统一理解为"过满不知退"。
  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original character forms. "Qian: Yuan, Heng, Li, Zhen" follows standard editions. "Tian Xing Jian" retains "Jian" without modern corruptions. "Qian Qian" kept as reduplicative compound. "Kang Long" interpreted as "excess without retreat."

- **叙事素材（narrative_snippets）**：

  - `[ns_zhouyi_001]` `[trigger: 卦=乾 AND 卦辞]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_guaci]` `[role: 主干]` 乾：元，亨，利，贞。万物资始，乃统天。 → 《周易·乾卦·卦辞》
  - `[ns_zhouyi_002]` `[trigger: 卦=乾 AND 初九]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_chujiu]` `[role: 条件分支]` 潜龙勿用：德已具而名未成，应隐伏不求闻达。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_003]` `[trigger: 卦=乾 AND 九二]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_jiuer AND zhouyi_zhongwei]` `[role: 条件分支]` 见龙在田，利见大人：德行显露于世，利于遇见大人。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_004]` `[trigger: 卦=乾 AND 九三]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_jiusan]` `[role: 条件分支]` 君子终日乾乾，夕惕若厉，无咎：身处险位，唯有日夜自律方免于咎。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_005]` `[trigger: 卦=乾 AND 九四]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_jiusi]` `[role: 条件分支]` 或跃在渊，无咎：进退未定之时，试探跃升但仍不离其群。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_006]` `[trigger: 卦=乾 AND 九五]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_jiuwu AND zhouyi_zhongwei]` `[role: 条件分支]` 飞龙在天，利见大人：大人居尊位，与天地日月四时相应而行道。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_007]` `[trigger: 卦=乾 AND 上九]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_shangjiu AND zhouyi_kangji]` `[role: 条件分支]` 亢龙有悔：只知进不知退、只知存不知亡、只知得不知丧，终致有悔。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_008]` `[trigger: 卦=乾 AND 用九]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_yao_yongjiu]` `[role: 条件分支]` 见群龙无首，吉：众阳皆动而无首领，天德不可为首。 → 《周易·乾卦·爻辞》
  - `[ns_zhouyi_009]` `[trigger: 卦=乾 AND 彖传]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_tuan AND zhouyi_yuan AND zhouyi_heng]` `[role: 主干依赖]` 大哉乾元！万物资始，乃统天。乾道变化，各正性命，保合大和。 → 《周易·乾卦·彖传》
  - `[ns_zhouyi_010]` `[trigger: 卦=乾 AND 象传]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_xiang AND zhouyi_trigram_qian]` `[role: 主干]` 天行健，君子以自强不息：以天道刚健为法，不断砥砺自身。 → 《周易·乾卦·象传》
  - `[ns_zhouyi_011]` `[trigger: 卦=乾 AND 文言四德]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_wenyan]` `[role: 主干]` 元亨利贞：元者善之长，亨者嘉之会，利者义之和，贞者事之干。 → 《周易·乾卦·文言》
  - `[ns_zhouyi_012]` `[trigger: 卦=乾 AND 文言进德]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_wenyan]` `[role: 主干依赖]` 君子进德修业：以忠信进德，以修辞立诚，以知几存义。 → 《周易·乾卦·文言》
  - `[ns_zhouyi_013]` `[trigger: 卦=乾 AND 文言大人]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_wenyan AND zhouyi_daren AND zhouyi_tiandi]` `[role: 总结]` 大人者，与天地合德，与日月合明，与四时合序，与鬼神合吉凶。 → 《周易·乾卦·文言》
  - `[ns_zhouyi_014]` `[trigger: 卦=乾 AND 文言亢极]` `[factor_trigger: zhouyi_gua_qian AND zhouyi_wenyan]` `[role: 总结]` 知进退存亡而不失其正者，其唯圣人乎！ → 《周易·乾卦·文言》"""
    normalized_text_zh: str = """"""
    subject: str = "乾卦（䷀）"
    factor_refs: list = ['zhouyi_trigram_qian', 'zhouyi_yuan_heng_li_zhen', 'zhouyi_six_dragons', 'zhouyi_tian_xing_jian', 'zhouyi_ziqiang_buxi', 'zhouyi_kanglong_youhui']
    
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
        l1_anchor="zy_v1.0.0_乾卦_001_L1",
    )
    version: str = "1.0.0"
