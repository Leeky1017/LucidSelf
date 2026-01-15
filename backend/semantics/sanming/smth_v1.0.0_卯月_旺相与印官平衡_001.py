"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288806
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
    semantic_id="smth_v1.0.0_卯月_旺相与印官平衡_001",
    book_id="sanming",
    engine_id="bazi"
)
class 卯月旺相与印官平衡(SemanticEntry):
    """
    - **原文（source_text）**：
  卯月。甲日得卯，旺相；乙日得卯，建禄，甲乙生卯月诸格无取，只利得身强命长，颇宜带时上偏官及诸不见之形，贵；偏官者，甲日庚时申时、乙日辛时酉时。若年日时...
    """
    
    original_text: str = """- **原文（source_text）**：
  卯月。甲日得卯，旺相；乙日得卯，建禄，甲乙生卯月诸格无取，只利得身强命长，颇宜带时上偏官及诸不见之形，贵；偏官者，甲日庚时申时、乙日辛时酉时。若年日时三宫无此，其命平常，原带偏官，喜合，忌正官运。丙丁日为印，喜露官印二星，忌天财运同。戊日为正官，喜坐财露官、三合六合、身旺，忌煞伤，官爱多合，运身旺喜财官、身弱喜旺，忌七煞伤官。己日为偏官，喜身旺有合，无则要制，忌身弱无合及露正官，运喜忌同。庚辛日为财，喜透自旺，不坐寅卯日，难为财，忌坐劫露比，运身旺喜财、身弱喜旺，忌劫比同。壬癸日为长生财，喜坐露财，如柱无财，便不是长生财，只是伤官背禄；月令颇宜带时上偏官，如壬日戊时巳时、癸日巳时午时，须是带诸不见之形，贵；运身旺喜财，身弱喜旺，带偏者官，喜合偏官，忌劫财、正官。

- 分字分词释义：
  - **旺相 / 建禄**：卯月为春木正旺之地，甲得旺相、乙得建禄，主身强气足。
  - **时上偏官**：通过时柱庚申、辛酉等形成偏官格，为卯月木盛命局增添贵气路径。
  - **天财运**：指偏财、横财过盛之运，对印星为用时反成损害。
  - **长生财（卯月）**：壬癸在卯月以木为财，是水之长生之地，须财透而有根方为真长生财。
  - **不见之形**：刑冲会合等隐伏结构不显于天干，需要从地支整体结构识别。

- 规范化释义（primary_lang_explained）：
  卯月为仲春时节，木气正盛，甲乙日在此多以「身强命长」为主色调。原文指出，卯月本身格局不另立贵格，甲日得卯为旺相、乙日为建禄，更多是打下坚实身根，因此需配合时上偏官与诸不见之形才能成就显要；若年日时三宫皆无此，则多是长寿而平常。丙丁日得卯为印：身旺且官印双露时，有利于学业、科第与名望，若反行天财之运，则易以财坏印，学识反成工具。戊日于卯为正官，己日为偏官：前者着重于财官相生与三合六合，后者则需身旺并有合或制，避免偏官失控。庚辛日得卯为财：财透而身旺则利经营与拓展，若坐劫、透比，则易劫财成耗。壬癸日于卯为长生财：财坐卯位且透出，方可论长生财；若财不显、只见伤官，则成「伤官背禄」。


- **完整对等诠释（secondary_lang_full）**：
  Mao month lies in mid‑spring, when wood qi is at its fullest. For Jia and Yi the text says there is no special noble pattern in the month itself: Jia merely gains prosperity, Yi gains establish‑salary, and the main gift is a solid, enduring body. Whether this becomes rank depends on what stands in the hour and hidden branches; when partial‑official patterns and other noble forms appear there, the chart upgrades to "strong with honour", otherwise it is mostly longevity and stamina.
  Bing and Ding treat Mao as a seal month. When proper officials and seal both appear and the day stem is strong, this supports education, examinations and reputation; running into heavy windfall wealth fortunes at such times, however, tends to damage the seal and turn learning into a consumable asset. Wu in Mao is proper‑official and Ji is partial‑official, both requiring a robust body: proper‑official likes clear wealth‑official combinations and harmonious triple or sextile unions, while partial‑official must either be tightly merged or properly controlled to avoid becoming rogue. For Geng and Xin, Mao is a direct wealth month: exposed wealth with a strong self favours enterprise and expansion, but sitting on Blades or heavy peers simply leads to competition and loss. Ren and Gui see Mao as another long‑life wealth position only when wood‑wealth is clearly revealed and rooted; if wealth is not visible and Hurting Officers dominate, the pattern is re‑classified as "talent that cannot bear salary" rather than a true wealth configuration.

- 核心要点：
  - 卯月对甲乙的贡献主要是身根，而非直接贵格：贵多由时上偏官与地支隐格承载。
  - 丙丁、戊己在卯月的成败关键，在于印与官能否在不被偏财破坏的前提下稳定显露。
  - 壬癸的长生财结构必须有财透且不被劫伤，不能因「长生」二字而自动视为高收益标签。

- 应用推演（操作顺序）：
  1) 判盘时识别卯月，并对甲乙标记为「身根月」，对壬癸标记为「长生财潜力月」，对戊己、庚辛标记为官月/财月。
  2) 检查时柱与日时中是否有偏官格或其他贵格，区分「身旺平常」与「身旺兼贵格」两类命局。
  3) 对丙丁、戊己，重点分析官印与财星的关系：印为用时忌偏财过重，官为用时忌七煞与伤官混杂。
  4) 在行运模拟中，将卯月对应的春木运标记为「身根激活与印官运作期」，对长生财格局同时记录「财透/不透」「劫比多寡」等，用于调节收益与风险预估。

- 反例与边界：
  - 不宜一见卯月甲乙就论「必有文名贵显」，原文明言若三宫无格，则仅得身强命长而已。
  - 不可把长生财等同于巨额财富，尤其在财不透或比劫重重时，应回退为中性甚至风险标签。
  - 工程实现中若只按「是否卯月」给出文化/教育倾向标签，会忽略其它四柱与实际环境对职业路径的修正。
  - 反向误区是忽视卯月的身根价值，只看眼前财官，而不重视其对长期承载力与恢复力的影响。

- 小例（示意）：
  - 某乙日命局生于卯月，时上辛酉偏官合，行运合偏官之乡，系统可标记为「身根坚实、偏官有格」：适合长期在制度体系内爬升，而非追求短期投机。
  - 另一命局壬日生于卯月，财不透而伤官重，行运再入火木旺地，系统则标记为「长生财不成、重伤官」：适合发挥创意与表达，但在传统官场或刚性结构中要谨慎。"""
    normalized_text_zh: str = """"""
    subject: str = "卯月：旺相与印官平衡"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'mao_month_prosperous_establish', 'bazi_semantic', 'hour_partial_official_noble', 'bazi_semantic', 'windfall_harms_seal_risk', 'bazi_semantic', 'official_seal_both_revealed', 'bazi_semantic', 'hidden_noble_forms', 'bazi_semantic', 'source_ref', 'rel_smth_04_025', 'mao_month_prosperous_establish', 'rel_smth_04_026', 'windfall_harms_seal_risk', 'rel_smth_04_027', 'hidden_noble_forms', 'evi_smth_04_025', 'mao_month_prosperous_establish', 'rule_mao_prosperous', 'evi_smth_04_026', 'official_seal_both_revealed', 'rule_official_seal', 'evi_smth_04_027', 'hidden_noble_forms', 'rule_hidden_noble', 'map_smth_04_017', 'map_smth_04_018']
    
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
        l1_anchor="smth_v1.0.0_卯月_旺相与印官平衡_001_L1",
    )
    version: str = "1.0.0"
