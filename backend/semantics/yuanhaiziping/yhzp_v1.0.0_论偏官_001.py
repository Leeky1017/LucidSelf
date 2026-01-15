"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558869
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
    semantic_id="yhzp_v1.0.0_论偏官_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论偏官(SemanticEntry):
    """
    - **原文（source_text）**：夫偏官者，盖甲木见庚金之类；阳见阳，阴见阴，乃谓之偏官，不成配偶。偏官即七杀，要制伏，盖偏官七杀即小人；小人无知，多凶暴，无忌惮，乃能劳力以养君子，而服役护...
    """
    
    original_text: str = """- **原文（source_text）**：夫偏官者，盖甲木见庚金之类；阳见阳，阴见阴，乃谓之偏官，不成配偶。偏官即七杀，要制伏，盖偏官七杀即小人；小人无知，多凶暴，无忌惮，乃能劳力以养君子，而服役护御君子者。小人也，惟是不惩不戒，无术以控制之，则不能驯伏而为用。有制伏则为偏官，无制伏则为七杀。身旺有制为偏官，身弱无制为七杀。如甲以庚为七杀，喜丙丁制之；乙合之，谓之'贪合忘杀'。

- **分字分词释义**：
  - **偏官/七杀**：克我且阴阳相同者，如甲木见庚金，庚金为甲木之七杀。
  - **不成配偶**：阴阳同性不能配合，故名"偏"，与正官"阴阳配合"相对。
  - **小人**：此处比喻七杀的特性——凶暴无忌惮，但可驯伏为用。
  - **制伏**：用食伤克制七杀，使其不能肆虐。
  - **驯伏**：驯服、驾驭，使七杀为我所用。
  - **有制为偏官/无制为七杀**：七杀有制则化凶为吉，无制则为凶神。
  - **丙丁制之**：以食神（丙）或伤官（丁）克制七杀（庚）。
  - **贪合忘杀**：七杀被劫财所合，贪恋合化而忘记克身，化解七杀之凶。

- **规范化释义（primary_lang_explained）**：偏官（七杀）是克我且阴阳相同者，如抱虎而眠。七杀要制伏，有制则为偏官可贵，无制则为七杀主凶。喜身旺、食伤制、劫财合杀，忌身弱、财生杀、无制伏。七杀有制化为权，身旺行杀运发福，身弱行杀运大凶。

- **完整对等诠释（secondary_lang_full）**：Indirect Officer (Seven Killings) is what-controls-me with same polarity, like embracing tiger while sleeping. Seven Killings requires control/transformation—with control becomes Indirect Officer bringing nobility, without control remains Seven Killings bringing calamity. Favors strong Self, Eating/Injuring controlling, Rob Wealth combining Killing; taboos weak Self, Wealth generating Killing, no control. Seven Killings with control transforms to authority—strong Self meeting Killing cycles brings fortune, weak Self meeting Killing cycles brings great calamity.

- **核心要点**：
  - 偏官/七杀是克我且阴阳相同者，如抱虎而眠
  - 七杀即小人，凶暴无忌惮，但可驯伏为用
  - 有制伏则为偏官可贵，无制伏则为七杀主凶
  - 喜身旺、食伤制杀（如丙丁制庚）
  - 喜劫财合杀，谓之"贪合忘杀"
  - 忌身弱、财生杀、无制伏

- **详细解说**：  
  本条论述七杀（偏官）的性质与制化。七杀是克我且阴阳相同者（如甲木见庚金），"不成配偶"（阴阳不配），故名"偏"。七杀的核心特性以"小人"比喻——"小人无知，多凶暴，无忌惮"，但"乃能劳力以养君子，而服役护御君子者"——意指七杀虽凶但可驯伏为己用，关键在于"制伏"。"有制伏则为偏官，无制伏则为七杀"——这是偏官与七杀的本质区别：有制化则七杀化为权柄成偏官，无制化则七杀肆虐主凶灾。制杀之法主要有二：一是食伤制杀（如甲木以丙丁火制庚金）；二是合杀（如甲木以乙木合庚金，谓"贪合忘杀"）。此条是七杀论的核心理论。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_074]` `[trigger: 七杀定义]` `[factor_trigger: seven_killings]` `[role: 主干]` 偏官者，甲木见庚金之类；阳见阳，阴见阴，乃谓之偏官。 → 《渊海子平·论偏官》
  - `[ns_yhzp_075]` `[trigger: 七杀如小人]` `[factor_trigger: seven_killings]` `[role: 主干依赖]` 偏官七杀即小人；小人无知，多凶暴，无忌惮。 → 《渊海子平·论偏官》
  - `[ns_yhzp_076]` `[trigger: 七杀可用]` `[factor_trigger: seven_killings]` `[role: 主干依赖]` 乃能劳力以养君子，而服役护御君子者。 → 《渊海子平·论偏官》
  - `[ns_yhzp_077]` `[trigger: 七杀需制]` `[factor_trigger: seven_killings]` `[role: 条件分支]` 惟是不惩不戒，无术以控制之，则不能驯伏而为用。 → 《渊海子平·论偏官》
  - `[ns_yhzp_078]` `[trigger: 有制为偏官]` `[factor_trigger: seven_killings]` `[role: 条件分支]` 有制伏则为偏官，无制伏则为七杀。 → 《渊海子平·论偏官》
  - `[ns_yhzp_079]` `[trigger: 食伤制杀]` `[factor_trigger: seven_killings AND eating_god]` `[role: 条件分支]` 如甲以庚为七杀，喜丙丁制之。 → 《渊海子平·论偏官》
  - `[ns_yhzp_080]` `[trigger: 贪合忘杀]` `[factor_trigger: seven_killings AND rob_wealth AND pattern_greedy_combine]` `[role: 总结]` 乙合之，谓之'贪合忘杀'。 → 《渊海子平·论偏官》"""
    normalized_text_zh: str = """"""
    subject: str = "论偏官"
    factor_refs: list = ['seven_killings', 'method_eating_controls_killing_proposal', 'pattern_greedy_combine_forgets_killing_proposal', 'relation_killing_seal_generation_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论偏官_001_L1",
    )
    version: str = "1.0.0"
