"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597076
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
    semantic_id="qtbj_v1.0.0_2__二月己土_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2二月己土卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月己土，阳气渐升，虽禾稼未成，万物出土，田园未展，先取甲木疏之，忌合。次取癸水润之。
  甲癸出干，定主科甲，加以一丙出透，势压百僚。一见壬水，微末...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月己土，阳气渐升，虽禾稼未成，万物出土，田园未展，先取甲木疏之，忌合。次取癸水润之。
  甲癸出干，定主科甲，加以一丙出透，势压百僚。一见壬水，微末官职。
  或见庚制甲，壬水出干，比劫重重，此必俗子。丙透犹有小富，丙藏衣禄无亏。
  或支成木局，庚透富贵，若柱多乙木，乙又屈庚，庚必输情于乙，不能扫邪于正，此必狡诈之徒，运入东南，恐有不测。当用丁泄之。有丁者、小人而已，不致无良。
  无比印、从杀者贵。
  若柱中无甲丙癸者，皆下格。

- **分字分词释义**：
  - **阳气渐升**：阳气逐渐上升 / 卯月特点 / 春暖
  - **田园未展**：田园尚未舒展 / 土实需疏 / 用甲
  - **势压百僚**：气势压倒百官 / 甲癸丙配合 / 极贵
  - **微末官职**：微小末等官职 / 见壬水 / 次凶
  - **俗子**：庸俗之人 / 庚壬比劫 / 凶象
  - **屈庚**：屈服庚金 / 乙庚合 / 凶象
  - **扫邪于正**：扫除邪气归于正 / 庚制乙 / 吉象
  - **狡诈之徒**：狡猾奸诈之人 / 乙多庚合 / 凶象
  - **从杀者贵**：从七杀格为贵 / 无比印 / 变格

- **规范化释义（primary_lang_explained）**：
  二月（卯月）的己土，阳气逐渐上升，虽然禾稼还未成熟，但万物已经出土，田园尚未舒展（土实），先取甲木疏通己土（正官疏土），忌讳甲己合（合则不疏）。其次取癸水滋润（财）。
  甲木癸水出干，定主科甲，加上一个丙火出透（印），气势压倒百僚（极贵）。一见壬水（大水），微末官职。
  如果见到庚金制甲（伤官见官），壬水出干（化伤），比劫重重（分财），这必定是俗人。丙火透出还有小富，丙火藏支衣禄无亏。
  如果地支合成木局（杀旺），庚金透出（制杀）主富贵。如果柱中多乙木（七杀），乙木又屈服庚金（乙庚合），庚金必定输送情意给乙木，不能扫除邪气（杀）归于正气，这必定是狡诈之徒。大运进入东南（木火），恐怕有不测之灾。应当用丁火泄乙木之气。有丁火的人，只是小人而已，不致于丧尽天良。
  如果没有比肩印绶，从杀格（从木）为贵。
  如果柱中无甲木、丙火、癸水，都是下格。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth in the 2nd Month (Rabbit Month): Yang Qi rises; though crops aren't ready, everything sprouts; fields are not yet spread out. First take Jia to dredge (avoid combining); then take Gui to moisten.
  If Jia and Gui reveal, Civil Service is certain. Adding one Bing revealed implies power suppressing all officials. Seeing Ren Water implies minor office.
  If Geng controls Jia, Ren reveals, and Parallels are heavy, this is a vulgar person. If Bing reveals, slight wealth; if Bing hidden, sufficient food/clothing.
  If branches form a Wood Frame, Geng revealed implies wealth/nobility. If many Yi Woods appear, and Yi bends Geng (combines), Geng conveys affection to Yi, failing to sweep Evil for Righteousness; this is a treacherous person. Luck entering SE (Wood/Fire) implies danger. Should use Ding to leak. With Ding, merely a petty person, not devoid of conscience.
  Without Parallels/Seals, "Follow Killing" is noble.
  If the pillar lacks Jia/Bing/Gui, all are Lower Grade.

