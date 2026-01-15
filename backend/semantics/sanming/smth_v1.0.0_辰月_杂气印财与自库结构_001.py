"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288819
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
    semantic_id="smth_v1.0.0_辰月_杂气印财与自库结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辰月杂气印财与自库结构(SemanticEntry):
    """
    - **原文（source_text）**：
  辰月。甲乙日生辰月为杂气印，喜见官星及印露，不露要冲，既露怕冲，忌见财多伤印，运喜忌同。丙丁日为杂气官，喜官透，不透要冲，见财身强发福，忌官伏无冲及煞...
    """
    
    original_text: str = """- **原文（source_text）**：
  辰月。甲乙日生辰月为杂气印，喜见官星及印露，不露要冲，既露怕冲，忌见财多伤印，运喜忌同。丙丁日为杂气官，喜官透，不透要冲，见财身强发福，忌官伏无冲及煞伤，运身强喜财官，弱喜旺，忌煞伤同。戊己日为杂气财，喜财露旺，不露要冲，忌财伏无冲，坐刃比肩，不坐亥子辰日，难为财，运身旺喜财，弱喜旺，忌劫同。庚辛日为余气财，贵，清明后七日半有乙木余气，方可发，如月初生，无比刃夺财皆可发；过期则辰中无利无害，平平，如日时带诸贵格，亦发；运有余气财，身旺喜财地，忌身弱劫地财衰。壬癸日为自库，只是身强少疾，月令无贵可取，颇宜时上偏官及日时诸不见之形，贵，依然发福，勿拘月令；运如时偏官者，喜行合制，忌行正官、伤官。

- 分字分词释义：
  - **杂气印 / 杂气官 / 杂气财**：辰支含乙癸戊三气，依不同日干可作为印、官或财使用，属性混合。
  - **余气财（辰月）**：庚辛在清明后七日半之前，尚可得乙木余气化为财用，之后则气尽而平。
  - **自库（月令自库）**：壬癸在辰月自坐水之库，偏重身强与健康，而贵格多依赖时柱偏官等隐伏结构。
  - **不露要冲、既露怕冲**：对印、官、财而言，若伏藏则需冲开才有用，若已透则再冲反致破格。

- 规范化释义（primary_lang_explained）：
  辰月为春末土湿之地，内藏木水土三气，因此被称为「杂气」之月。甲乙日在辰月以杂气印论：印伏不露时，需要冲动辰土以发用；一旦印与官星皆透，又怕再遇强冲破坏稳定。丙丁日在辰为杂气官：官透且身强时可发福，若官伏无冲或被煞伤，则难以发挥。戊己日在辰为杂气财：财露旺而不坐刃比时，财星有力；若财伏无冲、或与比肩、羊刃同宫，则容易被夺财。庚辛在辰月得乙木余气，可视为「余气财」：清明后七日半之前、且无比刃夺财者，多主有可观之财运；过期则辰中气尽，只能平平。壬癸在辰月为自库：不直接出贵，但身强少病，若时上偏官与诸不见之形得位，仍可「勿拘月令」而发福。


- **完整对等诠释（secondary_lang_full）**：
  Chen month sits at late spring when the ground is wet and mixed, hiding wood, water and earth together. The text calls it a "mixed‑qi" month: for Jia and Yi it becomes a mixed‑seal position that is useful only if the seal and its accompanying officials are either activated by clashes or clearly revealed. When seal and official have both surfaced, further heavy clashes are feared because they can break what has just been formed, and abundant wealth attacking seal is also warned against. For Bing and Ding, Chen offers mixed‑official power: visible, well‑supported officials with a strong body can bring success, but officials that are buried or struck by harsh stars remain ineffective.
  Wu and Ji read Chen as mixed‑qi wealth: exposed, strong wealth not sitting together with Blades and peers can work well, whereas hidden wealth with no clash or wealth mixed into peer‑heavy branches is easily seized rather than accumulated. Geng and Xin are said to draw "residual‑qi wealth" here from the last traces of Yi‑wood after Qingming; births in roughly the first seven and a half days after that node with little peer competition have a better chance at tangible wealth, while later births meet a branch whose mixed qi has largely dissipated. Ren and Gui in Chen are in a self‑storage position: the main benefit is a robust, low‑illness body, and their nobility, if any, comes from partial‑official patterns and hidden nobles at the hour. The overall principle is that in this month one must carefully distinguish between hidden versus revealed, and between clashes that activate mixed qi and clashes that simply break a fully exposed structure.

- 核心要点：
  - 辰月的核心在「杂气与库」：多种五行混合，使得印、官、财的取用条件增加一层「冲合与时节」判断。
  - 甲乙、丙丁、戊己分别取印、官、财时，都要处理「不露要冲、既露怕冲」的矛盾，工程上应将「是否伏藏」「是否受冲」拆分为独立特征。
  - 庚辛的余气财与壬癸的自库格，显示辰月在财运与健康上的潜在优势，但依赖具体时节与贵格，不可一概而论。

- 应用推演（操作顺序）：
  1) 判盘时识别辰月，并根据日干标记本月为杂气印、杂气官、杂气财或自库类型，作为第一层标签。
  2) 对应地计算「伏藏/显露」与「受冲/不受冲」的组合：如印伏且有冲者记为「可激活印」，印透又多冲者记为「印易破」等。
  3) 对庚辛，检查出生日期是否在清明后七日半前，并统计比肩、羊刃数量，用于区分「余气财充足」与「余气已尽」样本。
  4) 对壬癸，将时上偏官与诸不见之形纳入贵格评估，在行运模拟中将「合制偏官」与「正官、伤官过强」作为不同风险/机会情景编码。

- 反例与边界：
  - 不宜将辰月简单视为「潮湿之土皆不吉」，忽视其中杂气印、余气财、自库结构带来的细微分化。
  - 不可把一切冲动视为破坏，有些伏藏的印、官、财正须冲动才能显用，需结合是否透干与身强弱判断。
  - 工程实现中若不区分「伏藏+冲」与「透出+冲」，只用一个「有冲」特征，会严重混淆激活与破坏两类情形。
  - 反向误区是过分迷信库与余气，一见辰月庚辛、壬癸便大幅升档，而不看具体时令与比劫结构。

  - 小例（示意）：
  - 某庚日命局生于清明后数日之辰月，财透而比劫少，行运再入财地，系统可将其识别为「余气财有根」的格局，适合稳步经营与累积。
  - 另一命局癸日辰月，自库身强但时上偏官被正官、伤官夹攻，行运再逢官杀之乡，系统则标记为「库中有煞、激活风险高」：需在职业发展中谨慎处理与权力、规则相关的抉择。"""
    normalized_text_zh: str = """"""
    subject: str = "辰月：杂气印财与自库结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'chen_month_mixed_storage', 'bazi_semantic', 'mixed_qi_transparent_hidden', 'bazi_semantic', 'residual_qi_wealth_timing', 'bazi_semantic', 'self_storage_strong_body', 'bazi_semantic', 'hidden_needs_clash_activate', 'bazi_semantic', 'revealed_fears_clash_break', 'bazi_semantic', 'source_ref', 'rel_smth_04_028', 'hidden_needs_clash_activate', 'rel_smth_04_029', 'revealed_fears_clash_break', 'rel_smth_04_030', 'self_storage_strong_body', 'evi_smth_04_028', 'hidden_needs_clash_activate', 'rule_hidden_clash', 'evi_smth_04_029', 'revealed_fears_clash_break', 'rule_revealed_clash', 'evi_smth_04_030', 'self_storage_strong_body', 'rule_self_storage', 'map_smth_04_019', 'map_smth_04_020']
    
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
        l1_anchor="smth_v1.0.0_辰月_杂气印财与自库结构_001_L1",
    )
    version: str = "1.0.0"
