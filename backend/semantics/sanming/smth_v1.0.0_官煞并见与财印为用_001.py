"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458354
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
    semantic_id="smth_v1.0.0_官煞并见与财印为用_001",
    book_id="sanming",
    engine_id="bazi"
)
class 官煞并见与财印为用(SemanticEntry):
    """
    - **原文（source_text）**：
  人命官煞俱有，谓之混杂，只取财印为用。柱元有财，运行财发，大要身强，胜任其财方可；身弱官煞混，多夭贫。身旺有制亦好，无制，成印局化煞亦可。
  
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  人命官煞俱有，谓之混杂，只取财印为用。柱元有财，运行财发，大要身强，胜任其财方可；身弱官煞混，多夭贫。身旺有制亦好，无制，成印局化煞亦可。
  
  诗曰：官煞交加用命推，个中消息要详之。得时身旺分轻重，贵财分明辨别知。如壬辰、丙午、丙辰、癸巳，身煞俱旺，官从戊化，德秀兼备。丁亥、壬子、丁未、癸卯，丁从壬化，亥卯未会局，水木清奇。甲午、己巳、辛酉、甲午，辛日巳丙为官，二午丁为煞，喜旺专禄，巳酉会局胜煞，虽无制伏，初行西方，身益旺，故贵。观三命，不可以混杂为贱论。

- 分字分词释义：
  - **官煞混杂**：命局中同时见正官与七煞（偏官），且彼此交错并存。
  - **只取财印为用**：用神侧重财星与印绶，以财生官、印化煞为主轴，不再直接以官煞为用。
  - **身强胜任其财**：日主须足够有力，方能承受财星所生之官煞与责任，否则财多反为累。
  - **成印局化煞**：印绶成局能化解七煞为生身之力，使煞不再直接攻身。
  - **官煞交加**：正官与七煞俱见、交错分布于四柱。

- **规范化释义（primary_lang_explained）**：
  本节讨论的是命局中同时存在正官与七煞的情形，古人称之为"官煞混杂"。传统上有人认为官煞并见必为不清不贵，但本节指出：官煞混杂并非一定为贱，关键在于如何取用。一般而言，当官煞并见时，应以财星和印绶为主用：财可以生官、牵煞，印可以化煞生身；若日主身强，则能承受财官之重，反可发贵；若身弱而官煞混杂，则多有贫夭之患。
  
  文中列举三造：壬辰、丙午、丙辰、癸巳一命，身煞俱旺而官从戊土化，德秀兼备；丁亥、壬子、丁未、癸卯则以壬水为主，亥卯未会局，水木清奇；辛日甲午命则以巳中丙为官、午中丁为煞，喜旺专禄，巳酉会局胜煞，虽无明显制伏，但身旺行西方金地反得其贵。结论是：不能因为官煞混杂就一概视为低贱，仍需详审身强身弱、财印有无等具体条件。

- **完整对等诠释（secondary_lang_full）**：
  When a chart contains both proper officials and Seven Killing together it is called a mixed official–Killing structure, and the classics advise 'taking only wealth and Seal as the real handles'. If wealth is present in the pillars and fortune cycles move through wealth lands, then provided the body is strong enough to shoulder what wealth and office imply, success and rank can follow. If the body is weak while both official and Killing are tangled together, early death and poverty become common outcomes.
  For a strong body, it is good when there are clear controlling stars; even without obvious controllers, if the chart can form a solid Seal bureau that transforms the Killing to nourish the self, the mixture of officials and Killing can still be turned to use. In other words, mixed officials and Killing are not inherently base; their value depends on whether wealth and Seals are strong and the person has the capacity to carry them.


- 核心要点：
  - 官煞并见不等于必贱，关键在于**用财印调和**、身强能胜任。
  - 身旺、财印得力时，官煞混杂反可成灵动之局；身弱而官煞杂乱，则多主贫夭。
  - 印绶成局化煞，是处理官煞混杂的主要方式之一。

- 详细解说：
  正官象征有序的权力与规范，七煞象征猛烈的权力与压力；两者若同时出现，而无财印调和，一方面容易形成官煞混乱、上级多头、规章与压力并起的局面，另一方面也可能反映命主体制内外多重角色与期待。若日主身强、有足够资源与能力，则可以在这种复杂结构中游刃有余；若日主身弱，则容易在多重压力下崩溃。
  
  以例命来看，作者强调的不是官煞本身，而是"身"、"财"、"印"三者之间的平衡：壬辰、丙午、丙辰、癸巳一造中，官由戊土所化，说明官煞力量并非散乱，而是集中为可用之德；辛日甲午命中，虽煞旺，却因巳酉会局胜煞，加之行西方金运，反成贵格。这类分析反复说明一点：面对官煞混杂，应先问"身能否胜任"，再问"财印是否调和"，而不是单看官煞之多寡。

- 校勘与字词辨析：
  - 原文"官煞交加用命推"一句，"用命推"指以命局整体结构来推断吉凶，不可孤立看一二字神。
  - "观三命，不可以混杂为贱论"点明作者立场：反对简单以官煞混杂就断人品或贵贱。
  - **English**：
    - Avoids simplistic judgments of character or status based on mixed official-kill.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_064]` `[trigger: 官煞混杂]` `[factor_trigger: guansha_hunza_presence]` `[role: 主干]` 人命官煞俱有，谓之混杂，只取财印为用。 → 《三命通会》卷五#官煞混杂
  - `[ns_smth_05_065]` `[trigger: 身强胜任]` `[factor_trigger: shenqiang_shengren_score]` `[role: 主干依赖]` 大要身强，胜任其财方可；身弱官煞混，多夭贫。 → 《三命通会》卷五#官煞混杂
  - `[ns_smth_05_066]` `[trigger: 印局化煞]` `[factor_trigger: yinju_huasha_condition]` `[role: 条件分支]` 无制，成印局化煞亦可。 → 《三命通会》卷五#官煞混杂
  - `[ns_smth_05_067]` `[trigger: 不以混杂为贱]` `[factor_trigger: hunza_weijian_misjudge=false]` `[role: 总结]` 观三命，不可以混杂为贱论。 → 《三命通会》卷五#官煞混杂"""
    normalized_text_zh: str = """"""
    subject: str = "官煞并见与财印为用"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'guansha_hunza_presence', 'bazi_semantic', 'caiyin_tiaohe_config', 'bazi_semantic', 'shenqiang_shengren_score', 'bazi_semantic', 'guansha_lingdong_score', 'bazi_semantic', 'yinju_huasha_condition', 'bazi_semantic', 'hunza_weijian_misjudge', 'bazi_semantic', 'source_ref', 'rel_smth_05_049', 'guansha_hunza_presence', 'rel_smth_05_050', 'guansha_lingdong_score', 'rel_smth_05_051', 'yinju_huasha_condition', 'evi_smth_05_049', 'caiyin_tiaohe_config', 'rule_caiyin', 'evi_smth_05_050', 'shenqiang_shengren_score', 'rule_shengren', 'evi_smth_05_051', 'yinju_huasha_condition', 'rule_yinhua', 'map_smth_05_033', 'map_smth_05_034']
    
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
        l1_anchor="smth_v1.0.0_官煞并见与财印为用_001_L1",
    )
    version: str = "1.0.0"
