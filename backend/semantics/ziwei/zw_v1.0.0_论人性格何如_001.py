"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755664
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
    semantic_id="zw_v1.0.0_论人性格何如_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论人性格何如(SemanticEntry):
    """
    - 分字分词释义：

  - **身命星紧缓**：身命宫星曜是否稳固集中。
  - **禀性不常**：性情不稳定，喜怒无常。
  - **善星守命**：吉星守护命宫，主性情仁慈。
  - **凶杀守命...
    """
    
    original_text: str = """- 分字分词释义：

  - **身命星紧缓**：身命宫星曜是否稳固集中。
  - **禀性不常**：性情不稳定，喜怒无常。
  - **善星守命**：吉星守护命宫，主性情仁慈。
  - **凶杀守命**：凶星守护命宫，主性情残暴。
  - **五行生克**：金木水火土相生相克的关系。
  - **冷暖刚柔**：五行配置对性格的影响。

- 原文（断句）：

  如身命一星紧一星，缓则禀性不常，喜怒不一，善恶随风逐波。若善星守命，则赋性仁慈公直；凶杀守命，则禀性恶虐狂妄。又看金木水火土生克制化推详。

- 规范化释义（primary_lang_explained）：

  本条以身宫、命宫为性格判断的根基，指出其星曜之「紧」或「缓」，会直接影响人之性情是否稳定。若身命所依之星位置稳固、力量集中，多主禀性持重；若落点飘忽、受制太多，则易见喜怒无常、善恶摇摆，随境遇而起伏。此时需特别留意守命之星：若多为吉曜，则人多仁慈、公直、有分寸；若多为凶杀，则易偏向刚猛、乖戾，甚至残忍狂妄。

  原文最后提醒，仍须合参五行之生克制化：金木水火土之间的相生相克，会为性格增添冷暖刚柔的层次。例如木旺而火助，则性情外向而有温度；水寒而金重，则情绪偏冷、锋利；土厚而能承，则多稳重可信。性情之善恶与稳定与否，并非只由一星决定，而是身命星性与五行大局共同作用的结果。

- 完整对等诠释（secondary_lang_full）：

  This short passage explains how personality is read from the Life and Body
  palaces and from the five-element environment around them. When the stars
  that occupy Life and Body are firmly seated and supported, the native's
  temperament tends to be steady; when these positions are loose, scattered
  or heavily constrained, the nature becomes changeable, with moods and moral
  choices easily swayed by circumstance. If mainly benefic stars guard the
  Life palace, the text speaks of a kind, upright disposition; if killing
  stars dominate, it warns of cruelty, harshness and even reckless violence.

  At the same time, the five-element pattern colours this basic outline. Warm
  Wood-and-Fire arrangements can produce outgoing, generous people; cold
  Metal-and-Water emphasis may bring sharper, more detached minds; thick
  Earth can stabilise or dull the character depending on balance. The author
  therefore insists that one should not label a person "good" or "evil" on
  the basis of a single star, but must read the Life and Body stars together
  with the overall five-element structure to understand the complexity of a
  human temperament.

- 核心要点：

  1. 身宫、命宫所坐星曜的「紧/缓」与强弱，是判断性情稳不稳定的第一关键。
  2. 善星守命，多主性仁慈、公直；凶杀守命，多主性残暴、乖戾甚至狂妄。
  3. 喜怒不定、善恶随境，多与身命受制、星力散乱有关。
  4. 性格判断须合参五行生克制化，考察整体金木水火土的冷暖刚柔配置。
  5. 不可仅凭一星一象下绝对结论，须放回命盘全局理解人之复杂性情。

- 叙事素材（narrative_snippets）：

  - **星力紧缓**："身命所坐星曜紧缓强弱，是判断性情稳定的第一关键"，星力紧则性情稳。
  - **善星守命**："善星守命多主性仁慈公直"，吉星入命主性情仁善。
  - **凶杀守命**："凶杀守命多主性残暴乖戾"，杀星入命主性情刚烈。
  - **五行配置**："须合参金木水火土的冷暖刚柔配置"，五行影响性格冷暖。
  - **现代应用**：本条可作为"性格评估"的参考——先看身命星力，再看五行配置，综合判断性情。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j5_031]` `[trigger: 性情评估]` `[factor_trigger: xingqing_pinggu]` `[role: 主干]` 性情评估为根据身命星曜判断性格的方法。 → 《卷五》
  - `[ns_zwds_j5_032]` `[trigger: 星力紧缓]` `[factor_trigger: xingli_jinhuan]` `[role: 主干]` 星力紧缓为星曜力量集中或散乱的状态。 → 《卷五》"星曜紧缓强弱"
  - `[ns_zwds_j5_033]` `[trigger: 善星守命]` `[factor_trigger: shanxing_shouming]` `[role: 条件分支]` 善星守命为吉星入命主性情仁善的配置。 → 《卷五》"善星守命"
  - `[ns_zwds_j5_034]` `[trigger: 凶杀守命]` `[factor_trigger: xiongsha_shouming]` `[role: 条件分支]` 凶杀守命为杀星入命主性情刚烈的配置。 → 《卷五》"凶杀守命"
  - `[ns_zwds_j5_035]` `[trigger: 五行生克]` `[factor_trigger: wuxing_shengke]` `[role: 主干]` 五行生克为金木水火土相生相克的关系原理。 → 《卷五》"金木水火土生克制化"
  - `[ns_zwds_j5_036]` `[trigger: 冷暖刚柔]` `[factor_trigger: wuxing_lengnuangangrou]` `[role: 主干]` 冷暖刚柔为五行配置对性格影响的特性。 → 《卷五》"冷暖刚柔"
  - `[ns_zwds_j5_037]` `[trigger: 性仁慈公直]` `[factor_trigger: xingge_renci_gongzhi]` `[role: 结果]` 性仁慈公直为善星守命的性格结果。 → 《卷五》"赋性仁慈公直"
  - `[ns_zwds_j5_038]` `[trigger: 性恶虐狂妄]` `[factor_trigger: xingge_enue_kuangwang]` `[role: 结果]` 性恶虐狂妄为凶杀守命的性格结果。 → 《卷五》"禀性恶虐狂妄""""
    normalized_text_zh: str = """"""
    subject: str = "论人性格何如"
    factor_refs: list = ['state_jinghuan', 'pattern_shanxingshouming', 'pattern_xiongsha', 'state_xingqingbuchang', 'system_wuxing', 'source_ref', 'rel_xingge_001', 'state_jinghuan', 'rel_xingge_002', 'pattern_shanxingshouming', 'rel_xingge_003', 'system_wuxing', 'evi_xingge_001', 'pattern_shanxingshouming', 'rule_xingge_shan', 'evi_xingge_002', 'pattern_xiongsha', 'rule_xingge_xiong', 'concept_personality', 'concept_moral_tendency']
    
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
        l1_anchor="zw_v1.0.0_论人性格何如_001_L1",
    )
    version: str = "1.0.0"
