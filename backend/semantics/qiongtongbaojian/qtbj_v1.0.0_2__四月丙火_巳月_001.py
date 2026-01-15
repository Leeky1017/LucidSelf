"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596716
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
    semantic_id="qtbj_v1.0.0_2__四月丙火_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2四月丙火巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月丙火，建禄于巳，火势炎炎，宜专用壬水，解炎威之力，成既济之功。如无壬水，孤阳失辅，难透清光。得庚发水源，方为有根之水。壬庚两透，不见戊土，号曰湖水...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月丙火，建禄于巳，火势炎炎，宜专用壬水，解炎威之力，成既济之功。如无壬水，孤阳失辅，难透清光。得庚发水源，方为有根之水。壬庚两透，不见戊土，号曰湖水汪洋，广映太阳，光辉显着，文明之象，人格合此，不但科甲峥嵘，必有恩谥封荣，若不验，必暗损阴德。
  或无壬水，癸亦姑用，见庚透癸，不富必贵，但心性乖僻，巧谋善辩。或壬癸俱无，愚顽之辈。火炎无制，僧道之流，不然，须防夭折。
  或一派庚金，不见比劫，有富无贵。
  或丙午日干，四柱多壬，不见戊制，名曰阴刑杀重，光棍之流。或支水局，加之重重壬透，一无制伏，盗贼之命，如见己土，下贱鄙夫。

- **分字分词释义**：
  - **建禄于巳**：在巳建立禄位 / 巳月丙火 / 身旺
  - **炎威**：火焰威势 / 火旺之象 / 需制
  - **既济之功**：水火相济的功效 / 壬丙配合 / 格局
  - **孤阳失辅**：孤单阳气失去辅助 / 无水 / 凶象
  - **有根之水**：有源头的水 / 庚生壬 / 吉象
  - **湖水汪洋**：湖泊水势汪洋 / 壬庚两透 / 格局名
  - **广映太阳**：广泛映照太阳 / 丙水相映 / 吉象
  - **恩谥封荣**：皇恩封赠荣耀 / 大贵 / 吉象
  - **阴刑杀重**：阴柔刑罚七杀过重 / 丙午壬多 / 凶象
  - **光棍之流**：无妻孤独之人 / 杀重无制 / 凶象

- **规范化释义（primary_lang_explained）**：
  四月（巳月）的丙火，建禄在巳，火势炎炎，适宜专用壬水，解除炎热威猛的力量，成就水火既济的功业。如果没有壬水，孤阳失去辅助，难以透出清澈的光芒。得到庚金发源（生水），才是“有根之水”。
  壬水和庚金两透，不见戊土（克水），号称“湖水汪洋，广映太阳”，光辉显著，是文明的象，入格合此，不但科甲峥嵘，必有皇恩封赠荣耀。如果不灵验，必定是暗中损了阴德。
  或者没有壬水，癸水也姑且使用。见到庚金透出癸水，不富必贵，但心性乖僻，巧谋善辩（癸水阴柔）。如果壬癸全无，是愚顽之辈。火炎无制，是僧道之流，否则，须防夭折。
  如果一派庚金（财多），不见比劫，是有富无贵。
  如果是丙午日干（阳刃），四柱壬水多，不见戊土制约，叫“阴刑杀重”，是光棍之流。如果地支合成水局，加上重重壬水透出，全无制伏，是盗贼的命。如果见到己土（混杂），是下贱鄙夫。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 4th Month (Snake Month) is at Jianlu (Formation Prosperity); the fire is blazing. Exclusively use Ren Water to relieve the intense heat and achieve "Completion". Without Ren, Solitary Yang loses support and cannot shine clearly. Obtaining Geng to generate the Water source makes it "Rooted Water".
  If Ren and Geng are both revealed and Wu Earth is not seen, it is called "Vast Lake Reflecting the Sun", a symbol of civilization and brilliance. If the pattern fits, not only is Civil Service prominent, but imperial honors are certain. If not verified, one must have secretly damaged their hidden virtues.
  Or if there is no Ren, use Gui tentatively. If Geng and Gui are revealed, one is noble if not rich, but the temperament is eccentric, skillful in plotting and debating. If neither Ren nor Gui exists, one is stupid and stubborn. Uncontrolled blazing Fire leads to being a monk/Taoist, or one must guard against premature death.
  If there is a mass of Geng Metal and no Parallel/Rob Wealth, there is wealth but no nobility.
  If Bing-Wu Day Master sees abundant Ren in pillars without Wu to control, it is "Yin Punishment Heavy Killing", a rogue. If branches form a Water frame and Ren is heavily revealed without control, it is a thief's life; if Ji Earth is seen, a lowly vulgar man.

- **核心要点**：
  - **格局**：日照江湖（湖水汪洋，广映太阳）。
  - **最佳配置**：壬庚两透。
  - **次佳配置**：癸庚两透（心性乖僻）。
  - **凶象**：无水（僧道/夭折），水多无制（盗贼/光棍）。

- **详细解说**：
  巳月建禄，丙火最强。
  - “湖水汪洋，广映太阳”是丙火最高格局之一。需壬水有力（通根申亥或有庚生）。
  - 戊土是大忌，因为是“堤坝”挡住了光映，且克壬水。
  - “阴刑杀重”：指七杀太重攻身，日主虽旺（丙午），但杀更多，且无食神制杀，只能硬抗，故为光棍/盗贼。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_236]` `[trigger: 巳月丙火]` `[factor_trigger: month_si AND tiangan_bing AND tiangan_ren AND sun_shining_on_river]` `[role: 主干]` 四月丙火，建禄于巳，火势炎炎，宜专用壬水，解炎威之力，成既济之功。 → 《穷通宝鉴·三夏丙火》#13.2
  - `[ns_qttbj_237]` `[trigger: 湖水汪洋]` `[factor_trigger: month_si AND tiangan_bing AND tiangan_ren AND tiangan_geng AND NOT tiangan_wu AND vast_lake]` `[role: 条件分支]` 壬庚两透，不见戊土，号曰湖水汪洋，广映太阳，光辉显着，文明之象。 → 《穷通宝鉴·三夏丙火》#13.2
  - `[ns_qttbj_238]` `[trigger: 孤阳失辅]` `[factor_trigger: month_si AND tiangan_bing AND NOT tiangan_ren AND solitary_yang]` `[role: 例外处理]` 如无壬水，孤阳失辅，难透清光。 → 《穷通宝鉴·三夏丙火》#13.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 四月丙火（巳月）"
    factor_refs: list = ['vast_lake', 'solitary_yang', 'yin_punishment_killing']
    
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
        l1_anchor="qtbj_v1.0.0_2__四月丙火_巳月_001_L1",
    )
    version: str = "1.0.0"
