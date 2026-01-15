"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.885251
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
    semantic_id="zgjm_v1.0.0_佛道僧尼鬼神_001",
    book_id="zhougong",
    engine_id="dream"
)
class 佛道僧尼鬼神(SemanticEntry):
    """
    - **原文（source_text）**：

  诸佛菩萨大吉利，法师登座主疾病。老君真入皆主吉。  
  画神佛者得人钦，入神庙神动大吉。造幡盖者大吉利。  
  僧师教人念经吉，道士女冠言语吉。...
    """
    
    original_text: str = """- **原文（source_text）**：

  诸佛菩萨大吉利，法师登座主疾病。老君真入皆主吉。  
  画神佛者得人钦，入神庙神动大吉。造幡盖者大吉利。  
  僧师教人念经吉，道士女冠言语吉。和尚尼姑看经闷。  
  被神鬼打大不祥，堂上神佛大吉利。神佛不成形大凶。  
  烧香礼拜皆大吉，迎神赛社有外财。仙圣到家福禄至。  
  与鬼斗者主延寿，祭祀神道大吉利。身受戒行者子孝。  
  与神女通得贵子，与尼姑交主失财。看神佛者妻有子。  
  佛共人言有福助。

- 分字分词释义：

  - **诸佛菩萨**：佛教中的觉者与大乘菩萨，象征至高慈悲与智慧.
  - **法师登座**：法师升座讲法，往往与疾病、健康警示相关.
  - **老君真入**：道教太上老君或真人入梦，象征道法庇佑与长寿.
  - **画神佛、造幡盖**：制作宗教艺术品与供养之物，象征虔诚与功德.
  - **神动**：神像显灵、动态，象征神力加持或警示.
  - **僧道尼冠**：僧人、道士、尼姑、女冠等宗教人士.
  - **被神鬼打**：被超自然力量殴打，多主凶兆或惩戒.
  - **神佛不成形**：神佛形象模糊破碎，象征信仰动摇或灾异将至.
  - **烧香礼拜、迎神赛社**：宗教仪式与社区祭祀活动.
  - **与鬼斗**：与鬼魂搏斗，象征生命力顽强与延寿.
  - **与神女通、与尼姑交**：与宗教异性交往，有吉有凶.

- **规范化释义（primary_lang_explained）**：

  本类条目围绕"佛道僧尼鬼神"展开，揭示梦象学中对**宗教人物、超自然存在与信仰实践**的解读。梦见诸佛菩萨、老君真人多主吉利庇佑，但法师登座则可能预示疾病；画神佛、造幡盖、烧香礼拜等虔诚行为多主得人尊敬与福报；入神庙而神像显灵则大吉。僧道教人念经、与梦者言语往往主吉，但和尚尼姑看经则主烦闷。被神鬼殴打为大不祥，神佛形象模糊破碎亦主大凶。与鬼搏斗反主延寿，祭祀神道主吉利。与神女交通主得贵子，但与尼姑交往则主失财。佛共人言语则主有福助.

- 核心要点：

  - **宗教人物象征庇佑与警示**：诸佛菩萨、老君真人主吉，但法师登座可能关联疾病.
  - **虔诚行为多主功德**：画神佛、造幡盖、烧香礼拜、祭祀等多主得人钦敬与福报.
  - **神像状态决定吉凶**：神动大吉，神佛不成形大凶，堂上神佛大吉利.
  - **被动受害主凶**：被神鬼打大不祥，需警惕惩戒或业障.
  - **与超自然存在互动有别**：与鬼斗主延寿，与神女通得贵子，与尼姑交失财.

- 详细解说：

  **（一）宗教人物：庇佑与警示的双重象征**

  本类开篇即揭示"诸佛菩萨大吉利，法师登座主疾病，老君真入皆主吉"。诸佛菩萨与老君真人在梦中多象征至高的慈悲、智慧与道法庇佑，预示现实中将得贵人相助或心灵安定。但"法师登座"往往对应"超度亡魂""为病者祈福"等情境，因此与疾病、死亡有所关联.

  **（二）虔诚行为：功德与尊敬**

  "画神佛者得人钦，造幡盖者大吉利，烧香礼拜皆大吉，祭祀神道大吉利"四句构成"虔诚行为"的正向象征：制作宗教艺术品、供养之物、参与祭祀等行为，在梦中往往预示现实中将得他人尊敬、积累功德或获得福报。这些行为体现的是"虔诚、付出、敬畏"的态度，因此多主吉利.

  **（三）神像状态：显灵与破碎**

  "入神庙神动大吉，堂上神佛大吉利，神佛不成形大凶"三句揭示神像状态的吉凶分野：神像显灵、动态多主神力加持，预示好运与庇佑；堂上供奉的神佛形象完整庄严，则主家宅安宁、福禄增长；但若神佛形象模糊、破碎、不成形，则主信仰动摇或灾异将至，需警惕精神危机或家宅不宁.

  **（四）宗教人士：教导与烦闷**

  "僧师教人念经吉，道士女冠言语吉，和尚尼姑看经闷"三句区分不同宗教人士的梦象：僧人道士主动教导、与梦者言语，多主吉利，象征精神引导与智慧启发；但梦见和尚尼姑默默看经，则主烦闷，可能暗示梦者内心有未解的困扰或修行上的瓶颈.

  **（五）被动受害：神鬼之罚**

  "被神鬼打大不祥"一句是本类最强烈的凶象：被神鬼殴打往往象征因过失、业障或越界行为而遭受惩戒，预示现实中可能面临严重挫折、疾病或人际冲突，需要深刻反省并及时改正.

  **（六）与超自然存在互动：延寿、得子与失财**

  "与鬼斗者主延寿，与神女通得贵子，与尼姑交主失财"三句揭示不同互动的吉凶：与鬼搏斗反而主延寿，体现"生命力顽强、不畏阴邪"的象征；与神女交通主得贵子，象征天赐麟儿；但与尼姑交往则主失财，可能暗示违背戒律或卷入不当关系而招损失.

  综合而言，本类揭示梦象学中对**宗教、信仰与超自然存在**的复杂态度：虔诚、敬畏、正当互动多主吉利，但逾越边界、被动受罚、信仰动摇则主凶险，需要在精神层面保持清明与敬畏.

- 校勘与字词辨析（本类）：

  - "佛道僧尼鬼神"六字标题按底本录入，涵盖佛教、道教、宗教人士与超自然存在四大主题.
  - "法师登座主疾病"一句，"法师"指佛教或道教法师，"登座"指升座讲法或主持法事，梦象中反与疾病相关，释义中已说明.
  - "神动"指神像显灵或动态，不作"震动"解，本稿依梦象传统释为"神力加持".

- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_984]` `[trigger: 梦见诸佛菩萨]` `[factor_trigger: dream_buddha]` `[role: 主干]` 诸佛菩萨，大吉利。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_985]` `[trigger: 梦见法师登座]` `[factor_trigger: dream_master_seat]` `[role: 主干]` 法师登座，主疾病。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_986]` `[trigger: 梦见老君真人]` `[factor_trigger: dream_laozi]` `[role: 主干]` 老君真入，皆主吉。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_987]` `[trigger: 梦见画神佛]` `[factor_trigger: dream_paint_buddha]` `[role: 主干]` 画神佛者，得人钦。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_988]` `[trigger: 梦见入神庙神动]` `[factor_trigger: dream_temple_god]` `[role: 主干]` 入神庙神动，大吉。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_989]` `[trigger: 梦见造幡盖者]` `[factor_trigger: dream_make_banner]` `[role: 主干]` 造幡盖者，大吉利。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_990]` `[trigger: 梦见僧师教人念经]` `[factor_trigger: dream_monk_teach]` `[role: 主干]` 僧师教人念经，吉。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_991]` `[trigger: 梦见道士女冠言语]` `[factor_trigger: dream_daoist_speak]` `[role: 主干]` 道士女冠言语，吉。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_992]` `[trigger: 梦见和尚尼姑看经]` `[factor_trigger: dream_monk_read]` `[role: 主干]` 和尚尼姑看经，闷。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_993]` `[trigger: 梦见被神鬼打]` `[factor_trigger: dream_beaten_ghost]` `[role: 主干]` 被神鬼打，大不祥。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_994]` `[trigger: 梦见堂上神佛]` `[factor_trigger: dream_hall_buddha]` `[role: 主干]` 堂上神佛，大吉利。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_995]` `[trigger: 梦见神佛不成形]` `[factor_trigger: dream_buddha_unclear]` `[role: 主干]` 神佛不成形，大凶。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_996]` `[trigger: 梦见烧香礼拜]` `[factor_trigger: dream_incense_worship]` `[role: 主干]` 烧香礼拜，皆大吉。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_997]` `[trigger: 梦见迎神赛社]` `[factor_trigger: dream_welcome_god]` `[role: 主干]` 迎神赛社，有外财。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_998]` `[trigger: 梦见仙圣到家]` `[factor_trigger: dream_saint_home]` `[role: 主干]` 仙圣到家，福禄至。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_999]` `[trigger: 梦见与鬼斗者]` `[factor_trigger: dream_fight_ghost]` `[role: 主干]` 与鬼斗者，主延寿。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_1000]` `[trigger: 梦见祭祀神道]` `[factor_trigger: dream_sacrifice_god]` `[role: 主干]` 祭祀神道，大吉利。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_1001]` `[trigger: 梦见身受戒行者]` `[factor_trigger: dream_take_vows]` `[role: 主干]` 身受戒行者，子孝。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_1002]` `[trigger: 梦见与神女通]` `[factor_trigger: dream_goddess]` `[role: 主干]` 与神女通，得贵子。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_1003]` `[trigger: 梦见与尼姑交]` `[factor_trigger: dream_nun]` `[role: 主干]` 与尼姑交，主失财。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_1004]` `[trigger: 梦见看神佛者]` `[factor_trigger: dream_look_buddha]` `[role: 主干]` 看神佛者，妻有子。 → 《周公解梦·佛道僧尼鬼神》
  - `[ns_zgjm_1005]` `[trigger: 梦见佛共人言]` `[factor_trigger: dream_buddha_speak]` `[role: 主干]` 佛共人言，有福助。 → 《周公解梦·佛道僧尼鬼神》"""
    normalized_text_zh: str = """"""
    subject: str = "佛道僧尼鬼神"
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
        l1_anchor="zgjm_v1.0.0_佛道僧尼鬼神_001_L1",
    )
    version: str = "1.0.0"
