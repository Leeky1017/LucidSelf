"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288831
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
    semantic_id="smth_v1.0.0_巳月_长生财与偏官争锋_001",
    book_id="sanming",
    engine_id="bazi"
)
class 巳月长生财与偏官争锋(SemanticEntry):
    """
    - **原文（source_text）**：
  巳月。甲乙日得巳月为财，贵，不生于巳午日，难为财，亦名长生财，贵，戊土露则财星愈光，丙火露则伤神益壮，喜身旺财露，忌坐丑露比，运身旺喜财，身弱喜旺。丙...
    """
    
    original_text: str = """- **原文（source_text）**：
  巳月。甲乙日得巳月为财，贵，不生于巳午日，难为财，亦名长生财，贵，戊土露则财星愈光，丙火露则伤神益壮，喜身旺财露，忌坐丑露比，运身旺喜财，身弱喜旺。丙日建禄，丁旺相，丙丁生巳月无可取用为福，只是身旺年长，颇宜时带偏官及日时之贵格；又丙丁巳月亦是长生财，贵，要财露，如不露，只是伤官背禄，月令是长生财，喜行财运，带偏官，喜合运，忌动财、正官。戊己日为卯，亦是建禄，何以别之，只年月时露丙火为印；丙不露，更有壬癸字者，只是建禄印绶贵，喜露官星及行官印之地，忌伤官印，如建禄，时宜带偏官，喜自身强旺，运宜合偏官，忌正官。庚日为偏官，贵，印与同官，喜身旺合制，有合莫制；忌身弱无合，正官运亦同论，忌再见偏官，全无制，多夭，独庚申日则不然，何者？巳中有土，能生金，金既长生，又自坐禄，何夭之有。辛日为正官，辛为天德，喜官再透及财露，官爱多合及三合六合之地，忌坐七煞伤官，运身强喜财官，身弱喜旺，忌七煞伤官。壬日为偏官，喜身强，偏官有合莫制，忌身弱露官，运喜身旺合偏官，忌身弱旺官全无制伏，多夭。癸日为正官，喜露财官、三合六合、身旺，忌七煞伤官，官爱多合，运喜身旺及官印之地，弱则喜印，忌煞。

- 分字分词释义：
  - **长生财（巳月）**：巳为水之长生之地，甲乙得之为财，丙丁亦得长生财，须财露且身旺。
  - **建禄（巳月）**：丙建禄、丁旺相，戊己得卯（在巳月论建禄）皆指身根牢固、行动力强。
  - **偏官有合莫制**：偏官若有合，宜顺其化合，不再施以强力制伏；无合时才需适度制约。
  - **伤官背禄**：本可成长生财之局，却因财不露而多伤官，致才气耗泄、难承禄位。
  - **天德**：辛日得官格时如天德星，主品行与名望兼具。

- 规范化释义（primary_lang_explained）：
  巳月火土之气渐盛，其中藏庚戊丙，既是火的生地，也是水的长生之所。甲乙日得巳月为财，若非生于巳午日，则难算真财；尤其当戊土露出时，财星更有根基，丙火再透则使精神与表现力增强，但也增大消耗。丙丁日于巳一方面为建禄旺相，一方面又为长生财之地：若财星显露，则既有财利又有身根；若财不露，则成为伤官背禄。戊己日于巳月借卯意论建禄，重在身强配印：丙火为印透出时，能够将勤勉与稳重结合，行官印之运尤佳。庚辛在巳月多从官格角度看：庚为偏官，需身强且有印与之同宫或合制；辛为正官，喜官再透与财同来，并在三合六合之地成就「天德」之象。壬癸在此皆以偏官、正官论：身强时偏官、正官皆可成贵，身弱时则官星反成压力，行运不宜再重官杀。


- **完整对等诠释（secondary_lang_full）**：
  In Si month fire and earth begin to dominate while metal and water are reborn inside the branch. For Jia and Yi, Si is both a wealth place and a "long‑life wealth" position for water: when they are not themselves born on Si or Wu days and when Wu‑earth shows as a rooted base, wealth can be steady and lasting; when Bing fire further appears it boosts vitality and visibility but also increases consumption. Bing and Ding in Si have a double status, standing both on build‑salary/ prosperous roots and in the territory of long‑life wealth. If real wealth stars are revealed the configuration gives both money and a strong base; if wealth is missing, the same pattern reverts to Hurting‑Officer‑against‑salary, with talent and effort out front but material returns thin.
  Wu and Ji in Si borrow the idea of build‑salary from Mao and add the requirement of visible seal: with Bing fire as clear seal, their industry and responsibility can be recognised and supported, especially when walking official‑and‑seal fortunes. For Geng and Xin, Si is mainly judged as an official month: Geng plays the role of partial‑official and needs a strong day stem plus seal in the same palace or in good combination to turn sharpness into authority; Xin acts as proper‑official and likes to see officials show again together with wealth, set within triple or sextile formations that symbolise legitimate, well‑integrated rank, which the text calls a "Heavenly Virtue" quality. Ren and Gui here are also read as partial and proper officials. When the person is strong and there is sound merging and control, both can signal real power; when the body is weak and officials pile up without control, the same configuration becomes a burden, so later fortunes heavy in officials and killings are treated with caution rather than optimism.

- 核心要点：
  - 巳月对甲乙、丙丁主要提供「长生财 + 身根」的组合，对戊己、庚辛、壬癸则更多体现为官煞结构的成败。
  - 偏官与正官在巳月中纠缠，关键在身强弱与是否有印、合制：身旺有印、有合则可化煞为权，身弱无制则为凶。
  - 长生财格局需兼顾财星透出与不被伤官过度掩盖，否则只能算才华而非财禄。

- 应用推演（操作顺序）：
  1) 判盘时识别巳月，对甲乙、丙丁标记为「长生财/建禄月」，对戊己标记为「建禄印月」，对庚辛、壬癸标记为「官煞月」。
  2) 检查财星是否透出，以及伤官是否压过财星，对丙丁特别记录「长生财 vs 伤官背禄」的分叉路径。
  3) 对庚、壬等偏官格，评估合制结构与身旺程度，将「偏官有合/无合、有制/无制」各自编码成特征，用于判断是权柄还是压力。
  4) 在行运模拟中，将巳火相关运标记为「官煞易动期」，对身弱者提高风险权重，对身强且有印者则视为突破与上升的窗口。

- 反例与边界：
  - 不宜认为「巳月皆为长生财、必有大财」，忽略财不透或被伤官覆盖等情形。
  - 不可将一切偏官视为危险信号，巳月中许多偏官格反为权柄来源，关键在是否有印与合制。
  - 工程中若只用「巳月=火旺」简单标签，会错判诸多以水之长生、官煞结构为核心的命局。
  - 反向误区是过度依赖官杀，忽视身弱状态下官杀过重带来的健康与关系风险。

- 小例（示意）：
  - 某丙日命局生于巳月，财星透干、戊土有根，行运再入财乡，系统可标记为「长生财明透」：适合在高投入但可持续回报的领域累积资产。
  - 另一命局庚日生于巳月，偏官重而无印、无合，行运又多官杀，系统则标记为「官煞过重」：需在职业选择上警惕高压权责岗位，避免过早透支。"""
    normalized_text_zh: str = """"""
    subject: str = "巳月：长生财与偏官争锋"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'si_month_long_life_wealth_official', 'bazi_semantic', 'long_life_wealth_pattern', 'bazi_semantic', 'partial_official_merge_control', 'bazi_semantic', 'harm_official_back_salary_risk', 'bazi_semantic', 'heavenly_virtue_noble', 'bazi_semantic', 'establish_salary_seal_config', 'bazi_semantic', 'source_ref', 'rel_smth_04_031', 'long_life_wealth_pattern', 'rel_smth_04_032', 'partial_official_merge_control', 'rel_smth_04_033', 'establish_salary_seal_config', 'evi_smth_04_031', 'long_life_wealth_pattern', 'rule_long_life_si', 'evi_smth_04_032', 'heavenly_virtue_noble', 'rule_heavenly_virtue', 'evi_smth_04_033', 'partial_official_merge_control', 'rule_partial_merge', 'map_smth_04_021', 'map_smth_04_022']
    
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
        l1_anchor="smth_v1.0.0_巳月_长生财与偏官争锋_001_L1",
    )
    version: str = "1.0.0"