- **核心要点**：
  - **首要用神**：甲木（疏土）。卯月土实，需疏。忌合。
  - **配合**：癸（润）、丙（暖）。
  - **忌庚**：庚金合乙，或制甲（正官被伤），则俗。
  - **从杀**：无印比，从杀贵。

- **详细解说**：
  - 卯月七杀（乙木）当令，但己土喜甲（官）疏，不喜乙（杀）克。
  - “忌合”：甲己合土，失疏通之意，故喜甲透隔位不合。
  - “势压百僚”：财官印全，格局极大。
  - “输情于乙”：乙庚合，庚金贪合忘克，不能制杀，反助纣为虐（助杀势？不，是被杀绊住），故主狡诈。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_571]` `[trigger: 卯月己土甲癸为先]` `[factor_trigger: month_mao AND tiangan_ji AND tiangan_jia AND tiangan_gui AND likes_jia_dredge]` `[role: 主干]` 二月己土，阳气渐升，田园未展，先取甲木疏之，次取癸水润之。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_572]` `[trigger: 甲癸丙透势压百僚]` `[factor_trigger: month_mao AND tiangan_ji AND tiangan_jia AND tiangan_gui AND tiangan_bing AND suppress_all]` `[role: 条件分支]` 甲癸出干，加以一丙出透，势压百僚。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_573]` `[trigger: 见壬微末官职]` `[factor_trigger: month_mao AND tiangan_ji AND tiangan_ren AND minor_office]` `[role: 例外处理]` 一见壬水，微末官职。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_574]` `[trigger: 庚制甲壬出比劫重重俗子]` `[factor_trigger: month_mao AND tiangan_ji AND tiangan_geng AND tiangan_ren AND parallels_multiple AND vulgar_person]` `[role: 例外处理]` 见庚制甲，壬水出干，比劫重重，此必俗子。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_575]` `[trigger: 丙透小富丙藏衣禄无亏]` `[factor_trigger: month_mao AND tiangan_ji AND tiangan_bing AND (bing_revealed OR bing_in_branch) AND small_wealth]` `[role: 条件分支]` 丙透犹有小富，丙藏衣禄无亏。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_576]` `[trigger: 木局庚透富贵]` `[factor_trigger: month_mao AND tiangan_ji AND dizhi_wood_frame AND tiangan_geng AND wealth_noble]` `[role: 条件分支]` 或支成木局，庚透富贵。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_577]` `[trigger: 乙多庚屈狡诈之徒]` `[factor_trigger: month_mao AND tiangan_ji AND yi_multiple AND yi_geng_greedy_combine AND treacherous_petty]` `[role: 例外处理]` 若柱多乙木，乙又屈庚，庚必输情于乙，不能扫邪于正，此必狡诈之徒。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_578]` `[trigger: 丁泄乙小人不致无良]` `[factor_trigger: month_mao AND tiangan_ji AND yi_multiple AND tiangan_ding AND petty_not_vicious]` `[role: 条件分支]` 当用丁泄之，有丁者小人而已，不致无良。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_579]` `[trigger: 无比印从杀者贵]` `[factor_trigger: month_mao AND tiangan_ji AND NOT parallels_present AND NOT seal_present AND follow_killing_pattern]` `[role: 条件分支]` 无比印，从杀者贵。 → 《穷通宝鉴·三春己土》#25.2
  - `[ns_qttbj_580]` `[trigger: 无甲丙癸下格]` `[factor_trigger: month_mao AND tiangan_ji AND NOT tiangan_jia AND NOT tiangan_bing AND NOT tiangan_gui AND low_grade_pattern]` `[role: 例外处理]` 若柱中无甲丙癸者，皆下格。 → 《穷通宝鉴·三春己土》#25.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 二月己土（卯月）"
    factor_refs: list = ['suppress_all', 'convey_to_yi']
    
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
        l1_anchor="qtbj_v1.0.0_2__二月己土_卯月_001_L1",
    )
    version: str = "1.0.0"
