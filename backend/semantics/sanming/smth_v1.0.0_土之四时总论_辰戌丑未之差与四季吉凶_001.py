"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228963
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
    semantic_id="smth_v1.0.0_土之四时总论_辰戌丑未之差与四季吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 土之四时总论辰戌丑未之差与四季吉凶(SemanticEntry):
    """
    - **原文（source_text）**：  
  所忌者，火死酉也，水旺子也。盖土赖火印，火死则土囚，土喜水财，水旺则土虚。土得金火，方成大器。土高无贵，空惹灰尘。土聚则滞，土散则轻。辰戌丑未，土...
    """
    
    original_text: str = """- **原文（source_text）**：  
  所忌者，火死酉也，水旺子也。盖土赖火印，火死则土囚，土喜水财，水旺则土虚。土得金火，方成大器。土高无贵，空惹灰尘。土聚则滞，土散则轻。辰戌丑未，土之正位，分阴分阳，土则不同。辰有伏水，未有匿木，滋养万物，春夏为功；戌有藏火，丑有隐金，秋火冬金，肃杀万物。故土聚辰未为贵，聚戌丑不为贵。是土爱辰未而不爱丑、戌也明矣。若更五行有气，人命逄之，田产无比，晚年富贵悠悠。若土太实，无水则不和喿，无木则不疏通；土见火则焦，女命多不生长。土旺四季，惟戌土困弱。戊多为人好斗，多瞌睡；辰未人好食，丑人清省。丑有艮土有癸水，能润而膏。人命遇此，主能卓立。生于春月，其势虚弱，喜火生扶，恶木太过，忌水泛滥，欲喜比助，得金而制木为祥。金若多，仍盗土气。夏月之土，其势燥烈，得盛水滋润成功，忌旺火煆炼焦赤。木助火炎，生克无良；金生水泛，妻财有益。见比肩蹇滞不通，如太过又喜木袭。秋月之土，子旺母衰，金多而耗盗其气，术盛而制伏纯良，火重重而不厌，水泛泛而非祥，得比肩则能助力，至霜降，不比无妨。冬月之土，外寒内温，水旺财足，金多子秀，火盛有荣，木多无咎，再加土也尤佳，惟喜身强足寿。

- **分字分词释义**：
  - **土赖火印**：土以火为印绶，得火温养则有生气。
  - **土喜水财**：水为土之财星，有水则土能生万物。
  - **土高无贵，土聚则滞**：土过高过聚则壅塞不通，反成累赘。
  - **辰戌丑未土之正位**：四库之土，各分阴阳与伏藏之物，性质不同。
  - **伏水、匿木、藏火、隐金**：指在辰、未、戌、丑中分别伏藏之水、木、火、金。
  - **春夏为功、秋火冬金肃杀**：春夏偏于滋养，秋冬偏于肃杀收敛。
  - **土太实无水无木**：过重之土缺水木调和，则为顽钝不通。
  - **春夏秋冬之土**：分别点出四时土气的偏性与取用。

- **规范化释义（primary_lang_explained）**：  
  本段总论土在四时中的吉凶取向。就生克关系而言，土赖火为印，火若死绝则土囚；土喜水为财，水若泛滥则土虚。土得火与金相辅，方能成器；过高、过聚之土，反而只是扬尘壅塞。辰戌丑未为土的四个正位，其中辰伏水、未匿木，偏于滋养生长，多在春夏见功；戌藏火、丑隐金，偏于肃杀收敛，多在秋冬见用，故聚土于辰未为贵，聚于戌丑则多为杀伐之象。若配合得当、五行皆有根气，则命中多主田产丰厚、晚年富足。反之，土太实而无水润、无木疏，逢火则焦，尤其女命易有不育之忧。四季之中，土常旺于四季月，而戌土相对困弱。人格方面，戊土多见好斗与昏昏欲睡之性，辰未之人多好食，丑土则偏于朴实节省；丑中艮土含癸水，能润燥而成膏土，人命得之，多能卓立。再就季节细分：春月之土势虚弱，宜火来生扶，忌木太过、忌水泛滥；夏月之土燥烈，最喜盛水滋润，怕旺火再烧，木助火炎则为过，金生水反成泛滥；秋月之土子旺母衰，金多盗气，需火来调剂，水多则成漂泛；冬月之土外寒内温，水旺为财、金多子秀、火盛有荣，木多反无大害，再得适度之土，则以身强寿长为佳象。

- **完整对等诠释（secondary_lang_full）**：  
  This passage offers a seasonal general discourse on the Earth element. In terms of generating and controlling, Earth relies on Fire as its Seal; when Fire dies, Earth becomes imprisoned. Earth delights in Water as wealth; when Water overflows, Earth is hollowed out. Only when Earth is supported by both Fire and Metal can it truly become a useful vessel; overly high or overly accumulated Earth merely raises dust and causes blockage. The four Earth positions—Chen, Xu, Chou, and Wei—each hold different hidden agents: Chen stores Water, Wei conceals Wood and thus nourishes life in spring and summer; Xu hides Fire, Chou hides Metal and thus presides over the killing and harvesting of autumn Fire and winter Metal. Therefore, when Earth clusters around Chen and Wei it is considered noble; clustering at Xu and Chou tends instead toward harshness. When all Five Elements in the chart have proper root, encountering such Earth often indicates abundant land and property and leisurely wealth in later life. If Earth is too solid while lacking Water to moisten and Wood to loosen, it becomes hard and unyielding; encountering strong Fire then scorches it, and especially in female charts may signify difficulty in childbearing. Across the year, Earth is strong in all four season-ending months, yet Xu Earth is relatively constrained. In character, much Wu Earth makes one contentious and drowsy, Chen and Wei people tend to enjoy food, Chou Earth types are frugal and plain; within Chou, Gen Earth carries Gui Water, forming rich, lubricating soil that allows people with it to stand out. By seasons: in spring, Earth is weak and benefits from Fire’s support, dislikes excessive Wood and flooding Water; in summer, Earth is dry and blazing, needing abundant Water to moisten and fearing strong Fire further refining it, with Wood that feeds Fire becoming harmful and Metal that generates overabundant Water undermining stability; in autumn, the child (Metal) is strong while the mother (Earth) is weak, so too much Metal drains Earth, while sufficient Fire can regulate and restrain it, and aimless Water is inauspicious; in winter, the exterior is cold while the interior retains warmth—Water flourishes as wealth, much Metal indicates talented offspring, strong Fire brings honor, abundant Wood is not harmful, and adding proper Earth further improves matters so long as the body (Day Master) remains robust and long-lived.

- **核心要点**：
  - 土赖火印水财：火印温养土，水财滋润土，过亡则反成囚与虚。
  - 辰未为滋养之土，戌丑为肃杀之土，聚辰未贵、聚戌丑不贵。
  - 土太实而少水木，则壅塞顽钝，逢火则焦，女命尤忌。
  - 春土喜火忌水木，夏土喜水忌火，秋土喜火忌水，冬土身强则四行皆可用。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_126]` `[trigger: 四时之土]` `[factor_trigger: seasonal_earth AND chen_xu_chou_wei]` `[role: 主干]` 土赖火印，火死则土囚，土喜水财，水旺则土虚。土得金火，方成大器。辰戌丑未，土之正位，分阴分阳，土则不同。聚辰未为贵，聚戌丑不为贵。 → 《三命通会》卷一#土之四时总论

- **详细解说**：  
  这一总论将土从「结构—位置—季节」三个维度展开。结构层面，先用「土赖火印、土喜水财」点明土与火、水之间的双重关系：火是土之印绶，决定其是否具备生命张力；水是土之财星，决定其能否生养万物。若失火，则土冷硬而囚；若水泛，则土被掏空而无实。位置层面，以辰戌丑未四库土为轴：辰未偏重滋养与根基，戌丑偏重肃杀与收敛，因此「聚辰未为贵，聚戌丑不为贵」，也解释了为何同为库土而吉凶有别。季节层面，则分别说明春夏秋冬之土的偏性与调剂：春土本弱，宜火暖而忌木水过度；夏土最燥，非水不成功；秋土母衰子旺，若再被金耗泄则失势，需火来扶；冬土外寒内温，只要身强，则水财、金子、火荣皆可受用。人格与体质的短句补充，则将抽象土象具体化为性格气质与生活倾向，如戊多好斗昏昧、辰未人好食而重口福、丑土人简省朴实等，使命理解读落到可感之处。

- **校勘与字词辨析（双语）**：
  - **中文**：「不和喿」当作「不和燥」，指土太实而无水润，则燥烈不和；「术盛」多刻作「土盛」，此从命理语境释为土势强盛而能制伏金。
  - **English**: The phrase likely means "no harmony and excessive dryness" when Earth is overly solid without Water; "Earth abundant" is interpreted as strong Earth able to restrain Metal, fitting the doctrinal context better than "art abundant"."""
    normalized_text_zh: str = """"""
    subject: str = "土之四时总论：辰戌丑未之差与四季吉凶"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_土之四时总论_辰戌丑未之差与四季吉凶_001_L1",
    )
    version: str = "1.0.0"
