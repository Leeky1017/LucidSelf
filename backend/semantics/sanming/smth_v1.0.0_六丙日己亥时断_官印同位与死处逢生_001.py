"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157560
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
    semantic_id="smth_v1.0.0_六丙日己亥时断_官印同位与死处逢生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日己亥时断官印同位与死处逢生(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日己亥时断。

  六丙日生时己亥，官印同居死处逢；最喜身生寅午戌，平生福禄与君同。丙日己亥时，身衰官旺，伤官背禄，丙以癸为官，甲为印，亥上甲长生，癸禄...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日己亥时断。

  六丙日生时己亥，官印同居死处逢；最喜身生寅午戌，平生福禄与君同。丙日己亥时，身衰官旺，伤官背禄，丙以癸为官，甲为印，亥上甲长生，癸禄旺，己土伤官，丙死亥上，名死中逢生。柱无官煞，通木火身旺月者贵；不通，平常衣禄。

  丙子日己亥时，两神清澈，早成晚败。秋，行东运，贵。夏，生旺运，贵。

  丙寅日己亥时，寅午戌月身旺，复行寅午戌运，大贵。卯亥年月，贵显。巳酉丑，文学；申子辰，武职。

  丙辰日己亥时，生戌月，柱中无刑冲，大贵。无戌，行南运，风宪。

  丙午日己亥时，自刑克害。春，身旺，贵。夏，平常。秋凶，冬吉。

  丙申日己亥时，柱无官煞冲刑，行旺运，大贵。

  丙戌日己亥时，寅午戌月，干支无水，大贵。子月，行南运，风宪。

  丙日己亥时安排，身中衰绝莫徘徊；运行寅午火生旺，富贵荣华甲第开。丙日己亥时逢，生身死处相逢。若然身旺运扶持，福禄绑身无限。

- 分字分词释义：

  - **官印同位**：癸水正官与甲木正印同在亥上有气，官印双清。
  - **死处逢生**：丙火在亥为死地，但亥中甲木印绶可生扶日主。
  - **伤官背禄**：己土伤官克制癸水正官，破坏官禄。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，己亥时」：

  - 丙火在亥为死地，但亥中甲木印绶长生、癸水正官得禄，形成「死处逢生」的结构；
  - 己土伤官虽在，但若柱无官煞、通木火身旺月，则印绶可用，主贵；
  - 不通月气，则只是平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Ji-Hai Hour":

  - Bing Fire at Hai is at death position, but Hai contains Jia Wood Direct Seal at long life and Gui Water Direct Official with fortune—forming "life at death's door."
  - Though Ji Earth Hurting Official is present, if the chart lacks official-killing and connects with Wood-Fire strong-body month, seal becomes usable indicating nobility.
  - Without monthly connection, outcomes remain ordinary livelihood.

- 核心要点：

  - 本格以「死处逢生」为核心，印绶是关键。
  - 官印同位是优势，但伤官背禄是风险。
  - 需身旺月气来发挥印绶生身的作用。

- 详细解说：

  1. **死处逢生的用法**  
     - 丙火在亥为死地，本不佳；但亥中甲木印绶长生；  
     - 印绶可生扶日主，形成「死中有生」的结构。

  2. **官印同位的优势**  
     - 癸水正官在亥得禄，甲木正印在亥长生；  
     - 官印双清，若能配合身旺，可成就大贵。

  3. **伤官背禄的风险**  
     - 己土伤官克制癸水正官；  
     - 需要柱无官煞、或官星有救，方能化解。

- 校勘与字词辨析：

  - 「两神清澈」形容官印双清，格局纯净。
  - 「甲第开」指科举登第，跻身显贵。
  - **English**：
    - Passing imperial exam; joining the elite.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_141]` `[trigger: 官印同居]` `[factor_trigger: guanyin_tongju AND sichu_feng]` `[role: 主干]` 六丙日生时己亥，官印同居死处逢。 → 《三命通会》卷八#六丙日己亥时
  - `[ns_smth_08_142]` `[trigger: 身生寅午戌]` `[factor_trigger: shensheng_yinwuxu AND fulu_tongjun]` `[role: 主干依赖]` 最喜身生寅午戌，平生福禄与君同。 → 《三命通会》卷八#六丙日己亥时
  - `[ns_smth_08_143]` `[trigger: 死中逢生]` `[factor_trigger: sizhong_fengsheng AND tong_muhuo]` `[role: 条件分支]` 柱无官煞，通木火身旺月者贵；不通，平常衣禄。 → 《三命通会》卷八#六丙日己亥时
  - `[ns_smth_08_144]` `[trigger: 两神清澈]` `[factor_trigger: liangshen_qingche AND zaocheng_wanbai]` `[role: 总结]` 两神清澈，早成晚败。 → 《三命通会》卷八#六丙日己亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日己亥时断：官印同位与死处逢生"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_182', 'bazi_semantic', 'bazi_relation_factor_82', 'bazi_semantic', 'bazi_state_shangguan_5', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_wood_fire', 'bazi_semantic', 'source_ref', 'rel_smth_08_106', 'sichu_fengsheng', 'rel_smth_08_107', 'guanyin_tongwei', 'rel_smth_08_108', 'tongmuhuo_yue', 'evi_smth_08_106', 'sichu_fengsheng', 'rule_fengsheng', 'evi_smth_08_107', 'guanyin_tongwei', 'rule_tongwei', 'evi_smth_08_108', 'shangguan_beilu', 'rule_beilu2', 'map_smth_08_071', 'map_smth_08_072']
    
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
        l1_anchor="smth_v1.0.0_六丙日己亥时断_官印同位与死处逢生_001_L1",
    )
    version: str = "1.0.0"
