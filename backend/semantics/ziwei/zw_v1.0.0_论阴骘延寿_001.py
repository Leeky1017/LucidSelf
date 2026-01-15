"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755801
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
    semantic_id="zw_v1.0.0_论阴骘延寿_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论阴骘延寿(SemanticEntry):
    """
    - 分字分词释义：

  - **阴骘**：暗中行善、利物济人而不求名利的德行积累，被视为修正寿元的无形资产。
  - **延寿**：在本命寿元基础上，因阴德积累而延长实际寿命。
  - **倒限**...
    """
    
    original_text: str = """- 分字分词释义：

  - **阴骘**：暗中行善、利物济人而不求名利的德行积累，被视为修正寿元的无形资产。
  - **延寿**：在本命寿元基础上，因阴德积累而延长实际寿命。
  - **倒限**：结构凶险、易出大祸的大小限运，本应遇灾却因阴骘而缓解。
  - **利物济人**：以利他为目的，减轻众生苦难的具体行为，是阴骘的典型表现。
  - **作善降祥**：传统因果观，行善者天道必降福祥，虽遇凶限亦不致害。
  - **宋郊渡蚁**：典故，宋郊铺草渡蚁子，因此善行而延寿免祸。
  - **诸葛亮火烧藤甲军**：反例，杀戮过重而「减寿一纪」，说明恶行亦会折损寿元。
  - **减寿一纪**：一纪为十二年，重度伤人恶行可导致寿命缩短约一个生育周期。

- 原文（断句）：

  论阴骘延寿：

  阴骘延寿生百福，虽然倒限不遭伤。假如有人大小二限及太岁到凶陷地，有延过寿去不死者，还是其人曾行阴骘。平曰利物济人，反身修德，以作善降祥，虽凶不害。如宋郊编荻桥渡蚁是也。又如诸葛亮火烧藤甲军，伤人太毒，减寿一纪，当以此参详。

- 规范化释义（primary_lang_explained）：

  本条从命理与因果的结合角度，讨论「阴骘」——暗中行善、利物济人——如何对寿命与灾祸强度产生修正。前半句指出：阴骘可以「延寿生百福」，甚至在本应遭逢重凶的倒限之中，仍能不致致命；若有人本命与大小二限及太岁都走到凶陷之地，却仍能延寿过关、不至死亡，往往是因为其人过去曾有真实的阴德积累，而非命局本身无凶。也就是说，阴骘被视为一种可以「抵消部分限运之凶」的无形资产。

  后半段则通过两个典故，对「行善」与「伤人」的后果做对比：一方面，以宋郊在荻桥铺草渡蚁为例，强调利物济人为阴骘典型；另一方面，以诸葛亮火烧藤甲军、杀戮过重而「减寿一纪」为反例，说明严重伤人、伤众生的行为会折损寿命。综合来看，本条的要旨并非用道德直接否定命理，而是提出：在命局与限运的框架内，人的长期行为会对寿命与灾祸程度起到加减作用，行阴骘者可以在大凶限中减轻或化解灾祸，行恶者则可能在本可无事的运程中自减寿算。

- 完整对等诠释（secondary_lang_full）：

  This passage links fate with moral action through the idea of hidden virtue.
  It claims that quietly doing good—benefiting others without seeking credit—can
  "extend life and give rise to a hundred blessings", so that even when major
  and minor periods and the annual ruler fall in harsh places, a person may
  survive what should have been a deadly configuration. Conversely, heavy
  harming of others is said to "cut off" years from one's allotted span, as in
  the story of Zhuge Liang burning the rattan-armoured troops and thereby
  shortening his life by a 12‑year cycle.

  Read in a contemporary way, the rule suggests that charts and periods describe
  a range of risk rather than a fixed script. Within that range, long-term
  patterns of kindness or harm shape how severe events become and how long a
  person actually lives. Hidden virtue is treated as an invisible buffer that
  can soften hard periods; repeated cruelty erodes that buffer and lets the same
  periods bite more deeply. For practitioners, the teaching is less about
  scoring moral points and more about reminding clients that ethical choices are
  part of how destiny unfolds in practice.

- 核心要点：

  1. 阴骘指暗中行善、利物济人，可在命局与限运框架内对寿命与灾祸程度起修正作用。
  2. 大凶限中延寿不死者，多因其人曾行阴骘，积累了无形的德行资产。
  3. 宋郊渡蚁是阴骘典型，诸葛亮火烧藤甲军是恶行减寿的反例。
  4. 本条并非用道德否定命理，而是强调行为对命运实际展开的加减修正。
  5. 实务中可将阴骘视为风险缓冲，引导当事人在高危运中积善行德以减轻冲击。"""
    normalized_text_zh: str = """"""
    subject: str = "论阴骘延寿"
    factor_refs: list = ['concept_yinzhi', 'result_yanshou', 'state_daoxian', 'result_jianshou', 'action_liwujiren', 'source_ref', 'rel_yinzhi_001', 'concept_yinzhi', 'rel_yinzhi_002', 'action_shangren', 'rel_yinzhi_003', 'concept_yinzhi', 'evi_yinzhi_001', 'concept_yinzhi', 'rule_yinzhi_yanshou', 'evi_yinzhi_002', 'result_jianshou', 'rule_yinzhi_jianshou', 'concept_karma', 'concept_lifespan_mod']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_论阴骘延寿_001_L1",
    )
    version: str = "1.0.0"
