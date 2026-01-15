"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288855
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
    semantic_id="smth_v1.0.0_未月_自库身根与杂气官财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 未月自库身根与杂气官财(SemanticEntry):
    """
    - **分字分词释义**：
  - **自库月（未月）**：甲乙在未月自成身库，主身强少病，但福分多依赖其它柱与运势。
  - **杂气印 / 杂气官 / 杂气财**：未支含乙丁己三气，对丙丁、戊己、...
    """
    
    original_text: str = """- **分字分词释义**：
  - **自库月（未月）**：甲乙在未月自成身库，主身强少病，但福分多依赖其它柱与运势。
  - **杂气印 / 杂气官 / 杂气财**：未支含乙丁己三气，对丙丁、戊己、庚辛、壬癸分别呈现印、官、财与余气财。
  - **禄马同乡**：壬癸在小暑七日半后得丁余气，形成禄马同乡格，主财禄与行动力并举。
  - **伤为福之地**：原为福地的宫位被伤官或七煞破坏，导致好处难以保全。

- 规范化释义（primary_lang_explained）：
  未月为夏末土旺之时，内藏木火土之气，甲乙日在此自成身库：身强少病，但月令本身无明显财官可用，需要通过时上偏官与诸贵格来承接贵气。丙丁日在未月取杂气印：官印透出时利于权位与名声；印伏不露且行财运时，则易「财坏印」，能力被短期利益消耗。戊己日在未月为杂气官：身旺、财官透出且官不伏藏时可论贵；若官伏无冲或与煞、伤官混杂，则多是非与波折。庚辛日在未月，多主身根牢固、根基深厚，贵格则多赖偏官与贵格来激活。壬癸日在未月以印为主：喜官透印、财少来耗，可借金气之清肃形成「师表」或「专业权威」类型。

- **完整对等诠释（secondary_lang_full）**：
  Wei month belongs to late summer, when earth is strong and wood and fire are stored within it. For Jia and Yi this is a classic self‑storage month: the person tends to be sturdy and relatively healthy, but the month itself contributes little obvious wealth or office, so real advancement depends on partial‑official and other noble patterns at the hour and on later fortunes. Bing and Ding take Wei as mixed‑seal: when officials and seal both appear clearly, power and reputation are supported; when seal hides and the person walks pure wealth fortunes, the text warns of "wealth harming seal", where immediate gain erodes long‑term study and backing.
  Wu and Ji see Wei as mixed‑official: with a strong body and wealth and official both revealed, this can make a solid official structure; if officials are buried with no clash or are entangled with harsh stars and Hurting Officers, quarrels and reversals dominate instead. Geng and Xin treat Wei as mixed‑wealth: exposed, strong wealth with a sturdy self suits managing, saving and building assets, but hidden wealth surrounded by peers and Blades mainly signals effort with little retained. Ren and Gui here are also read as mixed‑wealth. When the person is strong and there is sound merging and control, both can signal real power; when the body is weak and officials or killings pile up without support, the same configuration becomes a burden, so later fortunes heavy in officials and killings are treated with caution rather than optimism.

- 核心要点：
  - 未月集中体现「身库 + 杂气官财」的特征：身强是基础，但财官印多依赖日时与运势的激活。
  - 对甲乙而言，自库本身不保证贵，只保身强；对壬癸而言，小暑前后与是否形成禄马同乡，是判断财禄水平的关键节点。
  - 杂气官、杂气财判断中需重点关注「透/伏」「冲/不冲」以及煞、伤官是否混入。

- 应用推演（操作顺序）：
  1) 判盘时识别未月，对甲乙标记为「自库身根月」，对丙丁、戊己、庚辛、壬癸分别标记为杂气印、官、财、余气财类型。
  2) 对各日干分别评估财官印的透伏状态及是否被煞、伤官破坏，将「自库+贵格」与「自库+平常」区分开来。
  3) 对壬癸重点计算生日与小暑节气的关系，并统计丁火、比劫数量，以区分「禄马同乡」与普通杂气财样本。
  4) 在行运模拟中，将未月对应的土运视为「身库运」，对身弱者提高修复与稳固功能，对身强有贵格者则视为承接财官的窗口期。

- 反例与边界：
  - 不宜将一切未月甲乙命简单归为「健康长寿、无须担心」，忽略其它四柱与运势对健康和安全的影响。
  - 不可把禄马同乡机械视为暴富标记，仍需结合财星根基与现实环境。
  - 工程实现中若只用「自库」与「杂气」作为粗标签，会误判大量依赖精细结构与时节的命局。
  - 反向误区是过度依赖官杀，忽视身弱状态下官杀过重带来的健康与关系风险。

- 小例（示意）：
  - 某甲日命局生于未月，自库身强且时上偏官有格，行运再入财乡，系统可将其识别为「身库逢贵」：适合在稳定体系中承担长期责任并逐步提升。
  - 另一命局癸日生于未月，小暑后七日半出生且财透、丁火余气足，行运再入财官旺地，系统则标记为「禄马同乡、财动有根」：但仍提醒注意节奏与风险控制。"""
    normalized_text_zh: str = """"""
    subject: str = "未月：自库身根与杂气官财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'wei_month_self_storage_mixed', 'bazi_semantic', 'self_storage_strong_body', 'bazi_semantic', 'mixed_qi_transparent_hidden', 'bazi_semantic', 'salary_horse_hometown', 'bazi_semantic', 'not_bound_by_month', 'bazi_semantic', 'residual_qi_wealth_timing', 'bazi_semantic', 'source_ref', 'rel_smth_04_037', 'self_storage_strong_body', 'rel_smth_04_038', 'salary_horse_hometown', 'rel_smth_04_039', 'not_bound_by_month', 'evi_smth_04_037', 'self_storage_strong_body', 'rule_wei_storage', 'evi_smth_04_038', 'salary_horse_hometown', 'rule_salary_horse', 'evi_smth_04_039', 'not_bound_by_month', 'rule_hour_compensate', 'map_smth_04_025', 'map_smth_04_026']
    
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
        l1_anchor="smth_v1.0.0_未月_自库身根与杂气官财_001_L1",
    )
    version: str = "1.0.0"
