"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288781
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
    semantic_id="smth_v1.0.0_丑月_杂气官财与自库之月_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丑月杂气官财与自库之月(SemanticEntry):
    """
    - **原文（source_text）**：
  丑月。甲乙日得丑月为杂气官，贵，喜官星透干；不透要冲，既透怕冲。运喜行财，忌官藏无冲、官煞混及伤官，官爱多合，身旺喜财官运，身弱喜行旺地，忌煞伤岁同。...
    """
    
    original_text: str = """- **原文（source_text）**：
  丑月。甲乙日得丑月为杂气官，贵，喜官星透干；不透要冲，既透怕冲。运喜行财，忌官藏无冲、官煞混及伤官，官爱多合，身旺喜财官运，身弱喜行旺地，忌煞伤岁同。丙丁日为杂气财，喜财透干，忌羊刃、比肩，运身旺喜财，身弱喜旺通，忌劫、财，若不遇申酉丑日生，难为财。戊己日为余气财，月初小寒后七日半生，有癸水余气，无比肩败财，羊刃亦能发财，贵；如过期生，丑中无利无害，平平，日时二宫能带诸贵格，亦可发；有余气财贵者，喜财露身旺，忌财衰身弱，运喜忌同。庚辛日为自库之月，只得身强、少病、多安、寿考，月令中更无物可采，颇宜时偏官贵，及带日时诸不见之形，依然发福，时偏官庚日丙时巳时，辛日丁时午时，运喜行合偏官，忌正官。壬癸日为杂气财，贵，喜透印见官及刑冲，忌印伏，运宜行官印之地，忌财伤印，余同前论。

- 分字分词释义：
  - **杂气官 / 杂气财**：丑支含癸辛己等复合气，甲乙得之为杂气官，丙丁、壬癸得之为杂气财，皆非纯粹单一之象。
  - **余气财**：丑月小寒后尚存癸水余气，戊己日在此阶段得以取财，过期则气尽而成平常之土。
  - **自库之月**：庚辛在丑月自坐金之墓库，偏重身强、少病、长寿，而非直接外显之贵。
  - **官藏无冲**：官星藏于支中而无冲开，难以为用，容易形成「有名无实」。
  - **刑冲动印**：壬癸日得丑为杂气财，反以透印见官及刑冲来激活局势，忌印伏不行。

- 规范化释义（primary_lang_explained）：
  丑月为寒土兼蓄余水之地，各日主在此月得到的，多是「混合气」的官或财。甲乙日得丑，为杂气官：官星藏于丑中，若能透干，则有贵气可取；若不透则须靠冲动丑土以发用，一旦透出又怕再被冲碎，体现「不透要冲，既透怕冲」的两难。此时运势宜行财运，以财来滋官；若官藏而无冲、官煞混杂或伤官过重，则多是官名不实。丙丁日得丑为杂气财：财透干则利可图，若被羊刃、比肩环绕，则多为劫财之象，原文并点出「不遇申酉丑日生，难为财」，强调需要金局来承财。戊己日在小寒后七日半前，得癸水余气，为余气财：此期内无比肩夺财、即便带羊刃亦可发财；过此之后则丑中难有财利，唯有日时贵格方可发。庚辛日在丑月被视为自库之月：格局重在身强少病、多安寿考，富贵则多仰赖时上偏官与隐伏贵格。壬癸日得丑为杂气财：要靠印透、见官及刑冲来活局，若印星伏藏不现，财反易伤印。


- **完整对等诠释（secondary_lang_full）**：
  In Chou month the earth is cold and damp, storing leftover water and mixed qi. For Jia and Yi this produces a "mixed‑qi official" rather than a clean, single official star: the authority is tucked inside the branch. If that official emerges clearly on the stem it can be used; if it stays hidden it must be knocked open by clashes, and once it has shown itself further violent clashes tend to damage it. The text therefore describes the awkward rule "when hidden it needs clash, when revealed it fears clash" and recommends walking wealth fortunes so that wealth can nourish the official configuration.
  For Bing and Ding the same Chou branch becomes mixed‑qi wealth. Wealth that appears on the stems, especially in metal months and days, can support real resources and careers, but when surrounded by Goat Blade and peer stars it is mostly fought over and lost. Wu and Ji temporarily enjoy "residual‑qi wealth" from the bit of Gui‑water still left just after Minor Cold; during roughly the first seven and a half days after that node, if there are no peers seizing wealth, even Blades can coincide with gain, whereas later births find only ordinary earth with little financial force unless other noble patterns appear. Geng and Xin treat Chou as a self‑storage month: the benefit is a sturdy, long‑lived body with few illnesses, while visible rank and wealth usually have to come from partial‑official and noble patterns at the hour. Ren and Gui again take mixed‑qi wealth here, but the wealth only truly works when seal and official are also visible and the branch is stirred; if seal remains buried, the same structure easily becomes "wealth that harms seal", consuming learning and support instead of strengthening them.

- 核心要点：
  - 丑月以「寒湿之土藏水」为主，更多提供的是「混合气」的官与财，不如纯官月、纯财月那样直接。
  - 甲乙取杂气官，关键在官星是否透干以及冲合是否得宜；丙丁、壬癸取杂气财，则在于财能否显现而不被比劫、伤官破坏。
  - 庚辛在丑月偏重自库与体质，现实判断中宜更多看健康、寿命与抗压能力，而将显贵寄托于时柱与其它贵格。

- 应用推演（操作顺序）：
  1) 判盘时先识别是否生于丑月，并标记各日干在此月对应为杂气官、杂气财、余气财或自库等类型。
  2) 检查官、财是否透干，及是否存在「不透要冲、既透怕冲」的结构：无透而有冲者，可标记者为「需外力激发」；透而再冲者，则为「易损官财」高风险结构。
  3) 对戊己日重点评估出生时节（小寒前后）与比肩、羊刃的数量，编码为「余气财可用 / 余气已尽」两类标签。
  4) 结合庚辛、壬癸在丑月的自库与杂气财特点，将健康寿命倾向、隐伏偏官贵格等信息纳入特征，用于长周期发展与风险评估。

- 反例与边界：
  - 不宜将丑月一概视为「土旺不利」或「不出贵」，原文明确指出杂气官、余气财与自库月中仍有发福路径。
  - 不可把「不透要冲、既透怕冲」简单理解为矛盾，而忽略其背后「激活 vs 破坏」的不同场景与程度。
  - 工程实现中若只用「是否杂气」作为降权标签，会错失一批依靠时上贵格、自库身强而稳健发展的样本。
  - 反向误区是过度迷信库月长寿，将所有庚辛丑月命局都视为健康无忧，而不看其它四柱与行运对体质的修正。

- 小例（示意）：
  - 某甲日命局生于丑月，官星透干且行财运，系统可标记为「杂气官得用」：虽起步不显，但在结构与制度环境中有稳步上升的可能。
  - 另一命局庚日生于丑月，自库身强而时柱偏官有合制，行运合偏官之地，系统则识别为「体质稳健、自库逢贵」：适合在稳定大机构中承担长期责任，发福较迟而绵长。"""
    normalized_text_zh: str = """"""
    subject: str = "丑月：杂气官财与自库之月"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'chou_month_mixed_qi', 'bazi_semantic', 'mixed_qi_transparent_hidden', 'bazi_semantic', 'residual_qi_wealth_timing', 'bazi_semantic', 'self_storage_strong_body', 'bazi_semantic', 'official_hidden_no_clash_risk', 'bazi_semantic', 'seal_official_clash_activate', 'bazi_semantic', 'source_ref', 'rel_smth_04_019', 'mixed_qi_transparent_hidden', 'rel_smth_04_020', 'residual_qi_wealth_timing', 'rel_smth_04_021', 'self_storage_strong_body', 'evi_smth_04_019', 'mixed_qi_transparent_hidden', 'rule_transparent_hidden', 'evi_smth_04_020', 'residual_qi_wealth_timing', 'rule_residual_qi_timing', 'evi_smth_04_021', 'self_storage_strong_body', 'rule_self_storage', 'map_smth_04_013', 'map_smth_04_014']
    
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
        l1_anchor="smth_v1.0.0_丑月_杂气官财与自库之月_001_L1",
    )
    version: str = "1.0.0"
