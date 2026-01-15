"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288793
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
    semantic_id="smth_v1.0.0_寅月_建禄旺相与偏官结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 寅月建禄旺相与偏官结构(SemanticEntry):
    """
    - **原文（source_text）**：
  寅月。甲日得寅建禄，乙日旺相，月令中无格可取，只利得身旺年久，颇宜带时偏官及日时诸不见之形，贵；时偏官者，甲日庚时申时、乙日辛时酉时，如年日时三宫无格...
    """
    
    original_text: str = """- **原文（source_text）**：
  寅月。甲日得寅建禄，乙日旺相，月令中无格可取，只利得身旺年久，颇宜带时偏官及日时诸不见之形，贵；时偏官者，甲日庚时申时、乙日辛时酉时，如年日时三宫无格可取，终身可知，有偏官者，喜行合偏官运，忌正官。丙丁日为印，贵，喜坐官露官、再露印星，忌露财，宜行官、印运，忌财、伤印。戊日为偏官，贵，两阳相攻，喜身旺，忌身弱；偏官有合莫制，无合要制，运喜身旺合制，忌身弱正官及再行煞乡。己日为正官，贵，阴阳和合，喜坐露财、再露官星、三合六合、身旺，忌七煞伤官，官爱明合，身旺喜行财官，身弱喜旺，忌七煞偏官。庚辛日为财，喜财多露身旺，忌坐刃透比，身弱不遇寅卯日，难为财运，身旺喜财，身弱喜旺，忌劫同。壬癸日为长生财，喜财透干，忌伏藏，如柱无财透，便不是长生财，只是伤官背禄，月令颇宜时上偏官，壬日戊时巳时、癸日巳时午时，须及年日时诸不见之形，贵，如三宫皆无格，难言好命，运身旺喜财，身弱喜旺，忌身弱正官。

- 分字分词释义：
  - **建禄 / 旺相**：甲得寅为建禄，乙在寅为旺相，主身强气足，为格局之根。
  - **偏官有合莫制，无合要制**：偏官若有合可化，宜顺其合；无合时则须有制，避免煞力过重。
  - **官爱明合**：正官宜有明合而不宜混杂，象征公开、正当的权力关系。
  - **长生财（寅月）**：壬癸在寅月，以木为财，为水之长生之地，财源萌发，要透而有根。
  - **不见之形**：偏官、刑冲、会合等隐伏格局不显于天干，需要通过地支结构分析。

- 规范化释义（primary_lang_explained）：
  寅月为春初木旺之时，甲乙木在此「建禄、旺相」，主身强而寿长，但月令本身不另立贵格，多仰赖时柱与日时中的偏官、诸贵格来成名。甲乙日若在时上得庚申、辛酉偏官相配，再加年日时其他隐格，则可从「单纯身旺」提升为「有贵可取」。丙丁日得寅为印：身旺而官星显露、印星再透时，多主文章与声名；若贪露财星，则印被夺而学业、名望受损。戊日在寅为偏官，己日在寅为正官：两者皆以官格论贵，但戊偏官两阳相攻，必须身旺且有合制，方能化煞为权；己正官则重在阴阳和合、官多明合，不宜七煞伤官混入。庚辛日得寅为财：财多露、身旺者利于经营与拓展；身弱而不见寅卯日，则难以承受财务压力。壬癸日在寅为长生财：财透而不伏藏者，才是真正可用的长生财；若无财透，则多成伤官背禄格，需依靠时上偏官与其他隐格另寻贵路。


- **完整对等诠释（secondary_lang_full）**：
  In Yin month the first spring wood begins to rise, and the chapter stresses that this is more a "root‑building" time than an automatic noble configuration. Jia and Yi here gain establish‑salary or prosperous status: the body and life‑force are strong and often long‑lived, but honour usually depends on what appears at the hour. When hour stems such as Geng‑Shen or Xin‑You form partial‑official patterns and other hidden nobles support them, the chart moves from merely strong to "strong with rank"; without them it is simply a sturdy life.
  For Bing and Ding, Yin functions as a seal month. When the body is robust, proper officials are visible and seal shows again, the text speaks of scholarship, writing and public recognition; if they chase exposed wealth instead, seal is damaged and learning becomes a mere tool. Wu in Yin is partial‑official and Ji in Yin is proper‑official: both can be noble patterns, but partial‑official needs a strong self and good combinations to turn sharpness into usable authority, while proper‑official prefers clear, balanced merges rather than mixed, chaotic structures. Geng and Xin treat Yin as a wealth month that tests capacity: multiple wealth stars on the stems help growth only if the person is strong enough to manage them. Ren and Gui see Yin as a place of long‑life wealth: when wood‑wealth reveals itself and is rooted, this becomes a genuine, renewable resource; when no wealth is visible and only Hurting Officers dominate, the pattern is recoded as talent that undermines salary unless hour partial‑official and hidden nobles open a different path.

- 核心要点：
  - 寅月强调「身根」与「官煞结构」：甲乙得身根，戊己立官格，庚辛壬癸多从财的角度看其可承受度。
  - 偏官与正官需要不同的处理方式：偏官重在「有合莫制、无合要制」，正官则重在「明合而不混杂」，工程上应区别建模。
  - 长生财结构若无财透而仅有伤官，则不宜机械按「长生财」升档，应退为伤官背禄的中性或负面标签。

- 应用推演（操作顺序）：
  1) 判盘时识别是否寅月生，并按日干标记为建禄、旺相、官月或财月，将「身根强弱」作为首要特征记录。
  2) 对戊己、庚辛、壬癸等非木日，重点分析官、财是否透出、是否伏藏，以及偏官、正官的合制关系，编码为不同风险/潜能维度。
  3) 对甲乙、丙丁，记录时柱及日时中是否存在偏官格与诸不见之形，以区分「仅身旺」与「身旺兼贵格」两类样本。
  4) 在行运模拟中，将寅月对应的春木运标记为「身根激活/官煞易动」时期，对偏官格者提高「突破与冲突」的双向权重，对正官格者增强「升迁与责任」权重。

- 反例与边界：
  - 不宜一见寅月甲日就断为「必贵」，原文明确指出若年日时三宫皆无格可取，则只是身旺年久而已。
  - 不可把偏官一律视作凶星，寅月中许多偏官格恰是贵格来源，关键在合制是否得宜。
  - 工程实现中若仅以「是否寅月」或「是否建禄」作为晋升标签，会掩盖身弱、官煞混杂、财透伤印等复杂结构。
  - 反向误区是过度回避官煞，一见寅月偏官就全面降权，而不看其是否已有稳定合制与身旺支撑。

- 小例（示意）：
  - 某甲日命局生于寅月，时上庚申偏官有合，又见年支贵格，行运合偏官之乡，系统可判定为「建禄身强、偏官有制」：适合在需要承担冲锋与决策的岗位上逐步升迁。
  - 另一命局壬日生于寅月，柱中财伏不透而伤官重，行运又多正官，系统则标记为「长生财不成、伤官背禄」：虽有才华与冲劲，但在官场或高度层级化组织中易感压制与失衡，宜往创造性与技术性角色倾斜。"""
    normalized_text_zh: str = """"""
    subject: str = "寅月：建禄旺相与偏官结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'yin_month_establish_prosperous', 'bazi_semantic', 'partial_official_merge_control_strategy', 'bazi_semantic', 'official_clear_merge', 'bazi_semantic', 'long_life_wealth_pattern_condition', 'bazi_semantic', 'hour_partial_official_noble', 'bazi_semantic', 'source_ref', 'rel_smth_04_022', 'yin_month_establish_prosperous', 'rel_smth_04_023', 'partial_official_merge_control_strategy', 'rel_smth_04_024', 'long_life_wealth_pattern_condition', 'evi_smth_04_022', 'yin_month_establish_prosperous', 'rule_yin_establish', 'evi_smth_04_023', 'partial_official_merge_control_strategy', 'rule_partial_control', 'evi_smth_04_024', 'hour_partial_official_noble', 'rule_hour_noble', 'map_smth_04_015', 'map_smth_04_016']
    
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
        l1_anchor="smth_v1.0.0_寅月_建禄旺相与偏官结构_001_L1",
    )
    version: str = "1.0.0"
