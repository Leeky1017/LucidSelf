"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288878
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
    semantic_id="smth_v1.0.0_酉月_正偏官与长生财的定型_001",
    book_id="sanming",
    engine_id="bazi"
)
class 酉月正偏官与长生财的定型(SemanticEntry):
    """
    - **原文（source_text）**：
  酉月。甲日酉月为正官，喜身旺、露官见财、三合六合，忌七煞伤官，官爱多合，运身旺喜财、官，弱喜旺，忌七煞伤官。乙日得酉月为偏官，喜身旺，有合莫制，有制莫...
    """
    
    original_text: str = """- **原文（source_text）**：
  酉月。甲日酉月为正官，喜身旺、露官见财、三合六合，忌七煞伤官，官爱多合，运身旺喜财、官，弱喜旺，忌七煞伤官。乙日得酉月为偏官，喜身旺，有合莫制，有制莫合，忌身弱正官，运亦如之，再忌见七煞运。丙丁日为财，喜身旺露财官、三合六合，忌刑冲破害、比肩、劫财，运身旺喜财，身弱喜旺，忌劫夺。戊己日为长生财，如柱中不带财露，便不是，只是伤官，月令宜时带偏官及诸贵格，偏官格喜合制，运身旺喜财，身弱喜旺，忌劫、财。庚日为建禄，辛为旺相，月中无物可取，只是身旺年长，颇宜时带偏官及日时诸贵格，有偏官喜合或制，忌正官，运亦然。壬癸日为印，喜露官透印，忌财，运亦如之。

- 分字分词释义：
  - **正官 / 偏官（酉月）**：甲得正官、乙得偏官，代表制度化权力与非常规权力两种模式。
  - **长生财（酉月）**：戊己在酉月以壬水为长生财，需财透而不被伤官所夺。
  - **旺相 / 建禄（金月）**：庚在酉旺相、辛在酉建禄，强调金性定型、身根坚实。
  - **官印相生**：壬癸日在印月，喜官透印协同发挥，忌财扰乱。

- 规范化释义（primary_lang_explained）：
  酉月金气极盛，官、财、印三者在金的框架下定型。甲日酉月为正官：身旺、官透、见财且成三合六合时，多主清贵与正当权力；若七煞、伤官混入，则易出现名誉与权力方面的冲突。乙日酉月为偏官：同样要身旺方能承受，偏官有合时宜顺其化解，无合时需加制，最忌身弱而再见正官与七煞运。丙丁日在酉月为财：身旺且财官同透者主富贵；若比肩、劫财与刑冲破害太多，则财难守。戊己日在酉月为长生财：财不透则退为伤官背禄，需通过时上偏官格来提格。庚辛在酉月多主身根牢固，贵格也多赖偏官与贵格来激活。壬癸日在酉月为印：喜官透印、财少来耗，可借金气之清肃形成「师表」或「专业权威」类型。

- **完整对等诠释（secondary_lang_full）**：
  You month is the height of summer, with fire at its peak. Jia and Yi treat You as both a wealth position and a place of long‑life wealth: when they are not themselves born on You or Wu days and when Wu‑earth shows as firm ground the wealth has roots, and when Ding shows it adds drive, charisma and public presence, though too much fire can also overheat and exhaust. Bing and Ding themselves stand on prosperous and build‑salary roots here and also receive long‑life wealth. If actual wealth stars are revealed, the combination supports both income and a powerful body; if wealth is absent and only Hurting Officers act, the pattern is re‑read as "talent against salary", where brilliance does not readily translate into secure pay.
  Wu and Ji treat You as a long‑life wealth month. They only truly gain that status when water‑wealth is visible and not muddied by heavy Wu‑earth; otherwise the same pattern is read as Hurting Officer without real financial root. Geng and Xin treat You as a build‑salary and flourishing position that gives a firm metal root rather than automatic rank, while Ren and Gui experience it as a pure seal month: officials that show cleanly and a bright, undisturbed seal can produce a serious professional or teacher‑type figure. Overall, You month is where metal hardens the structures of office, wealth and seal: good patterns become firmly established, and confused ones have their problems fixed in place.

- 核心要点：
  - 酉月强调「金性定型后的官与财」：身旺是前提，官、财、印结构是否清晰决定了贵贱层级。
  - 正官适合明合与公开，偏官适合合制与柔性处理，工程上要区分不同官星模式。
  - 长生财与伤官背禄的分界依赖财是否透出及是否被比劫、伤官夺用。

- 应用推演（操作顺序）：
  1) 判盘时识别酉月，对甲乙标记为正官/偏官月，对戊己标记为长生财月，对庚辛标记为金性定型月，对壬癸标记为印月。
  2) 分析官、财、印透伏与比劫、伤官状况，将「官清财明」「官煞混杂」「伤官背禄」等模式编码为结构标签。
  3) 在职业与权力路径推演中，对正官格加强「制度角色」权重，对偏官格加强「冲突与谈判」权重，对印格加强「专业/学术」权重。
  4) 行运模拟时，将金旺运视为结构强化期：善格者得以定型，杂乱结构者则风险放大。

- 反例与边界：
  - 不宜将一切酉月命一律视作「官多必贵」，需先检验身强弱与官煞混杂情况。
  - 不可简单把偏官等同于违法或越矩，许多领导与变革型角色恰依赖偏官能量。
  - 工程中若仅用「金旺=刚性」来建模，会忽略印与财对个体发展方向的调节。
  - 反向误区是完全压制偏官与伤官，忽视其在突破、创新和调节中的正向作用。

- 小例（示意）：
  - 某甲日命局生于酉月，官透财现成三合局，行运再入木火之乡，系统可标记为「官清财明」：适合在规则明确的体系中晋升。
  - 另一命局丁日酉月，财透而比劫、刑冲甚重，行运再入金地，系统则标记为「财多而难守」：宜谨慎负债与投资，重视风险管理。"""
    normalized_text_zh: str = """"""
    subject: str = "酉月：正偏官与长生财的定型"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'you_month_metal_defined', 'bazi_semantic', 'metal_nature_defined_state', 'bazi_semantic', 'official_clear_wealth_clear', 'bazi_semantic', 'proper_partial_official_mode', 'bazi_semantic', 'long_life_wealth_pattern', 'bazi_semantic', 'harm_official_back_salary_risk', 'bazi_semantic', 'source_ref', 'rel_smth_04_043', 'metal_nature_defined_state', 'rel_smth_04_044', 'proper_partial_official_mode', 'rel_smth_04_045', 'harm_official_back_salary_risk', 'evi_smth_04_043', 'metal_nature_defined_state', 'rule_you_defined', 'evi_smth_04_044', 'proper_partial_official_mode', 'rule_you_mode', 'evi_smth_04_045', 'harm_official_back_salary_risk', 'rule_you_back', 'map_smth_04_029', 'map_smth_04_030']
    
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
        l1_anchor="smth_v1.0.0_酉月_正偏官与长生财的定型_001_L1",
    )
    version: str = "1.0.0"
