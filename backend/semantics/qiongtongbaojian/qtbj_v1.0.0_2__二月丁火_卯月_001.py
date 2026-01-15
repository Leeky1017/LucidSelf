"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596854
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
    semantic_id="qtbj_v1.0.0_2__二月丁火_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2二月丁火卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月丁火，湿乙伤丁，先庚后甲，非庚不能去乙，非甲不能引丁。庚甲两透，科甲定然。庚透甲藏，亦有生贡。甲透庚藏，异路功名。
  或庚乙俱透，庚必输情于乙，...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月丁火，湿乙伤丁，先庚后甲，非庚不能去乙，非甲不能引丁。庚甲两透，科甲定然。庚透甲藏，亦有生贡。甲透庚藏，异路功名。
  或庚乙俱透，庚必输情于乙，未免贪合，运行金水，一贫彻骨。或庚透乙藏，则不能贪合，乙反引丁，即用乙亦无害，运入木火之乡，自然富贵。用乙者，水妻木子。若尽是乙木，不见一甲，此人富贵不久，因贪致祸，弄巧反拙。且不能承受先人之业。
  或支成木局，有庚透、主清贵。不见庚者、常人。二月乙木司权，必须有庚，有乙无庚，主贫苦无依。用庚者、土妻金子。
  得印旺杀高，大富大贵。或一派水，无一戊制，主贫苦无依。或乙少癸多，有戊出制，反吉。用土者、火妻土子。

- **分字分词释义**：
  - **湿乙伤丁**：潮湿乙木伤害丁火 / 卯月特征 / 湿木无焰
  - **先庚后甲**：先用庚金后用甲木 / 用神顺序 / 核心
  - **去乙引丁**：除去乙木引燃丁火 / 庚甲功能 / 机制
  - **输情于乙**：输送情意给乙木 / 乙庚贪合 / 凶象
  - **贪合**：贪恋合化 / 乙庚相合 / 破格
  - **弄巧反拙**：弄巧成拙 / 贪婪 / 祸患
  - **印旺杀高**：印星旺七杀高 / 杀印相生 / 大贵

- **规范化释义（primary_lang_explained）**：
  二月（卯月）的丁火，湿乙木（卯中乙木）伤害丁火（湿木无焰），先用庚金（财）克乙，后用甲木（印）引丁。没有庚金不能除去乙木的遮蔽，没有甲木不能引燃丁火。庚金和甲木两透，科甲功名是一定的。庚金透出甲木藏支，也有生员贡生。甲木透出庚金藏支，异路功名。
  如果庚金和乙木都透出，庚金必定输送情意给乙木（乙庚合），未免贪合忘克，如果运行金水运，一贫彻骨。如果庚金透出乙木藏支，就不能贪合，乙木反而能引丁（此处有疑，乙通常不引丁，或指乙不伤丁），即使使用乙木也无害，运入木火之乡，自然富贵。用乙木的人，水为妻木为子。如果尽是乙木，不见一个甲木，这人富贵不长久，因贪婪招致祸患，弄巧成拙，且不能承受先人的基业。
  如果地支合成木局，有庚金透出，主清高富贵。不见庚金的人，常人。二月乙木当权，必须有庚金，有乙木无庚金，主贫苦无依。用庚金的人，土为妻金为子。
  如果得到印旺杀高（杀印相生），大富大贵。如果一派水（官杀），没有一个戊土（伤官）制约，主贫苦无依。如果乙木少癸水多，有戊土出干制水，反而吉利。用土的人，火为妻土为子。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the 2nd Month (Rabbit Month): Wet Yi Wood harms Ding; first use Geng, then Jia. Without Geng, Yi cannot be removed; without Jia, Ding cannot be ignited. If Geng and Jia are both revealed, Civil Service is certain. Geng revealed and Jia hidden implies a Student/Tribute Scholar. Jia revealed and Geng hidden implies alternative fame.
  If Geng and Yi are both revealed, Geng conveys affection to Yi, inevitably greedy for combination; if Luck enters Metal/Water, one is poor to the bone. If Geng is revealed and Yi hidden, they cannot combine; Yi conversely supports Ding (or is harmless); entering Wood/Fire Luck brings natural wealth and nobility. Using Yi takes Water as Wife, Wood as Child. If it is all Yi Wood without a single Jia, wealth is not lasting; greed brings disaster, cleverness ends in clumsiness, and ancestral heritage cannot be kept.
  If branches form a Wood frame, having Geng revealed implies pure nobility. Without Geng, ordinary. In the 2nd Month, Yi commands; Geng is essential. Having Yi without Geng implies poverty and helplessness. Using Geng takes Earth as Wife, Metal as Child.
  Obtaining Prosperous Seal and High Killing implies great wealth and nobility. If a mass of Water appears without Wu to control, it implies poverty. If Yi is scarce and Gui abundant, having Wu to control is auspicious. Using Earth takes Fire as Wife, Earth as Child.

- **核心要点**：
  - **湿乙伤丁**：卯月乙木当令，湿木不能生火，反晦火光。
  - **去乙引丁**：喜庚金劈乙（制乙），喜甲木引丁（正印）。
  - **贪合**：乙庚透干相合，庚贪合忘克，破格。
  - **印局用财**：木局泛滥，必用庚财损印。

- **详细解说**：
  - 丁火在卯月是病地（因湿乙晦火）。
  - 甲木是丁火的嫡母，乙木是庶母。丁火喜嫡母（甲）引火，怕庶母（乙）塞火。
  - 庚金在此月的作用是“裁切”，类似修剪花草，让光透进来。
  - “印旺杀高”：指水生木旺，若有庚金制木生水，循环有情。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_267]` `[trigger: 卯月丁火]` `[factor_trigger: month_mao AND tiangan_ding AND tiangan_geng AND tiangan_jia AND wet_yi_harms]` `[role: 主干]` 二月丁火，湿乙伤丁，先庚后甲，非庚不能去乙，非甲不能引丁。 → 《穷通宝鉴·三春丁火》#16.2
  - `[ns_qttbj_268]` `[trigger: 乙庚贪合]` `[factor_trigger: month_mao AND tiangan_ding AND tiangan_yi AND tiangan_geng AND yi_geng_greedy]` `[role: 例外处理]` 庚乙俱透，庚必输情于乙，未免贪合，运行金水，一贫彻骨。 → 《穷通宝鉴·三春丁火》#16.2
  - `[ns_qttbj_269]` `[trigger: 弄巧反拙]` `[factor_trigger: month_mao AND tiangan_ding AND yi_multiple AND NOT tiangan_jia AND clever_foolish]` `[role: 例外处理]` 尽是乙木，不见一甲，此人富贵不久，因贪致祸，弄巧反拙。 → 《穷通宝鉴·三春丁火》#16.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 二月丁火（卯月）"
    factor_refs: list = ['wet_yi_harms', 'conveying_affection', 'clever_foolish']
    
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
        l1_anchor="qtbj_v1.0.0_2__二月丁火_卯月_001_L1",
    )
    version: str = "1.0.0"
