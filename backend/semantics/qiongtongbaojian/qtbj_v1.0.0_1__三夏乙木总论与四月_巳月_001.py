"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620055
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
    semantic_id="qtbj_v1.0.0_1__三夏乙木总论与四月_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三夏乙木总论与四月巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  三夏乙木，木性枯焦。四月专尚癸水。五六月先丙后癸，夏至前仍用癸水。
  先得丙透，支下又有丙火，名曰木秀火明。得一癸透，科甲中人。或透二丙一癸，可许采...
    """
    
    original_text: str = """- **原文（source_text）**：
  三夏乙木，木性枯焦。四月专尚癸水。五六月先丙后癸，夏至前仍用癸水。
  先得丙透，支下又有丙火，名曰木秀火明。得一癸透，科甲中人。或透二丙一癸，可许采芹。
  或一派癸水，有丁无丙，平常之人。或一癸透干，异途显宦，难由科甲。癸居子辰，异路小职。或丙藏支下，癸透年干，己出月上，虽非科甲，异路功名。又或重重癸水，或支藏癸水，由行伍出身得功名。

  四月乙木，自有丙火，耑取癸水为尊。四月乙木专用癸水，丙火酌用，虽以庚辛佐癸，须辛透为清。癸透、庚辛又透，科甲定然，独一点癸水、无金，是水无根，虽出天干，不过秀才小富，须要大运相扶。
  或土多困癸，贫贱之人。丙戊太多，支成火局，瞽目之流。
  用癸者，金妻水子。
  乙逢双女木伤残，若见辛金寿必难，不得丙丁来制伏，岂知安乐不久长。

- **分字分词释义**：
  - **木性枯焦**：木的本性枯槁焦燥 / 夏季特征 / 需水
  - **专尚癸水**：专门崇尚癸水 / 调候首选 / 救命
  - **木秀火明**：木秀丽火明亮 / 丙透有根 / 吉象
  - **采芹**：采摘芹菜 / 考中秀才 / 入学
  - **行伍出身**：从军队出身 / 武职功名 / 重癸
  - **耑取癸水为尊**：专门取癸水为至尊 / 首选用神 / 巳月
  - **水无根**：水没有根基 / 癸无金生 / 力弱
  - **瞽目之流**：瞎眼的一类 / 火炎土燥 / 凶象
  - **双女**：星次名 / 巳宫 / 乙木病地
  - **寿必难**：寿命必定难保 / 辛克乙 / 夭寿

