"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458240
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
    semantic_id="smth_v1.0.0_官印禄库聚合之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 官印禄库聚合之贵(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：官中见禄库逢财，金玉自天来。如甲乙逢乙丑，丙丁逢庚午，戊己逢壬辰，庚辛见乙未，壬癸逢丙戌是也。一命丁丑、辛亥、癸酉、壬戌，癸用丙为财，戌为财库，...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：官中见禄库逢财，金玉自天来。如甲乙逢乙丑，丙丁逢庚午，戊己逢壬辰，庚辛见乙未，壬癸逢丙戌是也。一命丁丑、辛亥、癸酉、壬戌，癸用丙为财，戌为财库，用戊为官，戌中戊土正旺，财库生助，酉为癸印，丑为印库，财官印俱逢库旺，无冲破，为贵。

- 分字分词释义：
  - **官中见禄库逢财**：在官星所在之支或相关宫位上，同时出现禄位、库地与财星，形成官、禄、财三者聚合之势。
  - **禄库**：既是禄之所藏，又是财、印等五行之库地，如戌为火土之库、辰为水木之库等。
  - **甲乙逢乙丑 / 丙丁逢庚午 / 戊己逢壬辰 / 庚辛见乙未 / 壬癸逢丙戌**：分别举出不同日干在特定地支上同时得官、禄、库与财的典型组合，用以说明格局成就的条件。
  - **财官印俱逢库旺**：财星、官星、印绶三者都在库地得旺气，有根有守，福力持久。

- **规范化释义（primary_lang_explained）**：
  本节讲的是"官印禄库"的聚合格局。所谓"官中见禄库逢财"，就是在官星所在的宫位或其相联系的宫位中，同时有禄位、库地与财星出现，好比官职在身，又有俸禄与财富根基，金玉自天而来。文中列出甲乙逢乙丑、丙丁逢庚午、戊己逢壬辰、庚辛见乙未、壬癸逢丙戌等组合，皆是官、禄、库、财并见的典型。
  
  所举一命丁丑、辛亥、癸酉、壬戌为例：癸水以丙火为财，戌为火库，又以戊土为官，而戌中戊土正旺，是为财库生官；酉金为癸之印，丑为印库，于是财、官、印俱在库地得旺，且不遭冲破，自然形成稳固而厚重的贵格。

- **完整对等诠释（secondary_lang_full）**：
  The saying "when within the official one sees salary, storage and meets wealth, gold and jade fall from Heaven" describes the "official–Seal–salary storage" pattern. It refers to situations in which, in the branch that holds the official star or in closely linked positions, the salary place, storage earth and wealth stars appear together, so that office, pay and material resources converge. The text lists combinations such as Jia or Yi meeting Yi-Chou, Bing or Ding meeting Geng-Wu, Wu or Ji meeting Ren-Chen, Geng or Xin seeing Yi-Wei, and Ren or Gui meeting Bing-Xu as typical layouts where official, salary, storage and wealth gather.
  In the example chart with Ding-Chou, Xin-Hai, Gui-You and Ren-Xu, Gui water takes Bing fire as wealth and Xu as the wealth storage, and uses Wu earth as official; within Xu, Wu earth is at full strength, so the wealth storage actively generates the official. You metal serves as Seal for Gui, and Chou is the storage for that Seal. Thus wealth, official and Seal all prosper together in storage places and are not broken by clashes, forming a solid and weighty noble pattern.

- 核心要点：
  - 官印禄库格的关键，在于**官、财、印三者同得库地之旺**，有根有守，福力绵长。
  - 官中见禄库逢财，多主金玉自天来，即官职、财富与声望同时俱足，而非虚浮之贵。
  - 忌库地受冲破，或财官印其一失势，则格局难以圆满；若三者皆遭刑冲，则福力不固，反有大起大落之虞。

  - 详细解说：
  从五行藏干的角度看，"库"不仅是某五行气之所聚，还是多个相关五行的交汇点。例如戌为火土之库，既藏火气，又有戊土旺气；辰为水木之库，既藏乙木又含癸水。因此，当官星、财星、印绶三者同时在库地得根，便形成了多重资源在同一处积累与相互滋养的局面，这就是"财官印俱逢库旺"的实质。
  
  此类格局与单纯的财库或官禄不同，它重在三者之间的配合和平衡：财可生官，印可生身并缓和官克日主的压力，而库地则为三者提供稳定的根基，使其不至于一时盛、一时衰。若再配合流年与大运开库、合库得当，则往往在特定阶段出现显著的飞跃式发展；反之，若遭冲库、破库，便容易表现为巨大的波动甚至破格。

- 校勘与字词辨析：
  - **"金玉自天来"**：比喻富贵、名誉如从天而降，非人力小计可得，强调此格有厚重的先天禀赋与机会。
  - 各种"逢某干支"的组合，实际可视作官、财、印三者在地支库地中同得其所的示意列表，具体命局仍需结合月令与全局强弱灵活判断，不宜机械套用。
  - **English**：
    - Flexible judgment based on body strength; not mechanically applied.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_024]` `[trigger: 官印禄库]` `[factor_trigger: guanyin_luku_presence]` `[role: 主干]` 官中见禄库逢财，金玉自天来。 → 《三命通会》卷五#官印禄库
  - `[ns_smth_05_025]` `[trigger: 库旺三者]` `[factor_trigger: cai_guan_yin_ku_wang AND no_chong_po]` `[role: 主干依赖]` 财官印俱逢库旺，无冲破，为贵。 → 《三命通会》卷五#官印禄库
  - `[ns_smth_05_026]` `[trigger: 多重积累]` `[factor_trigger: ku_di_zi_yang AND san_zhe_pingheng]` `[role: 条件分支]` 多重资源在同一处积累与相互滋养，形成稳固而厚重的贵格。 → 《三命通会》卷五#官印禄库
  - `[ns_smth_05_027]` `[trigger: 非虚浮贵]` `[factor_trigger: fu_li_mian_chang]` `[role: 总结]` 官职、财富与声望同时俱足，而非虚浮之贵。 → 《三命通会》卷五#官印禄库"""
    normalized_text_zh: str = """"""
    subject: str = "官印禄库聚合之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'guanyin_luku_ge_presence', 'bazi_semantic', 'kudi_juhe_config', 'bazi_semantic', 'sanzhe_pingheng_score', 'bazi_semantic', 'genshou_wengu_score', 'bazi_semantic', 'kaiku_heku_timing', 'bazi_semantic', 'kudi_chongpo_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_019', 'guanyin_luku_ge_presence', 'rel_smth_05_020', 'genshou_wengu_score', 'rel_smth_05_021', 'kaiku_heku_timing', 'evi_smth_05_019', 'kudi_juhe_config', 'rule_kujuhe', 'evi_smth_05_020', 'genshou_wengu_score', 'rule_kuwang', 'evi_smth_05_021', 'sanzhe_pingheng_score', 'rule_sanku', 'map_smth_05_013', 'map_smth_05_014']
    
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
        l1_anchor="smth_v1.0.0_官印禄库聚合之贵_001_L1",
    )
    version: str = "1.0.0"
