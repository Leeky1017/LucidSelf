"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597033
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
    semantic_id="qtbj_v1.0.0_2__八月戊土_酉月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2八月戊土酉月(SemanticEntry):
    """
    八月戊土，金泄身寒，赖丙照暖，喜水滋润，先丙后癸，不必木疏。
  丙癸两透，科甲中人。丙透癸藏，可许入泮。癸透丙藏，纳资得官。若丙藏又无癸，即多不透，此皆常人。丙癸全无，奔流之客。
  或四柱皆辛，无...
    """
    
    original_text: str = """八月戊土，金泄身寒，赖丙照暖，喜水滋润，先丙后癸，不必木疏。
  丙癸两透，科甲中人。丙透癸藏，可许入泮。癸透丙藏，纳资得官。若丙藏又无癸，即多不透，此皆常人。丙癸全无，奔流之客。
  或四柱皆辛，无丙丁，此名伤官格，为人清秀，即不能拾芥，亦可武庠。一见癸水，富而且贵。
  或支成水局，壬癸出干，此名才多身弱，愚懦无能。若天干有比劫，分散才神，颇言衣食。
  用神妻子仛前，秋土生金极弱，须丙火丁火出干方妙。

- **分字分词释义**：
  - **金泄身寒**：金气泄身导致寒冷 / 酉月特点 / 需暖
  - **丙照暖**：丙火照耀温暖 / 调候 / 用神
  - **入泮**：进入府学 / 秀才 / 功名
  - **纳资得官**：捐官得官职 / 癸透丙藏 / 异路
  - **奔流之客**：奔波劳苦之人 / 丙癸全无 / 凶象
  - **拾芥**：如拾芥菜般容易 / 取功名 / 吉象
  - **武庠**：武学生 / 武举 / 异路
  - **才多身弱**：财多身弱 / 水局壬癸透 / 凶象

- **规范化释义（primary_lang_explained）**：
  八月（酉月）的戊土，金（伤官）泄身导致寒冷，依赖丙火照暖，喜欢水滋润（金旺燥），先用丙火，后用癸水，不必用木疏通（金旺木死）。
  丙火癸水两透，科甲中人。丙火透出癸水藏支，可以许诺入泮（秀才）。癸水透出丙火藏支，捐官（纳资）得官。如果丙火藏支又没有癸水，或者多而不透，这些都是常人。丙癸全无，奔流的客人。
  如果四柱都是辛金（伤官），没有丙丁火，这叫“伤官格”（伤官伤尽？不，金水伤官喜见官，土金伤官去官？土金伤官宜佩印），为人清秀，即使不能像拾芥一样容易取得功名，也可以进武庠（武举）。一见癸水（伤官生财），富而且贵。
  如果地支合成水局，壬水癸水透出（财多），用戊土（比劫）止流，有比肩透出反主富（身财两停）。
  如果地支合成水局，壬水癸水透出，这叫“财多身弱”，愚蠢懦弱无能。如果天干有比肩劫财，分散财神，还可以说有衣食。
  用神和妻子看法同前（土妻金子？不，用丙则木妻火子）。秋土生金极弱，必须丙火丁火出干才妙。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 8th Month (Rooster Month): Metal leaks the body making it cold; rely on Bing to warm, like Water to moisten. Prioritize Bing, then Gui; Wood dredging is unnecessary.
  If Bing and Gui are both revealed, one is in Civil Service. With Bing revealed and Gui hidden, one enters the Academy. With Gui revealed and Bing hidden, one gains office via donation. If Bing is hidden and no Gui, or many hidden but none revealed, all are ordinary. Without Bing/Gui, a wanderer.
  If four pillars are all Xin, without Bing/Ding, it is "Hurting Officer Pattern"; the person is clear and elegant. Even if success is not easy like picking up mustard, one can enter Military School. Seeing Gui (generating Wealth) makes one rich and noble.
  If branches form a Water Frame and Ren/Gui reveal, it is "Abundant Wealth Weak Body", stupid and incompetent. If Parallels/Rob Wealth reveal to disperse Wealth, one has food/clothing.
  Autumn Earth generating Metal is extremely weak; Bing/Ding revealing is wondrous.

- **核心要点**：
  - **金泄身寒**：酉月伤官泄气，土虚。
  - **首要用神**：丙火（印）。制伤生身。
  - **配合**：癸水（财）。土金伤官佩印，或伤官生财。
  - **忌讳**：财多身弱（水多）。

- **详细解说**：
  - 酉月戊土死地（土长生在寅，死在酉）。
  - 伤官泄气重，故最喜佩印（丙丁）。
  - “不必木疏”：因金旺木死，且土已虚，不需木疏。
  - “拾芥”：比喻极容易的事（拾起地上的草芥）。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_530]` `[trigger: 酉月戊土用神次序]` `[factor_trigger: month_you AND tiangan_wu AND tiangan_bing AND tiangan_gui AND NOT need_wood_dredge]` `[role: 主干]` 八月戊土，金泄身寒，赖丙照暖，喜水滋润，先丙后癸，不必木疏。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_531]` `[trigger: 丙癸两透科甲中人]` `[factor_trigger: month_you AND tiangan_wu AND tiangan_bing AND tiangan_gui AND kejia_scholar]` `[role: 条件分支]` 丙癸两透，科甲中人。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_532]` `[trigger: 丙透癸藏入泮]` `[factor_trigger: month_you AND tiangan_wu AND bing_revealed AND gui_in_branch AND entry_academy]` `[role: 条件分支]` 丙透癸藏，可许入泮。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_533]` `[trigger: 癸透丙藏纳资得官]` `[factor_trigger: month_you AND tiangan_wu AND gui_revealed AND bing_in_branch AND donated_office]` `[role: 条件分支]` 癸透丙藏，纳资得官。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_534]` `[trigger: 丙藏无癸常人]` `[factor_trigger: month_you AND tiangan_wu AND bing_in_branch AND NOT tiangan_gui AND ordinary_status]` `[role: 条件分支]` 若丙藏又无癸，即多不透，此皆常人。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_535]` `[trigger: 丙癸全无奔流之客]` `[factor_trigger: month_you AND tiangan_wu AND NOT tiangan_bing AND NOT tiangan_gui AND wandering_guest]` `[role: 例外处理]` 丙癸全无，奔流之客。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_536]` `[trigger: 四柱皆辛伤官格武庠]` `[factor_trigger: month_you AND tiangan_wu AND four_pillars_xin AND NOT tiangan_bing AND NOT tiangan_ding AND hurting_officer_pattern AND clear_elegant]` `[role: 条件分支]` 或四柱皆辛，无丙丁，此名伤官格，为人清秀，即不能拾芥，亦可武庠。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_537]` `[trigger: 伤官格见癸富贵]` `[factor_trigger: month_you AND tiangan_wu AND four_pillars_xin AND tiangan_gui AND hurting_officer_generates_wealth]` `[role: 条件分支]` 一见癸水，富而且贵。 → 《穷通宝鉴·三秋戊土》#23.2
  - `[ns_qttbj_538]` `[trigger: 水局财多身弱与比劫分财]` `[factor_trigger: month_you AND tiangan_wu AND dizhi_water_frame AND ren_gui_revealed AND NOT parallels_then_weak_body OR (parallels_present AND wealth_split_for_food)]` `[role: 例外处理]` 或支成水局，壬癸出干，此名才多身弱，愚懦无能；若天干有比劫，分散才神，颇言衣食。 → 《穷通宝鉴·三秋戊土》#23.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 八月戊土（酉月）"
    factor_refs: list = ['picking_mustard', 'military_school', 'hurting_officer_pattern', 'clear_elegant']
    
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
        l1_anchor="qtbj_v1.0.0_2__八月戊土_酉月_001_L1",
    )
    version: str = "1.0.0"
