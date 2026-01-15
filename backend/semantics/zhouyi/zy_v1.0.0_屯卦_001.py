"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899711
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
    semantic_id="zy_v1.0.0_屯卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 屯卦(SemanticEntry):
    """
    - **原文（source_text）**：
  屯：元亨，利贞。勿用有攸往，利建侯。

  【爻辞】
  初九，磐桓，利居贞，利建侯。
  六二，屯如，邅如。乘马班如，匪寇婚媾。女子贞不字，十年乃字...
    """
    
    original_text: str = """- **原文（source_text）**：
  屯：元亨，利贞。勿用有攸往，利建侯。

  【爻辞】
  初九，磐桓，利居贞，利建侯。
  六二，屯如，邅如。乘马班如，匪寇婚媾。女子贞不字，十年乃字。
  六三，即鹿无虞，惟入于林中。君子几，不如舍，往吝。
  六四，乘马班如，求婚媾。往吉，无不利。
  九五，屯其膏。小，贞吉；大，贞凶。
  上六，乘马班如，泣血涟如。

  【彖传】
  《彖》曰：屯，刚柔始交而难生；动乎险中，大亨贞。雷雨之动满盈，天造草昧；宜建侯而不宁。

  【象传】
  《象》曰：云雷，屯；君子以经纶。

- 分字分词释义：

  - **屯**：卦名，本义为草木初生、萌芽未舒，引申为草昧初开、艰难聚集之时。象征事情初始、阻力纷至。
  - **元亨，利贞**：在艰难初始中仍具有根本通达、适宜守正的可能。
  - **勿用有攸往**：不宜轻率远行或贸然推进重大行动。
  - **利建侯**：有利于立国建侯、树立核心领导与秩序。
  - **磐桓**：徘徊停留、迟疑不进。
  - **利居贞**：利于安守正位，不可躁进。
  - **屯如，邅如**：艰难阻塞、曲折不前之状。
  - **乘马班如**：骑马往返、徘徊不进，象征行动受阻。
  - **匪寇婚媾**：不是强盗劫掠，而是婚嫁之事；提示误判、误会的可能。
  - **女子贞不字**：女子守贞暂不嫁人（不字，未出嫁）。
  - **十年乃字**：经历长久等待（十年为虚数），方才成婚。
  - **即鹿无虞**：追逐野鹿而无虞人（山泽官）指引，比喻冒进而缺乏专业引导。
  - **惟入于林中**：最终深入山林、迷失路径。
  - **君子几，不如舍，往吝**：君子察觉几微之机，应知舍弃；勉强前往则有羞吝之失。
  - **求婚媾**：主动求取婚姻、求合之事。
  - **屯其膏**：囤积脂膏，比喻积蓄资源而未施。
  - **小，贞吉；大，贞凶**：求小事尚吉，谋大事则凶；规模与时机不当则转凶。
  - **泣血涟如**：悲痛至极，泪如血涌、连绵不绝。
  - **云雷，屯**：上卦为坎之云雨，下卦为震之雷动，雷雨交作而尚在草昧之中。
  - **经纶**：经纬丝线，引申为筹划治理、经略天下。

- **规范化释义（primary_lang_explained）**：

  屯卦象征万事草创之初：刚柔始交，各种力量开始汇聚，却也带来重重艰难。卦辞“元亨，利贞”指出，即便处在险阻与混沌之中，若能守正依时，仍具有根本通达的可能；但“不宜有远行”，不宜轻率推进过远的目标，而应专注于“建侯”——确立核心领导与基本秩序。

  六爻爻辞从不同位置刻画“初难之世”的处境：初九“磐桓”，强调在险难之初宜徘徊观察、安居守正，并以谦下之姿建侯；六二“屯如，邅如”，形容进退维艰，如乘马徘徊，既可能误以为遇寇，实则为婚事之机，女子守贞久待，十年后方成婚，体现机会与误判并存；六三“即鹿无虞”，比喻冒然追逐利益而无专业引导，结果深入险境，君子知几，当以舍为上；六四再现“乘马班如”，但此时明确以“求婚媾”，顺势而往则吉而无不利；九五“屯其膏”，说明资源已积而未施，小事守贞尚吉，大事强行则凶；上六则以“泣血涟如”收束，呈现若始终不知变通，终将落入悲痛难支之境。

  彖传以“刚柔始交而难生”“雷雨之动满盈，天造草昧”概括屯卦的总态：天地造化伊始，雷雨交作、草昧未明，既充满生机，又伴随混乱与艰困；适宜建侯立国、筹划经略，却难以安于静止。象传以“云雷，屯；君子以经纶”点出：君子当在此时承担“经纶天下”的职责，而非逃避艰难。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Zhun, "Difficulty at the Beginning", symbolizes the initial stage of all endeavors when firmness and flexibility first interact, various forces begin to gather, yet bring layers of difficulty. The Judgment "yuan heng, li zhen" indicates that even amid obstacles and chaos, if one can maintain correctness and act according to timing, fundamental success remains possible; however, "it is not favorable to have somewhere to go"—one should not rashly advance distant goals but should focus on "establishing feudal lords"—confirming core leadership and basic order.

The Image "clouds and thunder, Zhun; the noble person thereby organizes" points out that the noble person should shoulder the responsibility of "organizing the world" at this time rather than avoiding difficulty. The six lines repeatedly present "hesitation, waiting, misjudgment, and choice": sometimes one should stay (hesitating, residing in steadfastness), sometimes one should abandon (pursuing the deer without a forester), sometimes one should seize the moment (seeking marriage alliance).

- 核心要点：

  - 屯卦之“屯”，重在草创初难：生机与阻力并存，是“刚柔始交而难生”的时期。
  - 大势可“元亨利贞”，但不宜轻率远行，只宜在险中稳步建构基本秩序（建侯）。
  - 各爻反复呈现“徘徊、等待、误判与抉择”：有时宜守（磐桓、居贞），有时宜舍（即鹿无虞），有时宜及时把握（求婚媾）。
  - 资源积聚（屯其膏）若用于小事尚吉，若盲目推向大事则凶，提示规模与节奏的重要性。
  - 终极警示在于：若不知因时变通，只一味困守与纠缠，最终可能陷入“泣血涟如”的悲剧。

- 详细解说：

  屯卦继乾坤之后，标志着“天地定位”之后万物初生的阶段：乾为天之始，坤为地之承，而屯则是天地既定后，万物在险中萌发的状态。彖传所谓“刚柔始交而难生”，正是说阳刚与阴柔的交感尚处初始，结构未稳，于是“难”便成为常态。这种难并非纯凶，而是“难中有通”的局面——“动乎险中，大亨贞”，在险地中调动正确的行动与守正的态度，反能大有通达。

  卦象“云雷，屯”：坎为云雨在上，震为雷动在下，如春雷乍动、雨气未畅，天地“草昧”之时。所谓“天造草昧”，既写出宇宙之初的混沌，也可以用来比喻一个时代、一个事业、一个人生命段落的开端：规则未立、人心未定，却充满潜能。

  从爻位看，初九处于下卦之始，以阳居刚，志在建侯，却以“磐桓”为态：在险难当头、秩序未定之时，反而必须暂缓脚步，“利居贞”而后“利建侯”。这种迟疑并非懦弱，而是一种战略上的谨慎筹划，与象传中“君子以经纶”相呼应。

  六二为居中之阴，因乘刚而受压，“屯如，邅如”，艰难重重；“乘马班如，匪寇婚媾”则生动地描绘了危险与机缘的混杂：远望似有强寇，近视原为婚事——提醒在初难阶段极易误判局势。女子守贞不嫁，十年后方字，说明某些关系与合作需经历漫长的酝酿与考验。

  六三“即鹿无虞”，则是对“冒进逐利”的批评：追鹿本无错，却无虞人指引，以致深入林中难以自拔。君子在此宜“几”，即察觉细微之机，不如舍之，若执意前往，则“往吝”。这条对现代决策尤具启示：在信息不全、缺乏专业指导的情况下贸然追逐“猎物”，往往陷入更深的困境。

  六四再现“乘马班如”，但加上“求婚媾”：此时位置已较安稳，上承九五之阳，下有初九之刚，若主动求合（无论是婚姻、伙伴或条约），顺势前往则“往吉”，而且“无不利”。可见同样是徘徊，若选对对象与时机，则可转守为攻。

  九五“屯其膏，小贞吉，大贞凶”则点出资源调度的问题：膏者脂膏、油脂，象征丰厚资源。屯于己而未施，若仅用于小范围之事，守正尚吉；若欲凭此一举图大业，则因时机、人心、结构未备，反致凶祸。这里提醒，我们在草创阶段对资源使用要循序渐进，不宜一口气推至极限。

  上六“泣血涟如”把屯卦的艰难推向情感高点：若经历重重犹豫、误判与错失之后，仍不肯调整方向，只会在反复徘徊中耗尽心血，其结果必是难以长久的痛苦局面。象传反问“何可长也”，正是对这种状态的判决：不可以让这种局面长久持续。

  整体而言，屯卦教人如何面对“开局的艰难”：一方面要有乾坤之根基——志在建构长久秩序（建侯）、守正不失；另一方面也必须承认“难”是草创阶段的常态，从而在徘徊与抉择中，学会观察时机、及时舍取、合理调度资源，而非被短期的阻塞与痛苦所吞没。"""
    normalized_text_zh: str = """"""
    subject: str = "屯卦（䷂）"
    factor_refs: list = ['zhouyi_gua_zhun', 'zhouyi_jianhou', 'zhouyi_jinglun']
    
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
        l1_anchor="zy_v1.0.0_屯卦_001_L1",
    )
    version: str = "1.0.0"