- **规范化释义（primary_lang_explained）**：
  夏天的乙木，木性枯槁焦燥。四月（巳月）专门崇尚癸水（调候）。五月六月（午未月）先用丙火（泄秀/防寒）后用癸水（润），但夏至前仍然主要用癸水。
  如果先得到丙火透出，地支下又有丙火，叫“木秀火明”。再得到一个癸水透出（润泽），是科甲中人。如果透出两个丙火一个癸水，可以许诺中秀才（采芹）。
  如果一派癸水，有丁火而没有丙火，是平常人。如果一个癸水透干，多是异途（非科举）显达的官吏。癸水在子或辰支，是异路小职。或者丙火藏支，癸水透年干，己土透月干，虽不是科甲，也是异路功名。又或者重重癸水，或地支藏癸水，往往由行伍（军职）出身得功名。

  四月（巳月）乙木，月令自带丙火（巳中丙），专门取癸水为尊。四月乙木专用癸水，丙火斟酌使用（不宜多），虽然用庚辛金辅助癸水（发水源），但必须辛金透出才清纯。癸水透、庚辛也透（杀印相生），科甲是一定的。如果只有一点癸水、没有金，是水无根，虽然透出天干，不过是秀才小富，还需要大运相扶。
  如果土多困住癸水，是贫贱之人。如果丙火戊土太多，地支合成火局，是瞎眼（瞽目）之流（火多木焚，目疾）。
  乙木遇到双女（巳宫），木气伤残，如果再见到辛金（七杀），寿命必定难保，如果不得丙丁火来制伏辛金，哪里知道安乐的日子不会久长。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the Three Summer Months is withered and scorched. In the 4th Month (Snake), exclusively value Gui Water. In the 5th/6th Months, use Bing first then Gui; but before the Summer Solstice, still use Gui.
  If Bing is revealed first and grounded in branches, it is "Wood Elegant Fire Bright". With one Gui revealed, one belongs to the Civil Service. Two Bings and one Gui promise a Xiucai degree.
  If there is a mass of Gui Water, with Ding but no Bing, one is ordinary. One Gui revealed denotes prominence via alternative paths. Gui sitting on Zi/Chen denotes minor alternative posts. If Bing is hidden, Gui on Year stem, Ji on Month stem, it is alternative fame. Heavy Gui or hidden Gui often implies fame from military service.
  
  In the 4th Month, Yi Wood has its own Bing (in Si); exclusively take Gui Water as supreme. Use Gui exclusively; use Bing sparingly. Although Geng/Xin assist Gui, Xin revealed is pure. If Gui and Geng/Xin are revealed, Civil Service is certain. Only one Gui without Metal means rootless Water; even if revealed, it's just a Xiucai or small wealth, requiring Luck support.
  If Earth is abundant trapping Gui, one is poor and lowly. If Bing/Wu are excessive and branches form a Fire Frame, one belongs to the blind (Eye disease due to Fire burning Wood).
  "Yi meeting Double Girl (Si) means Wood is injured; if Xin Metal appears, longevity is difficult; without Bing/Ding to control it, one will not know that peace is short-lived."

- **核心要点**：
  - **首要用神**：癸水（调候/润局）。无水必死。
  - **次要用神**：辛金（发水源）。
  - **格局**：木秀火明（丙透），杀印相生（辛癸透）。
  - **凶象**：丙戊火局（盲目），乙逢双女见辛（夭寿）。

- **详细解说**：
  四月乙木，病地，且火旺泄气。
  - "双女"即巳宫（天文宫位），乙木至此气散。
  - 最怕辛金七杀攻身（克泄交加），除非有丙丁火回克辛金，或癸水化杀。
  - "瞽目之流"：五行中木主目，火土太燥木被焚，故主眼疾。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_184]` `[trigger: 三夏乙木]` `[factor_trigger: season_summer AND tiangan_yi AND tiangan_gui]` `[role: 主干]` 三夏乙木，木性枯焦，四月专尚癸水。 → 《穷通宝鉴·三夏乙木》#8.1
  - `[ns_qttbj_185]` `[trigger: 木秀火明]` `[factor_trigger: month_si AND tiangan_yi AND bing_revealed AND bing_rooted AND gui_revealed]` `[role: 主干依赖]` 先得丙透，支下又有丙火，名曰木秀火明，得一癸透，科甲中人。 → 《穷通宝鉴·三夏乙木》#8.1
  - `[ns_qttbj_186]` `[trigger: 瞽目]` `[factor_trigger: month_si AND tiangan_yi AND fire_excessive AND dizhi_fire_frame AND NOT tiangan_gui]` `[role: 例外处理]` 丙戊太多，支成火局，瞽目之流。 → 《穷通宝鉴·三夏乙木》#8.1
  - `[ns_qttbj_187]` `[trigger: 双女见辛]` `[factor_trigger: month_si AND tiangan_yi AND tiangan_xin AND NOT (tiangan_bing OR tiangan_ding)]` `[role: 总结]` 乙逢双女木伤残，若见辛金寿必难，不得丙丁来制伏，岂知安乐不久长。 → 《穷通宝鉴·三夏乙木》#8.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三夏乙木总论与四月（巳月）"
    factor_refs: list = ['plucking_celery', 'double_girl', 'blindness', 'wood_elegant_fire_bright']
    
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
        l1_anchor="qtbj_v1.0.0_1__三夏乙木总论与四月_巳月_001_L1",
    )
    version: str = "1.0.0"
