"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288843
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
    semantic_id="smth_v1.0.0_午月_火旺长生财与官煞测试_001",
    book_id="sanming",
    engine_id="bazi"
)
class 午月火旺长生财与官煞测试(SemanticEntry):
    """
    - **分字分词释义**：
  - **火旺长生财（午月）**：甲乙在午为长生财，丙丁亦在午月得长生财，皆以火旺为背景。
  - **建禄印**：戊己在午月既为印又为建禄，要以丁火透出为印为准，代表根...
    """
    
    original_text: str = """- **分字分词释义**：
  - **火旺长生财（午月）**：甲乙在午为长生财，丙丁亦在午月得长生财，皆以火旺为背景。
  - **建禄印**：戊己在午月既为印又为建禄，要以丁火透出为印为准，代表根基与受托。
  - **正官星 / 偏官星**：午月火旺之中，庚为正官、辛为偏官，壬为正官正财、癸为偏官，体现火对金水的制化关系。
  - **伤益壮**：丁火露出使火性更盛，既能增益表现力，也增加过热与耗损。

- 规范化释义（primary_lang_explained）：
  午月盛夏火旺之极，甲乙在此为财，若己土露出则财根更稳，丁火再露则能强化事业与表现，但须防火太烈伤身。丙丁日自身在午得旺相与建禄，一方面身根极强，一方面也在午月得「长生财」：财星透出时财禄兼得；若财不露，则成为伤官背禄，仅剩才华与劳心。戊己日在午月一面为印、一面为建禄：丁火印星透出时，代表得到支持与托付，适合承担重要职责。庚辛、壬癸在午月则主要围绕官星展开：庚为正官，辛为偏官，壬日既见正官又见正财，癸日凸显偏官之力；身旺且有合制时，午火之强能转为官贵，身弱而官煞重则多为压制与冲克。

- **完整对等诠释（secondary_lang_full）**：
  Wu month is the height of summer, with fire at its peak. Jia and Yi treat Wu as both a wealth position and a place of long‑life wealth: when Ji earth appears as firm ground the wealth has roots, and when Ding shows it adds drive, charisma and public presence, though too much fire can also overheat and exhaust. Bing and Ding themselves stand on prosperous and build‑salary roots here and also receive long‑life wealth. If actual wealth stars are revealed, the combination supports both income and a powerful body; if wealth is absent and only Hurting Officers act, the pattern is re‑read as "talent against salary", where brilliance does not readily translate into secure pay.
  Wu and Ji in Wu month are both seal and build‑salary: the presence of Ding as a clear seal means duty, trust and backing are present, making such charts suited to carrying significant responsibility. For Geng and Xin, as well as Ren and Gui, Wu is largely evaluated through official stars. Geng plays proper‑official, Xin partial‑official, Ren combines proper‑official and proper‑wealth, and Gui again plays partial‑official. When the body is strong and there are good merge‑and‑control relationships, the fierce Wu fire is harnessed into visible office and leadership; when the body is weak and officials or killings pile up without support, the same fire becomes pressure, conflict and overwork. The month therefore tests how much heat and official load a person can truly carry, rather than promising greatness just because fire is strong.
- 核心要点：
  - 午月命局的核心是「火旺环境下的财与官印平衡」：身旺者可承财官之重，身弱者容易被火性环境透支。
  - 长生财格局在午月也需财透与不被伤官覆盖，不能仅凭「午=长生财」字面就判为富格。
  - 官星（庚、壬正官；辛、癸偏官）在火旺之中须有合制与印护，方能转为权柄而非灾祸。

- 应用推演（操作顺序）：
  1) 判盘时识别午月，对甲乙、丙丁标记为「火旺长生财月」，对戊己标记为「建禄印月」，对庚辛壬癸标记为「官煞月」。
  2) 对所有日干评估身强弱，在模型中将「身弱+火旺+官煞重」组合列为高风险标签，提醒可能的过劳与冲突。
  3) 检查财星与印星是否透出，并记录「长生财成格/不成格」「印有无托举」等特征，用于长期职业与财富路径推演。
  4) 在行运模拟中，将午火相关运标记为高能期：对身旺者适度提高晋升与扩大规模的权重，对身弱者则加大健康与关系风险的预警。

- 反例与边界：
  - 不宜一见午月就断「火旺必贵、必有大财」，忽略身弱、财不透或官煞混杂等前提条件。
  - 不可将长生财等同于所有火旺命局，需具体看财星是否真正存在且有根。
  - 工程实现中若只用「午月=高能量标签」来推荐高压职业，会误导部分身弱或水土薄弱的命局。
  - 反向误区是因惧怕火旺而完全回避核心岗位，错失适度承压带来的成长机会。

- 小例（示意）：
  - 某甲日命局生于午月，己土透出为财根，丁火再透为统筹力，行运南方火土，系统可识别为「火旺长生财可承」：适合在高能量职业中长期累积财富。
  - 另一命局壬日午月，官财双透而身弱，又行多重火运，系统则标记为「官财压身」：宜谨慎选择高权力职业，注重团队与制度分担压力。"""
    normalized_text_zh: str = """"""
    subject: str = "午月：火旺长生财与官煞测试"
    factor_refs: list = ['engine_id', 'wu_month_fire_peak', 'bazi_semantic', 'fire_peak_long_life_wealth', 'bazi_semantic', 'establish_salary_seal_config', 'bazi_semantic', 'official_seal_entrust', 'bazi_semantic', 'fire_peak_official_killing_control', 'bazi_semantic', 'harm_official_back_salary_risk', 'bazi_semantic', 'source_ref', 'rel_smth_04_034', 'wu_month_fire_peak_wealth', 'rel_smth_04_035', 'fire_peak_official_killing_control', 'rel_smth_04_036', 'harm_official_back_salary_risk', 'evi_smth_04_034', 'long_life_wealth_pattern', 'rule_wu_long_life', 'evi_smth_04_035', 'official_seal_entrust', 'rule_seal_entrust', 'evi_smth_04_036', 'harm_official_back_salary_risk', 'rule_back_salary', 'map_smth_04_023', 'map_smth_04_024']
    
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
        l1_anchor="smth_v1.0.0_午月_火旺长生财与官煞测试_001_L1",
    )
    version: str = "1.0.0"
