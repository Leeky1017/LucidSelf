"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558857
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
    semantic_id="yhzp_v1.0.0_论七杀_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论七杀(SemanticEntry):
    """
    - **原文（source_text）**：
  夫七杀者，亦名偏官，喜身旺合杀、喜制伏、喜阳刃；忌身弱、忌见财，生忌无制。身旺有气为偏官，身弱无制为七杀。凡有此杀不可便言凶？有正官不如有偏官，多有巨...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫七杀者，亦名偏官，喜身旺合杀、喜制伏、喜阳刃；忌身弱、忌见财，生忌无制。身旺有气为偏官，身弱无制为七杀。凡有此杀不可便言凶？有正官不如有偏官，多有巨富大贵之人；惟其身旺合杀为妙。如甲以庚为七杀，喜丙丁制之；乙合之，谓之'贪合忘杀'。七杀却宜制伏，亦不要制之太过；盖物极则反为祸矣！身旺又行身旺之运为福。如身弱又行身弱之乡，祸不旋踵。四柱中元有制伏，喜行七杀运；元无制伏，七杀出为祸。如行身旺乡，更有阳刃，贵不可言；但忌财旺，财能生杀故也。岁运临之，身旺亦多灾；身弱尤甚。甲申、乙酉、丁丑、戊寅、己卯、辛未、癸未，此七日生主杀，性急伶俐、心巧聪明。如见杀多者，主人凶夭贫薄。

- **分字分词释义**：
  - **七杀/偏官**：克我且阴阳相同者，如甲木见庚金，庚金为甲木之七杀。
  - **喜身旺合杀**：身旺能担杀，合杀则化敌为友。
  - **喜制伏**：以食伤制杀，使杀不能肆虐。
  - **喜阳刃**：阳刃帮身抗杀，刃杀相配成大贵格。
  - **忌身弱忌见财**：身弱不堪杀克，财生杀则杀更旺。
  - **身旺有气为偏官**：身强能担则杀化为偏官，可以驯用。
  - **身弱无制为七杀**：身弱无制则杀为凶神，克身为祸。
  - **贪合忘杀**：如甲木七杀庚金，乙木合庚则庚忘克甲，谓之贪合忘杀。
  - **制之太过**：制伏过度则杀无存，失去威权之用。
  - **物极则反**：过犹不及，制杀过度反为祸患。
  - **财能生杀**：财生官杀，财旺则杀更旺，身更危。
  - **七日生主杀**：甲申等七日为"坐杀"日柱，主性急聪明。

- **规范化释义（primary_lang_explained）**：
  七杀亦名偏官，是克我且阴阳相同者。七杀喜身旺合杀、喜制伏、喜阳刃；忌身弱、忌见财、忌无制。"身旺有气为偏官，身弱无制为七杀"——身强能担则化杀为偏官可用，身弱无制则杀为凶神。"有正官不如有偏官，多有巨富大贵之人"——偏官格反比正官格更易大富大贵，因其带权威之气。如甲以庚为七杀，喜丙丁制之（食伤制杀），乙合之则"贪合忘杀"。七杀宜制伏但"不要制之太过，盖物极则反为祸"——制杀过度失其威权。身旺行身旺运为福，身弱行弱运则祸不旋踵。四柱有制伏则喜行杀运，无制伏则杀运为祸。身旺加阳刃"贵不可言"（刃杀相配大贵），但忌财旺（财生杀克身）。甲申乙酉等七日为"坐杀"日柱，主人性急伶俐聪明。杀多者主凶夭贫薄。

- **完整对等诠释（secondary_lang_full）**：
  Seven Killing, also called Partial Officer, is that which controls me with same polarity. Seven Killing favors strong Self with combining Killing, favors subduing, favors Yang Blade; taboos weak Self, taboos seeing Wealth, taboos lacking control. "Strong Self with energy becomes Partial Officer; weak Self without control becomes Seven Killing"—if Self is strong enough to bear it, Killing transforms into usable Partial Officer; if Self is weak without control, Killing becomes a fierce spirit. "Having Direct Officer is not as good as having Partial Officer; many achieve great wealth and nobility"—Partial Officer pattern actually exceeds Direct Officer in producing great wealth and nobility, carrying authoritative energy. Like Jia using Geng as Seven Killing, it favors Bing-Ding controlling it (Eating-Injuring controlling Killing); Yi combining it creates "Greedy Combining Forgetting Killing." Seven Killing appropriately receives control but "should not be controlled excessively, as extreme things reverse into disaster"—excessive control loses its authoritative function. Strong Self running through strong-Self luck brings fortune; weak Self running through weak regions brings disaster instantly. If Four Pillars originally have control, one favors running Killing luck; without original control, Killing luck brings disaster. Strong Self plus Yang Blade creates "nobility beyond words" (Blade-Killing pairing for great nobility), but taboos vigorous Wealth (Wealth generating Killing attacks Self). Jia-Shen, Yi-You and five other days are "sitting-Killing" Day Pillars, indicating quick-tempered, clever, and intelligent nature. Abundant Killing indicates violent death, poverty and thinness.

- **核心要点**：
  - 七杀亦名偏官，克我且阴阳相同者
  - 七杀喜身旺、合杀、制伏、阳刃
  - 七杀忌身弱、见财、无制
  - 身旺有气为偏官，身弱无制为七杀
  - 有正官不如有偏官，多出大富大贵
  - 制杀不可太过，物极则反
  - 身旺加阳刃贵不可言，忌财旺
  - 甲申等七日坐杀，主性急聪明

- **详细解说**：
  本条专论七杀的性质与取用。七杀"亦名偏官"，是克我且阴阳相同者，与正官"阴阳相异"相对。七杀的核心判断是"身旺有气为偏官，身弱无制为七杀"——同样是七杀，身强能担则化为可用的偏官，身弱无制则为克身的凶神。七杀"喜身旺合杀、喜制伏、喜阳刃"——身旺能担，合杀化敌为友，制杀使其不能肆虐，阳刃帮身抗杀。"有正官不如有偏官，多有巨富大贵之人"——这是七杀格的特点，偏官带权威之气，反比正官更易成就大富大贵。"如甲以庚为七杀，喜丙丁制之；乙合之，谓之贪合忘杀"——制杀有食伤制和干合两种方式。但"七杀却宜制伏，亦不要制之太过；盖物极则反为祸矣"——制杀过度则杀无存，失去威权之用，这是命理"中和"之道的体现。"身旺加阳刃，贵不可言"是刃杀格的精要——阳刃帮身抗杀，刃杀相配成大贵格局。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_568]` `[trigger: 七杀定义]` `[factor_trigger: seven_killings]` `[role: 主干]` 夫七杀者，亦名偏官，喜身旺合杀、喜制伏、喜阳刃；忌身弱、忌见财。 → 《渊海子平·论七杀》
  - `[ns_yhzp_569]` `[trigger: 身旺为偏官]` `[factor_trigger: seven_killings AND day_master_strength]` `[role: 主干依赖]` 身旺有气为偏官，身弱无制为七杀。 → 《渊海子平·论七杀》
  - `[ns_yhzp_570]` `[trigger: 偏官出大贵]` `[factor_trigger: seven_killings]` `[role: 条件分支]` 有正官不如有偏官，多有巨富大贵之人。 → 《渊海子平·论七杀》
  - `[ns_yhzp_571]` `[trigger: 贪合忘杀]` `[factor_trigger: seven_killings AND combination AND combination_peach_promiscuity AND pattern_combine_forget_killing]` `[role: 条件分支]` 乙合之，谓之'贪合忘杀'。 → 《渊海子平·论七杀》
  - `[ns_yhzp_572]` `[trigger: 制杀不可太过]` `[factor_trigger: seven_killings AND food_god AND food_god_vigorous]` `[role: 例外处理]` 七杀却宜制伏，亦不要制之太过；盖物极则反为祸矣！ → 《渊海子平·论七杀》
  - `[ns_yhzp_573]` `[trigger: 刃杀大贵]` `[factor_trigger: seven_killings AND yang_blade AND day_master_strength]` `[role: 条件分支]` 如行身旺乡，更有阳刃，贵不可言。 → 《渊海子平·论七杀》
  - `[ns_yhzp_574]` `[trigger: 财生杀忌]` `[factor_trigger: seven_killings AND direct_wealth]` `[role: 条件分支]` 但忌财旺，财能生杀故也。 → 《渊海子平·论七杀》"""
    normalized_text_zh: str = """"""
    subject: str = "论七杀"
    factor_refs: list = ['seven_killings', 'partial_officer', 'pattern_combine_forget_killing', 'pattern_blade_killing_pairing']
    
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
        l1_anchor="yhzp_v1.0.0_论七杀_001_L1",
    )
    version: str = "1.0.0"
