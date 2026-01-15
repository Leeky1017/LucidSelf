"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492402
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
    semantic_id="zpzq_v1.0.0_阳刃格的特性与用法层次_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 阳刃格的特性与用法层次(SemanticEntry):
    """
    - **原文（source_text）**：
  四十三、论阳刃。
  阳刃者，劫我正财之神，乃正财之七煞也。禄前一位，惟五阳有之，故为旭刃。不曰劫而曰刃，劫之甚也。刃宜伏制，官煞皆宜，财印相随，尤为...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十三、论阳刃。
  阳刃者，劫我正财之神，乃正财之七煞也。禄前一位，惟五阳有之，故为旭刃。不曰劫而曰刃，劫之甚也。刃宜伏制，官煞皆宜，财印相随，尤为贵显。夫正官而财印相随美矣，七煞得之，夫乃甚乎？岂知他格以煞能伤身，故喜制伏，忌财印；阳刃用之，则赖以制刃，不怕伤身，故反喜财印，忌制伏也。

  阳刃用官，透刃不虑；阳刃露煞，透刃无成。盖官能制刃，透而不为害；刃能合煞，则有何功？如丙生午月，透壬制刃，而又露丁，丁与壬合，则七煞有贪合忘克之意，如何制刃？故无功也。

  然同是官煞制刃，而格亦有高低，如官煞露而根深，其贵也大；官煞藏而不露，或露而根浅，其贵也小。若己酉、丙子、壬寅、丙午，官透有力，旺财生之，丞相命也。又辛酉、甲午、丙申、壬辰，透煞根浅，财印助之，亦丞相命也。

  然亦有官煞制刃带伤食而贵者，何也？或是印护，或是煞太重而裁损之，官煞轻而取清之，如穆同知命，甲午、癸酉、庚寅、戊寅，癸水伤寅午之官，而戊以合之，所谓印护也，如贾平章命，甲寅、庚午、戊申、甲寅，煞两透而根太重，食以制之，所谓裁损也。如丙戌、丁酉、庚申、壬午，官煞竞出，而壬合丁官，煞纯而不杂。况阳刃之格，利于留煞，所谓取清也。

  其于丙生午月，内藏己土，可以克水，尤宜带财佩印，若戊生午月，干透丙火，支会火乙，则化刃为印，或官或煞，透则去刃存印其格愈清。倘或财煞并透露，则犯去印存煞之忌，不作生煞制煞之例，富贵两空矣。

  更若阳刃用财，格所不喜，然财根深而用伤食，以转刃生财，虽不比建禄月劫，可以取贵，亦可就富。不然，则刃与财相搏，不成局矣。

- 原注（原文注解）：
  　本章专论“阳刃格”的本质与多种用法层次。阳刃本为“劫我正财之神”，却又是极具爆发力与权势意味的一格。
  - 首句说明：
    - 阳刃是“禄前一位”，仅五阳干有之；
    - 为何“不曰劫而曰刃”？——因其锋利如刀，为“劫之甚者”；
    - 在一般格局中，七煞喜制伏、忌财印；
    - 唯阳刃格“反道而行”：以财印制刃，反成贵显。

  文中依次展开数类阳刃格：
  1) **阳刃用官格**：
     - 官为制刃之神：
       - 官透而有根 → 能节制阳刃之过，形成“官制刃”的稳定权力结构；
       - 若刃合煞而官不见，则“有刃无制”，空有杀伐之气而难成格.
  2) **官煞制刃的高低差异**：
     - 官煞露而根深 → 贵格高；
     - 官煞藏而浅 → 贵而不大；
     - 财印助官煞，可成“财印相随”的高等阳刃格，用以解释文中丞相诸命.
  3) **官煞制刃带伤食者**：
     - 通过印护、伤食裁损，使官煞不过度：
       - “印护” → 以印合去伤害官星的因素；
       - “裁损” → 伤食适度制煞，使煞不致过重；
     - 阳刃格反“利于留煞”，取其清而有力.
  4) **化刃为印、刃化为官煞者**：
     - 如丙生午月，内藏己土 → 可克水，配合财印而清；
     - 戊生午月，透丙会火 → 化刃为印、为官煞：
       - 去刃存印，格局愈清，体现“化险为依”的思路.
  5) **阳刃用财格**：
     - 理论上不喜：财为正财，被劫而危；
     - 唯有“财根深而用伤食，以转刃生财”，方可就贵就富；
     - 若仅刃与财相搏，则无局可言.

- 分字分词释义：
  - 阳刃：五阳日干在本气旺地所见之劫财，锋利如刀，故名阳刃；
  - 正财之七煞：阳刃对正财而言，如同七煞对日主，主争夺、压迫；
  - 伏制：使其潜伏而受制，仍保留力量但不至失控；
  - 取清：去混杂之神，保留单一、可用之力量；
  - 化刃为印：通过会局、透干，使刃之气转为印绶之用；
  - 刃生财：以阳刃所代表之资源、权力、锋芒去生发财富的过程.

- **规范化释义（primary_lang_explained）**：
  可将阳刃理解为“极端激进、极端集中的执行力”：
  - 其本质是对财与身的强烈侵夺；
  - 若制伏得宜，则成为“破局而不翻车”的利器；
  - 若失控，则是“自伤、自毁”的象征.

  本章重点在于：
- **完整对等诠释（secondary_lang_full）**：  
  Yang Blade symbolises extremely concentrated, aggressively mobilised life‑force. By nature it leans toward seizing, competing and overrunning boundaries: it can grab resources and partners, overwhelm ordinary limits and push both the self and others to the edge. When discipline and structure are weak, this shows as "fighting to the point of self‑harm": quarrels at home, broken partnerships, reckless spending of strength and money, and a tendency to burn bridges while charging ahead.

  Yet the same Blade, when properly checked and given a channel, becomes the sharp spearhead of a system: the person who dares to break deadlocks, rush into danger and carry heavy responsibilities others cannot bear. In that case, Officer and Killing provide rules and fields of action, Printing gives identity and obligations, and Wealth and Food offer concrete tasks and goals. The core question of this chapter is precisely how to combine Officer, Killing, Printing and Wealth so that Yang Blade has somewhere to exert force without tipping into self‑destruction.

  - 如何利用官、煞、印、财的组合，令阳刃有处发力又不至失控；
  - 说明何种情形下“留煞为佳”，何种情形下必须“化刃为印”。

- 详细解说：
  - 阳刃格，本质是“极端能量如何被制度化”的问题：
    - 官、煞是规则与权力；
    - 印是身份、资历与制度；
    - 财是资源与诱因；
    - 阳刃是难以驾驭的行动力；
  - 真正高阶的阳刃格，一定是这些力量之间达到某种高张而稳定的平衡，而不是单纯“刃越多越好”。

- **核心要点**：
  - 阳刃者，劫财之重者也
  - 阳刃用官，透官则贵，官煞混杂则贱
  - 阳刃用煞，煞来制刃，身煞两停则贵
  - 阳刃用财，财来生官制刃

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_569]` `[trigger: 阳刃格的特性与用法层]` `[role: 主干]` `[factor_trigger: yangren_jiecai_zhi_zhong]` 阳刃者，劫财之重者也 → 《子平真诠》#下卷
  - `[ns_zpzy_570]` `[trigger: 阳刃格的特性与用法层]` `[role: 条件分支]` `[factor_trigger: yangren_yongguan AND touguan_zegui AND guansha_hunza_zejian]` 阳刃用官，透官则贵，官煞混杂则贱 → 《子平真诠》#下卷
  - `[ns_zpzy_571]` `[trigger: 阳刃格的特性与用法层]` `[role: 条件分支]` `[factor_trigger: yangren_yongsha AND sha_lai_zhiren AND shensha_liangting_zegui]` 阳刃用煞，煞来制刃，身煞两停则贵 → 《子平真诠》#下卷
  - `[ns_zpzy_572]` `[trigger: 阳刃格的特性与用法层]` `[role: 条件分支]` `[factor_trigger: yangren_yongcai AND cai_lai_shengguan_zhiren]` 阳刃用财，财来生官制刃 → 《子平真诠》#下卷

#### 语义因子提取（因子层）

| 因子类型 | 因子标签       | 因子ID | 因子来源     | 角色/位置  | 取值/约束                                                           | 备注                         |
|----------|----------------|--------|--------------|------------|--------------------------------------------------------------------|------------------------------|
| 结构类   | 阳刃格类型     |        | new_candidate | 分型轴     | yang_ren_yong_guan / guan_sha_zhi_ren / hua_ren_wei_yin / yang_ren_yong_cai | 概括本章主要阳刃结构       |
| 关系类   | 刃与官煞强弱比 |        | new_candidate | 制衡枢纽  | ren_zhong_guan_qiang / ren_qiang_guan_qian / ren_sha_da致_ping衡       | 判断官煞能否有效制刃       |"""
    normalized_text_zh: str = """"""
    subject: str = "阳刃格的特性与用法层次"
    factor_refs: list = ['yangren', 'fuzhi', 'guan_zhiren', 'sha_zhiren', 'caiyin_xiangsui', 'huaren_weiyin', 'quqing', 'engine_id', 'yangren', 'bazi_rule_engine', 'yangren_yongguan_ge', 'bazi_rule_engine', 'yangren_yongsha_ge', 'bazi_rule_engine', 'huaren_weiyin_ge', 'bazi_rule_engine', 'yangren_yongcai_ge', 'bazi_rule_engine', 'guansha_genshenqian', 'bazi_rule_engine', 'ren_guansha_bi', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_43_01', 'yangren', 'rel_zpzq_43_02', 'guanxing', 'rel_zpzq_43_03', 'caiyin_xiangsui', 'rel_zpzq_43_04', 'guansha_genshenqian', 'rel_zpzq_43_05', 'huaren_weiyin', 'rel_zpzq_43_06', 'yangren_yongcai_ge', 'evi_zpzq_43_01', 'yangren', 'rule_yangren_benxing', 'evi_zpzq_43_02', 'rule_yangren_chengge_yaodian', 'evi_zpzq_43_03', 'yangren_yongguan_ge', 'rule_yangren_yongguan_yongsha_qubie', 'evi_zpzq_43_04', 'guansha_genshenqian', 'rule_guansha_zhiren_gaodi', 'evi_zpzq_43_05', 'huaren_weiyin_ge', 'rule_huaren_weiyin_chengge', 'concept_aggressive_force', 'concept_power_restraint', 'concept_transform_danger']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_阳刃格的特性与用法层次_001_L1",
    )
    version: str = "1.0.0"
