"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288890
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
    semantic_id="smth_v1.0.0_戌月_杂气财官与自库收束_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戌月杂气财官与自库收束(SemanticEntry):
    """
    - **原文（source_text）**：
  戌月。甲乙日戌月为杂气财，喜生旺财透，不透要冲，忌财伏无冲、比肩、羊刃，运亦然。丙丁日为自库月，亦主身旺年长，戌中无物可取为福，只宜时带诸贵格为妙，运...
    """
    
    original_text: str = """- **原文（source_text）**：
  戌月。甲乙日戌月为杂气财，喜生旺财透，不透要冲，忌财伏无冲、比肩、羊刃，运亦然。丙丁日为自库月，亦主身旺年长，戌中无物可取为福，只宜时带诸贵格为妙，运亦然。戌己日为杂气印，喜正官印透，不透要冲，忌印伏无冲、有财伤印，运忌伤官、伤印。庚辛日为杂气官，贵，要身旺印全，如官透，冲则用官为贵；印透，冲则用印为贵，不透要冲，忌官伏无冲，官爱多合，运身旺喜财官，身弱喜旺，忌七煞伤官。壬癸日为杂气财，要身旺、财官双全为贵，财透则冲用财，官透则冲用官，不透要冲，忌财伏无冲，运身旺喜财，身弱喜旺，忌劫奈。

- 分字分词释义：
  - **杂气财 / 杂气印 / 杂气官**：戌中含辛丁戊三气，对不同日干分别成财、印、官之用。
  - **自库月（戌月）**：丙丁生戌为自库，多主身旺年长，而贵格要靠时柱等处的贵星。
  - **冲用财 / 冲用官**：财或官伏藏不透时，需靠冲动戌土来激活；一旦透出再冲则可能破格。

- 规范化释义（primary_lang_explained）：
  戌月为秋土，内藏火金土三气，起收束与归库之用。甲乙日在戌为杂气财：财透于干且身旺时，既能聚财又能发挥施展空间；若财伏无冲且比肩、羊刃重，则易财难聚。丙丁日在戌为自库月：身旺年长，但月令本身不直接给福，多借助时上贵格与其它结构来显贵。戊己日在戌为杂气印：正官与印透时格局较高；若印伏而再被财所伤，则印受损，难以稳定发展。庚辛日在戌为杂气官：要身旺且印全，方能承官，官透时宜用官，印透时宜用印；若官伏无冲，则官名不显。壬癸日在戌为杂气财：财官双全时吉，财官俱伏却无冲时多平常，财或官透而再逢冲则要分辨是激活还是破坏。

- **完整对等诠释（secondary_lang_full）**：
  Xu month is autumn earth, a storage and closing phase holding fire, metal and earth together. For Jia and Yi it is mixed‑qi wealth: when wealth is revealed on the stems and the person is strong, they can both gather resources and retain room to act; when wealth is buried with no clash and surrounded by peers and Blades, money is hard to keep. Bing and Ding experience Xu as a self‑storage month: the body tends to be strong and lifespan long, but obvious blessings rarely come directly from the month, and honour usually depends on noble patterns at the hour and the way later fortunes shake the storage open.
  Wu and Ji read Xu as mixed‑seal: high patterns arise when proper‑official and seal both appear, but if seal hides and is further attacked by wealth, the stabilising function of seal is damaged and steady development is difficult. Geng and Xin treat Xu as mixed‑official: they need a strong body and complete seal support to carry official stars; when officials are apparent and moderate clashes simply bring them into use, "using official" becomes the noble path, whereas if officials stay hidden and unshaken their titles remain nominal. For Ren and Gui the same Xu branch is mixed‑wealth again: charts that combine a strong self with both wealth and official functioning are considered noble; charts where both hide with no clash are ordinary, and charts where wealth or official is revealed and then struck must be analysed carefully to distinguish helpful activation from destructive over‑clashing.

- 核心要点：
  - 戌月是「杂气财官与自库收束」之地：更多反映前期积累的收官状态，而非单点起飞。
  - 冲动戌土既可能激活伏藏之财官印，也可能打破已成之格，需结合透伏与身强弱判断。
  - 丙丁自库命不宜被简单视作「难发」，关键在有没有与之相配的时上贵格与行运配合。

- 应用推演（操作顺序）：
  1) 判盘时识别戌月，对甲乙、壬癸标记为杂气财月，对戊己标记为杂气印月，对庚辛标记为杂气官月，对丙丁标记为自库月。
  2) 计算财官印的透伏与冲合状态，将「伏藏+适度冲」「伏藏+无冲」「透出+重冲」分别编码，以区分激活、沉寂、破坏三种局面。
  3) 在自库格的评估中，引入时柱贵格与大运走势，使模型能识别「晚成」与「守成」类型样本。
  4) 行运模拟时，将戌月相关运视为收束期，对既成格局加强稳定和风险评估，而非单一看作上升期或衰退期。

- 反例与边界：
  - 不宜将戌月命统一视为「库中困住」，忽略杂气财官被激活时的上升潜力。
  - 不可把一切冲戌视为破坏，有时正是冲来启用伏藏之财官印。
  - 工程中若不显式区分「伏藏+冲」与「透出+冲」，将难以准确模拟戌月命局的变化。
  - 反向误区是过度期待自库命的「晚发」，在现实中忽视必要的学习与结构性努力。

- 小例（示意）：
  - 某丙日命局生于戌月，自库身旺而时上贵格清晰，行运向官印旺地，系统可标记为「自库晚成」：适合在中年以后承担更大责任。
  - 另一命局壬日戌月，财官伏而多比劫，行运再逢冲戌，系统则标记为「冲财破格风险」：需谨慎面对金融杠杆与高风险项目。"""
    normalized_text_zh: str = """"""
    subject: str = "戌月：杂气财官与自库收束"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'xu_month_mixed_self_storage', 'bazi_semantic', 'mixed_qi_transparent_hidden', 'bazi_semantic', 'clash_use_wealth_official', 'bazi_semantic', 'self_storage_strong_body', 'bazi_semantic', 'self_storage_late_success', 'bazi_semantic', 'not_bound_by_month', 'bazi_semantic', 'source_ref', 'rel_smth_04_046', 'clash_use_wealth_official', 'rel_smth_04_047', 'self_storage_strong_body', 'rel_smth_04_048', 'mixed_qi_transparent_hidden', 'evi_smth_04_046', 'clash_use_wealth_official', 'rule_xu_clash', 'evi_smth_04_047', 'self_storage_late_success', 'rule_xu_late', 'evi_smth_04_048', 'mixed_qi_transparent_hidden', 'rule_xu_hidden', 'map_smth_04_031', 'map_smth_04_032']
    
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
        l1_anchor="smth_v1.0.0_戌月_杂气财官与自库收束_001_L1",
    )
    version: str = "1.0.0"
