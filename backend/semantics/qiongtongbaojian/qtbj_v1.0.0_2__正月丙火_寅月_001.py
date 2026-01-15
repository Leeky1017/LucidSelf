"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596670
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
    semantic_id="qtbj_v1.0.0_2__正月丙火_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2正月丙火寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月丙火，三阳开泰，火气渐炎，取壬为尊，庚金佐之。壬庚两透，科甲定然。即壬透庚藏，亦有异途显达。
  若一庚高透，支藏一二丙火，纳粟奏名，主为人慷慨英...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月丙火，三阳开泰，火气渐炎，取壬为尊，庚金佐之。壬庚两透，科甲定然。即壬透庚藏，亦有异途显达。
  若一庚高透，支藏一二丙火，纳粟奏名，主为人慷慨英雄，有才迈众。
  或一派庚辛混杂，常人。得时月两透庚金、无辛者，定主清贵。或辛年辛时，名为贪合，酒色之徒。女命一理。
  或丙少壬多，而无戊制，名杀重身轻。斯人笑里藏刀，寻非痞棍。或见一戊制壬，反而富贵，宜见一二比肩方妙。
  或一片戊土，甲不出干，终非大器，且恐孤贫。正月之丙，忌戊晦光。或支成火局，耑取壬水为贵，无壬、癸亦姑用。若壬癸俱无，取戊以泄火气，但属平人。
  或支成火局，又作炎上而推，但不逢时耳。若不见东南岁运，反致孤贫。
  或四柱有甲木，得庚金暗制，可作秀才。

- **分字分词释义**：
  - **三阳开泰**：三个阳爻开启太平 / 寅月卦象 / 火气升
  - **纳粟奏名**：捐粮换取功名 / 捐官 / 富贵
  - **慷慨英雄**：慷慨大方的英雄 / 性格 / 庚透丙藏
  - **贪合**：贪恋合化 / 丙辛合 / 酒色
  - **杀重身轻**：七杀重日主轻 / 壬多无戊 / 凶格
  - **笑里藏刀**：笑容里藏着刀 / 阴险 / 痞棍
  - **炎上格**：火炎上升格局 / 火局 / 变格

- **规范化释义（primary_lang_explained）**：
  正月（寅月）的丙火，三阳开泰，火气逐渐炎热，取壬水为至尊（既济），庚金佐助（生水）。壬水和庚金都透出，科甲功名是一定的。即使壬水透出庚金藏支，也有异途（非科举）显达。
  如果一个庚金高透，地支藏有一两个丙火（身旺财透），可以纳粟奏名（捐官），主为人慷慨英雄，才华超越众人。
  如果一派庚辛金混杂，是常人。如果时干月干两透庚金、没有辛金混杂，定主清高富贵。如果是辛年辛时，这叫“贪合”（丙辛合），是酒色之徒。女命也是这个道理。
  如果丙火少而壬水多（杀重），且没有戊土制约，叫“杀重身轻”。这种人笑里藏刀，是寻是生非的痞棍。如果见到一个戊土制壬水（食神制杀），反而富贵，若再见一两个比肩（丙火）帮身才妙。
  如果一片戊土，甲木不透出（疏土），终究成不了大器，且恐怕孤苦贫穷。正月的丙火，忌讳戊土晦暗光芒。
  如果地支合成火局，专门取壬水为贵，没有壬水、癸水也可以勉强使用。如果壬癸全无，取戊土泄火气，但只是平人。
  如果地支合成火局，又可以当作“炎上格”推断，只是不逢时（生在寅月而非巳午月）。如果大运不走东南（木火），反而导致孤贫。
  如果四柱有甲木（偏印），得到庚金（财）暗制，可以做个秀才。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 1st Month (Tiger Month): Three Yangs open peacefully; Fire energy becomes gradually hot. Take Ren as supreme, with Geng Metal assisting. If both Ren and Geng are revealed, Civil Service is certain. If Ren is revealed and Geng hidden, one is prominent via alternative paths.
  If one Geng is highly revealed and branches hide one or two Bing Fires, one gains a title via donation; the person is generous and heroic, with talent surpassing the crowd.
  If a mass of Geng/Xin is mixed, one is ordinary. If Geng is revealed on both Month and Hour without Xin, it implies pure nobility. If Xin Year and Xin Hour appear, it is called "Greedy for Combination" (Bing combines with Xin), denoting a person of lust and wine. Same for female lives.
  If Bing is scarce and Ren abundant without Wu to control, it is "Heavy Killing Weak Body". Such a person hides a dagger in a smile, a troublemaking rogue. If one Wu is seen to control Ren, it becomes wealth and nobility; seeing one or two Parallel Shoulders is even better.
  If there is a mass of Wu Earth and Jia does not appear, one will never be a great vessel, and likely lonely and poor. Bing in the 1st Month dreads Wu obscuring its light.
  If branches form a Fire frame, exclusively take Ren Water as noble; without Ren, Gui is acceptable. If neither Ren nor Gui exists, take Wu to leak Fire, but one is ordinary.
  If branches form a Fire frame, it can be inferred as "Inflamed Upward Pattern" (Yan Shang), but it is not in the right season. If Luck does not go Southeast, it leads to loneliness and poverty.
  If the four pillars have Jia Wood, and Geng Metal controls it secretly, one can be a Xiucai.

- **核心要点**：
  - **首要用神**：壬水（既济）。
  - **配合**：庚金（生水）。
  - **忌讳**：戊土（晦光），辛金（贪合）。
  - **杀重身轻**：壬多无制，痞棍。
  - **炎上格**：寅月火局，需运助。

- **详细解说**：
  寅月丙火长生，火气已生。
  - “三阳开泰”：寅月卦象为泰，三阳生，故丙火向旺。
  - 此时最喜“庚壬”，即财滋杀。庚金劈寅中甲木引火，又生壬水映照太阳，格局最大。
  - 丙辛合在寅月，若不化水（寅月难化），则丙火贪合忘映，迷恋酒色（辛为柔金/珠玉/私情）。
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_225]` `[trigger: 寅月丙火]` `[factor_trigger: month_yin AND tiangan_bing AND tiangan_ren AND tiangan_geng]` `[role: 主干]` 正月丙火，三阳开泰，火气渐炎，取壬为尊，庚金佐之。壬庚两透，科甲定然。 → 《穷通宝鉴·三春丙火》#12.2
  - `[ns_qttbj_226]` `[trigger: 丙辛贪合]` `[factor_trigger: month_yin AND tiangan_bing AND tiangan_xin AND bing_xin_greedy_combine]` `[role: 例外处理]` 辛年辛时，名为贪合，酒色之徒。 → 《穷通宝鉴·三春丙火》#12.2
  - `[ns_qttbj_227]` `[trigger: 杀重身轻]` `[factor_trigger: month_yin AND tiangan_bing AND ren_excessive AND NOT tiangan_wu AND killing_heavy_body_weak]` `[role: 例外处理]` 丙少壬多，而无戊制，名杀重身轻，斯人笑里藏刀，寻非痞棍。 → 《穷通宝鉴·三春丙火》#12.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 正月丙火（寅月）"
    factor_refs: list = ['three_yangs', 'greedy_combine', 'obscuring_light']
    
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
        l1_anchor="qtbj_v1.0.0_2__正月丙火_寅月_001_L1",
    )
    version: str = "1.0.0"
