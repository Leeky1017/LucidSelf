"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436505
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
    semantic_id="smth_v1.0.0_旺子伤夫格与代际偏重_001",
    book_id="sanming",
    engine_id="bazi"
)
class 旺子伤夫格与代际偏重(SemanticEntry):
    """
    - 原文（source_text）：

  旺子伤夫。

  有旺子伤夫者何？此法专以月时推之。谓克我者为官为夫，有气得时，则夫发福；若支干失位，不得月气，柱中又逢冲克，时上又无旺气，而己生之子，引至...
    """
    
    original_text: str = """- 原文（source_text）：

  旺子伤夫。

  有旺子伤夫者何？此法专以月时推之。谓克我者为官为夫，有气得时，则夫发福；若支干失位，不得月气，柱中又逢冲克，时上又无旺气，而己生之子，引至时上，逢长生、临官、帝旺之地，又无刑克，是旺子伤夫也。如一命：己卯、甲戌、乙卯、戊寅。乙用庚为夫，九月庚金无气；乙用丙为子，丙火长生于寅，与戌会局，皆属火。月令既无金气，时引绝地，又被火克，是伤其夫星，旺其子息，故曰旺子伤夫，余仿此推。

- 分字分词释义：

  - **旺子伤夫**：子星极旺而夫星衰败，福力偏向子女一端，而对伴侣关系较不利。
  - **专以月时推之**：重点观察月令与时柱对夫星、子星的生克与取舍。
  - **克我者为官为夫**：女命以克身之官煞为夫星，其旺衰定夫之兴衰。
  - **己生之子，引至时上**：由日主所生之食伤引到时支，看其是否得旺地。

- **规范化释义（primary_lang_explained）**：

  本节结构与“旺夫克子”相对：

  - 若夫星在月、时上失位无气，又逢冲克，则夫端较难发福；
  - 若子星被引至时上，落于长生、临官、帝旺之地，且不受刑克，则子女一端反而兴旺；
  - 原例中庚金夫星在九月无气，又受火克；丙火子星在寅、戌火局之中大旺，故以“旺子伤夫”名之。

- **完整对等诠释（secondary_lang_full）**：

  In this pattern the centre of gravity shifts toward the child line rather than the spouse. On the axis formed by month and time, the spouse star loses seasonal support and often suffers further clashes or control, so that it struggles to unfold. The child star, born from the Day Master, is instead led to positions of Changsheng, Lin'guan or Diwang at the time pillar and remains free from heavy affliction. Structurally, this means that the long‑term storyline, especially in the later part of life, is more likely to be organised around raising and supporting children than around building up the partner’s path.

  In the example, Geng Metal as spouse star is out of season in the ninth lunar month and further weakened by Fire, while Bing Fire as child star thrives in the Yin–Xu Fire combination. This does not automatically signify misfortune for the partner, but it describes a pattern in which the native’s attention, sacrifice and hope flow more readily toward the next generation. For a modern reader, "Child‑Favoured" can thus be read as a call to balance: to honour the genuine desire to invest in children while also safeguarding the health, dignity and growth of the marital relationship.

- 核心要点：

  - 月令、时柱是判断夫子两端兴衰的关键参照。
  - 夫星失位、子星得旺，形成代际福力偏重于子女的格局。
  - “伤夫”主要指对伴侣端资源与发展较为不利，并非简单灾祸标签。

- 详细解说：

  1. **月令对夫星的影响**  
     - 月令为一局之权柄，夫星得令则易发福；  
     - 若如原例庚金在戌月无气，又再遇火局克制，则夫道较难展开。

  2. **时柱对子星的承接**  
     - 子星引至时支而得长生、临官、帝旺，多主子女有发展空间；  
     - 在现实中，常表现为子女在学业、事业或声誉上的相对突出。

  3. **家庭结构中的偏重**  
     - 这类命局往往令命主把大量心力投向子女，而伴侣关系可能相对被忽视或承压；  
     - 若能有意识地经营伴侣间的沟通与支持，可缓和“旺子伤夫”的结构压力。

- 校勘与字词辨析：

  - 原文“伤夫”与前节“伤子”同属结构性用语，本稿统一解释为在资源与发展上的偏不利，而非必然的身体伤害。
  - 例命叙述中的“绝地”等术语，在本稿仅作为五行旺衰位置使用，不作神秘化扩张。
  - **English**：
    - Used in specific position; no mystical expansion.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_045]` `[trigger: 旺子伤夫定义]` `[factor_trigger: wangzi_shangfu_ge]` `[role: 主干]` 旺子伤夫。 → 《三命通会》卷七#旺子伤夫
  - `[ns_smth_07_046]` `[trigger: 月时推之]` `[factor_trigger: zhuan_yi_yueshi_tui]` `[role: 主干依赖]` 此法专以月时推之。谓克我者为官为夫，有气得时，则夫发福。 → 《三命通会》卷七#旺子伤夫
  - `[ns_smth_07_047]` `[trigger: 子旺夫衰]` `[factor_trigger: zixing_wangdi AND fuxing_shiwei]` `[role: 条件分支]` 若支干失位，不得月气...而己生之子，引至时上，逢长生、临官、帝旺之地。 → 《三命通会》卷七#旺子伤夫
  - `[ns_smth_07_048]` `[trigger: 伤夫旺子]` `[factor_trigger: shang_fuxing_wang_zixi]` `[role: 总结]` 是伤其夫星，旺其子息，故曰旺子伤夫。 → 《三命通会》卷七#旺子伤夫"""
    normalized_text_zh: str = """"""
    subject: str = "旺子伤夫格与代际偏重"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_zi_3', 'bazi_semantic', 'bazi_structure_month_command_5', 'bazi_semantic', 'bazi_structure_hour_pillar_zi', 'bazi_semantic', 'bazi_state_relation_degree', 'bazi_semantic', 'source_ref', 'rel_smth_07_031', 'fuzi_fuli_zouxiang', 'rel_smth_07_032', 'shizhu_chengjie', 'rel_smth_07_033', 'banlu_chenya', 'evi_smth_07_031', 'fuzi_fuli_zouxiang', 'rule_wangzishangfu', 'evi_smth_07_032', 'shizhu_chengjie', 'rule_ziwang', 'evi_smth_07_033', 'banlu_chenya', 'rule_shangfu', 'map_smth_07_021', 'map_smth_07_022']
    
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
        l1_anchor="smth_v1.0.0_旺子伤夫格与代际偏重_001_L1",
    )
    version: str = "1.0.0"
