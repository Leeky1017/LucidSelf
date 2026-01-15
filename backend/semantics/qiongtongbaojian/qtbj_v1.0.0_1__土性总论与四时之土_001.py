"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596945
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
    semantic_id="qtbj_v1.0.0_1__土性总论与四时之土_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1土性总论与四时之土(SemanticEntry):
    """
    - **原文（source_text）**：
  五行之土，散冠四维，故金木水火，依而成象，是四时皆有用有忌者。火、死酉也。水、旺子也。盖土赖火运，火死则土囚。土喜水才，水旺则土虚。土得金火，方成大器...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行之土，散冠四维，故金木水火，依而成象，是四时皆有用有忌者。火、死酉也。水、旺子也。盖土赖火运，火死则土囚。土喜水才，水旺则土虚。土得金火，方成大器。土高无贵，空惹灰尘。土聚则滞，土散则轻。
  
  辰戌丑未，壹心正也。分阴分阳，主则不同。辰有伏水；未有匿木，滋养万物，春夏为功；戌有藏火；丑有隐金。秋火冬金，肃杀万物。
  
  土聚辰未为贵，聚丑戌不为贵。是土爱辰未、而不爱丑戌也明矣。若更五行有气，人命逢之，田产无比。晚年富贵悠悠。
  
  若土太实无水，燥则不和；无木则不疏通；土见火则焦，女命多不生长。
  
  土旺四季，惟戌土困弱。戌多为人好斗，多瞌睡。辰未人好食，丑人清省。丑为艮土，有癸水能润而膏，人命遇此，主能卓立。

- **分字分词释义**：
  - **散冠四维**：土分散而冠于四方 / 辰戌丑未四库 / 土之分布
  - **依而成象**：依托土方能成形象 / 金木水火借土显形 / 载体
  - **火死酉**：火气在酉位衰绝 / 酉月 / 火入死地
  - **水旺子**：水在子位旺盛 / 子月 / 水得长生
  - **土赖火运**：土依火生发而运转 / 火生土 / 元气来源
  - **土喜水才**：土喜水为财星 / 水润土生财 / 财象
  - **土得金火方成大器**：土得金火配合方能成器 / 火生土金泄秀 / 成器格
  - **土聚辰未为贵**：土聚在辰未为尊贵之土 / 湿暖之库 / 田产贵象
  - **土聚丑戌不为贵**：土聚在丑戌不贵反肃杀 / 寒燥之库 / 贱象
  - **土太实无水**：土过实又无水润 / 过旺难调 / 燥病
  - **女命多不生长**：女命多难孕育生养 / 土焦无滋 / 凶象
  - **丑为艮土**：丑属艮卦山土 / 丑位 / 厚重能立
  - **癸水能润而膏**：癸水能润为膏腴之土 / 癸水滋土 / 吉象

- **规范化释义（primary_lang_explained）**：
  五行中的土，分散在四季的末尾（四维：辰戌丑未），所以金木水火，都依靠土才能成象，土在四季都有可用和可忌的时候。火死于酉，水旺于子。因为土依赖火来生运（土赖火生），火死（酉）则土囚（无气）。土喜欢水作为财星，但水太旺（子）则土虚流散。土得到金（泄秀）和火（生身），才能成为大器。土如果只是高亢而没有贵气（无木疏/无水润），只是空惹灰尘。土聚集太重则停滞，土分散太轻则轻浮。
  
  辰戌丑未，本性都是土。但分阴阳，主事不同。辰中有伏藏的水，未中有隐匿的木，能滋养万物，春夏季节有功劳；戌中有藏火，丑中有隐金，秋火冬金（秋金冬水？或指戌丑肃杀之气），肃杀万物。
  
  土聚集在辰未（暖土/生发之土）为贵，聚集在丑戌（寒燥之土/肃杀之土）不为贵。可见土喜爱辰未，而不喜爱丑戌是明摆着的。如果五行更有气，人命遇到这种情况，田产无比丰厚，晚年富贵悠悠。
  
  如果土太实而没有水，燥热就不能和谐；没有木就不能疏通；土见到火就焦裂，女命多半不能生育生长。
  
  土旺于四季末，只有戌土困顿衰弱（火墓/燥土）。戌土多的人好斗，多瞌睡。辰未土多的人好饮食，丑土多的人清廉节省。丑是艮土，有癸水能润泽成膏土，人命遇到丑土，主能够卓立成家。

- **完整对等诠释（secondary_lang_full）**：
  Earth of the Five Elements is scattered across the Four Corners (Chen, Xu, Chou, Wei); thus Metal, Wood, Water, and Fire rely on it to form images. It is useful and dreaded in all four seasons. Fire dies in You; Water is prosperous in Zi. Earth relies on Fire for movement; if Fire dies, Earth is imprisoned. Earth likes Water as Wealth, but if Water is prosperous, Earth becomes hollow. Earth obtains Metal and Fire to become a great vessel. High Earth without nobility merely attracts dust. Accumulated Earth becomes stagnant; scattered Earth becomes light.
  
  Chen, Xu, Chou, Wei are all essentially Earth. Divided by Yin and Yang, their functions differ. Chen has hidden Water; Wei has concealed Wood; they nourish all things, meritorious in Spring and Summer. Xu has stored Fire; Chou has hidden Metal. Autumn Fire and Winter Metal kill all things.
  
  Earth gathering in Chen/Wei is noble; gathering in Chou/Xu is not noble. It is clear that Earth loves Chen/Wei and dislikes Chou/Xu. If other Five Elements have Qi, a person meeting this will have incomparable land and property, with leisurely wealth in old age.
  
  If Earth is too solid without Water, dryness prevents harmony; without Wood, there is no dredging. Earth seeing Fire becomes scorched; female lives often fail to grow/reproduce.
  
  Earth is prosperous in the Four Seasons, only Xu Earth is trapped and weak. Many Xu makes one combative and sleepy. Chen/Wei people love eating; Chou people are frugal. Chou is Gen Earth, with Gui Water to moisten it into paste; meeting this implies ability to stand outstandingly.

- **核心要点**：
  - **四库土性**：
    - 辰未：含水木，滋养万物，主贵/田产。
    - 丑戌：含金火，肃杀，不贵/好斗/清省。
  - **喜忌**：
    - 喜：火（生）、水（财/润）、木（疏）、金（泄）。
    - 忌：土实无水（燥）、无木（滞）、见火（焦）。
  - **土赖火生**：火死土囚。

- **详细解说**：
  - “土聚辰未为贵”：这是《穷通》独特的观点，认为辰未有生机（木水），适合万物生长；而丑戌寒燥（金火），不利生长。
  - “丑为艮土...能卓立”：丑虽寒，但湿土能生金晦火，有润泽之功，故也能成器。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_294]` `[trigger: 辰未聚土]` `[factor_trigger: dizhi_chen_wei AND earth_gather AND five_elements_qi AND land_property]` `[role: 条件分支]` 土聚辰未为贵，若更五行有气，人命逢之，田产无比，晚年富贵悠悠。 → 《穷通宝鉴·论土总论》#20.1
  - `[ns_qttbj_295]` `[trigger: 丑戌聚土]` `[factor_trigger: dizhi_chou_xu AND earth_gather AND NOT noble_earth]` `[role: 例外处理]` 土聚丑戌不为贵，是土爱辰未、而不爱丑戌也明矣。 → 《穷通宝鉴·论土总论》#20.1
  - `[ns_qttbj_296]` `[trigger: 土太实无水]` `[factor_trigger: earth_solid AND NOT tiangan_ren AND NOT tiangan_gui AND dry_unharmonious]` `[role: 例外处理]` 若土太实无水，燥则不和；无木则不疏通；土见火则焦，女命多不生长。 → 《穷通宝鉴·论土总论》#20.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 土性总论与四时之土"
    factor_refs: list = ['four_corners', 'sowing_reaping', 'gen_earth']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__土性总论与四时之土_001_L1",
    )
    version: str = "1.0.0"
