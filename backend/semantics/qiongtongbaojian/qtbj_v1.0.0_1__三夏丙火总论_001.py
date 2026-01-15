"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596705
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
    semantic_id="qtbj_v1.0.0_1__三夏丙火总论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三夏丙火总论(SemanticEntry):
    """
    - **原文（source_text）**：
  三夏丙火，阳威性烈，专用壬水。若亥宫壬水无力，回克泄气故也，仍用申宫长生之水，方云富贵。
  四月耑用壬水，金为佐。五月亦耑用壬。四五月壬透者富贵。丁...
    """
    
    original_text: str = """- **原文（source_text）**：
  三夏丙火，阳威性烈，专用壬水。若亥宫壬水无力，回克泄气故也，仍用申宫长生之水，方云富贵。
  四月耑用壬水，金为佐。五月亦耑用壬。四五月壬透者富贵。丁多、兼看癸水。六月用壬，但借庚金为佐。
  阳刃合杀，威权万里。丁火羊刃太旺，正谓羊刃倒戈，无头之鬼。丙火用壬，生旺坐实方好，忌壬水太多，名杀重身轻。

- **分字分词释义**：
  - **阳威性烈**：阳气威猛性情刚烈 / 夏丙特征 / 极旺
  - **申宫长生之水**：申宫的长生之水 / 壬水根源 / 贵
  - **阳刃合杀**：羊刃合七杀 / 威权格 / 贵
  - **羊刃倒戈**：羊刃倒转攻击 / 刃旺无制 / 凶死
  - **无头之鬼**：斠首的鬼魂 / 凶死 / 极凶
  - **生旺坐实**：生旺且根基稳固 / 壬水要求 / 吉

- **规范化释义（primary_lang_explained）**：
  夏季三个月的丙火，阳气威猛性情刚烈，专用壬水（调候/既济）。如果亥宫的壬水无力（因为亥中甲木泄水气且被巳冲？），容易被回克泄气，仍然要用申宫长生之水（申中壬水有庚生），才说得上富贵。
  四月（巳月）专用壬水，以金辅助（发水源）。五月（午月）也专用壬水。四月五月壬水透出的人富贵。丁火多的时候，兼看癸水（制劫）。六月（未月）用壬水，但需借庚金辅助（土重金泄土生水）。
  阳刃合杀（丙日主合辛金？不，通常指羊刃驾杀或刃合杀），威权万里。如果丁火羊刃太旺（午月），正是所谓的“羊刃倒戈”，可能做无头之鬼（凶死）。丙火用壬水，壬水要生旺坐实才好，忌讳壬水太多，那叫“杀重身轻”。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the Three Summer Months has majestic Yang and intense nature; exclusively use Ren Water. If Ren Water in Hai Palace is weak (due to leakage/clash), rely on Water in the Birth Place of Shen Palace to claim wealth and nobility.
  In the 4th Month, exclusively use Ren, with Metal assisting. In the 5th Month, also exclusively use Ren. If Ren is revealed in the 4th/5th Months, it implies wealth and nobility. If Ding is abundant, also consider Gui Water. In the 6th Month, use Ren, but borrow Geng Metal to assist.
  "Yang Edge Combining with Killing" implies authority extending ten thousand miles. If Ding Fire Yang Edge is too prosperous, it is called "Yang Edge Turning its Weapon", implying a headless ghost. When Bing Fire uses Ren, Ren should be prosperous and grounded; dread excessive Ren, which is called "Heavy Killing Weak Body".

- **核心要点**：
  - **首要用神**：壬水（调候/制刃）。夏火无水必夭。
  - **水源**：喜申金（壬长生），优于亥水（易受损）。
  - **配合**：四五月用壬，六月用壬庚。
  - **凶象**：羊刃倒戈（丁旺无制），杀重身轻（壬多无制）。

- **详细解说**：
  - “阳刃合杀”：通常指日主合杀（如甲日合己土？不，是日主合官，杀合刃）。这里可能是指“羊刃驾杀”的威权。
  - “羊刃倒戈”：指羊刃（劫财）太旺，反噬日主，主极凶。
  - “申宫长生之水”：申金是水的长生，且庚金能生水，源源不断，故贵。

- **分字分词释义**：
  - **阳威性烈**：阳气威猛性情刚烈 / 夏丙特征 / 极旺
  - **申宫长生之水**：申宫的长生之水 / 壬水根源 / 贵
  - **阳刃合杀**：羊刃合七杀 / 威权格 / 贵
  - **羊刃倒戈**：羊刃倒转攻击 / 刃旺无制 / 凶死
  - **无头之鬼**：斠首的鬼魂 / 凶死 / 极凶
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_234]` `[trigger: 三夏丙火]` `[factor_trigger: season_summer AND tiangan_bing AND summer_bing_likes_ren]` `[role: 主干]` 三夏丙火，阳威性烈，专用壬水。若亥宫壬水无力，仍用申宫长生之水，方云富贵。 → 《穷通宝鉴·三夏丙火》#13.1
  - `[ns_qttbj_235]` `[trigger: 羊刃倒戈]` `[factor_trigger: season_summer AND tiangan_bing AND ding_excessive AND yang_edge_turning_weapon]` `[role: 例外处理]` 丁火羊刃太旺，正谓羊刃倒戈，无头之鬼。 → 《穷通宝鉴·三夏丙火》#13.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三夏丙火总论"
    factor_refs: list = ['yang_blade_backstab', 'headless_ghost', 'authority_miles']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__三夏丙火总论_001_L1",
    )
    version: str = "1.0.0"
