"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288866
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
    semantic_id="smth_v1.0.0_申月_偏官与长生财之枢纽_001",
    book_id="sanming",
    engine_id="bazi"
)
class 申月偏官与长生财之枢纽(SemanticEntry):
    """
    - **原文（source_text）**：
  申月。甲日申月为偏官，喜身旺合制，忌身弱正官，运亦然，尤忌再见七煞。乙日申月为正官，喜身旺、露官见财、三合六合，忌七煞伤官，官爱多合，运身旺喜财、官，...
    """
    
    original_text: str = """- **原文（source_text）**：
  申月。甲日申月为偏官，喜身旺合制，忌身弱正官，运亦然，尤忌再见七煞。乙日申月为正官，喜身旺、露官见财、三合六合，忌七煞伤官，官爱多合，运身旺喜财、官，弱喜旺，忌七煞伤官。丙丁日为财官，丙见壬为七煞，丁见壬为正官，喜身旺露财官，忌伤七煞，运身旺喜财，弱喜旺，忌劫、财。戊己日为长生财，如柱中不带财露，便不是，只是伤官，月令宜时带偏官及诸贵格，月令中虽有长生水为财，内有戊土为害，运喜行长生财为妙，身强喜财，弱喜旺，时偏官喜合制，运忌正官身弱。庚日为建禄，辛为旺相，月中无物可取，只是身旺年长，颇宜时带偏官及日时诸贵格，有偏官喜合或制，忌正官，运亦然。壬癸日为印，喜露官透印，忌财，运亦如之。

- 分字分词释义：
  - **偏官 / 正官**：甲在申为偏官，乙在申为正官，代表不同类型的权力来源与约束结构。
  - **长生财（申月）**：戊己在申月以壬水为长生财，需财透而不被戊土混浊。
  - **建禄 / 旺相（申月）**：庚在申建禄、辛在申旺相，强调身强年长而不一定自带显贵。
  - **印透官明**：壬癸日以印为主，喜官透印协同发挥，忌财扰乱。

- 规范化释义（primary_lang_explained）：
  申月属金，兼带壬水长生之气，是偏官与长生财并存的枢纽。甲日在申为偏官，乙日在申为正官：前者偏锋、重突破，后者端正、重秩序，二者都要求身旺且有合理的合制，尤其忌身弱而官杀过重。丙丁日在申为财官并见：丙见壬成七煞，丁见壬成正官，若身旺且财官透出，则能以才华换取权力与资源；若伤七煞过重，则易陷争执与风险。戊己日在申取长生财：需水财显露且不被戊土混浊，否则只剩伤官之气。庚辛日在申，多主身强年长、根基牢固，贵格则多赖偏官与贵格来激活。壬癸日在申以印为主：喜官透印、财少来耗，可借金气之清肃形成「师表」或「专业权威」类型。

- **完整对等诠释（secondary_lang_full）**：
  Shen month belongs to metal and also carries the birth of Ren‑water, so it becomes a hinge between harsh officials and long‑life wealth. Jia in Shen is partial‑official and Yi in Shen is proper‑official: the former is sharper and more disruptive, the latter more orderly and institutional. Both require a strong body and well‑designed merges and controls; heavy officials sitting on a weak stem are repeatedly described as dangerous. For Bing and Ding, Shen brings both wealth and officials into play: Bing meeting Ren forms Seven Killings, Ding meeting Ren forms proper‑official, so much depends on whether the person is strong enough and whether wealth and officials are clearly revealed rather than mixed with damaging stars.
  Wu and Ji treat Shen as a long‑life wealth month. They only truly gain that status when water‑wealth is visible and not muddied by heavy Wu‑earth; otherwise the same pattern is read as Hurting Officer without real financial root. Geng and Xin treat Shen as a build‑salary and flourishing position that gives a firm metal root rather than automatic rank, while Ren and Gui experience it as a pure seal month: officials that show cleanly and a bright, undisturbed seal can produce a serious professional or teacher‑type figure. Overall, Shen month is where metal hardens the structures of office, wealth and seal: good patterns become firmly established, and confused ones have their problems fixed in place.

- 核心要点：
  - 申月的关键是「官煞与长生财的平衡」：身旺、有合制、有印护者，官煞可化为权；身弱或制化不当，则官煞成压。
  - 长生财格局必须避开戊土混浊与伤官夺财，否则形同「财名虚设」。
  - 庚辛在申月提供的是身根与承载力，不应机械视为必贵，需结合时柱与行运的偏官格一并判断。

- 应用推演（操作顺序）：
  1) 判盘时识别申月，对甲乙标记为偏官/正官月，对戊己标记为长生财月，对庚辛标记为建禄/旺相月，对壬癸标记为印月。
  2) 分析官煞、财、印的透伏状态，并记录是否有合制结构，特别标记「身弱+官煞重」组合为高风险。
  3) 对戊己的长生财，检查水财是否透出、是否被戊土混浊，编码为「长生财成格/不成格」两类特征。
  4) 在行运模拟中，将申金相关运标记为「官煞活跃期」，对有印护且身旺者增权力机会权重，对身弱者提高冲突与压力风险的预警。

- 反例与边界：
  - 不宜将一切申月命一律视作「官多必贵」，需先判断身旺与制化情况。
  - 不可将一切七煞结构视为大贵，原文也反复强调身弱无制者多夭或多祸。
  - 工程实现中若仅以「申月=金旺=官煞强」来生成标签，会误判许多以印为用、以财为辅的命局。
  - 反向误区是过度厌恶偏官，一见申月偏官格就全面降权，而忽视合制与印护带来的正向贡献。

- 小例（示意）：
  - 某甲日命局生于申月，身旺、有偏官合制且印星在旁，行运再入金水之乡，系统可标记为「偏官有制、权责相当」：适合担任决策与执行兼备的岗位。
  - 另一命局戊日申月，水财伏而不透、戊土重且伤官显，行运再逢官杀，系统则标记为「长生财不成、伤官破财」：适合回避高风险投机，偏向稳健经营。"""
    normalized_text_zh: str = """"""
    subject: str = "申月：偏官与长生财之枢纽"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'shen_month_official_wealth_pivot', 'bazi_semantic', 'partial_proper_official_pivot', 'bazi_semantic', 'long_life_wealth_pivot', 'bazi_semantic', 'seal_official_clear', 'bazi_semantic', 'wu_earth_muddy_risk', 'bazi_semantic', 'partial_official_merge_control', 'bazi_semantic', 'source_ref', 'rel_smth_04_040', 'partial_proper_official_pivot', 'rel_smth_04_041', 'long_life_wealth_pivot', 'rel_smth_04_042', 'seal_official_clear', 'evi_smth_04_040', 'partial_proper_official_pivot', 'rule_shen_official', 'evi_smth_04_041', 'wu_earth_muddy_risk', 'rule_wu_muddy', 'evi_smth_04_042', 'seal_official_clear', 'rule_seal_clear', 'map_smth_04_027', 'map_smth_04_028']
    
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
        l1_anchor="smth_v1.0.0_申月_偏官与长生财之枢纽_001_L1",
    )
    version: str = "1.0.0"
