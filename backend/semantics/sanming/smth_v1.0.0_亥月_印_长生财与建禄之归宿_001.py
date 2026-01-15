"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288902
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
    semantic_id="smth_v1.0.0_亥月_印_长生财与建禄之归宿_001",
    book_id="sanming",
    engine_id="bazi"
)
class 亥月印长生财与建禄之归宿(SemanticEntry):
    """
    - **原文（source_text）**：
  亥月。甲乙日得亥月为印，喜露官透印为福，忌财，运亦然。丙日为偏官，有合莫制，有制莫合，喜身旺，忌身弱正官，岁运同。丁日为正官，喜透财、露官、身旺，忌七...
    """
    
    original_text: str = """- **原文（source_text）**：
  亥月。甲乙日得亥月为印，喜露官透印为福，忌财，运亦然。丙日为偏官，有合莫制，有制莫合，喜身旺，忌身弱正官，岁运同。丁日为正官，喜透财、露官、身旺，忌七煞伤官，多合，运亦然。庚辛日为长生之财，如柱中全无财露，只是伤官背禄，月令颇宜时带偏官、日时诸贵格，喜财露自旺，忌无财身弱，运亦然。壬癸日，壬为建禄，癸为旺相，福无可取，只是身旺年久，颇宜时带偏官及日时诸贵格，如得时偏官，运喜行合偏官，忌正官。

- 分字分词释义：
  - **印月（亥月）**：甲乙在亥为印，重在学识、资源与庇护，而非直接财利。
  - **偏官 / 正官（亥月）**：丙在亥为偏官、丁在亥为正官，须以合制与身旺为前提。
  - **长生之财（亥月）**：庚辛在亥以水为财，为金之长生之地，财需透出方能成格。
  - **建禄 / 旺相（水月）**：壬在亥建禄、癸在亥旺相，主身旺年久，贵格仍仰赖时上偏官等结构。

- 规范化释义（primary_lang_explained）：
  亥月为冬水之始，气势深沉流动。甲乙日在此得印，若官星透出并配合印星，则有「官印相生」之福，适合走知识权威或制度内路径；若反以财星为重，则易因财坏印。丙日在亥为偏官，丁日在亥为正官：身旺且有合制时，偏官可化为权柄，正官可成清贵；身弱或制化失当，则官星反成压力与风险。庚辛日在亥为长生之财：财透且身旺时，财源清长，有利于长期积累；若全无财透，则退为伤官背禄，才华多于实利。壬癸日在亥，一个建禄、一个旺相，月令本身只保身旺年久，要成贵还需时上偏官与其它贵格配合，行运以合偏官之地为佳，忌正官过重。

- **完整对等诠释（secondary_lang_full）**：
  Hai month opens winter water and is described as deep, flowing qi gathering at the start of the cold season. Jia and Yi here receive seal: when proper officials also appear and cooperate with seal, this becomes the classic "official and seal mutually supporting" pattern, well suited to academic, professional or institutional careers; emphasising wealth instead easily leads to "wealth harming seal", where the drive for profit undermines learning and protection. Bing in Hai is partial‑official and Ding is proper‑official. Both need a strong day stem and appropriate combinations: partial‑official with good merges can become usable power rather than pure danger, while proper‑official with clear wealth and a firm body can form respectable authority; if the self is weak or control structures fail, these same officials become sources of stress and risk.
  Geng and Xin treat Hai as holding "long‑life wealth" for metal: water is their place of growth, so when wealth stars are actually revealed and the person is strong, this configuration points to long‑running, clean financial potential. If no wealth is visible, the month is downgraded to a Hurting‑Officer‑against‑salary pattern in which skill outruns secure income, and the classics recommend using hour partial‑official and noble forms to upgrade it. Ren and Gui in Hai take build‑salary and prosperous positions for the body itself. On its own this mostly promises stamina and longevity; genuine rank still depends on whether partial‑official at the hour is well‑placed and on whether later fortunes align with it, with heavy proper‑official fortunes being treated as a danger rather than an upgrade.

- 核心要点：
  - 亥月强调「水势初聚下的印与官财结构」：印为根，官为用，财为流，三者需取得平衡。
  - 对甲乙而言，维护印比结构比追财更关键；对庚辛而言，判断长生之财是否成格，是区分「清财」与「伤官背禄」的核心。
  - 壬癸在亥月不宜被简单视作「福厚」，其贵否全看偏官格与行运配合。

- 应用推演（操作顺序）：
  1) 判盘时识别亥月，对甲乙标记为印月，对丙丁标记为官月，对庚辛标记为长生财月，对壬癸标记为建禄/旺相身根月。
  2) 检查甲乙命局中官印关系，判断是「官印相生」还是「财坏印」，并据此影响教育、职业建议权重。
  3) 对庚辛评估财星有无透出与比劫状况，区分「长生清财」与「伤官背禄」，应用于财富与风险模型。
  4) 对壬癸重点考察时上偏官与大运合偏官的情况，将其视为是否能由「身旺年久」转向「贵显担当」的重要开关。

- 反例与边界：
  - 不宜将一切亥月命视作「水多必福」，忽略印、官、财结构的失衡可能。
  - 不可简单把长生之财等同于所有火旺命局，需具体看财是否真正透出与有根。
  - 工程中若只用「亥=水旺」标签，会混淆印为用、财为用、官为用的不同命理模式。
  - 反向误区是轻视亥月在学习、内在资源与国际化视野上的潜力，只关注短期财官成效。

- 小例（示意）：
  - 某甲日命局生于亥月，官印相生而财弱，行运再入水木之乡，系统可标记为「印旺官清」：适合走学术、公职或专业服务路径。
  - 另一命局庚日亥月，财不透而伤官重，行运多入金水之地，系统则标记为「伤官背禄」：宜偏向技术与创造性工作，避免过度依赖传统权力与显性财富路径。"""
    normalized_text_zh: str = """"""
    subject: str = "亥月：印、长生财与建禄之归宿"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'evi_smth_04_049', 'official_seal_mutual', 'rule_hai_seal', 'evi_smth_04_050', 'long_life_wealth_hai', 'rule_hai_wealth', 'evi_smth_04_051', 'wealth_harms_seal', 'rule_hai_risk', 'map_smth_04_033', 'map_smth_04_034', 'engine_id', 'hai_month_seal_wealth', 'bazi_semantic', 'official_seal_mutual', 'bazi_semantic', 'long_life_wealth_hai', 'bazi_semantic', 'wealth_harms_seal', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_亥月_印_长生财与建禄之归宿_001_L1",
    )
    version: str = "1.0.0"
